# MTT Selected StaticCoefficientTransferMap or CPOrientationFrontier v1

Status: `MTT_SELECTED_STATIC_COEFFICIENT_TRANSFER_MAP_BUILT_MIXED_REJECTED_CP_ORIENTATION_FRONTIER_OPEN`.

The old source-to-C1 transfer was exact but conditional, because the sector route
and normalization were not independently selected.  Later artifacts now close the
static SM-slot source tier:

```text
all six SM-slot source arrows       : true
static route                        : Z -> u,e ; X -> d,nuD
same-source consistency             : true
static trace/transfer normalization : true
dynamic C1/A_selected promotion     : false
```

Therefore the static coefficient transfer map is:

```text
lambda_Z = lambda_X = lambda_static
u,e      <- (I + Z) + lambda_static Z
d,nuD   <- (I + X) + lambda_static X
```

This rejects the two mixed branches at the static coefficient tier.  The four
algebraic branches are reduced to two selected-static-compatible branches:

```text
surviving lambdas                  : ['1+omega', '1+omega2']
rejected mixed branch count         : 2
surviving CP orientations           : ['positive']
selected physical matrices promoted : false
full SM closure                     : false
```

So the remaining wall has moved again: the mixed branches are gone, but MTT
still must select or explain coexistence of the conjugate `lambda_static`
branches, then promote dynamic physical matrices before CKM/PMNS/Yukawa values
can be claimed.

Next artifact: `MTT_Selected_CPOrientation_or_DynamicPhysicalMatrixPromotion_v1`.
