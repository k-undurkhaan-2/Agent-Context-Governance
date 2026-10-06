"""Supplied contract invariants; no task resolution, issuance or Git reads."""

from copy import deepcopy
import pytest
from contextctl_schema.static_validation import validate_host_overlay, validate_task_contract_static
from contextctl_schema._static_contract import _check_contract_plan
from contextctl_schema._static_core import DEFAULT_PROOF_LIMITS, _proof
from tests.schema.s4_synthetic import proofs, contract_bundle as _contract_bundle, codes, context


def contract_bundle(write=False):
    """Align portable identities before exercising contract-specific behavior."""
    b, o, c = _contract_bundle(write)
    b["project"]["metadata"]["id"] = "project.invalid"
    b["domains"][0]["metadata"]["id"] = "domain.invalid"
    b["worktreeRoles"][0]["metadata"]["id"] = "role.invalid"
    b["routingPolicy"]["metadata"]["id"] = "routing.invalid"
    return b, o, c


def _inventory_context(b, o, proofs):
    marker = object()
    proofs.snapshots[o["spec"]["hostId"], id(marker)] = (((o, b),), ())
    return marker


@pytest.mark.parametrize("write", [False, True])
def test_complete_contract_and_missing_materialization(write, proofs):
    b, o, c = contract_bundle(write)
    proofs.baseline(c)
    marker = _inventory_context(b, o, proofs)
    result = validate_task_contract_static(c, bundle=b, host_overlay=o,
        inventory_context=marker, proof_context=proofs.context)
    assert result.status == "PASS" and result.full_static_acceptance, result

    # Omission and explicit None cannot be rescued by a willing proof provider.
    proofs.snapshots[o["spec"]["hostId"], id(None)] = (((o, b),), ())
    for kwargs in ({}, {"inventory_context": None}):
        start = len(proofs.calls)
        missing = validate_task_contract_static(c, bundle=b, host_overlay=o,
            proof_context=proofs.context, **kwargs)
        assert missing.status == "PROOF_REQUIRED" and not missing.full_static_acceptance
        obligation, = [p for p in missing.required_proofs if p.requirement_id == "PROOF.SNAPSHOT"]
        assert obligation.profile == "trusted-complete-host-snapshot"
        assert obligation.required_binding[0] == "require_complete_host_snapshot"
        assert obligation.required_binding[-2:] == (id(c), (id(o["spec"]["hostId"]), id(None)))
        assert not any(op == "require_complete_host_snapshot" for op, _ in proofs.calls[start:])

    # Full decoded equality accepts independent copies, not just object identity.
    copied = validate_task_contract_static(c, bundle=deepcopy(b), host_overlay=deepcopy(o),
        inventory_context=marker, proof_context=proofs.context)
    assert copied.status == "PASS" and copied.full_static_acceptance
    for mismatch in ("overlay-id", "overlay-content", "bundle-content"):
        selected_b, selected_o = deepcopy(b), deepcopy(o)
        if mismatch == "overlay-id":
            selected_o["metadata"]["id"] = "overlay.other-invalid"
        elif mismatch == "overlay-content":
            selected_o["metadata"]["description"] = "Conspicuously synthetic changed overlay."
        else:
            selected_b["domains"][0]["metadata"]["description"] = "Conspicuously synthetic changed domain."
        assert validate_host_overlay(selected_o, bundle=selected_b, proof_context=proofs.context).full_static_acceptance
        absent = validate_task_contract_static(c, bundle=selected_b, host_overlay=selected_o,
            inventory_context=marker, proof_context=proofs.context)
        assert absent.status == "INVALID" and not absent.full_static_acceptance
        assert codes(absent) == {"S4.PROOF.SNAPSHOT"}

    def change_project(value):
        if isinstance(value, dict):
            if value.get("kind") == "Project" and "id" in value:
                value["id"] = "project.z-invalid"
            for child in value.values():
                change_project(child)
        elif isinstance(value, list):
            for child in value:
                change_project(child)

    # S4-REVIEW-P1-001: the public selected-only operand cannot omit a peer,
    # including peers belonging to another Project on the same host.
    for fault, expected in ((None, None), ("worktree", "S4.HX.A1"), ("root", "S4.HX.A2"),
                           ("state-equal", "S4.HX.B1"), ("state-child", "S4.HX.B2"),
                           ("lock-equal", "S4.HX.B3"), ("lock-child", "S4.HX.B4"),
                           ("host", "S4.PROOF.SNAPSHOT"), ("individual", "reason.overlay.path-widening")):
        peer, second = deepcopy(b), deepcopy(o)
        peer["project"]["metadata"]["id"] = "project.z-invalid"
        change_project(peer)
        change_project(second)
        second["metadata"]["id"] = "overlay.z-invalid"
        binding = second["spec"]["bindings"][0]
        binding["worktreeId"] = "worktree.z-invalid"
        binding["repositoryRoot"]["value"] += "-other"
        if fault == "worktree":
            binding["worktreeId"] = o["spec"]["bindings"][0]["worktreeId"]
        elif fault == "root":
            binding["repositoryRoot"] = deepcopy(o["spec"]["bindings"][0]["repositoryRoot"])
        elif fault and fault.startswith(("state", "lock")):
            kind = "stateRoot" if fault.startswith("state") else "lockRoot"
            second["spec"][kind] = deepcopy(o["spec"]["bindings"][0]["repositoryRoot"])
            if fault.endswith("child"):
                second["spec"][kind]["value"] += "/child"
        elif fault == "host":
            second["spec"]["hostId"] = "another.invalid"
        elif fault == "individual":
            second["spec"]["pathCeiling"]["include"] = ["outside"]
        if fault in (None, "worktree", "root"):
            assert validate_host_overlay(second, bundle=peer, proof_context=proofs.context).full_static_acceptance
        complete = object()
        proofs.snapshots[o["spec"]["hostId"], id(complete)] = (((o, b), (second, peer)), ())
        conflict = validate_task_contract_static(c, bundle=b, host_overlay=o,
            inventory_context=complete, proof_context=proofs.context)
        if expected:
            assert conflict.status == "INVALID" and not conflict.full_static_acceptance
            assert expected in codes(conflict)
        else:
            assert conflict.status == "PASS" and conflict.full_static_acceptance

    proofs.materializations.clear()
    result = validate_task_contract_static(c, bundle=b, host_overlay=o,
        inventory_context=marker, proof_context=proofs.context)
    assert result.status == "PROOF_REQUIRED"
    assert any(p.requirement_id == "PROOF.BASELINE" for p in result.required_proofs)
    assert not any(p.requirement_id == "PROOF.SNAPSHOT" for p in result.required_proofs)


@pytest.mark.parametrize("fault", ["write-mode", "lease", "post", "unsupported", "disjoint", "target", "transition", "unchanged-post", "scope", "time"])
def test_contract_faults(fault, proofs):
    b, o, c = contract_bundle()
    s = c["spec"]
    if fault == "write-mode":
        s["allowWrite"] = True
    elif fault == "lease":
        s["leaseRequired"] = True
    elif fault == "post":
        s["requiredPostconditions"].append({"type": "scope-contained"})
    elif fault == "unsupported":
        s["permittedTransitions"] = [{"type": "branch", "path": "synthetic/file", "from": "absent", "to": "present"}]
    elif fault == "disjoint":
        s["prohibitedScope"]["capabilities"] = ["inspect"]
    elif fault == "target":
        s["target"]["worktreeId"] = "missing.invalid"
    elif fault == "transition":
        s["permittedTransitions"] = [{"type": "untracked-path", "path": "synthetic/file", "from": "absent", "to": "present"}]
    elif fault == "unchanged-post":
        s["requiredPostconditions"].insert(0, {"type": "head-state", "expected": {"state": "present", "objectId": {"algorithm": "sha1", "value": "b" * 40}}})
    elif fault == "scope":
        s["authorizedScope"]["paths"] = ["outside"]
    elif fault == "time":
        s["freshness"]["expiresAt"] = s["freshness"]["issuedAt"]
    proofs.baseline(c)
    result = validate_task_contract_static(c, bundle=b, host_overlay=o,
        inventory_context=_inventory_context(b, o, proofs), proof_context=proofs.context)
    assert result.status == "INVALID", result


@pytest.mark.parametrize("fault", [None, "from", "path", "capability", "post", "jcs"])
def test_transition_plan(fault, proofs):
    b, o, c = contract_bundle(True)
    s = c["spec"]
    s["permittedTransitions"] = [{"type": "untracked-path", "path": "synthetic/file", "from": "absent", "to": "present"}]
    s["requiredPostconditions"].append({"type": "untracked-state", "expected": {"state": "exact", "paths": ["synthetic/file"]}})
    view = proofs.baseline(c)
    # Trusted static leaf-kind operand for a proposed ordinary path; no I/O.
    from contextctl_schema._static_baseline import _MaterializedBaselineView
    view = _MaterializedBaselineView(c, view.values, (), {"synthetic/file": "100644"}, {})
    proofs.materializations[id(c)] = view
    if fault == "from":
        s["permittedTransitions"][0]["from"] = "present"
    elif fault == "path":
        s["authorizedScope"]["paths"] = ["another"]
    elif fault == "capability":
        s["authorizedScope"]["capabilities"].remove("create")
    elif fault == "post":
        s["requiredPostconditions"].pop()
    elif fault == "jcs":
        proofs.unavailable.add("require_canonical_comparison")
    result = validate_task_contract_static(c, bundle=b, host_overlay=o,
        inventory_context=_inventory_context(b, o, proofs), proof_context=proofs.context)
    assert result.status == ("PASS" if fault is None else "PROOF_REQUIRED" if fault == "jcs" else "INVALID"), result
