"""Run the reproducibility checks for the MTT q79 proof package."""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "proof_corpus"
REPORT = ROOT / "reports" / "verification_report.txt"
CERTIFICATES = ROOT / "certificates"

AUDITS = [
    "terminal_closure_certificate_audit.py",
    "consolidated_exact_z64_to_q79_closure_audit.py",
    "z64_exact_branch_certificate_audit.py",
    "z7_fuyau_mukai_charge_sector_certificate_audit.py",
    "ckm_phase_bridge_no_proxy_audit.py",
    "flavor_no_proxy_mass_gap_audit.py",
    "theta_selected_overlap_kernel_skeleton_audit.py",
    "iwasawa_rank_one_yukawa_seed_audit.py",
    "rank_one_lift_correction_channel_ledger_audit.py",
    "e6_to_sm_yukawa_operator_dictionary_audit.py",
    "single_higgs_channel_projection_audit.py",
    "finite_channel_sets_for_rank_one_lift_audit.py",
    "q79_channel_restriction_audit.py",
    "selected_channel_weight_extraction_protocol_audit.py",
    "forced_c0_c6_channel_weight_blocks_audit.py",
    "c3_lens_nil_weight_source_audit.py",
    "c1_curvature_weight_source_audit.py",
    "c1_curvature_insertion_formula_audit.py",
    "c1_iwasawa_rplus_support_audit.py",
    "c1_alpha1_rank_lift_criterion_audit.py",
    "selected_c1_response_extraction_attempt_audit.py",
    "c1_finite_response_matrix_reduction_audit.py",
    "ckm_leading_noncommutation_criterion_audit.py",
    "jarlskog_closure_criterion_audit.py",
    "rank_one_lift_operator_hard_leap_audit.py",
    "full_sm_closure_attempt_audit.py",
    "selected_full_sm_data_theorem_attempt_audit.py",
    "shared_knob_cross_encoding_ledger_audit.py",
    "matrix_construction_routes_audit.py",
    "selected_zero_mode_basis_dotd_audit.py",
    "iwasawa_galerkin_zero_mode_slot_attempt_audit.py",
    "iwasawa_dolbeault_complex_extraction_audit.py",
    "iwasawa_monad_map_data_gate_audit.py",
    "corrected_a01_candidate_scan_audit.py",
    "index_to_three_family_upgrade_gate_audit.py",
    "invariant_mc_torsion_branch_gate_audit.py",
    "iwasawa_invariant_a01_repair_obstruction_audit.py",
    "post_invariant_way_forward_audit.py",
    "iwasawa_typed_monad_section_recovery_audit.py",
    "iwasawa_spectral_operator_gate_audit.py",
    "iwasawa_non_invariant_galerkin_protocol_audit.py",
    "iwasawa_galerkin_basis_skeleton_audit.py",
    "iwasawa_standard_lattice_deck_scaffold_audit.py",
    "iwasawa_scalar_deck_mode_filter_audit.py",
    "iwasawa_scalar_fe_gluing_audit.py",
    "iwasawa_bundle_fe_gluing_contract_audit.py",
    "iwasawa_rhoE_source_recovery_audit.py",
    "iwasawa_rhoE_validator_audit.py",
    "iwasawa_rhoE_mesh_validator_audit.py",
    "iwasawa_rhoE_metric_validator_audit.py",
    "iwasawa_sector_projection_validator_audit.py",
    "iwasawa_de_action_validator_audit.py",
    "iwasawa_riesz_gap_validator_audit.py",
    "iwasawa_reduced_green_validator_audit.py",
    "iwasawa_dotd_response_validator_audit.py",
    "selected_missing_data_calculation_audit.py",
    "iwasawa_diagnostic_h1_three_spectral_pipeline_audit.py",
    "iwasawa_selected_de_construction_attempt_audit.py",
    "selected_de_source_hunt_audit.py",
    "iwasawa_route_c_finite_solve_scaffold_audit.py",
    "iwasawa_route_c_branch_smoke_attempt_audit.py",
    "iwasawa_route_c_smoke_c1_dependency_audit.py",
    "su5_projection_tensor_derivation_attempt_audit.py",
    "selected_su5_source_proof_attempt_audit.py",
    "su5_block_orientation_route_split_audit.py",
    "dual_route_closure_attempt_audit.py",
    "route_b_heavy_link_overlap_difference_calculator_audit.py",
    "route_b_final_missing_object_calculation_attempt_audit.py",
    "selected_fourier_transport_proof_attempt_audit.py",
    "selected_gerbe_fourier_type_theorem_audit.py",
    "time_oriented_conjugate_branch_selection_audit.py",
    "time_oriented_fixed_gerbe_representative_audit.py",
    "time_oriented_m1_gerbe_period_table_audit.py",
    "time_oriented_m1_deck_cech_lift_audit.py",
    "time_oriented_m1_flat_gerbe_promotion_audit.py",
    "time_oriented_m1_freed_witten_cycle_gate_audit.py",
    "time_oriented_m1_qutrit_line_cycle_restrictions_audit.py",
    "visible_complex_worldvolume_spinc_gate_audit.py",
    "visible_active_f3_image_recovery_obstruction_audit.py",
    "visible_twisted_chan_paton_rescue_audit.py",
    "visible_twisted_d7_volume_selector_attempt_audit.py",
    "visible_twisted_d7_qutrit_symmetry_selector_audit.py",
    "visible_twisted_d7_equivariant_embedding_selector_audit.py",
    "visible_twisted_s3_source_packet_attempt_audit.py",
    "visible_twisted_s3_finite_cp_cancellation_audit.py",
    "visible_twisted_s3_smooth_source_lift_attempt_audit.py",
    "iwasawa_deligne_cover_gauge_reduction_audit.py",
    "visible_twisted_s3_class_restriction_packet_attempt_audit.py",
    "visible_twisted_s3_class_restriction_closure_audit.py",
    "time_oriented_m1_green_schwarz_gate_audit.py",
    "time_oriented_m1_visible_green_schwarz_requirement_audit.py",
    "time_oriented_m1_visible_green_schwarz_curvature_closure_audit.py",
    "time_oriented_m1_visible_green_schwarz_source_gate_audit.py",
    "time_oriented_m1_deresponse_target_audit.py",
    "su5_matter_slot_transversality_audit.py",
    "selected_matter_slot_transversality_source_gate_audit.py",
    "selected_matter_source_two_path_exploration_audit.py",
    "selected_hym_operator_source_gate_audit.py",
    "visible_operator_source_blocker_resolution_audit.py",
    "visible_operator_source_after_s3_closure_audit.py",
    "visible_chern_weil_formal_source_audit.py",
    "visible_chern_weil_quantization_gate_audit.py",
    "visible_integral_chern_source_candidate_audit.py",
    "visible_split_line_hym_no_go_audit.py",
    "visible_stable_source_sign_gate_audit.py",
    "iwasawa_monad_visible_source_role_audit.py",
    "visible_additive_source_factor_route_audit.py",
    "visible_rank2_extension_valpha_route_audit.py",
    "visible_rank2_l2_ext_h1_gate_audit.py",
    "constants_gr_cross_repo_clue_ledger_audit.py",
    "visible_valpha_chern_bianchi_source_packet_candidates_audit.py",
    "visible_rank2_l2_cohomology_source_hunt_audit.py",
    "visible_rank2_l2_invariant_dolbeault_attempt_audit.py",
    "visible_rank2_l2_pullback_cech_attempt_audit.py",
    "visible_rank2_l2_pullback_selection_attempt_audit.py",
    "visible_rank2_l2_source_ambiguity_classification_audit.py",
    "visible_rank2_l2_branch_selection_reduction_audit.py",
    "selected_pullback_l2_branch_orientation_source_gate_audit.py",
    "selected_gauduchon_wall_radius_gate_audit.py",
    "visible_rank2_l2_integral_lift_source_gap_audit.py",
    "visible_rank2_l2_appell_humbert_automorphy_audit.py",
    "visible_rank2_l2_selector_obstruction_audit.py",
    "visible_rank2_l2_selected_radius_import_nogo_audit.py",
    "visible_rank2_l2_ordered_source_promotion_gate_audit.py",
    "iwasawa_monad_l2_branch_orientation_candidate_audit.py",
    "monad_difference_l2_source_sufficiency_audit.py",
    "selected_monad_difference_l2_source_proof_attempt_audit.py",
    "monad_difference_pic0_switch_reduction_audit.py",
    "ordered_layer_pic0_quotient_audit.py",
    "ordered_layer_terminal_lane_selector_reduction_audit.py",
    "central_circle_neutral_terminal_lane_filter_audit.py",
    "terminal_map_source_principle_base_order_attempt_audit.py",
    "terminal_map_dual_extension_sign_audit.py",
    "terminal_g3_valpha_source_path_reduction_audit.py",
    "terminal_admissible_section_source_principle_audit.py",
    "unconditional_selected_monad_difference_l2_source_attempt_audit.py",
    "same_source_monad_gs_operator_fusion_gate_audit.py",
    "same_source_monad_gs_operator_fusion_attempt_audit.py",
    "selected_qa_su3_visible_source_architecture_import_audit.py",
    "selected_qa_su3_same_source_valpha_s3_operator_packet_attempt_audit.py",
    "valpha_s3_mod3_cocycle_compatibility_audit.py",
    "valpha_s3_full_mod3_pullback_obstruction_audit.py",
    "valpha_s3_two_block_mod3_lift_audit.py",
    "valpha_s3_two_block_source_selector_reduction_audit.py",
    "valpha_s3_symmetry_breaking_route_triage_audit.py",
    "selected_qa_su3_orientation_dedotd_source_packet_attempt_audit.py",
    "orientation_branch_antiunitary_equivalence_audit.py",
    "orientation_observable_parity_audit.py",
    "constants_m1_cw_source_route_import_audit.py",
    "valpha_operator_source_critical_path_audit.py",
    "selected_valpha_chern_weil_operator_source_attempt_audit.py",
    "selected_valpha_operator_source_sufficiency_audit.py",
    "terminal_valpha_remaining_parts_lockdown_audit.py",
    "all_remaining_valpha_gates_attempt_audit.py",
    "valpha_extension_stability_filter_attempt_audit.py",
    "valpha_zero_slope_yoneda_reduction_audit.py",
    "valpha_remaining_yoneda_scalar_attempt_audit.py",
    "valpha_kunneth_yoneda_scalar_proof_audit.py",
    "valpha_central_neutral_destabilizer_reduction_audit.py",
    "valpha_appell_humbert_yoneda_promotion_audit.py",
    "valpha_repo_update_source_frontier_audit.py",
    "q79_valpha_source_origin_finite_emission_bridge_audit.py",
    "q79_selected_phifin_alpha1_payload_audit.py",
    "q79_routec_basis_transport_primitive_source_theorem_audit.py",
    "q79_routec_weylpair_aselected_assembly_or_source_proof_audit.py",
    "q79_routec_weylpair_source_provenance_lemma_audit.py",
    "q79_routec_weylpair_sector_charge_or_chirality_certificate_audit.py",
    "q79_selected_matter_slot_charge_and_overlap_normalization_theorem_audit.py",
    "q79_samesource_operatorpacket_fill_or_nogo_audit.py",
    "q79_stability_hym_or_routec_residual_source_audit.py",
    "q79_global_destabilizer_enumeration_or_selected_residual_audit.py",
    "q79_selected_ah_goodcover_promotion_hym_certificate_audit.py",
    "q79_ah_source_selection_or_routec_residual_reduction_audit.py",
    "q79_selected_monad_l2_source_and_operatorpic0_or_routec_residual_audit.py",
    "q79_same_source_operator_provenance_or_selected_routec_solve_audit.py",
    "q79_selected_visible_bundle_operator_source_or_primitive_c1_contractions_audit.py",
    "q79_selected_de_green_dotd_source_for_primitive_c1_audit.py",
    "q79_routec_selected_source_certificate_or_typed_de_construction_audit.py",
    "q79_typed_monad_cech_or_hym_connection_witness_audit.py",
    "q79_selected_finite_connection_solve_execution_audit.py",
    "q79_selected_trace_equals_emitted_27mode_operator_or_full_hym_newton_replay_audit.py",
    "q79_selected_dotd_alpha1_c1_response_emission_audit.py",
    "q79_selected_alpha1_tangent_or_retarded_overlap_kernel_audit.py",
    "q79_selected_physical_alpha1_source_normalization_or_end0_sector_routing_value_fill_audit.py",
    "q79_theorem_change_list_for_paper_updates_audit.py",
    "visible_rhoE_source_ansatz_search_audit.py",
    "iwasawa_constant_wilson_ansatz_scan_audit.py",
    "iwasawa_scalar_phase_mesh_rhoE_prototype_audit.py",
    "iwasawa_diagonal_phase_mesh_rhoE_prototype_audit.py",
    "iwasawa_rotated_phase_mesh_rhoE_sector_prototype_audit.py",
    "iwasawa_puregauge_nonabelian_mesh_rhoE_prototype_audit.py",
    "iwasawa_face_graph_coboundary_diagnostic_audit.py",
    "iwasawa_selected_source_promotion_gate_audit.py",
    "iwasawa_n1_phase_coboundary_obstruction_audit.py",
    "iwasawa_n1_solvable_carrier_obstruction_audit.py",
    "iwasawa_projective_magnetic_carrier_audit.py",
    "iwasawa_projective_rhoE_mesh_validator_audit.py",
    "iwasawa_projective_twist_source_hunt_audit.py",
    "iwasawa_twisted_source_promotion_gate_audit.py",
    "iwasawa_twisted_source_packet_fill_attempt_audit.py",
    "iwasawa_discrete_gerbe_holonomy_candidate_audit.py",
    "iwasawa_flat_torsion_selection_gap_audit.py",
    "iwasawa_torsion_label_four_route_selector_audit.py",
    "iwasawa_orientation_de_dotd_bridge_audit.py",
    "iwasawa_block_factorized_twist_route_audit.py",
    "iwasawa_block_factorized_twisted_packet_candidate_audit.py",
    "iwasawa_block_coupling_invariant_selection_rule_audit.py",
    "iwasawa_block_factorized_sector_maps_audit.py",
    "iwasawa_c6_orientation_branch_reduction_audit.py",
    "iwasawa_c6_common_holonomy_branch_pair_audit.py",
    "iwasawa_c6_global_phase_block_audit.py",
    "iwasawa_c6_support_noncommutation_gate_audit.py",
    "ckm_heavy_link_gate_calculator_audit.py",
    "ckm_heavy_link_packet_fill_attempt_audit.py",
    "qutrit_c6_pure_heavy_link_support_audit.py",
    "c1_heavy_link_delta_t_reduction_audit.py",
    "su5_qutrit_basis_transport_heavy_link_candidate_audit.py",
    "su5_qutrit_transport_selector_hunt_audit.py",
    "qutrit_polarization_transport_lemma_audit.py",
    "su5_qutrit_polarization_selection_gate_audit.py",
    "selected_su5_qutrit_polarization_validator_audit.py",
    "selected_su5_qutrit_polarization_packet_fill_attempt_audit.py",
    "group_algebra_carrier_z64_audit.py",
    "finite_wilson_deck_carrier_extraction_audit.py",
    "mtt_flavor_hessian_extraction_audit.py",
    "pure_central_circle_block_reduction_audit.py",
    "exact_coherent_block_schur_collapse_audit.py",
    "selected_kernel_primitive_lag_closure_audit.py",
    "retarded_unit_lag_projection_proof.py",
    "mukai_discriminant_group_check.py",
    "stable_sheaf_existence_mukai_z7_audit.py",
    "mukai_z7_cp_character_identification_audit.py",
    "fu_yau_mukai_fixed_sector_selection_audit.py",
    "mukai_fixed_sector_descent_check.py",
    "selected_cp_character_dual_check.py",
    "crt_decomposition_q79_check.py",
]


def run_audit(script: str) -> tuple[int, str]:
    proc = subprocess.run(
        [sys.executable, script],
        cwd=CORPUS,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return proc.returncode, proc.stdout


def certificate_status() -> str:
    lines = ["Certificates", "============", ""]
    for path in sorted(CERTIFICATES.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        lines.append(f"{path.name}: {data.get('status', 'UNKNOWN')}")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    if not CORPUS.exists():
        print(f"Missing proof corpus: {CORPUS}")
        return 2

    report_parts = [
        "MTT q79 proof reproduction report",
        "=================================",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        f"Corpus: {CORPUS}",
        "",
    ]

    failures: list[str] = []
    for script in AUDITS:
        script_path = CORPUS / script
        report_parts.extend([f"## {script}", ""])
        if not script_path.exists():
            failures.append(script)
            report_parts.append(f"MISSING: {script_path}")
            report_parts.append("")
            continue

        code, output = run_audit(script)
        report_parts.append(output.rstrip())
        report_parts.append("")
        if code != 0:
            failures.append(script)

    report_parts.append(certificate_status())

    if failures:
        report_parts.append("Verification result: FAIL")
        report_parts.append("Failing or missing audits:")
        report_parts.extend(f"- {name}" for name in failures)
        exit_code = 1
    else:
        report_parts.append("Verification result: PASS")
        report_parts.append("Terminal q79 certificates are closed for the exact/charge branch.")
        report_parts.append(
            "Remaining OPEN/BLOCKED flavor and SM items are future no-proxy certificates, not terminal q79-branch blockers."
        )
        exit_code = 0

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(report_parts) + "\n", encoding="utf-8")

    print(REPORT.read_text(encoding="utf-8"))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
