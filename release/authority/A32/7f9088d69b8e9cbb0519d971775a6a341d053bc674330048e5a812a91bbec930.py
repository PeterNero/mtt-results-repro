from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutralspectralactionslopeorseesawsource"
STATUS = "MTT_SELECTED_NEUTRAL_SPECTRAL_AND_SEESAW_CANDIDATES_EXECUTED_TRANSFER_FUNCTOR_OPEN"
NEXT = "MTT_Selected_NeutralCircleToMassCostTransferOrRealStructureFunctor_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    packet = load(ROOT / "candidate_data" / SLUG / "neutral_spectral_and_seesaw_source_discrimination.packet.json")
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_NeutralSpectralActionSlopeOrSeesawSource_v1.md").read_text(encoding="utf-8")

    require(packet == candidate, "candidate/packet mismatch")
    require(packet["status"] == cert["status"] == STATUS, "status changed")
    require(packet["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next changed")
    require(packet["theorem"]["proved"] is True and cert["theorem_proved"] is True, "discrimination theorem failed")
    require(packet["observed_data_used_as_selector"] is False and packet["target_fitting_used"] is False, "empirical selector used")
    require(abs(packet["spectral_action_route"]["tau_int"] - 0.40698621549433234) < 1e-15, "tau changed")
    require(abs(packet["spectral_action_route"]["canonical_ratio_trial"] - 0.22776779060058736) < 1e-15, "SPT trial changed")
    require(packet["spectral_action_route"]["selected_beta_emitted"] is False, "beta overpromoted")
    ratios = packet["circle_drift_route"]["candidate_ratios"]
    require(abs(ratios["q79_global_phase"] - ratios["q369_conjugate_phase"]) < 1e-15, "conjugate ratios differ")
    require(abs(ratios["q7_over_qmod_drift"] - 0.031881329631239144) < 1e-15, "q7 ratio changed")
    require(packet["circle_drift_route"]["exact_candidate_selected"] is False, "circle clue overpromoted")
    majorana = packet["majorana_seesaw_route"]
    require(majorana["admissible_self_characters"] == [0, 672], "Majorana character cut changed")
    require(majorana["q79_or_q369_reused_as_majorana_character"] is False, "CP character reused")
    require(majorana["selected_neutral_real_structure_emitted"] is False, "real structure overpromoted")
    closes = packet["what_closes_here"]
    for key in ["canonical_selected_tau_trial_executed", "selected_circle_phase_trials_executed", "CP_to_Majorana_character_shortcut_rejected", "remaining_transfer_functor_typed"]:
        require(closes[key] is True, f"not closed: {key}")
    for key in ["selected_spectral_action_slope_beta", "selected_neutral_real_structure", "Dirac_only_action_completeness", "selected_Majorana_seesaw_blocks", "physical_scale_selected"]:
        require(closes[key] is False, f"overclosed: {key}")
    require(packet["new_physical_value_fields_closed_here"] == 0, "physical values overclosed")
    require(packet["readiness_subfields_closed"] == 9 and packet["readiness_subfields_total"] == 14, "readiness changed")
    for phrase in ["tau_int=log(448)/15", "q7/qmod", "separately typed Majorana", "two typed morphisms", NEXT]:
        require(phrase in note, f"note missing: {phrase}")

    print(json.dumps({"tau_trial_ratio": cert["canonical_spt_ratio"], "closest_circle_ratio": ratios["q7_over_qmod_drift"], "closest_residual": cert["closest_circle_candidate_residual"], "physical_rows": 0, "next": NEXT}, indent=2))
    print("selected neutral spectral/seesaw discrimination audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
