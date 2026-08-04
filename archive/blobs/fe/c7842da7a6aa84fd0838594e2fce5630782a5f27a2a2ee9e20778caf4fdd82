# Selected Branch Numeric CUV/Delta/Kappa Extraction v1

## Purpose

This note attempts the requested final coefficient calculation for

```text
s_* = (60 kappa C_UV^2 / delta)^(1/6).
```

It separates what the current corpus actually computes from what would require
new branch data.

## Kappa

The heterotic selection paper writes the unresolved-mode damping rate as

```text
gamma = kappa lambda - L - Delta_curv.
```

On the selected exact central-circle branch, the Z64 damping certificate gives

```text
L_64 = alpha L_tower,
alpha = 1,
lambda_* = 15,
K_ret,64 = S^-1,
E_Schur = 0.
```

The scale-lifting branch also uses the exact coherent projection case

```text
L = 0,
Delta_curv = 0.
```

In these normalized tower units the actual damping rate is therefore

```text
gamma = lambda.
```

Comparing with `gamma = kappa lambda` gives the source-certified value

```text
kappa = 1.
```

This is not an added convention. It is the normalization already fixed by the
selected exact-branch Hessian.

## Reduced Scale Formula

The previous coefficient-extraction note proved

```text
p = 4,
A = C_UV^2,
B = delta/(30 kappa),
s_* = (60 kappa C_UV^2 / delta)^(1/6).
```

Using the extracted exact-branch value `kappa=1`,

```text
B = delta/30,
s_* = (60 C_UV^2 / delta)^(1/6).
```

Thus the remaining calculation has only the ratio

```text
C_UV^2 / delta
```

open.

## Delta

The OU source writes the stochastic mode equation in the form

```text
da = -gamma a dt + sqrt(delta) dW_t,
Var(a) = delta/(2 gamma).
```

The white-noise/Markov-limit paper proves that white noise is the zero-memory
limit of finite-memory disturbance kernels and writes the integrated covariance
as a disturbance power. It does not compute that disturbance power from the
selected Z64/Strominger branch.

Therefore the current corpus supports the symbolic positive parameter

```text
delta > 0,
```

but it does not source-certify a numerical value for `delta`.

The canonical stochastic convention `delta=1` is allowed only as an internal
normalized demonstration branch. It is not a physical no-knob prediction unless
the finite-memory disturbance covariance is derived from the selected carrier
geometry.

## C_UV

The heterotic flux papers compute the `O(alpha')` Hull-Strominger/anomaly data
in the left-invariant sector and state that higher `O(alpha'^2)` curvature-
squared and higher-derivative corrections are suppressed in the controlled
large-volume regime.

The first omitted correction has the scale form

```text
epsilon_UV(s) = C_UV s^(-2),
F_UV(s) = C_UV^2 s^(-4).
```

But the corpus does not give the selected `O(alpha'^2)` local functional,
field-redefinition scheme, or invariant-frame evaluation of that correction on
the selected branch. Therefore the current corpus supports

```text
C_UV > 0,
```

but does not source-certify its numerical value.

## What Is Now Calculated

The remaining coefficient extraction is reduced from three coefficients to two:

```text
kappa = 1,
B = delta/30,
s_* = (60 C_UV^2 / delta)^(1/6).
```

Equivalently, the branch is fixed as soon as the single dimensionless ratio

```text
rho_UV := C_UV^2 / delta
```

is computed from selected branch data:

```text
s_* = (60 rho_UV)^(1/6).
```

## Demonstration Branch

If, only as an internal normalized demonstration, one sets

```text
C_UV = 1,
delta = 1,
kappa = 1,
```

then

```text
s_* = 60^(1/6) = 1.978602446467926.
```

This number is not certified as a physical prediction.

## No-Go for Full Closure from the Present Corpus

The present corpus does not contain:

```text
1. the selected O(alpha'^2) correction functional evaluated on the branch;
2. the finite-memory disturbance covariance induced by the selected carrier;
3. a fluctuation-dissipation or projection theorem tying that covariance to the
   same Hessian normalization.
```

Therefore full physical absolute-normalization closure cannot be honestly
claimed from the current files. The rigorous state is:

```text
kappa closed;
C_UV and delta open;
physical absolute normalization open.
```

This is a useful closure result because it proves the remaining gap is not a
hidden algebraic or variational problem. It is exactly the missing higher-order
correction and disturbance-covariance computation.
