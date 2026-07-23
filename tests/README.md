# Planned test strategy

No tests are implemented in the documentation-bootstrap phase. Future tests MUST be deterministic, MUST use sanitized synthetic data, and SHOULD cover the following categories.

## Categories

- **Unit tests:** parsing, validation, resolution, policy evaluation, state comparison, and scope matching in isolation.
- **Contract tests:** compatibility between public configuration objects, `TaskContract` records, adapter boundaries, and `ExecutionReceipt` records.
- **Integration tests:** the complete ordered lifecycle from untrusted task intent, through resolution and execution, to lease release and receipt finalization.
- **Concurrency tests:** competing write tasks, exclusive lease acquisition, lease release, stale owners, and state changes during revalidation.
- **Fixture tests:** reusable synthetic repositories and governance inputs representing valid and invalid states.
- **Golden tests:** stable diagnostics, denial reasons, normalized contracts, and sanitized receipts reviewed as intentional output changes.

Contract tests MUST prove that a `TaskContract` has authority only after trusted framework issuance or validation of trusted issuer, integrity, derivation, task and target binding, freshness, and current policy, runtime, and lease preconditions. A caller-, adapter-, or task-supplied claim MUST remain untrusted, and a digest alone MUST NOT be accepted as proof of issuance. Phase 0 selects no final signing mechanism.

Tests MUST prove that future governed adapter execution, including plan-only execution, requires a valid bounded `TaskContract` and rejects a missing, invalid, stale, or unbounded contract. They MUST also prove that temporary Phase 0 human bootstrap authority is not accepted as a runtime `TaskContract`.

## Required failure scenarios

Future integration coverage MUST exercise this order:

1. receive untrusted task intent;
2. resolve exactly one `Project`;
3. resolve a non-empty deterministic set of `Domain` identifiers;
4. use `RoutingPolicy` to select exactly one `WorktreeRole` that owns every resolved `Domain`;
5. resolve one local `HostOverlay` binding;
6. perform initial live preflight;
7. atomically acquire the task-owned write lease when required;
8. perform post-acquisition, pre-contract-issuance revalidation;
9. issue or validate a trusted, state-bound `TaskContract` that binds the same complete `Domain` set;
10. perform post-contract, immediately-before-action revalidation;
11. execute through an adapter;
12. perform post-execution scope and state verification;
13. capture pre-release evidence;
14. perform ownership-checked release;
15. record `releaseOutcome` and finalize the `ExecutionReceipt`; and
16. attempt receipt persistence or delivery outside portable governance.

The test suite MUST demonstrate fail-closed behavior for at least:

- missing, malformed, ambiguous, stale, or mismatched configuration or runtime state;
- unknown configuration fields and unsupported configuration API versions;
- forged, caller-, adapter-, or task-supplied objects claiming to be a `TaskContract`, and caller attempts to expand authority;
- zero resolved `Domain` identifiers, no role covering the complete `Domain` set, multiple eligible roles, and a wrong-role but unlocked worktree;
- the invalid combination `mode: plan-only` with `allowWrite: true`, plus write requests under the defaults `mode: plan-only` and `allowWrite: false`;
- an unregistered repository or worktree, an unexpected root, branch, or HEAD, dirty state, or an active Git operation;
- a `HostOverlay` attempting to widen customer governance;
- failed lease acquisition, conflicting leases, or a required lease that is absent, malformed, stale, or invalid at a protected checkpoint;
- post-acquisition denial and pre-contract cleanup that releases only the acquisition-result lease provably owned by the task without requiring a nonexistent contract;
- drift after contract issuance or at another checkpoint, and changes outside a `TaskContract`'s allowed scope;
- receipt storage or delivery failure, lease release failure, and failed or cancelled execution with an unresolved lease;
- an `ExecutionReceipt` being presented as authorization input;
- invalid in-worktree concrete `HostOverlay`, `TaskContract`, receipt, lock, lease, or runtime-state artifacts even if an ignore rule would otherwise hide them; and
- secrets or machine-specific runtime data appearing in diagnostics, fixtures, golden files, logs, or receipts.

Worktree-role ownership of the complete `Domain` set and runtime write leases MUST be exercised as independent controls. Tests MUST prove that execution outcome and lease liveness are independent and that generated receipts remain outside portable governance. Terminal processing MUST attempt to record a sanitized `ExecutionReceipt` for every issued-contract execution attempt; pre-contract denial receipts MAY remain policy-optional. Tests MUST NOT rely on automatic branch switching, branch creation, stashing, reset, cleaning, restoration, fetching, pulling, merging, rebasing, lease or lock breaking, or Git-state repair.
