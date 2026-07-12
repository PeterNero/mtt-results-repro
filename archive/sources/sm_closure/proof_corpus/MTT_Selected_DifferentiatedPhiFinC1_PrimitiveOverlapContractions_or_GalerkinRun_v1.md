# MTT Selected DifferentiatedPhiFinC1 PrimitiveOverlapContractions or GalerkinRun v1

Status: `MTT_SELECTED_DIFFERENTIATED_PHIFINC1_PRIMITIVEOVERLAP_OR_GALERKINRUN_BUILT_TRANSPORT_ONLY_NOGO_TEMPLATE_OPEN`.

This artifact attaches the theorem-derived alpha1/dotD driver to the
differentiated `Phi_fin^C1` contract, then proves the transport-only lane is
not enough.

Closed now:

```text
dU/dalpha = -(du/dalpha) ad(T3) U
selected_dotD_source_verified = true
alpha1_driver_verified        = true
canonical mode-conserving C1 response = 0 in u,d,e,nuD
```

The nonzero finite primitive candidates are imported only as unselected support:
active shift `(1,1)`, fixed fiber shifts `[0, 1, 2]`,
rank-three fixed-fiber matrices, and rank-one all-fiber envelope.

The emitted template is:

```text
candidate_data/selected_differentiated_phifinc1_primitiveoverlap_or_galerkinrun/primitive_overlap_contractions.template.json
```

It must be filled by a selected primitive vertex / basis-transport source
theorem or by an honest selected Galerkin C1 run.  Until then, the conditional
normal-form values remain unpromoted:

```text
A^T A         = [[12.0, 0.0], [0.0, 12.0]]
A^T b         = [12.0, 12.0]
deltaTheta_C1 = [1.0, 1.0]
```

No observed masses, mixings, CP phase, benchmark matrices, or target residuals
are used as selectors.

Next artifact: `MTT_Selected_PrimitiveVertexSource_or_BasisTransport_SelectionTheorem_v1`.
