"""Audit BN27 HYM/End(E) row-scope rejection and full-sector reduction."""

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
BUILDER = ROOT / "scripts" / "build_selected_bn27_hymende_rowscope_acceptance_or_fullsector_devalues.py"

SLUG = "selected_bn27_hymende_rowscope_acceptance_or_fullsector_devalues"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_BN27_HYMEndE_RowScopeAcceptance_or_FullSectorDEValues_v1.md"
ROUTE_A_PACKET = PACKET_DIR / "route_a_rowscope_sufficiency_rejection.packet.json"
ROUTE_B_PACKET = PACKET_DIR / "route_b_reduced_fullsector_validator_payload.packet.json"
GATE_PACKET = PACKET_DIR / "bn27_hymende_final_row_gate_after_rowscope_test.packet.json"
NEXT_PACKET = PACKET_DIR / "next_fullsector_bn27_hymende_validator_payload_contract.packet.json"

STATUS = (
    "MTT_SELECTED_BN27_HYMENDE_ROWSCOPE_ACCEPTANCE_REJECTED_"
    "FULLSECTOR_PAYLOAD_REDUCED"
)
NEXT = "MTT_Selected_FullSectorBN27HYMEndEValidatorPayload_v1"
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
    route_a = load(ROUTE_A_PACKET)
    route_b = load(ROUTE_B_PACKET)
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

    for payload in [candidate, cert, route_a, route_b, gate, next_packet]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    decision = candidate["closure_decision"]
    require(decision["route_A_evaluated"] is True, "Route A not evaluated")
    require(decision["route_A_row_scope_sufficiency_theorem_proved"] is False, "Route A overproved")
    require(decision["route_A_rejected_by_current_validators"] is True, "Route A not rejected")
    require(decision["route_B_fullsector_payload_reduced"] is True, "Route B not reduced")
    require(decision["already_closed_payload_field_count"] == 7, "closed payload count drift")
    require(decision["remaining_fullsector_field_count"] == 5, "remaining fullsector count drift")
    require(decision["two_premise_AH_equivalent_final_connection_tables_accepted"] == 7, "AH count")
    require(decision["HYM_or_EndE_final_row_accepted"] is False, "HYM row overaccepted")
    require(decision["strict_no_knob_closed"] is False, "strict no-knob overclaim")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclaim")

    require(route_a["row"] == FINAL_ROW, "Route A row mismatch")
    require(route_a["route_A_evaluated"] is True, "Route A packet not evaluated")
    require(route_a["route_A_row_scope_sufficiency_theorem_proved"] is False, "Route A packet overproved")
    require(route_a["route_A_rejected_by_current_validators"] is True, "Route A packet not rejected")
    require(route_a["row_scope_representative_available"] is True, "row scope support missing")
    evidence = route_a["validator_evidence"]
    require(evidence["eight_table_HYM_row_accepted"] is False, "eight-table overaccepted")
    require(evidence["first_field_transition_representative_accepted"] is False, "first field overaccepted")
    require(evidence["rtheta_diagonal_HYM_promoted_to_BN27_field"] is False, "Rtheta promoted incorrectly")
    require(evidence["rank2_to_sector_transfer_closed"] is False, "rank2-sector closed unexpectedly")
    require(evidence["actual_QaSU3_operator_packet_promoted"] is False, "Qa/SU3 operator promoted unexpectedly")
    require(evidence["selected_connection_witness_values_absent"] is True, "connection witness should be absent")

    already = route_b["already_closed_for_this_row"]
    for key in [
        "operator_level_projective_rhoE_transition_matrices",
        "selected_diagonal_End0_covariant_D_E",
        "selected_stationary_projector_Riesz_Green_transport",
        "selected_dotD_transport_derivative_formula",
        "same_branch_dotD_alpha1_values",
        "primitive_C1_first_response_layer",
        "source_layer",
    ]:
        require(already[key] is True, f"closed field not imported: {key}")

    remaining = route_b["remaining_fullsector_fields"]
    for key in [
        "rank2_to_rank3_sector_transfer_values",
        "selected_full_sector_covariant_D_E_matrices",
        "coherent_spectral_zero_mode_projectors",
        "full_sector_offdiagonal_End0_control",
        "BN27_final_row_validator_acceptance_certificate",
    ]:
        require(remaining[key] is True, f"remaining field missing: {key}")
    require(route_b["old_fullsector_ledger_context"]["old_required_field_count"] == 10, "old ledger count")
    require("F5_same_branch_dotD_alpha1_transport_derivative" in route_b["old_fullsector_ledger_context"]["superseded_for_bn27_final_row_scope"], "F5 supersession missing")
    require("F7_primitive_C1_overlap_contractions" in route_b["old_fullsector_ledger_context"]["superseded_for_bn27_final_row_scope"], "F7 supersession missing")
    require(len(route_b["minimal_payload_to_emit_next"]) == 5, "minimal payload count")

    require(gate["two_premise_AH_equivalent_final_connection_table_count"] == "7/8", "gate AH count")
    require(gate["route_A_row_scope_sufficiency_rejected"] is True, "gate Route A")
    require(gate["route_B_fullsector_payload_reduced"] is True, "gate Route B")
    require(gate["HYM_or_EndE_final_row_accepted"] is False, "gate HYM overaccepted")
    require(gate["strict_no_knob_closed"] is False, "gate strict overclaim")
    require(gate["true_SM_equivalence_closed"] is False, "gate true SM overclaim")

    require(next_packet["current_lanes"]["two_premise_AH_equivalent_lane"] == "7/8", "next AH lane")
    require(len(next_packet["must_emit"]) == 5, "next must emit count")
    require(any("rank2-to-rank3" in item for item in next_packet["must_emit"]), "rank2 next missing")
    require(any("full-sector covariant" in item for item in next_packet["must_emit"]), "DE next missing")
    require(any("coherent spectral" in item for item in next_packet["must_emit"]), "projector next missing")
    require("same-branch dotD alpha1" in next_packet["must_not_reopen"], "dotD reopen guard missing")
    require("primitive C1 first-response source layer" in next_packet["must_not_reopen"], "C1 reopen guard missing")

    require(cert["route_A_rejected_by_current_validators"] is True, "cert Route A rejection")
    require(cert["route_B_fullsector_payload_reduced"] is True, "cert Route B reduction")
    require(cert["already_closed_payload_field_count"] == 7, "cert closed count")
    require(cert["remaining_fullsector_field_count"] == 5, "cert remaining count")
    require(cert["two_premise_AH_equivalent_final_connection_tables_accepted"] == 7, "cert AH count")
    require(cert["HYM_or_EndE_final_row_accepted"] is False, "cert HYM guard")

    require("Route A is evaluated and rejected" in note, "note Route A")
    require("counted AH-equivalent lane remains `7/8`" in note, "note AH count")
    require("rank2-to-rank3 sector transfer values" in note, "note rank2")
    require(NEXT in note, "note next")

    print("BN27 HYM/EndE row-scope rejection/full-sector reduction audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
