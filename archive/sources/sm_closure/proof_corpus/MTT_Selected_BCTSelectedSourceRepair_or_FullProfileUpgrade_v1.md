# MTT Selected BCTSelectedSourceRepair or FullProfileUpgrade v1

Status: `MTT_SELECTED_BCTSELECTEDSOURCEREPAIR_OR_FULLPROFILEUPGRADE_BUILT_PROFILE_UPGRADED_SOURCE_REPAIR_BLOCKED`.

This is the non-looping follow-up to the BCT dual-lane attempt.

```text
BCT selected-source rows promoted       : 0
BCT empirical profile 95 percent closed : true
W/Z/H external coordinate rows imported : 5
external profile coordinates upgraded   : 8
full covariance / true SM closure        : false
```

The selected-source repair lane is not repeated unless
`SelectedRouteCStromingerGalerkinResidualSolve` changes.  The forward lane is
now the external profile layer: BCT empirical profile plus W/Z/H external
coordinates, still guarded as downstream validation data rather than selected
source data.

Next artifact: `MTT_Selected_ExternalProfileToFullCovarianceBridge_or_SelectedSourceRows_v1`.
