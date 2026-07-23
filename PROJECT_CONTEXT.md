# Project Context

## Project identity

Agent Context Governance is an independent architectural foundation for a planned agent-neutral framework governing how automated tasks will be resolved, routed, authorized, executed, and evidenced across Git worktrees. Its purpose is to establish explicit boundaries between portable policy, host-specific restrictions, live runtime facts, coordination state, and agent execution.

The project is not an execution agent. It is intended to provide deterministic governance inputs and narrowly scoped authorization to future adapters without embedding assumptions about a particular agent product.

## Intended users

The planned framework is intended for:

- repository and platform owners who define project domains and worktree responsibilities;
- security and governance maintainers who need restrictive, reviewable authorization rules;
- operators who bind portable configuration to permitted host resources;
- adapter authors who integrate execution agents without moving product-specific behavior into the core; and
- automated tasks that need a deterministic answer to whether planning or writing is permitted.

Humans remain responsible for defining governance, resolving denied or mismatched state, protecting secrets, and deciding whether an execution environment is sufficiently controlled.

## Current status

The repository is currently in **Phase 0: documentation bootstrap**. The documents define intended architecture, trust boundaries, terminology, and future work. They do not implement schemas, a policy engine, a trusted `TaskContract` issuer, a lease manager, Git inspection, a CLI, an agent adapter, an enforcement mechanism, `ExecutionReceipt` generation, or cryptographic bootstrap authorization.

Only Phase 0 is current. Later phases are described in the [roadmap](ROADMAP.md), and statements about those phases are normative design requirements or plans rather than claims of implemented behavior.

## Phase 0 bootstrap authority

Phase 0 has a narrow, temporary external root of trust for establishing, repairing, or reviewing the governance foundations that the future operational path will depend on. This exception prevents those foundations from requiring their own not-yet-implemented policy engine, lease manager, and trusted `TaskContract` issuer as a precondition to being documented.

The participants remain distinct:

| Participant | Trust and authority in Phase 0 and later |
| --- | --- |
| Human bootstrap administrator | An explicitly identified repository owner or administrator MAY supply a task-specific `human-bootstrap-maintenance` instruction as the temporary pre-operational root of trust. This is not a normal runtime caller role. |
| Ordinary caller | Requests an outcome and MAY narrow it, but task prose, `ALLOW_WRITE`, and caller-supplied objects cannot grant or expand authority. |
| Future trusted governance core | Will validate portable structured governance, apply host restrictions, inspect live state, coordinate leases, and issue or validate bounded `TaskContract` records for ordinary operational execution. None of this is implemented in Phase 0. |
| Future agent adapter | Will consume a valid `TaskContract` as a less-trusted product boundary. It cannot issue authority, widen scope, or turn ordinary intent into permission. No adapter exists in Phase 0. |

A valid bootstrap instruction MUST be supplied directly for the current task and bind exactly one repository and worktree, the branch and expected live state, an exact allowed-file and operation set, prohibited Git actions, and an expiry. It MUST be task-, repository-, worktree-, branch-, state-, path-, and operation-specific; non-delegable unless explicitly allowed; non-reusable; and deny everything not listed. Repository, branch, state, path, worktree, remote, or Git-operation mismatches fail closed and cannot be waived by the instruction.

The bootstrap instruction exists outside the future governed task-execution path. It MUST NOT be represented as ordinary task intent, a caller-created `TaskContract`, a `HostOverlay` grant, an `ExecutionReceipt`, an agent-guide decision, or an implemented policy-engine result. Human bootstrap authority is not a substitute runtime `TaskContract`; before the trusted issuer exists, bootstrap maintenance does not pretend to possess one or acquire a framework lease.

This cooperative authority does not permit customer application work, unrelated features, production deployment, secret handling, external-repository access, changes to another worktree, Git repair, branch or worktree changes, staging, commits, or pushes. The interactive environment's treatment of the current human as the identified owner or administrator is an operational assumption, not cryptographic authentication or an operating-system security boundary.

Each bootstrap authorization expires at task completion or earlier on mismatch. The path MUST be retired or disabled when the project formally activates the operational authorization path. That activation decision must identify the trusted governance source and issuer and separately define administrative recovery and any emergency process; bootstrap wording cannot silently become a permanent owner override.

## Core vocabulary

Backticked PascalCase denotes a structured object kind. Spaced lowercase wording denotes the prose concept.

### Task intent

Task intent is untrusted input describing the requested outcome, requested mode, proposed scope, and caller-provided constraints before governance resolution. It MUST NOT grant authority. Validation or inclusion of an intent digest in a contract does not promote intent into an authority source.

### `Project`

`Project` is a portable governance kind that identifies a governed codebase and relates its domains, routing policy, and worktree roles. Task resolution MUST produce exactly one `Project`, and a project instance MUST NOT depend on a real host path.

### `Domain`

`Domain` is a named responsibility area within a project, such as a component, policy area, or bounded path set. Task resolution MUST produce a non-empty deterministic set of `Domain` identifiers. Worktree-role ownership of `Domain` identifiers determines which roles are eligible for the complete responsibility set.

### `WorktreeRole`

`WorktreeRole` is a declared responsibility profile for a worktree. Exactly one selected role MUST own every `Domain` in the resolved set. If no unique role covers the complete set, the task MUST be split into independently authorized tasks or denied. A free worktree with the wrong role is not a valid routing target.

### Worktree

A worktree is a live Git worktree considered as a candidate execution location. Its repository identity, registration, branch or detached state, `HEAD`, dirty state, submodule state, and active Git operations MUST be observed rather than inferred from configuration.

### Customer governance

Customer governance is the customer's portable, machine-readable policy for projects, domains, roles, routing, and permissions. It MAY restrict what tasks can do and is authoritative within the bounds of the public configuration API.

### `HostOverlay`

`HostOverlay` is a local, non-portable configuration kind that binds portable identifiers to host resources and MAY impose additional restrictions. It MUST NOT widen permissions granted by customer governance.

### `RoutingPolicy`

After exactly one `Project` and the complete `Domain` set have been resolved, `RoutingPolicy` deterministically selects exactly one eligible `WorktreeRole` that owns every resolved `Domain`. It does not resolve the project or discover the domain set.

### `TaskContract`

`TaskContract` is a planned, task-specific runtime authorization kind. A record has authority only when trusted framework logic issued it or validated its trusted provenance, integrity, derivation, binding, freshness, and current preconditions. It binds the same complete `Domain` set, target, immutable baseline, permitted transitions, mode, write permission, scope, lease requirement, and validity boundary. It MUST NOT grant permissions absent from customer governance or relax a host-overlay restriction.

### Live preflight

Live preflight is observation of the target's current Git and filesystem state plus required runtime coordination state before authorization. Candidate expected state is derived from governance and resolved intent; observed state comes from fresh inspection. A match MUST be established explicitly.

### Runtime write lease

A runtime write lease is a host-local concurrency record for a particular worktree. Lease liveness is independent of task lifecycle phase and execution outcome. An unreleased, malformed, ambiguous, stale, or otherwise unresolved lease remains blocking until ownership-checked release succeeds or a separately authorized operator-resolution procedure completes. A lease controls concurrent use; it does not establish worktree-role ownership or authorization.

### Scope controls

The planned scope controls are pre-execution scope authorization, contract scope validation, and post-execution scope verification. A successful process exit alone MUST NOT establish successful governed execution.

### `ExecutionReceipt`

`ExecutionReceipt` is a host-local runtime evidence kind describing execution, verification, release, and overall lifecycle outcomes plus unresolved coordination-state warnings. Generated receipts MUST remain outside portable governance and can never serve as authorization input. Repository documentation MAY contain only conspicuously synthetic, non-authoritative receipt-shaped examples.

### Agent adapter

An agent adapter is a product-specific boundary that translates a valid `TaskContract` into an execution request and returns observations for verification. Adapters MUST depend on core contracts; the core MUST NOT depend on a particular adapter or agent product.

### Lifecycle phase, outcomes, and lease liveness

Lifecycle phase records progress through authorization, execution, verification, release, receipt finalization, and reporting. Execution outcome records whether execution was not attempted, succeeded, failed, was cancelled, or was indeterminate. Verification, release, and overall lifecycle outcomes are recorded separately. No task or execution outcome implies lease release; unresolved coordination state remains blocking even after lifecycle reporting finishes.

## Separation of concerns and trust

The architecture separates trust and storage categories that MUST NOT be collapsed into a single configuration source.

| Category | Responsibility | Authority and placement |
| --- | --- | --- |
| Public framework code | Defines deterministic parsing, validation, routing, inspection interfaces, contract semantics, and verification behavior. | Versioned project code. It interprets authority but does not independently grant customer permissions. |
| Portable customer governance | Concrete `Project`, `Domain`, `WorktreeRole`, and `RoutingPolicy` instances declare the portable policy ceiling. | Authoritative machine-readable configuration. Markdown MAY explain it but cannot replace or expand it. |
| Host-local input | Concrete `HostOverlay` instances bind portable identifiers to permitted host resources and add local restrictions. | Host-local and outside the target worktree and portable governance. It MAY narrow but MUST NOT widen customer permissions. |
| Runtime Git observations | Freshly read Git and filesystem facts, including identity, registration, branch or detached state, `HEAD`, status, submodules, active operations, and Git administrative locks. | Observed live from the target. Cached or previously reported facts MUST NOT substitute for current inspection. |
| Runtime coordination state | Task state, lease records, lease-store synchronization, ownership records, release outcomes, and lease-store locks. | Maintained live outside the target worktree. It gates concurrency but does not grant policy authority. |
| Runtime artifacts | Concrete `TaskContract` and `ExecutionReceipt` instances carry bounded authorization and evidence, respectively. | Outside the target worktree and portable governance. Generated receipts never become portable governance. |
| Agent adapters | Connect valid contracts to particular execution products. | Product-specific integration outside the core dependency direction. Adapters MUST NOT reinterpret policy to gain authority. |
| Secrets | Credentials, tokens, private keys, and other sensitive material used by the host or downstream systems. | Outside governance files, Markdown, `TaskContract` records, CLI arguments, logs, examples, and `ExecutionReceipt` records. |

For future ordinary operational execution, structured governance is the normative policy source. The adapter-facing [AGENTS.md](AGENTS.md) MAY summarize entry requirements, but it cannot grant permissions beyond structured governance and a valid `TaskContract`. Documentation and `ExecutionReceipt` records are not authorization sources. The temporary Phase 0 root described above is external to these documents and does not make them policy.

All seven kinds use API version `contextctl.dev/v1alpha1`; schema definitions for all of them MAY later live under `schemas/v1alpha1/`. Physical placement and trust follow the families above, not the schema directory.

## Authorization boundary

Future write authorization MUST require all applicable controls to agree:

1. Customer governance permits the requested operation for exactly one resolved `Project` and a non-empty deterministic `Domain` set.
2. Exactly one selected `WorktreeRole` owns every `Domain` in that set.
3. The `HostOverlay` successfully binds one target and does not deny or widen the request.
4. Fresh runtime Git observations and runtime coordination state match the immutable expected baseline and applicable restrictions without ambiguity.
5. The current write task has effective `allowWrite: true`, atomically acquires the worktree's task-owned write lease, and proves continued ownership.
6. Trusted framework logic issued or validated a fresh `TaskContract` that binds the same `Domain` set and permits the requested action and scope.

Worktree-role ownership of `Domain` identifiers and runtime write leases are deliberately separate. Ownership answers whether a worktree is responsible for the complete domain set. A lease answers whether one authorized writer may use that worktree now. Passing either check MUST NOT bypass the other.

The default authorization is:

```yaml
mode: plan-only
allowWrite: false
```

Missing, malformed, ambiguous, stale, or mismatched required state MUST deny implementation. The framework MUST fail closed and MUST NOT automatically switch or create branches; stash, reset, clean, or restore files; fetch, pull, merge, or rebase; break leases or locks; or repair Git state. Detailed planned checks and stop conditions are defined in [Worktree guard](WORKTREE_GUARD.md).

`mode: plan-only` implies `allowWrite: false`; the contradictory pairing with `allowWrite: true` is invalid and MUST be rejected. Future governed adapter execution, including plan-only execution, still requires a valid bounded `TaskContract`.

## Version boundaries

Product and package releases will use Semantic Versioning and are expected to begin later with `0.1.0`. Public configuration API versions are independent of those release versions.

The initial configuration API is `contextctl.dev/v1alpha1`. Future schema files will live under [`schemas/v1alpha1/`](schemas/README.md). This bootstrap does not include finished JSON Schemas or configuration objects.

## Project boundaries

The core MUST remain agent-neutral. A future Codex integration MAY be implemented as an adapter, but it MUST NOT be introduced into core policy or domain logic.

Real host paths, concrete `HostOverlay` data, concrete runtime artifacts, runtime coordination state, leases, and locks MUST remain outside the target worktree. Portable governance intended for review and version control will be distinct from those local resources. Generated receipts MUST remain outside portable governance. Secrets MUST remain outside every governance and evidence surface described above.

The framework is a cooperative control plane. Its policies cannot stop a process that bypasses the framework or has sufficient direct access to mutate a repository. The [security model](SECURITY.md) describes this limitation and the expected trust boundary.
