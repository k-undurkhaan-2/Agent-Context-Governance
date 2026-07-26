# Public configuration schemas

Phase 0 documentation bootstrap is complete at baseline commit
`79cc9d77fd48410f37645afdb429a7cd2e34a0bd`. Phase 1: Schemas and
Models is current, but Phase 1 implementation has not yet begun. The repository
remains pre-operational, and this directory contains no Schema implementation.
The v1alpha1 Schema contract design is recorded in
[the Schema contract design](../docs/schema-contract-v1alpha1.md).
The recorded history identifies independent design audit and
`integration-control` approval of the prior candidate as complete, and the six
earlier review findings as repaired, independently audited, confirmed, replied
to, and resolved. The third Codex review at exact HEAD
`658c2e0f65c7dff0553a3433ca8cf484847f3a66` produced three accepted findings.

Commit `9eac3e040a8d0f9c959eeb675eace795749e422a` records the three
third-review repairs and the repository owner's `TS-LEX-01 A`,
`REMOTE-HOST-01 A`, `REMOTE-NAMESPACE-01 A`, `REMOTE-REPOSITORY-01 A`, and
`REMOTE-DOTGIT-01 A` selections. The receipt-binding repair recorded there is
fully derived. The repair candidate received an independent read-only audit
before commit with decision `READY FOR THIRD-REVIEW REPAIR COMMIT`.

Exact committed-head `integration-control` confirmation and PR-evidence
synchronization are external gate records; this Markdown neither proves nor
replaces external audit, review, confirmation, merge, publication, or
implementation authority. The referenced external gate record states that PR
#1 remains open and unmerged. Commit
`9eac3e040a8d0f9c959eeb675eace795749e422a` contains design documentation only
and no implementation artifact. Integration and implementation require
separately recorded external decisions.

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

## Third-review repair contract

This documentation candidate records three accepted contract repairs; it does
not create a Schema, fixture, validator, model, or runtime behavior.

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
`9999`, Gregorian date and leap-year validity, and the 11 unchanged chronology
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
receipt/contract equality; chronology/outcomes; receipt digest; then delivery
binding/chronology. They do not replace or alter that protected pipeline.
`schema-contracts` specifies the structural/static contract and vectors;
future `model-implementation` owns executable codec, projection, hashing, and
cross-artifact conformance; Phase 3 owns live remote and host facts; and Phase 4
owns trusted provenance, authority, time, freshness, and evidence truth.

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
