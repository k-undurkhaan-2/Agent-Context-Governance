# Security

## Current status

This repository is currently an architectural documentation bootstrap. It does not yet contain schemas, an operational policy engine, Git guard, lease manager, trusted `TaskContract` issuer, Git inspector, CLI, execution adapter, enforcement mechanism, cryptographic bootstrap authorization, or security boundary. Planned controls described here MUST NOT be relied on as implemented protections.

For future ordinary governed execution, the authorization defaults are `mode: plan-only` and `allowWrite: false`. `mode: plan-only` implies `allowWrite: false`; the contradictory pairing with `allowWrite: true` is invalid and MUST be rejected. Missing, malformed, ambiguous, stale, or mismatched governance or runtime state MUST deny implementation. The temporary Phase 0 bootstrap authority described below is external to that not-yet-implemented path and is limited to governance-foundation maintenance.

## Phase 0 bootstrap authority and authentication

An instruction supplied directly for the current task by an explicitly identified repository owner or bootstrap administrator MAY serve as a temporary external root of trust under authority class `human-bootstrap-maintenance`. It is eligible only while the repository is explicitly Phase 0 or pre-operational, the normal governance core is absent, and the task establishes, repairs, or reviews governance foundations. It is not ordinary caller intent, a caller-created `TaskContract`, a `HostOverlay` permission, an `ExecutionReceipt`, an agent-facing document's decision, or an implemented policy-engine decision.

Authentication in Phase 0 is cooperative. The interactive development environment assumes that the current human operator is the identified repository owner or authorized administrator. There is no cryptographic proof attached to the bootstrap instruction, and the framework provides no operating-system access control or sandbox that establishes that identity. Misidentifying the operator could let an unauthorized person present an apparently valid bootstrap instruction.

That risk MUST be reduced by requiring every authorization to be task-, repository-, worktree-, branch-, live-state-, path-, operation-, and time- or lifecycle-specific; directly supplied for the current task; non-delegable unless explicit; non-reusable; and denied for anything not enumerated. Live preflight MUST verify the exact repository, one worktree, branch, `HEAD`, full status and file inventory, empty index, allowed-file set, remote when bound, and absence of active Git operations or locks. Any mismatch revokes the authority and MUST stop the task without repair or scope widening.

Bootstrap authority MUST NOT authorize customer application work, unrelated features, production deployment, secret handling, external-repository access, another worktree, automatic Git repair, branch or worktree changes, stash, reset, clean, restore, fetch, pull, merge, rebase, lease or lock breaking, staging, committing, or pushing. Human bootstrap authority is not a substitute runtime `TaskContract`; before the trusted issuer exists, a bootstrap task does not fabricate one, a lease, or a cryptographic authorization artifact.

These restrictions reduce accidental or opportunistic misuse by cooperating participants, but they cannot stop a user, agent, plugin, script, or process that bypasses the framework or directly mutates the repository. Phase 0 bootstrap authority is not containment.

The bootstrap path MUST be retired or disabled when the project formally activates its operational authorization path. The activation decision must identify the trusted governance source, trusted issuer, administrative recovery process, and whether a separately governed emergency process exists. Phase 0 authority MUST NOT persist as an implicit or unlimited owner override.

## Trust model

The planned framework separates policy, host binding, runtime observations, runtime coordination, authorization, execution, and evidence:

- For future ordinary operational execution, concrete `Project`, `Domain`, `WorktreeRole`, and `RoutingPolicy` instances are authoritative portable customer governance and MAY restrict permissions. Explanatory Markdown and agent-facing entry files MUST NOT independently grant authority. The temporary bootstrap root is a directly supplied external instruction, not authority created by those files.
- A concrete `HostOverlay` is host-local input that binds portable identities to host resources. It MAY further restrict customer governance, but MUST NOT widen it.
- Runtime Git observations are freshly read repository and filesystem facts, including identity, registration, branch or detached state, `HEAD`, tracked, untracked, ignored and submodule state, active Git operations, and Git administrative locks. Cached or previously reported facts MUST NOT substitute for observation at the required checkpoint.
- Runtime coordination state includes task state, lease records, lease-store synchronization, ownership records, release outcomes, and lease-store locks. Git administrative locks and lease-store locks are distinct. This state gates coordination but does not grant policy authority.
- Worktree-role ownership requires exactly one selected `WorktreeRole` to own every `Domain` in the resolved non-empty deterministic set. Runtime write leases coordinate writers. These are separate controls, and both MUST pass when both are required.
- A `TaskContract` has authority only when trusted framework logic issued it or validated its trusted issuer, integrity, derivation, task and target binding, freshness, and current policy, runtime, and lease preconditions. A caller-, adapter-, or task-supplied object claiming to be a `TaskContract` is untrusted input and MUST NOT grant or expand authority.
- A digest alone detects mutation but does not prove trusted issuance. Phase 0 does not select a final signing mechanism, and human bootstrap authority is not a substitute runtime `TaskContract`.
- Execution adapters are less trusted than the control plane. They MUST stay within the contract's scope and MUST submit their results to verification.
- Generated `ExecutionReceipt` records are host-local runtime evidence. They MUST remain outside portable governance and MUST NOT be used as authorization input, permission, proof that current state is still valid, or a substitute for live inspection.

All seven kinds use planned API version `contextctl.dev/v1alpha1`, and schema definitions for them MAY later live under `schemas/v1alpha1/`. Concrete `HostOverlay`, `TaskContract`, and `ExecutionReceipt` instances, real host paths, and runtime coordination state MUST remain outside the target worktree. Schema placement does not make those instances portable.

## State-bound `TaskContract` requirements

A future `TaskContract` MUST bind the object API version; contract version; unique contract identity; unique task identity; resolved `Project` identity; repository identity; selected target worktree identity or logical binding; complete non-empty `Domain` set; required `WorktreeRole`; trusted issuer or validated provenance information; policy and configuration digests; task-intent digest or equivalent immutable binding; requested and effective mode; explicit `allowWrite`; authorized path scope; prohibited path scope where represented; expected baseline branch or detached state; expected baseline `HEAD` or unborn state; expected index condition; expected tracked, untracked, ignored, and submodule conditions where required; explicit permitted transitions; required postconditions; `leaseRequired`; lease identity when required; issuance checkpoint; and mandatory expiry or equivalent freshness boundary.

The expected baseline remains immutable. Later validation MUST compare fresh observations with that baseline, explicitly permitted transitions, changes attributable to authorized execution, and required postconditions. Authorized writes MUST NOT absorb unrelated drift into a new trusted baseline.

## Enforcement limitations

The planned governance model is cooperative. It can deny actions performed through compliant framework entry points, but it cannot stop a user, agent, script, plugin, or other process that bypasses those entry points or directly uses operating-system and Git capabilities. A write lease coordinates cooperating participants; it is not an operating-system lock, sandbox, or access-control mechanism.

The framework therefore MUST NOT be presented as containment for arbitrary or compromised processes. Deployments requiring containment MUST apply independent operating-system permissions, process isolation, credential controls, repository protections, and audit controls appropriate to their threat model.

Live inspection reduces reliance on stale declarations but does not eliminate time-of-check/time-of-use risk. Four checkpoints MUST remain separate: (1) initial live preflight; (2) post-acquisition, pre-contract-issuance revalidation, or immediate pre-issuance revalidation when no lease is required; (3) post-contract, immediately-before-action revalidation; and (4) post-execution verification. The third checkpoint applies to governed plan-only actions as well as writes. External mutation after validation can still invalidate an assumption; implementations MUST fail closed when they detect that condition.

Anyone who can alter authoritative governance, trusted host bindings, contract issuance mechanisms, runtime coordination state, or the enforcing implementation may be able to subvert its decisions. Those components require protections outside the governance documents themselves.

The framework MUST NOT automatically switch branches, create branches, stash, reset, clean, restore files, fetch, pull, merge, rebase, break leases, break Git administrative or lease-store locks, repair Git state, or otherwise turn a denial into an apparently valid state. Operators MUST investigate and resolve mismatches outside the denied task, under separate authorization followed by fresh preflight.

## Secret handling

Secrets MUST remain outside:

- portable or local governance files;
- Markdown documentation;
- `TaskContract` records;
- command-line arguments;
- logs and diagnostics;
- examples, fixtures, and test snapshots;
- `ExecutionReceipt` records;
- runtime artifacts, coordination state, leases, and locks inside the target worktree.

This rule applies to passwords, access tokens, private keys, session material, signing material, credential-bearing URLs, and any value that grants or materially assists access. Sanitization MUST remove both secret values and contextual data that would make redacted credentials recoverable or useful.

Secrets SHOULD be supplied at execution time by an external secret-management or credential mechanism with least-privilege access and an appropriate lifetime. Governance MAY refer to a non-secret identifier only when a future schema explicitly defines that field; such an identifier MUST NOT embed a secret. Implementations MUST avoid exposing secrets through process listings, exception text, environment dumps, debug output, or receipt capture.

If a secret is exposed, it MUST be treated as compromised. The affected credential SHOULD be revoked or rotated through its owning system, and stored outputs containing the value MUST be handled according to that system's incident procedure. Adding the leaked value to an ignore rule or deleting a working copy is not sufficient remediation.

## Reporting security issues

This repository does not currently designate a private vulnerability-reporting address or channel. An address or channel MUST NOT be inferred from this document.

Reporters MUST NOT place secrets, exploit details, customer information, real host paths, or other sensitive evidence in a public report. A reporter MAY use contact information that the repository owner has independently and explicitly published to request a private reporting method, but that initial request MUST omit sensitive details. If no private method has been explicitly published or provided, the reporter SHOULD retain the sensitive details until one is available rather than guessing an address or disclosing them publicly.

Any report SHOULD contain the smallest sanitized description needed to identify the affected component, the security consequence, reproducible conditions, and suggested mitigations. Disclosure timing and coordination MUST be agreed after a private reporting method exists; this bootstrap document makes no response-time or remediation-time commitment.
