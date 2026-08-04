# MTT Selected q79 Picard-Lefschetz Interval Wall and Base Lift

## Purpose

A124 derived the exact local Picard-Lefschetz formula and matched its floating
transport with the observed one-sided beta jump. A125 promotes two previously
floating analytic layers:

1. existence, uniqueness, simplicity and transversality of the genuine wall;
2. the selected-side base Abel-Jacobi lift used as the initial condition for
   normal-function transport.

It also proves that the Picard-Lefschetz jump is nonzero. A125 does not promote
the endpoint selected-side beta vector; that now requires only validated
Gauss-Manin transport from the certified initial ball.

## Frozen analytic problem

The carrier is the A124 path

```text
A(s)=A_0 exp(s T),
```

where every entry of `A_0` and `T` is the exact real or complex number defined
by its stored decimal string. The base uniformization is evaluated directly by
Arb/ACB on

```text
w=1/4+i(1/4+u).
```

The wall equations in the regular `y` chart are the four real equations

```text
Re F=0, Im F=0, Re F_t=0, Im F_t=0
```

in `(s,u,Re t,Im t)`.

## Krawczyk wall certificate

At 90 decimal digits, A125 evaluates the equations and their complete real
Jacobian over the radius-`1e-10` box centered at

```text
s = 0.23502677005574063
u = 0.73455235511343608
t = 0.32587425869698694
    +0.00051355389152310971 i.
```

The midpoint Newton iterations are used only to choose this center. The proof
is the subsequent Krawczyk inclusion. The four coordinate inclusion margins
are

```text
6.38534e-11,
9.99864e-11,
9.99950e-11,
9.99949e-11.
```

They are all strictly positive, so the Krawczyk image lies in the interior of
the input box. The analytic wall system therefore has exactly one zero in this
box.

On the entire box, outward-rounded bounds give

```text
|F_tt|                    > 518938.3935
|F_u|                     > 32979.6834
|q_A(t_*)|                > 0.2858552
normalized y-chart scale  > 0.8740348452
Im(du_*/ds) in
  [-0.000335813942, -0.000335649074].
```

Thus the certified zero is a simple node, the real carrier crosses its
discriminant transversely, the selected splitting divisor misses the node, and
the chart remains regular. This independently confirms that the later A123
wall is genuine while its first wall remains a retired coordinate artifact.

## Nonzero jump theorem

At a simple node, A124 proved the exact local state

```text
V_k=2*pi*i*t_*^k/sqrt(F_tt(t_*)/2),  k=0,...,4.
```

A125 evaluates this expression on the full wall box and obtains

```text
|V_0| > 0.012334923056187106.
```

Hence `V` is nonzero. Away from the node, the homogeneous Gauss-Manin
fundamental matrix is invertible: its determinant obeys Liouville's formula
and cannot vanish when initialized by the identity. Therefore its transport
of `V` is nonzero.

**Q79IntervalTransverseNodeAndNonzeroPLJumpTheorem.** The frozen A124 carrier
has one unique transverse simple node in the certified box. Its selected
`q_A` divisor is disjoint and its `y` chart is regular. The oriented local
vanishing state and transported Picard-Lefschetz jump are nonzero. Consequently
the two one-sided beta limits cannot both vanish.

This theorem does not decide which side, if either, has zero selected
representative. It also does not decide equality to an integral period vector.

## Certified selected-side base lift

For a point guaranteed to lie on the selected side, A125 fixes

```text
s_- = lower(s-wall box)-0.005
    = 0.23002676995574059.
```

At the base fiber, ACB isolates both aligned `q_A` roots and all six sextic
roots. Starting on the exact sheets `U=G_A` at the two `q_A` roots, the
certifier:

- continues the square root through certified half-planes;
- integrates `t^k dt/U`, `k=0,...,4`, with `acb.integral`;
- inserts a 48-edge clockwise polygon around the selected branch point;
- returns both paths to the common outer point `20+7i`;
- cancels the opposite infinity sheets;
- applies the exact A123 `z`-to-`y` period transition.

The execution contains

```text
599 certified path segments
2995 rigorous scalar integrals
maximum subdivision depth                 13
minimum square-root half-plane margin      0.00130316
minimum branch-sign separation margin      1.37975765
opposite-sheet cancellation upper bound    5.176e-64
maximum base-lift component ball radius    9.366e-48.
```

The resulting `y`-chart lift is an interval vector containing approximately

```text
(-0.0051474621 +0.0910754316 i,
  0.0915767569 -0.0046917395 i,
 -0.2006793030 -0.0207606529 i,
  0.1182744739 -0.5033731624 i,
  2.3007052973 +0.4194662455 i).
```

Its midpoint agrees with the old floating base-lift execution to `3.87e-9`,
the latter's requested tolerance. This comparison is not needed for the Arb
certificate but confirms that A125 encloses the same selected lift.

## Lower-contour regularization

The original real base path passes within about `1.7e-6` of the selected-side
complex discriminant and creates a narrow Gauss-Manin conditioning spike. A
homotopic candidate contour through

```text
0,
0.65,
0.65-0.1i,
0.82-0.1i,
0.82,
1
```

reproduces the straight-path beta vector at common tight tolerance with

```text
maximum component difference       1.4535e-8
projective overlap                  1.0
condition-number reduction factor  17.6239.
```

This is a floating contour diagnostic. A trial low-condition path in a
different homotopy class produced a different beta and was rejected, showing
that endpoint agreement is a real branch guard rather than an automatic
consequence of contour deformation.

## Strict conclusion

A125 closes:

- interval existence and uniqueness of the genuine wall;
- interval simplicity, transversality, divisor disjointness and chart
  regularity;
- nonvanishing of the local state and transported PL jump;
- the theorem that both one-sided beta limits cannot vanish;
- the complete selected-side base Abel-Jacobi lift as an ACB interval vector;
- an explicitly better-conditioned same-branch floating contour for the next
  transport calculation.

A125 does not close:

- an interval homotopy certificate for the lower contour;
- high-order validated Gauss-Manin transport to the endpoint beta;
- an interval lower bound for the selected-side endpoint beta;
- the global `ell=0` no-go or exact `Z^92` branch selection.

The next artifact should use a validated high-order Taylor model, not the
rejected first-order interval exponential bound, to transport the certified
five-component initial ball and eight zero accumulator rows along the lower
contour.
