# v1alpha1 S3 structural Schema candidate

This unpublished candidate implements the seven public kind Schemas and three
supporting/container resources for `contextctl.dev/v1alpha1`, Schema-set
revision `v1alpha1-r1`, on the integrated S2 shared vocabulary. All ten former
S1 rejecting placeholders have been replaced. The 53 definitions in
`common.schema.json`, catalog, registry implementation, format checker,
package metadata, and dependency lock remain unchanged.

The distribution remains `agent-context-governance-schema` version `0.0.0`,
with import package `contextctl_schema`. This candidate is not a release or an
approved complete Schema baseline. Structural acceptance grants no operational
authorization and establishes neither trusted issuance nor lease ownership.

## Frozen resources and dispatch

All 11 JSON resources retain Draft 2020-12 and their exact reserved IDs from
the [integrated design](../../docs/schema-contract-v1alpha1.md#3-schema-set-revision-and-frozen-resource-catalog).

| Resource group | Members and boundary |
| --- | --- |
| Seven dispatchable kinds | Project, Domain, WorktreeRole, RoutingPolicy, HostOverlay, TaskContract, ExecutionReceipt. Each has exact API/kind discrimination and a closed envelope, metadata, and spec. |
| Common vocabulary | `common.schema.json` supplies reusable `$defs`. It does not dispatch instances. |
| Resource dispatcher | `resource.schema.json` has exactly seven `oneOf` references, with no fallback. It is not a kind. |
| Portable container | `governance-bundle.schema.json` contains only apiVersion, Project, Domains, WorktreeRoles, and RoutingPolicy. It excludes host-local input and runtime artifacts. |
| Delivery evidence | `receipt-delivery-result.schema.json` is a closed non-kind record for post-finalization delivery evidence. It cannot replace a receipt or grant authority. |

HostOverlay instances remain host-local. TaskContract and ExecutionReceipt
instances remain runtime artifacts outside portable governance and the target
worktree. Inline test data are conspicuously synthetic, not generated runtime
artifacts.

The immutable catalog contains 11 records. `get_resource(resource_name)` uses
exact resource-name lookup. `lookup_kind(schema_set_revision, api_version,
kind)` recognizes exactly the seven kinds; unknown names or tuples raise
`KeyError`. Common, resource, governance-bundle, and receipt-delivery-result
have null catalog kinds and are not dispatchable.

Cross-resource references use the frozen absolute UUID URNs, optionally with
definition fragments. Resource-local definitions compose the frozen common
profiles. Project's permission definition is reused by Domain and WorktreeRole.
Receipt postcondition references reuse TaskContract's eleven-value type
definition. These definition references introduce no new kind.

## Structural coverage

S3 follows the design's [common envelope](../../docs/schema-contract-v1alpha1.md#5-common-envelope),
[seven object-kind designs](../../docs/schema-contract-v1alpha1.md#7-seven-object-kind-designs),
and [supporting resources](../../docs/schema-contract-v1alpha1.md#8-supporting-and-container-schemas).

The candidate enforces required fields, exact types/constants, unknown-field
rejection, shared lexical profiles, local duplicate-object rejection, finite
conditional relationships, and closed unions. These include secure defaults;
typed references; review-only capability complements; routing structure;
five-field host bindings; TaskContract's four mode/write/lease combinations,
nine baseline dimensions, four transition types and eleven postcondition types;
and receipt origin, check-outcome, acquisition-reference, finalization,
operation-record, and local outcome constraints.

Receipt conditions check serialized claims. They do not prove that checks
occurred, an acquisition Source exists, a lease is owned, or a release succeeded.
The local acquisition/release/carrier conditions preserve consequences of the
contract invariant; S4 must independently validate the complete referenced
TaskContract and acquisition Source.

UUID and timestamp formats must be asserted explicitly.
`build_format_checker()` supplies the unchanged project-owned checker for
exactly `uuid` and `date-time`, using standard-library UUID/calendar validation.
Pass `format_checker=build_format_checker()` during validation. Format
annotation alone is insufficient; no optional format dependency is needed.

## Deferred validation and operational boundaries

The [validation matrix](../../docs/schema-contract-v1alpha1.md#12-structural-static-later-phase-and-external-control-matrix)
continues to apply.

| Requirement | Owner and boundary |
| --- | --- |
| Strict UTF-8 decoding, duplicate instance keys, raw numeric-token spelling, Unicode scalar/NFC checking, and validated canonical representation | Future Phase-1 model/codec implementation. Parsing Schema source files in tests is not a governance-instance decoder. |
| Cross-resource ID uniqueness, reference existence and kind resolution, coherent Project association, Domain-overlap symmetry, and resolved role ownership | S4 static validation over closed configuration data. |
| Canonical ordering and identity-key uniqueness beyond local Schema constraints; arbitrary structured-value equality and set relationships | S4. `uniqueItems` rejects identical objects but does not prove uniqueness by an individual identity field. |
| Complete HostOverlay inventory, same-host exclusivity, remote-name identity, and permission/remote narrowing | S4 with complete trusted comparison context. One overlay's Schema validity is insufficient. |
| Path-pattern parsing, path-language inclusion/automata, scope containment, transition composition and capability closure | S4 where derivable from closed data; live effects and attribution remain later-phase work. |
| Timestamp chronology, final-check selection, contiguous sequences, receipt/contract/Source equalities, and digest acceptance | Separate static/codec gates. Local Schema relationships do not prove chronology, provenance, or event truth. |
| Full synthetic fixture corpus, lifecycle matrices and cross-runtime fixture assets | S5 and subsequent conformance work. S3 uses bounded inline structural vectors only. |
| Models, serialization, JCS, digest projection, hashing, replay and cross-runtime equivalence | Future model implementation in its distinct worktree after approval and integration of the complete Schema baseline. |
| Task/Project/Domain resolution, matching, priority evaluation and covering-role selection | Phase 2. |
| Live filesystem/Git identity, aliases, containment, observed remotes, runtime coordination and leases | Phase 3. |
| Trusted issuance, provenance, freshness, authorization, sanitization, scope verification, receipt generation and delivery | Phase 4, with external trust and data-classification controls. |
| CLI, adapters and operational enforcement | Phases 5 and 6, composing approved prior-phase controls. |

Schema cannot prove that descriptive text or a sanitized summary is safe.
Test identities use synthetic values and reserved `.invalid` names.

## Source validation and packaging

Canonical JSON resources live only in this directory. Existing packaging copies
their bytes into `contextctl_schema/schemas/v1alpha1/` in a candidate wheel;
no second source-controlled copy is added.

`build_registry()` loads only the fixed package catalog, explicitly using Draft
2020-12. Unknown resources and fragments fail; its retrieval callback has no
network or caller-selected filesystem fallback. Each call creates a fresh
registry. Registry immutability does not freeze the JSON dictionaries.

The five source test modules cover the frozen catalog, registry, common
profiles, seven kind Schemas, and supporting/container Schemas. Registry tests
bind the unchanged package-resource accessor to the fixed checkout root only
inside a test fixture. This verifies candidate source bytes without rebuilding
or reinstalling the package; it is not installed-wheel evidence. The new
structural tests also use the fixed checkout resources and explicit project
format checker.

Use the already approved dependencies and source package, with
`PYTHONDONTWRITEBYTECODE=1`, Python `-B`, and pytest `-p no:cacheprovider`.
Run exactly `test_catalog.py`, `test_registry.py`, `test_common_profiles.py`,
`test_resource_schemas.py`, and `test_container_schemas.py` under `tests/schema/`.
No dependency installation, package build, wheel installation, cache generation,
or runtime execution is part of the S3 implementation transaction.

Publication is UNPUBLISHED. The project license remains undecided. Independent
audit, integration-control approval, and separately authorized administrative
actions remain necessary before a complete implementation baseline is integrated.

## S4 static validation candidate

The separate `contextctl_schema.static_validation` module composes the frozen
S3 Schemas and format checker with static checks over supplied closed values.
Its six entry points cover GovernanceBundle, individual HostOverlay, complete
same-host inventory, TaskContract, ExecutionReceipt, and receipt/delivery pairs.
An individual overlay result does not establish complete-host acceptance.
The package root exports and the S3 structural resources remain unchanged.

Results distinguish `INVALID`, `PROOF_REQUIRED`, and `PASS`, record their exact
validation scope, and carry immutable diagnostic and proof-obligation tuples.
Known predicate failures take precedence over missing proof. A result with
unevaluated prerequisites cannot claim full static acceptance. Validation does
not repair or normalize supplied values, sort their arrays, or grant authority.

Direct checks cover exact references, canonical array order, static narrowing,
supplied baseline relationships, supported simultaneous transitions, receipt
identities, sequence-based selectors, chronology and outcome consistency.
Restricted path patterns use finite automata, complement relative to the valid
relative-path universe, product intersection and complete emptiness search.
Non-NFC accepted words are excluded exactly before another emptiness search;
there is no sample, prefix or host-filesystem fallback. Unsupported syntax,
unavailable proof and deterministic resource-limit exhaustion fail closed.

Full acceptance also requires opaque, bound external proofs for model-owned
input provenance, canonical comparisons, digest verification, complete host
snapshots and otherwise missing baseline operands. S4 supplies consumer ports
only. No production provider or public trust-registration interface exists in
this candidate. A decoded mapping or caller assertion cannot establish trust.
The private synthetic test doubles exercise consumer behavior only; their
placeholder digest strings are not evidence of codec conformance.

Strict decoding, canonical representation, RFC 8785 serialization, digest
projections, hashing and replay remain model/codec work. S4 performs no actual
task routing, live Git or filesystem inspection, leases, contract issuance,
receipt generation, current-time authorization or operational enforcement.
Those Phase 2/3/4 responsibilities remain outside this validation surface.

The eleven `test_static_*.py` modules and `s4_synthetic.py` contain bounded
synthetic vectors. They are separate from the five frozen S3 test modules and
do not create the S5 fixture corpus. Run with the approved source-test runtime,
no bytecode and no pytest cache; evidence stays outside repository worktrees.
This candidate still requires test evidence and independent audit. It does not
declare the complete Schema baseline ready or authorize staging or publication.
