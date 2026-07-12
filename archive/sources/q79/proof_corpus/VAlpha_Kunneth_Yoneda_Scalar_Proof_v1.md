# VAlpha Kunneth Yoneda Scalar Proof v1

## The Matrix

The remaining finite branch scalar is the cup/Yoneda multiplication:

```text
H^0(1,1,0) x H^1(2,-4,0) -> H^1(3,-3,0).
```

In the reduced base-pullback Kunneth model it factors as:

```text
H^0_E1(O(1)) x H^0_E1(O(2)) -> H^0_E1(O(3))
H^0_E2(O(1)) x H^1_E2(O(-4)) -> H^1_E2(O(-3)).
```

The second map is the Serre-dual transpose of the ordinary multiplication
`H^0_E2(O(3)) -> H^0_E2(O(4))`.  Therefore the full finite matrix is the
Kronecker product:

```json
[
  [
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0
  ],
  [
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0
  ],
  [
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0
  ],
  [
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0
  ],
  [
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    0
  ],
  [
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0
  ],
  [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0
  ],
  [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0
  ],
  [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0
  ]
]
```

It has rank `6` and sends the selected Ext vector

```json
[
  1,
  0,
  0,
  0,
  0,
  0,
  0,
  0
]
```

to

```json
[
  1,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0
]
```

The target vector is nonzero.  Thus the remaining finite branch-candidate
injection `M=(-2,1,0)` is obstructed inside the selected reduced Kunneth model.

## What Is Still Not Claimed

This is not full V_alpha stability by itself.  The remaining global proof
obligations are:

1. prove every destabilizing rank-one/torsion-free subsheaf is in the finite
   branch list, or provide a source theorem reducing to it;
2. promote the reduced Kunneth functor to raw selected Appell-Humbert/Cech
   multiplication if the final paper requires good-cover transition data;
3. derive the HYM/Strominger source or use the stability result with the
   appropriate existence theorem.

It does not prove HYM existence or full SM closure.
