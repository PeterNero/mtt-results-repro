# RouteC R1 R4 FillAttempt Import v1

Status: `ROUTEC_R1_R4_FILL_ATTEMPT_IMPORTED_PRIMITIVE_SEARCH_OPEN`.

The R1 and R4 fills were attempted strictly:

- R1 source-certificate support is present, but selected `Phi_fin` values,
  selected minimizer identity, and selected HYM/operator source values are not
  emitted.
- R4 basis support is present, but selected scalar basis functions, deck/cover,
  bundle equivariance, quadrature, and selected `D_E` action are not emitted.

Honest replay remains blocked.  The next move is selected primitive emission
search, not a replay or lifted-flag promotion.

Next artifact: `MTT_Selected_RouteC_Selected_Primitive_Emission_Search_v1`.
