# Configuration Model

## Status

Phase 0 documentation bootstrap is complete at baseline commit
`79cc9d77fd48410f37645afdb429a7cd2e34a0bd`. Phase 1: Schemas and
Models is current, but Phase 1 implementation has not yet begun. The repository
remains pre-operational and has no Schema implementation, typed model, test,
fixture, package release, or Phase 2–6 operational feature. Phase 1 activation
is not operational-governance activation; the first Schema or model artifact
requires a later, separately authorized implementation task.

This document defines the responsibilities, authority classes, and relationships
of the planned configuration objects. It is not a finished field specification
and does not define JSON Schemas, exact property names, serialization layouts,
or a committed configuration instance. The semantic minimum bindings defined
below are mandatory future requirements even though their serialization is
deferred.

The initial public configuration API version is
`contextctl.dev/v1alpha1`. Future Schema files will live under
`schemas/v1alpha1/`.

Package releases use Semantic Versioning and will begin later with `0.1.0`.
Package versions and public configuration API versions are independent. A
package release number MUST NOT be interpreted as a configuration API version,
and no compatibility mapping is implied by matching or differing numbers.

## Configuration authority

Machine-readable structured customer governance is authoritative. Markdown MAY
explain, summarize, or mirror policy, but it cannot independently grant
authority. `AGENTS.md` is an explanatory, adapter-facing entry document. It is
not an execution adapter, policy source, `TaskContract`, or authorization
mechanism.

Task intent is untrusted input describing the requested outcome, requested mode,
proposed scope, and caller-provided constraints before governance resolution. It
MUST NOT grant authority. Validation, resolution, or a task-intent digest does
not promote it into an authority source.

The authorization model only narrows permission:

1. Customer governance establishes the portable maximum.
2. A `HostOverlay` binds that model to a particular host and MAY impose further
   restrictions.
3. Worktree-role ownership of the complete `Domain` set, live runtime state, and
   a runtime write lease when required determine whether the requested operation
   is currently eligible.
4. Trusted framework logic issues or validates a bounded `TaskContract`.
5. An `ExecutionReceipt` records evidence and is excluded from authorization.

A `HostOverlay` MUST NOT widen customer governance. Task intent, local
availability, an adapter's capabilities, and historical receipts also MUST NOT
widen it. Effective permission is the intersection of applicable restrictions,
conditioned on current runtime preconditions.

The default authorization is:

```yaml
mode: plan-only
allowWrite: false
```

Missing or inconclusive configuration MUST preserve that non-writing default;
it MUST NOT imply implementation permission.

`mode: plan-only` implies `allowWrite: false`. The combination of
`mode: plan-only` and `allowWrite: true` is invalid and MUST be rejected. Future
governed adapter execution, including plan-only execution, requires a valid
bounded `TaskContract`.

A `TaskContract` has authority only when trusted framework logic issued it or
validated its trusted issuer, integrity, derivation, task and target binding,
freshness, and current policy, runtime, and lease preconditions. A caller-,
adapter-, or task-supplied object claiming to be a `TaskContract` is untrusted
input and MUST NOT grant or expand authority. A digest alone detects mutation
but does not prove trusted issuance. Phase 0 does not select a final signing
mechanism, and pre-operational `human-bootstrap-maintenance` authority is not a
substitute runtime `TaskContract`.

## Planned object kinds and families

Backticked PascalCase denotes a structured object kind. Spaced lowercase wording
denotes the prose concept. All seven planned kinds use API version
`contextctl.dev/v1alpha1`; schema definitions for every kind MAY later live
under `schemas/v1alpha1/`. Schema placement does not determine instance trust or
physical storage.

| Family | Concrete kinds | Trust and placement |
| --- | --- | --- |
| Portable customer governance | `Project`, `Domain`, `WorktreeRole`, `RoutingPolicy` | Customer-governed policy authority that may be reviewed and versioned as portable configuration. |
| Host-local input | `HostOverlay` | Restriction-only binding outside the target worktree and portable governance. |
| Runtime artifacts | `TaskContract`, `ExecutionReceipt` | Conditional authorization and evidence outside the target worktree and portable governance. Generated receipts never become portable governance. |

### `Project`

`Project` is the portable root of a customer's governance model. It gives other
objects a stable project context and establishes project-wide secure defaults.
It MAY compose references to domains, roles, and routing policy, but its future
schema MUST avoid machine-specific paths and runtime state.

A valid `Project` does not establish that a local checkout exists or that its
Git state is suitable. Those are host-binding and live-inspection concerns.

Task resolution MUST produce exactly one `Project`; no match or multiple matches
deny implementation.

### `Domain`

`Domain` represents a responsibility area within a project. Resolution MUST
produce a non-empty deterministic set of `Domain` identifiers covering every
responsibility affected by the task. Domain constraints can narrow project-wide
permission; they MUST NOT silently broaden it.

Domain boundaries need to be precise enough that resolution is deterministic.
Zero domains, incomplete coverage, or ambiguous resolution MUST deny
implementation rather than select a convenient fallback.

### `WorktreeRole`

`WorktreeRole` describes what a worktree is allowed to be responsible for, not
where a worktree is located. Exactly one selected role MUST own every `Domain`
in the resolved set. Its ownership declaration is an authorization precondition
independent from worktree availability.

If no unique role covers the complete set, the task MUST be split into
independently authorized tasks or denied. An idle worktree with the wrong role
is not eligible. Conversely, a correct role does not imply that the worktree is
registered, on the expected branch, clean enough
for the task, or available for writing; live inspection and lease checks decide
those separate questions.

### `HostOverlay`

`HostOverlay` maps portable project and role identities to local resources and
host-specific expectations. Real host paths belong here or in host-local runtime
state, never in portable governance. Concrete `HostOverlay` instances and all
real host binding data MUST remain outside the target worktree.

The overlay applies an intersection rule: it MAY remove permissions or make a
binding more specific, but it MUST NOT add a `Domain`, worktree-role ownership, operation,
or write permission that customer governance does not allow. A missing,
malformed, stale, mismatched, or ambiguous required binding denies
implementation.

### `RoutingPolicy`

After exactly one `Project` and the complete `Domain` set have been resolved,
`RoutingPolicy` deterministically selects exactly one eligible `WorktreeRole`
that owns every resolved `Domain`. It does not resolve the project or discover
the domain set. It MUST evaluate worktree-role ownership before availability and
MUST NOT route to an ineligible role merely because its worktree is free or
treat a runtime write lease as evidence of ownership.

Phase 1 static integrity checks MAY reject duplicate identifiers, invalid
references, or declared ownership conflicts visible inside a closed loaded
bundle, but they MUST NOT evaluate a `RoutingPolicy` for an actual task or
determine its covering role. Conflicting or ambiguous operational routing
outcomes are Phase 2 decisions and deny implementation.

### `TaskContract`

`TaskContract` is a runtime artifact derived after configuration validation,
resolution, host binding, and initial live preflight. For a write task, issuance
also requires acquisition of the task-owned runtime write lease followed by
successful post-acquisition, pre-contract-issuance revalidation.

A future `TaskContract` MUST bind at least:

- object API version;
- contract version;
- unique contract identity;
- unique task identity;
- resolved `Project` identity;
- repository identity;
- selected target worktree identity or logical binding;
- the complete non-empty `Domain` set;
- required `WorktreeRole`;
- trusted issuer or validated provenance information;
- policy and configuration digests;
- task-intent digest or equivalent immutable binding;
- requested and effective mode;
- explicit `allowWrite`;
- authorized path scope;
- prohibited path scope where represented;
- expected baseline branch or detached state;
- expected baseline `HEAD` or unborn state;
- expected index condition;
- expected tracked, untracked, ignored, and submodule conditions where required;
- explicit permitted transitions;
- required postconditions;
- `leaseRequired`;
- lease identity when required;
- issuance checkpoint; and
- mandatory expiry or equivalent freshness boundary.

The expected baseline remains immutable. Later validation compares fresh
observations with that baseline, explicitly permitted transitions, changes
attributable to authorized execution, and required postconditions. Authorized
writes MUST NOT absorb unrelated drift into a new trusted baseline.

The contract MUST bind the same complete `Domain` set and be no broader than
customer governance or the `HostOverlay`. It remains conditional on live facts,
so the implementation path MUST perform post-contract,
immediately-before-action revalidation. Missing, malformed, ambiguous, stale, or
mismatched contract or runtime state denies implementation. A runtime lease does
not grant worktree-role ownership, and worktree-role ownership does not grant a runtime
lease. When a lease is required, the contract's lease identity MUST match the
acquisition result.

Release MUST target only the lease identified by the acquisition result and
provably owned by the task. If a `TaskContract` was issued, its lease identity
MUST match that lease. Pre-contract cleanup MUST NOT require a contract.

No `TaskContract` may contain secrets. Concrete host binding data, if required
at runtime, MUST remain in host-local storage outside the target worktree.

### `ExecutionReceipt`

An `ExecutionReceipt` MAY be created as evidence after a pre-contract denial
when future policy explicitly requires it. Terminal processing MUST attempt to
record a sanitized `ExecutionReceipt` for every issued-contract execution attempt. It is
finalized only after ownership-checked lease release is attempted and
`releaseOutcome` is known. It records execution outcome, verification outcome,
release outcome, overall lifecycle outcome, and unresolved coordination-state
warnings, along with enough sanitized context to explain the attempt.

A receipt MUST NOT be accepted as authorization input for the same task or a
later task. It does not prove that current Git state matches an earlier
observation. Receipts MUST NOT contain secrets. Generated `ExecutionReceipt`
records are host-local runtime evidence and MUST remain outside the target
worktree and portable governance. Repository documentation MAY contain only
conspicuously synthetic receipt-shaped examples; synthetic examples are not
generated runtime receipts and MUST NOT be authorization input.

Receipt persistence or delivery occurs after finalization. Failure MUST be
reported, MUST NOT grant authority or hide unresolved lease state, and MUST NOT
indefinitely retain an otherwise releasable lease.

## Runtime facts, coordination, and artifacts

Runtime Git observations are freshly read Git and filesystem facts, including
repository identity, worktree registration, branch or detached state, `HEAD`,
tracked, untracked, ignored and submodule state, active Git operations, and Git
administrative locks.

Runtime coordination state includes task state, lease records, lease-store
synchronization, ownership records, release outcomes, and lease-store locks.
Git administrative locks and lease-store locks are distinct. These facts and
coordination records MUST be observed or maintained live outside the target
worktree. A portable object may express an expectation, but it cannot make that
expectation an observed fact.

Concrete `TaskContract` and `ExecutionReceipt` instances are runtime artifacts,
not customer policy or a mechanism for editing or overriding it. Lease liveness
is independent of execution outcome; unresolved lease state remains blocking
until ownership-checked release or separately authorized operator resolution.

## Validation model

Phase 1 MAY implement only JSON Schema structural validation and static
configuration/model integrity validation. That boundary includes:

- unknown-field rejection;
- supported API-version checks;
- field type, format, enum, range, and required-property validation;
- object-local invariants;
- deterministic decoding and canonical serialization;
- model/Schema representation conformance;
- ID uniqueness inside a closed synthetic or loaded governance bundle;
- reference shape and reference existence checks inside that closed bundle;
- static restriction-shape checks that do not calculate an operational
  authorization result; and
- static model invariants that do not require task intent, host bindings, Git
  state, lease state, or runtime decisions.

Phase 1 MUST NOT execute broader operational semantics. It MUST NOT match task
intent to a `Project`; resolve an affected `Domain` set from a task; evaluate
`RoutingPolicy` for an actual task; select a `WorktreeRole`; decide split versus
deny for a real task; calculate effective operational authorization; resolve a
concrete `HostOverlay` binding; read live Git state; inspect or modify lease
state; issue or validate trusted runtime `TaskContract` authority; or generate
runtime `ExecutionReceipt` evidence.

Phase 2 owns task-intent resolution, exact `Project` selection, complete
`Domain`-set resolution, `RoutingPolicy` evaluation, covering-role selection,
routing ambiguity and split-or-deny decisions, and deterministic routing
results. Phase 3 owns live Git and worktree inspection, runtime coordination,
and write leases. Phase 4 owns trusted `TaskContract` issuance or provenance
validation, the scope authorization and verification lifecycle,
terminalization, and `ExecutionReceipt` generation. Phase 5 owns the CLI, and
Phase 6 owns agent adapters.

Runtime validation remains separate. A structurally and statically valid
configuration bundle under the Phase 1 boundary cannot prove the current
repository root, branch, HEAD, dirty state, active operation state, worktree
registration, role binding, or lease availability. Those later-phase
conditions MUST be inspected live and fail closed when missing, malformed,
ambiguous, stale, or mismatched.

This bootstrap intentionally leaves exact property names, nesting,
serialization choices, schema identifiers, compatibility rules within
`v1alpha1`, and migration mechanics for later design. Deferring those details
MUST NOT weaken the authority, narrowing, ownership, lease, live-inspection, or
evidence invariants defined here.

## Sensitive information

Secrets MUST remain outside governance files, Markdown, `TaskContract` records,
CLI arguments, logs, examples, and `ExecutionReceipt` records. Portable objects and examples
MUST use sanitized logical identifiers rather than real host paths or customer
infrastructure details. Host-local bindings and runtime files MUST remain
outside the target worktree.
