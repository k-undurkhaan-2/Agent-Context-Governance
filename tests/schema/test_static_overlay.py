"""Individual D10 narrowing and complete same-host static union."""

from copy import deepcopy
import pytest
from contextctl_schema.static_validation import validate_host_overlay, validate_same_host_inventory
from contextctl_schema._static_overlay import _exact_absolute_root_relation
from tests.schema.s4_synthetic import proofs, contract_bundle, codes
from contextctl_schema._static_overlay import _remote_key


def overlay_control():
    """Align the portable resource IDs before injecting overlay faults."""
    b, overlay, contract = contract_bundle()
    b["project"]["metadata"]["id"] = "project.invalid"
    b["domains"][0]["metadata"]["id"] = "domain.invalid"
    b["worktreeRoles"][0]["metadata"]["id"] = "role.invalid"
    b["routingPolicy"]["metadata"]["id"] = "routing.invalid"
    return b, overlay, contract


@pytest.mark.parametrize("fault,expected", [
    (None, None), ("project", "project-mismatch"), ("role", "role-not-in-project"),
    ("capability", "capability-widening"), ("repository", "repository-widening"),
    ("remote", "remote-widening"), ("name", "remote-unresolved"), ("path", "path-widening"),
])
def test_d10(fault, expected, proofs):
    b, o, _ = overlay_control()
    spec = o["spec"]
    if fault == "project":
        spec["projectRef"]["id"] = "another.invalid"
    elif fault == "role":
        spec["bindings"][0]["roleRef"]["id"] = "another.invalid"
    elif fault == "capability":
        spec["capabilityCeiling"] = ["modify"]
    elif fault == "repository":
        spec["repositoryIdentity"]["acceptedRemotes"][0]["repository"] = "another"
    elif fault == "remote":
        spec["remoteExpectations"][0]["acceptedRemotes"][0]["repository"] = "another"
    elif fault == "name":
        spec["bindings"][0]["remoteNames"] = ["missing"]
    elif fault == "path":
        spec["pathCeiling"]["include"] = ["outside/file"]
    result = validate_host_overlay(o, bundle=b, proof_context=proofs.context)
    if expected:
        assert "reason.overlay." + expected in codes(result)
    else:
        assert result.status == "PASS" and result.validation_scope == "host-overlay-individual"


@pytest.mark.parametrize("fault", [None, "worktree", "root", "state-equal", "state-child", "lock-equal", "lock-child", "host", "missing-proof", "individual"])
def test_complete_host_union(fault, proofs):
    b, first, _ = overlay_control()
    second = deepcopy(first)
    second["metadata"]["id"] = "overlay.z-invalid"
    binding = second["spec"]["bindings"][0]
    binding["worktreeId"] = "worktree.z-invalid"
    binding["repositoryRoot"]["value"] += "-other"
    if fault == "worktree":
        binding["worktreeId"] = first["spec"]["bindings"][0]["worktreeId"]
    elif fault == "root":
        binding["repositoryRoot"] = deepcopy(first["spec"]["bindings"][0]["repositoryRoot"])
    elif fault and fault.startswith(("state", "lock")):
        kind = "stateRoot" if fault.startswith("state") else "lockRoot"
        second["spec"][kind] = deepcopy(first["spec"]["bindings"][0]["repositoryRoot"])
        if fault.endswith("child"):
            second["spec"][kind]["value"] += "/child"
    elif fault == "host":
        second["spec"]["hostId"] = "another.invalid"
    elif fault == "individual":
        second["spec"]["pathCeiling"]["include"] = ["outside"]
    marker = object()
    if fault != "missing-proof":
        proofs.snapshots["host.invalid", id(marker)] = (((first, b), (second, b)), ())
    result = validate_same_host_inventory(host_id="host.invalid", inventory_context=marker, proof_context=proofs.context)
    assert result.status == ("PASS" if fault is None else "PROOF_REQUIRED" if fault == "missing-proof" else "INVALID")
    if fault == "individual":
        assert not any(code.startswith("S4.HX") for code in codes(result))


@pytest.mark.parametrize("root,relation", [("/a", "equal"), ("/a/b", "descendant"), ("/ab", "unrelated"), ("/", "unrelated")])
def test_exact_component_containment(root, relation):
    assert _exact_absolute_root_relation({"platform": "posix", "value": root}, {"platform": "posix", "value": "/a"}) == relation


@pytest.mark.parametrize("field,value", [("transport", "ssh"), ("host", "other.invalid"), ("port", 8443), ("namespace", ["other", "synthetic"]), ("repository", "another")])
def test_remote_identity_uses_every_component(field, value):
    b, _, _ = overlay_control()
    remote = b["project"]["spec"]["repositoryIdentity"]["acceptedRemotes"][0]
    other = deepcopy(remote)
    other[field] = value
    assert _remote_key(remote) != _remote_key(other)


def test_host_inventory_crosses_projects(proofs):
    b, first, _ = overlay_control()
    peer, second = deepcopy(b), deepcopy(first)
    peer["project"]["metadata"]["id"] = "project.z-invalid"
    def change_project(value):
        if isinstance(value, dict):
            if value.get("kind") == "Project" and "id" in value:
                value["id"] = "project.z-invalid"
            for child in value.values():
                change_project(child)
        elif isinstance(value, list):
            for child in value:
                change_project(child)
    change_project(peer)
    change_project(second)
    second["metadata"]["id"] = "overlay.z-invalid"
    second["spec"]["bindings"][0]["repositoryRoot"]["value"] += "-other"
    marker = object()
    proofs.snapshots["host.invalid", id(marker)] = (((first, b), (second, peer)), ())
    result = validate_same_host_inventory(host_id="host.invalid", inventory_context=marker, proof_context=proofs.context)
    assert "S4.HX.A1" in codes(result)
