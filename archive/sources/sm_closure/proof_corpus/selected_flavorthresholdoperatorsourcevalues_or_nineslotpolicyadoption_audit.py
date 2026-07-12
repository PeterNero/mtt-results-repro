"""Audit flavor-threshold operator source values / nine-slot policy adoption."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SLUG = "selected_flavorthresholdoperatorsourcevalues_or_nineslotpolicyadoption"

CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
SOURCE_VALUES = DATA / SLUG / "flavor_threshold_operator_policy_source_values.packet.json"
VALUE_TABLE = DATA / SLUG / "flavor_threshold_operator_value_table.packet.json"
ADOPTION = DATA / SLUG / "nine_slot_flavor_policy_adoption_decision.packet.json"
STRICT = DATA / SLUG / "strict_flavor_noknob_recheck_after_policy_values.packet.json"
NEXT_PACKET = DATA / SLUG / "next_cutset_after_flavor_policy_source_value_emission.packet.json"
NOTE = CORPUS / "MTT_Selected_FlavorThresholdOperatorSourceValues_or_NineSlotPolicyAdoption_v1.md"

STATUS = (
    "MTT_SELECTED_FLAVORTHRESHOLDOPERATORSOURCEVALUES_OR_NINESLOTPOLICYADOPTION_"
    "EMITTED_POLICY_SOURCE_VALUES_STRICT_NOKNOB_OPEN"
)
NEXT = "MTT_Selected_FlavorOperatorValueUse_or_CKMPMNSOrientationBridge_v1"


def load(path: Path) -> dict:
    assert path.exists(), f"missing {path.relative_to(ROOT)}"
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    candidate = load(CANDIDATE)
    cert = load(CERT)
    source_values = load(SOURCE_VALUES)
    value_table = load(VALUE_TABLE)
    adoption = load(ADOPTION)
    strict = load(STRICT)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    assert candidate["status"] == STATUS
    assert candidate["next_required_artifact"] == NEXT
    assert candidate["theorem"]["name"] == "FlavorOperatorPolicySourceValueEmissionTheorem"
    assert candidate["theorem"]["proved"] is True
    assert candidate["closure_claimed"] is True
    assert candidate["strict_no_knob_flavor_closure_claimed"] is False
    assert candidate["full_no_knob_closure_claimed"] is False
    assert candidate["observed_profile_values_used_as_parameter_values"] is True
    assert candidate["observed_data_used_as_selector"] is False
    assert candidate["target_fitting_used"] is False

    decision = candidate["closure_decision"]
    assert decision["flavor_operator_values_emitted"] is True
    assert decision["policy_source_value_row_count"] == 9
    assert decision["minimal_nine_slot_policy_adopted"] is True
    assert decision["minimal_profile_replay_parameter_slots"] == 9
    assert decision["accepted_selected_no_knob_coefficient_source_row_count"] == 0
    assert decision["strict_no_knob_flavor_closure"] is False
    assert decision["true_SM_equivalence_closed"] is False

    assert source_values["policy_source_value_row_count"] == 9
    assert source_values["strict_selected_no_knob_source_row_count"] == 0
    assert source_values["observed_profile_values_used_as_parameter_values"] is True
    assert all(row["accepted_as_minimal_policy_source_value"] is True for row in source_values["rows"])
    assert all(row["accepted_as_selected_no_knob_source_row"] is False for row in source_values["rows"])

    assert value_table["policy_source_value_row_count"] == 9
    assert value_table["strict_selected_no_knob_source_row_count"] == 0
    assert sorted(value_table["sector_operator_coefficients"].keys()) == ["d", "e", "u"]

    assert adoption["policy_adopted"] is True
    assert adoption["profile_replay_parameter_slots"] == 9
    assert adoption["strict_no_knob_flavor_closure"] is False

    assert strict["accepted_selected_coefficient_row_count"] == 0
    assert strict["policy_source_value_row_count"] == 9
    assert strict["strict_no_knob_flavor_closure"] is False

    assert next_packet["next_required_artifact"] == NEXT
    assert "same concrete flavor operator has nine attached policy source values" in next_packet["closed_now"]
    assert "source-emitted c_{s,k} rows from a selected threshold operator" in next_packet["still_open"]

    assert cert["status"] == STATUS
    assert cert["policy_source_value_row_count"] == 9
    assert cert["accepted_selected_no_knob_coefficient_source_row_count"] == 0
    assert cert["strict_no_knob_flavor_closure"] is False
    assert cert["observed_data_used_as_selector"] is False
    assert "FlavorOperatorPolicySourceValueEmissionTheorem" in note
    assert NEXT in note
    print("flavor-threshold operator source values / nine-slot policy adoption audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
