"""Static consistency of supplied receipt claims; no evidence production."""

from types import MappingProxyType

from ._static_core import (
    StaticValidationResult, _check_canonical_arrays, _proof, _root, _validate_shape,
)
from ._static_paths import _closed_path_membership


_G_TYPES = ("intent-validation", "project-domain-resolution", "role-routing",
            "host-binding", "initial-preflight")
_TYPES = {"N": "pre-issuance-revalidation", "A": "lease-acquisition",
    "R": "post-acquisition-revalidation", "I": "contract-issuance",
    "P": "pre-action-revalidation", "E": "execution",
    "V": "post-execution-verification", "L": "lease-release",
    "F": "receipt-finalization"}
_ORDINARY = frozenset((*_G_TYPES, *(_TYPES[key] for key in "NARIPEV")))
_PRE_RELEASE = _ORDINARY - {_TYPES["N"]}


class _PreparedReceiptSelectors:
    def __init__(self, groups, by_id, per_type):
        self.groups = MappingProxyType(groups)
        self.by_id = MappingProxyType(by_id)
        self.per_type = MappingProxyType(per_type)

    def __getitem__(self, key):
        return self.groups[key]


def _prepare_sequence_selectors(receipt, ctx):
    spec = receipt["spec"]
    checks, warnings = spec["checks"], spec["unresolvedCoordinationWarnings"]
    valid = (all(check["sequence"] == i for i, check in enumerate(checks))
             and all(warning["sequence"] == i for i, warning in enumerate(warnings))
             and len({check["checkId"] for check in checks}) == len(checks))
    if not ctx.check("RECEIPT.SEQUENCES", valid, "/spec/checks", "receipt-preparation"):
        return None
    groups = {alias: tuple(check for check in checks if check["checkType"] == kind)
              for alias, kind in _TYPES.items()}
    groups.update({kind: tuple(check for check in checks if check["checkType"] == kind) for kind in _G_TYPES})
    groups["G"] = tuple(check for check in checks if check["checkType"] in _G_TYPES)
    groups["nonF"] = tuple(check for check in checks if check["checkType"] != _TYPES["F"])
    groups["Dpre"] = tuple(check for check in checks if check["checkType"] not in (_TYPES["L"], _TYPES["F"]))
    groups["preRelease"] = tuple(check for check in checks if check["checkType"] in _PRE_RELEASE)
    checkpoint = spec["origin"].get("denialCheckpoint")
    groups["controllers"] = tuple(check for check in checks if check["checkType"] == checkpoint)
    per_type = {}
    for check in groups["V"]:
        if "postconditionRef" in check:
            per_type.setdefault(check["postconditionRef"]["type"], []).append(check)
    return _PreparedReceiptSelectors(groups, {check["checkId"]: check for check in checks},
                                     {key: tuple(values) for key, values in per_type.items()})


def _check_source_shape(source, ctx):
    fields = {"taskId": "canonicalUuid", "checkId": "checkIdentifier",
              "leaseId": "canonicalUuid", "acquisitionResultDigest": "taggedDigest"}
    if not ctx.check("RECEIPT.SOURCE_SHAPE", isinstance(source, dict) and set(source) == set(fields),
                     "/sources", "source-shape"):
        return False
    valid = True
    for field, profile in fields.items():
        valid = _validate_shape(source[field], _root("common") + "#/$defs/" + profile, ctx) and valid
    return valid


def _check_receipt_presence(receipt, selectors, contract_context, sources, ctx):
    spec = receipt["spec"]
    issued = spec["origin"]["type"] == "issued-contract"
    contract = None
    if issued:
        if contract_context is None:
            ctx.unavailable("PROOF.CONTRACT_BINDING", "/spec/origin", "complete-task-contract")
        elif _validate_shape(contract_context, _root("task-contract"), ctx):
            contract = contract_context
            _check_canonical_arrays(contract, _root("task-contract"), ctx)
    else:
        ctx.check("RECEIPT.DENIAL_MATRIX", contract_context is None, "/spec/origin", "denial-presence")
    stable = (contract["spec"]["leaseRequired"] if contract is not None else None) if issued else spec["origin"]["leaseAcquisition"]["state"] == "acquired"
    if stable is not None:
        ctx.check("AI14", ("acquisitionBinding" in spec) == stable, "/spec/acquisitionBinding", "acquisition-presence")
        ctx.check("AI15", len(sources) == (1 if stable else 0), "/sources", "acquisition-presence")
        ctx.check("RF01" if stable else "RF02", bool(selectors["L"]) if stable else not selectors["L"],
                  "/spec/checks", "release-presence")
    ctx.check("RF04", bool(selectors["F"]), "/spec/checks", "finalization-presence")
    if issued:
        ctx.check("AI01", all(selectors[kind] for kind in _G_TYPES), "/spec/checks", "issued-prefix")
        ctx.check("AI07", len(selectors["I"]) == 1, "/spec/checks", "issued-prefix")
        if stable is not None:
            ctx.check("AI05" if stable else "AI06", len(selectors["R"] if stable else selectors["N"]) == 1,
                      "/spec/checks", "issued-prefix")
            ctx.check("AI09", not selectors["N"] if stable else not selectors["A"] and not selectors["R"],
                      "/spec/checks", "issued-prefix")
        attempted = spec["executionOutcome"] != "not-attempted"
        ctx.check("RECEIPT.PEV_CARD", all(selectors[key] for key in "PEV") if attempted else not selectors["E"] and not selectors["V"],
                  "/spec/checks", "receipt-presence")
    if stable:
        ctx.check("AI03", len(selectors["A"]) == 1, "/spec/checks", "acquisition-presence")
    for i, warning in enumerate(spec["unresolvedCoordinationWarnings"]):
        ctx.check("RECEIPT.WARN_REFS", "relatedCheckId" not in warning or warning["relatedCheckId"] in selectors.by_id,
                  f"/spec/unresolvedCoordinationWarnings/{i}", "warning-reference")
    for source in sources:
        _check_source_shape(source, ctx)
    return {"contract": contract, "stable": stable, "issued": issued, "identity_valid": True}


def _completed_static(value, scope):
    return (isinstance(value, StaticValidationResult) and value.status == "PASS"
            and value.validation_scope == scope and value.full_static_acceptance
            and value.direct_checks_passed is True and not value.diagnostics and not value.required_proofs)


def _check_contract_source_bindings(receipt, selectors, contract_context, sources, ctx):
    spec = receipt["spec"]
    bindings = contract_context
    contract, stable = bindings["contract"], bindings["stable"]
    before = len(ctx.diagnostics)
    if bindings["issued"]:
        if contract is None:
            bindings["identity_valid"] = False
        else:
            completed = _proof(ctx, "PROOF.CONTRACT_BINDING", "require_completed_static_validation",
                (contract, "task-contract", ()), "/spec/origin", "completed-task-contract")
            if not _completed_static(completed, "task-contract"):
                if completed is not None:
                    ctx.unavailable("PROOF.CONTRACT_BINDING", "/spec/origin", "completed-task-contract")
                bindings["identity_valid"] = False
            else:
                digest = _proof(ctx, "RC02", "require_digest",
                    (contract, "profile.digest.task-contract-v1", "complete-task-contract", (contract,)),
                    "/spec/origin/contractDigest", "profile.digest.task-contract-v1")
                if digest is None:
                    bindings["identity_valid"] = False
                else:
                    ctx.check("RC02", spec["origin"]["contractDigest"] == digest, "/spec/origin/contractDigest", "contract-binding")
                c, origin = contract["spec"], spec["origin"]
                target = origin["resolvedTarget"]
                comparisons = {
                    "RC01": (origin["contractId"], contract["metadata"]["id"]),
                    "RC03": (spec["taskId"], c["taskId"]), "RC04": (target["projectRef"], c["projectRef"]),
                    "RC05": (target["worktreeRoleRef"], c["target"]["worktreeRoleRef"]),
                    "RC06": (target["worktreeId"], c["target"]["worktreeId"]),
                    "RC07": (target["domainRefs"], c["domainRefs"]), "RC08": (origin["effectiveMode"], c["effectiveMode"]),
                }
                for requirement, (left, right) in comparisons.items():
                    ctx.check(requirement, left == right, "/spec/origin", "contract-binding")
    if stable:
        if len(sources) != 1 or "acquisitionBinding" not in spec or len(selectors["A"]) != 1:
            bindings["identity_valid"] = False
        elif _check_source_shape(sources[0], ctx):
            source, binding = sources[0], spec["acquisitionBinding"]
            digest = _proof(ctx, "PROOF.SOURCE_DIGEST", "require_digest",
                (source, "profile.digest.lease-acquisition-identity-v1", "SourceIdentityProjection", (source,)),
                "/sources/0", "profile.digest.lease-acquisition-identity-v1")
            if digest is None:
                bindings["identity_valid"] = False
            else:
                for requirement, condition in (
                    ("AI19", digest == source["acquisitionResultDigest"]),
                    ("AI16", source["taskId"] == spec["taskId"]),
                    ("AI17", source["checkId"] == binding["checkId"]),
                    ("AI18", source["leaseId"] == binding["leaseId"]),
                    ("AI20", source["acquisitionResultDigest"] == binding["acquisitionResultDigest"]),
                    ("AI21", binding["checkId"] == selectors["A"][0]["checkId"]),
                    ("AI04", selectors["A"][0]["outcome"] == "passed"),
                ):
                    ctx.check(requirement, condition, "/spec/acquisitionBinding", "source-binding")
                reference = {"checkId": binding["checkId"]}
                for alias, requirement in (("A", "AI22"), ("R", "AI23"), ("L", "RF12")):
                    ctx.check(requirement, all(check.get("leaseAcquisitionRef") == reference for check in selectors[alias]),
                              "/spec/checks", "source-binding")
                if bindings["issued"] and contract is not None:
                    ctx.check("RC09", binding["leaseId"] == contract["spec"]["leaseId"],
                              "/spec/acquisitionBinding/leaseId", "contract-binding")
    elif stable is None:
        bindings["identity_valid"] = False
    if len(ctx.diagnostics) != before:
        bindings["identity_valid"] = False
    if not bindings["identity_valid"]:
        ctx.unevaluated = True
    return bindings


def _check_prefix_and_controller(receipt, selectors, bindings, ctx):
    spec, issued, stable = receipt["spec"], bindings["issued"], bindings["stable"]
    before = len(ctx.diagnostics)
    if issued:
        ctx.check("AI02", all(g["outcome"] == "passed" for g in selectors["G"]), "/spec/checks")
        ctx.check("AI08", all(q["outcome"] == "passed" for alias in "RNI" for q in selectors[alias]), "/spec/checks")
        ctx.check("AI12", all(q["sequence"] < i["sequence"] for alias in "RN" for q in selectors[alias] for i in selectors["I"]), "/spec/checks")
        ctx.check("AI13", all(i["sequence"] < p["sequence"] for i in selectors["I"] for p in selectors["P"]), "/spec/checks")
    if stable or issued and stable is False:
        gate = selectors["A"] if stable else selectors["N"]
        ctx.check("AI10", all(g["sequence"] < a["sequence"] for g in selectors["G"] for a in gate), "/spec/checks")
    if stable:
        ctx.check("AI11", all(a["sequence"] < r["sequence"] for a in selectors["A"] for r in selectors["R"]), "/spec/checks")
    if issued:
        return
    origin = spec["origin"]
    checkpoint = origin["denialCheckpoint"]
    state = origin["leaseAcquisition"]["state"]
    if checkpoint in _G_TYPES:
        prerequisites = _G_TYPES[:_G_TYPES.index(checkpoint)]
    elif checkpoint in (_TYPES["N"], _TYPES["A"]):
        prerequisites = _G_TYPES
    elif checkpoint == _TYPES["R"]:
        prerequisites = (*_G_TYPES, _TYPES["A"])
    else:
        prerequisites = (*_G_TYPES, *([_TYPES["A"], _TYPES["R"]] if stable else [_TYPES["N"]]))
    members = {kind: tuple(q for q in spec["checks"] if q["checkType"] == kind) for kind in prerequisites}
    ctx.check("DP01", all(members.values()), "/spec/checks")
    ctx.check("DP02", all(q["outcome"] == "passed" for values in members.values() for q in values), "/spec/checks")
    allowed = set(prerequisites) | {checkpoint}
    ctx.check("DP03", all(q["checkType"] not in _ORDINARY or q["checkType"] in allowed for q in spec["checks"]), "/spec/checks")
    candidates = selectors["controllers"]
    if not ctx.check("DP05", bool(candidates), "/spec/checks"):
        bindings["identity_valid"] = False
        return
    controller = candidates[-1]
    evidence = origin["preContractEvidence"]
    for requirement, condition in (
        ("DP04", all(q["sequence"] < controller["sequence"] for values in members.values() for q in values)),
        ("DP05", evidence["controllerCheckId"] == controller["checkId"]),
        ("DP06", controller["outcome"] in ("failed", "indeterminate")),
        ("DP07", evidence["observedAt"] == controller["observedAt"]),
        ("DP08", evidence["reasonCodes"] == controller["reasonCodes"]),
        ("DP09", all(q["outcome"] == "passed" for q in candidates[:-1])),
        ("RECEIPT.DENIAL_MATRIX", all(q["sequence"] <= controller["sequence"] for q in spec["checks"] if q["checkType"] in _ORDINARY)),
    ):
        ctx.check(requirement, condition, "/spec/origin/preContractEvidence")
    if checkpoint == _TYPES["A"]:
        ctx.check("DP10", len(candidates) == 1, "/spec/checks")
        ctx.check("DP13", state == {"failed": "not-acquired", "indeterminate": "indeterminate"}.get(controller["outcome"]), "/spec/origin/leaseAcquisition")
    if checkpoint == _TYPES["I"]:
        ctx.check("DP11", len(candidates) == 1, "/spec/checks")
        ctx.check("DP12", len(selectors["R"] if stable else selectors["N"]) <= 1, "/spec/checks")
    bindings["controller_equal"] = evidence["observedAt"] == controller["observedAt"]
    if len(ctx.diagnostics) != before:
        bindings["identity_valid"] = False


def _check_receipt_remaining(receipt, selectors, bindings, limits, ctx):
    spec, contract = receipt["spec"], bindings["contract"]
    if not bindings["issued"]:
        return
    attempted = spec["executionOutcome"] != "not-attempted"
    p, e, v = (selectors[alias] for alias in "PEV")
    ctx.check("RECEIPT.P_TERMINAL", all(q["outcome"] == "passed" for q in p) if attempted else all(q["outcome"] == "passed" for q in p[:-1]), "/spec/checks")
    ctx.check("RECEIPT.E_TERMINAL", all(q["outcome"] == "succeeded" for q in e[:-1]), "/spec/checks")
    ctx.check("RECEIPT.FINAL_OUTCOMES", (not e or e[-1]["outcome"] == spec["executionOutcome"]) and (not v or v[-1]["outcome"] == spec["verificationOutcome"]), "/spec/checks")
    ctx.check("RECEIPT.UNIVERSAL_V", spec["verificationOutcome"] != "passed" or all(q["outcome"] == "passed" for q in v), "/spec/checks")
    ctx.check("RECEIPT.PEV_SEQUENCE", (not p or all(p[-1]["sequence"] < q["sequence"] for q in e)) and all(x["sequence"] < y["sequence"] for x in e for y in v), "/spec/checks")
    if contract is None:
        ctx.unevaluated = True
        return
    c = contract["spec"]
    required = c["allowWrite"] and attempted
    ctx.check("RECEIPT.CARRIER_BIND", ("ordinaryOperationEvidence" in spec) == required and (c["allowWrite"] or not spec["changedPaths"]), "/spec/ordinaryOperationEvidence")
    carrier = spec.get("ordinaryOperationEvidence", ())
    paths = {record["path"] for record in carrier}
    ctx.check("RECEIPT.EVIDENCE_SUBSET", paths <= set(spec["changedPaths"]), "/spec/ordinaryOperationEvidence")
    if required and spec["verificationOutcome"] == "passed":
        operations = {op for record in carrier for op in record["operations"]}
        authorized, prohibited = c["authorizedScope"], c["prohibitedScope"]
        scope_valid = operations <= set(authorized["capabilities"]) and not operations.intersection(prohibited["capabilities"])
        for path in paths | set(spec["changedPaths"]):
            allowed = _closed_path_membership(path, {"include": authorized["paths"], "exclude": prohibited["paths"]}, limits, ctx)
            if allowed is None:
                ctx.unevaluated = True
            else:
                scope_valid = scope_valid and allowed
        scope_checks = selectors.per_type.get("scope-contained", ())
        scope_valid = scope_valid and bool(scope_checks) and scope_checks[-1]["outcome"] == "passed"
        ctx.check("RECEIPT.SCOPE", scope_valid, "/spec/ordinaryOperationEvidence")


def _check_postcondition_bindings(receipt, selectors, contract_context, ctx):
    if contract_context is None:
        ctx.unevaluated = True
        return
    required = {p["type"] for p in contract_context["spec"]["requiredPostconditions"]}
    ctx.check("PB04", set(selectors.per_type) <= required, "/spec/checks")
    if receipt["spec"]["executionOutcome"] != "not-attempted":
        ctx.check("PB05", required <= set(selectors.per_type), "/spec/checks")


def _check_outcome_and_finalization(receipt, selectors, ctx):
    spec = receipt["spec"]
    issued = spec["origin"]["type"] == "issued-contract"
    warnings = spec["unresolvedCoordinationWarnings"]
    if selectors["F"]:
        ctx.check("RF08", all(q["sequence"] < selectors["F"][0]["sequence"] for q in selectors["nonF"]), "/spec/checks")
    if selectors["L"]:
        last = selectors["L"][-1]
        ctx.check("RF03", spec["releaseOutcome"] == {"passed": "succeeded", "failed": "failed", "indeterminate": "indeterminate"}[last["outcome"]], "/spec/releaseOutcome")
        ctx.check("RF11", last["outcome"] == "passed" or any(w.get("relatedCheckId") == last["checkId"] for w in warnings), "/spec/unresolvedCoordinationWarnings")
        before = selectors["preRelease"] if issued else selectors["Dpre"]
        ctx.check("RF09" if issued else "RF10", all(q["sequence"] < release["sequence"] for q in before for release in selectors["L"]), "/spec/checks")
    else:
        uncertain = not issued and spec["origin"]["leaseAcquisition"]["state"] == "indeterminate"
        ctx.check("RF03", spec["releaseOutcome"] == ("indeterminate" if uncertain else "not-required"), "/spec/releaseOutcome")
    if issued:
        outcome = None
        for field, value, result in (
            ("releaseOutcome", "indeterminate", "indeterminate"), ("releaseOutcome", "failed", "failed"),
            ("verificationOutcome", "indeterminate", "indeterminate"), ("verificationOutcome", "failed", "failed"),
            ("executionOutcome", "indeterminate", "indeterminate"), ("executionOutcome", "failed", "failed"),
            ("executionOutcome", "cancelled", "cancelled"), ("executionOutcome", "not-attempted", "denied"),
        ):
            if spec[field] == value:
                outcome = result
                break
        if outcome is None:
            outcome = "indeterminate" if warnings else "succeeded"
        ctx.check("RECEIPT.LIFECYCLE", spec["lifecycleOutcome"] == outcome, "/spec/lifecycleOutcome")
    else:
        expected = {"failed": "failed", "indeterminate": "indeterminate"}.get(spec["releaseOutcome"], "denied")
        ctx.check("RECEIPT.DENIAL_OUTCOME", spec["lifecycleOutcome"] == expected and spec["executionOutcome"] == "not-attempted" and spec["verificationOutcome"] == "not-performed" and not spec["changedPaths"] and "ordinaryOperationEvidence" not in spec, "/spec")
        if spec["origin"]["leaseAcquisition"]["state"] == "indeterminate":
            ctx.check("RF14", bool(warnings), "/spec/unresolvedCoordinationWarnings")
