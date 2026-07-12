# RouteC Residual Projector Insertion Spec Import v1

Status: `ROUTEC_RESIDUAL_PROJECTOR_INSERTION_SPEC_IMPORTED_INPUTS_OPEN`.

The next Route-C fork is now imported as a reproducible checkpoint:

```text
Route A: residual-projector axiom appendix draft, not corpus-patched
Route B: honest Galerkin C1 first-execution spec, not run
```

Both lanes are locked to the same strict target:

```text
sectors = ['u', 'e', 'd', 'nuD']
total real coordinates = 72
conditional rank = 2
A^T A = [[12.0, 0.0], [0.0, 12.0]]
A^T b = [12.0, 12.0]
deltaTheta_C1 = [1.0, 1.0]
```

The required Galerkin input packets are:

- `hessian_or_source_vector_packet`: `candidate_data/selected_residualprojectoraxiominsertion_or_galerkinc1firstexecution/inputs/hessian_source_vector.packet.json`
- `primitive_contraction_terms_packet`: `candidate_data/selected_residualprojectoraxiominsertion_or_galerkinc1firstexecution/inputs/primitive_contraction_terms.packet.json`
- `sector_response_matrix_packet`: `candidate_data/selected_residualprojectoraxiominsertion_or_galerkinc1firstexecution/inputs/sector_response_matrices.packet.json`
- `zero_mode_basis_packet`: `candidate_data/selected_residualprojectoraxiominsertion_or_galerkinc1firstexecution/inputs/zero_mode_basis.packet.json`

Nothing is promoted yet: no main-corpus axiom patch, no selected Galerkin run,
no `A_selected`, no `b_selected`, no `deltaTheta_C1`, and no SM dynamic closure.

Next artifact: `MTT_Selected_GalerkinC1InputBasisFill_or_ResidualProjectorAxiomCorpusPatch_v1`.
