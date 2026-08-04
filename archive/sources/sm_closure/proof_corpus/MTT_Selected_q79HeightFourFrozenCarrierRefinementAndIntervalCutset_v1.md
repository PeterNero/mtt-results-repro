# MTT Selected q79 Height-Four Frozen-Carrier Refinement and Interval Cutset v1

## Result

A133 reruns the A127 validated selected-side beta transport at Taylor order 40
with maximum step `0.003`. The endpoint center agrees with A132 to
`3.410e-14`, while the rigorous uniform component radius improves from

```text
0.0070601942733186695  to  0.002168262443759486.
```

This is a factor `3.256153` refinement. The beta
enclosure is no longer what prevents a frozen-carrier decision for the A132
height-four seed.

## Honest fixed-carrier decision

At the refined center the largest residual occurs in row
`E32`:

```text
F_E32 center = -0.0028534354654821126
                                      -0.0047093745713692181 i,
|F_E32 center| = 0.005506387455413043.
```

The A131 two-run period envelope would give a positive separation lower bound
`0.0033381010396820146`. That is strong numerical
evidence, but it is not promoted to a theorem because the A131 envelope is not
an interval enclosure.

The exact remaining frozen-carrier object is only one complex number:

```text
sum_I m_I Pi_E32,I.
```

A rigorous enclosure of that selected combination with radius strictly below

```text
0.003338125011653557
```

proves separation in the `E32` row. Therefore all
720 individual period intervals are unnecessary for this decision. The full
primitive chain is emitted as `71` nonzero thimbles with
handle coordinates `[-1, 0, 1, 1, 0, 0, 0, 0]` so the next computation has no
hidden lattice reconstruction.

## Covariant scope

Frozen-carrier separation would not reject the height-four branch globally.
It would prove that the alignment must move. The branch must then be tested by

```text
F(A,m)=beta(A)-Pi_primary(A)m,
J_rs=nabla_s beta_r-sum_I m_I nabla_s Pi_rI.
```

Both derivative terms remain mandatory. A133 closes the refined beta and the
minimal interval cutset; it does not claim exact membership, exact separation,
or a covariant PGL3 zero.

No observed Standard Model value is used.
