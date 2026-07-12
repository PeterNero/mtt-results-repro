"""Audit q79 CKM phase bridge import / heavy-link orientation target."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SLUG = "selected_ckmq79phasebridgeimport_or_heavylinkorientationtarget"

CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
Q79_IMPORT = DATA / SLUG / "q79_ckm_phase_bridge_import.packet.json"
POSTCHECK = DATA / SLUG / "current_ckm_jarlskog_postcheck_from_q79.packet.json"
HEAVY_LINK = DATA / SLUG / "heavy_link_higher_breakdown_orientation_target.packet.json"
BOUNDARY = DATA / SLUG / "no_proxy_flavor_boundary_after_q79_import.packet.json"
NEXT_PACKET = DATA / SLUG / "next_cutset_after_ckm_q79_phase_bridge_import.packet.json"
NOTE = CORPUS / "MTT_Selected_CKMQ79PhaseBridgeImport_or_HeavyLinkOrientationTarget_v1.md"

STATUS = (
    "MTT_SELECTED_CKMQ79PHASEBRIDGEIMPORT_OR_HEAVYLINKORIENTATIONTARGET_"
    "IMPORTED_CKMPHASE_CONTACT_HEAVYLINK_VALUES_OPEN"
)
NEXT = "MTT_Selected_HeavyLinkVectorValues_or_CKMHigherBreakdownOrientationLaw_v1"


def load(path: Path) -> dict:
    assert path.exists(), f"missing {path.relative_to(ROOT)}"
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    candidate = load(CANDIDATE)
    cert = load(CERT)
    q79_import = load(Q79_IMPORT)
    postcheck = load(POSTCHECK)
    heavy_link = load(HEAVY_LINK)
    boundary = load(BOUNDARY)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    assert candidate["status"] == STATUS
    assert candidate["next_required_artifact"] == NEXT
    assert candidate["theorem"]["name"] == "CKMQ79PhaseBridgeImportAndHeavyLinkTargetTheorem"
    assert candidate["theorem"]["proved"] is True
    assert candidate["closure_claimed"] is True
    assert candidate["full_no_knob_closure_claimed"] is False
    assert candidate["true_SM_equivalence_claimed"] is False
    assert candidate["observed_data_used_as_selector"] is False
    assert candidate["target_fitting_used"] is False

    decision = candidate["closure_decision"]
    assert decision["selected_q79_branch_imported"] is True
    assert decision["selected_CKM_CP_phase_contact_imported"] is True
    assert decision["selected_kernel_principle_imported"] is True
    assert decision["no_empirical_label_scan"] is True
    assert decision["q_mod_448"] == 79
    assert 63.48 < decision["delta_q79_deg"] < 63.49
    assert decision["current_CKM_phase_residual_deg"] < 3.0
    assert decision["current_J_q79_relative_residual"] < 0.03
    assert decision["CKM_angles_derived"] is False
    assert decision["CKM_heavy_link_calculator_ready"] is True
    assert decision["selected_heavy_link_values_emitted"] is False
    assert decision["leading_CKM_noncommutation_values_closed"] is False
    assert decision["selected_csk_source_theorem_closed"] is False
    assert decision["full_true_SM_equivalence_closed"] is False
    assert decision["full_no_knob_closed"] is False

    assert q79_import["closed_branch_status"] == "CLOSED_EXACT_CENTRAL_CIRCLE_BRANCH"
    assert q79_import["q_mod_448"] == 79
    assert q79_import["q64"] == 15
    assert q79_import["q7"] == 2
    assert q79_import["no_empirical_label_scan"] is True
    assert q79_import["observed_CKM_used_as_selector"] is False
    assert q79_import["selected_CKM_CP_phase_contact_imported"] is True
    assert q79_import["full_CKM_orientation_values_derived"] is False

    assert postcheck["postcheck_only"] is True
    assert postcheck["CKM_angles_used_as_source_selector"] is False
    assert postcheck["CKM_angle_magnitudes_derived"] is False
    assert postcheck["phase_residual_deg"] < 3.0
    assert postcheck["jarlskog_relative_residual"] < 0.03

    assert heavy_link["leading_noncommutation_closed"] is True
    assert heavy_link["heavy_link_calculator_ready"] is True
    assert heavy_link["selected_packet_values_open"] is True
    assert len(heavy_link["required_packet_entries"]) == 8
    assert heavy_link["maps_to_current_higher_breakdown_hunch"] is True

    assert boundary["q79_phase_contact"] is True
    assert boundary["selected_full_sm_attempt_status"] == "SELECTED_FULL_SM_DATA_THEOREM_NOT_PROVED_SELECTED_DATA_ABSENT"
    assert "execution_ii_yukawa_matrices" in boundary["rejected_proxy_inputs_found"]

    assert next_packet["next_required_artifact"] == NEXT
    assert "selected t_u13,t_u23,t_d13,t_d23 heavy-link entries" in next_packet[
        "remaining_to_close"
    ]
    assert "q79 finite CP phase imported from closed exact/charge branch" in next_packet["closed_now"]

    assert cert["status"] == STATUS
    assert cert["selected_q79_branch_imported"] is True
    assert cert["selected_CKM_CP_phase_contact_imported"] is True
    assert cert["q_mod_448"] == 79
    assert cert["no_empirical_label_scan"] is True
    assert cert["CKM_heavy_link_calculator_ready"] is True
    assert cert["selected_heavy_link_values_emitted"] is False
    assert cert["CKM_angles_derived"] is False
    assert cert["full_true_SM_equivalence_closed"] is False
    assert cert["observed_data_used_as_selector"] is False
    assert cert["target_fitting_used"] is False
    assert NEXT in note
    assert "CKMQ79PhaseBridgeImportAndHeavyLinkTargetTheorem" in note
    print("q79 CKM phase bridge import / heavy-link orientation target audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
