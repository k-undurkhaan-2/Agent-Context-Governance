# S6 Fixture Contract v1

## Status and boundary

This document describes the forward-only Manifest v3 Fixture Contract: the
historical three-case Pilot plus the distinct 62-case Schema Ref-Identifier
Oracle Batch 01. The combined contract is a candidate for independent review
only. It does not grant authority, establish production proof, accept S6, close
a coverage obligation, activate S7, or authorize model work. Every operand,
proof response, path, identity, digest, and timestamp is conspicuously
synthetic.

Manifest v3 preserves all 2,166 historical logical case rows and their
Manifest-v2 descriptor bindings. The Pilot and Batch 01 add authenticated
operand and oracle sidecars without replacing the S5 descriptors. Historical
Manifest-v2 identity remains available through Git history; Manifest v3
intentionally has no self-digest.

The pilot contains exactly these cases:

1. `schema.branch-policy.negative.01-empty-prefix`
2. `phase1-static.branch-policy.negative.16-no-allow-match`
3. `static.branch-policy.positive.01-exact-allow-no-deny`

The three published Pilot bindings remain unchanged. Batch 01 is represented
separately by `fixtureContract.schemaOracleBatches` and contains exactly:

- `schema.common.gitrefidentifier.negative.ref-0` through `ref-19`;
- `schema.common.branchref.negative.ref-0` through `ref-19`, plus `.tag`; and
- `schema.common.branchprefix.negative.ref-0` through `ref-19`, plus
  `.heads-only`.

All cases outside the Pilot and Batch 01 retain their prior operand, oracle,
execution, disposition, and ownership state. Batch 01 preserves every source
value and historical descriptor binding.

## Contract and authentication

`fixture-contract-v1` uses strict JSON sidecar envelopes defined by
`tests/schema/fixtures/v1alpha1/s6/fixture-contract-v1.schema.json`. Manifest
v3 binds, for each contract case, the unchanged descriptor path and JSON
Pointer, the operand path and JSON Pointer, the selected validator entry point,
the diagnostic identity version, the expected validation status, and the
oracle path and JSON Pointer when the case is negative. Every referenced file
is bound by canonical UTF-8 byte length and SHA-256. Historical Pilot bindings
and new Batch 01 membership remain distinct.

Canonical sidecar bytes are UTF-8 without a BOM, use LF line endings, and end
with one LF byte. Authentication detects mutation; it does not establish
trusted issuance, event truth, production evidence, or operational authority.

The final candidate Manifest-v3 canonical identity is external to the
Manifest and therefore does not create a self-digest:

| Artifact | Canonical bytes | SHA-256 | Git Blob |
| --- | ---: | --- | --- |
| `tests/schema/fixtures/v1alpha1/manifest.json` | 1,908,779 | `bd3c5c4369a8c9a4161183c1e008cc3bc9875f700724ac745a57d548dcc27cde` | `929cc6ee663661ffe4afcce728e12e9b166bf19a` |

## Frozen operand identities

Each operand definition below was completed and frozen before its diagnostic
oracle was drafted. The identities were measured from the proposed canonical
bytes; no validator diagnostic output was used to choose or correct an expected
set.

| Sidecar | Canonical bytes | SHA-256 | Git Blob |
| --- | ---: | --- | --- |
| `tests/schema/fixtures/v1alpha1/s6/fixture-contract-v1.schema.json` | 14,450 | `887b79afd12950bad428fda4b2d3402ee5f3e7e82a75991f25cbabb53a14ed71` | `a12d4b9fb1ab829b5a2e10d95d516f03ee3dff06` |
| `tests/schema/fixtures/v1alpha1/s6/operands/branch-policy-pilot.json` | 31,786 | `8375e157311c2aa04be3297efaf6cf85d998a06fcc0b85ce7fcc30d31cdec2dc` | `732e147330244873261611ccdde8678db58352a7` |
| `tests/schema/fixtures/v1alpha1/s6/operands/schema-common-ref-batch01.json` | 25,393 | `f37015ee29a6933278b898a0953c0e4f97688f7fa0e6e1b7d68867b69496b038` | `a196f812ddb1d1bed1611cf7426a01e7c7925b2f` |

The Schema operand freezes the empty string and the exact
`common.schema.json#/$defs/branchPrefix` root. Each static operand freezes a
complete `TaskContract`, `GovernanceBundle`, `HostOverlay`, checkpoint-bound
same-host inventory context, exact one-member complete snapshot, and complete
nine-dimension materialized baseline. Input-provenance responses are explicit
and case-bound. Canonical-comparison, digest, and completed-validation response
sets are explicitly empty; the runner must fail closed on an undeclared proof
request. No generic `SyntheticPorts` success default may complete a pilot
operand.

The two static subjects differ only where their case semantics require it:
the negative role allows `refs/heads/other` while its expected baseline names
`refs/heads/release`; the positive role exactly allows
`refs/heads/release`. Their remaining inputs are complete synthetic controls,
not inferred defaults.

The Batch 01 operand freezes all 62 authenticated descriptive values against
exactly one of `common.schema.json#/$defs/gitRefIdentifier`, `#/$defs/branchRef`,
or `#/$defs/branchPrefix`. Its case map is strictly ASCII-sorted and contains no
case outside the authorized membership.

## Diagnostic identity contracts

`schema-diagnostic-v1` is the exact tuple:

```text
schemaResourceId
instancePointer
schemaPointer
keyword
```

`static-diagnostic-v1` is the exact tuple of the existing public static
diagnostic fields:

```text
code
subjectId
instancePointer
predicateFamily
schemaId
schemaPointer
keyword
```

Expected negative sets must be explicit, nonempty, unique, and canonically
ordered. The runner compares complete typed sets and reports both missing and
unexpected identities. `expectedFailureIdentity` remains historical S5 design
metadata and is never accepted as an exact oracle.

Schema diagnostic order is `(instancePointer, schemaResourceId,
schemaPointer, keyword)`. Static diagnostic order is `(instancePointer,
schemaId-or-empty, schemaPointer-or-empty, keyword, code,
subjectId-or-empty, predicateFamily)`.

## Independent oracle basis

The negative oracles are authored only from the frozen operands, the normative
branch-policy requirements in `docs/schema-contract-v1alpha1.md`, the approved
public Schema resources, and the public static diagnostic construction. Batch
01 additionally uses only the exact `gitRefIdentifier`, `branchRef`, and
`branchPrefix` definitions in `common.schema.json`. Actual validator
diagnostics, prior observed output, and existing regression results are
excluded as oracle-authoring inputs.

The independently drafted oracle sidecars have these canonical identities:

| Sidecar | Canonical bytes | SHA-256 | Git Blob |
| --- | ---: | --- | --- |
| `tests/schema/fixtures/v1alpha1/s6/oracles/schema-branch-policy-pilot.json` | 1,059 | `a3bbea2f6834ca0511e370b51e71c32c0e6854cecf24d2869cea7698c4c571ae` | `4443327b766aa177585f7c0618cd0ac8051efcdc` |
| `tests/schema/fixtures/v1alpha1/s6/oracles/schema-common-ref-batch01.json` | 26,997 | `f603ee91c4859e58539f7b5bbcf133a0dabb18fbcdd20231fe65d1355ee7effc` | `19a227b4122ba4021c32348904fbecf2ddd875b2` |
| `tests/schema/fixtures/v1alpha1/s6/oracles/static-branch-policy-pilot.json` | 727 | `3e5ebd6ddc07e1695cacb2d8610621c7173b4ce37023ed81af55570a3240b0a6` | `ec802cd113289b1d5bc15150b3520a5858ad8bbc` |

For the empty prefix, the frozen Schema root composes `branchRef` and
`gitRefIdentifier`. The empty string independently violates the branch-ref
pattern and the Git-ref minimum-length and pattern constraints, yielding three
typed identities. For the no-allow-match static case, the complete frozen
context satisfies the upstream, snapshot, baseline, and proof prerequisites;
the normative `allowMatch == true AND denyMatch == false` predicate alone is
false. The public diagnostic constructor therefore yields the one typed
`S4.BRANCH.STATIC` identity at `/spec/expectedBaseline/ref`.

Before the Batch 01 Oracle was written, a task-local derivation ledger outside
the repository recorded all 62 case-keyed derivations from the frozen operand.
Its 75 identities comprise 53 one-diagnostic cases, five two-diagnostic cases,
and four three-diagnostic cases. `ref-0` and `ref-1` carry applicable
minimum-length failures; `ref-19` carries the applicable maximum-length
failure; branch-root cases also carry the inherited branch pattern when it
fails; and every violated Git-ref pattern remains separately represented.

## Status meanings and remaining blockers

`PASS`, `INVALID`, and `PROOF_REQUIRED` remain distinct. A positive Pilot case
must return `PASS`; every negative Pilot or Batch 01 case must return `INVALID`
and an exact typed oracle match. `PROOF_REQUIRED` is neither acceptance nor an
invalid-data result.

Neither the Pilot nor Batch 01 weakens aggregate S6 gates. The remaining 426
missing executable operands and 1,471 missing exact negative oracles remain
blocking. All 42 open Phase-1 coverage obligations remain open and blocking,
row-19 responsibility remains unchanged, and all eight future-model
obligations remain outside S6.
