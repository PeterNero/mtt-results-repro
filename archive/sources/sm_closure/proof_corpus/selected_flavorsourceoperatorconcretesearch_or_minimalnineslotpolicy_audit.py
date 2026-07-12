"""Audit concrete flavor source-operator search / minimal nine-slot policy."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SLUG = "selected_flavorsourceoperatorconcretesearch_or_minimalnineslotpolicy"

CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
FEATURES = DATA / SLUG / "source_native_feature_rows.packet.json"
PROFILE_OPERATOR = DATA / SLUG / "exact_profile_flavor_operator.packet.json"
VALIDATOR = DATA / SLUG / "strict_flavor_source_operator_validator.packet.json"
SEARCH = DATA / SLUG / "concrete_source_operator_search.packet.json"
POLICY = DATA / SLUG / "minimal_nine_slot_profile_policy.packet.json"
NOTE = CORPUS / "MTT_Selected_FlavorSourceOperatorConcreteSearch_or_MinimalNineSlotPolicy_v1.md"

STATUS = (
    "MTT_SELECTED_FLAVORSOURCEOPERATORCONCRETESEARCH_OR_MINIMALNINESLOTPOLICY_"
    "BUILT_EXACT_PROFILE_OPERATOR_STRICT_SOURCE_OPEN"
)
NEXT = "MTT_Selected_FlavorThresholdOperatorSourceValues_or_NineSlotPolicyAdoption_v1"


def load(path: Path) -> dict:
    assert path.exists(), f"missing {path.relative_to(ROOT)}"
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    candidate = load(CANDIDATE)
    cert = load(CERT)
    features = load(FEATURES)
    profile = load(PROFILE_OPERATOR)
    validator = load(VALIDATOR)
    search = load(SEARCH)
    policy = load(POLICY)
    note = NOTE.read_text(encoding="utf-8")

    assert candidate["status"] == STATUS
    assert candidate["next_required_artifact"] == NEXT
    assert candidate["theorem"]["name"] == "ConcreteFlavorOperatorReplayVsSourceTheorem"
    assert candidate["theorem"]["proved"] is True
    assert candidate["closure_claimed"] is True
    assert candidate["strict_no_knob_flavor_closure_claimed"] is False
    assert candidate["full_no_knob_closure_claimed"] is False
    assert candidate["observed_data_used_as_selector"] is False
    assert candidate["target_fitting_used"] is False

    decision = candidate["closure_decision"]
    assert decision["formal_flavor_operator_skeleton_closed"] is True
    assert decision["exact_profile_replay_operator_emitted"] is True
    assert decision["accepted_profile_replay_operator_row_count"] == 9
    assert decision["accepted_selected_coefficient_source_row_count"] == 0
    assert decision["selected_flavor_threshold_source_operator_closed"] is False
    assert decision["strict_no_knob_flavor_closure"] is False
    assert decision["minimal_nine_slot_profile_policy_closed"] is True
    assert decision["minimal_profile_replay_parameter_slots"] == 9

    assert features["accepted_as_coefficient_values"] is False
    assert len(features["features_by_sector"]) == 3
    assert profile["accepted_profile_replay_row_count"] == 9
    assert profile["accepted_selected_no_knob_source_row_count"] == 0
    assert all(row["accepted_as_profile_replay_operator_row"] is True for row in profile["rows"])
    assert all(row["accepted_as_selected_no_knob_source_row"] is False for row in profile["rows"])

    assert validator["accepted_selected_source_operator"] is False
    assert validator["accepted_selected_coefficient_row_count"] == 0
    assert validator["profile_replay_operator_available"] is True
    assert validator["profile_replay_operator_row_count"] == 9

    assert search["status"] == "CONCRETE_SEARCH_EXECUTED_NO_STRICT_SOURCE_VALUES"
    assert len(search["lanes"]) == 4
    assert all(lane["accepted_as_selected_source_operator"] is False for lane in search["lanes"])
    assert search["lanes"][0]["max_abs_residual"] > 1.0
    assert search["lanes"][1]["max_abs_residual"] > 0.0
    assert search["lanes"][3]["accepted_as_profile_replay_operator"] is True

    assert policy["profile_replay_policy_closed"] is True
    assert policy["profile_replay_parameter_slots"] == 9
    assert policy["strict_no_knob_flavor_closure"] is False

    assert cert["status"] == STATUS
    assert cert["accepted_profile_replay_operator_row_count"] == 9
    assert cert["accepted_selected_coefficient_source_row_count"] == 0
    assert cert["minimal_profile_replay_parameter_slots"] == 9
    assert cert["strict_no_knob_flavor_closure"] is False
    assert "ConcreteFlavorOperatorReplayVsSourceTheorem" in note
    assert NEXT in note
    print("flavor source-operator concrete search / minimal nine-slot policy audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
