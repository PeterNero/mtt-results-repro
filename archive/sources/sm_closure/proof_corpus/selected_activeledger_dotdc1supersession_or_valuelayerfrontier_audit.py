"""Audit active-ledger dotD/C1 supersession and value-layer frontier."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SLUG = "selected_activeledger_dotdc1supersession_or_valuelayerfrontier"

CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
SUPERSESSION = DATA / SLUG / "active_ledger_supersession_decision.packet.json"
CLOSED_SOURCE = DATA / SLUG / "closed_source_layer_after_step24.packet.json"
VALUE_FRONTIER = DATA / SLUG / "value_layer_frontier_after_source_closure.packet.json"
NEXT_PACKET = DATA / SLUG / "next_cutset_value_functional_rows.packet.json"
NOTE = CORPUS / "MTT_Selected_ActiveLedger_dotDC1Supersession_or_ValueLayerFrontier_v1.md"

STATUS = "MTT_SELECTED_ACTIVELEDGER_DOTDC1SUPERSESSION_BUILT_VALUE_LAYER_FRONTIER_OPEN"
NEXT = "MTT_Selected_ThresholdResponseFunctionalRowEmission_or_ExternalSourceRowImport_v1"


def load(path: Path) -> dict:
    assert path.exists(), f"missing {path.relative_to(ROOT)}"
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    candidate = load(CANDIDATE)
    cert = load(CERT)
    supersession = load(SUPERSESSION)
    closed_source = load(CLOSED_SOURCE)
    value_frontier = load(VALUE_FRONTIER)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    assert candidate["status"] == STATUS
    assert candidate["theorem"]["name"] == "ActiveLedgerDotDC1SupersessionTheorem"
    assert candidate["theorem"]["proved"] is True
    assert candidate["closure_claimed"] is True
    assert candidate["full_no_knob_closure_claimed"] is False
    assert candidate["true_SM_equivalence_claimed"] is False
    assert candidate["observed_data_used_as_selector"] is False
    assert candidate["target_fitting_used"] is False
    assert candidate["next_required_artifact"] == NEXT

    decision = candidate["closure_decision"]
    assert decision["active_ledger_supersession_built"] is True
    assert decision["DE_Green_gap_layer_closed"] is True
    assert decision["dotD_alpha1_closed_by_active_ledger"] is True
    assert decision["primitive_C1_first_response_layer_closed_by_active_ledger"] is True
    assert decision["A_selected_closed_by_active_ledger"] is True
    assert decision["b_selected_closed_by_active_ledger"] is True
    assert decision["deltaTheta_C1_closed_by_active_ledger"] is True
    assert decision["source_layer_closed"] is True
    assert decision["accepted_value_functional_rows_closed"] is False
    assert decision["accepted_Yukawa_magnitudes_closed"] is False
    assert decision["accepted_threshold_mass_scheme_source_rows_closed"] is False
    assert decision["full_no_knob_closed"] is False
    assert decision["true_SM_equivalence_closed"] is False

    assert supersession["status"] == "STALE_Q79_ONLY_DOTD_OPEN_WORDING_SUPERSEDED"
    assert supersession["stale_open_claims"]["selected_dotD_source_theorem"] is True
    assert supersession["stale_open_claims"]["selected_primitive_C1_contractions"] is True
    assert supersession["superseded_now"]["selected_dotD_source_theorem"] is True
    assert supersession["superseded_now"]["same_branch_alpha1_driver_theorem"] is True
    assert supersession["superseded_now"]["honest_dotD_replay_without_lifted_flags"] is True
    assert supersession["superseded_now"]["selected_primitive_C1_contractions_first_response_layer"] is True
    assert supersession["superseded_now"]["A_selected"] is True
    assert supersession["superseded_now"]["b_selected"] is True
    assert supersession["superseded_now"]["deltaTheta_C1"] is True
    assert "active-ledger supersession" in supersession["guardrail"]

    closed = closed_source["closed_inputs"]
    for key in [
        "selected_27mode_DE_trace_equality",
        "selected_DE_Riesz_Green_gap_layer",
        "selected_dotD_alpha1_transport_formula",
        "selected_alpha1_driver_normalization",
        "honest_dotD_alpha1_replay",
        "selected_source_to_C1_transfer_map",
        "selected_dynamic_overlap_tensor",
        "selected_primitive_C1_first_response_layer",
        "selected_A_selected",
        "selected_b_selected",
        "selected_deltaTheta_C1",
        "selected_Hessian_source_normalization",
    ]:
        assert closed[key] is True
    assert closed_source["formal_rows"]["formal_110_rows_executed"] is True
    assert closed_source["formal_rows"]["formal_110_total_rows"] == 110
    assert closed_source["formal_rows"]["all_72_primitive_rows_exact"] is True
    assert closed_source["formal_rows"]["formal_110_max_abs_error"] < 1e-12
    assert closed_source["source_layer_closed"] is True

    assert value_frontier["status"] == "VALUE_FUNCTIONAL_ROWS_OPEN_AFTER_SOURCE_LAYER_CLOSURE"
    assert value_frontier["closure_claimed"] is False
    assert value_frontier["source_layer_closed"] is True
    assert value_frontier["value_layer_required_rows"] == 5
    assert value_frontier["value_layer_accepted_source_rows"] == 0
    assert value_frontier["accepted_true_value_source_row_emitted"] is False
    assert value_frontier["still_open"]["selected_threshold_response_functional"] is True
    assert value_frontier["still_open"]["selected_Yukawa_Higgs_value_functional"] is True
    assert "selected dotD_alpha1 and alpha1 driver" in value_frontier[
        "not_a_source_promotion_blocker_anymore"
    ]

    assert next_packet["status"] == "NEXT_IS_THRESHOLD_RESPONSE_OR_EXTERNAL_ROW_IMPORT"
    assert next_packet["next_required_artifact"] == NEXT
    assert "active-ledger selected dotD_alpha1 and alpha1 driver imported" in next_packet["closed_now"]
    assert "active-ledger primitive C1 first-response layer imported" in next_packet["closed_now"]
    assert "selected threshold response functional rows" in next_packet["still_open"]
    assert next_packet["why"] == "The source/operator layer is closed in the active ledger; accepted value-functional rows remain zero."

    assert cert["status"] == STATUS
    assert cert["active_ledger_supersession_built"] is True
    assert cert["dotD_alpha1_closed_by_active_ledger"] is True
    assert cert["primitive_C1_first_response_layer_closed_by_active_ledger"] is True
    assert cert["A_selected_closed_by_active_ledger"] is True
    assert cert["b_selected_closed_by_active_ledger"] is True
    assert cert["deltaTheta_C1_closed_by_active_ledger"] is True
    assert cert["source_layer_closed"] is True
    assert cert["accepted_value_functional_rows_closed"] is False
    assert cert["accepted_Yukawa_magnitudes_closed"] is False
    assert cert["accepted_threshold_mass_scheme_source_rows_closed"] is False
    assert cert["next_required_artifact"] == NEXT

    assert "ActiveLedgerDotDC1SupersessionTheorem" in note
    assert "selected `dotD_alpha1` and alpha1 driver: `True`" in note
    assert "primitive `C1` first-response layer: `True`" in note
    assert "accepted value-functional rows: `False`" in note
    assert NEXT in note
    print("active-ledger dotD/C1 supersession audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
