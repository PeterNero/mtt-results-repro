# Selected alpha1 Tangent or Retarded Overlap Kernel Construct v1

## Result

The finite alpha1 tangent kernel is now constructed:

```text
h = h_ext
dotD_h = (dh) ad(T3)
delta psi = -(h ad(T3)) psi_sel
D_sel(delta psi) + dotD_h psi_sel = 0
```

The canonical L2 dual normalization is also constructed:

```text
N_alpha1(f) = <f,h_ext> / ||h_ext||_L2^2
N_alpha1(h_ext) = 1
lambda_alpha1 candidate = 1
```

So the algebraic tangent and the unique current unit candidate are nailed down.

## Boundary

This is not yet the selected physical alpha1 driver. The same-source branch has
not emitted the normalization functional or source-strength coordinate as a
selected object, and the honest dotD replay still fails by
`alpha1_driver_verified`.

Status:

```text
SELECTED_ALPHA1_TANGENT_KERNEL_CONSTRUCTED_SELECTION_NORMALIZATION_OPEN
```

Next:

```text
MTT_Selected_SameSource_Alpha1_Normalization_Packet_Fill_v1
```
