# MTT Selected Actual Z64 Tower Kinetic Functional Typing or Resolvent Routing Promotion v1

## Actual selected spectrum

Enumerating all sixteen ordered compositions of `32=2^5` gives

```text
spec(L64) = 15(x1), 24(x4), 33(x3), 69(x3), 78(x2), 258(x2), 1023(x1).
```

Thus the selected eigenvalue is `15`, the next is `24`, and the exact gap is `9`. At
`tau_int=log(448)/15`, the ground heat weight is exactly `1/448`.

## A70 typing result

The A70 denominator `2*15+16+1/15` is not currently a trace of `L64`: the spectrum has one
copy of `15` and no `16`; `16` is a retarded carrier label, while `1/15` is a saturated proper
time/resolvent scalar. The exact branch also has zero Schur leakage. A70 remains a striking
target-ranked numerical candidate, but strict source promotion is rejected.

## What is proved for 31/42

For any isometry `V:C^2->C^42` and `A_ret=diag(15,16)`, normalized trace gives

```text
tau_42(V A_ret V^*) = Tr(A_ret)/42 = 31/42.
```

This identity is basis-independent. What remains open is physical selection of `A_ret`, `V`, and
the normalized trace as the gauge kinetic functional.

## Typed search

Eight predeclared heat/resolvent/determinant-scale functions of the actual `L64` spectrum were
executed. Exact matches to the profile-inferred residual: `0`. The next source must be a typed
same-action functional `F(L64,Delta79)` rather than arithmetic on retarded labels.

Next artifact: `MTT_Selected_GaugeKineticFunctionalOfL64AndQ79Chord_or_StrictResidualValueEmission_v1`.
