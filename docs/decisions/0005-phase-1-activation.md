# ADR 0005: Activate Phase 1 schemas and models

- Status: Accepted

## Context

Phase 0 documentation bootstrap established the project identity, vocabulary, architectural boundaries, authority model, worktree guard, and task lifecycle. Phase 0 is complete at baseline commit `79cc9d77fd48410f37645afdb429a7cd2e34a0bd`.

The repository is still pre-operational. It has no public JSON Schemas, typed models, deterministic router, live Git inspector, runtime write-lease manager, trusted `TaskContract` issuer, `ExecutionReceipt` generator, CLI, agent adapter, operational enforcement mechanism, or cryptographic authorization. The normal operational governance path therefore cannot authorize implementation of its own foundations.

An explicit decision is required to make Phase 1 current, define its exact boundary, preserve the temporary bootstrap authority needed while the governance core is absent, and separate implementation responsibilities before any Schema or model work begins.

## Decision

### Phase transition

Phase 0 is complete at baseline commit `79cc9d77fd48410f37645afdb429a7cd2e34a0bd`.

Phase 1: Schemas and Models is current. Activation does not mean Phase 1 is implemented or complete. Phase 1 implementation has not yet begun, and this decision creates no code, Schema, fixture, test, CLI, adapter, configuration instance, CI workflow, or operational control.

### Phase 1 scope

Phase 1 is limited to:

- public JSON Schema definitions under `schemas/v1alpha1/`;
- shared Schema definitions;
- strict object envelopes;
- Schema-expressible structural constraints;
- unknown-field rejection;
- types, formats, enums, required fields, and local structural invariants;
- conspicuously synthetic positive and negative Schema fixtures;
- in-memory typed models;
- strict decoding;
- canonical serialization;
- Schema validation and contract tests;
- model unit tests;
- Schema/model conformance tests; and
- static configuration/model integrity validation within the boundary below.

Phase 1 validation MAY implement JSON Schema structural validation,
unknown-field rejection, supported API-version checks, field type, format, enum,
range, and required-property validation, object-local invariants, deterministic
decoding, canonical serialization, model/Schema representation conformance, ID
uniqueness and reference shape or existence checks inside a closed synthetic or
loaded governance bundle, static restriction-shape checks that do not calculate
an operational authorization result, and static model invariants that do not
require task intent, host bindings, Git state, lease state, or runtime decisions.

Phase 1 MUST NOT match task intent to a `Project`; resolve a task's affected
`Domain` set; evaluate `RoutingPolicy` for an actual task; select a
`WorktreeRole`; decide split versus deny for a real task; calculate effective
operational authorization; resolve a concrete `HostOverlay` binding; read live
Git state; inspect or modify lease state; issue or validate trusted runtime
`TaskContract` authority; or generate runtime `ExecutionReceipt` evidence.

Deterministic task-intent resolution, exact `Project` selection, complete
`Domain`-set resolution, routing evaluation, covering-role selection, ambiguity
handling, and split-or-deny decisions remain Phase 2. Live Git and worktree
inspection, runtime coordination, and write leases remain Phase 3. Trusted
contract issuance or provenance validation, scope authorization and
verification, terminalization, and receipt generation remain Phase 4. The CLI
remains Phase 5, and agent adapters remain Phase 6.

The Schema contract baseline is sequentially prior to model implementation.
Typed models, decoding, serialization, and model tests MUST conform to the
integrated Schema contract baseline and MUST NOT redefine Schema semantics
independently.

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
reused as the model worktree.

Phase 1 continues to exclude:

- deterministic task routing implementation;
- live Git inspection;
- runtime write leases;
- `TaskContract` issuance;
- `ExecutionReceipt` generation;
- a CLI;
- agent adapters;
- operational enforcement; and
- cryptographic authorization.

### Logical worktree roles

`integration-control` owns phase decisions, cross-worktree coordination,
implementation sequencing, integration review, independent-audit gating, merge
readiness, promotion of approved baselines into `main`, release control, and
responsibility-boundary and escalation decisions. It does not own routine
Schema implementation, routine Python model implementation, Phase 2 routing
implementation, runtime Git or lease implementation, or CLI or adapter
implementation. `main` is the control and integration baseline, not an ordinary
implementation area.

`schema-contracts` owns `schemas/v1alpha1/**`, shared Schema definitions,
strict object envelopes, Schema-expressible structural constraints,
unknown-field rejection, types, formats, enums, required fields, local
structural invariants, conspicuously synthetic positive and negative Schema
fixtures, Schema validation and contract tests, and documentation changes
directly required to describe the finalized Schema contract. It does not own
Python model implementation, decoding implementation, canonical serializer
implementation, deterministic task resolution, routing-policy execution, live
Git inspection, runtime leases, `TaskContract` issuance, receipt generation, a
CLI, adapters, or operational enforcement. The role MAY document semantic
invariants that later phases must enforce, but it MUST NOT implement Phase 2
routing behavior.

`model-implementation` owns typed in-memory representations corresponding to
the approved Schema contract, strict decoding, canonical serialization,
model-level validation that does not execute later-phase control-plane
behavior, model unit tests, Schema/model conformance tests, and static
configuration-integrity checks permitted by the approved Phase 1 boundary. It
does not own independent redefinition of Schema fields or semantics,
task-intent resolution, `Project` selection, `Domain` resolution,
`RoutingPolicy` execution, role-selection decisions, host-binding execution,
live Git inspection, lease acquisition or release, `TaskContract` issuance,
`ExecutionReceipt` generation, a CLI, adapters, or operational enforcement.
Any Schema mismatch discovered by this role MUST stop model implementation for
the affected contract and be routed back to `schema-contracts`.

Logical worktree roles are portable governance concepts. Concrete local worktree paths are host-local and MUST NOT be committed. This decision does not create worktrees or host bindings and does not claim that operational role routing exists.

`integration-control` is a third, distinct responsibility role.
`schema-contracts` and `model-implementation` implementation tasks MUST use
distinct worktrees. They MUST NOT be assigned to, implemented in, or allowed to
write through the same worktree.

Branch creation, worktree creation or binding, committing, merging, and pushing
remain separately authorized repository-owner administrative actions. A Codex
implementation task MUST NOT create its own branch or worktree under the
current pre-operational procedure.

### Pre-operational bootstrap implementation authority

Pre-operational `human-bootstrap-maintenance` authority MAY be used for implementation or repair of this governance framework itself while all of the following remain true:

- the normal operational authorization path does not yet exist;
- the task implements or repairs the governance core;
- the authorization is supplied directly for the current task by the repository owner;
- exactly one repository and worktree, the branch, `HEAD`, complete status and file inventory, paths, permitted operations, prohibited operations, and lifetime are precisely bounded; and
- ordinary task intent, caller assertions, adapters, receipts, observed convenience, and other lower-trust input cannot widen the authorization.

The authorization is cooperative, narrow, fail closed, non-reusable, and non-delegable unless delegation is explicit. It expires at task completion or earlier on any repository, worktree, branch, `HEAD`, status, path, remote, operation, active-Git-state, administrative-lock, or scope mismatch. It is not ordinary task intent, a caller-created `TaskContract`, a `HostOverlay` permission, an `ExecutionReceipt`, a Markdown grant, or an implemented policy-engine decision. It MUST NOT be represented as a runtime contract, lease, receipt, or cryptographic authorization.

Bootstrap authority MUST NOT authorize:

- customer application work;
- unrelated feature work;
- another repository;
- another worktree unless separately and explicitly bound;
- production deployment;
- secret handling;
- automatic Git repair;
- branch switching or creation;
- worktree creation;
- staging;
- committing; or
- pushing.

Bootstrap authority also MUST NOT bypass logical role ownership, the distinct
worktree requirement, the Schema-before-model sequence, current-baseline
requirements, or the separation of repository-owner administrative actions
from an implementation task.

This authority remains necessary because the normal governance core and trusted issuer do not yet exist and cannot authorize their own implementation. It is temporary because retaining an external owner grant after operational activation would bypass structured governance, state binding, least authority, and deterministic enforcement. It MUST be retired or disabled when the project formally activates its operational governance and trusted contract-issuance path. That later activation decision must identify the trusted governance source, trusted issuer, and separately governed administrative recovery and emergency procedures.

Phase 1 activation is not the retirement condition and does not activate operational governance.

## Consequences

- Phase 0 has a fixed completion baseline, and Phase 1 has an explicit current status without a false implementation claim.
- Schema meaning is established once before typed models are allowed to encode it.
- The Schema baseline is independently audited, approved, committed, reviewed,
  and integrated before the distinct model worktree is created from updated
  `main`.
- Routine Schema and model implementation is kept out of `integration-control`
  and `main`, and the two implementation roles cannot share a worktree.
- Phase 1 static configuration/model integrity checks cannot become Phase 2
  routing, Phase 3 runtime coordination, or Phase 4 authorization execution.
- Portable role identity remains separate from host-local worktree paths and administrative Git actions.
- The repository remains fail closed and pre-operational while the narrowly bounded external root of trust is still necessary.
- Later phases cannot be inferred from Phase 1 activation and require their own explicit decisions and authority.

## Alternatives not selected

### Implementing on `main`

Using `main` as the ordinary Phase 1 implementation area was not selected because `integration-control` must remain focused on phase decisions, integration review, merge readiness, and release control rather than routine Schema or model construction.

### Developing schemas and models concurrently from the Phase 0 baseline

Concurrent independent development was not selected because models could silently define semantics that differ from the public Schema contract. The accepted order integrates the Schema baseline before model implementation begins.

### Reusing the Schema worktree for model implementation

Reusing even a free `schema-contracts` worktree was not selected because role
ownership and physical worktree isolation would be lost. Schema and model
implementation require distinct worktrees.

### Creating the model worktree before Schema integration

Creating or binding the model worktree from the Phase 0 baseline or before the
approved Schema baseline reaches `main` was not selected because it would allow
model work to begin without the integrated contract it must consume.

### Treating operational semantic validation as Phase 1 model validation

Broad operational resolution, routing, runtime, and authorization semantics
were not selected for Phase 1 because they belong to Phases 2 through 4. Phase
1 is limited to structural validation and static configuration/model integrity.

### Treating Phase 1 activation as operational-governance activation

This was not selected because routing, live Git inspection, leases, trusted contract issuance, receipts, adapters, enforcement, and cryptographic authorization do not exist. A phase decision cannot substitute for those controls.

### Allowing unrestricted owner implementation authority

An unrestricted owner grant was not selected because it would be reusable, scope-free authority that lower-trust input could exploit and that would defeat fail-closed state binding. The accepted bootstrap path is cooperative, task-specific, temporary, and precisely bounded.
