# RouteC Source Map Selection Boundary Import v1

Status: `ROUTEC_SOURCE_MAP_SELECTION_BOUNDARY_IMPORTED_DYNAMIC_APPLICATION_OPEN`.

The source-map selection boundary is now sharp.  Static terminal support,
`R_Z/R_X` residual shapes, canonical `Q_residual`, and the strict 72-real target
are closed.  Dynamic application is still open:

```text
phase R_Z selected now = False
shift R_X selected now = False
b source emitted now = False
physical projector application promoted now = False
```

If those antecedents are supplied, the replay remains exact:

```text
A^T A = [[12.0, 0.0], [0.0, 12.0]]
A^T b = [12.0, 12.0]
deltaTheta_C1 = [1.0, 1.0]
```

This is not source-map selection.  The next proof must derive differentiated
`Phi_fin^C1` application of `Q_residual` plus `b_selected`, or run honest
selected Galerkin C1 values.

Next artifact: `MTT_Selected_DifferentiatedPhiFinC1ResidualProjectorAxiom_or_GalerkinC1Execution_v1`.
