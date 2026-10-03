# v1alpha1 S2 shared-vocabulary candidate

The integrated S1 package establishes the package layout, frozen catalog,
and offline registry for `contextctl.dev/v1alpha1`, Schema-set revision
`v1alpha1-r1`. The distribution is `agent-context-governance-schema` version
`0.0.0`; its import package is `contextctl_schema`. It is not a release or
an approved complete Schema baseline.

All 11 JSON files retain Draft 2020-12 and the exact reserved IDs from the
[integrated design](../../docs/schema-contract-v1alpha1.md#3-schema-set-revision-and-frozen-resource-catalog).
This unpublished S2 candidate replaces the common placeholder with reusable
`$defs` in `common.schema.json`. Consumers select a definition fragment;
common is a supporting vocabulary, not a resource dispatcher. The other ten
resources retain their exact S1 rejecting placeholders (`"not": {}`).
The seven concrete kind Schemas and the closed seven-kind `oneOf` dispatch in
`resource.schema.json` remain S3 work.

S2 covers Schema-expressible lexical, type, bound, enum, required-field,
closed-object, union, and local structural constraints. UUID and timestamp
formats must be asserted explicitly by a capable validator. Syntax does not
establish reference existence, chronology, path containment, trusted issuance,
or authorization. Strict decoding, models, routing, live Git inspection,
leases, runtime contract/receipt execution, CLI, adapters, and enforcement
remain outside S2.

`build_format_checker()` supplies the S0-approved project-owned explicit
checker for exactly `uuid` and `date-time`. It uses project-owned lexical
validation and Python standard-library UUID/calendar validation; no optional
jsonschema format dependency is required. Asserted formats must be passed
explicitly during validation with `format_checker=build_format_checker()`.
This adapter does not implement the future strict decoder or model codec,
cross-field chronology, or trusted-clock freshness.

## Canonical resources and packaging

The canonical JSON files live only in this directory. Hatchling copies their
exact bytes into `contextctl_schema/schemas/v1alpha1/` in the candidate wheel.
There is no second source-controlled copy under `src/`.

The immutable `CATALOG` contains 11 records. The record attributes
`resource_name`, `schema_set_revision`, `api_version`, `repository_path`,
`schema_id`, `kind`, and `dispatchable_kind` represent the design's
resourceName, schemaSetRevision, apiVersion, repository-relative path, exact
$id, kind, and dispatchableKind respectively.

`get_resource(resource_name)` performs exact resource-name lookup.
`lookup_kind(schema_set_revision, api_version, kind)` dispatches exactly
Project, Domain, WorktreeRole, RoutingPolicy, HostOverlay, TaskContract, and
ExecutionReceipt. Unknown names or tuples raise `KeyError`.
Common, resource, governance-bundle, and receipt-delivery-result are supporting
or container resources; their kind is null and they are not dispatchable.

`build_registry()` loads only the package's fixed catalog and explicitly
interprets each resource as Draft 2020-12. Unknown resources fail; the
retrieval callback cannot access a network or caller-selected filesystem path.
A fresh registry is built for each call. Library Registry immutability does
not make the JSON document dictionaries an instance-immutability contract.

## Evidence boundary

Registry tests preserve catalog identities, dispatch boundaries, local
resolution, missing-resource and missing-fragment failure, fresh-registry
isolation, and universal rejection by the ten remaining placeholders.
`test_common_profiles.py` reads the checkout's common Schema directly. Its
synthetic vectors distinguish structural/lexical evidence from asserted
timestamp format/calendar evidence and from deliberately Schema-valid values
that still require a deferred gate. All format assertions use the explicit
project checker, including the timestamp calendar vectors; optional library
checkers are not required and these vectors do not skip.
These tests are not full S7 conformance, strict-decoder evidence, model
conformance, or operational authorization.

The [shared definitions](../../docs/schema-contract-v1alpha1.md#6-shared-definitions)
and [validation matrix](../../docs/schema-contract-v1alpha1.md#12-structural-static-later-phase-and-external-control-matrix)
assign the remaining requirements as follows:

| Deferred requirement | Owner and boundary |
| --- | --- |
| Strict UTF-8 decoding, duplicate-key rejection, raw numeric-token spelling, Unicode-scalar and NFC validation | Future model implementation of the Phase-1 strict decoding contract, before ordinary conversion loses source information. |
| Complete Gregorian calendar/year semantics beyond Schema and the available asserted format checker; cross-field chronology | Phase-1 static validation; future model implementation supplies parser and instant-comparison conformance. Phase 4 supplies trusted current time. |
| Cross-instance uniqueness, canonical ordering, set equality, reference existence/association, detached/unborn and other cross-field consistency | Phase-1 static validation over a closed loaded set. Schema only provides shapes and directly expressible local checks. |
| Path-pattern semantic parsing and path-language inclusion/automata proofs over the valid repository-path universe | Phase-1 static validation. S2 rejects lexical violations but implements no matcher, parser, or inclusion engine. |
| Remote canonical ordering, outer remote-name uniqueness, exact membership/narrowing, and canonical equality | Phase-1 static validation. Local duplicate objects and namespace cardinality/component bounds are structural; the namespace bounds imply joined length at most 1023. |
| Typed models, codec, validated canonical representation, serialization, JCS, hash projections, replay, and cross-runtime conformance | Future model implementation in its distinct worktree after the complete Schema baseline is approved and integrated. |
| Task resolution, Domain coverage, RoutingPolicy evaluation, and role selection | Later operational phase: Phase 2. |
| Live filesystem/Git/worktree identity, containment, aliases, observed remotes, and leases | Later operational phase: Phase 3. |
| Trusted issuance/provenance, operational freshness, authorization, sanitization, scope verification, and contract/receipt execution and delivery | Later operational phase: Phase 4, with external trust and data-classification controls. |
| CLI, adapters, and operational enforcement | Later operational phases: CLI in Phase 5, adapters in Phase 6, composing the approved Phase 2–4 controls. |

The Windows CPython 3.13 dependency lock is generated from `pyproject.toml`
with the approved build, test, and tooling dependencies. Package tests must run
against the installed wheel in the separately authorized external environment.
S2 profile tests read the candidate Schema directly using already available
dependencies; a source-resource registry check is distinct from installed-wheel
evidence. Bytecode generation and the pytest cache must be disabled. A Windows lock and
test result make no Linux completeness or conformance claim.

Publication is UNPUBLISHED. The project license remains undecided. Independent
audit, integration-control approval, and separately authorized administrative
actions remain necessary before an implementation baseline can be integrated.
