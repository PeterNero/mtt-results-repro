"""Audit the HYM/End(E) operator-sector cutset after the counted AH lane."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
BUILDER = ROOT / "scripts" / "build_selected_hymende_operatorsector_cutset_after_ahlane.py"

SLUG = "selected_hymende_operatorsector_cutset_after_ahlane"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HYMEndE_OperatorSector_Cutset_After_AHLane_v1.md"
RETIRE_PACKET = PACKET_DIR / "retired_hymende_blockers_after_latest_sector_packets.packet.json"
OPEN_PACKET = PACKET_DIR / "remaining_hymende_operatorsector_value_cutset.packet.json"
GATE_PACKET = PACKET_DIR / "ah_lane_hymende_final_row_gate.packet.json"
NEXT_PACKET = PACKET_DIR / "next_operatorsector_hymende_values_contract.packet.json"

STATUS = (
    "MTT_SELECTED_HYMENDE_OPERATORSECTOR_CUTSET_AFTER_AHLANE_"
    "STALE_BLOCKERS_RETIRED_FINAL_ROW_OPEN"
)
NEXT = "MTT_Selected_OperatorSectorHYMEndEValues_or_ProjectiveRhoEConnection_v1"
FINAL_ROW = "selected_HYM_or_projective_connection_coefficients"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    retire = load(RETIRE_PACKET)
    open_cutset = load(OPEN_PACKET)
    gate = load(GATE_PACKET)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(next_packet["next_required_artifact"] == NEXT, "next packet mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")

    for payload in [candidate, cert, retire, open_cutset, gate, next_packet]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    decision = candidate["closure_decision"]
    require(decision["strict_final_connection_tables_accepted"] == 4, "strict count drifted")
    require(decision["one_premise_final_connection_tables_accepted"] == 6, "one-premise count drifted")
    require(decision["two_premise_AH_equivalent_final_connection_tables_accepted"] == 7, "AH lane count drifted")
    require(decision["HYM_or_EndE_final_row_accepted"] is False, "HYM row overaccepted")
    require(decision["retired_blocker_count"] >= 10, "too few retired blockers")
    require(decision["remaining_operator_sector_value_count"] >= 6, "remaining cutset too small")
    require(decision["strict_no_knob_closed"] is False, "strict no-knob overclaim")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclaim")

    retired = retire["retired_blockers"]
    for key in [
        "diagonal_End0_operator_payload_closed",
        "row_model_offdiagonal_Ext_control_closed",
        "validator_ready_sector_rho_s_packet_closed",
        "selected_projector_promotion_Ps_Ks_closed",
        "selected_stationary_End0_to_sector_routing_values_closed",
        "selected_stationary_rho_s_matrix_values_closed",
        "selected_projective_rhoE_source_level_closed",
        "symbolic_transport_conjugation_validator_closed",
        "stationary_sector_transfer_closed",
    ]:
        require(retired[key] is True, f"retired blocker not closed: {key}")
    require("diagonal_End0_operator_payload" in retire["do_not_reopen_as_final_row_blockers"], "diagonal not retired")
    require("stationary_projectors_Ps_Ks" in retire["do_not_reopen_as_final_row_blockers"], "stationary projectors not retired")

    require(open_cutset["row"] == FINAL_ROW, "open row mismatch")
    require(open_cutset["accepted_as_final_connection_table_row"] is False, "open cutset overaccepted")
    remaining = open_cutset["remaining_operator_sector_values"]
    for key in [
        "operator_level_projective_rhoE_from_selected_connection",
        "selected_rhoE_transition_payload_fullS2_operator_tier",
        "selected_sector_basis_D_E_matrices",
        "selected_sector_basis_Riesz_projectors",
        "selected_sector_basis_Green_operators",
        "selected_sector_basis_dotD_matrices",
        "selected_fullS2_rhoE_D_E_operator_payload",
    ]:
        require(remaining[key] is True, f"remaining value not open: {key}")
    require("diagonal End0 payload alone" in open_cutset["rejected_shortcuts"], "diagonal shortcut not rejected")
    require(
        "source-level projective rho_E without operator-level transition values" in open_cutset["rejected_shortcuts"],
        "rhoE shortcut not rejected",
    )

    require(gate["strict_final_connection_table_count"] == "4/8", "gate strict count")
    require(gate["one_premise_final_connection_table_count"] == "6/8", "gate one-premise count")
    require(gate["two_premise_AH_equivalent_final_connection_table_count"] == "7/8", "gate AH count")
    require(gate["remaining_row"] == FINAL_ROW, "gate remaining row")
    require(gate["HYM_or_EndE_final_row_accepted"] is False, "gate HYM overaccepted")
    require(gate["strict_no_knob_closed"] is False, "gate strict overclaim")
    require(gate["true_SM_equivalence_closed"] is False, "gate true SM overclaim")

    require(next_packet["current_lanes"]["two_premise_AH_equivalent_lane"] == "7/8", "next AH lane")
    require(any("operator-level projective rho_E" in item for item in next_packet["must_emit_next"]), "next rhoE missing")
    require("diagonal_End0_operator_payload" in next_packet["must_not_reopen"], "next must-not-reopen missing")

    require(cert["two_premise_AH_equivalent_final_connection_tables_accepted"] == 7, "cert AH count")
    require(cert["HYM_or_EndE_final_row_accepted"] is False, "cert HYM guard")
    require(cert["retired_blocker_count"] >= 10, "cert retired count")
    require(cert["remaining_operator_sector_value_count"] >= 6, "cert remaining count")
    require(cert["strict_no_knob_closed"] is False, "cert strict guard")
    require(cert["true_SM_equivalence_closed"] is False, "cert true SM guard")

    require("counted AH-equivalent lane: `7/8`" in note, "note AH count")
    require("The final row remains open" in note, "note final row")
    require("diagonal End0 HYM payload" in note, "note retired diagonal")
    require(NEXT in note, "note next")

    print("HYM/EndE operator-sector cutset after AH lane audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
