# Agent Context Governance

Agent Context Governance is the architectural foundation for a planned agent-neutral framework that will decide whether an automated task may plan or write in a particular Git worktree. It is intended to make routing and authorization explicit, observable, and fail-closed before a future execution adapter changes a repository.

> **Current status:** This repository is in Phase 0, documentation bootstrap. It contains architectural intent and governance requirements only. A working CLI, policy engine, configuration schema, runtime inspector, lease manager, and agent adapter do not yet exist.

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

The initial public configuration API is `contextctl.dev/v1alpha1`. Future schema definitions for all object kinds MAY live under [`schemas/v1alpha1/`](schemas/README.md). Concrete `Project`, `Domain`, `WorktreeRole`, and `RoutingPolicy` instances are portable customer governance; concrete `HostOverlay` instances are host-local input; and concrete `TaskContract` and `ExecutionReceipt` instances are runtime artifacts. Concrete host-local and runtime instances MUST remain outside the target worktree, and generated receipts MUST remain outside portable governance. Public configuration API versions are independent of product and package releases, which will use Semantic Versioning and are expected to begin later at `0.1.0`. No schema files or releasable package exist in this phase.

## Fail-closed operation

Implementation MUST be denied when required state is missing, malformed, ambiguous, stale, or mismatched. The planned framework MUST NOT automatically switch or create branches; stash, reset, clean, or restore files; fetch, pull, merge, or rebase; break leases or locks; or repair Git state. A mismatch is a stop condition for separately authorized maintenance followed by fresh preflight.

The detailed planned checks are documented in [Worktree guard](WORKTREE_GUARD.md). The trust model and cooperative-enforcement limitation are documented in [Security](SECURITY.md).

## Repository map

- [Project context](PROJECT_CONTEXT.md) defines project identity, users, vocabulary, boundaries, and current status.
- [Roadmap](ROADMAP.md) separates this documentation bootstrap from future implementation phases.
- [`docs/`](docs/architecture.md) records architecture, configuration, lifecycle, and decisions.
- [`schemas/`](schemas/README.md) is reserved for future public configuration schemas.
- [`src/contextctl/`](src/contextctl/README.md) describes planned package boundaries without implementing them.
- [`tests/`](tests/README.md) describes the future validation strategy.
- [`examples/`](examples/README.md) defines requirements for sanitized examples.

## Non-goals for Phase 0

This phase MUST NOT implement operational framework behavior. It does not provide routing, authorization, Git mutation, concurrency locking, contract issuance, receipt generation, or enforcement. It also does not select a final software license; see [License decision](LICENSE-DECISION.md).
