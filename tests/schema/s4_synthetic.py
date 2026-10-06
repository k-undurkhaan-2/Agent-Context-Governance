"""Bounded, conspicuously synthetic S4 vectors and PRIVATE proof-port doubles.

Nothing here is codec conformance, trusted inventory, a runtime observation, a
production governance model or reusable S5 fixture corpus. Digest tokens are
opaque placeholders; no governance digest is produced by these tests.
"""

from copy import deepcopy
from dataclasses import dataclass
from types import MappingProxyType

import pytest

from contextctl_schema import _static_core as core
from contextctl_schema._static_baseline import _MaterializedBaselineView
from tests.schema.test_resource_schemas import (
    DIGEST, G_CHECKS, LEASE_ID, TIME, TASK_ID, OID, check, contract_spec,
    reference, resource, source_registry,
)
from tests.schema.test_container_schemas import bundle, delivery


def stamp(second):
    return f"2000-01-01T00:00:{second:02d}Z"


def resequence(receipt):
    for i, q in enumerate(receipt["spec"]["checks"]):
        q["sequence"] = i


def selected(receipt, kind):
    return [q for q in receipt["spec"]["checks"] if q["checkType"] == kind]


def context(subject=None, proof_context=None, name="execution-receipt"):
    return core._ValidationContext(subject or {}, core._root(name), proof_context)


def codes(result):
    return {d.code for d in result.diagnostics}


def frozen(value):
    if isinstance(value, dict) or isinstance(value, MappingProxyType):
        return tuple((key, frozen(item)) for key, item in value.items())
    if isinstance(value, (list, tuple)):
        return tuple(frozen(item) for item in value)
    if isinstance(value, _MaterializedBaselineView):
        return (id(value.contract), frozen(value.values), frozen(value.head_entries))
    return value


@dataclass
class SyntheticHandle:
    operation: str
    identities: tuple
    snapshot: tuple
    value: object


class SyntheticPorts:
    """Test injection only; no trust registration is added to production."""
    def __init__(self):
        self.context = core._ProofContext()
        self.calls = []
        self.unavailable = set()
        self.completed = {}
        self.materializations = {}
        self.snapshots = {}
        self.overrides = {}
        self.corrupt = False

    def issue(self, operation, args):
        self.calls.append((operation, args))
        if operation in self.unavailable:
            return None
        if operation in self.overrides:
            value = self.overrides[operation](*args)
        elif operation == "require_input_provenance":
            value = True
        elif operation == "require_digest":
            value = DIGEST
        elif operation == "require_completed_static_validation":
            value = self.completed.get((id(args[0]), args[1]))
        elif operation == "require_baseline_materialization":
            value = self.materializations.get(id(args[0]))
        elif operation == "require_complete_host_snapshot":
            value = self.snapshots.get((args[0], id(args[1])))
        else:
            left, lp, right, rp, comparison = args
            if comparison == "unsigned-jcs-byte-order":
                # An explicit synthetic response, never a claimed JCS encoder.
                value = -1
            else:
                if lp == "RuleProjection":
                    left, right = ({k: v for k, v in item.items() if k != "id"} for item in (left, right))
                elif lp == "MatchProjection":
                    left, right = left["match"], right["match"]
                value = "equal" if left == right else "unequal"
        return SyntheticHandle(operation, tuple(map(id, args)), frozen(args), value)

    def validate(self, handle, operation, args):
        if (self.corrupt or type(handle) is not SyntheticHandle
                or handle.operation != operation or handle.identities != tuple(map(id, args))
                or handle.snapshot != frozen(args)):
            return None
        return handle.value

    def complete(self, subject, scope):
        self.completed[id(subject), scope] = core.StaticValidationResult("PASS", scope, (), (), True, True)

    def baseline(self, contract):
        b = contract["spec"]["expectedBaseline"]
        values = {key: (tuple(value.get("entries", ())) if key in ("index", "tracked", "submodules")
                       else tuple(value.get("paths", ())) if key in ("untracked", "ignored")
                       else value) for key, value in b.items()}
        view = _MaterializedBaselineView(contract, MappingProxyType(values), (),
            MappingProxyType({p: "100644" for dimension in ("untracked", "ignored") for p in values[dimension]}),
            MappingProxyType({}))
        self.materializations[id(contract)] = view
        return view


@pytest.fixture
def proofs(monkeypatch):
    ports = SyntheticPorts()
    monkeypatch.setattr(core, "build_registry", source_registry)
    for operation in ("require_input_provenance", "require_canonical_comparison", "require_digest",
                      "require_complete_host_snapshot", "require_baseline_materialization", "require_completed_static_validation"):
        def method(self, *args, _operation=operation):
            return ports.issue(_operation, args)
        monkeypatch.setattr(core._ProofContext, operation, method)
    monkeypatch.setattr(core._ProofContext, "_validate_handle", lambda self, h, op, args: ports.validate(h, op, args))
    return ports


def contract_bundle(write=False):
    b, overlay, c = bundle(), resource("HostOverlay"), resource("TaskContract")
    c["spec"] = contract_spec(write)
    # Fixed literal scopes make most contract-vector tests independent of
    # broad glob proof costs, which have their own full language test module.
    for d in b["domains"]:
        d["spec"]["pathScope"]["include"] = ["synthetic/file"]
    overlay["spec"]["pathCeiling"]["include"] = ["synthetic/file"]
    c["spec"]["authorizedScope"]["paths"] = ["synthetic/file"]
    if write:
        caps = c["spec"]["authorizedScope"]["capabilities"]
        for r in (b["project"], *b["domains"], *b["worktreeRoles"]):
            r["spec"]["permissions"].update(modes=["implementation", "plan-only"], permittedCapabilities=list(caps))
        overlay["spec"]["capabilityCeiling"] = list(caps)
        c["spec"]["requiredPostconditions"].insert(0, {"type": "lease-state", "expected": "owned"})
    return b, overlay, c


def issued(lease=False):
    r, c = resource("ExecutionReceipt"), resource("TaskContract")
    sources = ()
    if lease:
        c["spec"] = contract_spec(True)
        c["spec"]["requiredPostconditions"].insert(0, {"type": "lease-state", "expected": "owned"})
        r["spec"]["origin"]["effectiveMode"] = "implementation"
        checks = r["spec"]["checks"]
        checks[5:6] = [check("lease-acquisition"), check("post-acquisition-revalidation")]
        x = {"checkId": "check.lease-acquisition", "leaseId": LEASE_ID, "acquisitionResultDigest": DIGEST}
        r["spec"]["acquisitionBinding"] = x
        checks.insert(-1, check("lease-release"))
        extra = check("post-execution-verification")
        extra.update(checkId="check.lease-post", postconditionRef={"type": "lease-state"})
        checks.insert(-2, extra)
        for q in checks:
            if q["checkType"] in ("lease-acquisition", "post-acquisition-revalidation", "lease-release"):
                q["leaseAcquisitionRef"] = {"checkId": x["checkId"]}
        r["spec"].update(releaseOutcome="succeeded", ordinaryOperationEvidence=[])
        sources = ({"taskId": TASK_ID, **x},)
        resequence(r)
    return r, c, sources


def denial(checkpoint="intent-validation", state="not-required", outcome="failed"):
    r = resource("ExecutionReceipt")
    spec = r["spec"]
    if checkpoint in G_CHECKS:
        types = G_CHECKS[:G_CHECKS.index(checkpoint)]
    elif checkpoint in ("pre-issuance-revalidation", "lease-acquisition"):
        types = list(G_CHECKS)
    elif checkpoint == "post-acquisition-revalidation":
        types = G_CHECKS + ["lease-acquisition"]
    else:
        types = G_CHECKS + (["lease-acquisition", "post-acquisition-revalidation"] if state == "acquired" else ["pre-issuance-revalidation"])
    checks = [check(kind) for kind in types] + [check(checkpoint, outcome)]
    controller = checks[-1]
    controller["reasonCodes"] = ["reason.synthetic.denied"]
    evidence = {"controllerCheckId": controller["checkId"], "observedAt": TIME,
                "reasonCodes": controller["reasonCodes"].copy(), "evidenceDigest": DIGEST,
                "sanitizedSummary": "Conspicuously synthetic denial."}
    spec.update(origin={"type": "pre-contract-denial", "denialCheckpoint": checkpoint,
        "leaseAcquisition": {"state": state}, "preContractEvidence": evidence},
        executionOutcome="not-attempted", verificationOutcome="not-performed", lifecycleOutcome="denied")
    sources = ()
    if state == "acquired":
        x = {"checkId": "check.lease-acquisition", "leaseId": LEASE_ID, "acquisitionResultDigest": DIGEST}
        spec["acquisitionBinding"] = x
        checks.append(check("lease-release"))
        for q in checks:
            if q["checkType"] in ("lease-acquisition", "post-acquisition-revalidation", "lease-release"):
                q["leaseAcquisitionRef"] = {"checkId": x["checkId"]}
        spec["releaseOutcome"] = "succeeded"
        sources = ({"taskId": TASK_ID, **x},)
    if state == "indeterminate":
        spec.update(releaseOutcome="indeterminate", lifecycleOutcome="indeterminate")
        spec["unresolvedCoordinationWarnings"] = [{"sequence": 0, "code": "reason.synthetic.unresolved", "profileId": "profile.validation.v1"}]
    checks.append(check("receipt-finalization"))
    spec["checks"] = checks
    resequence(r)
    return r, sources


def run_receipt(r, c, sources, proofs):
    from contextctl_schema.static_validation import validate_execution_receipt_static
    if c is not None:
        proofs.complete(c, "task-contract")
    return validate_execution_receipt_static(r, contract_context=c, sources=sources, proof_context=proofs.context)
