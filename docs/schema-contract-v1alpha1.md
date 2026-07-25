# contextctl.dev/v1alpha1 Schema Contract Design

Phase 1: Schemas and Models is current, but Schema implementation has not begun. This document is the proposed design contract for the first Schema baseline. Its governance status remains proposed until independent audit and `integration-control` approval are complete; it is not yet an approved or implementation-ready Schema contract. It is not a JSON Schema resource, configuration instance, execution adapter, policy engine, or authorization mechanism.

Nothing in this document grants operational authority. In particular, JSON-valid input shaped like a `TaskContract` is untrusted unless trusted framework logic issued it or validated its issuer, integrity, derivation, bindings, freshness, and current preconditions. A digest or successful Schema validation does not establish authority.

Concrete `HostOverlay`, `TaskContract`, `ExecutionReceipt`, lease, lock, runtime-state, and receipt-delivery records remain host-local and outside the target worktree and portable governance. The resource identifiers in this document are reserved for the first approved Schema baseline but remain unpublished.

## 1. Status, scope, and authority

The `schema-contracts` role owns the public JSON Schema contract under `schemas/v1alpha1/`, shared definitions, closed envelopes, Schema-expressible constraints, unknown-field rejection, conspicuously synthetic fixtures, Schema validation and contract tests, the static validation/codec contract for the internal validated representation defined in section 10, and directly required Schema documentation. It does not own production Python models, production decoding or serialization implementation, task resolution, operational routing, live Git inspection, leases, contract issuance, receipt generation, a CLI, adapters, or enforcement.

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
| Repository-relative path | POSIX `/` separators; no leading slash, drive prefix, backslash, empty segment, `.` segment, `..` segment, NUL, or trailing slash; maximum 4096 characters | Already NFC; canonical spelling and set ordering | Phase 3 resolves against the bound canonical root and checks containment live |
| Path pattern | Repository-relative grammar; `*` and `?` stay within a segment and `**` is allowed only as a complete segment; no negation, backslash, brace expansion, or host absolute syntax | Pattern parse succeeds; D10 language relationships are decided exactly by its finite-automata inclusion proof | Phase 2 resolves task coverage; Phase 3 checks concrete effects |
| Absolute host path | Closed object `{ platform, value }`, where `platform` is `windows` or `posix`; lexical checks only | Fixtures use conspicuously synthetic paths | Phase 3 canonicalizes, resolves aliases, and checks the real binding and containment |
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
| Timestamp | RFC 3339 UTC `date-time` ending in `Z` | Canonical lexical form | Phase 4 uses a trusted clock and checks freshness |
| Freshness boundary | Closed `{ issuedAt, expiresAt }` | Both timestamps present and `expiresAt` later than `issuedAt` | Phase 4 evaluates current time and policy bounds |
| Task, contract, lease, receipt ID | Canonical lower-case UUID; contract and receipt IDs narrow their envelope `metadata.id` | Uniqueness in the loaded artifact set | Trusted lifecycle logic checks ownership, derivation, and task binding |
| Structured remote | Closed `{ transport, host, port?, namespace, repository }`; transport is `https` or `ssh`; optional `port` is an integer from 1 through 65535 under the numeric profile; there is no user-info or credential field | Lower-case canonical host, omitted default port, unique canonical entries | Phase 3 compares configured remotes live without exposing credentials |
| Repository identity | Closed object with non-empty `acceptedRemotes` | Canonical uniqueness and portable-only content | Phase 3 observes and matches the target repository live |
| Remote expectation | Closed `{ remoteName, acceptedRemotes }`; `acceptedRemotes` is required and non-empty | One record per `remoteName`; outer records are unique and ordered by `S(remoteName)`, and nested remotes are unique and ordered by `J(remote)` | Phase 3 compares the observed Git remote for that name with the accepted set |
| Worktree logical identity | Logical `worktreeId` plus a `WorktreeRole` reference where required; never an absolute path | Reference existence in a closed set | Host binding and registration are checked in Phases 2–3 |
| Check outcome | Enum `passed`, `failed`, or `indeterminate` | — | Phase 4 records evidence without turning it into authority |
| Execution outcome | Enum `not-attempted`, `succeeded`, `failed`, `cancelled`, or `indeterminate` | — | Phase 4 derives it from the attempt |
| Verification outcome | Enum `not-performed`, `passed`, `failed`, or `indeterminate` | — | Phase 4 derives it from post-execution verification |
| Release outcome | Enum `not-required`, `succeeded`, `failed`, or `indeterminate` | — | Phase 3 supplies ownership-checked release evidence |
| Lifecycle outcome | Enum `denied`, `succeeded`, `failed`, `cancelled`, or `indeterminate` | Cross-field combinations are structurally bounded | Phase 4 derives the terminal outcome; it does not imply lease release |
| Receipt-delivery outcome | Enum `not-attempted`, `succeeded`, `failed`, or `indeterminate` | — | Phase 4 records the post-finalization delivery attempt separately |
| Scope | Closed `{ capabilities, paths }` with both arrays present | Arrays canonical; allowed/prohibited sets disjoint and containment checked where statically provable | Phases 2–4 calculate effective scope and verify effects |
| Permitted transition | One of the nine closed, target-keyed branches defined under `TaskContract`; no open transition name or generic path list exists | Target uniqueness and canonical target order before hashing | Phases 3–4 compare a live transition against immutable baseline authority |
| Required postcondition | One of the eleven closed branches defined under `TaskContract`; no open postcondition name or generic expected record exists | Type uniqueness, required `scope-contained`, and exact nested-state consistency | Phase 4 checks fresh observations after execution |

A structured remote uses lower-case canonical host text and ordered `namespace` segments. Default transport ports must be omitted so equivalent remotes do not acquire multiple encodings. Secret-bearing URLs, user-info, tokens, private-key material, and environment-derived host data are not representable fields.

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

Where a field uses the `sanitizedSummary` value profile, its value is an
already-NFC string of 1 through 1024 decoded Unicode characters with none of
U+0000 through U+001F or U+007F. The value profile defines string validity
only; each containing record independently requires or permits presence.
Schema validity proves only this shape. Phase 4 sanitization plus external
classification, DLP, review, and evidence-access controls are still required
to establish that the content is safe.

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

A Domain cannot reference itself. Overlap references must exist, remain within the Project, and be symmetric in a closed bundle. Phase 1 may identify undeclared or contradictory overlaps when the path grammar proves them, but does not resolve a real task to Domains. Include/exclude application, complete task coverage, and ambiguity are Phase 2. Domains contain neither host paths nor live state.

### `WorktreeRole`

Required `spec` fields:

| Field | Design |
| --- | --- |
| `projectRef` | The associated `Project` reference |
| `roleClass` | Enum `implementation`, `review`, or `integration-control` |
| `ownedDomainRefs` | Non-empty set of Domains the role owns |
| `excludedDomainRefs` | Set of explicitly excluded Domains |
| `permissions` | Mode and capability ceiling using the shared permission shape |
| `branchPolicy` | Closed allowed/denied exact-branch and prefix arrays |
| `cleanlinessPolicy` | Closed policy for tracked, untracked, ignored, index, and submodule state; each is `clean`/`none` or `contract-enumerated` as applicable |
| `exclusiveWriteRequired` | Required Boolean |
| `reviewOnly` | Required Boolean |

Owned and excluded Domains are disjoint and must exist in the same Project. A role may own multiple Domains. `roleClass: integration-control` identifies responsibility only; it grants no administrative operation. Branch deny rules win over allow rules during later evaluation. The object defines a logical responsibility profile, not a filesystem path or live worktree.

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

Positive vectors cover complete branch and detached records. Negative vectors
cover each missing field, every unknown field, duplicate or empty
`remoteNames`, an unknown remote name, non-canonical name order, a branch
without `branchRef`, a detached value with `branchRef`, `expectedBranch`, and
each forbidden cached observation.

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
the `repositoryRelativePath` profile. A path pattern is anchored to the whole
path and has exactly this restricted meaning:

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
| `expectedBaseline` | Immutable closed reference, HEAD, index, tracked, untracked, ignored, submodule, active-operation, and administrative-lock conditions |
| `permittedTransitions` | Canonical set of explicitly permitted transition records |
| `requiredPostconditions` | Canonical set of postcondition records |
| `leaseRequired` | Explicit Boolean |
| `leaseId` | Canonical UUID, present exactly when a lease is required |
| `issuanceCheckpoint` | Closed observation timestamp and `profile.digest.issuance-state-v1` state digest defined exactly in section 10 |
| `freshness` | Mandatory `issuedAt` and `expiresAt` boundary |

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

The mandatory 27 negative vectors are the Cartesian product of the three
non-writing rows—plan-only/plan-only, implementation/plan-only, and
implementation/implementation—with the nine transition types:
`ref-state`, `head-state`, `index-entry`, `tracked-entry`, `untracked-path`,
`ignored-path`, `submodule-entry`, `active-operation`, and
`administrative-lock`. Phase 1 rejects the closed contract and checks any
explicit state postcondition against the baseline. Phase 4 requires the empty
changed-path set and treats mutation or uncertain drift as failed or
indeterminate verification.

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
| `activeOperations` | `activeOperationsCondition` |
| `administrativeLocks` | `administrativeLocksCondition` |

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
   submodule root and descendant.
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
10. Require every repository-relative path to satisfy the defined repositoryRelativePath profile, strict UTF-8, and already-NFC checks.
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

#### Exact `permittedTransitions`

`TaskContract.spec.permittedTransitions` is a set-like array that may be
empty. Its members are limited to these nine closed branches:

| `type` | Required target field | Exact `from` and `to` types |
| --- | --- | --- |
| `ref-state` | — | `refState` |
| `head-state` | — | `headState` |
| `index-entry` | `path: repositoryRelativePath` | `entryPresence(indexEntryStateWithoutPath)` |
| `tracked-entry` | `path: repositoryRelativePath` | `entryPresence(trackedEntryStateWithoutPath)` |
| `untracked-path` | `path: repositoryRelativePath` | enum `absent` or `present` |
| `ignored-path` | `path: repositoryRelativePath` | enum `absent` or `present` |
| `submodule-entry` | `path: repositoryRelativePath` | `entryPresence(submoduleEntryStateWithoutPath)` |
| `active-operation` | `operation: activeOperation` | enum `inactive` or `active` |
| `administrative-lock` | `lock: administrativeLockIdentity` | enum `absent` or `present` |

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
- `(S(type), S(path))` for path-keyed branches;
- `(S(type), S(operation))` for `active-operation`; and
- `(S(type), L(lock))` for `administrative-lock`.

At most one transition may target a given `T(transition)`. Thus there is at
most one ref-state transition, at most one head-state transition, one
transition per `(type, path)`, one per `(type, operation)`, and one per
administrative-lock identity. Targets must be strictly ordered by
`T(transition)`. Target uniqueness is validated before hashing;
`J(transition)` is permitted only as a deterministic diagnostic tie-breaker
after that validation. A transition grants no authority outside the contract
scope, and actual transition attribution remains Phase 4 verification.

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
| `active-operations` | required `expected: activeOperationsCondition` |
| `administrative-locks` | required `expected: administrativeLocksCondition` |
| `lease-state` | required `expected` enum `not-required` or `owned` |

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
| `active-operation(operation)` | active if and only if the operation is in the complete set | `active-operations` |
| `administrative-lock(lock)` | present if and only if the lock identity is in the complete set | `administrative-locks` |

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

All transitions apply simultaneously and independently of array order:

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
restrictions, D2 checkout/observation rules, active-operation and
administrative-lock rules, and every other baseline cross-dimension invariant.

Every dimension changed by at least one transition requires its matching
postcondition from the table, and that postcondition's `expected` value equals
the corresponding canonical projection of `F`. A postcondition for an
unchanged dimension is optional; if present, it equals the unchanged baseline
projection. `scope-contained` and `lease-state` retain their independent
mandatory rules.

Phase 1 owns explicit closed-data comparison, simultaneous application,
canonical reconstruction, and static final-composite validation. Phase 3 owns
HEAD/live/object/index/filesystem materialization before issuance. Phase 4
compares final evidence with `F`, attributes transitions, and verifies scope
and postconditions.

Positive vectors include independent simultaneous changes whose order does
not affect the same valid final composite. Negative vectors cover baseline/
`from` mismatch, an attempted sequential dependency, an invalid final
cross-dimension composite, a missing postcondition for a changed dimension, a
mismatched final postcondition, and drift asserted by a postcondition on an
unchanged dimension.

Local constraints enforce the complete four-row mode/write/lease truth table,
including non-widening effective mode, `leaseRequired == allowWrite`, exact
`leaseId` presence, and any present `lease-state` postcondition. They also
require non-empty Domains, require effective scope not to exceed requested
scope structurally where provable, and require freshness ordering. Phase 1 can
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

The seven explicit invalid combinations are `succeeded`, `failed`,
`cancelled`, or `indeterminate` with `not-performed`, and `not-attempted` with
`passed`, `failed`, or `indeterminate`. Only after these combinations are
rejected is the existing lifecycle-precedence table below applied. Its
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
- `activeOperations.none` if and only if none exists; otherwise
  `activeOperations.exact`; and
- `administrativeLocks.none` if and only if none exists; otherwise
  `administrativeLocks.exact`.

This selection prevents two different baseline encodings from describing the
same observed state.

### Postcondition reuse

A required-postcondition branch that reuses a baseline condition also reuses
all of this section's inventory and cross-dimension semantics. There is no
weaker parallel definition for postconditions.

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
routing. Phase 2 collects all matching rules, finds the greatest matching
priority, and fails closed when more than one rule matches at that priority,
even when their decisions are identical. One highest-priority match yields its
route or deny decision; no match uses the required explicit deny fallback.
Global priority uniqueness is not required. Availability, host binding, and
lease state cannot change priority or make an ineligible role eligible.

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

`schema-contracts` defines and tests this static validation/codec boundary,
projection reconstruction, JCS bytes, and golden vectors. The future distinct
`model-implementation` worktree owns production typed models, typed round
trips, Schema/model conformance, and production decoders and serializers only
after the approved Schema baseline is integrated into `main` and the separate
worktree is created. Phase 4 owns operational replay against trusted issuer
provenance, current runtime state, contract authorization, execution evidence,
and receipts. This boundary does not weaken the Schema-before-model gate.

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
{"apiVersion":"contextctl.dev/v1alpha1","kind":"ExecutionReceipt","metadata":{"id":"00000000-0000-4000-8000-000000000003"},"spec":{"changedPaths":[],"checks":[],"executionOutcome":"succeeded","finishedAt":"2000-01-01T00:00:02Z","lifecycleOutcome":"succeeded","origin":{
"contractDigest":"sha256:238c3af3ceab3eafc70d660b6e3d5cef97c3741d48b76c49e9e998a26d8afe30","contractId":"00000000-0000-4000-8000-000000000002","effectiveMode":"plan-only","resolvedTarget":{"domainRefs":[{"apiVersion":"contextctl.dev/v1alpha1","id":"domain.invalid","kind":"Domain"}],"projectRef":{"apiVersion":"contextctl.dev/v1alpha1","id":"project.invalid","kind":"Project"},"worktreeId":"worktree.invalid","worktreeRoleRef":{"apiVersion":"contextctl.dev/v1alpha1","id":"role.invalid","kind":"WorktreeRole"}},"type":"issued-contract"},
"reasonCodes":[],"receiptVersion":"1","releaseOutcome":"not-required","sanitization":{"applied":true,"completedAt":"2000-01-01T00:00:02Z","profileId":"profile.sanitization.v1","redactionCount":0},"startedAt":"2000-01-01T00:00:01Z","taskId":"00000000-0000-4000-8000-000000000001","unresolvedCoordinationWarnings":[],"verificationOutcome":"passed"}}
```

The exact completed receipt, proving the sole excluded member, is:

```json
{"apiVersion":"contextctl.dev/v1alpha1","kind":"ExecutionReceipt","metadata":{"id":"00000000-0000-4000-8000-000000000003"},"spec":{"changedPaths":[],"checks":[],"executionOutcome":"succeeded","finishedAt":"2000-01-01T00:00:02Z","lifecycleOutcome":"succeeded","origin":{
"contractDigest":"sha256:238c3af3ceab3eafc70d660b6e3d5cef97c3741d48b76c49e9e998a26d8afe30","contractId":"00000000-0000-4000-8000-000000000002","effectiveMode":"plan-only","resolvedTarget":{"domainRefs":[{"apiVersion":"contextctl.dev/v1alpha1","id":"domain.invalid","kind":"Domain"}],"projectRef":{"apiVersion":"contextctl.dev/v1alpha1","id":"project.invalid","kind":"Project"},"worktreeId":"worktree.invalid","worktreeRoleRef":{"apiVersion":"contextctl.dev/v1alpha1","id":"role.invalid","kind":"WorktreeRole"}},"type":"issued-contract"},
"reasonCodes":[],"receiptDigest":"sha256:b4dee763f7f2113830aa90298940bd164099dd2049b339c8de6a82b0b650d9b6","receiptVersion":"1","releaseOutcome":"not-required","sanitization":{"applied":true,"completedAt":"2000-01-01T00:00:02Z","profileId":"profile.sanitization.v1","redactionCount":0},"startedAt":"2000-01-01T00:00:01Z","taskId":"00000000-0000-4000-8000-000000000001","unresolvedCoordinationWarnings":[],"verificationOutcome":"passed"}}
```

The exact post-finalization `ReceiptDeliveryResult` is not a new digest
payload. It copies the finalized receipt digest by exact tagged-string equality:

```json
{"apiVersion":"contextctl.dev/v1alpha1","attemptedAt":"2000-01-01T00:00:03Z","outcome":"succeeded","reasonCodes":[],"receiptDigest":"sha256:b4dee763f7f2113830aa90298940bd164099dd2049b339c8de6a82b0b650d9b6","receiptId":"00000000-0000-4000-8000-000000000003","sanitizedSummary":"Synthetic delivery succeeded."}
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
| `profile.digest.execution-receipt-v1` | `sha256:b4dee763f7f2113830aa90298940bd164099dd2049b339c8de6a82b0b650d9b6` |

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
| `WorktreeRole.branchPolicy.allowed.prefixes` | Set-like | `S(prefix)` | `S(prefix)` |
| `WorktreeRole.branchPolicy.denied.exact` | Set-like | `S(branchRef)` | `S(branchRef)` |
| `WorktreeRole.branchPolicy.denied.prefixes` | Set-like | `S(prefix)` | `S(prefix)` |
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
| `TaskContract.expectedBaseline.activeOperations.operations` | Set-like | `S(value)` | `S(value)` |
| `TaskContract.expectedBaseline.administrativeLocks.locks` | Set-like | `L(lock)` | `L(lock)` |
| `TaskContract.permittedTransitions` | Set-like | `T(transition)` | `T(transition)` |
| `TaskContract.requiredPostconditions` | Set-like | `S(type)` | `S(type)` |
| `TaskContract.requiredPostconditions[type="index-state"].expected.entries` | Set-like complete inventory reusing the stage-`0` baseline profile | `S(entry.path)` | `S(entry.path)` |
| `TaskContract.requiredPostconditions[type="tracked-state"].expected.entries` | Set-like | `S(entry.path)` | `S(entry.path)` |
| `TaskContract.requiredPostconditions[type="untracked-state"].expected.paths` | Set-like | `S(path)` | `S(path)` |
| `TaskContract.requiredPostconditions[type="ignored-state"].expected.paths` | Set-like | `S(path)` | `S(path)` |
| `TaskContract.requiredPostconditions[type="submodule-state"].expected.entries` | Set-like | `S(entry.path)` | `S(entry.path)` |
| `TaskContract.requiredPostconditions[type="active-operations"].expected.operations` | Set-like | `S(value)` | `S(value)` |
| `TaskContract.requiredPostconditions[type="administrative-locks"].expected.locks` | Set-like | `L(lock)` | `L(lock)` |
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

The final matrix contains 56 data rows, counted from the table above. It covers
every instance array in the `v1alpha1-r1` design. Shared definitions use the
same rule everywhere they are embedded. No v1alpha1 array is
"order-insensitive but preserved on the wire." Adding such a field would make
digests representation-sensitive and requires a new explicit design review.
JCS never reorders an array.

## 12. Structural, static, later-phase, and external-control matrix

| Requirement | JSON Schema structural enforcement | Phase 1 static or fixture hygiene | Later operational enforcement | External control |
| --- | --- | --- | --- | --- |
| Required fields, types, enums, closed objects | Enforce | Contract vectors | Not applicable | Not applicable |
| Identifier, path, digest, UUID, and format syntax | Enforce lexical profile | Canonical spelling and cross-reference checks | Bind to trusted/live values where required | Not applicable |
| Duplicate JSON keys | Not observable after ordinary parsing | Strict parser detects them during parsing before object construction completes | Same parser before later verification | Not applicable |
| Raw JSON-number token profile | `type: integer` cannot preserve lexical form | Strict parser enforces `0|[1-9][0-9]*`, the safe-integer ceiling, and field bounds before ordinary numeric conversion | Verification repeats raw-token validation or requires the complete validated canonical instance representation proof | Not applicable |
| Numeric field inventory | Exact integer type and per-field minimum/maximum | Reject any undeclared numeric field and audit the complete six-field inventory | A future signed or fractional field requires a contract revision | Not applicable |
| Strings and member names already NFC | Not portable as an ordinary Schema assertion | Reject non-NFC before canonicalization | Repeat before hashing and verification | Authoring guidance |
| Reference existence, uniqueness, subset rules, canonical arrays | Shape only or partial uniqueness | Enforce within a closed loaded set | Revalidate selected/runtime bindings | Not applicable |
| `displayName` is non-identifying | Length and character shape only | Conspicuously synthetic fixtures and best-effort scanner | Sanitize if copied into Phase 4 evidence | Author review and data classification |
| Description text is secret-free | Length and character shape only | Synthetic values and best-effort secret scanning | Phase 4 redaction/sanitization before evidence | Secret manager, DLP, review, and access controls |
| A hostname is non-sensitive | Hostname syntax only | Reserved `.invalid` fixture hosts | Phase 4 redacts sensitive environment evidence | Environment classification and access control |
| A `sanitizedSummary` is actually safe | Bounded string shape only | Synthetic fixture content | Phase 4 sanitizer must create/check it and fail closed on incomplete sanitization | DLP, review, and evidence access policy |
| No secrets in arbitrary permitted strings | Unknown secret-like fields are rejected; allowed strings can still hold secrets | Best-effort scanners | Phase 4 redaction; no secret values in contracts or receipts | External secret delivery and incident handling |
| Absolute path denotes the intended worktree | Platform/value syntax only | Synthetic path hygiene | Phase 3 canonical path, alias, registration, and containment checks | Host filesystem permissions |
| Domain resolution and routing are unambiguous | Policy shape only | Provable contradictions only | Phase 2 resolves and fails closed | Not applicable |
| HostOverlay narrows customer governance | Shape and conditional fields | Enforce D10 Project/role identity, exact capability equations, accepted-remote inclusions, binding-name resolution, and DFA path-language inclusions; any unsupported or indeterminate proof denies the configuration | Phases 2-3 consume the statically valid restriction and compare the bound worktree live; this row does not execute routing | Host configuration review |
| HostOverlay remote expectations have one record per name and non-empty accepted sets | Enforce closed records and non-empty `acceptedRemotes` | Outer uniqueness and order use only `S(remoteName)`; nested remote uniqueness and order use `J(remote)` | Phase 3 compares each observed named Git remote with its accepted set | Credential handling remains outside governance |
| Conflict-free index is representable | Enforce stage `0`, required false index flags, supported modes, and closed fields | Enforce path uniqueness, canonical order, and complete-inventory semantics | Phase 3 denies unmerged, intent-to-add, skip-worktree, assume-unchanged, sparse, unsupported-mode, or otherwise unrepresentable indexes before issuance | Phase 4 may record only sanitized pre-contract denial evidence |
| Baseline runtime structures are closed and exhaustive | Enforce all nine required dimensions, exact union branches, required and forbidden fields, enums, and branch-specific exact cardinalities | Cross-branch consistency and canonical identity checks | Phases 3–4 observe and compare the corresponding live state | Repository and host protections |
| ExpectedBaseline inventory and cross-dimension consistency | Enforce branch shapes and local field relationships | Enforce complete explicit inventories, index/tracked and gitlink/submodule equality, coverage, and exact-path disjointness where closed data suffices | Phase 3 enforces relationships requiring HEAD, objects, ignore rules, filesystem, checkout, or live index | Phase 4 verification reuses the same semantics for postconditions |
| Baseline and postcondition state entries are unique by repository-relative path | Enforce entry shape and required path | Reject duplicate `S(entry.path)` before hashing, regardless of other entry fields | Phases 3–4 compare live state by the same path identity | Not applicable |
| TaskContract mode, write, lease, and lease-state truth table | Enforce the four allowed closed combinations and conditional field presence | Reject every unlisted combination and cross-field mismatch | Phase 3 validates required lease ownership; Phase 4 validates effective authority and contract binding | Issuer and lease-store administration |
| Transition targets and postcondition types are unique | Enforce closed branch shapes | Reject duplicate `T(transition)` and duplicate `S(type)` before hashing | Phase 4 attributes transitions and checks postconditions | Not applicable |
| Required summary presence | Require `preContractEvidence.sanitizedSummary` and `ReceiptDeliveryResult.sanitizedSummary` while preserving optional warning and check summaries | Reject either missing required summary without widening optional fields | Phase 4 creates and checks summary content | DLP, review, and evidence access policy |
| Warning `relatedCheckId` integrity | Enforce identifier shape only | Resolve every present value to exactly one same-receipt `checkId`; forward and backward references are allowed | Phase 4 records the closed receipt evidence | Evidence retention and access policy |
| Branch, HEAD, dirty state, operation, lock, and lease match | Expected-state representation only | Local consistency | Phase 3 observes live and coordinates leases | Repository and host protections |
| TaskContract is trusted, fresh, and authoritative | Representation only | Structural/static consistency | Phase 4 validates issuer, derivation, integrity, bindings, freshness, and current preconditions | Issuer/key/trust administration |
| Receipt origin, contract binding, and pre-contract lease evidence agree | Closed `oneOf` branches and conditional fields | Reject fabricated contract binding, invalid checkpoint/state combinations, and impossible pre-contract execution claims | Phase 4 records the applicable origin and finalizes only after release outcome is known | Evidence retention and access policy |
| Receipt accurately reports and remains non-authoritative | Representation and forbidden unknown fields | Exact outcome precedence, origin consistency, sequence continuity, unique check IDs, and lease/release consistency | Phase 4 produces sanitized evidence after release outcome is known | Evidence retention and access policy |

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
  postcondition uniqueness, receipt outcome consistency, and closed-bundle
  validation;
- reproducible exact direct dependencies plus a transitive lock or verified hashes;
- dependency provenance and license review; and
- a pinned conformance profile covering every Schema feature actually used.

Error-record ordering is by instance pointer, Schema resource ID, Schema pointer, and keyword, with a deterministic final tie-breaker defined by the chosen adapter. A command failure and a valid empty result must remain distinguishable.

## 14. Toolchain gate

No validator has been selected. No `pyproject.toml`, dependency declaration, transitive lock, or approved toolchain exists. Therefore executable Schema tests, fixtures that depend on executable validation, and Schema implementation remain blocked.

If Python is selected, `pyproject.toml` and an approved exact dependency lock are required. If another language is selected, its corresponding approved manifest and lock are required. Ad hoc imports, globally installed packages, and untracked environments are not acceptable evidence.

`integration-control` owns the dependency, packaging, lock, provenance, license, and release decision. `schema-contracts` owns the capability requirements in section 13 and the future conformance vectors. Selecting a package requires a separate authorization and does not belong to this design-record task.

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

Planned Schema contract tests cover every Schema accepting its positive fixtures and rejecting its negative fixtures; nested unknown-field rejection; discriminator and supported-version enforcement; mandatory formats; exact offline catalog and `$ref` resolution; no network requirement; strict parser failures before validation; canonical array checks; closed-bundle uniqueness and reference integrity; deterministic structured errors; catalog UUID/resource invariants; non-mutating NFC/JCS/digest vectors; and confirmation that no test treats synthetic host/runtime data, a valid TaskContract shape, or a receipt as authority.

Baseline and postcondition contract tests require duplicate-path validation to fail before hashing. They prove that deterministic full-object order cannot make a duplicate path valid and that entry arrays nested in required postconditions use the same sole `S(entry.path)` uniqueness and ordering rule as baseline index, tracked, and submodule entries.

ExecutionReceipt contract tests exercise both closed origin branches, conditional contract fields, every pre-contract denial checkpoint class, every permitted checkpoint/acquisition-state pair, rejection of every unlisted pair, pre-contract denials before and after lease acquisition, acquired-lease acquisition-result binding, and cleanup outcomes that succeed, fail, or remain indeterminate. They reject fabricated contract binding, non-acquired or indeterminate states carrying lease identity, any pre-contract receipt that claims successful execution, an indeterminate acquisition without an unresolved coordination warning, and an issued-contract failed or indeterminate release without an unresolved coordination warning. HostOverlay contract tests exercise one outer record per `remoteName`, non-empty nested accepted sets, `S(remoteName)` outer ordering, `J(remote)` nested ordering, and every duplicate or non-canonical remote-expectation fixture above.

### Mandatory exhaustive SG-001 fixture/conformance matrix

This matrix is mandatory future coverage, not a claim that fixtures or tests
exist. `Schema` means JSON Schema structural enforcement, `Phase 1 static`
means closed-data integrity after strict parsing and Schema validation,
`Phase 3 live` means repository, Git, filesystem, checkout, and lease
observation, and `Phase 4 evidence` means contract verification,
post-execution verification, sanitization, terminalization, or receipt
evidence. Each row requires every listed positive and negative vector.

| Branch or invariant | Required positive vectors | Required negative vectors | Enforcement layer and responsibility |
| --- | --- | --- | --- |
| Reference and HEAD | branch plus commit; branch plus unborn; detached plus commit | detached plus unborn; branch missing `branchRef`; detached containing `branchRef`; commit missing `objectId`; unborn containing `objectId` | Schema enforces closed branches and required/forbidden fields; Phase 1 static rejects detached/unborn; Phase 3 live selects and compares the actual ref and HEAD |
| Conflict-free index | clean conflict-free index; exact non-empty stage-0 complete inventory; exact empty complete inventory representing removal of all HEAD paths | stage `1`; stage `2`; stage `3`; duplicate path; unsupported mode; `intentToAdd: true`; `skipWorktree: true`; `assumeUnchanged: true`; sparse entry; unmerged index presented as a `TaskContract` baseline | Schema fixes stage and flags and closes entries; Phase 1 static enforces path identity, order, and complete explicit inventory; Phase 3 live selects clean versus exact and denies unrepresentable state; Phase 4 evidence may record sanitized pre-contract denial only |
| Tracked | tracked clean; exact inventory containing clean; modified with equal `worktreeMode` and `indexMode`; deleted; type-changed with unequal modes | modified with unequal modes; type-changed with equal modes; missing required field; branch-inapplicable field; mode `160000`; tracked/index mode mismatch; tracked/index object mismatch; omitted index path from `tracked.exact`; tracked entry for a gitlink path | Schema enforces status branches and fields; Phase 1 static enforces mode relations and explicit index equality/coverage; Phase 3 live confirms content, deletion, type, HEAD-dependent equality, and completeness; Phase 4 evidence verifies postconditions |
| Untracked and ignored / D3 path inventory | `none` for each category; non-empty exact complete inventories; regular, executable, and non-dereferenced symlink leaves; recursive ignored-directory leaves; ignore negation; empty directory emitting no member; registered submodule boundary exclusion | empty exact inventory; duplicate or non-canonical path; cross-category or explicit-state collision; directory member; collapsed-directory alternative; unregistered nested repository; unreadable, racing, cyclic, identity/classification/submodule-boundary-unresolved, unrepresentable-path, or unsupported-object observation | Schema enforces unions and non-empty exact arrays; Phase 1 static enforces `S(path)`, explicit disjointness, and rejection of directory/collapsed encodings; Phase 3 live executes the sole eleven-step leaf-only profile and emits its exact reason code; Phase 4 evidence verifies postconditions without a weaker encoding |
| Submodules / D2 orthogonal state | `none`; absent/unavailable; uninitialized/unavailable; initialized/observed with each of all eight Boolean triples; initialized checkout ID equal to and different from `recordedObjectId` | absent/observed; uninitialized/observed; initialized/unavailable; missing or branch-inapplicable `checkedOutObjectId`; fields on unavailable; each missing observed Boolean; unknown field; `indeterminate`; superseded `worktreeState`; `recordedObjectId` mismatch; missing mode-`160000` inventory path; tracked/submodule collision | Schema enforces the closed checkout and observation unions; Phase 1 static enforces all pairings, explicit gitlink equality, coverage, and disjointness; Phase 3 live denies inconclusive initialized observation with one of the four D2 reason codes; Phase 4 transitions and postconditions reuse the complete checkout/observation value |
| Active operations | one vector for each `merge`, `rebase`, `cherry-pick`, `revert`, `bisect`, `sequencer`, and `apply-mailbox` | duplicate operation; unknown operation; non-canonical order; empty exact array | Schema enforces vocabulary and non-empty exact shape; Phase 1 static enforces uniqueness and `S(value)` order; Phase 3 live observes operation state; Phase 4 evidence verifies postconditions |
| Administrative locks | one vector for each `index`, `packed-refs`, `shallow`, `config`, `head`, `ref`, and `other` branch | duplicate identity; missing `ref` identifier; forbidden `ref` on singleton branch; missing `other` identifier; forbidden identifier on non-`other` branch; non-canonical order; empty exact array | Schema enforces every closed branch; Phase 1 static enforces `L(lock)` identity and order; Phase 3 live observes locks; Phase 4 evidence verifies postconditions |
| Permitted transitions | one positive vector for each `ref-state`, `head-state`, `index-entry`, `tracked-entry`, `untracked-path`, `ignored-path`, `submodule-entry`, `active-operation`, and `administrative-lock` branch | identical `from` and `to`; duplicate target; unknown type; missing target key; branch-inapplicable key; invalid target comparator | Schema enforces branch shapes; Phase 1 static enforces exact inequality, target uniqueness, and the unchanged normative `T(transition)` comparator; Phase 3 live observes Git transitions; Phase 4 evidence attributes only authorized transitions |
| Required postconditions | one positive vector for each `scope-contained`, `ref-state`, `head-state`, `index-state`, `tracked-state`, `untracked-state`, `ignored-state`, `submodule-state`, `active-operations`, `administrative-locks`, and `lease-state` branch | missing `scope-contained`; multiple `scope-contained`; duplicate type; `scope-contained` containing `expected`; state branch missing `expected`; invalid lease-state truth-table combination | Schema enforces closed branch fields; Phase 1 static enforces type uniqueness and reused baseline semantics; Phase 3 live observes state and lease ownership; Phase 4 evidence verifies every required postcondition |
| Warnings and checks | warning without optional fields; warning with summary only; warning with an earlier `relatedCheckId`; warning with a later `relatedCheckId`; check without optional summaries; check with `expectedSummary`; check with `observedSummary`; check with both; one check for every `intent-validation`, `project-domain-resolution`, `role-routing`, `host-binding`, `initial-preflight`, `lease-acquisition`, `post-acquisition-revalidation`, `contract-issuance`, `pre-action-revalidation`, `execution`, `post-execution-verification`, `lease-release`, and `receipt-finalization` value | warning or check sequence gap; warning or check sequence duplicate; duplicate `checkId`; dangling `relatedCheckId`; reference resolved only by another receipt or a delivery result; invalid reason-code order; unknown `checkType`; branch-inapplicable or unknown field | Schema enforces record shapes and vocabularies; Phase 1 static enforces sequences, unique check IDs, reason-code order, and same-receipt references independent of position; Phase 4 evidence produces and sanitizes the ordered records |
| Receipt outcomes and lease acquisition | every existing issued-contract outcome vector; every existing pre-contract-denial outcome vector; each `not-required`, `not-attempted`, `not-acquired`, `indeterminate`, and `acquired` branch; every allowed checkpoint/acquisition chronology; acquired cleanup success, failure, and indeterminate; indeterminate acquisition with required warning; every release/lifecycle precedence branch | every prohibited checkpoint/acquisition chronology; acquired or indeterminate branch missing required binding or warning; inconsistent cleanup, release, execution, verification, or lifecycle outcome; successful lifecycle with unresolved warning | Schema enforces origin and union shape; Phase 1 static enforces chronology, binding, warnings, and precedence; Phase 3 live supplies acquisition and release facts; Phase 4 evidence finalizes the consistent receipt |
| TaskContract truth table | each of the four allowed rows: plan-only/plan-only/non-writing; implementation/plan-only/non-writing; implementation/implementation/non-writing; implementation/implementation/writing with required lease and owned postcondition | requested plan-only with effective implementation; effective plan-only with `allowWrite: true`; `allowWrite: false` with `leaseRequired: true`; `allowWrite: true` with `leaseRequired: false`; `leaseId` present while no lease is required; `leaseId` absent while required; `owned` postcondition while no lease is required; `not-required` postcondition while a lease is required | Schema and Phase 1 static enforce the closed four-row invariant; Phase 3 live validates required ownership; Phase 4 evidence validates authority, binding, release, and postconditions |
| D1 validated canonical instance representation | strict UTF-8 source produces one immutable closed JSON value bound to the selected schema-set revision and root `$id`, complete strict-parse/number/NFC/Schema/static/array proof, and retained original bytes or same-process provenance; digest replay uses that representation | generic decoded object; missing or stale proof component; proof rebound to another value; mutable value; representation asserted as a public kind, production typed model, transferable authority, TaskContract, or runtime artifact | `schema-contracts` defines and tests the Phase 1 static validation/codec boundary; later `model-implementation` owns production typed round trips and serializers; Phase 4 owns operational replay and authenticity |
| D4 raw worktree-content digest | exact empty, binary regular, executable, and link-target byte vectors reproduce their fixed tagged hashes; stable identity, kind, length, and metadata before/after observation | filtered or EOL-converted bytes; decoded or Unicode-normalized text; dereferenced symlink; unreadable, replaced, raced, truncated, length-inconsistent, or lossy observation; directory, gitlink, or unsupported type | Schema binds `trackedEntry.contentDigest` to one catalog profile; Phase 3 supplies identity-bound raw bytes; Phase 4 replays the same raw profile |
| D5 non-writing contracts | all three non-writing truth-table rows have exactly empty transitions, baseline-equal state postconditions, no lease identity, optional `lease-state: not-required`, and issued-receipt `changedPaths: []`; observed drift is evidence only | the independently enumerable Cartesian product of all three non-writing rows and all nine transition types (27 cases); any drift-describing state postcondition; lease identity/ownership; non-empty changed paths; `execute-tests` or `execute-build` treated as a write override | Schema and Phase 1 static reject the closed contract and compare explicit postconditions with the immutable baseline; Phase 4 enforces empty changed paths and classifies drift as failed or indeterminate verification |
| D6 execution/verification biconditional | `not-attempted/not-performed`; each of `succeeded`, `failed`, `cancelled`, and `indeterminate` with each of `passed`, `failed`, and `indeterminate` | exactly seven pairs: each attempted execution outcome with `not-performed`, plus `not-attempted` with `passed`, `failed`, or `indeterminate` | Phase 1 static applies the biconditional before, and without changing, the existing lifecycle-precedence table; Phase 4 supplies evidence claims |
| D7 simultaneous transition composition | complete materialized `B`; every `from` equals `B(target)` by direct JCS bytes; independent transitions produce the same canonical `F` regardless of wire order; unchanged targets persist; every changed dimension has an `F`-equal matching postcondition; unchanged postconditions are absent or baseline-equal | baseline/from mismatch; sequential dependency; order-dependent result; invalid final cross-dimension composite; missing or mismatched changed-dimension postcondition; drift asserted for an unchanged dimension; incomplete D2 or D3 value | Phase 1 performs comparison, simultaneous `Apply`, canonical branch reconstruction, and static final-composite validation; Phase 3 materializes live-dependent `B`; Phase 4 compares evidence with `F`, attributes transitions, and verifies scope/postconditions |
| D8 closed HostOverlay binding | complete branch and detached records with exactly `roleRef`, `worktreeId`, `repositoryRoot`, `expectedRef`, and non-empty canonical `remoteNames`; every name resolves once | each missing field; every unknown field; empty, duplicate, or non-canonical remote names; unknown name; branch without `branchRef`; detached with `branchRef`; `expectedBranch`; each cached observed root/HEAD/branch/remote field | Schema closes the five-field record and ref branches; Phase 1 enforces binding identity, array canon, and name resolution; Phase 3 compares live canonical root, registration, ref, and every named remote |
| D9 RoutingPolicy projection equality | different priorities; case- or pattern-different matches; sample-equivalent but structurally different patterns; equal match at different priorities reaches its assigned classification | different IDs with equal `RuleProjection` JCS bytes; same-priority equal `MatchProjection` JCS bytes with same or different decisions; non-canonical nested array rejected before projection | Phase 1 compares direct RFC 8785 bytes with no digest, case folding, rewriting, inference, host transformation, or array reorder; exact-duplicate classification precedes identical-match classification; Phase 2 alone executes matching |
| D10 HostOverlay narrowing proof | exact Project/role consistency; capabilities satisfying `Cportable` and `Cbinding`; repository and remote subsets by `J(remote)`; all binding names resolve; `src/lib/**` is included within Project `src/**` by DFA language proof | each of the nine exact rejection-code classes; added capability or remote; role/project mismatch; `docs/**` outside the Project universe; unsupported syntax, compilation failure, resource exhaustion, or indeterminate emptiness; sample or prefix heuristic offered as proof | Phase 1 performs exact set/reference checks and automata complement/product/emptiness relative to `U`; Phase 3 supplies live binding comparison; neither layer executes task routing here |
| D11 digest catalog and golden corpus | all eleven digest field paths bind once to ten computations; every exact separator, raw payload, JCS payload, exclusion, completed source value, tagged hash, and delivery-copy equality reproduces the recorded corpus | included-field mutation; excluded-field mishandling; self-digest inclusion; missing/changed separator byte; substituted profile; changed raw bytes; wrong JCS projection; mismatched copied receipt digest; a cycle, ambiguity, duplicate binding, or missing field path | Phase 1 static/codec conformance reproduces exact bytes and verifies the acyclic catalog; Phase 3 supplies stable raw observations; Phase 4 replays operational bindings and exact delivery copy; every digest remains integrity-only |
| D12 review-only capability complement | exactly four permitted sets: empty, inspect, validate, and inspect-plus-validate; each has `roleClass: review`, only plan-only mode, exact `C − P` prohibited set, and no exclusive write | each of the eleven non-observation capabilities permitted separately; wrong role or mode; missing complement member; permitted/prohibited overlap or other complement error; exclusive write; restoration attempted through another field | Schema and Phase 1 static enforce the complete five-class partition and exact equations; later intersections may only narrow the result and cannot restore a forbidden capability |
| Cross-dimension baselines | complete inventories rather than deltas; index/tracked field equality; gitlink/submodule object equality; tracked/submodule and untracked/ignored disjointness; canonical clean/none versus exact selection | omitted inventory member; index/tracked mode or object mismatch; gitlink/submodule mismatch; tracked/submodule collision; untracked/ignored collision; exact-path collision with explicit index, tracked, or submodule path; a Phase 1 check incorrectly depending on live state | Schema enforces local shape; Phase 1 static enforces relationships over explicit closed data; Phase 3 live owns HEAD-, object-, ignore-, filesystem-, checkout-, and index-dependent checks; Phase 4 evidence reuses the same postcondition semantics |
| Required summaries and five-state correction | pre-contract evidence with required `sanitizedSummary`; delivery result with required `sanitizedSummary`; warnings and checks omitting or including their optional summaries; all five acquisition states | pre-contract evidence missing `sanitizedSummary`; delivery result missing `sanitizedSummary`; any stale four-state-only validator or vector | Schema enforces record-specific presence; Phase 1 static runs the vectors; Phase 4 evidence establishes actual sanitization and the five-state lifecycle meaning |
| SG-002 numeric profile | every existing canonical-token, field-minimum, and field-maximum vector, with Git stage `0` as its only valid stage | Git stage `1`, `2`, `3`, and `4`; every existing signed, negative-zero, leading-plus, leading-zero, fractional, exponent, unsafe, NaN, Infinity, and field-out-of-range vector | Strict parsing and Phase 1 static enforce `profile.number.v1alpha1-r1` before conversion and exact field ranges; Phase 4 verification requires raw-token replay or the complete validated-representation proof |

The matrix contains 25 logical data rows, independently counted from the table.
It preserves all existing issued-contract and pre-contract outcome vectors,
the normative `T(transition)` definition, and the complete SG-002 vectors. A
future implementation is conformant only when every matrix cell is covered at
its assigned layer; a lower layer MUST NOT claim a live or evidence property
it cannot establish.

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
- a non-empty exact active-operation set and every administrative-lock branch;
- every permitted-transition branch and every required-postcondition branch;
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
- a duplicate active operation and duplicate administrative-lock identity;
- a transition with identical `from` and `to`, a duplicate transition target,
  an unknown transition type, and a missing branch target key;
- a duplicate postcondition type, missing `scope-contained`, and multiple
  `scope-contained` entries;
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
chronology and outcome consistency are evaluated deterministically; failed or
indeterminate release cannot omit unresolved coordination warnings; and warning
and check arrays preserve contiguous evidence sequence.

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
- typed models, decoding, canonical serialization implementation, and Schema/model conformance in the later distinct model worktree;
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
