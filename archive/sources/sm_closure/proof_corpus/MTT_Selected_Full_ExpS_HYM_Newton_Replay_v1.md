# MTT Selected Full ExpS HYM Newton Replay v1

## Result

The diagonal trace-free `exp(S)` replay is solved in the selected `T3` lane:

```text
S = u*T3
H = exp(S)
Delta u = rho*exp(-2u) - mean(rho*exp(-2u))
rho = |eta_00^unit|^2
mean(u)=0
```

The zero mode is not a parameter: the right-hand side is forced to have mean
zero because `int Delta u = 0`.

## Numerical Certificate

```text
mesh = 24^4
iterations = 40
final residual L2 = 8.208e-13
u_min = -0.0912925545796
u_max = 0.045621750168
mean(rho exp(-2u)) = 1.09591232828
```

This closes the diagonal nonlinear replay with the quadratic metric factor
`exp(-2u)` included.

## Guardrail

This is still the diagonal `T3` HYM lane, not the full validator-ready operator
payload.  The remaining work is off-diagonal End0 connection components, a full
Jacobian/coercivity certificate, truncation bounds for operator extraction, and
the finite `rho_E`, `D_E`, Riesz/Green, `dotD`, and overlap payloads.

## Next Artifact

`MTT_Selected_HYM_Operator_Payload_Extraction_From_Diagonal_Replay_v1`.
