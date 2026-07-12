# Selected Sharp Semigroup Bound Theorem v1

## Result

The semigroup prefactor is closed on the selected exact central-circle branch:

```text
C_Q = 1.
```

The imported branch has:

```text
L_64 = alpha L_tower, alpha > 0
normalized alpha = 1
lambda_star = 15
Schur correction = 0
```

Because the selected generator is a positive self-adjoint Hessian block and the
complement is an orthogonal spectral complement, the spectral theorem gives:

```text
|| exp(-t L_64) Q || <= exp(-lambda_star t).
```

The prefactor is exactly `1`. A larger value is merely weaker, and a smaller
value fails at `t=0` for normalized complement states.

This closes the sharp bound for the selected exact branch. It does not assert a
nonnormal bound for an unprojected full mixed Hessian.

## Omega0 Consequence

With the already closed quotient-cell result:

```text
epsilon_adm = 1/448,
```

the formula becomes:

```text
Omega0 = chi_omega * sqrt(alpha_phys) * sqrt(15/log(448)).
```

Numerically:

```text
log(448) = 6.10479323241498
sqrt(15/log(448)) = 1.56750938592616
R1(sigma=1) = 0.637954712729934
omega_gap_phys/(chi_omega*sqrt(alpha_phys)) = 1.0702303196928
Lambda_gap_phys/(chi_omega*sqrt(alpha_phys)) = 4.14498420477644
```

## Still Open

Only two physical normalization gates remain in this chain:

```text
alpha_phys
chi_omega
```
