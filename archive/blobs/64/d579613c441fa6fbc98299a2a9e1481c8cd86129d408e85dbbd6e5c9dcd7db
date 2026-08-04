# Selected Scalar ExpS to Full HYM Row Model Lift v1

## Theorem

On the selected one-row Appell-Humbert extension model, the scalar diagonal
`exp(S)` replay proves the full finite row-model rank-2 HYM equation.

The selected holomorphic structure is:

```text
barpartial_V = [[barpartial_L, eta_00^unit], [0, barpartial_L^-1]]
```

Use the determinant-one Hermitian metric:

```text
S = s*T3
H = exp(S)=diag(exp(s), exp(-s))
det(H)=1
```

Then:

```text
off-diagonal HYM residual = 0
central trace residual = 0
trace-free diagonal residual = Delta s + |eta_00^unit|^2 exp(-2s)
                               - mean(|eta_00^unit|^2 exp(-2s))
```

The off-diagonal residual vanishes because `eta_00^unit` is harmonic in the
selected row model:

```text
barpartial eta_00 = 0
barpartial^* eta_00 = 0
```

The trace-free diagonal residual is exactly the scalar replay already solved:

```text
finite row-model HYM residual L2 = 9.887e-13
```

The zero-mean Jacobian has coercive lower bound:

```text
lambda >= (2*pi)^2 = 39.47841760435743
```

## Boundary

This proves the full finite HYM equation inside the selected one-row
Appell-Humbert row model. It does not yet emit the downstream finite derivative
basis, continuum truncation certificate, full connection-space gauge projector,
or validator-ready `rhoE/D_E/Riesz/Green/dotD` payload.

Status:

```text
SELECTED_SCALAR_EXPS_TO_FULL_HYM_ROW_MODEL_LIFT_PROVED_OPERATOR_PAYLOAD_OPEN
```

Next:

```text
MTT_Selected_Diagonal_HYM_Operator_Payload_Extraction_v1
```
