"""Audit flavor-threshold source-operator / reduced-coefficient theorem."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SLUG = "selected_flavorthresholdsourceoperator_or_reducedcoefficienttheorem"

CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
RANK_TESTS = DATA / SLUG / "reduced_coefficient_rank_tests.packet.json"
CONTRACT = DATA / SLUG / "selected_flavor_threshold_source_operator_contract.packet.json"
NEXT_PACKET = DATA / SLUG / "next_cutset_after_flavor_threshold_reduction.packet.json"
NOTE = CORPUS / "MTT_Selected_FlavorThresholdSourceOperator_or_ReducedCoefficientTheorem_v1.md"

STATUS = (
    "MTT_SELECTED_FLAVORTHRESHOLDSOURCEOPERATOR_OR_REDUCEDCOEFFICIENTTHEOREM_"
    "BUILT_REDUCTION_TESTS_FULL_RANK_SOURCE_OPERATOR_OPEN"
)
NEXT = "MTT_Selected_FlavorSourceOperatorConcreteSearch_or_MinimalNineSlotPolicy_v1"


def load(path: Path) -> dict:
    assert path.exists(), f"missing {path.relative_to(ROOT)}"
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    candidate = load(CANDIDATE)
    cert = load(CERT)
    rank_tests = load(RANK_TESTS)
    contract = load(CONTRACT)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    assert candidate["status"] == STATUS
    assert candidate["next_required_artifact"] == NEXT
    assert candidate["theorem"]["name"] == "FlavorThresholdSourceOperatorReductionWallTheorem"
    assert candidate["theorem"]["proved"] is True
    assert candidate["closure_claimed"] is True
    assert candidate["strict_no_knob_flavor_closure_claimed"] is False
    assert candidate["full_no_knob_closure_claimed"] is False
    assert candidate["observed_data_used_as_selector"] is False
    assert candidate["target_fitting_used"] is False

    decision = candidate["closure_decision"]
    assert decision["selected_family_spectral_basis_closed"] is True
    assert decision["degree2_log_response_basis_closed"] is True
    assert decision["coefficient_matrix_full_rank"] is True
    assert abs(decision["coefficient_matrix_determinant"] + 39.19844590574853) < 1e-10
    assert decision["current_reduced_coefficient_theorem_closed"] is False
    assert decision["selected_flavor_threshold_source_operator_closed"] is False
    assert decision["selected_log_coefficient_source_rows"] == 0
    assert decision["minimal_profile_replay_flavor_ledger_closed"] is True
    assert decision["minimal_profile_replay_parameter_slots"] == 9
    assert decision["strict_no_knob_flavor_closure"] is False
    assert decision["true_SM_equivalence_closed"] is False

    assert rank_tests["rank"] == 3
    assert rank_tests["selected_log_coefficient_source_rows"] == 0
    assert all(test["closes"] is False for test in rank_tests["tests"])
    assert rank_tests["tests"][0]["model"] == "rank_le_2_sector_coefficient_plane"
    assert rank_tests["tests"][1]["max_abs_residual"] > 0
    assert rank_tests["tests"][2]["max_abs_residual"] > 0

    assert contract["accepted_now"] is False
    assert "derive selected flavor threshold/source operator emitting c_{s,k}" in contract["legal_exits"]
    assert "solve c_{s,k} from versioned Yukawa magnitudes and relabel them as source rows" in contract["forbidden_exits"]

    assert next_packet["next_required_artifact"] == NEXT
    assert "selected log coefficient source rows" in next_packet["still_missing"]
    assert "selected three-family spectral basis" in next_packet["not_missing_anymore"]

    assert cert["status"] == STATUS
    assert cert["coefficient_matrix_full_rank"] is True
    assert cert["selected_log_coefficient_source_rows"] == 0
    assert cert["minimal_profile_replay_parameter_slots"] == 9
    assert cert["strict_no_knob_flavor_closure"] is False
    assert "FlavorThresholdSourceOperatorReductionWallTheorem" in note
    assert NEXT in note
    print("flavor-threshold source-operator / reduced-coefficient theorem audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
