# MTT Selected q79 Alignment Handles and Global Surface Relation v1

## Result

A129 extends A128's 90 promoted local Picard-Lefschetz actions by the two
selected base-torus handle actions. Both handle paths, continuous root tubes,
and projected braid words are certified. Their exact integral symplectic
actions satisfy the ordered punctured-torus surface relation with the 90
selected local factors.

This closes the global integral `H1` Gauss-Manin representation for the
selected-alignment genus-two fibration. It emits no period value and makes no
integral-branch or full gerbe claim.

## Handle carriers

On the normalized square torus with base point `(1+i)/4`, use the universal
cover paths from the base point to its translates by `1` and `i`. Direct
interval distance tests against all lattice lifts give positive minimum
clearances:

```text
90 selected critical balls       1.6786565077617785e-6
3 selected L1 chart-zero balls   0.24838289874007513
elliptic poles                   0.24999999999999001
```

Thus both paths remain in the same selected line chart and regular-fiber
locus.

## Handle promotion

The `A` trajectory has 539 segments. Its minimum Rouché margin is
`7.1359253306626033e-5`, its minimum pairwise tube separation is
`0.0030265730553996782`, and 11 projected crossings are interval-certified.

The `B` trajectory has 1,832 segments. Its minimum Rouché margin is
`2.7873169769727782e-8`, its minimum pairwise tube separation is
`5.7044606804632174e-5`, and 16 projected crossings are interval-certified.

Exact braid replay gives

```text
A = [[ 1,-1, 0, 0],
     [ 0, 1, 0, 0],
     [ 0, 0, 1, 0],
     [ 0, 0, 0, 1]]

B = [[-1,-1, 0, 1],
     [ 1,-1, 1, 0],
     [ 0, 1,-1,-1],
     [ 1, 0, 1,-1]].
```

Both matrices have determinant one and preserve the same integral
intersection form as all 90 A128 factors.

## Global relation

Order the meridians by the A127 radial fan, counterclockwise from the positive
`A` edge. With left actions and the convention

```text
M(gamma then delta)=M(delta) M(gamma),
```

the punctured-torus relation is

```text
A B A^-1 B^-1 = m1 m2 ... m90.
```

The independently computed exact integer matrices obey

```text
M90 ... M2 M1 = B^-1 A^-1 B A

                  [[ 0, 1,-1, 0],
                   [-1, 3,-1, 0],
                   [ 0, 0, 1, 0],
                   [-1, 2,-1, 1]].
```

No conjugation, matrix adjustment, or numerical tolerance enters this
equality. Every local factor is a positive rank-one Picard-Lefschetz
transvection, and their primitive vanishing cycles span rank four.

## Consequence and next step

The selected endpoint now has the same level of globally certified monodromy
input that the identity carrier had at A116. The next calculation is algebraic:

1. form the integral boundary map from the 90 selected vanishing cycles;
2. form the two-handle Fox boundary from the selected `A` and `B` actions;
3. compute their Smith forms and the rank-92 surface-cycle presentation;
4. then execute selected thimble and handle periods to orient and couple the
   final integral basis.

Next artifact:
`MTT_Selected_q79SelectedAlignmentIntegralSurfaceCyclePresentation_v1`.
