# RouteC Primitive C1 Source Map Candidate Import v1

Status: `ROUTEC_PRIMITIVE_C1_SOURCE_MAP_CANDIDATE_IMPORTED_SELECTION_OPEN`.

The primitive C1 frontier is now explicit.  The imported candidate maps the
phase leg to `R_Z`, the shift leg to `R_X`, and uses canonical `Q_residual`
support of rank `6` in the `72`-real
coordinate target.

The conditional algebra is exact:

```text
||R_Z||^2 = 4.0
||R_X||^2 = 2.0
A^T A = [[12.0, 0.0], [0.0, 12.0]]
A^T b = [12.0, 12.0]
deltaTheta_C1 = [1.0, 1.0]
```

This is still a candidate, not selected-source closure.  `R_Z`, `R_X`,
`b_selected`, `A_selected`, sector response matrices, and honest Galerkin C1
values remain unpromoted.

Next artifact: `MTT_Selected_SourceMapSelectionTheorem_or_HonestGalerkinC1ValueRun_v1`.
