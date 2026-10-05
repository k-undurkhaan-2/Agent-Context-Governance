"""Phase-1 closed-data validation, with explicit external proof obligations.

These results grant no execution authority. No production proof integration is
installed: ordinary decoded mappings can receive diagnostics but cannot receive
full static acceptance merely by claiming trusted provenance.
"""

from ._static_core import (
    DEFAULT_PROOF_LIMITS, ProofObligation, StaticDiagnostic,
    StaticValidationResult, _ValidationContext, _check_canonical_arrays,
    _finish_result, _proof, _root, _validate_shape,
)
from .catalog import SCHEMA_SET_REVISION as _REVISION
from ._static_bundle import (
    _closed_reference_indexes, _check_bundle_references,
    _check_overlap_symmetry, _check_rule_static_relations,
)
from ._static_overlay import (
    _check_overlay_individual, _consume_complete_host_inventory,
    _check_same_host_union,
)
from ._static_baseline import _check_baseline_consistency, _consume_materialized_baseline
from ._static_contract import _check_contract_bindings, _check_contract_plan
from ._static_receipt import (
    _prepare_sequence_selectors, _check_receipt_presence,
    _check_contract_source_bindings, _check_prefix_and_controller,
    _check_receipt_remaining, _check_postcondition_bindings,
    _check_outcome_and_finalization, _completed_static,
)
from ._static_chronology import (
    _check_prefix_chronology, _check_remaining_chronology, _relation,
)

__all__ = [
    "StaticDiagnostic", "ProofObligation", "StaticValidationResult",
    "DEFAULT_PROOF_LIMITS", "validate_governance_bundle", "validate_host_overlay",
    "validate_same_host_inventory", "validate_task_contract_static",
    "validate_execution_receipt_static", "validate_delivery_pair_static",
]


def _prepare(subject, name, ctx):
    root = _root(name)
    if not _validate_shape(subject, root, ctx):
        ctx.unevaluated = True
        return False
    _proof(ctx, "PROOF.INPUT", "require_input_provenance", (subject, root, _REVISION), profile="prepared-input")
    _check_canonical_arrays(subject, root, ctx)
    return not ctx.failed


def _bundle(bundle, ctx):
    if not _prepare(bundle, "governance-bundle", ctx):
        return None
    indexes = _closed_reference_indexes(bundle, ctx)
    _check_bundle_references(bundle, indexes, ctx)
    _check_overlap_symmetry(bundle, indexes, ctx)
    _check_rule_static_relations(bundle, indexes, ctx)
    return indexes if not ctx.failed else None


def validate_governance_bundle(bundle, *, proof_context=None):
    ctx = _ValidationContext(bundle, _root("governance-bundle"), proof_context)
    _bundle(bundle, ctx)
    return _finish_result("governance-bundle", ctx)


def validate_host_overlay(overlay, *, bundle, proof_context=None, limits=DEFAULT_PROOF_LIMITS):
    ctx = _ValidationContext(overlay, _root("host-overlay"), proof_context)
    if _prepare(overlay, "host-overlay", ctx):
        indexes = _bundle(bundle, ctx)
        if indexes is not None:
            _check_overlay_individual(overlay, bundle, indexes, limits, ctx)
        else:
            ctx.unevaluated = True
    return _finish_result("host-overlay-individual", ctx)


def validate_same_host_inventory(*, host_id, inventory_context, proof_context=None, limits=DEFAULT_PROOF_LIMITS):
    ctx = _ValidationContext(inventory_context, _root("host-overlay"), proof_context)
    snapshot = _consume_complete_host_inventory(host_id, inventory_context, ctx)
    # This private consumer payload is obtained only through an opaque proof
    # handle; a caller-provided inventory map never establishes completeness.
    if snapshot is not None:
        try:
            members, trusted_roots = snapshot
            validated, roots = [], list(trusted_roots)
            for overlay, bundle in members:
                result = validate_host_overlay(overlay, bundle=bundle, proof_context=proof_context, limits=limits)
                ctx.diagnostics.extend(result.diagnostics)
                ctx.required_proofs.extend(result.required_proofs)
                ctx.failed = ctx.failed or result.status == "INVALID"
                ctx.unevaluated = ctx.unevaluated or not result.full_static_acceptance
                ctx.check("PROOF.SNAPSHOT", overlay["spec"]["hostId"] == host_id, "/spec/hostId")
                if result.full_static_acceptance:
                    validated.append(overlay)
                    roots.extend((kind, overlay["spec"][kind]) for kind in ("stateRoot", "lockRoot"))
            for kind, root in roots:
                if kind not in ("stateRoot", "lockRoot"):
                    raise ValueError("Unrecognized coordination-root purpose")
                _validate_shape(root, _root("common") + "#/$defs/absoluteHostPath", ctx)
            if not ctx.failed and not ctx.unevaluated:
                _check_same_host_union(validated, roots, ctx)
        except (TypeError, ValueError, KeyError):
            ctx.unavailable("PROOF.SNAPSHOT", profile="complete-snapshot-operands")
    else:
        ctx.unevaluated = True
    return _finish_result("same-host-inventory", ctx)


def validate_task_contract_static(contract, *, bundle, host_overlay, proof_context=None, baseline_context=None, limits=DEFAULT_PROOF_LIMITS):
    ctx = _ValidationContext(contract, _root("task-contract"), proof_context)
    ctx.limits = limits
    if _prepare(contract, "task-contract", ctx):
        indexes = _bundle(bundle, ctx)
        if indexes is not None and _prepare(host_overlay, "host-overlay", ctx):
            _check_overlay_individual(host_overlay, bundle, indexes, limits, ctx)
            if not ctx.failed:
                _check_contract_bindings(contract, bundle, host_overlay, ctx)
                materialized = _consume_materialized_baseline(contract, baseline_context, ctx)
                _check_baseline_consistency(contract["spec"]["expectedBaseline"], materialized, ctx)
                _check_contract_plan(contract, materialized, limits, ctx)
                _check_prefix_chronology(None, None, {"contract": contract}, ctx)
        else:
            ctx.unevaluated = True
    return _finish_result("task-contract", ctx)


def validate_execution_receipt_static(receipt, *, contract_context=None, sources=(), proof_context=None, limits=DEFAULT_PROOF_LIMITS):
    ctx = _ValidationContext(receipt, _root("execution-receipt"), proof_context)
    if _prepare(receipt, "execution-receipt", ctx):
        selectors = _prepare_sequence_selectors(receipt, ctx)
        if selectors is not None:
            bindings = _check_receipt_presence(receipt, selectors, contract_context, sources, ctx)
            if not ctx.failed:
                _check_contract_source_bindings(receipt, selectors, bindings, sources, ctx)
                if bindings["identity_valid"] and not ctx.failed:
                    _check_prefix_and_controller(receipt, selectors, bindings, ctx)
                    _check_prefix_chronology(receipt, selectors, bindings, ctx)
                    if not bindings["issued"] and bindings["identity_valid"] and not ctx.failed:
                        digest = _proof(ctx, "PROOF.DENIAL_DIGEST", "require_digest",
                            (receipt, "profile.digest.pre-contract-evidence-v1", "DenialEvidenceProjection", tuple(sources)),
                            "/spec/origin/preContractEvidence/evidenceDigest", "profile.digest.pre-contract-evidence-v1")
                        if digest is not None:
                            ctx.check("PROOF.DENIAL_DIGEST", digest == receipt["spec"]["origin"]["preContractEvidence"]["evidenceDigest"], "/spec/origin/preContractEvidence/evidenceDigest")
                    _check_receipt_remaining(receipt, selectors, bindings, limits, ctx)
                    if bindings["issued"]:
                        _check_postcondition_bindings(receipt, selectors, bindings["contract"], ctx)
                    _check_remaining_chronology(receipt, selectors, bindings, ctx)
                    _check_outcome_and_finalization(receipt, selectors, ctx)
            if not ctx.failed and not ctx.unevaluated and not ctx.required_proofs:
                prerequisites = (contract_context,) if bindings["issued"] else tuple(sources)
                digest = _proof(ctx, "PROOF.RECEIPT_DIGEST", "require_digest",
                    (receipt, "profile.digest.execution-receipt-v1", "ReceiptDigestProjection", prerequisites),
                    "/spec/receiptDigest", "profile.digest.execution-receipt-v1")
                if digest is not None:
                    ctx.check("PROOF.RECEIPT_DIGEST", digest == receipt["spec"]["receiptDigest"], "/spec/receiptDigest")
    return _finish_result("execution-receipt", ctx)


def validate_delivery_pair_static(delivery, receipt, *, proof_context=None):
    ctx = _ValidationContext(receipt, _root("execution-receipt"), proof_context)
    completed = _proof(ctx, "PROOF.RECEIPT_DIGEST", "require_completed_static_validation",
                       (receipt, "execution-receipt", ()), profile="completed-static-and-codec-receipt")
    if not _completed_static(completed, "execution-receipt"):
        ctx.unavailable("PROOF.RECEIPT_DIGEST", profile="completed-static-and-codec-receipt")
    elif _prepare(delivery, "receipt-delivery-result", ctx) and _validate_shape(receipt, _root("execution-receipt"), ctx):
        ctx.check("DELIVERY.ID", delivery["receiptId"] == receipt["metadata"]["id"], "/receiptId")
        ctx.check("DELIVERY.COPY", delivery["receiptDigest"] == receipt["spec"]["receiptDigest"], "/receiptDigest")
        _relation(ctx, 19, (receipt["spec"]["finishedAt"] <= delivery["attemptedAt"],))
    return _finish_result("delivery-pair", ctx)
