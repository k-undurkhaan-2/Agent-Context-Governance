# Task Lifecycle

This document defines the planned authorization and execution lifecycle for a task. It is an architectural contract, not a description of implemented behavior. Every stage MUST fail closed: missing, malformed, ambiguous, stale, or mismatched state MUST deny implementation.

The lifecycle separates authorization from evidence. Structured governance and a valid, provenance-checked `TaskContract` may authorize future governed work. Governed adapter execution, including governed plan-only execution, requires a valid bounded `TaskContract`. An `ExecutionReceipt` records what happened and MUST NOT be used as authorization input. Backticked PascalCase denotes a structured object kind. Spaced lowercase wording denotes the prose concept.

## Object families and placement

All seven planned kinds use API version `contextctl.dev/v1alpha1`. Concrete `Project`, `Domain`, `WorktreeRole`, and `RoutingPolicy` instances are portable customer governance. Concrete `HostOverlay` instances are host-local input. Concrete `TaskContract` and `ExecutionReceipt` instances are runtime artifacts. Schema definitions for all kinds MAY later live under `schemas/v1alpha1/`, but concrete host-local and runtime instances MUST remain outside the target worktree. Generated receipts MUST never become portable governance.

The canonical scope controls are pre-execution scope authorization, contract scope validation, and post-execution scope verification.

## Independent state dimensions

Lifecycle phase, execution outcome, verification outcome, release outcome, overall lifecycle outcome, receipt-delivery outcome, and lease liveness are separate dimensions.

- Lifecycle phase records progress from intent receipt through resolution, authorization, execution, verification, release, receipt finalization, and reporting.
- Execution outcome records `not-attempted`, `succeeded`, `failed`, `cancelled`, or `indeterminate` as appropriate.
- Verification outcome records the result and limits of post-execution verification.
- Release outcome records `not-required`, `succeeded`, `failed`, or `indeterminate` after ownership-checked release is attempted.
- Overall lifecycle outcome incorporates execution, verification, release, and unresolved coordination-state warnings known when the receipt is finalized.
- Receipt-delivery outcome separately records the later persistence or delivery attempt; a delivery failure is reported without rewriting the finalized evidence or retaining an otherwise releasable lease.
- Lease liveness records whether a lease is absent, live, released, or unresolved; it is not inferred from any task or execution outcome.

An unreleased, malformed, ambiguous, stale, or otherwise unresolved lease remains blocking regardless of whether execution succeeded, was denied, failed, was cancelled, or was indeterminate. Competing writers MUST remain denied until ownership-checked release succeeds or a separately authorized operator-resolution procedure completes. The framework MUST NOT automatically break the lease. Lifecycle reporting may finish with a failed or indeterminate overall outcome while unresolved coordination state remains blocking.

Four checkpoints remain distinct: initial live preflight; post-acquisition, pre-contract-issuance revalidation, or immediate pre-issuance revalidation when no lease is required; post-contract, immediately-before-action revalidation; and post-execution verification.

## 1. Receive task intent

Task intent is untrusted input describing the requested outcome, requested mode, proposed scope, and caller-provided constraints before governance resolution. It MUST NOT grant authority.

- Intent MUST identify enough project and responsibility context for deterministic resolution.
- Values that affect authorization MUST be treated as requests, not grants.
- Omitted authorization fields MUST resolve to `mode: plan-only` and `allowWrite: false`. `mode: plan-only` implies `allowWrite: false`; the combination with `allowWrite: true` is invalid and MUST be rejected.
- Intent MUST NOT contain secrets.
- An ambiguous target, contradictory constraint, prohibited scope, or request that depends on secret material in the task input MUST be denied.

## 2. Resolve one `Project` and the complete `Domain` set

The control plane resolves the intent against authoritative, machine-readable customer governance.

- Exactly one `Project` MUST match.
- Every responsibility affected by the requested work MUST resolve to a non-empty deterministic set of `Domain` identifiers.
- Customer governance MAY restrict an otherwise valid request.
- Markdown, agent instructions, prior receipts, and adapter defaults MUST NOT fill an authorization gap or widen permissions.
- No project match, multiple project matches, zero domains, incomplete coverage, ambiguous resolution, or conflicting policy MUST deny implementation.

## 3. Route one covering `WorktreeRole`

After exactly one `Project` and the complete `Domain` set are resolved, the control plane applies `RoutingPolicy` to select exactly one eligible `WorktreeRole` that owns every resolved `Domain`. `RoutingPolicy` does not resolve the project or discover the domain set.

- Worktree-role ownership of `Domain` identifiers is an eligibility control: the selected role MUST own the complete set assigned to the task.
- Routing MUST produce exactly one eligible role. The concrete worktree MUST remain unresolved until host binding selects one valid binding for that role.
- A free worktree with the wrong role MUST NOT be selected.
- If no unique role covers the complete set, the task MUST be split into independently authorized tasks or denied.
- Load, availability, or the absence of a lease MUST NOT override worktree-role ownership.

## 4. Resolve one `HostOverlay` binding

The selected logical role is bound to a repository worktree on the current host through a local `HostOverlay`.

- The concrete `HostOverlay` MUST remain outside the target worktree and portable customer governance. Real host paths and other machine-local details MUST appear only in that local layer.
- A host overlay MAY narrow customer permissions but MUST NOT widen them.
- The binding MUST identify one repository root and its expected branch-or-detached condition without exposing secrets.
- A missing, duplicate, malformed, stale, or policy-incompatible binding MUST deny implementation.
- A binding to a repository or worktree inconsistent with the resolved `Project` or uniquely routed role MUST deny implementation.

## 5. Initial live preflight

Runtime Git observations MUST be freshly read from the target worktree at decision time. They include repository and filesystem facts. Runtime coordination state—including task state, lease records, lease-store synchronization, ownership records, release outcomes, and lease-store locks—MUST be read from its host-local store. Git administrative locks and lease-store locks are distinct. Cached observations, task prose, and prior receipts are not substitutes for live inspection.

Inspection MUST evaluate all checks required by policy, including:

- resolved repository root;
- current branch or detached state and the expected condition;
- current `HEAD` and any expected revision constraint;
- tracked, staged, modified, untracked, and ignored state as required by policy;
- in-progress Git operations and Git administrative locks;
- worktree registration and association;
- configured remote identity when policy requires it; and
- current role binding and runtime coordination state.

Any missing observation, command failure, unexpected repository root, branch or revision mismatch, prohibited dirty state, active operation, invalid registration, role mismatch, or ambiguous runtime result MUST deny implementation.

The framework MUST NOT repair a mismatch automatically. In particular, it MUST NOT switch or create branches, stash, reset, clean, restore files, fetch, pull, merge, rebase, break leases or locks, or repair Git state.

## 6. Atomic lease acquisition

A runtime write lease is a concurrency control, not a routing or authorization grant.

- A task with effective `allowWrite: true` MUST atomically acquire the task-owned write lease for its target worktree before a contract is issued. The acquisition result MUST carry a stable lease identity and enough ownership evidence for later release.
- At most one live write lease may be held for the worktree. Any malformed, ambiguous, stale, unreleased, or otherwise unresolved coordination state blocks acquisition and later writers.
- A plan-only task with `allowWrite: false` MUST NOT acquire or rely on a write lease and MUST remain unable to write.
- Lease records, lease-store locks, and other runtime coordination state MUST remain outside the target worktree.
- A conflicting lease held by another task, acquisition race, failed acquisition, ownership mismatch, or a required post-acquisition lease that is missing, malformed, ambiguous, or stale MUST deny implementation.
- The framework MUST NOT infer that a stale-looking lease is abandoned and MUST NOT break or steal a lease automatically.

Successful acquisition does not cure a wrong role, invalid host binding, or Git-state mismatch.

## 7. Post-acquisition, pre-contract-issuance revalidation

After lease acquisition, or immediately before contract issuance for a task that requires no lease, the control plane MUST re-observe all authorization-sensitive runtime Git observations and runtime coordination state.

- The `Project`, complete `Domain` set, `WorktreeRole`, host binding, Git state, pre-execution scope authorization, mode, and effective permissions MUST still match the proposed contract.
- A write task MUST prove that it still owns the same valid lease.
- Customer governance and the host overlay MUST be re-evaluated if either may have changed.
- Any change, uncertainty, expiration, or mismatch MUST prevent contract issuance.

If revalidation denies a task after lease acquisition, release MUST target only the lease identified by the acquisition result and provably owned by the task. Pre-contract cleanup MUST NOT require a nonexistent `TaskContract`. Failure to prove safe release MUST leave the worktree unavailable for new write tasks and require a separately authorized operator-resolution procedure; it MUST NOT trigger automatic lease or lock breaking.

## 8. Trusted `TaskContract` issuance or validation

A `TaskContract` has authority only when trusted framework logic issued it or validated its trusted issuer, integrity, derivation, task and target binding, freshness, and current policy, runtime, and lease preconditions. A caller-, adapter-, or task-supplied object claiming to be a `TaskContract` is untrusted input and MUST NOT grant or expand authority. A digest alone detects mutation but does not prove trusted issuance. Phase 0 does not select a final signing mechanism, and human bootstrap authority is not a substitute runtime `TaskContract`.

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

The expected baseline remains immutable. Later validation compares fresh observations with that baseline, explicitly permitted transitions, changes attributable to authorized execution, and required postconditions. Authorized writes MUST NOT absorb unrelated drift into a new trusted baseline.

- `allowWrite: true` MUST be explicit; absence MUST mean `false`.
- The contract MUST bind the same complete `Domain` set and MUST NOT grant more authority than customer governance, the `HostOverlay`, or the selected role permits.
- When a lease is required, the contract's lease identity MUST match the acquisition result.
- The contract MUST NOT contain secrets.
- A contract MUST be valid for only its bound target and task; adapters MUST NOT reuse it for another task, worktree, branch, or scope.
- If a complete, unambiguous contract cannot be issued or validated, implementation MUST be denied.

## 9. Post-contract revalidation and adapter execution

An execution adapter translates the agent-neutral contract into a product-specific invocation. The adapter is outside the core authorization model.

- The adapter MUST validate the contract's version, trusted provenance, freshness, target, mode, contract scope, and write permission before acting.
- Post-contract, immediately before any governed action, the execution path MUST revalidate the applicable contract, policy, runtime Git observations, runtime coordination state, contract scope, and lease ownership when required. This checkpoint applies to plan-only actions as well as writes. Drift or an unavailable observation MUST stop execution.
- The adapter MUST refuse a missing, unsupported, expired, altered, or mismatched contract.
- The adapter MUST NOT infer additional authority from agent instructions, Markdown, environment defaults, earlier receipts, or its own capabilities.
- Governed plan-only execution requires a valid bounded contract but MUST NOT produce repository writes or acquire a write lease.
- A write adapter MUST remain within the contracted worktree and scope and MUST retain the lease until the ownership-checked release step; stopping execution does not imply release.
- The adapter MUST NOT perform prohibited Git repair or branch-management actions on the framework's behalf.
- Adapter errors, timeouts, cancellation, or detected state drift MUST stop execution and enter terminal processing; they MUST NOT cause an automatic retry with broader authority.

## 10. Post-execution verification

Post-execution scope and state verification compares the attempted execution with the contract, its immutable baseline and permitted transitions, required postconditions, fresh runtime Git observations, and runtime coordination state.

- Verification MUST re-inspect the target worktree live.
- It MUST determine whether the actual files, complete `Domain` set, Git state, mode, and other observable effects stayed within contract scope.
- For a plan-only task, any detected repository write MUST be treated as a policy violation.
- Out-of-scope changes, an unexpected branch or repository, lost lease ownership, incomplete evidence, or an inspection failure MUST prevent a successful result.
- Verification MUST report uncertainty as indeterminate rather than infer success.

Cooperative verification cannot prevent a process that bypasses the framework. It provides detection and evidence for participating adapters; it is not an operating-system security boundary.

## 11. Capture pre-release terminal evidence

After post-execution verification, terminal processing MUST capture the available execution and verification evidence without yet asserting the final lifecycle outcome. Evidence capture MUST NOT be confused with final `ExecutionReceipt` creation because lease release can change the overall result.

## 12. Ownership-checked lease release

After pre-release evidence capture, a task that acquired a write lease MUST attempt ownership-checked release before receipt finalization.

- Release MUST target only the lease identified by the acquisition result and provably owned by the task.
- If a `TaskContract` was issued, its lease identity MUST match that lease.
- Pre-contract cleanup MUST NOT require a contract.
- The release attempt MUST produce `releaseOutcome` as `succeeded`, `failed`, or `indeterminate`; a task requiring no lease records `not-required`.
- Release failure, owner mismatch, malformed state, or ambiguous lease-store lock state MUST be reported and MUST deny subsequent write contracts for that worktree.
- The framework MUST NOT break, overwrite, or silently discard a lease it cannot prove it owns.

Receipt storage or delivery readiness MUST NOT delay this release attempt. An execution outcome does not imply release, and unresolved lease state remains blocking until ownership-checked release succeeds or a separately authorized operator-resolution procedure completes.

## 13. Finalize and deliver the `ExecutionReceipt`

After `releaseOutcome` is known, terminal processing MUST attempt to finalize a sanitized `ExecutionReceipt` for every issued-contract execution attempt, including unsuccessful or indeterminate attempts. A denial before contract issuance MAY also produce a sanitized denial receipt when future policy explicitly requires one; that record is evidence of the denial and MUST NOT be treated as a contract or authorization.

The finalized receipt MUST record the execution outcome, verification outcome, release outcome, overall lifecycle outcome, and unresolved coordination-state warnings. It SHOULD identify the task and contract, record the effective mode and logical target without machine-local secrets, and summarize the observed attempt.

After finalization, terminal processing MUST attempt to persist or deliver the receipt through host-local infrastructure outside portable governance.

- Generated `ExecutionReceipt` records are host-local runtime evidence and MUST remain outside the target worktree and portable governance.
- Repository documentation MAY contain only conspicuously synthetic receipt-shaped examples. Synthetic examples are not generated runtime receipts and MUST NOT be authorization input.
- Receipts MUST NOT contain secrets, credentials, or real host paths.
- A receipt MUST NOT authorize a retry, follow-up task, lease acquisition, or any other action.
- Missing receipt evidence MUST NOT be interpreted as success.
- Receipt persistence or delivery failure MUST be reported, MUST NOT grant authority or hide unresolved lease state, and MUST NOT indefinitely retain an otherwise releasable lease.

## Denial and failure summary

| Point | Required response |
| --- | --- |
| Intent is incomplete, contradictory, or requests prohibited material | Deny before resolution; apply safe defaults and do not implement. |
| `Project`, non-empty `Domain` set, covering `WorktreeRole`, or host binding is missing, multiple, stale, or mismatched | Deny; split independently where appropriate, but do not guess or route to a merely free worktree. |
| Runtime Git observations or runtime coordination inspection fails or differs from expected state | Deny; report the mismatch and do not repair it automatically. |
| Write permission is absent or restricted | Keep `mode: plan-only` and `allowWrite: false`; do not acquire a write lease. |
| A required write lease is unavailable or uncertain | Deny; do not wait by holding partial authority, steal the lease, or break a lock. |
| Post-acquisition revalidation fails | Do not issue a contract; release only the acquisition-result lease provably owned by the task, without requiring a contract. |
| Contract creation or adapter validation fails | Do not execute; treat any acquired lease through terminal cleanup rules. |
| Execution fails, times out, is cancelled, or drifts out of scope | Stop, perform post-execution verification, capture evidence, and attempt ownership-checked release before finalizing the receipt. |
| Verification or receipt recording is incomplete | Mark the applicable outcome indeterminate or failed; never infer success, release, or authorization. |
| Lease release is unsafe or fails | Record the release outcome, finalize with an unresolved-state warning, keep future writes denied, and require separately authorized operator resolution; never break the lease or lock automatically. |
| Receipt persistence or delivery fails | Report the failure without granting authority, hiding unresolved state, or retaining an otherwise releasable lease. |

## Related decisions

- [ADR 0001: Agent-neutral core](decisions/0001-agent-neutral-core.md)
- [ADR 0002: Configuration authority](decisions/0002-configuration-authority.md)
- [ADR 0003: Versioning model](decisions/0003-versioning-model.md)
- [ADR 0004: Worktree ownership and leases](decisions/0004-worktree-ownership-and-leases.md)
