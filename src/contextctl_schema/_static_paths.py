"""Exact bounded restricted-glob language proofs, with no host interpretation.

The residual is a lazy DFA product over exact scalar intervals. Non-NFC
accepted words are removed by singleton-language complement, never sampling.
"""

from collections import deque
import unicodedata

from ._static_core import DEFAULT_PROOF_LIMITS


class _Unavailable(Exception):
    pass


class _AutomatonAndBudget:
    def __init__(self, limits):
        if (set(limits) != set(DEFAULT_PROOF_LIMITS)
                or any(type(limits[k]) is not int or not 0 < limits[k] <= maximum
                       for k, maximum in DEFAULT_PROOF_LIMITS.items())):
            raise _Unavailable
        self.limits = dict(limits)
        self.counts = dict.fromkeys(DEFAULT_PROOF_LIMITS, 0)

    def use(self, key, amount=1):
        self.counts[key] += amount
        if self.counts[key] > self.limits[key]:
            raise _Unavailable
        if key != "max_work_units":
            self.use("max_work_units", amount)


# NUL, separator, backslash and surrogate code points are not segment scalars.
_SCALARS = ((1, 46), (48, 91), (93, 0xD7FF), (0xE000, 0x10FFFF))


class _NFA:
    def __init__(self, budget):
        self.budget = budget
        self.edges = []
        self.epsilon = []
        self.start = self.state()
        self.accepts = set()

    def state(self):
        self.budget.use("max_nfa_states")
        result = len(self.edges)
        self.edges.append([])
        self.epsilon.append([])
        return result

    def edge(self, source, target, intervals):
        self.budget.use("max_work_units")
        self.edges[source].extend((lo, hi, target) for lo, hi in intervals)

    def closure(self, states):
        found = set(states)
        pending = list(sorted(found, reverse=True))
        while pending:
            state = pending.pop()
            self.budget.use("max_work_units")
            for target in self.epsilon[state]:
                if target not in found:
                    found.add(target)
                    pending.append(target)
        return tuple(sorted(found))


class _DFA:
    def __init__(self, nfa, budget):
        self.nfa, self.budget = nfa, budget
        self.start = nfa.closure((nfa.start,))
        self.cache = {}
        self.sink = ()
        self.alphabet = ()

    def step(self, state, scalar):
        key = state, scalar
        if key not in self.cache:
            targets = set()
            for source in state:
                for lo, hi, target in self.nfa.edges[source]:
                    self.budget.use("max_work_units")
                    if lo <= scalar <= hi:
                        targets.add(target)
            self.cache[key] = self.nfa.closure(targets)
        return self.cache[key]

    def accepting(self, state):
        return bool(self.nfa.accepts.intersection(state))


def _parse_pattern(pattern, ctx):
    if (not isinstance(pattern, str) or not 1 <= len(pattern) <= 4096
            or pattern.startswith("/") or pattern.endswith("/")
            or (len(pattern) > 1 and pattern[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" and pattern[1] == ":")
            or any(c in "\\\0!{}[]()" or 0xD800 <= ord(c) <= 0xDFFF for c in pattern)):
        raise _Unavailable
    components = tuple(pattern.split("/"))
    if any(c in ("", ".", "..", ".git") or ("**" in c and c != "**") for c in components):
        raise _Unavailable
    return components


def _compile_component_nfa(tokens, budget):
    nfa = _NFA(budget)
    # The second coordinate proves at least one scalar was consumed. An
    # all-star component cannot manufacture an empty path segment.
    states = {(0, False): nfa.start}
    def state(position, consumed):
        key = position, consumed
        if key not in states:
            states[key] = nfa.state()
        return states[key]
    for position, token in enumerate(tokens):
        for consumed in (False, True):
            source = state(position, consumed)
            if token == "*":
                nfa.epsilon[source].append(state(position + 1, consumed))
                nfa.edge(source, state(position, True), _SCALARS)
            else:
                nfa.edge(source, state(position + 1, True),
                         _SCALARS if token == "?" else ((ord(token), ord(token)),))
    nfa.accepts.add(state(len(tokens), True))
    return nfa


def _compile_pattern_nfa(components, budget):
    nfa = _NFA(budget)
    boundaries = {(0, False): nfa.start}
    def boundary(position, seen):
        key = position, seen
        if key not in boundaries:
            boundaries[key] = nfa.state()
        return boundaries[key]
    for i, component in enumerate(components):
        fragment = _compile_component_nfa("*" if component == "**" else component, budget)
        for seen in (False, True):
            source = boundary(i, seen)
            if component == "**":
                nfa.epsilon[source].append(boundary(i + 1, seen))
            imported = [nfa.state() for _ in fragment.edges]
            if seen:
                nfa.edge(source, imported[fragment.start], ((47, 47),))
            else:
                nfa.epsilon[source].append(imported[fragment.start])
            for j, edges in enumerate(fragment.edges):
                for lo, hi, destination in edges:
                    nfa.edge(imported[j], imported[destination], ((lo, hi),))
                nfa.epsilon[imported[j]].extend(imported[k] for k in fragment.epsilon[j])
            target = boundary(i if component == "**" else i + 1, True)
            for accepting in fragment.accepts:
                nfa.epsilon[imported[accepting]].append(target)
    nfa.accepts.update(boundary(len(components), seen) for seen in (False, True))
    return nfa


def _determinize_lazy(nfa, budget):
    return _DFA(nfa, budget)


def _complete_dfa(dfa, alphabet_partition, budget):
    # Empty subset is an explicit rejecting sink, including all missing edges.
    dfa.alphabet = tuple(alphabet_partition)
    for scalar in dfa.alphabet:
        dfa.cache[(dfa.sink, scalar)] = dfa.sink
    return dfa


def _compile_scope(scope, budget):
    return tuple(tuple(_determinize_lazy(_compile_pattern_nfa(
        _parse_pattern(pattern, None), budget), budget)
        for pattern in scope.get(field, ())) for field in ("include", "exclude"))


class _Universe:
    start = (0, False, "")

    def step(self, state, scalar):
        if state is None:
            return None
        length, first_letter, component = state
        if (length == 4096 or scalar in (0, 92) or 0xD800 <= scalar <= 0xDFFF
                or (length == 1 and first_letter and scalar == 58)):
            return None
        if scalar == 47:
            if component in ("", ".", "..", ".git"):
                return None
            component = ""
        elif component != "*":
            candidate = component + chr(scalar)
            component = candidate if any(s.startswith(candidate) for s in (".", "..", ".git")) else "*"
        return length + 1, length == 0 and (65 <= scalar <= 90 or 97 <= scalar <= 122), component

    def accepting(self, state):
        return state is not None and state[0] > 0 and state[2] not in ("", ".", "..", ".git")


def _build_relative_universe_lexical_dfa(budget):
    return _Universe()


class _Residual:
    def __init__(self, universe, overlay, domains, budget):
        self.universe, self.budget = universe, budget
        self.scopes = (overlay, *domains)
        self.dfas = tuple(dfa for scope in self.scopes for side in scope for dfa in side)
        self.excluded = []

    def alphabet(self):
        boundaries = {0, 1, 47, 48, 58, 59, 65, 91, 92, 93, 97, 123,
                      0xD800, 0xE000, 0x110000}
        for char in ".git":
            boundaries.update((ord(char), ord(char) + 1))
        for dfa in self.dfas:
            for edges in dfa.nfa.edges:
                for lo, hi, _ in edges:
                    boundaries.update((lo, hi + 1))
        for word in self.excluded:
            for char in word:
                boundaries.update((ord(char), ord(char) + 1))
        points = sorted(boundaries)
        return tuple(x for x in points[:-1] if not 0xD800 <= x <= 0xDFFF)

    def accepting(self, state):
        universe, states, excluded_states = state
        if not self.universe.accepting(universe):
            return False
        if any(position == len(word) for position, word in zip(excluded_states, self.excluded)):
            return False
        offset = 0
        scope_accepts = []
        for includes, excludes in self.scopes:
            included = any(dfa.accepting(states[offset + i]) for i, dfa in enumerate(includes))
            offset += len(includes)
            excluded = any(dfa.accepting(states[offset + i]) for i, dfa in enumerate(excludes))
            offset += len(excludes)
            scope_accepts.append(included and not excluded)
        return scope_accepts[0] and not any(scope_accepts[1:])

    def search(self):
        alphabet = self.alphabet()
        for dfa in self.dfas:
            _complete_dfa(dfa, alphabet, self.budget)
        start = self.universe.start, tuple(d.start for d in self.dfas), (0,) * len(self.excluded)
        predecessor = {start: None}
        queue = deque((start,))
        self.budget.use("max_product_states")
        while queue:
            state = queue.popleft()
            if self.accepting(state):
                scalars = []
                current = state
                while predecessor[current] is not None:
                    current, scalar = predecessor[current]
                    scalars.append(chr(scalar))
                return "".join(reversed(scalars))
            for scalar in alphabet:
                self.budget.use("max_transition_steps")
                universe = self.universe.step(state[0], scalar)
                if universe is None:
                    continue
                next_states = tuple(d.step(s, scalar) for d, s in zip(self.dfas, state[1]))
                # All overlay include automata in a rejecting sink can never
                # accept a suffix. This is exact DFA dead-state pruning.
                if not any(next_states[:len(self.scopes[0][0])]):
                    continue
                excluded_states = tuple(position + 1 if 0 <= position < len(word)
                    and ord(word[position]) == scalar else -1
                    for position, word in zip(state[2], self.excluded))
                target = universe, next_states, excluded_states
                if target not in predecessor:
                    self.budget.use("max_product_states")
                    predecessor[target] = state, scalar
                    queue.append(target)
        return None


def _product_residual(universe, overlay, project_domain_scopes, budget):
    return _Residual(universe, overlay, project_domain_scopes, budget)


def _exact_nfc_relative_emptiness(residual, budget):
    if unicodedata.unidata_version != "15.1.0":
        raise _Unavailable
    while True:
        witness = residual.search()
        if witness is None:
            return True
        # This is membership of a hypothetical exact accepted word, not
        # normalization, decoding or repair of a supplied governance value.
        if unicodedata.is_normalized("NFC", witness):
            return False
        budget.use("max_nfc_refinements")
        residual.excluded.append(witness)


def _prove_scope_subset(overlay_scope, project_domain_scopes, limits, ctx):
    budget = None
    try:
        budget = _AutomatonAndBudget(limits)
        overlay = _compile_scope(overlay_scope, budget)
        project = tuple(_compile_scope(scope, budget) for scope in project_domain_scopes)
        residual = _product_residual(_build_relative_universe_lexical_dfa(budget), overlay, project, budget)
        result = _exact_nfc_relative_emptiness(residual, budget)
        if type(result) is not bool:
            raise _Unavailable
        ctx.check(getattr(ctx, "path_requirement", "D10.path-widening"),
                  result, ctx.location, "path-language")
        return result
    except (Exception, MemoryError):
        ctx.unavailable("D10.path-proof-unavailable", ctx.location,
                        "exact-path-language", direct=True)
        return None
    finally:
        if budget is not None:
            ctx.path_metrics.append(dict(budget.counts))


def _closed_path_membership(path, scope, limits, ctx):
    if not any(operation == "require_input_provenance" for operation, _, _ in ctx.proofs):
        ctx.unavailable("PROOF.INPUT", ctx.location, "path-input-provenance")
        return None
    try:
        budget = _AutomatonAndBudget(limits)
        compiled = _compile_scope(scope, budget)
        universe = _build_relative_universe_lexical_dfa(budget)
        ustate = universe.start
        dfas = tuple(d for side in compiled for d in side)
        states = tuple(d.start for d in dfas)
        for scalar in map(ord, path):
            budget.use("max_transition_steps")
            ustate = universe.step(ustate, scalar)
            states = tuple(d.step(s, scalar) for d, s in zip(dfas, states))
        count = len(compiled[0])
        result = (universe.accepting(ustate)
                  and any(d.accepting(s) for d, s in zip(dfas[:count], states[:count]))
                  and not any(d.accepting(s) for d, s in zip(dfas[count:], states[count:])))
        ctx.path_metrics.append(dict(budget.counts))
        return result
    except (Exception, MemoryError):
        ctx.unavailable("D10.path-proof-unavailable", ctx.location, "exact-path-membership")
        return None
