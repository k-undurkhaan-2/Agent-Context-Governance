# v1alpha1 S1 package candidate

This unpublished S1 candidate establishes the package layout, frozen catalog,
and offline registry for `contextctl.dev/v1alpha1`, Schema-set revision
`v1alpha1-r1`. The distribution is `agent-context-governance-schema` version
`0.0.0`; its import package is `contextctl_schema`. It is not a release or
an approved complete Schema baseline.

All 11 JSON files are Draft 2020-12 placeholders with the exact reserved IDs
from the [integrated design](../../docs/schema-contract-v1alpha1.md#3-schema-set-revision-and-frozen-resource-catalog).
Each contains `"not": {}` and rejects every instance. Shared definitions and
resource semantics remain later, separately authorized S2/S3 work. S1 does
not implement resource properties, format checkers, strict instance decoding,
models, routing, authorization, Git inspection, leases, contracts, or receipts.

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

S1 tests exercise catalog identities, dispatch boundaries, local resolution,
missing-resource failure, and universal rejection by the placeholders.
They are not full S7 conformance, strict-decoder evidence, model conformance,
or operational authorization.

The Windows CPython 3.13 dependency lock is generated from `pyproject.toml`
with the approved build, test, and tooling dependencies. Tests must run
against the installed wheel in the separately authorized external environment,
with bytecode generation and the pytest cache disabled. A Windows lock and
test result make no Linux completeness or conformance claim.

Publication is UNPUBLISHED. The project license remains undecided. Independent
audit, integration-control approval, and separately authorized administrative
actions remain necessary before an implementation baseline can be integrated.
