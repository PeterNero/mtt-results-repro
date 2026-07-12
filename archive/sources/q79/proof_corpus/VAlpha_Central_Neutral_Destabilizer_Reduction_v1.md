# VAlpha Central-Neutral Destabilizer Reduction v1

## Statement

Work in the selected reduced base-pullback Kunneth model for

```text
0 -> L -> V_alpha -> Q=L^-1 -> 0,
L=(1,-2,0), Q=(-1,2,0), mu(a,b,c)=a+2b.
```

Assume the rank-one line test class is central-neutral, so `M=(a,b,0)`.  Then
every nonnegative-slope central-neutral base-pullback line class with a possible
map to `V_alpha` is one of exactly six classes, and each is obstructed by the
selected extension boundary map in the reduced Kunneth model.

## Reduction

From the long exact Hom sequence

```text
0 -> Hom(M,L) -> Hom(M,V_alpha) -> Hom(M,Q) -> Ext^1(M,L),
```

we first test the two possible channels.

For `Hom(M,L)` one needs `L-M=(1-a,-2-b,0)` to be effective in the reduced
base-pullback model.  Thus `a<=1` and `b<=-2`, so `mu(M)=a+2b<=-3`.  No such
class can destabilize a slope-zero rank-two extension.

For `Hom(M,Q)` one needs `Q-M=(-1-a,2-b,0)` effective and `mu(M)>=0`.  Thus
`a<=-1`, `b<=2`, and `a+2b>=0`.  These inequalities force `b in {1,2}`, and
therefore the finite list:

```json
[
  [
    -4,
    2,
    0
  ],
  [
    -3,
    2,
    0
  ],
  [
    -2,
    1,
    0
  ],
  [
    -2,
    2,
    0
  ],
  [
    -1,
    1,
    0
  ],
  [
    -1,
    2,
    0
  ]
]
```

The bounded scan recorded in the certificate agrees with this inequality
proof.

## Boundary Table

The connecting map is cup/Yoneda multiplication by the selected extension class
`theta_plus_0_tensor_eta_minus_0 in H^1(2,-4,0)`.

| M | slope | dim Hom(M,Q) | dim Ext^1(M,L) | boundary rank | status |
|---|---:|---:|---:|---:|---|
| `(-4, 2, 0)` | `0` | `3` | `20` | `3` | `EXCLUDED_BY_INJECTIVE_REDUCED_KUNNETH_BOUNDARY` |
| `(-3, 2, 0)` | `1` | `2` | `16` | `2` | `EXCLUDED_BY_INJECTIVE_REDUCED_KUNNETH_BOUNDARY` |
| `(-2, 1, 0)` | `0` | `1` | `9` | `1` | `EXCLUDED_BY_PROVED_REDUCED_KUNNETH_YONEDA_SCALAR` |
| `(-2, 2, 0)` | `2` | `1` | `12` | `1` | `EXCLUDED_BY_INJECTIVE_REDUCED_KUNNETH_BOUNDARY` |
| `(-1, 1, 0)` | `1` | `1` | `6` | `1` | `EXCLUDED_BY_INJECTIVE_REDUCED_KUNNETH_BOUNDARY` |
| `(-1, 2, 0)` | `3` | `1` | `8` | `1` | `EXCLUDED_BY_NON_SPLIT_EXTENSION_BOUNDARY` |

The boundary map has full column rank in every row.  Hence no nonzero
`Hom(M,Q)` section lifts through `V_alpha`, and the `Hom(M,L)` channel is
already negative-slope only.  Therefore all central-neutral base-pullback
line-bundle destabilizers are obstructed in the selected reduced Kunneth model.

## Important Diagnostic

This sweep shows that the old finite branch list was not itself a complete
destabilizer enumeration.  It was a target/topological branch list.  The Hom
destabilizer cone adds four central-neutral nonnegative-slope candidates:

```json
[
  [
    -4,
    2,
    0
  ],
  [
    -3,
    2,
    0
  ],
  [
    -2,
    2,
    0
  ],
  [
    -1,
    1,
    0
  ]
]
```

Those four are not a failure of the route; they are precisely the rows this
packet now kills by injective reduced Kunneth boundary maps.

## What Remains Open

This is still not the full V_alpha stability theorem.  The remaining global
step is to prove that every destabilizing rank-one/torsion-free subsheaf has a
central-neutral base-pullback reflexive hull covered by this calculation, or to
replace that reduction with raw selected good-cover Appell-Humbert/Cech
multiplication and a direct HYM/Strominger source theorem.

No HYM existence, raw good-cover multiplication, primitive C1 matrices, or full
SM closure is claimed here.
