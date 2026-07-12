"""Audit direct H K-threshold row emission or H quartic functional theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_direcththresholdkrowemission_or_hquarticfunctionaltheorem"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
CROSS_IMPORT = PACKET_DIR / "crossrepo_higgs_h7b1z_import.packet.json"
H_K_ATTEMPT = PACKET_DIR / "h_k_threshold_emission_attempt.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_direct_h_attempt.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_DirectHThresholdKRowEmission_or_HQuarticFunctionalTheorem_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_DIRECTHTHRESHOLDKROWEMISSION_OR_HQUARTICFUNCTIONALTHEOREM_"
    "IMPORTED_H7B1Z_HYM_GRID_EHUV_BINDING_OPEN"
)
NEXT = "MTT_Selected_EHUvBindingTraceIdentityOrDirectHuvRows_to_HKThresholdEmission_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def require_close(value: float, expected: float, message: str) -> None:
    require(abs(float(value) - expected) < 1e-12, message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector violation")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting violation")
    require(packet.get("closure_claimed") is True, f"{label} should close its local import/gate")


def route_by_id(packet: dict, route_id: str) -> dict:
    for route in packet["attempted_routes"]:
        if route["route_id"] == route_id:
            return route
    raise AssertionError(f"missing route {route_id}")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    cross_import = load(CROSS_IMPORT)
    h_k_attempt = load(H_K_ATTEMPT)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("certificate", cert),
        ("cross import", cross_import),
        ("H K attempt", h_k_attempt),
        ("cutset", cutset),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "candidate theorem missing")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(data["full_no_knob_closure_claimed"] is False, "full no-knob overclaim")
    require(cert["true_SM_equivalence_claimed"] is False, "cert true SM overclaim")
    require(cert["full_no_knob_closure_claimed"] is False, "cert full no-knob overclaim")

    decision = data["closure_decision"]
    require(decision["H_source_equation_closed"] is True, "H source equation not closed")
    require(decision["H7B1Z_imported"] is True, "H7B1Z not imported")
    require(decision["HYM_solver_existence_retired_as_H_blocker"] is True, "HYM solver not retired")
    require(decision["direct_H_K_threshold_row_emitted"] is False, "direct H K overemitted")
    require(decision["selected_H_quartic_functional_emitted"] is False, "H quartic overemitted")
    require(decision["selected_E_H_UV_binding_emitted"] is False, "E_H_UV binding overemitted")
    require(decision["selected_projection_measure_equality_emitted"] is False, "projection equality overemitted")
    require(decision["direct_Herm2_Huv_payload_emitted"] is False, "Herm2 payload overemitted")
    require(decision["selected_s_beta_value_found"] is False, "s_beta overselected")
    require(decision["K_threshold_Omega_H_lambda_emitted"] is False, "H K row overemitted")
    require(decision["accepted_selected_K_source_row_count"] == 9, "selected K count mismatch")
    require(decision["selected_K_threshold_row_count_required"] == 10, "required K count mismatch")
    require(decision["ten_K_antecedent_satisfied"] is False, "ten-K antecedent overclosed")
    require(decision["strict_Omega_lambda_scalar_execution_closed"] is False, "Omega/lambda overclosed")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "scalar rows overaccepted")
    require(decision["true_SM_equivalence_closed"] is False, "true SM closure overclaimed")
    require(decision["full_no_knob_closed"] is False, "full no-knob closure overclaimed")

    require(cross_import["status"] == "H7B1Z_IMPORTED_HYM_GRID_RETIRED_EHUV_BINDING_OPEN", "import status")
    require(
        cross_import["imported_status"] == "MTT_CONST_HIGGS_01_H7B1Z_HYM_GRID_PARTIAL_FILL_EHUV_BINDING_OPEN",
        "H7B1Z imported status",
    )
    require(
        cross_import["imported_next"] == "MTT_CONST_HIGGS_01_H7B1ZA_EHUvBindingTraceIdentityOrDirectHuvRows_v1",
        "H7B1Z next mismatch",
    )
    closed = cross_import["closed_or_retired_by_import"]
    require(closed["H7B1Y_schema_ambiguity_retired"] is True, "schema ambiguity not retired")
    require(closed["source_diagonal_HYM_grid_replay_exists"] is True, "HYM grid missing")
    require(closed["computational_uniform_quadrature_exists"] is True, "uniform quadrature missing")
    require(closed["HYM_solver_existence_retired_as_blocker"] is True, "HYM solver blocker not retired")
    require(closed["same_branch_with_H7B1U_grid"] is True, "same branch missing")
    require(closed["selected_source_branch"] == "q79/F,m=1 eta_00 rank-2 V_alpha diagonal T3 HYM lane", "branch mismatch")
    require_close(closed["residual_l2"], 8.208178923714022e-13, "residual mismatch")
    require(closed["node_count"] == 331776, "node count mismatch")
    require(closed["uniform_weight_rational"] == "1/331776", "uniform weight mismatch")
    still = cross_import["still_open_by_import"]
    for key in [
        "actual_E_H_UV_finite_section_source_ids",
        "binding_diagonal_End0_HYM_lane_to_E_H_UV",
        "trace_to_H7B1U_grid_identity_as_physical_projection_measure",
        "no_extra_boundary_source_term_for_Higgs_projection",
        "direct_B_Huv_M_source_or_Huu_Hud_Hdd_values",
        "selected_s_beta",
        "lambda_H",
    ]:
        require(still[key] is True, f"H7B1Z open flag missing {key}")
    diagnostic = cross_import["diagnostic_replay_only"]
    require(diagnostic["conditional_local_formula"] == "tanh(2u)^2", "diagnostic formula")
    require_close(diagnostic["uniform_candidate_s_beta"], 0.004701083905943647, "uniform s_beta")
    require(diagnostic["selected_s_beta_promoted"] is False, "diagnostic s_beta promoted")
    require(diagnostic["accepted_as_physical_Higgs_projection_measure"] is False, "diagnostic measure accepted")

    require(
        h_k_attempt["status"] == "DIRECT_H_K_EMISSION_ATTEMPT_BLOCKED_BY_EHUV_BINDING_OR_HERM2_VALUES",
        "H K attempt status",
    )
    require(h_k_attempt["required_output"] == "K_threshold.Omega_H.lambda", "required output")
    source_eq = h_k_attempt["local_H_source_equation"]
    require(source_eq["direct_K_row"] == "K_threshold.Omega_H.lambda", "source equation direct K")
    require(
        source_eq["split_K_row"]
        == "K_threshold.Omega_H.lambda = L_rowlocal.Omega_H.lambda * T_scheme.Omega_H.lambda",
        "source equation split",
    )

    uniform_route = route_by_id(h_k_attempt, "use_H7B1Z_uniform_trace_as_H_projection_measure")
    require(uniform_route["accepted_as_H_K_source_row"] is False, "uniform route overaccepted")
    require(uniform_route["closed_support"]["source_HYM_grid_payload_emitted"] is True, "uniform HYM support")
    require(uniform_route["closed_support"]["computational_uniform_quadrature_emitted"] is True, "uniform quadrature support")
    require_close(uniform_route["closed_support"]["uniform_candidate_s_beta"], 0.004701083905943647, "uniform route s_beta")
    require("projection_measure_equality" in uniform_route["reason_rejected"], "uniform rejection missing")

    direct_route = route_by_id(h_k_attempt, "direct_Herm2_Huv_rows")
    require(direct_route["accepted_as_H_K_source_row"] is False, "direct Herm2 route overaccepted")
    for key in ["B_Huv", "M_source", "Huu", "Hud", "Hdd", "Delta", "Omega", "P_L", "s_beta"]:
        require(direct_route["attempted_outputs"][key] is None, f"direct output overemitted {key}")
    require("all absent" in direct_route["reason_rejected"], "direct route rejection missing")

    section_route = route_by_id(h_k_attempt, "E_H_UV_section_basis_quadrature_payload")
    require(section_route["accepted_as_H_K_source_row"] is False, "section route overaccepted")
    required_payload = section_route["required_payload"]
    require(required_payload["projection_measure"]["projection_measure_equality"] is None, "projection value should be open")
    require(required_payload["selected_HYM_data"]["Gram_matrix_G_Huv"] is None, "Huv metric should be open")
    require("no selected finite section basis" in section_route["reason_rejected"], "section route rejection missing")

    route_decision = h_k_attempt["route_decision"]
    for key in [
        "direct_H_K_threshold_row_emitted",
        "selected_H_quartic_functional_emitted",
        "selected_E_H_UV_binding_emitted",
        "selected_projection_measure_equality_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "selected_s_beta_value_found",
        "K_threshold_Omega_H_lambda_emitted",
        "ten_K_antecedent_satisfied",
        "strict_Omega_lambda_scalar_execution_closed",
    ]:
        require(route_decision[key] is False, f"route decision overclosed {key}")
    require(route_decision["accepted_selected_K_source_row_count"] == 9, "route selected K count")
    require(route_decision["selected_K_threshold_row_count_required"] == 10, "route required K count")
    require(route_decision["accepted_internal_scalar_value_row_count"] == 0, "route scalar count")
    require(h_k_attempt["next_source_object"]["artifact"] == NEXT, "attempt next mismatch")

    require(cutset["status"] == "NEXT_FRONTIER_EHUV_BINDING_TRACE_IDENTITY_OR_DIRECT_HUV_ROWS_TO_H_K", "cutset status")
    require(cutset["next_required_artifact"] == NEXT, "cutset next mismatch")
    for phrase in [
        "latest constants-repo H7B1Z imported into the H K-row gate",
        "HYM solver existence retired as the active H/lambda blocker",
        "computational uniform quadrature and q79/F,m=1 diagonal HYM grid registered as support",
        "direct H K emission attempted with zero accepted H source rows",
        "direct Herm2 Huv route tested and found values absent",
        "E_H^UV section-basis/quadrature route tested and found binding fields absent",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed missing {phrase}")
    for phrase in [
        "selected E_H^UV section basis/source ids",
        "binding diagonal End0 HYM lane to E_H^UV",
        "trace-to-H7B1U grid identity as physical Higgs projection measure",
        "direct B_Huv+M_source or Huu,Hud,Hdd Herm2 values",
        "selected s_beta or equivalent H quartic/threshold functional",
        "K_threshold.Omega_H.lambda source row",
        "strict Omega/lambda_H scalar execution",
        "selected matrix-level mixing extension and true SM equivalence",
    ]:
        require(phrase in cutset["still_open"], f"cutset open missing {phrase}")

    for phrase in [
        "imported constants-repo H7B1Z",
        "retired HYM solver existence",
        "tested direct `K_threshold.Omega_H.lambda` emission: `false`",
        "ten-K gate remains: `9/10`",
        "binding diagonal End0 HYM lane to `E_H^UV`",
        "selected `s_beta` or equivalent H quartic/threshold functional",
        "selected `K_threshold.Omega_H.lambda`: `false`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
