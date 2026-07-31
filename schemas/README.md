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
`a99e57773384c0af4a6531f38aa14bee3781f19d`. The sixth Codex review at that
exact HEAD identified two validated P1 findings requiring repair: require
valid immediately-before-action revalidation evidence to precede every
execution-stage check for an attempted issued-contract receipt in thread
`PRRT_kwDOThD5p86VKc3R`, and exclude Git administrative paths from portable
repository-relative paths, patterns, ordinary scopes, and changed-path
evidence in thread `PRRT_kwDOThD5p86VKc3X`. This working-tree revision records
the proposed documentation-only repairs for those findings. Both sixth-review
threads remain external GitHub records; no reply or resolution is claimed.

The proposed sixth-review repair awaits independent read-only audit, separate
commit authorization, exact committed-head verification, push authorization,
remote-head confirmation, GitHub evidence synchronization, re-review, and
merge-readiness review. Implementation and merge remain external and
unauthorized. No thread reply or resolution, PR-body update, review request,
Schema implementation, or model implementation is claimed.

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

## Retained fifth-review repairs and sixth-review proposed repairs

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
`pre-action-revalidation` check and let `E` be every `execution` check. Check
sequence is the array position:
sequences are contiguous from zero, check IDs are unique, and the final
applicable check is the unique greatest-sequence member of `P`. It is not
selected by `observedAt`, serialization, iteration order, locale, or check ID.
Every {succeeded, failed, cancelled, indeterminate} execution attempt requires
`count(P) >= 1`, requires that final applicable check to have outcome `passed`,
and requires it—and every other passed member of `P`—to be strictly before
`TaskContract.spec.freshness.expiresAt`. Earlier failed or indeterminate checks
may coexist with a later final pass. An earlier pass followed by a final failed
or indeterminate check is invalid even when all passed checks are pre-expiry.

For each execution outcome in `{succeeded, failed, cancelled, indeterminate}`,
an attempted receipt requires `count(P) >= 1`, `count(E) >= 1`, the
greatest-sequence member of `P` to be passed and strictly pre-expiry, every
passed member of `P` to be strictly pre-expiry, and
`finalApplicablePreActionCheck.sequence < e.sequence` for every `e` in `E`.
Any execution check before the final applicable pre-action check invalidates
the receipt even if another execution check occurs later.

A `not-attempted/not-performed` receipt may omit both `P` and `E` and may
retain failed or indeterminate denial evidence at or after expiry; any passed
pre-action check must still be strictly pre-expiry. Receipt completion and
later lifecycle stages may occur after expiry. `startedAt` is not proof of
action freshness, no `finishedAt <= expiresAt` rule exists, and final-check selection adds no
timestamp chronology relation. The focused inventory is exactly eight positive
and 33 negative classes, while chronology remains exactly 12 relations. Each
attempted positive has at least one execution check after the final valid
pre-action check. The eight added negatives are four attempted outcomes with no
execution check and the same four outcomes with an execution check before the
final applicable pre-action check; at least one ordering vector has execution
checks on both sides and still rejects universally.

D5 now contains exactly 21 `3 × 7` Cartesian negatives. Removing the retired
administrative-lock transition removes two TaskContract administrative-lock
array rows, so the array-ordering matrix contains 52 rows while the reusable
evidence union retains its identity and ordering rules.

The sixth-review proposed-repair invariant inventory is:

```text
Schema resources = 11
dispatchable kinds = 7
baseline dimensions = 9
permitted-transition branches = 7
required-postcondition branches = 11
array-ordering matrix rows = 52
mandatory SG-001 matrix rows = 25
D5 Cartesian negatives = 21 = 3 × 7
active-operation legacy-contract regressions = 21
administrative-lock legacy-contract regressions = 21
timestamp paths = 9
timestamp lexical/calendar positives = 10
timestamp lexical/calendar negatives = 24
chronology relations = 12
focused pre-action positive classes = 8
focused pre-action negative classes = 33
receipt/contract equalities = 8
receipt-binding positive vectors = 5
receipt-binding negative vectors = 18
digest-bearing paths = 11
digest computations = 10
receipt/delivery digest copies = 1
numeric fields = 6
```

The repaired synthetic receipt projection is 1530 UTF-8 bytes and its completed
form is 1620 UTF-8 bytes. Its independently recomputed digest is
`sha256:da362d27555ebf9c737b6bfcd7e31b12b3a7c7381280a6bba2b9965f0098f01e`,
and the delivery result copies that value without a new computation. The
protected corpus retains five distinct timestamp values across 20 occurrences
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
