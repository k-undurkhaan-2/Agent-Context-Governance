"""Bounded S3 structural vectors; all identities, paths and digests are synthetic.

These inline dictionaries are not a fixture corpus, runtime artifacts, models,
digest-verification evidence, or operational authorization. S4 cross-resource
proofs and S5/S7 corpus/conformance work remain separate.
"""

from copy import deepcopy
from functools import lru_cache
from itertools import product
import json
from pathlib import Path
from unittest.mock import patch

import pytest
from jsonschema import Draft202012Validator

from contextctl_schema import build_format_checker
from contextctl_schema.catalog import API_VERSION, CATALOG, get_resource
from contextctl_schema.registry import build_registry

ROOT = Path(__file__).resolve().parents[2]
KINDS = {
    "Project": "project",
    "Domain": "domain",
    "WorktreeRole": "worktree-role",
    "RoutingPolicy": "routing-policy",
    "HostOverlay": "host-overlay",
    "TaskContract": "task-contract",
    "ExecutionReceipt": "execution-receipt",
}
CAPABILITIES = [
    "create", "delete", "execute-build", "execute-tests", "external-secret-use",
    "git-branch", "git-commit", "git-remote", "git-stage", "inspect", "modify",
    "network", "validate",
]
TASK_ID = "00000000-0000-4000-8000-000000000001"
CONTRACT_ID = "00000000-0000-4000-8000-000000000002"
RECEIPT_ID = "00000000-0000-4000-8000-000000000003"
LEASE_ID = "00000000-0000-4000-8000-000000000004"
DIGEST = "sha256:" + "0" * 64
TIME = "2000-01-01T00:00:00Z"
OID = {"algorithm": "sha1", "value": "a" * 40}
G_CHECKS = [
    "intent-validation", "project-domain-resolution", "role-routing",
    "host-binding", "initial-preflight",
]


@lru_cache
def source_registry():
    # Fixed checkout root, only for source validation. Production retrieval
    # remains unchanged and takes no caller-selected path.
    with patch("contextctl_schema.registry.files", return_value=ROOT):
        return build_registry()


@lru_cache
def validator(name, fragment=""):
    record = get_resource(name + ".schema.json")
    registry = source_registry()
    schema = {"$ref": record.schema_id + fragment}
    return Draft202012Validator(
        schema, registry=registry, format_checker=build_format_checker()
    )


def reference(kind, identifier=None):
    defaults = {
        "Project": "project.invalid", "Domain": "domain.invalid",
        "WorktreeRole": "role.invalid", "RoutingPolicy": "routing.invalid",
    }
    return {"apiVersion": API_VERSION, "kind": kind,
            "id": identifier or defaults[kind]}


def permissions():
    return {"modes": ["plan-only"], "permittedCapabilities": ["inspect"],
            "prohibitedCapabilities": []}


def repository_identity():
    return {"acceptedRemotes": [{
        "transport": "https", "host": "repo.invalid",
        "namespace": ["synthetic"], "repository": "governance",
    }]}


def check(check_type, outcome="passed", sequence=0):
    return {
        "sequence": sequence, "checkId": "check." + check_type,
        "checkType": check_type, "outcome": outcome, "observedAt": TIME,
        "profileId": "profile.validation.v1", "reasonCodes": [],
    }


def project_spec():
    return {
        "repositoryIdentity": repository_identity(),
        "secureDefaults": {"mode": "plan-only", "allowWrite": False},
        "permissions": permissions(), "domainRefs": [reference("Domain")],
        "worktreeRoleRefs": [reference("WorktreeRole")],
        "routingPolicyRef": reference("RoutingPolicy"),
    }


def domain_spec():
    return {
        "projectRef": reference("Project"),
        "responsibility": "Conspicuously synthetic structural test domain.",
        "pathScope": {"include": ["synthetic/**"], "exclude": []},
        "permissions": permissions(), "overlapRefs": [],
    }


def role_spec():
    return {
        "projectRef": reference("Project"), "roleClass": "implementation",
        "ownedDomainRefs": [reference("Domain")], "excludedDomainRefs": [],
        "permissions": permissions(),
        "branchPolicy": {
            "allowed": {"exact": ["refs/heads/synthetic"], "prefixes": []},
            "denied": {"exact": [], "prefixes": []},
        },
        "cleanlinessPolicy": {
            "tracked": "clean", "untracked": "none", "ignored": "none",
            "index": "clean", "submodules": "none",
        },
        "exclusiveWriteRequired": False, "reviewOnly": False,
    }


def routing_spec():
    return {
        "projectRef": reference("Project"),
        "rules": [{
            "id": "rule.invalid", "priority": 1,
            "match": {
                "projectRef": reference("Project"),
                "domainSet": {"operator": "exact",
                              "domainRefs": [reference("Domain")]},
            },
            "decision": {"type": "route",
                         "worktreeRoleRef": reference("WorktreeRole")},
        }],
        "fallback": {"type": "deny", "reasonCode": "reason.synthetic.denied"},
    }


def overlay_spec():
    return {
        "hostId": "host.invalid", "projectRef": reference("Project"),
        "repositoryIdentity": repository_identity(),
        "bindings": [{
            "roleRef": reference("WorktreeRole"), "worktreeId": "worktree.invalid",
            "repositoryRoot": {"platform": "posix",
                               "value": "/srv/synthetic.invalid/worktree"},
            "expectedRef": {"state": "branch", "branchRef": "refs/heads/synthetic"},
            "remoteNames": ["origin"],
        }],
        "remoteExpectations": [{
            "remoteName": "origin",
            "acceptedRemotes": repository_identity()["acceptedRemotes"],
        }],
        "capabilityCeiling": ["inspect"],
        "pathCeiling": {"include": ["synthetic/**"], "exclude": []},
        "stateRoot": {"platform": "posix", "value": "/srv/synthetic.invalid/state"},
        "lockRoot": {"platform": "posix", "value": "/srv/synthetic.invalid/locks"},
    }


def contract_spec(write=False):
    spec = {
        "contractVersion": "1", "taskId": TASK_ID,
        "projectRef": reference("Project"), "repositoryIdentity": repository_identity(),
        "target": {"worktreeId": "worktree.invalid",
                   "worktreeRoleRef": reference("WorktreeRole")},
        "domainRefs": [reference("Domain")],
        "issuer": {"issuerId": "issuer.invalid", "issuanceMethod": "trusted-framework",
                   "derivationDigest": DIGEST},
        "digests": {name: DIGEST for name in
                    ["policyDigest", "configurationDigest", "taskIntentDigest"]},
        "requestedMode": "plan-only", "effectiveMode": "plan-only",
        "allowWrite": False,
        "authorizedScope": {"capabilities": ["inspect"], "paths": ["synthetic/**"]},
        "prohibitedScope": {"capabilities": [], "paths": []},
        "expectedBaseline": {
            "ref": {"state": "branch", "branchRef": "refs/heads/synthetic"},
            "head": {"state": "unborn"}, "index": {"state": "clean"},
            "tracked": {"state": "clean"}, "untracked": {"state": "none"},
            "ignored": {"state": "none"}, "submodules": {"state": "none"},
            "activeOperations": {"state": "none"},
            "administrativeLocks": {"state": "none"},
        },
        "permittedTransitions": [], "requiredPostconditions": [{"type": "scope-contained"}],
        "leaseRequired": False,
        "issuanceCheckpoint": {"observedAt": TIME, "stateDigest": DIGEST},
        "freshness": {"issuedAt": TIME, "expiresAt": "2000-01-01T00:01:00Z"},
    }
    if write:
        spec.update(requestedMode="implementation", effectiveMode="implementation",
                    allowWrite=True, leaseRequired=True, leaseId=LEASE_ID)
        spec["authorizedScope"]["capabilities"] = ["create", "delete", "git-stage", "inspect", "modify"]
    return spec


def receipt_spec():
    types = G_CHECKS + [
        "pre-issuance-revalidation", "contract-issuance", "pre-action-revalidation",
        "execution", "post-execution-verification", "receipt-finalization",
    ]
    checks = [check(t, "succeeded" if t == "execution" else "passed", i)
              for i, t in enumerate(types)]
    checks[-2]["postconditionRef"] = {"type": "scope-contained"}
    return {
        "receiptVersion": "1", "taskId": TASK_ID,
        "origin": {
            "type": "issued-contract", "contractId": CONTRACT_ID,
            "contractDigest": DIGEST, "effectiveMode": "plan-only",
            "resolvedTarget": {
                "projectRef": reference("Project"),
                "worktreeRoleRef": reference("WorktreeRole"),
                "worktreeId": "worktree.invalid", "domainRefs": [reference("Domain")],
            },
        },
        "executionOutcome": "succeeded", "verificationOutcome": "passed",
        "releaseOutcome": "not-required", "lifecycleOutcome": "succeeded",
        "unresolvedCoordinationWarnings": [], "checks": checks, "changedPaths": [],
        "reasonCodes": [], "sanitization": {
            "profileId": "profile.sanitization.v1", "applied": True,
            "redactionCount": 0, "completedAt": TIME,
        },
        "receiptDigest": DIGEST, "startedAt": TIME, "finishedAt": TIME,
    }


FACTORIES = {
    "Project": project_spec, "Domain": domain_spec, "WorktreeRole": role_spec,
    "RoutingPolicy": routing_spec, "HostOverlay": overlay_spec,
    "TaskContract": contract_spec, "ExecutionReceipt": receipt_spec,
}


def resource(kind):
    identifier = {
        "TaskContract": CONTRACT_ID, "ExecutionReceipt": RECEIPT_ID,
    }.get(kind, "synthetic.invalid")
    return {"apiVersion": API_VERSION, "kind": kind,
            "metadata": {"id": identifier}, "spec": FACTORIES[kind]()}


def assert_valid(kind, value):
    validator(KINDS[kind]).validate(value)


def assert_invalid(kind, value):
    assert not validator(KINDS[kind]).is_valid(value)


def object_paths(value, path=()):
    if isinstance(value, dict):
        yield path
        for key, child in value.items():
            yield from object_paths(child, (*path, key))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from object_paths(child, (*path, index))


def at(value, path):
    for key in path:
        value = value[key]
    return value


@pytest.mark.parametrize("kind", KINDS)
def test_seven_structural_positive_resources(kind):
    assert_valid(kind, resource(kind))


@pytest.mark.parametrize("kind", KINDS)
@pytest.mark.parametrize("change", [
    "wrong-api", "wrong-kind", "extra",
    "missing-apiVersion", "missing-kind", "missing-metadata", "missing-spec",
])
def test_closed_required_envelopes(kind, change):
    value = resource(kind)
    if change == "wrong-api":
        value["apiVersion"] = "contextctl.dev/v1alpha2"
    elif change == "wrong-kind":
        value["kind"] = "Unknown"
    elif change == "extra":
        value["unexpected"] = True
    else:
        del value[change.removeprefix("missing-")]
    assert_invalid(kind, value)


@pytest.mark.parametrize("kind", KINDS)
@pytest.mark.parametrize("value", [None, False, 1, "synthetic", []])
def test_resource_requires_object(kind, value):
    assert_invalid(kind, value)


@pytest.mark.parametrize("kind", KINDS)
def test_nested_objects_reject_unknown_fields(kind):
    original = resource(kind)
    for path in object_paths(original):
        value = deepcopy(original)
        at(value, path)["unexpected"] = "synthetic"
        assert not validator(KINDS[kind]).is_valid(value), path


@pytest.mark.parametrize("kind", KINDS)
def test_required_spec_members(kind):
    original = resource(kind)
    for name in original["spec"]:
        value = deepcopy(original)
        del value["spec"][name]
        assert not validator(KINDS[kind]).is_valid(value), name


@pytest.mark.parametrize("kind", KINDS)
def test_reference_kind_and_version_are_structural(kind):
    original = resource(kind)
    for path in object_paths(original):
        node = at(original, path)
        if set(node) == {"apiVersion", "kind", "id"}:
            for field, replacement in [("kind", "HostOverlay"), ("apiVersion", "unknown")]:
                value = deepcopy(original)
                at(value, path)[field] = replacement
                assert not validator(KINDS[kind]).is_valid(value), (path, field)


@pytest.mark.parametrize("kind", KINDS)
def test_metadata_shape(kind):
    value = resource(kind)
    value["metadata"].update(displayName="Synthetic display", description="Synthetic description.")
    assert_valid(kind, value)
    for field, bad in [("id", "Bad Identity"), ("displayName", "x" * 129),
                       ("description", "x" * 1025), ("displayName", "line\nbreak")]:
        mutated = deepcopy(value)
        mutated["metadata"][field] = bad
        assert_invalid(kind, mutated)


@pytest.mark.parametrize("kind", ["TaskContract", "ExecutionReceipt"])
def test_runtime_metadata_requires_uuid(kind):
    value = resource(kind)
    value["metadata"]["id"] = "synthetic.invalid"
    assert_invalid(kind, value)


@pytest.mark.parametrize("kind", ["Project", "Domain", "WorktreeRole"])
def test_permission_closure(kind):
    value = resource(kind)
    value["spec"]["permissions"]["prohibitedCapabilities"] = ["inspect"]
    assert_invalid(kind, value)
    value["spec"]["permissions"]["prohibitedCapabilities"] = []
    value["spec"]["permissions"]["permittedCapabilities"] = ["unknown"]
    assert_invalid(kind, value)


def test_project_secure_defaults_and_required_reference_sets():
    for field, bad in [("secureDefaults", {"mode": "implementation", "allowWrite": True}),
                       ("domainRefs", []), ("worktreeRoleRefs", []),
                       ("repositoryIdentity", {"acceptedRemotes": []})]:
        value = resource("Project")
        value["spec"][field] = bad
        assert_invalid("Project", value)


def test_domain_path_scope():
    value = resource("Domain")
    del value["spec"]["pathScope"]["exclude"]
    assert_valid("Domain", value)
    for paths in [[], [".git/**"], ["/synthetic"], ["synthetic/**", "synthetic/**"]]:
        value["spec"]["pathScope"]["include"] = paths
        assert_invalid("Domain", value)


@pytest.mark.parametrize("permitted", [[], ["inspect"], ["validate"], ["inspect", "validate"]])
def test_review_only_exact_permission_complements(permitted):
    value = resource("WorktreeRole")
    value["spec"].update(roleClass="review", reviewOnly=True)
    value["spec"]["permissions"] = {
        "modes": ["plan-only"], "permittedCapabilities": permitted,
        "prohibitedCapabilities": sorted(set(CAPABILITIES) - set(permitted)),
    }
    assert_valid("WorktreeRole", value)
    for field, bad in [("roleClass", "implementation"), ("exclusiveWriteRequired", True)]:
        mutated = deepcopy(value)
        mutated["spec"][field] = bad
        assert_invalid("WorktreeRole", mutated)
    mutated = deepcopy(value)
    mutated["spec"]["permissions"]["prohibitedCapabilities"].pop()
    assert_invalid("WorktreeRole", mutated)


@pytest.mark.parametrize("capability", [c for c in CAPABILITIES if c not in ["inspect", "validate"]])
def test_review_cannot_permit_non_observation_capability(capability):
    value = resource("WorktreeRole")
    value["spec"].update(roleClass="review", reviewOnly=True)
    value["spec"]["permissions"] = {
        "modes": ["plan-only"], "permittedCapabilities": [capability],
        "prohibitedCapabilities": sorted(set(CAPABILITIES) - {capability}),
    }
    assert_invalid("WorktreeRole", value)


@pytest.mark.parametrize("priority,valid", [(0, True), (1000, True), (-1, False), (1001, False), (True, False), (1.5, False)])
def test_routing_priority_bounds(priority, valid):
    value = resource("RoutingPolicy")
    value["spec"]["rules"][0]["priority"] = priority
    assert validator("routing-policy").is_valid(value) is valid


def test_routing_decision_and_match_unions():
    value = resource("RoutingPolicy")
    rule = value["spec"]["rules"][0]
    rule["match"]["domainSet"]["operator"] = "contains"
    rule["decision"] = {"type": "deny", "reasonCode": "reason.synthetic.denied"}
    assert_valid("RoutingPolicy", value)
    for bad in [{"type": "route"}, {"type": "deny"}, {"type": "unknown"},
                {"type": "deny", "reasonCode": "reason.synthetic.denied",
                 "worktreeRoleRef": reference("WorktreeRole")}]:
        rule["decision"] = bad
        assert_invalid("RoutingPolicy", value)
    value = resource("RoutingPolicy")
    value["spec"]["fallback"] = deepcopy(value["spec"]["rules"][0]["decision"])
    assert_invalid("RoutingPolicy", value)


def test_host_binding_closed_shape():
    value = resource("HostOverlay")
    binding = value["spec"]["bindings"][0]
    binding["expectedRef"] = {"state": "detached"}
    value["spec"]["pathCeiling"]["include"] = []
    assert_valid("HostOverlay", value)
    for field, bad in [
        ("expectedRef", {"state": "detached", "branchRef": "refs/heads/synthetic"}),
        ("remoteNames", []), ("remoteNames", ["origin", "origin"]),
        ("repositoryRoot", {"platform": "windows", "value": r"\\synthetic.invalid\share"}),
    ]:
        mutated = deepcopy(value)
        mutated["spec"]["bindings"][0][field] = bad
        assert_invalid("HostOverlay", mutated)
    value["spec"]["remoteExpectations"][0]["acceptedRemotes"] = []
    assert_invalid("HostOverlay", value)


@pytest.mark.parametrize("requested,effective,write,lease,present",
                         tuple(product(["plan-only", "implementation"], ["plan-only", "implementation"],
                                       [False, True], [False, True], [False, True])))
def test_contract_mode_write_lease_truth_table(requested, effective, write, lease, present):
    value = resource("TaskContract")
    spec = value["spec"]
    spec.update(requestedMode=requested, effectiveMode=effective,
                allowWrite=write, leaseRequired=lease)
    if present:
        spec["leaseId"] = LEASE_ID
    expected = (
        lease == write and present == write
        and (requested != "plan-only" or effective == "plan-only")
        and (not write or effective == "implementation")
    )
    assert validator("task-contract").is_valid(value) is expected


@pytest.mark.parametrize("dimension", [
    "ref", "head", "index", "tracked", "untracked", "ignored", "submodules",
    "activeOperations", "administrativeLocks",
])
def test_baseline_requires_all_nine_dimensions(dimension):
    value = resource("TaskContract")
    del value["spec"]["expectedBaseline"][dimension]
    assert_invalid("TaskContract", value)


def index_state():
    return {"stage": 0, "mode": "100644", "objectId": deepcopy(OID),
            "intentToAdd": False, "skipWorktree": False, "assumeUnchanged": False}


def tracked_state(status="modified"):
    state = {"status": status, "indexMode": "100644", "indexObjectId": deepcopy(OID)}
    if status in ["modified", "type-changed"]:
        state.update(worktreeMode="120000" if status == "type-changed" else "100644",
                     contentDigest=DIGEST)
    return state


def test_index_profile_and_empty_exact_inventory():
    value = resource("TaskContract")
    baseline = value["spec"]["expectedBaseline"]
    baseline["head"] = {"state": "commit", "objectId": deepcopy(OID)}
    baseline["index"] = {"state": "exact", "entries": []}
    assert_valid("TaskContract", value)
    entry = {"path": "synthetic/file.txt", **index_state()}
    baseline["index"]["entries"] = [entry]
    assert_valid("TaskContract", value)
    for field, bad in [("stage", 1), ("stage", 3), ("mode", "040000"),
                       ("mode", 100644), ("intentToAdd", True),
                       ("skipWorktree", True), ("assumeUnchanged", True)]:
        mutated = deepcopy(value)
        mutated["spec"]["expectedBaseline"]["index"]["entries"][0][field] = bad
        assert_invalid("TaskContract", mutated)


@pytest.mark.parametrize("status", ["clean", "modified", "deleted", "type-changed"])
def test_tracked_entry_status_branches(status):
    v = validator("task-contract", "#/$defs/trackedEntry")
    entry = {"path": "synthetic/file.txt", **tracked_state(status)}
    v.validate(entry)
    mutated = deepcopy(entry)
    mutated["indexMode"] = "160000"
    assert not v.is_valid(mutated)
    if status in ["clean", "deleted"]:
        entry["contentDigest"] = DIGEST
    else:
        entry["worktreeMode"] = "100644" if status == "type-changed" else "120000"
    assert not v.is_valid(entry)


def test_baseline_local_invariants():
    value = resource("TaskContract")
    for dimension, condition in [
        ("ref", {"state": "detached"}),
        ("tracked", {"state": "exact", "entries": []}),
        ("tracked", {"state": "exact", "entries": [
            {"path": "synthetic/file.txt", **tracked_state("clean")}]}),
        ("untracked", {"state": "exact", "paths": []}),
        ("ignored", {"state": "none", "paths": []}),
        ("activeOperations", {"state": "exact", "operations": ["merge"]}),
        ("administrativeLocks", {"state": "exact", "locks": [{"type": "index"}]}),
    ]:
        mutated = deepcopy(value)
        mutated["spec"]["expectedBaseline"][dimension] = condition
        assert_invalid("TaskContract", mutated)


@pytest.mark.parametrize("checkout,observed,valid", [
    ("absent", False, True), ("uninitialized", False, True),
    ("initialized", True, True), ("absent", True, False),
    ("uninitialized", True, False), ("initialized", False, False),
])
def test_submodule_checkout_observation_pairing(checkout, observed, valid):
    entry = {
        "path": "synthetic/submodule", "recordedObjectId": deepcopy(OID),
        "checkout": {"state": checkout}, "observation": {"state": "unavailable"},
    }
    if checkout == "initialized":
        entry["checkout"]["checkedOutObjectId"] = deepcopy(OID)
    if observed:
        entry["observation"] = {"state": "observed", "trackedChanges": False,
                                "untrackedChanges": True, "conflicts": False}
    v = validator("task-contract", "#/$defs/submoduleEntry")
    assert v.is_valid(entry) is valid


@pytest.mark.parametrize("transition", [
    {"type": "index-entry", "path": "synthetic/file.txt",
     "from": {"state": "absent"}, "to": {"state": "present", "value": index_state()}},
    {"type": "tracked-entry", "path": "synthetic/file.txt",
     "from": {"state": "present", "value": tracked_state("clean")},
     "to": {"state": "present", "value": tracked_state()}},
    {"type": "untracked-path", "path": "synthetic/file.txt", "from": "absent", "to": "present"},
    {"type": "ignored-path", "path": "synthetic/file.txt", "from": "present", "to": "absent"},
])
def test_supported_transitions_and_nonwriting_prohibition(transition):
    value = resource("TaskContract")
    value["spec"] = contract_spec(write=True)
    value["spec"]["permittedTransitions"] = [transition]
    assert_valid("TaskContract", value)
    readonly = resource("TaskContract")
    readonly["spec"]["permittedTransitions"] = [transition]
    assert_invalid("TaskContract", readonly)


@pytest.mark.parametrize("transition_type", [
    "ref-state", "head-state", "submodule-entry", "active-operation",
    "administrative-lock", "unknown",
])
def test_retired_transitions_reject(transition_type):
    value = resource("TaskContract")
    value["spec"] = contract_spec(write=True)
    value["spec"]["permittedTransitions"] = [{
        "type": transition_type, "path": "synthetic/file.txt",
        "from": "absent", "to": "present",
    }]
    assert_invalid("TaskContract", value)


POSTCONDITIONS = [
    {"type": "scope-contained"},
    {"type": "ref-state", "expected": {"state": "branch", "branchRef": "refs/heads/synthetic"}},
    {"type": "head-state", "expected": {"state": "unborn"}},
    {"type": "index-state", "expected": {"state": "clean"}},
    {"type": "tracked-state", "expected": {"state": "clean"}},
    {"type": "untracked-state", "expected": {"state": "none"}},
    {"type": "ignored-state", "expected": {"state": "none"}},
    {"type": "submodule-state", "expected": {"state": "none"}},
    {"type": "active-operations", "expected": {"state": "none"}},
    {"type": "administrative-locks", "expected": {"state": "none"}},
    {"type": "lease-state", "expected": "not-required"},
]


def test_eleven_postcondition_union_and_type_cardinality():
    value = resource("TaskContract")
    value["spec"]["requiredPostconditions"] = sorted(deepcopy(POSTCONDITIONS), key=lambda p: p["type"])
    assert_valid("TaskContract", value)
    for item in POSTCONDITIONS:
        mutated = deepcopy(value)
        mutated["spec"]["requiredPostconditions"].append(deepcopy(item))
        assert_invalid("TaskContract", mutated)
    value["spec"]["requiredPostconditions"] = [{"type": "lease-state", "expected": "not-required"}]
    assert_invalid("TaskContract", value)


@pytest.mark.parametrize("write,expected", [(False, "not-required"), (True, "owned")])
def test_lease_postcondition_matches_write_branch(write, expected):
    value = resource("TaskContract")
    value["spec"] = contract_spec(write)
    value["spec"]["requiredPostconditions"] = [
        {"type": "lease-state", "expected": expected}, {"type": "scope-contained"},
    ]
    assert_valid("TaskContract", value)
    value["spec"]["requiredPostconditions"][0]["expected"] = "owned" if not write else "not-required"
    assert_invalid("TaskContract", value)


def denial_resource(state="not-required"):
    value = resource("ExecutionReceipt")
    spec = value["spec"]
    checkpoint = {
        "not-required": "intent-validation", "not-attempted": "initial-preflight",
        "not-acquired": "lease-acquisition", "indeterminate": "lease-acquisition",
        "acquired": "post-acquisition-revalidation",
    }[state]
    spec["origin"] = {
        "type": "pre-contract-denial", "denialCheckpoint": checkpoint,
        "preContractEvidence": {
            "observedAt": TIME, "evidenceDigest": DIGEST,
            "controllerCheckId": "check." + checkpoint,
            "reasonCodes": ["reason.synthetic.denied"],
            "sanitizedSummary": "Conspicuously synthetic denial evidence.",
        }, "leaseAcquisition": {"state": state},
    }
    spec.update(executionOutcome="not-attempted", verificationOutcome="not-performed",
                lifecycleOutcome="denied")
    prerequisites = [] if checkpoint == "intent-validation" else G_CHECKS[:]
    if checkpoint in G_CHECKS:
        prerequisites = G_CHECKS[:G_CHECKS.index(checkpoint)]
    spec["checks"] = [check(t) for t in prerequisites]
    if state == "acquired":
        spec["checks"].append(check("lease-acquisition"))
        spec["acquisitionBinding"] = {
            "checkId": "check.lease-acquisition", "leaseId": LEASE_ID,
            "acquisitionResultDigest": DIGEST,
        }
        spec["releaseOutcome"] = "succeeded"
    controller = check(checkpoint, "indeterminate" if state == "indeterminate" else "failed")
    controller["reasonCodes"] = ["reason.synthetic.denied"]
    spec["checks"].append(controller)
    if state == "acquired":
        spec["checks"].append(check("lease-release"))
        for item in spec["checks"]:
            if item["checkType"] in ["lease-acquisition", "post-acquisition-revalidation", "lease-release"]:
                item["leaseAcquisitionRef"] = {"checkId": "check.lease-acquisition"}
    if state == "indeterminate":
        spec.update(releaseOutcome="indeterminate", lifecycleOutcome="indeterminate")
        spec["unresolvedCoordinationWarnings"] = [{
            "sequence": 0, "code": "reason.synthetic.unresolved",
            "profileId": "profile.synthetic.warning", "relatedCheckId": controller["checkId"],
        }]
    spec["checks"].append(check("receipt-finalization"))
    for i, item in enumerate(spec["checks"]):
        item["sequence"] = i
    return value


@pytest.mark.parametrize("state", ["not-required", "not-attempted", "not-acquired", "indeterminate", "acquired"])
def test_denial_state_union_and_acquisition_binding(state):
    value = denial_resource(state)
    assert_valid("ExecutionReceipt", value)
    value["spec"]["origin"]["leaseAcquisition"]["leaseId"] = LEASE_ID
    assert_invalid("ExecutionReceipt", value)
    value = denial_resource(state)
    if state == "acquired":
        del value["spec"]["acquisitionBinding"]
    else:
        value["spec"]["acquisitionBinding"] = {
            "checkId": "check.lease-acquisition", "leaseId": LEASE_ID,
            "acquisitionResultDigest": DIGEST,
        }
    assert_invalid("ExecutionReceipt", value)


@pytest.mark.parametrize("field,bad", [
    ("contractId", CONTRACT_ID), ("effectiveMode", "implementation"),
    ("resolvedTarget", {}), ("denialCheckpoint", "execution"),
    ("preContractEvidence", {}),
])
def test_denial_origin_rejects_issued_fields_and_invalid_checkpoint(field, bad):
    value = denial_resource()
    value["spec"]["origin"][field] = bad
    assert_invalid("ExecutionReceipt", value)


@pytest.mark.parametrize("check_type", G_CHECKS + [
    "lease-acquisition", "post-acquisition-revalidation", "pre-issuance-revalidation",
    "contract-issuance", "pre-action-revalidation", "post-execution-verification", "lease-release",
])
def test_nonexecution_check_outcomes(check_type):
    v = validator("execution-receipt", "#/$defs/check")
    for outcome in ["passed", "failed", "indeterminate"]:
        v.validate(check(check_type, outcome))
    for outcome in ["succeeded", "cancelled", "not-attempted", "unknown"]:
        assert not v.is_valid(check(check_type, outcome))


def test_execution_check_outcomes_and_finalization_specialization():
    v = validator("execution-receipt", "#/$defs/check")
    for outcome in ["succeeded", "failed", "cancelled", "indeterminate"]:
        v.validate(check("execution", outcome))
    assert not v.is_valid(check("execution", "passed"))
    final = check("receipt-finalization")
    v.validate(final)
    for field, bad in [
        ("checkId", "check.synthetic.alternate"),
        ("profileId", "profile.synthetic.alternate"),
        ("reasonCodes", ["reason.synthetic.alternate"]),
        ("outcome", "failed"), ("expectedSummary", "Synthetic text."),
        ("observedSummary", "Synthetic text."),
        ("postconditionRef", {"type": "scope-contained"}),
        ("leaseAcquisitionRef", {"checkId": "check.lease-acquisition"}),
    ]:
        mutated = deepcopy(final)
        mutated[field] = bad
        assert not v.is_valid(mutated), field


def test_postcondition_reference_is_verification_only():
    v = validator("execution-receipt", "#/$defs/check")
    value = check("post-execution-verification")
    value["postconditionRef"] = {"type": "scope-contained"}
    v.validate(value)
    for bad in [{"type": "unknown"}, {"type": "scope-contained", "expected": True}]:
        value["postconditionRef"] = bad
        assert not v.is_valid(value)
    value = check("initial-preflight")
    value["postconditionRef"] = {"type": "scope-contained"}
    assert not v.is_valid(value)


def test_receipt_local_conditionals():
    original = resource("ExecutionReceipt")
    for field, bad in [
        ("sanitization", {**original["spec"]["sanitization"], "applied": False}),
        ("verificationOutcome", "not-performed"),
        ("lifecycleOutcome", "failed"),
        ("ordinaryOperationEvidence", []),
        ("changedPaths", ["synthetic/file.txt"]),
        ("checks", original["spec"]["checks"][:-1]),
        ("checks", original["spec"]["checks"] + [deepcopy(original["spec"]["checks"][-1])]),
    ]:
        value = deepcopy(original)
        value["spec"][field] = bad
        assert_invalid("ExecutionReceipt", value)


def writing_receipt():
    value = resource("ExecutionReceipt")
    spec = value["spec"]
    spec["origin"]["effectiveMode"] = "implementation"
    spec["releaseOutcome"] = "succeeded"
    spec["acquisitionBinding"] = {
        "checkId": "check.lease-acquisition", "leaseId": LEASE_ID,
        "acquisitionResultDigest": DIGEST,
    }
    spec["checks"][5:6] = [check("lease-acquisition"), check("post-acquisition-revalidation")]
    spec["checks"].insert(-1, check("lease-release"))
    for i, item in enumerate(spec["checks"]):
        item["sequence"] = i
        if item["checkType"] in ["lease-acquisition", "post-acquisition-revalidation", "lease-release"]:
            item["leaseAcquisitionRef"] = {"checkId": "check.lease-acquisition"}
    spec["ordinaryOperationEvidence"] = []
    return value


def test_writing_receipt_operation_and_compact_reference_requirements():
    value = writing_receipt()
    assert_valid("ExecutionReceipt", value)
    for field in ["ordinaryOperationEvidence", "acquisitionBinding"]:
        mutated = deepcopy(value)
        del mutated["spec"][field]
        assert_invalid("ExecutionReceipt", mutated)
    for i, item in enumerate(value["spec"]["checks"]):
        if "leaseAcquisitionRef" in item:
            mutated = deepcopy(value)
            del mutated["spec"]["checks"][i]["leaseAcquisitionRef"]
            assert_invalid("ExecutionReceipt", mutated)


@pytest.mark.parametrize("operations,valid", [
    (["create"], True), (["delete"], True), (["modify"], True),
    (["create", "delete", "modify"], True),
    ([], False), (["modify", "create"], False), (["modify", "modify"], False),
    (["rename"], False),
])
def test_operation_record_closed_canonical_finite_vocabulary(operations, valid):
    v = validator("execution-receipt", "#/$defs/ordinaryOperationEvidenceRecord")
    value = {"path": "synthetic/file.txt", "operations": operations}
    assert v.is_valid(value) is valid


def test_formats_are_asserted_at_resource_level():
    for kind, path, bad in [
        ("TaskContract", ("spec", "taskId"), "not-a-uuid"),
        ("TaskContract", ("spec", "freshness", "expiresAt"), "2000-02-30T00:00:00Z"),
        ("ExecutionReceipt", ("spec", "finishedAt"), "2000-01-01T00:00:00+00:00"),
    ]:
        value = resource(kind)
        at(value, path[:-1])[path[-1]] = bad
        assert_invalid(kind, value)


def test_schema_acceptance_does_not_claim_static_or_operational_validation():
    value = resource("Project")
    value["spec"]["domainRefs"][0]["id"] = "missing.synthetic.invalid"
    assert_valid("Project", value)  # S4 must resolve existence in a closed bundle.
    value = resource("TaskContract")
    value["spec"]["freshness"]["expiresAt"] = "1999-01-01T00:00:00Z"
    assert_valid("TaskContract", value)  # Chronology requires a separate static gate.


@pytest.mark.parametrize("transition_type", ["index-entry", "tracked-entry"])
def test_absent_to_absent_entry_transition_rejects(transition_type):
    value = resource("TaskContract")
    value["spec"] = contract_spec(write=True)
    value["spec"]["permittedTransitions"] = [{
        "type": transition_type, "path": "synthetic/file.txt",
        "from": {"state": "absent"}, "to": {"state": "absent"},
    }]
    assert_invalid("TaskContract", value)


@pytest.mark.parametrize("transition_type", ["untracked-path", "ignored-path"])
def test_unchanged_path_presence_transition_rejects(transition_type):
    value = resource("TaskContract")
    value["spec"] = contract_spec(write=True)
    value["spec"]["permittedTransitions"] = [{
        "type": transition_type, "path": "synthetic/file.txt",
        "from": "present", "to": "present",
    }]
    assert_invalid("TaskContract", value)
