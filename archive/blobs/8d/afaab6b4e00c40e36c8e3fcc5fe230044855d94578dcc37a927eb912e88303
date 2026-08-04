"""Audit E_H^UV finite trace/quadrature C4 bridge closure."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_ehuvquadraturetraceprojectionmeasure_or_directhuvpayload"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
C4_TRACE = PACKET_DIR / "c4_ehuv_finite_trace_quadrature_attachment.packet.json"
BRIDGE_UPDATE = PACKET_DIR / "bridge_validator_c4_update.packet.json"
MEASURE_RECHECK = PACKET_DIR / "projection_measure_identity_recheck_after_c4.packet.json"
DIRECT_RECHECK = PACKET_DIR / "direct_herm2_huv_payload_recheck_after_c4.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_c4_trace.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_c4_trace.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_EHUvQuadratureTraceProjectionMeasure_or_DirectHuvPayload_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_EHUVQUADRATURETRACEPROJECTIONMEASURE_OR_DIRECTHUVPAYLOAD_"
    "C4_FINITE_TRACE_ATTACHED_C5_C6_OPEN"
)
NEXT = "MTT_Selected_EHUvTraceGridProjectionIdentity_or_DirectHuvPayload_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def require_close(value: float, expected: float, message: str, tol: float = 1e-15) -> None:
    require(abs(float(value) - expected) <= tol, message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")
    require(packet.get("closure_claimed") is True, f"{label} closure flag")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    c4 = load(C4_TRACE)
    bridge = load(BRIDGE_UPDATE)
    measure = load(MEASURE_RECHECK)
    direct = load(DIRECT_RECHECK)
    hk_gate = load(HK_GATE)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("C4 trace", c4),
        ("bridge update", bridge),
        ("measure recheck", measure),
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
        "bridge_validator_C4_closed",
        "finite_E_H_UV_quotient_basis_emitted",
        "selected_HYM_metric_or_connection_on_E_H_UV_emitted",
        "quadrature_weights_and_trace_normalization_emitted",
    ]:
        require(decision[key] is True, f"decision should close {key}")
    for key in [
        "bridge_validator_C5_closed",
        "bridge_validator_C6_closed",
        "trace_to_H7B1U_grid_identity_emitted",
        "projection_measure_equality_emitted",
        "accepted_as_physical_Higgs_projection_measure",
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

    require(c4["status"] == "C4_EHUV_FINITE_TRACE_QUADRATURE_ATTACHED", "C4 status")
    require(c4["bridge_clause"] == "C4_quadrature_weights_and_trace_normalization", "C4 clause")
    require(c4["bridge_clause_closed"] is True, "C4 clause closed")
    require("C4 is closed in the bridge-validator sense" in c4["interpretation"], "C4 interpretation")
    require("C5 remains the stronger statement" in c4["interpretation"], "C5 guard")

    trace = c4["finite_trace_quadrature"]
    require(trace["quadrature_rule_id"] == "Q_sel^U:E_H_UV:HYM_grid:Z24^4:normalized_uniform_trace", "rule id")
    require(trace["attached_to_selected_E_H_UV_basis"] is True, "basis attachment")
    require(trace["ordered_E_H_UV_source_ids"]["H_u"] == "Q_sel^U:E_H_UV:H_u:phi_(0,0)_e0", "H_u id")
    require(
        trace["ordered_E_H_UV_source_ids"]["H_d_dagger"]
        == "Q_sel^U:E_H_UV:H_d_dagger:phi_(0,0)_e0",
        "H_d id",
    )
    require(trace["node_count"] == 331776, "node count")
    require(trace["uniform_weight_rational"] == "1/331776", "weight rational")
    require_close(trace["uniform_weight"], 3.0140817901234566e-06, "uniform weight", tol=1e-21)
    require_close(trace["weight_sum"], 1.0, "weight sum")
    require(trace["weight_sum_is_one"] is True, "weight sum flag")
    require(trace["trace_normalization"] == "normalized arithmetic finite trace on the replay mesh", "trace norm")
    require(trace["source_independent_of_target_replay"] is True, "target independence")
    require(trace["finite_Weyl_trace_measure_derived"] is True, "finite Weyl trace")
    require(trace["uniform_reduction_best_current_source_aligned_candidate"] is True, "uniform support")

    blocker = c4["h7b1v_blocker_update_after_c3"]
    require(blocker["old_same_source_metric_bound_to_E_H_UV"] is False, "old metric blocker")
    require(blocker["new_same_source_metric_bound_to_E_H_UV"] is True, "new metric binding")
    require(blocker["trace_to_HYM_grid_binding_closed"] is False, "trace-to-grid overclosed")
    require(blocker["physical_measure_equals_Higgs_projection_measure"] is False, "projection overclosed")
    require(blocker["same_source_no_extra_boundary_or_source_term"] is False, "boundary overclosed")

    reductions = c4["downstream_reduction_candidates_not_promoted"]
    require_close(reductions["uniform_mean_conditional_s_beta"], 0.004701083905943647, "uniform s_beta")
    require_close(reductions["rho_weighted_mean_conditional_s_beta"], 0.01175427147946371, "rho s_beta")
    require_close(
        reductions["exp_density_weighted_mean_conditional_s_beta"],
        0.012349317823559027,
        "exp-density s_beta",
    )
    require(reductions["conditional_local_formula"] == "tanh(2u)^2", "conditional formula")
    require(reductions["selected_reduction_selector_emitted"] is False, "reduction overpromoted")
    require(reductions["selected_s_beta_promoted"] is False, "s_beta overpromoted")

    guards = c4["guardrails"]
    require(guards["quadrature_weights_and_trace_normalization_emitted"] is True, "C4 guard")
    for key in [
        "trace_to_H7B1U_grid_identity_emitted",
        "projection_measure_equality_emitted",
        "accepted_as_physical_Higgs_projection_measure",
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
        "C4_quadrature_weights_and_trace_normalization",
    ]:
        require(clauses[key] is True, f"bridge should close {key}")
    for key in [
        "C5_trace_to_H7B1U_grid_and_projection_measure_identity",
        "C6_no_extra_boundary_or_source_term",
        "B_direct_Herm2_Huv_rows",
    ]:
        require(clauses[key] is False, f"bridge overclosed {key}")
    c4_clause = bridge["clauses"]["C4_quadrature_weights_and_trace_normalization"]
    require(c4_clause["closed"] is True, "C4 clause in bridge")
    for phrase in [
        "331776 nodes",
        "uniform finite trace weight 1/331776",
        "normalized arithmetic finite trace",
    ]:
        require(any(phrase in item for item in c4_clause["evidence"]), f"C4 evidence missing {phrase}")
    for phrase in [
        "trace-to-H7B1U grid identity as physical Higgs projection measure",
        "same-source no-extra-boundary theorem",
        "selected finite reduction scalar s_beta",
        "direct Herm(2) Huv values",
        "K_threshold.Omega_H.lambda",
    ]:
        require(phrase in c4_clause["what_is_not_claimed"], f"C4 guard missing {phrase}")
    bridge_decision = bridge["decision"]
    require(bridge_decision["C4_closed_by_finite_trace_attachment"] is True, "C4 decision")
    require(bridge_decision["C5_C6_remain_required"] is True, "C5-C6 requirement")
    for key in [
        "bridge_validator_complete",
        "direct_Herm2_Huv_payload_emitted",
        "selected_s_beta_promoted",
        "uniform_mean_can_be_promoted_now",
    ]:
        require(bridge_decision[key] is False, f"bridge decision overclosed {key}")

    require(measure["finite_trace_attached"] is True, "measure trace")
    for key in [
        "C5_trace_to_H7B1U_grid_identity_emitted",
        "physical_Higgs_projection_measure_equality_emitted",
        "C6_no_extra_boundary_or_source_term_emitted",
    ]:
        require(measure[key] is False, f"measure overclosed {key}")
    require("C4 supplies the finite normalized trace rule" in measure["reason"], "measure reason")

    for key in ["B_Huv", "M_source", "Huu", "Hud", "Hdd", "Delta", "Omega", "P_L", "s_beta", "lambda_H"]:
        require(direct["actual_outputs"][key] is None, f"direct output overemitted {key}")
    require(direct["C4_trace_changes_direct_Huv_status"] is False, "direct status changed")
    require(direct["accepted_as_H_K_source_row"] is False, "direct accepted")

    h_row = hk_gate["H_row"]
    for key in [
        "ordered_quotient_scaffold_closed",
        "finite_section_source_ids_emitted",
        "section_basis_exactness_certificate_emitted",
        "bridge_validator_C2_closed",
        "selected_HYM_metric_or_connection_on_E_H_UV",
        "quadrature_weights_and_trace_normalization_emitted",
    ]:
        require(h_row[key] is True, f"H row should close {key}")
    for key in [
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
        "C4 finite quadrature weights and trace normalization attached to selected E_H^UV basis",
        "uniform normalized trace weight 1/331776 on 331776 nodes",
        "finite trace rule source-independent of target replay",
        "H K-threshold gate rechecked at 9/10",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed missing {phrase}")
    for phrase in [
        "C5 trace-to-H7B1U grid identity",
        "C5 Higgs projection-measure equality",
        "C6 same-source no-extra-boundary/source theorem",
        "direct B_Huv+M_source or Huu,Hud,Hdd rows",
        "selected s_beta or equivalent H quartic/threshold functional",
        "K_threshold.Omega_H.lambda source row",
        "strict Omega/lambda_H scalar execution",
    ]:
        require(phrase in cutset["still_open"], f"cutset open missing {phrase}")

    for phrase in [
        "closed C4 by attaching finite quadrature weights and trace normalization",
        "Q_sel^U:E_H_UV:HYM_grid:Z24^4:normalized_uniform_trace",
        "uniform normalized trace weight `1/331776`",
        "kept finite Weyl trace uniqueness as source support, not as the C5 physical projection-measure identity",
        "H K-threshold gate remains: `9/10`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
