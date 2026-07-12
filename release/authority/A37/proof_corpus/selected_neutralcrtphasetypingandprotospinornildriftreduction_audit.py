from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutralcrtphasetypingandprotospinornildriftreduction"
STATUS = "MTT_SELECTED_NEUTRAL_CRT_PHASE_TYPING_CLOSED_Q7_OVER_448_CLUE_RETIRED_NIL_DRIFT_SCALE_OPEN"
NEXT = "MTT_Selected_NeutralNilHolonomySourceAndAbsoluteScale_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    packet = load(ROOT / "candidate_data" / SLUG / "neutral_crt_phase_typing_and_nil_drift.packet.json")
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_NeutralCRTPhaseTypingAndProtoSpinorNilDriftReduction_v1.md").read_text(encoding="utf-8")

    require(packet == candidate, "candidate/packet mismatch")
    require(packet["status"] == cert["status"] == STATUS, "status changed")
    require(packet["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next changed")
    require(packet["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem failed")
    crt = packet["CRT_character_typing"]
    require(crt["q7_only_lift_mod448"] == 128, "q7 lift changed")
    require(crt["q64_only_lift_mod448"] == 399, "q64 lift changed")
    require(crt["lift_sum_mod448"] == 79, "CRT recombination failed")
    require(crt["mistyped_fraction_is_selected_character"] is False, "2/448 overpromoted")
    require(packet["supersession_decision"]["A32_q7_over_qmod_close_clue_retired"] is True, "mistyped clue not retired")
    require(packet["supersession_decision"]["A29_second_order_orbit_algebra_retracted"] is False, "valid algebra retracted")
    require(packet["supersession_decision"]["A31_excludes_proto_spinor_nil_drift_family"] is False, "A31 scope overextended")
    shape = packet["proto_spinor_neutral_shape"]
    require(shape["structural_formula_available"] is True, "nil drift formula missing")
    require(shape["phi_nu_selected_by_current_finite_character_packet"] is False, "phi overselected")
    require(shape["mu_nu_selected"] is False, "scale overselected")
    require(packet["reduced_physical_cutset"]["count"] == 2, "cutset count changed")
    closes = packet["what_closes_here"]
    for key in ["CRT_phase_typing", "q7_over_448_near_hit_retired", "proto_spinor_nil_drift_formula_imported", "physical_cutset_specialized_to_phi_and_scale"]:
        require(closes[key] is True, f"not closed: {key}")
    for key in ["neutral_nil_holonomy_selected", "absolute_neutral_scale_selected", "dimensionful_neutral_masses"]:
        require(closes[key] is False, f"overclosed: {key}")
    require(packet["new_physical_value_fields_closed_here"] == 0, "physical value overclaim")
    require(packet["observed_data_used_as_selector"] is False and packet["target_fitting_used"] is False, "empirical selector used")
    for phrase in ["128 mod 448", "not `2/448`", "near-hit is retired", "phi_nu", NEXT]:
        require(phrase in note, f"note missing: {phrase}")

    print(json.dumps({"q7_lift": cert["q7_only_CRT_lift"], "q64_lift": cert["q64_only_CRT_lift"], "global_q": cert["global_q"], "coordinates": cert["remaining_continuous_coordinate_count"], "next": NEXT}, indent=2))
    print("neutral CRT phase-typing/nil-drift audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
