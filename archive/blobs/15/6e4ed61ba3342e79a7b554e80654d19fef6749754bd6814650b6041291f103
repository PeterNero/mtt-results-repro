# MTT Selected PiCKMWeightRows CKMResidualDecision or HigherOrderClosure v1

Status: `MTT_SELECTED_PICKM_WEIGHT_ROWS_RESIDUAL_CAUSE_AUDITED_HIGHERORDER_OR_PROFILE_OPEN`.

## Theorem

`PiCKMWeightRowsResidualCauseAuditTheorem` is proved.

The selected Pi_CKM rows remain accepted at `3/3`, but exact central CKM replay
is not closed. The residual is audited rather than hand-waved:

```text
max relative angle residual  = 6.58769785126031e-06
max relative weight residual = 0.00013430483769361892
```

Ruled out:

```text
roundoff
one global normalization factor
one q/phase relabel
integer denominator error in 6/8/18
target-fitted row acceptance
```

Effective q values if each row is forced to match the frozen central replay:

```text
W12 q_eff = 79.00727703630918
W23 q_eff = 79.00096003264522
W13 q_eff = 78.98882733804643
```

These disagree by row, so the residual is sector-pair specific.

The local CKM packet has no full covariance/profile likelihood, but a diagonal
uncertainty estimate places all three selected predictions far below one
standard deviation from the frozen central replay. This means the selected rows
are empirically admissible at the current packet precision, while exact/no-knob
central-value closure remains open.

Next legal exits:

```text
1. selected higher-order sector-pair correction Delta W_ij
2. selected convention/normalization theorem changing the replay map
3. covariance/profile likelihood audit for the selected Pi_CKM prediction
```

Next artifact: `MTT_Selected_CKMCovarianceProfileOrHigherOrderResidualClosure_v1`.
