# MTT Selected q79 Projective Line-Chart Covariance and Ell-Zero Continuation

## What A123 corrects

A122 proved the aligned-divisor normal-function source. That exact theorem is
unchanged. Its exploratory descent, however, measured separation between roots
in the affine coordinate obtained by eliminating `z`. The two descents appeared
to approach a nodal wall with a nonzero beta residual.

A123 shows that this first wall was a projective chart artifact. It constructs a
second line chart, proves exact covariance of the splitting family, reduced
periods and residue rows, transports the same `ell=0` base lift between charts,
and continues the search beyond the former stopping point.

## Two projective line charts

Let

```text
ell=A(a,b,1)^T=(ell_0,ell_1,ell_2).
```

On `ell_2 != 0`, eliminate `z` and use `t_z=y/x`:

```text
X_z=(ell_2, ell_2 t_z, -(ell_0+ell_1 t_z)).
```

On `ell_1 != 0`, eliminate `y` and use `t_y=z/x`:

```text
X_y=(ell_1, -(ell_0+ell_2 t_y), ell_1 t_y).
```

On the overlap,

```text
t_z=-(ell_0+ell_2 t_y)/ell_1,
X_z=(ell_2/ell_1) X_y.
```

Consequently every homogeneous polynomial `P_d` of degree `d` obeys

```text
P_d(X_z(t_z(t_y)))=(ell_2/ell_1)^d P_d(X_y(t_y)).
```

The symbolic residual is zero for every monomial in degrees `2,3,4,6`, hence
simultaneously for `Q2,G3,H4,F6`. In particular, both charts preserve

```text
F6=G3^2+Q2 H4.
```

The hyperelliptic coordinates satisfy

```text
U_z=(ell_2/ell_1)^3 U_y.
```

Root differences therefore transform as

```text
t_z,i-t_z,j=-(ell_2/ell_1)(t_y,i-t_y,j).
```

A small `z`-chart root gap can thus be caused solely by a small chart scale
`ell_2/ell_1`; it is not itself a vanishing-cycle invariant.

## Residue and reduced-period covariance

For a line variation `v=(v_0,v_1,v_2)`, the denominator-free residue numerators
are

```text
N_z=ell_2[(v_0 ell_2-v_2 ell_0)
          +(v_1 ell_2-v_2 ell_1)t_z],

N_y=-ell_1[(v_0 ell_1-v_1 ell_0)
           +(v_2 ell_1-v_1 ell_2)t_y].
```

The minus sign records the orientation change. Direct substitution proves

```text
N_z dt_z/U_z = N_y dt_y/U_y
```

with exact symbolic residual zero.

Let `I_k^z` and `I_k^y` be the five reduced periods for powers `k=0,...,4`.
Writing

```text
alpha=-ell_0/ell_1,
gamma=-ell_2/ell_1,
C=-ell_1^2/ell_2^2,
```

gives the triangular transition

```text
I_k^z=C sum_{j=0}^k binom(k,j) alpha^(k-j) gamma^j I_j^y.
```

Its exact determinant is

```text
C^5 gamma^(0+1+2+3+4)=-1.
```

Thus the five-component reduced lift is nonsingular on the overlap. This also
identifies an important branch rule: the already selected base lift must be
transformed by this matrix. Recomputing unrelated straight Abel-Jacobi paths in
the second chart can add an integral period and therefore change the displayed
representative even though the Deligne quotient class is unchanged.

**Q79ProjectiveLineChartCovarianceTheorem.** On `ell_1 ell_2 != 0`, the two
line charts define the same aligned splitting curve, Mumford divisor, residue
one-forms and reduced normal-function lift. The period transition has
determinant `-1`. Hence affine root collapse caused by the chart scale is not a
Picard-Lefschetz degeneration.

## Numerical chart audit

At the latest clean A122 carrier, the full base loop gives

```text
minimum z-chart root gap: 0.005845
minimum y-chart root gap: 0.095842
```

At the independent corrected carrier it gives

```text
minimum z-chart root gap: 0.005252
minimum y-chart root gap: 0.127416
```

The `y` chart remains uniformly valid. Root sets transformed between the two
charts agree within the recorded floating root-matching envelope.

Using the exact five-period transition, the same clean `ell=0` representative
computed in both charts agrees to

```text
maximum absolute beta difference: 1.312e-5
projective beta overlap:           0.999999999975
base-lift transition residual:     1.241e-16.
```

The beta comparison is floating and tolerance-dependent; the chart and residue
identities above are exact.

## Continuation beyond the false wall

Three fresh-Jacobian steps followed by two guarded complex Broyden updates in
the regular `y` chart preserve the base lift selected in the original `z`
chart. The beta norm chain is

```text
2.729845
 -> 2.479946
 -> 2.403365
 -> 2.373616
 -> 2.358893
 -> 2.357980.
```

The first three regular-chart Jacobians remain numerically full rank. The final
fresh minimum singular value before the secant updates is `0.002815`.

At the new frontier, one branch pair is genuinely distinguished: the latest
projective separation is approximately `0.01202`, while the line chart remains
well conditioned. Larger trial steps produce a one-sided beta change near norm
`2.78`; a much smaller step remains on the original side. This is floating
evidence that the continuation has now reached a genuine simple-node
Picard-Lefschetz boundary. It is not yet a certified limiting-residual theorem.

## Strict conclusion

A123 closes:

- exact covariance of the degree `2,3,4,6` aligned family between two line
  charts;
- exact covariance of the moving residue one-forms;
- the exact five-period transition with determinant `-1`;
- same-integral-branch transport of the base normal-function lift;
- retirement of the first A122 apparent nodal wall as a chart artifact;
- reproducible `ell=0` continuation beyond that wall.

A123 does not prove:

- a smooth `ell=0` PGL3 zero;
- a global `ell=0` no-go;
- an interval-certified one-sided Picard-Lefschetz limit;
- a selected nonzero vector in `Z^92`.

The next target is the local simple-node regularization. One must extract the
Gauss-Manin residue, subtract its explicit Picard-Lefschetz singular term, and
interval-certify the two one-sided limiting beta vectors. A nonzero lower bound
on the selected side would exclude this `ell=0` basin without claiming a global
no-go; a zero enclosure would provide the candidate needed for interval Newton.
