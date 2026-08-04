# MTT Selected PiCKMNumeratorBranchRetentionPrinciple or WeightRows v1

Status: `MTT_SELECTED_PICKM_NUMERATOR_BRANCH_RETENTION_PROVED_WEIGHT_ROWS_EMITTED_EXACT_CKM_OPEN`.

## Theorem

`PiCKMFiniteBranchRetentionTheorem` is proved.

The selected finite quotient branch-retention census promotes the previous
Pi_CKM trace-law candidate to selected row certificates:

```text
Pi_CKM^12: W12 = (||R_Z||_F^2 + 5 sin(delta_79))/6
Pi_CKM^23: W23 = (sqrt(3) + 3 q |cos(delta_79)|/2)/8
Pi_CKM^13: W13 = (5q + 3(448/64))/18
```

Numerically:

```text
W12 = 1.4123293778994717
W23 = 6.829942647321135
W13 = 23.11111111111111
```

Accepted selected Pi_CKM weight rows are now `3/3`.

This is not exact CKM magnitude closure. The selected rows are source-owned,
but the frozen replay residual remains nonzero:

```text
max relative angle residual  = 6.58769785126031e-06
max relative weight residual = 0.00013430483769361892
```

No observed CKM magnitude, Wolfenstein parameter, or measured replay weight is
used as a source selector.

Next artifact: `MTT_Selected_PiCKMWeightRows_CKMResidualDecision_or_HigherOrderClosure_v1`.
