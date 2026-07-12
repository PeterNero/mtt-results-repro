"""Audit common-circle bundle csk functional / Phi_flavor_N refinement."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SLUG = "selected_commoncirclebundlecskfunctional_or_phiflavornrefinement"

CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
CORPUS_SUPPORT = DATA / SLUG / "common_circle_corpus_support.packet.json"
CONTRACT = DATA / SLUG / "common_circle_refined_csk_functional_contract.packet.json"
GUARD = DATA / SLUG / "common_circle_sector_resolution_guard.packet.json"
NEXT_PACKET = DATA / SLUG / "next_cutset_after_common_circle_refinement.packet.json"
NOTE = CORPUS / "MTT_Selected_CommonCircleBundleCSKFunctional_or_PhiFlavorNRefinement_v1.md"

STATUS = (
    "MTT_SELECTED_COMMONCIRCLEBUNDLECSKFUNCTIONAL_OR_PHIFLAVORNREFINEMENT_"
    "COMMON_CIRCLE_PLACED_IN_FUNCTIONAL_VALUES_OPEN"
)
NEXT = "MTT_Selected_CommonCircleSectorResponseExecution_or_CSKTraceRows_v1"


def load(path: Path) -> dict:
    assert path.exists(), f"missing {path.relative_to(ROOT)}"
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    candidate = load(CANDIDATE)
    cert = load(CERT)
    corpus_support = load(CORPUS_SUPPORT)
    contract = load(CONTRACT)
    guard = load(GUARD)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    assert candidate["status"] == STATUS
    assert candidate["next_required_artifact"] == NEXT
    assert candidate["theorem"]["name"] == "CommonCircleBundleCSKFunctionalRefinementTheorem"
    assert candidate["theorem"]["proved"] is True
    assert candidate["closure_claimed"] is True
    assert candidate["strict_csk_source_theorem_claimed"] is False
    assert candidate["full_no_knob_closure_claimed"] is False
    assert candidate["true_SM_equivalence_claimed"] is False
    assert candidate["observed_data_used_as_selector"] is False
    assert candidate["target_fitting_used"] is False

    decision = candidate["closure_decision"]
    assert decision["common_circle_applicable_to_csk_functional"] is True
    assert decision["common_circle_placed_inside_Phi_flavor_N"] is True
    assert decision["common_circle_alone_sources_csk"] is False
    assert decision["common_circle_only_shortcut_rejected"] is True
    assert decision["direct_HYM_overlap_attachment_rejected"] is True
    assert decision["csk_matrix_full_rank"] is True
    assert decision["admissible_common_circle_refined_functional_contract_closed"] is True
    assert decision["csk_row_value_obligation_count"] == 9
    assert decision["accepted_strict_csk_source_row_count"] == 0
    assert decision["strict_csk_source_theorem_closed"] is False
    assert decision["full_no_knob_closed"] is False
    assert decision["true_SM_equivalence_closed"] is False

    assert corpus_support["local_bridge_support_present"] is True
    assert any("S^1_cen" in row for row in corpus_support["corpus_reading"])
    assert corpus_support["observed_data_used_as_selector"] is False
    assert corpus_support["target_fitting_used"] is False

    assert "H_cen" in contract["mtt_native_source_form"]
    assert "Phi_sector_N" in contract["mtt_native_source_form"]
    assert "S^1_cen x Sigma_s" in contract["equivalent_bundle_integral_shadow"]
    assert contract["finite_projected_HYM_source_principle_closed"] is True
    assert contract["selected_Rtheta_scalar_value_functional_source_domain_closed"] is True
    assert contract["accepted_strict_csk_source_row_count"] == 0
    assert contract["functional_contract_refined"] is True
    assert contract["functional_values_executed"] is False

    assert guard["common_circle_alone_sources_csk"] is False
    assert guard["imports_sector_blind_hym_nogo"] is True
    assert guard["hym_rows_sector_blind"] is True
    assert guard["csk_matrix_full_rank"] is True
    assert guard["best_sector_blind_shared_row_max_abs_residual"] > 1.0
    assert "selected sector projectors P_u,P_d,P_e" in guard["required_extra_structure"]

    assert next_packet["next_required_artifact"] == NEXT
    assert "emit the finite common-circle holonomy/normalization operator H_cen" in next_packet[
        "ordered_execution_plan"
    ]
    assert "nine c_{s,k} trace evaluations" in next_packet["still_open"]

    assert cert["status"] == STATUS
    assert cert["common_circle_applicable_to_csk_functional"] is True
    assert cert["common_circle_placed_inside_Phi_flavor_N"] is True
    assert cert["common_circle_alone_sources_csk"] is False
    assert cert["admissible_common_circle_refined_functional_contract_closed"] is True
    assert cert["csk_row_value_obligation_count"] == 9
    assert cert["accepted_strict_csk_source_row_count"] == 0
    assert cert["next_required_artifact"] == NEXT
    assert cert["observed_data_used_as_selector"] is False
    assert cert["target_fitting_used"] is False

    assert "CommonCircleBundleCSKFunctionalRefinementTheorem" in note
    assert "H_cen" in note
    assert NEXT in note
    print("common-circle bundle csk functional / Phi_flavor_N refinement audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
