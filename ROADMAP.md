# Roadmap

## Status

Agent Context Governance is in **Phase 0: documentation bootstrap**. Phase 0 is the only current phase. Every later phase in this document is planned work, not implemented behavior or a release commitment.

Advancing to another phase MUST be an explicit project decision. A phase name or description MUST NOT be treated as evidence that its controls exist, are complete, or are safe to rely on.

Product and package releases will use Semantic Versioning, beginning later with `0.1.0`. Public configuration APIs are versioned independently. The planned initial configuration API is `contextctl.dev/v1alpha1`; its future schema files will live under `schemas/v1alpha1/`.

## Phase 0 - Documentation bootstrap (current)

Phase 0 establishes project identity, scope, vocabulary, architectural principles, trust boundaries, configuration authority, worktree responsibilities, task lifecycle expectations, and directory responsibilities.

This phase MUST remain documentation-only. It does not provide a working CLI, schemas, policy engine, router, Git inspector, lease manager, contract issuer, execution adapter, or receipt generator. Documentation MAY describe planned controls, but it MUST NOT claim that those controls are operational.

Phase 0 is complete only when the bootstrap documents are mutually consistent and clearly distinguish normative structured governance planned for later phases from explanatory Markdown.

## Phase 1 - Schemas and models (planned)

Define strict schemas and in-memory models for all kinds in the public configuration API. Schema definitions for `Project`, `Domain`, `WorktreeRole`, `HostOverlay`, `RoutingPolicy`, `TaskContract`, and `ExecutionReceipt` MAY live under `schemas/v1alpha1/`, but schema placement does not make every concrete instance portable. Concrete `Project`, `Domain`, `WorktreeRole`, and `RoutingPolicy` instances are portable customer governance; concrete `HostOverlay` instances are host-local input; and concrete `TaskContract` and `ExecutionReceipt` instances are runtime artifacts. Host-local and runtime instances MUST remain outside the target worktree, and generated receipts MUST never become portable governance.

Machine-readable structured governance configuration MUST be authoritative. Validation MUST reject unknown fields and MUST include semantic checks that cannot be expressed by JSON Schema alone. Markdown MAY explain or mirror policy, but MUST NOT independently grant authority. Package versions and configuration API versions MUST remain independent.

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
