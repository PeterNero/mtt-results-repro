"""Audit log-Yukawa coefficient source-row / minimal flavor-parameter ledger."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SLUG = "selected_logyukawacoefficientsourcerows_or_minimalflavorparameterledger"

CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
SOURCE_RECHECK = DATA / SLUG / "log_yukawa_coefficient_source_row_recheck.packet.json"
RANK_TEST = DATA / SLUG / "universal_parameter_reduction_rank_test.packet.json"
LEDGER = DATA / SLUG / "minimal_flavor_parameter_ledger.packet.json"
NEXT_PACKET = DATA / SLUG / "next_source_operator_or_flavor_parameter_selection.packet.json"
NOTE = CORPUS / "MTT_Selected_LogYukawaCoefficientSourceRows_or_MinimalFlavorParameterLedger_v1.md"

STATUS = (
    "MTT_SELECTED_LOGYUKAWACOEFFICIENTSOURCEROWS_OR_MINIMALFLAVORPARAMETERLEDGER_"
    "SOURCE_ROWS_ZERO_FULL_RANK_LEDGER_BUILT"
)
NEXT = "MTT_Selected_FlavorThresholdSourceOperator_or_ReducedCoefficientTheorem_v1"


def load(path: Path) -> dict:
    assert path.exists(), f"missing {path.relative_to(ROOT)}"
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    candidate = load(CANDIDATE)
    cert = load(CERT)
    source = load(SOURCE_RECHECK)
    rank = load(RANK_TEST)
    ledger = load(LEDGER)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    assert candidate["status"] == STATUS
    assert candidate["next_required_artifact"] == NEXT
    assert candidate["theorem"]["name"] == "LogYukawaCoefficientSourceRowsOrMinimalFlavorLedgerTheorem"
    assert candidate["theorem"]["proved"] is True
    assert candidate["sm_parity_profile_replay_ledger_closed"] is True
    assert candidate["strict_no_knob_flavor_closure_claimed"] is False
    assert candidate["observed_data_used_as_selector"] is False
    assert candidate["target_fitting_used"] is False

    decision = candidate["closure_decision"]
    assert decision["selected_family_spectral_basis_closed"] is True
    assert decision["diagnostic_log_coefficient_rows_filled"] == 9
    assert decision["selected_log_coefficient_source_rows"] == 0
    assert decision["coefficient_matrix_full_rank"] is True
    assert decision["one_to_three_universal_parameter_reduction_closed"] is False
    assert decision["minimal_profile_replay_flavor_ledger_closed"] is True
    assert decision["minimal_profile_replay_parameter_slots"] == 9
    assert decision["strict_no_knob_flavor_closure"] is False
    assert decision["true_SM_equivalence_closed"] is False

    assert source["selected_log_coefficient_source_rows"] == 0
    assert source["diagnostic_coefficients_imported"] == 9
    assert source["source_search_result"]["exact_literals_found_outside_diagnostic_packets"] == 0
    assert source["source_search_result"]["accepted_current_source_owner"] is False

    assert rank["full_rank"] is True
    assert abs(rank["determinant"] + 39.19844590574854) < 1e-12
    assert rank["universal_policy_selected_parameter_count_now"] == 0
    assert rank["maximum_live_universal_parameters"] == 3
    assert all(test["closes"] is False for test in rank["tests"])
    assert rank["tests"][0]["lane"] == "shared_polynomial_UP3"
    assert rank["tests"][0]["max_abs_residual"] > 1.0

    assert ledger["basis_map_closed"] is True
    assert ledger["coefficient_domain_closed"] is True
    assert ledger["profile_replay_parameter_slots"] == 9
    assert ledger["selected_no_knob_source_slots"] == 0
    assert ledger["strict_no_knob_flavor_closure"] is False
    assert ledger["sm_parity_profile_replay_ledger_closed"] is True
    assert len(ledger["rows"]) == 9
    assert all(row["accepted_as_profile_replay_parameter"] is True for row in ledger["rows"])
    assert all(row["accepted_as_no_knob_source_row"] is False for row in ledger["rows"])

    assert next_packet["next_required_artifact"] == NEXT
    assert "derive a selected flavor threshold/source operator emitting c_{s,k}" in next_packet["ordered_routes"]
    assert cert["status"] == STATUS
    assert cert["diagnostic_log_coefficient_rows_filled"] == 9
    assert cert["selected_log_coefficient_source_rows"] == 0
    assert cert["coefficient_matrix_full_rank"] is True
    assert cert["minimal_profile_replay_parameter_slots"] == 9
    assert "LogYukawaCoefficientSourceRowsOrMinimalFlavorLedgerTheorem" in note
    assert NEXT in note
    print("log-Yukawa coefficient source rows / minimal flavor ledger audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
