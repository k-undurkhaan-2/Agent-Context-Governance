# Agent Context Governance

Agent Context Governance is the architectural foundation for a planned agent-neutral framework that will decide whether an automated task may plan or write in a particular Git worktree. It is intended to make routing and authorization explicit, observable, and fail-closed before a future execution adapter changes a repository.

> **Current status:** Phase 0 documentation bootstrap is complete at baseline commit `79cc9d77fd48410f37645afdb429a7cd2e34a0bd`. Phase 1: Schemas and Models is current, but Phase 1 implementation has not yet begun. The repository remains pre-operational and has no Schema implementation, Python model, test, fixture, package release, normal policy engine, trusted `TaskContract` issuer, lease manager, Git inspector, CLI, adapter, enforcement mechanism, or cryptographic authorization. Phase 1 activation is not operational-governance activation; the first Schema or model artifact requires a later, separately authorized implementation task.

## Phase 1 activation boundary

[ADR 0005](docs/decisions/0005-phase-1-activation.md) activates Phase 1 without completing it. Phase 1 is limited to:

- public JSON Schema definitions under `schemas/v1alpha1/`;
- shared Schema definitions, strict object envelopes, Schema-expressible
  structural constraints, and unknown-field rejection;
- types, formats, enums, required fields, and local structural invariants;
- conspicuously synthetic positive and negative Schema fixtures;
- in-memory typed models;
- strict decoding and canonical serialization;
- Schema validation and contract tests;
- model unit tests and Schema/model conformance tests; and
- bounded static configuration/model integrity validation.

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

### Static validation boundary

Phase 1 MAY implement JSON Schema structural validation, unknown-field and API
version checks, field and object-local constraints, deterministic decoding,
canonical serialization, Schema/model conformance, closed-bundle ID and
reference integrity, and static restriction or model invariants that do not
calculate an operational result or require task intent, host bindings, Git
state, lease state, or runtime decisions.

Phase 1 MUST NOT execute task-to-`Project` matching, task `Domain` resolution,
`RoutingPolicy` evaluation, role selection, split-versus-deny decisions,
operational authorization, concrete host binding, live Git inspection, lease
coordination, trusted contract issuance or validation, or receipt generation.
Those responsibilities remain in Phases 2 through 4; the CLI and adapters
remain Phases 5 and 6.

Phase 1 excludes deterministic task routing implementation, live Git inspection, runtime write leases, `TaskContract` issuance, `ExecutionReceipt` generation, a CLI, agent adapters, operational enforcement, and cryptographic authorization.

### Logical worktree roles

- **`integration-control`** owns phase decisions, cross-worktree coordination,
  implementation sequencing, integration review, independent-audit gating,
  merge readiness, promotion of approved baselines into `main`, release
  control, and responsibility-boundary and escalation decisions. It does not
  own routine Schema or Python model implementation, Phase 2 routing, runtime
  Git or lease implementation, or CLI or adapter implementation. `main` is the
  control and integration baseline, not an ordinary implementation area.
- **`schema-contracts`** owns `schemas/v1alpha1/**`, shared definitions, strict
  envelopes, Schema-expressible constraints, unknown-field rejection, field
  constraints and local invariants, synthetic positive and negative fixtures,
  Schema validation and contract tests, and directly required Schema
  documentation. It does not own Python models, decoding, serialization,
  deterministic task resolution, routing execution, live Git, leases,
  contracts, receipts, a CLI, adapters, or operational enforcement.
- **`model-implementation`** owns typed representations of the approved Schema
  contract, strict decoding, canonical serialization, bounded model validation,
  model unit tests, Schema/model conformance tests, and permitted static
  integrity checks. It does not own Schema redefinition, task-intent or
  Project/Domain resolution, routing, role or host-binding decisions, live Git,
  leases, contracts, receipts, a CLI, adapters, or operational enforcement. A
  Schema mismatch stops affected model work and routes back to
  `schema-contracts`.

`integration-control` is a third responsibility role distinct from the two
implementation roles. `schema-contracts` and `model-implementation`
implementation tasks MUST use distinct worktrees. They MUST NOT be assigned to,
implemented in, or allowed to write through the same worktree.

These roles are portable governance concepts. Concrete worktree paths are
host-local and MUST NOT be committed. Branch creation, worktree creation or
binding, committing, merging, and pushing remain separately authorized
repository-owner administrative actions. A Codex implementation task MUST NOT
create its own branch or worktree under the current pre-operational procedure.

## The problem

An agent needs more than a filesystem path before it can safely implement a task. It needs a trustworthy answer to questions such as:

- Which single project and complete set of responsibility domains cover the requested work?
- Which worktree role owns every domain in that set?
- Does the live repository, branch, commit, and working-tree state match the task's expectations?
- Does a live or unresolved write lease already block that worktree?
- What exact actions and paths are authorized?
- Did execution remain inside that authorization boundary?

A worktree being idle or reachable is not sufficient. In particular, a free worktree with the wrong role is not a valid routing target. Missing, malformed, ambiguous, stale, or mismatched state MUST deny implementation.

## Planned framework

The planned framework will combine portable, machine-readable governance with host-local restrictions and live runtime inspection. If all required checks pass, trusted framework logic may issue or validate a narrowly scoped `TaskContract` for an execution adapter. Terminal processing will finalize an evidence-only `ExecutionReceipt` only after the lease-release outcome is known.

The core architecture MUST remain independent of any agent product. Product-specific integrations, including a future Codex integration, belong in adapters and MUST NOT define core policy semantics.

The intended control flow is:

1. Receive untrusted task intent and resolve exactly one `Project` plus a non-empty deterministic set of `Domain` identifiers.
2. After that resolution, use `RoutingPolicy` to select exactly one `WorktreeRole` that owns every resolved `Domain`; if no unique role covers the complete set, split the work into independently authorized tasks or deny it.
3. Resolve one local `HostOverlay` binding without widening portable governance.
4. Perform initial live preflight.
5. For a write task whose evaluated effective permission is explicitly `allowWrite: true`, atomically acquire the task-owned write lease.
6. Perform post-acquisition, pre-contract-issuance revalidation and clean up only a provably task-owned acquisition-result lease if issuance is denied.
7. Have trusted framework logic issue or validate a state-bound `TaskContract` that binds the same complete `Domain` set.
8. Perform post-contract, immediately-before-action revalidation and execute through an adapter within the bounded authority.
9. Perform post-execution scope and state verification and capture pre-release evidence.
10. Attempt ownership-checked lease release and record `releaseOutcome`.
11. Finalize the `ExecutionReceipt`, then attempt persistence or delivery outside portable governance.

See [Architecture](docs/architecture.md) and [Task lifecycle](docs/task-lifecycle.md) for the planned layers and denial paths.

## Core concepts

- **Task intent** is untrusted input describing the requested outcome, requested mode, proposed scope, and caller-provided constraints before governance resolution. It MUST NOT grant authority.
- **Worktree-role ownership of `Domain` identifiers** requires exactly one selected `WorktreeRole` to own every `Domain` in the task's complete non-empty set. Availability alone does not confer suitability or authority.
- **`RoutingPolicy`** acts only after one `Project` and the complete `Domain` set are resolved; it deterministically selects one eligible `WorktreeRole` and does not resolve the project or discover domains.
- **`TaskContract`** is the planned, bounded authorization artifact for one task. Possession is insufficient: trusted framework logic must issue it or validate its trusted provenance and current preconditions. It MUST NOT broaden its authoritative inputs.
- **Live preflight** observes repository root, worktree registration, branch, `HEAD`, dirty state, active Git operations, role, and relevant runtime state at decision time. Runtime Git state MUST always be observed live.
- **Runtime write lease** is a concurrency control distinct from worktree-role ownership. Its live, released, or unresolved state is independent of task phase and execution outcome.
- **Scope controls** are pre-execution scope authorization, contract scope validation, and post-execution scope verification.
- **`ExecutionReceipt`** is host-local runtime evidence about an attempted execution. It can never serve as authorization input or portable governance.

Worktree-role ownership of `Domain` identifiers answers whether a worktree is the right kind of target. A runtime write lease answers whether the current task has atomically acquired and still owns that target's exclusive writer slot. Both controls MUST pass for write execution, but neither is sufficient authorization by itself. An unreleased, malformed, ambiguous, stale, or otherwise unresolved lease remains blocking regardless of an execution outcome; later writers remain denied until ownership-checked release succeeds or a separately authorized operator-resolution procedure completes.

## Authority and defaults

Machine-readable structured governance configuration will be authoritative. Markdown MAY explain, summarize, or mirror policy, but it cannot independently grant authority. In particular, [AGENTS.md](AGENTS.md) is an explanatory, adapter-facing entry document. It is not an execution adapter, policy source, `TaskContract`, or authorization mechanism.

The default authorization is:

```yaml
mode: plan-only
allowWrite: false
```

Customer governance MAY restrict permissions. A local `HostOverlay` MAY further restrict those permissions or bind portable identifiers to local resources, but it MUST NOT widen customer governance. Real host paths, runtime state, leases, and locks MUST remain outside this repository. Secrets MUST remain outside governance files, Markdown, `TaskContract` records, CLI arguments, logs, examples, and `ExecutionReceipt` records.

`mode: plan-only` implies `allowWrite: false`. The combination of `mode: plan-only` and `allowWrite: true` is invalid and MUST be rejected. Future governed adapter execution, including plan-only execution, requires a valid bounded `TaskContract`.

Terminal processing MUST attempt to record a sanitized `ExecutionReceipt` for every issued-contract execution attempt. Pre-contract denial receipts MAY remain policy-optional. Finalization occurs after release outcome is known and includes execution, verification, release, and overall lifecycle outcomes plus unresolved coordination-state warnings. Receipt persistence or delivery failure MUST be reported, MUST NOT grant authority or hide unresolved lease state, and MUST NOT indefinitely retain an otherwise releasable lease.

The initial public configuration API is `contextctl.dev/v1alpha1`. Phase 1 schema definitions for all object kinds will live under [`schemas/v1alpha1/`](schemas/README.md). Concrete `Project`, `Domain`, `WorktreeRole`, and `RoutingPolicy` instances are portable customer governance; concrete `HostOverlay` instances are host-local input; and concrete `TaskContract` and `ExecutionReceipt` instances are runtime artifacts. Concrete host-local and runtime instances MUST remain outside the target worktree, and generated receipts MUST remain outside portable governance. Public configuration API versions are independent of product and package releases, which will use Semantic Versioning and are expected to begin later at `0.1.0`. Phase 1 activation itself creates no schema, model, test, fixture, package, or configuration instance.

## Fail-closed operation

Implementation MUST be denied when required state is missing, malformed, ambiguous, stale, or mismatched. The planned framework MUST NOT automatically switch or create branches; stash, reset, clean, or restore files; fetch, pull, merge, or rebase; break leases or locks; or repair Git state. A mismatch is a stop condition for separately authorized maintenance followed by fresh preflight.

The detailed planned checks are documented in [Worktree guard](WORKTREE_GUARD.md). The trust model and cooperative-enforcement limitation are documented in [Security](SECURITY.md).

## Repository map

- [Project context](PROJECT_CONTEXT.md) defines project identity, users, vocabulary, boundaries, and current status.
- [Roadmap](ROADMAP.md) separates the completed documentation bootstrap from the current and future implementation phases.
- [`docs/`](docs/architecture.md) records architecture, configuration, lifecycle, and decisions.
- [`schemas/`](schemas/README.md) is reserved for future public configuration schemas.
- [`src/contextctl/`](src/contextctl/README.md) describes planned package boundaries without implementing them.
- [`tests/`](tests/README.md) describes the future validation strategy.
- [`examples/`](examples/README.md) defines requirements for sanitized examples.

## Current implementation boundary

The repository remains pre-operational. Phase 1 does not provide routing, authorization, Git mutation, concurrency locking, contract issuance, receipt generation, CLI or adapter behavior, operational enforcement, or cryptographic authorization. It also does not select a final software license; see [License decision](LICENSE-DECISION.md).
