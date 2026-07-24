# Planned test strategy

Phase 0 documentation bootstrap is complete at baseline commit
`79cc9d77fd48410f37645afdb429a7cd2e34a0bd`. Phase 1: Schemas and
Models is current, but Phase 1 implementation has not yet begun. The repository
remains pre-operational, and no tests or fixtures exist yet. Future tests MUST
be deterministic and MUST use sanitized synthetic data. The planned Schema
contract, static-validation vectors, and fixture inventory are recorded in the
[v1alpha1 Schema contract design](../docs/schema-contract-v1alpha1.md).

## Validator and toolchain gate

No validator has been selected, and no `pyproject.toml`, dependency
declaration, transitive lock, or approved executable test environment exists.
Executable Schema tests and Schema implementation remain blocked until
`integration-control` approves the validator, packaging, lock, provenance,
license, and release decisions. `schema-contracts` owns the validator
capability requirements and future conformance vectors. Ad hoc imports,
globally installed packages, and untracked environments are not accepted.

Planned Phase 1 tests are limited to strict parsing prerequisites, JSON Schema
structure, offline reference resolution, canonical representation checks, and
closed-bundle static integrity. Task resolution and RoutingPolicy execution
remain Phase 2; live Git, worktree, and lease tests remain Phase 3; trusted
contract, scope-verification, sanitization, receipt, and delivery tests remain
Phase 4; CLI and adapter tests remain Phases 5 and 6.

## Phase 1 test order and ownership

Schema-contract testing comes first. A later, separately authorized
`schema-contracts` task in its dedicated worktree owns conspicuously synthetic
positive and negative Schema fixtures, Schema validation, and Schema contract
tests. The Schema baseline must then receive independent read-only audit,
approval through `integration-control`, and committed, reviewed integration
into `main`.

Only after that integration may the repository owner create or bind a distinct
`model-implementation` worktree from the updated `main`. That role owns model
unit tests and Schema/model conformance tests against the approved Schema
contract. The two implementation roles MUST NOT share a worktree, and a Schema
mismatch discovered during model work MUST stop the affected model work and be
routed back to a separately authorized `schema-contracts` task.

Phase 1 testing is limited to Schema structure and static configuration/model
integrity. Tests for actual task resolution and routing, live Git and worktree
inspection, runtime coordination and leases, trusted contract issuance and
receipt generation, CLI behavior, and agent adapters remain planned for Phases
2 through 6; they are not Phase 1 implementation.

## Categories

- **Unit tests:** parsing, validation, resolution, policy evaluation, state comparison, and scope matching in isolation.
- **Contract tests:** compatibility between public configuration objects, `TaskContract` records, adapter boundaries, and `ExecutionReceipt` records.
- **Integration tests:** the complete ordered lifecycle from untrusted task intent, through resolution and execution, to lease release and receipt finalization.
- **Concurrency tests:** competing write tasks, exclusive lease acquisition, lease release, stale owners, and state changes during revalidation.
- **Fixture tests:** reusable synthetic repositories and governance inputs representing valid and invalid states.
- **Golden tests:** stable diagnostics, denial reasons, normalized contracts, and sanitized receipts reviewed as intentional output changes.

Contract tests MUST prove that a `TaskContract` has authority only after trusted framework issuance or validation of trusted issuer, integrity, derivation, task and target binding, freshness, and current policy, runtime, and lease preconditions. A caller-, adapter-, or task-supplied claim MUST remain untrusted, and a digest alone MUST NOT be accepted as proof of issuance. Phase 0 selects no final signing mechanism.

Tests MUST prove that future governed adapter execution, including plan-only execution, requires a valid bounded `TaskContract` and rejects a missing, invalid, stale, or unbounded contract. They MUST also prove that pre-operational `human-bootstrap-maintenance` authority is not accepted as a runtime `TaskContract`.

Future `ExecutionReceipt` contract coverage MUST exercise both closed receipt-origin branches and the conditional presence of contract fields. It MUST cover pre-contract denials before and after lease acquisition, require acquisition binding only for a proven acquired lease, require applicable cleanup or indeterminate release evidence for acquired or indeterminate acquisition state, and reject both fabricated contract binding and successful-execution claims in pre-contract denial receipts. This coverage preserves optional policy-required pre-contract denial receipts without duplicating the field-level design recorded in the Schema contract.

### Path-keyed baseline and postcondition entries

Future Phase 1 static and contract tests MUST prove that the repository-relative path is the sole identity, uniqueness, and canonical ordering key, `S(entry.path)`, for `TaskContract` baseline index, tracked, and submodule entry arrays and every corresponding entry array nested in required postconditions. Two entries with the same path MUST be rejected even when their remaining fields differ, including index mode, stage, object identity, or other index-entry state; tracked object identity, mode, status, or other tracked-entry state; submodule object ID, branch or ref information, or dirty state; or required-postcondition entry contents.

`J(entry)` MAY be used only for deterministic diagnostic comparison after path uniqueness is established. It MUST NOT participate in entry identity, uniqueness, or canonical ordering, and differing full-object bytes MUST NOT make duplicate paths valid.

Tests MUST prove that duplicate-path rejection occurs after strict parsing and applicable structural validation, during Phase 1 static validation, and before canonical digest projection, RFC 8785 JCS serialization, and hashing. A duplicate path MUST NOT reach hashing as a valid instance.

Planned negative coverage MUST include:

- duplicate baseline index path with different entry contents;
- duplicate baseline tracked path with different entry contents;
- duplicate baseline submodule path with different object IDs or dirty state; and
- duplicate nested required-postcondition entry path with different contents.

Untracked and ignored path arrays MUST remain unique and canonically ordered by `S(path)`. Path arrays nested in postconditions MUST retain their applicable `S(path)` rule. This test-plan synchronization does not change the design record's [array-ordering contract](../docs/schema-contract-v1alpha1.md#11-complete-array-ordering-matrix).

### SG-001 closure coverage

Future Schema and static-contract coverage MUST implement every row of the
design record's [mandatory exhaustive fixture/conformance
matrix](../docs/schema-contract-v1alpha1.md#mandatory-exhaustive-sg-001-fixtureconformance-matrix).
That requirement remains planned and does not imply that the design is
approved, a validator is selected, or any fixture or executable test exists.

The required future coverage includes, concisely:

- the conflict-free stage-0 `TaskContract` index profile, including clean,
  non-empty exact, and empty exact complete inventories;
- fail-closed pre-contract denial of unmerged, intent-to-add, skip-worktree,
  assume-unchanged, sparse, unsupported-mode, and otherwise unrepresentable
  index states;
- complete-inventory rather than delta semantics for every exact baseline and
  the canonical meanings of every clean or none branch;
- index, tracked, submodule, untracked, and ignored cross-dimension
  consistency, coverage, equality, and exact-path disjointness at the
  appropriate Phase 1 static or Phase 3 live layer;
- the equality required for `tracked.modified` and inequality required for
  `tracked.type-changed` worktree/index modes, plus every other tracked status
  branch invariant;
- all four allowed `TaskContract` requested-mode, effective-mode, write,
  lease-required, lease-ID, and lease-state rows and every invalid combination;
- same-receipt `relatedCheckId` integrity, including absent, forward, backward,
  dangling, cross-receipt, duplicate-check, and delivery-result cases;
- exhaustive positive and applicable negative coverage for every ref/HEAD,
  baseline, transition, postcondition, warning, check, outcome, and
  lease-acquisition branch;
- required `preContractEvidence.sanitizedSummary` and
  `ReceiptDeliveryResult.sanitizedSummary` presence while warning and check
  summaries retain their designed optionality;
- the material pre-publication five-state lease-acquisition correction:
  `not-required`, `not-attempted`, `not-acquired`, `indeterminate`, and
  `acquired`; and
- the preserved `profile.number.v1alpha1-r1` numeric contract with Git index
  stage range exactly `0..0`, stage `0` valid, and stages `1` through `4`
  invalid.

### Closed runtime and numeric-profile conformance

Future Phase 1 Schema and static contract coverage MUST exercise the exact
closed runtime representations in the design record. Baseline fixtures MUST
cover all nine required dimensions; the conflict-free stage-0 clean, non-empty
exact, and empty exact index forms; every tracked, submodule,
active-operation, and administrative-lock branch; and rejection of missing or
unknown dimensions, branch-inapplicable fields, stage `1` through `4`,
unsupported index modes and flags, unmerged or sparse index state, and duplicate
path or lock identities. The complete-inventory clean, none, and exact forms
must remain canonical and unambiguous.

Every one of the nine permitted-transition branches and eleven
required-postcondition branches requires positive coverage. Negative coverage
MUST reject identical `from`/`to` values, missing target keys, unknown
transition types, duplicate transition targets, duplicate postcondition types,
and a missing or repeated `scope-contained` postcondition. Transition target
and postcondition type uniqueness MUST be established before digest projection
or hashing.

Receipt vectors MUST cover warning records with and without optional fields,
all check types, contiguous warning/check sequences, unique check IDs, ordered
reason-code sets, and every same-receipt `relatedCheckId` success and failure
case independent of sequence position. Issued-contract vectors MUST exercise successful,
denied-before-action, failed, cancelled, and indeterminate outcomes under the
exact precedence rules; failed or indeterminate release without an unresolved
coordination warning MUST be rejected. Pre-contract-denial vectors MUST cover
every permitted checkpoint/acquisition-state pair, reject every unlisted pair,
and cover acquired-lease cleanup that succeeds, fails, or remains indeterminate.
Impossible execution, verification, release, lifecycle, and unresolved-warning
combinations MUST be rejected deterministically.

The selected `v1alpha1-r1` number profile accepts only raw JSON number tokens
matching `0|[1-9][0-9]*`, with a universal maximum of
`9007199254740991`. Planned boundary vectors MUST cover RoutingPolicy
priority, remote port, Git index stage `0..0`, warning and check sequence, and
receipt redaction-count minima and maxima, plus their first out-of-range values.
Stage `0` is the sole valid Git index-stage vector; stages `1`, `2`, `3`, and
`4` are invalid. The vectors MUST reject negative and negative-zero forms,
leading plus or zeroes,
fractions, exponent forms, unsafe integers, NaN, Infinity, and equivalent
permissive-parser extensions in every numeric field.

Raw numeric-token validation and duplicate-key detection MUST occur during
strict parsing before ordinary decoding, Schema validation, static validation,
array checks, digest projection, JCS, or hashing. Planned conformance coverage
MUST prove no precision loss through parsing, model transfer, RFC 8785 JCS, or
replay; produce identical digest vectors across supported runtimes; combine
official RFC 8785 vectors with project-specific numeric boundaries; and reject
a generic decoded object that lacks trusted proof of strict profile parsing.
Validator research must prove this selected profile and MUST NOT choose or
weaken it. All coverage in this section remains planned and unimplemented.

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
- invalid receipt-origin combinations, including conditional contract-field violations, pre-contract denial around lease acquisition, and inconsistent cleanup or release evidence;
- an `ExecutionReceipt` being presented as authorization input;
- invalid in-worktree concrete `HostOverlay`, `TaskContract`, receipt, lock, lease, or runtime-state artifacts even if an ignore rule would otherwise hide them; and
- secrets or machine-specific runtime data appearing in diagnostics, fixtures, golden files, logs, or receipts.

Worktree-role ownership of the complete `Domain` set and runtime write leases MUST be exercised as independent controls. Tests MUST prove that execution outcome and lease liveness are independent and that generated receipts remain outside portable governance. Terminal processing MUST attempt to record a sanitized `ExecutionReceipt` for every issued-contract execution attempt; pre-contract denial receipts MAY remain policy-optional. Tests MUST NOT rely on automatic branch switching, branch creation, stashing, reset, cleaning, restoration, fetching, pulling, merging, rebasing, lease or lock breaking, or Git-state repair.
