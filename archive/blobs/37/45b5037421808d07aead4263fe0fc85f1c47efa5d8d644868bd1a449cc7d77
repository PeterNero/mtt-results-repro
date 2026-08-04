# Selected Scalar ExpS HYM Newton Replay v1

## Result

The selected diagonal scalar nonlinear replay closes on the finite theta grid.

With

```text
S = s*T3
H = exp(S)
rho = |eta_00^unit|^2
```

the solved equation is:

```text
Delta s + rho*exp(-2s) - mean(rho*exp(-2s)) = 0
mean(s)=0
```

Finite-grid result:

```text
mesh = 24^4
iterations = 61
residual_L2 = 9.887e-13
||s||_L2 = 0.02743487456065332
min(s), max(s) = -0.03750848523255589, 0.06968059291319133
mean(rho*exp(-2s)) = 0.9326509324572752
```

The zero-mean finite-grid Jacobian has the coercive lower bound:

```text
lambda >= (2*pi)^2 = 39.47841760435743
```

## Boundary

This closes the selected scalar diagonal `exp(S)` replay, including the
nonlinear exponential density term. It does not yet close the continuum
truncation certificate, the off-diagonal/full End0 connection coefficients, or
the full finite connection-space gauge projector.

Status:

```text
SELECTED_SCALAR_EXPS_HYM_REPLAY_CLOSED_FULL_CONNECTION_LIFT_OPEN
```

Next:

```text
MTT_Selected_ScalarExpS_to_Full_HYM_Operator_Lift_v1
```
