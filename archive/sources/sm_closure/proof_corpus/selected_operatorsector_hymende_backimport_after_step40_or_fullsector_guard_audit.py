"""Audit Step38-Step40 HYM/End(E) backimport and full-sector guard."""

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
BUILDER = ROOT / "scripts" / "build_selected_operatorsector_hymende_backimport_after_step40_or_fullsector_guard.py"

SLUG = "selected_operatorsector_hymende_backimport_after_step40_or_fullsector_guard"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_OperatorSector_HYMEndE_Backimport_AfterStep40_or_FullSectorGuard_v1.md"
IMPORT_PACKET = PACKET_DIR / "step38_step40_operatorsector_backimport.packet.json"
GATE_PACKET = PACKET_DIR / "bn27_hymende_row_scope_gate_after_step40.packet.json"
REMAINING_PACKET = PACKET_DIR / "remaining_fullsector_or_rowscope_sufficiency_cutset.packet.json"
NEXT_PACKET = PACKET_DIR / "next_bn27_hymende_rowscope_or_fullsector_contract.packet.json"

STATUS = (
    "MTT_SELECTED_OPERATORSECTOR_HYMENDE_BACKIMPORT_AFTER_STEP40_"
    "ROW_SCOPE_GUARD_FULLSECTOR_OPEN"
)
NEXT = "MTT_Selected_BN27HYMEndERowScopeAcceptance_or_FullSectorDEValues_v1"
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
    import_packet = load(IMPORT_PACKET)
    gate = load(GATE_PACKET)
    remaining = load(REMAINING_PACKET)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(next_packet["next_required_artifact"] == NEXT, "next packet mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")

    for payload in [candidate, cert, import_packet, gate, remaining, next_packet]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    imported = import_packet["imported_operator_values"]
    for key in [
        "operator_level_projective_rhoE_transition_matrices_closed",
        "nonidentity_projective_rhoE_selected_up_to_unitary_gauge",
        "step38_packet_numeric_gate_passes",
        "selected_diagonal_End0_covariant_D_E_closed",
        "selected_stationary_projector_Riesz_Green_transport_closed",
        "step39_operator_formula_present",
        "selected_dotD_transport_derivative_formula_closed",
        "selected_alpha1_driver_normalization_closed",
        "same_branch_dotD_alpha1_values_closed",
        "honest_dotD_alpha1_replay_closed",
        "step40_validator_math_passes",
        "source_layer_closed",
        "A_selected_closed_by_active_ledger",
        "b_selected_closed_by_active_ledger",
        "deltaTheta_C1_closed_by_active_ledger",
        "primitive_C1_first_response_layer_closed_by_active_ledger",
        "active_decision_supersedes_primitive_C1_open_wording",
        "formal_110_rows_executed",
    ]:
        require(imported[key] is True, f"imported value not closed: {key}")

    require(import_packet["selected_representatives"]["D_E_formula"] == "D_E = d + du ad(T3)", "D_E formula")
    require(import_packet["selected_representatives"]["rhoE_active_generators"] == ["g1", "g2"], "rhoE active")
    require(len(import_packet["old_operator_subblockers_retired"]) == 5, "retired subblocker count")
    require("same-branch dotD alpha1 transport" in import_packet["old_operator_subblockers_retired"], "dotD not retired")

    decision = candidate["closure_decision"]
    require(decision["imported_operator_value_count"] == len(imported), "import count mismatch")
    require(decision["old_operator_subblockers_retired_count"] == 5, "candidate retired count")
    require(decision["row_scope_diagonal_projective_EndE_representative_available"] is True, "row scope unavailable")
    require(decision["row_scope_sufficiency_theorem_proved"] is False, "row-scope theorem overclaimed")
    require(decision["full_sector_validator_ready"] is False, "full-sector overclaimed")
    require(decision["two_premise_AH_equivalent_final_connection_tables_accepted"] == 7, "AH lane count")
    require(decision["HYM_or_EndE_final_row_accepted"] is False, "HYM row overaccepted")
    require(decision["strict_no_knob_closed"] is False, "strict no-knob overclaim")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclaim")

    require(gate["row"] == FINAL_ROW, "gate row mismatch")
    require(gate["two_premise_AH_equivalent_final_connection_table_count"] == "7/8", "gate AH lane")
    require(gate["row_scope_diagonal_projective_EndE_representative_available"] is True, "gate representative")
    require(gate["row_scope_sufficiency_theorem_proved"] is False, "gate row-scope overclaim")
    require(gate["full_sector_validator_ready"] is False, "gate full-sector overclaim")
    require(gate["HYM_or_EndE_final_row_accepted"] is False, "gate row overaccepted")

    open_items = remaining["remaining_open_items"]
    for key in [
        "selected_full_sector_covariant_D_E_matrices",
        "coherent_spectral_zero_mode_projectors",
        "rank2_to_rank3_sector_transfer_values",
        "full_sector_offdiagonal_End0_control",
        "accepted_internal_scalar_rows",
        "accepted_value_functional_rows",
        "BN27_row_scope_sufficiency_theorem",
        "BN27_final_row_validator_acceptance_certificate",
    ]:
        require(open_items[key] is True, f"remaining item missing: {key}")
    require("route_A_row_scope_sufficiency" in remaining["two_legal_routes"], "Route A missing")
    require("route_B_full_sector_validator_payload" in remaining["two_legal_routes"], "Route B missing")
    require("reopening projective rho_E transition after Step38" in remaining["forbidden_loops"], "rhoE loop guard")
    require("reopening dotD/alpha1 after Step40 and the active ledger" in remaining["forbidden_loops"], "dotD loop guard")

    require(next_packet["current_lanes"]["two_premise_AH_equivalent_lane"] == "7/8", "next AH lane")
    require("route_A_row_scope_sufficiency" in next_packet["must_choose_one_route"], "next Route A")
    require("route_B_full_sector_validator_payload" in next_packet["must_choose_one_route"], "next Route B")
    require(any("BN27 final-row acceptance certificate" in item for item in next_packet["route_A_minimal_theorem"]), "Route A cert")
    require(any("coherent spectral zero-mode projectors" in item for item in next_packet["route_B_minimal_payload"]), "Route B projectors")

    require(cert["row_scope_diagonal_projective_EndE_representative_available"] is True, "cert representative")
    require(cert["row_scope_sufficiency_theorem_proved"] is False, "cert row-scope guard")
    require(cert["full_sector_validator_ready"] is False, "cert full-sector guard")
    require(cert["two_premise_AH_equivalent_final_connection_tables_accepted"] == 7, "cert AH count")
    require(cert["HYM_or_EndE_final_row_accepted"] is False, "cert HYM guard")
    require(cert["strict_no_knob_closed"] is False, "cert strict guard")
    require(cert["true_SM_equivalence_closed"] is False, "cert true SM guard")

    require("The counted AH-equivalent lane remains `7/8`" in note, "note AH lane")
    require("Step38 closes operator-level nonidentity projective `rho_E`" in note, "note Step38")
    require("Route A: prove row-scope sufficiency" in note, "note Route A")
    require("Route B: emit the full-sector covariant" in note, "note Route B")
    require(NEXT in note, "note next")

    print("Operator-sector HYM/EndE Step40 backimport audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
