"""Exact, immutable resource identities from the integrated v1alpha1 design."""

from dataclasses import dataclass
from types import MappingProxyType

SCHEMA_SET_REVISION = "v1alpha1-r1"
API_VERSION = "contextctl.dev/v1alpha1"


@dataclass(frozen=True, slots=True)
class ResourceRecord:
    """Catalog metadata only; this is not a governance instance model."""

    resource_name: str
    schema_set_revision: str
    api_version: str
    repository_path: str
    schema_id: str
    kind: str | None
    dispatchable_kind: bool


CATALOG: tuple[ResourceRecord, ...] = (
    ResourceRecord(
        "common.schema.json", SCHEMA_SET_REVISION, API_VERSION,
        "schemas/v1alpha1/common.schema.json",
        "urn:uuid:78833fbe-1819-45db-824c-2edb235f2864", None, False,
    ),
    ResourceRecord(
        "resource.schema.json", SCHEMA_SET_REVISION, API_VERSION,
        "schemas/v1alpha1/resource.schema.json",
        "urn:uuid:77fb943a-f8f8-491b-beaf-c1b4d9684801", None, False,
    ),
    ResourceRecord(
        "project.schema.json", SCHEMA_SET_REVISION, API_VERSION,
        "schemas/v1alpha1/project.schema.json",
        "urn:uuid:d5cecdb5-eadf-491d-80c6-869a7f4d10d9", "Project", True,
    ),
    ResourceRecord(
        "domain.schema.json", SCHEMA_SET_REVISION, API_VERSION,
        "schemas/v1alpha1/domain.schema.json",
        "urn:uuid:2bab91f3-c4d5-43e5-90f6-ffb786b42e65", "Domain", True,
    ),
    ResourceRecord(
        "worktree-role.schema.json", SCHEMA_SET_REVISION, API_VERSION,
        "schemas/v1alpha1/worktree-role.schema.json",
        "urn:uuid:4393a3fc-40da-41be-aca9-4276ddc752fa", "WorktreeRole", True,
    ),
    ResourceRecord(
        "routing-policy.schema.json", SCHEMA_SET_REVISION, API_VERSION,
        "schemas/v1alpha1/routing-policy.schema.json",
        "urn:uuid:5d929622-e8b2-40b4-80aa-5d8630625108", "RoutingPolicy", True,
    ),
    ResourceRecord(
        "host-overlay.schema.json", SCHEMA_SET_REVISION, API_VERSION,
        "schemas/v1alpha1/host-overlay.schema.json",
        "urn:uuid:c0de9354-1096-4cea-9cde-a33ad38ab313", "HostOverlay", True,
    ),
    ResourceRecord(
        "task-contract.schema.json", SCHEMA_SET_REVISION, API_VERSION,
        "schemas/v1alpha1/task-contract.schema.json",
        "urn:uuid:314c8f9e-2554-4ebc-b688-d48598693282", "TaskContract", True,
    ),
    ResourceRecord(
        "execution-receipt.schema.json", SCHEMA_SET_REVISION, API_VERSION,
        "schemas/v1alpha1/execution-receipt.schema.json",
        "urn:uuid:53faa365-c113-4b2d-a9c5-022cd87a21dd", "ExecutionReceipt", True,
    ),
    ResourceRecord(
        "governance-bundle.schema.json", SCHEMA_SET_REVISION, API_VERSION,
        "schemas/v1alpha1/governance-bundle.schema.json",
        "urn:uuid:e1293323-8af3-41ed-a55e-dc0c27f35206", None, False,
    ),
    ResourceRecord(
        "receipt-delivery-result.schema.json", SCHEMA_SET_REVISION, API_VERSION,
        "schemas/v1alpha1/receipt-delivery-result.schema.json",
        "urn:uuid:ffa1dcf4-5eb3-4a16-b1b2-be3bc1898684", None, False,
    ),
)

_BY_NAME = MappingProxyType({record.resource_name: record for record in CATALOG})
_BY_KIND = MappingProxyType({
    (record.schema_set_revision, record.api_version, record.kind): record
    for record in CATALOG
    if record.dispatchable_kind
})


def get_resource(resource_name: str) -> ResourceRecord:
    """Return an exact catalog entry; unknown names raise KeyError."""
    return _BY_NAME[resource_name]


def lookup_kind(
    schema_set_revision: str, api_version: str, kind: str
) -> ResourceRecord:
    """Dispatch only an exact approved revision/API/kind tuple."""
    return _BY_KIND[(schema_set_revision, api_version, kind)]
