# Route-C Source Selector and Basis Cutset Import v1

Status: `IMPORTED_CUTSET_SELECTOR_OPEN`.

This imports the current sibling-repo frontier for the selected Route-C/Strominger Galerkin run.

## Result

The first-run finite matrices are not the blocker.  The honest root manifest and the formal-lift diagnostic manifest have identical finite matrices; their only differences are provenance flags:

- `selected_source_verified`
- `selected_dotD_source_verified`
- `alpha1_driver_verified`

The imported theorem reports `36` total root/formal differences, all false-to-true changes of those flags.  The formal-lift lower validators pass, and the formal-lift `de_response` promotion gate passes.  This is conditional support only: lifted flags are not proof data.

## Locked Conditions

`C1_source_selector_condition` must derive the selected-source and alpha1-driver flags from MTT, not assert them.

`C2_basis_condition` must emit a quotient/deck-valid Galerkin basis `B_N`, quadrature, Gram/stiffness entries, bundle transition/equivariance matrices, and selected `D_E` action on that basis.

## Consequence

The proof frontier is now narrower than "find matrices": derive source provenance and a valid selected basis for the already-tested Route-C matrix pipeline.  Until those two objects are supplied, the pipeline remains a powerful diagnostic rather than full SM closure.

Next artifact: `MTT_Selected_RouteC_Source_Provenance_or_Basis_Certificate_v1`.
