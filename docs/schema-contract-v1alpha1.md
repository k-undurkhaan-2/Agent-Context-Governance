# contextctl.dev/v1alpha1 Schema Contract Design

Phase 1: Schemas and Models is current, but Schema implementation has not begun. The recorded history identifies independent design audit and `integration-control` design approval of the prior candidate as complete, the six earlier review findings as repaired, independently audited, confirmed, replied to, and resolved, the three third-review findings as repaired at commit `9eac3e040a8d0f9c959eeb675eace795749e422a`, the two fourth-review repairs as recorded at commit `b972382fad27a4dda0a4dff945c94b711019ec45`, and the two fifth-review repairs as present at exact commit `a99e57773384c0af4a6531f38aa14bee3781f19d`. The originating `a99e5777...` push transaction remains historically attribution-indeterminate.

The sixth-review documentation repair was committed at exact commit `37e3f373b012050ac424ea7d74c39396196d7da4` after its three-file candidate received independent read-only audit. The exact OpenPGP-signed committed head was independently verified; its single-ref non-force push and remote branch/PR-head confirmation completed; and both sixth-review threads, `PRRT_kwDOThD5p86VKc3R` and `PRRT_kwDOThD5p86VKc3X`, received exactly one owner evidence reply and were resolved.

The seventh-review documentation repair was committed at exact commit `529d9d535198b55b80aedf64141967e6bf66448f` after its three-file candidate received independent read-only audit. The exact OpenPGP-signed committed head was independently verified; its single-ref non-force push and remote branch/PR-head confirmation completed; all four seventh-review threads received owner replies and were resolved; and the PR body was synchronized. The seventh top-level `@codex review` request is REST comment `5151809449` / GraphQL comment `IC_kwDOThD5p88AAAABMxJfqQ`.

The eighth-review repair for REST review `4834819015` / GraphQL review `PRR_kwDOThD5p88AAAABIC17xw` was committed at exact commit `fa0f3acde1e596c1377a680185375b7f333513d7`, whose sole parent is `529d9d535198b55b80aedf64141967e6bf66448f`, after its correctly bound three-file candidate completed independent read-only re-audit. The exact OpenPGP-signed committed content was verified, GitHub reports its signature as verified and valid, its single-ref non-force push and remote branch, GitHub commit-object, REST PR-head, and GraphQL PR-head confirmations completed, all three eighth-review threads (`PRRT_kwDOThD5p86VoslV`, `PRRT_kwDOThD5p86VoslY`, and `PRRT_kwDOThD5p86VoslZ`) each received one owner evidence reply and were resolved, leaving 22 total / 22 resolved / 0 unresolved threads, and the PR body was synchronized. The eighth exact top-level `@codex review` request is REST comment `5158492410` / GraphQL comment `IC_kwDOThD5p88AAAABM3hY-g`, created `2026-08-02T14:21:43Z` with exact body `@codex review`. The accepted provenance begins with that correctly bound independent re-audit, not the provenance-invalid cross-worktree implementation receipt.

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

The resulting tenth-review repair closed the cross-type denial stop boundary
for all nine checkpoints, broadened DP-N02 without adding a primary ID,
repaired RF-N12 versus generic check-ID ownership, made the three digest rows
valid GFM while preserving their rendered `||` byte-construction expressions,
and recomputed the PG-1 attestation while retaining all eight owner selections.
That repair is the exact reviewed baseline commit
`ff002444ca10a71d1fcb5688ea6b258b3babe766`.

The tenth exact top-level `@codex review` request produced the eleventh Codex
review, REST review `4891197046` / GraphQL review
`PRR_kwDOThD5p88AAAABI4m-dg`, submitted `2026-08-09T11:07:15Z` against exact
commit `ff002444ca10a71d1fcb5688ea6b258b3babe766`. It reported exactly two P1
findings: lifecycle-start and issuance chronology in thread
`PRRT_kwDOThD5p86XmfkO`, rooted at REST comment `3743561019` / GraphQL comment
`PRRC_kwDOThD5p87fIjU7`; and issued-lease acquisition provenance in thread
`PRRT_kwDOThD5p86XmfkR`, rooted at REST comment `3743561022` / GraphQL comment
`PRRC_kwDOThD5p87fIjU-`.

At the read-only pre-edit snapshot for this separately authorized repair, the
PR was open and unmerged at that exact head, with ten exact top-level
`@codex review` requests, eleven completed Codex reviews, and 28 review
threads: 26 resolved and exactly those two unresolved. Each unresolved thread
was current (`outdated: false`), contained only its bot-authored root, and had
zero owner replies. The published PR body still stated that a fresh review
against `ff002444...` was pending; this task does not update it.

The repository owner selected these two additional commit-invariant choices:

```text
RECEIPT-START-SEMANTICS: RS-1
ISSUED-LEASE-EVIDENCE-BINDING: LB-2
```

The first working-tree implementation attempt for those choices was later
found invalid for acquisition provenance, bootstrap-operation conformance, and
AI primary-owner accounting. Its inherited dirty bytes were not retroactively
authorized. This fresh non-reusable BR-1 bootstrap task instead bound those
exact pre-existing three-file bytes as untrusted input after a successful
protected preflight. The repository owner also selected:

```text
ACQUISITION-PROVENANCE: AP-1
```

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
`SANITIZATION-FINALIZATION: APPLIED-TRUE`. This normative revision encodes all
three repairs without reopening G-1, NR-2, F-1, GR-2, DP-1, FS-1, PG-1,
FSAFE-1, RS-1, LB-2, or AP-1.

The repository documents themselves do not establish the external audit,
commit, push, thread-resolution, PR-body-synchronization, later-review, or
merge state of the revision containing these repairs; those remain separate
external gate records. This file grants no Schema or model implementation,
model-worktree creation, runtime activation, release, or merge authority.

All 11 Schema resources remain `reserved-unpublished`; the validator/toolchain and Schema-before-model gates remain binding. No Schema implementation exists or may begin until `integration-control` approves the validator/toolchain, packaging, dependency and lock, provenance, licensing, security, and release gate and a fresh, separately authorized `schema-contracts` task is issued. No model worktree or model implementation exists, and model-worktree creation and model implementation remain prohibited by the Schema-before-model sequence. This document remains an unpublished design record, not an implemented Schema contract, JSON Schema resource, configuration instance, execution adapter, policy engine, or authorization mechanism.

Nothing in this document grants operational authority. In particular, JSON-valid input shaped like a `TaskContract` is untrusted unless trusted framework logic issued it or validated its issuer, integrity, derivation, bindings, freshness, and current preconditions. A digest or successful Schema validation does not establish authority.

Concrete `HostOverlay`, `TaskContract`, `ExecutionReceipt`, lease, lock, runtime-state, and receipt-delivery records remain host-local and outside the target worktree and portable governance. The resource identifiers in this document are reserved for the first approved Schema baseline but remain unpublished.

## 1. Status, scope, and authority

The `schema-contracts` role owns the normative public JSON Schema contract under `schemas/v1alpha1/`, shared definitions, closed envelopes, Schema-expressible constraints, unknown-field rejection, conspicuously synthetic structural fixtures, the documented Phase 1 static invariants, the normative validation/canonicalization/digest pipeline and validated-canonical-representation contracts, the digest catalog and framing definitions, recorded canonical and raw bytes and expected digest values, non-executable conformance requirements, Schema validation and structural/static contract tests, and directly required Schema documentation. It specifies and records those contracts; it does not implement the project strict decoder, validated canonical instance representation, canonical serializer, digest projection, JCS, hashing, replay, cross-runtime equivalence, production Python models, task resolution, operational routing, live Git inspection, leases, contract issuance, receipt generation, a CLI, adapters, or enforcement. Those executable Phase 1 codec and model responsibilities belong to the future distinct `model-implementation` role after the Schema-before-model gates are satisfied.

The phase boundaries are binding:

- **Phase 1 — structural and static integrity:** JSON Schema validation, strict parsing prerequisites, supported-version checks, object-local invariants, closed-bundle uniqueness and reference integrity, canonical-order checks, and other static checks that need no task intent, host binding, live Git state, lease state, or runtime decision.
- **Phase 2 — deterministic resolution and routing:** actual task-to-`Project` matching, complete `Domain`-set resolution, `RoutingPolicy` execution, unique covering-role selection, and split-or-deny decisions.
- **Phase 3 — Git, runtime, and leases:** live repository/worktree inspection, path containment against a concrete binding, Git operations and locks, runtime coordination, atomic write-lease acquisition, ownership, and release.
- **Phase 4 — contracts and evidence:** trusted `TaskContract` issuance or provenance validation, scope authorization and verification, sanitization, terminalization, `ExecutionReceipt` generation, and receipt delivery.
- **Phase 5 — CLI:** command-line composition over already approved core semantics; it cannot create hidden authority or repair denied state.
- **Phase 6 — adapters:** product-specific execution boundaries that consume valid contracts without changing core policy.

The design preserves the authority and placement rules in the [configuration model](configuration-model.md). Portable customer governance consists of concrete `Project`, `Domain`, `WorktreeRole`, and `RoutingPolicy` instances. Concrete `HostOverlay` instances are host-local restrictive input. Concrete `TaskContract` and `ExecutionReceipt` instances are runtime artifacts. Markdown, task intent, a local binding, a lease, and a receipt cannot independently grant authority.

## 2. Dialect and validation profile

Every planned Schema resource uses JSON Schema Draft 2020-12 and declares:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema"
}
```

The validation profile requires:

- format assertion to be explicitly enabled and tested; format annotation alone is insufficient;
- closed objects at every object level, normally with `additionalProperties: false`, or with an equivalently audited `unevaluatedProperties: false` composition where applicators require it;
- rejection of every unknown field, including unknown nested fields;
- explicit `apiVersion` and `kind` discrimination for the seven kinds;
- a fixed, trusted offline registry containing every resource and required meta-schema;
- hard failure for an unknown or unresolved resource and no network fallback; and
- fixed catalog lookup rather than construction of an identifier from caller-controlled `apiVersion`, `kind`, filenames, or paths.

Schemas use `$defs` for resource-local definitions and absolute `$ref` values for cross-resource references. A fragment may follow an exact cataloged resource ID. Filenames use lower-case kebab-case followed by `.schema.json` and are planned under `schemas/v1alpha1/`. Unsupported or malformed `apiVersion` and `kind` values fail closed; validators must not infer them from filename, shape, package version, or prior success.

## 3. Schema-set revision and frozen resource catalog

The first planned Schema set is `v1alpha1-r1`. Its catalog is frozen below. All entries have status `reserved-unpublished`: the identifiers are reserved for the first baseline, but the resources do not yet exist and are not published or approved.

| resourceName | schemaSetRevision | apiVersion | filename | exact `$id` | kind | dispatchableKind | status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `common.schema.json` | `v1alpha1-r1` | `contextctl.dev/v1alpha1` | `schemas/v1alpha1/common.schema.json` | `urn:uuid:78833fbe-1819-45db-824c-2edb235f2864` |  | `false` | `reserved-unpublished` |
| `resource.schema.json` | `v1alpha1-r1` | `contextctl.dev/v1alpha1` | `schemas/v1alpha1/resource.schema.json` | `urn:uuid:77fb943a-f8f8-491b-beaf-c1b4d9684801` |  | `false` | `reserved-unpublished` |
| `project.schema.json` | `v1alpha1-r1` | `contextctl.dev/v1alpha1` | `schemas/v1alpha1/project.schema.json` | `urn:uuid:d5cecdb5-eadf-491d-80c6-869a7f4d10d9` | `Project` | `true` | `reserved-unpublished` |
| `domain.schema.json` | `v1alpha1-r1` | `contextctl.dev/v1alpha1` | `schemas/v1alpha1/domain.schema.json` | `urn:uuid:2bab91f3-c4d5-43e5-90f6-ffb786b42e65` | `Domain` | `true` | `reserved-unpublished` |
| `worktree-role.schema.json` | `v1alpha1-r1` | `contextctl.dev/v1alpha1` | `schemas/v1alpha1/worktree-role.schema.json` | `urn:uuid:4393a3fc-40da-41be-aca9-4276ddc752fa` | `WorktreeRole` | `true` | `reserved-unpublished` |
| `routing-policy.schema.json` | `v1alpha1-r1` | `contextctl.dev/v1alpha1` | `schemas/v1alpha1/routing-policy.schema.json` | `urn:uuid:5d929622-e8b2-40b4-80aa-5d8630625108` | `RoutingPolicy` | `true` | `reserved-unpublished` |
| `host-overlay.schema.json` | `v1alpha1-r1` | `contextctl.dev/v1alpha1` | `schemas/v1alpha1/host-overlay.schema.json` | `urn:uuid:c0de9354-1096-4cea-9cde-a33ad38ab313` | `HostOverlay` | `true` | `reserved-unpublished` |
| `task-contract.schema.json` | `v1alpha1-r1` | `contextctl.dev/v1alpha1` | `schemas/v1alpha1/task-contract.schema.json` | `urn:uuid:314c8f9e-2554-4ebc-b688-d48598693282` | `TaskContract` | `true` | `reserved-unpublished` |
| `execution-receipt.schema.json` | `v1alpha1-r1` | `contextctl.dev/v1alpha1` | `schemas/v1alpha1/execution-receipt.schema.json` | `urn:uuid:53faa365-c113-4b2d-a9c5-022cd87a21dd` | `ExecutionReceipt` | `true` | `reserved-unpublished` |
| `governance-bundle.schema.json` | `v1alpha1-r1` | `contextctl.dev/v1alpha1` | `schemas/v1alpha1/governance-bundle.schema.json` | `urn:uuid:e1293323-8af3-41ed-a55e-dc0c27f35206` |  | `false` | `reserved-unpublished` |
| `receipt-delivery-result.schema.json` | `v1alpha1-r1` | `contextctl.dev/v1alpha1` | `schemas/v1alpha1/receipt-delivery-result.schema.json` | `urn:uuid:ffa1dcf4-5eb3-4a16-b1b2-be3bc1898684` |  | `false` | `reserved-unpublished` |

Exactly seven entries are dispatchable object kinds. `common.schema.json`, `resource.schema.json`, `governance-bundle.schema.json`, and `receipt-delivery-result.schema.json` are supporting or container resources and do not add governance kinds.

Dispatch by `(schemaSetRevision, apiVersion, kind)` is permitted only for the seven kind Schemas. Supporting resources resolve by exact `resourceName` through the trusted catalog. Resource IDs are immutable after publication: one ID cannot later identify different Schema bytes. Changing a published resource requires a new ID and schema-set revision. Catalog lookup is offline, exact, and non-derivative; UUID possession and Schema validity establish neither ownership nor authority.

## 4. Compatibility and migration

This policy follows [ADR 0003](decisions/0003-versioning-model.md) and does not prohibit every change under an alpha API.

- Before publication, draft v1alpha1 resources may change when each material change is documented. No compatibility promise attaches to an unpublished draft.
- The first independently audited, approved, committed, reviewed, and integrated baseline establishes the first supported v1alpha1 schema-set revision.
- A published Schema resource is immutable. Modified Schema bytes receive a new `$id` and schema-set revision, even when `apiVersion` remains `contextctl.dev/v1alpha1`.
- A documentation-only correction outside a Schema resource needs no Schema revision.
- A compatible Schema correction preserves the accepted/rejected instance set and normative meaning. It still receives a new resource ID if published Schema bytes change.
- Adding an optional property to an object with `additionalProperties: false` is not fully compatible for older validators, because they reject instances that use the new property.
- An incompatible alpha change requires explicit project approval, documented old/new validation handling, migration instructions, and an unambiguous schema-set selector. `apiVersion` alone must not be used to guess between incompatible v1alpha1 revisions.
- `contextctl.dev/v1alpha2` is the normal choice for a clean semantic break. A same-v1alpha1 incompatible revision is an explicit alpha exception, not a silent replacement.
- Silent reinterpretation and silent migration are prohibited. Migration validates and preserves the source, emits a distinct target, validates that target under its selected schema set, and reports the result.
- Loading, validation, canonical hashing, and contract verification never perform migration.

Support for multiple revisions or API versions must use an explicit trusted mapping and retain the exact resources needed to validate supported historical data.

### Pre-publication lease-acquisition correction

The `indeterminate` lease-acquisition branch is a material pre-publication
correction to the earlier four-state draft. Uncertain acquisition cannot be
represented as conclusively `not-acquired`; the separate branch preserves
uncertainty and forces fail-closed cleanup and lifecycle handling. No
published Schema resource or supported instance contract was changed.

The current closed vocabulary is exactly `not-required`, `not-attempted`,
`not-acquired`, `indeterminate`, and `acquired`.

### Pre-publication ordinary-operation-evidence carrier

The owner-selected Review-15 A2 repair adds
`ExecutionReceipt.spec.ordinaryOperationEvidence` as a material
pre-publication wire-shape design change. All resources remain
`reserved-unpublished`; no published Schema resource or supported instance
contract is changed by this design repair. The immediate design retains
`apiVersion: contextctl.dev/v1alpha1`, schema-set revision `v1alpha1-r1`, and
`receiptVersion: "1"`. Compatibility, publication, and final version
confirmation remain an `integration-control` publication/release gate; this
document neither makes that decision nor claims publication.

## 5. Common envelope

Each of the seven object kinds has this closed top-level shape:

```json
{
  "apiVersion": "contextctl.dev/v1alpha1",
  "kind": "Project",
  "metadata": {
    "id": "project.invalid",
    "displayName": "Synthetic project",
    "description": "Conspicuously synthetic design data."
  },
  "spec": {}
}
```

`apiVersion`, `kind`, `metadata`, and `spec` are required. Every object is closed. Each kind Schema fixes `kind` with `const`, fixes `apiVersion` with `const`, and defines its own closed `spec`.

`metadata` contains:

- required `id`: a stable lower-case logical identifier, 1–63 ASCII characters, beginning and ending with an alphanumeric character and containing only alphanumerics, `-`, and `.`; an individual kind may narrow this to a canonical UUID;
- optional `displayName`: 1–128 decoded characters, no control characters, already NFC;
- optional `description`: 1–1024 decoded characters, no control characters, already NFC.

There is no `metadata.name`, label map, or annotation map in v1alpha1. Human-readable text is descriptive only. Length, character, and NFC checks do not prove that a display name is non-identifying or that a description is secret-free; those claims require the controls in section 12.

## 6. Shared definitions

`common.schema.json` will provide the shared structural vocabulary. “Static” below means Phase 1 validation after parsing and JSON Schema validation. “Later” means the identified operational phase, not authority created by the definition.

| Definition | Planned representation and JSON Schema enforcement | Phase 1 static validation | Later operational validation |
| --- | --- | --- | --- |
| API version | String constant `contextctl.dev/v1alpha1` | Supported schema-set selection is explicit | Future loaders reject unsupported mappings without guessing |
| Kind discriminator | One of the seven exact PascalCase strings in its dispatchable Schema | Catalog mapping must be unique | Trusted dispatch uses the fixed mapping only |
| Logical identifier | Lower-case ASCII, 1–63 characters, alphanumeric endpoints, internal alphanumerics, `-`, or `.` | Already NFC; uniqueness in its closed namespace | Identity binding must match current authoritative inputs |
| Reason code | Canonical `reasonCode` defined below | Already canonical; set-like arrays use `S(code)` | Identifier only; grants no authority |
| Profile identifier | Canonical `profileIdentifier` defined below | Already canonical | Identifies a declared profile; grants no authority |
| Check identifier | Canonical `checkIdentifier` defined below | Already canonical and unique within one receipt | Binds evidence records only; grants no authority |
| Sanitized summary | 1–1024-character `sanitizedSummary` value profile defined below; presence is decided by each containing record | Already NFC and free of ASCII controls | Phase 4 plus external controls establish actual sanitization |
| Canonical UUID | Lower-case canonical UUID string with `format: uuid` and a lexical pattern | Version-specific constraints where required | Identity does not prove issuer or ownership |
| Display text | Bounded string without control characters | Already NFC; fixture hygiene | Phase 4 sanitizes text copied into evidence; external classification still applies |
| Repository-relative path | POSIX `/` separators; no leading slash, drive prefix, backslash, empty segment, `.` segment, `..` segment, exact `.git` component, NUL, or trailing slash; maximum 4096 characters | Strict UTF-8, already NFC, exact case-sensitive `.git`-component exclusion, canonical spelling, and set ordering | Phase 3 resolves against the bound canonical root, rejects administrative aliases and indirection, and checks containment live |
| Path pattern | Repository-relative grammar over the valid `repositoryRelativePath` universe; `*` and `?` stay within a segment and `**` is allowed only as a complete segment; a literal component exactly `.git`, negation, backslash, brace expansion, and host absolute syntax are invalid | Pattern parse succeeds; literal `.git` components reject; D10 language relationships are decided exactly by its finite-automata inclusion proof over the revised universe | Phase 2 resolves task coverage; Phase 3 checks concrete effects and administrative-path boundaries |
| Absolute host path | Closed two-branch `{ platform, value }` union defined below; both fields are required and no other field is permitted | Enforce strict UTF-8/scalar/NFC, length, control, segment, POSIX, drive-only Windows, UNC-rejection, and exact-equality rules | Phase 3 checks actual host compatibility, filesystem identity, registration, aliases, and containment |
| Object reference | Closed `{ apiVersion, kind, id }` object | Target kind, uniqueness, existence, and bundle association where applicable | Later phases bind the reference to the selected runtime object |
| Mode | Enum `plan-only` or `implementation` | `plan-only` with `allowWrite: true` is rejected | Phase 4 checks requested/effective mode against authority |
| `allowWrite` | Required Boolean where used; omission is never treated as true | Contradictory mode/write combinations rejected | Phase 3 lease and Phase 4 contract checks remain mandatory |
| Capability | Enum `inspect`, `validate`, `create`, `modify`, `delete`, `execute-tests`, `execute-build`, `git-stage`, `git-commit`, `git-branch`, `git-remote`, `network`, or `external-secret-use` | Unknown values and permitted/prohibited overlap rejected | Phases 2–4 calculate the restrictive intersection; the token itself grants nothing |
| Tagged digest | String `sha256:` followed by exactly 64 lower-case hexadecimal digits | Projection identifier and digest placement checked | Phase 4 verifies provenance and the exact protected bytes; a digest is not authentication |
| Git object ID | Closed `{ algorithm, value }`; `algorithm` is `sha1` or `sha256`, with 40 or 64 matching lower-case hex characters | Algorithm/value lengths agree | Phase 3 obtains and compares the live object ID |
| Git mode | String enum `100644`, `100755`, `120000`, or `160000`; never a JSON number | Exact enum | Phase 3 observes the live mode |
| Branch reference | Fully qualified `refs/heads/...` string using the `gitRefIdentifier` profile below | Allowed/denied policy contradictions checked | Phase 3 reads the symbolic branch live |
| Reference state | Closed `branch`/`detached` union defined for `expectedBaseline.ref` below | Union and local consistency | Phase 3 distinguishes symbolic and detached state live |
| HEAD state | Closed `commit`/`unborn` union defined for `expectedBaseline.head` below | Union and local consistency, including detached/unborn rejection | Phase 3 observes the object identity or unborn state live |
| Timestamp | Named `canonicalUtcTimestamp` string in exact whole-second UTC form `YYYY-MM-DDTHH:MM:SSZ`; future Schema uses the exact pattern below plus asserted `format: date-time` | Exact lexical, Gregorian-calendar, year, and chronology validation below; no normalization | Phase 4 uses a trusted clock and checks authenticity and operational freshness |
| Freshness boundary | Closed `{ issuedAt, expiresAt }` | Both timestamps present and `expiresAt` later than `issuedAt` | Phase 4 evaluates current time and policy bounds |
| Task, contract, lease, receipt ID | Canonical lower-case UUID; contract and receipt IDs narrow their envelope `metadata.id` | Uniqueness in the loaded artifact set | Trusted lifecycle logic checks ownership, derivation, and task binding |
| Structured remote | Closed `{ transport, host, port?, namespace, repository }`; transport is `https` or `ssh`; `host` uses `remoteDnsHost`; `namespace` is an ordered bounded segment array; `repository` uses `remoteRepositoryName`; optional `port` is an integer from 1 through 65535 under the numeric profile | Exact lexical profiles, default-port omission, `J(remote)` identity, canonical ordering, and exact HostOverlay membership below | Phase 3 parses and compares observed remotes live without exposing credentials |
| Repository identity | Closed object with non-empty `acceptedRemotes` | Canonical uniqueness and portable-only content | Phase 3 observes and matches the target repository live |
| Remote expectation | Closed `{ remoteName, acceptedRemotes }`; `acceptedRemotes` is required and non-empty | One record per `remoteName`; outer records are unique and ordered by `S(remoteName)`, and nested remotes are unique and ordered by `J(remote)` | Phase 3 compares the observed Git remote for that name with the accepted set |
| Worktree logical identity | Logical `worktreeId` plus a `WorktreeRole` reference where required; never an absolute path | Reference existence in a closed set | Host binding and registration are checked in Phases 2–3 |
| Check outcome | One required `outcome` field under a closed `checkType` conditional: `execution` uses `succeeded`, `failed`, `cancelled`, or `indeterminate`; every non-execution type uses `passed`, `failed`, or `indeterminate` | Reject cross-phase and unknown values; do not add a second execution result or detail field | Phase 4 records evidence without turning it into authority |
| Execution outcome | Enum `not-attempted`, `succeeded`, `failed`, `cancelled`, or `indeterminate` | — | Phase 4 derives it from the attempt |
| Verification outcome | Enum `not-performed`, `passed`, `failed`, or `indeterminate` | — | Phase 4 derives it from post-execution verification |
| Release outcome | Enum `not-required`, `succeeded`, `failed`, or `indeterminate` | — | Phase 3 supplies ownership-checked release evidence |
| Lifecycle outcome | Enum `denied`, `succeeded`, `failed`, `cancelled`, or `indeterminate` | Cross-field combinations are structurally bounded | Phase 4 derives the terminal outcome; it does not imply lease release |
| Receipt-delivery outcome | Enum `not-attempted`, `succeeded`, `failed`, or `indeterminate` | — | Phase 4 records the post-finalization delivery attempt separately |
| Scope | Closed `{ capabilities, paths }` with both arrays present; `paths` contains path patterns over the revised valid `repositoryRelativePath` universe | Arrays canonical; allowed/prohibited sets disjoint and containment checked where statically provable; reserved `.git`-component paths are never members of an ordinary scope language | Phases 2–4 calculate effective scope and verify effects, with Git administrative effects outside ordinary path scope |
| Permitted transition | One of exactly seven closed, target-keyed branches defined under `TaskContract`; active-operation and administrative-lock are not contract transitions | Target uniqueness and canonical target order before hashing | Phases 3–4 compare a live transition against immutable baseline authority |
| Required postcondition | One of the eleven closed branches defined under `TaskContract`; `active-operations` and `administrative-locks` expectations are none-only, and no open postcondition name or generic expected record exists | Type uniqueness, required `scope-contained`, and exact nested-state consistency | Phase 4 checks fresh observations after execution |

The check-outcome conditional has exactly two branches, four allowed values for
an `execution` check, three allowed values for a non-execution check, and five
distinct outcome tokens across both branches. It rejects `passed` for
`execution`, rejects `succeeded` and `cancelled` for every other check type, and
rejects every unknown value. `failed` and `indeterminate` are the only shared
tokens. The single `outcome` member carries the complete result; there is no
second execution-result, detail, mapping, or lossy cancellation field.

A structured remote uses lower-case canonical host text and ordered `namespace` segments. Default transport ports must be omitted so equivalent remotes do not acquire multiple encodings. Secret-bearing URLs, user-info, tokens, private-key material, and environment-derived host data are not representable fields.

### Portable repository-relative paths and patterns

The named `repositoryRelativePath` profile first requires strict UTF-8
decoding to Unicode scalar values and then requires the decoded value to be
already NFC. Validators reject rather than decode permissively, normalize, or
repair. The resulting value uses POSIX `/` separators, is at most 4096 decoded
characters, and has no leading slash, drive prefix, backslash, empty segment,
`.` segment, `..` segment, NUL, or trailing slash.

After those decoding and NFC checks, split the value into `/`-separated
components. The value is invalid when any component is exactly `.git` under
case-sensitive equality. The reservation applies at every component position,
not only at the root. There is no case folding, alias expansion,
normalization, or repair. These values are therefore invalid:

```text
.git
.git/config
.git/hooks/pre-commit
.git/worktrees/example/HEAD
foo/.git
foo/.git/config
nested/repository/.git/HEAD
```

The reservation is deliberately narrow. Similar names remain valid when they
satisfy every other rule, including:

```text
.gitignore
.gitmodules
.github
foo.git
dir/.gitignore
dir/.github/workflow.yml
```

Path-pattern syntax retains its existing anchored `*`, `?`, and
complete-segment `**` grammar, but every pattern language is defined only over
the revised universe `U` of valid `repositoryRelativePath` values. A pattern
containing a literal component exactly equal to `.git` is itself invalid;
validators do not normalize it into another language. Required invalid
examples are:

```text
.git/**
.git/config
foo/.git/**
foo/.git/config
```

The broad pattern `**` remains valid, but it cannot match a value containing
an exact `.git` component because no such value belongs to `U`. Wildcards do
not reintroduce excluded values, and no broader similar-name reservation is
implied.

This same universe and pattern language apply without exception to Domain path
scope, WorktreeRole-derived path scope, HostOverlay path ceilings,
RoutingPolicy/static path-language inclusion, TaskContract authorized and
prohibited scopes, baseline path-keyed entries, required-postcondition
path-keyed entries, receipt `changedPaths`, and `scope-contained` verification
evidence. An ordinary `modify` capability combined with `**` therefore cannot
authorize `.git/config`, `.git/hooks/pre-commit`, refs, linked-worktree
metadata, or other Git administrative state. The separate `git-stage`,
`git-commit`, `git-branch`, and `git-remote` capability tokens do not convert a
Git administrative location into an ordinary repository-relative path and do
not authorize direct filesystem mutation of reserved administrative state.

An observed effect on a runtime-resolved Git administrative location is
outside ordinary repository path scope. It cannot be represented as a
successful ordinary `changedPaths` member, must make `scope-contained` fail or
become indeterminate according to the evidence available, and must not be
silently omitted while claiming successful scope verification. Phase 1 does
not claim to identify every host-local administrative path.

Phase 3 owns live resolution and rejection of a top-level `.git` file that
points elsewhere; the linked-worktree administrative directory; the common
Git directory; Git administrative paths outside the worktree root; symlink,
junction, reparse-point, alias, or other filesystem-indirection paths;
case-folded aliases; Windows 8.3 aliases; Unicode-normalized aliases;
registered-submodule administrative roots; and nested repositories and their
administrative roots. Portable governance must not record those host-specific
resolved paths. It does not normalize an alias into a portable path; runtime
ambiguity or aliasing fails closed.

### Canonical whole-second UTC timestamp profile

The one shared timestamp value profile is named `canonicalUtcTimestamp`. Its
only accepted lexical form is `YYYY-MM-DDTHH:MM:SSZ`, with this exact pattern:

```text
^[0-9]{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])T(?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]Z$
```

The lexical pattern is necessary but does not by itself establish calendar
validity. Phase 1 static validation additionally requires years `0001` through
`9999`, rejects year `0000`, and applies the Gregorian calendar and ordinary
Gregorian leap-year rules. February 29 is valid only in a leap year. Hours are
`00` through `23`, minutes and seconds are `00` through `59`, leap second
`60` is invalid, and `24:00:00` is invalid. Upper-case `T` and terminal `Z`
are mandatory. Fractional seconds, a trailing decimal point, UTC-offset
spellings, lower-case `t` or `z`, signed or five-digit years, missing zero
padding, and leading, trailing, or internal whitespace are invalid. The
accepted spelling is already canonical: validators reject rather than
uppercase, trim, pad, remove an offset or fraction, add `Z`, normalize, or
repair a date.

Future JSON Schema resources apply `type: string`, the exact pattern above, and
asserted `format: date-time` as an additional check rather than as the
canonicality definition. The project profile controls whenever a library's
broader `date-time` interpretation differs. This profile applies to exactly
these nine current field paths and creates no new timestamp field:

1. `TaskContract.spec.issuanceCheckpoint.observedAt`
2. `TaskContract.spec.freshness.issuedAt`
3. `TaskContract.spec.freshness.expiresAt`
4. `ExecutionReceipt.spec.startedAt`
5. `ExecutionReceipt.spec.finishedAt`
6. `ExecutionReceipt.spec.sanitization.completedAt`
7. `ExecutionReceipt.spec.checks[].observedAt`
8. `ExecutionReceipt.spec.origin.preContractEvidence.observedAt`
9. `ReceiptDeliveryResult.attemptedAt`

Phase 1 owns exact lexical enforcement, year-zero rejection, calendar and
leap-year validity, and comparison of the represented instants under the 31
displayed chronology relations below: 20 primitive/additive relations and eleven
derived/non-additive consequences. Future
`model-implementation` owns strict
decoding into the validated representation, executable parser conformance, and
instant-comparison implementation. Phase 4 owns trusted current time,
timestamp authenticity, operational freshness, and evidence that an event
occurred at the stated instant. Phase 1 uses no trusted clock; syntax and
ordering grant no authority.

Required future positive timestamp vectors cover exactly these classes:

1. `0001-01-01T00:00:00Z`;
2. `9999-12-31T23:59:59Z`;
3. `2000-02-29T00:00:00Z`;
4. `2004-02-29T23:59:59Z`;
5. a valid ordinary date in a non-leap year;
6. every current protected timestamp literal;
7. strict chronology progression;
8. every currently permitted equality boundary;
9. the strict freshness relation with whole-second separation; and
10. valid contract/receipt and receipt/delivery pairs.

Required future negative timestamp vectors independently reject:

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
24. otherwise valid chronology expressed through an invalid lexical spelling.

The eight current protected literal values from
`2000-01-01T00:00:00Z` through the existing `2000-01-01T00:01:00Z` value
occur 192 times in the mechanically recounted PG-1 broad region and remain
byte-identical.

### Canonical identifiers, Git references, and sanitized text

A `reasonCode` is an already-canonical lower-case ASCII identifier with this
form:

```text
reason.<segment>[.<segment>...]
```

Each segment is 1 through 32 characters, begins and ends with `[a-z0-9]`, and
may contain `-` only internally. Equivalently, a segment is either one
`[a-z0-9]` character or matches
`[a-z0-9][a-z0-9-]{0,30}[a-z0-9]`. The complete reason code is 8 through 160
characters. Examples are `reason.policy.denied`, `reason.git.head-mismatch`,
and `reason.lease.release-failed`. Reason codes are identifiers rather than
free text, grant no authority, MUST already be canonical, and MUST NOT be
silently normalized. Every reason-code array is set-like, unique, and ordered
by `S(code)`.

A `profileIdentifier` has the form
`profile.<segment>[.<segment>...]`, and a `checkIdentifier` has the form
`check.<segment>[.<segment>...]`. Both use the same segment grammar and
160-character maximum as `reasonCode`; their minimum total lengths are 9 and 7
characters respectively. Examples are `profile.validation.v1`,
`profile.sanitization.v1`, `profile.digest.receipt-v1`, and
`check.initial-preflight`. These values identify declared profiles or checks
only and grant no authority. They MUST already be canonical and MUST NOT be
silently normalized.

A `gitRefIdentifier` is an already-NFC ASCII string 6 through 1024 characters
long. It begins with `refs/` and has one or more non-empty `/`-separated
segments after that prefix. Each segment is 1 through 255 characters, contains
only ASCII letters, digits, `.`, `_`, or `-`, does not begin or end with `.`,
does not end with `.lock`, and does not contain `..`. A `branchRef` is a
`gitRefIdentifier` beginning with `refs/heads/` and containing at least one
segment after `heads`. These deliberately restricted profiles reject every
space, control character, `~`, `^`, `:`, `?`, `*`, `[`, backslash, repeated or
trailing slash, and implementation-specific Git shorthand rather than relying
on host normalization.

#### Closed `branchPrefix` and `branchPolicy` profile

A `branchPrefix` is exactly a valid `branchRef`. It therefore is an
already-NFC ASCII string, begins with `refs/heads/`, contains at least one
non-empty branch-name segment after `heads`, and inherits the complete
`gitRefIdentifier` and `branchRef` total-length, segment-length, permitted-
character, leading-dot, trailing-dot, `.lock`, `..`, repeated-slash, trailing-
slash, control-character, and Git-shorthand restrictions. It is not empty,
cannot equal only `refs/heads/`, does not end in `/`, and contains no wildcard,
glob, regular-expression, template, variable, or placeholder syntax. Every
otherwise permitted character, including `.`, is literal. The value is stored
exactly and is never case folded, normalized, rewritten, or suffixed with a
stored separator.

For one validated symbolic `branchRef` named `branch` and one validated
`branchPrefix` named `prefix`, define the inclusive component-prefix predicate:

```text
branchPrefixMatches(prefix, branch) =
  branch == prefix
  OR
  branch starts with prefix + "/"
```

Comparison is exact ASCII-byte comparison over the already validated values.
The appended `/` is part of the comparison operation and is not stored in the
prefix. Therefore `refs/heads/release` matches itself,
`refs/heads/release/2026`, and `refs/heads/release/2026/july`; it does not match
`refs/heads/release-malicious`, `refs/heads/releases`,
`refs/heads/releas`, or `refs/heads/release_candidate`. Raw character-prefix
matching and descendants-only matching are forbidden. A stored trailing-slash
namespace and every wildcard catch-all are invalid.

`WorktreeRole.spec.branchPolicy` is a closed object with required closed
`allowed` and `denied` objects. Those objects contain exactly these four
required arrays and no other members:

| Field | Exact value type, identity, and order |
| --- | --- |
| `allowed.exact` | set-like `branchRef[]`, unique and strictly ordered by `S(branchRef)` |
| `allowed.prefixes` | set-like `branchPrefix[]`, unique and strictly ordered by `S(branchPrefix)` |
| `denied.exact` | set-like `branchRef[]`, unique and strictly ordered by `S(branchRef)` |
| `denied.prefixes` | set-like `branchPrefix[]`, unique and strictly ordered by `S(branchPrefix)` |

Every array may be empty, is rejected when it contains a duplicate or is not
already canonically ordered, and is never silently sorted. One valid prefix
may contain another valid prefix; that redundancy is permitted. Exact and
prefix entries may overlap within or across allow and deny classes. Validation
does not normalize, infer, collapse, or remove such entries; the evaluation
below remains deterministic and deny precedence resolves every allow/deny
overlap.

For one observed symbolic branch `B`, define:

```text
allowExact =
  B equals any allowed.exact value

allowPrefix =
  branchPrefixMatches(P, B)
  for any P in allowed.prefixes

denyExact =
  B equals any denied.exact value

denyPrefix =
  branchPrefixMatches(P, B)
  for any P in denied.prefixes

allowMatch = allowExact OR allowPrefix
denyMatch = denyExact OR denyPrefix

branchPolicyEligible =
  allowMatch == true
  AND
  denyMatch == false
```

Any exact or prefix deny match overrides every allow match. No allow match is
denial; both allow arrays empty deny every symbolic branch. Empty deny arrays
create no permission. Exact-allow/exact-deny, exact-allow/prefix-deny, prefix-
allow/exact-deny, prefix-allow/prefix-deny, and several allow matches plus one
deny match all deny. There is no implicit allow-all state, no wildcard allow-
all prefix, and `refs/heads/` is not a valid catch-all prefix.

A symbolic branch with a valid `branchRef` is evaluated normally. A detached
HEAD has no `branchRef` and fails branch-policy eligibility. A symbolic unborn
branch may be evaluated by its symbolic `branchRef`, but the separate expected-
baseline and HEAD-state rules still decide whether the unborn state is
permitted. Branch-policy success does not prove the current live branch, HEAD
object, worktree registration, or repository state.

Phase 1 owns `branchRef` and `branchPrefix` lexical validation, the closed
`branchPolicy` structure, uniqueness and canonical order, the exact and
inclusive component-prefix semantics, deny precedence, and statically provable
contradictions. Phase 3 owns live symbolic/detached/unborn observation, actual
branch comparison, HEAD-state verification, worktree registration, branch
binding, and repository state.

The seven required planned positive vectors are:

1. exact allow with no deny;
2. prefix equality for branch and prefix `refs/heads/release`;
3. descendant `refs/heads/release/2026` under `refs/heads/release`;
4. deep descendant `refs/heads/release/2026/july` under that prefix;
5. one valid prefix contained by another, with deterministic allow;
6. simultaneous exact and prefix allow with no deny; and
7. an otherwise allowed symbolic unborn branch, still subject to the separate
   unborn HEAD-state gate.

The 33 required planned negative vectors are:

1. empty prefix;
2. `refs/heads/`;
3. stored trailing-slash prefix;
4. repeated slash;
5. empty component;
6. malformed `branchRef` component;
7. leading dot;
8. trailing dot;
9. `.lock` suffix;
10. `..`;
11. wildcard or glob syntax;
12. regular-expression syntax;
13. `refs/heads/release-malicious` does not match
    `refs/heads/release`;
14. `refs/heads/releases` does not match `refs/heads/release`;
15. `refs/heads/releas` does not match `refs/heads/release`;
16. no allow match;
17. both allow arrays empty;
18. exact allow plus exact deny;
19. exact allow plus prefix deny;
20. prefix allow plus exact deny;
21. prefix allow plus prefix deny;
22. several matching allows plus one matching deny;
23. detached HEAD;
24. duplicate value in `allowed.exact`;
25. duplicate value in `allowed.prefixes`;
26. duplicate value in `denied.exact`;
27. duplicate value in `denied.prefixes`;
28. non-canonical ordering in each of the four arrays;
29. raw character-prefix behavior that would match a partial component;
30. branch-policy success paired with a mismatching live branch observation;
31. symbolic unborn branch rejected by the separate HEAD-state rules;
32. a deny prefix equal to an allowed exact branch; and
33. an exact deny equal to a branch matched by an allow prefix.

All are planned contract vectors. They do not claim that a fixture or
executable test exists.

Where a field uses the `sanitizedSummary` value profile, its value is an
already-NFC string of 1 through 1024 decoded Unicode characters with none of
U+0000 through U+001F or U+007F. The value profile defines string validity
only; each containing record independently requires or permits presence.
Schema validity proves only this shape. Phase 4 sanitization plus external
classification, DLP, review, and evidence-access controls are still required
to establish that the content is safe.

### Canonical structured-remote profile

A structured remote is one closed record with required `transport`, `host`,
`namespace`, and `repository`, optional `port`, and no other field.
`transport` is exactly `https` or `ssh`. There is no raw-URL field, and no
field may represent user-info, credentials, a token, a password, private-key
material, a query, a fragment, URI-scheme text, or environment-derived secret
material.

The named `remoteDnsHost` profile accepts lower-case ASCII DNS names only.
The complete host is 3 through 253 ASCII characters including dots and has at
least two labels separated by exactly one dot. Each label is 1 through 63
characters and matches:

```text
[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?
```

Each label therefore has alphanumeric endpoints. Empty labels, a leading or
trailing dot, repeated dots, leading or trailing label hyphens, underscores,
uppercase ASCII, whitespace, controls, Unicode, `xn--` labels, IDNA conversion,
IPv4 or IPv6 literals, bracketed literals, zone identifiers, single-label
hosts, and `localhost` are invalid. Validators neither normalize nor case-fold.
The synthetic `repo.invalid` value remains valid; the `.invalid` suffix is
lexically accepted but proves neither reachability, DNS truth, ownership, nor
security.

`port` remains an optional integer from 1 through 65535 under the existing
numeric profile. The exact default table is `https -> 443` and `ssh -> 22`.
An omitted port means exactly the selected transport's default. Explicit
`https` port `443` and explicit `ssh` port `22` are invalid; a non-default
endpoint includes its non-default port. Zero, values above 65535, negative
values, strings, and fractions are invalid, and no default exists outside the
two-entry table. Validators do not add, remove, or otherwise repair a port.

`namespace` is an ordered, non-empty array of 1 through 16 lower-case ASCII
segments. Each segment is 1 through 63 characters, the joined namespace with
`/` separators is at most 1023 characters, and every segment matches:

```text
[a-z0-9](?:[a-z0-9._-]{0,61}[a-z0-9])?
```

Segments have alphanumeric endpoints. An empty segment, `.` or `..` segment,
any `..` substring, slash or backslash, whitespace, control, uppercase, or
Unicode is invalid. No normalization, path decoding, or separator inference is
performed. Segment order is significant and validators do not sort it. A
literal `.git` substring is permitted in a namespace segment when all other
rules pass. The protected `namespace: ["synthetic"]` remains valid.

The distinct named `remoteRepositoryName` profile is one lower-case ASCII
string segment of 1 through 128 characters, with alphanumeric first and final
characters and only lower-case letters, digits, `.`, `_`, and `-` internally.
Empty values, slash or backslash, whitespace, controls, uppercase, Unicode,
leading or trailing dot or hyphen, any `..` substring, and values equal to `.`
or `..` are invalid. No normalization or path parsing occurs. The protected
`governance` value remains valid.

An otherwise valid repository value ending in the exact lower-case `.git`
suffix is invalid. Because uppercase is outside the canonical language, an
ASCII-case-insensitive terminal `.git` representation is also outside the
selected profile. Validators do not strip or append the suffix, alias suffixed
and unsuffixed names, or silently convert a live remote into configuration.
Phase 3 owns later parsing of observed Git remotes under its approved contract.

After complete validation, structured-remote identity is exact `J(remote)` over
the full closed record. Because explicit default ports are invalid, this is
equivalent to exact equality of `(transport, host, effective port, ordered
namespace, repository)`, where effective port is the explicit non-default port
or the omitted transport default. Effective-port comparison never makes an
explicit default valid. Each `acceptedRemotes` array is set-like: duplicate
`J(remote)` values reject and values must already be strictly ordered by
`J(remote)`; validators do not sort. Several distinct valid remotes may occur
under one `remoteName`. In the outer `remoteExpectations` array, `remoteName`
remains the sole record identity and occurs at most once. HostOverlay narrowing
requires exact membership under this validated equality and must not ignore a
field, compare an alias, strip `.git`, add a default-port field, or widen the
accepted set.

Required future positive structured-remote vectors cover:

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

Required future negative structured-remote vectors independently reject:

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

Phase 1 owns these lexical profiles, closed shape, canonicality, equality,
uniqueness, ordering, and static HostOverlay inclusion. Future
`model-implementation` owns strict decoding and executable conformance. Phase 3
owns live Git-remote observation, transport parsing, repository comparison, and
runtime host facts. Phase 4 owns trusted authority and the contract/evidence
lifecycle. A canonical remote is an identity value, not proof of network
ownership or trust.

### Closed `absoluteHostPath` profile

Every `absoluteHostPath` is exactly one of these two records:

```json
{
  "platform": "posix",
  "value": "<posixAbsoluteHostPath>"
}
```

or:

```json
{
  "platform": "windows",
  "value": "<windowsDriveAbsoluteHostPath>"
}
```

Both records are closed. `platform` and `value` are required, and no other
field is permitted. The discriminator selects only the lexical branch; it
does not prove that the path is compatible with or present on the current
host.

For both branches, `value`:

- is decoded from strict UTF-8 and contains only Unicode scalar values;
- is already NFC, with validation rejecting rather than normalizing;
- contains from 1 through 4096 decoded Unicode scalar values, including all
  root syntax and separators;
- contains none of U+0000 through U+001F or U+007F through U+009F; and
- participates in exact static equality as the tuple `(platform, value)`.

Phase 1 performs no case folding, slash replacement, path resolution,
filesystem normalization, alias resolution, or symlink resolution. It
preserves the validated spelling exactly.

#### POSIX branch

The exact POSIX grammar is:

```text
"/" | "/" segment ("/" segment)*
```

A POSIX `segment` is non-empty, contains neither `/` nor `\`, contains no
prohibited control, is not exactly `.` or `..`, and is already NFC. Therefore
`/` is valid; relative paths, repeated separators, dot and dot-dot traversal
segments, and a trailing separator other than the root are invalid.
Backslash is neither an alternate separator nor an ordinary permitted segment
character.

#### Windows branch — drive-only

The exact Windows grammar is:

```text
[A-Z]:\ | [A-Z]:\segment(\segment)*
```

A Windows `segment` is non-empty, is already NFC, contains no prohibited
control, and contains none of `< > : " / \ | ? *`. It is not exactly `.` or
`..`, does not end with ASCII space, and does not end with `.`.

Define `deviceBase(segment)` as the substring before the first `.`, or as the
complete segment when no `.` occurs. Compare the device base using ASCII
case-insensitive equality. A segment is invalid when its device base is
`CON`, `PRN`, `AUX`, `NUL`, `CLOCK$`, `COM1` through `COM9`, or `LPT1`
through `LPT9`. The rule also rejects extensions such as `CON.txt` and
`LPT1.log`.

The Windows branch supports uppercase-drive absolute paths only. It rejects
every UNC path beginning with `\\`; the `\\?\` and `\\.\` device namespaces;
lowercase drive letters; drive-relative paths such as `C:relative`;
current-drive-rooted paths such as `\relative`; forward slashes; mixed
separators; repeated backslashes; empty segments; and trailing backslashes
except for the drive root. Spelling, including segment and drive-letter case,
is preserved exactly after validation. UNC support is intentionally absent
from `v1alpha1-r1` and requires an explicit, separately reviewed
Schema-contract revision.

#### Phase ownership and required vectors

Phase 1 owns the closed union shape, lexical grammars, strict UTF-8,
Unicode-scalar and already-NFC checks, decoded-scalar length, control and
character exclusions, root and segment rules, drive-only and UNC rejection,
reserved-device checks, and exact `(platform, value)` equality.

Phase 3 owns actual host-platform compatibility, filesystem existence,
canonical filesystem identity, drive availability, host-applicable
case-insensitive identity, aliases, symlinks and junctions, containment,
worktree registration, and real-path comparison. Structural validity never
proves that a host path exists or is safe to use.

Required conspicuously synthetic positive vectors include POSIX `/`,
`/srv/synthetic.invalid/worktree`, and
`/srv/synthetic.invalid/例`, plus Windows `C:\`,
`C:\Synthetic.Invalid\Worktree`, and `C:\Synthetic.Invalid\例`.

Required negative vectors cover:

- an empty value and a value of exactly 4097 decoded Unicode scalar values;
- a relative POSIX path, repeated POSIX separator, trailing non-root POSIX
  separator, `.` and `..` POSIX segments, and a POSIX backslash;
- a non-NFC value and each prohibited scalar from U+0000 through U+001F and
  U+007F through U+009F;
- a lowercase Windows drive, drive-relative path, current-drive-rooted path,
  UNC path, and both device namespaces;
- a forward slash, mixed separators, repeated backslash, trailing non-root
  backslash, and empty Windows segment;
- each forbidden Windows punctuation character, a segment ending in ASCII
  space, a segment ending in `.`, and `.` and `..` Windows segments; and
- every reserved device base, ASCII-case variants, every `COM1` through
  `COM9` and `LPT1` through `LPT9` member, and a reserved device base with an
  extension.

### Deterministic JSON-number profile

The selected `v1alpha1-r1` numeric profile is identified as
`profile.number.v1alpha1-r1`. Every JSON number in an instance MUST be a
non-negative canonical decimal integer whose raw token matches exactly:

```text
0|[1-9][0-9]*
```

Every such value MUST be no greater than `9007199254740991`, the largest
integer exactly representable in the RFC 8785 / IEEE 754 binary64
interoperability profile. The profile forbids negative values, `-0`, a leading
plus sign, leading zeros, fractions, decimal points, exponent notation,
integer-equivalent forms such as `1.0` and `1e0`, NaN, Infinity, and every
implementation-specific non-JSON numeric extension. No floating-point or
signed numeric instance field exists in `v1alpha1-r1`; a future need for one
requires an explicit Schema-contract revision.

Raw numeric-token validation occurs during strict parsing before ordinary
numeric conversion can erase lexical form. JSON Schema `type: integer` is
insufficient because a validator may accept a mathematically integral decimal
or exponent token. A JSON number in a field not explicitly declared numeric is
rejected structurally. The complete current numeric-field inventory and bounds
are:

| Numeric instance field | Minimum | Maximum |
| --- | ---: | ---: |
| `RoutingPolicy.spec.rules[].priority` | 0 | 1000 |
| Structured remote `port` | 1 | 65535 |
| `indexEntry.stage` | 0 | 0 |
| Warning `sequence` | 0 | 4095 |
| Check `sequence` | 0 | 4095 |
| `ExecutionReceipt.spec.sanitization.redactionCount` | 0 | 4294967295 |

Warning and check arrays therefore contain at most 4096 records, with sequence
values contiguous from zero. `redactionCount` is an unsigned 32-bit count.
`contractVersion` and `receiptVersion` remain strings. Lengths and array limits
used as JSON Schema keywords are Schema metadata rather than numeric instance
fields. There are no other numeric instance fields in `v1alpha1-r1`; adding
one requires this document to assign an exact range before implementation.

## 7. Seven object-kind designs

The fields below are planned contract fields. They do not create instances or implement the later-phase behavior they describe.

### `Project`

Required `spec` fields:

| Field | Design |
| --- | --- |
| `repositoryIdentity` | Portable credential-free identity with one or more accepted structured remotes |
| `secureDefaults` | Closed `{ mode: "plan-only", allowWrite: false }` |
| `permissions` | Closed `modes`, `permittedCapabilities`, and `prohibitedCapabilities` arrays |
| `domainRefs` | Non-empty set of `Domain` references |
| `worktreeRoleRefs` | Non-empty set of `WorktreeRole` references |
| `routingPolicyRef` | One `RoutingPolicy` reference |

Static validation requires unique existing references of the declared kinds, a routing policy associated with the same Project, canonical arrays, and disjoint permitted/prohibited capabilities. Project defaults are always plan-only/no-write; later governance may permit implementation only through explicit restrictive evaluation. A `Project` contains no host path, concrete worktree binding, observed Git state, lease, contract, receipt, or secret.

### `Domain`

Required `spec` fields:

| Field | Design |
| --- | --- |
| `projectRef` | The owning `Project` reference |
| `responsibility` | Bounded descriptive text; it is not routing input by itself |
| `pathScope` | Closed non-empty `include` and optional `exclude` pattern arrays |
| `permissions` | Permitted/prohibited mode and capability restrictions |
| `overlapRefs` | Canonical set of other Domains whose declared scope may overlap |

A Domain cannot reference itself. Overlap references must exist, remain within the Project, and be symmetric in a closed bundle. Every `pathScope` pattern is parsed over the revised valid `repositoryRelativePath` universe; a literal exact `.git` component is invalid, and `**` cannot cover a reserved path. Phase 1 may identify undeclared or contradictory overlaps when the path grammar proves them, but does not resolve a real task to Domains. Include/exclude application, complete task coverage, and ambiguity are Phase 2. Domains contain neither host paths nor live state.

### `WorktreeRole`

Required `spec` fields:

| Field | Design |
| --- | --- |
| `projectRef` | The associated `Project` reference |
| `roleClass` | Enum `implementation`, `review`, or `integration-control` |
| `ownedDomainRefs` | Non-empty set of Domains the role owns |
| `excludedDomainRefs` | Set of explicitly excluded Domains |
| `permissions` | Mode and capability ceiling using the shared permission shape |
| `branchPolicy` | Closed required `allowed.exact`, `allowed.prefixes`, `denied.exact`, and `denied.prefixes` arrays using `branchRef` and `branchPrefix` exactly as defined in section 6 |
| `cleanlinessPolicy` | Closed policy for tracked, untracked, ignored, index, and submodule state; each is `clean`/`none` or `contract-enumerated` as applicable |
| `exclusiveWriteRequired` | Required Boolean |
| `reviewOnly` | Required Boolean |

Owned and excluded Domains are disjoint and must exist in the same Project. A role may own multiple Domains. Its derived path language is the union of its owned Domains' valid path-scope languages and therefore never contains a path with an exact `.git` component. `roleClass: integration-control` identifies responsibility only; it grants no administrative operation. Branch-policy eligibility requires at least one exact or inclusive component-prefix allow match and no exact or prefix deny match. The object defines a logical responsibility profile, not a filesystem path or live worktree, and Phase 3 must still observe its actual branch and HEAD state.

#### Capability classes and review-only roles

The complete 13-member capability vocabulary is partitioned into exactly five
classes. Every member occurs in exactly one class:

| Capability class | Exact members |
| --- | --- |
| Observation | `inspect`, `validate` |
| Repository mutation | `create`, `modify`, `delete` |
| Execution | `execute-tests`, `execute-build` |
| Git administration | `git-stage`, `git-commit`, `git-branch`, `git-remote` |
| External access | `network`, `external-secret-use` |

Let `C` be that complete capability set and let `P` be
`permissions.permittedCapabilities`. When `reviewOnly` is `true`, all of the
following are required simultaneously:

```text
roleClass == review
permissions.modes == [plan-only]
P ⊆ {inspect, validate}
permissions.prohibitedCapabilities == C − P
exclusiveWriteRequired == false
```

The four valid permitted sets are exactly `[]`, `[inspect]`,
`[validate]`, and `[inspect,validate]`, each with the exact complement
in canonical order as its prohibited set. Permitted and prohibited sets remain
disjoint. Project, Domain, HostOverlay, routing, availability, adapter, or any
other field may narrow the result but cannot restore a capability excluded by
this rule. Negative vectors place each of the eleven non-observation members
in `P` separately and also cover a non-review role, any mode other than the
one-element plan-only set, a missing complement member, an extra prohibition
that overlaps `P`, `exclusiveWriteRequired: true`, and attempted restoration
through another field.

### `RoutingPolicy`

Required `spec` fields:

| Field | Design |
| --- | --- |
| `projectRef` | The Project for which the policy is defined |
| `rules` | Canonically ordered rule array |
| `fallback` | Closed decision fixed to explicit deny with a reason code |

Each rule is closed and contains `id`, integer `priority` from 0 through
1000 under the numeric profile, `match`, and `decision`. `match` contains an
exact `projectRef` and a `domainSet` with non-empty `domainRefs` plus
operator `exact` or `contains`. `decision` is a closed union: route to one
`worktreeRoleRef`, or deny with one reason code. Every referenced role and
Domain must belong to the policy Project, and a route target must statically
own the rule’s declared Domains. Phase 1 applies only the static rules in
section 9; actual matching and unique role selection remain Phase 2.

Static RoutingPolicy ownership and inclusion calculations consume only the
revised valid Domain path languages. Neither routing nor complete-set ownership
can restore a reserved `.git`-component path excluded from that universe.

### `HostOverlay`

Required `spec` fields:

| Field | Design |
| --- | --- |
| `hostId` | Non-secret logical host-local identity; it is not proof of host identity |
| `projectRef` | One portable `Project` reference |
| `repositoryIdentity` | Restrictive local repository expectation |
| `bindings` | Non-empty canonical set of the exact closed five-field binding records defined below |
| `remoteExpectations` | Set-like closed records containing `remoteName` and required non-empty `acceptedRemotes` |
| `capabilityCeiling` | Canonical capability set that may only narrow customer governance |
| `pathCeiling` | Canonical repository-relative include/exclude arrays |
| `stateRoot` | Absolute host-path representation for future runtime state outside the target worktree |
| `lockRoot` | Absolute host-path representation for future coordination locks outside the target worktree |

Within one HostOverlay, `remoteName` is the sole identity of a remote-expectation record. The outer `remoteExpectations` array is set-like, contains at most one record for each name, and is unique and canonically ordered by `S(remoteName)`. Each record's `acceptedRemotes` is required, non-empty, set-like, unique, and canonically ordered by `J(remote)`. Multiple acceptable repository remotes for one configured Git remote name are represented inside that one record. Two outer records with the same `remoteName` are invalid even when their accepted remote values differ. Runtime comparison with the observed Git remote remains Phase 3. The structured representation cannot contain a credential-bearing URL, user-info, query, fragment, local file transport, token, or key path.

#### Closed HostOverlay binding

Every `bindings` member is one closed record requiring exactly these five
fields and no others:

| Field | Exact type |
| --- | --- |
| `roleRef` | `WorktreeRole` object reference |
| `worktreeId` | `logicalIdentifier` |
| `repositoryRoot` | `absoluteHostPath` |
| `expectedRef` | the exact `refState` branch/detached union |
| `remoteNames` | non-empty `logicalIdentifier[]` |

`remoteNames` is set-like, unique, and strictly ordered by `S(value)`. Every
name resolves to exactly one `HostOverlay.remoteExpectations` record. A branch
`expectedRef` requires `branchRef`; a detached `expectedRef` forbids it. A
generic `expectedBranch` field and cached observed HEAD, branch, remote URL, or
other Git-state fields are forbidden. Binding identity remains
`(R(roleRef), S(worktreeId))`. `repositoryRoot` is restrictive host-local
input and grants no authority. Phase 3 compares the live canonical root,
worktree registration, ref state, and every named remote with this binding.

Every HostOverlay absolute path—`bindings[].repositoryRoot`, `stateRoot`, and
`lockRoot`—uses the same closed `absoluteHostPath` profile. Phase 1 rejects an
invalid POSIX spelling, a Windows value outside the uppercase-drive-only
grammar, and every UNC or device-namespace value before host binding. Exact
static comparison uses `(platform, value)`; Phase 3 separately checks whether
the selected lexical branch is compatible with the actual host and whether
the path resolves to the intended host-local resource.

#### Host-resource exclusivity

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

Positive vectors cover complete branch and detached records with valid POSIX
and drive-only Windows absolute paths. Negative vectors
cover each missing field, every unknown field, duplicate or empty
`remoteNames`, an unknown remote name, non-canonical name order, a branch
without `branchRef`, a detached value with `branchRef`, `expectedBranch`, and
each forbidden cached observation, plus every `absoluteHostPath` negative
class defined above.

#### Exact Phase 1 HostOverlay narrowing proof

For every binding, `HostOverlay.spec.projectRef` resolves exactly one Project,
`roleRef` occurs in that Project's `worktreeRoleRefs`, and the resolved
WorktreeRole's `projectRef` equals the overlay Project. An overlay cannot add,
replace, or modify portable role or Domain ownership.

Let `Pp` and `Pr` be the Project and WorktreeRole permitted-capability sets,
and let `Xp` and `Xr` be their prohibited-capability sets. Define:

```text
Cportable = (Pp ∩ Pr) − (Xp ∪ Xr)
HostOverlay.capabilityCeiling ⊆ Cportable
Cbinding = Cportable ∩ HostOverlay.capabilityCeiling
```

All comparisons use exact capability-enum membership. Unknown or unprovable
membership rejects the overlay.

Every structured remote in `HostOverlay.repositoryIdentity.acceptedRemotes`
must occur in `Project.repositoryIdentity.acceptedRemotes` by exact
`J(remote)` equality. Every value in every
`remoteExpectations[].acceptedRemotes` set must occur in the same Project set.
The overlay may remove acceptable remotes but cannot add one. Every binding
`remoteNames` member resolves to one non-empty narrowed expectation record.

For path proofs, `U` is the universe of all already-NFC strings accepted by
the revised `repositoryRelativePath` profile, which excludes every value with
an exact case-sensitive `.git` component. A literal `.git` component makes a
pattern invalid before automata construction. A path pattern is anchored to
the whole path and has exactly this restricted meaning:

- a literal character matches itself;
- `?` matches exactly one permitted non-`/` Unicode scalar within a segment;
- `*` matches zero or more permitted non-`/` scalars within one non-empty
  segment;
- `**` is special only as a complete segment and matches zero or more complete
  non-empty segments; and
- negation, brace expansion, absolute syntax, backslash, normalization, host
  transformation, and every other metacharacter or extension are forbidden.

Pattern syntax, matched paths, and path arrays must independently satisfy
their declared profiles. For one include/exclude scope `X`, define:

```text
L(X) = union(language(pattern) for pattern in X.include)
       − union(language(pattern) for pattern in X.exclude)

Lproject = union(L(Domain.pathScope) for Domain in Project.domainRefs)
Lrole    = union(L(Domain.pathScope) for Domain in WorktreeRole.ownedDomainRefs)
Loverlay = L(HostOverlay.pathCeiling)
Lbinding = Loverlay ∩ Lrole
```

An empty HostOverlay include array denotes the empty language. Phase 1 must
prove the exact restriction:

```text
Loverlay ∩ (U − Lproject) = ∅
```

The proof compiles the restricted grammar into deterministic automata,
complements `Lproject` relative to `U`, constructs the product intersection,
and tests emptiness. Unsupported syntax, compilation failure, resource
exhaustion, or an indeterminate result rejects the overlay. Samples, path
prefixes, and heuristic matching are never inclusion proof.

The exact rejection codes are:

- `reason.overlay.project-mismatch`;
- `reason.overlay.role-not-in-project`;
- `reason.overlay.role-project-mismatch`;
- `reason.overlay.capability-widening`;
- `reason.overlay.repository-widening`;
- `reason.overlay.remote-widening`;
- `reason.overlay.remote-unresolved`;
- `reason.overlay.path-widening`; and
- `reason.overlay.path-proof-unavailable`.

Vectors cover valid narrowing and widening for capabilities, Project/role
identity, repository identity, remote expectations, and path language. Path
vectors include `src/lib/**` within Project `src/**`, `docs/**` outside that
universe, unsupported syntax, compilation failure, resource exhaustion, and
an indeterminate emptiness result. This is static closed-configuration
restriction validation only; it does not resolve task intent or execute
RoutingPolicy.

Static validation checks binding shape, reference integrity, uniqueness,
absolute-path syntax, canonical arrays, and every restriction proof above.
Real path identity, registration, ref and remote observation, containment, and
runtime state remain Phase 3. The overlay has no secret or cached-observation
field, and concrete overlay instances remain outside the target worktree.

### `TaskContract`

`metadata.id` is the contract ID and is narrowed to a canonical lower-case UUID. Required `spec` fields are:

| Field | Design |
| --- | --- |
| `contractVersion` | Constant string `1` for this structural contract layout |
| `taskId` | Canonical UUID |
| `projectRef` | Resolved Project reference |
| `repositoryIdentity` | Credential-free repository binding |
| `target` | Closed logical `worktreeId` and required `worktreeRoleRef`; no absolute path |
| `domainRefs` | Complete non-empty canonical Domain set |
| `issuer` | Closed `issuerId`, `issuanceMethod: trusted-framework`, and `derivationDigest` representation; structural presence does not prove trust |
| `digests` | Tagged policy, configuration, and task-intent digests |
| `requestedMode` / `effectiveMode` | Explicit shared modes |
| `allowWrite` | Explicit Boolean |
| `authorizedScope` / `prohibitedScope` | Closed shared scopes |
| `expectedBaseline` | Immutable closed nine-dimension reference, HEAD, index, tracked, untracked, ignored, submodule, active-operation, and administrative-lock baseline; active operations and administrative locks are each exactly `none`, while their reusable non-empty unions remain observation/evidence-only |
| `permittedTransitions` | Canonical set of explicitly permitted transition records from exactly seven closed branches |
| `requiredPostconditions` | Canonical set of postcondition records |
| `leaseRequired` | Explicit Boolean |
| `leaseId` | Canonical UUID, present exactly when a lease is required |
| `issuanceCheckpoint` | Closed observation timestamp and `profile.digest.issuance-state-v1` state digest defined exactly in section 10 |
| `freshness` | Mandatory `issuedAt` and `expiresAt` boundary |

Both `authorizedScope.paths` and `prohibitedScope.paths` use pattern languages
over the revised valid repository-relative path universe. A literal exact
`.git` component is invalid, and even an authorized `modify` plus `**` cannot
grant ordinary-path authority over `.git/config`, hooks, refs, or other Git
administrative state. Git-administration capability tokens do not authorize
direct filesystem mutation of those locations.

The contract binds the exact Phase 2 routing result. Its `projectRef` is the
same resolved Project, `target.worktreeRoleRef` is the one selected role,
`target.worktreeId` is the same resolved target, and `domainRefs` is exactly
the complete non-empty resolved Domain-reference set. The set may neither omit
a resolved Domain nor add an unrelated Domain. A mismatch among routing's
complete set, selected role, resolved target, or these contract fields denies
issuance or validation. Several roles may never be unioned into one contract
target.

#### Closed mode, write, and lease truth table

The `requestedMode`, `effectiveMode`, `allowWrite`, `leaseRequired`, `leaseId`,
and any present `lease-state` postcondition form one closed contract invariant.
The allowed combinations are exactly:

| `requestedMode` | `effectiveMode` | `allowWrite` | `leaseRequired` | `leaseId` | `lease-state` if present |
| --- | --- | --- | --- | --- | --- |
| `plan-only` | `plan-only` | `false` | `false` | forbidden | `not-required` |
| `implementation` | `plan-only` | `false` | `false` | forbidden | `not-required` |
| `implementation` | `implementation` | `false` | `false` | forbidden | `not-required` |
| `implementation` | `implementation` | `true` | `true` | required | `owned` |

No other combination is valid. Effective mode MUST NOT widen requested mode:
a requested `plan-only` permits only effective `plan-only`. Effective
`plan-only` requires `allowWrite: false`; `allowWrite: true` requires effective
`implementation`; and effective `implementation` MAY remain non-writing. For
`v1alpha1-r1`, `leaseRequired` MUST equal `allowWrite`, and `leaseId` is present
if and only if `leaseRequired` is true. A present `lease-state` postcondition is
`owned` if and only if `leaseRequired` is true and is `not-required` if and
only if `leaseRequired` is false. Schema validity does not prove lease
ownership; actual ownership validation remains Phase 3 and Phase 4.

#### Non-writing contracts

For each of the first three truth-table rows, where `allowWrite` is `false`,
`permittedTransitions` is exactly `[]`. No transition type is implicitly
non-writing. If any state postcondition is present, its expected value equals
the corresponding immutable baseline projection; it cannot describe drift.
`leaseRequired` remains `false`, `leaseId` remains absent, and a present
`lease-state` remains `not-required`.

An issued-contract receipt for any non-writing contract has
`changedPaths: []`. Observed drift is denial or failure evidence, not
authorization. Possession of `execute-tests` or `execute-build` cannot
override `allowWrite: false`.

The mandatory 21 negative vectors are the Cartesian product of the three
non-writing rows—plan-only/plan-only, implementation/plan-only, and
implementation/implementation—with the seven permitted transition types:
`ref-state`, `head-state`, `index-entry`, `tracked-entry`, `untracked-path`,
`ignored-path`, and `submodule-entry`. The retired `active-operation` and
`administrative-lock` branches belong to their separate 21-case
legacy-contract rejection families and do not add an eighth or ninth D5
transition class. Phase 1 rejects
each closed non-writing contract and checks any explicit state postcondition
against the baseline. Phase 4 requires the empty changed-path set and treats
mutation or uncertain drift as failed or indeterminate verification.

#### Exact `expectedBaseline`

`TaskContract.spec.expectedBaseline` is one closed object. Every one of these
nine fields is required and no other field is permitted:

| Field | Exact type |
| --- | --- |
| `ref` | `refState` |
| `head` | `headState` |
| `index` | `indexCondition` |
| `tracked` | `trackedCondition` |
| `untracked` | `untrackedCondition` |
| `ignored` | `ignoredCondition` |
| `submodules` | `submoduleCondition` |
| `activeOperations` | Exact closed constant `{ "state": "none" }`; the reusable `activeOperationsCondition.exact` branch is observation/evidence only |
| `administrativeLocks` | Exact closed constant `{ "state": "none" }`; the reusable `administrativeLocksCondition.exact` branch is observation/evidence only |

All unions and records below are closed. A branch requires every field listed
for it and forbids every field listed only for another branch.

`refState` is exactly:

| `state` | Required additional field | Forbidden field |
| --- | --- | --- |
| `branch` | `branchRef: branchRef` | — |
| `detached` | — | `branchRef` |

Reference state carries no commit object ID. `headState` carries object
identity separately and is exactly:

| `state` | Required additional field | Forbidden field |
| --- | --- | --- |
| `commit` | `objectId: gitObjectId` | — |
| `unborn` | — | `objectId` |

`ref.state: detached` with `head.state: unborn` is invalid. A branch may
combine with either a committed or unborn HEAD.

Branch-policy evaluation remains a separate eligibility gate. A valid
symbolic branch is evaluated under the exact allow/deny rules in section 6; a
detached state fails because it supplies no `branchRef`. A symbolic unborn
branch may pass the branch-policy predicate, but it remains valid only when the
separate baseline, HEAD-state, and later live-observation gates also pass.

A `gitMode` is a JSON string, never a JSON number, and its complete vocabulary
is `100644`, `100755`, `120000`, and `160000`.

#### Conflict-free stage-0 index profile

A `TaskContract` baseline represents only a conflict-free, stage-0 Git index.
An unmerged index is not representable in a `TaskContract` and causes
fail-closed denial before contract issuance. `v1alpha1-r1` deliberately does
not define a nested conflict-stage representation.

`indexCondition` is exactly:

| `state` | Required additional field | Forbidden field |
| --- | --- | --- |
| `clean` | — | `entries` |
| `exact` | `entries: indexEntry[]`; the complete array MAY be empty | — |

`index.clean` means that the conflict-free stage-0 index equals the selected
HEAD tree; for an unborn HEAD, it means the index is empty. `index.exact` means
that the conflict-free stage-0 index differs from the selected HEAD tree and
that `entries` is the complete stage-0 index inventory, never a delta. An exact
inventory MAY be empty when every HEAD path has been deleted from the index.
Phase 3 selects `clean` versus `exact` by live comparison, and two encodings of
the same live state are invalid.

Every closed `indexEntry` requires exactly:

| Field | Exact type or value |
| --- | --- |
| `path` | `repositoryRelativePath` |
| `stage` | integer constant `0` under the numeric profile |
| `mode` | `gitMode`: `100644`, `100755`, `120000`, or `160000` |
| `objectId` | `gitObjectId` |
| `intentToAdd` | Boolean constant `false` |
| `skipWorktree` | Boolean constant `false` |
| `assumeUnchanged` | Boolean constant `false` |

Sparse-directory entries and unsupported modes are not representable. The
outer entry array contains at most one entry for a path and is unique and
strictly ordered solely by `S(entry.path)`. Phase 1 rejects duplicate paths
before digest projection; `J(entry)` remains diagnostic-only after path
uniqueness and cannot legalize a duplicate.

Every reference to an exact index in this design means a complete inventory
under the `v1alpha1-r1` conflict-free stage-0 profile, not a representation of
Git's general unmerged-index format.

Observation of any of the following prevents `TaskContract` issuance: stage
`1`, `2`, or `3`; simultaneous conflict-stage records; any unmerged index;
intent-to-add; skip-worktree; assume-unchanged; a sparse-index directory entry;
an unsupported index mode; or any index state this profile cannot represent
exactly. Such a state fails closed at initial preflight or post-acquisition
revalidation, may appear only in sanitized pre-contract denial evidence, MUST
NOT be coerced into a stage-0 baseline, MUST NOT be silently discarded, and
MUST NOT produce an issued-contract receipt.

The planned canonical denial codes include:

- `reason.git.index-unmerged`;
- `reason.git.index-intent-to-add`;
- `reason.git.index-skip-worktree`;
- `reason.git.index-assume-unchanged`;
- `reason.git.index-sparse`; and
- `reason.git.index-unsupported`.

These planned codes identify denial classes; they are not evidence that a
check actually occurred.

`trackedCondition` is exactly:

| `state` | Required additional field | Forbidden field |
| --- | --- | --- |
| `clean` | — | `entries` |
| `exact` | non-empty `entries: trackedEntry[]` | — |

Each `trackedEntry` requires `path` and exactly one of these status branches:

| `status` | Other required fields | Forbidden fields | Static mode relationship |
| --- | --- | --- | --- |
| `clean` | `indexMode`, `indexObjectId` | `worktreeMode`, `contentDigest` | — |
| `modified` | `indexMode`, `indexObjectId`, `worktreeMode`, `contentDigest` | — | `worktreeMode == indexMode` |
| `deleted` | `indexMode`, `indexObjectId` | `worktreeMode`, `contentDigest` | — |
| `type-changed` | `indexMode`, `indexObjectId`, `worktreeMode`, `contentDigest` | — | `worktreeMode != indexMode` |

`indexMode` and `worktreeMode` are restricted to regular tracked worktree
modes `100644`, `100755`, or `120000`; `160000` belongs exclusively to
submodule state and is forbidden in a normal tracked entry. `indexObjectId` is
a `gitObjectId`, and `contentDigest` is a tagged SHA-256 digest. Fields not
listed for the selected status are forbidden. An exact tracked condition
contains at most one entry for a path and is strictly ordered solely by
`S(entry.path)`; duplicate paths are invalid across status branches.

#### Raw tracked worktree-content digest

`trackedEntry.contentDigest` is bound only to
`profile.digest.worktree-content-v1` in the exhaustive digest catalog in
section 10. The profile payload is determined solely by the observed
worktree object:

- for mode `100644` or `100755`, it is the exact raw file bytes;
- for mode `120000`, it is the exact lossless link-target byte sequence;
- filters, clean/smudge processing, EOL conversion, decoding, Unicode
  normalization, and symlink dereference are forbidden; and
- mode, path, object ID, directories, and gitlinks are not payload bytes.

The payload is obtained from an opened, identity-bound object or an equivalent
observation that proves the same identity. Identity, kind, length, and relevant
metadata are checked before and after reading, and the path must still resolve
to the same object. Replacement, truncation, changed length, unreadability,
lossy link-target access, a race, or an unsupported object type denies
issuance. A directory or gitlink never receives `contentDigest`.

After the profile's exact domain separator is prepended, the fixed positive
vectors are:

| Worktree object | Exact payload hex | Tagged digest |
| --- | --- | --- |
| Empty regular file | empty | `sha256:75a1e5502a349f7d22cbb583985b3045b6d5fd084f9f053cf3379bbbfe3781f9` |
| Regular binary file | `00ff100a` | `sha256:d81685f62ae980ae8f1ca44242368c5c790894f055bd18ec1d76cbb5aa212db1` |
| Executable file with the same bytes | `00ff100a` | `sha256:d81685f62ae980ae8f1ca44242368c5c790894f055bd18ec1d76cbb5aa212db1` |
| Symlink target `../target.bin` | `2e2e2f7461726765742e62696e` | `sha256:dfe817225dbc5a625497132435cd03bb8330b34fab83b2263c8d9707d9e71940` |

Negative vectors use filtered or EOL-converted bytes, decoded or normalized
text, dereferenced symlink content, an unreadable file, replacement during
observation, changed or inconsistent length, a lossy link-target observation,
a directory, a gitlink, and every other unsupported object type.

`untrackedCondition` and `ignoredCondition` each use the same exact union:

| `state` | Required additional field | Forbidden field |
| --- | --- | --- |
| `none` | — | `paths` |
| `exact` | non-empty `paths: repositoryRelativePath[]` | — |

Every exact path array is unique and strictly ordered by `S(path)`.

#### Canonical untracked and ignored path inventory

`profile.git.path-inventory-v1alpha1-r1` is the sole observation and encoding
profile for baseline and postcondition untracked and ignored arrays. Its exact
algorithm is:

1. Resolve and identity-bind the repository root and its Git administrative
   locations.
2. Resolve every registered gitlink root before traversal.
3. Recursively traverse the worktree without following symlinks.
4. Exclude the repository's Git administrative data and every registered
   submodule root and descendant. Never emit a path containing an exact `.git`
   component.
5. Treat a regular file, executable file, or symlink as one leaf; executable
   state is not encoded in these path-only inventories.
6. Never emit a directory; consequently, an empty directory has no
   representation.
7. Deny an unregistered nested repository without traversing or collapsing
   it.
8. For each non-tracked candidate leaf, evaluate the complete effective Git
   ignore stack, including applicable `.gitignore` files, repository exclude
   data, configured global excludes, precedence, later-match behavior, and
   negation. Observer-only ad hoc rules are forbidden. Ignored directories
   are still traversed so qualifying leaves can be enumerated.
9. Put the leaf in ignored when the final effective result is ignored;
   otherwise put it in untracked. A leaf occurs in at most one class.
10. Require every repository-relative path to satisfy the revised
    `repositoryRelativePath` profile, including strict UTF-8, already-NFC, and
    exact case-sensitive `.git`-component rejection.
11. Strictly order each final array by `S(path)`. A directory entry, collapsed
    directory, or another expanded/collapsed alternative is invalid.

Unreadable directories, traversal races, cycles, unresolved filesystem
identity, unresolved ignore classification, unresolved submodule boundaries,
and unsupported object types fail closed. The exact reason codes are:

- `reason.git.path-inventory.unregistered-nested-repository`;
- `reason.git.path-inventory.unreadable`;
- `reason.git.path-inventory.traversal-race`;
- `reason.git.path-inventory.cycle`;
- `reason.git.path-inventory.identity-unresolved`;
- `reason.git.path-inventory.classification-unresolved`;
- `reason.git.path-inventory.path-unrepresentable`;
- `reason.git.path-inventory.submodule-boundary-unresolved`;
- `reason.git.path-inventory.object-type-unsupported`;
- `reason.contract.path-inventory.directory-entry`; and
- `reason.contract.path-inventory.collapsed-directory`.

Required vectors cover a regular leaf, executable leaf, symlink leaf without
dereference, recursive ignored-directory leaves, ignore-rule negation, an empty
directory, a registered submodule boundary, an unregistered nested repository,
unreadable/racing/cyclic traversal, unresolved identity or classification,
an unrepresentable filename, a directory member, and a collapsed-directory
alternative. The profile is not defined by one particular Git CLI command.

Phase 3 resolves top-level `.git` indirection, linked and common Git
directories, administrative locations outside the worktree root, filesystem
indirection and aliases, case-folded, Windows 8.3, and Unicode-normalized
aliases, registered-submodule administrative roots, and nested-repository
administrative roots before inventory acceptance. Host-local resolved paths
are not recorded in portable governance, and an unresolved boundary fails
closed.

`submoduleCondition` is exactly:

| `state` | Required additional field | Forbidden field |
| --- | --- | --- |
| `none` | — | `entries` |
| `exact` | non-empty `entries: submoduleEntry[]` | — |

Every closed `submoduleEntry` requires exactly `path`, `recordedObjectId`,
`checkout`, and `observation`. `recordedObjectId` and the initialized checkout
ID below are `gitObjectId` values. `checkout` is exactly:

| `state` | Required additional field | Forbidden field |
| --- | --- | --- |
| `absent` | — | `checkedOutObjectId` |
| `uninitialized` | — | `checkedOutObjectId` |
| `initialized` | `checkedOutObjectId` | — |

`observation` is exactly:

| `state` | Required additional fields | Forbidden additional fields |
| --- | --- | --- |
| `unavailable` | none | `trackedChanges`, `untrackedChanges`, `conflicts` |
| `observed` | `trackedChanges: Boolean`, `untrackedChanges: Boolean`, `conflicts: Boolean` | none |

`unavailable` is valid only with checkout `absent` or `uninitialized`.
`observed` is valid only with checkout `initialized`, and all eight Boolean
triples from `false,false,false` through `true,true,true` are valid. A
`checkedOutObjectId` different from `recordedObjectId` represents checkout
commit difference independently from the three Booleans. `unavailable` never
means clean. An initialized checkout without conclusive observation denies
issuance; neither an `indeterminate` observation nor the superseded
`worktreeState` field is valid contract data. Uncertainty may appear only in
sanitized pre-contract evidence.

The four exact denial codes are:

- `reason.git.submodule.observation-unavailable`;
- `reason.git.submodule.state-unreadable`;
- `reason.git.submodule.observation-race`; and
- `reason.git.nested-repository.unsupported`.

Positive vectors cover absent/unavailable, uninitialized/unavailable,
initialized/observed with each of the eight Boolean triples, and initialized
checkout IDs both equal to and different from `recordedObjectId`. Invalid
vectors cover absent/observed, uninitialized/observed,
initialized/unavailable, missing or branch-inapplicable
`checkedOutObjectId`, fields on `unavailable`, each missing observed Boolean,
unknown fields, `indeterminate`, and `worktreeState`.

Entries are unique and strictly ordered solely by `S(entry.path)`; same-path
entries remain invalid regardless of object IDs, checkout state, or
observation. The complete checkout and observation value passes unchanged
through `submodule-entry` transitions, final-composite validation, and
submodule-state postconditions; no weaker parallel representation exists.

`activeOperationsCondition` is exactly:

| `state` | Required additional field | Forbidden field |
| --- | --- | --- |
| `none` | — | `operations` |
| `exact` | non-empty `operations: activeOperation[]` | — |

`activeOperation` is the closed enum `merge`, `rebase`, `cherry-pick`,
`revert`, `bisect`, `sequencer`, or `apply-mailbox`. The array is
set-like, unique, and strictly ordered by `S(value)`. Details beyond presence
are Phase 3 observations and are not represented in `v1alpha1-r1`; an unknown
operation name fails closed.

The complete union remains reusable for non-authorizing observation and
sanitized evidence. Within `TaskContract.spec.expectedBaseline`, however,
`activeOperations` MUST equal exactly `{ "state": "none" }`. Each of the
seven single-operation exact baselines, every multi-operation exact baseline,
and every other `state: exact` baseline is invalid before contract issuance.
Bootstrap maintenance creates no runtime TaskContract and does not alter this
rule.

`administrativeLocksCondition` is exactly:

| `state` | Required additional field | Forbidden field |
| --- | --- | --- |
| `none` | — | `locks` |
| `exact` | non-empty `locks: administrativeLockIdentity[]` | — |

An `administrativeLockIdentity` is one of these closed branches:

| `type` | Required additional field | Forbidden fields |
| --- | --- | --- |
| `index` | — | `ref`, `identifier` |
| `packed-refs` | — | `ref`, `identifier` |
| `shallow` | — | `ref`, `identifier` |
| `config` | — | `ref`, `identifier` |
| `head` | — | `ref`, `identifier` |
| `ref` | `ref: gitRefIdentifier` | `identifier` |
| `other` | `identifier: logicalIdentifier` | `ref` |

Define `L(lock)` as `(S(type))` for the five singleton types,
`(S("ref"), S(ref))` for a ref lock, and
`(S("other"), S(identifier))` for an other lock. Lock identity, uniqueness,
and canonical order use only `L(lock)`, compared componentwise. Actual lock
discovery and interpretation remain Phase 3.

The complete `administrativeLocksCondition` union remains reusable for live
observation and sanitized evidence. Within
`TaskContract.spec.expectedBaseline`, however, `administrativeLocks` MUST equal
exactly `{ "state": "none" }`. The optional `administrative-locks`
postcondition is also none-only, and `administrative-lock` is not a permitted
transition. No non-empty lock condition can become issued-contract authority
or a successful final postcondition. Git administrative locks remain distinct
from task-owned runtime write leases, lease-store locks, and transient
command-internal lock files.

#### Active-operation checkpoint treatment

At initial preflight or any pre-issuance revalidation, observing a non-empty
active-operation condition denies before contract issuance. No TaskContract
exists. Optional sanitized pre-contract-denial evidence may retain the exact
observation.

At post-contract, immediately-before-action revalidation, observing a non-empty
active-operation condition permits no protected action. An issued-contract
receipt may be finalized, but `executionOutcome` MUST be `not-attempted` and
`verificationOutcome` MUST be `not-performed`; normal release and lifecycle
precedence remains applicable.

At post-execution verification, observing a non-empty active-operation
condition is unexpected terminal evidence. Verification MUST be `failed` or
`indeterminate`, according to the available evidence. A non-empty condition
is never an authorized final postcondition.

Positive observation/evidence vectors retain all seven active-operation names,
pre-contract denial, post-contract/pre-action non-attempted evidence, and
post-execution failed or indeterminate evidence. General malformed-observation
negatives retain duplicate and non-canonical arrays, unknown operations, and
empty exact arrays.

#### Administrative-lock checkpoint treatment

At initial live preflight and at the path-applicable pre-issuance revalidation
(`post-acquisition-revalidation` after lease acquisition or distinct
`pre-issuance-revalidation` on a no-lease path), a non-empty administrative-
lock observation denies contract issuance. Sanitized pre-contract-denial
evidence may retain the exact observation, but no TaskContract may contain it
as a baseline.

At post-contract, immediately-before-action revalidation, a non-empty
administrative-lock observation permits no protected action. Any resulting
issued-contract receipt MUST use `executionOutcome: not-attempted` and
`verificationOutcome: not-performed`. At post-execution verification, a
non-empty observation is failed or indeterminate terminal evidence and is
never a successful final postcondition.

Positive reusable observation/evidence vectors retain `none` and all seven
single-lock identity branches: `index`, `packed-refs`, `shallow`, `config`,
`head`, `ref`, and `other`. The exact administrative-lock legacy-contract
family contains 21 invalid cases: seven non-empty single-lock TaskContract
baselines, seven retired `administrative-lock` transitions, and seven
non-empty single-lock `administrative-locks` postconditions. Generic
observation-shape negatives remain separate and do not inflate that family:
duplicate lock identity, missing or forbidden branch identifiers, unknown
branch, non-canonical `L(lock)` order, empty exact arrays, and other malformed
reusable observation forms.

#### Exact `permittedTransitions`

`TaskContract.spec.permittedTransitions` is a set-like array that may be
empty. Its members are limited to exactly these seven closed branches:

| `type` | Required target field | Exact `from` and `to` types |
| --- | --- | --- |
| `ref-state` | — | `refState` |
| `head-state` | — | `headState` |
| `index-entry` | `path: repositoryRelativePath` | `entryPresence(indexEntryStateWithoutPath)` |
| `tracked-entry` | `path: repositoryRelativePath` | `entryPresence(trackedEntryStateWithoutPath)` |
| `untracked-path` | `path: repositoryRelativePath` | enum `absent` or `present` |
| `ignored-path` | `path: repositoryRelativePath` | enum `absent` or `present` |
| `submodule-entry` | `path: repositoryRelativePath` | `entryPresence(submoduleEntryStateWithoutPath)` |

Every transition requires `type`, `from`, and `to`, plus exactly the target
field shown for its branch; all other branch target fields are forbidden.
`entryPresence(T)` is a closed union: `{ state: "absent" }` forbids `value`,
while `{ state: "present", value: T }` requires it.
`indexEntryStateWithoutPath`, `trackedEntryStateWithoutPath`, and
`submoduleEntryStateWithoutPath` are the corresponding exact record or union
above with only `path` removed; every remaining required and forbidden-field
rule is unchanged.

`from` and `to` MUST differ as exact structured values. Only the explicitly
targeted key may change through a transition. Transition target identity and
order use `T(transition)`:

- `(S(type))` for the singleton `ref-state` and `head-state` branches;
- `(S(type), S(path))` for the five path-keyed branches.

At most one transition may target a given `T(transition)`. Thus there is at
most one ref-state transition, at most one head-state transition, one
transition per `(type, path)`. Targets must be strictly ordered by
`T(transition)`. Target uniqueness is validated before hashing;
`J(transition)` is permitted only as a deterministic diagnostic tie-breaker
after that validation. A transition grants no authority outside the contract
scope. For ordinary-file mutation-capability closure, an operation is never
inferred solely from the transition branch name: `ref-state`, `head-state`,
`index-entry`, and `submodule-entry` contribute no ordinary-file mutation,
while `tracked-entry`, `untracked-path`, and `ignored-path` are interpreted from
the complete baseline/final path state defined below. Actual transition and
execution-effect attribution remains Phase 4 verification.

Each of the five path-keyed transition targets must be a valid
`repositoryRelativePath`; any exact `.git` component rejects the contract. A
transition capability or Git-administration capability token cannot convert a
reserved administrative location into an ordinary transition target.

#### Exact `requiredPostconditions`

`TaskContract.spec.requiredPostconditions` is a non-empty set-like array with
only these eleven closed branches:

| `type` | Exact additional field |
| --- | --- |
| `scope-contained` | none; `expected` is forbidden |
| `ref-state` | required `expected: refState` |
| `head-state` | required `expected: headState` |
| `index-state` | required `expected: indexCondition` |
| `tracked-state` | required `expected: trackedCondition` |
| `untracked-state` | required `expected: untrackedCondition` |
| `ignored-state` | required `expected: ignoredCondition` |
| `submodule-state` | required `expected: submoduleCondition` |
| `active-operations` | required exact `expected: { "state": "none" }` |
| `administrative-locks` | required exact `expected: { "state": "none" }` |
| `lease-state` | required `expected` enum `not-required` or `owned` |

The `active-operations` and `administrative-locks` branches remain optional
and type-unique; neither is newly mandatory. Their reusable exact observation
unions do not widen the postcondition contract. Every non-empty active-operation
or administrative-lock expectation is invalid.

Every contract contains exactly one `scope-contained` postcondition. There is
at most one postcondition of every other type, and the array is strictly
ordered by `S(type)`. A `lease-state` postcondition in a plan-only or other
non-writing contract uses `not-required`; one in a write contract with
`leaseRequired: true` uses `owned`. Release is not a post-execution contract
postcondition because it occurs during terminalization after execution
verification. Phase 3 or 4 must observe lease ownership; structural validity
does not prove it.

Every entry or path array nested in an `expected` condition uses the identical
closed branch, branch-specific cardinality, sole path identity, uniqueness,
inventory, cross-dimension, and ordering rules defined for the baseline.
Every nested path therefore uses the revised valid path universe and rejects
an exact `.git` component. `scope-contained` verifies actual ordinary effects
against both the path and operation-capability predicates defined below: a
runtime-resolved Git administrative effect makes the postcondition failed or
indeterminate and may not be silently omitted.
Postcondition type uniqueness is validated before hashing.
`J(postcondition)` is diagnostic-only after type uniqueness; a duplicated or
conflicting type is invalid.

#### Simultaneous transition composition

Let `B` be the complete materialized baseline projection. For every transition
target, `B(target)` is defined exactly as follows:

| Transition target | Exact `B(target)` | Matching postcondition type |
| --- | --- | --- |
| `ref-state` | `expectedBaseline.ref` | `ref-state` |
| `head-state` | `expectedBaseline.head` | `head-state` |
| `index-entry(path)` | present with the complete matching index entry without `path`, or absent | `index-state` |
| `tracked-entry(path)` | present with the complete matching tracked entry without `path`, or absent | `tracked-state` |
| `untracked-path(path)` | present if and only if the path is in the complete untracked inventory | `untracked-state` |
| `ignored-path(path)` | present if and only if the path is in the complete ignored inventory | `ignored-state` |
| `submodule-entry(path)` | present with the complete matching D2 checkout/observation entry without `path`, or absent | `submodule-state` |

`B` still materializes all nine baseline dimensions. Its active-operation
and administrative-lock dimensions are each exactly `none`. Neither dimension
is an authorized transition target. Both remain exactly `none` in the final
composite `F`, and any optional matching `active-operations` or
`administrative-locks` postcondition is none-only. A present live Git
administrative lock still causes the governing guard to deny.

An explicit exact baseline supplies the complete target value directly. When
a clean or none branch requires HEAD, object, index, ignore, filesystem,
checkout, or other live information, Phase 3 materializes and verifies the
complete canonical target projection before issuance. An unprovable target
denies issuance.

For every transition, `from` equals `B(target)` by direct RFC 8785 JCS-byte
equality after strict parsing, static validation, and canonical-array checks;
no hash is used. A structurally different encoding is not equivalent. The
existing `from != to` and unique-target requirements remain mandatory. A
transition cannot use another transition's `to` as its `from`.

All seven transition branches apply simultaneously and independently of array
order:

```text
F = Apply(B, permittedTransitions)
```

For each unique target, `Apply` replaces the baseline value with that
transition's `to`; every unmentioned target retains its baseline value. No
sequential dependency is permitted. The wire array still uses canonical
`T(transition)` order, but reordering valid independent transitions cannot
change `F`.

The complete `F` is reconstructed into the unique canonical condition
branches and revalidated as one composite. Validation includes ref/HEAD
compatibility, index/tracked equality and coverage, index/submodule equality
and coverage, tracked/submodule disjointness, the canonical D3 untracked and
ignored inventories, explicit path-set disjointness, stage-0 and supported-mode
restrictions, D2 checkout/observation rules, the invariant that active
operations and administrative locks are each exactly `none`,
and every other baseline cross-dimension invariant.

##### Ordinary operation-capability closure

For the writing TaskContract `C`, define only as normative static-contract
notation:

```text
M = {create, modify, delete}
Acap = set(C.spec.authorizedScope.capabilities)
Qcap = set(C.spec.prohibitedScope.capabilities)
```

The existing scope rules keep `Acap` and `Qcap` disjoint. `M` uses three
existing members of the unchanged 13-member capability vocabulary; it adds no
wire member, helper object, reason code, or transition branch.

For every ordinary repository path, project the complete `B` and valid `F`
into exactly the information needed for ordinary-file operation
classification: `absent`, `present(exact known ordinary-file identity)`, or
`present(opaque ordinary-file identity)`. The per-path conservative operation
contribution is:

| Ordinary `B` projection | Ordinary `F` projection | Contribution |
| --- | --- | --- |
| `absent` | `present` | `{create}` |
| `present` | `absent` | `{delete}` |
| known `present` | known unequal `present` | `{modify}` |
| known `present` | known equal `present` | empty |
| `absent` | `absent` | empty |
| `present` with either identity opaque or equality otherwise unprovable | `present` | conservative possible `{modify}` |

Opaque present-to-present state is therefore not a proven no-op and requires
`modify`; opacity alone does not reject the contract when `modify` is
authorized and not prohibited.

Define `Oplan(B,F)` as the union across all ordinary paths of every member of
`M` that can occur in any effect consistent with that path's complete `B` and
`F` projections. It is the conservative least upper bound, not a branch-name
lookup. The seven transition branches remain unchanged and are treated as
follows:

- `ref-state` and `head-state` contribute no ordinary-file mutation;
- `index-entry` contributes no ordinary-file mutation in this ordinary-file
  model;
- `submodule-entry` contributes no outer-repository ordinary-file mutation;
  and
- `tracked-entry`, `untracked-path`, and `ignored-path` derive their
  contributions from complete `B`/`F` path state.

For tracked ordinary state, let `P` be `clean`, `modified`, or `type-changed`,
and let `D` be `deleted`. `P -> D` contributes `delete`; `D -> P` contributes
`create`; `P -> P` with known mode or content change contributes `modify`;
proven equal mode and content contributes nothing; and equality-unprovable
`P -> P` contributes possible `modify`. A tracked `deleted` value projects to
ordinary absence, so `deleted -> modified` is `create` and
`modified -> deleted` is `delete`. `entryPresence.state` alone is insufficient:
a tracked entry that becomes absent from that inventory may leave the same
ordinary leaf represented as untracked or ignored, or may leave no leaf.

Untracked and ignored absent-to-present state contributes `create`, and
present-to-absent contributes `delete`. Those inventories do not carry complete
mode/content identity, so a leaf present before and after whose equality cannot
be proved contributes possible `modify`. A classification transfer alone does
not imply `create` plus `delete` when the same ordinary leaf remains present.
A rename-equivalent effect at two paths contributes `delete` for the old path
and `create` for the new path.

Only after the complete `F` passes every existing cross-dimension invariant, a
valid writing contract requires exactly:

```text
Oplan(B,F) ⊆ Acap
and
Oplan(B,F) ∩ Qcap = ∅
```

All operations implied across all paths are required; authorization for only
one side of a rename-equivalent delete/create pair is insufficient. These
predicates extend D7 only. They do not alter D6, D8, D10, D12, the seven
transition shapes, or any digest projection.

Every dimension changed by at least one of the seven permitted transitions
requires its matching postcondition from the table, and that postcondition's
`expected` value equals the corresponding canonical projection of `F`. A
postcondition for an unchanged dimension is optional; if present, it equals
the unchanged baseline projection. An optional active-operation postcondition
or administrative-lock postcondition is none-only. `scope-contained` and
`lease-state` retain their independent mandatory rules.

Phase 1 owns explicit closed-data comparison, simultaneous application,
canonical reconstruction, static final-composite validation, `Oplan(B,F)`
derivation over available closed data, and the two operation-capability
predicates. Phase 3 owns HEAD/live/object/index/filesystem materialization
before issuance. Phase 4 compares final evidence with `F`, attributes
transitions and actual effects, and verifies scope and postconditions.

Positive vectors include independent simultaneous changes among the seven
permitted targets whose order does not affect the same valid nine-dimension
final composite while active operations and administrative locks remain none.
Negative vectors cover baseline/`from` mismatch, the retired active-operation
or administrative-lock transition, an attempted sequential dependency, an
invalid final cross-dimension composite, a missing postcondition for a changed
dimension, a mismatched final postcondition, and drift asserted by a
postcondition on an unchanged dimension.

Local constraints enforce the complete four-row mode/write/lease truth table,
including non-widening effective mode, `leaseRequired == allowWrite`, exact
`leaseId` presence, and any present `lease-state` postcondition. They also
require non-empty Domains, require effective scope not to exceed requested
scope structurally where provable, and require the TaskContract chronology
defined below. Phase 1 can
check reference and representation integrity but cannot prove trusted
issuance, authenticate a digest, observe Git, establish current lease
ownership, or grant authority because the JSON validates. Concrete contracts
remain outside the target worktree.

### `ExecutionReceipt`

`metadata.id` is the receipt ID and is narrowed to a canonical lower-case UUID.
The closed `spec` inventory has exactly 17 fields represented by 16 data rows
below because `startedAt` and `finishedAt` share one row. Conditional rules
below determine when the lease root and ordinary-operation carrier are present.

| Field | Design |
| --- | --- |
| `receiptVersion` | Constant string `1` |
| `taskId` | Canonical UUID |
| `origin` | One closed discriminated union branch, `issued-contract` or `pre-contract-denial` |
| `acquisitionBinding` | Closed stable-acquisition binding required iff issued lease-required or acquired denial; otherwise forbidden |
| `executionOutcome` | Shared execution outcome |
| `verificationOutcome` | Shared verification outcome |
| `releaseOutcome` | Shared release outcome |
| `lifecycleOutcome` | Shared overall lifecycle outcome |
| `unresolvedCoordinationWarnings` | Append-only sequenced sanitized warnings |
| `checks` | Append-only sequenced check evidence with expected/observed sanitized summaries and reason codes |
| `changedPaths` | Canonical repository-relative path set |
| `ordinaryOperationEvidence` | Conditional A2 carrier: a canonical array of closed per-path records containing exactly required `path` and `operations` members |
| `reasonCodes` | Canonical reason-code set |
| `sanitization` | Closed required `profileId`, `applied`, `redactionCount`, and `completedAt` record |
| `receiptDigest` | `profile.digest.execution-receipt-v1` over the complete `ExecutionReceipt` resource excluding only `spec.receiptDigest`, exactly as cataloged in section 10 |
| `startedAt` / `finishedAt` | Canonical UTC timestamps |

Under RS-1, `startedAt` is the lower time boundary of the complete lifecycle
evidence serialized in the receipt. The definition is identical for
`issued-contract` and `pre-contract-denial`: it is no later than every
`checks[]` member's `observedAt`, and on a denial it is also no later than
`preContractEvidence.observedAt`. For every issued receipt it is no later
than the referenced TaskContract's `freshness.issuedAt`. It is not an action-
freshness timestamp, a trusted-clock assertion, or permission to omit
pre-contract evidence.

Every `changedPaths` member is a valid actual repository-relative path from the
revised universe. A runtime-resolved Git administrative effect cannot appear as
a successful ordinary member, cannot be omitted while claiming successful
`scope-contained` verification, and instead requires failed or indeterminate
scope evidence.

#### Issued-receipt path-and-operation scope binding

For a complete `issued-contract` receipt and its referenced TaskContract `C`,
reuse `M`, `Acap`, and `Qcap` above and define the two exact path languages:

```text
Apath =
  the union of every path language in C.spec.authorizedScope.paths

Qpath =
  the union of every path language in C.spec.prohibitedScope.paths
```

`Qpath` is deliberately used here so it cannot be confused with the pre-action
check set `P` below. Both unions use the existing anchored path-pattern grammar
over the existing valid repository-relative-path universe.

Define the attempted-outcome and carrier-presence predicates:

```text
Attempted(e) :=
  e in {succeeded, failed, cancelled, indeterminate}

CarrierRequired(R,C) :=
  R.spec.origin.type == "issued-contract"
  and C.spec.allowWrite == true
  and Attempted(R.spec.executionOutcome)
```

`ExecutionReceipt.spec.ordinaryOperationEvidence` is present if and only if
`CarrierRequired(R,C)`. It is therefore required for every issued writing
attempt, including failed, cancelled, and indeterminate execution, and is
forbidden for pre-contract denials, every `allowWrite: false` or plan-only
contract, and an issued writing contract whose execution is `not-attempted`.
Later release failure changes neither presence nor contents. A writing attempt
with complete evidence of zero attributable ordinary effects has exactly the
one canonical representation `ordinaryOperationEvidence: []`.

When present, the carrier is an array of zero or more closed
`OrdinaryOperationEvidenceRecord` values. Each record contains exactly two
required members and permits no additional member:

```text
OrdinaryOperationEvidenceRecord:
  path: repositoryRelativePath
  operations: non-empty canonical set of create | modify | delete
```

The `path` member reuses the existing `repositoryRelativePath` profile without
normalization, case folding, or repair, including strict UTF-8, already-NFC
text, the 1-through-4096-scalar limit, POSIX separators, and rejection of an
exact lower-case `.git` component at any depth. Outer records are strictly
increasing by `S(record.path)`; duplicate paths and non-canonical input order
are invalid. Each `operations` array has one through three distinct members,
is strictly increasing by `S(operation-token)`, and therefore has the complete
possible order `create`, `delete`, `modify`. Empty arrays, duplicate tokens,
unknown tokens, and non-canonical input order are invalid and are never
silently sorted.

For each unique path, `operations` is the set union of every attributable
ordinary operation on that path during the attempt. Repetition, reversal, and
return to baseline do not erase a member: modify then restore is
`["modify"]`; create then modify is `["create","modify"]`; delete then
recreate and create then delete are both `["create","delete"]`; repeated
modify is `["modify"]`. A rename-equivalent effect records
`["delete"]` on the old path and `["create"]` on the new path. There is no
`rename`, `move`, `copy`, `replace`, `touch`, `unknown`, or other operation
token and no sequence, timestamp, artifact, digest, or external-reference
member.

Define the durable reconstruction:

```text
EvidencePaths :=
  {record.path | record in R.spec.ordinaryOperationEvidence}

for every p in EvidencePaths:
  OexecByPath[p] :=
    set(record.operations)
    for the unique record whose path == p

Oexec :=
  the union over every OexecByPath[p]
```

`Oexec` is reconstructed only from this carrier, never from `changedPaths`,
final repository state, summaries, `profileId`, `reasonCodes`, or human
interpretation. `ordinaryOperationEvidence` is the durable serialized
representation of the complete attributable ordinary-operation set known for
the attempt. It retains transient effects, restored effects, effects whose
final state equals baseline, multiple operation types on one path, and both
sides of a rename-equivalent effect. `Oplan(B,F)` remains separately necessary
for contract closure but is insufficient to recover actual intermediate
effects.

Every attributable ordinary-effect path must be present in the carrier, and
the exact cross-artifact relationship is:

```text
EvidencePaths ⊆ set(R.spec.changedPaths)
```

The reverse inclusion is not required. Every carrier path therefore also
appears in `changedPaths`, including transient or restored paths; an extra
`changedPaths` member does not invent an operation. If such an extra path is
independently known to carry an ordinary effect, omitting it from the carrier
violates evidence completeness.

For a writing contract, successful `scope-contained` conformance requires
exactly both path containment and operation-capability containment:

```text
for every x in set(R.spec.changedPaths):
  x is in Apath
  and
  x is not in Qpath

for every x in EvidencePaths:
  x is in Apath
  and
  x is not in Qpath

and

EvidencePaths ⊆ set(R.spec.changedPaths)
and
Oexec ⊆ Acap
and
Oexec ∩ Qcap = ∅
```

Path or capability prohibition overrides authorization. A
`verificationOutcome: passed` writing receipt requires both compound
predicates and requires
`finalV("scope-contained").outcome == "passed"` through an exact
`postconditionRef` to the contract's mandatory obligation. The B path and
operation-capability predicates remain unchanged and govern whether the
already-selected `finalV("scope-contained")` satisfies B. C-UNIVERSAL-PASS
independently governs whether the complete V history may culminate in top-level
passed verification; it changes neither global greatest-sequence V selection,
per-type `finalV(t)` selection, nor any B operation-capability predicate.

One unauthorized or prohibited path or operation invalidates a passed claim.
`verificationOutcome` is then `failed` or `indeterminate` according to the
available evidence, `lifecycleOutcome` is not `succeeded`, and every offending
observed path and effect remains in `changedPaths` and
`ordinaryOperationEvidence`.
Validators and evidence producers do not drop, sanitize, normalize, rewrite,
or otherwise hide an offending observation. If attribution cannot establish
whether an ordinary mutation occurred or whether attribution is complete,
every known attributable operation is still included, ambiguity is not
successful no-op evidence, and verification is indeterminate. Phase 1 validates
the serialized carrier and its static bindings; Phase 4 owns runtime
attribution truth and completeness. A receipt digest protects the serialized
evidence from mutation but does not prove the truth of omitted history.

The fail-closed carrier classifications are:

| Condition | Required classification |
| --- | --- |
| Required carrier missing, or carrier present where forbidden | Invalid receipt before receipt-digest acceptance |
| Required carrier is `[]` with complete zero-effect evidence | Valid representation |
| `[]` omits a known attributable operation | Evidence-conformance invalid; a failed outcome does not cure omission |
| `[]` while attribution is unresolved | Structurally valid representation, but scope verification is indeterminate and cannot pass |
| Empty `operations`, duplicate path or operation, non-canonical outer or nested order, invalid path, exact `.git` component, unknown operation, or unknown record member | Structurally invalid |
| Carrier path absent from `changedPaths` | Invalid cross-artifact binding |
| Extra `changedPaths` member with no independently known ordinary effect | Allowed by the one-way subset and does not invent an operation |
| Carrier path outside `Apath`, in `Qpath`, `Oexec` not a subset of `Acap`, or non-empty `Oexec ∩ Qcap` | Structurally valid evidence, but `scope-contained` fails |
| Effect occurrence or completeness cannot be established | Include every known attributable operation; verification is indeterminate |
| Malformed or statically invalid carrier with a matching receipt digest | Invalid; hashing cannot cure an earlier validation failure |

For every `allowWrite: false` contract, the existing D5 invariant remains
unchanged: `permittedTransitions`, `changedPaths`, and the ordinary operation
set are exactly empty, while the carrier is forbidden. An `execute-tests` or
build capability does not widen ordinary-file mutation.

The existing `profile.digest.execution-receipt-v1` rule covers the complete
finalized `ExecutionReceipt` except only `spec.receiptDigest`.
`ordinaryOperationEvidence` is therefore automatically part of the existing
receipt-digest preimage whenever present. No new digest profile, operation-
evidence digest, external artifact, dependency-graph node, computation, or
exact-copy relation is added by the operation carrier; the Option-B graph has 12 paths, 10 computations, and 2 exact copies. Structural and static carrier failures reject
before valid receipt-digest acceptance.

The five focused positive changed-path scope classes remain exactly the
following path-predicate owners, each with operation-capability containment
satisfied as mandatory non-additive background:

1. one changed path in `Apath` and not in `Qpath`, with passed verification
   and passed `finalV("scope-contained")` referenced evidence;
2. multiple changed paths, every one in `Apath` and not in `Qpath`, with passed
   verification and passed `finalV("scope-contained")` referenced evidence;
3. an empty writing result with required `ordinaryOperationEvidence: []` and
   complete passed no-effect verification evidence;
4. one or more out-of-scope paths retained under failed verification and a
   non-succeeded lifecycle; and
5. one or more out-of-scope paths retained under indeterminate verification
   and a non-succeeded lifecycle.

The six dedicated negative changed-path scope classes remain exactly the
following path-predicate owners, each with otherwise-valid
operation-capability evidence:

1. a valid ordinary path outside every language in `Apath` with passed
   verification;
2. a path in both `Apath` and `Qpath` with passed verification;
3. a path only in `Qpath` with passed verification;
4. multiple paths with one unauthorized member and passed verification;
5. any scope violation combined with `lifecycleOutcome: succeeded`; and
6. passed verification without a passed, exactly referenced
   `finalV("scope-contained")`.

A non-writing receipt with non-empty `changedPaths` remains an additional
required invalid class in the existing D5 family. It is cross-referenced here
but is not counted again in the focused 5/6 scope family.

The editorial family `ORDINARY-CAPABILITY-CLOSURE` has prefix `OC`
and exactly these three positive and eight negative primary predicates:

| Primary ID | Exact planned predicate |
| --- | --- |
| `OC-P01` | a B/F-consistent `create` with `create` authorized and not prohibited |
| `OC-P02` | a B/F-consistent or actual `modify` with `modify` authorized and not prohibited |
| `OC-P03` | a B/F-consistent `delete` with `delete` authorized and not prohibited |
| `OC-N01` | `create` is in `Oplan(B,F)` but absent from `Acap` |
| `OC-N02` | `modify` is in `Oplan(B,F)` but absent from `Acap` |
| `OC-N03` | `delete` is in `Oplan(B,F)` but absent from `Acap` |
| `OC-N04` | `create` is in `Oplan(B,F)` and in `Qcap` |
| `OC-N05` | `modify` is in `Oplan(B,F)` and in `Qcap` |
| `OC-N06` | `delete` is in `Oplan(B,F)` and in `Qcap` |
| `OC-N07` | a multi-path B/F composite uses valid paths but at least one implied ordinary operation is absent from `Acap` |
| `OC-N08` | net B/F effects pass contract closure, but an actual transient or restored operation on an authorized path makes `Oexec` exceed or intersect capability scope |

Mandatory non-additive OC variants cover untracked create/delete, ignored
create/delete, tracked `D -> P` create, tracked `P -> D` delete, tracked
`P -> changed-P` modify, a known ordinary no-op, ref/head/index/submodule
ordinary no-op, opaque present-to-present with `modify` authorized, absent, and
prohibited, create+modify+delete across distinct paths with all three
authorized, and rename-equivalent delete-old/create-new with both capabilities
required. These variants do not increase 3/8. OC identifiers do not reuse the
separate HX family, and OC adds no wire field, enum, reason code, capability
token, transition, digest member, or runtime implementation.

The separate focused `OPERATION-EVIDENCE` family has prefix `OE`, exactly ten
positive primary owners, and exactly eleven negative primary owners:

| Primary ID | Exact planned predicate |
| --- | --- |
| `OE-P01` | one carrier path with `["modify"]` |
| `OE-P02` | one carrier path with `["create"]` |
| `OE-P03` | one carrier path with `["delete"]` |
| `OE-P04` | one carrier path with `["create","modify"]` |
| `OE-P05` | one carrier path with `["create","delete"]` |
| `OE-P06` | multiple carrier records in canonical path order |
| `OE-P07` | transient modify followed by restoration retains `["modify"]` |
| `OE-P08` | transient create/delete followed by restoration retains `["create","delete"]` |
| `OE-P09` | rename-equivalent old path has `["delete"]` and new path has `["create"]` |
| `OE-P10` | complete carrier satisfies `EvidencePaths ⊆ changedPaths`, both path predicates, and permitted reconstructed `Oexec` |
| `OE-N01` | required carrier is missing |
| `OE-N02` | carrier is present where forbidden |
| `OE-N03` | duplicate carrier path |
| `OE-N04` | empty `operations` |
| `OE-N05` | duplicate operation token |
| `OE-N06` | non-canonical outer-record order |
| `OE-N07` | non-canonical operation order |
| `OE-N08` | unknown operation token |
| `OE-N09` | known attributable operation is omitted |
| `OE-N10` | carrier path is absent from `changedPaths` |
| `OE-N11` | ambiguous or unresolved attribution is represented as a passed successful no-op |

OE is exactly 10/11/21 and is not merged into OC. Invalid paths and reserved
`.git` components remain D3/path-profile owned; unauthorized or prohibited
paths remain changed-path-scope owned; modify-only transient create/delete
forms remain OC-N08 variants; rename missing create or delete authority remains
an OC-N07 rename variant with the corresponding existing operation-capability
fault; and malformed-carrier digest-acceptance forms remain non-additive
validation-order variants of the corresponding OE structural owner. No
duplicate ownership changes any frozen aggregate. The existing expanded
independent affected-family aggregate is 168; OC and OE remain separate non-additive case inventories.

`spec.origin` is exactly one of these closed branches:

- **`issued-contract`:** requires `type` fixed to `issued-contract`, `contractId`, `contractDigest`, `resolvedTarget`, and `effectiveMode`. `resolvedTarget` contains the Project, role, logical worktree, and complete canonical Domain references. This branch represents every receipt produced after a trusted contract was issued. It forbids `denialCheckpoint`, `preContractEvidence`, and the denial-only `origin.leaseAcquisition`. The receipt-level acquisitionBinding member follows the unified Option-B presence rule.
- **`pre-contract-denial`:** requires `type` fixed to `pre-contract-denial`, `denialCheckpoint`, `preContractEvidence`, and `leaseAcquisition`. It forbids `contractId`, `contractDigest`, `resolvedTarget`, and `effectiveMode`, so it cannot fabricate a contract or claim a fully authorized target.

`denialCheckpoint` is a closed vocabulary containing exactly
`intent-validation`, `project-domain-resolution`, `role-routing`,
`host-binding`, `initial-preflight`, `pre-issuance-revalidation`,
`lease-acquisition`, `post-acquisition-revalidation`, and
`contract-issuance`. It contains no checkpoint that occurs only after
contract issuance.

`preContractEvidence` is a closed sanitized record requiring `observedAt`, a
tagged `evidenceDigest` bound only to the exact
`profile.digest.pre-contract-evidence-v1` catalog projection, a
`controllerCheckId` under the closed `checkIdentifier` profile, a non-empty
canonical `reasonCodes` set, and a bounded `sanitizedSummary`.

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

`sanitization` is a closed record with exactly four required fields:
`profileId: profileIdentifier`, `applied: boolean`,
`redactionCount: integer` from 0 through 4294967295 under the numeric profile,
and `completedAt: timestamp`. These are evidence claims only; structural
validity does not prove that sanitization was complete.

The owner-selected static invariant is
`ExecutionReceipt.spec.sanitization.applied == true` for every serialized
receipt. `true` means that the selected profile actually completed its required
sanitization or evaluation; it does not mean that any redaction occurred, so
`redactionCount: 0` is valid. `false` means required sanitization is incomplete
and invalidates the serialized receipt before a passed terminal F, receipt-
digest projection, or delivery binding can be accepted. The wire member remains
a Boolean; no alternate false/no-op branch, enum, status field, or F field is
introduced.

#### Warning and check records

`ExecutionReceipt.spec.unresolvedCoordinationWarnings` is an append-only array
of at most 4096 closed records:

| Field | Presence and exact type |
| --- | --- |
| `sequence` | required integer 0 through 4095 under the numeric profile |
| `code` | required `reasonCode` |
| `profileId` | required `profileIdentifier` |
| `sanitizedSummary` | optional `sanitizedSummary` |
| `relatedCheckId` | optional `checkIdentifier` |

Sequence values are contiguous from zero and equal array position. Warning
order is evidence order and MUST NOT be sorted. Warning code and profile ID are
identifiers, not authority, and warning text remains subject to Phase 4
sanitization.

`ExecutionReceipt.spec.checks` is an append-only array of at most 4096 closed
records:

| Field | Presence and exact type |
| --- | --- |
| `sequence` | required integer 0 through 4095 under the numeric profile |
| `checkId` | required `checkIdentifier` |
| `checkType` | required closed enum below |
| `outcome` | required phase-dependent outcome under the exact `checkType` conditional below |
| `observedAt` | required shared timestamp |
| `profileId` | required `profileIdentifier` |
| `expectedSummary` | optional `sanitizedSummary` |
| `observedSummary` | optional `sanitizedSummary` |
| `postconditionRef` | optional closed `{type}` reference; permitted only for `post-execution-verification` and reusing the exact eleven-value required-postcondition `type` enum |
| `leaseAcquisitionRef` | closed `{checkId}` reference; required on A, every R, and every L on both stable-acquired origins; forbidden elsewhere |
| `reasonCodes` | required set-like `reasonCode[]` |

The complete `checkType` vocabulary is:

```text
intent-validation
project-domain-resolution
role-routing
host-binding
initial-preflight
lease-acquisition
post-acquisition-revalidation
pre-issuance-revalidation
contract-issuance
pre-action-revalidation
execution
post-execution-verification
lease-release
receipt-finalization
```

The `outcome` member uses this closed conditional vocabulary:

```text
if checkType == "execution":
  outcome is one of
    "succeeded", "failed", "cancelled", "indeterminate"

if checkType != "execution":
  outcome is one of
    "passed", "failed", "indeterminate"
```

An execution check using `passed`, a non-execution check using `succeeded` or
`cancelled`, and any check using an unknown outcome are invalid. No
`executionResult`, `detail`, or equivalent second result field exists.

The compact leaseAcquisitionRef is closed {checkId}. The unified Option-B binding requires it exactly on A, every R, and every L on stable-acquired paths, with exact equality to acquisitionBinding.checkId. It is forbidden on every other check and every other lifecycle. All references are covered by the complete receipt digest. The complete acquired-R and acquired-I goldens below include these members.

A `receipt-finalization` check is a closed specialization whose required and
permitted members are exactly `sequence`, `checkId`, `checkType`,
`outcome`, `observedAt`, `profileId`, and `reasonCodes`. It forbids
`expectedSummary`, `observedSummary`, `postconditionRef`, and
`leaseAcquisitionRef`; record
closure also forbids `sanitizedSummary`, `detail`, `payload`, and every
other free-form or unknown member.

FSAFE-1 closes the complete finalization identity domain. For every check,
`checkType == receipt-finalization` implies the exact protocol tuple
`checkId == check.receipt-finalization`,
`profileId == profile.validation.v1`, `reasonCodes == []`, and
`outcome == passed`. This is the primitive F implication; there is no
separate primitive `checkId == check.receipt-finalization`-implies-F
predicate.

Every serialized receipt independently requires exactly one F and requires
receipt-wide `checkId` uniqueness. Consequently, a non-F check cannot use
`check.receipt-finalization` in a valid receipt: it would duplicate the
mandatory F ID and is rejected by the generic check-ID uniqueness rule. That
non-F exclusion is a derived, non-additive consequence of the exact F tuple
plus global uniqueness, not an independently isolatable RF predicate.

The generic `checkIdentifier` lexical profile is unchanged.
`profile.validation.v1` is not F-exclusive and may continue to appear on
other valid checks; an empty `reasonCodes` array is not imposed universally
on other checks. But a regex-valid producer alternative is not a finalization
identity. In particular,
`check.c-users-alice.secrets.api-key-abcd1234`,
`profile.synthetic.secret.sk-live-abcdef123456`, and
`reason.synthetic.secret.token-abcdef123456` are invalid in the corresponding
F tuple positions, as is every other non-reserved alternative.

For post-sanitization receipt-finalization evidence, textual identity fields
are safe-by-construction only when their complete semantic value domain is
closed by the protocol. Lexical validity alone is insufficient. The
finalization marker therefore uses the exact reserved protocol tuple
`check.receipt-finalization / profile.validation.v1 / []`. A
producer-supplied alternative that merely satisfies the generic identifier
grammar is invalid. This protection targets arbitrary post-sanitization text,
host or operator material, path-like material, secret-like strings, and
diagnostic prose. It does not claim information-theoretic covert-channel
elimination.

When present, `postconditionRef` is a closed object containing exactly one
required `type` member. Its value is one of the same eleven strings in
`TaskContract.spec.requiredPostconditions[].type`; it is not an open identifier,
free-form label, copy of `expected`, or embedded postcondition. The member is
allowed only when `checkType == post-execution-verification`. Each of the other
thirteen check types forbids it. A verification check may omit the member and
remain general verification evidence, but that unreferenced check cannot
satisfy a particular required-postcondition obligation.

Check sequences are contiguous from zero and equal array position; checks
preserve evidence order and MUST NOT be sorted. `checkId` values are unique
within a receipt. Each required `reasonCodes` array is unique and strictly
ordered by `S(code)`; it may be empty when no reason code applies.

Every present warning `relatedCheckId` MUST equal exactly one `checkId` in the
same `ExecutionReceipt`. Check IDs are already unique, so resolution is
one-to-one. The referenced check may occur at any sequence position: forward
and backward references are both allowed, and validity is independent of the
warning and check array positions. References outside the same receipt are
forbidden, and a `ReceiptDeliveryResult` cannot satisfy the reference. Phase 1
static validation performs this closed-receipt reference check.

Planned positive vectors include a warning without `relatedCheckId`, a warning
referring to an earlier check, and a warning referring to a later check.
Planned negative vectors include a dangling `relatedCheckId`, a duplicate
`checkId`, a reference to a check ID appearing only in another receipt, and a
reference to a delivery-result identifier.

#### Issued-contract final applicable pre-action, execution, and verification checks

For one complete issued-contract receipt and referenced TaskContract pair,
define:

```text
P =
  every ExecutionReceipt.spec.checks[] member where
  checkType == "pre-action-revalidation"

E =
  every ExecutionReceipt.spec.checks[] member where
  checkType == "execution"

V =
  every ExecutionReceipt.spec.checks[] member where
  checkType == "post-execution-verification"

attempted =
  ExecutionReceipt.spec.executionOutcome is one of
  "succeeded", "failed", "cancelled", or "indeterminate"
```

The existing check-array requirements remain prerequisites: each `sequence`
equals its array position, sequences are contiguous from zero, and `checkId`
is unique. When `P` is non-empty, define:

```text
finalApplicablePreActionCheck =
  the unique member of P with the greatest sequence
```

This is equivalently the last `pre-action-revalidation` member in the
validated checks array. Selection uses `sequence` only. It does not use the
maximum `observedAt`, timestamp tie-breaking, locale, array serialization,
`checkId`, or implementation-specific iteration order. Sequence uniqueness
and contiguity make the selected member deterministic. Within the receipt's
evidence claim, the final applicable check is the represented authorization
point; the receipt itself remains non-authorizing evidence.

When `E` is non-empty, define:

```text
finalApplicableExecutionCheck =
  the unique member of E with the greatest sequence
```

This is equivalently the last `execution` member in the validated checks array.
Selection uses `sequence` only under the existing contiguous-sequence and
unique-check-ID prerequisites. It does not use maximum `observedAt`, timestamp
tie-breaking, outcome, locale, serialization, `checkId`, or iteration order.
The selected member's `checkType` is exactly `execution`, so its conditional
outcome is exactly one of `succeeded`, `failed`, `cancelled`, or
`indeterminate`. Under `EXECUTION-FAILURE-TERMINALITY: EF-1`, every member of
E strictly before `finalApplicableExecutionCheck` has outcome `succeeded`.
Equivalently, any E whose outcome is `failed`, `cancelled`, or `indeterminate`
is `finalApplicableExecutionCheck`, and no later E member exists in that
lifecycle. The unique greatest-sequence member still controls the receipt-
level execution outcome. EF-1 is an outcome/terminality rule and introduces no
E-to-E timestamp monotonicity.

When `V` is non-empty, define:

```text
finalApplicableVerificationCheck =
  the unique member of V with the greatest sequence
```

This is equivalently the last `post-execution-verification` member in the
validated checks array. Selection again uses `sequence` only under the existing
contiguous-sequence and unique-check-ID prerequisites. It does not use maximum
`observedAt`, timestamp tie-breaking, outcome, locale, serialization,
`checkId`, or iteration order. Earlier verification checks may have different
outcomes on a non-passed receipt; the unique greatest-sequence member remains
final and controls the receipt-level verification outcome.

Phase 1 static conformance requires:

```text
for every p in P where p.outcome == "passed":
  p.observedAt < TaskContract.spec.freshness.expiresAt

if attempted:
  count(P) >= 1
  count(E) >= 1
  count(V) >= 1
  for every p in P:
    p.outcome == "passed"
  for every e in E except finalApplicableExecutionCheck:
    e.outcome == "succeeded"
  finalApplicablePreActionCheck.outcome == "passed"
  finalApplicableExecutionCheck.checkType == "execution"
  executionOutcome == finalApplicableExecutionCheck.outcome
  finalApplicablePreActionCheck.observedAt
    < TaskContract.spec.freshness.expiresAt
  for every e in E:
    finalApplicablePreActionCheck.sequence < e.sequence
    finalApplicablePreActionCheck.observedAt <= e.observedAt
  for every e in E:
    for every v in V:
      e.sequence < v.sequence
      e.observedAt <= v.observedAt
  verificationOutcome == finalApplicableVerificationCheck.outcome
  if verificationOutcome == "passed":
    for every v in V:
      v.outcome == "passed"

if executionOutcome == "not-attempted":
  count(E) == 0
  count(V) == 0

if any p in P has outcome "failed" or "indeterminate":
  p == finalApplicablePreActionCheck
  every earlier member of P has outcome "passed"
  no later P exists
  executionOutcome == "not-attempted"
  verificationOutcome == "not-performed"
  count(E) == 0
  count(V) == 0
```

C-UNIVERSAL-PASS does not terminalize V collection: a failed or indeterminate
V may be followed by later V evidence. It imposes no failed-versus-indeterminate
severity precedence and does not require identical V outcomes on non-passed
receipts; the greatest-sequence member still binds the matching non-passed
top-level outcome. Once any V in one lifecycle is non-passed, that lifecycle
cannot regain passed verification or a succeeded lifecycle. A successful retry
or reverification requires a fresh lifecycle under fresh applicable
authorization, without adding retry or verification epochs, recovery IDs,
counters, kinds, check fields, or receipt fields.

The expiry boundary is strict. Equality at expiry and any later passed check
are invalid, including in a `not-attempted` receipt. Every P in an attempted
receipt is passed and strictly pre-expiry. A failed or indeterminate P
terminates the governed action attempt immediately: the same receipt/lifecycle
has no later P, E, or V and uses the existing
`not-attempted/not-performed` fail-closed path. If a lease was acquired, the
existing release-required evidence and lifecycle precedence still apply before
sanitization and terminal F; in all cases the lifecycle follows the existing
denied/fail-closed and release-precedence semantics. It can never
be `succeeded` or `cancelled`. Retry requires a fresh task, routing and live
inspection, applicable lease acquisition and pre-issuance revalidation, trusted
TaskContract issuance, post-contract revalidation, and a new receipt lifecycle.
No retry counter, epoch, same-contract recovery field, new kind, or new receipt
field is introduced.

EF-1 is the distinct attempted-execution terminality rule. A `failed`,
`cancelled`, or `indeterminate` E records attempted execution and terminates
only further E in the same lifecycle: that member is the final applicable E,
no later E exists, and `executionOutcome` remains exactly its outcome. It does
not convert the receipt to `executionOutcome: not-attempted` or
`verificationOutcome: not-performed`. By contrast, a failed or indeterminate
P means execution was not attempted and retains the P terminality rules above.

All E, including a final non-success E, still precede V. V remains required for
attempted execution and retains its existing ordering, greatest-sequence,
per-postcondition, and `verificationOutcome` rules. Terminal processing still
performs post-execution verification, captures pre-release evidence, attempts
ownership-checked L when release is required, applies sanitization, records
terminal F, validates the receipt digest, and attempts delivery. A failed or
indeterminate release leaves unresolved lease state blocking and never
authorizes a later E.

If execution must be attempted again after a non-success E, the retry starts a
fresh lifecycle and repeats task resolution, exact Project and Domain
resolution, routing, HostOverlay binding, live Git and runtime inspection,
lease acquisition when required, post-acquisition or no-lease pre-issuance
revalidation, trusted TaskContract issuance, and post-contract immediately-
before-action P before any new E. The same contract/lifecycle never appends a
later E after a non-success E. No retry/recovery wire state, public field,
kind, digest, or chronology edge is introduced.

The Review-12 counterexample contains an earlier failed or indeterminate P, a
later passed/pre-expiry final P, and then E and V under any attempted
`executionOutcome`. The superseded final-P-only rule accepted that shape; the
all-P-passed and first-failure terminality rules reject it before receipt-digest
acceptance.

For an attempted receipt, every execution check must occur after the final
applicable pre-action check by sequence and at or after it by timestamp. One
execution sequence or timestamp before that authorization point invalidates
the receipt even when another execution check occurs later; a later execution
check cannot cure the earlier universal-ordering violation. Every verification
check must follow every execution check by sequence and must be at or after
every execution check by timestamp. One verification check before or
interleaved with execution by either relation invalidates the receipt even when
the final verification check is otherwise valid. Timestamp equality is
permitted in both relations because `canonicalUtcTimestamp` has whole-second
precision.

Execution-check timestamps have no E-to-E monotonicity requirement. Earlier E
members may be later in time than the final E member provided every existing
final-P-to-E and E-to-V universal relation still holds. Sequence alone selects
the final E.

A final passed pre-action check may occur exactly at the permitted
issuance-side lower bound, subject to
`ExecutionReceipt.startedAt <= freshness.issuedAt <= I.observedAt <=
P.observedAt` and the universal `startedAt <= checks[].observedAt`
relation. It may also occur at the last valid whole second before expiry.
`startedAt` is the complete-recorded-lifecycle lower bound, not proof of
action freshness.
Receipt completion, verification, sanitization, release, finalization, and
delivery may occur after expiry; `finishedAt <= freshness.expiresAt` is not a
rule.

A `not-attempted/not-performed` receipt has an empty execution set `E` and an
empty verification set `V`. Its pre-action set `P` may be empty and may retain
failed or indeterminate denial evidence observed at or after expiry. Every
passed pre-action check, when present, must still be strictly pre-expiry, but no
final-passed pre-action requirement applies. Any stray execution or
verification check is invalid. No exactly-one-check rule, global check-type
uniqueness, requirement that execution checks form one contiguous region, or
requirement of exactly one verification check is introduced. This revision
introduces no check kind or denial checkpoint beyond the owner-selected
`pre-issuance-revalidation` identity and matching closed `denialCheckpoint`
enum member. It introduces no new timestamp or checkpoint field, trusted-clock
semantics, or evidence-truth claim.

#### Required-postcondition verification binding

For a complete issued-contract receipt and its already digest-verified,
field-equal referenced TaskContract `C`, define, for every required-postcondition
type `t` present in `C.spec.requiredPostconditions`:

```text
V(t) =
  every member v in V where
  v.postconditionRef.type == t

finalV(t) =
  the unique member of V(t) with the greatest sequence
```

`postconditionRef.type` is resolved only against that same complete `C`, after
the contract digest and all eight receipt/contract equalities pass. Because
required-postcondition types are unique in `C`, a valid reference identifies
exactly one obligation. A valid enum value absent from `C`, an obligation from
another contract, or a reference evaluated before contract binding is invalid.

Every attempted issued-contract receipt requires `count(V(t)) >= 1` for every
required type `t`. If `verificationOutcome == passed`, every `finalV(t)` must
have outcome `passed`; independently, C-UNIVERSAL-PASS requires every member of
V to have outcome `passed`. Greatest-sequence selection is per type: an earlier
passed `V(t)` cannot repair a later failed or indeterminate `finalV(t)`. A later
passed member remains the final evidence for that type, but cannot restore
passed top-level verification if any earlier V, including a `V(t)`, was
non-passed. No redundant all-`V(t)` predicate is introduced because `V(t)` is a
subset of V. An unreferenced member of V remains valid general evidence,
participates in C-UNIVERSAL-PASS, and satisfies no `t`.

The existing unique greatest-sequence member of all `V` remains
`finalApplicableVerificationCheck` and still controls the receipt-level
`verificationOutcome`. It may itself be referenced or unreferenced. Per-type
selection adds obligation identity without creating a second outcome field,
second verification pipeline, new postcondition type, or evidence-truth claim.
The existing not-attempted rule keeps `V` empty, so it also forbids every
`postconditionRef` in that path.

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
The eight required focused positive classes are exactly:

1. `succeeded` attempted execution with a final passed/pre-expiry check and an
   execution check after it;
2. `failed` attempted execution with a final passed/pre-expiry check and an
   execution check after it;
3. `cancelled` attempted execution with a final passed/pre-expiry check and an
   execution check after it;
4. `indeterminate` attempted execution with a final passed/pre-expiry check and
   an execution check after it;
5. a final passed check exactly at the permitted issuance-side lower-bound
   equality, followed by an execution check;
6. a final passed check at the last valid whole second before expiry, followed
   by an execution check;
7. completion and later lifecycle stages after expiry following a valid final
   passed/pre-expiry check and a later execution check; and
8. multiple pre-action checks, all passed, with the greatest-sequence final P
   strictly pre-expiry and followed by an execution check.

Every attempted-execution member of these eight positive classes contains at
least one `execution` check after the final applicable passed/pre-expiry
pre-action check.

The 37 required focused negative classes are the existing 33 classes plus
exactly four recovered-failure classes:

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

For each of cases 34 through 37, earlier `failed` and earlier `indeterminate`
are mandatory non-additive value variants of one outcome-specific predicate.
The final P is passed in each witness, so these cases do not duplicate cases
18 through 25, whose final P itself is failed or indeterminate.

Duplicate sequence, sequence gap, duplicate check ID, and other generic
check-array failures remain in their existing families and do not inflate this
37-class focused total.

#### Focused final-execution-evidence vectors

This closed family is separate from the focused pre-action,
post-execution-verification, and D6 families. Its eight positive classes are
exactly:

1. one final E `succeeded` with `executionOutcome: succeeded`;
2. one final E `failed` with `executionOutcome: failed`;
3. one final E `cancelled` with `executionOutcome: cancelled`;
4. one final E `indeterminate` with `executionOutcome: indeterminate`;
5. multiple E members with every earlier E `succeeded`, final E `succeeded`,
   and `executionOutcome: succeeded`;
6. multiple E members with every earlier E `succeeded`, final E `failed`, and
   `executionOutcome: failed`;
7. multiple E members with every earlier E `succeeded`, final E `cancelled`,
   and `executionOutcome: cancelled`; and
8. multiple E members with every earlier E `succeeded`, final E
   `indeterminate`, and `executionOutcome: indeterminate`.

The complete 12-class mismatch matrix is invalid:

| `executionOutcome` | Three invalid final-E outcomes |
| --- | --- |
| `succeeded` | `failed`; `cancelled`; `indeterminate` |
| `failed` | `succeeded`; `cancelled`; `indeterminate` |
| `cancelled` | `succeeded`; `failed`; `indeterminate` |
| `indeterminate` | `succeeded`; `failed`; `cancelled` |

Each matrix cell is one independent negative class. The
`succeeded`/final-`failed` cell contains multiple E members, including an
earlier `succeeded` member, so it also proves that an earlier matching result
cannot override a contradictory greatest-sequence final E; that class is
counted once, not twice.

The remaining nine final-E negative classes are exactly:

13. an attempted receipt with `E` empty, so every check is non-execution and no
    final E exists;
14. a `not-attempted/not-performed` receipt containing any E member;
15. an execution check using `passed`;
16. a P check using `succeeded`;
17. a V check using `succeeded`;
18. a P check using `cancelled`;
19. a V check using `cancelled`;
20. an execution check using an unknown outcome; and
21. a non-execution check using an unknown outcome.

The EF-1 addition is exactly one further primary negative class:

22. execution terminality violation: an E whose outcome is `failed`,
    `cancelled`, or `indeterminate` is followed by any later E member.

Class 22 has the mandatory `3 x 4 = 12` non-additive value variants: the
earlier terminal outcome is each of `failed`, `cancelled`, and `indeterminate`,
crossed with a later E outcome of `succeeded`, `failed`, `cancelled`, and
`indeterminate`. These are twelve witnesses for one predicate, not twelve
primary classes. Each witness keeps P valid and passed; E sequence, IDs, and
outcome vocabulary valid; top-level `executionOutcome` equal to the later
greatest-sequence E; V ordered and valid; scope, release, sanitization, F,
digest, and binding otherwise valid; and fails only because a non-success E is
followed by a later E.

Case 13 is the one explicit cross-family overlap: its four planned outcome-
specific variants correspond to focused pre-action negative cases 26 through 29.
Here they form one E-absence predicate class and satisfy both the attempted-E-
missing and all-checks-non-execution requirements; the overlap is stated and
the pre-EF-1 non-matrix inventory remains nine classes. The mechanical recount
is 12 mismatch-matrix classes + 9 existing non-matrix classes + 1 EF-1
terminality class = 22. The final-E family is therefore exactly 8 positive and
22 negative classes. All other final-E classes are non-overlapping with the
named focused families.

Multiple P members remain valid only when every member is passed and every
passed member is strictly pre-expiry. Phase 1 checks only the internal claims
in the complete artifact pair. Phase 4 retains trusted-current-time evaluation,
timestamp authenticity, actual immediacy, evidence truth, and operational
freshness enforcement.

#### Focused post-execution-verification vectors

This named family is separate from the focused pre-action family and from D6.
The ten required non-overlapping positive classes are exactly:

1. `succeeded/passed` with one matching final `E` and one later `V`;
2. `failed/passed` with one matching final `E` and one later `V`;
3. `cancelled/passed` with one matching final `E` and one later `V`;
4. `indeterminate/passed` with one matching final `E` and one later `V`;
5. `succeeded/failed` with the final `V` outcome `failed`;
6. `succeeded/indeterminate` with the final `V` outcome `indeterminate`;
7. valid `E`/`V` timestamp equality at whole-second precision;
8. multiple `E` members, all preceding one `V` by sequence and timestamp;
9. multiple `V` members after all `E` members, every V outcome `passed`, with
   the final V `passed` and `verificationOutcome: passed`; and
10. `not-attempted/not-performed` with `V` empty.

The twenty required non-overlapping negative classes are exactly:

1. `succeeded` attempted execution with `V` missing;
2. `failed` attempted execution with `V` missing;
3. `cancelled` attempted execution with `V` missing;
4. `indeterminate` attempted execution with `V` missing;
5. `succeeded` attempted execution with a `V` before an `E` and another valid
   final `V` later, proving that the later member cannot cure the violation;
6. `failed` attempted execution with a `V` sequenced before an `E`;
7. `cancelled` attempted execution with a `V` sequenced before an `E`;
8. `indeterminate` attempted execution with a `V` sequenced before an `E`;
9. a `V` interleaved between two `E` members;
10. correct sequence order but a `V` timestamp before an `E` timestamp;
11. multiple `V` members where one `V` timestamp is before an `E` while the
    final `V` is otherwise valid;
12. final `V` `passed` with receipt `verificationOutcome: failed`, including an
    earlier `V` with outcome `failed` that matches the receipt;
13. final `V` `passed` with receipt `verificationOutcome: indeterminate`;
14. final `V` `failed` with receipt `verificationOutcome: passed`; its
    mandatory non-additive C variant has an earlier unreferenced failed V, a
    later final passed V, and `verificationOutcome: passed`, with every
    unrelated predicate valid;
15. final `V` `failed` with receipt `verificationOutcome: indeterminate`;
16. final `V` `indeterminate` with receipt `verificationOutcome: passed`; its
    mandatory non-additive C variant has an earlier unreferenced indeterminate
    V, a later final passed V, and `verificationOutcome: passed`, with every
    unrelated predicate valid;
17. final `V` `indeterminate` with receipt `verificationOutcome: failed`;
18. `not-attempted/not-performed` with one stray `V` whose outcome is `passed`;
19. `not-attempted/not-performed` with one stray `V` whose outcome is `failed`;
    and
20. `not-attempted/not-performed` with one stray `V` whose outcome is
    `indeterminate`.

Except when a future fixture's primary fault belongs to the dedicated
postcondition-binding family, every planned attempted-issued class in this
10/20 family requires referenced V evidence for every required contract type,
and every passed-verification positive has every V outcome passed and each
per-type `finalV(t)` passed. Those are prerequisites, not additional cases.
Class 10 keeps V empty and therefore contains no reference. This integration
preserves the exact 10/20 total.

Case 12 proves greatest-sequence final selection because an earlier `V` matches
the receipt while the later final `V` does not. Generic sequence gaps,
duplicate sequences, duplicate check IDs, and malformed check arrays remain
outside this 10/20 family. The focused pre-action family remains 8/37, and D6
remains 13 valid and 7 invalid receipt-level combinations.

The mandatory class-14 and class-16 recovery variants use an unreferenced
earlier bad V. Referenced same-type recovery is a non-additive C-UNIVERSAL-PASS variant; it adds no PB primary.

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
and CH 20/20 positive/negative owners. The subtotal is
2*(5+23+13+14+20)=150. RC is 9/9, so the expanded aggregate is 168.
PB+AI+DP+RF has 110 numbered owner definitions; AI+RF has 74.
Scope/ordinary-capability/operation-evidence coverage remains separate,
with its existing 5/6 plus D5 cross-reference, OC 3/8, and OE 10/11
case inventories. Those unchanged case inventories are not added to the
independent five-family subtotal. These are documented conformance owners,
not a claim that executable Schema/model tests or a fixture manifest exist.

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

#### Receipt outcome consistency

Before lifecycle precedence is evaluated, every receipt must satisfy the exact
biconditional:

```text
verificationOutcome == not-performed
if and only if
executionOutcome == not-attempted
```

The complete allowed table is:

| `executionOutcome` | Allowed `verificationOutcome` |
| --- | --- |
| `not-attempted` | `not-performed` only |
| `succeeded` | `passed`, `failed`, or `indeterminate` |
| `failed` | `passed`, `failed`, or `indeterminate` |
| `cancelled` | `passed`, `failed`, or `indeterminate` |
| `indeterminate` | `passed`, `failed`, or `indeterminate` |

The table contains exactly 13 valid receipt-level combinations. The seven
explicit invalid combinations are `succeeded`, `failed`, `cancelled`, or
`indeterminate` with `not-performed`, and `not-attempted` with `passed`,
`failed`, or `indeterminate`; D6 remains exactly 13/7.

For every attempted `issued-contract` receipt, the additional final-evidence
bindings require `executionOutcome` to equal the outcome of the unique
greatest-sequence member of `E` and `verificationOutcome` to equal the outcome
of the unique greatest-sequence member of `V`. Every non-final E must be
`succeeded`; earlier V outcomes may differ on mixed non-passed histories, but
when `verificationOutcome` is `passed`, C-UNIVERSAL-PASS requires every V
outcome to be `passed`. A final E may independently be `succeeded`, `failed`, `cancelled`, or
`indeterminate`. A `not-attempted/not-performed` receipt requires both E and V
to be empty. These rules do not change the D6 table. C-UNIVERSAL-PASS is
evaluated after final-V binding and before lifecycle precedence,
successful-lifecycle derivation, and receipt-digest acceptance; it adds no D6
pair and rewrites no precedence. Only after D6, EF-1, final-`E` and final-`V`
binding, path-and-operation scope conformance, and the other P/E/V checks
succeed is the existing lifecycle-precedence table below applied; its
precedence is otherwise unchanged.

For an `issued-contract` receipt, Phase 1 static consistency applies the first
matching row in this exact precedence order:

| Precedence | Condition | Required `lifecycleOutcome` |
| ---: | --- | --- |
| 1 | `releaseOutcome: indeterminate` | `indeterminate` |
| 2 | `releaseOutcome: failed` | `failed` |
| 3 | `verificationOutcome: indeterminate` | `indeterminate` |
| 4 | `verificationOutcome: failed` | `failed` |
| 5 | `executionOutcome: indeterminate` | `indeterminate` |
| 6 | `executionOutcome: failed` | `failed` |
| 7 | `executionOutcome: cancelled` | `cancelled` |
| 8 | `executionOutcome: not-attempted` | `denied` |

If none of rows 1 through 8 matches, an issued-contract receipt has
`lifecycleOutcome: succeeded` if and only if `executionOutcome` is
`succeeded`, `verificationOutcome` is `passed`, `releaseOutcome` is
`succeeded` or `not-required`, `unresolvedCoordinationWarnings` is empty, and a
writing contract's every actual ordinary effect path satisfies the
`Apath`/`Qpath` predicate, `Oexec` satisfies both `Acap`/`Qcap` predicates, and
passed, exactly referenced `finalV("scope-contained")` evidence exists. If the
component outcomes have the successful values but unresolved coordination warnings are non-empty,
the required lifecycle outcome is `indeterminate`, never `succeeded`. A scope
violation makes a passed verification claim invalid and independently forbids
a succeeded lifecycle.

Additional issued-contract consistency rules are:

- `executionOutcome: succeeded` MUST NOT combine with
  `verificationOutcome: not-performed`;
- `executionOutcome: not-attempted` requires
  `verificationOutcome: not-performed`;
- `lifecycleOutcome: succeeded` forbids unresolved coordination warnings;
- `verificationOutcome: passed` on a writing contract requires every actual
  ordinary effect path to be in `Apath` and not in `Qpath`, requires
  `Oexec ⊆ Acap` and `Oexec ∩ Qcap = ∅`, and requires
  passed, exactly referenced `finalV("scope-contained")` evidence;
- any path or operation-capability scope violation requires failed or
  indeterminate verification, forbids `lifecycleOutcome: succeeded`, and
  remains retained as audit evidence;
- `releaseOutcome` of `failed` or `indeterminate` requires the unresolved
  warning bound exactly to `finalL.checkId`;
- `releaseOutcome: not-required` is required if and only if the referenced
  contract has `leaseRequired: false`; that path has `L` empty and still has
  its universal passed terminal F;
- every issued receipt has every G type present and every actual G passed, with
  finalG retained only as a diagnostic selector, exactly one passed I, and the
  applicable mutually exclusive passed R or N evidence;
- a referenced contract with `leaseRequired: true` requires the exact passed
  `G < A < R < I` prefix with N empty, at least one `L`, final-`L` outcome
  mapping, and the one passed terminal `F` before receipt finalization; and
- release/contract consistency is a Phase 1 cross-artifact static check against
  the referenced contract and its digest when full conformance is claimed;
  Schema shape alone cannot prove acquisition, release, finalization, or the
  evidence claims true.

For a `pre-contract-denial` receipt:

- `executionOutcome` is `not-attempted`,
  `verificationOutcome` is `not-performed`, and `changedPaths` is empty;
- if `releaseOutcome` is `failed`, `lifecycleOutcome` is `failed`;
- else if `releaseOutcome` is `indeterminate`, `lifecycleOutcome` is
  `indeterminate`;
- otherwise `lifecycleOutcome` is `denied`;
- `lifecycleOutcome` MUST NOT be `succeeded` or `cancelled`;
- `leaseAcquisition.state: acquired` requires at least one `L`, exact final-`L`
  outcome mapping, `preContractEvidence` before every `L`, and one passed
  terminal `F`; failed or indeterminate final release also requires the warning
  bound exactly to `finalL.checkId`;
- `leaseAcquisition.state: indeterminate` requires `L` empty, no stable lease
  identity, `releaseOutcome` and `lifecycleOutcome` both `indeterminate`, and at
  least one unresolved coordination warning, followed by passed terminal F;
- `not-required`, `not-attempted`, and `not-acquired` lease states require `L`
  empty, `releaseOutcome: not-required`, and passed terminal F; and
- a `pre-issuance-revalidation` denial has state `not-required`, a final
  failed or indeterminate N in Dpre, no I/E/V/L or changed path, and passed
  terminal F.

These are deterministic Phase 1 consistency checks over evidence claims. They
do not prove that checks occurred, a summary is safe, or an outcome is true.
Every serialized receipt has exactly one passed terminal F after all non-F
checks. On a release-required path, finalization occurs only after ordered
`L < F` evidence and final-`L` mapping pass, not merely after a top-level
`releaseOutcome` value is present. Future policy may require a pre-contract-
denial receipt, but it remains optional unless that policy does so. Receipt
delivery remains the separate post-finalization
`ReceiptDeliveryResult`. A receipt grants no authority, cannot authorize a
later task, does not imply lease release, and remains host-local evidence
outside portable governance.

### Cross-finding validation-order application

The sole validation dependency DAG in section 10 governs all artifacts. Pure selectors are constructed during preparation. Static acceptance includes source/binding identity, stateful denial, chronology, outcomes, scope and operation evidence. Receipt hashing follows those checks; delivery binding follows only when a result exists. Carrier acceptance preserves conditional presence, EvidencePaths ⊆ changedPaths, OexecByPath/Oexec reconstruction, path containment, capability containment, and C-UNIVERSAL-PASS.

## ExpectedBaseline inventory and cross-dimension consistency

The rules in this section are normative for `TaskContract.expectedBaseline`.
Every `exact` baseline array is the complete inventory for its stated category,
never a delta or exception list. `clean` and `none` are exact semantic states,
not omitted evidence. Phase 1 enforces every relationship fully derivable from
closed contract data. Phase 3 enforces relationships that require the selected
HEAD tree, repository object database, ignore rules, filesystem, submodule
checkout, or live index.

### Index and tracked relationship

`tracked.clean` means that every regular, non-gitlink stage-0 index path
matches the index in the working tree and that no regular tracked path is
modified, deleted, or type-changed.

`tracked.exact` means that `entries` is the complete inventory of every
regular, non-gitlink stage-0 index path, with exactly one entry per path. The
array MUST be non-empty, MUST contain at least one status other than `clean`,
and is not a delta list. Every tracked entry repeats `indexMode` and
`indexObjectId`.

When `index.exact` supplies a matching path, Phase 1 requires
`trackedEntry.indexMode` and `trackedEntry.indexObjectId` to equal that
`indexEntry.mode` and `indexEntry.objectId`. When `index.clean` is used, Phase
3 requires the repeated fields to equal the selected HEAD-tree entry. Every
tracked entry path identifies a regular, non-`160000` index path; no tracked
entry identifies a gitlink; and `tracked.exact` omits no regular index path.

### Exact tracked status rules

The four tracked status branches have these complete distinguishing
invariants:

- `clean` requires `indexMode` and `indexObjectId`, forbids `worktreeMode`
  and `contentDigest`, and Phase 3 confirms that working-tree mode and content
  match the index object.
- `modified` requires `indexMode`, `indexObjectId`, `worktreeMode`, and
  `contentDigest`; requires `worktreeMode == indexMode`; and Phase 3 confirms
  that content differs from the index content.
- `deleted` requires `indexMode` and `indexObjectId`, forbids `worktreeMode`
  and `contentDigest`, and Phase 3 confirms that the working-tree path is
  absent.
- `type-changed` requires `indexMode`, `indexObjectId`, `worktreeMode`, and
  `contentDigest`; requires `worktreeMode != indexMode`; and Phase 3 confirms
  the observed type and content.

For normal tracked worktree paths, `indexMode` and `worktreeMode` may be only
`100644`, `100755`, or `120000`; `160000` is forbidden. Every field that is
inapplicable to the selected status remains forbidden.

### Submodule and index relationship

`submodules.none` means that no stage-0 index path has mode `160000`.
`submodules.exact` is the complete non-empty inventory of every stage-0 index
path with mode `160000`, with each submodule path appearing exactly once.

For every submodule entry, `recordedObjectId` equals the matching stage-0
`indexEntry.objectId`. Phase 1 checks this equality when `index.exact` supplies
the path; Phase 3 checks it against the selected HEAD tree when `index.clean`
is used. A matching tracked entry is forbidden.

### Coverage rules when index.exact is explicit

When the complete `index.exact` inventory is present, Phase 1 MUST enforce all
of the following:

- every non-`160000` index entry is covered by the semantics of
  `tracked.clean` or by exactly one entry in `tracked.exact`;
- `tracked.exact` contains every non-`160000` index path;
- every `160000` index entry appears exactly once in `submodules.exact`;
- `submodules.none` is valid only when no `160000` index entry exists; and
- tracked and submodule path sets are disjoint.

When `index.clean` is used, equivalent coverage checks require the HEAD tree
and live state and therefore belong to Phase 3.

### Untracked and ignored inventories

`untracked.exact` and `ignored.exact` remain complete, non-empty inventories.
Phase 1 requires exact-path disjointness wherever both sides are explicit:

- untracked and ignored path sets are disjoint;
- an untracked path does not equal any explicit index, tracked, or submodule
  path;
- an ignored path does not equal any explicit index, tracked, or submodule
  path; and
- tracked and submodule path sets are disjoint.

When one side depends on `index.clean` and therefore the selected HEAD tree,
the equivalent collision check belongs to Phase 3. These are exact-path rules;
the design does not impose an unsupported general prefix-overlap prohibition.

### Canonical branch selection

Live observation selects each condition canonically:

- `index.clean` if and only if the index equals HEAD; otherwise
  `index.exact`;
- `tracked.clean` if and only if every regular tracked path is clean; otherwise
  `tracked.exact`;
- `submodules.none` if and only if no gitlink exists; otherwise
  `submodules.exact`;
- `untracked.none` if and only if no untracked path exists; otherwise
  `untracked.exact`;
- `ignored.none` if and only if no ignored path exists; otherwise
  `ignored.exact`;
- live `activeOperations.none` if and only if none exists; otherwise the
  reusable observation is `activeOperations.exact`; and
- live `administrativeLocks.none` if and only if none exists; otherwise the
  reusable observation is `administrativeLocks.exact`.

This selection prevents two different observation encodings from describing
the same live state. Only `activeOperations.none` and
`administrativeLocks.none` may be projected into a TaskContract baseline. A
live exact branch for either dimension denies before issuance and may be
retained only in the applicable non-authorizing denial or terminal evidence
context. The reusable observation/evidence unions retain their complete
identity, uniqueness, and canonical-order rules.

### Postcondition reuse

A required-postcondition branch that reuses a baseline condition also reuses
all of this section's inventory and cross-dimension semantics. The
`active-operations` and `administrative-locks` branches are each none-only.
There is no weaker parallel definition for postconditions.

## 8. Supporting and container Schemas

The four non-kind resources do not increase the seven-kind count:

- `common.schema.json` contains shared `$defs` and has no object-kind discriminator.
- `resource.schema.json` is a closed `oneOf` dispatch surface referencing exactly the seven kind Schemas. It is not itself a governance kind.
- `governance-bundle.schema.json` is a closed non-kind container with `apiVersion`, one `project`, canonical `domains`, canonical `worktreeRoles`, and one `routingPolicy`. It contains portable customer governance only. It cannot contain a `HostOverlay`, `TaskContract`, `ExecutionReceipt`, receipt-delivery record, host path, lease, lock, or runtime state.
- `receipt-delivery-result.schema.json` is a closed non-kind record containing required `apiVersion`, `receiptId`, `receiptDigest`, `outcome`, `attemptedAt`, canonical `reasonCodes`, and bounded `sanitizedSummary` fields. It is produced after receipt finalization, cannot alter or replace the receipt, and grants no authority.

GovernanceBundle static validation checks unique IDs, exact reference existence and kinds, one coherent Project association, canonical arrays, routing reference integrity, Domain-overlap declarations, and role ownership declarations. It does not include a concrete HostOverlay and does not execute task resolution or routing. TaskContract and ExecutionReceipt validate independently against their own exact Schemas and selected schema-set revision.

## 9. RoutingPolicy priority semantics

Rule IDs are unique. Duplicate numeric priorities are allowed, rules with
disjoint match conditions may share a priority, and canonical rule order
remains priority descending followed by ID ascending.

### Complete-set matching and Phase 1 static boundary

Let:

- `Dresolved` be the non-empty complete resolved Domain-reference set for one
  task after deterministic Project and Domain resolution;
- `Drule` be one rule's non-empty declared
  `match.domainSet.domainRefs`;
- `Rdecision` be the one WorktreeRole referenced by a route decision; and
- `Owned(R)` be the complete set of Domain references in
  `R.spec.ownedDomainRefs`.

Rule matching is exactly:

```text
operator == exact:
  Drule == Dresolved

operator == contains:
  Drule ⊆ Dresolved
```

Neither operator changes, truncates, replaces, narrows, or authorizes a
partial `Dresolved`. `contains` describes only whether a rule matches the
complete resolved set. It never permits a route target to own only `Drule`.

Phase 1 preserves the closed-bundle static checks: every rule Domain belongs
to the RoutingPolicy Project; every route target belongs to that Project;
every route target statically owns every Domain in `Drule`; every reference
exists with its declared kind; and rule arrays remain closed and canonical.
Phase 1 does not resolve a real task and therefore cannot prove complete
ownership of an unknown future `Dresolved` beyond the rule-declared set.

### Exact Phase 2 evaluation order

Phase 2 performs exactly this order:

1. Resolve exactly one Project.
2. Resolve one non-empty complete Domain-reference set `Dresolved`.
3. Evaluate every rule's `exact` or `contains` match against that same complete
   set.
4. Collect every matching rule.
5. If no rule matches, use the required explicit deny fallback.
6. Find the greatest priority among all matching rules.
7. If more than one rule matches at that greatest priority, deny, even when
   their decisions or route targets are identical or every target owns the
   complete set.
8. Apply the unique highest-priority rule's route-or-deny decision.
9. If the decision is deny, deny.
10. If the decision is route, require:

```text
Dresolved ⊆ Owned(Rdecision)
```

11. If complete ownership fails, deny the routing result.
12. Do not fall through to any lower-priority matching rule.
13. Do not combine multiple WorktreeRoles to form one target.
14. Do not allow worktree availability, HostOverlay binding, free capacity,
    lease availability or possession, branch state, runtime state, cached
    state, or previous receipt evidence to make an incomplete or otherwise
    ineligible role eligible.
15. Only the one eligible selected role may continue to HostOverlay binding.
16. A later trusted TaskContract must bind that exact selected role, exact
    complete `Dresolved`, same Project, and same resolved target.
17. Any mismatch among routing's complete Domain set, selected role,
    TaskContract `domainRefs`, or TaskContract target denies contract issuance
    or validation.

When the unique highest-priority route target does not own every Domain in
`Dresolved`, the original routing result is denied. Phase 2 does not remove
that rule and continue, select a lower-priority complete owner, reinterpret the
denial as policy fallback, or repair policy dynamically. For example, if a
priority-100 `contains {A}` rule routes to a role owning only `{A}`, while a
priority-50 `exact {A,B}` rule routes to a role owning `{A,B}`, a resolved set
`{A,B}` is denied at the priority-100 eligibility gate. The result is not the
priority-50 role.

### Split behavior

A split is not routing fallback within the original task. If no single
selected role may own the complete task, the original task is denied or
returned for split planning. Each split creates a distinct task intent with
its own non-empty complete Domain set and fresh Project resolution, Domain
resolution, RoutingPolicy evaluation, role selection, HostOverlay binding,
authorization, TaskContract, lease handling where applicable, and complete
lifecycle. The original task's contract, lease, and worktree binding cannot
authorize or be shared with a split task. A union of several WorktreeRoles is
never one target for the original task.

### Required routing vectors

Required planned positive vectors cover:

1. `exact` with `Drule == Dresolved` and a route role owning the full set;
2. `contains` with `Drule` a strict subset of `Dresolved` and a route role
   owning the full set;
3. exact and contains matches at different priorities, with one unique
   highest-priority match whose selected role owns the full set;
4. several matches at different priorities, with one unique highest-priority
   rule whose selected role owns the full set;
5. `contains {A}` against `{A,B}` where the selected role owns `{A,B}`; and
6. independently authorized split tasks A and B, each resolving and routing
   its own complete Domain set to one full owner.

Required planned negative vectors cover:

1. `contains {A}` against `{A,B}` where the selected role owns only `{A}`;
2. a higher-priority partial owner and lower-priority complete owner, proving
   denial without fallthrough;
3. several roles that collectively, but no one role that individually, cover
   `Dresolved`;
4. two greatest-priority matches routing to different complete owners;
5. two greatest-priority matches routing to the same role;
6. a complete selected owner with a TaskContract that omits a Domain, adds an
   unrelated Domain, or changes the selected role;
7. an incomplete selected owner despite a HostOverlay binding, free worktree,
   or available lease;
8. a split attempted under the original task, contract, lease, or target;
9. no matching rule with absent, malformed, or non-deny fallback;
10. attempted eligibility widening through availability, branch, host, or
    lease state;
11. exact and contains rules tied at the greatest matching priority; and
12. any TaskContract Domain set different from `Dresolved`.

These are normative planned Phase 2 vectors. They do not create fixtures,
executable tests, task resolution, or routing implementation in this Phase 1
design task.

For each already-valid, canonically ordered rule, define the closed
projections:

```text
RuleProjection = {
  priority: rule.priority,
  match: rule.match,
  decision: rule.decision
}

MatchProjection = rule.match
```

Two rules are exact duplicates when the RFC 8785 JCS bytes of their
`RuleProjection` values are equal. Rule ID is excluded, no digest is computed,
and different IDs do not legalize a duplicate. Two rules have identical
matches when the RFC 8785 JCS bytes of their closed `MatchProjection` values
are equal. At the same priority, identical matches are invalid whether the
decisions agree or differ.

No additional transformation occurs: there is no case folding, path-pattern
rewriting, inferred semantic equivalence, host transformation, or array
reordering. Inputs must pass strict parsing, structural/static validation, and
canonical-array checks before equality is evaluated. For deterministic
diagnostics, exact-duplicate classification takes precedence over
same-priority identical-match classification when both apply.

Positive and negative vectors cover different IDs with otherwise identical
rules; the same priority and match with different decisions; identical matches
at different priorities; independently valid case-different or
pattern-different matches; non-canonical array order rejected before
projection; and sample-equivalent but structurally different patterns that are
not equal.

Phase 1 may reject another contradiction only when it proves it statically and
deterministically without resolving a real task, and it does not execute
routing. Projection equality and other Phase 1 static checks do not alter the
exact Phase 2 matching and evaluation order above. Phase 2 evaluates every
rule against the complete `Dresolved`, denies multiple matches at the greatest
matching priority, and applies only the unique highest-priority decision. A
route is eligible only when its one selected role owns all of `Dresolved`;
failure denies without lower-priority fallthrough or role union. No match uses
the required explicit deny fallback. Global priority uniqueness is not
required, and host, availability, branch, runtime, or lease state cannot widen
eligibility.

## 10. Validation, digest profiles, and exact corpus

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
   comparisons. Validate stable-acquired X/Source presence, required Source
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


The schema-contracts role specifies these closed projections, static invariants, and planned conformance vectors. Future distinct model-implementation owns strict decoding, immutable representations, RFC 8785 implementation, executable tests, and cross-runtime reproduction. Integration-control retains approval, publication, and model-worktree gates. Phase 3/4 operational truth and authority remain unimplemented.

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

### Golden-vector corpus and exact bytes

The following corpus is conspicuously synthetic. Every member name and string
is ASCII and every number is a safe non-negative integer, so UTF-16 property
ordering and RFC 8785 escaping are unambiguous. No omitted field, default,
ellipsis, reference macro, or unexpanded named value participates in a payload.

Each exact separator is shown in hexadecimal:

| Profile | Exact `separator(profile)` hex |
| --- | --- |
| `profile.digest.worktree-content-v1` | `636f6e7465787463746c2e646576007631616c706861312d72310070726f66696c652e6469676573742e776f726b747265652d636f6e74656e742d763100` |
| `profile.digest.policy-selection-v1` | `636f6e7465787463746c2e646576007631616c706861312d72310070726f66696c652e6469676573742e706f6c6963792d73656c656374696f6e2d763100` |
| `profile.digest.configuration-snapshot-v1` | `636f6e7465787463746c2e646576007631616c706861312d72310070726f66696c652e6469676573742e636f6e66696775726174696f6e2d736e617073686f742d763100` |
| `profile.digest.task-intent-bytes-v1` | `636f6e7465787463746c2e646576007631616c706861312d72310070726f66696c652e6469676573742e7461736b2d696e74656e742d62797465732d763100` |
| `profile.digest.issuance-state-v1` | `636f6e7465787463746c2e646576007631616c706861312d72310070726f66696c652e6469676573742e69737375616e63652d73746174652d763100` |
| `profile.digest.contract-derivation-v1` | `636f6e7465787463746c2e646576007631616c706861312d72310070726f66696c652e6469676573742e636f6e74726163742d64657269766174696f6e2d763100` |
| `profile.digest.task-contract-v1` | `636f6e7465787463746c2e646576007631616c706861312d72310070726f66696c652e6469676573742e7461736b2d636f6e74726163742d763100` |
| `profile.digest.pre-contract-evidence-v1` | `636f6e7465787463746c2e646576007631616c706861312d72310070726f66696c652e6469676573742e7072652d636f6e74726163742d65766964656e63652d763100` |
| `profile.digest.lease-acquisition-identity-v1` | `636f6e7465787463746c2e646576007631616c706861312d72310070726f66696c652e6469676573742e6c656173652d6163717569736974696f6e2d6964656e746974792d763100` |
| `profile.digest.execution-receipt-v1` | `636f6e7465787463746c2e646576007631616c706861312d72310070726f66696c652e6469676573742e657865637574696f6e2d726563656970742d763100` |

For every JCS vector below, concatenate the ASCII lines in its code block in
physical order with no delimiter, whitespace, or line ending. The result is
the exact canonical JSON string and its exact UTF-8 payload bytes. The payload
follows the corresponding separator immediately, with no intervening byte.

#### `profile.digest.policy-selection-v1` payload

```json
{"domains":[{"apiVersion":"contextctl.dev/v1alpha1","kind":"Domain","metadata":{"id":"domain.invalid"},"spec":{"overlapRefs":[],"pathScope":{"exclude":[],"include":["README.md"]},"permissions":{"modes":["plan-only"],"permittedCapabilities":["inspect"],"prohibitedCapabilities":[]},"projectRef":{"apiVersion":"contextctl.dev/v1alpha1","id":"project.invalid","kind":"Project"},"responsibility":"Synthetic read-only domain."}}],
"project":{"apiVersion":"contextctl.dev/v1alpha1","kind":"Project","metadata":{"id":"project.invalid"},"spec":{"domainRefs":[{"apiVersion":"contextctl.dev/v1alpha1","id":"domain.invalid","kind":"Domain"}],"permissions":{"modes":["plan-only"],"permittedCapabilities":["inspect"],"prohibitedCapabilities":[]},"repositoryIdentity":{"acceptedRemotes":[{"host":"repo.invalid","namespace":["synthetic"],"repository":"governance","transport":"https"}]},"routingPolicyRef":{"apiVersion":"contextctl.dev/v1alpha1","id":"routing.invalid","kind":"RoutingPolicy"},"secureDefaults":{"allowWrite":false,"mode":"plan-only"},"worktreeRoleRefs":[{"apiVersion":"contextctl.dev/v1alpha1","id":"role.invalid","kind":"WorktreeRole"}]}},
"routingPolicy":{"apiVersion":"contextctl.dev/v1alpha1","kind":"RoutingPolicy","metadata":{"id":"routing.invalid"},"spec":{"fallback":{"reasonCode":"reason.synthetic.denied","type":"deny"},"projectRef":{"apiVersion":"contextctl.dev/v1alpha1","id":"project.invalid","kind":"Project"},"rules":[{"decision":{"type":"route","worktreeRoleRef":{"apiVersion":"contextctl.dev/v1alpha1","id":"role.invalid","kind":"WorktreeRole"}},"id":"rule.invalid","match":{"domainSet":{"domainRefs":[{"apiVersion":"contextctl.dev/v1alpha1","id":"domain.invalid","kind":"Domain"}],"operator":"exact"},"projectRef":{"apiVersion":"contextctl.dev/v1alpha1","id":"project.invalid","kind":"Project"}},"priority":1}]}},
"worktreeRole":{"apiVersion":"contextctl.dev/v1alpha1","kind":"WorktreeRole","metadata":{"id":"role.invalid"},"spec":{"branchPolicy":{"allowed":{"exact":["refs/heads/synthetic"],"prefixes":[]},"denied":{"exact":[],"prefixes":[]}},"cleanlinessPolicy":{"ignored":"none","index":"clean","submodules":"none","tracked":"clean","untracked":"none"},"excludedDomainRefs":[],"exclusiveWriteRequired":false,"ownedDomainRefs":[{"apiVersion":"contextctl.dev/v1alpha1","id":"domain.invalid","kind":"Domain"}],"permissions":{"modes":["plan-only"],"permittedCapabilities":["inspect"],"prohibitedCapabilities":[]},"projectRef":{"apiVersion":"contextctl.dev/v1alpha1","id":"project.invalid","kind":"Project"},"reviewOnly":false,"roleClass":"implementation"}}}
```

#### `profile.digest.configuration-snapshot-v1` payload

```json
{"governanceBundle":{"apiVersion":"contextctl.dev/v1alpha1","domains":[{"apiVersion":"contextctl.dev/v1alpha1","kind":"Domain","metadata":{"id":"domain.invalid"},"spec":{"overlapRefs":[],"pathScope":{"exclude":[],"include":["README.md"]},"permissions":{"modes":["plan-only"],"permittedCapabilities":["inspect"],"prohibitedCapabilities":[]},"projectRef":{"apiVersion":"contextctl.dev/v1alpha1","id":"project.invalid","kind":"Project"},"responsibility":"Synthetic read-only domain."}}],
"project":{"apiVersion":"contextctl.dev/v1alpha1","kind":"Project","metadata":{"id":"project.invalid"},"spec":{"domainRefs":[{"apiVersion":"contextctl.dev/v1alpha1","id":"domain.invalid","kind":"Domain"}],"permissions":{"modes":["plan-only"],"permittedCapabilities":["inspect"],"prohibitedCapabilities":[]},"repositoryIdentity":{"acceptedRemotes":[{"host":"repo.invalid","namespace":["synthetic"],"repository":"governance","transport":"https"}]},"routingPolicyRef":{"apiVersion":"contextctl.dev/v1alpha1","id":"routing.invalid","kind":"RoutingPolicy"},"secureDefaults":{"allowWrite":false,"mode":"plan-only"},"worktreeRoleRefs":[{"apiVersion":"contextctl.dev/v1alpha1","id":"role.invalid","kind":"WorktreeRole"}]}},
"routingPolicy":{"apiVersion":"contextctl.dev/v1alpha1","kind":"RoutingPolicy","metadata":{"id":"routing.invalid"},"spec":{"fallback":{"reasonCode":"reason.synthetic.denied","type":"deny"},"projectRef":{"apiVersion":"contextctl.dev/v1alpha1","id":"project.invalid","kind":"Project"},"rules":[{"decision":{"type":"route","worktreeRoleRef":{"apiVersion":"contextctl.dev/v1alpha1","id":"role.invalid","kind":"WorktreeRole"}},"id":"rule.invalid","match":{"domainSet":{"domainRefs":[{"apiVersion":"contextctl.dev/v1alpha1","id":"domain.invalid","kind":"Domain"}],"operator":"exact"},"projectRef":{"apiVersion":"contextctl.dev/v1alpha1","id":"project.invalid","kind":"Project"}},"priority":1}]}},
"worktreeRoles":[{"apiVersion":"contextctl.dev/v1alpha1","kind":"WorktreeRole","metadata":{"id":"role.invalid"},"spec":{"branchPolicy":{"allowed":{"exact":["refs/heads/synthetic"],"prefixes":[]},"denied":{"exact":[],"prefixes":[]}},"cleanlinessPolicy":{"ignored":"none","index":"clean","submodules":"none","tracked":"clean","untracked":"none"},"excludedDomainRefs":[],"exclusiveWriteRequired":false,"ownedDomainRefs":[{"apiVersion":"contextctl.dev/v1alpha1","id":"domain.invalid","kind":"Domain"}],"permissions":{"modes":["plan-only"],"permittedCapabilities":["inspect"],"prohibitedCapabilities":[]},"projectRef":{"apiVersion":"contextctl.dev/v1alpha1","id":"project.invalid","kind":"Project"},"reviewOnly":false,"roleClass":"implementation"}}]},
"hostOverlay":{"apiVersion":"contextctl.dev/v1alpha1","kind":"HostOverlay","metadata":{"id":"overlay.invalid"},"spec":{"bindings":[{"expectedRef":{"branchRef":"refs/heads/synthetic","state":"branch"},"remoteNames":["origin"],"repositoryRoot":{"platform":"posix","value":"/srv/synthetic.invalid/worktree"},"roleRef":{"apiVersion":"contextctl.dev/v1alpha1","id":"role.invalid","kind":"WorktreeRole"},"worktreeId":"worktree.invalid"}],
"capabilityCeiling":["inspect"],"hostId":"host.invalid","lockRoot":{"platform":"posix","value":"/srv/synthetic.invalid/locks"},"pathCeiling":{"exclude":[],"include":["README.md"]},"projectRef":{"apiVersion":"contextctl.dev/v1alpha1","id":"project.invalid","kind":"Project"},"remoteExpectations":[{"acceptedRemotes":[{"host":"repo.invalid","namespace":["synthetic"],"repository":"governance","transport":"https"}],"remoteName":"origin"}],
"repositoryIdentity":{"acceptedRemotes":[{"host":"repo.invalid","namespace":["synthetic"],"repository":"governance","transport":"https"}]},"stateRoot":{"platform":"posix","value":"/srv/synthetic.invalid/state"}}}}
```

#### Exact raw payloads

The `profile.digest.task-intent-bytes-v1` payload is the following exact
56-byte UTF-8 sequence, with no BOM, final newline, or other byte:

```text
{"requestedMode":"plan-only","task":"inspect README.md"}
```

Its exact payload hex is
`7b227265717565737465644d6f6465223a22706c616e2d6f6e6c79222c227461736b223a22696e737065637420524541444d452e6d64227d`.
The exact `profile.digest.worktree-content-v1` raw vectors are:

| Synthetic value | Mode | Exact payload hex | Tagged digest |
| --- | --- | --- | --- |
| Empty regular file | `100644` | empty byte sequence | `sha256:75a1e5502a349f7d22cbb583985b3045b6d5fd084f9f053cf3379bbbfe3781f9` |
| Binary regular file | `100644` | `00ff100a` | `sha256:d81685f62ae980ae8f1ca44242368c5c790894f055bd18ec1d76cbb5aa212db1` |
| Binary executable file | `100755` | `00ff100a` | `sha256:d81685f62ae980ae8f1ca44242368c5c790894f055bd18ec1d76cbb5aa212db1` |
| Symlink to `../target.bin` | `120000` | `2e2e2f7461726765742e62696e` | `sha256:dfe817225dbc5a625497132435cd03bb8330b34fab83b2263c8d9707d9e71940` |

#### `profile.digest.issuance-state-v1` payload

```json
{"expectedBaseline":{"activeOperations":{"state":"none"},"administrativeLocks":{"state":"none"},"head":{"state":"unborn"},"ignored":{"state":"none"},"index":{"state":"clean"},"ref":{"branchRef":"refs/heads/synthetic","state":"branch"},"submodules":{"state":"none"},"tracked":{"state":"clean"},"untracked":{"state":"none"}},"observedAt":"2000-01-01T00:00:00Z","repositoryIdentity":{"acceptedRemotes":[{"host":"repo.invalid","namespace":["synthetic"],"repository":"governance","transport":"https"}]},"target":{"worktreeId":"worktree.invalid","worktreeRoleRef":{"apiVersion":"contextctl.dev/v1alpha1","id":"role.invalid","kind":"WorktreeRole"}}}
```

#### `profile.digest.contract-derivation-v1` payload

The payload is the complete synthetic TaskContract with only
`spec.issuer.derivationDigest` excluded:

```json
{"apiVersion":"contextctl.dev/v1alpha1","kind":"TaskContract","metadata":{"id":"00000000-0000-4000-8000-000000000002"},"spec":{"allowWrite":false,"authorizedScope":{"capabilities":["inspect"],"paths":["README.md"]},"contractVersion":"1","digests":{"configurationDigest":"sha256:d673b61894f1377ae4e7b7a563db05204ec96cc95bfa9ffb08ccc191e3154f86","policyDigest":"sha256:632908742df166217cf19fc74febda89e2f8ea816d71ec69f65a11a1a4831743","taskIntentDigest":"sha256:f4dda8a653d84b21ae740b502386262ebd525e7086270c5eba7af31eda6929c8"},
"domainRefs":[{"apiVersion":"contextctl.dev/v1alpha1","id":"domain.invalid","kind":"Domain"}],"effectiveMode":"plan-only","expectedBaseline":{"activeOperations":{"state":"none"},"administrativeLocks":{"state":"none"},"head":{"state":"unborn"},"ignored":{"state":"none"},"index":{"state":"clean"},"ref":{"branchRef":"refs/heads/synthetic","state":"branch"},"submodules":{"state":"none"},"tracked":{"state":"clean"},"untracked":{"state":"none"}},
"freshness":{"expiresAt":"2000-01-01T00:01:00Z","issuedAt":"2000-01-01T00:00:00Z"},"issuanceCheckpoint":{"observedAt":"2000-01-01T00:00:00Z","stateDigest":"sha256:4b9cf13b1accd0e3c29754feedb601c5a7b43619842ad76cbf118a56ae4a2702"},"issuer":{"issuanceMethod":"trusted-framework","issuerId":"issuer.invalid"},"leaseRequired":false,"permittedTransitions":[],"prohibitedScope":{"capabilities":[],"paths":[]},
"projectRef":{"apiVersion":"contextctl.dev/v1alpha1","id":"project.invalid","kind":"Project"},"repositoryIdentity":{"acceptedRemotes":[{"host":"repo.invalid","namespace":["synthetic"],"repository":"governance","transport":"https"}]},"requestedMode":"plan-only","requiredPostconditions":[{"type":"scope-contained"}],"target":{"worktreeId":"worktree.invalid","worktreeRoleRef":{"apiVersion":"contextctl.dev/v1alpha1","id":"role.invalid","kind":"WorktreeRole"}},"taskId":"00000000-0000-4000-8000-000000000001"}}
```

#### `profile.digest.task-contract-v1` payload

This is the complete contract after insertion of its derivation digest:

```json
{"apiVersion":"contextctl.dev/v1alpha1","kind":"TaskContract","metadata":{"id":"00000000-0000-4000-8000-000000000002"},"spec":{"allowWrite":false,"authorizedScope":{"capabilities":["inspect"],"paths":["README.md"]},"contractVersion":"1","digests":{"configurationDigest":"sha256:d673b61894f1377ae4e7b7a563db05204ec96cc95bfa9ffb08ccc191e3154f86","policyDigest":"sha256:632908742df166217cf19fc74febda89e2f8ea816d71ec69f65a11a1a4831743","taskIntentDigest":"sha256:f4dda8a653d84b21ae740b502386262ebd525e7086270c5eba7af31eda6929c8"},
"domainRefs":[{"apiVersion":"contextctl.dev/v1alpha1","id":"domain.invalid","kind":"Domain"}],"effectiveMode":"plan-only","expectedBaseline":{"activeOperations":{"state":"none"},"administrativeLocks":{"state":"none"},"head":{"state":"unborn"},"ignored":{"state":"none"},"index":{"state":"clean"},"ref":{"branchRef":"refs/heads/synthetic","state":"branch"},"submodules":{"state":"none"},"tracked":{"state":"clean"},"untracked":{"state":"none"}},
"freshness":{"expiresAt":"2000-01-01T00:01:00Z","issuedAt":"2000-01-01T00:00:00Z"},"issuanceCheckpoint":{"observedAt":"2000-01-01T00:00:00Z","stateDigest":"sha256:4b9cf13b1accd0e3c29754feedb601c5a7b43619842ad76cbf118a56ae4a2702"},"issuer":{"derivationDigest":"sha256:9ced52eaa97d549c51caea566cc4681016f18614b68d1db0bc7a2748113f9a25","issuanceMethod":"trusted-framework","issuerId":"issuer.invalid"},"leaseRequired":false,"permittedTransitions":[],"prohibitedScope":{"capabilities":[],"paths":[]},
"projectRef":{"apiVersion":"contextctl.dev/v1alpha1","id":"project.invalid","kind":"Project"},"repositoryIdentity":{"acceptedRemotes":[{"host":"repo.invalid","namespace":["synthetic"],"repository":"governance","transport":"https"}]},"requestedMode":"plan-only","requiredPostconditions":[{"type":"scope-contained"}],"target":{"worktreeId":"worktree.invalid","worktreeRoleRef":{"apiVersion":"contextctl.dev/v1alpha1","id":"role.invalid","kind":"WorktreeRole"}},"taskId":"00000000-0000-4000-8000-000000000001"}}
```

#### Unified acquisition Source and exact binding

The following independent Source projection is exactly 157 bytes. The completed Source is exactly 234 bytes; the receipt binding is exactly 186 bytes. Each acquired golden is validated with exactly one associated copy of this external Source; it is never embedded in the receipt.

```json
{"acquisitionBinding":{"checkId":"check.lease-acquisition","leaseId":"00000000-0000-4000-8000-000000000004"},"taskId":"00000000-0000-4000-8000-000000000001"}
```

```json
{"acquisitionResultDigest":"sha256:6aec9485391fbba3fd7a35640e21dd45dc2da0228e87db83fe935ba99a100e7f","checkId":"check.lease-acquisition","leaseId":"00000000-0000-4000-8000-000000000004","taskId":"00000000-0000-4000-8000-000000000001"}
```

```json
{"acquisitionResultDigest":"sha256:6aec9485391fbba3fd7a35640e21dd45dc2da0228e87db83fe935ba99a100e7f","checkId":"check.lease-acquisition","leaseId":"00000000-0000-4000-8000-000000000004"}
```

#### Complete acquired-denial and state-creation corpus

All ten records below are conspicuously synthetic. acquired-R includes an earlier passed R and a failed L followed by a passed finalL. acquired-I includes a passed A/R prerequisite, a failed singleton I, an indeterminate finalL and its exactly linked unresolved warning. Both carry the same explicitly supplied Source above. The four single-state controls and four erased-success negatives have no Source and no acquisitionBinding. The I controls use the complete no-lease G/N prefix. No named macro replaces any serialized field.

##### acquired-R — ACCEPT

The exact evidence projection (507 bytes) is:

```json
{"acquisitionBinding":{"acquisitionResultDigest":"sha256:6aec9485391fbba3fd7a35640e21dd45dc2da0228e87db83fe935ba99a100e7f","checkId":"check.lease-acquisition","leaseId":"00000000-0000-4000-8000-000000000004"},"denialCheckpoint":"post-acquisition-revalidation","preContractEvidence":{"controllerCheckId":"check.post-acquisition-revalidation","observedAt":"2000-01-01T00:00:03Z","reasonCodes":["reason.synthetic.denied"],"sanitizedSummary":"Synthetic denial."},"taskId":"00000000-0000-4000-8000-000000000001"}
```

The exact receipt projection (3743 bytes) is:

```json
{"apiVersion":"contextctl.dev/v1alpha1","kind":"ExecutionReceipt","metadata":{"id":"00000000-0000-4000-8000-000000000010"},"spec":{"acquisitionBinding":{"acquisitionResultDigest":"sha256:6aec9485391fbba3fd7a35640e21dd45dc2da0228e87db83fe935ba99a100e7f","checkId":"check.lease-acquisition","leaseId":"00000000-0000-4000-8000-000000000004"},"changedPaths":[],"checks":[{"checkId":"check.intent-validation","checkType":"intent-validation","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":0},{"checkId":"check.project-domain-resolution","checkType":"project-domain-resolution","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":1},{"checkId":"check.role-routing","checkType":"role-routing","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":2},{"checkId":"check.host-binding","checkType":"host-binding","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":3},{"checkId":"check.initial-preflight","checkType":"initial-preflight","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":4},{"checkId":"check.lease-acquisition","checkType":"lease-acquisition","leaseAcquisitionRef":{"checkId":"check.lease-acquisition"},"observedAt":"2000-01-01T00:00:01Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":5},{"checkId":"check.revalidation-earlier","checkType":"post-acquisition-revalidation","leaseAcquisitionRef":{"checkId":"check.lease-acquisition"},"observedAt":"2000-01-01T00:00:02Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":6},{"checkId":"check.post-acquisition-revalidation","checkType":"post-acquisition-revalidation","leaseAcquisitionRef":{"checkId":"check.lease-acquisition"},"observedAt":"2000-01-01T00:00:03Z","outcome":"failed","profileId":"profile.validation.v1","reasonCodes":["reason.synthetic.denied"],"sequence":7},{"checkId":"check.release-earlier","checkType":"lease-release","leaseAcquisitionRef":{"checkId":"check.lease-acquisition"},"observedAt":"2000-01-01T00:00:04Z","outcome":"failed","profileId":"profile.validation.v1","reasonCodes":["reason.synthetic.denied"],"sequence":8},{"checkId":"check.lease-release","checkType":"lease-release","leaseAcquisitionRef":{"checkId":"check.lease-acquisition"},"observedAt":"2000-01-01T00:00:05Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":9},{"checkId":"check.receipt-finalization","checkType":"receipt-finalization","observedAt":"2000-01-01T00:00:06Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":10}],"executionOutcome":"not-attempted","finishedAt":"2000-01-01T00:00:06Z","lifecycleOutcome":"denied","origin":{"denialCheckpoint":"post-acquisition-revalidation","leaseAcquisition":{"state":"acquired"},"preContractEvidence":{"controllerCheckId":"check.post-acquisition-revalidation","evidenceDigest":"sha256:3f2a27da5bfdf587209700191c430aa1900cdbe4e428f82abb7d289efbee0429","observedAt":"2000-01-01T00:00:03Z","reasonCodes":["reason.synthetic.denied"],"sanitizedSummary":"Synthetic denial."},"type":"pre-contract-denial"},"reasonCodes":["reason.synthetic.denied"],"receiptVersion":"1","releaseOutcome":"succeeded","sanitization":{"applied":true,"completedAt":"2000-01-01T00:00:06Z","profileId":"profile.sanitization.v1","redactionCount":0},"startedAt":"2000-01-01T00:00:00Z","taskId":"00000000-0000-4000-8000-000000000001","unresolvedCoordinationWarnings":[],"verificationOutcome":"not-performed"}}
```

Complete receipt (3833 bytes):

```json
{"apiVersion":"contextctl.dev/v1alpha1","kind":"ExecutionReceipt","metadata":{"id":"00000000-0000-4000-8000-000000000010"},"spec":{"acquisitionBinding":{"acquisitionResultDigest":"sha256:6aec9485391fbba3fd7a35640e21dd45dc2da0228e87db83fe935ba99a100e7f","checkId":"check.lease-acquisition","leaseId":"00000000-0000-4000-8000-000000000004"},"changedPaths":[],"checks":[{"checkId":"check.intent-validation","checkType":"intent-validation","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":0},{"checkId":"check.project-domain-resolution","checkType":"project-domain-resolution","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":1},{"checkId":"check.role-routing","checkType":"role-routing","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":2},{"checkId":"check.host-binding","checkType":"host-binding","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":3},{"checkId":"check.initial-preflight","checkType":"initial-preflight","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":4},{"checkId":"check.lease-acquisition","checkType":"lease-acquisition","leaseAcquisitionRef":{"checkId":"check.lease-acquisition"},"observedAt":"2000-01-01T00:00:01Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":5},{"checkId":"check.revalidation-earlier","checkType":"post-acquisition-revalidation","leaseAcquisitionRef":{"checkId":"check.lease-acquisition"},"observedAt":"2000-01-01T00:00:02Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":6},{"checkId":"check.post-acquisition-revalidation","checkType":"post-acquisition-revalidation","leaseAcquisitionRef":{"checkId":"check.lease-acquisition"},"observedAt":"2000-01-01T00:00:03Z","outcome":"failed","profileId":"profile.validation.v1","reasonCodes":["reason.synthetic.denied"],"sequence":7},{"checkId":"check.release-earlier","checkType":"lease-release","leaseAcquisitionRef":{"checkId":"check.lease-acquisition"},"observedAt":"2000-01-01T00:00:04Z","outcome":"failed","profileId":"profile.validation.v1","reasonCodes":["reason.synthetic.denied"],"sequence":8},{"checkId":"check.lease-release","checkType":"lease-release","leaseAcquisitionRef":{"checkId":"check.lease-acquisition"},"observedAt":"2000-01-01T00:00:05Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":9},{"checkId":"check.receipt-finalization","checkType":"receipt-finalization","observedAt":"2000-01-01T00:00:06Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":10}],"executionOutcome":"not-attempted","finishedAt":"2000-01-01T00:00:06Z","lifecycleOutcome":"denied","origin":{"denialCheckpoint":"post-acquisition-revalidation","leaseAcquisition":{"state":"acquired"},"preContractEvidence":{"controllerCheckId":"check.post-acquisition-revalidation","evidenceDigest":"sha256:3f2a27da5bfdf587209700191c430aa1900cdbe4e428f82abb7d289efbee0429","observedAt":"2000-01-01T00:00:03Z","reasonCodes":["reason.synthetic.denied"],"sanitizedSummary":"Synthetic denial."},"type":"pre-contract-denial"},"reasonCodes":["reason.synthetic.denied"],"receiptDigest":"sha256:d8c44f4ae79b8402ffb0aa36cd8e9fff2d610df09e0c6f0a7a88c9ca4bfaec8f","receiptVersion":"1","releaseOutcome":"succeeded","sanitization":{"applied":true,"completedAt":"2000-01-01T00:00:06Z","profileId":"profile.sanitization.v1","redactionCount":0},"startedAt":"2000-01-01T00:00:00Z","taskId":"00000000-0000-4000-8000-000000000001","unresolvedCoordinationWarnings":[],"verificationOutcome":"not-performed"}}
```

##### acquired-I — ACCEPT

The exact evidence projection (483 bytes) is:

```json
{"acquisitionBinding":{"acquisitionResultDigest":"sha256:6aec9485391fbba3fd7a35640e21dd45dc2da0228e87db83fe935ba99a100e7f","checkId":"check.lease-acquisition","leaseId":"00000000-0000-4000-8000-000000000004"},"denialCheckpoint":"contract-issuance","preContractEvidence":{"controllerCheckId":"check.contract-issuance","observedAt":"2000-01-01T00:00:03Z","reasonCodes":["reason.synthetic.denied"],"sanitizedSummary":"Synthetic denial."},"taskId":"00000000-0000-4000-8000-000000000001"}
```

The exact receipt projection (3542 bytes) is:

```json
{"apiVersion":"contextctl.dev/v1alpha1","kind":"ExecutionReceipt","metadata":{"id":"00000000-0000-4000-8000-000000000011"},"spec":{"acquisitionBinding":{"acquisitionResultDigest":"sha256:6aec9485391fbba3fd7a35640e21dd45dc2da0228e87db83fe935ba99a100e7f","checkId":"check.lease-acquisition","leaseId":"00000000-0000-4000-8000-000000000004"},"changedPaths":[],"checks":[{"checkId":"check.intent-validation","checkType":"intent-validation","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":0},{"checkId":"check.project-domain-resolution","checkType":"project-domain-resolution","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":1},{"checkId":"check.role-routing","checkType":"role-routing","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":2},{"checkId":"check.host-binding","checkType":"host-binding","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":3},{"checkId":"check.initial-preflight","checkType":"initial-preflight","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":4},{"checkId":"check.lease-acquisition","checkType":"lease-acquisition","leaseAcquisitionRef":{"checkId":"check.lease-acquisition"},"observedAt":"2000-01-01T00:00:01Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":5},{"checkId":"check.post-acquisition-revalidation","checkType":"post-acquisition-revalidation","leaseAcquisitionRef":{"checkId":"check.lease-acquisition"},"observedAt":"2000-01-01T00:00:02Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":6},{"checkId":"check.contract-issuance","checkType":"contract-issuance","observedAt":"2000-01-01T00:00:03Z","outcome":"failed","profileId":"profile.validation.v1","reasonCodes":["reason.synthetic.denied"],"sequence":7},{"checkId":"check.lease-release","checkType":"lease-release","leaseAcquisitionRef":{"checkId":"check.lease-acquisition"},"observedAt":"2000-01-01T00:00:05Z","outcome":"indeterminate","profileId":"profile.validation.v1","reasonCodes":["reason.synthetic.denied"],"sequence":8},{"checkId":"check.receipt-finalization","checkType":"receipt-finalization","observedAt":"2000-01-01T00:00:06Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":9}],"executionOutcome":"not-attempted","finishedAt":"2000-01-01T00:00:06Z","lifecycleOutcome":"indeterminate","origin":{"denialCheckpoint":"contract-issuance","leaseAcquisition":{"state":"acquired"},"preContractEvidence":{"controllerCheckId":"check.contract-issuance","evidenceDigest":"sha256:93c0c3a28a9dbfdc05b29183fde51f653ad3c7cab65eb4c7b571dd3dc94bac4a","observedAt":"2000-01-01T00:00:03Z","reasonCodes":["reason.synthetic.denied"],"sanitizedSummary":"Synthetic denial."},"type":"pre-contract-denial"},"reasonCodes":["reason.synthetic.denied"],"receiptVersion":"1","releaseOutcome":"indeterminate","sanitization":{"applied":true,"completedAt":"2000-01-01T00:00:06Z","profileId":"profile.sanitization.v1","redactionCount":0},"startedAt":"2000-01-01T00:00:00Z","taskId":"00000000-0000-4000-8000-000000000001","unresolvedCoordinationWarnings":[{"code":"reason.synthetic.unresolved","profileId":"profile.validation.v1","relatedCheckId":"check.lease-release","sequence":0}],"verificationOutcome":"not-performed"}}
```

Complete receipt (3632 bytes):

```json
{"apiVersion":"contextctl.dev/v1alpha1","kind":"ExecutionReceipt","metadata":{"id":"00000000-0000-4000-8000-000000000011"},"spec":{"acquisitionBinding":{"acquisitionResultDigest":"sha256:6aec9485391fbba3fd7a35640e21dd45dc2da0228e87db83fe935ba99a100e7f","checkId":"check.lease-acquisition","leaseId":"00000000-0000-4000-8000-000000000004"},"changedPaths":[],"checks":[{"checkId":"check.intent-validation","checkType":"intent-validation","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":0},{"checkId":"check.project-domain-resolution","checkType":"project-domain-resolution","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":1},{"checkId":"check.role-routing","checkType":"role-routing","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":2},{"checkId":"check.host-binding","checkType":"host-binding","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":3},{"checkId":"check.initial-preflight","checkType":"initial-preflight","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":4},{"checkId":"check.lease-acquisition","checkType":"lease-acquisition","leaseAcquisitionRef":{"checkId":"check.lease-acquisition"},"observedAt":"2000-01-01T00:00:01Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":5},{"checkId":"check.post-acquisition-revalidation","checkType":"post-acquisition-revalidation","leaseAcquisitionRef":{"checkId":"check.lease-acquisition"},"observedAt":"2000-01-01T00:00:02Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":6},{"checkId":"check.contract-issuance","checkType":"contract-issuance","observedAt":"2000-01-01T00:00:03Z","outcome":"failed","profileId":"profile.validation.v1","reasonCodes":["reason.synthetic.denied"],"sequence":7},{"checkId":"check.lease-release","checkType":"lease-release","leaseAcquisitionRef":{"checkId":"check.lease-acquisition"},"observedAt":"2000-01-01T00:00:05Z","outcome":"indeterminate","profileId":"profile.validation.v1","reasonCodes":["reason.synthetic.denied"],"sequence":8},{"checkId":"check.receipt-finalization","checkType":"receipt-finalization","observedAt":"2000-01-01T00:00:06Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":9}],"executionOutcome":"not-attempted","finishedAt":"2000-01-01T00:00:06Z","lifecycleOutcome":"indeterminate","origin":{"denialCheckpoint":"contract-issuance","leaseAcquisition":{"state":"acquired"},"preContractEvidence":{"controllerCheckId":"check.contract-issuance","evidenceDigest":"sha256:93c0c3a28a9dbfdc05b29183fde51f653ad3c7cab65eb4c7b571dd3dc94bac4a","observedAt":"2000-01-01T00:00:03Z","reasonCodes":["reason.synthetic.denied"],"sanitizedSummary":"Synthetic denial."},"type":"pre-contract-denial"},"reasonCodes":["reason.synthetic.denied"],"receiptDigest":"sha256:d151aa6ce1c13f4e42ce3b47a058df488bcb072491506de936d3ad7873f74cff","receiptVersion":"1","releaseOutcome":"indeterminate","sanitization":{"applied":true,"completedAt":"2000-01-01T00:00:06Z","profileId":"profile.sanitization.v1","redactionCount":0},"startedAt":"2000-01-01T00:00:00Z","taskId":"00000000-0000-4000-8000-000000000001","unresolvedCoordinationWarnings":[{"code":"reason.synthetic.unresolved","profileId":"profile.validation.v1","relatedCheckId":"check.lease-release","sequence":0}],"verificationOutcome":"not-performed"}}
```

##### single-failed-A — ACCEPT

Complete receipt (2493 bytes):

```json
{"apiVersion":"contextctl.dev/v1alpha1","kind":"ExecutionReceipt","metadata":{"id":"00000000-0000-4000-8000-000000000012"},"spec":{"changedPaths":[],"checks":[{"checkId":"check.intent-validation","checkType":"intent-validation","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":0},{"checkId":"check.project-domain-resolution","checkType":"project-domain-resolution","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":1},{"checkId":"check.role-routing","checkType":"role-routing","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":2},{"checkId":"check.host-binding","checkType":"host-binding","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":3},{"checkId":"check.initial-preflight","checkType":"initial-preflight","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":4},{"checkId":"check.lease-acquisition","checkType":"lease-acquisition","observedAt":"2000-01-01T00:00:03Z","outcome":"failed","profileId":"profile.validation.v1","reasonCodes":["reason.synthetic.denied"],"sequence":5},{"checkId":"check.receipt-finalization","checkType":"receipt-finalization","observedAt":"2000-01-01T00:00:06Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":6}],"executionOutcome":"not-attempted","finishedAt":"2000-01-01T00:00:06Z","lifecycleOutcome":"denied","origin":{"denialCheckpoint":"lease-acquisition","leaseAcquisition":{"state":"not-acquired"},"preContractEvidence":{"controllerCheckId":"check.lease-acquisition","evidenceDigest":"sha256:a6e3d300a1dd1ef61aa7a203441f971c6229dd306157ac8aafc20268ac7ad42c","observedAt":"2000-01-01T00:00:03Z","reasonCodes":["reason.synthetic.denied"],"sanitizedSummary":"Synthetic denial."},"type":"pre-contract-denial"},"reasonCodes":["reason.synthetic.denied"],"receiptDigest":"sha256:04e565109819e271ddafc60bf50aa7a035c0a70cee005af67a6f84dacaf6c69e","receiptVersion":"1","releaseOutcome":"not-required","sanitization":{"applied":true,"completedAt":"2000-01-01T00:00:06Z","profileId":"profile.sanitization.v1","redactionCount":0},"startedAt":"2000-01-01T00:00:00Z","taskId":"00000000-0000-4000-8000-000000000001","unresolvedCoordinationWarnings":[],"verificationOutcome":"not-performed"}}
```

##### single-indeterminate-A — ACCEPT

Complete receipt (2639 bytes):

```json
{"apiVersion":"contextctl.dev/v1alpha1","kind":"ExecutionReceipt","metadata":{"id":"00000000-0000-4000-8000-000000000013"},"spec":{"changedPaths":[],"checks":[{"checkId":"check.intent-validation","checkType":"intent-validation","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":0},{"checkId":"check.project-domain-resolution","checkType":"project-domain-resolution","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":1},{"checkId":"check.role-routing","checkType":"role-routing","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":2},{"checkId":"check.host-binding","checkType":"host-binding","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":3},{"checkId":"check.initial-preflight","checkType":"initial-preflight","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":4},{"checkId":"check.lease-acquisition","checkType":"lease-acquisition","observedAt":"2000-01-01T00:00:03Z","outcome":"indeterminate","profileId":"profile.validation.v1","reasonCodes":["reason.synthetic.denied"],"sequence":5},{"checkId":"check.receipt-finalization","checkType":"receipt-finalization","observedAt":"2000-01-01T00:00:06Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":6}],"executionOutcome":"not-attempted","finishedAt":"2000-01-01T00:00:06Z","lifecycleOutcome":"indeterminate","origin":{"denialCheckpoint":"lease-acquisition","leaseAcquisition":{"state":"indeterminate"},"preContractEvidence":{"controllerCheckId":"check.lease-acquisition","evidenceDigest":"sha256:a6e3d300a1dd1ef61aa7a203441f971c6229dd306157ac8aafc20268ac7ad42c","observedAt":"2000-01-01T00:00:03Z","reasonCodes":["reason.synthetic.denied"],"sanitizedSummary":"Synthetic denial."},"type":"pre-contract-denial"},"reasonCodes":["reason.synthetic.denied"],"receiptDigest":"sha256:55e493aa0c23428037602c86fbc4b8dab52a7e2cf28fd5b0ff6d69d4cb5f1706","receiptVersion":"1","releaseOutcome":"indeterminate","sanitization":{"applied":true,"completedAt":"2000-01-01T00:00:06Z","profileId":"profile.sanitization.v1","redactionCount":0},"startedAt":"2000-01-01T00:00:00Z","taskId":"00000000-0000-4000-8000-000000000001","unresolvedCoordinationWarnings":[{"code":"reason.synthetic.unresolved","profileId":"profile.validation.v1","relatedCheckId":"check.lease-acquisition","sequence":0}],"verificationOutcome":"not-performed"}}
```

##### single-failed-I — ACCEPT

Complete receipt (2700 bytes):

```json
{"apiVersion":"contextctl.dev/v1alpha1","kind":"ExecutionReceipt","metadata":{"id":"00000000-0000-4000-8000-000000000014"},"spec":{"changedPaths":[],"checks":[{"checkId":"check.intent-validation","checkType":"intent-validation","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":0},{"checkId":"check.project-domain-resolution","checkType":"project-domain-resolution","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":1},{"checkId":"check.role-routing","checkType":"role-routing","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":2},{"checkId":"check.host-binding","checkType":"host-binding","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":3},{"checkId":"check.initial-preflight","checkType":"initial-preflight","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":4},{"checkId":"check.pre-issuance-revalidation","checkType":"pre-issuance-revalidation","observedAt":"2000-01-01T00:00:01Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":5},{"checkId":"check.contract-issuance","checkType":"contract-issuance","observedAt":"2000-01-01T00:00:03Z","outcome":"failed","profileId":"profile.validation.v1","reasonCodes":["reason.synthetic.denied"],"sequence":6},{"checkId":"check.receipt-finalization","checkType":"receipt-finalization","observedAt":"2000-01-01T00:00:06Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":7}],"executionOutcome":"not-attempted","finishedAt":"2000-01-01T00:00:06Z","lifecycleOutcome":"denied","origin":{"denialCheckpoint":"contract-issuance","leaseAcquisition":{"state":"not-required"},"preContractEvidence":{"controllerCheckId":"check.contract-issuance","evidenceDigest":"sha256:e53415c5bad5345082073b225dba4ddb01a895968f03815e9a5fcd0b80ebc839","observedAt":"2000-01-01T00:00:03Z","reasonCodes":["reason.synthetic.denied"],"sanitizedSummary":"Synthetic denial."},"type":"pre-contract-denial"},"reasonCodes":["reason.synthetic.denied"],"receiptDigest":"sha256:b887eb26f92bd9bacbe60be84295cac4b16abac138b94dae9490c835329da9aa","receiptVersion":"1","releaseOutcome":"not-required","sanitization":{"applied":true,"completedAt":"2000-01-01T00:00:06Z","profileId":"profile.sanitization.v1","redactionCount":0},"startedAt":"2000-01-01T00:00:00Z","taskId":"00000000-0000-4000-8000-000000000001","unresolvedCoordinationWarnings":[],"verificationOutcome":"not-performed"}}
```

##### single-indeterminate-I — ACCEPT

Complete receipt (2707 bytes):

```json
{"apiVersion":"contextctl.dev/v1alpha1","kind":"ExecutionReceipt","metadata":{"id":"00000000-0000-4000-8000-000000000015"},"spec":{"changedPaths":[],"checks":[{"checkId":"check.intent-validation","checkType":"intent-validation","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":0},{"checkId":"check.project-domain-resolution","checkType":"project-domain-resolution","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":1},{"checkId":"check.role-routing","checkType":"role-routing","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":2},{"checkId":"check.host-binding","checkType":"host-binding","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":3},{"checkId":"check.initial-preflight","checkType":"initial-preflight","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":4},{"checkId":"check.pre-issuance-revalidation","checkType":"pre-issuance-revalidation","observedAt":"2000-01-01T00:00:01Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":5},{"checkId":"check.contract-issuance","checkType":"contract-issuance","observedAt":"2000-01-01T00:00:03Z","outcome":"indeterminate","profileId":"profile.validation.v1","reasonCodes":["reason.synthetic.denied"],"sequence":6},{"checkId":"check.receipt-finalization","checkType":"receipt-finalization","observedAt":"2000-01-01T00:00:06Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":7}],"executionOutcome":"not-attempted","finishedAt":"2000-01-01T00:00:06Z","lifecycleOutcome":"denied","origin":{"denialCheckpoint":"contract-issuance","leaseAcquisition":{"state":"not-required"},"preContractEvidence":{"controllerCheckId":"check.contract-issuance","evidenceDigest":"sha256:e53415c5bad5345082073b225dba4ddb01a895968f03815e9a5fcd0b80ebc839","observedAt":"2000-01-01T00:00:03Z","reasonCodes":["reason.synthetic.denied"],"sanitizedSummary":"Synthetic denial."},"type":"pre-contract-denial"},"reasonCodes":["reason.synthetic.denied"],"receiptDigest":"sha256:6133e6152bf48b945916ec67d348ccc8baa3435846e1c2968b11d0e83e9e5d47","receiptVersion":"1","releaseOutcome":"not-required","sanitization":{"applied":true,"completedAt":"2000-01-01T00:00:06Z","profileId":"profile.sanitization.v1","redactionCount":0},"startedAt":"2000-01-01T00:00:00Z","taskId":"00000000-0000-4000-8000-000000000001","unresolvedCoordinationWarnings":[],"verificationOutcome":"not-performed"}}
```

##### passed-A-then-failed-A — REJECT DP-N10

Complete receipt (2681 bytes):

```json
{"apiVersion":"contextctl.dev/v1alpha1","kind":"ExecutionReceipt","metadata":{"id":"00000000-0000-4000-8000-000000000016"},"spec":{"changedPaths":[],"checks":[{"checkId":"check.intent-validation","checkType":"intent-validation","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":0},{"checkId":"check.project-domain-resolution","checkType":"project-domain-resolution","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":1},{"checkId":"check.role-routing","checkType":"role-routing","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":2},{"checkId":"check.host-binding","checkType":"host-binding","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":3},{"checkId":"check.initial-preflight","checkType":"initial-preflight","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":4},{"checkId":"check.erased-success","checkType":"lease-acquisition","observedAt":"2000-01-01T00:00:02Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":5},{"checkId":"check.lease-acquisition","checkType":"lease-acquisition","observedAt":"2000-01-01T00:00:03Z","outcome":"failed","profileId":"profile.validation.v1","reasonCodes":["reason.synthetic.denied"],"sequence":6},{"checkId":"check.receipt-finalization","checkType":"receipt-finalization","observedAt":"2000-01-01T00:00:06Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":7}],"executionOutcome":"not-attempted","finishedAt":"2000-01-01T00:00:06Z","lifecycleOutcome":"denied","origin":{"denialCheckpoint":"lease-acquisition","leaseAcquisition":{"state":"not-acquired"},"preContractEvidence":{"controllerCheckId":"check.lease-acquisition","evidenceDigest":"sha256:a6e3d300a1dd1ef61aa7a203441f971c6229dd306157ac8aafc20268ac7ad42c","observedAt":"2000-01-01T00:00:03Z","reasonCodes":["reason.synthetic.denied"],"sanitizedSummary":"Synthetic denial."},"type":"pre-contract-denial"},"reasonCodes":["reason.synthetic.denied"],"receiptDigest":"sha256:d3d5e1727b67bb896f6863f299e9734875c1340a1e514f5b5274ee25cf3bbbff","receiptVersion":"1","releaseOutcome":"not-required","sanitization":{"applied":true,"completedAt":"2000-01-01T00:00:06Z","profileId":"profile.sanitization.v1","redactionCount":0},"startedAt":"2000-01-01T00:00:00Z","taskId":"00000000-0000-4000-8000-000000000001","unresolvedCoordinationWarnings":[],"verificationOutcome":"not-performed"}}
```

Its mathematically recomputed digest is a test oracle over invalid input, never acceptance. The earlier passed A is the sole state-history attack; exact shape, contiguous sequence, unique IDs, controller linkage, outcomes, warnings, and independent chronology remain valid. No retry epoch exists.

##### passed-A-then-indeterminate-A — REJECT DP-N10

Complete receipt (2827 bytes):

```json
{"apiVersion":"contextctl.dev/v1alpha1","kind":"ExecutionReceipt","metadata":{"id":"00000000-0000-4000-8000-000000000017"},"spec":{"changedPaths":[],"checks":[{"checkId":"check.intent-validation","checkType":"intent-validation","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":0},{"checkId":"check.project-domain-resolution","checkType":"project-domain-resolution","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":1},{"checkId":"check.role-routing","checkType":"role-routing","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":2},{"checkId":"check.host-binding","checkType":"host-binding","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":3},{"checkId":"check.initial-preflight","checkType":"initial-preflight","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":4},{"checkId":"check.erased-success","checkType":"lease-acquisition","observedAt":"2000-01-01T00:00:02Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":5},{"checkId":"check.lease-acquisition","checkType":"lease-acquisition","observedAt":"2000-01-01T00:00:03Z","outcome":"indeterminate","profileId":"profile.validation.v1","reasonCodes":["reason.synthetic.denied"],"sequence":6},{"checkId":"check.receipt-finalization","checkType":"receipt-finalization","observedAt":"2000-01-01T00:00:06Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":7}],"executionOutcome":"not-attempted","finishedAt":"2000-01-01T00:00:06Z","lifecycleOutcome":"indeterminate","origin":{"denialCheckpoint":"lease-acquisition","leaseAcquisition":{"state":"indeterminate"},"preContractEvidence":{"controllerCheckId":"check.lease-acquisition","evidenceDigest":"sha256:a6e3d300a1dd1ef61aa7a203441f971c6229dd306157ac8aafc20268ac7ad42c","observedAt":"2000-01-01T00:00:03Z","reasonCodes":["reason.synthetic.denied"],"sanitizedSummary":"Synthetic denial."},"type":"pre-contract-denial"},"reasonCodes":["reason.synthetic.denied"],"receiptDigest":"sha256:2fde9652c4f03149a06d42a8c2128b6f33193bf198c26bf3524473a90f54b679","receiptVersion":"1","releaseOutcome":"indeterminate","sanitization":{"applied":true,"completedAt":"2000-01-01T00:00:06Z","profileId":"profile.sanitization.v1","redactionCount":0},"startedAt":"2000-01-01T00:00:00Z","taskId":"00000000-0000-4000-8000-000000000001","unresolvedCoordinationWarnings":[{"code":"reason.synthetic.unresolved","profileId":"profile.validation.v1","relatedCheckId":"check.lease-acquisition","sequence":0}],"verificationOutcome":"not-performed"}}
```

Its mathematically recomputed digest is a test oracle over invalid input, never acceptance. The earlier passed A is the sole state-history attack; exact shape, contiguous sequence, unique IDs, controller linkage, outcomes, warnings, and independent chronology remain valid. No retry epoch exists.

##### passed-I-then-failed-I — REJECT DP-N11

Complete receipt (2888 bytes):

```json
{"apiVersion":"contextctl.dev/v1alpha1","kind":"ExecutionReceipt","metadata":{"id":"00000000-0000-4000-8000-000000000018"},"spec":{"changedPaths":[],"checks":[{"checkId":"check.intent-validation","checkType":"intent-validation","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":0},{"checkId":"check.project-domain-resolution","checkType":"project-domain-resolution","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":1},{"checkId":"check.role-routing","checkType":"role-routing","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":2},{"checkId":"check.host-binding","checkType":"host-binding","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":3},{"checkId":"check.initial-preflight","checkType":"initial-preflight","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":4},{"checkId":"check.pre-issuance-revalidation","checkType":"pre-issuance-revalidation","observedAt":"2000-01-01T00:00:01Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":5},{"checkId":"check.erased-success","checkType":"contract-issuance","observedAt":"2000-01-01T00:00:02Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":6},{"checkId":"check.contract-issuance","checkType":"contract-issuance","observedAt":"2000-01-01T00:00:03Z","outcome":"failed","profileId":"profile.validation.v1","reasonCodes":["reason.synthetic.denied"],"sequence":7},{"checkId":"check.receipt-finalization","checkType":"receipt-finalization","observedAt":"2000-01-01T00:00:06Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":8}],"executionOutcome":"not-attempted","finishedAt":"2000-01-01T00:00:06Z","lifecycleOutcome":"denied","origin":{"denialCheckpoint":"contract-issuance","leaseAcquisition":{"state":"not-required"},"preContractEvidence":{"controllerCheckId":"check.contract-issuance","evidenceDigest":"sha256:e53415c5bad5345082073b225dba4ddb01a895968f03815e9a5fcd0b80ebc839","observedAt":"2000-01-01T00:00:03Z","reasonCodes":["reason.synthetic.denied"],"sanitizedSummary":"Synthetic denial."},"type":"pre-contract-denial"},"reasonCodes":["reason.synthetic.denied"],"receiptDigest":"sha256:d57f7c7fb94a295c2430f12e8a4bf899a779c5e45584e8c811555a114d882f74","receiptVersion":"1","releaseOutcome":"not-required","sanitization":{"applied":true,"completedAt":"2000-01-01T00:00:06Z","profileId":"profile.sanitization.v1","redactionCount":0},"startedAt":"2000-01-01T00:00:00Z","taskId":"00000000-0000-4000-8000-000000000001","unresolvedCoordinationWarnings":[],"verificationOutcome":"not-performed"}}
```

Its mathematically recomputed digest is a test oracle over invalid input, never acceptance. The earlier passed I is the sole state-history attack; exact shape, contiguous sequence, unique IDs, controller linkage, outcomes, warnings, and independent chronology remain valid. No retry epoch exists.

##### passed-I-then-indeterminate-I — REJECT DP-N11

Complete receipt (2895 bytes):

```json
{"apiVersion":"contextctl.dev/v1alpha1","kind":"ExecutionReceipt","metadata":{"id":"00000000-0000-4000-8000-000000000019"},"spec":{"changedPaths":[],"checks":[{"checkId":"check.intent-validation","checkType":"intent-validation","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":0},{"checkId":"check.project-domain-resolution","checkType":"project-domain-resolution","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":1},{"checkId":"check.role-routing","checkType":"role-routing","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":2},{"checkId":"check.host-binding","checkType":"host-binding","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":3},{"checkId":"check.initial-preflight","checkType":"initial-preflight","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":4},{"checkId":"check.pre-issuance-revalidation","checkType":"pre-issuance-revalidation","observedAt":"2000-01-01T00:00:01Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":5},{"checkId":"check.erased-success","checkType":"contract-issuance","observedAt":"2000-01-01T00:00:02Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":6},{"checkId":"check.contract-issuance","checkType":"contract-issuance","observedAt":"2000-01-01T00:00:03Z","outcome":"indeterminate","profileId":"profile.validation.v1","reasonCodes":["reason.synthetic.denied"],"sequence":7},{"checkId":"check.receipt-finalization","checkType":"receipt-finalization","observedAt":"2000-01-01T00:00:06Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":8}],"executionOutcome":"not-attempted","finishedAt":"2000-01-01T00:00:06Z","lifecycleOutcome":"denied","origin":{"denialCheckpoint":"contract-issuance","leaseAcquisition":{"state":"not-required"},"preContractEvidence":{"controllerCheckId":"check.contract-issuance","evidenceDigest":"sha256:e53415c5bad5345082073b225dba4ddb01a895968f03815e9a5fcd0b80ebc839","observedAt":"2000-01-01T00:00:03Z","reasonCodes":["reason.synthetic.denied"],"sanitizedSummary":"Synthetic denial."},"type":"pre-contract-denial"},"reasonCodes":["reason.synthetic.denied"],"receiptDigest":"sha256:bb97681c6ada4a5db3ddbfa38fcabe28f674ab358fe1e6752647c0b5ff7cb6f4","receiptVersion":"1","releaseOutcome":"not-required","sanitization":{"applied":true,"completedAt":"2000-01-01T00:00:06Z","profileId":"profile.sanitization.v1","redactionCount":0},"startedAt":"2000-01-01T00:00:00Z","taskId":"00000000-0000-4000-8000-000000000001","unresolvedCoordinationWarnings":[],"verificationOutcome":"not-performed"}}
```

Its mathematically recomputed digest is a test oracle over invalid input, never acceptance. The earlier passed I is the sole state-history attack; exact shape, contiguous sequence, unique IDs, controller linkage, outcomes, warnings, and independent chronology remain valid. No retry epoch exists.

#### `profile.digest.execution-receipt-v1` payload

The exact digest projection excludes only `spec.receiptDigest`:

The no-lease successful golden has this complete check sequence:

| Sequence | `checkType` | Outcome |
| ---: | --- | --- |
| 0 | `intent-validation` | `passed` |
| 1 | `project-domain-resolution` | `passed` |
| 2 | `role-routing` | `passed` |
| 3 | `host-binding` | `passed` |
| 4 | `initial-preflight` | `passed` |
| 5 | `pre-issuance-revalidation` | `passed` |
| 6 | `contract-issuance` | `passed` |
| 7 | `pre-action-revalidation` | `passed` |
| 8 | `execution` | `succeeded` |
| 9 | `post-execution-verification` | `passed` |
| 10 | `receipt-finalization` | `passed` |

The V member retains
`postconditionRef: {"type":"scope-contained"}`. A, R, L, lease identity, and
every acquisition claim remain empty because the referenced contract requires
no lease.

```json
{"apiVersion":"contextctl.dev/v1alpha1","kind":"ExecutionReceipt","metadata":{"id":"00000000-0000-4000-8000-000000000003"},"spec":{"changedPaths":[],"checks":[{"checkId":"check.intent-validation","checkType":"intent-validation","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":0},{"checkId":"check.project-domain-resolution","checkType":"project-domain-resolution","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":1},{"checkId":"check.role-routing","checkType":"role-routing","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":2},{"checkId":"check.host-binding","checkType":"host-binding","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":3},{"checkId":"check.initial-preflight","checkType":"initial-preflight","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":4},{"checkId":"check.pre-issuance-revalidation","checkType":"pre-issuance-revalidation","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":5},{"checkId":"check.contract-issuance","checkType":"contract-issuance","observedAt":"2000-01-01T00:00:01Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":6},{"checkId":"check.pre-action-revalidation","checkType":"pre-action-revalidation","observedAt":"2000-01-01T00:00:01Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":7},{"checkId":"check.execution","checkType":"execution","observedAt":"2000-01-01T00:00:02Z","outcome":"succeeded","profileId":"profile.validation.v1","reasonCodes":[],"sequence":8},{"checkId":"check.post-execution-verification","checkType":"post-execution-verification","observedAt":"2000-01-01T00:00:02Z","outcome":"passed","postconditionRef":{"type":"scope-contained"},"profileId":"profile.validation.v1","reasonCodes":[],"sequence":9},{"checkId":"check.receipt-finalization","checkType":"receipt-finalization","observedAt":"2000-01-01T00:00:02Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":10}],"executionOutcome":"succeeded","finishedAt":"2000-01-01T00:00:02Z","lifecycleOutcome":"succeeded","origin":{
"contractDigest":"sha256:238c3af3ceab3eafc70d660b6e3d5cef97c3741d48b76c49e9e998a26d8afe30","contractId":"00000000-0000-4000-8000-000000000002","effectiveMode":"plan-only","resolvedTarget":{"domainRefs":[{"apiVersion":"contextctl.dev/v1alpha1","id":"domain.invalid","kind":"Domain"}],"projectRef":{"apiVersion":"contextctl.dev/v1alpha1","id":"project.invalid","kind":"Project"},"worktreeId":"worktree.invalid","worktreeRoleRef":{"apiVersion":"contextctl.dev/v1alpha1","id":"role.invalid","kind":"WorktreeRole"}},"type":"issued-contract"},
"reasonCodes":[],"receiptVersion":"1","releaseOutcome":"not-required","sanitization":{"applied":true,"completedAt":"2000-01-01T00:00:02Z","profileId":"profile.sanitization.v1","redactionCount":0},"startedAt":"2000-01-01T00:00:00Z","taskId":"00000000-0000-4000-8000-000000000001","unresolvedCoordinationWarnings":[],"verificationOutcome":"passed"}}
```

The exact completed receipt, proving the sole excluded member, is:

```json
{"apiVersion":"contextctl.dev/v1alpha1","kind":"ExecutionReceipt","metadata":{"id":"00000000-0000-4000-8000-000000000003"},"spec":{"changedPaths":[],"checks":[{"checkId":"check.intent-validation","checkType":"intent-validation","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":0},{"checkId":"check.project-domain-resolution","checkType":"project-domain-resolution","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":1},{"checkId":"check.role-routing","checkType":"role-routing","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":2},{"checkId":"check.host-binding","checkType":"host-binding","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":3},{"checkId":"check.initial-preflight","checkType":"initial-preflight","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":4},{"checkId":"check.pre-issuance-revalidation","checkType":"pre-issuance-revalidation","observedAt":"2000-01-01T00:00:00Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":5},{"checkId":"check.contract-issuance","checkType":"contract-issuance","observedAt":"2000-01-01T00:00:01Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":6},{"checkId":"check.pre-action-revalidation","checkType":"pre-action-revalidation","observedAt":"2000-01-01T00:00:01Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":7},{"checkId":"check.execution","checkType":"execution","observedAt":"2000-01-01T00:00:02Z","outcome":"succeeded","profileId":"profile.validation.v1","reasonCodes":[],"sequence":8},{"checkId":"check.post-execution-verification","checkType":"post-execution-verification","observedAt":"2000-01-01T00:00:02Z","outcome":"passed","postconditionRef":{"type":"scope-contained"},"profileId":"profile.validation.v1","reasonCodes":[],"sequence":9},{"checkId":"check.receipt-finalization","checkType":"receipt-finalization","observedAt":"2000-01-01T00:00:02Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":10}],"executionOutcome":"succeeded","finishedAt":"2000-01-01T00:00:02Z","lifecycleOutcome":"succeeded","origin":{
"contractDigest":"sha256:238c3af3ceab3eafc70d660b6e3d5cef97c3741d48b76c49e9e998a26d8afe30","contractId":"00000000-0000-4000-8000-000000000002","effectiveMode":"plan-only","resolvedTarget":{"domainRefs":[{"apiVersion":"contextctl.dev/v1alpha1","id":"domain.invalid","kind":"Domain"}],"projectRef":{"apiVersion":"contextctl.dev/v1alpha1","id":"project.invalid","kind":"Project"},"worktreeId":"worktree.invalid","worktreeRoleRef":{"apiVersion":"contextctl.dev/v1alpha1","id":"role.invalid","kind":"WorktreeRole"}},"type":"issued-contract"},
"reasonCodes":[],"receiptDigest":"sha256:d3cc668ea95fa385392f04b4e5580cd2fdc810835ae7fd1ab285c102777402b0","receiptVersion":"1","releaseOutcome":"not-required","sanitization":{"applied":true,"completedAt":"2000-01-01T00:00:02Z","profileId":"profile.sanitization.v1","redactionCount":0},"startedAt":"2000-01-01T00:00:00Z","taskId":"00000000-0000-4000-8000-000000000001","unresolvedCoordinationWarnings":[],"verificationOutcome":"passed"}}
```

The exact post-finalization `ReceiptDeliveryResult` is not a new digest
payload. It copies the finalized receipt digest by exact tagged-string equality:

```json
{"apiVersion":"contextctl.dev/v1alpha1","attemptedAt":"2000-01-01T00:00:03Z","outcome":"succeeded","reasonCodes":[],"receiptDigest":"sha256:d3cc668ea95fa385392f04b4e5580cd2fdc810835ae7fd1ab285c102777402b0","receiptId":"00000000-0000-4000-8000-000000000003","sanitizedSummary":"Synthetic delivery succeeded."}
```

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

## 11. Complete array-ordering matrix

### PG-1 broad-region attestation

The pre-RS-1/LB-2 attestation is historical and superseded; it does not
identify the current protected region:

```text
historical/superseded PG-1 W = 35334 bytes / 271 CRLF / a4f80b731f4b6c9ee8ee4ec621350f85dc24ff694c2c4b47fa10902a8ed9b88d
historical/superseded PG-1 B = 35063 bytes / 271 LF / 75c200b287b770c418218ea34ed98a800a4a229ea536109ff0f764f449a3e2a7
```

The intermediate RS-1/LB-2 pre-AP-1 attestation is also historical and
superseded:

```text
PG-1 W bytes = 37326
PG-1 W CRLF separators = 295
PG-1 W SHA-256 = e6cd8deb426a509a2ade0c4df48f2bf7c6e148afed02d3ce697faeb910318251
PG-1 B bytes = 37031
PG-1 B LF separators = 295
PG-1 B SHA-256 = 8d8b0aee8b93559690d530402761347fba0aa222962ef11b99d42caf1262c432
```


The immediately preceding AP-1 attestation is historical and superseded by Option B:

```text
historical/superseded PG-1 W = 38914 bytes / 313 CRLF / cbe0ed9ad14919f5acfef5edba978233ce57d679644e22179dc591d5c2edd9ad
historical/superseded PG-1 B = 38601 bytes / 313 LF / 719899f43c6f8c0908d7b6887a720960d010aab98e99fc254031da7b2e404b58
```

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

Comparators and identity functions are defined as follows:

- `S(value)` compares the already-NFC decoded string lexicographically by
  unsigned UTF-16 code units, matching JCS object-property ordering. It
  performs no locale comparison, case folding, or normalization.
- `R(ref)` is the componentwise tuple `S(ref.apiVersion)`, `S(ref.kind)`,
  `S(ref.id)`.
- `J(value)` is the unsigned bytewise lexicographic comparison of the value's
  RFC 8785 UTF-8 representation after all nested arrays have passed their own
  canonical checks.
- `L(lock)` is the administrative-lock tuple defined in section 7.
- `T(transition)` is the transition target tuple defined in section 7.
- Tuple comparison is componentwise. Numeric priority comparison is ordinary
  integer comparison.
- A set-like array is valid only when its identity keys are strictly
  increasing in the required order; an equal identity key is a duplicate and
  is rejected.

| Array field | Classification | Identity or sequence key | Required order key |
| --- | --- | --- | --- |
| `repositoryIdentity.acceptedRemotes` wherever used | Set-like | `J(remote)` | `J(remote)` after canonical remote checks |
| `remote.namespace` | Ordered by explicit semantics | — | Preserve namespace path-segment position |
| `permissions.modes` | Set-like | `S(value)` | `S(value)` |
| `permissions.permittedCapabilities` | Set-like | `S(value)` | `S(value)` |
| `permissions.prohibitedCapabilities` | Set-like | `S(value)` | `S(value)` |
| `scope.capabilities` | Set-like | `S(value)` | `S(value)` |
| `scope.paths` | Set-like | `S(path)` | `S(path)` |
| `Project.domainRefs` | Set-like | `R(ref)` | `R(ref)` |
| `Project.worktreeRoleRefs` | Set-like | `R(ref)` | `R(ref)` |
| `Domain.pathScope.include` | Set-like | `S(pattern)` | `S(pattern)` |
| `Domain.pathScope.exclude` | Set-like | `S(pattern)` | `S(pattern)` |
| `Domain.overlapRefs` | Set-like | `R(ref)` | `R(ref)` |
| `WorktreeRole.ownedDomainRefs` | Set-like | `R(ref)` | `R(ref)` |
| `WorktreeRole.excludedDomainRefs` | Set-like | `R(ref)` | `R(ref)` |
| `WorktreeRole.branchPolicy.allowed.exact` | Set-like | `S(branchRef)` | `S(branchRef)` |
| `WorktreeRole.branchPolicy.allowed.prefixes` | Set-like | `S(branchPrefix)` | `S(branchPrefix)` |
| `WorktreeRole.branchPolicy.denied.exact` | Set-like | `S(branchRef)` | `S(branchRef)` |
| `WorktreeRole.branchPolicy.denied.prefixes` | Set-like | `S(branchPrefix)` | `S(branchPrefix)` |
| `RoutingPolicy.rules` | Ordered by explicit semantics | `S(rule.id)` | Priority descending, then `S(rule.id)` ascending |
| `RoutingPolicy.rules[].match.domainSet.domainRefs` | Set-like | `R(ref)` | `R(ref)` |
| `HostOverlay.bindings` | Set-like | `(R(roleRef), S(worktreeId))` | Same tuple |
| `HostOverlay.bindings[].remoteNames` | Set-like, non-empty | `S(value)` | `S(value)` |
| `HostOverlay.remoteExpectations` | Set-like | `S(remoteName)` | `S(remoteName)` |
| `HostOverlay.remoteExpectations[].acceptedRemotes` | Set-like | `J(remote)` | `J(remote)` after canonical remote checks |
| `HostOverlay.capabilityCeiling` | Set-like | `S(value)` | `S(value)` |
| `HostOverlay.pathCeiling.include` | Set-like | `S(path)` | `S(path)` |
| `HostOverlay.pathCeiling.exclude` | Set-like | `S(path)` | `S(path)` |
| `TaskContract.domainRefs` | Set-like | `R(ref)` | `R(ref)` |
| `TaskContract.authorizedScope.capabilities` and `.paths` | Set-like | `S(value)` and `S(path)` respectively | Same respective key |
| `TaskContract.prohibitedScope.capabilities` and `.paths` | Set-like | `S(value)` and `S(path)` respectively | Same respective key |
| `TaskContract.expectedBaseline.index.entries` | Set-like complete inventory; stage `0` only; conflict stages are rejected before `TaskContract` issuance | `S(entry.path)` | `S(entry.path)` |
| `TaskContract.expectedBaseline.tracked.entries` | Set-like | `S(entry.path)` | `S(entry.path)` |
| `TaskContract.expectedBaseline.untracked.paths` | Set-like | `S(path)` | `S(path)` |
| `TaskContract.expectedBaseline.ignored.paths` | Set-like | `S(path)` | `S(path)` |
| `TaskContract.expectedBaseline.submodules.entries` | Set-like | `S(entry.path)` | `S(entry.path)` |
| `TaskContract.permittedTransitions` | Set-like | `T(transition)` | `T(transition)` |
| `TaskContract.requiredPostconditions` | Set-like | `S(type)` | `S(type)` |
| `TaskContract.requiredPostconditions[type="index-state"].expected.entries` | Set-like complete inventory reusing the stage-`0` baseline profile | `S(entry.path)` | `S(entry.path)` |
| `TaskContract.requiredPostconditions[type="tracked-state"].expected.entries` | Set-like | `S(entry.path)` | `S(entry.path)` |
| `TaskContract.requiredPostconditions[type="untracked-state"].expected.paths` | Set-like | `S(path)` | `S(path)` |
| `TaskContract.requiredPostconditions[type="ignored-state"].expected.paths` | Set-like | `S(path)` | `S(path)` |
| `TaskContract.requiredPostconditions[type="submodule-state"].expected.entries` | Set-like | `S(entry.path)` | `S(entry.path)` |
| `ExecutionReceipt.origin.resolvedTarget.domainRefs` (`issued-contract` branch) | Set-like | `R(ref)` | `R(ref)` |
| `ExecutionReceipt.origin.preContractEvidence.reasonCodes` (`pre-contract-denial` branch) | Set-like | `S(code)` | `S(code)` |
| `ExecutionReceipt.unresolvedCoordinationWarnings` | Append-only evidence order | `sequence` | `sequence` equals array position and is contiguous from 0 |
| `ExecutionReceipt.checks` | Append-only evidence order | `sequence`; `S(checkId)` is independently unique | `sequence` equals array position and is contiguous from 0 |
| `ExecutionReceipt.checks[].reasonCodes` | Set-like | `S(code)` | `S(code)` |
| `ExecutionReceipt.changedPaths` | Set-like | `S(path)` | `S(path)` |
| `ExecutionReceipt.spec.ordinaryOperationEvidence` | Set-like; zero or more records when conditionally required | `S(record.path)` | `S(record.path)` |
| `ExecutionReceipt.spec.ordinaryOperationEvidence[].operations` | Set-like, non-empty; one through three operation tokens | `S(operation token)` | `S(operation token)`, yielding exactly `create`, `delete`, `modify` |
| `ExecutionReceipt.reasonCodes` | Set-like | `S(code)` | `S(code)` |
| `ReceiptDeliveryResult.reasonCodes` | Set-like | `S(code)` | `S(code)` |
| `GovernanceBundle.domains` | Set-like | `S(metadata.id)` | `S(metadata.id)` |
| `GovernanceBundle.worktreeRoles` | Set-like | `S(metadata.id)` | `S(metadata.id)` |

The final matrix contains 54 data rows, counted from the table above. It covers
every instance array in the `v1alpha1-r1` contract design. Relative to the
54-row prior baseline, the two now-impossible TaskContract administrative-lock
exact rows remain removed and the two A2 ordinary-operation-evidence rows are
added. The removed rows are
`expectedBaseline.administrativeLocks.locks` and
`requiredPostconditions[type="administrative-locks"].expected.locks`. The
reusable active-operation and administrative-lock observation/evidence unions
retain their prose-defined uniqueness and canonical-order requirements,
including `L(lock)` for administrative locks. Shared definitions use the same
rule everywhere they remain embedded. No v1alpha1 array is
"order-insensitive but preserved on the wire." Adding such a field would make
digests representation-sensitive and requires a new explicit design review.
JCS never reorders an array.

## 12. Structural, static, later-phase, and external-control matrix

| Requirement | JSON Schema structural enforcement | Phase 1 static or fixture hygiene | Later operational enforcement | External control |
| --- | --- | --- | --- | --- |
| Required fields, types, enums, closed objects | Enforce | Contract vectors | Not applicable | Not applicable |
| Identifier, path, digest, UUID, and format syntax | Enforce lexical profile, including exact `.git`-component rejection for repository-relative paths and literal path patterns | Canonical spelling, revised-universe pattern parsing, and cross-reference checks | Bind to trusted/live values where required; Phase 3 rejects administrative indirection and aliases | Not applicable |
| Duplicate JSON keys | Not observable after ordinary parsing | Contract records rejection before object construction; executable strict-parser detection and tests belong to future `model-implementation` | The same trusted decoder runs before later verification | Not applicable |
| Raw JSON-number token profile | `type: integer` cannot preserve lexical form | Contract records raw-token rejection, ceiling, and bounds; executable enforcement before conversion belongs to future `model-implementation` | Verification repeats raw-token validation or requires the complete validated canonical instance representation proof | Not applicable |
| Numeric field inventory | Exact integer type and per-field minimum/maximum | Reject any undeclared numeric field and audit the complete six-field inventory | A future signed or fractional field requires a contract revision | Not applicable |
| Strings and member names already NFC | Not portable as an ordinary Schema assertion | Contract records non-NFC rejection; executable checking belongs to future `model-implementation` | Repeat before hashing and verification | Authoring guidance |
| Reference existence, uniqueness, subset rules, canonical arrays | Shape only or partial uniqueness | Enforce within a closed loaded set | Revalidate selected/runtime bindings | Not applicable |
| `displayName` is non-identifying | Length and character shape only | Conspicuously synthetic fixtures and best-effort scanner | Sanitize if copied into Phase 4 evidence | Author review and data classification |
| Description text is secret-free | Length and character shape only | Synthetic values and best-effort secret scanning | Phase 4 redaction/sanitization before evidence | Secret manager, DLP, review, and access controls |
| A hostname is non-sensitive | Hostname syntax only | Reserved `.invalid` fixture hosts | Phase 4 redacts sensitive environment evidence | Environment classification and access control |
| A `sanitizedSummary` is actually safe | Bounded string shape only | Synthetic fixture content | Phase 4 sanitizer must create/check it and fail closed on incomplete sanitization | DLP, review, and evidence access policy |
| No secrets in arbitrary permitted strings | Unknown secret-like fields are rejected; allowed strings can still hold secrets | Best-effort scanners | Phase 4 redaction; no secret values in contracts or receipts | External secret delivery and incident handling |
| `absoluteHostPath` lexical validity and intended-host binding | Enforce the closed `posix`/`windows` union, required `platform` and `value`, unknown-field rejection, and Schema-expressible branch syntax | Enforce strict UTF-8/scalars, already-NFC, length from 1 through 4096 decoded scalars, control exclusions, exact POSIX grammar, uppercase-drive-only Windows grammar, segment/device rules, UNC/device-namespace rejection, exact equality, and the complete synthetic vector set | Phase 3 checks actual platform compatibility, canonical filesystem identity, drive availability, aliases, symlinks/junctions, registration, real-path equality, and containment | Host filesystem permissions |
| Domain resolution and routing are unambiguous | Policy shape only | Provable closed-bundle contradictions, complete-set matching contract, and expected vectors only | Phase 2 follows the exact 17-step order, requires `Dresolved ⊆ Owned(Rdecision)`, denies ties or incomplete ownership without fallthrough, and never unions roles | Not applicable |
| HostOverlay narrows customer governance | Shape and conditional fields | Enforce D10 Project/role identity, exact capability equations, accepted-remote inclusions, binding-name resolution, and DFA path-language inclusions; any unsupported or indeterminate proof denies the configuration | Phases 2-3 consume the statically valid restriction and compare the bound worktree live; this row does not execute routing | Host configuration review |
| HostOverlay remote expectations have one record per name and non-empty accepted sets | Enforce the closed five-field remote, exact transport enum, `remoteDnsHost`, namespace and `remoteRepositoryName` lexical bounds, terminal-`.git` rejection, numeric port bounds, explicit-default-port rejection, and non-empty `acceptedRemotes` | Enforce joined namespace length, outer uniqueness/order by only `S(remoteName)`, nested exact `J(remote)` uniqueness/order, and HostOverlay narrowing by exact canonical membership without normalization or ignored fields | Phase 3 parses and compares each observed named Git remote with its accepted set and owns runtime host facts | Credential handling remains outside governance |
| Conflict-free index is representable | Enforce stage `0`, required false index flags, supported modes, and closed fields | Enforce path uniqueness, canonical order, and complete-inventory semantics | Phase 3 denies unmerged, intent-to-add, skip-worktree, assume-unchanged, sparse, unsupported-mode, or otherwise unrepresentable indexes before issuance | Phase 4 may record only sanitized pre-contract denial evidence |
| Baseline runtime structures are closed and exhaustive | Enforce all nine required dimensions, required and forbidden fields, enums, branch-specific exact cardinalities, and exact `none` constants for TaskContract active operations and administrative locks | Cross-branch consistency, rejection of every non-empty active-operation or administrative-lock contract baseline, and reusable-observation identity/order including `L(lock)` | Phase 3 retains the reusable live observation unions but denies a non-empty operation or present live lock at the applicable checkpoint; Phase 4 retains pre-contract denial, post-contract non-attempted, and failed/indeterminate terminal evidence | Repository and host protections |
| ExpectedBaseline inventory and cross-dimension consistency | Enforce branch shapes, local field relationships, and the revised valid path profile | Enforce complete explicit inventories, `.git`-component exclusion, index/tracked and gitlink/submodule equality, coverage, and exact-path disjointness where closed data suffices | Phase 3 enforces relationships requiring HEAD, objects, ignore rules, filesystem, checkout, live index, or administrative-root resolution | Phase 4 verification reuses the same path and state semantics for postconditions and changed-path evidence |
| Baseline and postcondition state entries are unique by repository-relative path | Enforce entry shape and required path | Reject duplicate `S(entry.path)` before hashing, regardless of other entry fields | Phases 3–4 compare live state by the same path identity | Not applicable |
| TaskContract mode, write, lease, and lease-state truth table | Enforce the four allowed closed combinations and conditional field presence | Reject every unlisted combination and cross-field mismatch | Phase 3 validates required lease ownership; Phase 4 validates effective authority and contract binding | Issuer and lease-store administration |
| Seven transition targets and eleven postcondition types are unique | Enforce exactly seven transition branches and eleven postcondition branches, with active-operation and administrative-lock postconditions both none-only | Reject duplicate `T(transition)`, duplicate `S(type)`, either retired transition, and either non-empty postcondition before hashing | Phase 4 attributes only the seven authorized transition classes and checks all postconditions | Not applicable |
| Required denial bindings, safe summary placement, and safe F shape | Require closed state-only denial origin; receipt-level acquisitionBinding iff stable-acquired; controllerCheckId and sanitizedSummary; exact seven-member F shape and reserved tuple | Apply the explicit repeatable G/N/R versus singleton state-creating A/I matrix; unified Source/binding/A/every-R/every-L equality; controller identity/time/reasons; issued lease equality; required summary and warning linkage | Phase 3/4 retain event truth, provenance, ownership, sanitization, release, and authority |
| Warning `relatedCheckId` integrity | Enforce identifier shape only | Resolve every present value to exactly one same-receipt `checkId`; forward and backward references are allowed | Phase 4 records the closed receipt evidence | Evidence retention and access policy |
| Branch, HEAD, dirty state, operation, lock, and lease match | Expected-state representation only; the TaskContract active-operation and administrative-lock dimensions are both none-only | Local consistency plus separate checkpoint denial/evidence classification for reusable live operation and lock observations | Phase 3 observes live, denies every represented active operation or Git administrative lock at the applicable checkpoint, and separately coordinates leases | Repository and host protections |
| TaskContract is trusted, fresh, and authoritative | Representation only | Structural/static consistency | Phase 4 validates issuer, derivation, integrity, bindings, freshness, and current preconditions | Issuer/key/trust administration |
| Receipt origin, contract binding, and pre-contract lease evidence agree | Enforce closed `oneOf` branches, conditional fields, and the existing receipt/contract field shapes | For `issued-contract`, validate the complete referenced contract, recompute `profile.digest.task-contract-v1`, enforce all eight exact contract-ID, digest, task, complete target, complete ordered Domain, and effective-mode equalities before receipt-digest acceptance; also reject invalid checkpoint/state combinations and impossible pre-contract execution claims | Phase 4 verifies provenance, authenticity, current authority and preconditions, records the applicable origin, and finalizes only after release outcome is known | Evidence retention and access policy |
| Receipt and related-artifact chronology, consistency, and non-authority | Nine canonical timestamp fields, closed check outcomes, V-only postconditionRef, stable A/R/L compact shape, and closed receipt representation | Twenty primitive plus eleven derived chronology relations; universal every-G-before-A and A-before-every-R sequence/time; state-aware matrix; all independent PB/AI/DP/RF/RC owners; P/E/V and release outcome/terminality; immutable preparation selectors before static acceptance and receipt digest | Phase 4 retains trusted time, event truth, authority, receipt generation, and delivery |

Schema cannot prove that arbitrary text is secret-free, a display name is non-identifying, a hostname is non-sensitive, or a sanitized summary is safe. Fixture hygiene and scanners are defense in depth, not proofs.

## 13. Validator capability requirements

A later selected validator and parser must provide all of the following:

- complete Draft 2020-12 support for every adopted core, applicator, validation, and format vocabulary feature;
- correct `$schema`, `$id`, `$defs`, absolute `$ref`, `const`, composition, conditional, and closed-object behavior;
- mandatory format assertion with positive and negative vectors for every enabled format;
- a fixed offline registry that supports arbitrary absolute URI schemes, including the exact UUID URNs in section 3;
- hard errors for missing resources and no network retrieval or fallback;
- local availability of the required Draft 2020-12 meta-schemas, either pinned through the dependency or vendored by an approved process;
- duplicate-key detection and raw numeric-token validation during the same
  strict parse, before Schema validation and before an ordinary decoded object
  can erase either condition;
- strict UTF-8 and Unicode-scalar handling plus exact enforcement of
  `0|[1-9][0-9]*`, the `9007199254740991` ceiling, and every per-field
  numeric bound;
- proof that accepted integers transfer through strict parsing, the immutable
  validated canonical instance representation, RFC 8785 JCS, replay, and
  supported runtimes without precision loss, and rejection of a generic
  decoded object lacking the complete representation proof;
- structured error access exposing the resource/schema ID, instance JSON Pointer, Schema JSON Pointer, and failing keyword;
- deterministic ordering of error records without assertions against vendor-specific message prose;
- hooks for Phase 1 static validation, canonical-array checks, transition and
  postcondition uniqueness, greatest-sequence final-applicable `P`, `E`, and `V`
  selection, `count(P) >= 1`, `count(E) >= 1`, `count(V) >= 1`, every attempted
  P passed, same-lifecycle terminality of any failed or indeterminate P with no
  later P/E/V and not-attempted/not-performed outcomes, universal final-`P`-
  before-every-`E` and every-`E`-before-every-`V` ordering by sequence and
  timestamp, attempted-execution freshness, EF-1 execution terminality, final-`E` and final-`V` outcome
  binding, not-attempted E/V emptiness, path-and-operation scope conformance, mandatory
  `sanitization.applied == true`, receipt outcome consistency, and closed-bundle
  validation;
- reproducible exact direct dependencies plus a transitive lock or verified hashes;
- dependency provenance and license review; and
- a pinned conformance profile covering every Schema feature actually used.

Error-record ordering is by instance pointer, Schema resource ID, Schema pointer, and keyword, with a deterministic final tie-breaker defined by the chosen adapter. A command failure and a valid empty result must remain distinguishable.

## 14. Toolchain gate

No validator has been selected. No `pyproject.toml`, dependency declaration, transitive lock, or approved toolchain exists. Therefore executable Schema tests, fixtures that depend on executable validation, and Schema implementation remain blocked.

If Python is selected, `pyproject.toml` and an approved exact dependency lock are required. If another language is selected, its corresponding approved manifest and lock are required. Ad hoc imports, globally installed packages, and untracked environments are not acceptable evidence.

`integration-control` owns the validator/toolchain, packaging, dependency lock,
provenance, licensing, security, and release decision. `schema-contracts` owns
the capability requirements in section 13, structural/static Schema vectors,
and the recorded executable-codec expectations. The future distinct
`model-implementation` role owns executable decoder, canonical representation,
projection, JCS, hashing, replay, round-trip, Schema/model, and cross-runtime
conformance. Selecting a package requires a separate authorization and does
not belong to this design-record task.

## 15. Planned fixtures and contract tests

Every item in this section is planned and unimplemented. All values must be conspicuously synthetic, use reserved `.invalid` identities where appropriate, and contain no real host, customer, repository, incident, credential, or deployment data.

Planned positive fixtures include:

- minimal portable GovernanceBundle;
- valid multi-Domain bundle with declared overlap;
- valid review-only role;
- valid integration-control role that gains no implicit administrative authority;
- valid RoutingPolicy with same-priority disjoint rules;
- valid restrictive HostOverlay using synthetic absolute paths;
- valid HostOverlay with one `remoteName` and one accepted remote;
- valid HostOverlay with one `remoteName` and multiple accepted remotes;
- valid HostOverlay with multiple unique `remoteName` records;
- valid TaskContracts covering all four allowed requested-mode, effective-mode,
  write, lease, lease-ID, and lease-state truth-table rows;
- valid issued-contract receipt, including successful, denied, failed, cancelled, and indeterminate outcome shapes;
- valid issued-contract receipt with multiple P checks only when every attempted
  P passed;
- valid lease and no-lease issuance chronology with R/N equal to the issuance
  checkpoint and the checkpoint equal to `issuedAt`;
- valid serialized receipt with `sanitization.applied: true` and
  `redactionCount: 0`;
- valid pre-contract denial before lease acquisition;
- valid pre-contract denial after failed lease acquisition;
- valid pre-contract denial after acquired lease and successful ownership-checked cleanup;
- valid pre-contract denial after acquired lease and failed ownership-checked cleanup;
- valid pre-contract denial after acquired lease and indeterminate ownership-checked cleanup; and
- valid post-finalization ReceiptDeliveryResult.

Planned negative fixtures include:

- unknown field at every object depth and additional-property violations;
- missing, malformed, or unsupported API version and wrong kind discriminator;
- duplicate IDs, missing references, wrong-kind references, role reference to an unknown Domain, and RoutingPolicy reference to an unknown role;
- empty Domain set where non-empty is required, self-overlap, asymmetric overlap, and owned/excluded Domain intersection;
- every TaskContract combination outside the four-row mode/write/lease truth
  table, including requested `plan-only` with effective `implementation`,
  effective `plan-only` with `allowWrite: true`, either mismatch between
  `allowWrite` and `leaseRequired`, either invalid `leaseId` presence case, and
  either invalid `lease-state` expectation;
- every required valid and invalid repository-relative path and path-pattern
  example in the portable-path section, including literal `.git` components,
  broad `**`, and permitted similar names;
- reserved `.git`-component values attempted through Domain scope,
  role-derived scope, HostOverlay ceiling, TaskContract scopes, baseline and
  postcondition entries, transition targets, changed paths, and
  `scope-contained` evidence;
- HostOverlay widening capabilities, paths, roles, or repository identity;
- duplicate HostOverlay `remoteName` outer records even when their remote values differ;
- empty HostOverlay `acceptedRemotes`;
- duplicate accepted remote in one HostOverlay remote-expectation record;
- HostOverlay `acceptedRemotes` in non-canonical order;
- secret-like prohibited field and authority-like receipt grant field;
- TaskContract without freshness, with reversed freshness, or with `leaseRequired: true` and no `leaseId`;
- TaskContract with `leaseId` when no lease is required;
- duplicate TaskContract baseline index path with different entry contents;
- duplicate TaskContract baseline tracked path with different entry contents;
- duplicate TaskContract baseline submodule path with different object IDs,
  checkout, or observation contents;
- duplicate required-postcondition entry path with different contents;
- issued-contract receipt origin missing `contractId`;
- issued-contract receipt origin missing `contractDigest`;
- issued-contract receipt origin containing pre-contract-denial-only fields;
- pre-contract-denial receipt origin containing `contractId`;
- pre-contract-denial receipt origin containing `contractDigest`;
- pre-contract-denial receipt missing `denialCheckpoint`;
- `preContractEvidence` missing required `sanitizedSummary`;
- `preContractEvidence` missing required `controllerCheckId`, using an unknown
  controller ID, or disagreeing with the controller's mapped type,
  greatest-sequence identity, outcome, `observedAt`, `reasonCodes`, or
  cumulative-matrix position;
- a stable-acquired receipt missing acquisitionBinding or its one Source, or mismatching Source/binding task/check/lease/digest, X/A identity, or any A/R/L compact reference;
- any non-stable path carrying acquisitionBinding, Source, or a compact reference;

- `ReceiptDeliveryResult` missing required `sanitizedSummary`;
- F containing `expectedSummary`, `observedSummary`, both, or any other
  summary, detail, payload, or free-form member;
- any denial origin.leaseAcquisition branch carrying any member other than its exact state;

- pre-contract-denial receipt claiming successful execution;
- an issued receipt with a failed or indeterminate P followed by any later P, E,
  or V in the same lifecycle, or with execution/verification anything other
  than not-attempted/not-performed;
- a lease-required issued receipt with R after the issuance checkpoint, or a no-
  lease issued receipt with N after the issuance checkpoint;
- any serialized receipt with `sanitization.applied: false`;
- non-NFC string/member name, duplicate JSON key, malformed UTF-8, and unsupported number representation;
- non-canonical or duplicate set-like array entry and non-contiguous evidence sequence;
- different rule IDs whose exact `RuleProjection` RFC 8785 JCS bytes are equal;
  and
- same-priority rules whose exact `MatchProjection` RFC 8785 JCS bytes are
  equal, whether their decisions agree or differ.

Duplicate priority by itself is not an invalid fixture. Context-dependent multiple-highest-match execution tests belong to Phase 2.

Planned `schema-contracts` tests cover every Schema accepting structural
positive fixtures and rejecting structural negative fixtures; nested
unknown-field rejection; discriminators and supported versions; mandatory
formats; exact offline catalog and `$ref` resolution; canonical arrays over
already-decoded values; closed-bundle uniqueness, references, and static
integrity; catalog UUID/resource invariants; and confirmation that no synthetic
host/runtime value, valid TaskContract shape, digest, or receipt is authority.
The contract records strict-parser, validated-representation, NFC, projection,
JCS, hashing, replay, and golden-vector expectations, but executable coverage
of those behaviors belongs to future `model-implementation`, together with
typed round trips, Schema/model conformance, deterministic structured codec
errors, and cross-runtime byte and digest reproduction.

Baseline and postcondition contract tests require duplicate-path validation to fail before hashing. They prove that deterministic full-object order cannot make a duplicate path valid and that entry arrays nested in required postconditions use the same sole `S(entry.path)` uniqueness and ordering rule as baseline index, tracked, and submodule entries.

Planned ExecutionReceipt coverage includes both closed origin branches,
conditional contract fields, every pre-contract denial checkpoint class, every
permitted checkpoint/acquisition-state pair, and rejection of every unlisted
pair. Each denial class applies its exact cumulative prerequisite prefix,
controller ID/type/greatest-sequence/first-failure/outcome/time/reason binding, forbidden
future-stage set, acquired-only A/lease/digest binding, applicable cleanup,
sanitization, and exact-tuple terminal F. The plan rejects non-acquired or
indeterminate states carrying lease identity, successful-execution claims in
pre-contract receipts, missing prerequisites, either denial-stage boundary
variant, wrong controller/checkpoint/outcome, controller reference/binding
mismatch, acquired reference/identity mismatch, earlier non-passed same-type
controller history, forbidden F content, primitive F exact-tuple violations,
the derived generic non-F duplicate-ID case, and missing required
unresolved warnings. No executable test or fixture is claimed to exist.

Issued coverage validates the same complete C, all eight duplicated-claim comparisons, and issued X.leaseId=C.leaseId before receipt digest acceptance. Current RC01..09 owners cover those independent equalities; canonical-array faults and delivery are separate. The unified acquisition block, state-aware denial matrix, independent owner ledger, chronology graph, validation DAG, exact corpus, and adversarial matrix below jointly specify every affected path. Preserved P/E/V, scope, OC/OE, outcomes, F, and warning rules remain mandatory.

Planned HostOverlay contract tests exercise the complete selected
structured-remote language, all 15 positive and 61 independent negative remote
vectors, one outer record per `remoteName`, non-empty nested accepted sets,
`S(remoteName)` outer ordering, exact `J(remote)` nested identity and ordering,
and exact membership narrowing without normalization, aliasing, or field
omission.

Planned HostOverlay contract tests also exercise the separately counted HX
family: exactly five positive and thirteen negative primary predicates covering
complete trusted same-host membership, coherent snapshot-bound individual
validation and binding union, cross-resource binding-ID and exact-root
injectivity, cross-host comparison-domain separation, static coordination-root
exclusion in only the prohibited direction, and future fail-closed canonical
physical-worktree identity and containment. Variants are non-additive.

### Mandatory exhaustive SG-001 fixture/conformance matrix

This matrix is mandatory future coverage, not a claim that fixtures or tests
exist. `Schema` means JSON Schema structural enforcement, `Phase 1 static`
means `schema-contracts` structural/static integrity requirements over an
already-decoded closed value, and executable codec/model checks named in a row
belong to future `model-implementation`. `Phase 3 live` means repository, Git,
filesystem, checkout, and lease observation, and `Phase 4 evidence` means
trusted contract verification, post-execution verification, sanitization,
terminalization, or receipt evidence. Each row requires every listed positive
and negative vector at its assigned owner.

| Branch or invariant | Required positive vectors | Required negative vectors | Enforcement layer and responsibility |
| --- | --- | --- | --- |
| Reference, branch policy, and HEAD | branch plus commit; branch plus unborn; detached plus commit; all seven required positive `branchPrefix` and branch-policy vectors | detached plus unborn; branch missing `branchRef`; detached containing `branchRef`; commit missing `objectId`; unborn containing `objectId`; all 33 required negative branch-policy vectors, including raw-character-prefix, descendants-only, trailing-slash, and wildcard cases; plus each closed-shape missing-array variant | Schema enforces closed branches, four required policy arrays, and required/forbidden fields; Phase 1 static validates exact `branchRef`/`branchPrefix` syntax, `S(branchRef)`/`S(branchPrefix)` order and the recorded predicate vectors; Phase 3 live selects the symbolic branch or denies detached/unborn as specified, then compares actual ref and HEAD |
| Conflict-free index | clean conflict-free index; exact non-empty stage-0 complete inventory; exact empty complete inventory representing removal of all HEAD paths | stage `1`; stage `2`; stage `3`; duplicate path; unsupported mode; `intentToAdd: true`; `skipWorktree: true`; `assumeUnchanged: true`; sparse entry; unmerged index presented as a `TaskContract` baseline | Schema fixes stage and flags and closes entries; Phase 1 static enforces path identity, order, and complete explicit inventory; Phase 3 live selects clean versus exact and denies unrepresentable state; Phase 4 evidence may record sanitized pre-contract denial only |
| Tracked | tracked clean; exact inventory containing clean; modified with equal `worktreeMode` and `indexMode`; deleted; type-changed with unequal modes | modified with unequal modes; type-changed with equal modes; missing required field; branch-inapplicable field; mode `160000`; tracked/index mode mismatch; tracked/index object mismatch; omitted index path from `tracked.exact`; tracked entry for a gitlink path | Schema enforces status branches and fields; Phase 1 static enforces mode relations and explicit index equality/coverage; Phase 3 live confirms content, deletion, type, HEAD-dependent equality, and completeness; Phase 4 evidence verifies postconditions |
| Untracked and ignored / D3 path inventory | `none` for each category; non-empty exact complete inventories; regular, executable, and non-dereferenced symlink leaves; recursive ignored-directory leaves; ignore negation; empty directory emitting no member; registered submodule and Git-administrative boundary exclusion; valid `.gitignore`, `.gitmodules`, `.github`, `foo.git`, and nested similar-name paths | empty exact inventory; duplicate or non-canonical path; any exact `.git` component at any depth; cross-category or explicit-state collision; directory member; collapsed-directory alternative; unregistered nested repository; unreadable, racing, cyclic, identity/classification/submodule-boundary-unresolved, unrepresentable-path, unsupported-object, or unresolved administrative-root/alias observation | Schema enforces unions, non-empty exact arrays, and the revised path profile; Phase 1 static enforces `.git`-component rejection, `S(path)`, explicit disjointness, and directory/collapsed rejection; Phase 3 executes the leaf-only profile while resolving top-level indirection, linked/common Git dirs, aliases, registered-submodule roots, and nested repositories; Phase 4 evidence verifies postconditions without a weaker encoding |
| Submodules / D2 orthogonal state | `none`; absent/unavailable; uninitialized/unavailable; initialized/observed with each of all eight Boolean triples; initialized checkout ID equal to and different from `recordedObjectId` | absent/observed; uninitialized/observed; initialized/unavailable; missing or branch-inapplicable `checkedOutObjectId`; fields on unavailable; each missing observed Boolean; unknown field; `indeterminate`; superseded `worktreeState`; `recordedObjectId` mismatch; missing mode-`160000` inventory path; tracked/submodule collision | Schema enforces the closed checkout and observation unions; Phase 1 static enforces all pairings, explicit gitlink equality, coverage, and disjointness; Phase 3 live denies inconclusive initialized observation with one of the four D2 reason codes; Phase 4 transitions and postconditions reuse the complete checkout/observation value |
| Active operations | TaskContract baseline `none`; optional none-only postcondition; all seven `merge`, `rebase`, `cherry-pick`, `revert`, `bisect`, `sequencer`, and `apply-mailbox` identities as non-authorizing observations; pre-contract denial; post-contract/pre-action `not-attempted`; post-execution failed or indeterminate evidence | exactly 21 legacy contract regressions: seven single-operation exact baselines, seven retired active-operation transitions, and seven single-operation exact postconditions; separately, the generic observation-shape family covers duplicate, unknown, non-canonical, and empty-exact arrays | Schema enforces the reusable observation/evidence union but fixes TaskContract baseline and optional postcondition to `none`; Phase 1 rejects the 21 legacy contract cases and separately validates generic observation shape; Phase 3 live observes and denies; Phase 4 retains only non-authorizing denial or terminal evidence |
| Administrative locks | none-only TaskContract baseline and postcondition; all seven `index`, `packed-refs`, `shallow`, `config`, `head`, `ref`, and `other` branches as reusable observations/evidence; pre-contract denial; post-contract/pre-action `not-attempted`; post-execution failed or indeterminate evidence | exactly 21 legacy-contract regressions: seven non-empty single-lock baselines, seven retired transitions, and seven non-empty single-lock postconditions; separately, duplicate identity, missing or forbidden branch identifiers, unknown branch, non-canonical order, empty exact, and other malformed reusable observations | Schema enforces the reusable closed union but fixes TaskContract baseline and optional postcondition to `none`; Phase 1 rejects the 21 legacy cases and separately validates `L(lock)` identity/order; Phase 3 observes and denies; Phase 4 retains only non-authorizing denial or terminal evidence |
| Permitted transitions | one positive vector for each of exactly seven branches: `ref-state`, `head-state`, `index-entry`, `tracked-entry`, `untracked-path`, `ignored-path`, and `submodule-entry`, with every path-keyed branch in the revised valid universe; ordinary operation-capability cases cross-reference OC without adding a branch | identical `from` and `to`; duplicate target; unknown type; missing target key; branch-inapplicable key; invalid target comparator; any exact `.git` component; the retired `active-operation` and `administrative-lock` branches; OC negatives are cross-referenced rather than duplicated | Schema enforces seven closed branches and the path profile; Phase 1 static enforces exact inequality, target uniqueness, the normative `T(transition)` comparator, reserved-path rejection, retired-branch rejection, and the D7 `Oplan(B,F)` capability closure; Phase 3 live observes Git transitions; Phase 4 evidence attributes only authorized ordinary-path transitions |
| Required postconditions | one positive vector for each of eleven branches; optional `active-operations` and `administrative-locks` each expect `none`; path-keyed expected state uses the revised valid universe; successful writing `scope-contained` evidence has both path and operation-capability containment | missing or repeated `scope-contained`; duplicate type; `scope-contained` containing `expected`; state branch missing `expected`; reserved `.git`-component path; successful scope claim that omits an administrative effect or lacks path or operation-capability containment as a non-additive OC cross-reference; each forbidden single-operation active or administrative-lock expectation; malformed reusable observation condition; invalid lease-state truth-table combination | Schema enforces eleven closed branches, both none-only expectations, and valid paths; Phase 1 static enforces type uniqueness and reused baseline semantics; Phase 3 resolves administrative locations; Phase 4 requires an administrative, path-scope, or operation-capability violation to make `scope-contained` failed or indeterminate and verifies every postcondition |
| Warnings and checks | warning without optional fields; warning with summary only; warning with an earlier or later `relatedCheckId`; check without optional summaries; every one of 14 check types with its permitted outcomes; F with exactly its seven closed fields and reserved identity tuple; ordinary non-F generic IDs; general V without `postconditionRef`; referenced V for each of all eleven required-postcondition types | warning or check sequence gap/duplicate; duplicate `checkId`; dangling or cross-receipt `relatedCheckId`; invalid reason-code order; unknown check type/outcome; execution using `passed`; non-execution using `succeeded` or `cancelled`; F with either summary, any other free-form/payload member, or any non-reserved tuple value; non-F duplicating the reserved F ID under generic check-ID uniqueness; `postconditionRef` on each of the other thirteen check types; malformed/unknown reference; valid type absent from the bound contract | Schema enforces closed record shapes, the F-implies-exact-tuple specialization, 14 check types, exact 4/3 outcome conditional, and the V-only closed reference object; Phase 1 enforces sequences, globally unique IDs and the derived non-F reserved-ID exclusion, reason-code order, same-receipt warning references, complete-contract postcondition reference resolution, and per-type greatest-sequence selection; Phase 4 produces and sanitizes evidence |
| Receipt outcomes, issued-contract binding, lease acquisition, cumulative denial, timestamp chronology, and attempted-execution checks | Every origin/outcome; RC 9/9, CH 20/20 with 31 displayed relations, PB 5/5, AI 23/23, DP 13/13, RF 14/14 and their mandatory variants; retained lexical 10/24, P 8/37, final-E 8/22, verification 10/20, scope 5/6, OC 3/8, OE 10/11 case inventories; complete acquired-R/I and single-state controls | Four erased-success histories; independent sequence/time reversal; every cross-acquisition/task/check/lease/hash/copy mix; bad earlier R/L with good final member; all retained outcome, terminality, scope, warning and F negatives | Static checks and the dependency DAG precede receipt digest acceptance; operational truth remains Phase 3/4 |
| TaskContract truth table | each of the four allowed rows: plan-only/plan-only/non-writing; implementation/plan-only/non-writing; implementation/implementation/non-writing; implementation/implementation/writing with required lease and owned postcondition | requested plan-only with effective implementation; effective plan-only with `allowWrite: true`; `allowWrite: false` with `leaseRequired: true`; `allowWrite: true` with `leaseRequired: false`; `leaseId` present while no lease is required; `leaseId` absent while required; `owned` postcondition while no lease is required; `not-required` postcondition while a lease is required | Schema and Phase 1 static enforce the closed four-row invariant; Phase 3 live validates required ownership; Phase 4 evidence validates authority, binding, release, and postconditions |
| D1 validated canonical instance representation | strict UTF-8 source produces one immutable closed JSON value bound to the selected schema-set revision and root `$id`, complete strict-parse/number/NFC/Schema/static/array proof, and retained original bytes or same-process provenance; digest replay uses that representation | generic decoded object; missing or stale proof component; proof rebound to another value; mutable value; representation asserted as a public kind, production typed model, transferable authority, TaskContract, or runtime artifact | `schema-contracts` specifies the representation contract and records its vectors; future `model-implementation` implements and tests decoding, construction, provenance binding, typed round trips, serialization, and Schema/model conformance; Phase 4 owns trusted operational replay and authenticity |
| D4 raw worktree-content digest | exact empty, binary regular, executable, and link-target byte vectors reproduce their fixed tagged hashes; stable identity, kind, length, and metadata before/after observation | filtered or EOL-converted bytes; decoded or Unicode-normalized text; dereferenced symlink; unreadable, replaced, raced, truncated, length-inconsistent, or lossy observation; directory, gitlink, or unsupported type | Schema binds `trackedEntry.contentDigest` to one catalog profile; Phase 3 supplies identity-bound raw bytes; Phase 4 replays the same raw profile |
| D5 non-writing contracts | all three non-writing truth-table rows have exactly empty transitions, baseline-equal state postconditions, no lease identity, optional `lease-state: not-required`, and issued-receipt `changedPaths: []`; observed drift is evidence only | exactly 21 Cartesian negatives (`3 × 7`), pairing each non-writing row with each permitted transition branch; any drift-describing postcondition; lease identity/ownership; non-empty changed paths; test/build capability treated as a write override | Schema and Phase 1 static reject the closed contract and compare explicit postconditions with the immutable baseline; Phase 4 enforces empty changed paths and classifies drift as failed or indeterminate verification; the non-empty changed-path case is cross-referenced, not duplicated, by the focused scope family |
| D6 execution/verification biconditional | exactly 13 pairs: `not-attempted/not-performed`; each of `succeeded`, `failed`, `cancelled`, and `indeterminate` with each of `passed`, `failed`, and `indeterminate` | exactly seven pairs: each attempted execution outcome with `not-performed`, plus `not-attempted` with `passed`, `failed`, or `indeterminate` | Phase 1 static applies the unchanged 13/7 biconditional, then the separate final-`E` and final-`V` bindings and not-attempted E/V-empty rules, before the existing lifecycle-precedence table; Phase 4 supplies evidence claims |
| D7 simultaneous transition composition | complete nine-dimension materialized `B`; all seven `from` values bind directly to `B`; unique transitions apply simultaneously; one canonical nine-dimension `F` results regardless of wire order; active operations and administrative locks remain none; changed dimensions have exact `F` postconditions; after valid `F`, ordinary B/F projection derives conservative `Oplan(B,F)` and satisfies both `Oplan(B,F) ⊆ Acap` and `Oplan(B,F) ∩ Qcap = ∅` | baseline/from mismatch; either retired transition; sequential dependency; order-dependent result; non-none active-operation or administrative-lock final state; invalid final composite; missing or mismatched changed-dimension postcondition; drift asserted for an unchanged dimension; incomplete D2 or D3 value; missing or prohibited operation capability as cross-referenced to OC | Phase 1 compares, applies only seven transition types simultaneously, reconstructs and validates all nine dimensions, then derives `Oplan(B,F)` and checks both capability predicates; Phase 3 materializes live-dependent `B`; Phase 4 compares evidence with `F`, attributes transitions and actual effects, and verifies scope/postconditions |
| D8 closed HostOverlay binding and host-resource exclusivity | complete branch and detached records with exactly `roleRef`, `worktreeId`, `repositoryRoot`, `expectedRef`, and non-empty canonical `remoteNames`; every name resolves once; one coherent snapshot proves the complete trusted same-host overlay set, every member validates individually, and all five HX positives pass | each missing field; every unknown field; empty, duplicate, or non-canonical remote names; unknown name; branch without `branchRef`; detached with `branchRef`; `expectedBranch`; each cached observed root/HEAD/branch/remote field; incomplete, missing, ambiguous, untrusted, or mixed-snapshot same-host evidence; all thirteen HX negatives | Schema closes the unchanged five-field record and ref branches; Phase 1 enforces binding identity, unchanged array canon, name resolution, individual resource validity followed by complete snapshot-bound same-host union `worktreeId` and exact-root injectivity, fail-closed completeness and coherence, and static coordination-root exclusion; Phase 3 compares live canonical root, registration, ref, and every named remote and fails closed on physical-worktree or containment ambiguity |
| D9 RoutingPolicy projection equality and complete-set contract | all six required complete-set positive vectors; different priorities; case- or pattern-different matches; sample-equivalent but structurally different patterns; equal match at different priorities reaches its assigned classification | all twelve required complete-set negative vectors, including partial owner, no-fallthrough, same-target tie, collective-role union, split reuse, fallback failure, and TaskContract Domain/role/target mismatch; different IDs with equal `RuleProjection` JCS bytes; same-priority equal `MatchProjection` JCS bytes; non-canonical nested array | `schema-contracts` records projection equality, `Drule`/`Dresolved`/`Owned(R)` semantics, exact Phase 2 order, and vectors; executable projection/JCS comparison belongs to future `model-implementation`; Phase 2 alone resolves and routes the complete set, denies top-priority ambiguity or incomplete ownership, and never falls through or unions roles |
| D10 HostOverlay narrowing proof and canonical structured remotes | exact Project/role consistency; capabilities satisfying `Cportable` and `Cbinding`; all 15 structured-remote positives; repository and remote subsets by exact validated `J(remote)`; all binding names resolve; `src/lib/**` is included within Project `src/**`; broad `**` remains valid but excludes reserved paths | all 61 independent structured-remote negatives; each of the nine exact narrowing rejection-code classes; literal `.git/**`, `.git/config`, `foo/.git/**`, and `foo/.git/config`; added capability or remote; role/project mismatch; `docs/**` outside the Project universe; unsupported syntax, compilation failure, resource exhaustion, or indeterminate emptiness; sample, alias, normalization, ignored field, or prefix heuristic offered as proof; any binding, free capacity, or lease offered to make an incomplete selected owner eligible | Schema enforces the closed record, path profiles, named host/repository profiles, namespace and port rules; Phase 1 rejects literal `.git` components and performs exact lexical, `J(remote)`, set/reference, membership, order, and automata checks relative to revised `U`; only after Phase 2 selects one role that owns all of `Dresolved` may Phase 3 compare the live remote and reject administrative aliases; HostOverlay and runtime state can narrow or deny but never widen routing eligibility |
| D11 digest catalog and golden corpus | Twelve paths, ten computations, two exact copies; exact separators and raw/JCS bytes; unified Source, binding, conditional evidence, complete acquired-R/I and no-lease receipt/delivery values | Included-field mutation, wrong exclusion, self-digest, wrong separator/profile, changed raw bytes, invalid Source hash/copy or conditional projection, delivery identity/copy mismatch | Future model-implementation owns executable codec/hash/replay; Phase 3/4 own production, provenance, ownership, and truth |
| D12 review-only capability complement | exactly four permitted sets: empty, inspect, validate, and inspect-plus-validate; each has `roleClass: review`, only plan-only mode, exact `C − P` prohibited set, and no exclusive write | each of the eleven non-observation capabilities permitted separately; wrong role or mode; missing complement member; permitted/prohibited overlap or other complement error; exclusive write; restoration attempted through another field | Schema and Phase 1 static enforce the complete five-class partition and exact equations; later intersections may only narrow the result and cannot restore a forbidden capability |
| Cross-dimension baselines | complete inventories rather than deltas; index/tracked field equality; gitlink/submodule object equality; tracked/submodule and untracked/ignored disjointness; canonical clean/none versus exact selection | omitted inventory member; index/tracked mode or object mismatch; gitlink/submodule mismatch; tracked/submodule collision; untracked/ignored collision; exact-path collision with explicit index, tracked, or submodule path; a Phase 1 check incorrectly depending on live state | Schema enforces local shape; Phase 1 static enforces relationships over explicit closed data; Phase 3 live owns HEAD-, object-, ignore-, filesystem-, checkout-, and index-dependent checks; Phase 4 evidence reuses the same postcondition semantics |
| Required denial bindings, safe summaries, and five-state correction | Exact controller/evidence binding; state-only origin; unified acquisitionBinding and external Source on acquired paths; no binding/Source on the other states; all A/every-R/every-L compact refs; exact summary/warning/F placement | Four erased-success histories, bad earlier R/L, Source/binding mismatches, state mismatch, forbidden identity duplication in origin or evidence, missing summary, wrong F tuple and all controller defects | Five states and the ten-row lifecycle matrix are exhaustive; schema/static evidence checks confer no operational truth or authority |
| SG-002 numeric profile | every existing canonical-token, field-minimum, and field-maximum vector, with Git stage `0` as its only valid stage | Git stage `1`, `2`, `3`, and `4`; every existing signed, negative-zero, leading-plus, leading-zero, fractional, exponent, unsafe, NaN, Infinity, and field-out-of-range vector | `schema-contracts` specifies the six-field profile, exact bounds, and vectors; future `model-implementation` enforces raw tokens before conversion and proves precision-safe representation/JCS/replay across runtimes; Phase 4 verification requires raw-token replay or the complete validated-representation proof |

The matrix contains 25 logical data rows, independently counted from the table.
It preserves all existing issued-contract and pre-contract outcome vectors,
the normative `T(transition)` definition, and the complete SG-002 vectors. A
future implementation is conformant only when every matrix cell is covered at
its assigned layer; a lower layer MUST NOT claim a live or evidence property
it cannot establish.

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
| Apath / Qpath | every ordinary effect path is in authorized language and outside prohibited language | unauthorized path; prohibited overlap; canonical but out-of-scope earlier path despite a good final member |
| Acap / Qcap | Oplan and Oexec are subsets of Acap and disjoint from Qcap | unauthorized or prohibited create/modify/delete; permitted final operation cannot hide an earlier disallowed operation |
| Oplan(B,F) | simultaneous transitions produce one F; conservative ordinary effects satisfy capability closure | transition requiring a forbidden capability; after-state invented independently of B; administrative operation treated as ordinary |
| Carrier presence | exactly iff issued, writing, attempted; complete zero-effect case is [] | missing carrier on each attempted outcome; carrier on no-lease/non-writing, denial, or not-attempted path |
| Carrier shape/order | closed {path, operations}, non-empty canonical operations, canonical unique paths | extra key, empty/unknown operation, duplicate path/operation, unsorted path/operation |
| EvidencePaths | every carrier path belongs to changedPaths | carrier path missing from changedPaths |
| OexecByPath / Oexec | actual per-path unions and full union retain every listed operation | drop an earlier operation or reconstruct only final records |
| Verification / lifecycle | contained effects plus all passed referenced V and consistent outcomes | out-of-scope effect with passed verification or succeeded lifecycle; a later passed V cannot erase an earlier non-passed V |

Failed/indeterminate verification retains actual out-of-scope evidence; it does not rewrite or suppress the carrier. Oplan is a conservative planned effect set, not a claim that all planned operations actually happened. Exact index/submodule/admin surfaces keep their existing separate owners. These are static synthetic constructions and planned conformance requirements, not runtime enforcement or permission to execute effects.


### Option-B construction verification

Before audit freeze, in-memory synthetic construction checks exercised 45 denial/state/identity cases, the retained 43 scope/OC/OE cases, two issued identity cases, and all 20 independent temporal reversal assignments: 110 checks with the intended dispositions. The checks are disposable document-construction verification, not a repository validator or executable Schema/model test suite. The 31 framed hash cases and 13 completed-object byte cases were independently replayed by Node and PowerShell/.NET. Trusted issuance, runtime observation, acquisition/release truth, and scope attribution remain outside these checks.

Current owner numbers are derived from the row inventories, not inherited aggregate targets. All superseded current representations and count summaries are removed. Historical opening review records and explicitly historical PG-1 attestations retain their original values and meaning.

### Current invariant counts

```text
Schema resources = 11
dispatchable kinds = 7
baseline dimensions = 9
permitted-transition branches = 7
required-postcondition branches = 11
check types = 14
denial checkpoints = 9
ExecutionReceipt spec fields = 17
ExecutionReceipt field-table rows = 16
array-ordering matrix rows = 54
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
expanded affected-family aggregate including receipt/contract binding = 168
digest-bearing paths = 12
digest computations = 10
digest exact-copy paths = 2
numeric fields = 6
host-resource-exclusivity positives = 5
host-resource-exclusivity negatives = 13
```


Current continuous ranges are PB-P/N01..05, AI-P/N01..23, DP-P/N01..13, RF-P/N01..14, CH-P/N01..20, and RC-P/N01..09. Each row in the independent ledger has exactly one positive and one negative owner. Mandatory variants are non-additive. Scope 5/6, OC 3/8, OE 10/11 and other retained inventories are coverage-case counts outside this independently rebuilt aggregate.

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

### SG-001 runtime-structure vectors

Additional planned positive fixtures cover:

- a clean baseline with a valid reference and HEAD plus clean or none state for
  every remaining required dimension;
- a non-empty exact stage-0 index complete inventory and an empty exact
  stage-0 inventory representing removal of all HEAD paths;
- each `trackedEntry` status branch: `clean`, `modified`, `deleted`, and
  `type-changed`;
- absent/unavailable and uninitialized/unavailable submodules, plus
  initialized/observed submodules for all eight Boolean triples and checkout
  IDs both equal to and different from the recorded ID;
- the none-only TaskContract active-operation and administrative-lock baselines
  and optional postconditions, plus every active-operation and
  administrative-lock identity as non-authorizing observation/evidence;
- every one of the seven permitted-transition branches and all eleven
  required-postcondition branches;
- warning records both with and without the optional summary and related check
  fields;
- an issued-contract successful combination, an issued-contract
  denied-before-action combination, and issued-contract failed, cancelled, and
  indeterminate combinations; and
- pre-contract denials at every checkpoint with every permitted
  checkpoint/acquisition-state pair, including an acquired lease whose
  ownership-checked cleanup succeeds, fails, or is indeterminate.

Additional planned negative fixtures cover:

- a missing required baseline dimension, an unknown baseline dimension, and a
  field that is inapplicable to its selected baseline branch;
- a duplicate entry path; index stage `1`, `2`, or `3`; an unsupported mode;
  true `intentToAdd`, `skipWorktree`, or `assumeUnchanged`; a sparse entry; an
  unmerged index; initialized submodule without `checkedOutObjectId`;
  absent/observed, uninitialized/observed, or initialized/unavailable pairing;
  a missing observed Boolean; `indeterminate`; or a superseded
  `worktreeState` field;
- the exact 21-case active-operation legacy family: seven single-operation
  baselines, seven retired transitions, and seven single-operation
  postconditions; separately, duplicate, unknown, non-canonical, and empty-exact
  reusable active-operation observations;
- the exact 21-case administrative-lock legacy family: seven non-empty
  single-lock baselines, seven retired transitions, and seven non-empty
  single-lock postconditions; separately, duplicate identity, missing or
  forbidden branch identifiers, unknown branches, non-canonical order,
  empty-exact arrays, and other malformed reusable observations;
- a transition with identical `from` and `to`, a duplicate transition target,
  an unknown transition type, a missing branch target key, and the retired
  active-operation or administrative-lock branch;
- a duplicate postcondition type, missing or repeated `scope-contained`, and a
  non-none active-operation or administrative-lock postcondition;
- a write contract whose `lease-state` postcondition says `not-required` and
  a plan-only contract whose `lease-state` says `owned`;
- a warning sequence gap or duplicate, duplicate `checkId`, dangling or
  cross-receipt `relatedCheckId`, a delivery-result-only reference, and a check
  sequence gap or duplicate;
- a succeeded lifecycle with an unresolved warning, an issued-contract failed
  or indeterminate release without an unresolved warning, an indeterminate
  acquisition without an unresolved warning, and every outcome combination
  that violates the precedence table; and
- a pre-contract denial with an unlisted checkpoint/acquisition-state pair or
  an impossible execution, verification, release, or lifecycle outcome.

Planned SG-001 conformance rejects branch-inapplicable fields and validates exact path, transition-target, postcondition-type, and check-ID uniqueness before dependent operands are used. It covers the complete Option-B binding, controller/state matrix, all twenty primitive and eleven derived chronology relations, P/E/V outcomes and terminality, scope and operation evidence, release retries, warnings, and exact sanitized terminal F. Preparation constructs selectors; static acceptance precedes receipt digest acceptance; optional delivery follows. Executable Schema/model conformance remains future work.

### SG-002 number-profile vectors

Planned valid numeric vectors cover raw tokens `0`, `1`, and
`9007199254740991`; priority `0` and `1000`; port `1` and `65535`; index
stage `0`; warning and check sequence `0` and `4095`; and `redactionCount`
`0` and `4294967295`.

Planned invalid vectors cover `-0`, `-1`, `+1`, `00`, `01`, `1.0`,
`1.00`, `1e0`, `1E0`, `1e+0`, `1e-1`, `0.1`, `9007199254740992`,
another overlarge integer token, priority `1001`, port `0` and `65536`,
stage `1`, `2`, `3`, and `4`, sequence `4096`, and `redactionCount`
`4294967296`. They also cover integer-equivalent decimal and exponent forms in
every numeric field, overflow and underflow exponent tokens, and
implementation-specific NaN or Infinity tokens wherever a parser exposes such
extensions. The complete numeric instance-field inventory remains exactly six.

Leading-zero forms and other syntactically invalid JSON may fail during JSON
lexical parsing before a profile-specific assertion. They still require
conformance vectors so a permissive parser extension cannot accept them.

Planned SG-002 tests require raw-token-aware rejection before Schema
validation; exact lower and upper bounds; the exact safe-integer maximum; no
precision loss through strict parse, validated canonical instance
representation construction, JCS, or replay; identical digest vectors across
supported runtimes; rejection of a generic decoded object without the complete
representation proof; and official RFC 8785 vectors together with the
project-specific boundaries above. Validator and toolchain research must prove
conformance to this selected profile and MUST NOT choose or weaken it.

## 16. Deferred work

The following remain explicitly deferred:

- validator/package selection, package metadata, dependency lock, provenance and license approval;
- every JSON Schema file, fixture, executable test, parser, validator adapter, static-validation implementation, CI workflow, package, and release;
- typed models, strict decoding, validated canonical representation, canonical serialization, digest projection, JCS, hashing, replay, round trips, Schema/model conformance, and cross-runtime reproduction in the later distinct model worktree;
- Phase 2 task resolution, RoutingPolicy execution, covering-role selection, and context-dependent highest-priority ties;
- Phase 3 live Git/worktree inspection, concrete path containment, runtime coordination, and leases;
- Phase 4 trusted contract issuance/provenance, sanitization, scope verification, receipt generation, and receipt delivery;
- Phase 5 CLI and Phase 6 adapters;
- migration tooling, multi-revision runtime support, and any actual v1alpha2 design;
- an HTTPS Schema namespace unless domain control and permanence are separately demonstrated and approved;
- cryptographic authorization, issuer/key administration, operational recovery, and emergency procedures; and
- integration review, commits, merging, promotion to `main`, worktree creation, and release administration.

## 17. Implementation sequence and gates

The required sequence is:

1. This design document receives an independent read-only audit.
2. The design record is committed only through a separately authorized repository-owner action.
3. `integration-control` decides the validator, package metadata, lock strategy, provenance, licensing compatibility, and release implications.
4. Only after those decisions and a fresh, separately authorized schema-contracts task may Schema resources, synthetic fixtures, and executable contract tests be implemented.
5. The complete Schema baseline then receives independent audit, integration-control approval, commit/review, and integration into `main`.
6. No model worktree may be created until updated `main` contains that complete approved Schema baseline and the repository owner separately creates or binds a distinct `model-implementation` worktree from it.

A design record, resource reservation, valid Schema, successful test, or Phase 1 activation does not activate operational governance or grant execution authority.
