"""Audit CONST-EW-02 B9 profile reduction and universal-parameter gate."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b9_profile_reduction_and_universal_parameter_gate"
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
    profile = load(BASE / "one_loop_profile_reduction.packet.json")
    imports = load(BASE / "superset_imports_critical.packet.json")
    primitive = load(BASE / "one_universal_parameter_gate.packet.json")
    boundary = load(BASE / "weak_mixing_b9_boundary.packet.json")
    cert = load(CERT)

    for name, packet in [
        ("candidate", candidate),
        ("profile", profile),
        ("imports", imports),
        ("primitive", primitive),
        ("boundary", boundary),
        ("cert", cert),
    ]:
        require(packet["observed_data_used_as_selector"] is False, f"{name} used observed selector")
        require(packet["target_fitting_used"] is False, f"{name} used target fitting")
        require(packet["closure_claimed"] is False, f"{name} claimed closure")

    require(candidate["theorem"]["proved"] is True, "B9 reduction theorem did not prove")
    require(profile["reduction"]["high_scale_check"]["matches_B5_value"] is True, "high-scale replay mismatch")
    require(boundary["closed_now"]["one_loop_formula_reduced_to_u1_u2"] is True, "u1/u2 reduction not closed")
    require(boundary["closed_now"]["no_threshold_lane_reduced_to_single_y"] is True, "single-y lane not closed")
    require(boundary["still_open"]["source_selected_u1_u2_or_y"] is True, "source-selected profile incorrectly closed")
    require(boundary["still_open"]["strict_no_knob_low_scale_weak_angle"] is True, "strict weak angle incorrectly closed")
    require(cert["strict_no_knob_physical_weak_angle_closed"] is False, "certificate overclaims strict closure")
    require(cert["one_universal_parameter_selected"] is False, "universal parameter selected without source")

    lane = profile["reduction"]["no_threshold_one_profile_lane"]
    require(lane["derivative_at_y0"] < 0.0, "expected one-loop y profile to move weak angle downward at y=0")
    require(math.isclose(lane["samples_not_targets"]["y=0"], cert["high_scale_tree_sin2"], rel_tol=0.0, abs_tol=1e-15), "sample y=0 mismatch")
    require(
        primitive["weak_mixing_role"]["one_universal_parameter_extension"]["closed_now"] is False,
        "universal extension closed without primitive",
    )
    require(
        imports["imports"]["sm_parity_t1t2_covariant_green"]["usable_now"] is True,
        "T1/T2 Green support not imported",
    )
    require(
        "numeric weak-angle profile" in imports["imports"]["sm_parity_t1t2_covariant_green"]["what_it_does_not_give"],
        "T1/T2 import must not be promoted as numeric weak-angle profile",
    )

    print("CONST-EW-02 B9 profile reduction and universal-parameter gate audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
