from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutrallensdedekindtransgression_or_oneprimitiveprofile"
STATUS = "MTT_SELECTED_NEUTRAL_LENS_DEDEKIND_IDENTITY_CLOSED_PHASE_SOURCE_NORMALIZATION_OPEN_ONE_SCALE_PROFILE_READY"
NEXT = "MTT_Selected_NeutralAPSDeterminantLineIdentificationAndCountertermNormalization_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    packet = load(ROOT / "candidate_data" / SLUG / "neutral_lens_dedekind_transgression.packet.json")
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_NeutralLensDedekindTransgression_or_OnePrimitiveProfile_v1.md").read_text(encoding="utf-8")

    require(packet == candidate, "candidate/packet mismatch")
    require(packet["status"] == cert["status"] == STATUS, "status changed")
    require(packet["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next changed")
    require(packet["theorem"]["proved"] is True and cert["theorem_proved"] is True, "arithmetic theorem failed")
    residue = packet["selected_arithmetic"]["renormalized_mixed_residue"]
    require((residue["numerator"], residue["denominator"]) == (1, 240), "mixed residue changed")
    require(cert["candidate_phi_nu_exact"] == "pi/120", "phase candidate changed")
    require(abs(cert["pull_sigma_diagonal_approximation"]) < 0.1, "candidate no longer near oscillation profile")
    require(cert["conditional_continuous_neutral_mass_splitting_inputs"] == 1, "one-scale reduction changed")
    decision = packet["closure_decision"]
    require(decision["exact_Dedekind_reciprocity_identity_closed"] is True, "identity not closed")
    require(decision["conditional_two_to_one_neutral_scale_reduction_ready"] is True, "conditional reduction missing")
    for key in ["strict_determinant_line_phase_source_closed", "strict_absolute_scale_source_closed", "strict_neutral_no_knob_closed"]:
        require(decision[key] is False, f"overclosed: {key}")
    policy = packet["epistemic_policy"]
    require(policy["target_used_to_rank_this_hypothesis"] is True, "target-informed discovery hidden")
    require(policy["target_fitting_used"] is True and policy["pre_registered_prediction"] is False, "prediction mislabeled")
    require(packet["absolute_scale_boundary"]["imported_no_go"]["free_parameter_count_for_absolute_units"] == 1, "scale no-go changed")
    for phrase in ["exactly `1/240`", "not a pre-registered prediction", "one scale primitive", NEXT]:
        require(phrase in note, f"note missing: {phrase}")

    print(json.dumps({
        "residue": residue["text"],
        "phi": cert["candidate_phi_nu_exact"],
        "ratio": cert["candidate_ratio"],
        "pull_sigma": cert["pull_sigma_diagonal_approximation"],
        "conditional_mass_scale_inputs": 1,
        "strict_phase_source_closed": False,
        "strict_scale_source_closed": False,
        "next": NEXT,
    }, indent=2))
    print("neutral Lens/Dedekind transgression audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
