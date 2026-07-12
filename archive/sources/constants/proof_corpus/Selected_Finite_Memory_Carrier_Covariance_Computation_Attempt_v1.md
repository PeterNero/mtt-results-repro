# Selected Finite-Memory Carrier Covariance Computation Attempt v1

## Purpose

The previous repair theorem identified the last missing object:

```text
Q_tau = selected unresolved finite-memory carrier covariance.
```

This note computes it as far as the current corpus allows.

## Source Formula

The fixed-point disturbance corpus gives a deterministic homogenization route.
For the fast unresolved flow

```text
dot Y = L_x(Y)
```

with invariant measure `mu_x`, mean-zero coupling

```text
G(x,y) = g(x,y) - bar g(x),
```

and autocovariance

```text
R_x(s) = int G(x,Y_s) tensor G(x,Y_0) dmu_x(Y_0),
```

the effective diffusion tensor is the Green-Kubo integral

```text
sigma(x) sigma(x)^* =
  2 int_0^infty (R_x(s)+R_x(s)^*) ds.
```

This is exactly the mathematical form needed for the unresolved carrier
covariance. In the present notation,

```text
Q_tau := 2 int_0^infty (R_x(s)+R_x(s)^*) ds
```

restricted to the selected unresolved channel and expressed in the invariant
coefficient basis.

## Z64 Retarded-Kernel Reduction

The exact central-circle branch has

```text
K_ret,64 = S^-1 = S^63,
```

where `S e_j = e_{j+1 mod 64}`. Let the selected alpha_1 coefficient projection
be represented in the exact carrier basis by a unit row vector `p^T`.

Then the remaining covariance is

```text
||D_raw||_coeff^2 = p^T S^-1 Q_tau S p.
```

Equivalently, with

```text
p_+ := S p,
```

one has

```text
||D_raw||_coeff^2 = p_+^T Q_tau p_+.
```

Thus the retarded kernel does not introduce a new amplitude. It only shifts the
carrier coordinate before the covariance is read.

## Consequence Under Z64-Equivariant Covariance

If the selected unresolved carrier covariance is Z64-equivariant, then

```text
S^-1 Q_tau S = Q_tau.
```

In that case

```text
||D_raw||_coeff^2 = p^T Q_tau p.
```

If additionally the selected alpha_1 projection is a basis coordinate,
`p=e_0`, then

```text
||D_raw||_coeff^2 = (Q_tau)_{00}.
```

For any circulant Z64-equivariant covariance, all diagonal entries are equal, so
the problem reduces to a single scalar:

```text
d := (Q_tau)_{00}.
```

The branch ratio is therefore

```text
rho_UV(R) =
  [64(2pi)^2/(16 R^4 + 8)]^2 / d.
```

## Diagnostic Candidate Values

The current corpus does not select `d`. The following values are diagnostic
normalizations of the same algebraic carrier, not predictions:

| Carrier covariance | d | rho_UV multiplier |
|---|---:|---:|
| identity covariance `Q_tau=I` | 1 | 1 |
| trace-one maximally mixed covariance `Q_tau=I/64` | 1/64 | 64 |
| mean-zero Haar covariance `Q_tau=I-(1/64)11^T` | 63/64 | 64/63 |

The spread proves why the covariance cannot be guessed from symmetry alone.
All three are Z64-equivariant, positive semidefinite, and natural in different
normalization conventions.

## Numeric Conditional Table

Using

```text
v1_tilde(R)=64(2pi)^2/(16R^4+8),
rho_UV=v1_tilde(R)^2/d,
s_*=(60 rho_UV)^(1/6),
```

the candidate values are:

| R | d=1 rho_UV | d=1 s_* | d=1/64 rho_UV | d=1/64 s_* | d=63/64 rho_UV | d=63/64 s_* |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 11082.9899132021 | 9.34260594395577 | 709311.354444931 | 18.6852118879115 | 11258.9103880148 | 9.36715993584814 |
| 2 | 91.5949579603476 | 4.20084963151094 | 5862.07730946224 | 8.40169926302188 | 93.0488461819404 | 4.21189019432735 |
| 5 | 0.0637360035033962 | 1.25051626958438 | 4.07910422421736 | 2.50103253916876 | 0.0647476860986882 | 1.253802843644 |

## Verdict

The actual computation reduces the missing covariance to

```text
d = p^T Q_tau p,
```

or, under Z64-equivariance and coordinate projection,

```text
d = (Q_tau)_{00}.
```

The corpus supplies the Green-Kubo formula for `Q_tau` but not the selected
fast invariant measure `mu_x`, coupling autocovariance `R_x(s)`, or normalization
choosing among Z64-equivariant carrier covariances. Therefore the current corpus
does not yet produce a unique numeric `d`.

The next required data are:

```text
mu_x and R_x(s) for the selected unresolved Z64/Strominger carrier,
or an independent source theorem selecting one of the carrier covariance
normalizations above.
```
