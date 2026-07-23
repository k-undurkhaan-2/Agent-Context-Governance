# Architecture

## Status and scope

Agent Context Governance is in an architectural bootstrap phase. This document
defines the intended boundaries and invariants of a future implementation; it
does not describe an existing CLI, policy engine, router, Git inspector, lease
service, trusted `TaskContract` issuer, receipt generator, adapter, enforcement
system, or execution runtime.

The core architecture is agent-neutral. Core types and control-plane behavior
MUST NOT depend on Codex, another agent product, an agent SDK, or a product-
specific prompt format. Product integrations MAY be added later only as
execution adapters outside the core.

Authorization fails closed. Unless valid structured governance, all applicable
restrictions, and satisfied preconditions establish otherwise, the defaults are:

```yaml
mode: plan-only
allowWrite: false
```

An omitted, invalid, or inconclusive authorization input MUST NOT be interpreted
as permission to implement.

`mode: plan-only` implies `allowWrite: false`. The combination of
`mode: plan-only` and `allowWrite: true` is invalid and MUST be rejected.
Future governed adapter execution, including plan-only execution, requires a
valid bounded `TaskContract`.

## Architectural layers

The planned implementation is divided into the following layers.

### Core model

The innermost layer defines the semantics and invariants of governance objects,
authorization decisions, routing results, `TaskContract` records, and
`ExecutionReceipt` records. It contains no host paths, Git process integration,
storage drivers, or agent-product dependencies.

### Control plane

The control plane orchestrates decisions. It is responsible for loading and
validating structured governance, resolving exactly one `Project` and a
non-empty deterministic set of `Domain` identifiers, applying `RoutingPolicy`
to select exactly one `WorktreeRole` that owns every resolved `Domain`, applying
customer permissions and `HostOverlay` restrictions, requesting live runtime
observations, coordinating write leases, and arranging trusted issuance or
validation of a bounded `TaskContract`.

The control plane MUST distinguish a request from authorization. Task intent is
untrusted input describing the requested outcome, requested mode, proposed
scope, and caller-provided constraints before governance resolution. Task
intent, prose instructions, and adapter input grant no permission by themselves.
A `TaskContract` MUST NOT create permission that is absent from its authoritative
inputs.

### Runtime inspection and coordination

Runtime inspection supplies current Git observations through core-defined
ports. Its implementations freshly inspect repository identity, worktree
registration, branch or detached state, `HEAD`, tracked, untracked, ignored and
submodule state, active Git operations, Git administrative locks, and other
required filesystem facts. Runtime coordination supplies task state, lease
records, lease-store synchronization, ownership records, release outcomes, and
lease-store locks through separate ports.

Candidate expected state comes from validated governance, resolved untrusted
task intent, and host-local bindings. Contract expected state is an immutable
baseline bound by a valid `TaskContract`. Fresh observations MUST be compared
with that baseline, explicit permitted transitions, changes attributable to
authorized execution, and required postconditions. Declared or previously
cached state MUST NOT substitute for a live observation, and authorized writes
MUST NOT absorb unrelated drift into a new trusted baseline.

Real host paths, concrete host-local and runtime objects, lease records, locks,
and runtime coordination state MUST remain outside the target worktree. Runtime
inspection and coordination are infrastructure boundaries, not sources of
policy authority. Git administrative locks and lease-store locks are distinct.

### Execution adapters

Execution adapters translate a valid `TaskContract` into an invocation of an
agent or another execution mechanism. An adapter MUST consume the contract as a
constraint, MUST NOT reinterpret a request as broader permission, and MUST NOT
widen its permitted mode, write authority, worktree, branch, responsibility
`Domain` set, or scope.

An adapter MAY report that it cannot satisfy a contract. It MUST NOT repair or
bypass a failed precondition. `AGENTS.md` is an explanatory, adapter-facing
entry document. It is not an execution adapter, policy source, `TaskContract`,
or authorization mechanism.

### Evidence layer

The evidence layer first captures pre-release execution and post-execution
verification evidence. After ownership-checked release is attempted and
`releaseOutcome` is known, it finalizes an `ExecutionReceipt` containing the
execution, verification, release, and overall lifecycle outcomes plus unresolved
coordination-state warnings. External receipt storage or delivery is reached
through a core-defined output port only after finalization.

Generated `ExecutionReceipt` records are host-local runtime evidence and MUST
remain outside portable repository governance. They MUST NOT be used as
authorization input, converted into permission, or treated as proof that the
current runtime state still matches an earlier observation. Receipt persistence
or delivery failure MUST be reported, MUST NOT grant authority or hide unresolved
lease state, and MUST NOT indefinitely retain an otherwise releasable lease.
Repository documentation MAY contain only conspicuously synthetic,
non-authoritative receipt-shaped examples.

## Dependency direction

Source-code dependencies point inward:

1. The core model has no dependency on control-plane orchestration,
   infrastructure, storage, Git tooling, or agent products.
2. The control plane depends on the core model and on abstract ports defined at
   the core boundary.
3. Configuration readers, live Git inspectors, lease stores, evidence sinks,
   and execution adapters implement those ports and depend on the core types.
4. Product-specific adapter code MAY depend on its product integration, but no
   dependency from the core or control plane may point back to that adapter.

Runtime data flows across those boundaries, but data-flow direction does not
reverse the source-code dependency rule. In particular, an adapter response or
an `ExecutionReceipt` cannot modify the policy under which its `TaskContract` was
issued.

## Object families and physical storage

All seven planned kinds use API version `contextctl.dev/v1alpha1`. Schema
definitions for every kind MAY later live under `schemas/v1alpha1/`; schema
placement does not determine instance trust or portability.

| Family | Concrete kinds | Required placement |
| --- | --- | --- |
| Portable customer governance | `Project`, `Domain`, `WorktreeRole`, `RoutingPolicy` | May be reviewed and versioned as portable policy. |
| Host-local input | `HostOverlay` | Outside the target worktree and portable governance. |
| Runtime artifacts | `TaskContract`, `ExecutionReceipt` | Outside the target worktree and portable governance. Generated receipts never become portable governance. |

Concrete host-local or runtime instances MUST NOT be placed in the target
worktree. Only conspicuously synthetic and non-authoritative receipt-shaped
documentation examples may appear in the repository.

## Authority and trust boundaries

The architecture has distinct trust domains:

| Input or component | Architectural role | Authority rule |
| --- | --- | --- |
| Structured customer governance | Portable policy authority | Defines the maximum permissions and worktree-role ownership of `Domain` identifiers available to the control plane. |
| Markdown and task intent | Human- and agent-facing explanation or request | May narrow a request but cannot independently grant authority. |
| `HostOverlay` | Host-local binding and restriction | MAY further restrict customer governance; MUST NOT widen it. |
| Runtime Git observations | Fresh facts about Git and filesystem state, including Git administrative locks | Gate execution but do not grant policy permission. |
| Runtime coordination state | Task, lease, ownership, release, synchronization, and lease-store-lock state | Gates coordination but does not grant policy permission. |
| Runtime write lease | Exclusive coordination for a write task | Gates concurrent writes but does not establish worktree-role ownership of `Domain` identifiers. |
| `TaskContract` | Derived, bounded authorization | Has authority only after trusted issuance or provenance validation and while all policy and runtime preconditions remain satisfied. |
| Execution adapter | Contract consumer | Cannot add authority or bypass a denial. |
| `ExecutionReceipt` | Host-local evidence output | Is never authorization input or portable governance. |

Valid customer governance, `HostOverlay` restrictions, worktree-role eligibility,
matching live state, and any required runtime write lease are independent
preconditions for `TaskContract` issuance. Any missing, malformed, ambiguous,
stale, or mismatched input denies issuance. Implementation additionally requires
a valid applicable `TaskContract` whose mode, `allowWrite` value, target, and
scope permit the protected action, followed by the required live revalidation.

A `TaskContract` has authority only when trusted framework logic issued it or
validated its trusted issuer, integrity, derivation, task and target binding,
freshness, and current policy, runtime, and lease preconditions. A caller-,
adapter-, or task-supplied object claiming to be a `TaskContract` is untrusted
input and MUST NOT grant or expand authority. A digest alone detects mutation
but does not prove trusted issuance. Phase 0 does not select a final signing
mechanism, and human bootstrap authority is not a substitute runtime `TaskContract`.

Customer governance and a `HostOverlay` are deliberately asymmetric. Customer
governance establishes the portable authorization ceiling. A `HostOverlay` binds
logical identities to local resources and can lower that ceiling. If the
overlay attempts to permit something forbidden by customer governance, the
customer restriction wins. If a required binding is absent or ambiguous, the
control plane MUST deny implementation.

## Ownership and concurrency are independent controls

Task resolution MUST first produce exactly one `Project` and a non-empty
deterministic set of `Domain` identifiers. `RoutingPolicy` then selects exactly
one `WorktreeRole` that owns every resolved `Domain`; it does not resolve the
project or discover the domain set. If no unique role covers the complete set,
the task MUST be split into independently authorized tasks or denied. A worktree
that is idle or otherwise free but has the wrong role is not an eligible target,
and the `TaskContract` MUST bind the same complete set.

A runtime write lease answers: **Does this task currently and provably own the
exclusive writer slot for this worktree?** Lease liveness is independent of
lifecycle phase and execution outcome. An unreleased, malformed, ambiguous,
stale, or otherwise unresolved lease remains blocking after success, denial,
failure, cancellation, or indeterminate execution.

Both checks are necessary for a write task, and neither implies the other. A
correct role with an unavailable lease MUST be denied for the current attempt.
Any retry begins a fresh lifecycle and MUST repeat routing, live inspection, and
lease acquisition. Planning does not turn a role-ineligible worktree into a
valid routing target. Competing writers remain denied until ownership-checked
release succeeds or a separately authorized operator-resolution procedure
completes. The framework MUST NOT break a lease automatically.

## Live inspection and fail-closed execution

The lifecycle has four distinct checkpoints: initial live preflight;
post-acquisition, pre-contract-issuance revalidation; post-contract,
immediately-before-action revalidation; and post-execution verification.
Runtime Git observations and runtime coordination state MUST be freshly read at
the applicable checkpoint. Issuing a `TaskContract` does not freeze Git state;
a mismatch found during revalidation invalidates the implementation path.

Inspection MUST be observational. The framework MUST NOT automatically:

- switch branches or create branches;
- stash, reset, clean, or restore files;
- fetch or pull;
- merge or rebase;
- break leases or locks; or
- repair Git state in any other way.

On a failed check, the control plane MUST report the observed mismatch without
performing corrective Git operations. Release MUST target only the lease
identified by the acquisition result and provably owned by the task. If a
`TaskContract` was issued, its lease identity MUST match that lease. Pre-contract
cleanup MUST NOT require a contract. If lease ownership cannot be verified or
safe release fails, the framework MUST report the failure, leave the lease and
lease-store lock intact, and deny later writers rather than break either. A
successful release is not authorization for further work.

## Contract and evidence flow

The intended control flow is:

1. Receive untrusted task intent.
2. Resolve exactly one `Project`.
3. Resolve a non-empty deterministic `Domain` set.
4. Use `RoutingPolicy` to select exactly one `WorktreeRole` covering every resolved `Domain`.
5. Resolve one local `HostOverlay` binding.
6. Perform initial live preflight.
7. Atomically acquire the task-owned write lease when required.
8. Re-read runtime Git observations and runtime coordination state.
9. If checks fail before contract issuance, deny issuance and release only the acquisition-result lease provably owned by the task without requiring a contract.
10. Have trusted framework logic issue or validate a state-bound `TaskContract`.
11. Perform post-contract, immediately-before-action contract scope validation and live-state revalidation.
12. Execute through an adapter within bounded authority.
13. Perform post-execution scope and state verification.
14. Capture pre-release execution and verification evidence.
15. Attempt ownership-checked lease release.
16. Record `releaseOutcome`.
17. Finalize the `ExecutionReceipt` with all terminal outcomes and unresolved coordination-state warnings.
18. Attempt external receipt persistence or delivery.
19. Leave unresolved lease state blocking until authorized resolution.
20. Complete lifecycle reporting without treating the receipt as authority.

Pre-execution scope authorization occurs before issuance, contract scope
validation occurs before action, and post-execution scope verification occurs
after execution. Every transition MUST have a denial or failure outcome.
Terminal processing MUST attempt to record a sanitized `ExecutionReceipt` for
every issued-contract execution attempt; pre-contract denial receipts MAY remain
policy-optional. Receipt failure cannot retroactively authorize execution or
retain an otherwise releasable lease, and an earlier receipt cannot satisfy a
later task's preflight.

## Sensitive and local information

Secrets MUST remain outside structured governance, Markdown, `TaskContract`
records, CLI arguments, logs, examples, and `ExecutionReceipt` records. Documentation and
evidence MUST use non-secret identifiers and sanitized examples. Portable
governance MUST NOT embed real host paths. Any local binding that requires a
real path belongs in a concrete `HostOverlay` outside the target worktree, and
runtime artifacts, lock material, and coordination state belong in host-local
runtime storage outside portable governance.
