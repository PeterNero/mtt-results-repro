# RouteC Smooth BN Galerkin Lift Import v1

Status: `ROUTEC_SMOOTH_BN_GALERKIN_LIFT_IMPORTED_SELECTED_DE_OPEN`.

The Route-C branch now imports the smooth `B_N` Galerkin scaffold.  The lift has
dimension `27`, `9` metric
quadrature nodes, a three-dimensional model-active kernel, and positive
complement gap `4.38649084493`.  The model-active
Gram/stiffness, Riesz projector, and reduced Green data are emitted.

This is not a full straight proof.  The imported object is projectively
equivariant rather than ordinarily equivariant, and it remains a model-active
Galerkin scaffold until the selected `D_E` action on the same basis, sector
projectors, `dotD_alpha1` response, and full Iwasawa truncation-error certificate
are supplied.

Next artifact: `MTT_Selected_RouteC_DE_Action_on_Smooth_BN_v1`.
