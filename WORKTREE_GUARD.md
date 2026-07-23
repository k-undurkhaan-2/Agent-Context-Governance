# Worktree Guard

This document specifies the planned fail-closed worktree guard for Agent Context Governance and the cooperative preflight required for narrowly authorized Phase 0 bootstrap maintenance. No operational guard, schema, policy engine, trusted `TaskContract` issuer, lease manager, Git inspector, CLI, adapter, enforcement mechanism, or cryptographic bootstrap authorization is implemented in this repository.

## Authority and defaults

The future operational guard MUST evaluate machine-readable structured governance, beginning with configuration API `contextctl.dev/v1alpha1`. Task intent is untrusted input describing the requested outcome, requested mode, proposed scope, and caller-provided constraints before governance resolution; it MUST NOT grant authority. Before contract issuance, routing and lease-eligibility checks also use resolved intent and a `HostOverlay` binding, but those preliminary results do not authorize execution. After lease acquisition when required and successful revalidation, every future governed execution check, including plan-only execution, MUST also evaluate a valid bounded `TaskContract`. Markdown is explanatory and MUST NOT grant authority. Customer governance defines the future operational maximum permissions; a local `HostOverlay` MAY bind portable identities to host resources and MAY further restrict permissions, but MUST NOT widen them.

For future ordinary operational execution, unless valid structured governance and a valid `TaskContract` say otherwise, authorization is:

```yaml
mode: plan-only
allowWrite: false
```

An `ExecutionReceipt` records evidence after an attempt. It MUST NOT supply expected values, renew permission, or authorize a later attempt. Secrets MUST remain outside governance files, including `HostOverlay` instances, as well as Markdown, `TaskContract` records, command-line arguments, logs, examples, and receipts.

`mode: plan-only` implies `allowWrite: false`. The combination of `mode: plan-only` and `allowWrite: true` is invalid and MUST be rejected. A plan-only contract permits only bounded non-writing action.

A `TaskContract` has authority only when trusted framework logic issued it or validated its trusted issuer, integrity, derivation, task and target binding, freshness, and current policy, runtime, and lease preconditions. A caller-, adapter-, or task-supplied object claiming to be a `TaskContract` is untrusted input and MUST NOT grant or expand authority. A digest alone detects mutation but does not prove trusted issuance. Phase 0 does not select a final signing mechanism, and human bootstrap authority is not a substitute runtime contract.

## Phase 0 bootstrap preflight and stop conditions

Before the operational governance core and trusted `TaskContract` issuer exist, a directly supplied repository-owner or bootstrap-administrator instruction with authority class `human-bootstrap-maintenance` MAY make a governance-foundation task eligible for cooperative execution. This is a temporary external root of trust, not authority created by Markdown, ordinary task intent, a caller-created `TaskContract`, a `HostOverlay`, an `ExecutionReceipt`, an agent-facing guide, or an implemented policy-engine decision. A bootstrap task MUST NOT fabricate a `TaskContract`, lease, or receipt to imitate mechanisms that do not exist.

Bootstrap authority is eligible only when all of the following are explicit and true:

- the repository is designated Phase 0 or pre-operational, and the normal operational authorization path is absent;
- the task establishes, repairs, or reviews governance foundations rather than customer or unrelated product work;
- the instruction is supplied directly for the current task by an identified repository owner or bootstrap administrator;
- exactly one repository, one registered worktree, its expected branch, and its expected exact `HEAD` or unborn condition are identified;
- the complete expected file and status inventory, exact allowed-file set, and permitted operations are enumerated; and
- no caller, prompt, adapter, receipt, observed state, or other lower-trust input is allowed to widen the instruction.

The authorization MUST be task-, repository-, worktree-, branch-, state-, path-, and operation-specific; non-delegable unless delegation is explicit; non-reusable; and limited to the stated task lifecycle or time. Anything not explicitly listed is denied. It is revoked at completion, expiry, or the first mismatch.

Immediately before a permitted edit, bootstrap preflight MUST observe and compare at least:

1. the canonical repository top level and repository identity;
2. the current symbolic branch and exact `HEAD` commit or verified unborn state;
3. a complete inventory of tracked, staged, modified, untracked, and ignored paths;
4. an empty index and absence of unmerged entries unless the authorization explicitly requires a narrower different state;
5. both worktree-specific and common Git administrative state, including operations and locks;
6. exactly one registered worktree whose path, Git directory, branch, and repository association match;
7. the exact existing files authorized for modification and the absence of unexpected paths;
8. the configured remote identity when the authorization binds it; and
9. that the work remains inside the authorized repository and requires no external-repository access or scope widening.

Any missing, failed, stale, ambiguous, or mismatched observation MUST stop the task without editing or repair. Bootstrap authority cannot waive repository-root, branch, `HEAD`, state, path, allowed-file, worktree, remote, active-operation, administrative-lock, or Git-operation checks. Revalidation MUST occur immediately before the first write and at later protected boundaries; a relevant state change invalidates earlier observations.

Bootstrap authority MUST NOT authorize customer application work, unrelated features, production deployment, secret handling, external-repository access, another worktree, automatic Git repair, branch switching or creation, stash, reset, clean, restore, fetch, pull, merge, rebase, lease or lock breaking, staging, committing, or pushing. A future separately designed administrative procedure would be required to govern any such exceptional action; this bootstrap path does not provide one.

Current authentication is cooperative and depends on the interactive development environment treating the operator as the identified owner or administrator. It is not cryptographic proof, an operating-system permission, a sandbox, or protection against a process that bypasses the framework. The bootstrap path MUST be retired or disabled when the project formally activates the operational governance path.

## Expected state and observed state

In the future operational path before contract issuance, candidate expected state is derived from validated structured governance and resolved task intent after `HostOverlay` restrictions are applied. It is used only to test routing, live state, pre-execution scope authorization, and lease eligibility. After successful lease acquisition when required and revalidation, a valid `TaskContract` MUST bind at least the object API version; contract version; unique contract identity; unique task identity; resolved `Project` identity; repository identity; selected target worktree identity or logical binding; complete non-empty `Domain` set; required `WorktreeRole`; trusted issuer or validated provenance information; policy and configuration digests; task-intent digest or equivalent immutable binding; requested and effective mode; explicit `allowWrite`; authorized path scope; prohibited path scope where represented; expected baseline branch or detached state; expected baseline `HEAD` or unborn state; expected index condition; expected tracked, untracked, ignored, and submodule conditions where required; explicit permitted transitions; required postconditions; `leaseRequired`; lease identity when required; issuance checkpoint; and mandatory expiry or equivalent freshness boundary.

The expected baseline remains immutable. Later checks compare fresh observations with that baseline, explicitly permitted transitions, changes attributable to authorized execution, and required postconditions. Authorized writes MUST NOT absorb unrelated drift into a new trusted baseline. Only a separately authorized new task and fresh preflight may establish a new baseline.

Runtime Git observations are freshly collected repository and filesystem facts, including repository identity, registration, branch or detached state, `HEAD`, status, submodules, active operations, and Git administrative locks. Runtime coordination state includes task state, lease records, lease-store synchronization, ownership records, release outcomes, and lease-store locks. Git administrative locks and lease-store locks are distinct. Every observation MUST be associated with the canonical target and inspection time and distinguish a command failure from a legitimate empty result.

A check passes only when all required observations succeed and exactly satisfy the immutable expected baseline, permitted transitions, required postconditions, and applicable restrictions. Missing, malformed, ambiguous, stale, non-unique, or mismatched data is a denial, never an invitation to guess. A state-changing boundary invalidates earlier observations and requires reinspection.

## Required checks

The numbered checks below define the future ordinary operational guard. For Phase 0 bootstrap maintenance, checks 1 through 6 apply as direct live observations under the exact external instruction and its complete expected inventory; the task MUST NOT fabricate the unimplemented role, lease, policy, or contract mechanisms described in checks 7 and 8. Where a numbered check refers to a `TaskContract` or structured governance, that requirement applies to the future operational path rather than replacing the bootstrap preflight above.

### 1. Repository root

The expected state MUST identify one canonical target worktree and repository. The guard MUST resolve the target path without relying on the process working directory and MUST observe the repository top level and Git directory from that target. The observed top level MUST equal the expected canonical worktree path, and the repository identity MUST match the expected project. A nested repository, path alias that cannot be resolved unambiguously, target outside the declared project, or Git directory belonging to another repository or worktree MUST deny implementation.

### 2. Branch

The expected baseline MUST explicitly identify either a symbolic branch or an authorized detached state. The guard MUST read the current condition from the target worktree immediately before use. A missing or ambiguous ref, a detached `HEAD` when a branch is expected, a branch when detached state is expected, a branch-name mismatch, a detached-commit mismatch, or observation failure MUST deny implementation. The guard MUST NOT treat a similarly named branch as equivalent.

### 3. `HEAD`

The expected state MUST declare either an exact `HEAD` commit or an explicit unborn-repository condition. The guard MUST resolve `HEAD` live and distinguish a nonexistent `HEAD` in an unborn repository from resolution errors. A resolvable commit when unborn state is expected, an unborn state when a commit is expected, a different commit, or any ambiguous resolution MUST deny implementation.

If an authorized operation is intended to change `HEAD`, each later checkpoint MUST compare against the immutable baseline, contract-defined permitted transition, task-attributable changes, and required postconditions. The guard MUST NOT accept an unexpected commit merely because the current task may have produced it or rewrite the baseline during the contract.

### 4. Dirty state

The guard MUST inspect the complete working-tree state, including staged changes, unstaged changes, untracked files, ignored files relevant to policy, submodule state, and conflicts. The default expected state for ordinary operational implementation is clean. Any permitted pre-existing state MUST be described explicitly and narrowly by the applicable authority and, in the ordinary path, the `TaskContract`; an unclassified path or change MUST deny implementation. A Phase 0 bootstrap instruction MAY bind a different state only by enumerating its complete exact inventory.

The observed state MUST be compared by status class and path, not reduced to a single clean/dirty boolean. A conflict, unexpected modification, unexpected staging, unexpected untracked or ignored content, unreadable path, or status failure MUST deny implementation. The guard MUST NOT silently absorb a task's own earlier changes into the expected baseline.

### 5. Active Git operation

The guard MUST inspect both worktree-specific and common Git administrative state for an in-progress merge, rebase, cherry-pick, revert, bisect, apply-mailbox operation, sequencer operation, or lock that could make mutation unsafe. The normal expected state is that none is active. An active or ambiguous operation, an unexpected lock, or an unreadable administrative state MUST deny implementation. A stale-looking marker or lock MUST still deny implementation; the guard MUST NOT complete, abort, remove, or break it.

### 6. Worktree registration

The guard MUST inspect the common repository's live worktree registration. The canonical target MUST be registered exactly once and its registered path, Git directory, branch-or-detached metadata, and repository association MUST agree with the expected state and direct target observations. Missing or duplicate registration, a prunable or otherwise inconsistent record, mismatched branch-or-detached metadata, an unexpected common Git directory, or a target registered to another repository MUST deny implementation.

Registration proves repository membership only. It does not prove that a worktree's role owns the complete required `Domain` set or that the worktree is available for writing.

### 7. Worktree role ownership

In the future operational path, task resolution MUST produce exactly one `Project` and a non-empty deterministic set of `Domain` identifiers. After that resolution, `RoutingPolicy` MUST select exactly one `WorktreeRole` that owns every resolved `Domain`, and the `HostOverlay` MUST bind that role to one canonical local worktree without widening the mapping. The guard MUST compare the complete domain set and required role with the selected worktree's declared role. Role MUST NOT be inferred from path, branch, availability, lease state, or historical use. The `TaskContract` MUST bind the same complete set.

Implementation MUST be denied when the project, domain set, covering role, or binding is missing, ambiguous, stale, mismatched, or narrowed away by the `HostOverlay`. If no unique role covers the complete set, the task MUST be split into independently authorized tasks or denied. A free worktree with the wrong role is not a fallback routing target. Worktree-role ownership is an authorization check and remains required even when no write lease is held by another task.

### 8. Runtime write lease

Every ordinary governed task that may write MUST have effective `allowWrite: true` and MUST acquire, through an atomic operation, the task-owned write lease for the canonical worktree before contract issuance. The acquisition result MUST carry a stable lease identity and ownership evidence. The guard MUST inspect the runtime lease store live and bind the lease to the exact worktree and task identity. At most one live write lease may be held for a worktree; any malformed, ambiguous, stale, unreleased, or otherwise unresolved coordination state blocks acquisition and later writers. Plan-only eligibility MUST NOT be interpreted as write authorization. A Phase 0 bootstrap task relies only on its bounded external authorization and direct live revalidation; it MUST NOT create or claim a framework lease.

A conflicting lease held by another task, failed atomic acquisition, a missing required lease after acquisition, identity mismatch, malformed or unreadable lease record, ambiguous coordination state, or unexpected lease-store lock MUST deny writing. A held lease is acceptable only when the current task can prove that it acquired and still owns that exact lease. Apparent expiry or staleness MUST NOT authorize automatic takeover or lease-store-lock breaking. After acquisition, every repository, role, scope, policy, and authorization check MUST run again so a race or intervening change fails closed. A lease does not correct a wrong role, expand scope, or replace a valid `TaskContract`.

Release MUST target only the lease identified by the acquisition result and provably owned by the task. If a `TaskContract` was issued, its lease identity MUST match that lease. Pre-contract cleanup MUST NOT require a contract. An unreleased, malformed, ambiguous, stale, or otherwise unresolved lease remains blocking regardless of whether execution succeeded, was denied, failed, was cancelled, or was indeterminate. Later writers remain denied until ownership-checked release succeeds or a separately authorized operator-resolution procedure completes; the guard MUST NOT erase or break the record to make the worktree appear free.

## Checkpoints and stop conditions

For the future operational path, four checkpoints are distinct: (1) initial live preflight; (2) post-acquisition, pre-contract-issuance revalidation, or immediate pre-issuance revalidation when no lease is required; (3) post-contract, immediately-before-action revalidation, including contract scope validation; and (4) post-execution scope and state verification. Only successful checkpoint-two revalidation MAY allow trusted `TaskContract` issuance or validation. Relevant checks MUST also run at later policy-defined boundaries. If live state changes after observation, the observation is stale and MUST be repeated. A Phase 0 bootstrap task instead uses the external authorization and bootstrap preflight above and MUST NOT pretend that a `TaskContract` or lease was issued.

The guard MUST stop implementation and return a denial when any of the following is true:

- for an ordinary governed task, structured governance, resolved intent, or the `HostOverlay` binding is absent, invalid, stale, ambiguous, inconsistent, or not applicable to the target, or an execution checkpoint lacks a valid applicable `TaskContract`;
- the task proposes `mode: plan-only` with `allowWrite: true`; a plan-only action attempts a write; a proposed write lacks effective `allowWrite: true`; or any requested operation or scope exceeds applicable authorization;
- the target worktree or expected branch-or-detached condition is missing or non-unique;
- any applicable repository-root, branch, `HEAD`, dirty-state, active-operation, or registration check fails, or an ordinary governed task fails role-ownership or lease checks;
- an observation cannot be collected or its freshness and target association cannot be established;
- state changes between a successful check and the protected action;
- execution would require another repository, an unbound host resource, or disclosure of a secret; or
- post-execution verification finds an out-of-scope or unexpected change.

On denial, the system MUST perform no further protected write. It SHOULD report the failed check, expected state, observed state or observation error, checkpoint, and authoritative input identifiers without exposing secrets. If denial occurs after a write, the system MUST preserve evidence and stop; it MUST NOT claim success or attempt an automatic rollback.

## No automatic repair

The guard is a permit-or-deny control, not a Git repair tool. To make observed state match expected state, the framework MUST NOT automatically:

- switch branches or create branches;
- stash changes;
- reset or clean the worktree;
- restore files;
- fetch or pull;
- merge or rebase;
- break leases or locks; or
- otherwise repair Git state.

It also MUST NOT rewrite governance as automatic repair, relax a role, fabricate a `TaskContract`, or delete a lease to turn a denial into permission. Remediation requires separately authorized maintenance followed by a completely new live preflight.
