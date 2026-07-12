# RouteC Strominger Execution Plan Import v1

Status: `ROUTEC_STROMINGER_EXECUTION_PLAN_IMPORTED_C1_FILL_OR_QUADRATURE_ROWS_OPEN`.

The Strominger/HYM C1 gate is now executable, but not closed.

Route A first-variation fields still required:

```text
['selected_trace_map', 'first_variation_identity', 'hessian_or_coercivity', 'boundary_cancellation', 'normalization_compatibility']
```

Route B quadrature rows still required:

```text
{'zero_mode_basis_rows': 19, 'primitive_contraction_rows': 72, 'hessian_source_rows': 2, 'sector_matrix_rows': 36}
```

Execution order:

```text
['basis', 'primitive_contractions', 'hessian_source', 'sector_matrices']
```

Locked replay target remains:

```text
A^T A = [[12.0, 0.0], [0.0, 12.0]]
A^T b = [12.0, 12.0]
deltaTheta_C1 = [1.0, 1.0]
```

Next artifact: `MTT_Selected_C1FirstVariationCertificateFill_or_QuadratureRowsFirstRun_v1`.
