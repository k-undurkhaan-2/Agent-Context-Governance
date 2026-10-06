"""Closed exact references and contradictions without task resolution."""

from copy import deepcopy
import pytest
from contextctl_schema.static_validation import validate_governance_bundle
from contextctl_schema._static_bundle import _branch_policy_contains
from tests.schema.s4_synthetic import proofs, bundle, codes, reference


def closed_bundle():
    """Align the structural fixture's resource IDs with its existing references."""
    b = bundle()
    b["project"]["metadata"]["id"] = "project.invalid"
    b["domains"][0]["metadata"]["id"] = "domain.invalid"
    b["worktreeRoles"][0]["metadata"]["id"] = "role.invalid"
    b["routingPolicy"]["metadata"]["id"] = "routing.invalid"
    return b


@pytest.mark.parametrize("fault", [None, "reference", "policy", "ownership", "permissions", "overlap", "rule-id", "rule-project", "rule-projection", "match-projection"])
def test_bundle_integrity(fault, proofs):
    b = closed_bundle()
    if fault == "reference":
        b["project"]["spec"]["domainRefs"][0]["id"] = "missing.invalid"
    elif fault == "policy":
        b["project"]["spec"]["routingPolicyRef"]["id"] = "missing.invalid"
    elif fault == "ownership":
        b["worktreeRoles"][0]["spec"]["excludedDomainRefs"] = [reference("Domain")]
    elif fault == "permissions":
        b["domains"][0]["spec"]["permissions"]["prohibitedCapabilities"] = ["inspect"]
    elif fault == "overlap":
        b["domains"][0]["spec"]["overlapRefs"] = [reference("Domain")]
    elif fault and fault.startswith("rule-") or fault == "match-projection":
        rules = b["routingPolicy"]["spec"]["rules"]
        if fault == "rule-project":
            rules[0]["match"]["projectRef"]["id"] = "missing.invalid"
        else:
            rules.append(deepcopy(rules[0]))
            if fault != "rule-id":
                rules[-1]["id"] = "rule.z-invalid"
            if fault == "match-projection":
                rules[-1]["decision"] = {"type": "deny", "reasonCode": "reason.synthetic.denied"}
    saved = deepcopy(b)
    result = validate_governance_bundle(b, proof_context=proofs.context)
    assert result.status == ("PASS" if fault is None else "INVALID")
    assert b == saved


@pytest.mark.parametrize("symmetric", [True, False])
def test_overlap_is_symmetric(symmetric, proofs):
    b = closed_bundle()
    peer = deepcopy(b["domains"][0])
    peer["metadata"]["id"] = "domain.z-invalid"
    b["domains"][0]["spec"]["overlapRefs"] = [reference("Domain", peer["metadata"]["id"])]
    if symmetric:
        peer["spec"]["overlapRefs"] = [reference("Domain")]
    b["domains"].append(peer)
    b["project"]["spec"]["domainRefs"].append(reference("Domain", peer["metadata"]["id"]))
    result = validate_governance_bundle(b, proof_context=proofs.context)
    assert result.status == ("PASS" if symmetric else "INVALID")


@pytest.mark.parametrize("branch,allowed", [("refs/heads/a", True), ("refs/heads/a/b", True), ("refs/heads/ab", False), ("refs/heads/a/private", False)])
def test_static_branch_prefix_components(branch, allowed):
    policy = {"allowed": {"exact": [], "prefixes": ["refs/heads/a"]}, "denied": {"exact": ["refs/heads/a/private"], "prefixes": []}}
    assert _branch_policy_contains(policy, branch) is allowed
