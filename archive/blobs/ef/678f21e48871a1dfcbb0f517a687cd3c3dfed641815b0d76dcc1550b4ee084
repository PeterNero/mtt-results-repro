# MTT Selected q79 Genus-Two Local Monodromy Promotion v1

Status: `MTT_U6_Q79_ALL_90_LOCAL_AND_TWO_HANDLE_MONODROMIES_PROMOTED_GLOBAL_RELATION_OPEN`

## What A115 closes

A115 promotes all 90 local Picard-Lefschetz matrices that A113 correctly kept
at candidate status. It reconstructs every six-root trajectory over the exact
A113 based meridian. A certified two-chart atlas avoids false root motion at a
branch-coordinate infinity:

```text
s_0=1/t                         on 88 paths,
s_minus1=1/(t+1)               on a34 and a41.
```

The transition from A114's frozen chart `s_old=1/(t-(2+3i))` to each chart has
disjoint rational-image tubes, interval-certified braid crossings and an exact
integral symplectic matrix `P_target`. Every local action is returned to the
common marking by

```text
M_old = P_target^(-1) M_target P_target.
```

This transport reproduces the 90 A113 matrices exactly. The optimized execution
stores `300518` root samples rather than
the old 733,053, while preserving every matrix.

Arb fourth-order elliptic-flow Taylor enclosures and Rouche tests then certify
six pairwise-disjoint continuous root tubes over all
`300428` local path segments. The final 80-digit
projection certificate resolves all
`2392` piecewise-linear
crossings, including `77`
segments with multiple ordered events. The global minimum crossing height and
Rouche relative margin are positive:

```text
crossing height >= 0.022428869860599086,
Rouche relative margin >= 5.3081842978946372e-07.
```

Convex disjoint tubes identify each true braid with its recorded PL braid.
Classical Birman-Hilden lifting sends adjacent half-twists to chain Dehn twists.
Exact replay therefore promotes 90/90 integral `Sp(4,Z)` rank-one unipotent
actions. Together with A114, the promoted inventory is now 90 local plus two
torus-handle actions, and the local vanishing cycles span all four homology
directions.

## What remains exact and open

The A113 based meridians were chosen independently. Their root-id order is not
an ordered distinguished cut system and may not be inserted into the punctured-
torus relation by fiat. A116 must construct that cut system, compute the
homotopy/conjugation words from the promoted loops, freeze the left-action
convention, and check the genus-one relation

```text
[A,B] gamma_1 ... gamma_90 = 1
```

in both the branch braid group and `Sp(4,Z)`. Until then the global rank-four
Gauss-Manin local system, the `8x92` period execution, beta vector, integral
branch and gerbe zero/no-go remain open. A115 removes zero strict MTT source
moduli and does not select the trial q79 carrier.

## Reproduction

```powershell
python scripts/certify_q79genus2branchcharttransition.py --target zero
python scripts/certify_q79genus2branchcharttransition.py --target minus-one
python scripts/run_q79genus2localtrajectorybatch.py --jobs 4
python scripts/run_q79genus2localtubebatch.py --jobs 8 --chunk-size 4000
python scripts/certify_q79genus2local_pl_braids.py
python proof_corpus/selected_q79genus2localmonodromypromotion_audit.py
```

The expensive tube run is frozen by hashes in the active verifier. Set the
explicit recomputation flag documented by the audit to repeat it from scratch.
