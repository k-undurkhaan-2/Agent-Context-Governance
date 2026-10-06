"""The 20 primitive chronology families and 11 transitive displays.

All timestamps have already passed the canonical UTC profile. Lexicographic
comparison therefore compares the represented whole-second instants exactly.
There is no clock read, global monotonicity, event-authenticity assertion or
time-based selector here.
"""


def _relation(ctx, number, comparisons):
    valid = all(comparisons)
    identifier = f"CH{number:02d}"
    if not hasattr(ctx, "chronology"):
        ctx.chronology = {}
    ctx.chronology[identifier] = valid
    ctx.check(identifier, valid, "", "chronology")


def _check_prefix_chronology(receipt, selectors, bindings, ctx):
    contract = bindings.get("contract")
    if receipt is None:
        if contract is not None:
            spec = contract["spec"]
            _relation(ctx, 1, (spec["issuanceCheckpoint"]["observedAt"] <= spec["freshness"]["issuedAt"],))
            _relation(ctx, 2, (spec["freshness"]["issuedAt"] < spec["freshness"]["expiresAt"],))
        return
    if bindings.get("stable") and len(selectors["A"]) == 1:
        acquisition = selectors["A"][0]["observedAt"]
        _relation(ctx, 8, (g["observedAt"] <= acquisition for g in selectors["G"]))
        _relation(ctx, 10, (acquisition <= r["observedAt"] for r in selectors["R"]))


def _check_remaining_chronology(receipt, selectors, bindings, ctx):
    spec = receipt["spec"]
    contract = bindings.get("contract")
    issued = spec["origin"]["type"] == "issued-contract"
    stable = bindings.get("stable")
    _relation(ctx, 3, (spec["startedAt"] <= q["observedAt"] for q in spec["checks"]))
    _relation(ctx, 4, (q["observedAt"] <= spec["sanitization"]["completedAt"] for q in selectors["nonF"]))
    _relation(ctx, 17, (spec["sanitization"]["completedAt"] <= f["observedAt"] for f in selectors["F"]))
    _relation(ctx, 18, (f["observedAt"] <= spec["finishedAt"] for f in selectors["F"]))
    if issued and contract is not None:
        c = contract["spec"]
        checkpoint = c["issuanceCheckpoint"]["observedAt"]
        issued_at, expiry = c["freshness"]["issuedAt"], c["freshness"]["expiresAt"]
        _relation(ctx, 1, (checkpoint <= issued_at,))
        _relation(ctx, 2, (issued_at < expiry,))
        _relation(ctx, 5, (p["observedAt"] < expiry for p in selectors["P"] if p["outcome"] == "passed"))
        if not c["leaseRequired"] and len(selectors["N"]) == 1:
            n = selectors["N"][0]["observedAt"]
            _relation(ctx, 9, (g["observedAt"] <= n for g in selectors["G"]))
            _relation(ctx, 12, (n <= checkpoint,))
        if c["leaseRequired"] and len(selectors["R"]) == 1:
            _relation(ctx, 11, (selectors["R"][0]["observedAt"] <= checkpoint,))
        if len(selectors["I"]) == 1:
            issuance = selectors["I"][0]["observedAt"]
            _relation(ctx, 13, (issued_at <= issuance,))
            _relation(ctx, 14, (issuance <= p["observedAt"] for p in selectors["P"]))
        if spec["executionOutcome"] != "not-attempted":
            if selectors["P"]:
                _relation(ctx, 6, (selectors["P"][-1]["observedAt"] <= e["observedAt"] for e in selectors["E"]))
            _relation(ctx, 7, (e["observedAt"] <= v["observedAt"] for e in selectors["E"] for v in selectors["V"]))
    if stable:
        before_release = selectors["preRelease"] if issued else selectors["Dpre"]
        _relation(ctx, 15 if issued else 16,
                  (q["observedAt"] <= release["observedAt"] for q in before_release for release in selectors["L"]))
        _relation(ctx, 20, (earlier["observedAt"] <= later["observedAt"]
                  for i, earlier in enumerate(selectors["L"]) for later in selectors["L"][i + 1:]))
    delivery = bindings.get("delivery")
    if delivery is not None:
        _relation(ctx, 19, (spec["finishedAt"] <= delivery["attemptedAt"],))
    applicability = {
        "nonF": bool(selectors["nonF"]), "F": len(selectors["F"]) == 1,
        "issued": issued and contract is not None,
        "denial": not issued and bindings.get("controller_equal", False),
        "R": issued and stable and len(selectors["R"]) == 1,
        "N": issued and stable is False and len(selectors["N"]) == 1,
        "L": stable and bool(selectors["L"]),
    }
    ctx.derived_chronology = _derive_chronology_relations(ctx.chronology, applicability, ctx)


def _derive_chronology_relations(validated_primitives, applicability, ctx):
    """Expose closure only after its actual operands and premises are valid.

    A failed derived display belongs to its failed primitive owner; it never
    creates a duplicate diagnostic or a twenty-first primitive relation.
    """
    specifications = {
        21: ((3, 4), ("nonF",)),
        22: ((17, 18), ("F",)),
        23: ((3, 4, 17, 18), ("nonF", "F")),
        24: ((3,), ("denial",)),
        25: ((4,), ("denial",)),
        26: ((4, 17), ("denial", "F")),
        27: ((3, 1, 11 if applicability.get("R") else 12), ("issued",)),
        28: ((16,), ("denial", "L")),
        29: ((4, 17), ("nonF", "F")),
        30: ((11, 1), ("R",)),
        31: ((12, 1), ("N",)),
    }
    return {f"CH.DERIVED.{number}": (
        True if all(applicability.get(name) for name in required)
        and all(validated_primitives.get(f"CH{p:02d}") is True for p in premises) else None)
        for number, (premises, required) in specifications.items()}
