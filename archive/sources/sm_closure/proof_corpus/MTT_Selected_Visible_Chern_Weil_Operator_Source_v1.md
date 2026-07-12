# MTT Selected Visible Chern-Weil Operator Source v1

## Result

The selected visible Chern-Weil/operator-source problem is reduced to one
same-source packet.  The source itself is not closed yet.

This is **superset convergence with repair**:

- Straight path: `STRAIGHT_PATH_RETIRED`.  Split line-bundle or diagonal
  Cartan HYM is ruled out for the positive visible `alpha_1` row.
- Superset convergence: `SUPERSET_CONVERGENCE_PRIMARY`.  The primary branch is
  `rank2_non_split_extension_preferred_L_1_-2_0` with source shape `0 -> L -> V_alpha -> L^-1 -> 0`.
- Superset repair: `SUPERSET_REPAIR_PARALLEL`.  Route-C finite
  HYM/Strominger remains legal if it emits the same selected operator payload.
- Superset support repair: `SUPERSET_REPAIR_SUPPORT`.  S3/gerbe
  projective support is closed at source-support level, but cannot promote by
  patchwork.
- Diagnostic/backfit: not used as proof.

## Closed Support

- `selected_s3_gerbe_source_level`
- `visible_green_schwarz_curvature_row_closed`
- `old_s3_fw_projector_blockers_retired`
- `stable_source_sign_convention_closed`
- `downstream_validator_stack_conditionally_sufficient`
- `selected_hym_operator_validator_formulated`

## Retired Or Demoted

- `split_line_or_diagonal_cartan_HYM_final_source`
- `abelian_row_retained_only_as_chern_bianchi_support`
- `positive_math_ch2_wording_rejected`
- `patchwork_constituent_proof_rejected`
- `lifted_flag_smoke_not_proof`

## Remaining Same-Source Cut Set

- `Chern_Weil_row_derived_from_selected_source`
- `HYM_or_Route_C_residual_for_visible_source`
- `coherent_spectral_zero_mode_projectors`
- `primitive_C1_contractions`
- `selected_D_E_dotD_Riesz_Green`
- `selected_visible_bundle_or_sheaf_model`

## Required Packet Fields

- `source_certificate`
- `selected_holomorphic_structure_for_L_squared`
- `finite_Cech_or_Dolbeault_cochain_packet`
- `nonzero_closed_nonexact_Ext_vector`
- `non_split_extension_and_stability_certificate`
- `Chern_Bianchi_Freed_Witten_packet_for_c2_4_alpha1`
- `HYM_or_Strominger_or_Route_C_residual_certificate`
- `same_source_D_E_operator_block`
- `same_source_dotD_alpha1_response`
- `Riesz_projector_and_reduced_Green_packet`
- `trace_action_normalization`
- `SM_sector_projector_retention`

## Hard Acceptance Tests

- H^1(X,L^2) validator exits 0 for selected data with h1>0
- the selected Ext vector is closed and not exact
- the extension is non-split and stable in the selected chamber
- Chern/Bianchi/Freed-Witten data realize c1=0,c2=+4 alpha_1 on the same source
- HYM/Strominger residual or Route-C finite residual is certified
- D_E, dotD_alpha1, Riesz projector, and Green operator are derived from the same source
- sector projectors and SM dictionary are recomputed or protected for the total source

## Theorem

`SelectedVisibleChernWeilOperatorSourceReduction` is proved:

After selected S3 gerbe/projector support and visible Green-Schwarz curvature closure, the visible Chern-Weil/operator-source frontier reduces to a single same-source packet. The straight split-line HYM/diagonal Cartan source is ruled out; the primary live branch is the non-split rank-two V_alpha extension with L=(1,-2,0), while Route-C finite HYM/Strominger remains the parallel repair path. The artifact does not prove the selected visible source itself; it proves the exact remaining contract.

## What This Closes

- `split_line_hym_route_retired_as_final_source`
- `stable_sign_convention_for_visible_row_closed`
- `primary_non_split_rank2_valpha_branch_identified`
- `route_c_parallel_repair_branch_preserved`
- `s3_gerbe_green_schwarz_support_consumed_without_patchwork_promotion`
- `downstream_validator_sufficiency_imported`
- `single_same_source_packet_contract_locked`

## What Remains Open

- `selected_nonzero_Ext_class`
- `Pic0_selection_or_physical_quotient`
- `non_split_stability_or_selected_HYM_residual`
- `same_source_Chern_Weil_row_derivation`
- `selected_D_E_dotD_Riesz_Green`
- `coherent_spectral_zero_mode_projectors`
- `primitive_C1_overlap_tensors`
- `selected_Qa_SU3_color_operator_packet`
- `full_SM_parity_closure`
- `no_knob_closure`

## Next Artifact

`MTT_Selected_NonSplit_Rank2_or_RouteC_SameSource_Packet_v1`
