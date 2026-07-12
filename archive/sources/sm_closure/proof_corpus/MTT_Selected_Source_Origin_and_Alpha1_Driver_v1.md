# MTT Selected Source-Origin and Alpha1 Driver v1

## Result

The selected source-origin and alpha_1 driver problems reduce to one missing
object: `SelectedPhiFinAlpha1Payload`.

This is **superset repair with straight support**:

- Straight path: the fixed q79/F,m=1 S3/GS sector, Strominger selection support,
  projective gerbe source, and alpha_1 operator-level row are available.
- Superset convergence: S3/gerbe, visible Chern-Weil, Route-C, finite operator
  validators, and C1 response equations all point to the same selected payload.
- Superset repair: construct the selected `Phi_fin` alpha_1 payload, rather than
  adding separate knobs for source flags and alpha_1 flags.
- Diagnostic/backfit: not used as proof.

## Source-Origin Audit

Support already closed:

- `fixed_topological_sector_named`: `True`
- `mtt_strominger_selection_available`: `True`
- `same_source_support_converges`: `True`
- `s3_projective_gerbe_support_promoted`: `True`
- `visible_chern_weil_contract_reduced`: `True`

Selected flags still missing:

- `selected_by_mtt`: `False`
- `visible_bundle_or_twisted_gerbe_source`: `False`
- `pic0_selected_or_quotiented`: `False`
- `selection_justified_by_source`: `False`
- `same_branch_derivative_verified`: `False`
- `selected_D_E_source_flags`: `False`
- `selected_Green_source_flags`: `False`
- `selected_dotD_source_flags`: `False`

Finite `Phi_fin` shape gates:

- `de_riesz_green_dotd_shapes_present`: `True`
- `positive_gap_fields_present`: `True`
- `residual_codomain_shape_present`: `True`
- `sector_slots_present`: `True`

Selected `Phi_fin` payload flags:

- `de_action`: `False`
- `dotd_alpha1`: `False`
- `dotd_response`: `False`
- `reduced_green`: `False`
- `rhoE_mesh`: `False`
- `riesz_gap`: `False`
- `route_c_residual`: `False`

## Alpha1 Audit

Operator-level support:

- `selected_driver_alpha1_row`: `True`
- `selected_Xi_operator_level_source`: `True`
- `Hess_Xi_principal_symbol_blocks`: `True`
- `single_driver_not_algebraically_fatal`: `True`
- `rank_lift_criterion_known`: `True`

Selected values still missing:

- `evaluated_grad_V_C1_alpha1_source_vector`: `False`
- `full_lower_order_Hess_Xi_blocks`: `False`
- `deltaTheta_C1_solution`: `False`
- `sector_dotD_Q_u_d_L_e_N_H`: `False`
- `zero_mode_bases`: `False`
- `primitive_contractions`: `False`
- `response_matrices`: `False`

Rank lift condition:

```text
C33(M_C1^(alpha1)) != 0
```

## Unified Payload Contract

Domain:

```text
selected MTT Strominger/HYM minimizer in fixed q79/F,m=1 S3/GS sector
```

Codomain:

```text
rho_E transition data, Hermitian metric, sector projectors, D_E action slots for Q,u,d,L,e,N,H, Riesz projectors, complement gaps, reduced Green operators, dotD_alpha1 matrices and horizontal responses, primitive C1 overlap tensors
```

It must emit:

- non-identity selected rho_E/connection transition data
- selected Hermitian metric and sector projectors
- selected D_E action slots with selected_source_verified true
- selected Riesz projector, complement gap, and reduced Green
- selected dotD_alpha1 as the same-branch derivative of selected D_E
- finite Hessian/C1 source vector and lower-order Hessian blocks
- deltaTheta_C1, sector dotD slots, zero-mode bases, and primitive C1 contractions

Acceptance:

- all existing Phi_fin shape gates remain true
- all selected_payload_flags become true by construction, not by lifted flags
- source_origin_selected_flags all become true
- alpha1_selected_values all become true
- q79/q369 branch choice is source-selected or antiunitary-equivalent with retarded selector
- no observed masses, CKM phase, or benchmark entries are used as inputs

## What This Closes

- `source_origin_support_not_the_blocker`
- `Phi_fin_codomain_shape_already_built`
- `ordinary_rhoE_retired_projective_gerbe_route_live`
- `alpha1_driver_row_and_operator_level_source_imported`
- `single_alpha1_driver_can_lift_rank_if_C33_nonzero`
- `source_and_alpha1_reduced_to_one_payload`
- `target_fitting_excluded_from_promotion`

## What Remains Open

- `selected_PhiFin_alpha1_payload`
- `selected_nonidentity_rhoE_connection_values`
- `source_origin_selected_flags`
- `same_branch_dotD_alpha1_derivative`
- `finite_C1_source_vector_and_Hessian_blocks`
- `deltaTheta_C1_and_sector_dotD`
- `zero_mode_bases_and_primitive_contractions`
- `branch_selection_or_antiunitary_retarded_selector`
- `full_SM_or_no_knob_closure`

## Theorem

`SelectedSourceOriginAndAlpha1DriverReduction` is proved:

Given the current corpus and repo certificates, the selected source-origin blocker and the alpha1-driver blocker reduce to the same object: a selected Phi_fin alpha1 payload emitted from the q79/F,m=1 S3/GS Strominger/HYM branch. The artifact proves this reduction and the exact acceptance contract; it does not compute the selected payload values.

Next artifact: `MTT_Selected_PhiFin_Alpha1_Payload_v1`.
