"""Receipt acceptance is a prerequisite to optional delivery pair checks."""

import pytest
from contextctl_schema.static_validation import validate_delivery_pair_static
from tests.schema.s4_synthetic import proofs, resource, delivery, codes


@pytest.mark.parametrize("fault", [None, "id", "digest", "time", "proof", "scope"])
def test_delivery_pair(fault, proofs):
    r, d = resource("ExecutionReceipt"), delivery()
    if fault != "proof":
        proofs.complete(r, "governance-bundle" if fault == "scope" else "execution-receipt")
    if fault == "id":
        d["receiptId"] = "00000000-0000-4000-8000-000000000099"
    elif fault == "digest":
        d["receiptDigest"] = "sha256:" + "1" * 64
    elif fault == "time":
        d["attemptedAt"] = "1999-12-31T23:59:59Z"
    result = validate_delivery_pair_static(d, r, proof_context=proofs.context)
    assert result.status == ("PASS" if fault is None else "PROOF_REQUIRED" if fault in ("proof", "scope") else "INVALID")
    if fault in ("proof", "scope"):
        assert not {"S4.DELIVERY.ID", "S4.DELIVERY.COPY", "S4.CH19"}.intersection(codes(result))
