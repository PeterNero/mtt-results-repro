"""Audit mass-ratio orientation law search / finite-phase CKM clue."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SLUG = "selected_massratioorientationlawsearch_or_finitephaseckmclue"

CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
FINITE_PHASE = DATA / SLUG / "finite_phase_ckm_clue.packet.json"
MASS_RATIO = DATA / SLUG / "mass_ratio_orientation_law_search.packet.json"
NEXT_PACKET = DATA / SLUG / "next_cutset_after_massratio_orientation_search.packet.json"
NOTE = CORPUS / "MTT_Selected_MassRatioOrientationLawSearch_or_FinitePhaseCKMClue_v1.md"

STATUS = (
    "MTT_SELECTED_MASSRATIOORIENTATIONLAWSEARCH_OR_FINITEPHASECKMCLUE_"
    "BUILT_Q79_PHASE_CLUE_ORIENTATION_SOURCE_OPEN"
)
NEXT = "MTT_Selected_CKMQ79PhaseSourceBridge_or_MassRatioOrientationTheorem_v1"


def load(path: Path) -> dict:
    assert path.exists(), f"missing {path.relative_to(ROOT)}"
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    candidate = load(CANDIDATE)
    cert = load(CERT)
    finite_phase = load(FINITE_PHASE)
    mass_ratio = load(MASS_RATIO)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    assert candidate["status"] == STATUS
    assert candidate["next_required_artifact"] == NEXT
    assert candidate["theorem"]["name"] == "MassRatioOrientationSearchAndFinitePhaseCKMClueTheorem"
    assert candidate["theorem"]["proved"] is True
    assert candidate["closure_claimed"] is True
    assert candidate["full_no_knob_closure_claimed"] is False
    assert candidate["true_SM_equivalence_claimed"] is False
    assert candidate["orientation_source_theorem_claimed"] is False
    assert candidate["observed_data_used_as_selector"] is False
    assert candidate["target_fitting_used"] is False

    decision = candidate["closure_decision"]
    assert decision["finite_q79_ckm_phase_clue_found"] is True
    assert decision["q79_CKM_phase_residual_deg"] < decision["plus_i_CKM_phase_residual_deg"]
    assert decision["GST_like_Cabibbo_row_promising"] is True
    assert decision["GST_like_23_13_simple_law_rejected"] is True
    assert decision["selected_orientation_source_theorem_closed"] is False
    assert decision["selected_CKM_PMNS_values_derived"] is False
    assert decision["full_true_SM_equivalence_closed"] is False

    assert finite_phase["status"] == "Q79_CLOSE_TO_CKM_CP_PHASE_SOURCE_BRIDGE_OPEN"
    assert finite_phase["q79_to_CKM_absolute_phase_residual_deg"] < finite_phase[
        "plus_i_to_CKM_absolute_phase_residual_deg"
    ]
    assert finite_phase["strict_source_bridge_closed"] is False
    assert "diagnostic only" in finite_phase["target_fitting_warning"]

    gst = mass_ratio["orthogonal_complex_nesting_tests"]
    assert mass_ratio["source_law_closed"] is False
    assert mass_ratio["observed_data_used_as_selector"] is False
    assert mass_ratio["target_fitting_used"] is False
    assert gst["GST_12"]["plus_i_relative_residual"] < 0.02
    assert gst["GST_23"]["continuous_phase_can_hit_target"] is False
    assert gst["GST_13"]["continuous_phase_can_hit_target"] is False
    assert len(mass_ratio["best_rational_exponent_rows"]["CKM_s12"]) == 10

    assert next_packet["next_required_artifact"] == NEXT
    assert "derive the physical CKM phase map delta_CKM = 2*pi*79/448 plus allowed transport correction or prove exact equality in the selected convention" in next_packet[
        "remaining_to_promote"
    ]

    assert cert["status"] == STATUS
    assert cert["finite_q79_ckm_phase_clue_found"] is True
    assert cert["GST_like_Cabibbo_row_promising"] is True
    assert cert["GST_like_23_13_simple_law_rejected"] is True
    assert cert["selected_orientation_source_theorem_closed"] is False
    assert cert["observed_data_used_as_selector"] is False
    assert cert["target_fitting_used"] is False
    assert NEXT in note
    assert "MassRatioOrientationSearchAndFinitePhaseCKMClueTheorem" in note
    print("mass-ratio orientation law search / finite-phase CKM clue audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
