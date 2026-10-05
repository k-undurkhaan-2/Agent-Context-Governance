"""Supplied contract invariants; no task resolution, issuance or Git reads."""

from copy import deepcopy
import pytest
from contextctl_schema.static_validation import validate_task_contract_static
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


@pytest.mark.parametrize("write", [False, True])
def test_complete_contract_and_missing_materialization(write, proofs):
    b, o, c = contract_bundle(write)
    proofs.baseline(c)
    result = validate_task_contract_static(c, bundle=b, host_overlay=o, proof_context=proofs.context)
    assert result.status == "PASS", result
    proofs.materializations.clear()
    result = validate_task_contract_static(c, bundle=b, host_overlay=o, proof_context=proofs.context)
    assert result.status == "PROOF_REQUIRED"


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
    result = validate_task_contract_static(c, bundle=b, host_overlay=o, proof_context=proofs.context)
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
    result = validate_task_contract_static(c, bundle=b, host_overlay=o, proof_context=proofs.context)
    assert result.status == ("PASS" if fault is None else "PROOF_REQUIRED" if fault == "jcs" else "INVALID"), result
