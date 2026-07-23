# ADR 0004: Worktree role ownership and runtime write leases

- Status: Accepted

## Context

Choosing where a task is allowed to run and preventing concurrent writers are different safety questions. Availability alone does not establish worktree-role ownership of `Domain` identifiers, while that ownership alone does not show that a worktree is currently safe for exclusive write execution.

Conflating these questions could route work to an idle but unauthorized worktree or allow simultaneous writers in a correctly assigned worktree.

This ADR defines future routing and lease requirements. It does not claim that a router, lease store or manager, trusted `TaskContract` issuer, or enforcement system exists during Phase 0.

## Decision

The framework MUST apply two separate controls.

Backticked PascalCase denotes a structured object kind. Spaced lowercase wording denotes the prose concept.

### Worktree role ownership

Worktree-role ownership of `Domain` identifiers is a routing eligibility control. Task resolution MUST produce exactly one `Project` and a non-empty deterministic set of `Domain` identifiers. A task MAY use only the one selected worktree whose declared `WorktreeRole` owns every `Domain` in that complete set. The future `TaskContract` MUST bind the same set.

- After the project and complete domain set are resolved, `RoutingPolicy` MUST select exactly one eligible `WorktreeRole`; host binding MUST then resolve one unique worktree for that role.
- A free worktree with the wrong role MUST NOT be used.
- If no unique role covers every resolved `Domain`, implementation MUST be denied or the intent MUST be split into independently authorized tasks.
- Host binding MUST NOT change the responsibility owned by a role.
- Customer governance MAY restrict role eligibility, and a `HostOverlay` MAY further restrict the available bindings; the overlay MUST NOT widen ownership.

Worktree-role ownership answers, "May this complete class of work be assigned here?" It does not authorize writing, validate live Git state, or reserve the worktree.

### Runtime write lease

A runtime write lease is an exclusive concurrency control. At most one live write lease may be held for a worktree. Any malformed, ambiguous, stale, unreleased, or otherwise unresolved coordination state blocks acquisition and later writers. Lease liveness is independent of lifecycle phase and execution outcome.

- A task MUST first pass role routing, host binding, structured-governance permission evaluation, and live inspection.
- A task with `allowWrite: true` MUST atomically acquire the target worktree's lease before contract issuance and MUST prove continued ownership during revalidation and verification.
- A task with the default `mode: plan-only` and `allowWrite: false` MUST NOT write and MUST NOT treat lease availability as write permission.
- A correct role with a conflicting lease, or with lease ownership that the current task cannot prove, MUST NOT receive a new write contract.
- Lease records, lease-store synchronization, task ownership records, release outcomes, lease-store locks, and real host paths are runtime coordination state and MUST remain outside the target worktree. They are distinct from freshly read runtime Git observations and Git administrative locks.
- Missing, malformed, ambiguous, stale, or mismatched lease state MUST deny implementation.
- The framework MUST NOT break, steal, overwrite, or automatically repair a lease or lock.
- Release MUST target only the lease identified by the acquisition result and provably owned by the task. If a `TaskContract` was issued, its lease identity MUST match that lease. Pre-contract cleanup MUST NOT require a contract.
- Lease release MUST be ownership-checked. Failure to release safely, or an unreleased, malformed, ambiguous, stale, or otherwise unresolved lease, MUST deny later writes regardless of whether execution succeeded, was denied, failed, was cancelled, or was indeterminate, until ownership-checked release succeeds or a separately authorized operator-resolution procedure completes.

A lease answers, "Is one authorized write task exclusively using this worktree now?" It does not establish worktree-role ownership of the complete `Domain` set, grant `allowWrite`, or prove that Git state matches the contract.

### Combined decision

For a write task to proceed, all of the following MUST independently succeed:

1. structured governance permits the resolved `Project`, complete non-empty `Domain` set, requested mode, and scope;
2. the selected `WorktreeRole` owns every resolved `Domain`;
3. the host overlay provides one valid binding without widening customer governance;
4. fresh runtime Git observations and runtime coordination state match expected state;
5. the task atomically acquires the worktree's write lease;
6. revalidation confirms the same state and lease ownership; and
7. trusted framework logic issues or validates a bounded `TaskContract` with `allowWrite: true`, the same `Domain` set, and a lease identity matching the acquisition result.

Failure of any control MUST deny implementation. Success in one control MUST NOT compensate for failure in another.

## Consequences

- Routing remains deterministic and responsibility-based rather than availability-based.
- One live lease excludes a competing writer, and unresolved coordination state continues to block acquisition regardless of task outcome.
- Read-only planning does not become write-authorized merely because no lease is held.
- Runtime coordination requires atomic, machine-local lease storage and explicit recovery procedures.
- Suspected stale leases may reduce availability, but fail-closed handling preserves the ownership boundary.
- Live Git preflight remains necessary even after ownership and lease checks succeed.
- A terminal execution outcome does not make an unreleased or unresolved lease nonblocking.

## Alternatives not selected

### First free worktree

Routing to any available worktree was not selected because availability does not establish worktree-role ownership of the complete `Domain` set.

### Worktree-role ownership as an implicit lock

Treating a declared role as exclusive runtime ownership was not selected because multiple tasks could still attempt concurrent writes without a lease.

### Lease possession as authorization

Treating lease acquisition as permission was not selected because a concurrency primitive cannot replace customer policy, host restrictions, worktree-role ownership of the complete `Domain` set, live inspection, or a valid contract.
