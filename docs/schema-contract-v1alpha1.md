# contextctl.dev/v1alpha1 Schema Contract Design

Phase 1: Schemas and Models is current, but Schema implementation has not begun. This document is the proposed design contract for the first Schema baseline. Its governance status remains proposed until independent audit and `integration-control` approval are complete; it is not yet an approved or implementation-ready Schema contract. It is not a JSON Schema resource, configuration instance, execution adapter, policy engine, or authorization mechanism.

Nothing in this document grants operational authority. In particular, JSON-valid input shaped like a `TaskContract` is untrusted unless trusted framework logic issued it or validated its issuer, integrity, derivation, bindings, freshness, and current preconditions. A digest or successful Schema validation does not establish authority.

Concrete `HostOverlay`, `TaskContract`, `ExecutionReceipt`, lease, lock, runtime-state, and receipt-delivery records remain host-local and outside the target worktree and portable governance. The resource identifiers in this document are reserved for the first approved Schema baseline but remain unpublished.

## 1. Status, scope, and authority

The `schema-contracts` role owns the public JSON Schema contract under `schemas/v1alpha1/`, shared definitions, closed envelopes, Schema-expressible constraints, unknown-field rejection, conspicuously synthetic fixtures, Schema validation and contract tests, and directly required Schema documentation. It does not own Python models, decoding, canonical serialization implementation, task resolution, operational routing, live Git inspection, leases, contract issuance, receipt generation, a CLI, adapters, or enforcement.

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
| Canonical UUID | Lower-case canonical UUID string with `format: uuid` and a lexical pattern | Version-specific constraints where required | Identity does not prove issuer or ownership |
| Display text | Bounded string without control characters | Already NFC; fixture hygiene | Phase 4 sanitizes text copied into evidence; external classification still applies |
| Repository-relative path | POSIX `/` separators; no leading slash, drive prefix, backslash, empty segment, `.` segment, `..` segment, NUL, or trailing slash; maximum 4096 characters | Already NFC; canonical spelling and set ordering | Phase 3 resolves against the bound canonical root and checks containment live |
| Path pattern | Repository-relative grammar; `*` and `?` stay within a segment and `**` is allowed only as a complete segment; no negation, backslash, brace expansion, or host absolute syntax | Pattern parse succeeds; include/exclude relationships are statically checked where provable | Phase 2 resolves task coverage; Phase 3 checks concrete effects |
| Absolute host path | Closed object `{ platform, value }`, where `platform` is `windows` or `posix`; lexical checks only | Fixtures use conspicuously synthetic paths | Phase 3 canonicalizes, resolves aliases, and checks the real binding and containment |
| Object reference | Closed `{ apiVersion, kind, id }` object | Target kind, uniqueness, existence, and bundle association where applicable | Later phases bind the reference to the selected runtime object |
| Mode | Enum `plan-only` or `implementation` | `plan-only` with `allowWrite: true` is rejected | Phase 4 checks requested/effective mode against authority |
| `allowWrite` | Required Boolean where used; omission is never treated as true | Contradictory mode/write combinations rejected | Phase 3 lease and Phase 4 contract checks remain mandatory |
| Capability | Enum `inspect`, `validate`, `create`, `modify`, `delete`, `execute-tests`, `execute-build`, `git-stage`, `git-commit`, `git-branch`, `git-remote`, `network`, or `external-secret-use` | Unknown values and permitted/prohibited overlap rejected | Phases 2–4 calculate the restrictive intersection; the token itself grants nothing |
| Tagged digest | String `sha256:` followed by exactly 64 lower-case hexadecimal digits | Projection identifier and digest placement checked | Phase 4 verifies provenance and the exact protected bytes; a digest is not authentication |
| Git object ID | Closed `{ algorithm, value }`; `algorithm` is `sha1` or `sha256`, with 40 or 64 matching lower-case hex characters | Algorithm/value lengths agree | Phase 3 obtains and compares the live object ID |
| Branch reference | Fully qualified `refs/heads/...` string using a restricted Git-ref lexical profile | Allowed/denied policy contradictions checked | Phase 3 reads the symbolic branch or detached state live |
| HEAD state | Tagged closed union for `branch`, `detached`, or `unborn`; branch and object-ID fields are conditionally required | Union and local consistency | Phase 3 distinguishes unborn, detached, and symbolic states live |
| Timestamp | RFC 3339 UTC `date-time` ending in `Z` | Canonical lexical form | Phase 4 uses a trusted clock and checks freshness |
| Freshness boundary | Closed `{ issuedAt, expiresAt }` | Both timestamps present and `expiresAt` later than `issuedAt` | Phase 4 evaluates current time and policy bounds |
| Task, contract, lease, receipt ID | Canonical lower-case UUID; contract and receipt IDs narrow their envelope `metadata.id` | Uniqueness in the loaded artifact set | Trusted lifecycle logic checks ownership, derivation, and task binding |
| Structured remote | Closed `{ transport, host, port?, namespace, repository }`; transport is `https` or `ssh`; there is no user-info or credential field | Lower-case canonical host, omitted default port, unique canonical entries | Phase 3 compares configured remotes live without exposing credentials |
| Repository identity | Closed object with non-empty `acceptedRemotes` | Canonical uniqueness and portable-only content | Phase 3 observes and matches the target repository live |
| Remote expectation | Closed `{ remoteName, acceptedRemotes }`; `acceptedRemotes` is required and non-empty | One record per `remoteName`; outer records are unique and ordered by `S(remoteName)`, and nested remotes are unique and ordered by `J(remote)` | Phase 3 compares the observed Git remote for that name with the accepted set |
| Worktree logical identity | Logical `worktreeId` plus a `WorktreeRole` reference where required; never an absolute path | Reference existence in a closed set | Host binding and registration are checked in Phases 2–3 |
| Check outcome | Enum `passed`, `failed`, or `indeterminate` | — | Phase 4 records evidence without turning it into authority |
| Execution outcome | Enum `not-attempted`, `succeeded`, `failed`, `cancelled`, or `indeterminate` | — | Phase 4 derives it from the attempt |
| Verification outcome | Enum `not-attempted`, `passed`, `failed`, or `indeterminate` | — | Phase 4 derives it from post-execution verification |
| Release outcome | Enum `not-required`, `succeeded`, `failed`, or `indeterminate` | — | Phase 3 supplies ownership-checked release evidence |
| Lifecycle outcome | Enum `denied`, `succeeded`, `failed`, `cancelled`, or `indeterminate` | Cross-field combinations are structurally bounded | Phase 4 derives the terminal outcome; it does not imply lease release |
| Receipt-delivery outcome | Enum `not-attempted`, `succeeded`, `failed`, or `indeterminate` | — | Phase 4 records the post-finalization delivery attempt separately |
| Scope | Closed `{ capabilities, paths }` with both arrays present | Arrays canonical; allowed/prohibited sets disjoint and containment checked where statically provable | Phases 2–4 calculate effective scope and verify effects |
| Permitted transition | Closed object with `transitionId`, `from`, `to`, and repository-relative `paths` | Unique IDs, canonical paths, no internally contradictory transition | Phase 3/4 compare a live transition against immutable baseline authority |
| Required postcondition | Closed object with `postconditionId`, `type`, and a typed `expected` record whose entry/path arrays use baseline rules | Unique IDs and local expected-state consistency | Phase 4 checks fresh observations after execution |

A structured remote uses lower-case canonical host text and ordered `namespace` segments. Default transport ports must be omitted so equivalent remotes do not acquire multiple encodings. Secret-bearing URLs, user-info, tokens, private-key material, and environment-derived host data are not representable fields.

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

Owned and excluded Domains are disjoint and must exist in the same Project. A role may own multiple Domains. `reviewOnly: true` requires `roleClass: review`, excludes implementation mode and write capabilities, and does not become write-capable through another field. `roleClass: integration-control` identifies responsibility only; it grants no administrative operation. Branch deny rules win over allow rules during later evaluation. The object defines a logical responsibility profile, not a filesystem path or live worktree.

### `RoutingPolicy`

Required `spec` fields:

| Field | Design |
| --- | --- |
| `projectRef` | The Project for which the policy is defined |
| `rules` | Canonically ordered rule array |
| `fallback` | Closed decision fixed to explicit deny with a reason code |

Each rule is closed and contains `id`, integer `priority`, `match`, and `decision`. `match` contains an exact `projectRef` and a `domainSet` with non-empty `domainRefs` plus operator `exact` or `contains`. `decision` is a closed union: route to one `worktreeRoleRef`, or deny with one reason code. Every referenced role and Domain must belong to the policy Project, and a route target must statically own the rule’s declared Domains. Phase 1 applies only the static rules in section 9; actual matching and unique role selection remain Phase 2.

### `HostOverlay`

Required `spec` fields:

| Field | Design |
| --- | --- |
| `hostId` | Non-secret logical host-local identity; it is not proof of host identity |
| `projectRef` | One portable `Project` reference |
| `repositoryIdentity` | Restrictive local repository expectation |
| `bindings` | Role-to-worktree binding records containing `roleRef`, `worktreeId`, synthetic-capable absolute-path representation, and optional expected branch/remote names |
| `remoteExpectations` | Set-like closed records containing `remoteName` and required non-empty `acceptedRemotes` |
| `capabilityCeiling` | Canonical capability set that may only narrow customer governance |
| `pathCeiling` | Canonical repository-relative include/exclude arrays |
| `stateRoot` | Absolute host-path representation for future runtime state outside the target worktree |
| `lockRoot` | Absolute host-path representation for future coordination locks outside the target worktree |

Within one HostOverlay, `remoteName` is the sole identity of a remote-expectation record. The outer `remoteExpectations` array is set-like, contains at most one record for each name, and is unique and canonically ordered by `S(remoteName)`. Each record's `acceptedRemotes` is required, non-empty, set-like, unique, and canonically ordered by `J(remote)`. Multiple acceptable repository remotes for one configured Git remote name are represented inside that one record. Two outer records with the same `remoteName` are invalid even when their accepted remote values differ. Runtime comparison with the observed Git remote remains Phase 3. The structured representation cannot contain a credential-bearing URL, user-info, query, fragment, local file transport, token, or key path.

Bindings have unique `(roleRef, worktreeId)` keys. Static validation checks reference shape, uniqueness, absolute-path syntax, and canonical arrays. Closed-bundle static validation rejects a capability, path, role, or repository identity that visibly widens portable governance. Real path identity, branch, remote, registration, containment, and runtime state remain Phase 3 observations. The overlay has no secret field and no field for cached Git observations. Concrete overlay instances remain outside the target worktree.

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
| `expectedBaseline` | Immutable expected HEAD, index, tracked, untracked, ignored, submodule, active-operation, and administrative-lock conditions |
| `permittedTransitions` | Canonical set of explicitly permitted transition records |
| `requiredPostconditions` | Canonical set of postcondition records |
| `leaseRequired` | Explicit Boolean |
| `leaseId` | Canonical UUID, present exactly when a lease is required |
| `issuanceCheckpoint` | Closed observation timestamp and tagged state digest |
| `freshness` | Mandatory `issuedAt` and `expiresAt` boundary |

`expectedBaseline.index` and `.tracked` contain a condition plus canonical `entries`; `.untracked` and `.ignored` contain a condition plus canonical `paths`; `.submodules` contains a condition plus canonical `entries`. Entry objects are closed and keyed by repository-relative path, with the exact Git mode, status, and object-ID fields required by their category.

Every index, tracked, and submodule entry array in `expectedBaseline` MUST contain at most one entry for each repository-relative path. The same rule applies to every entry array nested in `requiredPostconditions` and to any transition or postcondition structure representing state keyed by repository-relative path. The sole uniqueness and canonical ordering key is `S(entry.path)`. Two entries with the same path are invalid even when their remaining fields differ. `J(entry)` MAY be used only for deterministic diagnostic comparison after path uniqueness has already been established; it MUST NOT participate in the uniqueness key, and full-object differences never make duplicate paths acceptable. Untracked and ignored path arrays, transition path arrays, and postcondition path arrays remain unique and canonically ordered by `S(path)`.

Local constraints reject `plan-only` with `allowWrite: true`, require `leaseRequired: true` whenever `allowWrite` is true, require `leaseId` exactly when `leaseRequired` is true, require non-empty Domains, require effective scope not to exceed requested scope structurally where provable, and require freshness ordering. Phase 1 can check reference and representation integrity but cannot prove trusted issuance, authenticate a digest, observe Git, establish current lease ownership, or grant authority because the JSON validates. Concrete contracts remain outside the target worktree.

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
| `sanitization` | Closed profile ID, applied flag, and completion timestamp |
| `receiptDigest` | Tagged digest over the versioned receipt projection that excludes this field |
| `startedAt` / `finishedAt` | Canonical UTC timestamps |

`spec.origin` is exactly one of these closed branches:

- **`issued-contract`:** requires `type` fixed to `issued-contract`, `contractId`, `contractDigest`, `resolvedTarget`, and `effectiveMode`. `resolvedTarget` contains the Project, role, logical worktree, and complete canonical Domain references. This branch represents every receipt produced after a trusted contract was issued. It forbids `denialCheckpoint`, `preContractEvidence`, and `leaseAcquisition`.
- **`pre-contract-denial`:** requires `type` fixed to `pre-contract-denial`, `denialCheckpoint`, `preContractEvidence`, and `leaseAcquisition`. It forbids `contractId`, `contractDigest`, `resolvedTarget`, and `effectiveMode`, so it cannot fabricate a contract or claim a fully authorized target.

`denialCheckpoint` is a closed vocabulary containing exactly `intent-validation`, `project-domain-resolution`, `role-routing`, `host-binding`, `initial-preflight`, `lease-acquisition`, `post-acquisition-revalidation`, and `contract-issuance`. It contains no checkpoint that occurs only after contract issuance.

`preContractEvidence` is a closed sanitized record requiring `observedAt`, a tagged `evidenceDigest` over its versioned evidence projection, a non-empty canonical `reasonCodes` set, and a bounded `sanitizedSummary`. Together with the receipt's ordered `checks`, it records enough evidence to explain the denial without asserting contract authority. It has no issuer, contract, absolute-host-path, secret, or authority-grant field. Structural validation cannot prove arbitrary summary text safe; Phase 4 sanitization and external controls remain required.

`leaseAcquisition` is one closed discriminated union with these states:

- `not-required`, `not-attempted`, and `not-acquired` each contain only their fixed `state` discriminator and therefore forbid `leaseId` and acquisition-result binding fields;
- `acquired` requires `state` fixed to `acquired`, a canonical `leaseId`, and a tagged `acquisitionResultDigest` that immutably binds the acquisition result.

Acquisition is concurrency evidence, never proof of authority. For a pre-contract denial with `leaseAcquisition.state: acquired`, `releaseOutcome` must be `succeeded`, `failed`, or `indeterminate` so ownership-checked cleanup is preserved. For the other three lease-acquisition states, `releaseOutcome` must be `not-required`. Every pre-contract-denial receipt requires `executionOutcome: not-attempted`, `verificationOutcome: not-attempted`, `lifecycleOutcome: denied`, and an empty `changedPaths` array. This permits denial evidence before lease acquisition, after failed acquisition, and after acquired-lease cleanup whether release succeeded, failed, or was indeterminate, without implying that acquisition authorized execution.

Every warning and check has required integer `sequence`; values are contiguous from zero and equal array position. A check also contains `checkId`, `outcome`, `expectedSummary`, `observedSummary`, `reasonCodes`, and `checkedAt`. Phase 1 validates structure, sequence continuity, ordering, origin-conditional fields, lease-evidence conditions, and local outcome consistency only. It cannot prove that summaries are safe, that checks occurred, or that outcomes are truthful. Receipt finalization occurs only after `releaseOutcome` is known. Future policy may require a pre-contract-denial receipt, but it remains optional unless that policy does so. Receipt delivery remains the separate post-finalization `ReceiptDeliveryResult`. A receipt grants no authority, cannot authorize a later task, does not imply lease release, and remains host-local evidence outside portable governance.

## 8. Supporting and container Schemas

The four non-kind resources do not increase the seven-kind count:

- `common.schema.json` contains shared `$defs` and has no object-kind discriminator.
- `resource.schema.json` is a closed `oneOf` dispatch surface referencing exactly the seven kind Schemas. It is not itself a governance kind.
- `governance-bundle.schema.json` is a closed non-kind container with `apiVersion`, one `project`, canonical `domains`, canonical `worktreeRoles`, and one `routingPolicy`. It contains portable customer governance only. It cannot contain a `HostOverlay`, `TaskContract`, `ExecutionReceipt`, receipt-delivery record, host path, lease, lock, or runtime state.
- `receipt-delivery-result.schema.json` is a closed non-kind record containing `apiVersion`, `receiptId`, `receiptDigest`, `outcome`, `attemptedAt`, canonical `reasonCodes`, and a bounded sanitized summary. It is produced after receipt finalization, cannot alter or replace the receipt, and grants no authority.

GovernanceBundle static validation checks unique IDs, exact reference existence and kinds, one coherent Project association, canonical arrays, routing reference integrity, Domain-overlap declarations, and role ownership declarations. It does not include a concrete HostOverlay and does not execute task resolution or routing. TaskContract and ExecutionReceipt validate independently against their own exact Schemas and selected schema-set revision.

## 9. RoutingPolicy priority semantics

The priority model is:

- rule IDs are unique;
- duplicate numeric priorities are allowed;
- rules with disjoint match conditions may share a priority;
- canonical rule order is priority descending and then ID ascending;
- Phase 1 rejects an exact normalized duplicate rule after ignoring its ID;
- Phase 1 rejects rules with the same priority and identical normalized match conditions, whether their decisions agree or conflict;
- Phase 1 may reject another contradiction only when it can prove it statically and deterministically, without resolving a real task;
- Phase 1 does not execute routing;
- Phase 2 collects all matching rules, finds the greatest matching priority, and fails closed when more than one rule matches at that priority, even when their decisions are identical;
- one highest-priority match yields its route or deny decision; and
- no match uses the required explicit deny fallback.

Global priority uniqueness is not required. Availability, host binding, and lease state cannot change rule priority or make an ineligible role eligible.

## 10. Non-mutating validation and canonicalization pipeline

Validation, canonicalization, hashing, and verification use these ten ordered steps:

1. Accept strict UTF-8 JSON bytes. Reject a BOM, malformed UTF-8, invalid Unicode scalar data, non-JSON numeric values, and values outside the selected RFC 8785-compatible number profile.
2. Parse with duplicate object-member detection. Reject duplicate keys before a normal object representation can discard them.
3. Inspect every decoded member name and string value. Reject anything not already Unicode NFC; do not normalize or rewrite it.
4. Perform structural validation against one explicitly selected schema-set revision using the fixed offline registry and mandatory format-assertion profile.
5. Perform Phase 1 static validation, including closed-bundle references, uniqueness, restrictions, local contradictions, and canonical identifiers.
6. Verify that every array already has the canonical order in section 11 and that evidence sequences are contiguous. Reject non-canonical order; do not sort.
7. Construct the explicitly versioned digest projection, such as excluding a receipt's own digest field, without mutating the source object.
8. Serialize that unchanged projection with RFC 8785 JSON Canonicalization Scheme.
9. Hash the exact JCS UTF-8 bytes with SHA-256 and encode the result as `sha256:` followed by lower-case hexadecimal.
10. Verification repeats the same pipeline and compares the result; it does not repair, normalize, sort, or migrate input.

There is no silent Unicode normalization, array sorting, or migration during loading, hashing, contract verification, or receipt verification. JCS sorts object property names but preserves string values and array order. A future formatter or migrator, if authorized, is a separate explicit operation that emits a new value and submits it to the complete pipeline from step 1.

## 11. Complete array-ordering matrix

Comparators are defined as follows:

- `S(value)` compares the already-NFC decoded string lexicographically by unsigned UTF-16 code units, matching JCS object-property ordering. It performs no locale comparison, case folding, or normalization.
- `R(ref)` is the componentwise tuple `S(ref.apiVersion)`, `S(ref.kind)`, `S(ref.id)`.
- `J(value)` is the unsigned bytewise lexicographic comparison of the value's RFC 8785 UTF-8 representation after all nested arrays have passed their own canonical checks.
- Tuple comparison is componentwise. Numeric priority comparison is ordinary integer comparison.
- A set-like array is valid only when its keys are strictly increasing; an equal key is a duplicate and is rejected.

| Array field | Classification | Required order or key |
| --- | --- | --- |
| `repositoryIdentity.acceptedRemotes` wherever used | Set-like | `J(remote)` after canonical remote checks |
| `remote.namespace` | Ordered by explicit semantics | Preserve namespace path-segment order |
| `permissions.modes` | Set-like | `S(value)` |
| `permissions.permittedCapabilities` | Set-like | `S(value)` |
| `permissions.prohibitedCapabilities` | Set-like | `S(value)` |
| `scope.capabilities` | Set-like | `S(value)` |
| `scope.paths` | Set-like | `S(path)` |
| `Project.domainRefs` | Set-like | `R(ref)` |
| `Project.worktreeRoleRefs` | Set-like | `R(ref)` |
| `Domain.pathScope.include` | Set-like | `S(pattern)` |
| `Domain.pathScope.exclude` | Set-like | `S(pattern)` |
| `Domain.overlapRefs` | Set-like | `R(ref)` |
| `WorktreeRole.ownedDomainRefs` | Set-like | `R(ref)` |
| `WorktreeRole.excludedDomainRefs` | Set-like | `R(ref)` |
| `WorktreeRole.branchPolicy.allowed.exact` | Set-like | `S(branchRef)` |
| `WorktreeRole.branchPolicy.allowed.prefixes` | Set-like | `S(prefix)` |
| `WorktreeRole.branchPolicy.denied.exact` | Set-like | `S(branchRef)` |
| `WorktreeRole.branchPolicy.denied.prefixes` | Set-like | `S(prefix)` |
| `RoutingPolicy.rules` | Ordered by explicit semantics | Priority descending, then `S(rule.id)` ascending |
| `RoutingPolicy.rules[].match.domainSet.domainRefs` | Set-like | `R(ref)` |
| `HostOverlay.bindings` | Set-like | `(R(roleRef), S(worktreeId))` |
| `HostOverlay.remoteExpectations` | Set-like | `S(remoteName)` |
| `HostOverlay.remoteExpectations[].acceptedRemotes` | Set-like | `J(remote)` after canonical remote checks |
| `HostOverlay.capabilityCeiling` | Set-like | `S(value)` |
| `HostOverlay.pathCeiling.include` | Set-like | `S(path)` |
| `HostOverlay.pathCeiling.exclude` | Set-like | `S(path)` |
| `TaskContract.domainRefs` | Set-like | `R(ref)` |
| `TaskContract.authorizedScope.capabilities` and `.paths` | Set-like | `S(value)` and `S(path)` respectively |
| `TaskContract.prohibitedScope.capabilities` and `.paths` | Set-like | `S(value)` and `S(path)` respectively |
| `TaskContract.expectedBaseline.index.entries` | Set-like | `S(entry.path)` |
| `TaskContract.expectedBaseline.tracked.entries` | Set-like | `S(entry.path)` |
| `TaskContract.expectedBaseline.untracked.paths` | Set-like | `S(path)` |
| `TaskContract.expectedBaseline.ignored.paths` | Set-like | `S(path)` |
| `TaskContract.expectedBaseline.submodules.entries` | Set-like | `S(entry.path)` |
| `TaskContract.permittedTransitions` | Set-like | `J(transition)`; nested `paths` use `S(path)` |
| `TaskContract.requiredPostconditions` | Set-like | `J(postcondition)`; every nested entry array uses `S(entry.path)` and every nested path array uses `S(path)` |
| `ExecutionReceipt.origin.resolvedTarget.domainRefs` (`issued-contract` branch) | Set-like | `R(ref)` |
| `ExecutionReceipt.origin.preContractEvidence.reasonCodes` (`pre-contract-denial` branch) | Set-like | `S(code)` |
| `ExecutionReceipt.unresolvedCoordinationWarnings` | Append-only evidence order | Required `sequence` equals position and is contiguous from 0 |
| `ExecutionReceipt.checks` | Append-only evidence order | Required `sequence` equals position and is contiguous from 0 |
| `ExecutionReceipt.checks[].reasonCodes` | Set-like | `S(code)` |
| `ExecutionReceipt.changedPaths` | Set-like | `S(path)` |
| `ExecutionReceipt.reasonCodes` | Set-like | `S(code)` |
| `ReceiptDeliveryResult.reasonCodes` | Set-like | `S(code)` |
| `GovernanceBundle.domains` | Set-like | `S(metadata.id)` |
| `GovernanceBundle.worktreeRoles` | Set-like | `S(metadata.id)` |

This matrix covers every instance array in the v1alpha1 design. Shared definitions use the same rule everywhere they are embedded. No v1alpha1 array is "order-insensitive but preserved on the wire." Adding such a field would make digests representation-sensitive and requires a new explicit design review. JCS never reorders an array.

## 12. Structural, static, later-phase, and external-control matrix

| Requirement | JSON Schema structural enforcement | Phase 1 static or fixture hygiene | Later operational enforcement | External control |
| --- | --- | --- | --- | --- |
| Required fields, types, enums, closed objects | Enforce | Contract vectors | Not applicable | Not applicable |
| Identifier, path, digest, UUID, and format syntax | Enforce lexical profile | Canonical spelling and cross-reference checks | Bind to trusted/live values where required | Not applicable |
| Duplicate JSON keys | Not observable after ordinary parsing | Strict pre-Schema parser rejects them | Same parser before later verification | Not applicable |
| Strings and member names already NFC | Not portable as an ordinary Schema assertion | Reject non-NFC before canonicalization | Repeat before hashing and verification | Authoring guidance |
| Reference existence, uniqueness, subset rules, canonical arrays | Shape only or partial uniqueness | Enforce within a closed loaded set | Revalidate selected/runtime bindings | Not applicable |
| `displayName` is non-identifying | Length and character shape only | Conspicuously synthetic fixtures and best-effort scanner | Sanitize if copied into Phase 4 evidence | Author review and data classification |
| Description text is secret-free | Length and character shape only | Synthetic values and best-effort secret scanning | Phase 4 redaction/sanitization before evidence | Secret manager, DLP, review, and access controls |
| A hostname is non-sensitive | Hostname syntax only | Reserved `.invalid` fixture hosts | Phase 4 redacts sensitive environment evidence | Environment classification and access control |
| A `sanitizedSummary` is actually safe | Bounded string shape only | Synthetic fixture content | Phase 4 sanitizer must create/check it and fail closed on incomplete sanitization | DLP, review, and evidence access policy |
| No secrets in arbitrary permitted strings | Unknown secret-like fields are rejected; allowed strings can still hold secrets | Best-effort scanners | Phase 4 redaction; no secret values in contracts or receipts | External secret delivery and incident handling |
| Absolute path denotes the intended worktree | Platform/value syntax only | Synthetic path hygiene | Phase 3 canonical path, alias, registration, and containment checks | Host filesystem permissions |
| Domain resolution and routing are unambiguous | Policy shape only | Provable contradictions only | Phase 2 resolves and fails closed | Not applicable |
| HostOverlay narrows customer governance | Shape and conditional fields | Static subset checks where provable | Phases 2-3 calculate the actual restrictive intersection | Host configuration review |
| HostOverlay remote expectations have one record per name and non-empty accepted sets | Enforce closed records and non-empty `acceptedRemotes` | Outer uniqueness and order use only `S(remoteName)`; nested remote uniqueness and order use `J(remote)` | Phase 3 compares each observed named Git remote with its accepted set | Credential handling remains outside governance |
| Baseline and postcondition state entries are unique by repository-relative path | Enforce entry shape and required path | Reject duplicate `S(entry.path)` before hashing, regardless of other entry fields | Phases 3-4 compare live state by the same path identity | Not applicable |
| Branch, HEAD, dirty state, operation, lock, and lease match | Expected-state representation only | Local consistency | Phase 3 observes live and coordinates leases | Repository and host protections |
| TaskContract is trusted, fresh, and authoritative | Representation only | Structural/static consistency | Phase 4 validates issuer, derivation, integrity, bindings, freshness, and current preconditions | Issuer/key/trust administration |
| Receipt origin, contract binding, and pre-contract lease evidence agree | Closed `oneOf` branches and conditional fields | Reject fabricated contract binding, invalid checkpoint/state combinations, and impossible pre-contract execution claims | Phase 4 records the applicable origin and finalizes only after release outcome is known | Evidence retention and access policy |
| Receipt accurately reports and remains non-authoritative | Representation and forbidden unknown fields | Local outcome consistency | Phase 4 produces sanitized evidence after release outcome is known | Evidence retention and access policy |

Schema cannot prove that arbitrary text is secret-free, a display name is non-identifying, a hostname is non-sensitive, or a sanitized summary is safe. Fixture hygiene and scanners are defense in depth, not proofs.

## 13. Validator capability requirements

A later selected validator and parser must provide all of the following:

- complete Draft 2020-12 support for every adopted core, applicator, validation, and format vocabulary feature;
- correct `$schema`, `$id`, `$defs`, absolute `$ref`, `const`, composition, conditional, and closed-object behavior;
- mandatory format assertion with positive and negative vectors for every enabled format;
- a fixed offline registry that supports arbitrary absolute URI schemes, including the exact UUID URNs in section 3;
- hard errors for missing resources and no network retrieval or fallback;
- local availability of the required Draft 2020-12 meta-schemas, either pinned through the dependency or vendored by an approved process;
- duplicate-key detection before Schema validation;
- strict UTF-8, Unicode-scalar, and RFC 8785-compatible number parsing;
- structured error access exposing the resource/schema ID, instance JSON Pointer, Schema JSON Pointer, and failing keyword;
- deterministic normalization and sorting of error records without assertions against vendor-specific message prose;
- hooks for Phase 1 static validation, canonical-array checks, and closed-bundle validation;
- reproducible exact direct dependencies plus a transitive lock or verified hashes;
- dependency provenance and license review; and
- a pinned conformance profile covering every Schema feature actually used.

Normalized error ordering is by instance pointer, Schema resource ID, Schema pointer, and keyword, with a deterministic final tie-breaker defined by the chosen adapter. A command failure and a valid empty result must remain distinguishable.

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
- valid plan-only TaskContract;
- valid write-shaped TaskContract with lease fields structurally consistent but no claim of authority;
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
- `plan-only` with `allowWrite: true`;
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
- duplicate TaskContract baseline submodule path with different object IDs or dirty state;
- duplicate required-postcondition entry path with different contents;
- issued-contract receipt origin missing `contractId`;
- issued-contract receipt origin missing `contractDigest`;
- issued-contract receipt origin containing pre-contract-denial-only fields;
- pre-contract-denial receipt origin containing `contractId`;
- pre-contract-denial receipt origin containing `contractDigest`;
- pre-contract-denial receipt missing `denialCheckpoint`;
- acquired lease state missing `leaseId`;
- acquired lease state missing `acquisitionResultDigest`;
- non-acquired lease state containing `leaseId`;
- pre-contract-denial receipt claiming successful execution;
- non-NFC string/member name, duplicate JSON key, malformed UTF-8, and unsupported number representation;
- non-canonical or duplicate set-like array entry and non-contiguous evidence sequence;
- exact normalized duplicate RoutingPolicy rule; and
- same-priority rules with identical normalized match conditions.

Duplicate priority by itself is not an invalid fixture. Context-dependent multiple-highest-match execution tests belong to Phase 2.

Planned Schema contract tests cover every Schema accepting its positive fixtures and rejecting its negative fixtures; nested unknown-field rejection; discriminator and supported-version enforcement; mandatory formats; exact offline catalog and `$ref` resolution; no network requirement; strict parser failures before validation; canonical array checks; closed-bundle uniqueness and reference integrity; deterministic structured errors; catalog UUID/resource invariants; non-mutating NFC/JCS/digest vectors; and confirmation that no test treats synthetic host/runtime data, a valid TaskContract shape, or a receipt as authority.

Baseline and postcondition contract tests require duplicate-path validation to fail before hashing. They prove that deterministic full-object order cannot make a duplicate path valid and that entry arrays nested in required postconditions use the same sole `S(entry.path)` uniqueness and ordering rule as baseline index, tracked, and submodule entries.

ExecutionReceipt contract tests exercise both closed origin branches, conditional contract fields, every pre-contract denial checkpoint class, pre-contract denials before and after lease acquisition, acquired-lease acquisition-result binding, and cleanup outcomes that succeed, fail, or remain indeterminate. They reject fabricated contract binding, non-acquired states carrying lease identity, and any pre-contract receipt that claims successful execution. HostOverlay contract tests exercise one outer record per `remoteName`, non-empty nested accepted sets, `S(remoteName)` outer ordering, `J(remote)` nested ordering, and every duplicate or non-canonical remote-expectation fixture above.

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
