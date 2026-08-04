"""Audit full-sector HYM operator payload / Delta_S2 row-emission frontier."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SLUG = "selected_fullsectorhymoperatorpayload_or_deltas2rowemission"

CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
PAYLOAD = DATA / SLUG / "fullsector_hym_payload_field_ledger.packet.json"
ROW_BRIDGE = DATA / SLUG / "deltas2_row_emission_bridge_after_fullsector_payload.packet.json"
SUPERSESSION = DATA / SLUG / "rhoe_source_blocker_supersession.packet.json"
NEXT_PACKET = DATA / SLUG / "next_cutset_after_fullsector_payload_contract.packet.json"
NOTE = CORPUS / "MTT_Selected_FullSectorHYMOperatorPayload_or_DeltaS2RowEmission_v1.md"

STATUS = "MTT_SELECTED_FULLSECTORHYMOPERATORPAYLOAD_CONTRACT_BUILT_DELTAS2_ROWS_OPEN"
NEXT = "MTT_Selected_Visible_Chern_Weil_Operator_Source_v1"


def load(path: Path) -> dict:
    assert path.exists(), f"missing {path.relative_to(ROOT)}"
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    candidate = load(CANDIDATE)
    cert = load(CERT)
    payload = load(PAYLOAD)
    row_bridge = load(ROW_BRIDGE)
    supersession = load(SUPERSESSION)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    assert candidate["status"] == STATUS
    assert candidate["theorem"]["name"] == "FullSectorHYMPayloadReductionAndRhoESupersessionTheorem"
    assert candidate["theorem"]["proved"] is True
    assert candidate["closure_claimed"] is True
    assert candidate["strict_delta_s2_source_rows_claimed"] is False
    assert candidate["strict_csk_source_theorem_claimed"] is False
    assert candidate["full_no_knob_closure_claimed"] is False
    assert candidate["true_SM_equivalence_claimed"] is False
    assert candidate["observed_data_used_as_selector"] is False
    assert candidate["target_fitting_used"] is False

    decision = candidate["closure_decision"]
    assert decision["payload_contract_built"] is True
    assert decision["required_payload_field_count"] == 10
    assert decision["support_field_count"] >= 8
    assert decision["selected_payload_field_count"] == 1
    assert decision["blocking_payload_field_count"] == 9
    assert decision["old_rhoE_source_blocker_retired"] is True
    assert decision["visible_operator_source_closed"] is False
    assert decision["fullsector_payload_closed"] is False
    assert decision["delta_s2_source_rows_emitted"] == 0
    assert decision["accepted_phi_sector_n_numeric_row_count"] == 0
    assert decision["accepted_strict_csk_source_row_count"] == 0
    assert decision["next_required_artifact"] == NEXT

    assert payload["status"] == "FULLSECTOR_HYM_PAYLOAD_TYPED_CONTRACT_BUILT_VALUES_OPEN"
    assert payload["required_field_count"] == 10
    assert payload["selected_payload_field_count"] == 1
    assert payload["blocking_field_count"] == 9
    assert payload["latest_progress"]["old_projective_rhoE_source_blocker_retired"] is True
    assert payload["latest_progress"]["visible_operator_source_still_open"] is True
    assert payload["latest_progress"]["diagonal_End0_lane_closed"] is True
    assert payload["latest_progress"]["stationary_Riesz_Green_transport_lane_closed"] is True
    assert payload["latest_progress"]["full_sector_D_E_closed"] is False
    assert "F0_projective_gerbe_rhoE_S3_source" in payload["selected_payload_fields"]
    assert "F1_selected_visible_Chern_Weil_operator_source" in payload["blocking_fields"]
    assert "F8_End0_to_sector_functor_values" in payload["blocking_fields"]
    assert "F9_nonlinear_HYM_offdiagonal_control" in payload["blocking_fields"]

    assert row_bridge["status"] == "ROW_EMISSION_BRIDGE_READY_PAYLOAD_VALUES_OPEN"
    assert row_bridge["fullsector_payload_closed"] is False
    assert row_bridge["full_s2_execution_allowed_now"] is False
    assert row_bridge["delta_s2_row_count_required"] == 9
    assert row_bridge["delta_s2_source_rows_emitted_now"] == 0
    assert row_bridge["phi_sector_n_numeric_rows_emitted_now"] == 0
    assert row_bridge["strict_csk_source_rows_emitted_now"] == 0
    assert row_bridge["conditional_if_payload_closes"]["delta_s2_source_rows"] == 9
    assert row_bridge["conditional_if_payload_closes"]["strict_csk_source_rows"] == 9
    assert row_bridge["row_guard"]["diagnostic_policy_residual_replay_allowed"] is False
    assert row_bridge["row_guard"]["accept_rows_only_from_selected_payload"] is True

    assert supersession["status"] == "OLD_RHOE_SOURCE_BLOCKER_RETIRED_VISIBLE_OPERATOR_SOURCE_REMAINS"
    assert supersession["previous_delta_s2_clause"] == "C3_projective_rhoE_transition"
    assert supersession["retired_now"]["selected_S3_gerbe_source_level"] is True
    assert supersession["retired_now"]["map_to_qutrit_central_cocycle"] is True
    assert supersession["retired_now"]["Freed_Witten"] is True
    assert supersession["retired_now"]["Green_Schwarz_Bianchi"] is True
    assert supersession["not_retired"]["selected_visible_Chern_Weil_operator_source"] is True
    assert supersession["not_retired"]["selected_D_E_dotD_Riesz_Green"] is True

    assert next_packet["status"] == "NEXT_IS_SELECTED_VISIBLE_CHERN_WEIL_OPERATOR_SOURCE"
    assert next_packet["next_required_artifact"] == NEXT
    assert "full-sector HYM operator payload field ledger built" in next_packet["closed_now"]
    assert "old rhoE-source-open wording superseded by visible-operator-source wall" in next_packet[
        "closed_now"
    ]
    assert "construct selected visible bundle/sheaf or Route-C operator source on q79/F,m=1" in next_packet[
        "ordered_attack"
    ]
    assert next_packet["projective_gerbe_next_packet"] == NEXT

    assert cert["status"] == STATUS
    assert cert["payload_contract_built"] is True
    assert cert["required_payload_field_count"] == 10
    assert cert["selected_payload_field_count"] == 1
    assert cert["blocking_payload_field_count"] == 9
    assert cert["old_rhoE_source_blocker_retired"] is True
    assert cert["visible_operator_source_closed"] is False
    assert cert["fullsector_payload_closed"] is False
    assert cert["delta_s2_source_rows_emitted"] == 0
    assert cert["accepted_phi_sector_n_numeric_row_count"] == 0
    assert cert["accepted_strict_csk_source_row_count"] == 0
    assert cert["next_required_artifact"] == NEXT

    assert "FullSectorHYMPayloadReductionAndRhoESupersessionTheorem" in note
    assert "old `rhoE` source-level blocker retired: `True`" in note
    assert "accepted strict `c_{s,k}` source rows: `0`" in note
    assert NEXT in note
    print("full-sector HYM operator payload / Delta_S2 row-emission audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
