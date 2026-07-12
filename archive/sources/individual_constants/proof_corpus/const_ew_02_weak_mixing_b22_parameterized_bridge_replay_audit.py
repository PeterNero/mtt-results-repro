"""Audit CONST-EW-02 B22 parameterized bridge replay."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b22_parameterized_bridge_replay"
DATA = ROOT / "candidate_data"
BASE = DATA / SLUG
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    candidate = load(DATA / f"{SLUG}.candidate.json")
    replay = load(BASE / "symbolic_weak_angle_replay.packet.json")
    strict = load(BASE / "strict_source_promotion_gate.packet.json")
    param = load(BASE / "universal_parameter_pressure_test.packet.json")
    boundary = load(BASE / "weak_mixing_b22_boundary.packet.json")
    next_work = load(BASE / "next_labeled_workorder.packet.json")
    cert = load(CERT)

    for name, packet in [
        ("candidate", candidate),
        ("replay", replay),
        ("strict", strict),
        ("param", param),
        ("boundary", boundary),
        ("cert", cert),
    ]:
        require(packet["observed_data_used_as_selector"] is False, f"{name} used observed selector")
        require(packet["target_fitting_used"] is False, f"{name} used target fitting")
        require(packet["closure_claimed"] is False, f"{name} claimed closure")

    require(candidate["theorem"]["proved"] is True, "B22 theorem did not prove")
    require(candidate["symbolic_replay_built"] is True, "symbolic replay not built")
    require(candidate["active_bridge_parameters_in_weak_angle"] == ["u_dyn"], "wrong active weak bridge parameter")
    require(candidate["reserved_bridge_parameters"] == ["u_phys"], "wrong reserved bridge parameter")
    require(candidate["strict_no_knob_closed"] is False, "strict no-knob overclosed")
    require(candidate["physical_weak_angle_closure"] is False, "physical weak angle overclosed")

    general = replay["general_one_loop_formula"]
    require(general["formula"] == "sin2 = 3*(1+u2)/(3*(1+u2)+5*(1/r12+u1))", "general formula changed")
    require(abs(general["r12"] - 0.56027) < 1e-15, "r12 changed")

    lane = replay["no_threshold_bridge_lane"]
    require(lane["matches_B10_y_unit"] is True, "u_dyn bridge does not match B10 y")
    require(lane["matches_B11_conditional_sin2"] is True, "u_dyn=1 does not recover B11")
    require(abs(lane["y_unit_when_u_dyn_1"] - 0.019852738294064105) < 1e-15, "y unit drifted")
    require(abs(lane["u_dyn_0_high_scale_sin2"] - 0.2515877565744274) < 1e-15, "u_dyn=0 high-scale drifted")
    require(abs(lane["u_dyn_1_conditional_sin2"] - 0.2315309482915084) < 1e-15, "u_dyn=1 conditional drifted")
    require(replay["u_phys_lane"]["used_in_this_replay"] is False, "u_phys used in weak replay")
    require(replay["guardrails"]["observed_weak_angle_used"] is False, "observed weak angle used")
    require(replay["guardrails"]["parameter_values_fitted"] is False, "parameters fitted")
    require(replay["guardrails"]["no_knob_claimed"] is False, "no-knob claimed")

    require(strict["strict_no_knob_closed"] is False, "strict gate overclosed")
    require(strict["selected_source_promoted"] is False, "source promotion overclaimed")
    require("selected same-source dynamic transfer identity" in strict["required_to_retire_u_dyn"], "u_dyn retirement missing dynamic identity")
    require("central-circle rod/clock physical unit theorem" in strict["required_to_retire_u_phys"], "u_phys retirement missing metrology route")

    require(param["parameter_count"]["declared"] == 2, "declared parameter count changed")
    require(param["parameter_count"]["active_in_weak_angle_replay"] == 1, "weak active parameter count changed")
    require(param["parameter_count"]["reserved_for_alpha_physical_anchor"] == 1, "reserved parameter count changed")
    require(param["credibility_tests"]["global_not_sector_specific"] is True, "sector tuning allowed")
    require(param["credibility_tests"]["not_chosen_from_observed_targets"] is True, "observed target choice allowed")
    require(param["credibility_tests"]["must_feed_multiple_constants_or_retire"] is True, "retirement rule missing")
    require(param["credibility_tests"]["parameterized_result_labeled_nonfinal"] is True, "parameter result not labeled nonfinal")

    require(boundary["closed_now"]["symbolic_general_u1u2_replay_built"] is True, "general replay not closed")
    require(boundary["closed_now"]["symbolic_no_threshold_u_dyn_replay_built"] is True, "u_dyn replay not closed")
    require(boundary["closed_now"]["u_dyn_1_recovers_B11_conditional_bridge"] is True, "B11 recovery not closed")
    require(boundary["closed_now"]["u_phys_reserved_not_used_for_weak_angle"] is True, "u_phys reservation not closed")
    require(boundary["still_open"]["u_dyn_source_derivation"] is True, "u_dyn derivation not open")
    require(boundary["still_open"]["u_phys_source_derivation"] is True, "u_phys derivation not open")
    require(boundary["still_open"]["physical_weak_angle_closure"] is True, "weak angle not open")
    require(boundary["still_open"]["strict_no_knob_closure"] is True, "strict no-knob not open")

    require(next_work["active_label"] == "CONST-EW-02 / WEAK-MIXING / B23-RETIRE-U-DYN-OR-BRIDGE-AUDIT", "wrong B23 label")
    require("U-DYN-SOURCE-DERIVATION" in next_work["primary"]["label"], "primary B23 route wrong")
    require("BRIDGE-AUDIT-NO-BACKFIT" in next_work["bridge"]["label"], "bridge B23 route wrong")

    require(cert["symbolic_replay_built"] is True, "certificate replay missing")
    require(cert["u_dyn_1_recovers_B11_conditional_bridge"] is True, "certificate B11 recovery missing")
    require(cert["active_bridge_parameter_count_for_weak_angle"] == 1, "certificate active parameter count wrong")
    require(cert["total_provisional_parameter_count"] == 2, "certificate total parameter count wrong")
    require(cert["strict_no_knob_closed"] is False, "certificate strict no-knob overclosed")

    print("CONST-EW-02 B22 parameterized bridge replay audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
