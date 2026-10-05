"""Opaque producer-port consumers and validation-order failure boundaries."""

from copy import deepcopy
import pytest
from contextctl_schema import _static_core as core
from contextctl_schema import static_validation as api
from tests.schema.s4_synthetic import proofs, bundle, context, issued, denial, run_receipt, selected, contract_bundle, codes


def coherent_bundle():
    """Keep closed-bundle direct predicates valid before testing proof trust."""
    b = bundle()
    b["project"]["metadata"]["id"] = "project.invalid"
    b["domains"][0]["metadata"]["id"] = "domain.invalid"
    b["worktreeRoles"][0]["metadata"]["id"] = "role.invalid"
    b["routingPolicy"]["metadata"]["id"] = "routing.invalid"
    return b


@pytest.mark.parametrize("provider", [None, True, False, {"trusted": True}, object(), core._ProofContext()])
def test_caller_assertions_never_create_trust(provider, monkeypatch):
    from tests.schema.s4_synthetic import source_registry
    monkeypatch.setattr(core, "build_registry", source_registry)
    result = api.validate_governance_bundle(coherent_bundle(), proof_context=provider)
    assert result.validation_scope == "governance-bundle"
    assert result.status == "PROOF_REQUIRED"
    assert result.direct_checks_passed is True
    assert not result.full_static_acceptance
    assert [(p.requirement_id, p.profile) for p in result.required_proofs] == [
        ("PROOF.INPUT", "prepared-input")
    ]
    assert "S4.BUNDLE.REFERENCES" not in codes(result)


@pytest.mark.parametrize("operation,args", [
    ("require_input_provenance", ({"synthetic": True}, "root.invalid", "revision.invalid")),
    ("require_canonical_comparison", ({}, "RuleProjection", {}, "RuleProjection", "jcs-equality")),
    ("require_digest", ({}, "profile.digest.task-contract-v1", "complete-task-contract", ())),
    ("require_complete_host_snapshot", ("host.invalid", {})),
    ("require_baseline_materialization", ({}, ("index",))),
    ("require_completed_static_validation", ({}, "task-contract", ())),
])
@pytest.mark.parametrize("failure", ["missing", "invalid", "wrong-binding", "changed"])
def test_proof_ports_fail_closed(operation, args, failure, proofs):
    proofs.overrides[operation] = lambda *unused: True
    ctx = context({}, proofs.context)
    input_continuity = failure == "changed" and operation == "require_input_provenance"
    if input_continuity:
        subject = coherent_bundle()
        ctx = core._ValidationContext(subject, core._root("governance-bundle"), proofs.context)
        args = (subject, ctx.root_id, core.SCHEMA_SET_REVISION)
    if failure == "missing":
        proofs.unavailable.add(operation)
    elif failure == "invalid":
        proofs.corrupt = True
    elif failure == "wrong-binding":
        original = proofs.issue
        def wrong(op, operands):
            h = original(op, operands)
            h.identities = ()
            return h
        proofs.issue = wrong
    if input_continuity:
        assert api._prepare(subject, "governance-bundle", ctx)
        value = True
    else:
        value = core._proof(ctx, "PROOF.INPUT", operation, args)
    if failure == "changed":
        assert value is True
        accepted = core._finish_result("governance-bundle", ctx)
        assert accepted.status == "PASS" and accepted.full_static_acceptance
        old_handle = ctx.proofs[0][2]
        mutable = next((a for a in args if isinstance(a, dict)), None)
        mutable["changed"] = "synthetic"
        result = core._finish_result("governance-bundle", ctx)
        assert result.status == "PROOF_REQUIRED"
        assert not result.full_static_acceptance
        obligation, = result.required_proofs
        assert obligation.requirement_id == "PROOF.INPUT"
        assert obligation.profile == "proof-continuity"
        assert obligation.subject_id is None
        assert obligation.instance_pointer == ""
        current_operands = (ctx.subject, ctx.root_id, core.SCHEMA_SET_REVISION)
        fresh = core._ValidationContext(ctx.subject, ctx.root_id)
        core._proof(fresh, "PROOF.INPUT", "require_input_provenance", current_operands,
                    profile="prepared-input")
        assert obligation.required_binding == fresh.required_proofs[0].required_binding
        assert obligation.required_binding == (
            "require_input_provenance", ctx.root_id, core.SCHEMA_SET_REVISION,
            id(ctx.subject), tuple(map(id, current_operands)),
        )
        mutable.pop("changed")
        if input_continuity:
            # A coherent nested mutation isolates provenance from shape rejection.
            mutable["project"]["metadata"]["description"] = "Conspicuously synthetic changed value."
            original_issue = proofs.issue
            proofs.issue = lambda op, operands: old_handle
            replay = api.validate_governance_bundle(mutable, proof_context=proofs.context)
            assert replay.status == "PROOF_REQUIRED" and not replay.full_static_acceptance
            proofs.issue = original_issue
            fresh_result = api.validate_governance_bundle(mutable, proof_context=proofs.context)
            assert fresh_result.status == "PASS" and fresh_result.full_static_acceptance
    else:
        assert value is None and ctx.required_proofs


@pytest.mark.parametrize("missing", ["require_input_provenance", "require_completed_static_validation", "require_digest"])
def test_receipt_proofs_cannot_be_bypassed(missing, proofs):
    r, c, sources = issued(True)
    proofs.unavailable.add(missing)
    result = run_receipt(r, c, sources, proofs)
    assert result.status == "PROOF_REQUIRED"
    assert not result.full_static_acceptance


def test_failed_static_never_requests_receipt_digest(proofs):
    r, c, sources = issued()
    selected(r, "pre-action-revalidation")[0]["outcome"] = "failed"
    assert run_receipt(r, c, sources, proofs).status == "INVALID"
    assert not any(op == "require_digest" and args[1] == "profile.digest.execution-receipt-v1" for op, args in proofs.calls)


def test_acquired_denial_waits_for_source_and_controller(proofs):
    r, sources = denial("post-acquisition-revalidation", "acquired")
    r["spec"]["origin"]["preContractEvidence"]["controllerCheckId"] = "check.wrong"
    assert run_receipt(r, None, sources, proofs).status == "INVALID"
    profiles = [args[1] for op, args in proofs.calls if op == "require_digest"]
    assert "profile.digest.lease-acquisition-identity-v1" in profiles
    assert "profile.digest.pre-contract-evidence-v1" not in profiles
    assert "profile.digest.execution-receipt-v1" not in profiles


def test_postcondition_reference_waits_for_complete_contract(proofs):
    r, c, sources = issued()
    selected(r, "post-execution-verification")[0]["postconditionRef"]["type"] = "head-state"
    result = api.validate_execution_receipt_static(r, contract_context=c, proof_context=proofs.context)
    assert result.status == "PROOF_REQUIRED"
    assert "S4.PB04" not in codes(result)


def test_remote_order_proof_and_projection_precedence(proofs):
    b = coherent_bundle()
    remotes = b["project"]["spec"]["repositoryIdentity"]["acceptedRemotes"]
    another = deepcopy(remotes[0])
    another["host"] = "z.invalid"
    remotes.append(another)
    proofs.unavailable.add("require_canonical_comparison")
    assert api.validate_governance_bundle(b, proof_context=proofs.context).status == "PROOF_REQUIRED"
    proofs.unavailable.clear()
    b = coherent_bundle()
    rules = b["routingPolicy"]["spec"]["rules"]
    rules.append(deepcopy(rules[0]))
    rules[-1]["id"] = "rule.z-invalid"
    result = api.validate_governance_bundle(b, proof_context=proofs.context)
    assert result.status == "INVALID"
    assert not any(op == "require_canonical_comparison" and args[1] == "MatchProjection" for op, args in proofs.calls)
