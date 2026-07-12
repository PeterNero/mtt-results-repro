# MTT Selected MagProfileValueFunctional or OfficialFullProfileWorkspace v1

Status: `MTT_SELECTED_MAGPROFILEVALUEFUNCTIONAL_OR_OFFICIALFULLPROFILEWORKSPACE_BUILT_TEN_VALUE_PAYLOAD_ROWS_CLOSED_PRECISION_OPEN`

## Result

The `M_magprofile` value-payload layer now splits into two accepted blocks at
the current one-shared-physical-primitive/profile standard:

- charged block: `9/9` finite-replay Yukawa magnitude rows,
- H/lambda block: `1/1` strict direct `K_threshold.Omega_H.lambda` row.

So the ten value-payload rows are closed at the split profile tier.

This does not reopen Yukawa magnitudes.  The charged rows import the locked
finite-replay result with max log residual
`8.715792346058762e-14`.

The H/lambda row imports the strict direct-K row:

`K_threshold.Omega_H.lambda = (A_EW(mu_match) * s_beta) / (D_fin.H * epsilon_Theta^(1/3))`.

## Boundary

This is not full true-precision equivalence.  The direct-K lambda coordinate
and the common-scale lambda profile coordinate live in declared scheme/profile
coordinates.  A true precision claim still needs either a full covariance
profile likelihood/workspace or internally selected threshold/mass-scheme
transport into one common scheme.

Next required artifact:
`MTT_Selected_PrecisionLayerFullCovarianceOrInternalTransport_v1`.
