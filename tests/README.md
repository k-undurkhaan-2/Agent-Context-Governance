# Planned test strategy

Phase 0 documentation bootstrap is complete at baseline commit
`79cc9d77fd48410f37645afdb429a7cd2e34a0bd`. Phase 1: Schemas and
Models is current, but Phase 1 implementation has not yet begun. The repository
remains pre-operational, and no tests or fixtures exist yet. Future tests MUST
be deterministic and MUST use sanitized synthetic data. The planned Schema
contract, static-validation vectors, and fixture inventory are recorded in the
[v1alpha1 Schema contract design](../docs/schema-contract-v1alpha1.md).

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
`SANITIZATION-FINALIZATION: APPLIED-TRUE`. This revision plans all three
repairs without reopening G-1, NR-2, F-1, GR-2, DP-1, FS-1, PG-1, FSAFE-1,
RS-1, LB-2, or AP-1.

The repository documents themselves do not establish the external audit,
commit, push, thread-resolution, PR-body-synchronization, later-review, or
merge state of the revision containing these repairs; those remain separate
external gate records. This README grants no Schema or model implementation,
model-worktree creation, runtime activation, release, or merge authority.

All 11 resources remain `reserved-unpublished`; the validator/toolchain and
Schema-before-model gates remain binding. No Schema implementation exists.
Model-worktree creation and model implementation remain prohibited by the
Schema-before-model sequence.

## Validator and toolchain gate

No validator has been selected, and no `pyproject.toml`, dependency
declaration, transitive lock, or approved executable test environment exists.
Executable Schema tests and Schema implementation remain blocked until
`integration-control` approves the validator/toolchain, packaging, dependency
lock, provenance, licensing, security, and release gate and a fresh, separately
authorized `schema-contracts` task is issued. `schema-contracts` specifies the
validator capability requirements, JSON Schema structural/static conformance
requirements over already-decoded values, and the expected codec/model
vectors. Future `model-implementation` owns executable strict-decoder,
validated-representation, canonical serialization, projection, JCS, hashing,
replay, typed-round-trip, Schema/model, and cross-runtime tests. Ad hoc imports,
globally installed packages, and untracked environments are not accepted.

Planned `schema-contracts` Phase 1 tests are limited to JSON Schema structure,
offline reference resolution, canonical-array and other static checks over
already-decoded closed values, and structural closed-bundle integrity. They do
not claim that incidental JSON loading proves byte-level parsing, duplicate-key
or raw-number rejection, NFC/provenance binding, canonical representation,
JCS, digest projection/hashing/replay, or cross-runtime equality. Task
resolution and RoutingPolicy execution remain Phase 2; live Git, worktree, and
lease tests remain Phase 3; trusted contract, scope-verification, sanitization,
receipt, and delivery tests remain Phase 4; CLI and adapter tests remain Phases
5 and 6.

## Phase 1 test order and ownership

Schema-contract testing comes first. A later, separately authorized
`schema-contracts` task in its dedicated worktree owns conspicuously synthetic
positive and negative Schema fixtures, Schema validation, and Schema contract
tests for structural and static requirements over already-decoded values. It
specifies and records the normative pipeline, representation contract, digest
catalog/framing, canonical bytes, digests, and expected executable vectors; it
does not implement the project codec. The Schema baseline must then receive
independent read-only audit, approval through `integration-control`, and
committed, reviewed integration into `main`.

Only after that integration may the repository owner create or bind a distinct
`model-implementation` worktree from the updated `main`. That role owns model
unit tests; strict UTF-8/token decoding and duplicate/raw-number rejection;
NFC and immutable provenance-bound representation construction; typed models;
canonical serialization; projection, RFC 8785 JCS, SHA-256 framing,
verification, and replay; typed round trips; Schema/model conformance; and
cross-runtime byte/digest reproduction against the approved contract. The two
implementation roles MUST NOT share a worktree. A Schema mismatch discovered
during model work MUST stop the affected work, must not redefine Schema in the
model worktree, and must be routed through separate Schema audit and integration
before model work resumes.

Phase 1 testing is limited to Schema structure and static configuration/model
integrity. Tests for actual task resolution and routing, live Git and worktree
inspection, runtime coordination and leases, trusted contract issuance and
receipt generation, CLI behavior, and agent adapters remain planned for Phases
2 through 6; they are not Phase 1 implementation. No Schema implementation,
model worktree, or model implementation exists or is authorized by this repair.

## Categories

- **Unit tests:** parsing, validation, resolution, policy evaluation, state comparison, and scope matching in isolation.
- **Contract tests:** compatibility between public configuration objects, `TaskContract` records, adapter boundaries, and `ExecutionReceipt` records.
- **Integration tests:** the complete ordered lifecycle from untrusted task intent, through resolution and execution, to lease release and receipt finalization.
- **Concurrency tests:** competing write tasks, exclusive lease acquisition, lease release, stale owners, and state changes during revalidation.
- **Fixture tests:** reusable synthetic repositories and governance inputs representing valid and invalid states.
- **Golden tests:** stable diagnostics, denial reasons, canonical contract serialization bytes, and sanitized receipts reviewed as intentional output changes.

Contract tests MUST prove that a `TaskContract` has authority only after trusted framework issuance or validation of trusted issuer, integrity, derivation, task and target binding, freshness, and current policy, runtime, and lease preconditions. A caller-, adapter-, or task-supplied claim MUST remain untrusted, and a digest alone MUST NOT be accepted as proof of issuance. Phase 0 selects no final signing mechanism.

Tests MUST prove that future governed adapter execution, including plan-only execution, requires a valid bounded `TaskContract` and rejects a missing, invalid, stale, or unbounded contract. They MUST also prove that pre-operational `human-bootstrap-maintenance` authority is not accepted as a runtime `TaskContract`.

### Issued-contract receipt and TaskContract binding coverage

Future `ExecutionReceipt` contract coverage MUST exercise both closed
receipt-origin branches and conditional contract fields. Pre-contract vectors
cover denial before and after acquisition, require acquisition binding only for
a proven acquired lease, require applicable cleanup or indeterminate release
evidence, and reject both fabricated contract binding and successful-execution
claims. Policy-required pre-contract receipts remain optional unless later
policy requires them.

For `origin.type: issued-contract`, coverage retains origin `contractId`,
`contractDigest`, `resolvedTarget`, and `effectiveMode`; receipt-level
`taskId`; and the complete referenced TaskContract's `metadata.id`,
`spec.taskId`, `spec.projectRef`, `spec.domainRefs`,
`spec.target.worktreeRoleRef`, `spec.target.worktreeId`, and
`spec.effectiveMode`. It MUST enforce all eight equalities:

```text
receipt.spec.origin.contractId
  == contract.metadata.id

receipt.spec.origin.contractDigest
  == recomputed profile.digest.task-contract-v1(contract)

receipt.spec.taskId
  == contract.spec.taskId

receipt.spec.origin.resolvedTarget.projectRef
  == contract.spec.projectRef

receipt.spec.origin.resolvedTarget.worktreeRoleRef
  == contract.spec.target.worktreeRoleRef

receipt.spec.origin.resolvedTarget.worktreeId
  == contract.spec.target.worktreeId

receipt.spec.origin.resolvedTarget.domainRefs
  == contract.spec.domainRefs

receipt.spec.origin.effectiveMode
  == contract.spec.effectiveMode
```

LB-2 retains a separate lease-required cross-artifact predicate:

```text
receipt.spec.leaseAcquisitionEvidence.leaseId
  == LeaseAcquisitionResultIdentity.leaseId
  == contract.spec.leaseId
```

The receipt root remains a closed exact
`{checkId, leaseId, acquisitionResultDigest}` record. AP-1 separately defines
the non-public closed source identity:

```text
{
  taskId,
  checkId,
  leaseId,
  acquisitionResultDigest
}
```

It is not an eighth public kind, portable governance, a TaskContract or receipt
field, a second full object embedded in the receipt, or runtime implementation.
Tests recompute `profile.digest.issued-lease-acquisition-v1` only for this
source over closed `{taskId, leaseAcquisitionEvidence:{checkId,leaseId}}` and
require the receipt-root digest to copy the valid source digest exactly. They
then require receipt/source `taskId`, source/root/A `checkId`, and
source/root/contract `leaseId` equality plus the exact compact
`leaseAcquisitionRef: {checkId}` on singleton passed A, singleton passed R,
and every L. I and every other check type forbid the compact reference.
No-lease, denial, and indeterminate-acquisition paths forbid the AP-1
source/root/reference chain. Acquired-denial origin/reference wire shape,
projection, digest, example, and expected bytes remain unchanged.

Phase 1 owns shape, digest-profile, copy/equality, and static-conformance
expectations. Phase 3 produces the acquisition result and stable identity.
Phase 4 validates trusted source provenance, ownership, and evidence truth and
supplies the associated identity during issued-receipt validation/finalization.
Static binding does not prove acquisition, authenticity, current ownership, or
release.

The exact non-digest target projection under test is:

```text
{
  projectRef: contract.spec.projectRef,
  worktreeRoleRef: contract.spec.target.worktreeRoleRef,
  worktreeId: contract.spec.target.worktreeId,
  domainRefs: contract.spec.domainRefs
}
```

Equality is exact post-validation canonical equality. Object references compare
as complete closed objects. Domain arrays require the same canonical length,
members, order, and byte-equivalent canonical member representations; omission,
addition, substitution, reordering, and partial resolution are invalid. Tests
MUST NOT introduce another digest or a fictitious
`TaskContract.spec.taskContractDigest`, or compare other nonduplicated
`requestedMode`, `allowWrite`, scope, `contractVersion`,
freshness, or expected baseline.

The required conformance order is:

1. strictly decode and structurally validate the complete receipt and complete
   referenced TaskContract under the selected Schema revision and, for a
   lease-required issued path, the associated closed non-public
   `LeaseAcquisitionResultIdentity`;
2. apply both public artifacts' local Phase 1 and canonical-array checks plus
   the source identity's closed-shape/member-profile checks;
3. validate the complete contract and derivation prerequisites;
4. recompute `profile.digest.task-contract-v1` over its exact projection;
5. compare digest, contract ID, task ID, complete target, and effective mode;
6. validate LB-2 root presence/absence; require the AP-1 source when applicable;
   recompute and validate the source digest; bind receipt/source task ID,
   source/root/A check ID, and source/root/contract lease ID; require the root
   digest to copy the valid source digest exactly; and bind A/R/every-L compact
   references;
7. apply all 24 primitive chronology comparisons and verify all 30 displayed
   consequences against the same contract and receipt;
8. apply final P/E/V, per-type final V, diagnostic finalG, and final L
   selection; every actual G and every attempted P passed; terminate the same
   lifecycle on any failed/indeterminate P with no later P/E/V and
   not-attempted/not-performed outcomes; exact applicable A/R/N/I; cumulative
   denial prerequisites and future-stage exclusions; per-type reference
   coverage; G/A, G/N, A/R, R/checkpoint, N/checkpoint, checkpoint/issuedAt,
   derived R/issuedAt and N/issuedAt, issuedAt/I,
   every-I/every-P, P/E/V, issued-pre-
   release/L, acquired-Dpre/L, evidence/L, every-non-F/sanitization,
   sanitization/F, and F/finish ordering; mandatory
   `sanitization.applied == true`; EF-1 execution terminality and final E/V/L bindings; scope,
   universal singleton passed terminal F, warning, L-empty, receipt outcome,
   non-writing, and remaining consistency;
9. only then compute and verify or accept the receipt digest; and
10. only after receipt finalization validate delivery receipt-ID binding, exact
    finalized digest copy, and delivery chronology.
Positive vectors MUST cover:

1. a matching plan-only contract/receipt pair;
2. a matching lease-required implementation-mode pair with one valid AP-1
   source, source-profile-valid digest, exact source-to-root digest copy,
   source/root/A identity, A/R/every-L references, and
   source/root/contract lease-ID equality;
3. a matching multi-Domain pair proving complete ordered equality;
4. exact Project, role, worktree, task, contract, digest, and mode equality; and
5. a valid pair followed by a correctly bound delivery result.

Independent negative vectors MUST alter and reject:

1. `contractId`;
2. `contractDigest`;
3. receipt-level `taskId`;
4. `resolvedTarget.projectRef`;
5. `resolvedTarget.worktreeRoleRef`;
6. `resolvedTarget.worktreeId`;
7. one omitted Domain;
8. one added Domain;
9. one substituted Domain;
10. non-canonical or reordered Domains;
11. `effectiveMode`;
12. a correct contract digest with incorrect duplicated claims;
13. matching duplicated claims with a wrong contract digest;
14. matching duplicated claims with another complete contract's digest;
15. matching contract ID with another contract body;
16. receipt-digest acceptance before cross-artifact equality;
17. reinterpretation of the mismatch as `pre-contract-denial`;
18. delivery bound to another receipt ID or digest; and
19. an otherwise-valid lease-required pair whose issued root `leaseId`
    differs from `contract.spec.leaseId`.

Every negative rejects before receipt-digest acceptance; validators neither
repair nor switch contracts. `schema-contracts` specifies this static contract
and its expected vectors. Future `model-implementation` owns strict decoding,
projection, hashing, exact-copy, and executable cross-artifact tests. Phase 3
produces the acquisition result/source identity. Phase 4 owns trusted source and
issuer provenance, lease ownership, authenticity, current authority and
preconditions, and evidence truth. Static binding and digest equality alone
grant no authority.

### Complete resolved-Domain routing coverage

The design contract defines `Dresolved` as one task's non-empty complete
resolved Domain-reference set, `Drule` as one rule's non-empty declared Domain
set, `Rdecision` as the one role selected by a route decision, and `Owned(R)`
as that role's complete `spec.ownedDomainRefs`. Planned tests MUST preserve:

```text
operator == exact:    Drule == Dresolved
operator == contains: Drule ⊆ Dresolved

route eligibility:    Dresolved ⊆ Owned(Rdecision)
```

Neither match operator narrows `Dresolved`. Future Phase 2 integration coverage
MUST exercise the exact order: resolve one Project; resolve one non-empty
complete `Dresolved`; evaluate every rule against that same set; collect all
matches; use explicit deny fallback when none match; find the greatest matching
priority; deny multiple matches at that priority even for the same decision,
same role, or complete owners; apply the unique top rule; deny a deny decision;
require the complete-ownership equation for a route; deny incomplete ownership;
never fall through; never union roles; never widen eligibility through host,
availability, branch, runtime, cached, receipt, or lease state; bind only the
eligible selected role to HostOverlay; require a later trusted TaskContract to
bind the same Project, role, complete Domain set, and target; and deny every
contract mismatch.

The six required planned positive vectors are:

1. `exact` with `Drule == Dresolved` and one route role owning the full set.
2. `contains` with `Drule` a strict subset and one route role owning all of
   `Dresolved`.
3. Exact and contains matches at different priorities, with one unique highest
   match whose role owns the full set.
4. Several matches at different priorities, with one unique highest match whose
   role owns the full set.
5. `contains {A}` against `{A,B}`, with the route role owning `{A,B}`.
6. Independently authorized split tasks A and B, each with its own complete set,
   fresh routing, and one role owning its full split set.

The twelve required planned negative vectors are:

1. `contains {A}` against `{A,B}` with a selected role owning only `{A}`.
2. A higher-priority partial owner and lower-priority complete owner: deny with
   no fallthrough.
3. Several roles collectively cover `Dresolved`, but no one role covers it.
4. Two greatest-priority matches route to different complete owners.
5. Two greatest-priority matches route to the same role.
6. The selected role owns the full set, but the TaskContract omits a Domain,
   adds an unrelated Domain, or changes the selected role.
7. The selected role is incomplete despite a HostOverlay binding, free
   worktree, or available lease.
8. A split is attempted under the original task, contract, lease, or target.
9. No rule matches and fallback is absent, malformed, or not explicit deny.
10. Availability, branch, host, or lease state is offered to widen eligibility.
11. Exact and contains rules tie at the greatest matching priority.
12. The TaskContract Domain set differs from `Dresolved`.

A split is never fallback inside the original lifecycle. Each split requires a
new task intent and fresh Project/Domain resolution, policy evaluation, role
selection, HostOverlay binding, authorization, TaskContract, applicable lease,
and complete lifecycle. These are recorded expectations only; Phase 2 routing
tests and implementation do not exist and are not authorized here.

### Closed `branchPrefix` and branch-policy coverage

A `branchPrefix` is exactly a valid `branchRef`. Matching uses exact ASCII
bytes and only this inclusive component-prefix predicate:

```text
branchPrefixMatches(prefix, branch) =
  branch == prefix
  OR
  branch starts with prefix + "/"
```

The closed policy has exactly four required arrays: `allowed.exact` and
`denied.exact` are set-like `branchRef[]` ordered by `S(branchRef)`;
`allowed.prefixes` and `denied.prefixes` are set-like `branchPrefix[]` ordered
by `S(branchPrefix)`. Each rejects duplicates and non-canonical input without
sorting. Any exact or prefix deny overrides every allow; no allow match denies;
both allow arrays empty deny all branches; empty deny arrays grant nothing.

The seven required planned positive vectors are:

1. Exact allow with no deny.
2. Prefix equality: branch and prefix `refs/heads/release`.
3. Descendant `refs/heads/release/2026` under `refs/heads/release`.
4. Deep descendant `refs/heads/release/2026/july` under that prefix.
5. One valid prefix contained by another, with deterministic allow.
6. Simultaneous exact and prefix allow with no deny.
7. An otherwise allowed symbolic unborn branch, still subject to the separate
   unborn HEAD-state gate.

The 33 required planned negative vectors are:

1. Empty prefix.
2. `refs/heads/`.
3. Stored trailing-slash prefix.
4. Repeated slash.
5. Empty component.
6. Malformed `branchRef` component.
7. Leading dot.
8. Trailing dot.
9. `.lock` suffix.
10. `..`.
11. Wildcard or glob syntax.
12. Regular-expression syntax.
13. `refs/heads/release-malicious` does not match `refs/heads/release`.
14. `refs/heads/releases` does not match `refs/heads/release`.
15. `refs/heads/releas` does not match `refs/heads/release`.
16. No allow match.
17. Both allow arrays empty.
18. Exact allow plus exact deny.
19. Exact allow plus prefix deny.
20. Prefix allow plus exact deny.
21. Prefix allow plus prefix deny.
22. Several matching allows plus one matching deny.
23. Detached HEAD.
24. Duplicate value in `allowed.exact`.
25. Duplicate value in `allowed.prefixes`.
26. Duplicate value in `denied.exact`.
27. Duplicate value in `denied.prefixes`.
28. Non-canonical ordering in each of the four arrays.
29. Raw character-prefix behavior that would match a partial component.
30. Branch-policy success paired with a mismatching live branch observation.
31. Symbolic unborn branch rejected by the separate HEAD-state rules.
32. A deny prefix equal to an allowed exact branch.
33. An exact deny equal to a branch matched by an allow prefix.

Thus `refs/heads/release` matches itself and its one- or multi-component
descendants, but not `refs/heads/release-malicious`, `refs/heads/releases`,
`refs/heads/releas`, or `refs/heads/release_candidate`. Phase 1 owns lexical,
closed-shape, ordering, predicate, precedence, and static vector requirements.
Phase 3 owns actual symbolic/detached/unborn observation, live branch and HEAD,
worktree registration, binding, and repository-state comparison. No branch
fixture or executable test exists yet.

### Closed absolute-host-path coverage

Future Schema and Phase 1 static coverage MUST implement the design record's
[closed `absoluteHostPath`
profile](../docs/schema-contract-v1alpha1.md#closed-absolutehostpath-profile).
It MUST prove the closed required `{ platform, value }` union, exact POSIX
grammar `"/" | "/" segment ("/" segment)*`, and exact drive-only Windows
grammar `[A-Z]:\ | [A-Z]:\segment(\segment)*`.

Positive vectors MUST include `/`, `/srv/synthetic.invalid/worktree`,
`/srv/synthetic.invalid/例`, `C:\`,
`C:\Synthetic.Invalid\Worktree`, and `C:\Synthetic.Invalid\例`.
Negative vectors MUST cover empty and an exactly 4097-scalar value; non-NFC and
every prohibited control scalar; relative, repeated-separator, trailing,
dot-segment, and backslash-invalid POSIX forms; and every Windows lowercase
drive, drive-relative, current-drive-rooted, UNC, device-namespace,
forward-slash, mixed-separator, repeated-backslash, trailing-backslash,
empty-segment, forbidden-punctuation, trailing-space, trailing-dot,
dot-segment, and reserved-device-base class. Reserved-device vectors include
`CON`, `PRN`, `AUX`, `NUL`, `CLOCK$`, every `COM1` through `COM9` and
`LPT1` through `LPT9` value under ASCII-case-insensitive comparison, and
extensions such as `CON.txt` and `LPT1.log`.

These are lexical/static checks only. They MUST preserve spelling and exact
`(platform, value)` equality without normalization, slash replacement, or
case folding. Actual host compatibility, existence, aliases, symlinks and
junctions, registration, identity, and containment remain Phase 3.

### Host-resource-exclusivity coverage

`HOST-RESOURCE-EXCLUSIVITY` is an editorial label and `HX` is its focused
planned-fixture prefix. Neither value is part of the wire or API surface.

The exact Finding A predicates are:

- **A1.** Across the complete `HostOverlay.spec.bindings` array, every
  `worktreeId` is globally unique. A different `roleRef` does not permit reuse.
- **A2.** Every already-validated exact `repositoryRoot` identity is globally
  exclusive across distinct bindings. Static comparison is exact
  `(platform, value)` equality only; it performs no filesystem resolution,
  case folding, Unicode normalization, symlink, junction, reparse-point,
  registration, or other alias resolution.
- **A3.** In future Phase 3, every distinct binding MUST resolve to a distinct
  canonical registered physical Git worktree.
- **A4.** Future Phase 3 uncertainty about physical-worktree identity fails
  closed, including alias, case, symlink, junction, reparse-point, and
  registration ambiguity.

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
| `HX-A-P01` | Distinct `worktreeId` and exact `repositoryRoot` identities across all bindings pass static validation. |
| `HX-A-P02` | Future Phase 3 proves that every distinct binding resolves to a distinct canonical registered physical Git worktree. |
| `HX-B-P01` | Both coordination roots are statically outside or siblings of every binding root; equal coordination roots and a worktree beneath a coordination root are non-additive valid variants. |
| `HX-B-P02` | Future Phase 3 proves that both coordination roots resolve outside every actual bound registered worktree. |
| `HX-A-N01` | A duplicate `worktreeId` rejects; reuse under a different `roleRef` is a non-additive variant. |
| `HX-A-N02` | A duplicate already-validated exact `repositoryRoot` identity rejects. |
| `HX-A-N03` | Lexically distinct binding roots that resolve to the same physical worktree reject in future Phase 3. |
| `HX-A-N04` | Indeterminate physical-worktree distinctness rejects in future Phase 3. |
| `HX-B-N01` | `stateRoot` exactly equals a binding `repositoryRoot`. |
| `HX-B-N02` | `stateRoot` is a strict descendant of a binding `repositoryRoot`. |
| `HX-B-N03` | `lockRoot` exactly equals a binding `repositoryRoot`. |
| `HX-B-N04` | `lockRoot` is a strict descendant of a binding `repositoryRoot`. |
| `HX-B-N05` | A lexically separate coordination root resolves equal to or inside an actual bound registered worktree in future Phase 3. |
| `HX-B-N06` | Live alias or containment identity is indeterminate in future Phase 3. |

HX is exactly 4 positive and 10 negative primary predicates. It is separately
counted and does not revise any retained focused-family or regression total.

WIRE/API SURFACE UNCHANGED: Review-13 A+B only shrinks the accepted
`HostOverlay` set. It does not alter the API version, revision, resource kinds,
JSON property names, HostOverlay binding fields, enums, reason codes, check
types, transition types, postconditions, receipt outcomes, or digest fields.
The digest graph remains 14 field paths, 11 computations, and 3 exact copies.

### Canonical timestamp and chronology coverage

The shared `canonicalUtcTimestamp` accepts only
`YYYY-MM-DDTHH:MM:SSZ` matching:

```text
^[0-9]{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])T(?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]Z$
```

Future Schema uses `type: string`, that pattern, and asserted
`format: date-time` as an additional check. Phase 1 additionally requires
years `0001` through `9999`, rejects `0000`, and validates Gregorian dates
and ordinary leap years. Hours stop at `23`; minutes and seconds stop at `59`.
Leap second `60`, `24:00:00`, fractions, offsets, lower-case delimiters,
whitespace, alternate spellings, normalization, and repair are invalid.

The exact nine paths are:

1. `TaskContract.spec.issuanceCheckpoint.observedAt`;
2. `TaskContract.spec.freshness.issuedAt`;
3. `TaskContract.spec.freshness.expiresAt`;
4. `ExecutionReceipt.spec.startedAt`;
5. `ExecutionReceipt.spec.finishedAt`;
6. `ExecutionReceipt.spec.sanitization.completedAt`;
7. `ExecutionReceipt.spec.checks[].observedAt`;
8. `ExecutionReceipt.spec.origin.preContractEvidence.observedAt`; and
9. `ReceiptDeliveryResult.attemptedAt`.

RS-1 defines receipt `startedAt` as the lower time boundary of the complete
lifecycle evidence serialized in either origin. Every check is at or after it;
denial `preContractEvidence` is at or after it; and every issued contract has
`startedAt <= freshness.issuedAt`. For referenced contract C, lease-required
tests enforce `R.observedAt <= C.issuanceCheckpoint.observedAt <=
C.freshness.issuedAt <= I.observedAt`; no-lease tests enforce
`N.observedAt <= C.issuanceCheckpoint.observedAt <= C.freshness.issuedAt <=
I.observedAt`. Equality is allowed at every non-strict boundary but is not
required. The strict sequence chains remain independently `G < A < R < I < P`
and `G < N < I < P`.

Positive lexical/calendar and artifact vectors MUST cover:

1. `0001-01-01T00:00:00Z`;
2. `9999-12-31T23:59:59Z`;
3. `2000-02-29T00:00:00Z`;
4. `2004-02-29T23:59:59Z`;
5. a valid ordinary date in a non-leap year;
6. every current protected timestamp literal;
7. strict chronology progression;
8. every permitted equality boundary;
9. strict freshness with whole-second separation; and
10. valid contract/receipt and receipt/delivery pairs.

Independent negative vectors MUST reject:

1. lower-case `t`;
2. lower-case `z`;
3. a numeric UTC offset;
4. missing `Z`;
5. missing zero padding;
6. any fractional seconds;
7. one fractional digit;
8. three fractional digits;
9. six fractional digits;
10. a trailing decimal point;
11. leap second `:60`;
12. `24:00:00`;
13. an invalid month;
14. an invalid day;
15. an invalid month/day combination;
16. an invalid February 29;
17. year `0000`;
18. a five-digit year;
19. a signed year;
20. leading whitespace;
21. trailing whitespace;
22. internal whitespace;
23. an alternate spelling of an equivalent instant; and
24. valid chronology encoded with an invalid lexical spelling.

Phase 1 owns lexical, calendar, leap-year, and instant-order checks without a
trusted clock. Future `model-implementation` owns strict decoding and
executable parser/comparison conformance. Phase 4 owns trusted time,
authenticity, freshness, and event truth. The mechanically recounted PG-1 broad
region contains five distinct timestamp values across 38 occurrences; its full
remote and digest counts are mirrored below.

Future Phase 1 static and contract coverage MUST enforce all 24 primitive
chronology relations and verify all 30 displayed consequences in the design
record's [timestamp chronology
section](../docs/schema-contract-v1alpha1.md#timestamp-chronology). Equality
remains permitted at every earlier allowed boundary. The existing
`freshness.issuedAt < freshness.expiresAt` and every-passed-P-before-expiry
relations remain the only strict timestamp relations.

The planned chronology ledger assigns `CH-P01..CH-P24` and
`CH-N01..CH-N24` to the 24 primitive relations. CH15 now owns R/checkpoint and
CH16 owns N/checkpoint; their positive and reversal IDs do not change. The direct
R/issuedAt and N/issuedAt relations are derived through the existing
checkpoint/issuedAt primitive. Each primitive owns one planned positive witness
and one independent reversal predicate. Strict progression, equality, receipt-
origin, empty/populated-array, universal-member, and later-valid-member forms are
mandatory non-additive variants. The six displayed transitive relations:
sanitization/finish, start/finish, denial-evidence/F, non-F/F, R/issuedAt, and
N/issuedAt, are derived/non-additive and own no reversal class. The Review-12
lease and no-lease counterexamples keep both old direct relations and
checkpoint/issuedAt valid while placing the checkpoint before R or N; the old
direct-only rule accepted them and CH-N15/CH-N16 now reject them. Executable
fixtures
and a fixture manifest have not been implemented.

The chronology inventory counts ordering between distinct lifecycle events.
Exact timestamp equality used only to bind two representations of one evidence
identity is not chronology. Thus
`preContractEvidence.observedAt == controller.observedAt` has DP-owned
equality-positive coverage, a DP-N04-owned mismatch, and no displayed,
primitive/additive, or derived/non-additive CH count. Tests apply the same
binding-family classification to receipt/contract exact equality, digest
copies, denial acquisition lease-ID/digest equality, LB-2 root/reference and
contract lease-ID equality, and `controllerCheckId`.

For one complete issued-contract receipt and referenced TaskContract pair, let
P be every pre-action-revalidation check, E every execution check, and V every
post-execution-verification check. Existing array validation first requires
sequence equal to position, contiguous sequence, and unique check IDs. Final P,
E, and V are the unique greatest-sequence members; sequence alone selects them.

The check vocabulary is exactly fourteen types and one conditional outcome
field: execution uses `succeeded`, `failed`, `cancelled`, or `indeterminate`;
every other check uses `passed`, `failed`, or `indeterminate`. The optional
closed `postconditionRef: {type}` uses the exact eleven required-postcondition
types and is allowed only on V; the other thirteen types, including N, forbid
it. General V may omit it but cannot satisfy a named obligation.

The separate compact `leaseAcquisitionRef` is a closed exact `{checkId}`
object. It is required only on A, R, and every L of a lease-required issued
receipt and always names the receipt-level issued root and singleton A. It is
forbidden on I, every other check type, all checks in a no-lease issued receipt,
and every pre-contract-denial check. Tests reject an unknown member, a
`leaseId` or digest inside the compact object, missing A or R reference, any
bad earlier L reference even when finalL is correct, and every forbidden-path
presence.

After complete contract digest/equality binding, tests define V(t) for each
required type t as the referenced subset and select `finalV(t)` by greatest
sequence. Every attempted receipt has at least one V(t) for every required type;
passed verification requires every finalV(t) passed. An earlier passed member
cannot repair a later failed or indeterminate finalV(t). The global final V
continues to bind `verificationOutcome` and may be referenced or general.

Every attempted receipt also requires P, E, and V. Every P in an attempted
receipt is passed and strictly pre-expiry. Under
`EXECUTION-FAILURE-TERMINALITY: EF-1`, every E strictly before final E is
`succeeded`; an E with outcome `failed`, `cancelled`, or `indeterminate` is
final E and has no later E in that lifecycle. Every E follows final P and every
V follows every E by strict sequence and non-decreasing timestamp. Final E
still binds `executionOutcome`; global final V binds `verificationOutcome`.
EF-1 adds no E-to-E timestamp ordering.

Any failed or indeterminate P is the final P, has only passed earlier P
members, forbids every later P/E/V, leaves E/V empty, and requires
`not-attempted/not-performed`. Release and closure evidence remain applicable,
and the lifecycle follows the existing denied/fail-closed and release-
precedence semantics. Recovery from P terminality requires a fresh task,
contract, attempt, and receipt lifecycle.

A final non-success E is different: execution was attempted, so the matching
`executionOutcome` remains `failed`, `cancelled`, or `indeterminate`; required
V still follows all E, and terminal processing still covers pre-release
evidence, ownership-checked L when applicable, sanitization, F, receipt-digest
validation, and delivery. Release failure or any later processing result never
permits another E in the same lifecycle. A retry requires a fresh lifecycle
and repeats task resolution, Project/Domain resolution, routing, HostOverlay
binding, live Git/runtime inspection, lease acquisition when required,
pre-issuance revalidation, trusted TaskContract issuance, and immediately-
before-action P. No retry/recovery wire state, public field, digest, or
chronology edge is added. A not-attempted receipt keeps E and
V empty and may omit P.

GTypes is exactly `intent-validation`, `project-domain-resolution`,
`role-routing`, `host-binding`, and `initial-preflight`. Every issued receipt
has at least one of each type and every actual G is passed. Tests MUST reject a
failed or indeterminate G even when a later same-type G passed. FinalG remains
a greatest-sequence diagnostic only; same-receipt recovery is forbidden.
Repeated G is positive coverage only when all members are passed. Every issued
receipt has exactly one passed I.

Lease-required issuance has singleton passed A/R, N empty, and
`every G < A < R < I < every P`. No-lease issuance has A/R empty, singleton
passed N, no lease identity, and `every G < N < I < every P`. Attempted paths
retain final P < every E < every V; non-attempted paths keep E/V empty and may
omit P. Every actual G participates in ordering.

The lease-required path also requires one valid AP-1 source, source-profile
digest validation, exact source-to-root digest copy, source/root/A identity,
compact A/R references, source/root/contract lease-ID equality, and the RS-1
timestamp bracket `R <= issuanceCheckpoint <= issuedAt <= I`. The no-lease
path forbids the source, root, and all compact references, requires
`releaseOutcome: not-required`, and uses
`N <= issuanceCheckpoint <= issuedAt <= I`. An indeterminate acquisition cannot create a stable
source, issued root, or issued contract; it remains a pre-contract denial with
no stable lease identity.

DP-1 planned coverage uses the exact cumulative denial prefixes, structured
bindings, and controller stop boundary. Every one of the nine positive
checkpoint forms requires
`preContractEvidence.controllerCheckId` to resolve to exactly one same-receipt
check. The checkpoint-to-type mapping is exact and identity-valued across the
nine closed checkpoint tokens. The controller MUST be the unique greatest-
sequence member of that type, have failed/indeterminate outcome, exactly equal
`observedAt` and canonical `reasonCodes`, have only passed earlier same-type
members, and occupy the matrix-required position. The controller is therefore
both the first non-passed and final same-type observation. This rule applies to
all nine checkpoint types. Tests reject `failed -> failed`, `failed ->
indeterminate`, `indeterminate -> failed`, `indeterminate ->
indeterminate`, `failed -> passed`, and `indeterminate -> passed`. They
accept `passed -> failed`, `passed -> indeterminate`, `passed -> passed ->
failed`, and `passed -> passed -> indeterminate` when the remaining
cumulative conditions hold. Recovery requires a new task, attempt, and
lifecycle, with no retry epoch. Successful issued-path A/R/N/I cardinalities
remain separate. `sanitizedSummary` is an explanatory derivative only; it is
not controller identity and has no equality requirement with optional check
prose.

Let `O` be exactly the twelve ordinary lifecycle-stage check types:
`intent-validation`, `project-domain-resolution`, `role-routing`,
`host-binding`, `initial-preflight`, `pre-issuance-revalidation`,
`lease-acquisition`, `post-acquisition-revalidation`,
`contract-issuance`, P, E, and V. L and F are outside `O`. For each row,
tests require every actual member of `Prereq(r)` to be passed with
`sequence < controller.sequence`, not merely an existing, greatest, final,
or selected member. Only prerequisite and controller ordinary types may occur;
every unreached ordinary type is empty; and no ordinary check may occur after
the controller. Only required acquired-path L and universal F may follow, with
`controller < every L < F`; all other rows keep L empty and allow only F.
These checks compare sequence only and add no timestamp relation.

If and only if the origin acquisition state is `acquired`,
`preContractEvidence` also requires the closed
`acquisitionEvidenceRef {checkId, leaseId, acquisitionResultDigest}`. It
selects the exact same-receipt singleton passed A required by the matrix, and
its lease ID and digest equal the acquired origin exactly. Every non-acquired
state forbids the reference, and it contains no issued-contract field.

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

Every denial has `changedPaths: []`, sanitization, and terminal passed F. Tests
MUST independently reject the six DP primary classes: a missing completed
prerequisite; a denial-stage boundary violation; a wrong controller/checkpoint/
outcome; a controller reference/binding mismatch; and an acquired-reference/
identity mismatch; plus a non-passed same-type observation before the
controller. DP-N02 owns both Variant A, unreached future-stage evidence
anywhere, and Variant B, a prerequisite re-observation or other ordinary check
after the controller, under one row-level predicate and without a new primary
or timestamp relation. Mandatory non-additive variants include missing/unknown
controller ID, wrong type, earlier same-type or non-greatest member, later pass,
timestamp mismatch, reason-code mismatch/reorder/extra/missing, check reorder,
missing acquired reference, reference on a non-acquired state, wrong or
non-passed A, non-A, lease mismatch, and digest mismatch. DP-N06 remains only
the four failed/indeterminate-to-failed/indeterminate same-type histories;
`failed -> passed` and `indeterminate -> passed` remain DP-N03, and the
documented passed histories remain accepted. N denial cannot be encoded as R.
Acquired-R denial cannot omit G/A, fabricate I/P/E/V, or skip required
ownership-checked post-controller L cleanup.

Every serialized receipt requires `sanitization.applied: true`. True means the
selected sanitizer or evaluation completed; it does not mean a redaction
occurred, so `redactionCount: 0` is valid. False is structurally Boolean but
invalidates the receipt before passed terminal F, receipt-digest acceptance, or
delivery binding. No new wire field or branch is introduced.

Every serialized receipt has exactly one passed terminal F. A positive F
contains exactly `sequence`, `checkId`, `checkType`, `outcome`,
`observedAt`, `profileId`, and `reasonCodes`; tests MUST reject
`expectedSummary`, `observedSummary`, both, `postconditionRef`,
`leaseAcquisitionRef`, or any
other summary, detail, payload, free-form, or unknown member. Its exact tuple is
`checkId: check.receipt-finalization`,
`profileId: profile.validation.v1`, `reasonCodes: []`, and passed outcome.
The primitive rule is F implies that exact tuple. Every receipt's mandatory
single F plus global check-ID uniqueness makes non-F use of the reserved ID a
derived generic duplicate-ID rejection, not an RF-N12 variant. Generic
`checkIdentifier` syntax is unchanged, the validation profile is not
F-exclusive, and empty reason codes are not universal. Every non-F check
precedes F by sequence and is no later than sanitization; every denial's
`preContractEvidence` is no later than sanitization; sanitization is no later
than F; and F is no later than `finishedAt`. Whole-second equality is
permitted. F is finalization completion after sanitization, not proof of digest
insertion, delivery, lifecycle success, or release success.

For post-sanitization F evidence, textual identity is safe-by-construction only
when its complete semantic value domain is protocol-closed.
Lexical validity alone is insufficient. A producer alternative satisfying
generic grammar is invalid, including
`check.c-users-alice.secrets.api-key-abcd1234`,
`profile.synthetic.secret.sk-live-abcdef123456`, and
`reason.synthetic.secret.token-abcdef123456`. Coverage targets arbitrary
post-sanitization text, host/operator or path-like material, secret-like
strings, and diagnostic prose; it does not claim information-theoretic
covert-channel elimination.

A lease-required issued receipt or acquired denial requires L, finalL mapping,
every applicable pre-release/Dpre check before every L, every L no later than
sanitization, and exact warning binding for failed/indeterminate finalL. Every
no-release path keeps L empty but still sanitizes and records F. Indeterminate
acquisition retains no stable identity, its warning and indeterminate outcomes,
and F.

For a lease-required issued receipt, every L carries the same compact root
reference as A and R. This is universal over all L and not a finalL-only rule.
An acquired denial retains its unchanged origin/evidence reference and forbids
the issued root and compact references.

The six complete evidence paths are:

```text
lease required, attempted:
  every G < A < R < I < every P < every E < every V < every L < F

lease required, not attempted:
  every G < A < R < I < optional P < every L < F
  E == empty and V == empty

no lease, attempted:
  every G < N < I < every P < every E < every V < F
  A == empty and R == empty and L == empty

no lease, not attempted:
  every G < N < I < optional P < F
  E == empty and V == empty and A == empty and R == empty and L == empty

acquired pre-contract denial:
  every Dpre < every L < F
  preContractEvidence <= every L <= sanitization <= F by timestamp

other pre-contract denial:
  every non-F check < F
  preContractEvidence <= sanitization <= F by timestamp
  L == empty
```

All non-F checks are no later than sanitization, sanitization is no later than
F, and F is no later than finish. There is no E-to-E or L-to-L timestamp
monotonicity. The complete displayed/primitive/derived chronology counts are 30/24/6.
The eight exact focused positive classes are:

1. `succeeded` attempted execution with a final passed/pre-expiry check and a
   later execution check;
2. `failed` attempted execution with a final passed/pre-expiry check and a
   later execution check;
3. `cancelled` attempted execution with a final passed/pre-expiry check and a
   later execution check;
4. `indeterminate` attempted execution with a final passed/pre-expiry check and
   a later execution check;
5. a final passed check exactly at the permitted issuance-side lower-bound
   equality followed by an execution check;
6. a final passed check at the last valid whole second before expiry followed
   by an execution check;
7. completion and later lifecycle stages after expiry following a valid final
   passed/pre-expiry check and later execution check; and
8. multiple pre-action checks, all passed, with the greatest-sequence final P
   strictly pre-expiry and followed by an execution check.

Every attempted-execution positive contains at least one `execution` check
after the final valid pre-action check.

The first 33 of the 37 exact focused negative classes are the existing 25
classes plus exactly eight execution-presence and ordering classes:

1. `succeeded` attempted execution with the required check missing;
2. `failed` attempted execution with the required check missing;
3. `cancelled` attempted execution with the required check missing;
4. `indeterminate` attempted execution with the required check missing;
5. `succeeded` attempted execution with only failed pre-action checks;
6. `failed` attempted execution with only failed pre-action checks;
7. `cancelled` attempted execution with only failed pre-action checks;
8. `indeterminate` attempted execution with only failed pre-action checks;
9. `succeeded` attempted execution with only indeterminate pre-action checks;
10. `failed` attempted execution with only indeterminate pre-action checks;
11. `cancelled` attempted execution with only indeterminate pre-action checks;
12. `indeterminate` attempted execution with only indeterminate pre-action
    checks;
13. a passed pre-action check exactly at expiry;
14. a passed pre-action check after expiry;
15. a whole receipt lifecycle beginning after expiry while claiming successful
    attempted execution;
16. a `not-attempted` receipt containing a passed check exactly at expiry;
    and
17. a `not-attempted` receipt containing a passed check after expiry;
18. `succeeded` execution with an earlier passed/pre-expiry check followed by
    a final failed check;
19. `failed` execution with an earlier passed/pre-expiry check followed by a
    final failed check;
20. `cancelled` execution with an earlier passed/pre-expiry check followed by
    a final failed check;
21. `indeterminate` execution with an earlier passed/pre-expiry check followed
    by a final failed check;
22. `succeeded` execution with an earlier passed/pre-expiry check followed by
    a final indeterminate check;
23. `failed` execution with an earlier passed/pre-expiry check followed by a
    final indeterminate check;
24. `cancelled` execution with an earlier passed/pre-expiry check followed by
    a final indeterminate check; and
25. `indeterminate` execution with an earlier passed/pre-expiry check followed
    by a final indeterminate check;
26. `succeeded` attempted execution with no execution check;
27. `failed` attempted execution with no execution check;
28. `cancelled` attempted execution with no execution check;
29. `indeterminate` attempted execution with no execution check;
30. `succeeded` attempted execution with an execution check before the final
    applicable pre-action check and another execution check after it;
31. `failed` attempted execution with an execution check before the final
    applicable pre-action check;
32. `cancelled` attempted execution with an execution check before the final
    applicable pre-action check; and
33. `indeterminate` attempted execution with an execution check before the
    final applicable pre-action check;
34. `succeeded` attempted execution with an earlier failed or indeterminate P,
    a later passed P, and execution;
35. `failed` attempted execution with an earlier failed or indeterminate P, a
    later passed P, and execution;
36. `cancelled` attempted execution with an earlier failed or indeterminate P,
    a later passed P, and execution; and
37. `indeterminate` attempted execution with an earlier failed or
    indeterminate P, a later passed P, and execution.

For cases 34 through 37, failed and indeterminate earlier-P values are mandatory
non-additive variants of one outcome-specific predicate. The final P is passed,
so these do not duplicate cases 18 through 25. Duplicate sequence, sequence
gap, duplicate check ID, and other generic check-array failures remain in their
existing families and do not inflate this 37-class focused pre-action total.

#### Focused final-execution-evidence vector family

The exact eight positive classes are:

1. single final E `succeeded` exactly matching
   `executionOutcome: succeeded`;
2. single final E `failed` exactly matching `executionOutcome: failed`;
3. single final E `cancelled` exactly matching
   `executionOutcome: cancelled`;
4. single final E `indeterminate` exactly matching
   `executionOutcome: indeterminate`;
5. multiple E members with every earlier E `succeeded`, final E `succeeded`,
   and a matching top-level outcome;
6. multiple E members with every earlier E `succeeded`, final E `failed`, and
   a matching top-level outcome;
7. multiple E members with every earlier E `succeeded`, final E `cancelled`,
   and a matching top-level outcome; and
8. multiple E members with every earlier E `succeeded`, final E
   `indeterminate`, and a matching top-level outcome.

The complete 12-class mismatch matrix independently rejects each pairing of
one top-level execution outcome with each of the other three final-E outcomes:

| `executionOutcome` | Invalid final-E outcomes |
| --- | --- |
| `succeeded` | `failed`; `cancelled`; `indeterminate` |
| `failed` | `succeeded`; `cancelled`; `indeterminate` |
| `cancelled` | `succeeded`; `failed`; `indeterminate` |
| `indeterminate` | `succeeded`; `failed`; `cancelled` |

The `succeeded`/final-`failed` cell uses multiple E members with an earlier
`succeeded` result. It proves the earlier matching result cannot override the
contradictory final E and is counted once, not twice.

The remaining nine negative classes are:

13. attempted execution with E empty and therefore no final E because every
    check is non-execution;
14. `not-attempted/not-performed` with any E member;
15. execution using outcome `passed`;
16. P using outcome `succeeded`;
17. V using outcome `succeeded`;
18. P using outcome `cancelled`;
19. V using outcome `cancelled`;
20. execution using an unknown outcome; and
21. a non-execution check using an unknown outcome.

One additional EF-1 primary negative is:

22. execution terminality violation: an E with `failed`, `cancelled`, or
    `indeterminate` outcome is followed by any later E member.

The mandatory non-additive variants are the `3 x 4 = 12` Cartesian product of
earlier terminal outcome (`failed`, `cancelled`, `indeterminate`) and later E
outcome (`succeeded`, `failed`, `cancelled`, `indeterminate`). They remain one
primary predicate, not twelve primary classes.

Case 13 explicitly overlaps focused pre-action negative cases 26 through 29:
those four planned outcome-specific variants satisfy the one E-absence
predicate class here. The final-E recount is 12 mismatch-matrix classes + 9
existing non-matrix classes + 1 EF-1 terminality class = 22. This family is
exactly 8 positive and 22 negative classes and no other class is double-
counted.

Every EF-1 negative witness keeps P valid and passed; final-P ordering valid;
E sequence contiguous; check IDs unique; outcome vocabulary valid; top-level
`executionOutcome` equal to the later greatest-sequence E; V valid and after
all E; scope valid; required L/release valid; `sanitization.applied: true`; F,
digest, contract binding, and delivery-independent state otherwise valid. The
only failure is a non-success E followed by a later E.

Required adversarial replay cases are:

- `EF-FAIL-RECOVER`: E9 `failed`, E10 `succeeded`, top-level `succeeded` ->
  reject;
- `EF-CANCEL-RECOVER`: E9 `cancelled`, E10 `failed`, top-level `failed` ->
  reject;
- `EF-INDET-REPEAT`: E9 `indeterminate`, E10 `indeterminate`, top-level
  `indeterminate` -> reject;
- `EF-VALID-SUCCESS-THEN-FAIL`: E9 `succeeded`, E10 `failed`, top-level
  `failed` -> accept;
- `EF-VALID-MULTI-SUCCESS`: E9 `succeeded`, E10 `succeeded`, top-level
  `succeeded` -> accept; and
- `EF-VALID-SINGLE-FAIL`: single E9 `failed`, matching top-level `failed`,
  followed by valid V, applicable L, sanitization, and F -> accept.

#### Focused post-execution-verification vector family

This named family is separate from the focused pre-action family and from D6.
The exact ten non-overlapping positive classes are:

1. `succeeded/passed` with one valid E and one later V;
2. `failed/passed` with one valid E and one later V;
3. `cancelled/passed` with one valid E and one later V;
4. `indeterminate/passed` with one valid E and one later V;
5. `succeeded/failed` with final V `failed`;
6. `succeeded/indeterminate` with final V `indeterminate`;
7. valid E/V timestamp equality at whole-second precision;
8. multiple E members, all preceding one V by sequence and timestamp;
9. multiple V members after all E members, with an earlier failed or
   indeterminate V followed by a final passed V; and
10. `not-attempted/not-performed` with V empty.

The exact twenty non-overlapping negative classes are:

1. `succeeded` attempted execution with V missing;
2. `failed` attempted execution with V missing;
3. `cancelled` attempted execution with V missing;
4. `indeterminate` attempted execution with V missing;
5. `succeeded` attempted execution with a V sequenced before an E and another
   valid final V later, proving that the later V cannot cure the violation;
6. `failed` attempted execution with a V sequenced before an E;
7. `cancelled` attempted execution with a V sequenced before an E;
8. `indeterminate` attempted execution with a V sequenced before an E;
9. a V interleaved between two E members;
10. correct sequence order but a V timestamp before an E timestamp;
11. multiple V members where one V timestamp is before an E while the final V
    is otherwise valid;
12. final V `passed` with receipt `verificationOutcome: failed`, including an
    earlier V with outcome `failed` that matches the receipt;
13. final V `passed` with receipt `verificationOutcome: indeterminate`;
14. final V `failed` with receipt `verificationOutcome: passed`;
15. final V `failed` with receipt `verificationOutcome: indeterminate`;
16. final V `indeterminate` with receipt `verificationOutcome: passed`;
17. final V `indeterminate` with receipt `verificationOutcome: failed`;
18. `not-attempted/not-performed` with one stray V whose outcome is `passed`;
19. `not-attempted/not-performed` with one stray V whose outcome is `failed`;
    and
20. `not-attempted/not-performed` with one stray V whose outcome is
    `indeterminate`.

Except when the primary fault belongs to the dedicated postcondition-binding
family, every planned attempted-issued class in this 10/20 family requires
referenced V evidence for every required type, and every passed-verification
positive requires each per-type final V passed. Those are prerequisites, not added cases. Class 10
keeps V empty and therefore contains no reference. The exact 10/20 total is
unchanged.

Case 12 proves greatest-sequence final selection because the earlier V matches
the receipt and the later final V does not. Generic sequence gaps, duplicate
sequences, duplicate check IDs, and malformed check arrays remain outside this
10/20 family. The focused pre-action inventory remains 8/37, and the unchanged
D6 receipt-level table remains exactly 13 valid and 7 invalid combinations.

#### Focused required-postcondition verification-binding vector family

The exact fifteen positive classes are:

1. **PB-P01:** passed referenced final V for `scope-contained`;
2. **PB-P02:** passed referenced final V for `ref-state`;
3. **PB-P03:** passed referenced final V for `head-state`;
4. **PB-P04:** passed referenced final V for `index-state`;
5. **PB-P05:** passed referenced final V for `tracked-state`;
6. **PB-P06:** passed referenced final V for `untracked-state`;
7. **PB-P07:** passed referenced final V for `ignored-state`;
8. **PB-P08:** passed referenced final V for `submodule-state`;
9. **PB-P09:** passed referenced final V for `active-operations`;
10. **PB-P10:** passed referenced final V for `administrative-locks`;
11. **PB-P11:** passed referenced final V for `lease-state`;
12. **PB-P12:** one referenced V serving as both per-type and global final V;
13. **PB-P13:** earlier failed/indeterminate same-type V followed by passed finalV(t);
14. **PB-P14:** complete per-type passed evidence followed by a matching unreferenced global
    final V; and
15. **PB-P15:** all eleven type-unique obligations, each with passed finalV(t), under passed
    receipt verification.

Classes 2 through 11 also include mandatory scope evidence but do not count it
again. The exact twenty negative classes are:

1. **PB-N01:** reference on `intent-validation`;
2. **PB-N02:** reference on `project-domain-resolution`;
3. **PB-N03:** reference on `role-routing`;
4. **PB-N04:** reference on `host-binding`;
5. **PB-N05:** reference on `initial-preflight`;
6. **PB-N06:** reference on `lease-acquisition`;
7. **PB-N07:** reference on `post-acquisition-revalidation`;
8. **PB-N08:** reference on `contract-issuance`;
9. **PB-N09:** reference on `pre-action-revalidation`;
10. **PB-N10:** reference on `execution`;
11. **PB-N11:** reference on `lease-release`;
12. **PB-N12:** reference on `receipt-finalization`;
13. **PB-N13:** missing `type` or an extra reference-object member;
14. **PB-N14:** type outside the exact eleven-value enum;
15. **PB-N15:** valid enum type absent from the bound contract;
16. **PB-N16:** missing scope V(t) while another referenced type passes;
17. **PB-N17:** missing any other required V(t) while scope passes;
18. **PB-N18:** unreferenced general V offered as sole evidence for an obligation;
19. **PB-N19:** earlier passed V(t), failed finalV(t), and passed top-level verification; and
20. **PB-N20:** earlier passed V(t), indeterminate finalV(t), and passed top-level
    verification.

`pre-issuance-revalidation` is a mandatory planned non-additive check-type
variant of the same non-V reference rejection predicate. Its future fixture
must be fully serialized, but no such fixture exists yet. It does not create a
twenty-first primary class. The 14-token plan covers the one V-permitted type
and all thirteen V-forbidden types while the family remains exactly 15/20.

Duplicate contract types, contract/digest mismatch, global final-V mismatch,
and stray not-attempted V remain in their existing families. A future multi-
predicate fixture is intended to be assigned to its lowest-numbered primary
class and reused only non-additively. This planned family is exactly 15/20.

#### Focused lease-acquisition evidence-chain vectors

These vectors define normative planned fixture classes. `primaryOwner` denotes
the intended attribution for a future serialized fixture; the primary ID named
below is also its intended owner. Executable fixtures and a fixture manifest
have not been implemented. This documentation establishes identifiers,
predicates, and planned boundaries only; it does not establish that serialized
payloads exist or that future manifest ownership uniqueness has already been
mechanically verified.

The six planned positive primary predicates are exactly:

1. **AI-P01 — complete all-passed GTypes:** every issued path has all five G
   types and every actual G passed, with lease/no-lease variants;
2. **AI-P02 — repeated all-passed G:** one G type appears more than once and
   every member is passed, with each of the five types as a non-additive
   variant;
3. **AI-P03 — lease-required attempted:** complete
   `G/A/R/I/P/E/V/L/F` issued chain with one profile-valid associated Source,
   exact source-to-root digest copy, source/root/A identity, compact A/R
   references, and every L bound to that same identity;
4. **AI-P04 — lease-required non-attempted:** complete
   `G/A/R/I/[P]/L/F` chain with E and V empty and the same
   Source/root/A/R/every-L binding;
5. **AI-P05 — no-lease attempted:** complete `G/N/I/P/E/V/F` chain with A,
   R, and L empty; and
6. **AI-P06 — no-lease non-attempted:** complete `G/N/I/[P]/F` chain with E,
   V, A, R, and L empty.

The twenty-eight planned negative primary predicates are exactly:

1. **AI-N01 — missing mandatory G type:** each omitted type is a non-additive
   variant;
2. **AI-N02 — any G non-passed:** failed and indeterminate outcomes, every G
   type, and an earlier bad G followed by a later passed same-type G are
   non-additive variants of the all-G-passed violation;
3. **AI-N03 — missing A** on a lease-required issued receipt;
4. **AI-N04 — duplicate A**;
5. **AI-N05 — missing R** on a lease-required issued receipt;
6. **AI-N06 — duplicate R**;
7. **AI-N07 — missing N** on a no-lease issued receipt;
8. **AI-N08 — duplicate N**;
9. **AI-N09 — missing universal I**, with both issued path variants;
10. **AI-N10 — duplicate I**, with both issued path variants;
11. **AI-N11 — non-passed singleton A/R/N/I:** each applicable type and both
    failed and indeterminate outcomes are non-additive variants;
12. **AI-N12 — N on a lease-required path**;
13. **AI-N13 — R on a no-lease path**;
14. **AI-N14 — A on a no-lease path**;
15. **AI-N15 — G after the applicable A/N boundary:** both paths and all five
    G types are non-additive one-bad-member variants;
16. **AI-N16 — A after R** by sequence;
17. **AI-N17 — applicable R/N after I** by sequence;
18. **AI-N18 — I after an earlier P** by sequence, including a later valid P
    that cannot repair the universal violation;
19. **AI-N19 — conditional issued-root presence/absence violation:** the root
    is missing on a lease-required issued receipt or present on a no-lease
    issued receipt or pre-contract denial;
20. **AI-N20 — R acquisition-reference mismatch:** singleton passed R lacks the
    compact reference or names a `checkId` different from the issued root and
    singleton passed A;
21. **AI-N21 — receipt/source task-identity mismatch (`primaryOwner:
    AI-N21`):** `ExecutionReceipt.spec.taskId` differs from the associated
    `LeaseAcquisitionResultIdentity.taskId`; different valid UUID values are
    mandatory non-additive variants;
22. **AI-N22 — associated-source cardinality violation (`primaryOwner:
    AI-N22`):** a lease-required issued receipt does not have exactly one
    associated `LeaseAcquisitionResultIdentity`; missing source and multiple
    ambiguous sources are mandatory non-additive variants;
23. **AI-N23 — A acquisition-reference mismatch (`primaryOwner: AI-N23`):**
    singleton passed A lacks the compact reference or names a `checkId`
    different from the issued root and source identity;
24. **AI-N24 — source/root check-identity mismatch (`primaryOwner: AI-N24`):**
    the associated source `checkId` differs from
    `ExecutionReceipt.spec.leaseAcquisitionEvidence.checkId`; different valid
    `checkIdentifier` values are mandatory non-additive variants;
25. **AI-N25 — source/A check-identity mismatch (`primaryOwner: AI-N25`):**
    the associated source `checkId` does not identify singleton passed A. A
    source and root that agree with each other but identify a different valid
    check from A are a mandatory non-additive variant;
26. **AI-N26 — source/root lease-identity mismatch (`primaryOwner: AI-N26`):**
    the associated source `leaseId` differs from
    `ExecutionReceipt.spec.leaseAcquisitionEvidence.leaseId`; different valid
    UUID values are mandatory non-additive variants;
27. **AI-N27 — associated-source digest-computation failure (`primaryOwner:
    AI-N27`):** exactly one associated source has a syntactically valid tagged
    digest whose `profile.digest.issued-lease-acquisition-v1` recomputation
    from the closed source projection fails to match. A lexically malformed
    digest remains generic structural/digest ownership; and
28. **AI-N28 — source-to-receipt digest-copy mismatch (`primaryOwner:
    AI-N28`):** the source digest validates successfully, but
    `ExecutionReceipt.spec.leaseAcquisitionEvidence.acquisitionResultDigest`
    is a different syntactically valid tagged digest.

The seven primary witnesses are independent and no scenario is assigned to two
primary negatives. AI-N21 changes only the source `taskId`. AI-N24 keeps source
`checkId` equal to A while changing only the root `checkId`. AI-N25 keeps
source and root `checkId` equal while changing A's `checkId`. AI-N26 keeps the
source and referenced contract on one lease while changing only the root
`leaseId`; any cross-effect is non-additive, and receipt/contract negative 19
instead keeps source and root equal while both differ from the contract.
AI-N22 independently uses zero or two otherwise eligible associated sources.
AI-N27 keeps exactly one source and an exact root copy but uses a valid-shaped
source digest that fails recomputation. AI-N28 keeps a valid recomputed source
digest and changes only the receipt root to another valid-shaped digest.
Therefore AI-N21/N24/N25/N26 exercise four independent equalities, and
AI-N22/N27/N28 exercise three independent source/provenance predicates.

Sequence equality remains a generic contiguous-sequence fault. Permitted
timestamp equalities and the seven acquisition/issuance timestamp reversals are
non-additive CH variants. A no-lease `leaseId` remains a TaskContract truth-
table fault. Forbidden placement, unknown members, closed-shape faults, and UUID
or identifier lexical faults remain generic structural owners or mandatory
non-additive variants. Source/root presence on a no-lease or denial path,
substitution of the issued chain for the unchanged denial chain, and promotion
of indeterminate acquisition to a stable Source are mandatory conditional/union
rejections and add no primary. The planned acquisition/issuance inventory is
exactly 6 positive and 28 negative primary predicates. Contract/source/root
lease-ID mismatch is the independent nineteenth receipt/contract-binding
negative, not an AI primary.

#### Focused cumulative denial-prerequisite vectors

The nine planned positive primary predicates correspond one-for-one to the
closed denial checkpoints and the cumulative matrix above. Every positive has
an exact `controllerCheckId` binding, including exact mapped type,
greatest-sequence selection, failed/indeterminate outcome, `observedAt`, and
`reasonCodes`. DP-P08 and the acquired DP-P09 variant also have the exact
passed-A, lease-ID, and acquisition-result-digest binding; all non-acquired
variants forbid `acquisitionEvidenceRef`:

Every positive also requires every actual member of `Prereq(r)` passed and
before the controller, all unreached ordinary types empty, and no ordinary
check after the controller. Only applicable acquired cleanup L and then F, or
F alone, may follow.

1. **DP-P01 — intent denial:** controlling failed/indeterminate intent check,
   no fabricated prerequisite or future stage, and F;
2. **DP-P02 — project/domain denial:** passed intent evidence, controlling
   project/domain failure or indeterminacy, no future stage, and F;
3. **DP-P03 — role-routing denial:** passed intent and project/domain evidence,
   controlling routing failure or indeterminacy, no future stage, and F;
4. **DP-P04 — host-binding denial:** the three earlier G types passed,
   controlling host failure or indeterminacy, no future stage, and F;
5. **DP-P05 — initial-preflight denial:** the four earlier G types passed,
   controlling preflight failure or indeterminacy, no future stage, and F;
6. **DP-P06 — N denial:** all five G types present and all actual G passed,
   controlling N failed/indeterminate, no A/R/I/P/E/V/L, and F;
7. **DP-P07 — acquisition denial:** all five G types present and passed,
   controlling A failed/indeterminate, no stable acquired identity or later
   stage, applicable warning, and F;
8. **DP-P08 — acquired R denial:** all five G types passed, singleton passed A,
   selected by the exact acquisition-evidence reference and matching the
   acquired lease identity/digest, with controlling R failed/indeterminate, no
   I/P/E/V, ownership-checked L cleanup, and F; and
9. **DP-P09 — issuance denial:** all five G types passed, the applicable passed
   A/R or N path, controlling I failed/indeterminate, no P/E/V, applicable
   cleanup, acquired-reference binding exactly on the acquired variant and
   reference absence on the no-lease variant, and F.

Across all nine checkpoint positives, mandatory non-additive controller-history
variants include `passed -> failed`, `passed -> indeterminate`, `passed ->
passed -> failed`, and `passed -> passed -> indeterminate`.

The six planned negative primary predicates are exactly:

1. **DP-N01 — missing cumulative prerequisite:** one stage known to have
   completed before the denial is absent from checks;
2. **DP-N02 — denial-stage boundary violation:** the row-level predicate
   requiring every prerequisite-stage observation before the controller,
   every unreached ordinary type empty, and no ordinary check after the
   controller is false. Variant A is unreached future-stage evidence anywhere;
   Variant B is a prerequisite re-observation or other ordinary check after
   the controller;
3. **DP-N03 — wrong controller/checkpoint/outcome:** the selected checkpoint
   maps to the wrong controlling check type, its mapped check set is empty, or
   its greatest-sequence controller is passed; each checkpoint, wrong-type,
   failed/indeterminate, and wrong-checkpoint form is a non-additive variant;
4. **DP-N04 — controller reference/binding mismatch:** `controllerCheckId` is
   missing, unknown, references an earlier same-type or otherwise non-greatest
   member, references a wrong-type member, or disagrees on exact `observedAt`
   or canonical `reasonCodes`; reason-code reorder, extra, missing,
   same-type-later-member, and check-reorder forms are non-additive variants;
   and
5. **DP-N05 — acquired evidence reference/identity mismatch:** the reference is
   missing on an acquired denial, present on any non-acquired state, selects
   the wrong A, a failed/indeterminate A, or a non-A check, or disagrees with
   the acquired origin's exact `leaseId` or `acquisitionResultDigest`; and
6. **DP-N06 — non-passed same-type observation before the referenced
   controller:** `failed -> failed`, `failed -> indeterminate`,
   `indeterminate -> failed`, and `indeterminate -> indeterminate` are
   mandatory non-additive variants.

Checkpoint, state, controller-ID, member-order, timestamp, reason-code,
acquisition-reference, lease-identity, and digest choices are mandatory
non-additive variants of their named primary predicate. Both DP-N02 variants
belong to its single row-level sequence/membership predicate; they add neither
a seventh negative primary nor a timestamp edge. Missing or malformed
cleanup/F, warning, and top-level release mapping remain RF-owned; chronology
reversals remain CH-owned. `failed -> passed` and `indeterminate -> passed`
remain mandatory non-additive DP-N03 variants because the greatest controller
is passed. Only the four non-passed-to-non-passed same-type histories belong to
DP-N06, and the documented passed histories remain positive. Exact
controller/evidence timestamp equality is DP positive binding coverage and
mismatch is DP-N04. The planned denial-prerequisite inventory remains exactly
9 positive and 6 negative primary predicates.

#### Focused lease-release and receipt-finalization vectors

Every positive primary requires `sanitization.applied: true`; a
`redactionCount` of zero is a mandatory valid variant.

The eleven planned positive primary predicates are exactly:

1. **RF-P01 — lease attempted, final L passed:** release succeeded,
   sanitization completed, and terminal F passed;
2. **RF-P02 — final L failed:** release failed, the exact final-L warning,
   sanitization completed, and terminal F passed;
3. **RF-P03 — final L indeterminate:** release indeterminate, the exact final-L
   warning, sanitization completed, and terminal F passed;
4. **RF-P04 — multiple L:** an earlier failed or indeterminate L followed by
   final passed L and succeeded release;
5. **RF-P05 — complete issued pre-release set:** all eleven possible lease-path
   pre-release check types precede every L, sanitization, and F;
6. **RF-P06 — acquired denial:** complete cumulative `G/A/R/L/F` denial path
   with failed/indeterminate controlling R and valid cleanup;
7. **RF-P07 — lease-required non-attempted:** complete prefix and `L/F`, with E
   and V empty;
8. **RF-P08 — no-lease attempted:** complete `G/N/I/P/E/V/F`, with L empty;
9. **RF-P09 — no-lease non-attempted:** complete `G/N/I/[P]/F`, with E, V,
   and L empty;
10. **RF-P10 — other conclusive denial:** passed F with L empty for every
    applicable `not-required`, `not-attempted`, and `not-acquired` checkpoint
    variant; and
11. **RF-P11 — indeterminate acquisition:** no stable identity, required
    warning, L empty, indeterminate outcomes, sanitization, and passed F.

The fourteen planned negative primary predicates are exactly:

1. **RF-N01 — missing L on a release-required path:** issued and acquired-
   denial origins are non-additive variants;
2. **RF-N02 — finalL/top-level mismatch:** all off-diagonal value pairs are
   non-additive variants with otherwise-correct warning evidence;
3. **RF-N03 — missing universal F:** every receipt origin/path is a non-
   additive variant;
4. **RF-N04 — duplicate F**;
5. **RF-N05 — non-passed singleton F:** failed and indeterminate variants;
6. **RF-N06 — non-terminal F / non-F after F by sequence:** the two
   descriptions are one wire predicate under singleton F and contiguous
   sequence;
7. **RF-N07 — issued pre-release check after L by sequence**;
8. **RF-N08 — acquired-denial Dpre after L by sequence**;
9. **RF-N09 — L on a no-release path:** all no-lease and non-acquired denial
   states are non-additive variants; and
10. **RF-N10 — final-L warning absent or wrongly referenced:** failed and
    indeterminate final-L and absent/wrong-check warning variants; and
11. **RF-N11 — forbidden post-sanitization F content:** F contains
    `expectedSummary`, `observedSummary`, both summaries, or another
    forbidden free-form member such as `sanitizedSummary`, `detail`, or
    `payload` or an unknown member; each forbidden-member presence form is a
    non-additive variant with intended `primaryOwner: RF-N11`; and
12. **RF-N12 — primitive finalization exact-tuple violation:** wrong F
    `checkId`, wrong F `profileId`, non-empty F `reasonCodes`, and
    regex-valid secret-like F check/profile/reason alternatives are mandatory
    non-additive variants of one exact-F-tuple predicate with intended
    `primaryOwner: RF-N12`; and
13. **RF-N13 — issued every-L acquisition-reference violation:** at least one
    lease-required issued L lacks the compact reference or names a different
    source/root/A `checkId`. An earlier bad L followed by a correctly bound
    finalL is a mandatory non-additive variant; and
14. **RF-N14 — incomplete sanitization applied flag:** an otherwise-valid
    serialized receipt has `sanitization.applied: false` while retaining the
    otherwise-correct singleton F fields, including outcome passed, sequence,
    Boolean shape, redaction count, digest projection, and delivery-independent
    state; the false flag means that F is not accepted as a valid terminal F.
    Zero and
    positive redaction counts are mandatory non-additive variants.

A non-F use of `check.receipt-finalization` cannot be an independently
isolated RF-N12 specimen because every valid receipt already contains the
mandatory F with that exact ID. The malformed non-F case is a generic
receipt-wide duplicate-`checkId` rejection, derived and non-additive. The RF
inventory is therefore exactly 11 positive and 13 negative primaries.

F-before-sanitization, F-after-finish, a non-F check after sanitization, denial
evidence after sanitization, and the four release-related timestamp reversals
are CH-owned and cross-referenced here without another primary count.
`postconditionRef` on F remains PB-N12-owned and is a non-additive
cross-reference here. Stable identity on indeterminate acquisition remains a
closed-union fault. The planned release/finalization inventory is exactly 11
positive and 14 negative primary predicates. AI plus RF therefore contains 59
planned primary predicates.

Across AI, DP, RF, CH, and the existing PB family, every primary predicate has
one unique planned ID and that same ID is its intended `primaryOwner`. Origin,
value, check-type, warning-form, equality, and later-valid-member variants are
mandatory but non-additive. Generic array defects remain generic-array-owned;
derived chronology relations own no primary fixture. This is a documentation
consistency model, not executable fixture or manifest verification.
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
greatest-sequence selection or sequence comparisons as timestamp chronology.
Tests also MUST NOT require E or V members to form contiguous type regions.
Phase 1 checks internal claims only. Phase 4 owns trusted time, authenticity,
actual immediacy, evidence truth, and operational freshness.

The universal twelve-step pipeline remains byte-identical. The digest catalog
now has fourteen field paths, eleven computations, and three exact copies. The
`profile.digest.issued-lease-acquisition-v1` projection and golden belong to
the AP-1 source and remain distinct from the unchanged acquired-denial profile;
its source computation precedes the exact receipt-root copy, LB-2 binding, and
the containing receipt digest. The other ten computation profiles/results and
their non-receipt golden bytes remain unchanged.

The source vector has an exact 163-byte non-digest projection and a 234-byte
completed closed `LeaseAcquisitionResultIdentity`. Independent runtime-only
Python, Node, and PowerShell/.NET extraction reproduces
`sha256:c99b362ffd7200478eddc317427976e7d8cc60f4174110c6f4ef3d27e9f25ac6`.
The associated receipt-root vector copies that tagged value exactly and adds no
computation; a different root digest is an independent exact-copy rejection.

The no-lease successful golden has the complete lifecycle sequence:

```text
0  intent-validation                   passed
1  project-domain-resolution           passed
2  role-routing                        passed
3  host-binding                        passed
4  initial-preflight                   passed
5  pre-issuance-revalidation           passed
6  contract-issuance                   passed
7  pre-action-revalidation             passed
8  execution                           succeeded
9  post-execution-verification         passed
10 receipt-finalization                passed
```

V at sequence 9 retains exactly
`postconditionRef: {"type":"scope-contained"}`. A, R, L, lease identity, and
every acquisition claim remain empty; the AP-1 source, issued root, and compact
references are absent. `startedAt`, G0-4, N5, and contract `freshness.issuedAt` are at
`2000-01-01T00:00:00Z`; I6 and P7 retain the next second. This proves the
RS-1 no-lease bracket without requiring either equality. F at sequence 10 is
inside the digest projection and means evidence closure only.

The projection is exactly 3337 bytes and the completed value is exactly 3427
bytes. Independent runtime-only Python, Node, and PowerShell/.NET extraction of
the actual Markdown fences reproduces
`sha256:d3cc668ea95fa385392f04b4e5580cd2fdc810835ae7fd1ab285c102777402b0`.
The delivery result copies that tagged value exactly rather than computing a
new digest.

The authoritative PG-1 broad region in the design begins inclusively at exact
heading `### Complete digest-profile catalog` and ends exclusively at exact
heading `## 11. Complete array-ordering matrix`. W is the unmodified on-disk
byte slice; B performs only CRLF-to-LF replacement. The prior values W =
35334 bytes / 271 CRLF /
`a4f80b731f4b6c9ee8ee4ec621350f85dc24ff694c2c4b47fa10902a8ed9b88d`
and B = 35063 bytes / 271 LF /
`75c200b287b770c418218ea34ed98a800a4a229ea536109ff0f764f449a3e2a7`
are historical and superseded. The intermediate RS-1/LB-2 pre-AP-1
attestation is also historical and superseded:

```text
PG-1 W = 37326 bytes / 295 CRLF / e6cd8deb426a509a2ade0c4df48f2bf7c6e148afed02d3ce697faeb910318251
PG-1 B = 37031 bytes / 295 LF / 8d8b0aee8b93559690d530402761347fba0aa222962ef11b99d42caf1262c432
```

The current AP-1 external attestation, independently reproduced with Python,
Node, and PowerShell/.NET, is exactly:

```text
PG-1 W = 38914 bytes / 313 CRLF / cbe0ed9ad14919f5acfef5edba978233ce57d679644e22179dc591d5c2edd9ad
PG-1 B = 38601 bytes / 313 LF / 719899f43c6f8c0908d7b6887a720960d010aab98e99fc254031da7b2e404b58
```

The recount includes all prose, tables, and JSON examples in that broad region.
It contains 5 distinct timestamp values across 38 occurrences, 7 structured-
remote object occurrences, 34 tagged-digest occurrences representing 13
distinct values, and 3 `profile.digest.execution-receipt-v1` tagged-value
occurrences. Those three are exactly the completed `ExecutionReceipt`, the
`ReceiptDeliveryResult` exact copy, and the `Recalculated golden results`
table entry; the receipt digest projection contains zero `receiptDigest`
members. The attestation is outside the exclusive boundary; no receipt-only
subregion replaces or narrows PG-1.

### Portable repository-relative path coverage

Future strict-decoder and static coverage MUST require strict UTF-8 and an
already-NFC value before applying the POSIX relative-path grammar. It MUST
reject, without normalization, case folding, aliasing, or repair, any exact
case-sensitive `.git` component at any depth. Exact invalid path vectors are
`.git`, `.git/config`, `.git/hooks/pre-commit`,
`.git/worktrees/example/HEAD`, `foo/.git`, `foo/.git/config`, and
`nested/repository/.git/HEAD`. Exact valid similar-name vectors are
`.gitignore`, `.gitmodules`, `.github`, `foo.git`, `dir/.gitignore`, and
`dir/.github/workflow.yml`.

Pattern coverage retains anchored segment-local `*` and `?` plus
complete-segment `**`, all over the revised valid path universe `U`. Exact
invalid literal-component patterns are `.git/**`, `.git/config`,
`foo/.git/**`, and `foo/.git/config`. `**` itself is valid and MUST be proved
unable to match a reserved path because reserved paths are outside `U`.

The vector matrix MUST apply the same rule to Domain and role-derived scope,
HostOverlay ceilings and D10 automata inclusion, RoutingPolicy/static
inclusion, TaskContract authorized and prohibited scopes, baseline and
postcondition paths, all five path-keyed transition branches, receipt
`changedPaths`, and `scope-contained` verification. `modify` plus `**` and
Git-administration capability tokens MUST NOT authorize direct `.git/config`,
hook, ref, or other administrative-path mutation. A runtime-resolved
administrative effect cannot be reported as a successful ordinary changed path
or silently omitted; `scope-contained` must be failed or indeterminate.

For a complete issued receipt and referenced TaskContract `C`, tests define
`Apath` as the union of `C.spec.authorizedScope.paths` languages and `Qpath` as
the union of `C.spec.prohibitedScope.paths` languages. For every changed path
`x`, a passed writing scope claim requires `x` in `Apath` and `x` not in
`Qpath`; prohibited membership overrides authorized membership. Passed
verification also requires passed, exactly referenced
`finalV("scope-contained")`. One bad member invalidates the passed claim,
requires failed or indeterminate verification, forbids a succeeded lifecycle,
and remains in the receipt as audit evidence. Tests MUST
reject silent dropping, sanitizing, normalizing, or rewriting of an offending
path. Empty writing results satisfy membership vacuously but retain every
completeness and evidence requirement.

The five focused positive scope classes are exactly:

1. one authorized, non-prohibited changed path;
2. multiple changed paths, all authorized and non-prohibited;
3. an empty writing result with complete passed no-effect evidence;
4. offending paths retained with failed verification and a non-succeeded
   lifecycle; and
5. offending paths retained with indeterminate verification and a
   non-succeeded lifecycle.

The six dedicated negative scope classes are exactly:

1. a valid ordinary path outside every authorized language with passed
   verification;
2. a path in both authorized and prohibited languages with passed verification;
3. a prohibited-only path with passed verification;
4. multiple paths with one unauthorized member and passed verification;
5. any scope violation with `lifecycleOutcome: succeeded`; and
6. passed verification without passed, exactly referenced
   `finalV("scope-contained")` evidence.

The non-writing/non-empty-changed-path invalid case remains in D5. It is a
required cross-reference but does not add a seventh dedicated scope negative.

Phase 3 vectors retain live resolution for top-level `.git` indirection,
linked and common Git directories, administrative locations outside the
worktree root, symlink, junction, reparse-point and other aliases, case-folded,
Windows 8.3, and Unicode-normalized aliases, registered-submodule
administrative roots, and nested-repository administrative roots. Each
unresolved or aliased boundary fails closed, and portable expected values never
contain the resolved host path.

### Canonical structured-remote coverage

Future Schema and static tests MUST enforce the closed record with required
`transport`, `host`, `namespace`, and `repository`, optional `port`, and
no other field. Transport is exactly `https` or `ssh`. No raw URL, user-info,
credential, token, password, private-key material, query, fragment, URI scheme,
or environment-derived secret material is representable.

The named `remoteDnsHost` permits only lower-case ASCII DNS names from 3
through 253 characters with at least two labels. Each 1-through-63 character
label matches:

```text
[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?
```

Tests reject empty, leading, trailing, or repeated-dot labels; leading/trailing
label hyphens; underscore, uppercase, whitespace, controls, Unicode, `xn--`,
IDNA conversion, IP literals, brackets, zone identifiers, a single label, and
`localhost`. They neither normalize nor case-fold. `repo.invalid` remains
valid without implying reachability, DNS truth, ownership, or security.

The default table is exactly `https -> 443` and `ssh -> 22`. Omitted `port`
means that default, while explicit HTTPS 443 or SSH 22 is invalid. A non-default
endpoint includes its integer port from 1 through 65535 under the existing
numeric profile. Validators do not add or remove a port.

`namespace` is an ordered array of 1 through 16 lower-case ASCII segments,
each 1 through 63 characters and with joined slash-separated length at most
1023. Every segment matches:

```text
[a-z0-9](?:[a-z0-9._-]{0,61}[a-z0-9])?
```

Empty, `.`, `..`, or `..`-containing segments; slash, backslash, whitespace,
controls, uppercase, and Unicode reject. Segment order is significant; no
sorting, normalization, path decoding, or separator inference occurs. A
`.git` substring in a valid namespace segment remains literal.

The distinct `remoteRepositoryName` is one lower-case ASCII segment from 1
through 128 characters, with alphanumeric endpoints and internal
`[a-z0-9._-]`. Tests reject empty, separators, whitespace, controls,
uppercase, Unicode, leading/trailing dot or hyphen, any `..` substring, `.`,
`..`, and a terminal lower-case `.git` suffix. They do not normalize, parse
as a path, strip or append `.git`, or alias suffixed and unsuffixed names.

After complete validation, identity is exact `J(remote)`, equivalently exact
transport, host, effective port, ordered namespace, and repository. Explicit
defaults remain invalid. `acceptedRemotes` is set-like, rejects duplicate
`J(remote)`, and must already be strictly ordered by `J(remote)`. The outer
record remains uniquely keyed and ordered only by `remoteName`. HostOverlay
narrowing requires exact validated membership and cannot ignore a field,
compare an alias, or widen the set.

Positive vectors MUST cover:

1. HTTPS with omitted default port;
2. SSH with omitted default port;
3. HTTPS with a valid non-default port;
4. SSH with a valid non-default port;
5. a minimum valid two-label DNS host;
6. a maximum-length valid host;
7. a one-segment namespace;
8. a multi-segment namespace;
9. minimum-length namespace and repository segments;
10. maximum-length namespace and repository values;
11. exact equality of two identical canonical remote records;
12. inequality from one changed field;
13. multiple accepted remotes under one `remoteName`;
14. canonical `acceptedRemotes` ordering; and
15. the unchanged protected remote
    `{"host":"repo.invalid","namespace":["synthetic"],"repository":"governance","transport":"https"}`.

Independent negative vectors MUST reject:

1. missing `transport`;
2. missing `host`;
3. missing `namespace`;
4. missing `repository`;
5. an unknown field;
6. an unsupported transport;
7. a raw URL in a field;
8. user-info;
9. credential or token material;
10. an uppercase host;
11. a single-label host;
12. `localhost`;
13. a trailing dot;
14. a leading dot;
15. a repeated dot;
16. an empty DNS label;
17. a leading hyphen in a label;
18. a trailing hyphen in a label;
19. an underscore in a host label;
20. an `xn--` label;
21. a Unicode host;
22. an IPv4 literal;
23. an IPv6 literal;
24. bracketed IPv6;
25. port zero;
26. a port above 65535;
27. a negative port;
28. a string port;
29. a fractional port;
30. explicit HTTPS port 443;
31. explicit SSH port 22;
32. an empty namespace array;
33. more than 16 namespace segments;
34. an empty namespace segment;
35. a namespace segment over 63 characters;
36. a joined namespace over 1023 characters;
37. namespace segment `.`;
38. namespace segment `..`;
39. a namespace `..` substring;
40. a slash in a namespace segment;
41. a backslash in a namespace segment;
42. an uppercase namespace;
43. a Unicode namespace;
44. an empty repository;
45. a repository over 128 characters;
46. a leading repository dot;
47. a trailing repository dot;
48. a leading repository hyphen;
49. a trailing repository hyphen;
50. a repository `..` substring;
51. a slash in the repository;
52. a backslash in the repository;
53. an uppercase repository;
54. a Unicode repository;
55. a terminal `.git` suffix;
56. a duplicate canonical remote;
57. non-canonical `acceptedRemotes` ordering;
58. a duplicate outer `remoteName`;
59. the same endpoint attempted through explicit default-port spelling;
60. HostOverlay acceptance on one runtime through an alias rejected by another;
    and
61. attempted widening by ignoring one remote field.

Phase 1 owns these lexical, closed-shape, canonicality, equality, uniqueness,
ordering, and static-membership checks. Future `model-implementation` owns
strict decoding and executable conformance. Phase 3 owns live Git-remote
observation, transport parsing, repository comparison, and runtime host facts.
Phase 4 owns trusted authority and contract/evidence lifecycle. Canonical remote
identity proves neither network ownership nor trust.

### Path-keyed baseline and postcondition entries

Future Phase 1 static and contract tests MUST prove that the repository-relative path is the sole identity, uniqueness, and canonical ordering key, `S(entry.path)`, for `TaskContract` baseline index, tracked, and submodule entry arrays and every corresponding entry array nested in required postconditions. Two entries with the same path MUST be rejected even when their remaining fields differ, including index mode, stage, object identity, or other index-entry state; tracked object identity, mode, status, or other tracked-entry state; submodule object ID, checkout, or observation contents; or required-postcondition entry contents.

`J(entry)` MAY be used only for deterministic diagnostic comparison after path uniqueness is established. It MUST NOT participate in entry identity, uniqueness, or canonical ordering, and differing full-object bytes MUST NOT make duplicate paths valid.

Tests MUST prove that duplicate-path rejection occurs after strict parsing and applicable structural validation, during Phase 1 static validation, and before canonical digest projection, RFC 8785 JCS serialization, and hashing. A duplicate path MUST NOT reach hashing as a valid instance.

Planned negative coverage MUST include:

- duplicate baseline index path with different entry contents;
- duplicate baseline tracked path with different entry contents;
- duplicate baseline submodule path with different object IDs, checkout, or
  observation contents; and
- duplicate nested required-postcondition entry path with different contents.

Untracked and ignored path arrays MUST remain unique and canonically ordered by `S(path)`. Path arrays nested in postconditions MUST retain their applicable `S(path)` rule. This test-plan synchronization does not change the design record's [array-ordering contract](../docs/schema-contract-v1alpha1.md#11-complete-array-ordering-matrix).

### Current conformance coverage

Future Schema and static-contract coverage MUST implement every row of the
design record's [mandatory exhaustive fixture/conformance
matrix](../docs/schema-contract-v1alpha1.md#mandatory-exhaustive-sg-001-fixtureconformance-matrix).
Prior approval and third-review repair history remain recorded externally and
at commit `9eac3e040a8d0f9c959eeb675eace795749e422a`. This section records design-only,
non-executable current conformance coverage requirements for the retained
prior-review repairs. The current review status is stated above;
this test plan neither proves nor replaces external audit, GitHub, or
authorization records. Matrix coverage remains planned: no validator, fixture,
executable test, or Schema implementation exists, and the toolchain and
separately authorized implementation gates remain blocking.

### F-01–F-12 semantic-closure coverage

Future conformance coverage MUST exercise every D1–D12 contract recorded in
the design, while preserving its assigned phase and ownership boundary:

- **D1:** `schema-contracts` specifies the internal immutable validated
  canonical-instance contract and vectors; future `model-implementation`
  constructs it only after strict parse, Schema, static-invariant, and array
  checks, binds proof to original bytes or the same-process value, rejects a
  generic decoded object, and never treats it as a public kind, TaskContract,
  or authority.
- **D2:** cover absent/unavailable, uninitialized/unavailable, and
  initialized/observed with all eight Boolean triples, checkout commit
  difference, every forbidden pairing, all four denial codes, and unchanged
  reuse through transitions and postconditions.
- **D3:** exercise the sole eleven-step recursive leaf-only untracked/ignored
  inventory, complete ignore precedence and negation, submodule and nested-repo
  boundaries, `S(path)` order, require every repository-relative path to
  satisfy the revised `repositoryRelativePath` profile, strict UTF-8,
  already-NFC, and exact `.git`-component rejection, cover the exact valid and
  invalid similar-name vectors, and cover every fail-closed administrative-root
  and alias observation class.
- **D4:** reproduce the fixed raw regular, executable, and link-target byte
  digests without filters, decoding, normalization, or dereference, and reject
  unstable, unreadable, replaced, truncated, or unsupported objects.
- **D5:** require exactly empty transitions, baseline-equal state
  postconditions, no lease, and empty issued-receipt changed paths for all three
  non-writing rows; cover exactly 21 Cartesian negatives, `3 × 7`, across
  the seven permitted transition branches; cross-reference, without
  duplicating, the non-empty changed-path invalid case from scope coverage.
- **D6:** enforce `verificationOutcome: not-performed` if and only if
  `executionOutcome: not-attempted`, cover every allowed pair and all seven
  invalid pairs, then apply EF-1 execution terminality, final E/global V, per-type final V, and final L
  bindings, finalG, exact applicable A/R/N/I, universal terminal F,
  L/finalL/warning, and not-attempted E/V plus no-release L-empty gates before
  lifecycle precedence.
- **D7:** bind each `from` directly to the complete nine-dimension
  baseline, apply only the seven unique permitted transitions simultaneously,
  reconstruct and validate one nine-dimension final composite with active
  operations and administrative locks both still none, require exact
  changed-dimension postconditions, and allow only none-valued active-operation
  and administrative-lock postconditions.
- **D8:** require exactly the unchanged five closed HostOverlay binding fields,
  canonical non-empty `remoteNames`, exact ref-branch conditions, name
  resolution, rejection of `expectedBranch` or any cached observation field,
  global `worktreeId` and exact-root exclusivity, and static coordination-root
  exclusion using the exact strict-descendant comparator; cover all four HX
  positives and ten HX negatives without changing binding ordering; Phase 3
  owns canonical physical-worktree injectivity, live containment, and
  fail-closed ambiguity.
- **D9:** record all six positive and twelve negative complete-set routing
  vectors, `Drule`/`Dresolved`/`Owned(R)` semantics, no-fallthrough and no-union
  behavior, split independence, and exact-duplicate precedence; future
  `model-implementation` compares exact RFC 8785 JCS bytes of `RuleProjection`
  and `MatchProjection` with no digest, case folding, rewriting, inference,
  host transformation, or array reordering; Phase 2 alone resolves and routes.
- **D10:** prove Project/role identity, exact capability equations, repository
  and remote inclusion, binding-name resolution, and path-language inclusion
  with deterministic automata over revised `U`; reject each literal `.git`
  component pattern, prove broad `**` excludes reserved paths, reject widening
  and every unavailable proof;
  and prove HostOverlay, availability, branch, or lease state cannot make an
  incomplete selected role eligible.
- **D11:** `schema-contracts` catalogs fourteen digest field paths bound once
  to eleven computations and three exact-copy paths, plus the acyclic dependency
  graph, framing, projections, completed values, recorded bytes/digests, and
  expected vectors. Every public selector resolves to a valid branch in its
  closed union; the non-public AP-1 source path is not a resource selector. The
  acquired computation selector is exactly
  `ExecutionReceipt.spec.origin[type=pre-contract-denial].leaseAcquisition[state=acquired].acquisitionResultDigest`;
  the acquired exact-copy selector is exactly
  `ExecutionReceipt.spec.origin[type=pre-contract-denial].preContractEvidence.acquisitionEvidenceRef.acquisitionResultDigest`;
  the issued source computation path is exactly
  `LeaseAcquisitionResultIdentity.acquisitionResultDigest`; the issued receipt
  exact-copy selector is exactly
  `ExecutionReceipt.spec.leaseAcquisitionEvidence.acquisitionResultDigest`;
  and the invalid `leaseAcquisition` predicate `[type=acquired]` is rejected.
  The source projection is closed
  `{taskId, leaseAcquisitionEvidence:{checkId,leaseId}}`, excludes the source
  digest, and validates before the root exact copy, source/root/A/R/every-L
  identity chain, and contract lease binding. Future `model-implementation`
  constructs projections, JCS, hashes, exact copies, verification, and
  executable replay of every separator, raw/JCS payload, exclusion, completed
  value, tagged hash, negative vector, denial acquisition copy, issued-source
  computation, receipt-root copy, delivery copy, and cross-runtime result.
  Phase 3 produces the acquisition result/source identity; Phase 4 performs
  trusted provenance and operational replay.
- **D12:** verify the complete five-class capability partition and all four
  valid review-only permitted sets with exact prohibited-set complements, plus
  every non-observation, role, mode, overlap, complement, exclusive-write, and
  restoration negative.

`schema-contracts` specifies the D1–D12 contracts, structural/static checks over
already-decoded values, catalogs, and expected vectors. It does not implement
or executably prove strict decoding, validated-representation construction,
canonical serialization, projection, JCS, hashing, verification, replay, typed
round trips, Schema/model conformance, or cross-runtime reproduction. Those
codec/model tests belong to future `model-implementation` after the audit,
approval, integration, and distinct-worktree gates. Phase 2 retains routing,
Phase 3 retains live Git/branch/worktree/lease observation, and Phase 4 retains
trusted replay, issuer provenance, authority, receipt truth, and delivery.

The current invariant inventory is exact:

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
host-resource-exclusivity positives = 4
host-resource-exclusivity negatives = 10
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

Each planned range is continuous. Each primary ID is the intended
`primaryOwner` for a future serialized fixture. Variants are mandatory but non-
additive; derived chronology has no primary. Executable fixtures and a fixture
manifest have not been implemented, so these are documentation-consistency
counts rather than executable payload or manifest verification.

The PG-1 broad corpus has 5 distinct timestamp values across 38 occurrences, 7
structured-remote object occurrences, 34 tagged-digest occurrences representing
13 distinct values, and 3 `profile.digest.execution-receipt-v1` tagged-value
occurrences. Those are exactly the completed receipt, delivery exact copy, and
recalculated-results table entry; the projection has zero `receiptDigest`
members. Its exact W/B identities and inclusive/exclusive headings are recorded
above and must mirror the design and Schema README exactly.
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
  baseline, transition, postcondition, warning, check, outcome, V-only
  postcondition reference, issued LB-2 root and compact A/R/every-L reference,
  lease-acquisition, lease-release, and receipt-
  finalization branch;
- required `preContractEvidence.controllerCheckId` and
  `sanitizedSummary`, exact acquired-only `acquisitionEvidenceRef`
  presence/absence and binding, and `ReceiptDeliveryResult.sanitizedSummary`
  presence; warning and non-F check summaries retain their designed
  optionality, while F forbids every summary or payload field;
- the material pre-publication five-state lease-acquisition correction:
  `not-required`, `not-attempted`, `not-acquired`, `indeterminate`, and
  `acquired`; and
- the preserved `profile.number.v1alpha1-r1` numeric contract with Git index
  stage range exactly `0..0`, stage `0` valid, and stages `1` through `4`
  invalid.

### Retained fifth-review operation and lock coverage

Active-operation positives cover a none-only TaskContract baseline, an optional
none-only postcondition, all seven operation identities as non-authorizing live
observations, pre-contract denial evidence, post-contract/pre-action
`not-attempted/not-performed` evidence, and post-execution failed or
indeterminate evidence. The exact legacy contract family has 21 negatives:
seven single-operation exact baselines, seven retired active-operation
transitions, and seven single-operation exact postconditions. Duplicate,
unknown, non-canonical, and empty-exact observations form a separate generic
shape family. Multi-operation cases do not inflate the 21-case legacy family.

Administrative-lock TaskContract coverage now mirrors the retired
active-operation contract surface: a none-only baseline, an optional none-only
postcondition, and no permitted transition. Its exact legacy contract family
has 21 negatives: seven single-lock exact baselines, seven retired
administrative-lock transitions, and seven single-lock exact postconditions.
The reusable observation/evidence union still covers all seven lock identities
and retains separate duplicate-identity, missing-or-forbidden-field,
non-canonical-order, unknown-identity, and empty-exact generic shape negatives.
A present live Git administrative lock still denies at the governing guard
checkpoint and remains distinct from runtime leases, lease-store locks, and
command-internal transient locks.

At initial or pre-issuance revalidation, a non-empty active-operation or
administrative-lock observation denies before a contract exists and may be
retained in optional pre-contract evidence. At post-contract
immediately-before-action revalidation it permits no protected action and
requires an issued receipt to be `not-attempted/not-performed`. At
post-execution verification it is unexpected terminal evidence with failed or
indeterminate verification, never a successful postcondition.

### Closed runtime and numeric-profile conformance

Future Phase 1 Schema and static contract coverage MUST exercise the exact
closed runtime representations in the design record. Planned baseline classes cover
all nine required dimensions; conflict-free stage-0 clean, non-empty exact, and
empty exact index forms; every tracked and submodule branch; the none-only
TaskContract active-operation and administrative-lock dimensions; and rejection
of missing or unknown dimensions, branch-inapplicable fields, stage `1` through
`4`, unsupported index state, duplicate paths, and every single-identity exact
active-operation or administrative-lock baseline. Both reusable
observation/evidence unions retain all seven identities and their separate
malformed duplicate, order, unknown, and empty-exact negatives, including the
existing `L(lock)` identity and ordering rules.

Every one of the seven permitted-transition branches and all eleven
required-postcondition branches requires positive coverage. The optional
active-operation and administrative-lock postconditions are both none-only.
Negative coverage MUST reject identical `from`/`to`, missing target keys,
unknown transition types, both retired transition types, duplicate transition
targets, duplicate postcondition types, non-empty active-operation or
administrative-lock expectations, any exact `.git` component in a path-keyed
value, a successful scope claim that omits an administrative effect, and a
missing or repeated `scope-contained`.
Uniqueness is established before digest projection or hashing.

Receipt vectors cover warnings with and without optional fields, all 14 check
types, the exact 4/3 outcome conditional, V-only closed references, contiguous
sequences, unique IDs, ordered reason codes, and same-receipt warning links.
Planned issued-contract vectors cover all outcomes, all 24 primitive chronology
relations and 30 displayed consequences, the 8/37 pre-action, 8/22
final-E, 10/20 verification, and 5/6 scope families, plus 15/20 postcondition-
binding, rebuilt 6/28 acquisition/issuance, 9/6 cumulative-denial, and 11/14
release/finalization families. They cover EF-1 execution terminality, final P/E/V, per-type final V,
diagnostic finalG and final L selection; every G and every attempted P passed;
failed/indeterminate P same-lifecycle terminality with no later P/E/V and
not-attempted/not-performed outcomes; exact applicable
A/R/N/I; one source-profile-valid AP-1 identity, exact source-to-root digest
copy, source/root/A identity, compact A/R/every-L references, and
source/root/contract lease-ID equality; P/E/V presence; cumulative denial
all-member
prerequisite/controller ordering and stop-boundary membership; G/A, G/N, A/R,
R/checkpoint, N/checkpoint, checkpoint/issuedAt, derived R/issuedAt and
N/issuedAt, issuedAt/I, every-I/every-P, P/E/V, issued-pre-release/L,
acquired-Dpre/L, evidence/L, every-non-F/sanitization, sanitization/F, and
F/finish order; mandatory `sanitization.applied == true`; final
E/V/L mapping; scope; terminal exact-tuple F; warning linkage; not-attempted
E/V emptiness; and L emptiness on every no-release path. Planned pre-contract-
denial vectors cover every checkpoint/state pair, every actual prerequisite
before the controller, unreached-stage emptiness, the ordinary-stage
post-controller stop boundary, exact controller ID/type/greatest/outcome/time/
reason binding, acquired-only A/lease/digest binding, and acquired cleanup
outcome.
These are requirements, not claims of existing executable vectors.

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

The contract requires raw numeric-token validation and duplicate-key detection
during strict parsing before ordinary decoding, Schema validation, static
validation, array checks, validated-representation construction, digest
projection, JCS, or hashing. `schema-contracts` specifies the exact six-field
inventory, tokens, bounds, and expected vectors. Future
`model-implementation` owns executable rejection before conversion and MUST
prove no precision loss through parsing, representation construction, RFC 8785
JCS, or replay; reproduce identical digest vectors across supported runtimes;
combine official RFC 8785 vectors with project-specific numeric boundaries;
and reject a generic decoded object lacking complete representation proof.
Phase 4 verification requires raw-token replay or the complete trusted
representation proof. Validator research must prove this selected profile and
MUST NOT choose or weaken it. All coverage remains planned and unimplemented.

### Cross-finding validation-order coverage

The repairs MUST be tested as this effective application of the existing
universal pipeline and artifact dependency graph, not as a replacement
pipeline:

1. strict byte/token decoding prerequisites;
2. timestamp and structured-remote lexical validation;
3. JSON Schema structural validation;
4. local Phase 1 static invariants;
5. canonical-array and remote-order validation;
6. validated canonical representation construction;
7. digest projection and digest computation where applicable;
8. complete TaskContract digest verification;
9. issued receipt/TaskContract field equality plus AP-1 associated-source
   profile validation, source-to-root exact digest copy, and LB-2
   root/reference/lease binding;
10. all 24 primitive chronology comparisons and all 30 displayed consequences;
    final P/E/V, per-type final V, diagnostic finalG, and finalL selection;
    attempted P/E/V and per-type reference presence; final-P freshness; every
    actual G and every attempted P passed; failed/indeterminate P same-lifecycle
    terminality with no later P/E/V and not-attempted/not-performed outcomes;
    exact applicable A/R/N/I; cumulative denial all-member
    prerequisite/controller ordering, future-stage exclusion, and ordinary
    post-controller stop boundary; G/A, G/N, A/R, R/checkpoint, N/checkpoint,
    checkpoint/issuedAt, derived R/issuedAt and N/issuedAt, issuedAt/I,
    every-I/every-P,
    P/E/V, issued-pre-release/L, acquired-Dpre/L, evidence/L, every-non-F/
    sanitization, sanitization/F, and F/finish ordering; mandatory
    `sanitization.applied == true`; EF-1 execution terminality and final E/V/L binding;
    scope, terminal F, warning, L-empty, and outcome consistency;
11. receipt digest verification; and
12. delivery-result binding and chronology.

## Required failure scenarios

Future integration coverage MUST exercise this order:

1. receive untrusted task intent;
2. resolve exactly one `Project`;
3. resolve a non-empty deterministic set of `Domain` identifiers;
4. use the exact complete-set RoutingPolicy order above to select exactly one
   `WorktreeRole` that owns every resolved `Domain`, or deny without fallthrough;
5. resolve one local `HostOverlay` binding;
6. perform initial live preflight;
7. atomically acquire the task-owned write lease when required;
8. perform `post-acquisition-revalidation` after required acquisition, or the
   distinct `pre-issuance-revalidation` when no lease is required;
9. issue or validate a trusted, state-bound `TaskContract` that binds the same complete `Domain` set;
10. perform post-contract, immediately-before-action revalidation;
11. execute through an adapter;
12. perform post-execution scope and state verification;
13. capture pre-release evidence;
14. perform ownership-checked release;
15. bind `releaseOutcome` to final L, complete sanitization, record passed
    terminal F as finalization completion, and finalize the
    `ExecutionReceipt`; and
16. attempt receipt persistence or delivery outside portable governance.

The test suite MUST demonstrate fail-closed behavior for at least:

- missing, malformed, ambiguous, stale, or mismatched configuration or runtime
  state; unknown fields or API versions; forged contracts; and caller attempts
  to expand authority;
- zero or ambiguously resolved Domains, incomplete or collectively composed
  owners, routing fallthrough, wrong-role targets, HostOverlay widening, and
  plan-only/write contradictions;
- an unregistered or mismatched root, worktree, branch, HEAD, remote, Git state,
  operation, or administrative lock;
- each missing G type; any failed or indeterminate G; a failed/indeterminate G
  followed by a later same-type pass; missing/duplicate/non-passed or wrong-
  path A/R/N/I; every G/A/R/N/I/P sequence violation; a missing/invalid
  associated source; invalid source-profile digest; missing, forbidden,
  malformed, or misbound issued root; source/root digest-copy mismatch;
  receipt/source task mismatch; source/root/A check mismatch; source/root or
  source/contract lease mismatch; or a missing/mismatched compact A/R/every-L
  reference;
- every cumulative denial defect: missing completed prerequisite, fabricated
  future stage, origin/preContract/check disagreement, missing controlling
  check, passed controlling check, any non-passed same-type observation before
  the controller, later pass inconsistent with denial origin, N encoded as R,
  or acquired R denial without G/A/cleanup;
- drift after issuance, changes outside authorized scope, invalid receipt
  origins, and a receipt presented as authorization input;
- F missing, duplicate, non-passed, non-terminal, carrying a forbidden member,
  or using any non-exact identity tuple; generic duplicate-ID rejection of
  non-F use of the reserved F ID; F
  before sanitization; F after finish; any non-F check after sanitization; any
  denial evidence after sanitization; or delivery before finish;
- release-required L missing; finalL/top-level mismatch; failed/indeterminate
  finalL without the exact warning; Dpre after L; L on a no-release path;
  release failure with an unresolved lease; and receipt persistence/delivery
  failure; and
- secrets or machine-specific runtime data in diagnostics, planned payloads,
  golden files, logs, or receipts.

The active rejection matrix MUST independently exercise:

- each of the five missing G types;
- a failed G and an indeterminate G for every type, including each followed by
  a later same-type pass that cannot recover the receipt;
- for each attempted execution outcome, an earlier failed P and an earlier
  indeterminate P followed by a later passed P and E/V, proving that the same
  lifecycle cannot recover;
- one G after A and one G after N; A after R; R/N after I; and an earlier P
  before I despite a later valid P;
- N on a lease path, R or A on a no-lease path, missing/duplicate/non-passed
  A/R/N/I, and all applicable origin variants;
- RS-1 reversals for `startedAt/issuedAt`, R/checkpoint, N/checkpoint,
  checkpoint/issuedAt, and issuedAt/I, while also checking the derived direct
  R/issuedAt and N/issuedAt consequences;
- AI-N19 conditional issued-root presence/absence; unchanged AI-N20 R compact-
  reference mismatch; AI-N21 receipt/source task mismatch; AI-N22 missing or
  multiple associated sources; unchanged AI-N23 A compact-reference mismatch;
  AI-N24 source/root `checkId` mismatch; AI-N25 source/singleton-A `checkId`
  mismatch; AI-N26 source/root `leaseId` mismatch; AI-N27 exactly one
  associated source with a valid-shaped digest that fails recomputation; and
  AI-N28 a valid source digest plus a different syntactically valid receipt-
  root digest;
- source/root/reference presence on a no-lease path, use of the issued chain to
  rewrite a pre-contract denial, and promotion of indeterminate acquisition to
  a stable source identity, as mandatory non-additive conditional variants;
- DP-N01 missing prerequisite evidence for each checkpoint prefix;
- DP-N02 Variant A, an unreached future-stage check anywhere, and Variant B, a
  passed prerequisite re-observation or any other ordinary check after the
  controller, for every applicable checkpoint row;
- DP-N03 wrong controller/checkpoint/outcome, including empty mapped type,
  wrong mapped type or checkpoint, passed greatest-sequence controller, and
  both `failed -> passed` and `indeterminate -> passed` histories;
- DP-N04 controller reference/binding mismatch: missing or unknown ID, wrong
  type, earlier same-type or other non-greatest member, later same-type member,
  check reorder, `observedAt` mismatch, and reason-code mismatch, reorder,
  extra, or omission; and
- DP-N05 acquired evidence-reference/identity mismatch: missing acquired
  reference, reference on every non-acquired state, wrong A, failed or
  indeterminate A, non-A, wrong lease ID, and wrong acquisition-result digest;
- DP-N06 non-passed history before the referenced controller, with independent
  serialized variants for `failed -> failed`, `failed -> indeterminate`,
  `indeterminate -> failed`, and `indeterminate -> indeterminate`;
- N denial represented as acquired R, and acquired R denial missing any G, A,
  L, final-L mapping, or required warning;
- an unrelated passed V without the required postcondition reference;
- missing F on every receipt-origin/path variant; duplicate F; non-passed F;
  any check after F by sequence; and RF-N11 F with `expectedSummary`,
  `observedSummary`, both, or an unknown/free-form summary/detail/payload
  member;
- RF-N12 F with a wrong exact `checkId`, the regex-valid secret-like
  `check.c-users-alice.secrets.api-key-abcd1234`, a wrong `profileId`, the
  regex-valid secret-like `profile.synthetic.secret.sk-live-abcdef123456`,
  non-empty `reasonCodes`, the regex-valid secret-like
  `reason.synthetic.secret.token-abcdef123456`;
- a non-F check using `check.receipt-finalization`, owned only by generic
  receipt-wide check-ID uniqueness because the mandatory F already uses that
  ID; this is derived/non-additive and not RF-N12;
- CH-N05 a non-F check after sanitization, CH-N07 denial evidence after
  sanitization, CH-N22 F before sanitization, CH-N23 F after finish, plus every
  other primitive chronology reversal;
- missing L on both release-required origins; every finalL/top-level off-
  diagonal mismatch; final-L warning absent/wrongly referenced; RF-N13 with any
  bad issued L reference, including a bad earlier L before a correct finalL;
  RF-N14 with `sanitization.applied: false` and no other defect; Dpre after L;
  and L on every no-release path.

The active acceptance matrix MUST independently exercise:

- canonical F with exactly `check.receipt-finalization`,
  `profile.validation.v1`, `[]`, and passed outcome, plus ordinary non-F
  checks using other generic-profile IDs; every such serialized receipt has
  `sanitization.applied: true`, including a valid `redactionCount: 0` variant;
- repeated same-type all-passed G, including every G type as a variant;
- multiple P members only when all are passed, with the greatest-sequence final
  P strictly pre-expiry before E/V;
- complete lease-required attempted and non-attempted issued chains with one
  valid AP-1 source, source-profile-valid digest, exact source-to-root digest
  copy, receipt/source task identity, source/root/A check identity, compact
  A/R/every-L references, and source/root/contract lease-ID equality, including
  multiple L members all bound to that same identity;
- no-lease attempted `G/N/I/P/E/V/F` and non-attempted `G/N/I/[P]/F`, with
  source, root, and compact references absent and
  `releaseOutcome: not-required`;
- for each of all nine denial checkpoints, a controller with no earlier
  same-type observation and mandatory non-additive histories `passed ->
  failed`, `passed -> indeterminate`, `passed -> passed -> failed`, and
  `passed -> passed -> indeterminate`, subject to the cumulative matrix;
- each of the first five denial checkpoints with exactly its passed cumulative
  prefix, every actual prerequisite before the controller, exact controller
  ID/type/greatest/outcome/time/reason binding, no unreached type or ordinary
  post-controller check, sanitization, and exact-tuple F;
- N denial with cumulative all-passed G, exact N controller binding, no
  A/R/I/P/E/V/L or acquired reference, and exact-tuple F;
- acquired R denial with cumulative all-passed G and passed A all ordered
  before the exact R controller tuple, exact A/lease/digest reference binding,
  ownership-checked post-controller L, sanitization, and exact-tuple F;
- acquisition and both issuance-denial variants with exact controller binding,
  including indeterminate acquisition with its warning, acquired issuance with
  exact I controller and A/lease/digest reference tuple, no-lease issuance
  without that reference, all actual prerequisites before I, no ordinary check
  after I, and exact-tuple F;
- the unchanged repaired preContractEvidence example; the AP-1 163-byte source
  projection, 234-byte completed source identity, and receipt-root exact-copy
  vector; and the RS-1 issued no-lease golden, including all recorded exact
  bytes and digests and independent Python/Node/PowerShell replay;
- multiple V(t) members with passed greatest-sequence finalV(t), and multiple L
  members with passed greatest-sequence finalL;
- execution failed with verification/release passed and F, and verification
  failed with release passed and F; and
- timestamp equality and non-equality witnesses for both RS-1 issuance
  brackets, including `R == issuanceCheckpoint == issuedAt` and
  `N == issuanceCheckpoint == issuedAt`, plus equality at every permitted FS-1
  boundary, including non-F/sanitization, denial-evidence/sanitization,
  sanitization/F, and F/finish.
Worktree-role ownership of the complete `Domain` set and runtime write leases MUST be exercised as independent controls. Tests MUST prove that execution outcome and lease liveness are independent and that generated receipts remain outside portable governance. Terminal processing MUST attempt to record a sanitized `ExecutionReceipt` for every issued-contract execution attempt; pre-contract denial receipts MAY remain policy-optional. Tests MUST NOT rely on automatic branch switching, branch creation, stashing, reset, cleaning, restoration, fetching, pulling, merging, rebasing, lease or lock breaking, or Git-state repair.
