# MTT Selected Route-C/Strominger Galerkin Solve Spec v1

## Result

The selected Route-C/Strominger Galerkin solve is now an executable spec, not a
loose wish.

This is **superset repair executable spec**:

- Straight path: scaffold only; selected values remain open.
- Superset convergence: Route-C residuals, Galerkin basis protocol,
  rho_E/D_E/Riesz/Green/dotD validators, and C1 response all lock one target.
- Superset repair: run or symbolically fill the first selected small-N solve.
- Diagnostic/backfit: not used as proof.

## Mesh Scaffold

- `boundary_face_incidences`: `192`
- `closed_cell_nodes`: `64`
- `complex_rho_entries_table_ansatz`: `1296`
- `corner_nodes_with_multiple_boundary_faces`: `57`
- `mesh_N`: `1`
- `metric_real_entries_full_node_table`: `576`
- `rank3_bundle_dofs_identity_smoke`: `3`
- `scalar_quotient_dofs_identity_smoke`: `1`
- `unique_rho_boundary_matrices_table_ansatz`: `144`

Matches q79 scaffold certificate: `True`.

## Residual Acceptance

- pass rule: Every residual value must be present and <= its tolerance; all positive gates must exceed strict lower bounds.
- selected source rule: selected_source_verified must be true because the residual solve, not the target data, selects the branch.

## Spectral Acceptance

- cluster rule: lambda_1 <= lambda_2 <= lambda_3 <= epsilon_low
- gap rule: lambda_4 >= gamma_gap
- error budget: eta_total = eta_basis + eta_operator_residual + eta_quadrature + eta_HYM
- pass rule: epsilon_low + eta_total < tau < gamma_gap - eta_total for some tau > 0
- consequence: the Riesz projector below tau has rank three and is stable under the certified errors
- basis minimum: The solve must use a quotient-valid basis beyond the left-invariant scalar_count=1 smoke sector.

## Execution Stages

### S0_selected_source
Must emit:
- source_selected_by_mtt
- fixed q79/F,m=1 S3/GS branch
- no measured-data selector
Validator: `validate_iwasawa_route_c_residuals.py`

### S1_basis_and_domain
Must emit:
- basis_B_N
- deck/periodic constraints
- bundle transition/equivariance matrices
- metric quadrature
Validator: `iwasawa_spectral_galerkin_data.template.json success_gates`

### S2_connection_metric_rhoE
Must emit:
- A*
- h*
- projective/twisted rho_E induced by selected source
Validator: `validate_iwasawa_rhoE_mesh.py, validate_iwasawa_rhoE_metric.py`

### S3_sector_operators
Must emit:
- sector projectors
- D_E action for Q,u,d,L,e,N,H
Validator: `validate_iwasawa_sector_maps.py, validate_iwasawa_de_action.py`

### S4_spectral_projectors
Must emit:
- Riesz projectors
- complement gaps
- reduced Green operators
- truncation error bounds
Validator: `validate_iwasawa_riesz_gap.py, validate_iwasawa_reduced_green.py`

### S5_alpha1_response
Must emit:
- deltaTheta_C1
- same-branch dotD_alpha1
- horizontal zero-mode responses
Validator: `validate_iwasawa_dotd_response.py`

### S6_c1_contractions
Must emit:
- zero-mode bases
- primitive 3x3 contraction terms
- response matrices and C33 tests
Validator: `selected_c1_primitive_contractions.template.json fill contract`

## Output Manifest

- `route_c_residual`: `candidate_data/selected_routec_strominger_galerkin_solve/route_c_residual.candidate.json`
- `rhoE_mesh`: `candidate_data/selected_routec_strominger_galerkin_solve/rhoE_mesh.candidate.json`
- `rhoE_metric`: `candidate_data/selected_routec_strominger_galerkin_solve/rhoE_metric.candidate.json`
- `sector_maps`: `candidate_data/selected_routec_strominger_galerkin_solve/sector_maps.candidate.json`
- `de_action`: `candidate_data/selected_routec_strominger_galerkin_solve/de_action.candidate.json`
- `riesz_gap`: `candidate_data/selected_routec_strominger_galerkin_solve/riesz_gap.candidate.json`
- `reduced_green`: `candidate_data/selected_routec_strominger_galerkin_solve/reduced_green.candidate.json`
- `dotd_response`: `candidate_data/selected_routec_strominger_galerkin_solve/dotd_response.candidate.json`
- `spectral_galerkin_data`: `candidate_data/selected_routec_strominger_galerkin_solve/spectral_galerkin_data.candidate.json`
- `c1_primitive_contractions`: `candidate_data/selected_routec_strominger_galerkin_solve/c1_primitive_contractions.candidate.json`

## What This Closes

- `selected_solve_executable_spec_built`
- `mesh_N1_accounting_reproduced`
- `residual_acceptance_contract_built`
- `spectral_gap_error_contract_built`
- `output_manifest_built`
- `validator_order_locked`
- `promotion_guardrail_linked`
- `target_fitting_excluded`

## What Remains Open

- `actual_selected_small_N_solve_or_symbolic_ansatz`
- `selected_rhoE_metric_connection_values`
- `actual_basis_B_N_and_quadrature`
- `selected_DE_Riesz_Green_dotD_outputs`
- `spectral_gap_error_numbers`
- `zero_mode_bases_and_C1_primitives`
- `full_SM_or_no_knob_closure`

## Theorem

`SelectedRouteCStromingerGalerkinSolveSpecification` is proved:

The selected Route-C/Strominger Galerkin solve is now specified as an executable finite contract. It reuses the q79 finite residual scaffold, non-invariant Galerkin matrix protocol, downstream validators, Riesz gap/error rule, and C1 response contract. It does not compute selected values; the next step is to run or symbolically fill the first honest selected small-N solve.

Next artifact: `MTT_Selected_RouteC_Strominger_Galerkin_First_Run_v1`.
