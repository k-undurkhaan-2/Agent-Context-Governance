# Planned `contextctl` package boundaries

Phase 0 documentation bootstrap is complete at baseline commit
`79cc9d77fd48410f37645afdb429a7cd2e34a0bd`. Phase 1: Schemas and
Models is current, but Phase 1 implementation has not yet begun. The repository
remains pre-operational, and this directory contains no Python implementation,
packaging metadata, command-line executable, or operational framework behavior.

Initial model work begins only after the Schema contract baseline has been
designed in `schema-contracts`, independently audited, approved through
`integration-control`, committed, reviewed, and integrated into `main`. Only
then may the repository owner create or bind the distinct
`model-implementation` worktree from that updated `main`. The model role
consumes the approved Schema baseline and MUST stop for the affected contract
and route any requested Schema semantic change back to a separately authorized
`schema-contracts` task for prior integration.

## Phase 1 model boundary

`model-implementation` owns typed in-memory representations corresponding to
the approved Schema contract, strict decoding, canonical serialization,
model-level validation that does not execute later-phase control-plane
behavior, model unit tests, Schema/model conformance tests, and static
configuration-integrity checks permitted by the approved Phase 1 boundary.

Phase 1 model validation MAY cover deterministic decoding and serialization,
model/Schema representation conformance, ID uniqueness and reference existence
inside a closed synthetic or loaded governance bundle, static
restriction-shape checks that do not calculate operational authorization, and
static model invariants that do not require task intent, host bindings, Git
state, lease state, or runtime decisions.

The model role MUST NOT independently redefine Schema fields or semantics or
implement task-intent resolution, `Project` or `Domain` resolution,
`RoutingPolicy` execution, role selection, host-binding execution, live Git
inspection, lease acquisition or release, `TaskContract` issuance,
`ExecutionReceipt` generation, a CLI, adapters, or operational enforcement.

## Later package areas

Resolution and routing remain Phase 2; runtime Git and worktree inspection and
leases remain Phase 3; trusted contract issuance, scope verification,
terminalization, and receipts remain Phase 4; the CLI remains Phase 5; and
agent adapters remain Phase 6. None of those package areas is implemented.

Dependencies will point inward toward models and policy rules. The core will
remain independent of any agent product, and later runtime inspection and
persistence will be isolated behind explicit interfaces.
