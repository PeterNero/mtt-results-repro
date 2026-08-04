"""Audit spectral Yukawa response basis / coefficient-source wall."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SLUG = "selected_spectralyukawaresponsebasis_or_coefficientsourcewall"

CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
BASIS = DATA / SLUG / "selected_family_spectral_response_basis.packet.json"
COEFF = DATA / SLUG / "diagnostic_log_yukawa_response_coefficients.packet.json"
FUNCTIONAL = DATA / SLUG / "spectral_threshold_response_functional_contract.packet.json"
NEXT_PACKET = DATA / SLUG / "next_coefficient_source_rows_or_minimal_parameter_policy.packet.json"
NOTE = CORPUS / "MTT_Selected_SpectralYukawaResponseBasis_or_CoefficientSourceWall_v1.md"

STATUS = (
    "MTT_SELECTED_SPECTRALYUKAWARESPONSEBASIS_OR_COEFFICIENTSOURCEWALL_"
    "BASIS_CLOSED_COEFFICIENT_SOURCE_OPEN"
)
NEXT = "MTT_Selected_LogYukawaCoefficientSourceRows_or_MinimalFlavorParameterLedger_v1"


def load(path: Path) -> dict:
    assert path.exists(), f"missing {path.relative_to(ROOT)}"
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    candidate = load(CANDIDATE)
    cert = load(CERT)
    basis = load(BASIS)
    coeff = load(COEFF)
    functional = load(FUNCTIONAL)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    assert candidate["status"] == STATUS
    assert candidate["next_required_artifact"] == NEXT
    assert candidate["theorem"]["name"] == "SelectedSpectralYukawaResponseBasisTheorem"
    assert candidate["theorem"]["proved"] is True
    assert candidate["basis_map_closed"] is True
    assert candidate["coefficient_source_rows_closed"] is False
    assert candidate["accepted_Yukawa_magnitudes_as_no_knob_predictions"] is False
    assert candidate["accepted_for_SM_parity_profile_replay"] is True
    assert candidate["observed_data_used_as_selector"] is False
    assert candidate["target_fitting_used"] is False

    decision = candidate["closure_decision"]
    assert decision["selected_family_spectral_basis_closed"] is True
    assert decision["unique_degree2_log_response_basis_closed"] is True
    assert decision["coefficient_domain_closed"] is True
    assert decision["diagnostic_common_scale_replay_exact"] is True
    assert decision["diagnostic_log_coefficient_rows_filled"] == 9
    assert decision["selected_log_coefficient_source_rows"] == 0
    assert decision["Yukawa_magnitude_value_functional_closed_as_structure"] is True
    assert decision["Yukawa_magnitude_value_functional_closed_as_no_knob_source"] is False
    assert decision["minimal_parameter_flavor_ledger_closed"] is False
    assert decision["true_SM_equivalence_closed"] is False

    assert basis["status"] == "SELECTED_FAMILY_SPECTRAL_RESPONSE_BASIS_CLOSED"
    assert basis["basis_nonsingular"] is True
    assert basis["accepted_as_selected_basis_map"] is True
    assert basis["accepted_as_magnitude_value_source"] is False
    assert len(basis["lagrange_projector_polynomials"]) == 3
    assert abs(basis["vandermonde_determinant"]) > 1e-12

    assert coeff["coefficient_domain_closed"] is True
    assert coeff["coefficient_source_rows_closed"] is False
    assert coeff["coefficient_row_count"] == 9
    assert len(coeff["sector_rows"]) == 3
    assert coeff["max_abs_reconstruction_residual"] < 1e-12
    assert all(row["accepted_as_no_knob_coefficient_source"] is False for row in coeff["sector_rows"])
    assert all(row["accepted_as_profile_replay_coefficients"] is True for row in coeff["sector_rows"])

    assert functional["status"] == "SPECTRAL_FUNCTIONAL_DERIVED_COEFFICIENT_SOURCE_WALL_EXPOSED"
    assert functional["input_status_reconciliation"]["27_matrix_minimal_ledger_closed"] is True
    assert functional["input_status_reconciliation"]["source_projection_weights_closed"] is True
    assert functional["input_status_reconciliation"]["magnitude_bearing_projection_weights_closed"] is False
    assert functional["input_status_reconciliation"]["higher_response_sector_coefficients_closed"] is False
    assert functional["input_status_reconciliation"]["previous_value_functional_closed"] is False

    assert next_packet["next_required_artifact"] == NEXT
    assert cert["status"] == STATUS
    assert cert["basis_map_closed"] is True
    assert cert["coefficient_source_rows_closed"] is False
    assert cert["diagnostic_log_coefficient_rows_filled"] == 9
    assert cert["selected_log_coefficient_source_rows"] == 0
    assert "SelectedSpectralYukawaResponseBasisTheorem" in note
    assert NEXT in note
    print("spectral Yukawa response basis / coefficient-source wall audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
