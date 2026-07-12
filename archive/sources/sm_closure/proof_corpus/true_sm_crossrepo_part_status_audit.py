from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "candidate_data" / "true_sm_crossrepo_part_status_audit.candidate.json"
BUILDER = ROOT / "scripts" / "build_true_sm_crossrepo_part_status.py"


def main() -> None:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)
    data = json.loads(PACKET.read_text(encoding="utf-8"))
    parts = {part["part"]: part for part in data["parts"]}

    assert data["guardrails"]["observed_sm_values_used"] is False
    assert data["guardrails"]["benchmark_rows_promoted_to_proof"] is False
    assert data["guardrails"]["stale_open_packets_allowed_to_override_later_closure"] is False

    alpha = parts["alpha1/dotD driver and honest dotD replay"]
    assert alpha["status"] == "CLOSED_SELECTED_IN_ACTIVE_LEDGER"
    active_alpha_evidence = alpha["evidence"][0]
    assert active_alpha_evidence["alpha1_dotD_driver_imported"] is True
    assert active_alpha_evidence["honest_dotD_replay_imported"] is True
    qa_alpha_evidence = alpha["evidence"][1]
    assert qa_alpha_evidence["alpha1_driver_verified"] is True
    assert qa_alpha_evidence["selected_dotD_source_verified"] is True
    assert qa_alpha_evidence["honest_dotD_validator_closed"] is True

    matter = parts["Matter-slot orientation and U10/Ubar5/1M operator blocks"]
    assert matter["status"] == "CLOSED_SELECTED_IN_ACTIVE_LEDGER"
    matter_evidence = matter["evidence"][0]
    assert matter_evidence["matter_slot_orientation_imported"] is True
    assert matter_evidence["operator_blocks_imported"] is True
    assert matter_evidence["overlap_normalization_imported"] is True

    primitive = parts["Primitive C1 atom table for u,d,e,nuD"]
    assert primitive["status"] == "CLOSED_SELECTED_FIRST_RESPONSE_LAYER_IN_ACTIVE_LEDGER"
    step24_evidence = primitive["evidence"][0]
    assert step24_evidence["selected_dynamic_overlap_tensor_or_transfer_functor"] is True
    assert step24_evidence["selected_primitive_C1_contractions_first_response_layer"] is True
    assert step24_evidence["selected_b_selected_promoted"] is True
    assert step24_evidence["selected_Hessian_source_normalization_promoted"] is True
    assert step24_evidence["accepted_value_functional_rows_closed"] is False
    dynamic_evidence = primitive["evidence"][1]
    assert dynamic_evidence["selected_dynamic_overlap_tensor_promoted"] is True
    assert dynamic_evidence["primitive_C1_contractions_selected_emitted_first_response_layer"] is True
    step23_evidence = primitive["evidence"][2]
    assert step23_evidence["phase_Z_routed_to_u_e_column"] is True
    assert step23_evidence["shift_X_routed_to_d_nuD_column"] is True
    assert step23_evidence["selected_dynamic_overlap_tensor_or_transfer_functor"] is False
    step22_evidence = primitive["evidence"][3]
    assert step22_evidence["selected_source_to_C1_transfer_map_emitted"] is False
    assert step22_evidence["selected_A_selected_promoted"] is False
    assert step22_evidence["blocking_clause_count"] > 0
    step21_evidence = primitive["evidence"][4]
    assert step21_evidence["conditional_decomposition_reconstructs_aggregate"] is True
    assert step21_evidence["selected_vertex_source_theorem_proved"] is False
    assert step21_evidence["selected_replacement_sixterm_decomposition_emitted"] is False
    step20_evidence = primitive["evidence"][5]
    assert step20_evidence["conditional_payload_built"] is True
    assert step20_evidence["conditional_normal_form_validated"] is True
    assert step20_evidence["selected_source_theorem_for_conditional_payload"] is False
    assert step20_evidence["six_term_primitive_atom_decomposition_emitted"] is False
    step19_evidence = primitive["evidence"][6]
    assert step19_evidence["primitive_C1_atom_assembly_schema_closed"] is True
    assert step19_evidence["current_corpus_payload_fill_nogo_closed"] is True
    assert step19_evidence["missing_leaf_count"] == 40
    qa_primitive_evidence = primitive["evidence"][7]
    assert qa_primitive_evidence["missing_atom_count"] == 24
    assert qa_primitive_evidence["primitive_C1_contractions_closed"] is False
    assert qa_primitive_evidence["superseded_by_active_step24_for_first_response_layer"] is True

    matrices = parts["A_selected and b_selected finite value matrices"]
    assert matrices["status"] == "CLOSED_SELECTED_IN_ACTIVE_LEDGER"
    assert matrices["evidence"][0]["selected_A_selected_promoted"] is True
    assert matrices["evidence"][0]["selected_b_selected_promoted"] is True
    assert matrices["evidence"][0]["selected_deltaTheta_C1_promoted"] is True
    assert matrices["evidence"][0]["selected_Hessian_source_normalization_promoted"] is True
    assert matrices["evidence"][1]["A_selected_emitted"] is False
    assert matrices["evidence"][1]["b_selected_emitted"] is False
    assert matrices["evidence"][1]["superseded_by_active_step24"] is True

    rtheta = parts["R_theta internal scalar rows / no-knob numerical rows"]
    assert rtheta["status"] == "OPEN_VALUE_FUNCTIONAL"
    evidence = {item["path"]: item for item in rtheta["evidence"]}

    step42 = evidence["candidate_data/selected_step42_executable_value_replay_solution_or_noknobrowfrontier.candidate.json"]
    assert step42["executable_admitted_replay_value_solution_closed"] is True
    assert step42["Step41_source_branch_attached_to_value_rows"] is True
    assert step42["versioned_common_scale_Yu_Yd_Ye_lambdaH_rows_emitted"] is True
    assert step42["admitted_external_threshold_rows_closed"] is True
    assert step42["admitted_external_threshold_row_count"] == 7
    assert step42["admitted_external_mass_scheme_rows_closed"] is True
    assert step42["admitted_external_mass_scheme_row_count"] == 3
    assert step42["diagonal_profile_replay_tier_closed"] is True
    assert step42["Pi_Rtheta_closed"] is True
    assert step42["Rtheta_readiness_8_of_9"] is True
    assert step42["accepted_for_true_precision_equivalence"] is False
    assert step42["accepted_as_no_knob_MTT_prediction"] is False
    assert step42["accepted_internal_scalar_row_count"] == 0
    assert step42["accepted_coefficient_value_count"] == 0
    assert step42["true_SM_equivalence_closed"] is False
    assert step42["full_no_knob_closed"] is False

    step41 = evidence["candidate_data/selected_step41_singlebranch_solution_assembly_or_valuefunctionalfrontier.candidate.json"]
    assert step41["single_branch_first_response_solution_assembled"] is True
    assert step41["selected_q79_F_m1_branch_fixed"] is True
    assert step41["primitive_C1_first_response_layer_closed"] is True
    assert step41["selected_A_selected_promoted"] is True
    assert step41["selected_b_selected_promoted"] is True
    assert step41["selected_deltaTheta_C1_promoted"] is True
    assert step41["selected_dynamic_overlap_tensor_closed"] is True
    assert step41["selected_source_to_C1_transfer_map_closed"] is True
    assert step41["selected_Rtheta_scalar_value_functional_source_domain_closed"] is True
    assert step41["accepted_internal_scalar_row_count"] == 0
    assert step41["accepted_value_functional_rows_closed"] is False
    assert step41["accepted_Yukawa_magnitudes_closed"] is False
    assert step41["CKM_PMNS_measured_value_closure_closed"] is False
    assert step41["lambda_H_row_emitted"] is False
    assert step41["true_SM_equivalence_closed"] is False
    assert step41["full_no_knob_closed"] is False

    step40 = evidence["candidate_data/selected_step40_dotdtransport_alpha1import_or_primitivec1frontier.candidate.json"]
    assert step40["selected_dotD_transport_derivative_formula_closed"] is True
    assert step40["selected_alpha1_driver_normalization_closed"] is True
    assert step40["same_branch_dotD_alpha1_values_closed"] is True
    assert step40["honest_dotD_alpha1_replay_closed"] is True
    assert step40["primitive_C1_contractions_from_operator_values_closed"] is False
    assert step40["selected_A_selected_closed"] is False
    assert step40["selected_b_selected_closed"] is False
    assert step40["accepted_internal_scalar_row_count"] == 0

    step39 = evidence["candidate_data/selected_step39_diagonalend0_covariantde_import_or_fullsectorfrontier.candidate.json"]
    assert step39["selected_diagonal_End0_covariant_D_E_closed"] is True
    assert step39["selected_stationary_projector_Riesz_Green_transport_closed"] is True
    assert step39["selected_full_sector_covariant_D_E_matrices_closed"] is False
    assert step39["rank2_to_rank3_sector_transfer_values_closed"] is False
    assert step39["offdiagonal_End0_control_closed"] is False
    assert step39["same_branch_dotD_alpha1_values_closed"] is False
    assert step39["coherent_spectral_zero_mode_projectors_closed"] is False
    assert step39["primitive_C1_contractions_from_operator_values_closed"] is False
    assert step39["accepted_internal_scalar_row_count"] == 0

    step38 = evidence["candidate_data/selected_step38_finiteheisenberg_rhoe_promotion_or_deoperatorfrontier.candidate.json"]
    assert step38["selected_s3_class_restriction_layer_closed"] is True
    assert step38["finite_trace_DE_gap_layer_closed"] is True
    assert step38["operator_level_projective_rhoE_transition_matrices_closed"] is True
    assert step38["nonidentity_projective_rhoE_selected_up_to_unitary_gauge"] is True
    assert step38["selected_covariant_D_E_matrices_closed"] is False
    assert step38["selected_Riesz_Green_values_closed"] is False
    assert step38["same_branch_dotD_alpha1_values_closed"] is False
    assert step38["coherent_spectral_zero_mode_projectors_closed"] is False
    assert step38["primitive_C1_contractions_from_operator_values_closed"] is False
    assert step38["accepted_internal_scalar_row_count"] == 0

    step37 = evidence["candidate_data/selected_step37_finitetrace_degap_import_or_fulloperatorvaluefrontier.candidate.json"]
    assert step37["selected_s3_class_restriction_layer_closed"] is True
    assert step37["finite_trace_DE_gap_layer_closed"] is True
    assert step37["transition_rhoE_or_Cech_Dolbeault_DE_data_finite_trace_slot_closed"] is True
    assert step37["selected_trace_equality_closed"] is True
    assert step37["positive_gap_Riesz_Green_lock_imported"] is True
    assert step37["operator_level_projective_rhoE_transition_matrices_closed"] is False
    assert step37["selected_covariant_D_E_matrices_closed"] is False
    assert step37["selected_Riesz_Green_values_closed"] is False
    assert step37["same_branch_dotD_alpha1_values_closed"] is False
    assert step37["coherent_spectral_zero_mode_projectors_closed"] is False
    assert step37["primitive_C1_contractions_from_operator_values_closed"] is False
    assert step37["accepted_internal_scalar_row_count"] == 0

    step36 = evidence["candidate_data/selected_step36_s3classclosure_reconciliation_or_operatorvaluefrontier.candidate.json"]
    assert step36["selected_s3_differential_cohomology_class_closed"] is True
    assert step36["s3_restriction_pullback_table_closed"] is True
    assert step36["smooth_freed_witten_cancellation_closed"] is True
    assert step36["block_family_higgs_projector_retention_closed"] is True
    assert step36["good_cover_removed_as_physical_knob"] is True
    assert step36["operator_level_projective_rhoE_transition_closed"] is False
    assert step36["selected_D_E_Riesz_Green_dotD_values_closed"] is False
    assert step36["coherent_spectral_zero_mode_projectors_closed"] is False
    assert step36["selected_visible_operator_source_closed"] is False
    assert step36["accepted_internal_scalar_row_count"] == 0

    step35 = evidence["candidate_data/selected_step35_covergauge_reduction_or_s3classrestrictionselector.candidate.json"]
    assert step35["good_cover_removed_as_physical_knob"] is True
    assert step35["cover_refinement_invariance_imported"] is True
    assert step35["step34_functor_preserved"] is True
    assert step35["frontier_reduced_to_selected_s3_class_restriction"] is True
    assert step35["selected_s3_differential_cohomology_class_closed"] is False
    assert step35["s3_restriction_pullback_table_closed"] is False
    assert step35["smooth_freed_witten_projector_retention_closed"] is False
    assert step35["operator_level_projective_rhoE_transition_closed"] is False
    assert step35["selected_D_E_Riesz_Green_dotD_values_closed"] is False
    assert step35["accepted_internal_scalar_row_count"] == 0

    step34 = evidence["candidate_data/selected_step34_flatgerbe_sourcefunctor_or_selectedcoverselector.candidate.json"]
    assert step34["finite_to_smooth_flat_gerbe_source_functor_constructed"] is True
    assert step34["qutrit_central_extension_holonomy_map_constructed"] is True
    assert step34["finite_twisted_CP_cancellation_conditionally_transported"] is True
    assert step34["selected_cover_classifying_map_obligation_isolated"] is True
    assert step34["operator_promotion_boundary_reduced_to_selected_cover_and_projectors"] is True
    assert step34["selected_classifying_map_c_closed"] is False
    assert step34["selected_good_cover_closed"] is False
    assert step34["smooth_freed_witten_projector_retention_closed"] is False
    assert step34["operator_level_projective_rhoE_transition_closed"] is False
    assert step34["selected_D_E_Riesz_Green_dotD_values_closed"] is False
    assert step34["accepted_internal_scalar_row_count"] == 0

    step33 = evidence["candidate_data/selected_step33_smooths3validator_reconciliation_or_holonomyoperatorpromotion.candidate.json"]
    assert step33["strict_q79_smooth_validator_promoted_to_active_gate"] is True
    assert step33["older_projective_gerbe_retired_blocker_wording_demoted"] is True
    assert step33["finite_s3_cp_and_projector_support_kept_closed"] is True
    assert step33["holonomy_operator_promotion_contract_emitted"] is True
    assert step33["minimal_smooth_source_fill_targets_extracted"] is True
    assert step33["smooth_s3_twisted_source_lift_closed"] is False
    assert step33["selected_smooth_cover_or_scaffold_closed"] is False
    assert step33["smooth_freed_witten_projector_retention_closed"] is False
    assert step33["operator_level_projective_rhoE_transition_closed"] is False
    assert step33["selected_D_E_Riesz_Green_dotD_values_closed"] is False
    assert step33["accepted_internal_scalar_row_count"] == 0

    step32 = evidence["candidate_data/selected_step32_samesourcesymmetrybreaking_to_smooths3twistedsource.candidate.json"]
    assert step32["same_source_symmetrybreaking_reduced_to_smooth_s3_twisted_source"] is True
    assert step32["direct_pic0_invariance_route_retired"] is True
    assert step32["gerbe_twisted_s3_route_primary"] is True
    assert step32["finite_s3_restriction_projector_retention_closed"] is True
    assert step32["smooth_s3_twisted_source_lift_closed"] is False
    assert step32["smooth_freed_witten_projector_retention_closed"] is False
    assert step32["operator_level_projective_rhoE_transition_closed"] is False
    assert step32["selected_D_E_Riesz_Green_dotD_values_closed"] is False
    assert step32["accepted_internal_scalar_row_count"] == 0

    step31 = evidence["candidate_data/selected_step31_visiblecwsource_to_samesourcesymmetrybreaking.candidate.json"]
    assert step31["visible_CW_operator_source_reduced_to_common_source"] is True
    assert step31["rank2_non_split_lane_prioritized"] is True
    assert step31["routec_lane_retained_as_parallel_repair"] is True
    assert step31["same_source_symmetrybreaking_contract_emitted"] is True
    assert step31["same_source_symmetrybreaking_source_closed"] is False
    assert step31["selected_visible_operator_source_closed"] is False
    assert step31["selected_D_E_Riesz_Green_dotD_values_closed"] is False
    assert step31["accepted_internal_scalar_row_count"] == 0

    step30 = evidence["candidate_data/selected_step30_projectivebn_mechanicallift_or_visiblesourcecutset.candidate.json"]
    assert step30["projective_BN_mechanical_lift_fields_closed"] is True
    assert step30["smooth_scalar_basis_quadrature_gram_stiffness_closed"] is True
    assert step30["model_active_D_E_projectors_Green_dotD_emitted"] is True
    assert step30["source_level_projective_gerbe_rhoE_closed"] is True
    assert step30["selected_visible_operator_source_closed"] is False
    assert step30["operator_level_projective_rhoE_transition_closed"] is False
    assert step30["selected_source_verified_operator_flags_closed"] is False
    assert step30["selected_sector_basis_D_E_Riesz_Green_dotD_matrices_closed"] is False
    assert step30["accepted_internal_scalar_row_count"] == 0

    step29 = evidence["candidate_data/selected_step29_operatorsector_rhoede_attempt_or_projectivebnsourcecutset.candidate.json"]
    assert step29["operator_sector_smoke_inventory_filled"] is True
    assert step29["identity_rhoE_smoke_retired_as_selected_route"] is True
    assert step29["nonidentity_projective_rhoE_candidate_imported"] is True
    assert step29["ordinary_nonidentity_rhoE_route_retired"] is True
    assert step29["projective_smooth_BN_lift_contract_emitted"] is True
    assert step29["selected_operator_level_projective_rhoE_transition_closed"] is False
    assert step29["selected_sector_basis_D_E_Riesz_Green_dotD_matrices_closed"] is False
    assert step29["selected_smooth_BN_Galerkin_basis_closed"] is False
    assert step29["accepted_internal_scalar_row_count"] == 0

    step28 = evidence["candidate_data/selected_step28_sectorpromotion_reconciliation_or_operatorsectorvaluecutset.candidate.json"]
    assert step28["step27_sector_promotion_frontier_refined"] is True
    assert step28["selected_stationary_End0_to_sector_routing_values_closed"] is True
    assert step28["selected_projector_promotion_Ps_Ks_closed"] is True
    assert step28["selected_stationary_rho_s_matrix_values_closed"] is True
    assert step28["selected_projective_rhoE_source_level_closed"] is True
    assert step28["functional_matter_slot_blocks_and_overlap_normalization_closed"] is True
    assert step28["operator_level_projective_rhoE_from_selected_connection_closed"] is False
    assert step28["selected_rhoE_transition_payload_fullS2_operator_tier_closed"] is False
    assert step28["selected_sector_basis_D_E_Riesz_Green_dotD_matrices_closed"] is False
    assert step28["accepted_internal_scalar_row_count"] == 0

    step27 = evidence["candidate_data/selected_step27_fulls2_subpayload_reduction_or_sectorpromotioncutset.candidate.json"]
    assert step27["diagonal_End0_HYM_subpayload_closed"] is True
    assert step27["protected_T3_Riesz_Green_closed"] is True
    assert step27["T1_T2_covariant_Green_closed"] is True
    assert step27["selected_End0_to_sector_routing_values_closed"] is False
    assert step27["selected_rhoE_transition_payload_closed"] is False
    assert step27["accepted_internal_scalar_row_count"] == 0

    step26 = evidence["candidate_data/selected_step26_phifintrace_matterslot_reconciliation_or_fulls2payloadcutset.candidate.json"]
    assert step26["functional_PhiFin_trace_closed"] is True
    assert step26["static_U10_Ubar5_1M_source_closed"] is True
    assert step26["selected_fullS2_rhoE_D_E_operator_payload_closed"] is False
    assert step26["dynamic_PhiFin_C1_payload_closed"] is False
    assert step26["accepted_internal_scalar_row_count"] == 0

    step25 = evidence["candidate_data/selected_step25_thresholdexternalreplay_noknobkernel_or_fulls2cutset.candidate.json"]
    assert step25["admitted_external_threshold_row_count"] == 7
    assert step25["admitted_external_mass_scheme_row_count"] == 3
    assert step25["final_no_knob_kernel_typed"] is True
    assert step25["accepted_internal_scalar_row_count"] == 0
    assert step25["selected_fullS2_payload_ready"] is False
    assert step25["candidate_specific_universal_source_anchor_selected"] is False

    value_frontier = evidence["candidate_data/selected_acceptedvaluelayerfrontier_or_nonloopingsourcerows.candidate.json"]
    assert value_frontier["source_layer_closed"] is True
    assert value_frontier["value_layer_accepted_source_rows"] == 0
    assert value_frontier["value_layer_required_rows"] == 5

    lambda12 = parts["lambda12 / electroweak local determinant table"]
    assert lambda12["status"] == "OPEN_COMPUTATIONAL"
    assert lambda12["evidence"][0]["lambda_12_closed"] is False
    assert lambda12["evidence"][0]["lambda_12_computable_from_this_gate"] is False

    higgs = parts["Higgs lambda_H / UV two-Higgs Huv payload"]
    assert higgs["status"] == "OPEN_HUV_PAYLOAD"

    values = parts["Yukawa magnitudes, CKM/PMNS, and masses"]
    assert values["status"] == "OPEN_VALUE_PREDICTION"
    assert values["evidence"][0]["source_layer_row_available"] is True
    assert values["evidence"][0]["accepted_true_value_source_row_emitted"] is False
    assert values["evidence"][1]["admitted_external_threshold_rows_closed"] is True
    assert values["evidence"][1]["admitted_external_mass_scheme_rows_closed"] is True
    assert values["evidence"][1]["accepted_internal_scalar_row_count"] == 0
    assert values["evidence"][1]["lambda_H_row_emitted"] is False

    repos = {repo["repo"] for repo in data["repo_summary"]}
    expected = {
        "mtt-sm-parity-closure",
        "mtt-sm-parity-repro",
        "mtt-q79-proof-repro",
        "mtt-qa-su3-packet-proof",
        "mtt-nonsm-constants-no-knob",
        "mtt-protospinor-gr-response-proof",
        "mtt-individual-constants-source-search",
        "18 Theta-Closure & Execution Program",
    }
    assert expected <= repos

    assert data["status"] == "CROSS_REPO_STATUS_AUDIT_UPDATED_STEP42_EXECUTABLE_REPLAY_SOLUTION_CLOSED_NOKNOB_ROWS_OPEN"
    assert data["guardrails"]["stale_open_packets_allowed_to_override_later_closure"] is False

    print("AUDIT_PASS: cross-repo part status is coherent; Step42 closes executable replay solution and leaves no-knob rows, lambda12, and Huv open.")


if __name__ == "__main__":
    main()
