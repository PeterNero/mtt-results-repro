"""Audit selected first PEW gauge-action normalization value/direct-K run."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_firstpewgaugeactionnormalizationvalue_or_directkcertificaterun"
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
SCAN = DATA / SLUG / "repo_wide_pew_numeric_clue_scan.packet.json"
GATE = DATA / SLUG / "first_pew_value_acceptance_gate.packet.json"
NEXT_PACKET = DATA / SLUG / "next_exact_correction_or_physical_normalization.packet.json"
NOTE = CORPUS / "MTT_Selected_FirstPEWGaugeActionNormalizationValue_or_DirectKCertificateRun_v1.md"

STATUS = (
    "MTT_SELECTED_FIRSTPEWGAUGEACTIONNORMALIZATIONVALUE_OR_DIRECTKCERTIFICATERUN_"
    "NUMERIC_SCAN_FILLED_ZERO_ACCEPTED_SOURCE_ROWS"
)
NEXT = "MTT_Selected_AEWCorrectionFactorSourceTheorem_or_PhysicalNormalizationRun_v1"


def load(path: Path) -> dict:
    assert path.exists(), f"missing {path.relative_to(ROOT)}"
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    candidate = load(CANDIDATE)
    cert = load(CERT)
    scan = load(SCAN)
    gate = load(GATE)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    assert candidate["status"] == STATUS
    assert candidate["next_required_artifact"] == NEXT
    assert candidate["theorem"]["name"] == "FirstPEWGaugeActionNormalizationValueRunTheorem"
    assert candidate["theorem"]["proved"] is True
    assert candidate["numeric_candidate_rows_filled"] == 5
    assert candidate["strict_P_EW_source_theorem_closed"] is False
    assert candidate["direct_K_threshold_Omega_H_lambda_closed"] is False
    assert candidate["full_no_knob_closure_claimed"] is False
    assert candidate["true_SM_equivalence_claimed"] is False
    assert candidate["observed_data_used_as_selector"] is False
    assert candidate["target_fitting_used"] is False

    decision = candidate["closure_decision"]
    assert decision["payload_contract_locked"] is True
    assert decision["numeric_candidate_rows_filled"] == 5
    assert decision["accepted_strict_P_EW_source_rows"] == 0
    assert decision["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0
    assert decision["best_formula"] == "8*Delta_G12/pi^2"
    assert abs(decision["best_value"] - 0.06849557446844383) < 1e-16
    assert abs(decision["best_relative_residual"] - 8.426540979088263e-05) < 1e-18
    assert abs(decision["best_correction_factor_required"] - 1.0000842725110486) < 1e-15
    assert decision["source_filled_field_count"] == 0
    assert decision["full_no_knob_closed"] is False
    assert decision["true_SM_equivalence_closed"] is False

    assert scan["status"] == "NUMERIC_CANDIDATES_FILLED_ZERO_ACCEPTED"
    assert scan["closure_claimed"] is True
    assert scan["independent_scalar_count"] == 19154
    assert scan["near_candidate_count"] == 48526
    assert scan["target_value_leakage_excluded"] is True
    assert scan["accepted_source_row_count"] == 0
    assert len(scan["roots_scanned"]) == 6
    assert len(scan["candidate_rows"]) == 5
    assert all(row["accepted_as_source"] is False for row in scan["candidate_rows"])
    assert scan["candidate_rows"][0]["formula"] == "8*Delta_G12/pi^2"

    assert gate["status"] == "FIRST_VALUE_GATE_REJECTS_ALL_CURRENT_NUMERIC_CANDIDATES"
    assert gate["accepted_strict_P_EW_source_rows"] == 0
    assert gate["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0
    assert gate["observed_data_used_as_selector"] is False
    assert gate["target_fitting_used"] is False

    assert next_packet["status"] == "NEXT_IS_CORRECTION_FACTOR_SOURCE_OR_PHYSICAL_NORMALIZATION"
    assert next_packet["next_required_artifact"] == NEXT
    assert "correction factor 1.0000842725110486" in " ".join(next_packet["required_payload"])

    assert cert["status"] == STATUS
    assert cert["theorem_proved"] is True
    assert cert["numeric_candidate_rows_filled"] == 5
    assert cert["accepted_strict_P_EW_source_rows"] == 0
    assert cert["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0
    assert cert["full_no_knob_closed"] is False
    assert cert["true_SM_equivalence_closed"] is False
    assert cert["observed_data_used_as_selector"] is False
    assert cert["target_fitting_used"] is False

    assert "FirstPEWGaugeActionNormalizationValueRunTheorem" in note
    assert "accepted strict `P_EW` rows: `0`" in note
    assert "accepted direct `K_threshold.Omega_H.lambda` rows: `0`" in note
    assert "correction factor required: `1.0000842725110486`" in note
    assert NEXT in note
    print("first PEW normalization value/direct-K run audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
