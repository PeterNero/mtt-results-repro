# dotD alpha1 TransportDerivative Import v1

## Result

The dynamic transport formula is now imported:

```text
U = exp(-u ad(T3))
dU/dalpha = -(du/dalpha) ad(T3) U
dotD_h = (dh) ad(T3)
delta psi = -(h ad(T3)) psi_sel
D_sel(delta psi) + dotD_h psi_sel = 0
```

So the dotD source algebra is closed. The finite dotD matrices pass once the
alpha1 driver flag is theorem-derived. They still cannot be promoted by lifted
flags or coordinate convention.

Status:

```text
DOTD_ALPHA1_TRANSPORT_DERIVATIVE_IMPORTED_DRIVER_NORMALIZATION_OPEN
```

Remaining gate:

```text
same-branch source-strength normalization identifying h_ext with physical alpha1
```

Next:

```text
MTT_Selected_Alpha1_SourceStrength_Normalization_or_Driver_Theorem_v1
```
