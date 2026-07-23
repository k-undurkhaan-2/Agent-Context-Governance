# Roadmap

## Status

**Phase 0: Documentation Bootstrap** is complete at baseline commit `79cc9d77fd48410f37645afdb429a7cd2e34a0bd`. **Phase 1: Schemas and Models** is current. Phase 1 implementation has not yet begun, and activation is not evidence that a Schema implementation, Python model, test, fixture, package release, or any later operational control exists.

The repository remains pre-operational; normal operational governance still does not exist.

Advancing to another phase remains an explicit project decision. A phase name or description MUST NOT be treated as evidence that its controls exist, are complete, or are safe to rely on.

Product and package releases will use Semantic Versioning, beginning later with `0.1.0`. Public configuration APIs are versioned independently. The planned initial configuration API is `contextctl.dev/v1alpha1`; its future schema files will live under `schemas/v1alpha1/`.

## Phase 0 - Documentation Bootstrap (complete)

Phase 0 established project identity, scope, vocabulary, architectural principles, trust boundaries, configuration authority, worktree responsibilities, task lifecycle expectations, and directory responsibilities.

Phase 0 remained documentation-only and provided no working CLI, schemas, policy engine, router, Git inspector, lease manager, contract issuer, execution adapter, or receipt generator. Its completion baseline is `79cc9d77fd48410f37645afdb429a7cd2e34a0bd`.

Completion means the baseline bootstrap documents were mutually consistent and distinguished normative structured governance planned for later phases from explanatory Markdown. It does not mean the operational governance path exists.

## Phase 1 - Schemas and Models (current)

Phase 1 is activated, but implementation has not yet begun. Its exact scope is:

- public JSON Schema definitions under `schemas/v1alpha1/`;
- shared Schema definitions;
- strict object envelopes;
- Schema-expressible structural constraints and unknown-field rejection;
- field types, formats, enums, required properties, and local invariants;
- conspicuously synthetic positive and negative Schema fixtures;
- in-memory typed models;
- strict decoding;
- canonical serialization;
- Schema validation and contract tests;
- model unit tests and Schema/model conformance tests; and
- bounded static configuration/model integrity validation.

Future Schema definitions will cover `Project`, `Domain`, `WorktreeRole`, `HostOverlay`, `RoutingPolicy`, `TaskContract`, and `ExecutionReceipt`, but Schema placement will not make every concrete instance portable. Concrete `Project`, `Domain`, `WorktreeRole`, and `RoutingPolicy` instances are portable customer governance; concrete `HostOverlay` instances are host-local input; and concrete `TaskContract` and `ExecutionReceipt` instances are runtime artifacts. Host-local and runtime instances MUST remain outside the target worktree, and generated receipts MUST never become portable governance.

Machine-readable structured governance configuration will be authoritative for
the future operational path. Phase 1 validation MAY implement JSON Schema
structural checks; unknown-field and supported-version rejection; field and
object-local constraints; deterministic decoding; canonical serialization;
Schema/model conformance; ID uniqueness and reference checks within a closed
synthetic or loaded governance bundle; and static restriction or model
invariants that do not calculate an operational result or require task intent,
host bindings, Git state, lease state, or runtime decisions. Markdown MAY
explain or mirror policy, but MUST NOT independently grant authority. Package
versions and configuration API versions MUST remain independent.

Phase 1 MUST NOT execute task-to-`Project` matching, task `Domain` resolution,
`RoutingPolicy` evaluation, role selection, split-versus-deny decisions,
effective operational authorization, concrete host binding, live Git
inspection, lease operations, trusted runtime contract issuance or validation,
or runtime receipt generation. Those responsibilities remain in Phases 2
through 4; CLI and adapter implementation remain Phases 5 and 6.

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

The planned logical worktree roles are:

- **`integration-control`** owns phase decisions, cross-worktree coordination,
  implementation sequencing, integration review, independent-audit gating,
  merge readiness, promotion of approved baselines into `main`, release
  control, and responsibility-boundary and escalation decisions. It does not
  own routine Schema or Python model implementation, Phase 2 routing, runtime
  Git or lease implementation, or CLI or adapter implementation. `main` is the
  control and integration baseline, not an ordinary implementation area.
- **`schema-contracts`** owns `schemas/v1alpha1/**`, shared definitions, strict
  envelopes, Schema-expressible constraints, unknown-field rejection, field
  constraints and local invariants, synthetic fixtures, Schema validation and
  contract tests, and directly required Schema documentation. It does not own
  Python models, decoding, serialization, task resolution, routing execution,
  live Git, leases, contracts, receipts, a CLI, adapters, or operational
  enforcement.
- **`model-implementation`** owns typed representations of the approved Schema
  contract, strict decoding, canonical serialization, bounded model validation,
  model unit tests, Schema/model conformance tests, and permitted static
  integrity checks. It does not own Schema redefinition, task-intent or
  Project/Domain resolution, routing, role or host-binding decisions, live Git,
  leases, contracts, receipts, a CLI, adapters, or operational enforcement. A
  Schema mismatch stops affected model work and routes back to
  `schema-contracts`.

`integration-control` is a third responsibility role. `schema-contracts` and
`model-implementation` implementation tasks MUST use distinct worktrees. They
MUST NOT be assigned to, implemented in, or allowed to write through the same
worktree.

Logical worktree roles are portable governance concepts. Concrete local paths
remain host-local and MUST NOT be committed. Branch creation, worktree creation
or binding, committing, merging, and pushing remain separately authorized
repository-owner administrative actions. A Codex implementation task MUST NOT
create its own branch or worktree under the current pre-operational procedure.

Phase 1 explicitly excludes deterministic task routing implementation, live Git inspection, runtime write leases, `TaskContract` issuance, `ExecutionReceipt` generation, a CLI, agent adapters, operational enforcement, and cryptographic authorization.

Because the normal operational authorization path does not yet exist, a repository owner MAY still provide narrow pre-operational `human-bootstrap-maintenance` authority for implementation or repair of this governance framework itself. It MUST be repository-, worktree-, branch-, `HEAD`-, status-, path-, operation-, and lifetime-bounded, supplied directly for the task, fail closed on mismatch, and immune to widening by lower-trust input. It MUST NOT authorize customer application work, unrelated feature work, another repository, another worktree unless separately and explicitly bound, production deployment, secret handling, automatic Git repair, branch switching or creation, worktree creation, staging, committing, or pushing. It cannot bypass role ownership, distinct-worktree requirements, sequencing, current-baseline requirements, or administrative-action separation. This temporary cooperative path retires when the operational governance and trusted contract-issuance path is formally activated, not merely because Phase 1 is current.

## Phase 2 - Deterministic routing (planned)

Task intent is untrusted input describing the requested outcome, requested mode, proposed scope, and caller-provided constraints before governance resolution. It MUST NOT grant authority. Resolution MUST produce exactly one `Project` and a non-empty deterministic set of `Domain` identifiers. Only after that resolution, `RoutingPolicy` MUST deterministically select exactly one eligible `WorktreeRole` that owns every resolved `Domain`; it MUST NOT resolve the project or discover the domain set. If no unique role covers the complete set, the task MUST be split into independently authorized tasks or denied. A free worktree with the wrong role MUST NOT be considered a valid target, and the future `TaskContract` MUST bind the same complete `Domain` set.

Customer governance MAY restrict permissions. A local `HostOverlay` MAY bind portable identities to host resources and further restrict permissions, but MUST NOT widen customer governance. Missing, malformed, ambiguous, stale, or mismatched routing state MUST deny implementation.

## Phase 3 - Git preflight and leases (planned)

Implement live inspection of repository root, branch, HEAD, dirty state, active Git operations, worktree registration, and other required runtime Git state. Expected state MUST be compared with freshly observed state immediately before authorized execution.

Implement runtime write leases as a separate control from worktree-role ownership of `Domain` identifiers. Lease liveness MUST remain independent of lifecycle phase and execution outcome. An unreleased, malformed, ambiguous, stale, or otherwise unresolved lease remains blocking after success, denial, failure, cancellation, or an indeterminate outcome. Competing writers remain denied until ownership-checked release succeeds or a separately authorized operator-resolution procedure completes. Passing a worktree-role-ownership check MUST NOT imply lease availability, and holding a lease MUST NOT imply worktree-role ownership.

Runtime Git observations are freshly read Git and filesystem facts. Runtime coordination state includes task state, lease records, lease-store synchronization, ownership records, release outcomes, and lease-store locks. Git administrative locks and lease-store locks are distinct, and neither type may be broken automatically.

The framework MUST fail closed on a mismatch and MUST NOT automatically switch or create branches, stash changes, reset, clean, restore files, fetch, pull, merge, rebase, break leases or locks, or repair Git state.

## Phase 4 - Contracts and receipts (planned)

Issue bounded `TaskContract` records only after governance resolution, host binding, initial live preflight, lease acquisition when required, and post-acquisition, pre-contract-issuance revalidation all succeed. The authorization defaults MUST be `mode: plan-only` and `allowWrite: false`; `mode: plan-only` implies `allowWrite: false`, and the contradictory pairing with `allowWrite: true` MUST be rejected.

Define pre-execution scope authorization, contract scope validation, and post-execution scope verification. Use two-phase terminalization: capture execution and verification evidence, attempt ownership-checked lease release, record `releaseOutcome`, finalize the `ExecutionReceipt` with execution, verification, release, and overall lifecycle outcomes plus unresolved coordination-state warnings, and then attempt external persistence or delivery. A receipt MUST NOT be accepted as authorization input and MUST NOT expand, renew, or replace a `TaskContract`. Generated receipts MUST remain host-local and outside portable governance.

## Phase 5 - CLI (planned)

Provide a command-line interface over the established models and deterministic control-plane operations. The CLI MUST preserve fail-closed behavior and MUST NOT introduce hidden authorization, implicit Git repair, or product-specific assumptions.

CLI arguments, output, logs, and diagnostics MUST NOT contain secrets. Interfaces MUST distinguish planning, denial, authorized execution, verification, and evidence generation.

## Phase 6 - Agent adapters (planned)

Add adapters for agent products after the core interfaces are stable. Adapters MUST translate product-specific inputs and outputs at the boundary and MUST NOT become normative policy sources. They MUST NOT grant permissions beyond authoritative structured governance and a valid `TaskContract`.

The core architecture MUST remain agent-neutral. Support for any particular agent product is future adapter work, not a core dependency.

## Cross-phase requirements

All implementation phases MUST preserve these invariants:

- Runtime Git state MUST be observed live and revalidated at the point required by the lifecycle.
- Missing, malformed, ambiguous, stale, or mismatched state MUST deny implementation.
- Worktree-role ownership of the complete `Domain` set and runtime write leases MUST remain distinct controls.
- Concrete `HostOverlay`, `TaskContract`, and `ExecutionReceipt` instances, real host paths, and runtime coordination files MUST remain outside the target worktree.
- Secrets MUST remain outside governance files, Markdown, task contracts, CLI arguments, logs, examples, and receipts.
- Generated `ExecutionReceipt` records are evidence only, MUST remain outside portable governance, and MUST NOT serve as authorization input.
- An execution outcome MUST NOT imply lease release; unresolved coordination state remains blocking until safely resolved.
