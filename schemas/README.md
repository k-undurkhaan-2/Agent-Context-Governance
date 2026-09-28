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

The two fourth-review repairs are recorded at commit
`b972382fad27a4dda0a4dff945c94b711019ec45`, and the two fifth-review repairs
are present at exact commit
`a99e57773384c0af4a6531f38aa14bee3781f19d`. The originating `a99e5777...`
push transaction remains historically attribution-indeterminate.

The sixth-review documentation repair was committed at exact commit
`37e3f373b012050ac424ea7d74c39396196d7da4` after its three-file candidate
received independent read-only audit. The exact OpenPGP-signed committed head
was independently verified; its single-ref non-force push and remote
branch/PR-head confirmation completed; and both sixth-review threads,
`PRRT_kwDOThD5p86VKc3R` and `PRRT_kwDOThD5p86VKc3X`, received exactly one owner
evidence reply and were resolved.

The seventh-review documentation repair was committed at exact commit
`529d9d535198b55b80aedf64141967e6bf66448f` after independent read-only
candidate audit. The exact OpenPGP-signed committed head was independently
verified; its single-ref non-force push and remote branch/PR-head confirmation
completed; all four seventh-review threads received owner replies and were
resolved; and the PR body was synchronized. The seventh top-level
`@codex review` request is REST comment `5151809449` / GraphQL comment
`IC_kwDOThD5p88AAAABMxJfqQ`.

The eighth-review repair for REST review `4834819015` / GraphQL review
`PRR_kwDOThD5p88AAAABIC17xw` was committed at exact commit
`fa0f3acde1e596c1377a680185375b7f333513d7`, whose sole parent is
`529d9d535198b55b80aedf64141967e6bf66448f`, after its correctly bound
three-file candidate completed independent read-only re-audit. The exact
OpenPGP-signed committed content was verified, GitHub reports its signature as
verified and valid, and its single-ref non-force push and remote branch,
GitHub commit-object, REST PR-head, and GraphQL PR-head confirmations
completed. All three eighth-review threads (`PRRT_kwDOThD5p86VoslV`,
`PRRT_kwDOThD5p86VoslY`, and `PRRT_kwDOThD5p86VoslZ`) each received one owner
evidence reply and were resolved, leaving 22 total / 22 resolved / 0
unresolved threads, and the PR body was synchronized. The eighth exact
top-level `@codex review` request is REST comment `5158492410` / GraphQL
comment `IC_kwDOThD5p88AAAABM3hY-g`, created `2026-08-02T14:21:43Z` with
exact body `@codex review`. The accepted provenance begins with that correctly
bound independent re-audit, not the provenance-invalid cross-worktree
implementation receipt.

The eighth exact top-level `@codex review` request is REST comment
`5158492410` / GraphQL comment `IC_kwDOThD5p88AAAABM3hY-g`. It produced the
ninth Codex review, REST review `4838766732` / GraphQL review
`PRR_kwDOThD5p88AAAABIGm4jA`, submitted `2026-08-02T14:24:32Z` against exact
commit `fa0f3acde1e596c1377a680185375b7f333513d7`. That review reported exactly
one P2 status-synchronization finding in thread `PRRT_kwDOThD5p86VxzBP`,
whose top-level comment is REST `3699333921` / GraphQL
`PRRC_kwDOThD5p87cf1sh`.

At the read-only `integration-control` triage snapshot taken after that review
and before any ninth-review repair evidence was published, the PR contained
eight exact top-level review requests, nine completed Codex reviews, and 23
review threads: 22 resolved and one unresolved. The ninth-review thread had
zero owner replies. These counts describe that named historical snapshot only;
current branch, review, reply, resolution, PR-body, and merge state must be
established from authoritative Git and GitHub records.

The ninth-review status repair is present at exact commit
`e66b80912b8f389285f3d27a43b3fa480d5d14ed`. The tenth Codex review is REST
review `4847839469` / GraphQL review `PRR_kwDOThD5p88AAAABIPQo7Q`, submitted
`2026-08-03T19:27:18Z` against that exact commit. It reported exactly three P1
findings: thread `PRRT_kwDOThD5p86WGRRs`, rooted at REST comment `3707079915` /
GraphQL comment `PRRC_kwDOThD5p87c9Yzr`; thread
`PRRT_kwDOThD5p86WGRRz`, rooted at REST comment `3707079923` / GraphQL comment
`PRRC_kwDOThD5p87c9Yzz`; and thread `PRRT_kwDOThD5p86WGRR7`, rooted at REST
comment `3707079933` / GraphQL comment `PRRC_kwDOThD5p87c9Yz9`.

At the read-only pre-edit GitHub snapshot for the separately authorized tenth-
review repair, the PR had nine exact top-level `@codex review` requests, ten
completed Codex reviews, and 26 review threads: 23 resolved and exactly those
three unresolved. Each unresolved thread contained only its bot-authored root
comment and had zero owner evidence replies. No owner reply, thread resolution,
post-repair re-review, PR-body synchronization, or merge-readiness decision for
this repair had occurred. These counts and absences describe that named
historical snapshot only.

The first three-file working-tree candidate formed after that tenth review
addressed the three reported review findings. A subsequent independent read-
only working-tree audit of that first candidate found four P1 defect classes:
pre-acquisition G-before-A and issuance-before-every-P ordering; acquired-
denial Dpre-before-L ordering; F closure on every L-empty path; and invalid
acquisition/release focused-vector totals caused by non-independent classes.
The resulting four-P1 correction was then recorded in the same three-file
candidate.

A second independent read-only working-tree re-audit of that correction found
that mandatory issued-lifecycle G presence was still unspecified, no-lease
pre-issuance revalidation and universal contract-issuance evidence were still
missing, receipt-finalization semantics remained unresolved, and the vector
ledger depended on those unresolved semantics. It also found that the then-
current status paragraph had made itself stale. A repository-owner decision
memo subsequently selected G-1, NR-2, and F-1: complete per-type G evidence;
a distinct `pre-issuance-revalidation` wire check; and one passed terminal
`receipt-finalization` check in every serialized receipt. The resulting
three-file G1/NR2/F1 candidate then failed a further independent read-only
audit. That audit reported six P1 defect classes: same-receipt recovery after
a failed or indeterminate G; missing cumulative denial prerequisites;
finalization ordered before sanitization; no direct denial-evidence-to-
sanitization-to-finalization chain; an improperly narrowed receipt-only
protected region; and stale primitive/derived vector ownership and totals. It
also reported one P2 documentation defect: claims that future serialized
fixtures and a fixture manifest already existed.

The repository-owner decision memo then selected these seven commit-invariant
contract choices:

```text
G-PRESENCE: G-1
NO-LEASE-REVALIDATION: NR-2
RECEIPT-FINALIZATION: F-1
G-FAILURE-RECOVERY: GR-2
DENIAL-PREREQUISITES: DP-1
FINALIZATION-SEMANTICS: FS-1
PROTECTED-GOLDEN-REGION: PG-1
```

An earlier independent read-only working-tree audit of that seven-choice
candidate failed it with two P1 defects and two P2 documentation defects. The
P1 defects were post-sanitization free-form content on F and the absence of
machine-verifiable controller and acquired-A identity bindings on pre-contract
denials. The P2 defects were the stale common-profile chronology count and an
incorrect description of the three execution-receipt digest occurrences in
the PG-1 corpus.

After those four repairs, the latest independent read-only working-tree audit
found two further P1 defects and two P2 documentation defects. The first P1
was that F still admitted open producer-selected semantic value domains through
otherwise regex-valid `checkId`, `profileId`, and `reasonCodes` values. The
second P1 was that denial controllers were not required to be the first
non-passed same-type observations. The first P2 was the resulting incomplete
DP/RF planned-vector inventory and totals. The second P2 was ambiguity over
whether the exact controller/evidence timestamp identity equality belonged to
DP binding or lifecycle chronology.

The repository owner subsequently selected the eighth commit-invariant choice:

```text
FINALIZATION-SAFE-DOMAIN: FSAFE-1
```

That eight-choice candidate then received a further independent read-only
working-tree audit. It found one P1 and two P2 defects. The P1 was that the
cumulative denial prerequisites were required and passed but every actual
prerequisite-stage observation was not required to precede the selected
controller, and ordinary lifecycle-stage evidence was not completely stopped
at that denial boundary. The first P2 was that RF-N12 treated non-F use of the
reserved F check ID as an independently isolatable RF primary even though the
mandatory exact F ID and receipt-wide check-ID uniqueness necessarily make it
a generic duplicate-ID fault. The second P2 was that three normative digest-
catalog rows used literal `||` inside GFM table cells and therefore parsed into
extra cells.

The repository owner selected `RECEIPT-START-SEMANTICS: RS-1` and
`ISSUED-LEASE-EVIDENCE-BINDING: LB-2`. The first working-tree implementation
attempt was later found invalid for acquisition provenance, bootstrap-operation
conformance, and AI primary-owner accounting; its inherited dirty bytes were
not retroactively authorized. A fresh non-reusable BR-1 task bound those exact
pre-existing three-file bytes as untrusted input after its protected preflight,
and the repository owner selected `ACQUISITION-PROVENANCE: AP-1`.

The Review-11 repair is recorded at exact commit
`b1441d4b3886d382e265ec1a378d52f0d6f01bdc`. It defines the external
acquisition-result source identity, requires the exact source-to-receipt digest
copy, and records the atomic AI primary-owner split while preserving RS-1,
LB-2, and AP-1. It selects neither RS-2, LB-1, nor AP-2 and adds no retry epoch.

The eleventh exact top-level `@codex review` request is REST issue comment
`5239459561` / GraphQL issue comment `IC_kwDOThD5p88AAAABOEvO6Q`. It produced
Review 12, REST review `4896227450` / GraphQL review
`PRR_kwDOThD5p88AAAABI9aAeg`, submitted `2026-08-10T11:26:50Z` against exact
reviewed commit `b1441d4b3886d382e265ec1a378d52f0d6f01bdc`. Review 12 reported
three P1 findings: recovered pre-action failure in thread
`PRRT_kwDOThD5p86X2S8z`, rooted at GraphQL comment
`PRRC_kwDOThD5p87fdbj7`; issuance-checkpoint chronology in thread
`PRRT_kwDOThD5p86X2S86`, rooted at GraphQL comment
`PRRC_kwDOThD5p87fdbkD`; and sanitization/finalization in thread
`PRRT_kwDOThD5p86X2S9A`, rooted at GraphQL comment
`PRRC_kwDOThD5p87fdbkL`.

Independent `integration-control` triage classified the first two findings as
`VALID-P1` and the third as `VALID-P1` after repository-owner semantic
resolution: the third finding was owner-choice-dependent, and the repository
owner subsequently selected
`SANITIZATION-FINALIZATION: APPLIED-TRUE`. This revision encodes all three
repairs without reopening G-1, NR-2, F-1, GR-2, DP-1, FS-1, PG-1, FSAFE-1,
RS-1, LB-2, or AP-1.

The repository documents themselves do not establish the external audit,
commit, push, thread-resolution, PR-body-synchronization, later-review, or
merge state of the revision containing these repairs; those remain separate
external gate records. This README grants no Schema or model implementation,
model-worktree creation, runtime activation, release, or merge authority.

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

#### Unified stable acquisition binding — OPTION_B

This is a material pre-publication structural design change. All eleven
resources remain `reserved-unpublished`; `contextctl.dev/v1alpha1`,
`v1alpha1-r1`, and receipt version `1` remain unchanged pending the existing
integration-control publication gate. No backward compatibility with the
superseded unpublished dual representation is claimed.

Let C be the same complete, validated, digest-bound TaskContract on an issued
path; let X be `ExecutionReceipt.spec.acquisitionBinding`; and let Source
be the associated non-public `LeaseAcquisitionResultIdentity`.
The receipt has one closed optional binding, with exactly these required fields:

```text
acquisitionBinding = {
  checkId: checkIdentifier,
  leaseId: canonical UUID,
  acquisitionResultDigest: tagged digest
}
```

The stable-acquired condition is exactly
`(origin.type == issued-contract AND C.spec.leaseRequired == true) OR
(origin.type == pre-contract-denial AND origin.leaseAcquisition.state == acquired)`.
X is required iff that condition holds and is otherwise forbidden.
Exactly one associated Source is required iff that same condition holds;
every other path forbids both X and Source. Missing X cannot remove the
independently required Source. Source is closed and contains exactly
`{taskId, checkId, leaseId, acquisitionResultDigest}`, with the same UUID,
checkIdentifier, and tagged-digest profiles as the corresponding receipt fields.
It is not an eighth public kind, a TaskContract field, portable governance,
a second full object embedded in a receipt, or authorization input.
It remains outside portable governance. Phase 3 produces it; Phase 4 checks
trusted provenance, ownership, and event truth. Static checks establish
integrity and equality only.

The one origin-independent profile is
`profile.digest.lease-acquisition-identity-v1`. Its closed projection is
bijectively formed from Source's three non-digest members:

```text
{
  taskId: Source.taskId,
  acquisitionBinding: {
    checkId: Source.checkId,
    leaseId: Source.leaseId
  }
}
```

The source digest excludes `acquisitionResultDigest` and is the tagged
SHA-256 of `separator(profile) || UTF8(JCS(projection))`.
The binding digest is an exact copy, never a second computation.
The complete unified AP-1 summary is:

```text
exactly one Source when X is present
Source.taskId == receipt.spec.taskId
Source.checkId == X.checkId
Source.leaseId == X.leaseId
Source.acquisitionResultDigest == recomputed source-profile digest
X.acquisitionResultDigest == Source.acquisitionResultDigest
count(A) == 1 and A.outcome == passed
X.checkId == A.checkId
A.leaseAcquisitionRef == {checkId: X.checkId}
for every R: R.leaseAcquisitionRef == {checkId: X.checkId}
for every L: L.leaseAcquisitionRef == {checkId: X.checkId}
issued only: X.leaseId == C.spec.leaseId
for every g in G: g.sequence < A.sequence
for every g in G: g.observedAt <= A.observedAt
for every R: A.sequence < R.sequence
for every R: A.observedAt <= R.observedAt
```

G is every same-receipt checks[] member whose checkType is intent-validation,
project-domain-resolution, role-routing, host-binding, or initial-preflight.
A, R, and L are the same receipt's lease-acquisition,
post-acquisition-revalidation, and lease-release subsets. After cardinality,
outcome, and X.checkId equality validate, A denotes the unique passed
state-creating acquisition identified by X.checkId. Whenever X exists,
every actual G, including every repeated passed observation, MUST precede A
by sequence and be no later than A by timestamp. Presence and passed outcomes
for all five G types remain required by the applicable issued/denial branch.
The unified stable-acquired prefix is every G < A < every R by sequence and
every G <= A <= every R by time. It applies to issued lease-required receipts,
acquired R denials, and acquired I denials; an origin change cannot remove it.
R quantifies the
issued singleton, an acquired-denial controller, every earlier passed R before
that controller, and the passed R prerequisite of acquired issuance denial.
L quantifies every release attempt, including earlier unsuccessful members.
A correctly bound controller or finalL cannot hide a bad earlier member.

The compact reference is closed `{checkId}` only. On stable-acquired paths it
is required exactly on A, every R, and every L; G, N, I, P, E, V, and F forbid
it. On all other paths it is forbidden everywhere. No compact reference
contains a lease ID or digest. Existing source/binding/contract equalities and
all eight issued receipt/contract comparisons remain mandatory.

Direct references on I/P/E/V are unnecessary by prerequisite closure.
On issued paths, A/R bind X, X.leaseId equals C.leaseId, I records issuance of
that same complete C, and P/E/V operate under that same validated C.
On acquired I denial, A and every R bind X and I is reached only after that
valid acquired prefix. I inherits the subject through those prerequisites.
This argument introduces no new reference placement or retry epoch.

`origin.leaseAcquisition` on a denial is a closed state-only record in every
branch, including acquired. Its sole member is `state`, one of
`not-required`, `not-attempted`, `not-acquired`, `indeterminate`, or
`acquired`. It never contains checkId, leaseId, or acquisitionResultDigest.
Stable identity is carried only by receipt-level X. A denial's
`preContractEvidence` is closed with exactly `observedAt`,
`evidenceDigest`, `controllerCheckId`, non-empty canonical `reasonCodes`,
and bounded `sanitizedSummary`. It contains no acquisition identity copy.

The canonical pre-contract-evidence projection is the closed object
`{taskId, denialCheckpoint, preContractEvidence}`, where the last member is the evidence record with only evidenceDigest removed,
with exactly one additional `acquisitionBinding` member iff the denial state
is acquired. That member is the complete validated receipt-level X, including
its copied source digest. In all other states the member is absent, never
null, an empty object, or a default. The profile remains
`profile.digest.pre-contract-evidence-v1`. The complete receipt digest
continues to cover the complete receipt excluding only `spec.receiptDigest`,
including X and all A/R/L references whenever present.

| Lifecycle | X / Source | A/R/L compact references |
| --- | --- | --- |
| Issued lease-required | required / exactly one | A, singleton R, every L |
| Issued no-lease | forbidden / zero | forbidden everywhere |
| Acquired denial | required / exactly one | A, every R, every L |
| Denial not-required | forbidden / zero | forbidden everywhere |
| Denial not-attempted | forbidden / zero | forbidden everywhere |
| Denial not-acquired | forbidden / zero | forbidden everywhere |
| Denial indeterminate | forbidden / zero | forbidden everywhere |

The seven cells are exhaustive. Indeterminate acquisition has no stable
identity and no L; it retains the blocking warning and indeterminate release
and lifecycle outcomes. The other three non-acquired states have no L and
releaseOutcome not-required.

The shared `canonicalUtcTimestamp` accepts only whole-second UTC strings
matching:

```text
^[0-9]{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])T(?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]Z$
```

Future Schema uses `type: string`, that exact pattern, and asserted
`format: date-time`. Phase 1 additionally enforces years `0001` through
`9999`, Gregorian date and leap-year validity, all 20 primitive chronology
relations, and all 31 displayed consequences. Lower-case delimiters, offsets,
fractions, leap seconds,
`24:00:00`, whitespace, alternate spellings, and repair are forbidden. The
profile applies to the three TaskContract timestamps, receipt `startedAt`,
`finishedAt`, `sanitization.completedAt`, every `checks[].observedAt`,
the pre-contract origin's `preContractEvidence.observedAt`, and
`ReceiptDeliveryResult.attemptedAt`: exactly nine paths.

Receipt startedAt bounds the complete lifecycle. The issuance bracket is R/N <= checkpoint <= issuedAt <= I. Current CH11 owns R/checkpoint, CH12 owns N/checkpoint, and CH13 owns issuedAt/I; R/N-to-issuedAt and start-to-issuedAt are derived. The full independently rebuilt chronology ledger below is normative.

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
`acceptedRemotes` is set-like, duplicate-free, and already strictly ordered by
`J(remote)`; outer remote expectations remain keyed and ordered by only
`remoteName`. HostOverlay narrowing uses exact validated membership without
aliases or ignored fields.

The required-postcondition vocabulary remains eleven types and the check
vocabulary contains fourteen types, including the distinct
`pre-issuance-revalidation` token. A check has an optional closed
`postconditionRef: {type}` using the exact eleven-value enum. Only
`post-execution-verification` may carry it; the other thirteen check types
forbid it. F is further specialized to exactly `sequence`, `checkId`,
`checkType`, `outcome`, `observedAt`, `profileId`, and `reasonCodes`;
it forbids `expectedSummary`, `observedSummary`, `postconditionRef`,
`leaseAcquisitionRef`, and
every other free-form, payload, or unknown field. FSAFE-1 additionally requires
the exact tuple `check.receipt-finalization / profile.validation.v1 / []` and
passed outcome. The primitive implication is
`checkType == receipt-finalization` implies
`checkId == check.receipt-finalization`. Because every receipt has exactly one
F and globally unique check IDs, a non-F use of that ID is instead a derived
generic duplicate-ID rejection, not an independent RF predicate. Generic
identifier grammar is unchanged,
`profile.validation.v1` is not F-exclusive, and empty reason codes are not
universal. All thirteen non-V placements, including N, remain forbidden. Current independent PB/AI/DP/RF/RC/CH owners and their mandatory non-additive variants are defined below.

For post-sanitization receipt-finalization evidence, textual identity fields
are safe-by-construction only when their complete semantic value domain is
closed by the protocol. Lexical validity alone is insufficient. The exact
reserved tuple above rejects producer alternatives that merely satisfy generic
identifier grammar, including path-like, host/operator-derived, secret-like, or
diagnostic values. This protects against arbitrary post-sanitization text in F;
it does not claim information-theoretic covert-channel elimination.

### Validation dependency DAG

Validation uses a dependency DAG, not a chronology-before-selector loop.
An absent candidate is a preparation result; it is never an accepted omission.
No intermediate digest or successful preparation grants acceptance or authority.

1. **Preparation.** Strict UTF-8/token decoding rejects BOM, malformed Unicode,
   duplicate keys, non-NFC strings, invalid raw number tokens, and unsafe or
   out-of-range numbers before lossy conversion. Validate closed shapes,
   supported versions, identifier/UUID/digest/timestamp profiles, Gregorian
   dates, and mandatory offline format assertion. Verify canonical arrays,
   contiguous sequences, and receipt-wide check-ID uniqueness without sorting.
   Construct immutable decoded values and pure deterministic type subsets,
   including every G and the A/R/L candidates, before using their operands.
   Construct greatest-sequence candidates, finalP/finalE/finalV/finalL, per-type finalV(t),
   diagnostic finalG, and controller candidates. Selectors use sequence alone.
   Selector construction is not acceptance and does not await chronology.
2. **Static acceptance.** With those prepared values, validate conditional
   presence and cardinalities, the same complete TaskContract and its
   derivation prerequisites/digest when applicable, and all eight receipt/C
   comparisons. Contract acceptance first rejects unsupported transition
   members, checks Ptrans against Apath/Qpath and upstream narrowed authority,
   validates simultaneous B/F reconstruction, and enforces both RequiredPlanCaps
   predicates with unchanged Oplan plus Iplan. Matching postconditions, an empty
   ordinary-operation set, or a receipt digest cannot bypass these gates. Validate stable-acquired X/Source presence, required Source
   cardinality and digest, Source→X task/check/lease equality and digest copy,
   A singleton/passed state and X→A identity, issued X→C lease equality, and
   every A/R/L compact reference. On stable-acquired paths, validate required
   G/R presence and applicable outcomes, then apply every-G→A sequence and
   timestamp predicates (AI10/CH08), followed by A→every-R predicates
   (AI11/CH10). Continue with controller identity/time/reasons, state-aware A/I
   singleton denial rules, cumulative prerequisites, and issued suffix rules.
   Recompute denial evidenceDigest from its exact conditional projection after
   Source/binding inputs and controller bindings validate. Apply remaining
   sequence/chronology, outcomes and terminality, warning linkage, required-
   postcondition binding, scope, ordinary-operation evidence, sanitization,
   and F acceptance. This causal dependency order is mandatory; unrelated
   independent predicates may run in either order after their operands exist.
   Every applicable predicate must pass before receipt-digest acceptance.
   A contract/source digest is an input to these checks, not receipt acceptance.
3. **Receipt digest acceptance.** Only after every applicable receipt-internal
   and static cross-artifact predicate passes, freeze the complete receipt
   projection excluding only spec.receiptDigest; obtain the profile's payload
   bytes, prepend its exact separator, hash, and compare receiptDigest exactly.
   For acquired denial the source digest and X exact copy precede the
   evidence-digest projection, which precedes receipt hashing. Selectors,
   acceptance proofs, and delivery results are not extra receipt members.
4. **Delivery pair.** Only when a delivery result exists, validate its closed
   outcome shape, exact receipt-ID binding, exact finalized receiptDigest copy,
   and finishedAt <= attemptedAt. Delivery-only chronology is inapplicable
   without that pair and cannot block preparation or receipt acceptance.

The internal validated canonical instance representation is non-serializable:
it binds the immutable closed JSON value, selected schema revision/root ID,
completed strict-parser/shape/array/static proofs, and retained original bytes
or same-process provenance to that same value. A prepared value is not yet
this fully validated representation. Caller-created decoded objects cannot
claim these proofs. No normalization, repair, migration, or array sorting is
part of validation.

For every digest computation the rule is exactly:

```text
RAW profile: payloadBytes = exact retained original bytes
JCS profile: payloadBytes = UTF8(JCS(exact closed projection))
digest = tagged SHA256(separator(profile) || payloadBytes)
```

Raw profiles forbid trimming, newline conversion, filtering, transcoding,
or normalization. JCS sorts object members only and preserves validated
strings and array order. The existing NUL-delimited separator convention is
unchanged. Complete schema/static validation of each computation's own source
precedes its projection; this does not require the downstream receipt to
already have a verified receiptDigest. Failed delivery never rewrites a
finalized receipt or establishes acquisition, release, or authorization.

## Review-13 host-resource exclusivity

`HOST-RESOURCE-EXCLUSIVITY` is an editorial label and `HX` is its focused
planned-fixture prefix. Neither value is part of the wire or API surface.

The exact Finding A predicates are:

For one Phase 1 validation or revalidation checkpoint and exactly one target
`hostId`, the comparison authority is the complete trusted configuration set
of every configured `HostOverlay` whose `spec.hostId` matches exactly, across
all `projectRef` values. Complete membership and every participating resource's
exact contents MUST derive from one trusted configuration validation snapshot:
a checkpoint-local, internally coherent, read-only view of a trusted closed
configuration inventory. A task, caller, adapter, selected Project,
`projectRef`, selected overlay, `HostOverlay.metadata.id`, resource ID, role,
active-only filter, or other convenient subset MUST NOT narrow that set.

Each participating `HostOverlay` MUST first be individually structurally and
semantically valid exactly as represented in that same snapshot. Only then does
Phase 1 form one comparison domain by taking the union of every participating
`spec.bindings` array. The exact Finding A predicates over that complete binding
union are:

- **A1.** Across every two distinct bindings in the complete same-host union,
  `worktreeId` values MUST differ. A different `HostOverlay` resource,
  `projectRef`, `roleRef`, or other resource identity does not permit reuse.
- **A2.** Across every two distinct bindings in that union, the
  already-validated exact `(platform, repositoryRoot.value)` identities MUST
  differ. Static comparison is exact equality only; it performs no filesystem
  resolution, case folding, Unicode normalization, symlink, junction,
  reparse-point, registration, or other alias resolution.
- **A3.** In future Phase 3, every distinct binding in the checkpoint's
  complete same-host set MUST resolve to a distinct canonical registered
  physical Git worktree.
- **A4.** Future Phase 3 uncertainty about physical-worktree identity fails
  closed, including case or Unicode identity, symlink, junction, reparse-point,
  Windows 8.3, `.git` indirection, linked-worktree registration,
  common-Git-directory, conflicting-registration, canonicalization, or other
  alias ambiguity.

Equal lexical `repositoryRoot.value` strings under different `hostId` values
are outside one same-host comparison domain and are not rejected solely for
that equality. If complete trusted same-host membership cannot be established,
or any participating resource or contents are missing, ambiguous, or untrusted,
the complete-set proof fails closed. Membership, exact contents, individual
validation, union construction, and injectivity MUST NOT be composed across
incompatible snapshots; a relevant mid-proof configuration change invalidates
the complete proof. At every lifecycle checkpoint where control governance
requires the proof, that checkpoint independently re-establishes it from one
coherent snapshot; an earlier checkpoint's result is not later proof.

Phase 1 owns only these deterministic same-host logical and exact comparisons.
Phase 3 owns live canonical registered physical-worktree identity and ambiguity.
Validation rejects; it does not normalize, relocate, delete, repair, switch,
rebind, or clean a repository or worktree.

The D8 binding remains the existing closed five-field record with exactly
`roleRef`, `worktreeId`, `repositoryRoot`, `expectedRef`, and `remoteNames`.
A1 and A2 are validity predicates only: they do not add, remove, or rename a
field, change binding identity, or change the canonical `bindings` array
ordering `(R(roleRef), S(worktreeId))`.

For the Finding B comparator, an already-validated coordination-root identity
`C` is a strict descendant of an already-validated binding `repositoryRoot`
identity `W` exactly when all three conditions hold:

1. `C` and `W` have the exact same validated platform and root identity;
2. the components of `W` are an exact prefix of the components of `C`; and
3. `C` has at least one additional component.

The exact Finding B predicates are:

- **B1.** `stateRoot` MUST NOT exactly equal any binding `repositoryRoot`.
- **B2.** `stateRoot` MUST NOT be a strict descendant of any binding
  `repositoryRoot`.
- **B3.** `lockRoot` MUST NOT exactly equal any binding `repositoryRoot`.
- **B4.** `lockRoot` MUST NOT be a strict descendant of any binding
  `repositoryRoot`.
- **B5.** In future Phase 3, neither coordination root may resolve equal to or
  inside any actual bound registered worktree.
- **B6.** Future live alias or containment uncertainty rejects, including case,
  symlink, junction, reparse-point, canonicalization, and registration
  ambiguity.

The B predicates do not add a `stateRoot != lockRoot` rule. They also do not
reject solely because a binding `repositoryRoot` is beneath `stateRoot` or
beneath `lockRoot`. Only the coordination-root-equal-to-or-inside-bound-
worktree direction is prohibited.

The focused HX family contains exactly these primary planned vectors. Variants
are mandatory but non-additive:

| ID | Primary predicate |
| --- | --- |
| `HX-A-P01` | A complete trusted same-host set containing at least two individually valid `HostOverlay` resources, including a different-`projectRef` variant, has distinct `worktreeId` and exact `(platform, repositoryRoot.value)` identities across its snapshot-bound binding union and passes Phase 1 exclusivity. |
| `HX-A-P02` | Future Phase 3 proves that every distinct binding across the checkpoint's complete same-host set resolves to a distinct canonical registered physical Git worktree. |
| `HX-A-P03` | Complete sets for different `hostId` values may contain lexically equal `repositoryRoot.value` strings without rejection solely for that cross-host equality. |
| `HX-B-P01` | Both coordination roots are statically outside or siblings of every binding root; equal coordination roots and a worktree beneath a coordination root are non-additive valid variants. |
| `HX-B-P02` | Future Phase 3 proves that both coordination roots resolve outside every actual bound registered worktree. |
| `HX-A-N01` | Distinct `HostOverlay` resources for the same host reuse one `worktreeId`; different `projectRef` and `roleRef` values are mandatory non-additive variants, and the complete union rejects. |
| `HX-A-N02` | Distinct same-host resources with distinct IDs, Projects, roles, or `worktreeId` values reuse one already-validated exact `(platform, repositoryRoot.value)` identity, and the complete union rejects. |
| `HX-A-N03` | Lexically distinct same-host binding roots that resolve to the same physical worktree reject in future Phase 3. |
| `HX-A-N04` | Indeterminate same-host physical-worktree distinctness rejects in future Phase 3. |
| `HX-A-N05` | A caller or other input supplies only a proper subset of the configured trusted same-host overlays; incomplete membership rejects. |
| `HX-A-N06` | A participating same-host resource or its exact contents are missing, ambiguous, or untrusted, so the complete-set proof rejects. |
| `HX-A-N07` | Membership from one configuration state is combined with contents, individual validation, union construction, or injectivity from an incompatible state; the mixed-snapshot proof rejects. |
| `HX-B-N01` | `stateRoot` exactly equals a binding `repositoryRoot`. |
| `HX-B-N02` | `stateRoot` is a strict descendant of a binding `repositoryRoot`. |
| `HX-B-N03` | `lockRoot` exactly equals a binding `repositoryRoot`. |
| `HX-B-N04` | `lockRoot` is a strict descendant of a binding `repositoryRoot`. |
| `HX-B-N05` | A lexically separate coordination root resolves equal to or inside an actual bound registered worktree in future Phase 3. |
| `HX-B-N06` | Live alias or containment identity is indeterminate in future Phase 3. |

HX is exactly 5 positive and 13 negative primary predicates. It is separately
counted and does not revise any retained focused-family or regression total.

WIRE/API SURFACE UNCHANGED: Review-13 A+B and the Review-14 A complete-set
closure only shrink accepted `HostOverlay` configurations. They do not alter
the API version, revision, resource kinds, JSON property names, HostOverlay
binding fields, enums, reason codes, check types, transition types,
postconditions, receipt outcomes, or digest fields. The complete same-host set
and snapshot are trusted validator/control-plane comparison context, not a
serialized resource, field, collection, `GovernanceBundle` member,
`TaskContract` field, or digest input. The existing `configurationDigest`
projection remains the closed `{governanceBundle, hostOverlay}` shape. The
digest graph is now 12 field paths, 10 computations, and 2 exact copies under Option B.

## Current contract summary

The fourth-review active-operation retirement remains unchanged. A
`TaskContract` materializes nine baseline dimensions, and both
`expectedBaseline.activeOperations` and
`expectedBaseline.administrativeLocks` are exactly `{ "state": "none" }`.
Their reusable non-empty exact unions remain available only for
non-authorizing observation and evidence. A present live Git active operation
or administrative lock still denies at the governing guard checkpoint; neither
may be contracted as an allowed baseline, transition, or final postcondition.
Git administrative locks remain distinct from runtime write leases,
lease-store locks, and transient command-internal lock files.

The closed permittedTransitions union has exactly four supported path-keyed
branches: index-entry, tracked-entry, untracked-path, and ignored-path.
Ref-state, head-state, and submodule-entry transition members reject
structurally under v1alpha1-r1 before capability inference. All eleven
postcondition branches remain; optional ref-state, head-state, and
submodule-state require baseline-equal observations, and optional active-
operations/administrative-locks remain none-only. Simultaneous composition
uses only the four supported types, preserves ref/HEAD/submodules, and
reconstructs one valid nine-dimension F.

For a writing TaskContract `C`, the design-only mirror defines
`M = {create, modify, delete}`,
`Acap = set(C.spec.authorizedScope.capabilities)`, and
`Qcap = set(C.spec.prohibitedScope.capabilities)`. Existing rules keep the two
capability sets disjoint; the complete capability vocabulary remains exactly
13. Only after simultaneous D7 composition produces a valid final composite
`F`, every ordinary path is projected from complete `B` and `F` as absent,
present with exact known ordinary-file identity, or present with opaque
ordinary-file identity. Absent-to-present contributes `create`,
present-to-absent contributes `delete`, known unequal present-to-present
contributes `modify`, known equal and absent-to-absent contribute nothing, and
opaque or equality-unprovable present-to-present conservatively contributes
possible `modify`. Opacity alone does not reject when `modify` is authorized
and not prohibited.

`Oplan(B,F)` is the least-upper-bound union, across every ordinary path, of
every ordinary mutation capability possible in a B/F-consistent effect. The
operation is not inferred from a transition branch name. An index-entry alone
contributes no ordinary-file mutation; any ordinary effect of the complete
composite still contributes. Tracked, untracked, and ignored contributions
use complete B/F path state. Ref/HEAD/submodule transitions are unsupported. For
tracked `P = {clean, modified, type-changed}` and `D = deleted`, `P -> D` is
delete, `D -> P` is create, known changed `P -> P` is modify, proven equal
`P -> P` is no-op, and equality-unprovable `P -> P` is possible modify.
`entryPresence.state` alone is insufficient. Untracked/ignored
absent-to-present is create, present-to-absent is delete, and opaque
present-to-present is possible modify; a classification transfer alone is not
create+delete when the same leaf remains present. A rename-equivalent old/new
pair requires both delete and create.

The complete closure is RequiredPlanCaps = Oplan(B,F) union Iplan, with
RequiredPlanCaps subset Acap and RequiredPlanCaps intersection Qcap empty.
Iplan is {git-stage} whenever an index-entry is present, otherwise empty.
The ordinary Oplan predicates remain necessary within this conjunction.
The direct Ptrans path predicates and all upstream narrowing also apply.
This material pre-publication transition-union narrowing retains the API,
revision, eleven postconditions, capability enum, receipt fields, and digest
graph. SG-001 remains 25 rows; its existing transition, postcondition, D5,
D7, and receipt scope rows cover the repaired contract.

#### Transition authorization — HYBRID_A_PLUS_C

ROOT-TRANSITION-AUTHORIZATION joins TA-01 capability closure and TA-02 path
closure. ADR-TA-01 and ADR-TA-02 remove ref-state, head-state, and
submodule-entry from the current closed transition union. Endpoint ref/HEAD
state cannot identify checkout/switch, commit, reset-like movement,
detach/reattach, or initial-commit semantics, so it MUST NOT be mapped
opportunistically to git-branch or git-commit. The former submodule branch
mixes outer gitlink state, nested initialization/HEAD, and nested
dirty/untracked/conflict observations; it receives no broad capability.
A future design may separate outer-gitlink authority, nested-repository
authority, and operation/effect evidence. Transition-design Option B is
deferred; the existing unified-acquisition OPTION_B remains unchanged.

The complete supported transition vocabulary and postcondition mapping is:

| Supported transition | Required postcondition when that dimension changes |
| --- | --- |
| index-entry | index-state |
| tracked-entry | tracked-state |
| untracked-path | untracked-state |
| ignored-path | ignored-state |

All nine baseline dimensions and all eleven postcondition branches remain.
F = Apply(B, permittedTransitions) applies only these four transition types
simultaneously. Untargeted values retain B, always including
F.ref = B.ref, F.head = B.head, and F.submodules = B.submodules.
Optional ref-state, head-state, and submodule-state postconditions therefore
describe only unchanged baseline projections. They confer no transition
authority. Cross-dimension reconstruction remains mandatory: in particular,
an index gitlink change cannot evade the immutable submodule projection or
the index/submodule equality and coverage rules. Actual drift prevents
successful verification. The mandatory scope-contained obligation remains.

Possession of a capability token does not create a permitted state
transition. A state dimension may change only when this revision defines a
supported permittedTransition for that dimension and all corresponding static
authority predicates pass. The shared 13-token capability enum is unchanged,
including git-branch, git-commit, and git-remote. In v1alpha1-r1, neither
git-branch nor git-commit confers permission to change ref or HEAD, because
no supported ref/head transition exists.

Define the following over the already validated contract C:

```text
Ptrans = {t.path | t in C.spec.permittedTransitions}
Apath = union(language(p) for p in C.spec.authorizedScope.paths)
Qpath = union(language(p) for p in C.spec.prohibitedScope.paths)

for every p in Ptrans:
  p in Apath
  p not in Qpath
```

These direct transition-target predicates are mandatory before contract
acceptance for every supported member, independently of whether Oplan is
empty, an ordinary effect is produced, a later receipt includes the path, or
matching postcondition evidence exists. Deny precedence is unconditional.
The pattern languages use the existing valid repository-relative path
universe and exact anchored grammar; .git remains reserved.

These checks do not replace the complete resolved Domain-set binding,
one covering WorktreeRole's ownership, Project restrictions, or HostOverlay
narrowing. Authorized paths must remain within the resolved Domains' scope
and the covering role/Project/overlay authority at the applicable static and
issuance gates. Widening authorizedScope.paths cannot legalize a target
outside that authority. Retain every existing upstream identity, subset,
inclusion, and narrowing proof. Phase 1 checks supplied closed data; Phase 2
resolves the real complete Domain set and role; trusted Phase 4 validates the
resulting binding before issuance. Missing or unprovable authority denies.

ADR-TA-04 defines the derived index requirement without a new wire field:

```text
Iplan = {git-stage}  if any permittedTransition has type index-entry
Iplan = empty        otherwise

Acap = set(C.spec.authorizedScope.capabilities)
Qcap = set(C.spec.prohibitedScope.capabilities)
RequiredPlanCaps = Oplan(B,F) union Iplan

RequiredPlanCaps subset Acap
RequiredPlanCaps intersection Qcap = empty
```

Here union, subset, and intersection mean exact set union, inclusion, and
intersection. Acap and Qcap remain disjoint. Requirements are conjunctive:
git-stage never substitutes for create/modify/delete, and an ordinary token
never substitutes for git-stage. Oplan retains its complete-composite ordinary
create/modify/delete semantics, including conservative opaque identity and
all effects implied by B/F. The derived union is not a branch-name substitute.

For this contract layer, git-stage covers only authorized logical stage-0
index effects represented by supported index-entry transitions: staging,
unstaging, exact supported entry replacement, and exact supported entry
removal. It does not authorize ref/HEAD movement, commit creation, branch
switching, unsupported submodule operations, or arbitrary administrative-file
writes. index-entry(path) targets the logical repository path, not .git/index.
A direct runtime filesystem write to .git/index or another resolved Git
administrative location remains subject to the existing runtime administrative-
path boundary and cannot be relabeled as ordinary portable scope evidence.
Trusted runtime handling must distinguish a supported logical Git index effect
from a direct administrative-file mutation; a token alone proves neither.

ADR-TA-03 selects TA-A. No ExecutionReceipt field or digest profile is added.
Phase 1 statically validates requested transition authority; Phase 3
materializes required baseline/live state; trusted Phase 4 compares observed
final state with F and performs actual transition and effect attribution.
The existing ordinaryOperationEvidence carrier keeps its exact ordinary-only
role. An archived receipt does not independently reconstruct the complete
operation history of non-ordinary Git effects. Endpoint equality cannot prove
that an unauthorized transient index mutation did not occur and get restored.
Runtime attribution MUST fail closed when trusted evidence is insufficient;
it cannot assert successful verification from endpoint equality alone.
These limits do not weaken any contract-time predicate. Durable typed replay
of actual administrative-operation history would require a separate TA-B
architecture change.

#### Transition-authorization conformance and ownership

All cases below are planned static/synthetic conformance requirements, not
implemented validators or runtime evidence. Each construction uses complete,
otherwise-valid B/F resources, canonical arrays, required postconditions,
the same complete resolved authority, and refreshed dependent digests.
Companion transitions required by cross-dimension consistency stay present;
they cannot be omitted merely to create an apparently isolated branch test.

The additive TA owner graph has exactly three positive/negative owner pairs:

| Owner pair | Independent predicate | Isolating negative and positive control |
| --- | --- | --- |
| TA-P01 / TA-N01 | Ptrans subset Apath | Supported index-effect witness at p with Qpath empty and all capabilities/Domain authority valid; omit p from Apath, then restore it. |
| TA-P02 / TA-N02 | Ptrans intersection Qpath is empty | Same witness with p=src/private/item and authorized pattern src/**; prohibit src/private/**, then remove it. Distinct pattern tokens preserve literal-set disjointness while their matched languages overlap. |
| TA-P03 / TA-N03 | Iplan subset Acap, the index projection of RequiredPlanCaps inclusion | Same witness with Oplan empty, valid paths, and Qcap empty; omit git-stage, then authorize it. |

One universal path predicate owns its variants across all four branch types.
Wrong-Domain/role/Project/overlay cases keep their existing upstream owners.
Unsupported-type rejection keeps the generic closed-enum/union owner;
ref-state, head-state, and submodule-entry are three required variants, not
three new owners, and reject before any capability inference. An undefined
requirement always rejects. RequiredPlanCaps is the derived union, not another
additive owner. Its ordinary inclusion projection retains the existing OC
ownership; its index projection is TA03. The required prohibited-intersection
check remains explicit, but is non-additive in this independent graph: with
RequiredPlanCaps subset Acap and Acap disjoint Qcap, it is implied. A
git-stage-only-in-Qcap case necessarily also lacks authorized git-stage and
cannot isolate an additional prohibition owner. Keep that mandatory negative
without double counting. The three positive controls use distinct synthetic
contract identities; companion metadata transitions do not add owners.

| Coverage family | Required negative variants | Valid control |
| --- | --- | --- |
| Unsupported old members | ref-state; head-state; submodule-entry, with any capability contents, including inspect-only or the former putative Git token | Each of the four supported closed shapes with all other gates satisfied |
| Direct paths, each of four supported types | target outside Apath; target inside Qpath; target in a wrong Domain-owned area despite a widened Apath | Correct target with proper Domain/role/Project/overlay binding and complete capabilities |
| Index capability | index-entry without git-stage; git-stage present only in Qcap | git-stage in Acap and outside Qcap |
| Ordinary capability | retain missing create/modify/delete and each prohibited ordinary operation, OC-N01..06 | retain OC-P01..03 |
| Index plus ordinary delete | Acap={delete}; Acap={git-stage}, with Qcap empty | Acap={delete,git-stage}, with neither prohibited; both tokens are necessary |
| Inspect-only, Acap={inspect} | index effect lacks git-stage; tracked modify lacks modify; untracked create lacks create; ignored create lacks create | Supply the complete required capability set and valid path authority |
| Non-writing | all three allowWrite=false truth-table rows paired with each of the four supported types | Empty transitions and baseline-equal optional state postconditions |
| Runtime evidence | unproved transient index history or unauthorized ref/HEAD/submodule drift claimed as passed | Trusted complete attribution and observed final state equal to F, with all other evidence gates passed |

The direct-path matrix has 4 x 3 = 12 negative variants and four positive
branch controls, not twelve independent primary predicates. The non-writing
matrix has 3 x 4 = 12 D5 negatives. There are three unsupported-member
variants and four inspect-only negatives. These case inventories overlap the
owner witnesses and are not added to the independent owner aggregate.

A complete index-only ordinary-no-effect control uses a synthetic committed
HEAD with one ordinary path p, the same complete stage-0 index, and a tracked
deleted entry for p: the ordinary leaf is absent. Remove the index entry and
its matching tracked metadata together. F has an empty exact index (different
from unchanged non-empty HEAD), tracked.clean, no untracked/ignored/submodule
entries, and the unchanged ref/HEAD. Supply index-state and tracked-state
postconditions plus scope-contained. The ordinary leaf stays absent, so
Oplan is empty and Iplan={git-stage}; no create/delete is manufactured from
the index change. Correct git-stage alone passes this capability family,
subject to all remaining gates. For the conjunctive delete control, begin
with that ordinary leaf present and known clean instead, then remove the
index entry and tracked leaf/metadata together: Oplan={delete} and
Iplan={git-stage}. Both controls preserve the original reconstruction rules.

Rebuilding the retained row inventories yields PB 5/5, AI 23/23, DP 13/13,
RF 14/14, CH 20/20, and RC 9/9: 150 in the five-family subtotal, 168 with RC.
TA adds 3/3, giving 174 independent positive/negative owners including RC
and TA. Scope 5/6, OC 3/8, OE 10/11, D5 variants, generic structural
rejections, and upstream narrowing variants are separate non-additive case
inventories; they do not inflate this aggregate.

#### Transition repair corpus disposition

The current exact golden corpus contains one complete TaskContract and its
derivation projection, both with permittedTransitions: []. They remain valid
current specimens; neither requires conversion, replacement, or historical-
only reclassification for unsupported transition members. No golden input
bytes change in this repair, so all downstream derivation, complete-contract,
receipt, and delivery bindings retain their existing values after replay.
The digest graph still follows the catalog's field dependencies: no new
digest-bearing field, profile, computation, or copy is introduced.

PG-1's exact broad catalog-through-golden slice is outside the edited
transition/validation text. Its raw W and CRLF-to-LF B identities and every
occurrence/attestation copy must still be checked against the actual slice;
no old hash or count is a repair target. The retained prior OPTION_B golden
and PG-1 headings refer to acquisition binding, not the deferred transition-
design Option B or a new receipt-history carrier.

A non-empty active operation or administrative lock at initial or pre-issuance
revalidation denies before a contract exists. At post-contract
immediately-before-action revalidation it permits no protected action and any
issued receipt uses `not-attempted/not-performed`. At post-execution
verification it is unexpected terminal evidence with failed or indeterminate
verification, never an authorized final postcondition. The reusable
administrative-lock condition union and its seven lock identities remain part
of generic observation and evidence; they no longer create a contract
transition branch.

The active-operation legacy contract family remains exactly 21 cases: seven
single-operation exact baselines, seven retired transitions, and seven
single-operation exact postconditions. The administrative-lock legacy contract
family is likewise exactly 21 cases: seven single-lock exact baselines, seven
retired transitions, and seven single-lock exact postconditions. Its generic
observation-shape negatives remain separate: duplicate lock identity, missing
or forbidden branch identifiers, unknown branch, non-canonical order, empty
exact array, and other malformed reusable observation forms. These cases do
not inflate the 21-case administrative-lock family; active-operation generic
shape failures likewise remain outside its 21-case family.

The sixth-review portable `repositoryRelativePath` profile first requires
strict UTF-8 decoding and an already-NFC value; it never decodes permissively,
normalizes, case-folds, aliases, or repairs input. After the existing POSIX
relative-path checks, any component exactly equal to lower-case `.git` under
case-sensitive equality is invalid at any depth. Required invalid vectors are
`.git`, `.git/config`, `.git/hooks/pre-commit`,
`.git/worktrees/example/HEAD`, `foo/.git`, `foo/.git/config`, and
`nested/repository/.git/HEAD`. The deliberately similar `.gitignore`,
`.gitmodules`, `.github`, `foo.git`, `dir/.gitignore`, and
`dir/.github/workflow.yml` values remain valid when every other rule passes.

The anchored pattern grammar retains segment-local `*` and `?` and
complete-segment `**`, but each language is defined over the revised universe
`U` of valid repository-relative paths. A literal exact `.git` component makes
the pattern invalid, including `.git/**`, `.git/config`, `foo/.git/**`, and
`foo/.git/config`. The broad pattern `**` remains valid but cannot match a
reserved value because that value is outside `U`.

This one rule applies to Domain and role-derived path scope, HostOverlay path
ceilings and D10 inclusion, RoutingPolicy/static inclusion, TaskContract
authorized and prohibited scopes, baseline and postcondition path entries, the
four supported path-keyed transition branches, receipt `changedPaths`, and
`scope-contained` verification. `modify` plus `**` cannot authorize
`.git/config` or hooks. Git-administration capability tokens do not turn an
administrative filesystem location into an ordinary path. A runtime-resolved
administrative effect cannot be a successful `changedPaths` member and cannot
be silently omitted; it makes `scope-contained` failed or indeterminate.

Phase 3 resolves top-level `.git` indirection, linked and common Git
directories, administrative paths outside the worktree root, symlink,
junction, reparse-point and other aliases, case-folded, Windows 8.3, and
Unicode-normalized aliases, registered-submodule administrative roots, and
nested-repository administrative roots. Uncertainty fails closed, and portable
governance never records the resolved host paths.

For an issued-contract receipt, let `P` be every
`pre-action-revalidation` check, `E` every `execution` check, and `V` every
`post-execution-verification` check. Check sequence equals array position,
sequences are contiguous, and check IDs are unique. The final applicable P, E,
and V are their unique greatest-sequence members. Per required-postcondition
type `t`, `V(t)` is the referenced subset and `finalV(t)` is its unique
greatest-sequence member. Selection uses sequence only, never timestamp,
outcome, serialization, locale, check ID, or iteration order.

The single check `outcome` field retains exactly two conditional branches:
execution uses `succeeded`, `failed`, `cancelled`, or `indeterminate`; every
non-execution check uses `passed`, `failed`, or `indeterminate`. The optional
closed `postconditionRef` is permitted only on V. It contains exactly `type`,
reuses the eleven required-postcondition strings, and resolves only against the
same complete digest-verified, field-equal TaskContract. A valid enum value
absent from that contract is invalid; unreferenced V remains general evidence
and satisfies no obligation.

Every attempted issued receipt requires P, E, V, and at least one `V(t)` for
every required type. Every P in an attempted receipt is passed and strictly
pre-expiry. Under `EXECUTION-FAILURE-TERMINALITY: EF-1`, every E strictly
before final E is `succeeded`; any E with outcome `failed`, `cancelled`, or
`indeterminate` is final E and has no later E in that lifecycle. Final E and
global final V still exactly bind the two top-level outcomes, and passed
verification requires every V outcome passed and every per-type final V
passed. Mixed V outcomes remain valid on non-passed histories when global
final V matches the top-level non-passed outcome. A non-passed V does not
terminate later V evidence or impose severity precedence, but it prevents the
same lifecycle from regaining passed verification or success; successful
reverification requires a fresh lifecycle under fresh applicable
authorization, without new retry or verification wire state. Every E follows
final P and every V follows every E by strict sequence and non-decreasing
timestamp. EF-1 introduces no E-to-E timestamp relation.

If any P is failed or indeterminate, that P is the final P, every earlier P is
passed, no later P/E/V exists, E and V are empty, and the receipt uses
`not-attempted/not-performed`. Applicable release evidence, sanitization, and
terminal F remain required, and the lifecycle follows the existing
denied/fail-closed and release-precedence semantics. Recovery from P terminality
requires a fresh task, contract, attempt, and receipt lifecycle.

A final non-success E instead records attempted execution and terminates only
further E. It retains its exact top-level `executionOutcome`, proceeds through
required V, pre-release evidence, ownership-checked L when applicable,
sanitization, F, receipt-digest validation, and delivery, and never authorizes
a later E through release failure or any other terminal-processing result. A
retry starts a fresh lifecycle and repeats task resolution, Project/Domain
resolution, routing, HostOverlay binding, live Git/runtime inspection, lease
acquisition when required, pre-issuance revalidation, trusted TaskContract
issuance, and immediately-before-action P. No retry/recovery wire state,
public field, digest, or chronology edge is added. A
`not-attempted/not-performed` receipt keeps E and V empty and may omit P.

The focused final-E family retains exactly eight positives: four single-E
cases for final `succeeded`, `failed`, `cancelled`, and `indeterminate`, plus
four multiple-E cases in which every earlier E is `succeeded` and the final E
independently takes each of those four outcomes with a matching top-level
`executionOutcome`. Its negatives are mechanically 12 final-E mismatch-matrix
classes + 9 existing non-matrix classes + 1 EF-1 terminality class = 22. The
new class rejects any `failed`, `cancelled`, or `indeterminate` E followed by
any later E. Its `3 x 4 = 12` earlier-terminal/later-outcome combinations are
mandatory non-additive value variants of that one primary predicate, with
otherwise-valid P, E sequence/IDs/vocabulary, later-final top-level binding,
V, scope, release, sanitization, F, digest, and cross-artifact binding.

For every issued receipt, GTypes is exactly `intent-validation`,
`project-domain-resolution`, `role-routing`, `host-binding`, and
`initial-preflight`. Each type is present at least once and every actual G has
outcome `passed`. The greatest-sequence finalG remains a deterministic
diagnostic selector only: a failed or indeterminate G invalidates the current
receipt even if a later same-type G passed. Recovery requires a fresh task,
attempt, and lifecycle; no retry epoch or recovery identifier is added.
Repeated same-type G is valid only when every member is passed. Every issued
receipt also has exactly one passed I.

A lease-required issued receipt specializes the unified stable-acquired
prefix: singleton passed A and R, no N, and `every G < A < R < I < every P`. A no-lease issued receipt has no A or R,
singleton passed N, no lease identity, and
`every G < N < I < every P`. Attempted receipts retain
`final P < every E < every V`; non-attempted receipts keep E/V empty, may omit
P, and order every present P after I. Missing, duplicate, non-passed, or wrong-
path A/R/N/I and any G, A, R/N, or I sequence inversion reject.

#### Cumulative pre-contract-denial prerequisites

Use G1..G5 for intent-validation, project-domain-resolution, role-routing,
host-binding, and initial-preflight in that order; N for
pre-issuance-revalidation; A for lease-acquisition; R for
post-acquisition-revalidation; I for contract-issuance; P/E/V for
pre-action-revalidation/execution/post-execution-verification; L for
lease-release; and F for receipt-finalization. Each abbreviation denotes its
complete same-receipt type subset, not merely its selected final member.
The controller candidate is the greatest-sequence check whose type equals
denialCheckpoint. Selection is pure preparation, not acceptance.

For each denial the required controllerCheckId resolves exactly to that
candidate; its outcome is failed or indeterminate, its observedAt equals
preContractEvidence.observedAt, and its canonical reasonCodes exactly equal
the evidence's non-empty reasonCodes. sanitizedSummary is explanatory only
and need not equal optional check prose.

| Controller family | Allowed denial history | Required interpretation |
| --- | --- | --- |
| Repeatable observations: G1..G5, N, R | zero or more passed members, then one failed/indeterminate greatest controller | first non-passed is final; no later recovery |
| State-creating A | exactly one failed/indeterminate A | no earlier passed A; no implicit retry epoch |
| State-creating I | exactly one failed/indeterminate I | no earlier passed I; no implicit retry epoch |

A passed A creates acquisition state. Later denial must use acquired R or
acquired I lifecycle; it cannot erase successful acquisition into not-acquired
or indeterminate. At an A denial, failed means conclusive no ownership and
maps exactly to not-acquired; indeterminate maps exactly to indeterminate.
A passed I means a contract exists, so subsequent evidence cannot fabricate
a pre-contract-denial origin. The four histories passed-A→failed-A,
passed-A→indeterminate-A, passed-I→failed-I, and passed-I→indeterminate-I
are rejected by the state-creating cardinality rule even when their final
controller, outcome, digests, and cleanup claims look plausible.

Let O be exactly G1..G5, N, A, R, I, P, E, V. For the selected row:
every listed prerequisite type is present; every actual prerequisite member
is passed and precedes the controller by sequence; only prerequisite types
and the controlling ordinary type may occur; no ordinary member follows the
controller. All unlisted ordinary types are empty everywhere. Repeated
prerequisite G observations are allowed only when all pass and precede the
controller. On either acquired-denial row they MUST additionally satisfy the
unified every-G-before-A sequence and timestamp predicates; preceding the
controller alone is insufficient. Acquired A is always singleton; prerequisite N or R before an I
denial is singleton passed. Earlier same-type controller observations are
allowed only for the repeatable family and must all pass.

| Denial checkpoint / controlling type | Required passed prerequisites | State | Cleanup |
| --- | --- | --- | --- |
| intent-validation | none | not-required or not-attempted | L empty; F |
| project-domain-resolution | G1 | not-required or not-attempted | L empty; F |
| role-routing | G1, G2 | not-required or not-attempted | L empty; F |
| host-binding | G1, G2, G3 | not-required or not-attempted | L empty; F |
| initial-preflight | G1, G2, G3, G4 | not-required or not-attempted | L empty; F |
| pre-issuance-revalidation | all G | not-required | L empty; F |
| lease-acquisition | all G | failed→not-acquired; indeterminate→indeterminate | L empty; F; indeterminate warning when applicable |
| post-acquisition-revalidation | all G, singleton A; every G < A < every R | acquired | one or more L; F |
| contract-issuance, no-lease | all G, singleton N | not-required | L empty; F |
| contract-issuance, acquired | all G, singleton A, singleton R; every G < A < R < I controller | acquired | one or more L; F |

These ten rows cover nine checkpoints and both issuance-denial branches;
all other checkpoint/state pairs are forbidden by the closed origin union.
Every row has executionOutcome not-attempted, verificationOutcome
not-performed, changedPaths empty, ordinaryOperationEvidence absent,
sanitization.applied true, and exactly one passed terminal F.
Every release-required row uses the unified X/Source/A/every-R/every-L
binding and universal every-G-before-A and A-before-every-R sequence and
timestamp rules.
Every Dpre member (all non-L/non-F checks) precedes every L, every L precedes
F, and all non-F evidence is no later than sanitization, then F, then finish.
Controller/evidence timestamp equality is an identity predicate; its implied
chronology consequences receive no extra owner.

G/N/R histories passed*→failed/indeterminate remain valid under the table.
Any earlier non-passed observation rejects. A/I never use this repeat rule.
Failed or indeterminate L followed by passed finalL remains valid with correct
binding, chronology, final-L outcome mapping, and warnings; release retries
do not authorize acquisition or issuance retries.


#### Lease-acquisition evidence chain

GTypes is exactly intent-validation, project-domain-resolution, role-routing,
host-binding, and initial-preflight. Every issued receipt contains at least
one check of each G type and every actual G is passed. Repeated G is permitted
only when all pass; finalG is diagnostic only and cannot erase an earlier
failure. Every issued receipt contains exactly one passed I.

For lease-required issued receipts, A and R are singleton passed, N is empty,
and the unified X and exactly one Source are mandatory. For no-lease issued
receipts, N is singleton passed, A/R/L/X/Source are absent. In both branches
all eight receipt/C equalities and the complete C digest must validate.

```text
unified stable-acquired prefix, sequence:
  every G < A < every R
unified stable-acquired prefix, time:
  every G <= A <= every R

issued lease-required suffix, sequence:
  singleton R < I < every P
issued lease-required suffix, time:
  R <= C.issuanceCheckpoint.observedAt
  C.issuanceCheckpoint.observedAt <= C.freshness.issuedAt <= I <= every P
issued no-lease, sequence:
  every G < N < I < every P
issued no-lease, time:
  every G <= N <= C.issuanceCheckpoint.observedAt
  C.issuanceCheckpoint.observedAt <= C.freshness.issuedAt <= I <= every P
```

Sequence comparisons are strict. Each listed timestamp edge permits equality.
Every actual G and every actual P participates. The stable-acquired prefix is
origin-independent; the issued suffixes and no-lease branch apply to both
attempted and not-attempted issued receipts. A not-attempted receipt may omit P
and has E/V empty; I and the required G/A/R or G/N prefix remain mandatory.
Attempted receipts additionally require finalP < every E < every V by sequence,
finalP <= every E <= every V by time, every P passed and strictly before expiry,
and the unchanged EF-1 and C-UNIVERSAL-PASS outcome rules.

The unified acquisition block applies identically to acquired denials:
Source task/check/lease equality, source recomputation, X exact digest copy,
X.checkId=A.checkId, and every A/R/L reference are mandatory before digest
acceptance. The issued branch additionally compares X.leaseId=C.leaseId.
No-lease issuance cannot invent acquisition evidence. Static integrity is not
trusted provenance, event truth, current lease ownership, or authorization.


F is closed with exactly sequence, checkId, checkType, outcome, observedAt, profileId, and reasonCodes. It requires checkId check.receipt-finalization, profileId profile.validation.v1, outcome passed, and reasonCodes []. F forbids every summary, postconditionRef, leaseAcquisitionRef, payload, and unknown member. Check IDs are receipt-wide unique. Duplicate exact F therefore also violates generic check-ID uniqueness. Sanitization.applied must be true.

#### Lease release and receipt finalization evidence

For any receipt, define:

```text
L = every checks[] member where checkType == "lease-release"
F = every checks[] member where checkType == "receipt-finalization"

releaseRequired =
  issued-contract with referenced C where C.spec.leaseRequired == true
  or pre-contract-denial where leaseAcquisition.state == "acquired"
```

For every pre-contract denial, additionally define:

```text
Dpre =
  every checks[] member whose checkType is neither
  "lease-release" nor "receipt-finalization"
```

Every actually serialized `ExecutionReceipt`—issued-contract or pre-contract
denial, lease or no-lease, attempted or not-attempted, and acquired,
non-acquired, or indeterminate—contains exactly one F. Its outcome is
`passed`, and it is the unique terminal greatest-sequence member of the
entire checks array:

```text
count(F) == 1
F.outcome == "passed"

for every non-F check q:
  q.sequence < F.sequence
  q.observedAt <= sanitization.completedAt

sanitization.completedAt <= F.observedAt
F.observedAt <= finishedAt

for every pre-contract-denial receipt:
  preContractEvidence.observedAt <= sanitization.completedAt
```

The existing `startedAt` lower bounds remain applicable. Thus every non-F
check and every denial's `preContractEvidence` is no later than sanitization;
sanitization completes no later than F; and F is no later than `finishedAt`.
Whole-second equality is allowed at each of these non-freshness boundaries. In
particular, every denial has the direct chain
`preContractEvidence.observedAt <= sanitization.completedAt <= F.observedAt`
even when L is empty. An acquired denial additionally retains
`preContractEvidence <= every L`, `Dpre <= every L`, and, through the universal
non-F rule, `every L <= sanitization`; that L-to-sanitization instance is
non-additive rather than a separate chronology primitive.

F is the finalization completion gate recorded only after sanitization. It
means exactly that the lifecycle evidence and known release outcome in the
receipt projection have been sanitized and closed for receipt finalization. It
does not mean that `receiptDigest` has already been inserted, that F proves
itself hashed, that delivery occurred, that the lifecycle succeeded, or that
lease release succeeded.

The digest pipeline is unchanged and ordered exactly as follows: produce all
lifecycle evidence; establish `releaseOutcome`; complete sanitization; record
the passed terminal F; freeze the complete projection excluding only
`spec.receiptDigest`; apply JCS, framing, and SHA-256; insert the digest; then
require delivery to copy it exactly. F is evidence inside the projection, not
a self-hash, delivery marker, release proof, or digest-insertion proof.

When L is non-empty, `finalL` is the unique greatest-sequence member of L.
Every release-required receipt has `count(L) >= 1`. Every L precedes F by
strict sequence and non-decreasing timestamp. No check may occur after F.

For every release-required receipt and every pair of distinct members `l1` and
`l2` in L, Phase 1 applies this rule to their already-validated
`canonicalUtcTimestamp` instants:

```text
if l1.sequence < l2.sequence:
  instant(l1.observedAt) <= instant(l2.observedAt)
```

The comparison is universal over all ordered pairs, not only adjacent L
members. Whole-second equality is allowed. It applies identically to a lease-
required issued receipt and an acquired pre-contract denial. `finalL` remains
selected only by greatest sequence; timestamps are neither a selector nor a
tie-breaker. This rule adds no E-to-E or global check-timestamp monotonicity.

On both stable-acquired origins, every L requires leaseAcquisitionRef == {checkId: acquisitionBinding.checkId}. Source, binding, A, every R, and every L identify the same acquisition. Earlier failed/indeterminate L members remain subject to the same universal binding. A correctly bound finalL cannot hide an earlier mismatch. Indeterminate acquisition has no stable binding, Source, compact reference, or L.

For an issued-contract receipt, the actual pre-release set is every present
check whose type is in this exact closed eleven-type set:

```text
intent-validation
project-domain-resolution
role-routing
host-binding
initial-preflight
lease-acquisition
post-acquisition-revalidation
contract-issuance
pre-action-revalidation
execution
post-execution-verification
```

This set definition does not require every type to be present; it closes which
present checks are pre-release. Every actual pre-release check has a lower
sequence than every l in L and an equal or earlier `observedAt`.

For an acquired pre-contract denial, every d in Dpre has a lower sequence than
every l in L and an equal or earlier `observedAt`. The derived
`preContractEvidence.observedAt <= l.observedAt` relation also holds for every
l. Consequently release cannot begin and then be followed by host binding,
initial preflight, revalidation, contract-issuance evidence, or any other
non-L/F check. No nonexistent TaskContract is required, and the existing
denial-path E/V and changed-path empty-set rules remain unchanged.

For every release-required receipt, `releaseOutcome` is bound exactly to
`finalL`: final `passed` maps only to
`succeeded`, final `failed` maps only to `failed`, and final `indeterminate`
maps only to `indeterminate`. An acquisition result, an earlier release check,
or a general verification check cannot substitute for `finalL`. Receipt
finalization therefore follows recorded release evidence rather than merely
following a copied top-level release claim.

If `finalL` is `failed` or `indeterminate`, at least one unresolved coordination
warning must have `relatedCheckId` exactly equal to `finalL.checkId`; a warning
bound only to an earlier release check is insufficient. An earlier failed or
indeterminate L followed by a final passed L is valid only when every ordered L
pair also satisfies the non-decreasing timestamp rule. It then produces
`releaseOutcome: succeeded` and does not require a warning solely because of
the earlier member. Existing lifecycle rules still prevent a succeeded
lifecycle when any unresolved coordination warning remains.

On every no-release path L is empty but the universal singleton passed terminal
F remains required. A no-lease issued receipt has
`releaseOutcome: not-required`, no associated Source, receipt-level acquisitionBinding, or compact reference, and
no compact lease-acquisition reference on any check. Pre-contract denials in `not-required`,
`not-attempted`, or `not-acquired` acquisition state also have L empty and
`releaseOutcome: not-required`. An `indeterminate` acquisition has no stable
lease identity, keeps L empty, requires both release and lifecycle outcomes
`indeterminate`, retains its required unresolved warning, and still ends in
passed F because F records evidence closure rather than acquisition or release
success. Any L on one of these paths is invalid. Future policy may decide
whether to emit a pre-contract-denial receipt; once one is serialized, F is
mandatory.

The complete evidence chains below specialize the unified stable-acquired
prefix where X exists; their origin variants do not add primary owners:

```text
lease required, attempted, by sequence:
  every G < A < R < I < every P
  final applicable P < every E < every V
  every actual pre-release check < every L < F

lease required, not attempted, by sequence:
  every G < A < R < I < every present P
  E == empty and V == empty
  every actual pre-release check < every L < F

no lease, attempted, by sequence:
  every G < N < I < every P
  final applicable P < every E < every V < F
  A == empty and R == empty and L == empty

no lease, not attempted, by sequence:
  every G < N < I < every present P < F
  E == empty and V == empty
  A == empty and R == empty and L == empty

acquired R denial, by sequence:
  every G < A < every R; greatest R is the denial controller
  every Dpre < every L < F

acquired I denial, by sequence:
  every G < A < every R < singleton I controller
  every Dpre < every L < F

both acquired-denial branches, by time:
  every G <= A <= every R
  every Dpre <= every L; preContractEvidence <= every L

every other pre-contract denial, by sequence:
  every non-F check < F
  L == empty
```

For every listed lifecycle path, all non-F evidence is no later than
sanitization, sanitization is no later than F, and F is no later than
`finishedAt`. Every pre-contract denial consequently orders
`preContractEvidence` no later than sanitization. Acquired denials additionally
order `preContractEvidence` and every Dpre member no later than every L; every
L is then covered by the universal non-F-to-sanitization relation.

Greatest-sequence selections and strict sequence comparisons are
sequence/outcome consistency invariants and do not themselves add timestamp
relations; the explicit pairwise L rule is independent of `finalL` selection.
The detailed chronology inventory below displays 31 normative relations,
classifies 20 as primitive/additive, and marks eleven transitive consequences
derived/non-additive.


#### Timestamp chronology

The complete graph below uses validated whole-second UTC instants.
Checkpoint abbreviates C.spec.issuanceCheckpoint.observedAt. Start, finish,
sanitization, and all named checks belong to the same receipt; issuedAt and
expiresAt belong to the same fully bound C. Exactly two relations are strict:
issuedAt<expiresAt and every passed P<expiresAt. Sequence and timestamp
graphs are separate; no sequence edge supplies an unstated timestamp edge.

The current ledger is rebuilt from all lifecycle paths, mandatory non-F
membership, controller/evidence exact equality, and the full issuance bracket.
It has 31 displayed relations: 20 independent primitive predicate families and
11 derived/non-additive relations. Current IDs are continuous CH01..CH20,
with one positive CH-Pnn and one independent negative CH-Nnn per row.
Historical review IDs retain their historical meaning.

| Current owner pair | Context | Primitive relation | Isolating negative assignment |
| --- | --- | --- | --- |
| CH-P01 / CH-N01 | TaskContract checkpoint | `checkpoint <= issuedAt` | TaskContract alone; checkpoint 2, issuedAt 1, expiry 3. |
| CH-P02 / CH-N02 | TaskContract freshness | `issuedAt < expiresAt` | TaskContract alone; checkpoint 0, issuedAt 1, expiry 1. |
| CH-P03 / CH-N03 | Every receipt check q | `startedAt <= q.observedAt` | G1-denial; start 2, controller/evidence 1, sanitization 3, F/finish 4. |
| CH-P04 / CH-N04 | Every non-F check q | `q.observedAt <= sanitization.completedAt` | No-lease issued, no P/E/V; I 2, sanitization 1, F/finish 3, other times 0. |
| CH-P05 / CH-N05 | Every passed P, issued | `P.observedAt < expiresAt` | No-lease issued; checkpoint/issuedAt 0, expiry 1, I 0, passed P 1, E/V empty, closure 2. |
| CH-P06 / CH-N06 | Attempted issued, every E | `finalP.observedAt <= E.observedAt` | P 2, one E 1, every V 3, expiry 9; prefix 0, closure 4. |
| CH-P07 / CH-N07 | Attempted issued, every E/V pair | `E.observedAt <= V.observedAt` | P 0, E 2, V 1, expiry 9; prefix 0, closure 3. |
| CH-P08 / CH-N08 | Every stable-acquired path, every G | `G.observedAt <= A.observedAt` | Acquired R-denial: one G 2, other G 0, A 1, every R/controller/evidence 3, every L 4, closure 5; keep every G<A by sequence. Issued lease and acquired I are non-additive variants. |
| CH-P09 / CH-N09 | Issued no-lease, every G | `G.observedAt <= N.observedAt` | One G 2, N 1, checkpoint/issuedAt/I 3, closure 4. |
| CH-P10 / CH-N10 | Every stable-acquired path, every R | `A.observedAt <= R.observedAt` | Acquired R-denial; A 2, earlier passed R 1, controller/evidence R 3, L 4, closure 5; sequence A<R<R. |
| CH-P11 / CH-N11 | Issued lease | `R.observedAt <= checkpoint` | A 0, R 2, checkpoint 1, issuedAt/I 3, L 4, closure 5. |
| CH-P12 / CH-N12 | Issued no-lease | `N.observedAt <= checkpoint` | G 0, N 2, checkpoint 1, issuedAt/I 3, closure 4. |
| CH-P13 / CH-N13 | Issued, singleton I | `issuedAt <= I.observedAt` | Prefix/checkpoint 0, issuedAt 2, I 1, no P/E/V, expiry 9, closure 3. |
| CH-P14 / CH-N14 | Issued, every P | `I.observedAt <= P.observedAt` | Prefix/issuedAt 0, I 2, P 1, expiry 9, no E/V, closure 3. |
| CH-P15 / CH-N15 | Issued lease, every pre-release q / every L | `q.observedAt <= L.observedAt` | Prefix/issuedAt 0, I 2, L 1, no P/E/V, closure 3. |
| CH-P16 / CH-N16 | Acquired denial, every Dpre / every L | `Dpre.observedAt <= L.observedAt` | Acquired R-denial: every G 0, A 1, every R/controller/evidence 3, every L 2, closure 4; G→A→R sequence/time and pairwise L times remain valid. |
| CH-P17 / CH-N17 | Every receipt | `sanitization.completedAt <= F.observedAt` | Non-F 0, sanitization 2, F 1, finish 3. |
| CH-P18 / CH-N18 | Every receipt | `F.observedAt <= finishedAt` | Non-F/sanitization 0, F 2, finish 1. |
| CH-P19 / CH-N19 | Existing delivery pair only | `finishedAt <= attemptedAt` | Valid receipt finish 2, delivery attempt 1. |
| CH-P20 / CH-N20 | Every release-required path; every ordered pair L1<L2 | `L1.observedAt <= L2.observedAt` | Pre-release 0, L1 2, L2 1, sanitization/F/finish 3. |

The assignments are offsets in whole seconds from the synthetic epoch
2000-01-01T00:00:00Z. Unspecified start/prefix times are 0, omitted suffixes
are legitimately not-attempted, and unspecified expiry is 9. Complete the
applicable valid lifecycle, preserve outcomes/identities/sequence, set remaining
closure times to the stated closure, and recompute dependent digests.
Each row reverses only that independent timestamp family. Derived displays may
also fail and are attributed to the same owner. Positive counterparts restore
the target comparison to equality (or one second separation for strict rows).
Origin, repeated-member, non-adjacent-member, and later-correct-member cases
are mandatory non-additive variants. In CH08, keep every G before A by sequence,
put an earlier G at second 2, a later same-type G at 0, and A at 1; the later
valid timestamp cannot hide the earlier violation. Equality G.time=A.time
remains valid. In CH10 the earlier passed R witnesses
universality while the controlling R remains after A in both time and sequence.

| Display | Derived relation | Proof from the complete graph |
| --- | --- | --- |
| 21 | startedAt <= sanitization | Every valid path has at least one non-F check; CH03 then CH04. |
| 22 | sanitization <= finishedAt | CH17 then CH18. |
| 23 | startedAt <= finishedAt | Display 21 then CH17 then CH18. |
| 24 | startedAt <= denial evidence | Evidence time equals its required controller time; CH03. |
| 25 | denial evidence <= sanitization | Controller is non-F; exact equality then CH04. |
| 26 | denial evidence <= F | Display 25 then CH17. |
| 27 | startedAt <= issuedAt | Required R or N has CH03 lower bound; CH11 or CH12 then CH01. |
| 28 | denial evidence <= every L | Controller belongs to Dpre; exact equality then CH16. |
| 29 | every non-F <= F | CH04 then CH17. |
| 30 | issued R <= issuedAt | CH11 then CH01. |
| 31 | issued N <= issuedAt | CH12 then CH01. |

The superseded ledger's CH03, CH06, CH07, CH08, and CH20 are therefore
derived/non-additive (displays 21, 24, 25, 27, and 28 respectively); they have
no current independent reversal owner. The unified stable-acquired every-G→A
relation is independently primitive CH08, and A→every-R is independently
primitive CH10. Generalizing lifecycle applicability adds origin variants,
not new owners on top of their issued-path predicates.

For a mechanical independence check, expand each universal family into edges
on a legal lifecycle, identify controller/evidence nodes by their equality,
remove one candidate family, and compute transitive reachability of all
remaining primitive edges, carrying strictness through any strict edge.
The table supplies a satisfying assignment for the remaining graph plus the
candidate's reversal. Displayed consequences are verified by closure, never
counted again. Conditional operands must exist on the chosen lifecycle;
vacuous omitted-event comparisons are not fabricated witnesses.

There is no global adjacent-check timestamp order, no E-to-E, G-to-G, or
R-to-R timestamp monotonicity. CH20 alone orders same-type L timestamps by
sequence, universally over every ordered pair. finalL is constructed by
sequence during preparation, then tested against chronology and outcomes.
Failed L→passed finalL and indeterminate L→passed finalL remain valid when
all pairwise times and bindings pass. Completion, sanitization, F, and
delivery need not precede contract expiry.


#### Current independent owner ledger

This ledger replaces current PB/AI/DP/RF/RC primary numbering; historical
review records and their IDs remain historical. Every row below is one
conditional logical invariant and has exactly one positive owner PREFIX-Pnn
and one negative owner PREFIX-Nnn. The row's negative is a constructive
isolating recipe. Positive counterparts restore that row with otherwise-valid
inputs. Distinct positive specimens use distinct synthetic receipt IDs and
are counted once, never once per predicate they happen to satisfy.

Shape predicates are evaluated before predicates needing shaped operands;
presence/cardinality predicates precede singleton identity/outcome/sequence
operands. An unavailable operand rejects at its presence owner, not a second
invented mismatch. This is validation dependency, not permission to accept
missing data. For each negative, preserve all unrelated independent predicates,
recompute valid prerequisite digests and every dependent evidence/receipt digest,
and preserve delivery copies when present. Claimed-invalid source computation
and claimed-invalid exact-copy cases are the explicit exception at their target
edge. A digest side effect is never counted as another primary.

Families distinguish shape, presence/cardinality, identity equality, sequence,
timestamp, outcome, digest computation/copy, scope, and finalization.
Generic array/lexical/closed-union faults keep their existing structural owner.
Forbidden compact-reference placement is one generic shape predicate;
its G/N/I/P/E/V/F and non-stable-path manifestations are variants.
The closed denial checkpoint/state union remains mandatory independently of
its outcome-to-state rule. The complete chronology graph and its CH owners
are specified separately.

| PB current owner pair | Family | Required predicate | Isolating negative recipe |
| --- | --- | --- | --- |
| PB-P01 / PB-N01 | shape | postconditionRef occurs only on V | Put an otherwise closed valid reference on one non-V check; all thirteen non-V types are variants. |
| PB-P02 / PB-N02 | shape | postconditionRef has exactly required type | Use one extra member or omit type on V; lexical enum/membership checks require a shaped operand. |
| PB-P03 / PB-N03 | shape | postconditionRef.type is in the eleven-token enum | Use one unknown type on V; closed-contract membership is tested only for well-shaped references. |
| PB-P04 / PB-N04 | identity equality | Every well-shaped V reference names a required type in the same C | Use an allowed enum type absent from C, retaining evidence for every actually required type. |
| PB-P05 / PB-N05 | presence/cardinality | Every required type has at least one V(t) on an attempted receipt | Keep general V and all other obligations, but omit the named type; scope-contained and all ten optional types are variants. |

| AI current owner pair | Family | Required predicate | Isolating negative recipe |
| --- | --- | --- | --- |
| AI-P01 / AI-N01 | presence/cardinality | Every issued G type is present | Omit one G type from a no-lease issued prefix. |
| AI-P02 / AI-N02 | outcome | Every issued G is passed | One G fails; a later passed same-type G is a variant, never recovery. |
| AI-P03 / AI-N03 | presence/cardinality | Stable-acquired paths have exactly one A | Omit A or add a distinct-ID A; identity/sequence checks require the singleton operand. |
| AI-P04 / AI-N04 | outcome | The stable-acquired singleton A is passed | Change its outcome only; controller A denials are outside this predicate. |
| AI-P05 / AI-N05 | presence/cardinality | Issued lease-required R is singleton | Omit R or add a distinct-ID passed R; acquired denial R history is not constrained by this issued-only predicate. |
| AI-P06 / AI-N06 | presence/cardinality | Issued no-lease N is singleton | Omit N or add a distinct-ID passed N. |
| AI-P07 / AI-N07 | presence/cardinality | Issued I is singleton | Omit I or add a distinct-ID passed I; denial I is DP11-owned. |
| AI-P08 / AI-N08 | outcome | Issued singleton R/N/I is passed | Change one applicable singleton outcome; all type/outcome forms are variants. |
| AI-P09 / AI-N09 | presence/cardinality | Issued lease path forbids N; issued no-lease path forbids A/R | Add a wrong-path check without a forbidden compact reference; binding presence is evaluated from C. |
| AI-P10 / AI-N10 | sequence | Every G precedes A on every stable-acquired path, or N on issued no-lease paths | Move one G after A/N but before every R, I, denial controller, L, and F that is present; preserve valid timestamps. Issued lease, acquired R, acquired I, and no-lease N are non-additive variants. |
| AI-P11 / AI-N11 | sequence | Stable singleton A precedes every R | Acquired R denial: put an earlier passed R before A and keep the controlling R after A; all timestamps equal. |
| AI-P12 / AI-N12 | sequence | Issued applicable R/N precedes I | Swap the two checks, keeping timestamps equal and G/A before both. |
| AI-P13 / AI-N13 | sequence | Every issued I precedes every P | Put an earlier P before I and later P after it; keep E/V empty and times equal. |
| AI-P14 / AI-N14 | presence/cardinality | X is present iff the stable-acquired condition holds | Omit X with Source retained, or add X on a non-stable path; binding operands are otherwise gated. |
| AI-P15 / AI-N15 | presence/cardinality | Source count is one iff stable-acquired, otherwise zero | Supply zero or two eligible Sources on a stable path, or one on a non-stable path. |
| AI-P16 / AI-N16 | identity equality | Source.taskId equals receipt.taskId | Change Source.taskId, recompute its digest and exact binding copy; keep receipt/C task equality. |
| AI-P17 / AI-N17 | identity equality | Source.checkId equals X.checkId | Change Source.checkId; keep X=A and every ref=X; recompute Source and descendant digests. |
| AI-P18 / AI-N18 | identity equality | Source.leaseId equals X.leaseId | Change Source.leaseId; keep issued X=C.leaseId and every check binding; recompute descendants. |
| AI-P19 / AI-N19 | digest computation/copy | Source digest matches its closed source-profile computation | Use a different valid tagged Source digest and copy it exactly into X; rehash descendants. |
| AI-P20 / AI-N20 | digest computation/copy | X digest copies the validated Source digest exactly | Keep valid Source, use a different well-shaped X digest, and rehash descendants. |
| AI-P21 / AI-N21 | identity equality | X.checkId equals the singleton A.checkId | Source and X agree; rename A only, preserving the self-reference value X and all other references. |
| AI-P22 / AI-N22 | identity equality | A compact reference equals {checkId:X.checkId} | Omit or alter A's compact reference; Source/X/A IDs themselves remain equal. |
| AI-P23 / AI-N23 | identity equality | Every R compact reference equals {checkId:X.checkId} | Alter an earlier passed R only, retaining a correctly bound controlling R; issued R and acquired I prerequisite R are variants. |

| DP current owner pair | Family | Required predicate | Isolating negative recipe |
| --- | --- | --- | --- |
| DP-P01 / DP-N01 | presence/cardinality | Every denial prerequisite type exists | Remove one required G/N/R stage; stable A presence remains AI03-owned. |
| DP-P02 / DP-N02 | outcome | Every denial prerequisite observation G/N/R is passed | Fail a prerequisite G while keeping the controller and its same-type history valid. |
| DP-P03 / DP-N03 | scope | Only row-prerequisite and controller ordinary types occur | Add unreached P before the controller with all other boundaries valid. |
| DP-P04 / DP-N04 | sequence | Every ordinary prerequisite member precedes the controller | No-acquisition G5 denial: move one repeated passed prerequisite G1 after the controller but before F; all times remain valid. |
| DP-P05 / DP-N05 | identity equality | controllerCheckId names the greatest mapped-type candidate | Name a different same-receipt check; candidate type/outcome/time/reasons stay valid. |
| DP-P06 / DP-N06 | outcome | The mapped-type controller candidate is failed or indeterminate | Use passed R as the candidate, with otherwise-valid acquired origin and cleanup. |
| DP-P07 / DP-N07 | identity equality | Evidence.observedAt equals controller.observedAt | Change only evidence time within all remaining chronology bounds and rehash evidence. |
| DP-P08 / DP-N08 | identity equality | Evidence.reasonCodes exactly equal controller.reasonCodes | Use another non-empty canonical reason array; summaries remain unconstrained derivatives. |
| DP-P09 / DP-N09 | outcome | Every earlier G/N/R controller-family observation is passed | Use failed or indeterminate earlier same-type observation then failed/indeterminate controller. |
| DP-P10 / DP-N10 | presence/cardinality | A-denial has exactly one A | Insert earlier passed A before single failed/indeterminate A controller; no X or Source. |
| DP-P11 / DP-N11 | presence/cardinality | I-denial has exactly one I | Insert earlier passed I before failed/indeterminate I controller, with valid N or acquired A/R prefix. |
| DP-P12 / DP-N12 | presence/cardinality | An I-denial's prerequisite N/R has at most one member | Duplicate the passed prerequisite N or R with a distinct ID; all refs/times remain valid. |
| DP-P13 / DP-N13 | outcome | A-denial outcome maps failed→not-acquired and indeterminate→indeterminate | Swap the two permitted states, adapting release/lifecycle/warning claims to that state; only the causal state mapping fails. |

| RF current owner pair | Family | Required predicate | Isolating negative recipe |
| --- | --- | --- | --- |
| RF-P01 / RF-N01 | presence/cardinality | Release-required paths have at least one L | Remove every L; finalL-dependent checks are gated, not separately counted. |
| RF-P02 / RF-N02 | presence/cardinality | No-release paths have no L | Add unreferenced L to a no-lease receipt, preserving not-required release and F. |
| RF-P03 / RF-N03 | outcome | releaseOutcome equals the finalL mapping | Change top-level release outcome and its lifecycle consequences, retaining valid warnings. |
| RF-P04 / RF-N04 | presence/cardinality | Every serialized receipt has at least one F | Remove F; maximum-one is derived from exact F ID and check-ID uniqueness. |
| RF-P05 / RF-N05 | outcome | The singleton F is passed | Use failed or indeterminate F with its exact identity tuple. |
| RF-P06 / RF-N06 | finalization | F uses exact reserved checkId/profileId/empty reasonCodes | Change one identity member to a valid alternative; F outcome remains passed. |
| RF-P07 / RF-N07 | shape | F forbids generic-check summary fields | Add expectedSummary or observedSummary; unknown fields remain generic-owned, postconditionRef is PB01-owned, and compact placement is generic-owned. |
| RF-P08 / RF-N08 | sequence | F is terminal | Put one otherwise-permitted non-F check after F with valid timestamps. |
| RF-P09 / RF-N09 | sequence | Every issued pre-release check precedes every L | Put an L before I while retaining G/A/R/I order and terminal F. |
| RF-P10 / RF-N10 | sequence | Every acquired-denial Dpre precedes every L | Put L before the controller but after all prerequisites; all times equal. |
| RF-P11 / RF-N11 | identity equality | Failed/indeterminate finalL has an exactly related warning | Retain only a warning naming an earlier valid check, not finalL. |
| RF-P12 / RF-N12 | identity equality | Every L compact reference equals {checkId:X.checkId} | Alter an earlier L only; finalL remains correctly bound. Both stable origins are variants. |
| RF-P13 / RF-N13 | finalization | sanitization.applied is true | Use false with otherwise-valid times, exact F tuple, zero or positive redactionCount, and rehashed receipt. |
| RF-P14 / RF-N14 | presence/cardinality | Indeterminate acquisition retains an unresolved coordination warning | Use an indeterminate A-denial with empty warnings and otherwise-correct indeterminate outcomes. |

| RC current owner pair | Family | Required predicate | Isolating negative recipe |
| --- | --- | --- | --- |
| RC-P01 / RC-N01 | identity equality | receipt.contractId equals C.metadata.id | Use another valid receipt-origin contract ID. |
| RC-P02 / RC-N02 | digest computation/copy | receipt.contractDigest equals the complete C digest | Use another tagged digest; keep all duplicated non-digest claims equal. |
| RC-P03 / RC-N03 | identity equality | receipt.taskId equals C.spec.taskId | Use another receipt task UUID and a consistently matching Source when applicable. |
| RC-P04 / RC-N04 | identity equality | receipt target projectRef equals C.spec.projectRef | Use another canonical Project reference. |
| RC-P05 / RC-N05 | identity equality | receipt target worktreeRoleRef equals C target role | Use another canonical role reference. |
| RC-P06 / RC-N06 | identity equality | receipt target worktreeId equals C target worktree | Use another logical worktree ID. |
| RC-P07 / RC-N07 | identity equality | receipt domainRefs equal the entire canonical C Domain set | Omit, add, or substitute a Domain while keeping canonical array order. |
| RC-P08 / RC-N08 | identity equality | receipt effectiveMode equals C.spec.effectiveMode | Use the other valid mode without altering C. |
| RC-P09 / RC-N09 | identity equality | Issued X.leaseId equals C.spec.leaseId | Source and X agree on another lease, with valid source digest and exact copy; C remains unchanged. |

The original detailed coverage is retained as mandatory non-additive variants:
all eleven required-postcondition types; referenced/global finalV coincidence;
multiple all-passed V(t); a later general V; all eleven obligations together;
every forbidden non-V reference placement; all nine denial checkpoints with
both I branches; all issued lease/no-lease attempted/not-attempted paths; all
five G types; failed/indeterminate controller values; all finalL outcomes;
every repeated/early-bad/final-good reference case; and all receipt/C Domain
omission/addition/substitution forms. Array reordering is generic canonicality,
not a second RC Domain-identity primary.

Referenced failed/indeterminate V under passed top-level verification is an
instance of the existing C-UNIVERSAL-PASS predicate, shared with general V,
not an additional PB primary. The verification-family owner retains it.
Duplicate F with an exact F tuple necessarily duplicates its reserved check ID;
generic check-ID uniqueness owns that rejection. No independent duplicate-F
primary exists. Source→A equality follows Source→X→A; acquired identity is
AI-owned on both origins and is not counted again under DP. Controller→L
sequence is the Dpre→L instance, owned only by RF10. Evidence→L time is
derived CH display 28. Missing or wrong A/R/L compact references are AI22,
AI23, and RF12 respectively. A valid source/X pair on the wrong issued lease
is RC09, not AI18.

AI10 owns the one conditional G-prefix sequence predicate: its A branch now
covers every stable-acquired origin, while its issued no-lease N branch is
unchanged. The acquired R and I forms add variants, not independent owners.
Without AI10, G5 may follow A while still preceding every R/controller/L/F;
valid times and every remaining sequence family permit that construction.
CH08 likewise owns every G<=A timestamp comparison on all stable-acquired
origins. Without CH08, G5 at second 2, A at 1, and every R at 3 satisfy the
remaining graph. Thus neither edge is derived; both reuse existing owners.
CH16 remains independently necessary: controller/evidence at 3 and L at 2
violates only Dpre<=L while G at 0 and A at 1 satisfy the repaired prefix.
The complete row inventory therefore remains 20 primitive timestamp families,
11 derived displays, and the existing 23 AI families, with no added primary.

The five focused families have PB 5/5, AI 23/23, DP 13/13, RF 14/14,
and CH 20/20 positive/negative owners. Their rebuilt subtotal is
2*(5+23+13+14+20)=150. RC is 9/9, giving a retained subtotal of 168.
The transition-authorization ledger adds three independent TA owner pairs,
so the expanded aggregate including RC and TA is 174.
PB+AI+DP+RF has 110 numbered owner definitions; AI+RF has 74.
Scope/ordinary-capability/operation-evidence coverage remains separate,
with its existing 5/6 plus D5 cross-reference, OC 3/8, and OE 10/11
case inventories. Those unchanged case inventories are not added to the
independent five-family subtotal. These are documented conformance owners,
not a claim that executable Schema/model tests or a fixture manifest exist.

For referenced TaskContract `C`, `Apath` is the union of
`C.spec.authorizedScope.paths` languages and `Qpath` is the union of
`C.spec.prohibitedScope.paths` languages. For receipt `R`, define
`Attempted(e)` as membership in `succeeded`, `failed`, `cancelled`, or
`indeterminate`, and define:

```text
CarrierRequired(R,C) :=
  R.spec.origin.type == "issued-contract"
  and C.spec.allowWrite == true
  and Attempted(R.spec.executionOutcome)
```

The owner-selected A2 design adds exactly one proposed serialized field,
`ExecutionReceipt.spec.ordinaryOperationEvidence`, present if and only if
`CarrierRequired(R,C)`. It is forbidden for denials, non-writing/plan-only
contracts, and not-attempted issued receipts. A writing attempt with complete
zero-effect evidence uses exactly `[]`; failure, cancellation, indeterminacy,
or later release failure does not suppress the required carrier or known
effects.

Each array member is a closed record containing exactly required `path` and
`operations`. `path` reuses `repositoryRelativePath` exactly.
`operations` is a non-empty one-through-three-member distinct set over only
`create`, `modify`, and `delete`. Records are strictly ordered by
`S(record.path)` and operations by `S(token)`, giving token order
`create`, `delete`, `modify`; duplicates, empty operation sets, unknown tokens,
unknown record fields, invalid paths, and non-canonical input order reject
without sorting.

For each unique path, operations are the union of all attributable ordinary
operations during the attempt. Repetition, reversal, restoration, and return
to baseline erase nothing. Transient modify remains `["modify"]`;
create/modify is `["create","modify"]`; create/delete or delete/recreate is
`["create","delete"]`; and rename-equivalent effects are old-path
`["delete"]` plus new-path `["create"]`, never a rename token.

The durable static reconstruction is:

```text
EvidencePaths =
  {record.path | record in R.spec.ordinaryOperationEvidence}

OexecByPath[p] =
  set(the unique record.operations for p)

Oexec =
  union over every OexecByPath[p]
```

`Oexec` is not derived from `changedPaths`, final repository state, summaries,
profiles, reasons, or human interpretation. Every attributable ordinary-effect
path appears in the carrier, and the exact one-way binding is
`EvidencePaths ⊆ set(R.spec.changedPaths)`, not equality. Transient/restored
paths remain in both arrays; extra changed paths do not invent operations.

Passed writing scope evidence requires every `changedPaths` and
`EvidencePaths` member to be in `Apath` and not in `Qpath`, the subset binding,
`Oexec ⊆ Acap`, and `Oexec ∩ Qcap = ∅`. Acap/Qcap remain global
capability sets, not per-path grants. Passed verification also requires passed,
exactly referenced `finalV("scope-contained")`. The Review-14 B path and
operation predicates remain unchanged, and A2 makes `Oexec` durably
reconstructible. C-UNIVERSAL-PASS remains unchanged and independently requires
every V to pass when top-level verification passes.

Missing-required or forbidden-present carrier, malformed shape/order, omitted
known operations, and a carrier path absent from `changedPaths` are invalid
before receipt-digest acceptance. `[]` is valid only with complete zero-effect
evidence; unresolved attribution with every known operation retained is
structurally representable but requires indeterminate verification and cannot
pass. Unauthorized/prohibited paths or operations are structurally
representable but fail scope. Phase 1 validates shape, ordering,
reconstruction, and static binding; Phase 4 owns runtime attribution truth and
completeness. The existing receipt digest covers the complete receipt except
only `receiptDigest`, so it automatically includes the carrier when present
but proves no omitted history.

No external evidence artifact, digest profile, digest computation, or exact
copy is added by the operation carrier; the Option-B graph is 12 paths / 10 computations / 2 exact copies. This is a material pre-publication
wire-shape design change while all resources remain `reserved-unpublished`.
`contextctl.dev/v1alpha1`, `v1alpha1-r1`, and receipt version `1` remain
unchanged pending the `integration-control` compatibility/publication/version
gate. No Schema resource or executable validator is implemented here.

For every non-writing contract, transitions, changed paths, and the ordinary
operation set remain empty and the carrier is forbidden; execute-tests/build
does not widen mutation. The changed-path scope inventory remains exactly 5/6
with the D5 cross-reference, while the separate
`ORDINARY-CAPABILITY-CLOSURE` family remains exactly 3/8.

The OC primary IDs mirror the design exactly: `OC-P01`, `OC-P02`, and
`OC-P03` are authorized, non-prohibited create, modify, and delete;
`OC-N01..OC-N03` omit the respective operation from `Acap`;
`OC-N04..OC-N06` place the respective operation in `Qcap`; `OC-N07` is a
valid-path multi-path composite missing at least one implied operation; and
`OC-N08` is a net-valid contract whose actual execution performs an
unauthorized transient/restored operation on an authorized path. Mandatory
non-additive variants cover untracked and ignored create/delete, tracked
`D -> P`, `P -> D`, and changed `P -> P`, known no-op,
unchanged ref/HEAD/submodule observation and a logical index ordinary no-op, opaque same-present with modify
authorized/absent/prohibited, all three operations across distinct paths, and
rename delete/create with both tokens required. OC does not reuse HX IDs or add
wire state, a reason code, a capability, a transition, or runtime collection;
the separately owned A2 carrier is not an OC addition.

The separate planned `OPERATION-EVIDENCE` family is exactly:

| ID | Primary predicate |
| --- | --- |
| `OE-P01` | one path plus modify |
| `OE-P02` | one path plus create |
| `OE-P03` | one path plus delete |
| `OE-P04` | one path plus create and modify |
| `OE-P05` | one path plus create and delete |
| `OE-P06` | multiple canonically ordered paths |
| `OE-P07` | transient modify then restore |
| `OE-P08` | transient create/delete then restore |
| `OE-P09` | rename-equivalent old-path delete and new-path create |
| `OE-P10` | complete carrier, subset and path predicates, and permitted reconstructed `Oexec` |
| `OE-N01` | missing required carrier |
| `OE-N02` | carrier present where forbidden |
| `OE-N03` | duplicate path |
| `OE-N04` | empty operations |
| `OE-N05` | duplicate operation |
| `OE-N06` | non-canonical outer order |
| `OE-N07` | non-canonical operation order |
| `OE-N08` | unknown operation |
| `OE-N09` | omitted known attributable operation |
| `OE-N10` | carrier path absent from `changedPaths` |
| `OE-N11` | unresolved attribution represented as a passed successful no-op |

OE is 10/11/21 and remains separate from OC. Invalid path and `.git` cases are
D3-owned; unauthorized/prohibited paths are changed-path-scope-owned;
modify-only transient create/delete and rename capability faults remain
non-additive OC-N08/OC-N07 variants; malformed-digest acceptance remains a
non-additive variant of the corresponding OE structural owner. The existing
independent affected-family aggregate including TA is 174 and excludes the separate OC and OE case inventories.

D5 now contains exactly 12 `3 × 4` Cartesian negatives. Removing the retired
administrative-lock transition removes two TaskContract administrative-lock
array rows, while A2 adds the carrier-record and nested-operation rows, so the
array-ordering matrix contains 54 rows. The reusable evidence union retains
its identity and ordering rules.

A `not-attempted/not-performed` receipt has E and V empty, while P is optional.
If P contains a failed or indeterminate member, it is the final P, every earlier
P is passed, and no later P exists; that terminal member may be at or after
expiry. Every passed P must still be strictly pre-expiry. Every stray E or V is
invalid, and a later passed P cannot recover the same lifecycle. Tests MUST
NOT require completion, sanitization, finalization, or delivery before expiry;
infer freshness from `startedAt`; impose `finishedAt <= expiresAt`; introduce
any check kind or denial checkpoint beyond the owner-selected
`pre-issuance-revalidation` identity and matching closed `denialCheckpoint`
enum member; introduce a new timestamp or checkpoint field; require exactly one
P, E, or V member; require global check-type uniqueness; or treat
greatest-sequence selection or sequence comparisons by themselves as timestamp
chronology. The explicit pairwise L rule is independent of finalL selection.
Tests also MUST NOT require E or V members to form contiguous type regions.
Phase 1 checks internal claims only. Phase 4 owns trusted time, authenticity,
actual immediacy, evidence truth, and operational freshness.



### Option-B adversarial construction and disposition matrix

Each mutation starts from the complete acquired-R or acquired-I record in the exact corpus and its one associated Source, or from a complete matching issued pair for RC09. Change only the described semantic edge. Restore contiguous sequence by assigning each physical position as sequence, keep check IDs unique and shapes closed, and recompute every affected Source/evidence/receipt digest and any delivery copy. A target digest/copy fault is deliberately retained only at that edge. This prevents a stale hash from masking the intended predicate.

| Identity case | Concrete isolated mutation | Precise owner |
| --- | --- | --- |
| A=X, R=Y | acquired-I: change the passed R compact checkId to check.other-acquisition, leaving A/Source/binding correct | AI-N23 |
| A=X, L=Y | acquired-I: change its L compact checkId only | RF-N12 |
| Correct R controller, bad earlier R | acquired-R: alter only check.revalidation-earlier compact checkId | AI-N23 |
| Correct finalL, bad earlier L | acquired-R: alter only check.release-earlier compact checkId | RF-N12 |
| Source task mismatch | change Source.taskId to another canonical UUID; recompute Source and copy its new digest into unchanged-task binding/receipt | AI-N16 |
| Source check mismatch | change Source.checkId only; X.checkId and every A/R/L reference still name A; recompute Source and digest copy | AI-N17 |
| Source lease mismatch | change Source.leaseId only; X.leaseId remains the original; recompute Source and digest copy | AI-N18 |
| Binding digest is not Source copy | keep valid Source, change only X.acquisitionResultDigest to another tagged value and rehash descendants | AI-N20 |
| Issued binding lease differs from C | keep C unchanged; Source and X agree on another lease and valid source digest/copy, A/R/L remain bound | RC-N09 |

| Causality case | Otherwise-valid construction | Precise owner |
| --- | --- | --- |
| G-after-A sequence, acquired R | Swap A with the sole G5 in the complete acquired-R golden, renumber sequence, preserve every timestamp and other field, and rehash the receipt | AI-N10 |
| G-after-A timestamp | Keep every G before A by sequence; in acquired-R set only G5 time to second 2 while A stays at 1, R at 2/3, and L at 4/5. Repeat on acquired-I with R at 2 and I at 3 | CH-N08; both origins are variants |
| Earlier repeated G after A | In acquired-R move G5a immediately after A, then add distinct-ID passed G5b after G5a and before every R/controller. Keep both G times at 0 and rehash | AI-N10; repeated-member variant |
| Earlier bad G time, later valid G | Keep G5a and a distinct-ID G5b before A by sequence; G5a time 2, later G5b time 0, A time 1, R/controller time 3, and L time 4 or later | CH-N08; universal-quantifier variant |
| G/A inversion, acquired I | Swap A with G5 in the complete acquired-I golden; keep R before singleton failed I, all original timestamps, cleanup, and identity bindings | AI-N10 |
| Issued stable-acquired prefix | In a complete matching lease-required issued pair, swap G5/A with valid times, or keep valid sequence and set G5 time after A but before R; run attempted and not-attempted forms independently | AI-N10 or CH-N08, never new origin owners |
| R sequence before A with valid times | acquired-R: move the earlier passed R immediately before A; keep the controlling R after A; set all A/R times to second 1 and evidence to controller time | AI-N11 |
| A sequence before R but R time before A | keep the acquired-R array; A time 2, earlier passed R time 1, controller/evidence time 3, every L time 4 or later | CH-N10 |
| Bad early R, good controller | the first two constructions independently demonstrate that a correctly ordered controlling R cannot erase a bad earlier R | same AI-N11 / CH-N10, non-additive |
| Controlling R time inversion | A time 2, earlier R time 2, controlling R/evidence time 1; all other bounds remain valid | CH-N10, non-additive |
| Sequence-only selection trap | retain greatest-sequence finalL while inverting an earlier/later L timestamp pair; finalL outcome and all references remain valid | CH-N20 |

The known acquired-R G5/A swap has correctly recomputed receiptDigest
`sha256:d906c9e66457617fc23e3d0d7a86654f67ba1f64a3dbc41bd69d3b9afd273c65`.
It MUST reject at AI-N10 during static acceptance, before receipt-digest
acceptance; a correct digest does not rescue G5.sequence>A.sequence.
Positive controls retain both complete acquired-denial goldens and issued
lease-required attempted/not-attempted paths, including repeated passed G
entirely before A and G.observedAt==A.observedAt at whole-second boundaries.
Run each sequence/time negative separately for all five G types and each
stable-acquired origin, with every unrelated predicate and dependent digest
valid. In the repeated sequence inversion, the latest G may satisfy outcome,
time, and controller bounds, but cannot satisfy G<A when an earlier-by-sequence
G is already after A. The separate timestamp variant isolates an earlier bad
G while the latest same-type G satisfies G<=A. finalG never replaces every G.

The four exact erased-success histories in the corpus reject under DP-N10 (A) or DP-N11 (I), with single failed/indeterminate A/I controls accepted. An acquired I variant inserts a passed I after its passed A/R prefix and before the failed I: it also rejects only the I-denial singleton rule. Each G/N/R controller admits passed* followed by one failed/indeterminate controller; all nine checkpoints do not share that rule. Empty mapped type is a structural/presence failure; wrong controller ID, time, or reasons uses DP05, DP07, or DP08 separately.

Positive release variants replace acquired-R's early failed L with indeterminate L while retaining passed finalL. Both histories are accepted with every L bound and pairwise chronological; neither requires an unresolved warning solely for the earlier member. acquired-I's indeterminate finalL requires a warning naming that final L. A warning naming only an earlier L rejects RF-N11. Removing all L rejects RF-N01. F is always present, passed, exact-tuple, sanitized, and terminal.

Negative controls cover missing/multiple Source, missing/forbidden X, invalid Source hash, wrong X/A identity, missing A/R/L compact refs, and forbidden compact placements on G/N/I/P/E/V/F and every non-stable path. These use AI14..AI23, RF12, or the generic shape owner as defined by the ledger; no extra primary is added for the same mismatch on another origin. Unreached denial types and prerequisite observations after the controller reject DP03/DP04.

The acceptance matrix also retains no-lease issued attempted and not-attempted paths; both lease-required issued paths; all ten denial matrix rows; repeated all-passed G; passed-only P before expiry; non-passed P terminality; EF-1 execution terminality; mixed non-passed V histories; exact per-type V coverage; and every outcome/release precedence row. G-to-G, E-to-E, and R-to-R timestamp inversions remain valid where all explicit edges pass. Timestamps never select the final member.

### Scope and operation regression matrix

Option B does not change the scope projection or the operation carrier. Re-run each retained case against a receipt with the repaired acquisition bindings and refreshed dependent digests.

| Independent surface | Accepted control | Rejected or fail-closed mutation |
| --- | --- | --- |
| Apath / Qpath | every Ptrans target is directly authorized and non-prohibited before acceptance; receipt paths separately satisfy their scope predicates | unauthorized/prohibited transition target even with Oplan empty; wrong Domain authority; canonical but out-of-scope earlier receipt path despite a good final member |
| Acap / Qcap | RequiredPlanCaps and Oexec are subsets of Acap and disjoint from Qcap | unauthorized/prohibited create/modify/delete or required git-stage; neither capability family substitutes for the other, and a permitted final operation cannot hide earlier disallowed effects |
| Oplan(B,F) | simultaneous transitions produce one F; conservative ordinary effects satisfy capability closure | transition requiring a forbidden capability; after-state invented independently of B; administrative operation treated as ordinary |
| Carrier presence | exactly iff issued, writing, attempted; complete zero-effect case is [] | missing carrier on each attempted outcome; carrier on no-lease/non-writing, denial, or not-attempted path |
| Carrier shape/order | closed {path, operations}, non-empty canonical operations, canonical unique paths | extra key, empty/unknown operation, duplicate path/operation, unsorted path/operation |
| EvidencePaths | every carrier path belongs to changedPaths | carrier path missing from changedPaths |
| OexecByPath / Oexec | actual per-path unions and full union retain every listed operation | drop an earlier operation or reconstruct only final records |
| Verification / lifecycle | contained effects plus all passed referenced V and consistent outcomes | out-of-scope effect with passed verification or succeeded lifecycle; a later passed V cannot erase an earlier non-passed V |

Failed/indeterminate verification retains actual out-of-scope evidence; it does not rewrite or suppress the carrier. Oplan is a conservative planned effect set, not a claim that all planned operations actually happened. Index authority is TA03-owned; unsupported ref/HEAD/submodule transition shapes and runtime administrative-path checks retain their separate owners. These are static synthetic constructions and planned conformance requirements, not runtime enforcement or permission to execute effects.


### Historical Option-B construction verification

At the prior Option-B audit freeze, in-memory synthetic construction checks exercised 45 denial/state/identity cases, the retained 43 scope/OC/OE cases, two issued identity cases, and all 20 independent temporal reversal assignments: 110 checks with the intended dispositions. The checks are disposable document-construction verification, not a repository validator or executable Schema/model test suite. The 31 framed hash cases and 13 completed-object byte cases were independently replayed by Node and PowerShell/.NET. Trusted issuance, runtime observation, acquisition/release truth, and scope attribution remain outside these checks.

Current owner numbers are derived from the row inventories, not inherited aggregate targets. All superseded current representations and count summaries are removed. Historical opening review records and explicitly historical PG-1 attestations retain their original values and meaning.

### Current invariant counts

```text
Schema resources = 11
dispatchable kinds = 7
baseline dimensions = 9
permitted-transition branches = 4
required-postcondition branches = 11
check types = 14
denial checkpoints = 9
ExecutionReceipt spec fields = 17
ExecutionReceipt field-table rows = 16
array-ordering matrix rows = 54
mandatory SG-001 rows = 25
D5 Cartesian negatives = 12
active-operation regressions = 21
administrative-lock regressions = 21
check-outcome conditional branches = 2
non-execution check-outcome values = 3
execution check-outcome values = 4
distinct check-outcome tokens = 5
timestamp paths = 9
timestamp lexical/calendar positives = 10
timestamp lexical/calendar negatives = 24
normative displayed chronology relations = 31
primitive additive chronology relations = 20
chronology derived relations = 11
chronology positive primary classes = 20
chronology reversal primary classes = 20
chronology primary classes = 40
focused pre-action positives = 8
focused pre-action negatives = 37
final-E exact-match positives = 4
final-E multi-E positives = 4
final-E total positives = 8
final-E mismatch-matrix negatives = 12
final-E total negatives = 22
focused post-execution-verification positives = 10
focused post-execution-verification negatives = 20
required-postcondition binding positives = 5
required-postcondition binding negatives = 5
lease-acquisition-chain positives = 23
lease-acquisition-chain negatives = 23
cumulative-denial-prerequisite positives = 13
cumulative-denial-prerequisite negatives = 13
lease-release/finalization positives = 14
lease-release/finalization negatives = 14
PB/AI/DP/RF numbered primary definitions = 110
acquisition-plus-release focused primary classes = 74
five focused-family primary classes = 150
changed-path scope positives = 5
changed-path scope dedicated negatives = 6
changed-path scope D5 cross-reference = 1 existing family, not additive
ordinary-capability-closure positives = 3
ordinary-capability-closure negatives = 8
ordinary-capability-closure primary classes = 11
operation-evidence positives = 10
operation-evidence negatives = 11
operation-evidence primary classes = 21
D6 valid receipt-level combinations = 13
D6 invalid receipt-level combinations = 7
receipt/contract equalities = 8
receipt/contract binding positives = 9
receipt/contract binding negatives = 9
receipt/contract binding primary classes = 18
expanded retained-family aggregate including receipt/contract binding = 168
transition-authorization positive independent owners = 3
transition-authorization negative independent owners = 3
transition-authorization independent owner classes = 6
expanded affected-family aggregate including receipt/contract binding and TA = 174
transition-path negative variants = 12
transition-path positive branch controls = 4
unsupported former-transition variants = 3
inspect-only supported-transition negatives = 4
digest-bearing paths = 12
digest computations = 10
digest exact-copy paths = 2
numeric fields = 6
host-resource-exclusivity positives = 5
host-resource-exclusivity negatives = 13
```


Current continuous ranges are PB-P/N01..05, AI-P/N01..23, DP-P/N01..13, RF-P/N01..14, CH-P/N01..20, RC-P/N01..09, and TA-P/N01..03. Each row in the independent ledger has exactly one positive and one negative owner. Mandatory variants are non-additive. Scope 5/6, OC 3/8, OE 10/11 and other retained inventories are coverage-case counts outside this independently rebuilt aggregate.

### Retained historical protected-region records

Domain B performs only CRLF-to-LF replacement. The previous values W = 35334
bytes / 271 CRLF /
`a4f80b731f4b6c9ee8ee4ec621350f85dc24ff694c2c4b47fa10902a8ed9b88d`
and B = 35063 bytes / 271 LF /
`75c200b287b770c418218ea34ed98a800a4a229ea536109ff0f764f449a3e2a7`
are historical and superseded. The intermediate RS-1/LB-2 pre-AP-1 values are
also historical and superseded:

```text
PG-1 W = 37326 bytes / 295 CRLF / e6cd8deb426a509a2ade0c4df48f2bf7c6e148afed02d3ce697faeb910318251
PG-1 B = 37031 bytes / 295 LF / 8d8b0aee8b93559690d530402761347fba0aa222962ef11b99d42caf1262c432
```



### Complete digest-profile catalog

The final field graph has 12 digest-bearing paths, 10 independent computations, and 2 exact-copy paths. Counts follow the twelve rows below; consumers cannot select another profile. Source is non-public and contributes no resource kind.

```text
separator(profile) = ASCII("contextctl.dev") || NUL || ASCII("v1alpha1-r1") || NUL || ASCII(profile identifier) || NUL
taggedDigest = "sha256:" || lowercaseHex(SHA256(separator(profile) || payloadBytes))
RAW: payloadBytes = exact retained original bytes
JCS: payloadBytes = UTF8(JCS(exact closed projection))
```

Raw bytes are never normalized, trimmed, filtered, transcoded, or converted between line endings. JCS preserves validated strings and array order. Every computation is framed, including both raw profiles. Table pipe escapes are Markdown syntax only and never input bytes.

| Exact field path | Exact profile and payload kind | Exact protected value and included fields | Exact exclusions | Byte construction, replay source, and lifecycle phase |
| --- | --- | --- | --- | --- |
| `trackedEntry.contentDigest` | `profile.digest.worktree-content-v1`; raw | Exact D4 regular-file bytes or symlink-target bytes | Path, mode, Git object ID, filters, decoded text, directories, gitlinks | `separator(profile) \|\| rawBytes`; stable Phase 3 observation and Phase 4 verification |
| `TaskContract.spec.issuer.derivationDigest` | `profile.digest.contract-derivation-v1`; JCS | Complete `TaskContract` resource, including identity, every source digest, target, scope, baseline, transitions, postconditions, lease fields, issuance checkpoint, and freshness | Only `issuer.derivationDigest` | `separator(profile) \|\| UTF8(JCS(projection))`; validated representation and issuance/provenance replay in Phase 4 |
| `TaskContract.spec.digests.policyDigest` | `profile.digest.policy-selection-v1`; JCS | Closed `{project, domains, worktreeRole, routingPolicy}` containing the complete selected Project, complete canonically ordered resolved Domain resource set, selected WorktreeRole, and selected RoutingPolicy | HostOverlay and all runtime state | Same framed JCS construction; authoritative configuration snapshot used for issuance and Phase 4 verification |
| `TaskContract.spec.digests.configurationDigest` | `profile.digest.configuration-snapshot-v1`; JCS | Closed `{governanceBundle, hostOverlay}` containing the complete GovernanceBundle used for resolution and complete selected HostOverlay | Secrets, leases, contracts, receipts | Same framed JCS construction; validated configuration source used for issuance and verification |
| `TaskContract.spec.digests.taskIntentDigest` | `profile.digest.task-intent-bytes-v1`; raw | Exact original strict UTF-8 task-intent bytes | BOM, normalization, trimming, line-ending conversion, JCS, semantic interpretation | `separator(profile) \|\| originalBytes`; retained original intent bytes at issuance and verification |
| `TaskContract.spec.issuanceCheckpoint.stateDigest` | `profile.digest.issuance-state-v1`; JCS | Closed `{repositoryIdentity, target, expectedBaseline, observedAt}` using the contract values and `issuanceCheckpoint.observedAt` | `stateDigest` itself and every other contract field | Same framed JCS construction; issuance-checkpoint representation and Phase 4 replay |
| `ExecutionReceipt.spec.origin[type=issued-contract].contractDigest` | `profile.digest.task-contract-v1`; JCS | Complete `TaskContract` resource including `issuer.derivationDigest` | Nothing | Same framed JCS construction; referenced trusted contract bytes during receipt binding and verification |
| `ExecutionReceipt.spec.origin[type=pre-contract-denial].preContractEvidence.evidenceDigest` | `profile.digest.pre-contract-evidence-v1`; JCS | Closed {taskId, denialCheckpoint, preContractEvidence}, with only evidenceDigest removed from the last member; plus complete receipt-level acquisitionBinding iff acquired | Only evidenceDigest from evidence; acquisitionBinding is absent on every non-acquired branch | Source validation and binding copy precede acquired projection; all other evidence fields are included |
| `LeaseAcquisitionResultIdentity.acquisitionResultDigest` | `profile.digest.lease-acquisition-identity-v1`; JCS | Closed {taskId, acquisitionBinding:{checkId,leaseId}}, bijectively formed from all three non-digest Source members | Source acquisitionResultDigest | One computation on either stable-acquired origin; Phase 3 produces evidence, Phase 4 validates provenance and ownership |
| `ExecutionReceipt.spec.acquisitionBinding.acquisitionResultDigest` | `profile.digest.lease-acquisition-identity-v1`; exact copy | Exactly the validated associated Source.acquisitionResultDigest | No second computation or receipt-derived source | Exact tagged-string copy after task/check/lease equality; both stable-acquired origins require it |
| `ExecutionReceipt.spec.receiptDigest` | `profile.digest.execution-receipt-v1`; JCS | Complete `ExecutionReceipt` resource | Only `spec.receiptDigest`; `ReceiptDeliveryResult` occurs after finalization and is outside the receipt | Same framed JCS construction; validated receipt representation at Phase 4 finalization and replay |
| `ReceiptDeliveryResult.receiptDigest` | `profile.digest.execution-receipt-v1`; exact copy, no additional computation | The referenced finalized receipt's already-computed `ExecutionReceipt.spec.receiptDigest` | The delivery result is never included in or rehashed as the receipt | Exact tagged-string equality with the referenced receipt and receipt ID after finalization; the same execution-receipt profile remains the sole binding |

The graph is acyclic. Policy/configuration/raw intent/issuance-state → contract derivation → complete contract → issued contractDigest. Independently, Source non-digest identity → Source digest → exact acquisitionBinding copy → acquired-denial evidenceDigest when applicable → receiptDigest → optional delivery copy. The source projection has no receipt-digest input. The non-acquired evidence projection omits acquisitionBinding. Worktree content is an independent raw leaf. Static acceptance of all applicable bindings precedes receipt hashing; a hash proves integrity only, never event truth, provenance, ownership, or authority.


### Option-B exact golden mirror

The design document contains fully expanded acquired-R and acquired-I projections and completions, their conditional evidence projections, the full Source and binding, four single-state controls, and four explicit erased-success negatives. These tables mirror its exact values. Single failed/indeterminate A and I controls are accepted. The four passed-prefix state-creation specimens reject DP10 or DP11 before digest acceptance, even though their test hashes are mathematically correct.

#### Recalculated golden results

| Vector / profile | Payload bytes | Complete object bytes where applicable | Tagged digest |
| --- | ---: | ---: | --- |
| policy-selection | 2572 | — | `sha256:632908742df166217cf19fc74febda89e2f8ea816d71ec69f65a11a1a4831743` |
| configuration-snapshot | 3717 | — | `sha256:d673b61894f1377ae4e7b7a563db05204ec96cc95bfa9ffb08ccc191e3154f86` |
| issuance-state | 642 | — | `sha256:4b9cf13b1accd0e3c29754feedb601c5a7b43619842ad76cbf118a56ae4a2702` |
| contract-derivation | 1882 | — | `sha256:9ced52eaa97d549c51caea566cc4681016f18614b68d1db0bc7a2748113f9a25` |
| task-contract | 1975 | — | `sha256:238c3af3ceab3eafc70d660b6e3d5cef97c3741d48b76c49e9e998a26d8afe30` |
| execution-receipt | 3337 | 3427 | `sha256:d3cc668ea95fa385392f04b4e5580cd2fdc810835ae7fd1ab285c102777402b0` |
| task-intent-bytes-v1 (raw) | 56 | — | `sha256:f4dda8a653d84b21ae740b502386262ebd525e7086270c5eba7af31eda6929c8` |
| worktree-content-v1 (empty raw) | 0 | — | `sha256:75a1e5502a349f7d22cbb583985b3045b6d5fd084f9f053cf3379bbbfe3781f9` |
| lease-acquisition-identity-v1 Source | 157 | 234 | `sha256:6aec9485391fbba3fd7a35640e21dd45dc2da0228e87db83fe935ba99a100e7f` |
| acquired-R evidence | 507 | — | `sha256:3f2a27da5bfdf587209700191c430aa1900cdbe4e428f82abb7d289efbee0429` |
| acquired-R receipt | 3743 | 3833 | `sha256:d8c44f4ae79b8402ffb0aa36cd8e9fff2d610df09e0c6f0a7a88c9ca4bfaec8f` |
| acquired-I evidence | 483 | — | `sha256:93c0c3a28a9dbfdc05b29183fde51f653ad3c7cab65eb4c7b571dd3dc94bac4a` |
| acquired-I receipt | 3542 | 3632 | `sha256:d151aa6ce1c13f4e42ce3b47a058df488bcb072491506de936d3ad7873f74cff` |
| single-failed-A evidence | 275 | — | `sha256:a6e3d300a1dd1ef61aa7a203441f971c6229dd306157ac8aafc20268ac7ad42c` |
| single-failed-A receipt | 2403 | 2493 | `sha256:04e565109819e271ddafc60bf50aa7a035c0a70cee005af67a6f84dacaf6c69e` |
| single-indeterminate-A evidence | 275 | — | `sha256:a6e3d300a1dd1ef61aa7a203441f971c6229dd306157ac8aafc20268ac7ad42c` |
| single-indeterminate-A receipt | 2549 | 2639 | `sha256:55e493aa0c23428037602c86fbc4b8dab52a7e2cf28fd5b0ff6d69d4cb5f1706` |
| single-failed-I evidence | 275 | — | `sha256:e53415c5bad5345082073b225dba4ddb01a895968f03815e9a5fcd0b80ebc839` |
| single-failed-I receipt | 2610 | 2700 | `sha256:b887eb26f92bd9bacbe60be84295cac4b16abac138b94dae9490c835329da9aa` |
| single-indeterminate-I evidence | 275 | — | `sha256:e53415c5bad5345082073b225dba4ddb01a895968f03815e9a5fcd0b80ebc839` |
| single-indeterminate-I receipt | 2617 | 2707 | `sha256:6133e6152bf48b945916ec67d348ccc8baa3435846e1c2968b11d0e83e9e5d47` |
| passed-A-then-failed-A evidence | 275 | — | `sha256:a6e3d300a1dd1ef61aa7a203441f971c6229dd306157ac8aafc20268ac7ad42c` |
| passed-A-then-failed-A receipt | 2591 | 2681 | `sha256:d3d5e1727b67bb896f6863f299e9734875c1340a1e514f5b5274ee25cf3bbbff` |
| passed-A-then-indeterminate-A evidence | 275 | — | `sha256:a6e3d300a1dd1ef61aa7a203441f971c6229dd306157ac8aafc20268ac7ad42c` |
| passed-A-then-indeterminate-A receipt | 2737 | 2827 | `sha256:2fde9652c4f03149a06d42a8c2128b6f33193bf198c26bf3524473a90f54b679` |
| passed-I-then-failed-I evidence | 275 | — | `sha256:e53415c5bad5345082073b225dba4ddb01a895968f03815e9a5fcd0b80ebc839` |
| passed-I-then-failed-I receipt | 2798 | 2888 | `sha256:d57f7c7fb94a295c2430f12e8a4bf899a779c5e45584e8c811555a114d882f74` |
| passed-I-then-indeterminate-I evidence | 275 | — | `sha256:e53415c5bad5345082073b225dba4ddb01a895968f03815e9a5fcd0b80ebc839` |
| passed-I-then-indeterminate-I receipt | 2805 | 2895 | `sha256:bb97681c6ada4a5db3ddbfa38fcabe28f674ab358fe1e6752647c0b5ff7cb6f4` |

The unchanged policy, configuration, raw intent/content, issuance state, derivation, complete contract, and no-lease receipt/delivery goldens are retained only after recomputation from their exact payloads. Each changed profile separator, Source projection, binding copy, evidence projection, complete denial receipt, and byte count is recomputed. The source projection has no digest member; the receipt projection excludes only spec.receiptDigest. Four invalid histories have correct mathematical test hashes but fail static acceptance before a validator may accept those hashes.

Mutating an included field, excluding the wrong member, inserting a self-digest, changing any separator byte or profile, or changing any raw byte produces a different result. Closed-shape extras and invalid arrays reject before projection. Missing/different Source cannot be substituted by self-consistent receipt claims. A delivery result copies the exact referenced finalized receipt digest and never creates a second hash. All results establish integrity only, not event truth, ownership, provenance, release, or authority.


### Current Option-B protected-region attestation

PG-1 starts at the unique complete heading line `### Complete digest-profile catalog` in the design and ends before the unique complete heading line `## 11. Complete array-ordering matrix`. W is the exact raw UTF-8 on-disk slice, including every intervening byte. B replaces only CRLF with LF. This attestation lies outside the protected slice and cannot self-reference. No smaller receipt-only slice substitutes for PG-1.

```text
PG-1 W bytes = 75920
PG-1 W CRLF separators = 343
PG-1 W lone LF separators = 0
PG-1 W SHA-256 = d45cdded71ff568f440cdb657a6e83a787ad4dfa2e7103c8c1ade15fdb90cae2
PG-1 B bytes = 75577
PG-1 B LF separators = 343
PG-1 B SHA-256 = 8df69ec3d5c4298b400c2781705c9a80497dab3d03ca343fa6333521b9a37a8d
protected distinct timestamp values = 8
protected timestamp occurrences = 192
protected structured-remote occurrences = 7
protected tagged-digest occurrences = 76
protected distinct tagged-digest values = 25
protected execution-receipt tagged-value occurrences = 23
```

Counts cover all prose, tables, and JSON fences in that same broad slice. Each canonical whole-second UTC token, each complete closed structured-remote JSON object, and each exact sha256: plus 64 lower-case hex token is counted per textual occurrence; distinct counts deduplicate exact strings only. The execution-receipt total counts the eleven distinct receipt hashes: ten denial specimens each appear in its completed record and results row, and the no-lease hash appears in completion, delivery copy, and results row. Projections contain no receiptDigest member. The four rejected histories still count as exact byte specimens, without implying acceptance.

| Literal profile identifier | Occurrences in PG-1 |
| --- | ---: |
| `profile.digest.worktree-content-v1` | 3 |
| `profile.digest.policy-selection-v1` | 3 |
| `profile.digest.configuration-snapshot-v1` | 3 |
| `profile.digest.task-intent-bytes-v1` | 3 |
| `profile.digest.issuance-state-v1` | 3 |
| `profile.digest.contract-derivation-v1` | 3 |
| `profile.digest.task-contract-v1` | 3 |
| `profile.digest.pre-contract-evidence-v1` | 2 |
| `profile.digest.lease-acquisition-identity-v1` | 3 |
| `profile.digest.execution-receipt-v1` | 4 |

Node and PowerShell/.NET independently reproduce canonical payloads and SHA-256 values for all retained and changed goldens, including raw vectors; complete-object byte counts are also independently checked. PG-1 W/B bytes and SHA-256 were recomputed separately from the final region. No Schema/model test suite or runtime producer is implemented.

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
