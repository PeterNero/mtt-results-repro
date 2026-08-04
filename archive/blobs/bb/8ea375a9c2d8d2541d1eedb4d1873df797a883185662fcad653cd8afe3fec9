# DifferentiatedPhiFinC1 PrimitiveOverlapContractions or GalerkinRun Import v1

Status: `DIFFERENTIATED_PHIFINC1_PRIMITIVE_OVERLAP_IMPORTED_TRANSPORT_NOGO_TEMPLATE_OPEN`.

## Closed

The selected alpha1/dotD driver is attached to the differentiated `Phi_fin^C1`
contract.  The canonical transport-only lane is rejected: pure stationary
transport with the canonical mode-conserving primitive tensor emits zero C1
matrices in all four sectors, so it cannot produce the phase/shift columns.

## Template

The primitive-overlap template is imported at:

```text
candidate_data\differentiated_phifinc1_primitiveoverlap_or_galerkinrun_import\primitive_overlap_contractions.template.json
```

It keeps the primitive three-by-three contractions, linear response matrices,
Hessian counterterms, `A_selected`, `b_selected`, and `deltaTheta_C1` empty until
a selected primitive vertex / basis-transport source theorem or an honest
selected Galerkin C1 run fills them.

## Conditional Values

The normal-form values remain diagnostic only:

```text
A^T A = [[12.0, 0.0], [0.0, 12.0]]
A^T b = [12.0, 12.0]
deltaTheta_C1 = [1.0, 1.0]
```

No observed masses, mixings, CP phase, benchmark matrices, or target residuals
are used as selectors.

Next artifact: `MTT_Selected_PrimitiveVertexSource_or_BasisTransport_SelectionTheorem_v1`.
