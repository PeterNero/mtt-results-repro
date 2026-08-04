# Selected Diagonal HYM Operator Payload Extraction v1

## Result

The selected row-model HYM solution now emits the rank-2 diagonal
metric/connection payload:

```text
H = diag(exp(s), exp(-s))
A_diag = d s * T3
```

The determinant is pointwise fixed:

```text
max |det(H)-1| = 2.220e-16
```

The finite curvature residual remains:

```text
||Delta s + rho exp(-2s)-mean(rho exp(-2s))||_L2 = 9.887e-13
```

Gradient norm:

```text
||d s||_L2 = 0.1788376609756834
```

The shared-circle/`z3` direction remains zero.

## Boundary

This is still not validator-ready `rhoE/D_E/Riesz/Green/dotD` data. It is the
selected rank-2 metric and diagonal connection payload needed by the next End0
operator extraction.

Status:

```text
SELECTED_DIAGONAL_HYM_OPERATOR_PAYLOAD_EXTRACTED_END0_DE_OPEN
```

Next:

```text
MTT_Selected_End0_DE_Payload_From_Diagonal_HYM_v1
```
