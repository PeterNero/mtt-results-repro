"""Audit CONST-EW-02 B11 loop-volume bridge proof attempt."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b11_loop_volume_bridge_proof_attempt"
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
    proof_attempt = load(BASE / "selected_loop_volume_bridge_proof_attempt.packet.json")
    underdet = load(BASE / "current_source_underdetermination.packet.json")
    conditional = load(BASE / "conditional_one_primitive_bridge.packet.json")
    boundary = load(BASE / "weak_mixing_b11_boundary.packet.json")
    cert = load(CERT)

    for name, packet in [
        ("candidate", candidate),
        ("proof_attempt", proof_attempt),
        ("underdet", underdet),
        ("conditional", conditional),
        ("boundary", boundary),
        ("cert", cert),
    ]:
        require(packet["observed_data_used_as_selector"] is False, f"{name} used observed selector")
        require(packet["target_fitting_used"] is False, f"{name} used target fitting")
        require(packet["closure_claimed"] is False, f"{name} claimed physical closure")

    require(candidate["theorem"]["proved"] is True, "B11 theorem statement did not prove")
    require(candidate["strict_bridge_proved"] is False, "strict bridge incorrectly proved")
    require(candidate["conditional_bridge_proved"] is True, "conditional bridge not proved")
    require(cert["strict_bridge_proved"] is False, "certificate overclaims strict bridge")
    require(cert["conditional_bridge_proved"] is True, "certificate missed conditional bridge")
    require(cert["current_source_underdetermination_proved"] is True, "underdetermination not certified")

    require(proof_attempt["right_hand_side_source"]["emitted"] is True, "RHS metrology invariant not sourced")
    require(proof_attempt["left_hand_side_source"]["product_xL_selected"] is False, "xL product incorrectly selected")
    require(underdet["lemma"]["proved"] is True, "underdetermination lemma not proved")
    require(boundary["still_open"]["strict_SelectedEWLoopVolumeProfileBridge"] is True, "strict bridge not left open")
    require(boundary["still_open"]["source_emitted_xL_product"] is True, "xL product not left open")
    require(conditional["conditional_theorem"]["proved"] is True, "conditional theorem not proved")
    require(conditional["primitive_selected_now"] is False, "primitive selected without source")
    require(conditional["not_no_knob"] is True, "primitive lane must be marked not no-knob")

    expected_y = math.sqrt(15.0 / math.log(448.0)) / (8.0 * math.pi * math.pi)
    require(math.isclose(cert["y_if_condition_met"], expected_y, rel_tol=0.0, abs_tol=1e-15), "conditional y mismatch")
    require(cert["x_required_if_5TeV_scaffold_used"] > 0.0, "diagnostic x must be positive")
    require(
        "Choose P_univ from the weak angle." in conditional["forbidden_future_use"],
        "missing weak-angle primitive backsolve guardrail",
    )

    print("CONST-EW-02 B11 loop-volume bridge proof attempt audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
