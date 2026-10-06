"""Exact finite-language proof and fail-closed bounds; never sampled inclusion."""

import pytest
from contextctl_schema import _static_paths as paths
from contextctl_schema._static_core import DEFAULT_PROOF_LIMITS, _proof
from tests.schema.s4_synthetic import proofs, context, codes

METRICS = []


def scope(include, exclude=()):
    return {"include": list(include), "exclude": list(exclude)}


@pytest.mark.parametrize("overlay,domains,expected", [
    (scope(["src/lib/**"]), [scope(["src/**"])], True),
    (scope(["src/**"]), [scope(["src/**"])], True),
    (scope([]), [scope(["src/**"])], True),
    (scope(["src/**"], ["src/private/**"]), [scope(["src/**"])], True),
    (scope(["a", "b"]), [scope(["a"]), scope(["b"])], True),
    (scope(["docs/**"]), [scope(["src/**"])], False),
    (scope(["a"]), [scope(["?"])], True),
    (scope(["ab"]), [scope(["?"])], False),
    (scope(["a/b"]), [scope(["*"])], False),
    (scope(["a/b"]), [scope(["a/**/b"])], True),
    (scope(["a/x/y/b"]), [scope(["a/**/b"])], True),
    (scope(["a/b"]), [scope(["**/**/b"])], True),
    (scope(["a"]), [scope(["**/a"])], True),
    (scope(["a"]), [scope(["a/**"])], True),
    (scope(["a/b"]), [scope(["a/**"], ["a/b"])], False),
    (scope(["\U0001f600"]), [scope(["?"])], True),
    (scope([".GIT/a"]), [scope(["**"])], True),
])
def test_exact_language(overlay, domains, expected):
    ctx = context()
    assert paths._prove_scope_subset(overlay, domains, DEFAULT_PROOF_LIMITS, ctx) is expected
    METRICS.extend(ctx.path_metrics)
    assert ("reason.overlay.path-widening" in codes(ctx)) is (not expected)


@pytest.mark.parametrize("pattern", [".git", "a/.git/b", "a**", "***", "!a", "{a,b}", "[ab]", "a\\b", "/a", "C:/a", "a//b", "a/./b", "a/../b"])
def test_unsupported_grammar(pattern):
    ctx = context()
    assert paths._prove_scope_subset(scope([pattern]), [scope(["**"])], DEFAULT_PROOF_LIMITS, ctx) is None
    assert "reason.overlay.path-proof-unavailable" in codes(ctx)


@pytest.mark.parametrize("path,expected", [("a", True), ("a" * 4096, True), ("a" * 4097, False), (".git/a", False), ("a/.git", False), (".GIT", True), (".gitx", True), ("a/../b", False)])
def test_relative_universe(path, expected, proofs):
    ctx = context({}, proofs.context)
    _proof(ctx, "PROOF.INPUT", "require_input_provenance", (ctx.subject, ctx.root_id, "synthetic-revision"))
    assert paths._closed_path_membership(path, scope(["**"]), DEFAULT_PROOF_LIMITS, ctx) is expected
    METRICS.extend(ctx.path_metrics)


@pytest.mark.parametrize("limit", ["max_nfa_states", "max_product_states", "max_transition_steps", "max_work_units"])
def test_limit_exhaustion(limit):
    limits = dict(DEFAULT_PROOF_LIMITS, **{limit: 1})
    ctx = context()
    assert paths._prove_scope_subset(scope(["src/**"]), [scope(["src/**"])], limits, ctx) is None
    assert "reason.overlay.path-proof-unavailable" in codes(ctx)
    METRICS.extend(ctx.path_metrics)


@pytest.mark.parametrize("bad", [True, 0, -1, 16385])
def test_invalid_limits(bad):
    ctx = context()
    assert paths._prove_scope_subset(scope([]), [], dict(DEFAULT_PROOF_LIMITS, max_nfa_states=bad), ctx) is None


def test_non_nfc_singleton_is_removed_exactly():
    ctx = context()
    assert paths._prove_scope_subset(scope(["e\u0301"]), [], DEFAULT_PROOF_LIMITS, ctx) is True
    assert ctx.path_metrics[-1]["max_nfc_refinements"] == 1
    ctx = context()
    assert paths._prove_scope_subset(scope(["e\u0301", "\u00e9"]), [], DEFAULT_PROOF_LIMITS, ctx) is False


def test_refinement_exhaustion_and_compile_failure(monkeypatch):
    ctx = context()
    assert paths._prove_scope_subset(scope(["e\u0301", "a\u0301"]), [], dict(DEFAULT_PROOF_LIMITS, max_nfc_refinements=1), ctx) is None
    monkeypatch.setattr(paths, "_compile_scope", lambda *args: (_ for _ in ()).throw(MemoryError()))
    assert paths._prove_scope_subset(scope(["a"]), [], DEFAULT_PROOF_LIMITS, context()) is None


def test_indeterminate_and_missing_unicode_fail_closed(monkeypatch):
    monkeypatch.setattr(paths, "_exact_nfc_relative_emptiness", lambda *args: None)
    assert paths._prove_scope_subset(scope(["a"]), [], DEFAULT_PROOF_LIMITS, context()) is None


def test_path_membership_cannot_bypass_input_proof():
    ctx = context()
    assert paths._closed_path_membership("a", scope(["**"]), DEFAULT_PROOF_LIMITS, ctx) is None
