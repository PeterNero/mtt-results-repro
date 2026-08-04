# VAlpha Extension Stability Filter Attempt v1

## Claim Being Tested

Use the selected non-split extension

```text
0 -> L -> V_alpha -> L^-1 -> 0
L = [1, -2, 0]
```

as a stability filter rather than searching blindly over matrices.  The selected
wall is `p = [1, 2, 1]`, so `mu(L) = -3`
and `mu(L^-1) = 3`.

## What Closes

The displayed subline is not destabilizing in the selected chamber because its
slope is strictly negative.  The obvious positive-slope quotient class
`L^-1 = [-1, 2, 0]` is also excluded as an
actual subline: EXCLUDED_BY_NON_SPLIT_EXTENSION.  The reason is the standard extension
criterion: a section of the quotient map would split the extension, and the
terminal Cech packet supplies a closed, non-exact selected Ext vector
`[1, 0, 0, 0, 0, 0, 0, 0]`.

This is genuine progress.  It removes the largest fake obstruction without
using benchmark flavor data, observed masses, CKM values, or proxy fitting.

## What Remains

Within the currently available finite branch-candidate set, the only unresolved
candidate classes are the zero-slope ones:

```json
[
  {
    "M": [
      -2,
      1,
      0
    ],
    "label": "branch_candidate",
    "slope_at_selected_p": 0,
    "destabilizing_risk": true,
    "status": "ZERO_SLOPE_NEEDS_HOM_AND_YONEDA_EXCLUSION",
    "detail": {
      "reason": "Stable, not merely semistable, requires excluding zero-slope rank-one subobjects.  This needs H^0(L^{-1} tensor M^{-1}) and the Yoneda pullback of the selected extension through every quotient projection.",
      "closed_by_current_data": false,
      "needed_data": [
        "basis of Hom(M,L^{-1}) = H^0(X,L^{-1} tensor M^{-1})",
        "pullback obstruction matrix Hom(M,L^{-1}) -> Ext^1(M,L)",
        "proof no Hom vector has zero pulled-back selected obstruction"
      ]
    }
  },
  {
    "M": [
      2,
      -1,
      0
    ],
    "label": "branch_candidate",
    "slope_at_selected_p": 0,
    "destabilizing_risk": true,
    "status": "ZERO_SLOPE_NEEDS_HOM_AND_YONEDA_EXCLUSION",
    "detail": {
      "reason": "Stable, not merely semistable, requires excluding zero-slope rank-one subobjects.  This needs H^0(L^{-1} tensor M^{-1}) and the Yoneda pullback of the selected extension through every quotient projection.",
      "closed_by_current_data": false,
      "needed_data": [
        "basis of Hom(M,L^{-1}) = H^0(X,L^{-1} tensor M^{-1})",
        "pullback obstruction matrix Hom(M,L^{-1}) -> Ext^1(M,L)",
        "proof no Hom vector has zero pulled-back selected obstruction"
      ]
    }
  }
]
```

They cannot be ignored: stable means every proper rank-one subsheaf has
strictly smaller slope than `V_alpha`, so zero-slope injections would still
block stability.  The next missing object is the explicit Hom/Yoneda obstruction
data:

```text
Hom(M,L^-1) = H^0(X,L^-1 tensor M^-1)
Hom(M,L^-1) --pullback selected extension--> Ext^1(M,L).
```

For each residual zero-slope class, every possible quotient projection must
pull back the selected extension to a nonzero obstruction.  If the Hom space is
zero, that candidate is excluded even faster.

## Search-Space Consequence

The wall is not a giant iterative search anymore.  Current data reduce the
rank-two stability check to:

1. a full destabilizer enumeration theorem, or a justified finite reduction to
   the branch candidates recorded here;
2. the Hom/Yoneda matrices for the residual zero-slope classes;
3. a selected HYM/Strominger existence result after stability is proven.

External HYM/Kobayashi-Hitchin-style existence theorems can be used only after
the holomorphic stability hypotheses are proven.  They are excellent filters,
but they do not by themselves select the missing MTT source.

## External Filter References

The external role is deliberately narrow:

- Donaldson-Uhlenbeck-Yau theorem overview in HYM context: https://pmc.ncbi.nlm.nih.gov/articles/PMC8741718/ (documents the stable holomorphic bundle <-> HYM connection bridge in a modern HYM setting)
- Gauduchon/Hermitian-manifold stability correspondence context: https://www.sciencedirect.com/science/article/abs/pii/S0007449723000623 (records the Li-Yau/Gauduchon-type generalization context for non-Kahler Hermitian manifolds)
- Numerical HYM in heterotic vector-bundle stability: https://arxiv.org/abs/1004.4399 (motivates using HYM/stability as a computational filter rather than as a fitted SM input)

## Guardrail

This document does not prove full stability, does not prove HYM existence, and
does not prove full SM closure.  It proves that the selected nonzero Ext packet
excludes the quotient `L^-1` destabilizer and makes the remaining finite
obstruction data completely explicit.
