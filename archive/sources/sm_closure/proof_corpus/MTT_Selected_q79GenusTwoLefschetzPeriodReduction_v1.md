# MTT Selected q79 Genus-Two Lefschetz Period Reduction v1

Status: `MTT_U6_Q79_EXPLICIT_GENUS2_LEFSCHETZ_FIBRATION_90_NODES_AND_PRYM_NORMAL_FUNCTION_INPUT_CLOSED_CERTIFIED_PERIOD_EXECUTION_OPEN`

## A new exact projection

Project the smooth A110 incidence surface to its square elliptic factor:

```text
pi_E:C -> E_i,                 E_i: b^2=a^3-a,
C_e: a*x+b*y+z=0 in the K3.
```

On `x=1`, put `t=y/x`, `u=w/x^3`, and `z=-a-b*t`. The fiber is

```text
u^2=f_ab(t),
f_ab=g_ab^2+q_ab*h_ab,
q_ab=-(t^2+b*t+a).
```

The degrees are `6=2*3=2+4`, so every smooth fiber is the genus-two curve in
the K3 polarization class `H`. This replaces an unspecified surface good-cover
integration by a concrete family of hyperelliptic curves over one elliptic base.

## Exact discriminant theorem

SymPy elimination over `QQ` gives

```text
Disc_t(f_ab)=P45(a)+b*Q43(a) modulo b^2-a^3+a.
```

Taking the elliptic norm gives

```text
N90(a)=P45(a)^2-(a^3-a)Q43(a)^2.
```

The generated certificate verifies exactly

```text
deg N90=90,
gcd(N90,N90')=1,
gcd(P45,Q43)=1.
```

At `O=[0:1:0]`, `P45` has pole order 90 while `b Q43` has pole order 89, so
there is no missing discriminant zero at infinity. Thus there are exactly 90
distinct discriminant points. A simple binary-sextic discriminant zero is one
transverse double-root collision, hence one nodal fiber. Their total Euler
contribution is 90, independently reproducing `c2(C)=90` and `b2(C)=92`.

## The eight forms are now explicit

For the six off-diagonal matrices and two Cartan matrices of `sl3`, set

```text
L_M=X^T M e,
X=(1,t,-a-b*t),
e=(a,b,1).
```

The eight independent A106 forms are

```text
omega_M=L_M(a,b,t) dt wedge da/(2 b u).
```

All eight numerators are emitted in the packet and have exact coefficient
rank eight. This is the concrete residue basis needed by the period engine.

## The gerbe source is an algebraic normal function

On a smooth fiber, the two roots of `q_ab` cut the split curve `R_plus` at

```text
P_i=(t=r_i,u=g_ab(r_i)).
```

Since `delta=R_plus-H`, its restriction is represented by

```text
D_delta(e)=P_1+P_2-P_infinity_plus-P_infinity_minus.
```

This has degree zero and gives an explicit Abel-Jacobi normal function with
coordinates obtained from `dt/u` and `t dt/u`. The A110 Poincare cocycle
restricts trivially on each curve because `H^2(C_e,O^*)=0`. In the Leray
description, continuation of these fiberwise trivializations is represented by
the same restricted `O(delta)` cocycle. Abel's theorem identifies it with
`AJ(D_delta(e))`. The gerbe calculation therefore becomes one inhomogeneous
rank-four genus-two Gauss-Manin problem.
No beta period or integral relation is inferred merely from this reduction.

## Remaining certified execution

The next computation must isolate the 90 critical values, calculate integral
Picard-Lefschetz monodromy, assemble the rank-92 surface homology, continue the
normal function with interval bounds, and evaluate the eight-by-92 period
matrix. Only exact equality `z=Pi ell` for `ell in Z^92`, or a proved separation
bound, decides `beta_C`.

The constructive `tau=i` and identity alignment remain unselected, zero strict
source moduli are removed, and U6 is not declared closed.

## External computational basis

- Lairez, Pichon-Pharabod and Vanhove, *Effective homology and periods of
  complex projective hypersurfaces*, arXiv:2306.05263.
- Sertoz, *Computing Periods of Hypersurfaces*, arXiv:1803.08068.
- Brinzanescu and Moraru, *Twisted Fourier-Mukai transforms and bundles on
  non-Kahler elliptic surfaces*, arXiv:math/0309031.

Next artifact: `MTT_Selected_q79GenusTwoMonodromyBetaPeriodExecution_v1`.
