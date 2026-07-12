"""Audit E_H^UV HYM metric/connection C3 bridge closure."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_ehuvhymmetricconnectionfixedpoint_or_directhuvpayload"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
C3_BINDING = PACKET_DIR / "c3_ehuv_hym_metric_connection_binding.packet.json"
BRIDGE_UPDATE = PACKET_DIR / "bridge_validator_c3_update.packet.json"
DIRECT_RECHECK = PACKET_DIR / "direct_herm2_huv_payload_recheck_after_c3.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_c3_metric.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_c3_metric.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_EHUvHYMMetricConnectionFixedPoint_or_DirectHuvPayload_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_EHUVHYMMETRICCONNECTIONFIXEDPOINT_OR_DIRECTHUVPAYLOAD_"
    "C3_DIAGONAL_METRIC_BOUND_C4_C6_OPEN"
)
NEXT = "MTT_Selected_EHUvQuadratureTraceProjectionMeasure_or_DirectHuvPayload_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def require_close(value: float, expected: float, message: str) -> None:
    require(abs(float(value) - expected) < 1e-12, message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")
    require(packet.get("closure_claimed") is True, f"{label} closure flag")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    binding = load(C3_BINDING)
    bridge = load(BRIDGE_UPDATE)
    direct = load(DIRECT_RECHECK)
    hk_gate = load(HK_GATE)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("C3 binding", binding),
        ("bridge update", bridge),
        ("direct recheck", direct),
        ("H K gate", hk_gate),
        ("cutset", cutset),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "certificate next")
    require(data["theorem"]["proved"] is True, "theorem flag")
    require(cert["theorem_proved"] is True, "cert theorem flag")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")

    decision = data["closure_decision"]
    for key in [
        "bridge_validator_C1_closed",
        "bridge_validator_C2_closed",
        "bridge_validator_C3_closed",
        "finite_E_H_UV_quotient_basis_emitted",
        "selected_HYM_metric_or_connection_on_E_H_UV_emitted",
    ]:
        require(decision[key] is True, f"decision should close {key}")
    for key in [
        "bridge_validator_C4_closed",
        "bridge_validator_C5_closed",
        "bridge_validator_C6_closed",
        "quadrature_weights_and_trace_normalization_emitted",
        "trace_to_H7B1U_grid_identity_emitted",
        "projection_measure_equality_emitted",
        "no_extra_boundary_source_term_for_Higgs_projection",
        "direct_Herm2_Huv_payload_emitted",
        "selected_minimal_lift_rule_emitted",
        "selected_rank_one_light_projector_emitted",
        "selected_s_beta_value_found",
        "K_threshold_Omega_H_lambda_emitted",
        "ten_K_antecedent_satisfied",
        "strict_Omega_lambda_scalar_execution_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
    require(decision["accepted_selected_K_source_row_count"] == 9, "K selected count")
    require(decision["selected_K_threshold_row_count_required"] == 10, "K required count")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "scalar count")

    require(binding["status"] == "C3_EHUV_DIAGONAL_HYM_METRIC_CONNECTION_FIXED_POINT_BOUND", "binding status")
    require(binding["bridge_clause_closed"] is True, "C3 binding flag")
    changed = binding["what_changed_since_H7B1Z"]
    require(changed["C2_finite_basis_now_emitted"] is True, "C2 basis not used")
    require(changed["binding_scope"] == "C3 metric/connection only", "binding scope")
    require(
        changed["C2_source_ids"]
        == [
            "Q_sel^U:E_H_UV:H_u:phi_(0,0)_e0",
            "Q_sel^U:E_H_UV:H_d_dagger:phi_(0,0)_e0",
        ],
        "C2 source ids",
    )

    basis = binding["basis_binding"]
    require(
        basis["ordered_E_H_UV_source_ids"]["H_u"] == "Q_sel^U:E_H_UV:H_u:phi_(0,0)_e0",
        "H_u id",
    )
    require(
        basis["ordered_E_H_UV_source_ids"]["H_d_dagger"]
        == "Q_sel^U:E_H_UV:H_d_dagger:phi_(0,0)_e0",
        "H_d id",
    )
    eig = basis["T3_eigenline_identification"]
    require(eig["H_u"]["T3_eigenvalue"] == "+1", "H_u eigenvalue")
    require(eig["H_u"]["metric_entry"] == "exp(u)", "H_u metric")
    require(eig["H_u"]["connection_entry"] == "+du", "H_u connection")
    require(eig["H_d_dagger"]["T3_eigenvalue"] == "-1", "H_d eigenvalue")
    require(eig["H_d_dagger"]["metric_entry"] == "exp(-u)", "H_d metric")
    require(eig["H_d_dagger"]["connection_entry"] == "-du", "H_d connection")
    require(basis["D_term_involution_alignment"]["projector_or_s_beta_promoted"] is False, "D-term overpromotion")

    metric = binding["metric_connection_fixed_point"]
    require(metric["metric_on_E_H_UV_basis"] == "diag(exp(u), exp(-u)) in the selected diagonal End0 lane", "metric formula")
    require(metric["connection_on_E_H_UV_basis"] == "A_diag = d u * T3 in the selected diagonal End0 lane", "connection formula")
    require(metric["determinant_one"] == "exp(u)*exp(-u)=1 pointwise", "det one")
    require(metric["fixed_point_converged"] is True, "fixed point convergence")
    require(metric["observed_target_inputs_used"] is False, "observed target input")
    require_close(metric["residual_l2"], 8.208178923714022e-13, "residual")
    summary = metric["solution_summary"]
    require_close(summary["final_residual_l2"], 8.208178923714022e-13, "summary residual")
    require_close(summary["u_max"], 0.04562175016803212, "u max")
    require_close(summary["u_min"], -0.09129255457956154, "u min")
    require_close(summary["u_l2"], 0.03443643655279868, "u l2")

    conditional = binding["conditional_downstream_formula_available_not_promoted"]
    require(conditional["minimal_lift_formula_proved"] is True, "minimal lift formula")
    require(conditional["metric_candidate"] == ["exp(u)", "exp(-u)"], "metric candidate")
    require(conditional["conditional_local_s_beta"] == "tanh(2u)^2", "conditional s_beta")
    for key in [
        "selected_minimal_lift_promoted",
        "selected_rank_one_projector_promoted",
        "selected_s_beta_promoted",
        "finite_scalar_reduction_emitted",
    ]:
        require(conditional[key] is False, f"conditional overpromoted {key}")

    guards = binding["guardrails"]
    require(guards["selected_HYM_metric_or_connection_on_E_H_UV_emitted"] is True, "metric guard")
    for key in [
        "quadrature_weights_and_trace_normalization_emitted",
        "trace_to_H7B1U_grid_identity_emitted",
        "projection_measure_equality_emitted",
        "same_source_no_extra_boundary_source_proof_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "selected_minimal_lift_rule_emitted",
        "selected_rank_one_light_projector_emitted",
        "selected_s_beta_promoted",
        "K_threshold_Omega_H_lambda_emitted",
    ]:
        require(guards[key] is False, f"guard overclosed {key}")

    clauses = bridge["clause_status"]
    for key in [
        "C1_branch_and_ordered_channel_labels",
        "C2_typed_E_H_UV_section_basis_or_finite_quotient",
        "C3_selected_HYM_metric_or_connection_fixed_point",
    ]:
        require(clauses[key] is True, f"bridge should close {key}")
    for key in [
        "C4_quadrature_weights_and_trace_normalization",
        "C5_trace_to_H7B1U_grid_and_projection_measure_identity",
        "C6_no_extra_boundary_or_source_term",
        "B_direct_Herm2_Huv_rows",
    ]:
        require(clauses[key] is False, f"bridge overclosed {key}")
    c3_clause = bridge["clauses"]["C3_selected_HYM_metric_or_connection_fixed_point"]
    require(c3_clause["closed"] is True, "C3 clause")
    for phrase in [
        "finite quadrature weights as physical Higgs projection measure",
        "trace-to-H7B1U grid identity",
        "same-source no-extra-boundary theorem",
        "rank-one light projector P_L",
        "selected s_beta or lambda_H",
        "direct Herm(2) Huv values",
    ]:
        require(phrase in c3_clause["what_is_not_claimed"], f"C3 guard missing {phrase}")
    bridge_decision = bridge["decision"]
    require(bridge_decision["C3_closed_by_diagonal_metric_binding"] is True, "C3 decision")
    require(bridge_decision["C4_to_C6_remain_required"] is True, "C4-C6 requirement")
    for key in [
        "bridge_validator_complete",
        "direct_Herm2_Huv_payload_emitted",
        "selected_s_beta_promoted",
        "uniform_mean_can_be_promoted_now",
    ]:
        require(bridge_decision[key] is False, f"bridge decision overclosed {key}")

    for key in ["B_Huv", "M_source", "Huu", "Hud", "Hdd", "Delta", "Omega", "P_L", "s_beta", "lambda_H"]:
        require(direct["actual_outputs"][key] is None, f"direct output overemitted {key}")
    require(direct["C3_metric_changes_direct_Huv_status"] is False, "direct status changed")
    require(direct["accepted_as_H_K_source_row"] is False, "direct accepted")

    h_row = hk_gate["H_row"]
    for key in [
        "ordered_quotient_scaffold_closed",
        "finite_section_source_ids_emitted",
        "section_basis_exactness_certificate_emitted",
        "bridge_validator_C2_closed",
        "selected_HYM_metric_or_connection_on_E_H_UV",
    ]:
        require(h_row[key] is True, f"H row should close {key}")
    for key in [
        "quadrature_weights_and_trace_normalization_emitted",
        "trace_to_H7B1U_grid_identity_emitted",
        "projection_measure_equality_emitted",
        "no_extra_boundary_source_term_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "selected_s_beta_value_found",
        "K_threshold_Omega_H_lambda_emitted",
    ]:
        require(h_row[key] is False, f"H row overclosed {key}")
    require(hk_gate["accepted_selected_K_source_row_count"] == 9, "HK count")
    require(hk_gate["selected_K_threshold_row_count_required"] == 10, "HK required")
    current = hk_gate["conditional_consequent_current"]
    require(current["ten_K_antecedent_satisfied"] is False, "ten K overclosed")
    require(current["strict_Omega_lambda_scalar_execution_closed"] is False, "strict scalar overclosed")
    require(current["accepted_internal_scalar_value_row_count"] == 0, "scalar rows")

    for phrase in [
        "C3 selected E_H^UV HYM metric/connection fixed point bound",
        "selected diagonal HYM metric diag(exp(u),exp(-u)) attached to H_u/H_d^dagger source IDs",
        "selected diagonal connection A_diag=du*T3 attached to the E_H^UV basis",
        "H K-threshold gate rechecked at 9/10",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed missing {phrase}")
    for phrase in [
        "C4 finite quadrature weights and trace normalization as selected Higgs projection measure",
        "C5 trace-to-H7B1U grid identity and Higgs projection-measure equality",
        "C6 same-source no-extra-boundary/source theorem",
        "direct B_Huv+M_source or Huu,Hud,Hdd rows",
        "selected minimal lift or rank-one light projector P_L",
        "selected s_beta or equivalent H quartic/threshold functional",
        "K_threshold.Omega_H.lambda source row",
        "strict Omega/lambda_H scalar execution",
    ]:
        require(phrase in cutset["still_open"], f"cutset open missing {phrase}")

    for phrase in [
        "closed C3 by binding the selected diagonal HYM fixed-point metric",
        "attached `diag(exp(u),exp(-u))`",
        "attached connection `A_diag=du*T3`",
        "H K-threshold gate remains: `9/10`",
        "C4 finite quadrature weights and trace normalization",
        "selected `K_threshold.Omega_H.lambda`: `false`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
