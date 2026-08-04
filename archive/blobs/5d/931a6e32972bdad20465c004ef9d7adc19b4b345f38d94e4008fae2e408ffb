"""Audit c_{s,k} finite-functional obligation / sector-blind HYM no-go."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SLUG = "selected_cskfinitefunctionalobligation_or_sectorblindhymnogotheorem"

CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NO_GO = DATA / SLUG / "sector_blind_hym_direct_attachment_nogo.packet.json"
CONTRACT = DATA / SLUG / "csk_finite_response_functional_contract.packet.json"
MANIFEST = DATA / SLUG / "csk_row_value_obligation_manifest.packet.json"
NEXT_PACKET = DATA / SLUG / "next_cutset_after_csk_functional_obligation.packet.json"
NOTE = CORPUS / "MTT_Selected_CSKFiniteFunctionalObligation_or_SectorBlindHYMNoGoTheorem_v1.md"

STATUS = (
    "MTT_SELECTED_CSKFINITEFUNCTIONALOBLIGATION_OR_SECTORBLINDHYMNOGOTHEOREM_"
    "DIRECT_HYM_ATTACH_REJECTED_FINITE_FUNCTIONAL_OBLIGATION_CLOSED"
)
NEXT = "MTT_Selected_CSKFiniteResponseFunctionalExecution_or_SectorProjectionWeights_v1"


def load(path: Path) -> dict:
    assert path.exists(), f"missing {path.relative_to(ROOT)}"
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    candidate = load(CANDIDATE)
    cert = load(CERT)
    no_go = load(NO_GO)
    contract = load(CONTRACT)
    manifest = load(MANIFEST)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    assert candidate["status"] == STATUS
    assert candidate["next_required_artifact"] == NEXT
    assert candidate["theorem"]["name"] == "CSKFiniteFunctionalObligationAndSectorBlindHYMNoGoTheorem"
    assert candidate["theorem"]["proved"] is True
    assert candidate["closure_claimed"] is True
    assert candidate["strict_csk_source_theorem_claimed"] is False
    assert candidate["full_no_knob_closure_claimed"] is False
    assert candidate["true_SM_equivalence_claimed"] is False
    assert candidate["observed_data_used_as_selector"] is False
    assert candidate["target_fitting_used"] is False

    decision = candidate["closure_decision"]
    assert decision["direct_HYM_overlap_attachment_rejected"] is True
    assert decision["hym_rows_sector_blind"] is True
    assert decision["csk_matrix_full_rank"] is True
    assert decision["best_sector_blind_shared_row_max_abs_residual"] > 1.0
    assert decision["finite_projected_HYM_source_principle_closed"] is True
    assert decision["selected_Rtheta_scalar_value_functional_source_domain_closed"] is True
    assert decision["sector_aware_projection_skeleton_closed"] is True
    assert decision["admissible_csk_source_functional_contract_closed"] is True
    assert decision["csk_row_value_obligation_count"] == 9
    assert decision["accepted_strict_csk_source_row_count"] == 0
    assert decision["one_to_three_universal_parameter_reduction_closed"] is False
    assert decision["strict_csk_source_theorem_closed"] is False
    assert decision["full_no_knob_closed"] is False
    assert decision["true_SM_equivalence_closed"] is False

    assert no_go["direct_attachment_rejected"] is True
    assert no_go["hym_rows_sector_blind"] is True
    assert len(no_go["hym_generation_vector"]) == 3
    assert abs(no_go["csk_matrix_determinant"]) > 1.0
    assert no_go["csk_matrix_full_rank"] is True
    assert no_go["best_sector_blind_shared_row_max_abs_residual"] > 1.0
    assert no_go["observed_data_used_as_selector"] is False
    assert no_go["target_fitting_used"] is False

    assert contract["finite_projected_HYM_source_principle_closed"] is True
    assert contract["automatic_finite_cutoff_exactness_closed"] is True
    assert contract["selected_Rtheta_scalar_value_functional_source_domain_closed"] is True
    assert contract["sector_aware_projection_skeleton_closed"] is True
    assert contract["all_sectors_family_resolved"] is True
    assert contract["family_resolving_operator_closed"] is True
    assert "Tr_N(P_s * B_k * Phi_flavor_N)" in contract["required_source_form"]
    assert contract["accepted_strict_csk_source_row_count"] == 0
    assert contract["functional_contract_closed"] is True
    assert contract["functional_values_executed"] is False

    assert manifest["policy_source_value_row_count"] == 9
    assert manifest["strict_selected_no_knob_source_row_count"] == 0
    assert manifest["ledger_profile_replay_slots"] == 9
    assert manifest["coefficient_matrix_full_rank"] is True
    assert len(manifest["rows"]) == 9
    assert all(row["strict_source_value_emitted"] is False for row in manifest["rows"])
    assert all(row["accepted_as_no_knob_source_row"] is False for row in manifest["rows"])

    assert next_packet["next_required_artifact"] == NEXT
    assert "construct P_u,P_d,P_e as selected sector projectors in A_N" in next_packet[
        "ordered_execution_plan"
    ]
    assert "strict selected c_{s,k} numerical source rows" in next_packet["not_closed"]

    assert cert["status"] == STATUS
    assert cert["direct_HYM_overlap_attachment_rejected"] is True
    assert cert["hym_rows_sector_blind"] is True
    assert cert["csk_matrix_full_rank"] is True
    assert cert["admissible_csk_source_functional_contract_closed"] is True
    assert cert["csk_row_value_obligation_count"] == 9
    assert cert["accepted_strict_csk_source_row_count"] == 0
    assert cert["next_required_artifact"] == NEXT
    assert cert["observed_data_used_as_selector"] is False
    assert cert["target_fitting_used"] is False

    assert "CSKFiniteFunctionalObligationAndSectorBlindHYMNoGoTheorem" in note
    assert "directly attached" in note or "directly" in note
    assert NEXT in note
    print("csk finite-functional obligation / sector-blind HYM no-go audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
