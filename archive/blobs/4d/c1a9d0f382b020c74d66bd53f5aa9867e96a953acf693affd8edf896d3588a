"""Audit the Higgs dynamic-strain / C5b-C6 projection bridge packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgsdynamicstrainkernel_or_c5bc6projectionnoboundaryproof"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PROJECTION = PACKET_DIR / "metric_quotient_projection_morphism.packet.json"
C5B_PROOF = PACKET_DIR / "c5b_projection_measure_equality_proof.packet.json"
C6_PROOF = PACKET_DIR / "c6_projection_no_boundary_source_proof.packet.json"
SBETA = PACKET_DIR / "selected_finite_reduction_sbeta_promotion.packet.json"
STRAIN_RECHECK = PACKET_DIR / "dynamic_strain_kernel_route_after_projection_bridge.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_c5bc6_projection.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_c5bc6_projection.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsDynamicStrainKernel_or_C5bC6ProjectionNoBoundaryProof_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_HIGGSDYNAMICSTRAINKERNEL_OR_C5BC6PROJECTIONNOBOUNDARYPROOF_"
    "C5B_C6_PROJECTION_REDUCTION_CLOSED_DYNAMIC_HERM2_AND_HK_OPEN"
)
NEXT = "MTT_Selected_HSectorQuarticThresholdFromProjectionReduction_or_DynamicHerm2Rows_v1"
SBETA_VALUE = 0.004701083905943647


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure flag")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    projection = load(PROJECTION)
    c5b = load(C5B_PROOF)
    c6 = load(C6_PROOF)
    sbeta = load(SBETA)
    strain = load(STRAIN_RECHECK)
    hk_gate = load(HK_GATE)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("projection", projection),
        ("C5b proof", c5b),
        ("C6 proof", c6),
        ("s_beta promotion", sbeta),
        ("strain recheck", strain),
        ("H K gate", hk_gate),
        ("cutset", cutset),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "certificate next")
    require(data["theorem"]["proved"] is True, "candidate theorem")
    require(cert["theorem_proved"] is True, "cert theorem")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")

    decision = data["closure_decision"]
    for key in [
        "bridge_validator_C1_closed",
        "bridge_validator_C2_closed",
        "bridge_validator_C3_closed",
        "bridge_validator_C4_closed",
        "bridge_validator_C5a_trace_grid_identity_closed",
        "bridge_validator_C5b_projection_measure_equality_closed",
        "bridge_validator_C6_no_boundary_closed",
        "metric_quotient_projection_morphism_selected",
        "selected_finite_reduction_policy_emitted",
        "selected_s_beta_value_found",
    ]:
        require(decision[key] is True, f"decision should close {key}")
    require(abs(decision["selected_s_beta_value"] - SBETA_VALUE) < 1e-18, "s_beta value")
    for key in [
        "selected_dynamic_strain_kernel_emitted",
        "selected_F_H_second_variation_emitted",
        "selected_H_response_table_emitted",
        "selected_Hermitian_M_H_values_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "selected_Delta_row_emitted",
        "selected_Re_Omega_row_emitted",
        "selected_Im_Omega_row_emitted",
        "mass_light_line_projector_P_L_emitted",
        "selected_H_quartic_functional_emitted",
        "selected_H_threshold_scheme_functional_emitted",
        "K_threshold_Omega_H_lambda_emitted",
        "ten_K_antecedent_satisfied",
        "strict_Omega_lambda_scalar_execution_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
    require(decision["accepted_selected_K_source_row_count"] == 9, "selected K count")
    require(decision["selected_K_threshold_row_count_required"] == 10, "required K count")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "internal scalar rows")

    require(
        projection["status"] == "METRIC_QUOTIENT_HIGGS_PROJECTION_MORPHISM_SELECTED",
        "projection status",
    )
    require(projection["theorem"]["proved"] is True, "projection theorem")
    exact = projection["input_exact_sequence"]
    require(exact["quotient_map_matrix_over_Z"] == [[1, 1]], "q matrix")
    require(exact["kernel_inclusion_matrix_over_Z"] == [[1], [-1]], "kernel matrix")
    require(exact["q_Hu_equals_q_Hd_dagger"] is True, "q equality")
    require(exact["kernel_is_span_Hu_minus_Hd_dagger"] is True, "kernel span")
    checks = projection["metric_quotient_formula"]["checks"]
    for key in [
        "q_sigma_G_equals_identity_on_H",
        "P_q_idempotent",
        "P_q_G_self_adjoint",
        "kernel_P_q_equals_kernel_q",
        "image_P_q_equals_G_orthogonal_complement_of_kernel_q",
    ]:
        require(checks[key] is True, f"projection check {key}")
    require(checks["free_beta_parameter_introduced"] is False, "beta knob introduced")
    scope = projection["scope_guard"]
    require(scope["selects_physical_projection_measure"] is True, "projection measure not selected")
    require(scope["selects_mass_light_line_projector_P_L"] is False, "mass P_L overclosed")
    require(scope["selects_dynamic_Herm2_Hessian"] is False, "Herm2 overclosed")

    require(
        c5b["status"] == "C5B_PHYSICAL_HIGGS_PROJECTION_MEASURE_EQUALITY_CLOSED",
        "C5b status",
    )
    require(c5b["theorem"]["proved"] is True, "C5b theorem")
    for key in [
        "C2_exact_E_H_UV_to_H_quotient",
        "C3_selected_HYM_metric_bound_to_E_H_UV",
        "C4_normalized_finite_trace_attached",
        "C5a_trace_to_H7B1U_grid_identity",
        "premise_free_phi_fin_restriction_morphism",
        "transport_closed_symbolic_quotient",
    ]:
        require(c5b["closed_inputs"][key] is True, f"C5b input {key}")
    old = c5b["old_blocker_resolved"]
    require(old["previous_C5b_emitted"] is False, "old C5b should have been false")
    identity = c5b["projection_measure_identity"]
    require(identity["accepted_as_physical_Higgs_projection_measure"] is True, "measure accept")
    require(identity["projection_measure_equality"] is True, "measure equality")
    require(identity["node_count"] == 331776, "node count")
    require(identity["uniform_weight_rational"] == "1/331776", "uniform weight")
    require(identity["target_or_observed_value_used"] is False, "target used")
    for key in [
        "rho_weighted_mean_promoted",
        "exp_density_weighted_mean_promoted",
        "observed_Higgs_or_beta_selector_used",
        "direct_Herm2_Huv_rows_emitted",
    ]:
        require(c5b["non_promotions"][key] is False, f"C5b overpromoted {key}")

    require(
        c6["status"] == "C6_HIGGS_PROJECTION_NO_EXTRA_BOUNDARY_SOURCE_CLOSED",
        "C6 status",
    )
    require(c6["theorem"]["proved"] is True, "C6 theorem")
    owner = c6["source_owner_certificate"]
    require(owner["physical_action_source_owner"] == "PhysicalPhiFinC1ActionSource", "owner")
    require(owner["premise_free_phi_fin_restriction_morphism_proved"] is True, "restriction")
    require(owner["premise_free_route_A_certificate_valid"] is True, "route A")
    require(owner["no_extra_physical_boundary_or_source_term"] is True, "no boundary")
    require(owner["source_row_premise_used"] is False, "source row premise")
    require(owner["same_branch"] is True, "same branch")
    boundary = c6["finite_projection_boundary_check"]
    require(boundary["P_q_internal_to_Q_sel_U"] is True, "P internal")
    require(boundary["finite_trace_cyclicity_applies"] is True, "trace cyclicity")
    require(boundary["continuum_boundary_integral_introduced"] is False, "continuum boundary")
    require(boundary["extra_source_term_introduced_by_projection"] is False, "extra source")
    require(boundary["raw_27mode_truncation_used"] is False, "raw truncation")
    require(c6["no_extra_boundary_source_term"] is True, "C6 flag")

    require(
        sbeta["status"] == "SELECTED_UNIFORM_FINITE_REDUCTION_SBETA_PROMOTED",
        "s_beta status",
    )
    require(sbeta["theorem"]["proved"] is True, "s_beta theorem")
    policy = sbeta["selected_finite_reduction_policy"]
    for key in [
        "selected_finite_reduction_policy_emitted",
        "selected_minimal_lift_policy_emitted",
        "source_metric_bound_to_E_H_UV",
        "physical_projection_measure_equality",
        "no_extra_boundary_source_term",
    ]:
        require(policy[key] is True, f"s_beta policy {key}")
    selected = sbeta["selected_s_beta"]
    require(selected["formula"] == "tanh(2u)^2", "s_beta formula")
    require(abs(selected["value"] - SBETA_VALUE) < 1e-18, "selected s_beta")
    require(selected["selected_s_beta_promoted"] is True, "s_beta not promoted")
    require(selected["observed_higgs_or_beta_used"] is False, "observed beta")
    non = sbeta["non_promotions"]
    for key in [
        "selected_H_quartic_functional_emitted",
        "selected_H_threshold_scheme_functional_emitted",
        "K_threshold_Omega_H_lambda_emitted",
        "dynamic_Herm2_Hessian_emitted",
        "mass_light_line_projector_P_L_emitted",
    ]:
        require(non[key] is False, f"s_beta overpromotion {key}")

    require(
        strain["status"] == "DYNAMIC_STRAIN_KERNEL_RECHECKED_STILL_ABSENT_AFTER_C5B_C6",
        "strain status",
    )
    bridge = strain["projection_bridge_now_closed"]
    require(bridge["C5b_projection_measure_equality_closed"] is True, "strain C5b")
    require(bridge["C6_no_extra_boundary_source_term_closed"] is True, "strain C6")
    require(bridge["selected_s_beta_promoted"] is True, "strain s_beta")
    dynamic = strain["dynamic_Herm2_route_state"]
    for key in [
        "selected_dynamic_strain_kernel_emitted",
        "selected_F_H_second_variation_emitted",
        "selected_H_response_table_emitted",
        "selected_Hermitian_M_H_values_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "selected_Delta_row_emitted",
        "selected_Re_Omega_row_emitted",
        "selected_Im_Omega_row_emitted",
    ]:
        require(dynamic[key] is False, f"dynamic overclosed {key}")
    distinction = strain["mass_projector_distinction"]
    require(distinction["quotient_horizontal_projector_P_q_selected"] is True, "Pq")
    require(distinction["mass_light_line_projector_P_L_selected"] is False, "PL")
    require(
        distinction["H7B1G_old_projector_underdetermination_resolved_for_projection_measure_only"]
        is True,
        "projection-only resolution",
    )
    require(
        distinction["H7B1G_old_projector_underdetermination_retained_for_mass_Hessian_light_line"]
        is True,
        "mass underdetermination should remain",
    )

    require(
        hk_gate["status"]
        == "H_K_THRESHOLD_GATE_C5B_C6_SBETA_CLOSED_H_QUARTIC_K_OPEN_9_OF_10",
        "H K status",
    )
    require(hk_gate["accepted_selected_K_source_row_count"] == 9, "H K count")
    require(hk_gate["selected_K_threshold_row_count_required"] == 10, "H K required")
    h_row = hk_gate["H_row"]
    for key in [
        "C5b_projection_measure_equality_emitted",
        "C6_no_extra_boundary_source_term_emitted",
        "selected_metric_quotient_projection_morphism_emitted",
        "selected_finite_reduction_policy_emitted",
        "selected_s_beta_value_found",
    ]:
        require(h_row[key] is True, f"H row should close {key}")
    require(abs(h_row["selected_s_beta_value"] - SBETA_VALUE) < 1e-18, "H row s_beta")
    for key in [
        "selected_H_quartic_functional_emitted",
        "selected_H_threshold_scheme_functional_emitted",
        "selected_dynamic_strain_kernel_emitted",
        "selected_F_H_second_variation_emitted",
        "selected_Hermitian_M_H_values_emitted",
        "selected_Delta_row_emitted",
        "selected_Re_Omega_row_emitted",
        "selected_Im_Omega_row_emitted",
        "K_threshold_Omega_H_lambda_emitted",
    ]:
        require(h_row[key] is False, f"H row overclosed {key}")
    cons = hk_gate["conditional_consequent_current"]
    require(cons["ten_K_antecedent_satisfied"] is False, "ten K")
    require(cons["strict_Omega_lambda_scalar_execution_closed"] is False, "strict scalar")
    require(cons["accepted_internal_scalar_value_row_count"] == 0, "scalar rows")
    require(cons["lambda_H_row_executable"] is False, "lambda executable")

    require(
        cutset["status"] == "NEXT_FRONTIER_H_QUARTIC_THRESHOLD_OR_DYNAMIC_HERM2_ROWS",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "metric-horizontal quotient projection morphism selected",
        "C5b physical Higgs projection-measure equality closed",
        "C6 no-extra-boundary/source proof closed for the finite Higgs projection",
        "uniform finite reduction policy selected",
        "s_beta=tanh(2u)^2 uniform finite trace value promoted",
        "H K-threshold gate remains 9/10",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed missing {phrase}")
    for phrase in [
        "selected H-sector quartic functional",
        "selected H-sector threshold/scheme functional",
        "selected L_rowlocal.Omega_H.lambda and T_scheme.Omega_H.lambda, or direct K_threshold.Omega_H.lambda",
        "selected dynamic strain/response functional F_H with nonzero Herm(2) trace-free part",
        "Delta/Re(Omega)/Im(Omega) dynamic mass-strain rows",
        "strict Omega/lambda_H scalar execution",
    ]:
        require(phrase in cutset["still_open"], f"cutset open missing {phrase}")

    for phrase in [
        "closed `C5b`",
        "closed `C6`",
        f"`s_beta={SBETA_VALUE}`",
        "mass light-line projector",
        "`K_threshold.Omega_H.lambda` still requires",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: C5b/C6 Higgs projection reduction closed; selected s_beta "
        "promoted; dynamic Herm(2) and H K-threshold rows remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
