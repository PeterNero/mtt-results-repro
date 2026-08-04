"""Audit corpus flavor-coefficient theorem scan / R_theta provenance frontier."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SLUG = "selected_corpusflavorcoefficienttheorem_scan_or_rthetaprovenancefrontier"

CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
PAPER_SCAN = DATA / SLUG / "paper_corpus_flavor_coefficient_scan.packet.json"
REPO_SCAN = DATA / SLUG / "repo_rtheta_coefficient_source_status.packet.json"
DECISION = DATA / SLUG / "corpus_match_decision.packet.json"
NEXT_PACKET = DATA / SLUG / "next_rtheta_provenance_frontier.packet.json"
NOTE = CORPUS / "MTT_Selected_CorpusFlavorCoefficientTheoremScan_or_RThetaProvenanceFrontier_v1.md"

STATUS = (
    "MTT_SELECTED_CORPUSFLAVORCOEFFICIENTTHEOREMSCAN_OR_RTHETAPROVENANCEFRONTIER_"
    "STRUCTURE_FOUND_SOURCE_VALUES_OPEN"
)
NEXT = "MTT_Selected_RThetaPiKernel_from_SelectedHYMConnection_or_BNBasisEmission_v1"


def load(path: Path) -> dict:
    assert path.exists(), f"missing {path.relative_to(ROOT)}"
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    candidate = load(CANDIDATE)
    cert = load(CERT)
    paper = load(PAPER_SCAN)
    repo = load(REPO_SCAN)
    decision = load(DECISION)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    assert candidate["status"] == STATUS
    assert candidate["next_required_artifact"] == NEXT
    assert candidate["corpus_contains_close_structural_match"] is True
    assert candidate["corpus_closes_numeric_source_rows"] is False
    assert candidate["theorem"]["name"] == "CorpusFlavorCoefficientTheoremScanAndRThetaFrontierTheorem"
    assert candidate["theorem"]["proved"] is True
    assert candidate["observed_data_used_as_selector"] is False
    assert candidate["target_fitting_used"] is False

    cd = candidate["closure_decision"]
    assert cd["paper_overlap_response_support_found"] is True
    assert cd["paper_numeric_source_theorem_found"] is False
    assert cd["rtheta_basis_map_closed"] is True
    assert cd["rtheta_coefficient_functional_skeleton_closed"] is True
    assert cd["rtheta_domain_readiness_closed"] is True
    assert cd["firstpass_Rtheta_coefficient_values_closed"] is True
    assert cd["latest_alpha1_dotd_provenance_imported"] is True
    assert cd["latest_value_evaluator_readiness_present_count"] == 5
    assert cd["latest_value_evaluator_readiness_required_count"] == 7
    assert cd["selected_Rtheta_coefficient_source_rows"] == 0
    assert cd["selected_value_evaluator_closed"] is False
    assert cd["Pi_Rtheta_closed"] is False
    assert cd["strict_no_knob_charged_yukawa_values_closed"] is False

    assert paper["status"] == "PAPER_CORPUS_SUPPORTS_OVERLAP_RESPONSE_NOT_NUMERIC_SOURCE_ROWS"
    assert len(paper["findings"]) == 4
    assert all(item["source_theorem_for_c_s_k"] is False for item in paper["findings"])

    assert repo["status"] == "RTHETA_FUNCTIONAL_SKELETON_FOUND_VALUES_OPEN"
    assert repo["positive_matches"]["basis_map_closed"] is True
    assert repo["positive_matches"]["charged_basis_row_count"] == 9
    assert repo["positive_matches"]["coefficient_functional_skeleton_closed"] is True
    assert repo["positive_matches"]["charged_functional_row_count"] == 9
    assert repo["positive_matches"]["latest_alpha1_dotd_provenance_imported"] is True
    assert repo["positive_matches"]["latest_value_evaluator_readiness_present_count"] == 5
    assert repo["positive_matches"]["latest_value_evaluator_readiness_required_count"] == 7
    assert repo["still_open"]["selected_Rtheta_coefficient_values_closed"] is False
    assert repo["still_open"]["selected_Rtheta_source_rows_closed"] is False
    assert repo["still_open"]["selected_value_evaluator_closed"] is False
    assert repo["still_open"]["Pi_Rtheta_closed"] is False
    assert repo["still_open"]["accepted_coefficient_value_count"] == 0
    assert repo["still_open"]["latest_still_open_readiness_rows"] == [
        "coherent_spectral_projector_retention",
        "selected_DE_Riesz_Green_dotD",
    ]
    assert repo["still_open"]["latest_pi_minimal_missing_primitives"] == [
        "gauge_fixed_selected_HYM_connection_representative",
        "selected_finite_basis_quadrature_error_contract",
        "selected_D_E_Riesz_Green_from_connection",
        "coherent_spectral_zero_mode_projector_retention",
    ]

    assert decision["answer"] == "yes_structural_no_numeric_source"
    assert "R_theta coefficient functional skeleton" in decision["best_match"]
    assert next_packet["next_required_artifact"] == NEXT
    assert next_packet["status"] == "NEXT_IS_PI_RTHETA_FROM_SELECTED_HYM_CONNECTION_OR_BN_BASIS"
    assert next_packet["latest_minimal_missing_primitives"] == [
        "gauge_fixed_selected_HYM_connection_representative",
        "selected_finite_basis_quadrature_error_contract",
        "selected_D_E_Riesz_Green_from_connection",
        "coherent_spectral_zero_mode_projector_retention",
    ]
    assert cert["status"] == STATUS
    assert cert["corpus_contains_close_structural_match"] is True
    assert cert["corpus_closes_numeric_source_rows"] is False
    assert cert["latest_alpha1_dotd_provenance_imported"] is True
    assert cert["latest_value_evaluator_readiness_present_count"] == 5
    assert cert["latest_value_evaluator_readiness_required_count"] == 7
    assert cert["selected_Rtheta_coefficient_source_rows"] == 0
    assert "R_theta" in note
    assert NEXT in note
    print("corpus flavor coefficient theorem scan / R_theta frontier audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
