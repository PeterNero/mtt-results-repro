"""Audit Phi_sector_N source-value inventory / no-knob csk rows gate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SLUG = "selected_phisectornsourcevalues_or_noknobcskrows"

CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
INVENTORY = DATA / SLUG / "phisectorn_candidate_source_inventory.packet.json"
PROMOTION = DATA / SLUG / "phisectorn_value_promotion_decision.packet.json"
TRACE_ACCEPTANCE = DATA / SLUG / "csk_trace_acceptance_after_phisectorn_inventory.packet.json"
NEXT_PACKET = DATA / SLUG / "next_cutset_after_phisectorn_inventory.packet.json"
NOTE = CORPUS / "MTT_Selected_PhiSectorNSourceValues_or_NoKnobCSKRows_v1.md"

STATUS = (
    "MTT_SELECTED_PHISECTORNVALUES_OR_NOKNOBCSKROWS_"
    "SOURCE_INVENTORY_CLOSED_VALUES_OPEN"
)
NEXT = "MTT_Selected_SectorResponseDensitySourceTheorem_or_NoKnobCSKRowEmission_v1"


def load(path: Path) -> dict:
    assert path.exists(), f"missing {path.relative_to(ROOT)}"
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    candidate = load(CANDIDATE)
    cert = load(CERT)
    inventory = load(INVENTORY)
    promotion = load(PROMOTION)
    trace_acceptance = load(TRACE_ACCEPTANCE)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    assert candidate["status"] == STATUS
    assert candidate["next_required_artifact"] == NEXT
    assert candidate["theorem"]["name"] == "PhiSectorNSourceValueInventoryTheorem"
    assert candidate["theorem"]["proved"] is True
    assert candidate["closure_claimed"] is True
    assert candidate["strict_phi_sector_n_values_claimed"] is False
    assert candidate["strict_csk_source_theorem_claimed"] is False
    assert candidate["full_no_knob_closure_claimed"] is False
    assert candidate["true_SM_equivalence_claimed"] is False
    assert candidate["observed_data_used_as_selector"] is False
    assert candidate["target_fitting_used"] is False

    decision = candidate["closure_decision"]
    assert decision["common_circle_trace_engine_closed"] is True
    assert decision["source_inventory_closed"] is True
    assert decision["source_normalized_sector_projection_weights_closed"] is True
    assert decision["first_dynamic_support_rows_accepted"] == 2
    assert decision["first_dynamic_rows_magnitude_bearing"] is False
    assert decision["threshold_response_functional_closed"] is False
    assert decision["Phi_sector_N_required_numeric_value_count"] == 9
    assert decision["Phi_sector_N_numeric_values_emitted"] is False
    assert decision["accepted_Phi_sector_N_source_value_count"] == 0
    assert decision["accepted_strict_csk_source_row_count"] == 0
    assert decision["policy_replay_rows_accepted_as_source"] is False
    assert decision["strict_csk_source_theorem_closed"] is False

    assert inventory["status"] == "PHI_SECTOR_N_SOURCE_INVENTORY_CLOSED_NO_NUMERIC_VALUES"
    assert inventory["counts"]["phi_sector_n_required_numeric_values"] == 9
    assert inventory["counts"]["phi_sector_n_numeric_values_emitted"] == 0
    assert inventory["counts"]["accepted_phi_sector_n_source_values"] == 0
    assert inventory["counts"]["accepted_source_normalized_projection_rows"] == 4
    assert inventory["counts"]["accepted_first_dynamic_support_rows"] == 2
    assert inventory["counts"]["accepted_magnitude_bearing_projection_rows"] == 0
    assert inventory["counts"]["accepted_threshold_response_source_rows"] == 0
    assert inventory["observed_data_used_as_selector"] is False
    assert inventory["target_fitting_used"] is False

    source_weight_support = [
        row for row in inventory["accepted_support"] if row["support_id"] == "source_normalized_sector_projection_weights"
    ][0]
    assert source_weight_support["accepted"] is True
    assert source_weight_support["row_count"] == 4
    assert "non-magnitude-bearing" in source_weight_support["why_not_phi_sector_n_value"]

    first_dynamic_support = [
        row for row in inventory["accepted_support"] if row["support_id"] == "first_dynamic_matter_overlap_rows"
    ][0]
    assert first_dynamic_support["accepted"] is True
    assert first_dynamic_support["row_count"] == 2
    assert "rejects use as a magnitude" in first_dynamic_support["why_not_phi_sector_n_value"]

    threshold_feed = [
        row for row in inventory["rejected_or_open_feeds"] if row["feed_id"] == "threshold_response_functional"
    ][0]
    assert threshold_feed["accepted_source_row_count"] == 0
    assert threshold_feed["closed"] is False

    assert promotion["status"] == "PHI_SECTOR_N_VALUE_PROMOTION_REJECTED_STRICT_VALUES_OPEN"
    assert promotion["required_row_count"] == 9
    assert promotion["accepted_strict_phi_sector_n_row_count"] == 0
    assert promotion["accepted_policy_replay_row_count"] == 0
    assert len(promotion["rows"]) == 9
    assert all(row["source_value_emitted"] is False for row in promotion["rows"])
    assert all(row["accepted_as_strict_source"] is False for row in promotion["rows"])
    assert promotion["guardrail"]["unit_projection_weights_promoted_to_magnitudes"] is False
    assert promotion["guardrail"]["first_dynamic_rows_promoted_to_csk_coefficients"] is False
    assert promotion["guardrail"]["policy_values_promoted_to_source"] is False

    assert trace_acceptance["formal_trace_row_count"] == 9
    assert trace_acceptance["formal_trace_rows_executed"] is True
    assert trace_acceptance["accepted_strict_phi_sector_n_row_count"] == 0
    assert trace_acceptance["accepted_strict_csk_source_row_count"] == 0
    assert trace_acceptance["policy_replay_rows_accepted_as_source"] is False

    assert next_packet["next_required_artifact"] == NEXT
    assert "selected sector-resolving finite response density Phi_sector_N" in next_packet["still_open"]
    assert "policy replay values kept quarantined" in next_packet["closed_now"]

    assert cert["status"] == STATUS
    assert cert["source_inventory_closed"] is True
    assert cert["source_normalized_sector_projection_weights_closed"] is True
    assert cert["first_dynamic_support_rows_accepted"] == 2
    assert cert["accepted_magnitude_bearing_projection_rows"] == 0
    assert cert["accepted_threshold_response_source_rows"] == 0
    assert cert["Phi_sector_N_required_numeric_value_count"] == 9
    assert cert["Phi_sector_N_numeric_values_emitted"] is False
    assert cert["accepted_Phi_sector_N_source_value_count"] == 0
    assert cert["accepted_strict_csk_source_row_count"] == 0
    assert cert["policy_replay_rows_accepted_as_source"] is False
    assert cert["next_required_artifact"] == NEXT

    assert "PhiSectorNSourceValueInventoryTheorem" in note
    assert "accepted strict `Phi_sector_N` values: `0`" in note
    assert NEXT in note
    print("Phi_sector_N source-value inventory / no-knob csk rows audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
