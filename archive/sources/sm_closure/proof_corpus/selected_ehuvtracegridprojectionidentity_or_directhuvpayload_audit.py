"""Audit the E_H^UV trace-grid projection identity split packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_ehuvtracegridprojectionidentity_or_directhuvpayload"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
TRACE_ID = PACKET_DIR / "c5a_trace_grid_identity.packet.json"
MEASURE_GATE = PACKET_DIR / "c5b_projection_measure_gate.packet.json"
DIRECT_RECHECK = PACKET_DIR / "direct_hresponse_huv_table_recheck_after_c5a.packet.json"
BRIDGE_UPDATE = PACKET_DIR / "bridge_validator_c5a_update.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_c5a_trace_identity.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_c5a_trace_identity.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_EHUvTraceGridProjectionIdentity_or_DirectHuvPayload_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_EHUVTRACEGRIDPROJECTIONIDENTITY_OR_DIRECTHUVPAYLOAD_"
    "C5A_TRACE_GRID_IDENTITY_CLOSED_PROJECTION_BOUNDARY_DIRECT_OPEN"
)
NEXT = "MTT_Selected_EHUvProjectionMeasureNoBoundary_or_HResponseHuvTable_v1"


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
    trace_id = load(TRACE_ID)
    measure_gate = load(MEASURE_GATE)
    direct = load(DIRECT_RECHECK)
    bridge = load(BRIDGE_UPDATE)
    hk_gate = load(HK_GATE)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("trace identity", trace_id),
        ("measure gate", measure_gate),
        ("direct recheck", direct),
        ("bridge update", bridge),
        ("H K gate", hk_gate),
        ("cutset", cutset),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "certificate next")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "cert theorem")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(cert["true_SM_equivalence_claimed"] is False, "cert true SM overclaim")
    require(cert["full_no_knob_closure_claimed"] is False, "cert no-knob overclaim")

    decision = data["closure_decision"]
    for key in [
        "bridge_validator_C1_closed",
        "bridge_validator_C2_closed",
        "bridge_validator_C3_closed",
        "bridge_validator_C4_closed",
        "bridge_validator_C5a_trace_grid_identity_closed",
        "B_Huv_two_column_uv_lift_emitted",
        "M_H_three_row_source_functional_contract_closed",
    ]:
        require(decision[key] is True, f"decision should close {key}")
    for key in [
        "bridge_validator_C5b_projection_measure_equality_closed",
        "bridge_validator_C6_no_boundary_closed",
        "selected_H_response_table_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "selected_Delta_row_emitted",
        "selected_Re_Omega_row_emitted",
        "selected_Im_Omega_row_emitted",
        "selected_s_beta_value_found",
        "K_threshold_Omega_H_lambda_emitted",
        "ten_K_antecedent_satisfied",
        "strict_Omega_lambda_scalar_execution_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
    require(decision["accepted_selected_K_source_row_count"] == 9, "selected K count")
    require(decision["selected_K_threshold_row_count_required"] == 10, "required K count")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "scalar count")

    require(trace_id["status"] == "C5A_TRACE_TO_H7B1U_GRID_IDENTITY_CLOSED", "trace status")
    require(trace_id["proved"] is True, "trace identity not proved")
    checks = trace_id["identity_checks"]
    for key in [
        "attached_to_selected_E_H_UV_basis",
        "same_node_count",
        "same_nodes_or_grid",
        "same_selected_source_branch",
        "same_source_independent_of_target_replay",
        "same_trace_normalization",
        "same_uniform_weight_rational",
        "weight_sum_is_one",
    ]:
        require(checks[key] is True, f"trace identity check failed {key}")
    require(
        checks["same_source_branch_label"]
        == "q79/F,m=1 eta_00 rank-2 V_alpha diagonal T3 HYM lane",
        "branch label",
    )
    require(trace_id["quadrature_rule_id"] == "Q_sel^U:E_H_UV:HYM_grid:Z24^4:normalized_uniform_trace", "quadrature id")
    require(trace_id["node_count"] == 331776, "node count")
    require(trace_id["uniform_weight_rational"] == "1/331776", "weight")
    require(trace_id["ordered_E_H_UV_source_ids"]["H_u"].startswith("Q_sel^U:E_H_UV:H_u"), "H_u source id")
    require(trace_id["ordered_E_H_UV_source_ids"]["H_d_dagger"].startswith("Q_sel^U:E_H_UV:H_d_dagger"), "H_d source id")
    for key, value in trace_id["not_claimed"].items():
        require(value is False, f"trace identity overclaimed {key}")

    require(
        measure_gate["status"]
        == "C5B_PHYSICAL_PROJECTION_MEASURE_EQUALITY_OPEN_AFTER_TRACE_GRID_IDENTITY",
        "measure status",
    )
    require(measure_gate["C5a_trace_to_H7B1U_grid_identity_closed"] is True, "C5a not imported")
    require(measure_gate["C5b_physical_Higgs_projection_measure_equality_emitted"] is False, "C5b overclosed")
    require(measure_gate["C6_no_extra_boundary_or_source_term_emitted"] is False, "C6 overclosed")
    open_fields = measure_gate["open_physical_fields"]
    require(open_fields["accepted_as_physical_Higgs_projection_measure"] is False, "physical measure overaccepted")
    require(open_fields["projection_measure_equality"] is False, "projection equality overclosed")
    require(open_fields["selected_s_beta_promoted"] is False, "s_beta overpromoted")
    require(open_fields["trace_to_H7B1U_grid_identity_as_physical_projection_measure"] is True, "physical trace obligation missing")
    require(measure_gate["diagnostic_values_not_promoted"]["conditional_local_formula"] == "tanh(2u)^2", "diagnostic formula")
    require(
        abs(measure_gate["diagnostic_values_not_promoted"]["uniform_candidate_s_beta"] - 0.004701083905943647)
        < 1e-15,
        "diagnostic uniform s_beta",
    )
    require("not merely the attached computational trace" in measure_gate["why_C5_not_fully_closed"], "C5b reason")

    require(direct["status"] == "BHUV_DOMAIN_AND_FUNCTIONAL_CLOSED_HRESPONSE_HUV_TABLE_STILL_OPEN", "direct status")
    require(direct["B_Huv_two_column_lift_emitted"] is True, "B_Huv missing")
    require(direct["B_Huv_symbolic_exact_payload_emitted"] is True, "B_Huv exact missing")
    require(direct["M_H_three_row_functional_closed"] is True, "three-row functional missing")
    require(direct["direct_Herm2_Huv_payload_emitted"] is False, "direct Huv overemitted")
    require(direct["selected_H_response_table_emitted"] is False, "H response table overemitted")
    require(direct["M_source_emitted"] is False, "M_source overemitted")
    for key, value in direct["required_table"].items():
        require(value is None, f"required table overfilled {key}")
    for key, value in direct["values_emitted_now"].items():
        require(value is None, f"value overemitted {key}")
    require("no longer missing the domain or extraction map" in direct["refined_direct_blocker"], "direct blocker refinement")

    require(bridge["status"] == "BRIDGE_VALIDATOR_C1_C2_C3_C4_C5A_CLOSED_C5B_C6_DIRECT_OPEN", "bridge status")
    clause_status = bridge["clause_status"]
    for key in [
        "C1_branch_and_ordered_channel_labels",
        "C2_typed_E_H_UV_section_basis_or_finite_quotient",
        "C3_selected_HYM_metric_or_connection_fixed_point",
        "C4_quadrature_weights_and_trace_normalization",
        "C5a_trace_to_H7B1U_grid_identity",
    ]:
        require(clause_status[key] is True, f"bridge clause should close {key}")
    for key in [
        "C5b_physical_Higgs_projection_measure_equality",
        "C6_no_extra_boundary_or_source_term",
        "B_direct_Herm2_Huv_rows",
    ]:
        require(clause_status[key] is False, f"bridge clause overclosed {key}")
    bridge_decision = bridge["decision"]
    require(bridge_decision["bridge_validator_complete"] is False, "bridge complete overclaim")
    require(bridge_decision["C5a_trace_grid_identity_closed"] is True, "C5a decision")
    require(bridge_decision["C5_full_closed"] is False, "C5 full overclaim")
    require(bridge_decision["C6_closed"] is False, "C6 decision")
    require(bridge_decision["K_threshold_Omega_H_lambda_emitted"] is False, "K row overemitted")

    require(
        hk_gate["status"] == "H_K_THRESHOLD_GATE_C5A_CLOSED_PROJECTION_BOUNDARY_VALUES_OPEN_9_OF_10",
        "H K status",
    )
    require(hk_gate["accepted_selected_K_source_row_count"] == 9, "H K selected")
    require(hk_gate["selected_K_threshold_row_count_required"] == 10, "H K required")
    h_row = hk_gate["H_row"]
    require(h_row["trace_to_H7B1U_grid_identity_emitted"] is True, "H row trace identity")
    require(h_row["C5a_trace_grid_identity_closed"] is True, "H row C5a")
    for key in [
        "C5b_projection_measure_equality_emitted",
        "no_extra_boundary_source_term_emitted",
        "K_threshold_Omega_H_lambda_emitted",
        "selected_H_response_table_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "selected_s_beta_value_found",
    ]:
        require(h_row[key] is False, f"H row overclosed {key}")
    current = hk_gate["conditional_consequent_current"]
    require(current["ten_K_antecedent_satisfied"] is False, "ten-K overclosed")
    require(current["strict_Omega_lambda_scalar_execution_closed"] is False, "scalar execution overclosed")
    require(current["accepted_internal_scalar_value_row_count"] == 0, "scalar rows")

    require(
        cutset["status"] == "NEXT_FRONTIER_PROJECTION_MEASURE_NO_BOUNDARY_OR_HRESPONSE_HUV_TABLE",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "C5a computational trace-to-H7B1U grid identity",
        "bridge validator split into C5a closed versus C5b/C6 open",
        "B_Huv/domain and Pauli/Riesz three-row functional retained closed",
        "direct H_response/Huv table rechecked with domain closed and values absent",
        "H K-threshold gate remains 9/10",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed missing {phrase}")
    for phrase in [
        "C5b physical Higgs projection-measure equality",
        "C6 same-source no-extra-boundary/source theorem",
        "selected H_response/Huv table values Huu,Hud,Hdd",
        "or full same-source M_source+R_H restriction",
        "selected s_beta or equivalent H quartic/threshold functional",
        "K_threshold.Omega_H.lambda source row",
        "strict Omega/lambda_H scalar execution",
    ]:
        require(phrase in cutset["still_open"], f"cutset open missing {phrase}")

    for phrase in [
        "split C5 into `C5a` trace-grid identity",
        "closed `C5a`",
        "rechecked direct route with `B_Huv`",
        "H K-threshold gate remains `9/10`",
        "`C5b` physical Higgs projection-measure equality",
        "selected `K_threshold.Omega_H.lambda`: `false`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: E_H^UV C5a trace-grid identity is closed; "
        "C5b/C6 and H_response/Huv values remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
