# ADR 0002: Configuration authority

- Status: Accepted

## Context

Governance information will appear in several forms: portable customer configuration, explanatory Markdown, local host bindings, runtime observations, derived task contracts, adapter instructions, and execution evidence. Without an explicit authority order, a convenient but stale or unaudited source could accidentally grant permission.

Phase 0 documentation bootstrap is complete at baseline commit `79cc9d77fd48410f37645afdb429a7cd2e34a0bd`, and Phase 1: Schemas and Models is current. Phase 1 implementation has not yet begun. The repository remains pre-operational and has no Schema implementation, typed models, tests, fixtures, package release, policy engine, trusted `TaskContract` issuer, lease manager, Git inspector, CLI, adapter, enforcement mechanism, or cryptographic authorization. Phase 1 activation is not operational-governance activation, and the first Schema or model artifact requires a later, separately authorized implementation task. Requiring those future mechanisms to authorize implementation of their own governance core would create a bootstrap deadlock.

## Decision

### Future operational authority

Backticked PascalCase denotes a structured object kind. Spaced lowercase wording denotes the prose concept.

Machine-readable structured governance configuration MUST be the normative policy source for ordinary operational execution. Markdown MAY explain, summarize, or mirror policy, but Markdown MUST NOT independently grant authority. `AGENTS.md` is an explanatory, adapter-facing entry document. It is not an execution adapter, policy source, `TaskContract`, or authorization mechanism.

Task intent is untrusted input describing the requested outcome, requested mode, proposed scope, and caller-provided constraints before governance resolution. It MUST NOT grant authority. Normalization, resolution, validation, or inclusion of a task-intent digest in a contract does not promote intent into an authority source.

Authority and restriction flow MUST follow these rules:

1. Customer governance defines the portable maximum authority for `Project`, `Domain`, `WorktreeRole`, `RoutingPolicy`, and task constraints.
2. A local `HostOverlay` binds permitted logical resources to the current host and MAY further restrict customer governance. It MUST remain outside the repository.
3. A host overlay MUST NOT widen, replace, or reinterpret customer authorization. It MAY deny or narrow a customer-authorized operation; an attempted widening MUST be rejected.
4. Live runtime and Git observations determine whether expected state currently matches reality. Runtime Git state MUST always be observed live.
5. Task resolution MUST produce exactly one `Project` and a non-empty deterministic set of `Domain` identifiers; `RoutingPolicy` then selects exactly one `WorktreeRole` that owns every resolved `Domain`.
6. Trusted framework logic MAY issue or validate a bounded `TaskContract` only from valid structured governance, permitted host restrictions, successful current observations, and required lease state. The contract MUST bind the same complete `Domain` set.
7. Execution adapters MAY consume a valid contract but MUST NOT extend it.
8. An `ExecutionReceipt` is evidence only and MUST NOT be accepted as authorization input.

Effective permissions MUST be the intersection of customer governance and valid `HostOverlay` restrictions. An attempted widening, or any inconsistency that cannot be represented as a valid narrowing restriction, MUST deny implementation. The framework MUST NOT use Markdown, adapter behavior, previous receipts, or caller intent to repair an absent structured grant. Missing, malformed, ambiguous, stale, or mismatched state MUST deny implementation.

Default authorization MUST be:

```yaml
mode: plan-only
allowWrite: false
```

`mode: plan-only` implies `allowWrite: false`. The combination of `mode: plan-only` and `allowWrite: true` is invalid and MUST be rejected. Future governed adapter execution, including plan-only execution, requires a valid bounded `TaskContract`.

A `TaskContract` has authority only when trusted framework logic issued it or validated its trusted issuer, integrity, derivation, task and target binding, freshness, and current policy, runtime, and lease preconditions. A caller-, adapter-, or task-supplied object claiming to be a `TaskContract` is untrusted input and MUST NOT grant or expand authority. A digest alone detects mutation but does not prove trusted issuance. Phase 0 selected no final signing mechanism, Phase 1 activation does not select one, and pre-operational bootstrap authority is not a substitute runtime `TaskContract`.

Under `contextctl.dev/v1alpha1`, concrete `Project`, `Domain`, `WorktreeRole`, and `RoutingPolicy` instances are portable customer governance; concrete `HostOverlay` instances are host-local input; and concrete `TaskContract` and `ExecutionReceipt` instances are runtime artifacts. Schema definitions for every kind MAY later live under `schemas/v1alpha1/`, but concrete host-local and runtime instances MUST remain outside the target worktree. Generated receipts MUST remain outside portable governance; repository documentation MAY contain only conspicuously synthetic, non-authoritative receipt-shaped examples.

Write authority MUST be explicit. A runtime write lease is necessary for an authorized write task, but a lease MUST NOT itself grant permission or establish worktree-role ownership of `Domain` identifiers.

Secrets MUST remain outside governance files, Markdown, `TaskContract` records, command-line arguments, logs, examples, and receipts. Real host paths and runtime state, lock, and lease files MUST remain outside the target worktree.

### No automatic repair

The framework MUST NOT automatically switch branches, create branches, stash, reset, clean, restore, fetch, pull, merge, rebase, break leases, break locks, or repair Git state. Remediation requires separately authorized maintenance followed by a fresh preflight. This rule does not weaken or expand the separately documented temporary pre-operational bootstrap path.

### Pre-operational bootstrap authority

While the repository is pre-operational and the normal operational authorization path does not yet exist, the explicitly identified repository owner MAY supply narrow, out-of-band pre-operational `human-bootstrap-maintenance` authority to implement, repair, or review this governance framework's core. The instruction is a temporary external root of trust supplied directly for the current task. It remains available for bounded Phase 1 governance-core implementation because the trusted operational authority and issuer have not yet been implemented. Phase 1 activation is not operational-governance activation.

The bootstrap instruction MUST identify exactly one repository and one worktree; bind the branch and exact `HEAD` or unborn expectation; enumerate the complete expected live file and Git status, exact allowed files, and permitted operations; state prohibited Git actions; and define its task-lifecycle or time limit. It MUST be task-, repository-, worktree-, branch-, state-, path-, and operation-specific; non-delegable unless delegation is explicit; non-reusable; and default to denial for everything not listed. Repository identity and live Git state MUST be verified and revalidated immediately before writing. Root, branch, state, path, worktree, remote, active-operation, lock, or Git-operation mismatches revoke the authorization and fail closed; the bootstrap instruction cannot waive those checks.

This external root MUST NOT be represented as ordinary task intent, a caller-created `TaskContract`, a `HostOverlay` permission, an `ExecutionReceipt`, an agent-facing guide's decision, or an implemented policy-engine result. `ALLOW_WRITE`, caller assertions, observed convenience, adapters, and receipts remain untrusted and cannot create or expand it. Before the trusted issuer exists, a bootstrap-maintenance task does not pretend to possess a `TaskContract`, lease, or operational receipt.

Bootstrap authority MUST NOT authorize customer application work, unrelated feature work, another repository, another worktree unless separately and explicitly bound, production deployment, secret handling, automatic Git repair, branch switching or creation, worktree creation, stash, reset, clean, restore, fetch, pull, merge, rebase, lease or lock breaking, staging, committing, or pushing. Branch creation, worktree creation or binding, committing, merging, and pushing remain separately authorized repository-owner administrative actions. A Codex implementation task MUST NOT create its own branch or worktree under the current pre-operational procedure. This decision does not create an unlimited owner override.

Pre-operational authentication is cooperative: the interactive development environment treats the current operator as the identified repository owner. It is not cryptographic identity proof, operating-system access control, a sandbox, or protection against a process that bypasses the framework.

### Retirement

The pre-operational bootstrap path MUST be retired or disabled when the project formally activates its operational authorization path. That future activation decision MUST identify the activation milestone, trusted governance source, trusted issuer, administrative recovery path, and whether a separately governed emergency or break-glass process exists. Phase 1 activation is not that milestone. Bootstrap authority MUST NOT silently persist as a permanent bypass after operational activation.

## Consequences

- Human-readable guidance can improve discovery without becoming an alternative policy channel.
- Pre-operational bootstrap authority resolves the authorization deadlock during governance-core implementation without treating ordinary caller intent as trusted.
- Bootstrap tasks incur strict live-state, file-scope, operation-scope, and lifecycle checks and may reduce convenience or availability when any observation is uncertain.
- Cooperative operator identification creates a residual impersonation or misidentification risk until a separately designed authentication mechanism exists.
- An ordinary operational task is denied when authoritative structured configuration is unavailable, even if prose appears to permit it.
- Host administrators can reduce local exposure without silently expanding customer policy.
- Authorization decisions require current runtime inspection rather than cached evidence.
- Receipts support audit and diagnosis but cannot create precedent or authorize retries.
- Phase 1 implementations MAY validate document structure and closed-bundle
  cross-object static integrity; later Phase 2–4 implementations MUST perform
  operational resolution, runtime, and authorization validation before issuing
  a contract.
- This ADR documents authority boundaries only; it does not claim that schemas, policy evaluation, contract issuance, leases, inspection, adapters, enforcement, or cryptographic authorization now exist.

## Alternatives not selected

### Markdown as policy

Using Markdown as a grant source was not selected because prose is difficult to validate strictly and can diverge across entry documents.

### Unlimited owner override

Keeping a permanent or scope-free owner bypass was not selected because it would defeat deterministic policy, state binding, and least authority. The accepted bootstrap root is temporary and narrowly bounded.

### Requiring the future issuer during pre-operational implementation

Requiring an already operational policy engine and trusted `TaskContract` issuer was not selected because those components do not exist and cannot authorize the act of implementing their own governance foundation.

### Host configuration as an override in either direction

Allowing a host overlay to widen customer governance was not selected because machine-local configuration must not exceed the customer's portable authorization boundary.

### Receipts as reusable authorization

Treating a previous successful execution as authority was not selected because evidence describes past state and may be stale, mismatched, or outside the present task's scope.

## Related decision

- [ADR 0005: Activate Phase 1 schemas and models](0005-phase-1-activation.md)
