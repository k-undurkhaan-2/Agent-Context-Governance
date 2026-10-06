"""Twenty primitive relation owners and eleven derived displays."""

from copy import deepcopy
import pytest
from contextctl_schema._static_receipt import _prepare_sequence_selectors
from contextctl_schema._static_chronology import (
    _check_prefix_chronology, _check_remaining_chronology, _derive_chronology_relations,
)
from tests.schema.s4_synthetic import context, issued, denial, selected, stamp, codes, resequence


def temporal_pair(lease=True):
    r, c, _ = issued(lease)
    c["spec"]["issuanceCheckpoint"]["observedAt"] = stamp(8)
    c["spec"]["freshness"].update(issuedAt=stamp(9), expiresAt=stamp(20))
    times = {"lease-acquisition": 5, "post-acquisition-revalidation": 6, "pre-issuance-revalidation": 6,
             "contract-issuance": 10, "pre-action-revalidation": 11, "execution": 12,
             "post-execution-verification": 13, "lease-release": 14, "receipt-finalization": 16}
    for q in r["spec"]["checks"]:
        q["observedAt"] = stamp(times.get(q["checkType"], 2))
    r["spec"]["sanitization"]["completedAt"] = stamp(15)
    r["spec"]["finishedAt"] = stamp(17)
    return r, c


@pytest.mark.parametrize("number", range(1, 21), ids=lambda n: f"CH{n:02d}")
def test_primitive_owners(number):
    r, c = temporal_pair(number not in (9, 12))
    bindings = {"contract": c, "stable": c["spec"]["leaseRequired"]}
    if number == 16:
        r, _ = denial("post-acquisition-revalidation", "acquired")
        c = None
        bindings = {"contract": None, "stable": True, "controller_equal": True}
    if number == 20:
        earlier = deepcopy(selected(r, "lease-release")[0])
        earlier["checkId"] = "check.release-earlier"
        r["spec"]["checks"].insert(earlier["sequence"], earlier)
        resequence(r)
    if number == 19:
        bindings["delivery"] = {"attemptedAt": stamp(17)}
    def run():
        ctx = context(r)
        selectors = _prepare_sequence_selectors(r, ctx)
        _check_prefix_chronology(r, selectors, bindings, ctx)
        _check_remaining_chronology(r, selectors, bindings, ctx)
        return ctx
    assert not run().failed
    def at(kind, second, index=0):
        selected(r, kind)[index]["observedAt"] = stamp(second)
    if number == 1:
        c["spec"]["issuanceCheckpoint"]["observedAt"] = stamp(10)
    elif number == 2:
        c["spec"]["freshness"]["expiresAt"] = stamp(9)
        r["spec"]["checks"] = [q for q in r["spec"]["checks"] if q["checkType"] not in ("pre-action-revalidation", "execution", "post-execution-verification")]
        r["spec"].update(executionOutcome="not-attempted", verificationOutcome="not-performed")
        resequence(r)
    elif number == 3:
        r["spec"]["startedAt"] = stamp(3)
    elif number == 4:
        r["spec"]["sanitization"]["completedAt"] = stamp(13)
    elif number == 5:
        c["spec"]["freshness"]["expiresAt"] = stamp(11)
    elif number == 6:
        at("execution", 10)
    elif number == 7:
        at("post-execution-verification", 11)
    elif number == 8:
        at("intent-validation", 6)
    elif number == 9:
        at("intent-validation", 7)
    elif number == 10:
        at("post-acquisition-revalidation", 4)
    elif number == 11:
        at("post-acquisition-revalidation", 9)
    elif number == 12:
        at("pre-issuance-revalidation", 9)
    elif number == 13:
        at("contract-issuance", 8)
    elif number == 14:
        at("pre-action-revalidation", 9)
    elif number == 15:
        at("lease-release", 12)
    elif number == 16:
        at("post-acquisition-revalidation", 1)
        at("receipt-finalization", 2)
        r["spec"]["sanitization"]["completedAt"] = stamp(2)
        r["spec"]["finishedAt"] = stamp(2)
    elif number == 17:
        r["spec"]["sanitization"]["completedAt"] = stamp(17)
    elif number == 18:
        r["spec"]["finishedAt"] = stamp(15)
    elif number == 19:
        bindings["delivery"]["attemptedAt"] = stamp(16)
    elif number == 20:
        at("lease-release", 15)
    assert {code for code in codes(run()) if code.startswith("S4.CH")} == {f"S4.CH{number:02d}"}


@pytest.mark.parametrize("number", range(21, 32))
def test_derived_display_requires_all_premises(number):
    primitives = {f"CH{i:02d}": True for i in range(1, 21)}
    applicability = dict.fromkeys(("nonF", "F", "issued", "denial", "R", "N", "L"), True)
    ctx = context()
    assert _derive_chronology_relations(primitives, applicability, ctx)[f"CH.DERIVED.{number}"] is True
    assert _derive_chronology_relations({}, applicability, ctx)[f"CH.DERIVED.{number}"] is None
    assert not ctx.diagnostics


def test_selectors_ignore_time_order():
    r, _ = temporal_pair()
    original = _prepare_sequence_selectors(r, context())
    selected(r, "execution")[0]["observedAt"] = stamp(1)
    new = _prepare_sequence_selectors(r, context())
    assert new["E"][-1]["checkId"] == original["E"][-1]["checkId"]
