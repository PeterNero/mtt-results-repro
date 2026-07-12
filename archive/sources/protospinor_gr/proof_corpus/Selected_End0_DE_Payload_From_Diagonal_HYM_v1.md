# Selected End0 DE Payload From Diagonal HYM v1

## Result

The diagonal HYM connection now induces a selected `End_0(V_alpha)` operator
payload:

```text
A_diag = d s * T3
D_E = d + ad(A_diag)
D_a = partial_a I_3 + (partial_a s) ad(T3)
```

on the real adjoint basis:

```text
['T1', 'T2', 'T3']
```

with

```text
ad(T3) = [[0, -1, 0], [1, 0, 0], [0, 0, 0]]
```

The shared central circle directions remain zero for this `eta_00` replay.

## Boundary

This is a straight rank-2-to-`End0` extraction, not a qutrit/sector promotion.
It does not yet emit the validator-ready finite derivative basis,
Riesz/Green operator, `dotD`, rank2-to-sector transfer, or off-diagonal control
certificate.

Status:

```text
SELECTED_END0_DE_DIAGONAL_PAYLOAD_BUILT_RIESZ_DOTD_TRANSFER_OPEN
```

Next:

```text
MTT_Selected_Riesz_Green_dotD_From_Diagonal_End0_DE_v1
```
