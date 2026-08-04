# MTT Selected q79 Covariant Period Branch Cutset and Tight Beta Transport v1

## Result

A126 proved that the frozen selected-side `ell=0` representative is nonzero.
It did not decide the analytic-Brauer class modulo the integral period image.
A127 advances that exact problem in three ways:

1. it tightens the selected-side endpoint beta enclosure;
2. it proves the same-carrier rule and removes an invalid identity/endpoint
   period comparison;
3. it constructs the selected-alignment genus-two fibration, all 90 simple
   critical values, a certified distinguished cut system, and all 90
   pointwise Picard-Lefschetz monodromies.

No observed Standard-Model value is used. The frozen alignment is still a
selected-side computational carrier, not yet an MTT source-selection theorem.

## Tight endpoint beta

The A126 interval engine was rerun on the same certified local lower contour
with order 40 and maximum trial step `0.005`. It accepted 262 steps and
rejected 15. The result is

```text
||beta_center||_2                 2.3571952407293737
uniform component radius         0.0070601942733186695
||beta||_2 lower bound            2.3372259957407406
maximum component lower bound    1.4020766256556605
```

The old A126 component radius was `0.037895684949...`; the new enclosure is
more than five times tighter and has the same endpoint center to the stored
precision. Thus the selected-side `ell=0` exclusion is preserved and
strengthened. This still says nothing by itself about `ell != 0`.

## Same-carrier cutset

The exact equation from A106 is

```text
F(A,ell)=z(A)-Pi(A) ell,
J=nabla z(A)-sum_I ell_I nabla Pi_I(A).
```

Both `z` and `Pi` depend on the alignment and Hodge carrier. Consequently,
the A126 selected-alignment beta cannot be compared with A119's
identity-alignment period table. A small residual obtained from that mixed
pair has no mathematical status.

The retained lawful identity-alignment LLL/Kannan diagnostic illustrates the
other problem. It finds a floating residual of about `2.6843e-8`, while the
two-run period-plus-beta uncertainty proxy is about `1.0209e-3`. The proxy is
not an interval bound, and no branch-height theorem is available. Therefore
the search proves neither membership nor nonmembership.

There is, however, an important simplification. Let `B` and `B'` be complete
integral bases of endpoint `H_2`, with `B'=B U` and
`U in GL(92,Z)`. Then

```text
Pi_B'=Pi_B U,
image(Pi_B')=image(Pi_B).
```

Hence the endpoint membership problem does not require transporting A119's
individual identity-basis columns. It is enough to construct any complete
integral basis directly on the selected endpoint surface, provided the beta
and period rows use the same eight residue forms. This changes the executable
target from a 92-column cross-carrier transport to a direct endpoint
Lefschetz calculation.

## Selected-alignment fibration

Write the selected interval alignment as `A` and

```text
L=A [a,b,1]^T,
L0*x+L1*y+L2*z=0,
b^2=a^3-a.
```

On the `L1 != 0` chart, use `x=1`, `t=z/x` and
`y=-(L0+L2*t)/L1`. Homogeneous `L1^d` scaling gives interval binary forms
`F6,G3,Q2,H4`. All 196 coefficient balls of

```text
F6-G3^2-Q2*H4
```

contain zero; their maximum radius is below `8.82e-98`. The alignment
determinant has lower absolute bound `0.99999999999999989`.

## Exact dual discriminant

For a line `L`, the binary sextic discriminant in the above chart factors as

```text
Disc_t F(L1,-L0-L2*t,L1*t)=L1^30 D30(L0,L1,L2).
```

The code computes the exact integral homogeneous polynomial `D30`, with 496
terms. Pullback by the identity alignment reproduces A111's exact
`P45(a)+b Q43(a)` rows coefficient for coefficient. Pullback by the selected
interval alignment gives

```text
D30(A[a,b,1])=P45_A(a)+b Q43_A(a),
N90_A=P45_A(a)^2-(a^3-a) Q43_A(a)^2.
```

`N90_A` has interval-certified degree 90. FLINT isolates 90 disjoint root
balls, with minimum pairwise separation lower bound
`0.0054542032078333394`. At every root:

- `Q43_A` excludes zero;
- the chosen elliptic lift `b=-P45_A/Q43_A` excludes zero;
- `N90_A'` excludes zero;
- the opposite elliptic-sheet factor excludes zero.

The worst lower bounds are respectively about `9.98`, `0.0948`,
`1.197e7`, and `7.53`. Thus all 90 discriminant zeros are simple on the
elliptic base. A simple point of the binary-form discriminant is one sextic
with exactly one double root, so these are 90 nodal genus-two fibers.

The 90 points are lifted to the square elliptic uniformization. Their torus
balls have minimum pairwise separation above `0.0028924`. The three zeros of
the selected `L1` line chart are also isolated; their distance from every
critical ball is positive.

## Distinguished paths and monodromy

A radial fan based at `1/4+i/4` now supplies 90 ordered meridians. Every
critical, pole, boundary, pairwise-circle and selected-line-chart clearance
is positive. In particular, the smallest selected-chart clearance on an
outbound segment is above `4.64e-4`, so one fixed line chart is valid on the
entire fan.

The selected interval binary sextic was then connected to the existing
six-root braid action. For every meridian the pointwise ACB root continuation
returns a transposition and an integral symplectic rank-one unipotent matrix
`M`, with

```text
rank(M-I)=1,
(M-I)^2=0.
```

These 90 matrices are pointwise computations. A127 does not promote them to
continuous root tubes, does not yet assemble the endpoint integral surface
basis, and emits no endpoint period column.

## Exact remaining chain

The next artifact has a finite, non-repeating job:

1. certify continuous six-root tubes on the 90 already fixed paths;
2. assemble the selected endpoint integral `H_2` presentation;
3. execute 90 thimble and eight handle period columns in the same selected
   residue rows;
4. append the two exact Leray-edge columns;
5. decide `z in image(Pi)` by an exact branch certificate, not by a small
   floating residual.

Only after that decision may the rank-one spectral gerbe, inverse
Fourier-Mukai bundle, balanced HYM and differential Bianchi chain be promoted.

Next artifact:
`MTT_Selected_q79SelectedAlignmentRootTubesIntegralBasisAndPeriodExecution_v1`.
