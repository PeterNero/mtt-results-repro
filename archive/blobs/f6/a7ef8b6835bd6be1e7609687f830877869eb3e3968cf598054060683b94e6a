# MTT Selected q79 Aligned-Divisor Normal-Function Source and PGL3 Branch Diagnosis

> **A123 supersession note.** A123 preserves the exact aligned-source theorem
> below but retires the exploratory interpretation of the first small affine
> root gap as a nodal wall. Exact projective line-chart covariance shows that
> the gap was scaled by `ell_2/ell_1`; the same `ell=0` branch has since been
> continued in the regular chart to the first genuinely distinguished pair.

## What A122 closes

A121 fixed the normalized Deligne representative

```text
beta_C=[R_B] in C^8/Pi(H^2(C,Z))
```

at the identity alignment. To vary the eight `PGL3` alignment coordinates, the
genus-two sextic, splitting divisor, normal function and residue rows must all
be varied on the same carrier. A122 proves and implements the missing
same-carrier source rule.

The correction matters. The first exploratory nonidentity evaluator aligned
the sextic and residue rows but continued to use the identity divisor
`q=t^2+b t+a` in the inhomogeneous normal-function source. Those nonidentity
beta vectors and Jacobians are retired. The identity A121 computation is not
affected because at `A=I` the aligned and identity divisors coincide exactly.

## Exact aligned family

Let

```text
ell=A (a,b,1)^T
```

for `A in PGL3`. In the affine line chart set

```text
z=-(ell_0+ell_1 t)/ell_2,   U=ell_2^3 u.
```

Homogeneity gives the denominator-free aligned polynomials

```text
f_A=ell_2^6 F|line,
g_A=ell_2^3 G|line,
q_A=ell_2^2 Q|line,
h_A=ell_2^4 H|line.
```

Therefore the splitting identity survives exactly:

```text
f_A=g_A^2+q_A h_A.
```

The moving residue numerator scales as `L ell_2^2`. This is the same
homogeneous substitution used by the aligned period evaluator.

## Aligned source theorem

The two moving points of the splitting divisor satisfy

```text
q_A(a(w),b(w),t_i(w))=0.
```

At a smooth divisor point, `partial_t q_A` is nonzero. Differentiating the
displayed equation gives

```text
dt_i/dw =
 -(partial_a(q_A) da/dw + partial_b(q_A) db/dw)/partial_t(q_A).
```

If `E_k(t)` is the exact-term numerator produced by the Gauss-Manin reduction,
the inhomogeneous source row is

```text
S_k = sum_i [ E_k(t_i)/g_A(t_i)
              + t_i^k (dt_i/dw)/g_A(t_i) ].
```

For the reciprocal coordinate `s=1/t`, the same rule is applied to

```text
q_A^vee=s^2 q_A(a,b,1/s),
g_A^vee=s^3 g_A(a,b,1/s).
```

The chain-rule residual reduces symbolically to zero. At `A=I`, the frozen
packet uses the unit-normalized expressions

```text
q_A=-(t^2+b t+a),
q_A^vee=-(a s^2+b s+1),
```

whose roots and implicit-velocity ratio are exactly those of the A120/A121
formula. The common unit `-1` cancels between numerator and denominator in
the implicit derivative.

**Q79AlignedSplittingDivisorNormalFunctionSourceTheorem.** For every smooth
aligned carrier on which `q_A` is quadratic and `partial_t q_A` does not vanish
at its two roots, the packet-selected normal-function source is the source
above. It is not lawful to align `f,g,q,h` and then reuse roots or velocities
from the identity divisor.

## Numerical compatibility

The generalized evaluator at `A=I` agrees with the independently frozen A121
beta vector to

```text
7.156e-10
```

in maximum absolute component difference.

At a nonidentity carrier, a perturbation of maximum coordinate size
`1.171875e-5` changes the corrected beta vector by only

```text
7.823e-5.
```

Forcing the Arb reduction at every connection evaluation gives the same local
continuity. Thus the former order-one jump was caused by the wrong divisor
source, not by the mixed-precision threshold.

## Corrected zero search

A fresh-Jacobian trust search was restarted from the identity, without using
any retired nonidentity beta or Jacobian. Four accepted carriers give

```text
||beta||:
5.110165 -> 4.588310 -> 3.831934 -> 3.226341 -> 2.729845.
```

All four corrected complex `8x8` Jacobians have eight nonzero floating
singular values. Their smallest singular values are

```text
0.03231, 0.02425, 0.01433, 0.007366.
```

The minimum branch-point separation simultaneously falls to

```text
0.005844.
```

An independent arbitrary carrier, recomputed entirely with the corrected
source, reaches norm `3.072335` at separation `0.005249`. The latest beta
directions from the two trajectories have projective overlap

```text
0.989307.
```

Three-point local extrapolations give nonzero limiting vector norms `2.553`
and `2.847`. These regressions are evidence of a common nodal residual; they
are not interval enclosures and are not a separation theorem.

## Basin and integral checks

Twelve deterministic random carriers at coordinate scales `0.06`, `0.12` and
`0.20` were screened along sampled identity-to-carrier paths. All retained
paths stayed above branch separation `0.02`. Their beta norms range from
`4.831` to `10.398`; none is a zero.

A bounded `ell_j in {-1,0,1}` MILP search on the A119 `8x92` period table was
also executed. It timed out without optimality and its best incumbent has
support 58 and residual norm `1.921`. It is retained only as a negative
exploratory result. It is not an exact integral branch.

## Strict conclusion

A122 closes:

- the homogeneous aligned splitting family;
- the packet-selected `q_A` roots in the normal-function source;
- the implicit aligned root-velocity formula;
- exact identity and reciprocal-chart specialization;
- retirement of the invalid pre-fix nonidentity beta/Jacobian values;
- a reproducible corrected floating branch diagnosis.

A122 does not prove:

- a smooth `ell=0` PGL3 zero;
- a global `ell=0` no-go;
- exact membership or nonmembership in the `Z^92` period image;
- a certified Jacobian at a gerbe zero.

The historical next target stated here was a local-coordinate residual theorem.
A123 has now removed the first apparent wall as a chart artifact. The active
target is the one-sided Picard-Lefschetz regularization at the later, genuinely
distinguished branch pair, or a selected nonzero integral branch transported on
the same aligned carrier.
