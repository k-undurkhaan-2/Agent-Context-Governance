# Public configuration schemas

Phase 0 documentation bootstrap is complete at baseline commit
`79cc9d77fd48410f37645afdb429a7cd2e34a0bd`. Phase 1: Schemas and
Models is current, but Phase 1 implementation has not yet begun. The repository
remains pre-operational, and this directory contains no Schema implementation.
The v1alpha1 Schema contract design is recorded in
[the Schema contract design](../docs/schema-contract-v1alpha1.md).
The recorded history identifies independent design audit and
`integration-control` approval of the prior candidate as complete, the six
earlier review findings as repaired and closed, and the three third-review
repairs as recorded at commit
`9eac3e040a8d0f9c959eeb675eace795749e422a`.

The fourth Codex review `PRR_kwDOThD5p88AAAABHQ0C0g` at exact HEAD
`df9b6eca8ad60aaf9e496688d936a5f97ce25c2b` identified two accepted P1
findings: active-operation issued-contract inconsistency in thread
`PRRT_kwDOThD5p86T4aiK` and pre-action freshness relative to contract expiry
in thread `PRRT_kwDOThD5p86T4aiM`. This revision records the proposed repairs
for those two findings. Administrative-lock semantics remain unchanged.

Independent re-audit, commit, push, exact-head confirmation, owner replies,
thread resolution, PR synchronization, re-review, merge-readiness review,
implementation, and merge remain external gates and actions. This Markdown
neither proves nor replaces external GitHub, audit, or authorization state.
No Schema or model implementation is authorized.

All 11 resources remain `reserved-unpublished`; the validator/toolchain and
Schema-before-model gates remain binding. The exact UUID-URN catalog reserves
identifiers but does not publish or implement Schema resources, and no Schema
artifact exists.

The initial public configuration API version is `contextctl.dev/v1alpha1`.
Future Schema definitions will live under `schemas/v1alpha1/`. Configuration
API versions MUST evolve independently of package release versions, which will
use Semantic Versioning.

No Schema implementation may begin until `integration-control` has approved
the validator/toolchain, packaging, dependency lock, provenance, licensing,
security, and release gate. The first Schema artifact then requires a fresh,
separately authorized `schema-contracts` task in this dedicated role worktree.
No model worktree or model implementation exists. Model-worktree creation
remains prohibited until the approved Schema baseline is integrated into `main`.

## Phase 1 ownership and boundary

`schema-contracts` owns `schemas/v1alpha1/**`, shared Schema definitions,
strict object envelopes, Schema-expressible structural constraints,
unknown-field rejection, types, formats, enums, required fields, local
structural invariants, conspicuously synthetic positive and negative Schema
fixtures, Schema validation and contract tests, and documentation changes
directly required to describe the proposed Schema contract through approval.

Within the Phase 1 boundary established by ADR 0005, `schema-contracts`
specifies the normative pipeline and validated-canonical-representation
contract, digest projection catalog and framing, recorded canonical bytes and
digests, JSON Schema structural constraints, static invariants over
already-decoded closed values, and expected positive and negative vectors. It
MAY cover supported API-version checks; field type, format, enum, range, and
required-property validation; object-local invariants; and Schema-expressible
or closed-bundle-static ID, reference, canonical-array, restriction, routing,
and branch-policy checks.

`schema-contracts` does not implement or claim executable coverage for strict
decoding, duplicate-key or raw-number-token rejection, NFC validation, the
immutable validated representation, typed models, canonical serialization,
digest projection, RFC 8785 JCS, hashing, verification, replay, typed round
trips, Schema/model conformance, or cross-runtime byte reproduction. Those
executable codec/model responsibilities belong to the future distinct
`model-implementation` role. Deterministic task resolution and
`RoutingPolicy` execution remain Phase 2; live branch, HEAD, Git/worktree, and
lease enforcement remain Phase 3; and trusted replay, issuer provenance,
authority, contract verification, receipt generation, and delivery remain
Phase 4.

The Schema baseline MUST be designed, independently audited, approved through
`integration-control`, committed, reviewed, and integrated into `main` before a
distinct `model-implementation` worktree is created or bound from that updated
`main` by a separately authorized repository-owner action. Schema and model
implementation tasks MUST NOT share a worktree. `integration-control` owns the
independent approval, toolchain, dependency, packaging, licensing, release,
and cross-worktree gates; this design repair does not authorize either
implementation task.

## Retained third-review repair contract

This retained design record documents three accepted third-review repairs; it
does not create a Schema, fixture, validator, model, or runtime behavior.

For an `issued-contract` receipt validated with its complete referenced
TaskContract, future Phase 1 static conformance requires exact equality of
receipt `contractId` to contract `metadata.id`; receipt `contractDigest` to
the recomputed `profile.digest.task-contract-v1` value; receipt `taskId` to
contract `spec.taskId`; every Project, role, logical worktree, and complete
ordered Domain member in `resolvedTarget` to its TaskContract source; and
receipt `effectiveMode` to contract `spec.effectiveMode`. The exact
non-digest target projection is:

```text
{
  projectRef: contract.spec.projectRef,
  worktreeRoleRef: contract.spec.target.worktreeRoleRef,
  worktreeId: contract.spec.target.worktreeId,
  domainRefs: contract.spec.domainRefs
}
```

Both complete artifacts and the TaskContract derivation prerequisites validate
before its cataloged digest is recomputed. All eight equalities, chronology,
and outcome/release consistency validate before receipt-digest acceptance.
Delivery binding and chronology validate only after receipt finalization. No
new digest or `TaskContract.spec.taskContractDigest` field is introduced, and
a mismatch is invalid rather than normalized, repaired, reclassified, or
matched to another contract.

The shared `canonicalUtcTimestamp` accepts only whole-second UTC strings
matching:

```text
^[0-9]{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])T(?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]Z$
```

Future Schema uses `type: string`, that exact pattern, and asserted
`format: date-time`. Phase 1 additionally enforces years `0001` through
`9999`, Gregorian date and leap-year validity, and all 12 chronology
relations. Lower-case delimiters, offsets, fractions, leap seconds,
`24:00:00`, whitespace, alternate spellings, and repair are forbidden. The
profile applies to the three TaskContract timestamps, receipt `startedAt`,
`finishedAt`, `sanitization.completedAt`, every `checks[].observedAt`,
the pre-contract origin's `preContractEvidence.observedAt`, and
`ReceiptDeliveryResult.attemptedAt`: exactly nine paths.

A structured remote remains the closed
`{ transport, host, port?, namespace, repository }` record. Transport is
`https` or `ssh`. The selected `remoteDnsHost` accepts 3-through-253
character lower-case ASCII DNS names with at least two 1-through-63 character
labels; it rejects single labels, `localhost`, IP literals, Unicode, IDNA or
`xn--`, trailing dots, and normalization. Omitted ports mean exactly HTTPS
443 or SSH 22, explicit default ports are invalid, and an included non-default
port remains an integer from 1 through 65535 under the existing numeric
profile.

Namespace is an ordered array of 1 through 16 lower-case ASCII segments, each 1
through 63 characters, with joined length at most 1023 and no empty, dot,
dot-dot, `..`-containing, separator, whitespace, control, uppercase, or Unicode
segment. The distinct `remoteRepositoryName` is one 1-through-128 character
lower-case ASCII segment with alphanumeric endpoints, the same internal
`[a-z0-9._-]` vocabulary, no `..`, separators, whitespace, controls,
uppercase, Unicode, or leading/trailing dot or hyphen, and no terminal `.git`.
Validators do not normalize, sort, add or remove ports, strip or append
`.git`, or parse either value as a path.

Validated remote identity remains exact `J(remote)`, equivalently the exact
transport, host, effective port, ordered namespace, and repository tuple.
`acceptedRemotes` is set-like, duplicate-free, and already strictly ordered
by `J(remote)`; outer remote expectations remain keyed and ordered by only
`remoteName`. HostOverlay narrowing uses exact validated membership without
aliases or ignored fields. The design and test plan record all five positive
and 18 negative receipt vectors, ten positive and 24 negative timestamp
vectors, and 15 positive and 61 negative remote vectors.

These repairs apply the existing universal pipeline in this effective
dependency order: strict bytes/tokens; timestamp and remote lexemes; Schema
structure; local Phase 1 invariants; array and remote order; validated
representation; digest projection/computation; complete TaskContract digest;
receipt/contract equality; chronology/pre-action freshness/outcomes; receipt
digest; then delivery binding/chronology. They do not replace or alter that protected pipeline.
`schema-contracts` specifies the structural/static contract and vectors;
future `model-implementation` owns executable codec, projection, hashing, and
cross-artifact conformance; Phase 3 owns live remote and host facts; and Phase 4
owns trusted provenance, authority, time, freshness, and evidence truth.

## Fourth-review proposed repairs

The TaskContract still materializes nine baseline dimensions.
`expectedBaseline.activeOperations` is exactly `{ "state": "none" }`; its
reusable non-empty exact union remains available only for non-authorizing
observation and evidence. Administrative-lock contract semantics are unchanged:
`expectedBaseline.administrativeLocks` retains the complete
`administrativeLocksCondition` union, the `administrative-lock` transition
remains available, and the matching postcondition reuses the full condition.
A present live Git administrative lock still denies at the governing guard
checkpoint and remains distinct from a runtime write lease, lease-store lock,
or command-internal transient lock.

`permittedTransitions` has exactly eight branches: `ref-state`,
`head-state`, `index-entry`, `tracked-entry`, `untracked-path`,
`ignored-path`, `submodule-entry`, and `administrative-lock`. The
required-postcondition union remains at eleven branches. Its optional
`active-operations` branch is none-only and is not newly mandatory; its
`administrative-locks` branch retains the complete condition grammar.
Simultaneous composition applies the eight permitted transitions while
reconstructing one final nine-dimension composite in which active operations
remain none and administrative locks follow their ordinary condition semantics.

A non-empty active operation at initial or pre-issuance revalidation denies
before a contract exists. At post-contract immediately-before-action
revalidation it permits no protected action and any issued receipt uses
`not-attempted/not-performed`. At post-execution verification it is unexpected
terminal evidence with failed or indeterminate verification, never an
authorized final postcondition. Administrative-lock live denial is a separate
guard rule and does not narrow its baseline, transition, or postcondition
contract.

For an issued-contract receipt, let `P` be every
`pre-action-revalidation` check and `A` the passed members of `P`. Every
{succeeded, failed, cancelled, indeterminate} execution attempt requires at
least one member of `A`, and every member of `A` must be strictly before
`TaskContract.spec.freshness.expiresAt`. Failed and indeterminate pre-action
checks may coexist with valid passed/pre-expiry evidence. An attempted receipt
with only failed checks, only indeterminate checks, or no passed check is
invalid. Equality at expiry and any later passed check are invalid for every
outcome.

A `not-attempted` receipt may omit pre-action checks and may retain failed or
indeterminate denial evidence at or after expiry; any passed check must still
be strictly pre-expiry. Receipt completion and later lifecycle stages may occur
after expiry. `startedAt` is not proof of action freshness, no
`finishedAt <= expiresAt` rule exists, and check sequence creates no
additional freshness or chronology relation. The expiry/check inventory is
exactly eight positive and 17 negative classes.

The corrected inventory is: nine baseline dimensions; eight transitions;
eleven postconditions; 54 array-ordering rows; 25 SG-001 rows; D5 with exactly
24 `3 × 8` negatives; nine timestamp paths; 12 chronology relations; eleven
digest-bearing paths; ten digest computations; one receipt/delivery digest
copy; five positive and 18 negative receipt-binding vectors; eight
receipt/contract equalities; six numeric fields; and eleven catalog resources.
Timestamp lexical vectors remain 10 positive and 24 negative.

The active-operation legacy contract family is exactly 21 cases: seven
single-operation exact baselines, seven retired active-operation transitions,
and seven single-operation exact postconditions. Duplicate, unknown,
non-canonical, and empty-exact observation cases form a separate generic shape
family and do not inflate that 21. Administrative-lock vectors retain ordinary
positive baseline, transition, and postcondition coverage plus their existing
identity, branch-field, uniqueness, order, and empty-exact negatives.

The repaired synthetic receipt projection is 1355 UTF-8 bytes and its completed
form is 1445 UTF-8 bytes. Its independently recomputed digest is
`sha256:0bdca1267e2e9d983565587b03a8cb8185b69e4f00271d897435661e974f2f77`,
and the delivery result copies that value without a new computation. The
protected corpus retains five distinct timestamp values across 18 occurrences
and seven structured-remote occurrences. The universal twelve-step pipeline,
all eleven digest selectors, ten profiles/computations, framing, separators,
dependency graph, the other nine digest results, API/revision/version values,
resource IDs, filenames, UUID URNs, and `reserved-unpublished` statuses remain
unchanged.

This section records design-only requirements and planned vectors. It creates
no Schema, fixture, validator, executable test, model, codec, runtime behavior,
or authority. Independent audit and later gate outcomes are recorded outside
this repository when performed; this README neither asserts their current state
nor replaces those records. No Schema or model implementation is authorized.

## Object families and later validation

Schema definitions for all seven kinds—`Project`, `Domain`, `WorktreeRole`,
`HostOverlay`, `RoutingPolicy`, `TaskContract`, and `ExecutionReceipt`—MAY later
live here. Schema location does not determine concrete-instance trust or
storage. Concrete `Project`, `Domain`, `WorktreeRole`, and `RoutingPolicy`
instances are portable customer governance; concrete `HostOverlay` instances
are host-local input; and concrete `TaskContract` and `ExecutionReceipt`
instances are runtime artifacts. Host-local and runtime instances MUST remain
outside the target worktree, and generated receipts MUST never become portable
governance.

Phase 1 static configuration and model integrity validation MUST remain
separate from operational semantic execution. Matching task intent to a
`Project`, resolving a task's `Domain` set, evaluating `RoutingPolicy`, selecting
a role, and deciding split versus deny are Phase 2. Live Git and worktree
inspection, runtime coordination, and leases are Phase 3. Trusted runtime
contract issuance or provenance validation, scope authorization and
verification, terminalization, and receipt generation are Phase 4. CLI and
adapter implementation remain Phases 5 and 6, respectively.

The design's complete-set contract does not execute routing in this directory:
every rule matches the same complete `Dresolved`, the unique highest-priority
route is eligible only when `Dresolved ⊆ Owned(Rdecision)`, and incomplete
ownership denies without lower-priority fallthrough or a union of roles. The
closed branch-policy contract likewise records four required arrays and the
inclusive component-prefix predicate `branch == prefix OR branch starts with
prefix + "/"`; Phase 3 alone evaluates the actual symbolic branch and live
HEAD. Host or lease state can narrow or deny, never make an incomplete role
eligible.

Machine-readable structured customer governance will be authoritative for the
future operational path. Markdown MAY explain or mirror that configuration,
but it MUST NOT independently grant authority. See the
[configuration model](../docs/configuration-model.md) for the planned objects
and trust boundaries.
