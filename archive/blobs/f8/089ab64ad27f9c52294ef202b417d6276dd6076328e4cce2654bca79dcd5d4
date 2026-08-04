"""Audit Step50 selected operator-payload owner theorem reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step50_operatorpayload_owner_theorem_or_omega_clauseclosure"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SUPPORT = PACKET_DIR / "step50_operator_payload_support_consolidation.packet.json"
ROW_LEDGER = PACKET_DIR / "step50_operator_payload_promotion_row_ledger.packet.json"
OMEGA_RECHECK = PACKET_DIR / "step50_omega_operator_clause_recheck.packet.json"
NEXT_FRONTIER = PACKET_DIR / "step50_next_operator_payload_frontier.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step50_OperatorPayloadOwnerTheorem_or_OmegaClauseClosure_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP50_OPERATORPAYLOAD_OWNER_THEOREM_REDUCED_SECTOR_ROWS_OPEN"
NEXT = "MTT_Selected_End0SectorTransfer_ProjectorPromotion_or_RhoEDEOperatorValues_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    support = load(SUPPORT)
    rows = load(ROW_LEDGER)
    omega = load(OMEGA_RECHECK)
    frontier = load(NEXT_FRONTIER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "reduction theorem not proved")

    for packet in [data, support, rows, omega, frontier, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    closed = support["closed_do_not_reopen"]
    for key in [
        "dotD_alpha1_payload",
        "visible_routec_operator_source",
        "functional_PhiFin_trace",
        "same_branch_alpha1_derivative",
        "transport_closed_validator_replay",
        "validator_ready_sector_rho_s_packet",
        "diagonal_End0_operator_payload",
        "static_matter_slot_source_tier",
    ]:
        require(closed[key] is True, f"closed support missing: {key}")
    require(len(support["not_enough_for_omega"]) == 4, "support warning count mismatch")

    require(rows["row_count"] == 11, "promotion row count mismatch")
    require(rows["selected_row_count"] == 3, "selected support row count mismatch")
    require(rows["support_only_row_count"] == 8, "support-only row count mismatch")
    require(rows["operator_payload_closed"] is False, "operator payload overclosed")
    row_ids = {row["row_id"] for row in rows["promotion_rows"]}
    for key in [
        "selected_End0_to_sector_routing_values",
        "selected_P_s_K_s_projector_promotion_values",
        "selected_rho_E_transition_payload",
        "selected_D_E_Riesz_Green_dotD_sector_matrices",
        "dynamic_PhiFin_C1_payload_rows",
        "actual_QaSU3_operator_payload",
    ]:
        require(key in row_ids, f"missing promotion row: {key}")
    for item in rows["promotion_rows"]:
        if item["row_id"] in {
            "sector_projectors_dotD_alpha1",
            "diagonal_End0_operator_payload",
            "functional_PhiFin_trace_and_transport",
        }:
            require(item["selected_now"] is True, f"closed support not selected: {item['row_id']}")
        else:
            require(item["selected_now"] is False, f"support-only row overselected: {item['row_id']}")

    require(omega["omega_clause"] == "selected_higher_response_operator_payload", "wrong omega clause")
    require(omega["selected_higher_response_operator_payload_closed"] is False, "omega clause overclosed")
    require(omega["full_S2_value_execution_ready"] is False, "full S2 overready")
    require(omega["accepted_scalar_row_count_now"] == 0, "scalar rows overaccepted")

    require(frontier["next_required_artifact"] == NEXT, "frontier next mismatch")
    for key in [
        "operator_payload_support_consolidated",
        "promotion_row_ledger_filled",
        "dotD_alpha1_diagonal_End0_PhiFin_trace_support_locked",
        "omega_operator_clause_rechecked",
    ]:
        require(frontier["closed_now"][key] is True, f"frontier close missing: {key}")
    require(len(frontier["must_emit_next"]) >= 5, "must emit list too small")

    decision = data["closure_decision"]
    require(decision["operator_payload_support_consolidated"] is True, "decision support missing")
    require(decision["operator_payload_promotion_row_ledger_filled"] is True, "decision ledger missing")
    for key in [
        "selected_higher_response_operator_payload_closed",
        "full_S2_value_execution_closed",
        "selected_lambda_H_row_closed",
        "minimal_parameter_closure_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"candidate overclosed: {key}")
        require(cert[key] is False, f"certificate overclosed: {key}")
    require(decision["accepted_internal_Rtheta_coefficient_row_count"] == 0, "Rtheta rows overaccepted")
    require(decision["accepted_internal_scalar_row_count"] == 0, "scalar rows overaccepted")
    require(data["minimal_parameter_closure_claimed"] is False, "minimal closure overclaimed")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaimed")

    for phrase in [
        "promotion rows filled                  : 11",
        "selected support rows                  : 3",
        "support-only/open rows                 : 8",
        "Omega operator clause closed           : false",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
