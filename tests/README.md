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

#### Issued-contract receipt and referenced TaskContract binding

The closed `issued-contract` origin retains exactly `contractId`,
`contractDigest`, `resolvedTarget`, and `effectiveMode`, together with the
receipt-level `ExecutionReceipt.spec.taskId`. Conformance uses the complete
referenced TaskContract fields `metadata.id`, `spec.taskId`,
`spec.projectRef`, `spec.domainRefs`, `spec.target.worktreeRoleRef`,
`spec.target.worktreeId`, and `spec.effectiveMode`. It does not invent
`TaskContract.spec.taskContractDigest`. Instead, the complete TaskContract
digest is recomputed with `profile.digest.task-contract-v1` over the exact
validated complete TaskContract projection already defined in the digest
catalog, including its existing derivation binding.

When `receipt.spec.origin.type == issued-contract` and the receipt is validated
with its complete referenced TaskContract, Phase 1 static conformance requires
all eight equalities:

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

LB-2 adds one independent cross-artifact lease predicate after those eight
duplicated-claim equalities. It is not a ninth duplicated origin field:

```text
if contract.spec.leaseRequired == true:
  receipt.spec.acquisitionBinding.leaseId
    == LeaseAcquisitionResultIdentity.leaseId
    == contract.spec.leaseId
```

The referenced contract's local truth table already requires exactly one
`leaseId` on that branch. The receipt root and associated source are separately
required, source-profile validated, and proven equal before this comparison.
The independent receipt/contract-binding fault remains a contract `leaseId`
that differs from the already-bound source/root lease. When
`contract.spec.leaseRequired == false`, the contract `leaseId`, receipt root,
and associated source are all absent, so no fabricated null or sentinel
equality is introduced.

The exact non-digest `resolvedTarget` projection is:

```text
{
  projectRef: contract.spec.projectRef,
  worktreeRoleRef: contract.spec.target.worktreeRoleRef,
  worktreeId: contract.spec.target.worktreeId,
  domainRefs: contract.spec.domainRefs
}
```

Equality is exact post-validation canonical equality. Object-reference equality
is exact equality of the complete closed reference objects. For `domainRefs`,
both arrays have the same canonical length, the same complete Domain-reference
members, the same member order, and byte-equivalent canonical member
representations. A receipt may not omit, add, substitute, or reorder a Domain
or use a partial resolved set.

The unified AP-1 Source/binding block supplies the acquisition profile and copy rules on both stable-acquired origins. It preserves all eight comparisons above and additionally compares issued binding.leaseId with C.spec.leaseId. No equality is invented for unduplicated contract fields. Validation follows the Preparation → Static acceptance → Receipt digest → optional Delivery pair DAG below. Constructing selectors never implies acceptance; all cross-artifact predicates must pass before receipt digest acceptance.

Receipt/contract comparisons have current owners RC01..RC09 in the independent ledger below. Matching plan-only, lease-required, multi-Domain, all-identity, and delivery-pair cases remain mandatory variants. Domain omission/addition/substitution and wrong complete-contract body/digest cases remain negative variants; array disorder belongs to canonicality. Cross-artifact mismatches reject before receipt digest acceptance and cannot be reinterpreted as denials or repaired by switching contracts. Phase 3 produces acquisition evidence; Phase 4 validates trusted provenance, ownership, event truth, and authority. Static source/contract binding proves only integrity and equality.

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
region contains eight distinct timestamp values across 192 occurrences; its full
remote and digest counts are mirrored below.

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

After complete contract digest/equality binding, tests define V(t) for each
required type t as the referenced subset and select `finalV(t)` by greatest
sequence. Every attempted receipt has at least one V(t) for every required
type; passed verification requires every V passed and every finalV(t) passed.
An earlier passed member cannot repair a later failed or indeterminate
finalV(t), and an earlier non-passed V(t) cannot be erased by a later passed
finalV(t) to regain passed top-level verification. The global final V continues
to bind `verificationOutcome` and may be referenced or general. Mixed outcomes
remain valid on non-passed histories when that final V matches the top-level
non-passed outcome; later V collection remains permitted.

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

Lease-required issuance specializes the unified stable-acquired prefix:
singleton passed A/R, N empty, and `every G < A < R < I < every P`. No-lease issuance has A/R empty, singleton
passed N, no lease identity, and `every G < N < I < every P`. Attempted paths
retain final P < every E < every V; non-attempted paths keep E/V empty and may
omit P. Every actual G participates in ordering.

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
9. multiple V members after all E members, every V outcome `passed`, with the
   final V `passed` and top-level verification `passed`; and
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
14. final V `failed` with receipt `verificationOutcome: passed`; its mandatory
    non-additive C variant has an earlier unreferenced failed V, a later final
    passed V, and top-level verification `passed`, with every unrelated
    predicate valid;
15. final V `failed` with receipt `verificationOutcome: indeterminate`;
16. final V `indeterminate` with receipt `verificationOutcome: passed`; its
    mandatory non-additive C variant has an earlier unreferenced indeterminate
    V, a later final passed V, and top-level verification `passed`, with every
    unrelated predicate valid;
17. final V `indeterminate` with receipt `verificationOutcome: failed`;
18. `not-attempted/not-performed` with one stray V whose outcome is `passed`;
19. `not-attempted/not-performed` with one stray V whose outcome is `failed`;
    and
20. `not-attempted/not-performed` with one stray V whose outcome is
    `indeterminate`.

Except when the primary fault belongs to the dedicated postcondition-binding
family, every planned attempted-issued class in this 10/20 family requires
referenced V evidence for every required type, and every passed-verification
positive requires every V outcome passed and each per-type final V passed.
Those are prerequisites, not added cases. Class 10 keeps V empty and therefore
contains no reference. The exact 10/20 total is unchanged.

Case 12 proves greatest-sequence final selection because the earlier V matches
the receipt and the later final V does not. Generic sequence gaps, duplicate
sequences, duplicate check IDs, and malformed check arrays remain outside this
10/20 family. The focused pre-action inventory remains 8/37, and the unchanged
D6 receipt-level table remains exactly 13 valid and 7 invalid combinations.

The mandatory class-14 and class-16 recovery variants use an unreferenced
earlier bad V. Referenced same-type recovery variants belong only to the C-UNIVERSAL-PASS owner, preserving non-additive unique ownership.

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



### Retained historical protected-region records

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
postcondition paths, all four supported path-keyed transition branches, receipt
`changedPaths`, and `scope-contained` verification. `modify` plus `**` and
Git-administration capability tokens MUST NOT authorize direct `.git/config`,
hook, ref, or other administrative-path mutation. A runtime-resolved
administrative effect cannot be reported as a successful ordinary changed path
or silently omitted; `scope-contained` must be failed or indeterminate.

For a complete issued receipt and referenced TaskContract `C`, tests define
`M = {create, modify, delete}`,
`Acap = set(C.spec.authorizedScope.capabilities)`,
`Qcap = set(C.spec.prohibitedScope.capabilities)`, `Apath` as the union of
`C.spec.authorizedScope.paths` languages, and `Qpath` as the union of
`C.spec.prohibitedScope.paths` languages. Planned coverage defines
`Attempted(e)` as `succeeded`, `failed`, `cancelled`, or `indeterminate` and
requires `ExecutionReceipt.spec.ordinaryOperationEvidence` if and only if the
origin is `issued-contract`, `C.spec.allowWrite` is true, and the execution
outcome is attempted.

Coverage MUST require the carrier for successful, failed, cancelled, and
indeterminate writing attempts, forbid it for pre-contract denial,
plan-only/non-writing, and not-attempted issued paths, and prove that later
release failure changes neither presence nor contents. A complete zero-effect
writing attempt has exactly `ordinaryOperationEvidence: []`; no second zero-
effect representation is accepted.

Each member is a closed record containing exactly required `path` and
`operations`. Planned structural/static cases reuse the complete
`repositoryRelativePath` profile, require one through three distinct
`create|modify|delete` tokens, reject unknown members and operations, reject
empty operations and duplicate paths/tokens, and require outer
`S(record.path)` order plus nested `S(token)` order, exactly `create`,
`delete`, `modify`, without sorting invalid input.

Per path, operations are the union of every attributable operation during the
attempt. Tests retain repeated, transient, restored, and baseline-restored
effects; cover multiple operation types on one path; and encode rename-
equivalent old-path delete and new-path create without a rename token. They
reconstruct only:

```text
EvidencePaths =
  {record.path | record in ordinaryOperationEvidence}

OexecByPath[p] =
  set(the unique record.operations for p)

Oexec =
  union over every OexecByPath[p]
```

They MUST NOT derive `Oexec` from `changedPaths`, final state, summaries,
profiles, reasons, or human interpretation. Every attributable ordinary-effect
path is carried, and the exact cross-artifact relationship is
`EvidencePaths ⊆ set(changedPaths)`, not equality. Transient/restored paths
remain in both; extra changed paths do not invent operations.

A passed writing scope claim requires every changed and carrier path in
`Apath` and not in `Qpath`, the subset relation,
`Oexec ⊆ Acap`, and `Oexec ∩ Qcap = ∅`; Acap/Qcap remain global
capability sets. Passed verification also requires passed, exactly referenced
`finalV("scope-contained")`. Review-14 B remains unchanged and A2 makes its
`Oexec` durable. C-UNIVERSAL-PASS remains unchanged: every V is passed whenever
top-level verification is passed, without changing either greatest-sequence
selector, mixed non-passed history, or fresh-lifecycle recovery.

Missing-required or forbidden-present carrier, malformed shape/order, omitted
known operations, and a carrier path absent from `changedPaths` reject before
receipt-digest acceptance. `[]` with complete zero-effect evidence is valid;
`[]` omitting known evidence is evidence-conformance invalid; `[]` under
unresolved attribution may be structurally valid but requires indeterminate
verification. Unauthorized/prohibited paths or operations are structurally
valid evidence but fail scope. Every known effect remains represented when
attribution is incomplete. Phase 1 owns carrier structure, ordering,
reconstruction, and static binding; Phase 4 owns runtime truth/completeness.
The existing complete-receipt digest automatically includes the carrier when
present, but a matching digest cannot cure malformed input or prove omitted
history. No new profile, external artifact, graph node, computation, or copy is
planned.

This planned carrier is a material pre-publication wire-shape change while all
resources remain `reserved-unpublished`. Coverage retains
`contextctl.dev/v1alpha1`, `v1alpha1-r1`, and receipt version `1`; compatibility,
publication, and version confirmation remain a later `integration-control`
gate. No Schema, fixture, validator, or executed test is claimed here.

The five focused positive changed-path scope classes remain exactly, with valid
operation-capability containment as non-additive background:

1. one authorized, non-prohibited changed path;
2. multiple changed paths, all authorized and non-prohibited;
3. an empty writing result with complete passed no-effect evidence;
4. offending paths retained with failed verification and a non-succeeded
   lifecycle; and
5. offending paths retained with indeterminate verification and a
   non-succeeded lifecycle.

The six dedicated negative changed-path scope classes remain exactly, with
otherwise-valid operation-capability evidence:

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

#### `ORDINARY-CAPABILITY-CLOSURE` coverage

For writing contracts, tests derive the ordinary path projection only after
the complete simultaneous D7 final composite `F` is valid. Each path projects
as absent, present with exact known ordinary-file identity, or present with
opaque ordinary-file identity. Absent-to-present is create,
present-to-absent is delete, known unequal present-to-present is modify, known
equal and absent-to-absent are no-op, and equality-unprovable present-to-present
is conservative possible modify. `Oplan(B,F)` is the least-upper-bound union
over every B/F-consistent ordinary effect and must satisfy both
`Oplan(B,F) ⊆ Acap` and `Oplan(B,F) ∩ Qcap = ∅`.

The exact three positive and eight negative primary owners are:

| Primary ID | Required planned vector |
| --- | --- |
| `OC-P01` | authorized, non-prohibited create |
| `OC-P02` | authorized, non-prohibited modify |
| `OC-P03` | authorized, non-prohibited delete |
| `OC-N01` | create implied but absent from `Acap` |
| `OC-N02` | modify implied but absent from `Acap` |
| `OC-N03` | delete implied but absent from `Acap` |
| `OC-N04` | create implied and present in `Qcap` |
| `OC-N05` | modify implied and present in `Qcap` |
| `OC-N06` | delete implied and present in `Qcap` |
| `OC-N07` | valid-path multi-path B/F composite with at least one implied operation absent from `Acap` |
| `OC-N08` | net-valid B/F state but an actual unauthorized transient/restored operation on an authorized path |

Mandatory non-additive variants cover untracked create/delete; ignored
create/delete; tracked `D -> P` create, `P -> D` delete, and changed `P -> P`
modify; a known ordinary no-op; unchanged ref/HEAD/submodule observation and a logical index ordinary no-op; opaque
same-present with modify authorized, absent, and prohibited; create+modify+delete
across distinct paths with all three authorized; and rename-equivalent
delete-old/create-new with both tokens required. An index-entry alone adds no
ordinary-file operation but still requires git-stage; ref/HEAD/submodule
transitions reject structurally. Tracked/untracked/ignored classifications
derive only from complete B/F path state, and classification transfer alone is not create+delete when the leaf
remains present. `entryPresence.state` alone is insufficient.

The family remains exactly OC 3/8/11 and reuses no HX ID. It adds no wire field,
enum, reason, capability token, transition, uncertainty member, digest input, or
runtime collector; the separately owned A2 carrier is not an OC addition. For
`allowWrite: false`, transitions, changed paths, and the ordinary operation set
remain empty, the carrier is forbidden, and execute-tests/build does not widen
ordinary mutation.

#### Focused `OPERATION-EVIDENCE` coverage

This separately counted, planned, non-executable family has exactly ten
positive primary owners:

1. **OE-P01:** one path plus modify;
2. **OE-P02:** one path plus create;
3. **OE-P03:** one path plus delete;
4. **OE-P04:** one path plus create and modify;
5. **OE-P05:** one path plus create and delete;
6. **OE-P06:** multiple canonically ordered paths;
7. **OE-P07:** transient modify then restore;
8. **OE-P08:** transient create/delete then restore;
9. **OE-P09:** rename-equivalent old-path delete and new-path create; and
10. **OE-P10:** complete carrier, `EvidencePaths ⊆ changedPaths`, satisfied
    carrier-path predicates, and permitted reconstructed `Oexec`.

It has exactly eleven negative primary owners:

1. **OE-N01:** missing required carrier;
2. **OE-N02:** carrier present where forbidden;
3. **OE-N03:** duplicate path;
4. **OE-N04:** empty operations;
5. **OE-N05:** duplicate operation;
6. **OE-N06:** non-canonical outer-record order;
7. **OE-N07:** non-canonical operation order;
8. **OE-N08:** unknown operation;
9. **OE-N09:** omitted known attributable operation;
10. **OE-N10:** carrier path absent from `changedPaths`; and
11. **OE-N11:** ambiguous/unresolved attribution represented as a passed
    successful no-op.

OE is exactly 10/11/21 and is not merged into OC. Invalid path and exact
`.git`-component witnesses remain D3/path-profile owned. Unauthorized and
prohibited path witnesses remain changed-path-scope owned. Modify-only
transient create/delete witnesses remain OC-N08 variants. Rename missing
create/delete authority remains an OC-N07 rename variant with the corresponding
existing capability fault. A malformed carrier accepted on the digest path is
a non-additive validation-order variant of its OE structural owner. D6,
PB/global verification, OC 3/8/11, and every existing aggregate retain their
independent ownership. No fixture file or executable test is created or
claimed executed. The expanded prior-family aggregate excludes OC and OE and
is 168 and excludes the separate OC and OE case inventories.

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
The row count remains exactly 25. Review-14 B extends only the existing
Permitted transitions, Required postconditions, D7 simultaneous transition
composition, and Receipt outcomes/scope rows; OC is cross-referenced and does
not add a matrix row. A2 extends only that existing Receipt outcomes/scope row
with conditional carrier presence, static validity,
`EvidencePaths ⊆ changedPaths`, reconstruction, and path/capability
predicates; OE adds no SG row.
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
  reuse through unchanged final-composite reconstruction and optional
  submodule-state postconditions; reject submodule-entry transitions.
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
  postconditions, no lease, empty issued-receipt changed paths, and an empty
  ordinary operation set for all three non-writing rows; cover exactly 12
  Cartesian negatives, `3 × 4`, across
  the four supported transition branches; cross-reference, without
  duplicating, the non-empty changed-path invalid case from scope coverage.
- **D6:** enforce `verificationOutcome: not-performed` if and only if
  `executionOutcome: not-attempted`, cover every allowed pair and all seven
  invalid pairs, then apply EF-1 execution terminality, final E/global V, per-type final V, and final L
  bindings, finalG, exact applicable A/R/N/I, universal terminal F,
  L/finalL/warning, and not-attempted E/V plus no-release L-empty gates before
  lifecycle precedence.
- **D7:** bind each `from` directly to the complete nine-dimension
  baseline, apply only the four supported transition types simultaneously,
  preserve ref/HEAD/submodules and none-valued active operations/administrative
  locks, reconstruct one valid nine-dimension F, and require exact changed-
  dimension postconditions plus baseline-equal optional unchanged ones.
  Check Ptrans directly against Apath/Qpath regardless of ordinary effects.
  Derive unchanged Oplan(B,F), add Iplan, and require RequiredPlanCaps subset
  Acap and disjoint Qcap; retain complete Domain/role/Project/overlay narrowing.
- **D8:** require exactly the unchanged five closed HostOverlay binding fields,
  canonical non-empty `remoteNames`, exact ref-branch conditions, name
  resolution, rejection of `expectedBranch` or any cached observation field,
  individual validation of every member of one complete trusted same-host set,
  coherent snapshot-bound binding-union `worktreeId` and exact-root
  injectivity, fail-closed membership, and static coordination-root exclusion
  using the exact strict-descendant comparator; cover all five HX positives and
  thirteen HX negatives without changing binding ordering; Phase 3 owns
  canonical physical-worktree injectivity, live containment, and fail-closed
  ambiguity.
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
- **D11:** the complete twelve-row catalog in this document has ten computations and two exact copies. Both stable-acquired origins share the external Source computation, exact acquisitionBinding copy, A/every-R/every-L identity, and receipt digest. Acquired evidence includes the complete binding; other denials omit it. The source, evidence, receipt, and optional delivery graph is acyclic. Future model-implementation owns executable projection, framed raw/JCS hashing, copying, replay, and conformance; Phase 3/4 own production and trusted provenance/ownership.

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
  postcondition reference, unified acquisitionBinding and A/every-R/every-L references on both stable-acquired origins,
  lease-acquisition, lease-release, and receipt-
  finalization branch;
- required `preContractEvidence.controllerCheckId` and
  `sanitizedSummary`, exact stable-acquired acquisitionBinding/Source presence and binding, and `ReceiptDeliveryResult.sanitizedSummary`
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

Every one of the four supported permitted-transition branches and all eleven
required-postcondition branches requires positive coverage. The optional
active-operation and administrative-lock postconditions are both none-only.
The transition vectors cross-reference ordinary B/F projection and the OC
family: unchanged ref/HEAD/submodule observation and a logical index ordinary no-op, tracked/untracked/ignored
create/modify/delete classification, opaque same-present conservatism, and both
`Oplan(B,F)` capability predicates within RequiredPlanCaps, plus Iplan and
Ptrans closure. Successful `scope-contained` coverage has
changed-path and carrier-path containment, `EvidencePaths ⊆ changedPaths`,
reconstructed `Oexec`, and operation-capability containment.
Negative coverage MUST reject identical `from`/`to`, missing target keys,
unknown transition types, all five unsupported/retired types, duplicate transition
targets, duplicate postcondition types, non-empty active-operation or
administrative-lock expectations, any exact `.git` component in a path-keyed
value, a successful scope claim that omits an administrative effect or lacks
path or operation-capability containment, and a missing or repeated
`scope-contained`.
Uniqueness is established before digest projection or hashing.

Receipt vectors cover warnings with and without optional fields, all 14 check
types, the exact 4/3 outcome conditional, V-only closed references, contiguous
sequences, unique IDs, ordered reason codes, and same-receipt warning links.
All outcomes retain the independent owner ledger and full chronology graph above, universal P/E/V and scope predicates, exact Source/binding/A/every-R/every-L linkage, issued lease equality, state-aware denial matrix, warning linkage, pairwise L chronology, and exact terminal F. The complete synthetic corpus and adversarial recipes make intended dispositions reviewable; executable Schema/model tests remain a later authorized implementation.

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
  path A/R/N/I; G-after-A sequence or timestamp inversion on every stable-
  acquired origin, including repeated passed G and acquired R/I denials;
  every other G/A/R/N/I/P sequence violation; a missing/invalid
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

Worktree-role ownership of the complete `Domain` set and runtime write leases MUST be exercised as independent controls. Tests MUST prove that execution outcome and lease liveness are independent and that generated receipts remain outside portable governance. Terminal processing MUST attempt to record a sanitized `ExecutionReceipt` for every issued-contract execution attempt; pre-contract denial receipts MAY remain policy-optional. Tests MUST NOT rely on automatic branch switching, branch creation, stashing, reset, cleaning, restoration, fetching, pulling, merging, rebasing, lease or lock breaking, or Git-state repair.
