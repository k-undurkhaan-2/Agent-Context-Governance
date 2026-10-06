"""Receipt identities, denial rows, P/E/V histories, scope and finalization."""

from copy import deepcopy
from itertools import product
import pytest
from contextctl_schema import _static_core as core, _static_receipt as receipt_owner
from tests.schema.s4_synthetic import (
    proofs, issued, denial, run_receipt, selected, resequence, check, G_CHECKS,
    DIGEST, codes,
)


@pytest.mark.parametrize("lease", [False, True])
def test_issued_paths(lease, proofs):
    r, c, sources = issued(lease)
    assert run_receipt(r, c, sources, proofs).status == "PASS"


DENIAL_ROWS = [(kind, "not-required") for kind in G_CHECKS] + [
    ("pre-issuance-revalidation", "not-required"), ("lease-acquisition", "not-acquired"),
    ("lease-acquisition", "indeterminate"), ("post-acquisition-revalidation", "acquired"),
    ("contract-issuance", "not-required"), ("contract-issuance", "acquired")]


@pytest.mark.parametrize("checkpoint,state", DENIAL_ROWS)
def test_all_denial_rows(checkpoint, state, proofs):
    r, sources = denial(checkpoint, state, "indeterminate" if state == "indeterminate" else "failed")
    assert run_receipt(r, None, sources, proofs).status == "PASS"
    r["spec"]["origin"]["preContractEvidence"]["controllerCheckId"] = "check.missing"
    assert "S4.DP05" in codes(run_receipt(r, None, sources, proofs))


@pytest.mark.parametrize("fault", ["missing-prerequisite", "failed-prerequisite", "unlisted", "late-prerequisite", "controller-passed", "time", "reasons", "earlier-bad", "retry-A", "retry-I", "retry-N", "state"])
def test_denial_owner_negatives(fault, proofs):
    checkpoint = "lease-acquisition" if fault in ("retry-A", "state") else "contract-issuance"
    r, sources = denial(checkpoint, "not-acquired" if checkpoint == "lease-acquisition" else "not-required")
    checks = r["spec"]["checks"]
    controller = selected(r, checkpoint)[-1]
    if fault == "missing-prerequisite":
        checks.pop(0)
    elif fault == "failed-prerequisite":
        checks[0]["outcome"] = "failed"
    elif fault == "unlisted":
        checks.insert(-1, check("pre-action-revalidation"))
    elif fault == "late-prerequisite":
        checks.insert(-1, checks.pop(0))
    elif fault == "controller-passed":
        controller["outcome"] = "passed"
    elif fault == "time":
        r["spec"]["origin"]["preContractEvidence"]["observedAt"] = "2000-01-01T00:00:01Z"
    elif fault == "reasons":
        controller["reasonCodes"] = ["reason.synthetic.other"]
    elif fault in ("earlier-bad", "retry-A", "retry-I"):
        earlier = deepcopy(controller)
        earlier["checkId"] = "check.earlier"
        earlier["outcome"] = "failed" if fault == "earlier-bad" else "passed"
        checks.insert(-2, earlier)
    elif fault == "retry-N":
        earlier = check("pre-issuance-revalidation")
        earlier["checkId"] = "check.earlier"
        checks.insert(-2, earlier)
    elif fault == "state":
        controller["outcome"] = "indeterminate"
    resequence(r)
    assert run_receipt(r, None, sources, proofs).status == "INVALID"


def _assert_public_g_structure(receipt, contract, sources, proofs, pointer,
                               schema_pointer, keyword, constraint):
    result = run_receipt(receipt, contract, sources, proofs)
    assert result.status == "INVALID"
    diagnostic, = result.diagnostics
    assert (diagnostic.code, diagnostic.instance_pointer,
            diagnostic.predicate_family, diagnostic.schema_id,
            diagnostic.schema_pointer, diagnostic.keyword) == (
        "S4.VALIDATOR.STRUCTURED_ERRORS", pointer, "structural",
        "urn:uuid:53faa365-c113-4b2d-a9c5-022cd87a21dd", schema_pointer, keyword)
    schema = core.build_registry().contents(diagnostic.schema_id)
    for part in schema_pointer.strip("/").split("/"):
        schema = schema[int(part)] if isinstance(schema, list) else schema[part]
    assert schema[keyword] == constraint


def _g_owner_operands(receipt, contract, sources, proofs):
    # Unit boundary only: the full issued Schema cannot admit these negatives.
    # Start from the accepted control, check the shaped components explicitly,
    # and prepare canonical arrays and sequence selectors without changing them.
    ctx = core._ValidationContext(receipt, core._root("execution-receipt"), proofs.context)
    assert core._validate_shape(contract, core._root("task-contract"), ctx)
    for item in receipt["spec"]["checks"]:
        assert core._validate_shape(item, core._root("execution-receipt") + "#/$defs/check", ctx)
    for source in sources:
        assert receipt_owner._check_source_shape(source, ctx)
    core._check_canonical_arrays(receipt, core._root("execution-receipt"), ctx)
    core._check_canonical_arrays(contract, core._root("task-contract"), ctx)
    selectors = receipt_owner._prepare_sequence_selectors(receipt, ctx)
    assert selectors is not None
    assert not ctx.diagnostics and not ctx.required_proofs and not ctx.unevaluated
    # The existing private synthetic port binds completion to this same C.
    proofs.complete(contract, "task-contract")
    return ctx, selectors


def _assert_ai02_owner(receipt, contract, sources, proofs):
    ctx, selectors = _g_owner_operands(receipt, contract, sources, proofs)
    bindings = receipt_owner._check_receipt_presence(receipt, selectors, contract, sources, ctx)
    assert all(selectors[kind] for kind in G_CHECKS)  # AI01 passes.
    receipt_owner._check_contract_source_bindings(receipt, selectors, bindings, sources, ctx)
    assert bindings["identity_valid"] and not ctx.failed
    assert not ctx.diagnostics and not ctx.required_proofs and not ctx.unevaluated
    receipt_owner._check_prefix_and_controller(receipt, selectors, bindings, ctx)
    result = core._finish_result("execution-receipt", ctx)
    assert result.status == "INVALID" and codes(result) == {"S4.AI02"}
    assert len(result.diagnostics) == 1 and not result.required_proofs
    assert result.diagnostics[0].instance_pointer == "/spec/checks"


@pytest.mark.parametrize("lease,kind", product([False, True], G_CHECKS))
def test_every_issued_g_present_and_passed(lease, kind, proofs):
    r, c, sources = issued(lease)
    assert run_receipt(r, c, sources, proofs).status == "PASS"
    if not lease:
        assert c["spec"]["requestedMode"] == c["spec"]["effectiveMode"] == "plan-only"
        assert c["spec"]["allowWrite"] is False and c["spec"]["leaseRequired"] is False
        assert "leaseId" not in c["spec"] and sources == ()
    failed = selected(r, kind)[0]
    assert failed["outcome"] == "passed"
    failed["outcome"] = "failed"
    issued_checks = "/properties/spec/allOf/7/then/allOf/3/properties/checks"
    outcome_pointer = f"/spec/checks/{failed['sequence']}/outcome"
    _assert_public_g_structure(r, c, sources, proofs, outcome_pointer,
        issued_checks + "/items/then/properties/outcome", "const", "passed")
    _assert_ai02_owner(r, c, sources, proofs)

    # Frozen AI-N02 variant: a later passed same-type G never recovers a failure.
    repeated = deepcopy(r)
    later = deepcopy(failed)
    later.update(checkId=failed["checkId"] + "-later", outcome="passed")
    repeated["spec"]["checks"].insert(failed["sequence"] + 1, later)
    resequence(repeated)
    repeated_control = deepcopy(repeated)
    selected(repeated_control, kind)[0]["outcome"] = "passed"
    assert run_receipt(repeated_control, c, sources, proofs).status == "PASS"
    _assert_public_g_structure(repeated, c, sources, proofs, outcome_pointer,
        issued_checks + "/items/then/properties/outcome", "const", "passed")
    _assert_ai02_owner(repeated, c, sources, proofs)

    r["spec"]["checks"] = [q for q in r["spec"]["checks"] if q["checkType"] != kind]
    resequence(r)
    _assert_public_g_structure(r, c, sources, proofs, "/spec/checks",
        issued_checks + f"/allOf/{G_CHECKS.index(kind)}", "contains",
        {"properties": {"checkType": {"const": kind}}, "required": ["checkType"]})
    ctx, selectors = _g_owner_operands(r, c, sources, proofs)
    assert not selectors[kind]
    bindings = receipt_owner._check_receipt_presence(r, selectors, c, sources, ctx)
    receipt_owner._check_contract_source_bindings(r, selectors, bindings, sources, ctx)
    assert bindings["identity_valid"] and not ctx.unevaluated
    result = core._finish_result("execution-receipt", ctx)
    assert result.status == "INVALID" and codes(result) == {"S4.AI01"}
    assert len(result.diagnostics) == 1 and not result.required_proofs
    assert result.diagnostics[0].instance_pointer == "/spec/checks"


@pytest.mark.parametrize("fault", ["source-task", "source-check", "source-lease", "source-digest", "binding-check", "binding-digest", "A-ref", "R-ref", "L-ref", "source-count", "contract-id", "contract-digest", "domain", "target", "mode", "lease"])
def test_issued_source_and_contract_identity(fault, proofs):
    r, c, sources = issued(True)
    x, source, origin = r["spec"]["acquisitionBinding"], sources[0], r["spec"]["origin"]
    other_uuid = "00000000-0000-4000-8000-000000000099"
    if fault.startswith("source-") and fault != "source-count":
        field = {"source-task": "taskId", "source-check": "checkId", "source-lease": "leaseId", "source-digest": "acquisitionResultDigest"}[fault]
        source[field] = "check.other" if field == "checkId" else "sha256:" + "1" * 64 if field == "acquisitionResultDigest" else other_uuid
    elif fault == "binding-check":
        x["checkId"] = "check.other"
    elif fault == "binding-digest":
        x["acquisitionResultDigest"] = "sha256:" + "1" * 64
    elif fault.endswith("-ref"):
        kind = {"A-ref": "lease-acquisition", "R-ref": "post-acquisition-revalidation", "L-ref": "lease-release"}[fault]
        selected(r, kind)[0]["leaseAcquisitionRef"]["checkId"] = "check.other"
    elif fault == "source-count":
        sources = ()
    elif fault == "contract-id":
        origin["contractId"] = other_uuid
    elif fault == "contract-digest":
        origin["contractDigest"] = "sha256:" + "1" * 64
    elif fault == "domain":
        origin["resolvedTarget"]["domainRefs"][0]["id"] = "another.invalid"
    elif fault == "target":
        origin["resolvedTarget"]["worktreeId"] = "another.invalid"
    elif fault == "mode":
        origin["effectiveMode"] = "review"
    elif fault == "lease":
        c["spec"]["leaseId"] = other_uuid
    assert run_receipt(r, c, sources, proofs).status == "INVALID"


@pytest.mark.parametrize("earlier,later", product(["failed", "cancelled", "indeterminate"], ["succeeded", "failed", "cancelled", "indeterminate"]))
def test_execution_cannot_recover(earlier, later, proofs):
    r, c, sources = issued()
    original = selected(r, "execution")[0]
    original["outcome"] = later
    first = deepcopy(original)
    first.update(checkId="check.execution-earlier", outcome=earlier)
    r["spec"]["checks"].insert(original["sequence"], first)
    resequence(r)
    r["spec"]["executionOutcome"] = later
    r["spec"]["lifecycleOutcome"] = "succeeded" if later == "succeeded" else later
    assert "S4.RECEIPT.E_TERMINAL" in codes(run_receipt(r, c, sources, proofs))


@pytest.mark.parametrize("execution,verification", product(["succeeded", "failed", "cancelled", "indeterminate"], ["passed", "failed", "indeterminate"]))
def test_final_outcomes_and_precedence(execution, verification, proofs):
    r, c, sources = issued()
    selected(r, "execution")[0]["outcome"] = execution
    selected(r, "post-execution-verification")[0]["outcome"] = verification
    lifecycle = verification if verification != "passed" else execution
    r["spec"].update(executionOutcome=execution, verificationOutcome=verification, lifecycleOutcome=lifecycle)
    assert run_receipt(r, c, sources, proofs).status == "PASS"
    selected(r, "execution")[0]["outcome"] = "failed" if execution != "failed" else "succeeded"
    assert "S4.RECEIPT.FINAL_OUTCOMES" in codes(run_receipt(r, c, sources, proofs))


@pytest.mark.parametrize("fault", ["P-missing", "E-missing", "V-missing", "P-failed", "P-late", "V-early", "V-recovery", "post-missing", "post-other", "F-late", "warning-ref", "sequence", "id", "carrier", "evidence-path", "scope-path", "scope-operation"])
def test_receipt_static_faults(fault, proofs):
    r, c, sources = issued(True)
    checks = r["spec"]["checks"]
    p = selected(r, "pre-action-revalidation")[0]
    v = selected(r, "post-execution-verification")[0]
    if fault.endswith("-missing") and fault[0] in "PEV":
        kind = {"P": "pre-action-revalidation", "E": "execution", "V": "post-execution-verification"}[fault[0]]
        checks[:] = [q for q in checks if q["checkType"] != kind]
    elif fault == "P-failed":
        p["outcome"] = "failed"
    elif fault == "P-late":
        checks.remove(p)
        checks.insert(-2, p)
    elif fault == "V-early":
        checks.remove(v)
        checks.insert(0, v)
    elif fault == "V-recovery":
        first = deepcopy(v)
        first.update(checkId="check.failed-unreferenced", outcome="failed")
        first.pop("postconditionRef")
        checks.insert(v["sequence"], first)
    elif fault == "post-missing":
        v.pop("postconditionRef")
    elif fault == "post-other":
        v["postconditionRef"]["type"] = "head-state"
    elif fault == "F-late":
        checks.insert(0, checks.pop())
    elif fault == "warning-ref":
        r["spec"]["unresolvedCoordinationWarnings"] = [{"sequence": 0, "code": "reason.synthetic.warning", "profileId": "profile.validation.v1", "relatedCheckId": "check.missing"}]
    elif fault == "id":
        checks[1]["checkId"] = checks[0]["checkId"]
    elif fault == "carrier":
        r["spec"].pop("ordinaryOperationEvidence")
    elif fault in ("evidence-path", "scope-path", "scope-operation"):
        path = "outside" if fault == "scope-path" else "synthetic/file"
        r["spec"]["ordinaryOperationEvidence"] = [{"path": path, "operations": ["modify"]}]
        if fault != "evidence-path":
            r["spec"]["changedPaths"] = [path]
        if fault == "scope-operation":
            c["spec"]["authorizedScope"]["capabilities"].remove("modify")
    resequence(r)
    if fault == "sequence":
        checks[0]["sequence"] = 1
    assert run_receipt(r, c, sources, proofs).status == "INVALID"


@pytest.mark.parametrize("outcome,release", [("passed", "succeeded"), ("failed", "failed"), ("indeterminate", "indeterminate")])
def test_release_mapping_warning_and_retry(outcome, release, proofs):
    r, c, sources = issued(True)
    last = selected(r, "lease-release")[0]
    earlier = deepcopy(last)
    earlier.update(checkId="check.release-earlier", outcome="failed")
    r["spec"]["checks"].insert(last["sequence"], earlier)
    last["outcome"] = outcome
    resequence(r)
    r["spec"].update(releaseOutcome=release, lifecycleOutcome=release)
    if outcome != "passed":
        r["spec"]["unresolvedCoordinationWarnings"] = [{"sequence": 0, "code": "reason.synthetic.release", "profileId": "profile.validation.v1", "relatedCheckId": last["checkId"]}]
    assert run_receipt(r, c, sources, proofs).status == "PASS"
    if outcome != "passed":
        r["spec"]["unresolvedCoordinationWarnings"][0]["relatedCheckId"] = earlier["checkId"]
        assert "S4.RF11" in codes(run_receipt(r, c, sources, proofs))
