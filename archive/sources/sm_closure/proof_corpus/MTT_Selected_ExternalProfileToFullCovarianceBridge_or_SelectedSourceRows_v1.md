# MTT Selected ExternalProfileToFullCovarianceBridge or SelectedSourceRows v1

Status: `MTT_SELECTED_EXTERNALPROFILETOFULLCOVARIANCEBRIDGE_OR_SELECTEDSOURCEROWS_BUILT_8X8_COVARIANCE_TARGET_SELECTED_ROWS_OPEN`.

The external profile layer now has a fixed covariance target.

```text
external coordinates              : 8
full covariance shape             : 8 x 8
symmetric covariance entries       : 36
BCT empirical block entries        : 6
W/Z/H surrogate block entries      : 15
BCT-W/Z/H cross entries missing    : 15
selected source rows closed        : false
```

This moves the frontier from "need full profile" to a precise object:
import/reconstruct the eight-coordinate profile likelihood or replace the
external coordinates with selected source rows from Route-C/no-knob derivation.

Next artifact: `MTT_Selected_PublishedCovarianceLikelihoodImport_or_RouteCSelectedSourceEmission_v1`.
