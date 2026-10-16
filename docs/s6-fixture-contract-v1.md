# S6 Fixture Contract v1

## Status and boundary

This document describes the forward-only Manifest v3 Fixture Contract: the
historical three-case Pilot, the distinct 62-case Schema Ref-Identifier Oracle
Batch 01, the distinct 104-case Schema Text Oracle Batch 02, and the distinct
73-case Schema Identifier Lexical Oracle Batch 03, and the distinct 98-case
Schema Scalar Negative Oracle Batch 04. The combined
contract is a candidate for independent review only. It does not grant
authority, establish production proof, accept S6, close a coverage obligation,
activate S7, or authorize model work. Every operand, proof response, path,
identity, digest, and timestamp is conspicuously synthetic.

Manifest v3 preserves all 2,166 historical logical case rows and their
Manifest-v2 descriptor bindings. The Pilot and all four Oracle batches add
authenticated operand and oracle sidecars without replacing the S5
descriptors. Historical Manifest-v2 identity remains available through Git
history; Manifest v3 intentionally has no self-digest.

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

Batch 02 is represented separately and contains exactly:

- `schema.common.displaytext.negative.control-0` through `control-31`;
- `schema.common.displaytext.negative.control-127` through `control-159`;
- `schema.common.displaytext.negative.empty`, `.too-long`, and `.wrong-type`;
- `schema.common.sanitizedsummary.negative.control-0` through `control-31`;
- `schema.common.sanitizedsummary.negative.control-127`; and
- `schema.common.sanitizedsummary.negative.empty`, `.too-long`, and
  `.wrong-type`.

The exact ASCII-sorted Batch 02 membership is frozen as one case ID per line,
with LF endings and a final LF: 4,964 bytes and SHA-256
`3e23bb284e58ccc5bbbc7d0d3646aca36065fe4cfda90579732c3caf030fe708`.
The explicit list is duplicated fail-closed in the runner, operand, Oracle, and
104 Manifest bindings.

Batch 03 contains exactly the negative cases selected by these authenticated
source profiles:

- `remoteRepositoryName` — 16 cases;
- `remoteNamespaceComponent` — 15 cases;
- `logicalIdentifier` — 12 cases;
- `checkIdentifier` — 10 cases;
- `profileIdentifier` — 10 cases; and
- `reasonCode` — 10 cases.

The exact ASCII-sorted Batch 03 membership is frozen as one case ID per line,
with LF endings and a final LF: 3,966 bytes and SHA-256
`68f1bcc6d39e769249b065d20ab0ee45c3e0418e45b95aa4cda1df8210444638`.
The explicit list is duplicated fail-closed in the runner, operand, Oracle, and
73 Manifest bindings.

Batch 04 contains exactly the negative cases selected by these authenticated
source profiles:

- integer range profiles: `indexStage`, `redactionCount`, `remotePort`,
  `routingPriority`, and `sequence` — six cases each, 30 total; and
- string enum profiles: `capability` — 15 cases, `kind` — nine cases,
  `executionCheckOutcome` — eight cases, `checkOutcome`, `executionOutcome`,
  and `lifecycleOutcome` — seven cases each, `receiptDeliveryOutcome` and
  `releaseOutcome` — six cases each, and `gitMode` — three cases, 68 total.

The exact ASCII-sorted Batch 04 membership is frozen as one case ID per line,
with LF endings and a final LF: 4,959 bytes and SHA-256
`72fe7b7b2b80fdae80a75afe77377feb332f4b2badab1f8b0331c6c9e089ffe1`.
The explicit list is duplicated fail-closed in the runner, operand, Oracle, and
98 Manifest bindings. Batch 04 is disjoint from the Pilot and Batches 01
through 03. All cases outside the Pilot and Batches 01 through 04 retain their
prior operand, oracle, execution, disposition, and ownership state. All four
batches preserve every source value and historical descriptor binding.

## Contract and authentication

`fixture-contract-v1` uses strict JSON sidecar envelopes defined by
`tests/schema/fixtures/v1alpha1/s6/fixture-contract-v1.schema.json`. Manifest
v3 binds, for each contract case, the unchanged descriptor path and JSON
Pointer, the operand path and JSON Pointer, the selected validator entry point,
the diagnostic identity version, the expected validation status, and the
oracle path and JSON Pointer when the case is negative. Every referenced file
is bound by canonical UTF-8 byte length and SHA-256. Historical Pilot bindings
and all four Oracle-batch memberships remain distinct.

Canonical sidecar bytes are UTF-8 without a BOM, use LF line endings, and end
with one LF byte. Authentication detects mutation; it does not establish
trusted issuance, event truth, production evidence, or operational authority.

The final candidate Manifest-v3 canonical identity is external to the
Manifest and therefore does not create a self-digest:

| Artifact | Canonical bytes | SHA-256 | Git Blob |
| --- | ---: | --- | --- |
| `tests/schema/fixtures/v1alpha1/manifest.json` | 2,290,369 | `ef7c753aa8629696584cddde5f66521dd1e9b974b777679c7c828f374be39e24` | `f07e260ffe96dab65ed1f4d65a1fe3d6c960fa1f` |

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
| `tests/schema/fixtures/v1alpha1/s6/operands/schema-common-text-batch02.json` | 39,337 | `7dee52bb82d5187d6e7a933973c129d3103982828d295ba09d29de26ebe4ff89` | `5236bb13bb085d791201632f4c49d860c16dc946` |
| `tests/schema/fixtures/v1alpha1/s6/operands/schema-common-identifiers-batch03.json` | 27,747 | `057699046579a57a5da528eab3b0cf0cb30f4a0cfa310e9d12d2f77bf6ddb48b` | `1abd86416e434d078b16e4369e3b8aebc3223602` |
| `tests/schema/fixtures/v1alpha1/s6/operands/schema-common-scalars-batch04.json` | 35,046 | `7d4f2587f6228d1d9994d3d50f3a372229e91327414c1ef1054af1eb91c36953` | `74de4d790ae1ebef11fbd5b239f3f88b17a5bacb` |

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

The Batch 02 operand freezes 68 authenticated `displayText` values and 36
authenticated `sanitizedSummary` values against their exact
`common.schema.json` `$defs` roots. It was frozen before the Batch 02 Oracle was
authored. Its case map is strictly ASCII-sorted, matches the authenticated
source values exactly, and contains no case outside the authorized membership.
The selection source remains 179,081 bytes, SHA-256
`62d6ad159d10ceb89e212852aa57af5af2b430f7637be25aa601bdca7609c749`,
Git blob `94b503faf31f6115e354bdac5c77116af2f727c1`. The normative
`common.schema.json` remains 19,205 bytes, SHA-256
`28bebf46eaf4dbeaa5314b713801b6ddf3039589de56a9eeee321dc1387f577d`,
Git blob `b1469d6c09e37284426ee97c5b1ab870dd6911b7`.

The Batch 03 operand freezes 73 authenticated descriptive values against
exactly one of the `remoteRepositoryName`, `remoteNamespaceComponent`,
`logicalIdentifier`, `checkIdentifier`, `profileIdentifier`, or `reasonCode`
roots in `common.schema.json`. It was frozen before the Batch 03 derivation
ledger and Oracle were authored. Its case map is strictly ASCII-sorted,
matches the authenticated source values exactly, and contains no case outside
the authorized membership. The same authenticated source and normative Schema
identities shown above remain unchanged.

The Batch 04 operand freezes 98 authenticated descriptive values against
exactly one of the 14 integer-range or string-enum roots named above in
`common.schema.json`. It was frozen before the Batch 04 derivation ledger and
Oracle were authored. Its case map is strictly ASCII-sorted, matches every
authenticated source value exactly, and contains no case outside the
authorized membership. The same authenticated source and normative Schema
identities shown above remain unchanged.

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
`branchPrefix` definitions in `common.schema.json`. Batch 02 uses only the exact
`displayText` and `sanitizedSummary` definitions. Batch 03 uses only the exact
six identifier definitions named above. Batch 04 uses only the exact `type`,
`minimum`, `maximum`, and `enum` assertions declared by its 14 selected
`common.schema.json` definitions. Actual validator diagnostics, prior observed
output, and existing regression results are excluded as oracle-authoring
inputs.

The independently drafted oracle sidecars have these canonical identities:

| Sidecar | Canonical bytes | SHA-256 | Git Blob |
| --- | ---: | --- | --- |
| `tests/schema/fixtures/v1alpha1/s6/oracles/schema-branch-policy-pilot.json` | 1,059 | `a3bbea2f6834ca0511e370b51e71c32c0e6854cecf24d2869cea7698c4c571ae` | `4443327b766aa177585f7c0618cd0ac8051efcdc` |
| `tests/schema/fixtures/v1alpha1/s6/oracles/schema-common-ref-batch01.json` | 26,997 | `f603ee91c4859e58539f7b5bbcf133a0dabb18fbcdd20231fe65d1355ee7effc` | `19a227b4122ba4021c32348904fbecf2ddd875b2` |
| `tests/schema/fixtures/v1alpha1/s6/oracles/schema-common-text-batch02.json` | 41,354 | `e16613e4d3dcfd712fc6902a37a064799fa61f045974a6d6e41611bec7b74b17` | `0d5d3fe7103a2a7b9210d97ac90bc8183ec2c6bd` |
| `tests/schema/fixtures/v1alpha1/s6/oracles/schema-common-identifiers-batch03.json` | 32,210 | `452b14fc97e2730ac815efa306c9804fe57fa3f8bf4815a32db507b1e81ce050` | `7bd9d3e5959f51c3a88d2e46de9006f8a0e7a25e` |
| `tests/schema/fixtures/v1alpha1/s6/oracles/schema-common-scalars-batch04.json` | 41,193 | `e35cee2f297fec67f035220214ea67fd16065843453d7bc2b055cb293ec0063f` | `494f8b239090ed82de06fcd794fcf7d55b0b648a` |
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

Before the Batch 02 Oracle was written, a task-local derivation ledger outside
the repository recorded all 104 case-keyed derivations from the frozen operand.
The ledger is 96,675 canonical bytes with SHA-256
`d9dee43925a04c4bed66321571ff463c72f524d2b52f20acb352054886065b66`.
Its 106 identities comprise 102 one-diagnostic cases and two two-diagnostic
cases. Each forbidden C0 value, DEL, and each Batch 02 `displayText` C1 value
violates `pattern`; `sanitizedSummary` has no unsupported C1 restriction. Each
empty string violates both `minLength` and `pattern`; each 1,025-character
string violates `maxLength`; and each array operand violates only `type`
because string-only assertions do not apply. Description-only NFC, content
classification, and actual-sanitization requirements add no Schema diagnostic
identity.

After the Oracle was frozen, 104 bounded Validator executions returned
`INVALID` and matched all 106 identities exactly. Targeted contract tests also
exercise missing- and unexpected-identity rejection, sidecar and Manifest
authentication, historical Pilot and Batch 01 preservation, offline registry
and cross-resource attribution, and the unchanged global blocker accounting.

Before the Batch 03 Oracle was written, a task-local derivation ledger outside
the repository recorded all 73 case-keyed derivations from the frozen operand
and exact Schema assertions. The ledger is 55,711 canonical bytes with SHA-256
`2c052c797abf1f4a0c5202c36a78134baedc10ca78e105c516e721a91526cfcb`.
Its 82 identities comprise 64 one-diagnostic cases and nine two-diagnostic
cases: 69 `pattern`, six `minLength`, six `maxLength`, and one `type` identity.
String-only assertions do not apply to the wrong-type operand. The applicable
minimum- or maximum-length failures remain distinct from pattern failures, and
the three 161-character prefixed identifiers violate only `maxLength` because
their segments still satisfy the declared pattern.

Only after the Batch 03 Oracle was frozen and authenticated, 73 bounded
Validator executions returned `INVALID` and matched all 82 identities exactly.
Targeted contract tests exercise missing- and unexpected-identity rejection,
sidecar and Manifest authentication, historical Pilot and Batches 01 and 02
preservation, offline registry and cross-resource attribution, explicit
membership, and unchanged fail-closed blocker accounting.

Before the Batch 04 Oracle was written, a task-local derivation ledger outside
the repository recorded all 98 case-keyed derivations from the frozen operand,
the exact Schema assertions, and JSON Schema Draft 2020-12 assertion
applicability. The ledger is 105,353 canonical bytes with SHA-256
`88ee0f8f8bd5e287e0399e64a84b5152c92061566eaeec0881bf003b62569615`.
Its 110 identities comprise 86 one-diagnostic cases and 12 two-diagnostic
cases: 68 `enum`, 30 `type`, six `minimum`, and six `maximum` identities.
Boolean operands are not integers or numbers. Non-integral numbers violate
`type` while still participating independently in numeric bounds: the
`indexStage` fraction also violates `maximum`, and the `remotePort` fraction
also violates `minimum`. Null enum operands violate both `enum` and `type`, the
numeric `gitMode` operand is not a string mode and violates both assertions,
and unknown or differently capitalized strings violate only `enum`.

Only after the Batch 04 Oracle was frozen and authenticated, 98 bounded
Validator executions returned `INVALID` and matched all 110 identities
exactly. Targeted contract tests exercise integer, fractional-boundary, and
enum applicability; missing- and unexpected-identity rejection; sidecar and
Manifest authentication; historical Pilot and Batches 01 through 03
preservation; offline registry and attribution; exact membership; and
unchanged fail-closed blocker accounting.

## Status meanings and remaining blockers

`PASS`, `INVALID`, and `PROOF_REQUIRED` remain distinct. A positive Pilot case
must return `PASS`; every negative Pilot or Batch 01, 02, 03, or 04 case must return
`INVALID` and an exact typed oracle match. `PROOF_REQUIRED` is neither
acceptance nor an invalid-data result.

Neither the Pilot nor any Oracle batch weakens aggregate S6 gates. Batch 04
adds two physical assets and 98 exact bindings without changing any historical
logical case: the corpus now has 150 physical assets, 152 total corpus paths,
12 Fixture Contract assets, four Schema Oracle batches, and 337 Oracle-batch
bindings (340 total Fixture Contract case bindings including the Pilot). The
remaining 426 missing executable operands and 1,196 missing exact
negative oracles remain blocking. All 42 open Phase-1 coverage obligations
remain open and blocking, row-19 responsibility remains unchanged, and all
eight future-model obligations remain outside S6. S6 acceptance remains
`BLOCKED`.
