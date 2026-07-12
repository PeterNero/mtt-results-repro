"""Audit Delta_S2 density correction source / strict csk rows gate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SLUG = "selected_deltas2densitycorrectionsource_or_strictcskrows"

CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
CLAUSES = DATA / SLUG / "deltas2_source_clause_ledger.packet.json"
ROWS = DATA / SLUG / "deltas2_row_emission_attempt.packet.json"
CONDITIONAL = DATA / SLUG / "conditional_strict_csk_closure_witness.packet.json"
NEXT_PACKET = DATA / SLUG / "next_cutset_after_deltas2_source_gate.packet.json"
NOTE = CORPUS / "MTT_Selected_DeltaS2DensityCorrectionSource_or_StrictCSKRows_v1.md"

STATUS = (
    "MTT_SELECTED_DELTAS2DENSITYCORRECTIONSOURCE_OR_STRICTCSKROWS_"
    "SOURCE_GATE_BUILT_ROWS_OPEN"
)
NEXT = "MTT_Selected_FullSectorHYMOperatorPayload_or_DeltaS2RowEmission_v1"


def load(path: Path) -> dict:
    assert path.exists(), f"missing {path.relative_to(ROOT)}"
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    candidate = load(CANDIDATE)
    cert = load(CERT)
    clauses = load(CLAUSES)
    rows = load(ROWS)
    conditional = load(CONDITIONAL)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    assert candidate["status"] == STATUS
    assert candidate["next_required_artifact"] == NEXT
    assert candidate["theorem"]["name"] == "DeltaS2DensityCorrectionSourceGateTheorem"
    assert candidate["theorem"]["proved"] is True
    assert candidate["closure_claimed"] is True
    assert candidate["strict_delta_s2_source_rows_claimed"] is False
    assert candidate["strict_csk_source_theorem_claimed"] is False
    assert candidate["full_no_knob_closure_claimed"] is False
    assert candidate["true_SM_equivalence_claimed"] is False
    assert candidate["observed_data_used_as_selector"] is False
    assert candidate["target_fitting_used"] is False

    decision = candidate["closure_decision"]
    assert decision["delta_s2_source_gate_built"] is True
    assert decision["required_clause_count"] == 7
    assert decision["selected_clause_count"] == 1
    assert decision["blocking_clause_count"] == 6
    assert decision["projective_rhoE_operator_level_closed"] is True
    assert decision["projective_rhoE_selected_source_closed"] is False
    assert decision["diagonal_End0_DE_closed"] is True
    assert decision["full_sector_operator_payload_closed"] is False
    assert decision["delta_s2_source_rows_emitted"] == 0
    assert decision["accepted_phi_sector_n_numeric_row_count"] == 0
    assert decision["accepted_strict_csk_source_row_count"] == 0
    assert decision["conditional_strict_csk_closure_witness_built"] is True

    assert clauses["status"] == "DELTAS2_SOURCE_CLAUSE_LEDGER_BUILT_INCOMPLETE"
    assert clauses["required_clause_count"] == 7
    assert clauses["selected_clause_count"] == 1
    assert clauses["blocking_clause_count"] == 6
    assert len(clauses["clauses"]) == 7
    selected = [item["clause_id"] for item in clauses["clauses"] if item["selected_for_delta_s2_now"]]
    assert selected == ["C0_full_s2_density_contract"]
    assert "C4_full_sector_DE_Riesz_Green_dotD" in clauses["blocking_clauses"]
    assert clauses["support_summary"]["projective_rhoE_operator_level_closed"] is True
    assert clauses["support_summary"]["projective_rhoE_source_closed"] is False
    assert clauses["support_summary"]["diagonal_End0_D_E_closed"] is True
    assert clauses["support_summary"]["full_sector_D_E_closed"] is False
    assert clauses["support_summary"]["full_S2_execution_allowed_now"] is False
    assert clauses["support_summary"]["full_S2_accepted_scalar_row_count_now"] == 0

    assert rows["status"] == "NO_DELTAS2_SOURCE_ROWS_EMITTED_CURRENT_SUPPORT_INCOMPLETE"
    assert rows["policy_residual_values_used_only_as_diagnostic"] is True
    assert rows["required_row_count"] == 9
    assert rows["accepted_delta_s2_source_row_count"] == 0
    assert rows["accepted_phi_sector_n_numeric_row_count"] == 0
    assert rows["accepted_strict_csk_source_row_count"] == 0
    assert len(rows["rows"]) == 9
    assert all(row["source_value_emitted"] is False for row in rows["rows"])
    assert all(row["accepted_as_delta_s2_source_row"] is False for row in rows["rows"])
    assert all(row["accepted_as_csk_source_row"] is False for row in rows["rows"])

    assert conditional["status"] == "CONDITIONAL_WITNESS_BUILT_WAITING_FOR_FULL_SECTOR_HYM_PAYLOAD"
    assert conditional["if_all_clauses_selected"]["Delta_S2_source_rows_would_emit"] == 9
    assert conditional["if_all_clauses_selected"]["Phi_sector_N_numeric_rows_would_emit"] == 9
    assert conditional["if_all_clauses_selected"]["strict_csk_rows_would_close"] == 9
    assert conditional["current_result"]["Delta_S2_source_rows_emitted"] == 0
    assert conditional["current_result"]["strict_csk_rows_closed"] == 0
    assert "sector-transfer map from diagonal End0 lane to Q,u,d,L,e,N,H operator bases" in conditional[
        "minimum_next_payload"
    ]["minimum_fields"]
    assert conditional["operator_value_frontier"]["covariant_D_E_matrices_on_selected_B_N_basis"] is True

    assert next_packet["next_required_artifact"] == NEXT
    assert "Delta_S2 strict source-emission validator built" in next_packet["closed_now"]
    assert "selected HYM projector source promotion" in next_packet["still_open"]
    assert "nine Delta_S2 source rows" in next_packet["still_open"]

    assert cert["status"] == STATUS
    assert cert["required_clause_count"] == 7
    assert cert["selected_clause_count"] == 1
    assert cert["blocking_clause_count"] == 6
    assert cert["projective_rhoE_operator_level_closed"] is True
    assert cert["projective_rhoE_selected_source_closed"] is False
    assert cert["diagonal_End0_DE_closed"] is True
    assert cert["full_sector_operator_payload_closed"] is False
    assert cert["delta_s2_source_rows_emitted"] == 0
    assert cert["accepted_phi_sector_n_numeric_row_count"] == 0
    assert cert["accepted_strict_csk_source_row_count"] == 0
    assert cert["conditional_strict_csk_closure_witness_built"] is True
    assert cert["next_required_artifact"] == NEXT

    assert "DeltaS2DensityCorrectionSourceGateTheorem" in note
    assert "accepted `Delta_S2` source rows: `0`" in note
    assert NEXT in note
    print("Delta_S2 density correction source / strict csk rows audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
