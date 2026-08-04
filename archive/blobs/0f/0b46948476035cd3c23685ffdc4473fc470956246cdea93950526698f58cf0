# MTT Selected q79 K3-Period Xi-Hessian Execution or Marked-Model Gerbe Certificate v1

Status: `MTT_U6_Q79_EXPLICIT_SMOOTH_MARKED_SPLITTING_CONIC_K3_CLOSED_PERIOD_GERBE_AND_SELECTION_OPEN`

## Constructive result

A109 takes the direct-model branch of A108 and fills an actual algebraic K3
carrier. Over the rationals, set

```text
Q2 = x*z-y^2,
G3 = -x^3+x^2*y+2*x^2*z-2*x*y^2+2*x*y*z+x*z^2+z^3,
H4 = -x^3*z-x^2*y*z-2*x*y^2*z-y^4+2*y^3*z-2*y^2*z^2+2*y*z^3,
F6 = G3^2+Q2*H4.
```

Then

```text
S: w^2=F6(x,y,z) subset P(1,1,1,3)
```

is a smooth K3 surface and the inverse image of `Q2=0` splits into

```text
R_plus : Q2=0, w=+G3,
R_minus: Q2=0, w=-G3.
```

## Exact smoothness certificate

All checks are over `QQ` with exact Groebner reduction. On each projective
chart `x=1`, `y=1`, and `z=1`, the following ideals have reduced basis `[1]`:

1. `Q2` plus its three partial derivatives;
2. the three partial derivatives of `F6`;
3. `Q2,G3` plus all `2x2` minors of their gradient matrix;
4. `Q2,G3,H4`.

Euler's identity `x Fx+y Fy+z Fz=6F6` has exact residual zero. Therefore the
conic and branch sextic are smooth, `Q2` and `G3` meet transversely in six
points, and `H4` is nonzero at every intersection. This is an exact algebraic
certificate, not floating-point sampling.

## q79 lattice marking

Let `H` be the pullback of a line and set `delta=R_plus-H`. Adjunction and the
six reduced intersections give

```text
H^2=2,
R_plus^2=R_minus^2=-2,
H.R_plus=H.R_minus=2,
R_plus.R_minus=6,
H.delta=0,
delta^2=-4.
```

Thus the model realizes the exact q79 lattice

```text
Gram(H,delta)=diag(2,-4).
```

The class `delta` is primitive: if `delta=2D`, evenness of the K3 lattice
would make `delta^2` divisible by eight, contradicting `delta^2=-4`. More
strongly, the discriminant form on `Z2 x Z4` has no nonzero isotropic class.
The span `<H,delta>` therefore has no proper even overlattice and is
primitively embedded in the K3 lattice.

## What this fills

A108's direct route had eight fields. A109 fills four exactly:

```text
Q2 coefficients,
G3 modulo Q2*L1 coefficients,
H4 coefficients,
projective smoothness certificate.
```

The remaining strict fields are

```text
elliptic tau,
PGL3 alignment A,
integral branch ell in Z^92,
exact relative-Deligne zero or no-go.
```

If the still-open Z4 Chern-orbit bridge is later proved, `tau=i` fills a fifth
field. It is not counted as strict here.

## Selection guard

This model proves nonemptiness and gives A106 a concrete exact carrier. It does
not prove that MTT selects these coefficients. Choosing one rational point in
the 18-complex-dimensional family removes zero strict source moduli and must be
published as a constructive test witness, not a no-knob prediction.

No observed physics value and no fitted physics parameter was used.

Next artifact: `MTT_Selected_q79ExplicitModelRelativeDeligneGerbeZeroOrNoGoExecution_v1`.
