from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutralcompositespectralattenuationreduction_or_branchbridgetheorem"
STATUS = "MTT_SELECTED_NEUTRAL_ATTENUATION_COMPRESSED_TO_COMPOSITE_SPECTRUM_BRANCH_BRIDGE_OPEN"
NEXT = "MTT_Selected_NeutralNative10D_or_MTheoryLiftOperatorSelectionAndBranchBridge_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    packet = load(ROOT / "candidate_data" / SLUG / "neutral_composite_spectral_attenuation.packet.json")
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_NeutralCompositeSpectralAttenuationReduction_or_BranchBridgeTheorem_v1.md").read_text(encoding="utf-8")

    require(packet == candidate, "packet/candidate mismatch")
    require(packet["status"] == cert["status"] == STATUS, "status changed")
    require(packet["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next changed")
    require(packet["theorem"]["proved"] is True and cert["theorem_proved"] is True, "reduction theorem failed")
    require(cert["composite_eigenvalue_exact"] == "661/4", "composite eigenvalue changed")
    require(cert["attenuation_compression_identity_closed"] is True, "attenuation identity open")
    require(cert["profile_normalization_identity_closed"] is True, "profile identity open")
    for key in [
        "elevenfold_multiplicity_selected",
        "neutral_operator_selected_on_11D_lift",
        "nil_quarter_saturation_selected",
        "same_operator_branch_bridge_closed",
        "selected_action_normalization_closed",
        "strict_source_promotion_closed",
    ]:
        require(cert[key] is False, f"source premise overclosed: {key}")
    require(packet["source_no_go"]["candidate_numerically_refuted"] is False, "candidate incorrectly rejected")
    require(packet["source_no_go"]["candidate_structurally_sharpened"] is True, "candidate not sharpened")
    require(packet["conditional_closing_operator"]["operator_selected_by_MTT"] is False, "conditional operator overpromoted")
    require(packet["conditional_closing_operator"]["physical_neutral_operator_lifted_to_11D"] is False, "neutral 11D lift overclosed")
    require(packet["conditional_closing_operator"]["dimension_census_closed_from_corpus"] is True, "recursive 11D census missing")
    require(packet["native_10D_counterfactual"]["native_10D_matches_neutral_profile"] is False, "native 10D incorrectly accepted")
    require(packet["native_10D_counterfactual"]["ratio_to_A40_A_nu"] > 1e5, "native 10D mismatch guard changed")
    require(packet["epistemic_policy"]["new_target_fit_performed"] is False, "new target fit introduced")
    for phrase in ["selected neutral eigenvalue `661/4`", "native MTT stops", "conditional M-theory lift", "No current theorem places", "forbids combining them", "one shared", NEXT]:
        require(phrase in note, f"note missing: {phrase}")

    print(json.dumps(cert, indent=2, sort_keys=True))
    print("neutral composite spectral attenuation audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
