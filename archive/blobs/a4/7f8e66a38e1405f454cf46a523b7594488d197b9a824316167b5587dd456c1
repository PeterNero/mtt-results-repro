"""Audit CONST-EW-02 B13 dual-route xL emission attempt."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b13_dual_route_xl_emission_attempt"
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
    heterotic = load(BASE / "heterotic_strominger_scale_route.packet.json")
    rho = load(BASE / "rho_uv_phi_ew_route.packet.json")
    synthesis = load(BASE / "dual_route_synthesis.packet.json")
    boundary = load(BASE / "weak_mixing_b13_boundary.packet.json")
    cert = load(CERT)

    for name, packet in [
        ("candidate", candidate),
        ("heterotic", heterotic),
        ("rho", rho),
        ("synthesis", synthesis),
        ("boundary", boundary),
        ("cert", cert),
    ]:
        require(packet["observed_data_used_as_selector"] is False, f"{name} used observed selector")
        require(packet["target_fitting_used"] is False, f"{name} used target fitting")
        require(packet["closure_claimed"] is False, f"{name} claimed closure")

    require(candidate["theorem"]["proved"] is True, "B13 theorem did not prove")
    require(candidate["strict_xL_emitted_now"] is False, "xL incorrectly emitted")
    require(cert["strict_xL_emitted_now"] is False, "certificate overclaims xL")
    require(cert["heterotic_route_refined"] is True, "heterotic route not refined")
    require(cert["rhoUV_route_refined"] is True, "rhoUV route not refined")

    rows = heterotic["diagnostic_scale_laws"]
    require(len(rows) == 3, "expected H1/H2/FP rows")
    require(all(row["emits_xL"] is False for row in rows), "scale-law row emitted xL")
    h2 = heterotic["best_support_candidate"]
    require(h2["name"].startswith("H2"), "H2 should be best support candidate")
    require(h2["x_required_to_hit_C"] > 0.0, "H2 required x must be positive")
    require("electroweak projection" in " ".join(heterotic["why_xL_not_emitted"]), "missing electroweak projection blocker")

    require(rho["emits_xL"] is False, "rho route emitted xL")
    require("selected response-row inner product G_11" in rho["missing_for_phi_ew"], "missing G11 blocker")
    require("xL = rho_UV" in rho["forbidden_direct_maps"], "missing direct rho guardrail")
    require(boundary["still_open"]["actual_xL_source_emission"] is True, "xL not left open")
    require(boundary["still_open"]["selected_horizontal_scale_law"] is True, "scale law not left open")
    require(boundary["still_open"]["Phi_EW_rhoUV_to_xL"] is True, "Phi_EW not left open")

    expected = math.sqrt(15.0 / math.log(448.0))
    require(math.isclose(cert["required_xL"], expected, rel_tol=0.0, abs_tol=1e-15), "required xL mismatch")
    require(synthesis["new_minimal_bridge"]["name"] == "SelectedHorizontalScaleLawAndEWProjectionBridge", "wrong next bridge")

    print("CONST-EW-02 B13 dual-route xL emission attempt audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
