"""Audit CONST-EW-02 B10 loop-volume profile candidate."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b10_loop_volume_profile_candidate"
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
    candidates = load(BASE / "source_y_candidates.packet.json")
    bridge = load(BASE / "loop_volume_bridge_requirement.packet.json")
    boundary = load(BASE / "weak_mixing_b10_boundary.packet.json")
    cert = load(CERT)

    for name, packet in [
        ("candidate", candidate),
        ("candidates", candidates),
        ("bridge", bridge),
        ("boundary", boundary),
        ("cert", cert),
    ]:
        require(packet["observed_data_used_as_selector"] is False, f"{name} used observed selector")
        require(packet["target_fitting_used"] is False, f"{name} used target fitting")
        require(packet["closure_claimed"] is False, f"{name} claimed closure")

    require(candidate["theorem"]["proved"] is True, "B10 candidate theorem did not prove")
    require(boundary["closed_now"]["best_loop_volume_candidate_identified"] is True, "best candidate not identified")
    require(boundary["still_open"]["SelectedEWLoopVolumeProfileBridge"] is True, "bridge lemma incorrectly closed")
    require(cert["bridge_lemma_proved"] is False, "certificate overclaims bridge lemma")
    require(cert["source_selected_y_promoted"] is False, "certificate promoted y")
    require(cert["physical_weak_angle_closure_claimed"] is False, "certificate overclaims weak-angle closure")

    best = candidates["best_structural_candidate"]
    require(best["name"] == "inv_sqrt_tau_int", "unexpected best source candidate")
    expected_y = math.sqrt(15.0 / math.log(448.0)) / (8.0 * math.pi * math.pi)
    require(math.isclose(best["y_candidate"], expected_y, rel_tol=0.0, abs_tol=1e-15), "best y expression mismatch")
    require(best["promoted"] is False, "best source candidate promoted without bridge")
    require("x*log(mu_Theta/MZ)" in bridge["required_lemma"]["statement"], "bridge statement missing x*L requirement")
    require(
        "select inv_sqrt_tau because it matches a measured weak angle" in load(BASE / "next_labeled_workorder.packet.json")["forbidden_shortcuts"],
        "missing forbidden near-hit selection shortcut",
    )

    print("CONST-EW-02 B10 loop-volume profile candidate audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
