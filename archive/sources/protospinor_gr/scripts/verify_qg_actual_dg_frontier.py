from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run(relative_path: str) -> str:
    process = subprocess.run(
        [sys.executable, relative_path],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if process.returncode != 0:
        raise SystemExit(
            f"Command failed: {relative_path}\nSTDOUT:\n{process.stdout}\nSTDERR:\n{process.stderr}"
        )
    return process.stdout.strip()


def main() -> None:
    steps = [
        "scripts/compute_q79_s3_strain_intertwiner.py",
        "proof_corpus/q79_s3_strain_intertwiner_audit.py",
        "scripts/compute_world_in_world_z64_metric_source_map.py",
        "proof_corpus/world_in_world_z64_metric_source_map_audit.py",
        "scripts/compute_same_circle_weight2_bundle_obstruction.py",
        "proof_corpus/same_circle_weight2_bundle_obstruction_audit.py",
        "scripts/compute_protospinor_odd_weight_lift_selector_dichotomy.py",
        "proof_corpus/protospinor_odd_weight_lift_selector_dichotomy_audit.py",
        "scripts/compute_q79_signed_sheet_w2_branch_divisor_reduction.py",
        "proof_corpus/q79_signed_sheet_w2_branch_divisor_reduction_audit.py",
        "scripts/compute_q79_trial_branch_irreducibility_and_spin_decision.py",
        "proof_corpus/q79_trial_branch_irreducibility_and_spin_decision_audit.py",
        "scripts/compute_q79_selected_side_spin_spinc_decision.py",
        "proof_corpus/q79_selected_side_spin_spinc_decision_audit.py",
        "scripts/compute_q79_shared_circle_spinc_determinant_bridge.py",
        "proof_corpus/q79_shared_circle_spinc_determinant_bridge_audit.py",
        "scripts/compute_q79_shared_z64_same_source_monodromy_map.py",
        "proof_corpus/q79_shared_z64_same_source_monodromy_map_audit.py",
        "scripts/compute_q79_spinc_flat_hym_ramification_extension.py",
        "proof_corpus/q79_spinc_flat_hym_ramification_extension_audit.py",
        "scripts/compute_q79_branch_cusp_resolution_rootstack_hym.py",
        "proof_corpus/q79_branch_cusp_resolution_rootstack_hym_audit.py",
        "scripts/compute_q79_cubic_norm_full_monodromy_rootstack_bridge.py",
        "proof_corpus/q79_cubic_norm_full_monodromy_rootstack_bridge_audit.py",
        "scripts/compute_global_helicity_bundle_same_circle_nogo.py",
        "proof_corpus/global_helicity_bundle_same_circle_nogo_audit.py",
        "scripts/compute_global_covariant_helicity2_dg_bundle.py",
        "proof_corpus/global_covariant_helicity2_dg_bundle_audit.py",
        "scripts/compute_selected_q79_z64_qww_source_factorization.py",
        "proof_corpus/selected_q79_z64_qww_source_factorization_audit.py",
        "scripts/compute_q79_spectral_hym_strain_symbol_bridge.py",
        "proof_corpus/q79_spectral_hym_strain_symbol_bridge_audit.py",
        "scripts/compute_q79_complement_quarterturn_hessian_scalarization.py",
        "proof_corpus/q79_complement_quarterturn_hessian_scalarization_audit.py",
        "scripts/compute_q79_shared_z64_fuyau_parent_quarterturn_descent.py",
        "proof_corpus/q79_shared_z64_fuyau_parent_quarterturn_descent_audit.py",
        "scripts/compute_q79_square_theta_quarterturn_strain_nogo.py",
        "proof_corpus/q79_square_theta_quarterturn_strain_nogo_audit.py",
        "scripts/compute_q79_shared_rootplane_twisted_exterior_jde_functor.py",
        "proof_corpus/q79_shared_rootplane_twisted_exterior_jde_functor_audit.py",
        "scripts/compute_q79_finite_rootstack_reynolds_tt_hessian.py",
        "proof_corpus/q79_finite_rootstack_reynolds_tt_hessian_audit.py",
        "scripts/compute_q79_ordinary_exterior_dual_hym_nogo_and_derived_kernel_cutset.py",
        "proof_corpus/q79_ordinary_exterior_dual_hym_nogo_and_derived_kernel_cutset_audit.py",
        "scripts/compute_q79_marked_shared_circle_c4_descent_nogo.py",
        "proof_corpus/q79_marked_shared_circle_c4_descent_nogo_audit.py",
        "scripts/compute_global_tt_hessian_action_uniqueness_reduction.py",
        "proof_corpus/global_tt_hessian_action_uniqueness_reduction_audit.py",
        "scripts/compute_massless_tt_pole_internal_gap_no_go.py",
        "proof_corpus/massless_tt_pole_internal_gap_no_go_audit.py",
        "scripts/compute_q79_coherent_zero_mode_tt_source.py",
        "proof_corpus/q79_coherent_zero_mode_tt_source_audit.py",
        "scripts/compute_closure_to_einstein_action_reduction.py",
        "proof_corpus/closure_to_einstein_action_reduction_audit.py",
        "scripts/compute_closure_anholonomy_teleparallel_einstein_bridge.py",
        "proof_corpus/closure_anholonomy_teleparallel_einstein_bridge_audit.py",
        "scripts/compute_strict_same_source_teleparallel_selection.py",
        "proof_corpus/strict_same_source_teleparallel_selection_audit.py",
        "scripts/compute_q79_shared_circle_double_return_cln_nil_flat_endpoint.py",
        "proof_corpus/q79_shared_circle_double_return_cln_nil_flat_endpoint_audit.py",
        "scripts/compute_q79_zero_defect_vacuum_selection_nogo_and_state_cutset.py",
        "proof_corpus/q79_zero_defect_vacuum_selection_nogo_and_state_cutset_audit.py",
        "scripts/compute_q79_finite_source_tegr_classical_closure.py",
        "proof_corpus/q79_finite_source_tegr_classical_closure_audit.py",
        "scripts/compute_quadratic_tt_nonlinear_action_nogo.py",
        "proof_corpus/quadratic_tt_nonlinear_action_nogo_audit.py",
        "scripts/compute_spectral_action_einstein_ir_limit.py",
        "proof_corpus/spectral_action_einstein_ir_limit_audit.py",
        "scripts/compute_stieltjes_massless_gaussian_no_go.py",
        "proof_corpus/stieltjes_massless_gaussian_no_go_audit.py",
        "scripts/compute_q79_free_graviton_quantization_and_uv_cutset.py",
        "proof_corpus/q79_free_graviton_quantization_and_uv_cutset_audit.py",
        "scripts/compute_q79_interacting_low_energy_qg_eft_closure.py",
        "proof_corpus/q79_interacting_low_energy_qg_eft_closure_audit.py",
        "scripts/compute_q79_f3x2_discrete_torsion_modular_orbit.py",
        "proof_corpus/q79_f3x2_discrete_torsion_modular_orbit_audit.py",
        "scripts/compute_q79_twisted_group_algebra_topological_character.py",
        "proof_corpus/q79_twisted_group_algebra_topological_character_audit.py",
        "scripts/compute_q79_seven_seed_modular_induction_stabilizers.py",
        "proof_corpus/q79_seven_seed_modular_induction_stabilizers_audit.py",
        "scripts/compute_q79_degree2_k3_fuyau_torsion_glsm_base.py",
        "proof_corpus/q79_degree2_k3_fuyau_torsion_glsm_base_audit.py",
        "scripts/compute_q79_aggregate_tlsm_anomaly_and_odd_bundle_nogo.py",
        "proof_corpus/q79_aggregate_tlsm_anomaly_and_odd_bundle_nogo_audit.py",
        "scripts/compute_q79_shared_circle_clutching_c2_c3_independence.py",
        "proof_corpus/q79_shared_circle_clutching_c2_c3_independence_audit.py",
        "scripts/compute_q79_fuyau_mixed_c2_hodge_admissibility.py",
        "proof_corpus/q79_fuyau_mixed_c2_hodge_admissibility_audit.py",
        "scripts/compute_q79_standard_tlsm_pullback_chirality_nogo.py",
        "proof_corpus/q79_standard_tlsm_pullback_chirality_nogo_audit.py",
        "scripts/compute_q79_heterotic_string_uv_inheritance_cutset.py",
        "proof_corpus/q79_heterotic_string_uv_inheritance_cutset_audit.py",
        "scripts/compute_q79_primitive_branch_selection_cutset.py",
        "proof_corpus/q79_primitive_branch_selection_cutset_audit.py",
        "scripts/compute_qg_actual_dg_frontier_synthesis.py",
        "proof_corpus/qg_actual_dg_frontier_synthesis_audit.py",
    ]
    outputs = [run(step) for step in steps]
    print("\n\n".join(outputs))
    print("QG_ACTUAL_DG_FRONTIER_VERIFY_PASS")


if __name__ == "__main__":
    main()
