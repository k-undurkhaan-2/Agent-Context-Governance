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

**Phase 0: Documentation Bootstrap** is complete at baseline commit `79cc9d77fd48410f37645afdb429a7cd2e34a0bd`. **Phase 1: Schemas and Models** is current. Its activation records the next bounded area of work; it does not mean Phase 1 implementation is complete or has begun.

The repository remains pre-operational. It has no Schema implementation,
Python model, test, fixture, package release, normal policy engine, trusted
`TaskContract` issuer, lease manager, Git inspector, CLI, adapter, enforcement
mechanism, or cryptographic authorization. Phase 1 activation is not
operational-governance activation, and the first Schema or model artifact
requires a later, separately authorized implementation task.

### Review-14 A control-governance decision

The repository owner selected exactly:

```text
A-REGISTRY-SCOPE-01 = OPTION-A
```

Review 14 identified cross-overlay worktree exclusivity as a P1 finding. The
owner selected comparison of every configured `HostOverlay` for one `hostId`
across all Projects, using a trusted closed host-local configuration inventory.
This candidate changes only control governance. It does not fully close
Review-14 A: the normative Schema-contract mirror and A-family fixture/test-plan
coverage remain pending in a separate, later-authorized `schema-contracts`
task and worktree. Review-14 B and Review-14 C remain unresolved. No merge,
Schema implementation, model-worktree creation, or model implementation
authority follows from this decision or candidate.

Phase 1 scope is exactly:

- public JSON Schema definitions under `schemas/v1alpha1/`;
- shared Schema definitions;
- strict object envelopes;
- Schema-expressible structural constraints and unknown-field rejection;
- types, formats, enums, required fields, and local structural invariants;
- conspicuously synthetic positive and negative Schema fixtures;
- in-memory typed models;
- strict decoding;
- canonical serialization;
- Schema validation and contract tests;
- model unit tests and Schema/model conformance tests; and
- bounded static configuration/model integrity checks.

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

The two implementation roles MUST use distinct worktrees. The model worktree
MUST NOT be created from the Phase 0 baseline or before the approved Schema
baseline reaches `main`, and a free Schema worktree cannot be reused for model
implementation.

### Static and operational validation boundary

Phase 1 MAY implement JSON Schema structural validation; unknown-field,
supported-version, type, format, enum, range, and required-property checks;
object-local invariants; deterministic decoding; canonical serialization;
Schema/model conformance; closed-bundle ID and reference integrity; and static
restriction or model invariants that do not calculate an operational result or
require task intent, task-specific host-binding resolution, Git state, lease
state, or runtime decisions. Phase 1 static integrity may validate each
`HostOverlay` individually and then validate cross-resource binding
injectivity over an already-established complete same-host overlay set; it
does not select a concrete binding or prove a physical worktree identity.

Phase 1 MUST NOT execute task-intent resolution, actual `Project` or `Domain`
resolution, `RoutingPolicy` evaluation, role selection, split-versus-deny
decisions, concrete host binding, operational authorization, live Git
inspection, lease coordination, trusted runtime contract issuance or
validation, or receipt generation. Deterministic resolution and routing belong
to Phase 2, live Git and leases to Phase 3, contract and receipt lifecycle work
to Phase 4, CLI work to Phase 5, and adapters to Phase 6.

Phase 1 excludes deterministic task routing implementation, live Git inspection, runtime write leases, `TaskContract` issuance, `ExecutionReceipt` generation, a CLI, agent adapters, operational enforcement, and cryptographic authorization. The normal operational governance and trusted contract-issuance path therefore still do not exist.

## Pre-operational bootstrap authority

The pre-operational repository has narrow pre-operational
`human-bootstrap-maintenance` authority as a temporary external root of trust
for implementing or repairing the governance core that the future operational
path will depend on. This exception remains necessary during Phase 1 because
the normal operational authorization path, policy engine, lease manager, and
trusted `TaskContract` issuer do not yet exist and therefore cannot authorize
their own implementation.

The participants remain distinct:

| Participant | Trust and authority while pre-operational and later |
| --- | --- |
| Human bootstrap administrator | The explicitly identified repository owner MAY supply a task-specific `human-bootstrap-maintenance` instruction for implementation or repair of this governance framework itself while the normal operational path is absent. This is the temporary pre-operational root of trust, not a normal runtime caller role. |
| Ordinary caller | Requests an outcome and MAY narrow it, but task prose, `ALLOW_WRITE`, and caller-supplied objects cannot grant or expand authority. |
| Future trusted governance core | Will validate portable structured governance, apply host restrictions, inspect live state, coordinate leases, and issue or validate bounded `TaskContract` records for ordinary operational execution. None of this is operational when Phase 1 is activated. |
| Future agent adapter | Will consume a valid `TaskContract` as a less-trusted product boundary. It cannot issue authority, widen scope, or turn ordinary intent into permission. Agent adapters are outside Phase 1. |

A valid bootstrap instruction MUST be supplied directly for the current task by the repository owner and bind exactly one repository and worktree, the branch and expected live state, an exact allowed-file and operation set, prohibited Git actions, and an expiry. It MUST be task-, repository-, worktree-, branch-, state-, path-, operation-, and lifetime-specific; non-delegable unless explicitly allowed; non-reusable; and deny everything not listed. Lower-trust input MUST NOT widen it. Repository, branch, state, path, worktree, remote, or Git-operation mismatches fail closed and cannot be waived by the instruction.

The bootstrap instruction exists outside the future governed task-execution path. It MUST NOT be represented as ordinary task intent, a caller-created `TaskContract`, a `HostOverlay` grant, an `ExecutionReceipt`, an agent-guide decision, or an implemented policy-engine result. Pre-operational `human-bootstrap-maintenance` authority is not a substitute runtime `TaskContract`; before the trusted issuer exists, bootstrap maintenance does not pretend to possess one or acquire a framework lease.

This cooperative authority does not permit customer application work, unrelated feature work, another repository, another worktree unless separately and explicitly bound, production deployment, secret handling, automatic Git repair, branch switching or creation, worktree creation, staging, committing, or pushing. It also cannot bypass role ownership, distinct-worktree requirements, Schema-before-model sequencing, current-baseline requirements, or administrative-action separation. The interactive environment's treatment of the current human as the identified repository owner is an operational assumption, not cryptographic authentication or an operating-system security boundary.

Each bootstrap authorization expires at task completion or earlier on mismatch. The path MUST be retired or disabled when the project formally activates the operational authorization path. Phase 1 activation is not that retirement milestone. The future operational activation decision must identify the trusted governance source and issuer and separately define administrative recovery and any emergency process; bootstrap wording cannot silently become a permanent owner override.

## Phase 1 logical worktree roles

Phase 1 establishes three portable logical roles without committing concrete local worktree paths:

| Role | Ownership and boundary |
| --- | --- |
| `integration-control` | Owns phase decisions, cross-worktree coordination, implementation sequencing, integration review, independent-audit gating, merge readiness, promotion of approved baselines into `main`, release control, and responsibility-boundary and escalation decisions. It does not own routine Schema or Python model implementation, Phase 2 routing, runtime Git or lease implementation, or CLI or adapter implementation. `main` is the control and integration baseline, not an ordinary implementation area. |
| `schema-contracts` | Owns `schemas/v1alpha1/**`, shared definitions, strict envelopes, Schema-expressible constraints, unknown-field rejection, field constraints and local invariants, conspicuously synthetic positive and negative fixtures, Schema validation and contract tests, and directly required Schema documentation. It does not own Python models, decoding, canonical serialization, task resolution, routing execution, live Git, leases, contracts, receipts, a CLI, adapters, or operational enforcement. It may document later semantic invariants but cannot implement Phase 2 routing behavior. |
| `model-implementation` | Owns typed representations of the approved Schema contract, strict decoding, canonical serialization, bounded model validation, model unit tests, Schema/model conformance tests, and permitted static integrity checks. It does not own Schema redefinition, task-intent or Project/Domain resolution, routing, role or host-binding decisions, live Git, leases, contracts, receipts, a CLI, adapters, or operational enforcement. A Schema mismatch stops affected model work and routes back to `schema-contracts`. |

`integration-control` is a third responsibility role distinct from the two
implementation roles. `schema-contracts` and `model-implementation`
implementation tasks MUST use distinct worktrees and MUST NOT be assigned to,
implemented in, or allowed to write through the same worktree.

For the owner-selected Review-14 A semantics, `integration-control` owns the
trusted closed inventory boundary, the same-host collection boundary, set-wide
gate sequencing, fail-closed handling when completeness is unavailable, and
integration/review gating. A later separately authorized `schema-contracts`
task owns the normative Schema mirror and A-family fixtures. This candidate
grants no authority to `model-implementation`.

Logical worktree roles are portable governance concepts. Concrete local paths
are host-local and MUST NOT be committed. Branch creation, worktree creation or
binding, committing, merging, and pushing remain separately authorized
repository-owner administrative actions. A Codex implementation task MUST NOT
create its own branch or worktree under the current pre-operational procedure.

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

One individually valid overlay is not host-wide isolation evidence. Before one
of its bindings is eligible, the control plane must establish the
[complete same-host overlay set](docs/configuration-model.md#hostoverlay),
validate every member, and validate binding injectivity across their union,
including across Project boundaries. Incomplete or ambiguous inventory denies.

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

For future ordinary operational execution, structured governance is the normative policy source. The adapter-facing [AGENTS.md](AGENTS.md) MAY summarize entry requirements, but it cannot grant permissions beyond structured governance and a valid `TaskContract`. Documentation and `ExecutionReceipt` records are not authorization sources. The temporary pre-operational root described above is external to these documents and does not make them policy.

All seven kinds use API version `contextctl.dev/v1alpha1`; schema definitions for all of them MAY later live under `schemas/v1alpha1/`. Physical placement and trust follow the families above, not the schema directory.

## Authorization boundary

Future write authorization MUST require all applicable controls to agree:

1. Customer governance permits the requested operation for exactly one resolved `Project` and a non-empty deterministic `Domain` set.
2. Exactly one selected `WorktreeRole` owns every `Domain` in that set.
3. The complete same-host overlay set is known and valid, its binding union is
   injective, and the selected `HostOverlay` successfully binds one target
   without denying or widening the request.
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

The initial configuration API is `contextctl.dev/v1alpha1`. Phase 1 schema files will live under [`schemas/v1alpha1/`](schemas/README.md). Phase 1 activation does not include finished JSON Schemas or configuration objects.

## Project boundaries

The core MUST remain agent-neutral. A future Codex integration MAY be implemented as an adapter, but it MUST NOT be introduced into core policy or domain logic.

Real host paths, concrete `HostOverlay` data, concrete runtime artifacts, runtime coordination state, leases, and locks MUST remain outside the target worktree. Portable governance intended for review and version control will be distinct from those local resources. Generated receipts MUST remain outside portable governance. Secrets MUST remain outside every governance and evidence surface described above.

The framework is a cooperative control plane. Its policies cannot stop a process that bypasses the framework or has sufficient direct access to mutate a repository. The [security model](SECURITY.md) describes this limitation and the expected trust boundary.
