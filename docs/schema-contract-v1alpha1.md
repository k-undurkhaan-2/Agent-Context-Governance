# contextctl.dev/v1alpha1 Schema Contract Design

Phase 1: Schemas and Models is current, but Schema implementation has not begun. The recorded history identifies independent design audit and `integration-control` design approval of the prior candidate as complete, the six earlier review findings as repaired, independently audited, confirmed, replied to, and resolved, the three third-review findings as repaired at commit `9eac3e040a8d0f9c959eeb675eace795749e422a`, the two fourth-review repairs as recorded at commit `b972382fad27a4dda0a4dff945c94b711019ec45`, and the two fifth-review repairs as present at exact commit `a99e57773384c0af4a6531f38aa14bee3781f19d`. The originating `a99e5777...` push transaction remains historically attribution-indeterminate.

The sixth-review documentation repair was committed at exact commit `37e3f373b012050ac424ea7d74c39396196d7da4` after its three-file candidate received independent read-only audit. The exact OpenPGP-signed committed head was independently verified; its single-ref non-force push and remote branch/PR-head confirmation completed; and both sixth-review threads, `PRRT_kwDOThD5p86VKc3R` and `PRRT_kwDOThD5p86VKc3X`, received exactly one owner evidence reply and were resolved.

The seventh Codex review, REST review `4828747866` and GraphQL review `PRR_kwDOThD5p88AAAABH9DYWg`, was submitted `2026-07-31T13:11:51Z` against exact head `37e3f373b012050ac424ea7d74c39396196d7da4` and produced exactly four validated findings in threads `PRRT_kwDOThD5p86VbJ8z`, `PRRT_kwDOThD5p86VbJ83`, `PRRT_kwDOThD5p86VbJ85`, and `PRRT_kwDOThD5p86VbJ89`. This working-tree revision records proposed documentation-only repairs for those four findings. All four seventh-review threads remain unresolved external records with no owner reply.

This candidate awaits independent read-only audit, separate commit authorization, exact committed-head verification, push authorization, remote/PR-head confirmation, GitHub evidence synchronization, re-review, and merge-readiness review. Schema implementation, model implementation, model-worktree creation, and merge remain external and unauthorized. This Markdown neither proves nor replaces external GitHub, audit, or authorization state. No seventh-review thread reply or resolution, PR-body update, review request, Schema implementation, model implementation, or model-worktree action is claimed.

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
| Check outcome | Enum `passed`, `failed`, or `indeterminate` | — | Phase 4 records evidence without turning it into authority |
| Execution outcome | Enum `not-attempted`, `succeeded`, `failed`, `cancelled`, or `indeterminate` | — | Phase 4 derives it from the attempt |
| Verification outcome | Enum `not-performed`, `passed`, `failed`, or `indeterminate` | — | Phase 4 derives it from post-execution verification |
| Release outcome | Enum `not-required`, `succeeded`, `failed`, or `indeterminate` | — | Phase 3 supplies ownership-checked release evidence |
| Lifecycle outcome | Enum `denied`, `succeeded`, `failed`, `cancelled`, or `indeterminate` | Cross-field combinations are structurally bounded | Phase 4 derives the terminal outcome; it does not imply lease release |
| Receipt-delivery outcome | Enum `not-attempted`, `succeeded`, `failed`, or `indeterminate` | — | Phase 4 records the post-finalization delivery attempt separately |
| Scope | Closed `{ capabilities, paths }` with both arrays present; `paths` contains path patterns over the revised valid `repositoryRelativePath` universe | Arrays canonical; allowed/prohibited sets disjoint and containment checked where statically provable; reserved `.git`-component paths are never members of an ordinary scope language | Phases 2–4 calculate effective scope and verify effects, with Git administrative effects outside ordinary path scope |
| Permitted transition | One of exactly seven closed, target-keyed branches defined under `TaskContract`; active-operation and administrative-lock are not contract transitions | Target uniqueness and canonical target order before hashing | Phases 3–4 compare a live transition against immutable baseline authority |
| Required postcondition | One of the eleven closed branches defined under `TaskContract`; `active-operations` and `administrative-locks` expectations are none-only, and no open postcondition name or generic expected record exists | Type uniqueness, required `scope-contained`, and exact nested-state consistency | Phase 4 checks fresh observations after execution |

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
leap-year validity, and comparison of the represented instants under the 14
chronology relations below: the twelve retained relations plus the two
universal final-`P`-to-every-`E` and every-`E`-to-every-`V` timestamp
relations. Future
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

The five current protected literal values from
`2000-01-01T00:00:00Z` through the existing `2000-01-01T00:01:00Z` value,
including all 22 protected occurrences after the golden-receipt repair, remain byte-identical.

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

At initial live preflight and at post-acquisition, pre-contract-issuance
revalidation, a non-empty administrative-lock observation denies contract
issuance. Sanitized pre-contract-denial evidence may retain the exact
observation, but no TaskContract may contain it as a baseline.

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
scope, and actual transition attribution remains Phase 4 verification.

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
against that same universe: a runtime-resolved Git administrative effect makes
the postcondition failed or indeterminate and may not be silently omitted.
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

Every dimension changed by at least one of the seven permitted transitions
requires its matching postcondition from the table, and that postcondition's
`expected` value equals the corresponding canonical projection of `F`. A
postcondition for an unchanged dimension is optional; if present, it equals
the unchanged baseline projection. An optional active-operation postcondition
or administrative-lock postcondition is none-only. `scope-contained` and
`lease-state` retain their independent mandatory rules.

Phase 1 owns explicit closed-data comparison, simultaneous application,
canonical reconstruction, and static final-composite validation. Phase 3 owns
HEAD/live/object/index/filesystem materialization before issuance. Phase 4
compares final evidence with `F`, attributes transitions, and verifies scope
and postconditions.

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

`metadata.id` is the receipt ID and is narrowed to a canonical lower-case UUID. The common required `spec` fields are:

| Field | Design |
| --- | --- |
| `receiptVersion` | Constant string `1` |
| `taskId` | Canonical UUID |
| `origin` | One closed discriminated union branch, `issued-contract` or `pre-contract-denial` |
| `executionOutcome` | Shared execution outcome |
| `verificationOutcome` | Shared verification outcome |
| `releaseOutcome` | Shared release outcome |
| `lifecycleOutcome` | Shared overall lifecycle outcome |
| `unresolvedCoordinationWarnings` | Append-only sequenced sanitized warnings |
| `checks` | Append-only sequenced check evidence with expected/observed sanitized summaries and reason codes |
| `changedPaths` | Canonical repository-relative path set |
| `reasonCodes` | Canonical reason-code set |
| `sanitization` | Closed required `profileId`, `applied`, `redactionCount`, and `completedAt` record |
| `receiptDigest` | `profile.digest.execution-receipt-v1` over the complete `ExecutionReceipt` resource excluding only `spec.receiptDigest`, exactly as cataloged in section 10 |
| `startedAt` / `finishedAt` | Canonical UTC timestamps |

Every `changedPaths` member is a valid actual repository-relative path from the
revised universe. A runtime-resolved Git administrative effect cannot appear as
a successful ordinary member, cannot be omitted while claiming successful
`scope-contained` verification, and instead requires failed or indeterminate
scope evidence.

`spec.origin` is exactly one of these closed branches:

- **`issued-contract`:** requires `type` fixed to `issued-contract`, `contractId`, `contractDigest`, `resolvedTarget`, and `effectiveMode`. `resolvedTarget` contains the Project, role, logical worktree, and complete canonical Domain references. This branch represents every receipt produced after a trusted contract was issued. It forbids `denialCheckpoint`, `preContractEvidence`, and `leaseAcquisition`.
- **`pre-contract-denial`:** requires `type` fixed to `pre-contract-denial`, `denialCheckpoint`, `preContractEvidence`, and `leaseAcquisition`. It forbids `contractId`, `contractDigest`, `resolvedTarget`, and `effectiveMode`, so it cannot fabricate a contract or claim a fully authorized target.

`denialCheckpoint` is a closed vocabulary containing exactly `intent-validation`, `project-domain-resolution`, `role-routing`, `host-binding`, `initial-preflight`, `lease-acquisition`, `post-acquisition-revalidation`, and `contract-issuance`. It contains no checkpoint that occurs only after contract issuance.

`preContractEvidence` is a closed sanitized record requiring `observedAt`, a
tagged `evidenceDigest` bound only to the exact
`profile.digest.pre-contract-evidence-v1` catalog projection, a non-empty
canonical `reasonCodes` set, and a bounded `sanitizedSummary`. Together with
the receipt's ordered `checks`, it records enough evidence to explain the
denial without asserting contract authority. It has no issuer, contract,
absolute-host-path, secret, or authority-grant field. Structural validation
cannot prove arbitrary summary text safe; Phase 4 sanitization and external
controls remain required.

`leaseAcquisition` is one closed discriminated union with these states:

- `not-required`, `not-attempted`, `not-acquired`, and `indeterminate` each contain only their fixed `state` discriminator and therefore forbid `leaseId` and acquisition-result binding fields;
- `acquired` requires `state` fixed to `acquired`, a canonical `leaseId`, and
  `acquisitionResultDigest` bound only to the exact
  `profile.digest.lease-acquisition-result-v1` catalog projection.

The states have these exact lifecycle meanings:

- `not-required` means the control plane determined before denial that the task did not require a write lease;
- `not-attempted` means a write lease would have been required, but denial occurred before an acquisition attempt;
- `not-acquired` means required acquisition was attempted and conclusively produced no task-owned lease;
- `indeterminate` means acquisition was attempted but race, malformed state, ambiguous ownership, or another uncertainty prevents proving whether a lease exists; it asserts no lease identity and leaves coordination state blocking; and
- `acquired` means acquisition produced the task-owned lease bound by `leaseId` and `acquisitionResultDigest`, and denial occurred later.

`denialCheckpoint` and `leaseAcquisition.state` form this closed chronology table:

| `denialCheckpoint` | Permitted `leaseAcquisition.state` |
| --- | --- |
| `intent-validation` | `not-required` or `not-attempted` |
| `project-domain-resolution` | `not-required` or `not-attempted` |
| `role-routing` | `not-required` or `not-attempted` |
| `host-binding` | `not-required` or `not-attempted` |
| `initial-preflight` | `not-required` or `not-attempted` |
| `lease-acquisition` | `not-acquired` or `indeterminate` |
| `post-acquisition-revalidation` | `not-required` or `acquired` |
| `contract-issuance` | `not-required` or `acquired` |

Every pair not listed is invalid. In particular, an acquired lease cannot be claimed before post-acquisition revalidation, and a conclusive failure or indeterminate acquisition is recorded at `lease-acquisition`, not at a later checkpoint.

Acquisition is concurrency evidence, never proof of authority. The exact
pre-contract release and lifecycle relationships are defined under outcome
consistency below.

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

No new receipt or contract digest expresses these relationships. Conformance
does not add equality rules for values that the receipt does not duplicate,
including `requestedMode`, `allowWrite`, `leaseId`, scope,
`contractVersion`, freshness, or expected baseline. Existing local receipt
and contract invariants remain independently required.

Static conformance applies this exact artifact-dependency order:

1. Strictly decode and structurally validate the complete receipt and complete
   referenced TaskContract under the selected Schema revision.
2. Apply each artifact's local Phase 1 static checks and canonical-array checks.
3. Validate the complete TaskContract and its existing derivation
   prerequisites.
4. Recompute the complete `profile.digest.task-contract-v1` digest over the
   exact validated TaskContract projection.
5. Compare `contractDigest`, `contractId`, receipt `taskId`, the complete
   `resolvedTarget`, and `effectiveMode`.
6. Apply all applicable cross-artifact chronology, including the strict
   attempted-execution pre-action freshness relation and the universal
   final-`P`-to-every-`E` and every-`E`-to-every-`V` timestamp relations,
   against that same referenced contract.
7. Apply greatest-sequence `P` and `V` selection, required P/E/V presence,
   universal sequence ordering, final-`V` outcome binding, receipt outcome,
   release, non-writing, and other cross-field consistency checks.
8. Only after every preceding check succeeds, compute and verify or accept the
   receipt's `profile.digest.execution-receipt-v1` value.
9. Only after receipt finalization validate a `ReceiptDeliveryResult`,
   including exact receipt-ID binding, exact finalized receipt-digest copy,
   and delivery chronology.

Any cross-artifact mismatch makes the issued-contract receipt invalid before
receipt-digest acceptance. A mismatch is not a valid denial receipt, a receipt
outcome, a recoverable alias, permission to switch contracts, or permission to
rewrite duplicated claims. Validators do not normalize or repair it.

Required future positive issued-receipt vectors cover:

1. a matching plan-only TaskContract and issued-contract receipt pair;
2. a matching implementation-mode TaskContract and issued-contract receipt
   pair for which every other requirement is valid;
3. a matching multi-Domain pair proving exact complete `domainRefs` equality;
4. a pair with exact Project, role, worktree, task, contract, digest, and mode
   equality; and
5. a valid matching pair followed by a correctly bound
   `ReceiptDeliveryResult`.

Required future negative issued-receipt vectors independently alter and reject:

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
12. a correct contract digest paired with incorrect duplicated claims;
13. matching duplicated claims paired with a wrong contract digest;
14. matching duplicated claims paired with a digest from another complete
    contract;
15. matching `contractId` but another contract body;
16. receipt-digest acceptance attempted before cross-artifact equality;
17. attempted reinterpretation of the mismatch as `pre-contract-denial`; and
18. a delivery result bound to another receipt ID or digest.

Every negative vector rejects before receipt-digest acceptance. The
`schema-contracts` role specifies these equality, dependency-order, and
expected-vector requirements. Future `model-implementation` owns executable
strict decoding, projection, hashing, and cross-artifact tests. Phase 4 verifies
trusted issuer provenance, authenticity, current authority and preconditions,
and whether evidence is truthful. Digest equality alone establishes neither
authenticity nor authority.

`sanitization` is a closed record with exactly four required fields:
`profileId: profileIdentifier`, `applied: boolean`,
`redactionCount: integer` from 0 through 4294967295 under the numeric profile,
and `completedAt: timestamp`. These are evidence claims only; structural
validity does not prove that sanitization was complete.

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
| `outcome` | required shared `checkOutcome` |
| `observedAt` | required shared timestamp |
| `profileId` | required `profileIdentifier` |
| `expectedSummary` | optional `sanitizedSummary` |
| `observedSummary` | optional `sanitizedSummary` |
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
contract-issuance
pre-action-revalidation
execution
post-execution-verification
lease-release
receipt-finalization
```

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

#### Issued-contract final applicable pre-action and verification checks

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
outcomes; the unique greatest-sequence member is final and controls the
receipt-level verification outcome.

Phase 1 static conformance requires:

```text
for every p in P where p.outcome == "passed":
  p.observedAt < TaskContract.spec.freshness.expiresAt

if attempted:
  count(P) >= 1
  count(E) >= 1
  count(V) >= 1
  finalApplicablePreActionCheck.outcome == "passed"
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

if executionOutcome == "not-attempted":
  count(V) == 0
```

The expiry boundary is strict. Equality at expiry and any later passed check
are invalid, including in a `not-attempted` receipt. Earlier failed or
indeterminate pre-action checks may coexist with attempted execution only when
the final applicable check is passed and strictly pre-expiry. An earlier
passed/pre-expiry check followed by a final failed or indeterminate check makes
every attempted-execution outcome invalid before receipt-digest acceptance.

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

A final passed pre-action check may occur exactly at the permitted
issuance-side lower bound, subject to the existing
`freshness.issuedAt <= ExecutionReceipt.startedAt` and
`startedAt <= checks[].observedAt` relations. It may also occur at the last
valid whole second before expiry. `startedAt` is not proof of action freshness.
Receipt completion, verification, sanitization, release, finalization, and
delivery may occur after expiry; `finishedAt <= freshness.expiresAt` is not a
rule.

A `not-attempted/not-performed` receipt may contain neither a pre-action check
nor an execution check and may retain failed or indeterminate denial evidence
observed at or after expiry. Every passed pre-action check, when present, must
still be strictly pre-expiry, but no final-passed or execution-check presence
requirement applies. Its verification set `V` must be empty; any stray
verification check is invalid. No exactly-one-check rule, global check-type
uniqueness, requirement that execution checks form one contiguous region, or
requirement of exactly one verification check is introduced. The repair also
introduces no new check kind, timestamp, checkpoint field, trusted-clock
semantics, or evidence-truth claim.

The complete attempted evidence chain is:

```text
by sequence:
  final applicable P < every E < every V

by timestamp:
  final applicable P <= every E <= every V
```

The greatest-sequence selections and the two strict sequence comparisons are
sequence/outcome consistency invariants. The two universal timestamp
comparisons are chronology relations, increasing the exact total from 12 to
14.

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
8. earlier failed and/or indeterminate checks followed by a final
   passed/pre-expiry check and then an execution check.

Every attempted-execution member of these eight positive classes contains at
least one `execution` check after the final applicable passed/pre-expiry
pre-action check.

The 33 required focused negative classes are the existing 25 classes plus
exactly eight execution-presence and ordering classes:

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
    final applicable pre-action check.

Duplicate sequence, sequence gap, duplicate check ID, and other generic
check-array failures remain in their existing families and do not inflate this
33-class focused total.

Earlier failed or indeterminate checks followed by a final passed/pre-expiry
check remain valid. Phase 1 checks only the internal claims in the complete
artifact pair. Phase 4 retains trusted-current-time evaluation, timestamp
authenticity, actual immediacy, evidence truth, and operational freshness
enforcement.

#### Focused post-execution-verification vectors

This named family is separate from the focused pre-action family and from D6.
The ten required non-overlapping positive classes are exactly:

1. `succeeded/passed` with one valid `E` and one later `V`;
2. `failed/passed` with one valid `E` and one later `V`;
3. `cancelled/passed` with one valid `E` and one later `V`;
4. `indeterminate/passed` with one valid `E` and one later `V`;
5. `succeeded/failed` with the final `V` outcome `failed`;
6. `succeeded/indeterminate` with the final `V` outcome `indeterminate`;
7. valid `E`/`V` timestamp equality at whole-second precision;
8. multiple `E` members, all preceding one `V` by sequence and timestamp;
9. multiple `V` members after all `E` members, with an earlier `failed` or
   `indeterminate` `V` followed by a final `passed` `V`; and
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
14. final `V` `failed` with receipt `verificationOutcome: passed`;
15. final `V` `failed` with receipt `verificationOutcome: indeterminate`;
16. final `V` `indeterminate` with receipt `verificationOutcome: passed`;
17. final `V` `indeterminate` with receipt `verificationOutcome: failed`;
18. `not-attempted/not-performed` with one stray `V` whose outcome is `passed`;
19. `not-attempted/not-performed` with one stray `V` whose outcome is `failed`;
    and
20. `not-attempted/not-performed` with one stray `V` whose outcome is
    `indeterminate`.

Case 12 proves greatest-sequence final selection because an earlier `V` matches
the receipt while the later final `V` does not. Generic sequence gaps,
duplicate sequences, duplicate check IDs, and malformed check arrays remain
outside this 10/20 family. The focused pre-action family remains 8/33, and D6
remains 13 valid and 7 invalid receipt-level combinations.

#### Timestamp chronology

All comparisons in this section operate on the instants represented by the
validated `canonicalUtcTimestamp` strings. Equality remains allowed for every
earlier comparison except the existing strict issuance freshness boundary; the
new passed pre-action freshness relation is also strict.

| Artifact or validation context | Required chronology | Equality |
| --- | --- | --- |
| `TaskContract` issuance checkpoint | `issuanceCheckpoint.observedAt <= freshness.issuedAt` | Allowed |
| `TaskContract` freshness | `freshness.issuedAt < freshness.expiresAt` | Forbidden; this relation remains strict |
| Every `ExecutionReceipt` | `startedAt <= sanitization.completedAt` | Allowed |
| Every `ExecutionReceipt` | `sanitization.completedAt <= finishedAt` | Allowed |
| Derived receipt relation | `startedAt <= finishedAt` | Allowed; follows from the two preceding relations |
| Every `checks[]` member | `startedAt <= checks[].observedAt` | Allowed |
| Every `checks[]` member | `checks[].observedAt <= sanitization.completedAt` | Allowed |
| `pre-contract-denial` origin | `startedAt <= preContractEvidence.observedAt` | Allowed |
| `pre-contract-denial` origin | `preContractEvidence.observedAt <= sanitization.completedAt` | Allowed |
| `issued-contract` receipt validated with its complete referenced `TaskContract` | `TaskContract.freshness.issuedAt <= ExecutionReceipt.startedAt` | Allowed |
| `issued-contract` receipt validated with its complete referenced `TaskContract`, for every passed `p` in `P` | `p.observedAt < TaskContract.freshness.expiresAt` | Forbidden; strict for every passed pre-action check |
| Attempted `issued-contract` receipt, for the final applicable `P` and every `e` in `E` | `finalApplicablePreActionCheck.observedAt <= e.observedAt` | Allowed; universal over every execution check |
| Attempted `issued-contract` receipt, for every `e` in `E` and every `v` in `V` | `e.observedAt <= v.observedAt` | Allowed; universal over every execution/verification pair |
| Closed receipt and `ReceiptDeliveryResult` pair | `ExecutionReceipt.finishedAt <= ReceiptDeliveryResult.attemptedAt` | Allowed |

Check timestamps need not be strictly increasing between adjacent checks, and
timestamps of unrelated checks need not follow check-type order. The two
mandatory cross-type chronology relations nevertheless require final
applicable `P <= every E <= every V` by timestamp for attempted receipts.
Receipt completion need not occur before contract expiry:
`finishedAt <= freshness.expiresAt` is not a rule, and expiry evaluation
against trusted current time remains Phase 4. Timestamp syntax alone does not
prove truth, Phase 1 does not use a trusted clock, and timestamp ordering grants
no authority.

The greatest-sequence selections, final-passed requirement, check-presence
requirements, and strict check-sequence comparisons are sequence/outcome
consistency invariants and do not add timestamp relations. The two universal
cross-type timestamp comparisons add exactly two chronology relations, so the
chronology relation count is exactly 14.

JSON Schema owns timestamp field types, required presence, the exact
`canonicalUtcTimestamp` pattern, and asserted `format: date-time`. Phase 1
static validation owns calendar validity, all 14 chronology relations above,
the complete-contract/receipt comparison, and the closed
receipt/delivery-result comparison. Phase 4 owns
trusted-clock evaluation,
timestamp authenticity, operational freshness, and whether each recorded event
actually occurred at the stated instant.

Required positive vectors cover strict progression; all-equality boundaries
within each applicable earlier artifact combination while both strict
freshness relations remain strict; each permitted equality boundary
independently, including the two new whole-second cross-type equalities; both
receipt origins; empty and populated `checks` arrays; the eight focused
pre-action positive classes; the ten focused post-execution-verification
positive classes; and complete issued-contract/contract and
receipt/delivery-result pairs. Required negative vectors reverse each of the 14
chronology relations independently, including a check before `startedAt` or
after sanitization completion, pre-contract evidence before `startedAt` or
after sanitization completion, an issuance checkpoint after `issuedAt`, an
issued-contract receipt beginning before contract issuance, a final applicable
`P` timestamp after any `E`, any `V` timestamp before any `E`, and a delivery
attempt before receipt completion. They also cover the 33 focused pre-action
and 20 focused post-execution-verification negative classes. One violating
member invalidates the universal relation even when a later member is valid.
Existing equal and reversed issuance freshness boundaries remain required
negatives.

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
binding requires `verificationOutcome` to equal the outcome of the unique
greatest-sequence member of `V`. Earlier `V` outcomes may differ and do not
control the receipt. A `not-attempted/not-performed` receipt requires `V` to be
empty. These rules do not change the D6 table. Only after D6, final-`V` binding,
and the other P/E/V checks succeed is the existing lifecycle-precedence table
below applied; its precedence is otherwise unchanged.

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
`succeeded` or `not-required`, and
`unresolvedCoordinationWarnings` is empty. If those three component outcomes
have the successful values but unresolved coordination warnings are non-empty,
the required lifecycle outcome is `indeterminate`, never `succeeded`.

Additional issued-contract consistency rules are:

- `executionOutcome: succeeded` MUST NOT combine with
  `verificationOutcome: not-performed`;
- `executionOutcome: not-attempted` requires
  `verificationOutcome: not-performed`;
- `lifecycleOutcome: succeeded` forbids unresolved coordination warnings;
- `releaseOutcome` of `failed` or `indeterminate` requires at least one
  unresolved coordination warning;
- `releaseOutcome: not-required` is required if and only if the referenced
  contract has `leaseRequired: false`;
- `releaseOutcome` of `succeeded`, `failed`, or `indeterminate` is valid
  only when the referenced contract has `leaseRequired: true` and the ordered
  check evidence records successful lease acquisition; and
- release/contract consistency is a Phase 1 cross-artifact static check against
  the referenced contract and its digest when full conformance is claimed;
  Schema shape alone cannot prove acquisition or the evidence claims true.

For a `pre-contract-denial` receipt:

- `executionOutcome` is `not-attempted`,
  `verificationOutcome` is `not-performed`, and `changedPaths` is empty;
- if `releaseOutcome` is `failed`, `lifecycleOutcome` is `failed`;
- else if `releaseOutcome` is `indeterminate`, `lifecycleOutcome` is
  `indeterminate`;
- otherwise `lifecycleOutcome` is `denied`;
- `lifecycleOutcome` MUST NOT be `succeeded` or `cancelled`;
- `leaseAcquisition.state: acquired` requires `releaseOutcome` to be
  `succeeded`, `failed`, or `indeterminate`; failed or indeterminate cleanup
  also requires at least one unresolved coordination warning;
- `leaseAcquisition.state: indeterminate` requires `releaseOutcome` and
  `lifecycleOutcome` to be `indeterminate` and requires at least one unresolved
  coordination warning; and
- `not-required`, `not-attempted`, and `not-acquired` lease states require
  `releaseOutcome: not-required`.

These are deterministic Phase 1 consistency checks over evidence claims. They
do not prove that checks occurred, a summary is safe, or an outcome is true.
Receipt finalization occurs only after `releaseOutcome` is known. Future policy
may require a pre-contract-denial receipt, but it remains optional unless that
policy does so. Receipt delivery remains the separate post-finalization
`ReceiptDeliveryResult`. A receipt grants no authority, cannot authorize a
later task, does not imply lease release, and remains host-local evidence
outside portable governance.

### Cross-finding validation-order application

The accumulated review repairs apply the existing universal twelve-step pipeline and its
artifact dependency graph in this effective order; this is not a replacement
for, alteration of, or second normative pipeline:

1. strict byte/token decoding prerequisites;
2. timestamp and structured-remote lexical validation;
3. JSON Schema structural validation;
4. local Phase 1 static invariants;
5. canonical-array and remote-order validation;
6. validated canonical representation construction;
7. digest projection and digest computation where applicable;
8. complete TaskContract digest verification;
9. issued receipt/TaskContract field equality;
10. cross-artifact chronology, final-applicable `P` and `V` selection,
    attempted P/E/V presence, universal sequence and timestamp ordering,
    final-`V` outcome binding, and outcome consistency;
11. receipt digest verification; and
12. delivery-result binding and chronology.

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

## 10. Non-mutating validation and canonicalization pipeline

Validation, canonicalization, hashing, and verification use these twelve
ordered steps:

1. Accept strict UTF-8 JSON bytes and begin strict JSON tokenization. Reject a
   BOM, malformed UTF-8, invalid Unicode scalar data, and non-JSON tokens.
2. As each numeric token is recognized, validate its raw bytes against
   `0|[1-9][0-9]*` and the `9007199254740991` universal ceiling before
   ordinary numeric conversion and before duplicate-key-complete object
   construction. Then apply the exact declared field bound.
3. During the same strict parse, detect duplicate object-member names before a
   normal object representation can discard them. Raw numeric-token validation
   and duplicate-key detection are parser responsibilities; neither is
   deferred to JSON Schema, and either failure prevents creation of a valid
   decoded instance.
4. Inspect every decoded member name and string value. Reject anything not
   already Unicode NFC; do not normalize or rewrite it.
5. Perform structural validation against one explicitly selected schema-set
   revision using the fixed offline registry and mandatory format-assertion
   profile.
6. Perform Phase 1 static validation, including closed-bundle references,
   uniqueness, restrictions, local contradictions, field-specific numeric
   bounds, identifier canonicality, and outcome consistency.
7. Verify that every array already has the canonical order in section 11 and
   that evidence sequences are contiguous. Reject non-canonical order; do not
   sort.
8. Construct the internal `validated canonical instance representation`
   defined below, binding the immutable value and completed proof to the
   selected Schema and original bytes or same-process provenance.
9. Construct the exact field-bound digest projection from the profile catalog
   below without mutating the immutable source value.
10. Serialize that unchanged projection with RFC 8785 JSON Canonicalization
   Scheme.
11. Hash the exact JCS UTF-8 bytes with SHA-256 and encode the result as
    `sha256:` followed by lower-case hexadecimal.
12. Verification repeats the same pipeline and compares the result; it does
    not repair, normalize, sort, migrate, or infer prior parser compliance.

The `validated canonical instance representation` is an internal,
non-serializable record containing exactly:

1. the immutable closed JSON value;
2. the selected schema-set revision and exact root Schema `$id`;
3. proof that strict UTF-8, duplicate-key, raw-number-token, NFC, JSON Schema,
   Phase 1 static-invariant, and canonical-array checks all passed; and
4. retained original bytes or same-process provenance that binds that proof to
   the same immutable value.

A caller-created or generic decoded object cannot claim this status. The
representation is not a public kind, production typed model, transferable
authority, `TaskContract`, or runtime artifact. Static replay of a digest from
it establishes integrity only and does not establish trusted issuance or
operational authenticity.

The twelve steps above are unchanged normative requirements, with these
non-overlapping responsibilities:

| Responsibility | Owned result |
| --- | --- |
| `schema-contracts` | Specifies the pipeline and validated-representation contract, digest projection catalog and framing, recorded canonical bytes and digests, structural JSON Schema constraints, static invariants over already-decoded closed values, and expected positive and negative vectors. It does not implement or claim executable coverage for the decoder, representation, projection, JCS, hashing, replay, round trips, or cross-runtime behavior. |
| future distinct `model-implementation` | Implements and tests strict UTF-8/token decoding, duplicate-key and raw-number rejection, NFC checks, immutable validated canonical representation and provenance binding, typed models, canonical serialization, exact digest projection, RFC 8785 JCS, SHA-256 framing and verification, replay, typed round trips, Schema/model conformance, and cross-runtime reproduction of the recorded bytes and digests. |
| `integration-control` | Independently reviews and approves the Schema baseline, validator/toolchain, dependency, packaging, licensing, release, and cross-worktree gates; it does not absorb either implementation role. |
| Phase 4 trusted operational path | Replays the same profiles against trusted issuer provenance, current policy/runtime/lease state, contract authority and binding, execution evidence, receipt finalization, and delivery. |

Digest equality establishes integrity only. It is not proof of trusted
issuance, authenticity, freshness, authorization, or operational authority.
The future model work remains blocked until the complete Schema baseline is
independently audited, approved through `integration-control`, committed,
reviewed, and integrated into `main`, after which the repository owner must
separately create or bind a distinct model worktree from that updated `main`.
This design task neither creates that worktree nor authorizes Schema or model
implementation.

Every accepted integer token is exactly representable under binary64, and RFC
8785 serialization emits its canonical number representation without
precision rounding. No negative-zero normalization is needed because `-0` is
rejected. No fraction or exponent normalization is needed because those token
forms are rejected. Verification repeats raw-token validation whenever the
original JSON bytes are available. If verification begins from a
`validated canonical instance representation`, its retained same-process proof
must include successful validation under `profile.number.v1alpha1-r1` and bind
that proof to the immutable value. A generic decoded object without that proof
is insufficient for digest verification.

There is no silent Unicode normalization, array sorting, numeric
normalization, or migration during loading, hashing, contract verification, or
receipt verification. JCS sorts object property names but preserves string
values and array order. A future formatter or migrator, if authorized, is a
separate explicit operation that emits a new value and submits it to the
complete pipeline from step 1.

### Complete digest-profile catalog

The design contains exactly eleven digest-valued field paths and ten
independent digest computations. Every field is bound to exactly one profile;
an instance cannot choose or substitute a profile. The universal framing is:

```text
separator(profile) =
  ASCII("contextctl.dev") || NUL ||
  ASCII("v1alpha1-r1") || NUL ||
  ASCII(profile identifier) || NUL

taggedDigest =
  sha256: || lowercaseHex(
    SHA256(separator(profile) || payloadBytes)
  )
```

For a JCS profile, `payloadBytes` is the UTF-8 encoding of the exact RFC 8785
JCS projection. For a raw profile, it is the exact source bytes. A digest in
any row establishes integrity only; it never establishes issuer provenance,
trusted authenticity, authorization, or that an evidence claim is true.

| Exact field path | Exact profile and payload kind | Exact protected value and included fields | Exact exclusions | Byte construction, replay source, and lifecycle phase |
| --- | --- | --- | --- | --- |
| `trackedEntry.contentDigest` | `profile.digest.worktree-content-v1`; raw | Exact D4 regular-file bytes or symlink-target bytes | Path, mode, Git object ID, filters, decoded text, directories, gitlinks | `separator(profile) || rawBytes`; stable Phase 3 observation and Phase 4 verification |
| `TaskContract.spec.issuer.derivationDigest` | `profile.digest.contract-derivation-v1`; JCS | Complete `TaskContract` resource, including identity, every source digest, target, scope, baseline, transitions, postconditions, lease fields, issuance checkpoint, and freshness | Only `issuer.derivationDigest` | `separator(profile) || UTF8(JCS(projection))`; validated representation and issuance/provenance replay in Phase 4 |
| `TaskContract.spec.digests.policyDigest` | `profile.digest.policy-selection-v1`; JCS | Closed `{project, domains, worktreeRole, routingPolicy}` containing the complete selected Project, complete canonically ordered resolved Domain resource set, selected WorktreeRole, and selected RoutingPolicy | HostOverlay and all runtime state | Same framed JCS construction; authoritative configuration snapshot used for issuance and Phase 4 verification |
| `TaskContract.spec.digests.configurationDigest` | `profile.digest.configuration-snapshot-v1`; JCS | Closed `{governanceBundle, hostOverlay}` containing the complete GovernanceBundle used for resolution and complete selected HostOverlay | Secrets, leases, contracts, receipts | Same framed JCS construction; validated configuration source used for issuance and verification |
| `TaskContract.spec.digests.taskIntentDigest` | `profile.digest.task-intent-bytes-v1`; raw | Exact original strict UTF-8 task-intent bytes | BOM, normalization, trimming, line-ending conversion, JCS, semantic interpretation | `separator(profile) || originalBytes`; retained original intent bytes at issuance and verification |
| `TaskContract.spec.issuanceCheckpoint.stateDigest` | `profile.digest.issuance-state-v1`; JCS | Closed `{repositoryIdentity, target, expectedBaseline, observedAt}` using the contract values and `issuanceCheckpoint.observedAt` | `stateDigest` itself and every other contract field | Same framed JCS construction; issuance-checkpoint representation and Phase 4 replay |
| `ExecutionReceipt.spec.origin[type=issued-contract].contractDigest` | `profile.digest.task-contract-v1`; JCS | Complete `TaskContract` resource including `issuer.derivationDigest` | Nothing | Same framed JCS construction; referenced trusted contract bytes during receipt binding and verification |
| `ExecutionReceipt.spec.origin[type=pre-contract-denial].preContractEvidence.evidenceDigest` | `profile.digest.pre-contract-evidence-v1`; JCS | Closed `{taskId, denialCheckpoint, preContractEvidence}` with all evidence members other than its digest | Only `preContractEvidence.evidenceDigest`; receipt checks and later receipt fields are outside the protected value | Same framed JCS construction; retained pre-contract evidence in Phase 4 |
| `ExecutionReceipt.spec.origin[type=pre-contract-denial].leaseAcquisition[state=acquired].acquisitionResultDigest` | `profile.digest.lease-acquisition-result-v1`; JCS | Closed `{taskId, denialCheckpoint, leaseAcquisition:{state:acquired,leaseId}}` | Only `acquisitionResultDigest` and every other receipt field | Same framed JCS construction; acquisition-result evidence from Phase 3, bound in Phase 4 |
| `ExecutionReceipt.spec.receiptDigest` | `profile.digest.execution-receipt-v1`; JCS | Complete `ExecutionReceipt` resource | Only `spec.receiptDigest`; `ReceiptDeliveryResult` occurs after finalization and is outside the receipt | Same framed JCS construction; validated receipt representation at Phase 4 finalization and replay |
| `ReceiptDeliveryResult.receiptDigest` | `profile.digest.execution-receipt-v1`; exact copy, no additional computation | The referenced finalized receipt's already-computed `ExecutionReceipt.spec.receiptDigest` | The delivery result is never included in or rehashed as the receipt | Exact tagged-string equality with the referenced receipt and receipt ID after finalization; the same execution-receipt profile remains the sole binding |

The computation dependency graph is acyclic. Policy, configuration, raw intent,
and issuance-state values precede contract derivation; the full contract then
precedes the receipt's contract binding; the full receipt is finalized last.
Worktree content, pre-contract evidence, and lease-acquisition-result
computations are independent leaves. The delivery result copies the finalized
receipt digest and adds no computation.

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
| `profile.digest.lease-acquisition-result-v1` | `636f6e7465787463746c2e646576007631616c706861312d72310070726f66696c652e6469676573742e6c656173652d6163717569736974696f6e2d726573756c742d763100` |
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

#### `profile.digest.pre-contract-evidence-v1` payload and completion

```json
{"denialCheckpoint":"post-acquisition-revalidation","preContractEvidence":{"observedAt":"2000-01-01T00:00:00Z","reasonCodes":["reason.synthetic.denied"],"sanitizedSummary":"Synthetic denial."},"taskId":"00000000-0000-4000-8000-000000000001"}
```

The exact completed source value, proving the sole excluded member, is:

```json
{"denialCheckpoint":"post-acquisition-revalidation","preContractEvidence":{"evidenceDigest":"sha256:db7c19635103fc202ab07f4d9e2eb3686cf0046bba8c79887a7aabfd0e72be20","observedAt":"2000-01-01T00:00:00Z","reasonCodes":["reason.synthetic.denied"],"sanitizedSummary":"Synthetic denial."},"taskId":"00000000-0000-4000-8000-000000000001"}
```

#### `profile.digest.lease-acquisition-result-v1` payload and completion

```json
{"denialCheckpoint":"post-acquisition-revalidation","leaseAcquisition":{"leaseId":"00000000-0000-4000-8000-000000000004","state":"acquired"},"taskId":"00000000-0000-4000-8000-000000000001"}
```

The exact completed source value, proving the sole excluded member, is:

```json
{"denialCheckpoint":"post-acquisition-revalidation","leaseAcquisition":{"acquisitionResultDigest":"sha256:1aeb432f3667229535829959d6a1bcb463472150a31eb999aaf058423f65b244","leaseId":"00000000-0000-4000-8000-000000000004","state":"acquired"},"taskId":"00000000-0000-4000-8000-000000000001"}
```

#### `profile.digest.execution-receipt-v1` payload

The exact digest projection excludes only `spec.receiptDigest`:

```json
{"apiVersion":"contextctl.dev/v1alpha1","kind":"ExecutionReceipt","metadata":{"id":"00000000-0000-4000-8000-000000000003"},"spec":{"changedPaths":[],"checks":[{"checkId":"check.pre-action-revalidation","checkType":"pre-action-revalidation","observedAt":"2000-01-01T00:00:01Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":0},{"checkId":"check.execution","checkType":"execution","observedAt":"2000-01-01T00:00:02Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":1},{"checkId":"check.post-execution-verification","checkType":"post-execution-verification","observedAt":"2000-01-01T00:00:02Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":2}],"executionOutcome":"succeeded","finishedAt":"2000-01-01T00:00:02Z","lifecycleOutcome":"succeeded","origin":{
"contractDigest":"sha256:238c3af3ceab3eafc70d660b6e3d5cef97c3741d48b76c49e9e998a26d8afe30","contractId":"00000000-0000-4000-8000-000000000002","effectiveMode":"plan-only","resolvedTarget":{"domainRefs":[{"apiVersion":"contextctl.dev/v1alpha1","id":"domain.invalid","kind":"Domain"}],"projectRef":{"apiVersion":"contextctl.dev/v1alpha1","id":"project.invalid","kind":"Project"},"worktreeId":"worktree.invalid","worktreeRoleRef":{"apiVersion":"contextctl.dev/v1alpha1","id":"role.invalid","kind":"WorktreeRole"}},"type":"issued-contract"},
"reasonCodes":[],"receiptVersion":"1","releaseOutcome":"not-required","sanitization":{"applied":true,"completedAt":"2000-01-01T00:00:02Z","profileId":"profile.sanitization.v1","redactionCount":0},"startedAt":"2000-01-01T00:00:01Z","taskId":"00000000-0000-4000-8000-000000000001","unresolvedCoordinationWarnings":[],"verificationOutcome":"passed"}}
```

The exact completed receipt, proving the sole excluded member, is:

```json
{"apiVersion":"contextctl.dev/v1alpha1","kind":"ExecutionReceipt","metadata":{"id":"00000000-0000-4000-8000-000000000003"},"spec":{"changedPaths":[],"checks":[{"checkId":"check.pre-action-revalidation","checkType":"pre-action-revalidation","observedAt":"2000-01-01T00:00:01Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":0},{"checkId":"check.execution","checkType":"execution","observedAt":"2000-01-01T00:00:02Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":1},{"checkId":"check.post-execution-verification","checkType":"post-execution-verification","observedAt":"2000-01-01T00:00:02Z","outcome":"passed","profileId":"profile.validation.v1","reasonCodes":[],"sequence":2}],"executionOutcome":"succeeded","finishedAt":"2000-01-01T00:00:02Z","lifecycleOutcome":"succeeded","origin":{
"contractDigest":"sha256:238c3af3ceab3eafc70d660b6e3d5cef97c3741d48b76c49e9e998a26d8afe30","contractId":"00000000-0000-4000-8000-000000000002","effectiveMode":"plan-only","resolvedTarget":{"domainRefs":[{"apiVersion":"contextctl.dev/v1alpha1","id":"domain.invalid","kind":"Domain"}],"projectRef":{"apiVersion":"contextctl.dev/v1alpha1","id":"project.invalid","kind":"Project"},"worktreeId":"worktree.invalid","worktreeRoleRef":{"apiVersion":"contextctl.dev/v1alpha1","id":"role.invalid","kind":"WorktreeRole"}},"type":"issued-contract"},
"reasonCodes":[],"receiptDigest":"sha256:95bb30141cd59f06c678ef685d754ee27ac9329af29050045836c7669530360d","receiptVersion":"1","releaseOutcome":"not-required","sanitization":{"applied":true,"completedAt":"2000-01-01T00:00:02Z","profileId":"profile.sanitization.v1","redactionCount":0},"startedAt":"2000-01-01T00:00:01Z","taskId":"00000000-0000-4000-8000-000000000001","unresolvedCoordinationWarnings":[],"verificationOutcome":"passed"}}
```

The exact post-finalization `ReceiptDeliveryResult` is not a new digest
payload. It copies the finalized receipt digest by exact tagged-string equality:

```json
{"apiVersion":"contextctl.dev/v1alpha1","attemptedAt":"2000-01-01T00:00:03Z","outcome":"succeeded","reasonCodes":[],"receiptDigest":"sha256:95bb30141cd59f06c678ef685d754ee27ac9329af29050045836c7669530360d","receiptId":"00000000-0000-4000-8000-000000000003","sanitizedSummary":"Synthetic delivery succeeded."}
```

#### Recalculated golden results

| Independent computation profile | Tagged digest |
| --- | --- |
| `profile.digest.worktree-content-v1` (empty payload) | `sha256:75a1e5502a349f7d22cbb583985b3045b6d5fd084f9f053cf3379bbbfe3781f9` |
| `profile.digest.policy-selection-v1` | `sha256:632908742df166217cf19fc74febda89e2f8ea816d71ec69f65a11a1a4831743` |
| `profile.digest.configuration-snapshot-v1` | `sha256:d673b61894f1377ae4e7b7a563db05204ec96cc95bfa9ffb08ccc191e3154f86` |
| `profile.digest.task-intent-bytes-v1` | `sha256:f4dda8a653d84b21ae740b502386262ebd525e7086270c5eba7af31eda6929c8` |
| `profile.digest.issuance-state-v1` | `sha256:4b9cf13b1accd0e3c29754feedb601c5a7b43619842ad76cbf118a56ae4a2702` |
| `profile.digest.contract-derivation-v1` | `sha256:9ced52eaa97d549c51caea566cc4681016f18614b68d1db0bc7a2748113f9a25` |
| `profile.digest.task-contract-v1` | `sha256:238c3af3ceab3eafc70d660b6e3d5cef97c3741d48b76c49e9e998a26d8afe30` |
| `profile.digest.pre-contract-evidence-v1` | `sha256:db7c19635103fc202ab07f4d9e2eb3686cf0046bba8c79887a7aabfd0e72be20` |
| `profile.digest.lease-acquisition-result-v1` | `sha256:1aeb432f3667229535829959d6a1bcb463472150a31eb999aaf058423f65b244` |
| `profile.digest.execution-receipt-v1` | `sha256:95bb30141cd59f06c678ef685d754ee27ac9329af29050045836c7669530360d` |

The corpus requires deterministic negative vectors at the projection boundary:

- mutating any included field produces different payload bytes and a different
  digest;
- adding an otherwise-valid source member that the catalog explicitly excludes
  leaves the defined projection unchanged, while adding a member forbidden by
  the source's closed shape is rejected before projection;
- including a self-digest that the profile excludes is a wrong projection and
  cannot reproduce the golden value;
- deleting or changing any separator byte, including any NUL, cannot reproduce
  the golden value;
- substituting any other profile identifier changes the separator and cannot
  reproduce the golden value;
- changing, trimming, transcoding, filtering, dereferencing, or appending a
  newline to a raw payload cannot reproduce its golden value;
- selecting a partial, expanded, reordered-array, implementation-defined, or
  otherwise wrong JCS projection cannot reproduce the golden value; and
- a `ReceiptDeliveryResult` whose `receiptId` does not identify the referenced
  finalized receipt or whose tagged digest differs from that receipt is
  rejected rather than rehashed.

These results establish only static integrity of the exact framed bytes. None
establishes trusted issuance, provenance, authenticity, authorization, or the
truth of evidence.

## 11. Complete array-ordering matrix

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
| `ExecutionReceipt.reasonCodes` | Set-like | `S(code)` | `S(code)` |
| `ReceiptDeliveryResult.reasonCodes` | Set-like | `S(code)` | `S(code)` |
| `GovernanceBundle.domains` | Set-like | `S(metadata.id)` | `S(metadata.id)` |
| `GovernanceBundle.worktreeRoles` | Set-like | `S(metadata.id)` | `S(metadata.id)` |

The final matrix contains 52 data rows, counted from the table above. It covers
every instance array in the `v1alpha1-r1` contract design. Relative to the
54-row prior baseline, the two removed rows are the now-impossible
TaskContract administrative-lock exact arrays under
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
| Required summary presence | Require `preContractEvidence.sanitizedSummary` and `ReceiptDeliveryResult.sanitizedSummary` while preserving optional warning and check summaries | Reject either missing required summary without widening optional fields | Phase 4 creates and checks summary content | DLP, review, and evidence access policy |
| Warning `relatedCheckId` integrity | Enforce identifier shape only | Resolve every present value to exactly one same-receipt `checkId`; forward and backward references are allowed | Phase 4 records the closed receipt evidence | Evidence retention and access policy |
| Branch, HEAD, dirty state, operation, lock, and lease match | Expected-state representation only; the TaskContract active-operation and administrative-lock dimensions are both none-only | Local consistency plus separate checkpoint denial/evidence classification for reusable live operation and lock observations | Phase 3 observes live, denies every represented active operation or Git administrative lock at the applicable checkpoint, and separately coordinates leases | Repository and host protections |
| TaskContract is trusted, fresh, and authoritative | Representation only | Structural/static consistency | Phase 4 validates issuer, derivation, integrity, bindings, freshness, and current preconditions | Issuer/key/trust administration |
| Receipt origin, contract binding, and pre-contract lease evidence agree | Enforce closed `oneOf` branches, conditional fields, and the existing receipt/contract field shapes | For `issued-contract`, validate the complete referenced contract, recompute `profile.digest.task-contract-v1`, enforce all eight exact contract-ID, digest, task, complete target, complete ordered Domain, and effective-mode equalities before receipt-digest acceptance; also reject invalid checkpoint/state combinations and impossible pre-contract execution claims | Phase 4 verifies provenance, authenticity, current authority and preconditions, records the applicable origin, and finalizes only after release outcome is known | Evidence retention and access policy |
| Receipt and related-artifact chronology, consistency, and non-authority | Enforce all nine timestamp fields with the exact whole-second `canonicalUtcTimestamp` pattern plus asserted `format: date-time`, receipt representation, and forbidden unknown fields | Enforce Gregorian validity, all 14 chronology relations, greatest-sequence final-`P` and final-`V` selection, required attempted P/E/V presence, universal P/E/V sequence and timestamp ordering, final passed/pre-expiry `P`, every passed pre-action check strictly before expiry, final-`V` outcome binding, not-attempted `V` emptiness, complete-contract/receipt and receipt/delivery-result comparisons, exact outcome precedence, origin consistency, unique check IDs, and lease/release consistency before receipt-digest and delivery acceptance | Phase 4 evaluates trusted time, actual immediacy, authenticity, evidence truth, and operational freshness and produces sanitized evidence after release outcome is known | Evidence retention and access policy |

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
  postcondition uniqueness, greatest-sequence final-applicable `P` and `V`
  selection, `count(P) >= 1`, `count(E) >= 1`, `count(V) >= 1`, universal
  final-`P`-before-every-`E` and every-`E`-before-every-`V` ordering by sequence
  and timestamp, attempted-execution freshness, final-`V` outcome binding,
  not-attempted `V` emptiness, receipt outcome consistency, and closed-bundle
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
- `ReceiptDeliveryResult` missing required `sanitizedSummary`;
- acquired lease state missing `leaseId`;
- acquired lease state missing `acquisitionResultDigest`;
- non-acquired lease state containing `leaseId`;
- pre-contract-denial receipt claiming successful execution;
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

Planned ExecutionReceipt contract tests exercise both closed origin branches,
conditional contract fields, every pre-contract denial checkpoint class, every
permitted checkpoint/acquisition-state pair, rejection of every unlisted pair,
pre-contract denials before and after lease acquisition, acquired-lease
acquisition-result binding, and every cleanup outcome. They reject non-acquired
or indeterminate states carrying lease identity, successful-execution claims in
pre-contract receipts, and missing required unresolved warnings.

Issued-contract coverage validates the complete referenced TaskContract,
recomputes its cataloged digest, enforces all eight exact equalities and complete
ordered Domain projection before receipt-digest acceptance, and includes all
five positive and 18 independent negative binding vectors above. It then
applies all 14 chronology relations; the complete passed pre-action freshness
invariant; greatest-sequence final-`P` and final-`V` selection; all eight
focused positive and 33 focused negative pre-action classes; all ten focused
positive and 20 focused negative post-execution-verification classes; P/E/V
presence; universal sequence and timestamp ordering; final-`V` outcome
binding; not-attempted `V` emptiness; and outcome/release consistency before
the receipt digest. It validates delivery binding and chronology only after
receipt finalization.

Planned HostOverlay contract tests exercise the complete selected
structured-remote language, all 15 positive and 61 independent negative remote
vectors, one outer record per `remoteName`, non-empty nested accepted sets,
`S(remoteName)` outer ordering, exact `J(remote)` nested identity and ordering,
and exact membership narrowing without normalization, aliasing, or field
omission.

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
| Permitted transitions | one positive vector for each of exactly seven branches: `ref-state`, `head-state`, `index-entry`, `tracked-entry`, `untracked-path`, `ignored-path`, and `submodule-entry`, with every path-keyed branch in the revised valid universe | identical `from` and `to`; duplicate target; unknown type; missing target key; branch-inapplicable key; invalid target comparator; any exact `.git` component; the retired `active-operation` and `administrative-lock` branches | Schema enforces seven closed branches and the path profile; Phase 1 static enforces exact inequality, target uniqueness, the normative `T(transition)` comparator, reserved-path rejection, and retired-branch rejection; Phase 3 live observes Git transitions; Phase 4 evidence attributes only authorized ordinary-path transitions |
| Required postconditions | one positive vector for each of eleven branches; optional `active-operations` and `administrative-locks` each expect `none`; path-keyed expected state uses the revised valid universe | missing or repeated `scope-contained`; duplicate type; `scope-contained` containing `expected`; state branch missing `expected`; reserved `.git`-component path; successful scope claim that omits an administrative effect; each forbidden single-operation active or administrative-lock expectation; malformed reusable observation condition; invalid lease-state truth-table combination | Schema enforces eleven closed branches, both none-only expectations, and valid paths; Phase 1 static enforces type uniqueness and reused baseline semantics; Phase 3 resolves administrative locations; Phase 4 requires an administrative effect to make `scope-contained` failed or indeterminate and verifies every postcondition |
| Warnings and checks | warning without optional fields; warning with summary only; warning with an earlier `relatedCheckId`; warning with a later `relatedCheckId`; check without optional summaries; check with `expectedSummary`; check with `observedSummary`; check with both; one check for every `intent-validation`, `project-domain-resolution`, `role-routing`, `host-binding`, `initial-preflight`, `lease-acquisition`, `post-acquisition-revalidation`, `contract-issuance`, `pre-action-revalidation`, `execution`, `post-execution-verification`, `lease-release`, and `receipt-finalization` value | warning or check sequence gap; warning or check sequence duplicate; duplicate `checkId`; dangling `relatedCheckId`; reference resolved only by another receipt or a delivery result; invalid reason-code order; unknown `checkType`; branch-inapplicable or unknown field | Schema enforces record shapes and vocabularies; Phase 1 static enforces sequences, unique check IDs, reason-code order, and same-receipt references independent of position; Phase 4 evidence produces and sanitizes the ordered records |
| Receipt outcomes, issued-contract binding, lease acquisition, timestamp chronology, and attempted-execution checks | every existing origin/outcome vector; all five exact receipt/contract binding vectors; every acquisition and cleanup branch; all ten timestamp-positive classes; all 14 chronology relations; all eight focused pre-action positives; all ten focused post-execution-verification positives; both origins; empty and populated checks; complete contract/receipt and receipt/delivery pairs | all 18 receipt/contract mismatches before receipt digest; every prohibited acquisition/outcome combination; all 24 timestamp lexical/calendar negatives; each chronology relation reversed independently; equal or reversed issuance freshness; all 33 focused pre-action negatives; all 20 focused post-execution-verification negatives, including universal-order, final-outcome mismatch, and stray-`V` classes | Schema enforces origin/union shape and all nine timestamp paths; Phase 1 validates both complete artifacts, calendar validity, contract digest, eight equalities, 14 chronology relations, greatest-sequence final-`P` and final-`V` selection, `count(P) >= 1`, `count(E) >= 1`, `count(V) >= 1`, final passed/pre-expiry `P`, every passed pre-action check pre-expiry, universal final-`P`-before-every-`E` and every-`E`-before-every-`V` ordering by sequence and timestamp, final-`V` outcome binding, and not-attempted `V` emptiness before receipt digest and delivery; Phase 3 supplies acquisition/release facts; Phase 4 owns provenance, trusted time, immediacy, evidence truth, authority, freshness, and final evidence |
| TaskContract truth table | each of the four allowed rows: plan-only/plan-only/non-writing; implementation/plan-only/non-writing; implementation/implementation/non-writing; implementation/implementation/writing with required lease and owned postcondition | requested plan-only with effective implementation; effective plan-only with `allowWrite: true`; `allowWrite: false` with `leaseRequired: true`; `allowWrite: true` with `leaseRequired: false`; `leaseId` present while no lease is required; `leaseId` absent while required; `owned` postcondition while no lease is required; `not-required` postcondition while a lease is required | Schema and Phase 1 static enforce the closed four-row invariant; Phase 3 live validates required ownership; Phase 4 evidence validates authority, binding, release, and postconditions |
| D1 validated canonical instance representation | strict UTF-8 source produces one immutable closed JSON value bound to the selected schema-set revision and root `$id`, complete strict-parse/number/NFC/Schema/static/array proof, and retained original bytes or same-process provenance; digest replay uses that representation | generic decoded object; missing or stale proof component; proof rebound to another value; mutable value; representation asserted as a public kind, production typed model, transferable authority, TaskContract, or runtime artifact | `schema-contracts` specifies the representation contract and records its vectors; future `model-implementation` implements and tests decoding, construction, provenance binding, typed round trips, serialization, and Schema/model conformance; Phase 4 owns trusted operational replay and authenticity |
| D4 raw worktree-content digest | exact empty, binary regular, executable, and link-target byte vectors reproduce their fixed tagged hashes; stable identity, kind, length, and metadata before/after observation | filtered or EOL-converted bytes; decoded or Unicode-normalized text; dereferenced symlink; unreadable, replaced, raced, truncated, length-inconsistent, or lossy observation; directory, gitlink, or unsupported type | Schema binds `trackedEntry.contentDigest` to one catalog profile; Phase 3 supplies identity-bound raw bytes; Phase 4 replays the same raw profile |
| D5 non-writing contracts | all three non-writing truth-table rows have exactly empty transitions, baseline-equal state postconditions, no lease identity, optional `lease-state: not-required`, and issued-receipt `changedPaths: []`; observed drift is evidence only | exactly 21 Cartesian negatives (`3 × 7`), pairing each non-writing row with each permitted transition branch; any drift-describing postcondition; lease identity/ownership; non-empty changed paths; test/build capability treated as a write override | Schema and Phase 1 static reject the closed contract and compare explicit postconditions with the immutable baseline; Phase 4 enforces empty changed paths and classifies drift as failed or indeterminate verification |
| D6 execution/verification biconditional | exactly 13 pairs: `not-attempted/not-performed`; each of `succeeded`, `failed`, `cancelled`, and `indeterminate` with each of `passed`, `failed`, and `indeterminate` | exactly seven pairs: each attempted execution outcome with `not-performed`, plus `not-attempted` with `passed`, `failed`, or `indeterminate` | Phase 1 static applies the unchanged 13/7 biconditional, then the separate final-`V` binding and not-attempted `V`-empty rules, before the existing lifecycle-precedence table; Phase 4 supplies evidence claims |
| D7 simultaneous transition composition | complete nine-dimension materialized `B`; all seven `from` values bind directly to `B`; unique transitions apply simultaneously; one canonical nine-dimension `F` results regardless of wire order; active operations and administrative locks remain none; changed dimensions have exact `F` postconditions | baseline/from mismatch; either retired transition; sequential dependency; order-dependent result; non-none active-operation or administrative-lock final state; invalid final composite; missing or mismatched changed-dimension postcondition; drift asserted for an unchanged dimension; incomplete D2 or D3 value | Phase 1 compares, applies only seven transition types simultaneously, reconstructs all nine dimensions, and validates `F`; Phase 3 materializes live-dependent `B`; Phase 4 compares evidence with `F`, attributes transitions, and verifies scope/postconditions |
| D8 closed HostOverlay binding | complete branch and detached records with exactly `roleRef`, `worktreeId`, `repositoryRoot`, `expectedRef`, and non-empty canonical `remoteNames`; every name resolves once | each missing field; every unknown field; empty, duplicate, or non-canonical remote names; unknown name; branch without `branchRef`; detached with `branchRef`; `expectedBranch`; each cached observed root/HEAD/branch/remote field | Schema closes the five-field record and ref branches; Phase 1 enforces binding identity, array canon, and name resolution; Phase 3 compares live canonical root, registration, ref, and every named remote |
| D9 RoutingPolicy projection equality and complete-set contract | all six required complete-set positive vectors; different priorities; case- or pattern-different matches; sample-equivalent but structurally different patterns; equal match at different priorities reaches its assigned classification | all twelve required complete-set negative vectors, including partial owner, no-fallthrough, same-target tie, collective-role union, split reuse, fallback failure, and TaskContract Domain/role/target mismatch; different IDs with equal `RuleProjection` JCS bytes; same-priority equal `MatchProjection` JCS bytes; non-canonical nested array | `schema-contracts` records projection equality, `Drule`/`Dresolved`/`Owned(R)` semantics, exact Phase 2 order, and vectors; executable projection/JCS comparison belongs to future `model-implementation`; Phase 2 alone resolves and routes the complete set, denies top-priority ambiguity or incomplete ownership, and never falls through or unions roles |
| D10 HostOverlay narrowing proof and canonical structured remotes | exact Project/role consistency; capabilities satisfying `Cportable` and `Cbinding`; all 15 structured-remote positives; repository and remote subsets by exact validated `J(remote)`; all binding names resolve; `src/lib/**` is included within Project `src/**`; broad `**` remains valid but excludes reserved paths | all 61 independent structured-remote negatives; each of the nine exact narrowing rejection-code classes; literal `.git/**`, `.git/config`, `foo/.git/**`, and `foo/.git/config`; added capability or remote; role/project mismatch; `docs/**` outside the Project universe; unsupported syntax, compilation failure, resource exhaustion, or indeterminate emptiness; sample, alias, normalization, ignored field, or prefix heuristic offered as proof; any binding, free capacity, or lease offered to make an incomplete selected owner eligible | Schema enforces the closed record, path profiles, named host/repository profiles, namespace and port rules; Phase 1 rejects literal `.git` components and performs exact lexical, `J(remote)`, set/reference, membership, order, and automata checks relative to revised `U`; only after Phase 2 selects one role that owns all of `Dresolved` may Phase 3 compare the live remote and reject administrative aliases; HostOverlay and runtime state can narrow or deny but never widen routing eligibility |
| D11 digest catalog and golden corpus | all eleven digest field paths bind once to ten computations; every exact separator, raw payload, JCS payload, exclusion, completed source value, tagged hash, and delivery-copy equality reproduces the recorded corpus | included-field mutation; excluded-field mishandling; self-digest inclusion; missing/changed separator byte; substituted profile; changed raw bytes; wrong JCS projection; mismatched copied receipt digest; a cycle, ambiguity, duplicate binding, or missing field path | `schema-contracts` specifies the acyclic catalog, framing, projection contract, and recorded corpus; future `model-implementation` reconstructs projections, emits JCS bytes, hashes, replays, and proves cross-runtime reproduction; Phase 3 supplies stable raw observations; Phase 4 performs trusted operational replay and exact delivery-copy checks; every digest remains integrity-only |
| D12 review-only capability complement | exactly four permitted sets: empty, inspect, validate, and inspect-plus-validate; each has `roleClass: review`, only plan-only mode, exact `C − P` prohibited set, and no exclusive write | each of the eleven non-observation capabilities permitted separately; wrong role or mode; missing complement member; permitted/prohibited overlap or other complement error; exclusive write; restoration attempted through another field | Schema and Phase 1 static enforce the complete five-class partition and exact equations; later intersections may only narrow the result and cannot restore a forbidden capability |
| Cross-dimension baselines | complete inventories rather than deltas; index/tracked field equality; gitlink/submodule object equality; tracked/submodule and untracked/ignored disjointness; canonical clean/none versus exact selection | omitted inventory member; index/tracked mode or object mismatch; gitlink/submodule mismatch; tracked/submodule collision; untracked/ignored collision; exact-path collision with explicit index, tracked, or submodule path; a Phase 1 check incorrectly depending on live state | Schema enforces local shape; Phase 1 static enforces relationships over explicit closed data; Phase 3 live owns HEAD-, object-, ignore-, filesystem-, checkout-, and index-dependent checks; Phase 4 evidence reuses the same postcondition semantics |
| Required summaries and five-state correction | pre-contract evidence with required `sanitizedSummary`; delivery result with required `sanitizedSummary`; warnings and checks omitting or including their optional summaries; all five acquisition states | pre-contract evidence missing `sanitizedSummary`; delivery result missing `sanitizedSummary`; any stale four-state-only validator or vector | Schema enforces record-specific presence; Phase 1 static runs the vectors; Phase 4 evidence establishes actual sanitization and the five-state lifecycle meaning |
| SG-002 numeric profile | every existing canonical-token, field-minimum, and field-maximum vector, with Git stage `0` as its only valid stage | Git stage `1`, `2`, `3`, and `4`; every existing signed, negative-zero, leading-plus, leading-zero, fractional, exponent, unsafe, NaN, Infinity, and field-out-of-range vector | `schema-contracts` specifies the six-field profile, exact bounds, and vectors; future `model-implementation` enforces raw tokens before conversion and proves precision-safe representation/JCS/replay across runtimes; Phase 4 verification requires raw-token replay or the complete validated-representation proof |

The matrix contains 25 logical data rows, independently counted from the table.
It preserves all existing issued-contract and pre-contract outcome vectors,
the normative `T(transition)` definition, and the complete SG-002 vectors. A
future implementation is conformant only when every matrix cell is covered at
its assigned layer; a lower layer MUST NOT claim a live or evidence property
it cannot establish.

### Seventh-review proposed-repair invariant counts

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
timestamp paths = 9
timestamp lexical/calendar positives = 10
timestamp lexical/calendar negatives = 24
chronology relations = 14
focused pre-action positives = 8
focused pre-action negatives = 33
focused post-execution-verification positives = 10
focused post-execution-verification negatives = 20
D6 valid receipt-level combinations = 13
D6 invalid receipt-level combinations = 7
receipt/contract equalities = 8
receipt-binding positives = 5
receipt-binding negatives = 18
digest-bearing paths = 11
digest computations = 10
receipt/delivery digest copies = 1
numeric fields = 6
```

The repaired synthetic execution-receipt projection is exactly 1741 UTF-8
bytes, the completed receipt is exactly 1831 UTF-8 bytes, and its independently
recomputed tagged digest is the execution-receipt value recorded in the table
above. The delivery result copies that tagged value exactly and performs no
additional computation. The protected corpus retains exactly five distinct timestamp
literal values across 22 occurrences and exactly seven structured-remote
occurrences.

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

Planned SG-001 contract tests prove that every closed union rejects
branch-inapplicable fields; baseline and postcondition arrays enforce exact
path uniqueness before hashing; transition target uniqueness and postcondition
type uniqueness are checked before hashing; receipt checkpoint/acquisition
chronology, all 14 timestamp relations, attempted-execution freshness, P/E/V
presence and universal ordering, greatest-sequence final-`P` and final-`V`
selection, final-`V` outcome binding, and not-attempted `V` emptiness are
evaluated deterministically; failed or indeterminate release
cannot omit unresolved coordination warnings; and warning and check arrays
preserve contiguous evidence sequence.

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
