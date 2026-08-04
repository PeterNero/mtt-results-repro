"""Audit the selected AH representative Cech-row emission packet."""

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
BUILDER = ROOT / "scripts" / "build_selected_cech_ah_representative_or_hymende_values.py"

SLUG = "selected_cech_ah_representative_or_hymende_values"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Cech_AH_Representative_or_HYMEndE_Values_v1.md"
CECH_PACKET = PACKET_DIR / "selected_ah_representative_for_cech_row.packet.json"
HYM_PACKET = PACKET_DIR / "hym_ende_row_recheck_after_ah_representative.packet.json"
GATE_PACKET = PACKET_DIR / "ah_representative_connection_row_gate.packet.json"
NEXT_PACKET = PACKET_DIR / "next_hymende_or_literalgoodcover_contract.packet.json"

STATUS = (
    "MTT_SELECTED_CECH_AH_REPRESENTATIVE_OR_HYMENDE_VALUES_"
    "AH_EQUIVALENT_CECH_ROW_COUNTED_HYM_OPEN"
)
NEXT = "MTT_Selected_HYMEndEConnectionValues_or_LiteralGoodCoverUpgrade_v1"
BN27_PREMISE = "SelectedBN27ThresholdSourceEmissionPrinciple"
AH_REPRESENTATIVE_PREMISE = "SelectedAHCechRepresentativeEquivalencePrinciple"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    cech = load(CECH_PACKET)
    hym = load(HYM_PACKET)
    gate = load(GATE_PACKET)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "cert next mismatch")
    require(next_packet["next_required_artifact"] == NEXT, "next packet mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "cert theorem not proved")

    for payload in [candidate, cert, cech, hym, gate, next_packet]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    decision = candidate["closure_decision"]
    require(decision["strict_final_connection_tables_accepted"] == 4, "strict count drifted")
    require(decision["one_premise_final_connection_tables_accepted"] == 6, "one-premise count drifted")
    require(decision["two_premise_AH_equivalent_final_connection_tables_accepted"] == 7, "AH lane count mismatch")
    require(decision["counted_principles"] == [BN27_PREMISE, AH_REPRESENTATIVE_PREMISE], "principle list mismatch")
    require(decision["AH_equivalent_cech_row_accepted"] is True, "AH Cech row not accepted")
    require(decision["literal_goodcover_Deligne_Cech_row_accepted"] is False, "literal good-cover overclaim")
    require(decision["HYM_or_EndE_final_row_accepted"] is False, "HYM overclaim")
    require(decision["remaining_row_after_AH_equivalent_lane"] == "selected_HYM_or_projective_connection_coefficients", "remaining row mismatch")
    require(decision["strict_no_knob_closed"] is False, "strict no-knob overclaim")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclaim")

    require(cech["row"] == "cech_transition_cocycles", "Cech row id")
    require(cech["literal_good_cover_Deligne_Cech_row_accepted"] is False, "Cech literal overclaim")
    require(cech["accepted_as_AH_equivalent_cech_row"] is True, "AH representative not accepted")
    require(cech["premise_name"] == AH_REPRESENTATIVE_PREMISE, "AH premise name")
    require(cech["premise_count_added"] == 1, "AH premise count")
    require(cech["selected_source_layer"]["selected_ordered_AH_goodcover_source_for_stability_layer"] is True, "AH source missing")
    require(cech["AH_representative_values"]["central_shared_circle_trivial"] is True, "shared circle guard")
    require(
        cech["AH_representative_values"]["c1_deck_alternating_matrix_order_g1_to_g6"][0][1] == 2,
        "c1 g1/g2 mismatch",
    )
    require(
        cech["AH_representative_values"]["c1_deck_alternating_matrix_order_g1_to_g6"][2][3] == -4,
        "c1 g3/g4 mismatch",
    )
    require(cech["selected_Ext_class_values"]["nonzero_extension_class_label"] == "theta_plus_0_tensor_eta_minus_0", "Ext label")
    require(cech["selected_Ext_class_values"]["extension_class_vector_C1"] == [1, 0, 0, 0, 0, 0, 0, 0], "Ext vector")
    require(cech["cocycle_certificates"]["cocycle_law_holds_on_generators_mod_2pi_i"] is True, "generator cocycle")
    require(cech["cocycle_certificates"]["cocycle_law_holds_on_small_lattice_box_mod_2pi_i"] is True, "box cocycle")
    require(cech["guardrails"]["raw_good_cover_Aij_Bi_gijk_hij_emitted"] is False, "raw Cech overclaim")
    require(cech["guardrails"]["operator_layer_Pic0_recheck_closed"] is False, "Pic0 overclaim")
    require(cech["guardrails"]["strict_unconditional_cech_row_closed"] is False, "strict Cech overclaim")

    require(hym["row"] == "selected_HYM_or_projective_connection_coefficients", "HYM row id")
    require(hym["accepted_as_final_connection_table_row"] is False, "HYM accepted incorrectly")
    require(hym["support_imported"]["diagonal_End0_connection_formula"] is True, "diagonal support missing")
    require(hym["support_imported"]["directionwise_D_E_connection_matrices"] is True, "D_E support missing")
    require(hym["support_imported"]["ad_T3_matrix_on_basis_T1_T2_T3"][0][1] == -1, "ad T3 mismatch")
    require(hym["why_not_accepted"]["selected_operator_values_closed"] is False, "selected operator values overclosed")
    require(hym["why_not_accepted"]["actual_visible_operator_payload_emitted"] is False, "visible payload overemitted")
    require(hym["why_not_accepted"]["rank2_to_rank3_sector_transfer_values_open"] is True, "rank2-sector guard missing")

    require(gate["strict_final_connection_table_count"] == "4/8", "gate strict count")
    require(gate["one_premise_final_connection_table_count"] == "6/8", "gate one-premise count")
    require(gate["one_premise_literal_goodcover_cech_row_accepted"] is False, "gate one-premise overclaim")
    require(gate["two_premise_AH_equivalent_final_connection_table_count"] == "7/8", "gate AH count")
    require(gate["two_premise_counted_principles"] == [BN27_PREMISE, AH_REPRESENTATIVE_PREMISE], "gate premises")
    require(gate["two_premise_cech_row_accepted"] is True, "gate Cech")
    require(gate["two_premise_hym_row_accepted"] is False, "gate HYM")
    require(gate["remaining_rows_after_AH_equivalent_lane"] == ["selected_HYM_or_projective_connection_coefficients"], "gate remaining")

    require(next_packet["current_lanes"]["strict_lane"] == "4/8", "next strict lane")
    require(next_packet["current_lanes"]["one_premise_BN27_lane"] == "6/8", "next one-premise lane")
    require(next_packet["current_lanes"]["two_premise_AH_equivalent_lane"] == "7/8", "next AH lane")
    require("derive the AH representative equivalence principle instead of counting it as an additional premise" in next_packet["allowed_exits"], "next derivation exit missing")
    require("diagonal rank-two End0 D_E support alone" in next_packet["must_not_count_as_final_HYM_row"], "next HYM guard missing")

    require(cert["two_premise_AH_equivalent_final_connection_tables_accepted"] == 7, "cert AH count")
    require(cert["AH_equivalent_cech_row_accepted"] is True, "cert Cech")
    require(cert["literal_goodcover_Deligne_Cech_row_accepted"] is False, "cert literal guard")
    require(cert["HYM_or_EndE_final_row_accepted"] is False, "cert HYM guard")
    require(cert["strict_no_knob_closed"] is False, "cert strict guard")
    require(cert["true_SM_equivalence_closed"] is False, "cert true SM guard")

    require("one-premise BN27 lane: `6/8`" in note, "note one-premise count")
    require("AH-equivalent final connection tables: `7/8`" in note, "note AH count")
    require("literal good-cover Deligne-Cech cochains" in note, "note literal guard")
    require(NEXT in note, "note next")

    print("Selected Cech AH representative / HYM-EndE audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
