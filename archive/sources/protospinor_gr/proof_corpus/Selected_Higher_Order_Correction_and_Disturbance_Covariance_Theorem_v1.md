# Selected Higher-Order Correction and Disturbance Covariance Theorem v1

## Result

The physical source-data problem has been made exact. It is not closed yet, but
the current corpus no longer leaves a vague normalization gap.

Closed same-branch data:

```text
G_11 = 1
U_raw = (v1_tilde, 0, 0)
v1_tilde(alpha_prime=1) = 64*(2*pi)^2/(16*R^4+8)
kappa = 1
lambda_internal = 15
K_ret,64 = S^-1 = S^63
```

The unit-covariance shortcut is refuted. The disturbance denominator must be
computed as the selected finite-memory projection

```text
d_Q = int_R P K_ret Q_tau K_ret^* P^* dt
rho_UV = C_UV^2 / d_Q
s_star = (60 rho_UV)^(1/6)
Lambda_gap_phys = sqrt(15) * Omega_0 / s_star
```

## What Remains

Three primitive source objects remain:

```text
C_UV   selected higher-order correction coefficient
Q_tau  selected unresolved finite-memory carrier covariance
Omega_0 physical inverse-length/action unit
```

This is the correct next gate because it prevents two bad moves: setting
`||D_raw||^2=1` by convention, and importing the unrelated threshold `delta`
as the OU/covariance denominator.

## Conditional Closure

If the branch supplies `C_UV`, derives `Q_tau`, evaluates `d_Q>0`, and supplies
`Omega_0` without observed target constants, then the earlier physical omega-gap
and modal-gap bridge certificates close the path to `ell_p`, `kappa_11`,
`G_eff`, and the TT Einstein-response scale.
