# Architecture

## Status and scope

Phase 0 documentation bootstrap is complete at baseline commit
`79cc9d77fd48410f37645afdb429a7cd2e34a0bd`. Phase 1: Schemas and
Models is current, but Phase 1 implementation has not yet begun. The repository
remains pre-operational and has no Schema implementation, typed model, test,
fixture, package release, normal policy engine, trusted `TaskContract` issuer,
lease manager, Git inspector, CLI, adapter, enforcement mechanism, or
cryptographic authorization. Phase 1 activation is not operational-governance
activation, and the first Schema or model artifact requires a later, separately
authorized implementation task.

This document defines the intended boundaries and invariants of a future
implementation; it does not describe an existing execution runtime. The
initial architecture implementation is limited to the Schema and model layers
described below. Control-plane routing, runtime inspection and coordination,
authorization, execution adapters, and evidence remain later-phase work.

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

## Phase 1 implementation boundary

Phase 1 is limited to public JSON Schema definitions under
`schemas/v1alpha1/`, shared Schema definitions, strict object envelopes,
Schema-expressible structural constraints, conspicuously synthetic positive and
negative Schema fixtures, typed in-memory models, strict decoding, canonical
serialization, model unit tests, Schema validation and contract tests,
Schema/model conformance tests, and static configuration/model integrity
validation.

Allowed Phase 1 validation includes JSON Schema structural checks,
unknown-field rejection, supported API-version checks, field type and value
constraints, object-local invariants, deterministic decoding, canonical
serialization, representation conformance, ID uniqueness and reference checks
inside a closed synthetic or loaded bundle, and static restriction or model
invariants that do not calculate an operational result or require task intent,
task-specific host-binding resolution, Git state, lease state, or runtime
decisions. It also includes individual `HostOverlay` validation followed by
cross-resource binding-injectivity validation over an already-established
complete same-host overlay set; that validation does not select a target or
prove live physical identity.

Phase 1 MUST NOT match task intent to a `Project`, resolve a task's `Domain`
set, evaluate `RoutingPolicy` for an actual task, select a role, decide split
versus deny, calculate operational authorization, resolve a concrete host
binding, read live Git state, inspect or modify lease state, issue or validate
trusted runtime contract authority, or generate runtime receipt evidence.
Deterministic resolution and routing are Phase 2; live Git, worktree inspection,
runtime coordination, and leases are Phase 3; trusted contract issuance or
provenance validation, scope authorization and verification, terminalization,
and receipts are Phase 4; the CLI is Phase 5; and agent adapters are Phase 6.

### Required Schema-before-model sequence

1. Phase 1 activation is committed to `main`.
2. The repository owner creates or binds a dedicated `schema-contracts`
   worktree from that updated `main`.
3. The Schema contract baseline is designed in `schema-contracts`.
4. The Schema baseline receives independent read-only audit.
5. The Schema baseline is approved through `integration-control`.
6. The Schema baseline is committed, reviewed, and integrated into `main`.
7. Only after updated `main` contains the approved Schema baseline may the
   repository owner create or bind a distinct `model-implementation` worktree.
8. That model worktree MUST be created from the updated `main` containing the
   approved Schema baseline.
9. Model implementation then consumes the approved Schema contract.
10. Any requested Schema semantic change discovered during model work MUST be
    routed back to a separately authorized `schema-contracts` task and
    integrated first.

The model worktree MUST NOT be created from the Phase 0 baseline or before the
approved Schema baseline reaches `main`, and a free Schema worktree cannot be
reused for model implementation.

### Logical responsibility roles

`integration-control` owns phase decisions, cross-worktree coordination,
implementation sequencing, integration review, independent-audit gating, merge
readiness, promotion of approved baselines into `main`, release control, and
responsibility-boundary and escalation decisions. It does not own routine
Schema or Python model implementation, Phase 2 routing implementation, runtime
Git or lease implementation, or CLI or adapter implementation. `main` is the
control and integration baseline, not an ordinary implementation area.

`schema-contracts` owns `schemas/v1alpha1/**`, shared Schema definitions,
strict object envelopes, Schema-expressible structural constraints,
unknown-field rejection, types, formats, enums, required fields, local
structural invariants, conspicuously synthetic positive and negative Schema
fixtures, Schema validation and contract tests, and documentation changes
directly required to describe the finalized Schema contract. It does not own
Python models, decoding, canonical serialization, deterministic task
resolution, routing-policy execution, live Git inspection, runtime leases,
contract issuance, receipt generation, a CLI, adapters, or operational
enforcement. It MAY document semantic invariants that later phases must enforce
but MUST NOT implement Phase 2 routing behavior.

`model-implementation` owns typed in-memory representations corresponding to
the approved Schema contract, strict decoding, canonical serialization,
model-level validation that does not execute later control-plane behavior,
model unit tests, Schema/model conformance tests, and permitted static
configuration-integrity checks. It does not own independent redefinition of
Schema fields or semantics, task-intent resolution, `Project` or `Domain`
resolution, `RoutingPolicy` execution, role selection, host-binding execution,
live Git inspection, lease acquisition or release, contract issuance, receipt
generation, a CLI, adapters, or operational enforcement. A Schema mismatch
MUST stop model implementation for the affected contract and be routed back to
`schema-contracts`.

`integration-control` is a third responsibility role distinct from both
implementation roles. `schema-contracts` and `model-implementation`
implementation tasks MUST use distinct worktrees; they MUST NOT be assigned to,
implemented in, or allowed to write through the same worktree. A free Schema
worktree cannot be reused for model implementation. Concrete local paths are
host-local and are not portable governance. Branch creation, worktree creation
or binding, committing, merging, and pushing require separately authorized
repository-owner administrative actions; a Codex implementation task MUST NOT
perform them under the current pre-operational procedure.

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

For each validation or revalidation checkpoint, configuration authority MUST
provide one trusted configuration validation snapshot: an internally coherent,
read-only view of the trusted closed configuration inventory for that
checkpoint. It MAY establish that view through an immutable snapshot or read
view, a transactionally consistent read, an authority-native configuration
revision, or an equivalent trusted state identity; no storage technology is
required. The mechanism MUST prove that both complete same-host membership and
the exact contents of every participating resource belong to one coherent
configuration state.

The control plane MUST consume that single view as one atomic or consistent
proof boundary for target `hostId` selection, complete same-host enumeration,
completeness, individual resource validation, binding-union construction,
set-wide injectivity, and resulting static eligibility. If snapshot consistency
cannot be established or a relevant configuration change occurs while the
proof is formed, the current gate fails closed and no partial result becomes
eligibility evidence. A later checkpoint MAY use a newer coherent snapshot,
but evidence from incompatible snapshots MUST NOT be composed into one
eligibility result.

From that checkpoint's snapshot, before exposing a host binding as statically
eligible, the control plane MUST obtain the [complete same-host overlay
set](configuration-model.md#hostoverlay). Every configured `HostOverlay` for
the target `hostId`, exactly as represented in that snapshot, participates
across all `projectRef` values. After each overlay validates individually,
Phase 1 static validation MUST validate the union of those snapshot-bound
bindings for host-wide `worktreeId` uniqueness and exclusivity of each
already-validated exact `(platform, repositoryRoot.value)` identity. Project
boundaries, distinct overlay IDs, task input, and adapter selection cannot
partition or narrow this comparison; incomplete evidence fails closed.

`integration-control` owns the inventory boundary, set-wide gate sequencing,
fail-closed completeness rule, and integration review. The complete same-host
overlay set is control-plane comparison context, not a serialized resource.
Each `HostOverlay` remains host-local and outside portable customer governance,
and it may bind or narrow authority but never widen it.

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

At future Phase 3 checkpoints relevant to binding, contract issuance, and
action, runtime inspection MUST prove that every distinct binding across the
complete same-host overlay set derived from that checkpoint's coherent trusted
configuration validation snapshot still resolves to a distinct canonical
registered physical Git worktree. Case and Unicode identity, filesystem
aliases, symlinks, junctions, reparse points, Windows 8.3 aliases, `.git`
indirection, linked-worktree registration, common-Git-directory relationships,
conflicting registrations, inaccessible canonicalization, and every other
unresolved physical-identity ambiguity fail closed. Equal path strings on
different hosts are not globally exclusive merely because their spelling is
equal. Runtime inspection does not repair, normalize, rebind, switch branches,
or delete worktrees to manufacture a passing identity proof.

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
mechanism, and pre-operational `human-bootstrap-maintenance` authority is not a
substitute runtime `TaskContract`.

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
5. From one coherent checkpoint-local trusted configuration validation
   snapshot, establish the complete same-host overlay set, pass individual and
   set-wide static gates, and then resolve one local `HostOverlay` binding.
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
