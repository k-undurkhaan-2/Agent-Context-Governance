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

The wording in this file records the completed eighth-review lineage and the
ninth-review finding. It does not assert the audit, commit, committed-head
content or signature verification, push, remote/PR-head, reply, resolution,
PR-body, re-review, merge-readiness, or merge state of any repair after
`fa0f3acde1e596c1377a680185375b7f333513d7`. No statement in this file grants
authority for those actions, Schema or model implementation, model-worktree
creation, runtime activation, release, or merge.

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
phase-dependent check outcomes, final-P/E/V selection and binding,
changed-path scope conformance, and outcome/release consistency validate before
receipt-digest acceptance. Delivery binding and chronology validate only after
receipt finalization. No
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
`9999`, Gregorian date and leap-year validity, and all 14 chronology
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
and 18 negative receipt/contract equality-binding vectors, ten positive and 24
negative timestamp vectors, eight positive and 21 negative final-E vectors,
ten positive and 20 negative focused post-execution-verification vectors, five
positive and six dedicated negative changed-path scope vectors, and 15 positive
and 61 negative remote vectors.

These repairs apply the existing universal pipeline in this effective
dependency order: strict bytes/tokens; timestamp and remote lexemes; Schema
structure; local Phase 1 invariants; array and remote order; validated
representation; digest projection/computation; complete TaskContract digest;
receipt/contract equality; chronology, P/E/V presence and universal ordering,
final-`P` freshness, final-`E` and final-`V` outcome binding, changed-path scope
conformance, not-attempted E/V emptiness and outcome consistency; receipt
digest; then delivery binding/chronology. They do
not replace or alter that protected pipeline.
`schema-contracts` specifies the structural/static contract and vectors;
future `model-implementation` owns executable codec, projection, hashing, and
cross-artifact conformance; Phase 3 owns live remote and host facts; and Phase 4
owns trusted provenance, authority, time, freshness, and evidence truth.

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
`post-execution-verification` check. Check sequence is the array position:
sequences are contiguous from zero and check IDs are unique. The final
applicable pre-action, execution, and verification checks are the unique
greatest-sequence members of `P`, `E`, and `V`, respectively. Every selection
uses `sequence` only, never `observedAt`, outcome, serialization, iteration
order, locale, or check ID. Earlier E and V outcomes may differ; only the final
greatest-sequence E and V members control their receipt-level outcomes.

The single check `outcome` field has exactly two conditional branches. An
`execution` check uses exactly `succeeded`, `failed`, `cancelled`, or
`indeterminate`; every non-execution check uses exactly `passed`, `failed`, or
`indeterminate`. Execution `passed`, non-execution `succeeded` or `cancelled`,
and every unknown outcome are invalid. There is no second execution result,
detail, mapping, or lossy cancellation field.

Every `{succeeded, failed, cancelled, indeterminate}` execution attempt
requires `count(P) >= 1`, `count(E) >= 1`, and `count(V) >= 1`. The final
applicable `P` must be passed and strictly before contract expiry; every other
passed `P` must also be strictly pre-expiry. For every `e` in `E`, the final
applicable `P` has a lower sequence and an equal or earlier `observedAt`. For
every `e` in `E` and every `v` in `V`, `e` has a lower sequence and an equal or
earlier `observedAt`. The receipt `verificationOutcome` must equal the final
applicable `V` outcome exactly, and `executionOutcome` must equal the final
applicable `E` outcome exactly. These universal rules mean one early or
interleaved member invalidates the receipt even when a later member is valid.
Whole-second timestamp equality is permitted.

The complete attempted chain is:

```text
by sequence:  final applicable P < every E < every V
by timestamp: final applicable P <= every E <= every V
```

A `not-attempted/not-performed` receipt has both E and V empty; P is optional.
It may retain failed or indeterminate pre-action denial evidence at or after
expiry, while any passed pre-action check remains strictly pre-expiry. Any
stray E or V is invalid. Receipt completion and later lifecycle stages may
occur after expiry. `startedAt` is not proof of action freshness, no
`finishedAt <= expiresAt` rule exists, sequence selection adds no timestamp
relation, and there is no E-to-E timestamp monotonicity requirement. The two
universal cross-type comparisons keep the chronology total exactly 14.

The focused pre-action inventory remains exactly eight positive and 33 negative
classes. The closed final-E family is exactly eight positive and 21 negative
classes: four single-E exact matches; four multi-E exact matches covering every
final outcome; the complete 12-cell top-level/final-E mismatch matrix; E absent
for attempted execution; stray E for not-attempted execution; execution
`passed`; P or V `succeeded`; P or V `cancelled`; and unknown outcomes in both
conditional branches. The multi-E contradiction is one mismatch-matrix cell,
not an added class. The E-absence class explicitly overlaps the four
outcome-specific focused pre-action cases 26 through 29 and is counted once in
the final-E predicate family.

The separate focused post-execution-verification family remains exactly ten
positive and 20 negative classes, including all final-V mismatch and stray-V
cases. Generic sequence gaps, duplicate sequences, duplicate check IDs, and
malformed arrays remain outside these named families. D6 remains exactly 13
valid and 7 invalid receipt-level combinations; final-E and final-V binding are
additional gates and do not change that table.

For referenced TaskContract `C`, `A` is the union of
`C.spec.authorizedScope.paths` languages and `Q` is the union of
`C.spec.prohibitedScope.paths` languages. A writing receipt's successful scope
claim requires every changed path to be in `A` and not in `Q`; prohibited
membership overrides authorization. Passed verification also requires passed
mandatory `scope-contained` evidence. One bad member invalidates the passed
claim, requires failed or indeterminate verification, and forbids a succeeded
lifecycle, while the offending path remains audit evidence. Empty writing
results satisfy membership vacuously without waiving completeness or evidence.

The focused scope family is exactly five positive and six dedicated negative
classes: single and multiple authorized results; empty writing no-effect
evidence; offending paths retained under failed and indeterminate verification;
outside-A, A-and-Q, Q-only, one-bad-of-many, succeeded-lifecycle violation, and
missing passed `scope-contained` evidence negatives. The unchanged D5
non-writing/non-empty-changed-path invalid class is cross-referenced, not
duplicated.

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
chronology relations = 14
focused pre-action positives = 8
focused pre-action negatives = 33
final-E exact-match positives = 4
final-E multi-E positives = 4
final-E total positives = 8
final-E mismatch-matrix negatives = 12
final-E total negatives = 21
focused post-execution-verification positives = 10
focused post-execution-verification negatives = 20
changed-path scope positives = 5
changed-path scope dedicated negatives = 6
changed-path scope D5 cross-reference = 1 existing family, not additive
D6 valid receipt-level combinations = 13
D6 invalid receipt-level combinations = 7
receipt/contract equalities = 8
receipt/contract equality-binding positives = 5
receipt/contract equality-binding negatives = 18
digest-bearing paths = 11
digest computations = 10
receipt/delivery digest copies = 1
numeric fields = 6
```

The repaired synthetic receipt projection is 1744 UTF-8 bytes and its completed
form is 1834 UTF-8 bytes. Its independently recomputed digest is
`sha256:7d7b613acc8f2e7cae920e77bf254989d6a021c36ed977030f8a49c046b83014`,
and the delivery result copies that value without a new computation. The
protected corpus retains five distinct timestamp values across 22 occurrences
and seven structured-remote occurrences. The universal twelve-step pipeline,
all eleven digest selectors, ten profiles/computations, framing, separators,
dependency graph, the other nine digest results, API/revision/version values,
resource IDs, filenames, UUID URNs, and `reserved-unpublished` statuses remain
unchanged.

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
