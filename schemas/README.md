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

LB-2 retains one closed receipt root containing exactly `checkId`, `leaseId`,
and `acquisitionResultDigest`, plus compact
`leaseAcquisitionRef: {checkId}` on A, R, and every L. AP-1 separately defines
the non-public closed `LeaseAcquisitionResultIdentity` source with exactly
`taskId`, `checkId`, `leaseId`, and `acquisitionResultDigest`. It is not an
eighth public kind, portable governance, a TaskContract or receipt field, a
second full object embedded in the receipt, or runtime implementation.

The source's `acquisitionResultDigest` is the sole independent
`profile.digest.issued-lease-acquisition-v1` computation over closed
`{taskId, leaseAcquisitionEvidence:{checkId,leaseId}}`, bijectively projected
from the three non-digest source members. The receipt-root digest is an exact
copy of that validated source value. A lease-required issued receipt requires
one associated source and exact receipt/source `taskId`, source/root/A
`checkId`, source/root/contract `leaseId`, source-to-root digest copy, and
A/R/every-L compact-reference bindings. I and every other check type forbid the
compact reference. No-lease, denial, and indeterminate-acquisition paths forbid
the AP-1 source/root/reference chain; acquired denial retains its unchanged
origin/reference/profile/projection/digest/example chain.

Phase 1 defines source shape, digest profile, equality/copy relationships, and
static conformance. Phase 3 produces the acquisition result and stable source
identity. Phase 4 validates trusted provenance, ownership, and evidence truth
and supplies that source during issued-receipt validation/finalization. Static
binding does not prove acquisition, authenticity, current ownership, or
release.

Both complete public artifacts, the associated source when required, and the
TaskContract derivation prerequisites validate before their cataloged digests
are accepted. All eight duplicated-claim equalities, AP-1 source-profile and
exact-copy chain, root/A/R/every-L references, source/root/contract lease-ID
equality, chronology, phase-dependent check outcomes, final-P/E/V selection and
binding, changed-path scope conformance, and outcome/release consistency
validate before receipt-digest acceptance. Delivery binding and chronology
validate only after receipt finalization. No TaskContract acquisition-digest
field, new TaskContract or ExecutionReceipt digest profile, or
`TaskContract.spec.taskContractDigest` field is introduced. A mismatch is
invalid rather than normalized, repaired, reclassified, or matched to another
contract.

The shared `canonicalUtcTimestamp` accepts only whole-second UTC strings
matching:

```text
^[0-9]{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])T(?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]Z$
```

Future Schema uses `type: string`, that exact pattern, and asserted
`format: date-time`. Phase 1 additionally enforces years `0001` through
`9999`, Gregorian date and leap-year validity, all 24 primitive chronology
relations, and all 30 displayed consequences. Lower-case delimiters, offsets,
fractions, leap seconds,
`24:00:00`, whitespace, alternate spellings, and repair are forbidden. The
profile applies to the three TaskContract timestamps, receipt `startedAt`,
`finishedAt`, `sanitization.completedAt`, every `checks[].observedAt`,
the pre-contract origin's `preContractEvidence.observedAt`, and
`ReceiptDeliveryResult.attemptedAt`: exactly nine paths.

RS-1 defines receipt `startedAt` as the lower time boundary of the complete
lifecycle evidence serialized in either origin. It is no later than every
check, no later than denial `preContractEvidence`, and, for an issued receipt,
no later than `freshness.issuedAt`. For referenced contract C, lease-required
issuance is bracketed by `R.observedAt <= C.issuanceCheckpoint.observedAt <=
C.freshness.issuedAt <= I.observedAt`; no-lease issuance is bracketed by
`N.observedAt <= C.issuanceCheckpoint.observedAt <= C.freshness.issuedAt <=
I.observedAt`. Equality is allowed but never required. CH-P15/CH-N15 own the
primitive R-to-checkpoint comparison and CH-P16/CH-N16 own the primitive
N-to-checkpoint comparison. Direct R-to-issuedAt and N-to-issuedAt relations
are derived through the existing checkpoint-to-issuedAt primitive. The Review-12
lease and no-lease counterexamples keep both old direct relations and the
checkpoint-to-issuedAt relation valid while placing the checkpoint before R or
N; the former direct-only rule accepted them and the transferred CH-N15/CH-N16
relations reject them. The strict
sequence chains remain `G < A < R < I < P` and `G < N < I < P`; timestamps
do not duplicate sequence edges.

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
universal. N is a mandatory planned non-additive forbidden-type variant, so the
postcondition-binding family remains 15/20. The design and test plan retain the
existing 5/19 receipt-binding, 10/24 timestamp lexical, 8/22 final-E, 10/20
verification, 5/6 scope, and 15/61 remote families, and record rebuilt 6/28
acquisition/issuance, 9/6 cumulative-denial, 11/14 release/finalization, and
24/24 primitive-chronology families under intended-owner and non-additive-
variant rules.

For post-sanitization receipt-finalization evidence, textual identity fields
are safe-by-construction only when their complete semantic value domain is
closed by the protocol. Lexical validity alone is insufficient. The exact
reserved tuple above rejects producer alternatives that merely satisfy generic
identifier grammar, including path-like, host/operator-derived, secret-like, or
diagnostic values. This protects against arbitrary post-sanitization text in F;
it does not claim information-theoretic covert-channel elimination.

These repairs retain the existing universal pipeline dependency order: strict
bytes/tokens; timestamp and remote lexemes; Schema structure; local Phase 1
invariants; array and remote order; validated representation; digest
projection/computation; complete TaskContract digest; receipt/contract
equality plus AP-1 source-profile/exact-copy and LB-2 root/reference/lease binding; the current 24
primitive chronology checks and 30 displayed
consequences; final P/E/V, diagnostic finalG, per-type V, and finalL selection;
every actual G and every attempted P passed; failed/indeterminate P same-lifecycle
terminality with no later P/E/V and not-attempted/not-performed outcomes; exact
applicable A/R/N/I; cumulative denial all-member
prerequisite/controller ordering and stop-boundary membership; R/N-to-checkpoint, checkpoint-to-issuedAt, derived R/N-to-issuedAt,
issuedAt-to-I, P/E/V,
acquisition/release, non-F/sanitization, sanitization/F,
and F/finish ordering; EF-1 execution terminality and final E/V/L binding; mandatory `sanitization.applied == true`; outcome, scope, terminal F, warning, and L-empty
consistency; receipt digest; then delivery binding/chronology. The byte-
protected twelve-step design block remains unchanged in content and order; its
historical count label does not replace the current normative inventory.
`schema-contracts` specifies the structural/static contract and vectors;
future `model-implementation` owns executable codec, projection, hashing, and
cross-artifact conformance; Phase 3 owns live remote and host facts and produces
the acquisition result/source identity; and Phase 4 owns trusted source/issuer
provenance, lease ownership, authority, time, freshness, and evidence truth.

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
digest graph remains 14 field paths, 11 computations, and 3 exact copies.

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

`permittedTransitions` has exactly seven branches: `ref-state`, `head-state`,
`index-entry`, `tracked-entry`, `untracked-path`, `ignored-path`, and
`submodule-entry`. The required-postcondition union remains at eleven branches.
Its optional `active-operations` and `administrative-locks` branches are both
none-only and are not newly mandatory. Simultaneous composition applies the
seven transitions while reconstructing one final nine-dimension composite in
which both active operations and administrative locks remain none.

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
five path-keyed transition branches, receipt `changedPaths`, and
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
verification requires every per-type final V passed. Every E follows final P
and every V follows every E by strict sequence and non-decreasing timestamp.
EF-1 introduces no E-to-E timestamp relation.

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

A lease-required issued receipt has singleton passed A and R, no N, and
`every G < A < R < I < every P`. A no-lease issued receipt has no A or R,
singleton passed N, no lease identity, and
`every G < N < I < every P`. Attempted receipts retain
`final P < every E < every V`; non-attempted receipts keep E/V empty, may omit
P, and order every present P after I. Missing, duplicate, non-passed, or wrong-
path A/R/N/I and any G, A, R/N, or I sequence inversion reject.

DP-1 requires a pre-contract denial to retain every stage completed before its
controlling checkpoint, order every actual prerequisite-stage observation
before the greatest-sequence failed/indeterminate controller, stop all ordinary
lifecycle-stage evidence at that controller, and then record only applicable
cleanup, sanitization, and F. Unreached future stages remain forbidden
everywhere in the receipt. Every denial requires
`preContractEvidence.controllerCheckId`, which resolves to exactly one
same-receipt check. That check's type is the exact identity mapping from each of
the nine `denialCheckpoint` tokens to its same-named `checkType`; it is the
unique greatest-sequence member of that type; its outcome is failed or
indeterminate; every earlier same-type member is passed; its `observedAt` and
canonical `reasonCodes` exactly equal the evidence values; and it occupies the
applicable cumulative-matrix position. The referenced controller is therefore
both the first non-passed and final same-type observation. Missing/unknown IDs,
earlier same-type or wrong-type references, non-greatest selection, passed
outcome, an earlier non-passed same-type member, time/reason mismatch, and
reorder, extra, or missing reason variants reject.

Let `O` be exactly the twelve ordinary lifecycle-stage check types:
`intent-validation`, `project-domain-resolution`, `role-routing`,
`host-binding`, `initial-preflight`, `pre-issuance-revalidation`,
`lease-acquisition`, `post-acquisition-revalidation`,
`contract-issuance`, P, E, and V. L and F are outside `O`. For row `r`,
every actual member whose type is in `Prereq(r)` is passed and has sequence
less than the controller; this quantifies every member rather than only an
existence, greatest, final, or selected member. Only `Prereq(r)` and the
controller type may occur from `O`; every unreached ordinary type is empty;
and no member of `O` occurs after the controller. Only required acquired-path
L and universal F may follow: `controller < every L < F`; otherwise L is
empty and only F follows. These are sequence predicates only and add no
timestamp edge.

This first-failure rule applies to all nine controller types. It rejects
`failed -> failed`, `failed -> indeterminate`, `indeterminate -> failed`,
`indeterminate -> indeterminate`, `failed -> passed`, and `indeterminate
-> passed`. It permits `passed -> failed`, `passed -> indeterminate`,
`passed -> passed -> failed`, and `passed -> passed -> indeterminate` when
the rest of the cumulative matrix holds. Recovery requires a new task, attempt,
and lifecycle; no retry epoch is added. Issued-path singleton A/R/N/I rules are
unchanged and remain distinct from denial-controller repeats.

Lifecycle chronology counts temporal ordering between distinct lifecycle
events. The exact identity equality
`preContractEvidence.observedAt == controller.observedAt` is instead DP
controller binding: equality-positive coverage is DP-owned and a mismatch is
DP-N04-owned. It adds no displayed, primitive/additive, or
derived/non-additive chronology relation, consistently with receipt/contract
equalities, digest copies, acquisition lease-ID/digest bindings, and
`controllerCheckId` identity.

`sanitizedSummary` is only a sanitized explanatory derivative: it is
non-authoritative, does not identify the controller, and need not equal
optional check prose. An acquired denial additionally requires the closed
`acquisitionEvidenceRef {checkId, leaseId, acquisitionResultDigest}`; every
non-acquired state forbids it. The reference selects the exact same-receipt
singleton passed A required by the matrix, and its lease ID and digest equal
the acquired origin exactly. It cannot reference another A, failed A, non-A,
lease, digest, or receipt and contains no issued-contract field. The exact
cumulative prefixes and stop boundaries are:

| Checkpoint | `Prereq(r)`: every actual member passed and before controller | Controller | Unreached `O` types empty everywhere | Acquisition binding | Only post-controller checks |
| --- | --- | --- | --- | --- | --- |
| intent | empty | greatest intent, failed/indeterminate | project/domain, routing, host, preflight, N, A, R, I, P, E, V | `not-required` or `not-attempted`; no acquired reference | F only; L empty |
| project/domain | intent | greatest project/domain, failed/indeterminate | routing, host, preflight, N, A, R, I, P, E, V | `not-required` or `not-attempted`; no acquired reference | F only; L empty |
| role routing | intent, project/domain | greatest routing, failed/indeterminate | host, preflight, N, A, R, I, P, E, V | `not-required` or `not-attempted`; no acquired reference | F only; L empty |
| host binding | intent, project/domain, routing | greatest host, failed/indeterminate | preflight, N, A, R, I, P, E, V | `not-required` or `not-attempted`; no acquired reference | F only; L empty |
| initial preflight | intent, project/domain, routing, host | greatest preflight, failed/indeterminate | N, A, R, I, P, E, V | `not-required` or `not-attempted`; no acquired reference | F only; L empty |
| N pre-issuance | all five G types | greatest N, failed/indeterminate | A, R, I, P, E, V | exactly `not-required`; no lease identity or acquired reference | F only; L empty |
| lease acquisition | all five G types | greatest A, failed/indeterminate | N, R, I, P, E, V | `not-acquired` or `indeterminate`; no stable identity or acquired reference | F only; L empty |
| acquired R | all five G types plus singleton passed referenced A | greatest R, failed/indeterminate | N, I, P, E, V | exactly `acquired`; exact A/lease/digest binding | one or more L, then F; `controller < every L < F` |
| contract issuance | no-lease: all five G plus singleton passed N; acquired: all five G plus singleton passed A/R | greatest I, failed/indeterminate | no-lease: A, R, P, E, V; acquired: N, P, E, V | no-lease: `not-required`, no reference; acquired: exact A/lease/digest reference | no-lease: F only, L empty; acquired: one or more L, then F |

Every row also requires the exact structured controller binding,
`changedPaths: []`, and one passed terminal F. The N row cannot be represented
by R. Its earlier passed N observations may exist only before the controller;
the controller-selected greatest N is failed/indeterminate and no later pass
preserves that denial. The acquired-R row requires the exact acquired
reference/origin/A binding, no I/P/E/V, at least one post-controller L, exact
final-L top-level mapping and warning, sanitization, and F. The first five rows
record only their exact completed G prefix and controller-selected G failure;
a passed prerequisite re-observation after any controller rejects.

Every serialized receipt requires `sanitization.applied: true`. True means the
selected sanitizer or evaluation completed; it does not mean a redaction
occurred, so `redactionCount: 0` is valid. False is a well-formed Boolean but
invalidates the receipt before passed terminal F, receipt-digest acceptance, or
delivery binding. The wire member remains Boolean and no new field or branch is
introduced.

Let L be all lease-release checks and F all receipt-finalization checks. Every
serialized receipt has exactly one passed terminal greatest-sequence F. F is a
closed record with only `sequence`, `checkId`, `checkType`, `outcome`,
`observedAt`, `profileId`, and `reasonCodes`; it forbids both summary
fields, `postconditionRef`, `leaseAcquisitionRef`, and every other
free-form/payload/unknown member.
F has exactly `checkId: check.receipt-finalization`,
`profileId: profile.validation.v1`, `reasonCodes: []`, and passed outcome.
This is an F-implies-exact-tuple primitive. Exactly one mandatory F plus global
check-ID uniqueness makes non-F use of the reserved ID a derived generic
duplicate-ID rejection; it is not a separate RF primitive.
A producer-selected regex-valid alternative, including
`check.c-users-alice.secrets.api-key-abcd1234`,
`profile.synthetic.secret.sk-live-abcdef123456`, or
`reason.synthetic.secret.token-abcdef123456`, is invalid. Every non-F check
precedes F by sequence and is no later than sanitization; every
denial's `preContractEvidence` is no later than sanitization; sanitization is no
later than F; and F is no later than `finishedAt`. F is the finalization
completion gate after sanitization, not proof of digest insertion, delivery,
lifecycle success, or release success.

Release is required for a lease-required issued receipt and an acquired
denial. Such a path has at least one L, every applicable pre-release/Dpre check
before every L, and top-level release outcome mapped exactly from finalL.
Failed or indeterminate finalL requires a warning bound exactly to finalL.
On a lease-required issued receipt, every L—not only finalL—has a compact
reference whose `checkId` equals the issued root, source identity, and singleton A. The
singleton R carries the same reference. One bad earlier L remains invalid even
when finalL is correctly bound. An acquired denial forbids the AP-1 source, issued root, and compact
references and retains only its unchanged origin/evidence binding.
Acquired denials also require `preContractEvidence <= every L`; every L is a
non-F member and therefore no later than sanitization. No-release paths keep L
empty but retain sanitization and passed F, including indeterminate acquisition
with no stable identity and its required warning.

The six complete sequence paths remain lease-required attempted
`G/A/R/I/P/E/V/L/F`; lease-required non-attempted `G/A/R/I/[P]/L/F`; no-lease
attempted `G/N/I/P/E/V/F`; no-lease non-attempted `G/N/I/[P]/F`; acquired
denial `Dpre/L/F`; and other denial `non-F/F`. The normative chronology
displays 30 relations: 24 primitive/additive and six derived/non-additive
(sanitization/finish, start/finish, denial-evidence/F, non-F/F, R/issuedAt,
and N/issuedAt). CH15/16 retain their 24/24 IDs but their primitive ownership
moves to R/checkpoint and N/checkpoint; the direct R/N-to-issuedAt relations are
derived through checkpoint/issuedAt. Each primitive owns one planned CH
positive and one planned reversal; equality and member variants are non-
additive.

The focused inventories remain pre-action 8/37, final-E 8/22,
post-execution verification 10/20, changed-path scope 5/6 plus one D5 cross-
reference, D6 13/7, and postcondition binding 15/20. Rebuilding under the final
owner choices yields acquisition/issuance 6/28, cumulative denial 9/6,
release/finalization 11/14, and primitive chronology 24/24. AI plus RF contains
59 planned primary predicates; PB + AI + DP + RF contain 109 numbered primary
definitions; the five focused families PB + AI + DP + RF + CH contain 157.
Adding the separate 5/19 receipt/contract-binding family yields the clearly
labeled expanded affected-family aggregate of 181. The four added pre-action
negatives are outcome-specific succeeded, failed, cancelled, and indeterminate
same-lifecycle recovery shapes with an earlier failed/indeterminate P, a later
passed P, and execution; failed and indeterminate earlier-P values are mandatory
non-additive variants.
The six continuous DP negative owners are DP-N01 missing prerequisite, DP-N02
denial-stage boundary violation, DP-N03 wrong controller/checkpoint/outcome,
DP-N04 controller reference/binding mismatch, and DP-N05 acquired
reference/identity mismatch, plus DP-N06 non-passed same-type history before
the controller. DP-N02 has two mandatory non-additive variants under the same
row predicate: Variant A is unreached future-stage evidence anywhere, and
Variant B is a prerequisite re-observation or other ordinary lifecycle check
after the controller. It adds no primary or timestamp relation. DP-N06 owns
only the four failed/indeterminate-to-failed/indeterminate same-type histories.
`failed -> passed` and `indeterminate -> passed` remain non-additive DP-N03
forms, while the documented passed histories remain accepted. Their member,
order, time, reason, state, A, lease, and digest forms are mandatory
non-additive variants. The first ten RF negative owners retain their existing
predicates. RF-N11 uniquely owns forbidden post-sanitization F member presence
with `expectedSummary`, `observedSummary`, both, unknown payload, and other
free-form/payload variants. RF-N12 owns only primitive exact-F-tuple faults:
wrong F ID, wrong F profile, non-empty F reasons, and their regex-valid
secret-like F alternatives. Those RF-N12 forms are mandatory and non-additive.
RF-N13 owns the universal issued every-L compact-reference violation against the
same source/root identity, including an earlier bad L followed by a correctly
bound finalL. RF-N14 uniquely owns an otherwise-valid serialized receipt with
`sanitization.applied: false`; zero and positive redaction counts are mandatory
non-additive variants, and its witness preserves an otherwise-correct wire F
tuple, digest projection, and delivery-independent state; the false flag means
that F is not accepted as valid. AI-N19 owns conditional issued-root
presence/absence; AI-N20
retains R compact-reference-to-root binding; AI-N21 owns only receipt/source
task identity; AI-N22 owns exactly-one associated-source cardinality; and
AI-N23 retains A compact-reference-to-root binding. AI-N24 owns source/root
`checkId` equality, AI-N25 owns source/singleton-A `checkId` equality, AI-N26
owns source/root `leaseId` equality, AI-N27 owns successful source-profile
digest recomputation, and AI-N28 owns the exact source-to-receipt digest copy.
AI-N21/N24/N25/N26 are four independent equality predicates, while
AI-N22/N27/N28 are three independent source/provenance predicates; each ID is
its own intended `primaryOwner` and has an independently isolatable negative
witness. Forbidden placement, closed-shape, unknown-field, lexical digest, and
UUID/identifier lexical faults remain generic or mandatory non-additive
variants. Source/root/contract lease-ID mismatch remains the independent
nineteenth receipt/contract-binding negative: source and root agree with each
other and jointly differ from the contract, so it is neither AI-N26 nor
RF-N13.
A non-F reserved-ID example is necessarily a duplicate of the mandatory F ID;
generic check-ID uniqueness owns that derived, non-additive rejection, so it
does not add or vary an RF primary. RF is therefore 11/14.

These are normative planned fixture classes. A planned primary ID is its
intended `primaryOwner` for a future serialized fixture. Origin, outcome,
check-type, warning-form, equality, and member variants are mandatory but non-
additive; chronology owns timestamp reversals, generic arrays own array faults,
and derived relations own no primary. Executable fixtures and a fixture
manifest have not been implemented, so documentation consistency does not
claim payload existence or future manifest uniqueness verification.
For referenced TaskContract `C`, `Apath` is the union of
`C.spec.authorizedScope.paths` languages and `Qpath` is the union of
`C.spec.prohibitedScope.paths` languages. A writing receipt's successful scope
claim requires every changed path in `Apath` and not in `Qpath`, with prohibited
membership overriding authorization. Passed verification also requires passed,
exactly referenced `finalV("scope-contained")`. One bad member requires failed
or indeterminate verification and forbids a succeeded lifecycle while the path
remains evidence. Empty writing results satisfy membership vacuously without
waiving completeness or evidence. The scope inventory remains exactly 5/6,
and the D5 non-writing/non-empty changed-path invalid class remains a non-
additive cross-reference.
D5 now contains exactly 21 `3 × 7` Cartesian negatives. Removing the retired
administrative-lock transition removes two TaskContract administrative-lock
array rows, so the array-ordering matrix contains 52 rows while the reusable
evidence union retains its identity and ordering rules.

The current invariant inventory is:

```text
Schema resources = 11
dispatchable kinds = 7
baseline dimensions = 9
permitted-transition branches = 7
required-postcondition branches = 11
check types = 14
denial checkpoints = 9
array-ordering matrix rows = 52
mandatory SG-001 rows = 25
D5 Cartesian negatives = 21
active-operation regressions = 21
administrative-lock regressions = 21
check-outcome conditional branches = 2
non-execution check-outcome values = 3
execution check-outcome values = 4
distinct check-outcome tokens = 5
timestamp paths = 9
timestamp lexical/calendar positives = 10
timestamp lexical/calendar negatives = 24
normative displayed chronology relations = 30
primitive additive chronology relations = 24
chronology positive primary classes = 24
chronology reversal primary classes = 24
focused pre-action positives = 8
focused pre-action negatives = 37
final-E exact-match positives = 4
final-E multi-E positives = 4
final-E total positives = 8
final-E mismatch-matrix negatives = 12
final-E total negatives = 22
focused post-execution-verification positives = 10
focused post-execution-verification negatives = 20
required-postcondition binding positives = 15
required-postcondition binding negatives = 20
lease-acquisition-chain positives = 6
lease-acquisition-chain negatives = 28
cumulative-denial-prerequisite positives = 9
cumulative-denial-prerequisite negatives = 6
lease-release/finalization positives = 11
lease-release/finalization negatives = 14
PB/AI/DP/RF numbered primary definitions = 109
acquisition-plus-release focused primary classes = 59
five focused-family primary classes = 157
changed-path scope positives = 5
changed-path scope dedicated negatives = 6
changed-path scope D5 cross-reference = 1 existing family, not additive
D6 valid receipt-level combinations = 13
D6 invalid receipt-level combinations = 7
receipt/contract equalities = 8
receipt/contract binding positives = 5
receipt/contract binding negatives = 19
receipt/contract binding primary classes = 24
expanded affected-family aggregate including receipt/contract binding = 181
digest-bearing paths = 14
digest computations = 11
digest exact-copy paths = 3
numeric fields = 6
host-resource-exclusivity positives = 5
host-resource-exclusivity negatives = 13
PG-1 distinct timestamp values = 5
PG-1 timestamp occurrences = 38
PG-1 structured-remote occurrences = 7
PG-1 tagged-digest occurrences = 34
PG-1 distinct tagged-digest values = 13
PG-1 profile.digest.execution-receipt-v1 tagged-value occurrences = 3
```

The synchronized affected-family intended-owner mirror is:

```text
postcondition-binding positives = PB-P01..PB-P15 = 15
postcondition-binding negatives = PB-N01..PB-N20 = 20
acquisition/issuance positives = AI-P01..AI-P06 = 6
acquisition/issuance negatives = AI-N01..AI-N28 = 28
cumulative-denial positives = DP-P01..DP-P09 = 9
cumulative-denial negatives = DP-N01..DP-N06 = 6
release/finalization positives = RF-P01..RF-P11 = 11
release/finalization negatives = RF-N01..RF-N14 = 14
PB/AI/DP/RF numbered primary definitions = 109
primitive chronology witnesses = CH-P01..CH-P24 = 24
primitive chronology reversals = CH-N01..CH-N24 = 24
acquisition-plus-release primary classes = 59
five focused families subtotal = 157
receipt/contract binding positives = 5
receipt/contract binding negatives = 19
receipt/contract binding primary classes = 24
expanded affected-family aggregate = 181
```

Each planned range is continuous. Each primary ID denotes the intended
`primaryOwner` of a future serialized fixture. Variants are mandatory but non-
additive, and derived chronology has no primary. No executable fixture payload
or fixture manifest exists.

The AP-1 source synthetic vector has an exact 163-byte non-digest projection,
a 234-byte completed closed `LeaseAcquisitionResultIdentity`, and independently
reproduced Python, Node, and PowerShell/.NET digest
`sha256:c99b362ffd7200478eddc317427976e7d8cc60f4174110c6f4ef3d27e9f25ac6`.
The associated receipt-root vector copies that tagged value exactly and adds no
computation. Receipt/source task, source/root/A check, source/root/contract
lease, and A/R/every-L compact-reference bindings validate separately.
The issued no-lease golden projection remains 3337 UTF-8 bytes and its
completed form remains 3427 UTF-8 bytes. Independent Python, Node, and
PowerShell/.NET runtime-only recomputations produce
`sha256:d3cc668ea95fa385392f04b4e5580cd2fdc810835ae7fd1ab285c102777402b0`,
and delivery copies it without a new computation. Its sequence is passed G
0-4, N5, I6, P7, E8, V9, and F10; A/R/L, the AP-1 source, issued root, compact references,
and lease identity are empty. `startedAt`, G0-4, N5, and contract
`freshness.issuedAt` share the synthetic issuance second; I6 and P7 retain the
next second. This satisfies the RS-1 no-lease issuance bracket without making
either equality mandatory. Equal sanitization, F, and finish timestamps satisfy
FS-1.

The authoritative PG-1 broad region in the design begins inclusively at the
exact heading `### Complete digest-profile catalog` and ends exclusively at
the exact heading `## 11. Complete array-ordering matrix`. Domain W is the raw
on-disk slice with no trimming, normalization, re-encoding, or reordering.
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

The current AP-1 values, reproduced independently with Python, Node, and
PowerShell/.NET, are:

```text
PG-1 W = 38914 bytes / 313 CRLF / cbe0ed9ad14919f5acfef5edba978233ce57d679644e22179dc591d5c2edd9ad
PG-1 B = 38601 bytes / 313 LF / 719899f43c6f8c0908d7b6887a720960d010aab98e99fc254031da7b2e404b58
```

The recount scope is that same broad region and includes all prose, tables, and
JSON examples. It contains 5 distinct canonical timestamps across 38
occurrences, 7 exact structured-remote object occurrences, 34 tagged-digest
occurrences representing 13 distinct values, and 3
`profile.digest.execution-receipt-v1` tagged-value occurrences. Those three
are exactly the completed `ExecutionReceipt`, the `ReceiptDeliveryResult`
exact copy, and the `Recalculated golden results` table entry; the receipt
digest projection contains zero `receiptDigest` members. The attestation
itself is after the exclusive boundary and cannot self-reference. No
receipt-only subregion replaces or narrows PG-1.

The universal twelve-step pipeline remains byte-identical. The catalog now has
fourteen digest selectors, eleven computations, and three exact-copy paths. The
`profile.digest.issued-lease-acquisition-v1` computation belongs to the AP-1
source identity, is distinct from the unchanged acquired-denial profile, and
precedes its exact receipt-root copy, LB-2 bindings, and containing receipt
digest. Framing, the other ten computation profiles/results, the three copy
semantics, API/revision/version values, resource IDs, filenames, UUID URNs, and
`reserved-unpublished` statuses remain unchanged.
This section records design-only requirements and planned vectors. It creates
no Schema, fixture, validator, executable test, model, codec, runtime behavior,
or authority. The current review status is stated above; this README neither
proves nor replaces external audit, GitHub, or authorization records. No Schema
or model implementation is authorized.

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
