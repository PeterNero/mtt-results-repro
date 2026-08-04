"""Audit CONST-EW-02 B12 profile-product source contract."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b12_profile_product_source_contract"
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
    routes = load(BASE / "profile_product_route_matrix.packet.json")
    contract = load(BASE / "source_emission_contract.packet.json")
    support = load(BASE / "internal_x_equals_one_support_lane.packet.json")
    boundary = load(BASE / "weak_mixing_b12_boundary.packet.json")
    cert = load(CERT)

    for name, packet in [
        ("candidate", candidate),
        ("routes", routes),
        ("contract", contract),
        ("support", support),
        ("boundary", boundary),
        ("cert", cert),
    ]:
        require(packet["observed_data_used_as_selector"] is False, f"{name} used observed selector")
        require(packet["target_fitting_used"] is False, f"{name} used target fitting")
        require(packet["closure_claimed"] is False, f"{name} claimed physical closure")

    require(candidate["theorem"]["proved"] is True, "B12 theorem did not prove")
    require(candidate["strict_xL_emitted_now"] is False, "xL incorrectly emitted")
    require(candidate["contract_ready"] is True, "source contract not ready")
    require(cert["strict_xL_emitted_now"] is False, "certificate overclaims xL emission")
    require(cert["source_contract_ready"] is True, "certificate misses contract readiness")
    require(cert["physical_weak_angle_closure_claimed"] is False, "certificate overclaims weak-angle closure")

    require(routes["route_verdict"]["strict_no_knob_xL_emitted_now"] is False, "route matrix overclaims xL")
    require(routes["route_verdict"]["best_next_route"] == "R3_HETEROTIC_STROMINGER_THRESHOLD_KERNEL", "wrong best strict route")
    require(routes["route_verdict"]["secondary_route"] == "R4_RHO_UV_RESPONSE_BRIDGE", "wrong secondary route")
    require(
        all(row["current_source_emits_xL"] is False for row in routes["routes"]),
        "a route emitted xL without source theorem",
    )
    require(boundary["still_open"]["actual_xL_source_emission"] is True, "xL source emission not left open")
    require(boundary["still_open"]["Phi_EW_rhoUV_response_map"] is True, "Phi_EW not left open")

    require(support["promoted"] is False, "internal x=1 support promoted physically")
    require(support["internal_kernel_support"]["K_gauge_int"] == "1", "missing internal K gauge support")
    expected_ratio = math.exp(math.sqrt(15.0 / math.log(448.0)))
    require(
        math.isclose(support["if_internal_x_int_equals_1"]["required_scale_ratio"], expected_ratio, rel_tol=0.0, abs_tol=1e-12),
        "internal support scale ratio mismatch",
    )
    require(
        "rho_UV may enter only through Phi_EW theorem" in contract["minimal_acceptance_contract"]["required_guardrails"],
        "missing rho_UV guardrail",
    )

    print("CONST-EW-02 B12 profile-product source contract audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
