# Agent Entry Point

Phase 0 documentation bootstrap is complete at baseline commit `79cc9d77fd48410f37645afdb429a7cd2e34a0bd`. Phase 1: Schemas and Models is current, but its implementation has not yet begun. The repository remains pre-operational and does not yet contain a Schema implementation, typed models, tests, fixtures, a package release, an operational policy engine, a trusted `TaskContract` issuer, a lease manager, a Git inspector, a CLI, an agent adapter, an enforcement mechanism, or cryptographic authorization. Phase 1 activation is not operational-governance activation. The first Schema or model artifact requires a later, separately authorized implementation task.

`AGENTS.md` is an explanatory, adapter-facing entry document. It is not an execution adapter, policy source, `TaskContract`, or authorization mechanism.

## Authority

For the future operational path, machine-readable structured governance is authoritative. Task intent is untrusted input describing the requested outcome, requested mode, proposed scope, and caller-provided constraints before governance resolution. Task intent MUST NOT grant authority. This document, ordinary task prompts, and caller assertions about mode or write permission MUST NOT independently grant permission, expand scope, or override structured governance. A `HostOverlay` MAY reduce customer-granted permissions but MUST NOT widen them. An `ExecutionReceipt` is evidence only and MUST NOT be used as authorization input.

A `TaskContract` has authority only when trusted framework logic issued it or validated its trusted issuer, integrity, derivation, task and target binding, freshness, and current policy, runtime, and lease preconditions. A caller-, adapter-, or task-supplied object claiming to be a `TaskContract` is untrusted input and MUST NOT grant or expand authority. A digest alone can detect mutation but does not prove trusted issuance. Phase 0 selected no final signing mechanism, and Phase 1 activation does not select or implement one.

Absent valid, unambiguous authorization, the defaults are `mode: plan-only` and `allowWrite: false`. `mode: plan-only` implies `allowWrite: false`; the combination of `mode: plan-only` and `allowWrite: true` is invalid and MUST be rejected. Future governed adapter execution, including plan-only execution, requires a valid bounded `TaskContract`.

## Pre-operational bootstrap maintenance

This section describes a temporary external root of trust; it does not make `AGENTS.md` authoritative. While the repository is pre-operational and the normal operational authorization path does not yet exist, an instruction supplied directly for the current task by the explicitly identified repository owner MAY provide narrow pre-operational `human-bootstrap-maintenance` authority for an implementation or repair task for this governance framework itself. That eligibility includes Phase 1 governance-core work; Phase 1 activation does not activate normal operational governance.

The instruction MUST identify exactly one repository and worktree, the expected branch and `HEAD` condition, the complete expected live file and Git status, the exact existing files and operations permitted, the prohibited Git actions, and the task-lifecycle or time limit. It MUST be repository-, worktree-, branch-, state-, path-, and operation-bounded; non-delegable unless delegation is explicit; non-reusable; and denied for everything not listed. Lower-trust input MUST NOT widen it. It MUST NOT be represented as ordinary task intent, a caller-created `TaskContract`, a `HostOverlay` permission, an `ExecutionReceipt`, this guide's decision, or an implemented policy-engine decision. Pre-operational `human-bootstrap-maintenance` authority is not a substitute runtime `TaskContract`; before a trusted issuer exists, a bootstrap task does not pretend to possess one.

Repository-root, branch, `HEAD`, status, path, allowed-file, worktree-registration, active-Git-operation, administrative-lock, remote, or operation-scope mismatches MUST fail closed. Bootstrap authority cannot waive those checks, logical role ownership, distinct-worktree requirements, the Schema-before-model sequence, current-baseline requirements, or administrative-action separation. It cannot authorize customer application work, unrelated feature work, another repository, another worktree unless separately and explicitly bound, production deployment, secret handling, automatic Git repair, branch switching or creation, worktree creation, staging, committing, or pushing. Authentication is cooperative: the development environment treats the interactive operator as the identified repository owner; this is not cryptographic identity proof, operating-system access control, or protection against a bypassing process.

An authorization expires at the end of its stated task or earlier on any mismatch. This pre-operational path MUST be retired or disabled when the project formally activates its operational governance and trusted contract-issuance path.

## Phase 1 worktree roles

`integration-control` owns phase decisions, cross-worktree coordination,
implementation sequencing, integration review, independent-audit gating, merge
readiness, promotion of approved baselines into `main`, release control, and
responsibility-boundary and escalation decisions. It does not own routine
Schema implementation, routine Python model implementation, Phase 2 routing,
runtime Git or lease implementation, or CLI or adapter implementation. `main`
is the control and integration baseline, not an ordinary implementation area.

`schema-contracts` owns `schemas/v1alpha1/**`, shared Schema definitions,
strict object envelopes, Schema-expressible structural constraints,
unknown-field rejection, types, formats, enums, required fields, local
structural invariants, conspicuously synthetic positive and negative Schema
fixtures, Schema validation and contract tests, and documentation changes
directly required to describe the finalized Schema contract. It does not own
Python models, decoding, canonical serialization, deterministic task
resolution, routing-policy execution, live Git inspection, runtime leases,
contract issuance, receipt generation, a CLI, adapters, or operational
enforcement. It MAY document semantic invariants for later enforcement but
MUST NOT implement Phase 2 routing behavior.

`model-implementation` owns typed representations corresponding to the approved
Schema contract, strict decoding, canonical serialization, model-level
validation that does not execute later control-plane behavior, model unit
tests, Schema/model conformance tests, and permitted static integrity checks. It
does not own Schema redefinition, task-intent resolution, `Project` selection,
`Domain` resolution, routing execution, role selection, host-binding execution,
live Git inspection, leases, contracts, receipts, a CLI, adapters, or
operational enforcement. A Schema mismatch MUST stop model implementation for
the affected contract and be routed back to `schema-contracts`.

`integration-control` is a third, distinct responsibility role.
`schema-contracts` and `model-implementation` implementation tasks MUST use
distinct worktrees. They MUST NOT be assigned to, implemented in, or allowed to
write through the same worktree. A free Schema worktree cannot be reused as the
model worktree.

For host-binding governance, `integration-control` owns the trusted inventory
boundary and set-wide acceptance sequencing for the
[complete same-host overlay set](docs/configuration-model.md#hostoverlay). One
individually valid `HostOverlay` is not an isolation proof. Every configured
overlay for the same `hostId` participates across all `projectRef` values, and
neither a task, caller, adapter, Project, nor selected overlay may omit another
same-host overlay. An incomplete inventory fails closed.

Only after every overlay is individually valid may Phase 1 statically compare
the union of their bindings and require host-wide `worktreeId` uniqueness and
exclusivity of each already-validated exact `(platform,
repositoryRoot.value)` identity. Different overlay identifiers do not waive
those requirements. Future Phase 3 must separately and freshly prove that the
same distinct bindings resolve to distinct canonical registered physical Git
worktrees; uncertainty denies execution. These are explanatory control-plane
requirements, not authority supplied by this document or a replacement for the
Schema-before-model sequence and distinct-worktree rules.

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
approved Schema baseline reaches `main`.

Logical worktree roles are portable governance concepts. Concrete local paths
are host-local and MUST NOT be committed. Branch creation, worktree creation or
binding, committing, merging, and pushing are separately authorized
repository-owner administrative actions. A Codex implementation task MUST NOT
create its own branch or worktree under the current pre-operational procedure.

## Required entry sequence

Before assigning or executing a task, an agent MUST read the current phase and
logical-role routing and all repository governance documents applicable to the
task, including [WORKTREE_GUARD.md](WORKTREE_GUARD.md), [the configuration
model](docs/configuration-model.md), and [the task
lifecycle](docs/task-lifecycle.md). A pre-operational bootstrap task MUST follow
the bootstrap preflight and stop conditions in the worktree guard. Ordinary
assignment and routing MUST remain within structured governance; preliminary
eligibility does not authorize execution.

For a Phase 1 implementation request, an agent MUST refuse routine Schema or
model implementation on `main` or in the `integration-control` worktree. It
MUST refuse to assign Schema and model implementation to the same worktree and
MUST refuse model implementation until the approved Schema baseline has been
committed, reviewed, and integrated into `main` and a distinct model worktree
has been created or bound from that updated baseline by a separately authorized
repository-owner administrative action. Phase 1 work is limited to structural
and static configuration/model integrity validation; broad operational
resolution, routing, runtime, authorization, contract, and receipt semantics
remain later-phase work. A model-role Schema mismatch MUST stop the affected
work rather than redefine Schema semantics.

For an ordinary governed task after the operational path exists, an agent MUST:

1. Resolve exactly one `Project` and a non-empty deterministic set of `Domain` identifiers. Use `RoutingPolicy` to select exactly one `WorktreeRole` that owns every `Domain` in that set, then bind exactly one target worktree. If no unique role covers the complete set, split the work into independently authorized tasks or deny it. A free worktree with the wrong role is not a valid target.
2. Validate the applicable structured governance and resolved task intent. Missing, malformed, ambiguous, stale, or mismatched authority MUST deny routing or implementation.
3. Observe Git and worktree state live and apply every check in [WORKTREE_GUARD.md](WORKTREE_GUARD.md). Cached state and prior receipts MUST NOT substitute for inspection.
4. For a proposed write task, require evaluated effective permission of `allowWrite: true`, atomically acquire the task-owned write lease, and perform post-acquisition, pre-contract-issuance revalidation. Lease availability or possession is not authority.
5. Require a valid, provenance-checked `TaskContract` issued by trusted framework logic or accepted through trusted issuer validation only after the successful checks and revalidation, then perform post-contract, immediately-before-action revalidation. The contract MUST bind the same complete `Domain` set. No preliminary decision or lease is execution authority.
6. Operate only within the contract's target, `Domain` set, permissions, and scope; perform post-execution scope and state verification; capture pre-release evidence; attempt ownership-checked lease release; record the release outcome; finalize the evidence-only `ExecutionReceipt`; and attempt to persist or deliver it outside portable governance.

An execution outcome never implies lease release. An unreleased, malformed, ambiguous, stale, or otherwise unresolved lease remains blocking regardless of whether execution succeeded, failed, was cancelled, was denied, or was indeterminate. Competing writers MUST remain denied until ownership-checked release succeeds or a separately authorized operator-resolution procedure completes. The framework MUST NOT break the lease automatically.

At every gate, uncertainty or disagreement between expected and observed state MUST fail closed. The agent MUST stop and report the denial; it MUST NOT repair Git state, reinterpret authority, expose secrets, or continue on an inferred exception.
