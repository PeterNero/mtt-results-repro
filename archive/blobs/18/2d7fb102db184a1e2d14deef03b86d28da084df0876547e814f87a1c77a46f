# Selected Horizontal Scale Law for Iwasawa rho_UV v1

## Purpose

This theorem closes the scale-law choice left open by the
Bianchi-constrained scale-lifting check.

The issue was whether the UV term along the selected Iwasawa path is

```text
H1: rho_UV(R) R^(-4)
```

or

```text
H2: rho_UV(R).
```

The selected law is H2.

## Reason

The final selected-character rho_UV theorem defines

```text
rho_UV(R) = ||U_raw(R)||_coeff^2 / ||D_raw||_coeff^2.
```

On the selected character branch,

```text
||D_raw||_coeff^2 = 1
```

and the UV response row is

```text
U_raw(R) = (v1_tilde(R),0,0),
v1_tilde(R) = 64(2pi)^2/(16R^4+8).
```

Therefore

```text
rho_UV(R) = v1_tilde(R)^2
```

is already the squared UV response evaluated on the Bianchi-constrained
horizontal branch

```text
R -> (r1,r2,r3) = (R,R,r3(R)).
```

Multiplying by an additional `R^(-4)` would count the horizontal curvature
scaling twice: once through `v1_tilde(R)`, and again through an external
generic-dilation factor. That generic factor belongs to the abstract
scale-lifting lemma before the selected branch coefficient is evaluated. After
branch evaluation, the selected UV term is the evaluated response norm itself.

Thus the selected Bianchi-constrained horizontal functional is

```text
F_H2(R) = rho_UV(R) + R^2/30.
```

## Selected Functional

Using

```text
rho_UV(R) = [64(2pi)^2/(16R^4+8)]^2,
```

the selected functional is

```text
F_H2(R)
  = [64(2pi)^2/(16R^4+8)]^2 + R^2/30,
  R > 0.
```

The `R^2/30` term is the selected OU/damping floor with

```text
kappa = 1,
lambda0 = 15,
delta = 1
```

on the selected character-normalized branch.

## Euler Equation

Let

```text
a = 64(2pi)^2.
```

Then

```text
F_H2(R) = a^2/(16R^4+8)^2 + R^2/30.
```

Writing `x=R^2`, the derivative equation is

```text
dF_H2/dx = 1/30 - 64 a^2 x/(16x^2+8)^3 = 0.
```

Equivalently,

```text
(16x^2+8)^3 = 1920 a^2 x.
```

This equation has two positive stationary points. The very small one is a
local maximum near `R=0`; the large one is the global minimum. Direct
evaluation gives:

```text
R_max = 0.0002043829462837498,
R_*   = 4.440528182269818.
```

The selected minimizer is therefore

```text
R_* = 4.440528182269818.
```

## Final Selected Values

At the selected H2 minimizer:

```text
R_*     = 4.440528182269818,
r3      = 4.440028979122532,
v1      = 0.405623467693425,
rho_UV  = 0.164530397543639,
s_*     = 1.464646774701829.
```

Here `s_*` is the scale-lifting value computed from `rho_UV`; it is not equal
to `R_*` because the fixed-point law `R=s_*(R)` has been rejected as the final
Euler equation for the Bianchi-constrained functional.

## Status of the Earlier Candidates

The old candidates are now classified:

```text
FP: R = s_*(R)
    useful compatibility equation, not the selected Euler equation.

H1: rho_UV(R) R^(-4) + R^2/30
    rejected because it double-counts the curvature scaling already present
    in v1_tilde(R).

H2: rho_UV(R) + R^2/30
    selected horizontal scale law.
```

## Primitive-Constant Note

No primitive `R` is needed for this internal branch. The radius is selected by
the horizontal functional before comparison to external constants.

Primitive constants may still exist elsewhere in the theory, but this rho_UV
branch no longer requires one at this gate.

## Verdict

The next true gate is closed:

```text
selected horizontal scale law = H2,
R_* = 4.440528182269818,
rho_UV = 0.164530397543639.
```

This is an internal dimensionless branch result. It still does not by itself
predict a dimensionful SI constant.
