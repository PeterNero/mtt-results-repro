# Selected Electroweak Threshold Kernel Reduction v1

## Purpose

The electroweak bridge audit showed that `rho_UV` is closed internally but not
yet connected to electroweak observables. This reduction makes the missing
object algebraically precise.

## Setup

Let the Theta overlap ratio select:

```text
r_12 := g_1(mu_Theta)^2 / g_2(mu_Theta)^2 = I_2(Theta) / I_1(Theta).
```

The Theta V source uses the representative value:

```text
r_12 = 0.56027.
```

Let:

```text
x := g_2(mu_Theta)^2.
```

Then:

```text
g_1(mu_Theta)^2 = r_12 x,
g_2(mu_Theta)^2 = x.
```

At one loop, with threshold/matching corrections written as additive entries in
`1/g_a^2`, the low-scale couplings satisfy:

```text
1/g_1(M_Z)^2 = 1/(r_12 x) + A_1 + T_1,
1/g_2(M_Z)^2 = 1/x       + A_2 + T_2,
```

where:

```text
A_a = b_a/(8 pi^2) log(mu_Theta/M_Z)
```

and `T_a` denotes the selected electroweak threshold/matching correction in
the same convention.

The weak angle is:

```text
sin^2(theta_W)(M_Z)
  = (3/5) g_1(M_Z)^2 / ((3/5) g_1(M_Z)^2 + g_2(M_Z)^2).
```

## Consequence

The high-scale ratio `r_12` alone fixes the high-scale GUT-normalized tree
identity:

```text
sin^2(theta_W)(mu_Theta) = (3 r_12)/(3 r_12 + 5).
```

But the low-scale angle depends on:

```text
x,
T_1,
T_2,
mu_Theta,
scheme.
```

Therefore a true no-knob electroweak closure must supply a selected kernel:

```text
K_EW(selected MTT branch)
  -> (mu_Theta, x, T_1, T_2, scheme)
```

or an equivalent source-certified object.

## Where rho_UV May Enter

The closed internal number:

```text
rho_UV = 0.164530397543639
```

may become relevant if the selected kernel proves one of the following:

```text
T_a = c_a rho_UV + d_a,
x   = X(rho_UV, finite branch data),
mu_Theta = Mu(rho_UV, finite branch data),
or a combined threshold functional whose entries are evaluated from rho_UV.
```

But none of these maps is presently source-certified. The allowed next move is
to derive the map. The forbidden move is to choose `c_a`, `d_a`, `x`, or
`mu_Theta` so that the observed weak angle is reproduced.

## Minimal Closure Theorem

The next theorem should prove:

```text
1. r_12 is selected by Theta overlaps with fixed normalization.
2. x is selected internally, or replaced by one permitted universal primitive.
3. T_1 and T_2 are selected by a finite electroweak threshold kernel.
4. mu_Theta is selected before comparison with data.
5. the RG and matching scheme is fixed before comparison with data.
```

Then the weak angle can be computed without using `sin^2(theta_W)` as an
input.

## Verdict

The exact missing piece is not another qualitative Standard Model statement.
It is a finite response/matching object:

```text
K_EW: selected MTT branch -> electroweak inverse-coupling corrections.
```

Once `K_EW` is source-certified, the weak-angle calculation becomes an
ordinary executable evaluation rather than a fit.
