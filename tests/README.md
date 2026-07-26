# Planned test strategy

Phase 0 documentation bootstrap is complete at baseline commit
`79cc9d77fd48410f37645afdb429a7cd2e34a0bd`. Phase 1: Schemas and
Models is current, but Phase 1 implementation has not yet begun. The repository
remains pre-operational, and no tests or fixtures exist yet. Future tests MUST
be deterministic and MUST use sanitized synthetic data. The planned Schema
contract, static-validation vectors, and fixture inventory are recorded in the
[v1alpha1 Schema contract design](../docs/schema-contract-v1alpha1.md).

Independent design audit and `integration-control` approval of the prior
candidate remain complete. The six earlier review findings were repaired,
independently audited, confirmed, replied to, and resolved. The third Codex
review at exact HEAD `658c2e0f65c7dff0553a3433ca8cf484847f3a66` produced
three accepted findings. The repository owner has selected `TS-LEX-01 A`,
`REMOTE-HOST-01 A`, `REMOTE-NAMESPACE-01 A`,
`REMOTE-REPOSITORY-01 A`, and `REMOTE-DOTGIT-01 A`; the receipt-binding
repair is fully derived. This uncommitted three-finding working candidate
requires fresh independent audit and `integration-control` confirmation. PR
#1 remains open and unmerged. The candidate is not audited, confirmed,
committed, pushed, integrated, merge-ready, or implementation-ready.

All 11 Schema resources remain `reserved-unpublished`, and no Schema
implementation exists. Model-worktree creation and model implementation remain
prohibited by the Schema-before-model sequence.

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
`TaskContract.spec.taskContractDigest`, or compare nonduplicated
`requestedMode`, `allowWrite`, `leaseId`, scope, `contractVersion`,
freshness, or expected baseline.

The required conformance order is:

1. strictly decode and structurally validate the complete receipt and complete
   referenced TaskContract under the selected Schema revision;
2. apply both artifacts' local Phase 1 and canonical-array checks;
3. validate the complete contract and derivation prerequisites;
4. recompute `profile.digest.task-contract-v1` over its exact projection;
5. compare digest, contract ID, task ID, complete target, and effective mode;
6. apply chronology against the same contract;
7. apply receipt outcome, release, non-writing, and remaining consistency;
8. only then compute and verify or accept the receipt digest; and
9. only after receipt finalization validate delivery receipt-ID binding, exact
   finalized digest copy, and delivery chronology.

Positive vectors MUST cover:

1. a matching plan-only contract/receipt pair;
2. a matching valid implementation-mode pair;
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
17. reinterpretation of the mismatch as `pre-contract-denial`; and
18. delivery bound to another receipt ID or digest.

Every negative rejects before receipt-digest acceptance; validators neither
repair nor switch contracts. `schema-contracts` specifies this static contract
and its expected vectors. Future `model-implementation` owns strict decoding,
projection, hashing, and executable cross-artifact tests. Phase 4 owns trusted
issuer provenance, authenticity, current authority and preconditions, and
evidence truth. Digest equality alone grants no authority.

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
authenticity, freshness, and event truth. The five existing protected values
and all 16 occurrences remain byte-identical.

Future Phase 1 static and contract coverage MUST enforce all chronology
relations in the design record's [timestamp chronology
section](../docs/schema-contract-v1alpha1.md#timestamp-chronology). Equality is
permitted for every relation except the strict
`freshness.issuedAt < freshness.expiresAt` boundary.

Positive vectors MUST cover strict progression, all-equality boundaries within
each applicable artifact combination with strict freshness preserved, each
permitted equality boundary independently, both receipt origins, empty and
populated check arrays, a complete issued-contract receipt/TaskContract pair,
and a complete receipt/delivery-result pair. Negative vectors MUST reverse
each relation independently, including checks before `startedAt` or after
`sanitization.completedAt`, pre-contract evidence outside that interval,
`issuanceCheckpoint.observedAt` after `freshness.issuedAt`, an issued-contract
receipt starting before contract issuance, a delivery attempt before receipt
completion, and equal and reversed freshness boundaries.

Tests MUST NOT impose check-type or adjacent-check timestamp order, require
receipt completion before contract expiry, infer truth from timestamp syntax,
use a trusted clock in Phase 1, or treat chronology as authority. Existing
canonical JSON, golden-vector bytes, digest projections, and recorded digests
must remain unchanged.

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

### SG-001 closure coverage

Future Schema and static-contract coverage MUST implement every row of the
design record's [mandatory exhaustive fixture/conformance
matrix](../docs/schema-contract-v1alpha1.md#mandatory-exhaustive-sg-001-fixtureconformance-matrix).
The prior design approval remains recorded, but PR integration is incomplete.
This current three-finding working candidate requires fresh independent audit and
`integration-control` confirmation before integration. Matrix coverage remains
planned: no validator, fixture, executable test, or Schema implementation
exists, and the toolchain and separately authorized implementation gates remain
blocking.

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
  satisfy the defined `repositoryRelativePath` profile, strict UTF-8, and
  already-NFC checks, and cover every fail-closed observation class.
- **D4:** reproduce the fixed raw regular, executable, and link-target byte
  digests without filters, decoding, normalization, or dereference, and reject
  unstable, unreadable, replaced, truncated, or unsupported objects.
- **D5:** require exactly empty transitions, baseline-equal state
  postconditions, no lease, and empty issued-receipt changed paths for all three
  non-writing rows, including the complete three-by-nine negative product.
- **D6:** enforce `verificationOutcome: not-performed` if and only if
  `executionOutcome: not-attempted`, cover every allowed pair and all seven
  invalid pairs, and apply this gate before lifecycle precedence.
- **D7:** bind each `from` directly to the complete materialized baseline,
  apply all unique transitions simultaneously, reconstruct and validate one
  canonical final composite, and require an exact final postcondition for every
  changed dimension.
- **D8:** require exactly the five closed HostOverlay binding fields, canonical
  non-empty `remoteNames`, exact ref-branch conditions, name resolution, and
  rejection of `expectedBranch` or any cached observation field.
- **D9:** record all six positive and twelve negative complete-set routing
  vectors, `Drule`/`Dresolved`/`Owned(R)` semantics, no-fallthrough and no-union
  behavior, split independence, and exact-duplicate precedence; future
  `model-implementation` compares exact RFC 8785 JCS bytes of `RuleProjection`
  and `MatchProjection` with no digest, case folding, rewriting, inference,
  host transformation, or array reordering; Phase 2 alone resolves and routes.
- **D10:** prove Project/role identity, exact capability equations, repository
  and remote inclusion, binding-name resolution, and path-language inclusion
  with deterministic automata; reject widening and every unavailable proof;
  and prove HostOverlay, availability, branch, or lease state cannot make an
  incomplete selected role eligible.
- **D11:** `schema-contracts` catalogs eleven digest field paths bound once to
  ten computations, the acyclic dependency graph, framing, projections,
  completed values, recorded bytes/digests, and expected vectors; every
  cataloged selector resolves to a valid branch in its closed union, and the
  acquired acquisition-result selector is exactly
  `ExecutionReceipt.spec.origin[type=pre-contract-denial].leaseAcquisition[state=acquired].acquisitionResultDigest`;
  the invalid `leaseAcquisition` predicate `[type=acquired]` is rejected.
  Future `model-implementation` constructs projections, JCS, hashes,
  verification, and executable replay of every separator, raw/JCS payload,
  exclusion, completed value, tagged hash, negative vector, delivery copy, and
  cross-runtime result. Phase 4 alone performs trusted operational replay.
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
9. issued receipt/TaskContract field equality;
10. cross-artifact chronology and outcome consistency;
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
- zero resolved `Domain` identifiers; a selected role that owns only the
  rule-declared subset; a higher-priority partial owner above a lower-priority
  complete owner; several roles offered as a collective union; multiple
  greatest-priority matches; split reuse; TaskContract Domain/role/target
  mismatch; and a wrong-role but unlocked worktree;
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
