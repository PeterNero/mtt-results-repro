# Selected Scale Coefficient Extraction for Flux/Strominger Branch v1

## Purpose

This note fixes the remaining coefficient-extraction gap as far as the current
corpus allows.

The scale-lifting lemma proved that

```text
F_scale(s) = A s^(-p) + B s^2
```

has a unique minimizer for `A,B,p > 0`. The present gate asks whether the
selected MTT/Strominger corpus supplies the actual coefficients.

## Extracted Exponent

The heterotic flux corpus states that the explicit solutions solve the
Hull-Strominger system at `O(alpha')`, while `O(alpha'^2)` curvature-squared and
higher-derivative corrections appear. Parametric control requires large volume
and small flux in string units.

Under a common dilation of the internal metric,

```text
length scale  -> s length scale,
curvature     -> s^(-2) curvature,
alpha'/R^2    -> s^(-2) (alpha'/R0^2).
```

The admissibility defect of the first omitted correction therefore scales as

```text
epsilon_UV(s) = C_UV s^(-2).
```

Since the minimization functional uses squared residual/barrier terms, the UV
penalty scales as

```text
F_UV(s) = A s^(-4).
```

Thus the selected squared-defect functional fixes

```text
p = 4.
```

The coefficient is

```text
A = C_UV^2,
```

where `C_UV` is the selected dimensionless coefficient of the first omitted
higher-alpha-prime/curvature correction in the chosen branch.

## Extracted OU Coefficient

The fixed-point/heterotic corpus gives, modewise,

```text
Var(a) = delta/(2 gamma),
gamma = kappa lambda - L - Delta_curv.
```

For the exact coherent branch after projector/gauge fixing, the scale-lifting
lemma used the most permissive case

```text
L = 0,
Delta_curv = 0.
```

The selected central-circle Hessian gives the normalized eigenvalue

```text
lambda0 = 15
```

before dilation, and under dilation

```text
lambda(s) = lambda0 / s^2.
```

Therefore

```text
F_OU(s) = delta/(2 kappa lambda(s))
        = delta/(2 kappa lambda0) s^2.
```

So

```text
B = delta/(2 kappa lambda0) = delta/(30 kappa).
```

If the selected exact-branch damping convention normalizes

```text
delta = 1,
kappa = 1,
```

then

```text
B = 1/30.
```

This normalization is not yet source-certified in the corpus. It must not be
silently assumed for physical predictions.

## Resulting Branch Formula

With the extracted exponent `p=4`, the scale-lifting minimizer becomes

```text
s_* = (4 A / (2 B))^(1/6)
    = (2 A / B)^(1/6).
```

Substituting `A=C_UV^2` and `B=delta/(30 kappa)` gives

```text
s_* = (60 kappa C_UV^2 / delta)^(1/6).
```

If, and only if, the selected branch later certifies

```text
C_UV = 1,
delta = 1,
kappa = 1,
```

then

```text
s_* = 60^(1/6) = 1.978602446467926.
```

This number is a normalized demonstration branch, not a physical constant.

## What Is Fixed

The current corpus fixes the coefficient structure:

```text
p = 4,
B = delta/(30 kappa),
A = C_UV^2,
s_* = (60 kappa C_UV^2 / delta)^(1/6).
```

This closes the algebraic coefficient-extraction gap.

## What Remains

The corpus does not currently compute:

```text
C_UV,
delta,
kappa
```

from the selected full MTT/Strominger branch.

Therefore physical absolute normalization remains open. The remaining task is
now narrower:

```text
compute C_UV, delta, and kappa from source-certified branch data,
then evaluate s_*,
then propagate to G10/R1^3 and only afterwards compare to observations.
```

## Forbidden Shortcuts

The program must not set `C_UV`, `delta`, or `kappa` by matching:

```text
G_N,
M_Pl,
H0,
rho_DE,
absolute f_a,
or any other target dimensionful observable.
```

## Verdict

The final lemma gap is fixed as a formula-level extraction:

```text
p=4,
A=C_UV^2,
B=delta/(30 kappa),
s_*=(60 kappa C_UV^2/delta)^(1/6).
```

The remaining gap is no longer structural or variational. It is the explicit
branch-coefficient computation for `C_UV`, `delta`, and `kappa`.
