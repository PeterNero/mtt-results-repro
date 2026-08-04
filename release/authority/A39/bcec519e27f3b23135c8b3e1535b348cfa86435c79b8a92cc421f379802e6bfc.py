from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutralfiniteheisenbergdeterminantnogoandsmoothlifttarget"
STATUS = "MTT_SELECTED_NEUTRAL_FINITE_HEISENBERG_DETERMINANT_NOGO_CLOSED_SMOOTH_U1_LIFT_AND_SCALE_OPEN"
NEXT = "MTT_Selected_NeutralSmoothDeterminantLineHolonomyAndAnchoredScale_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    packet = load(ROOT / "candidate_data" / SLUG / "neutral_finite_heisenberg_determinant_nogo.packet.json")
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_NeutralFiniteHeisenbergDeterminantNoGoAndSmoothLiftTarget_v1.md").read_text(encoding="utf-8")

    require(packet == candidate, "candidate/packet mismatch")
    require(packet["status"] == cert["status"] == STATUS, "status changed")
    require(packet["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next changed")
    require(packet["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem failed")
    proof = packet["finite_Heisenberg_determinant_proof"]
    require(proof["element_count"] == 27, "group count changed")
    require(proof["max_abs_det_minus_one"] < 1e-11, "determinant residual")
    require(proof["image_subgroup"] == "SU(3)" and proof["determinant_character"] == "trivial", "image typing failed")
    consequence = packet["neutral_phase_consequence"]
    require(consequence["all_have_exact_twofold_degeneracy"] is True, "finite phases split orbit")
    require(consequence["can_source_small_nonzero_continuous_nil_drift"] is False, "finite phase overpromoted")
    guard = packet["scope_guard"]
    require(guard["finite_rhoE_promotion_retracted"] is False and guard["finite_projective_gauge_class_closed"] is True, "valid rhoE result lost")
    closes = packet["what_closes_here"]
    for key in ["finite_operator_level_rhoE_imported", "finite_Heisenberg_determinant_triviality", "finite_qutrit_source_for_continuous_phi_nu_rejected", "smooth_determinant_line_target_typed"]:
        require(closes[key] is True, f"not closed: {key}")
    for key in ["phi_nu_value", "mu_nu_value", "dimensionful_neutral_masses"]:
        require(closes[key] is False, f"overclosed: {key}")
    require(packet["observed_data_used_as_selector"] is False and packet["target_fitting_used"] is False, "empirical selector used")
    for phrase in ["All 27 elements", "lies", "SU(3)", "cannot emit", "smooth", NEXT]:
        require(phrase in note, f"note missing: {phrase}")

    print(json.dumps({"elements": cert["finite_group_elements_checked"], "max_det_residual": cert["max_determinant_residual"], "finite_image_SU3": cert["finite_image_in_SU3"], "next": NEXT}, indent=2))
    print("neutral finite-Heisenberg determinant no-go audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
