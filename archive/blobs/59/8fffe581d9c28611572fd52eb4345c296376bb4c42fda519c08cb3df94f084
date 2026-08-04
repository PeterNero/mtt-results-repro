"""Audit visible Chern-Weil / D_E-Green import for full-sector payload upgrade."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SLUG = "selected_visiblechernweildegreenimport_or_fullsectorpayloadupgrade"

CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
IMPORT_LEDGER = DATA / SLUG / "visible_chernweil_degreen_import_ledger.packet.json"
PAYLOAD_UPGRADE = DATA / SLUG / "fullsector_payload_upgrade_after_q79_trace.packet.json"
ROW_GATE = DATA / SLUG / "deltas2_row_gate_after_degreen_import.packet.json"
NEXT_PACKET = DATA / SLUG / "next_cutset_after_degreen_import.packet.json"
NOTE = CORPUS / "MTT_Selected_VisibleChernWeilDEGreenImport_or_FullSectorPayloadUpgrade_v1.md"

STATUS = "MTT_SELECTED_VISIBLECHERNWEIL_DEGREEN_IMPORT_BUILT_DOTD_C1_ROWS_OPEN"
NEXT = "Q79_Selected_Alpha1_Tangent_or_Retarded_Overlap_Kernel_v1"


def load(path: Path) -> dict:
    assert path.exists(), f"missing {path.relative_to(ROOT)}"
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    candidate = load(CANDIDATE)
    cert = load(CERT)
    import_ledger = load(IMPORT_LEDGER)
    payload_upgrade = load(PAYLOAD_UPGRADE)
    row_gate = load(ROW_GATE)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    assert candidate["status"] == STATUS
    assert candidate["theorem"]["name"] == "VisibleChernWeilDEGreenImportTheorem"
    assert candidate["theorem"]["proved"] is True
    assert candidate["closure_claimed"] is True
    assert candidate["strict_delta_s2_source_rows_claimed"] is False
    assert candidate["strict_csk_source_theorem_claimed"] is False
    assert candidate["full_no_knob_closure_claimed"] is False
    assert candidate["true_SM_equivalence_claimed"] is False
    assert candidate["observed_data_used_as_selector"] is False
    assert candidate["target_fitting_used"] is False

    decision = candidate["closure_decision"]
    assert decision["DE_Green_import_built"] is True
    assert decision["selected_trace_equality_for_27mode_DE"] is True
    assert decision["D_E_Riesz_Green_gap_layer_closed"] is True
    assert decision["local_step39_DE_open_wording_superseded"] is True
    assert decision["dotD_alpha1_source_closed"] is False
    assert decision["primitive_C1_closed"] is False
    assert decision["fullsector_payload_closed"] is False
    assert decision["delta_s2_source_rows_emitted"] == 0
    assert decision["accepted_phi_sector_n_numeric_row_count"] == 0
    assert decision["accepted_strict_csk_source_row_count"] == 0
    assert decision["next_required_artifact"] == NEXT

    assert import_ledger["status"] == "Q79_DE_GREEN_GAP_LAYER_IMPORTED_DOTD_C1_OPEN"
    closed = import_ledger["imported_closed_layers"]
    assert closed["selected_trace_equality_for_27mode_DE"] is True
    assert closed["D_E_source_flags_theorem_derived"] is True
    assert closed["D_E_honest_replay_contract_locked"] is True
    assert closed["selected_Riesz_Green_gap_layer_closed"] is True
    assert import_ledger["selected_gap_layer"]["basis_dimension"] == 27
    assert import_ledger["selected_gap_layer"]["selected_eta_N"] == 1.0
    assert import_ledger["selected_gap_layer"]["selected_gap_lower_bound"] > 0
    assert import_ledger["not_imported_as_closed"]["dotD_alpha1_source"] is True
    assert import_ledger["not_imported_as_closed"]["primitive_C1_response"] is True
    assert import_ledger["not_imported_as_closed"]["strict_csk_rows"] is True

    assert payload_upgrade["status"] == "DEGREEN_LAYER_UPGRADED_FULL_PAYLOAD_STILL_OPEN"
    assert payload_upgrade["D_E_Riesz_Green_gap_layer_closed"] is True
    assert payload_upgrade["dotD_alpha1_source_closed"] is False
    assert payload_upgrade["primitive_C1_closed"] is False
    assert payload_upgrade["fullsector_payload_closed"] is False
    assert payload_upgrade["supersedes_local_step39_DE_open_wording"] is True
    assert "U1_selected_trace_equality_for_27mode_DE" in payload_upgrade["upgraded_closed_layers"]
    assert "U2_selected_DE_gap_Riesz_Green_layer" in payload_upgrade["upgraded_closed_layers"]
    assert "selected alpha1 tangent or retarded-overlap derivative formula" in payload_upgrade[
        "still_open_payload_fields"
    ]

    assert row_gate["status"] == "ROW_GATE_STILL_BLOCKED_BY_DOTD_C1_AND_FULL_PAYLOAD"
    assert row_gate["D_E_Riesz_Green_gap_layer_closed"] is True
    assert row_gate["fullsector_payload_closed"] is False
    assert row_gate["delta_s2_source_rows_emitted_now"] == 0
    assert row_gate["phi_sector_n_numeric_rows_emitted_now"] == 0
    assert row_gate["strict_csk_source_rows_emitted_now"] == 0
    assert row_gate["conditional_if_remaining_payload_closes"]["strict_csk_source_rows"] == 9
    assert "selected dotD_alpha1 source and alpha1 driver" in row_gate["row_blockers_after_import"]

    assert next_packet["status"] == "NEXT_IS_SELECTED_ALPHA1_TANGENT_OR_RETARDED_KERNEL"
    assert next_packet["next_required_artifact"] == NEXT
    assert "selected 27-mode D_E trace equality imported from q79" in next_packet["closed_now"]
    assert next_packet["minimal_next_contract"]["name"] == "Selected_alpha1_Tangent_or_Retarded_Overlap_Kernel_v1"
    assert "dotD_alpha1" in next_packet["reason"]

    assert cert["status"] == STATUS
    assert cert["DE_Green_import_built"] is True
    assert cert["selected_trace_equality_for_27mode_DE"] is True
    assert cert["D_E_Riesz_Green_gap_layer_closed"] is True
    assert cert["local_step39_DE_open_wording_superseded"] is True
    assert cert["dotD_alpha1_source_closed"] is False
    assert cert["primitive_C1_closed"] is False
    assert cert["fullsector_payload_closed"] is False
    assert cert["delta_s2_source_rows_emitted"] == 0
    assert cert["accepted_phi_sector_n_numeric_row_count"] == 0
    assert cert["accepted_strict_csk_source_row_count"] == 0
    assert cert["next_required_artifact"] == NEXT

    assert "VisibleChernWeilDEGreenImportTheorem" in note
    assert "selected Riesz/Green gap layer: `True`" in note
    assert "accepted strict `c_{s,k}` source rows: `0`" in note
    assert NEXT in note
    print("visible Chern-Weil / D_E-Green import audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
