# ProtoSpinor Odd-Weight Lift Selector or SpinC Dichotomy v1

Date: 2026-07-15

## The gravity and proto-spinor gates meet at one Z2 problem

The two `Z64` roots of the TT character are `chi_1` and `chi_33`. Their ratio
is `chi_32`. In a weight-`m` representation the ratio becomes

```text
chi_(32m) = 1       for m even,
chi_(32m) = chi_32  for m odd.
```

This proves a sharp division:

```text
TT/helicity 2: cannot see the root sign,
odd/spinorial weight: can see the root sign.
```

Thus the same-circle QG clause and the proto-spinor global-lift clause are not
independent. They share an order-two lifting problem.

## What the local q79 result supplies

The signed sheet action has local binary preimage `Dic_3`, and its central
`-1` is generated. The extension is non-split: lifted transpositions square to
`-1`. This proves that a central sign is genuinely present in the local
spinorial carrier.

It does not prove that this central `-1` is the same geometric object as the
shared-circle `chi_32`. Equal group order is not a bundle or connection
intertwiner. The q79 packet has zero of five global Spin fields closed, and the
revised proto-spinor paper correctly requires all actual branch-complement
relators to close with sign `+1`.

## Strict Spin route

A strict root selection requires all of the following:

1. the actual q79 branch-complement presentation and lifted relator signs;
2. vanishing of the relevant `w2` and extension through ramification;
3. an explicit map identifying Spin central `-1` with shared-circle `chi_32`;
4. an odd-weight/spinorial source map whose square is the computed TT map.

If these hold, the odd sector can distinguish the two roots without adding a
continuous fitted parameter.

## SpinC route

If strict Spin does not close, a combined SpinC carrier is possible only after
selecting a determinant line `L_det` and proving

```text
c1(L_det) mod 2 = w2
```

together with connection, holonomy, branch, and HYM compatibility. An abstract
order-two sign character is not by itself this proof.

## What the other artifacts contribute

The terminal return paper and the ambient Majorana check both exhibit the
correct order-two representation type. They do not select `chi_1` or `chi_33`,
and they do not identify their sign line with the gravity mismatch. The
Majorana paper also correctly forbids reusing the CP character as the neutral
self-conjugate character.

## Exact current frontier

The next artifact is no longer another TT matrix calculation. It must emit:

```text
common pullback base and lines
+ q79 global relator signs/w2
+ shared-circle differential character
+ central-kernel comparison map
+ odd source or SpinC determinant line.
```

Current status:

```text
EVEN_TT_AMBIGUITY_PROVED_SHARED_Z2_SPIN_SELECTOR_CUTSET_ISOLATED_NO_ROOT_SELECTED
```
