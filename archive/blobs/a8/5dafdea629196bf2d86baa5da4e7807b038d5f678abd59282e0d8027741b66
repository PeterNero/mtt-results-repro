from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "physical_scale_lifting_anchor_gate_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    require(
        cert["status"] == "INTERNAL_SCALE_LIFT_IMPORTED_PHYSICAL_DIMENSIONAL_ANCHOR_STILL_OPEN",
        "unexpected status",
    )
    closed = cert["closed_tests"]
    open_tests = cert["open_tests"]
    guards = cert["guardrails"]
    imported = cert["imported_internal_scale_lift"]

    require(closed["internal_rho_uv_branch_closed"] is True, "internal rho_UV should be closed")
    require(closed["selected_character_channel_covariance_closed"] is True, "character covariance should close")
    require(closed["selected_horizontal_scale_law_closed"] is True, "horizontal scale law should close")
    require(imported["rho_UV"] > 0, "rho_UV should be positive")
    require(imported["R_star"] > 0, "R_star should be positive")
    require(imported["s_star_from_rho"] > 0, "s_star should be positive")
    require(open_tests["physical_absolute_dimensionful_anchor_closed"] is False, "physical anchor should remain open")
    require(open_tests["physical_scale_lift_closed"] is False, "physical scale lift should remain open")
    require(guards["claims_internal_scale_lift_closed"] is True, "internal scale lift should be claimed")
    require(guards["claims_physical_Newton_prediction"] is False, "must not claim Newton prediction")
    require(guards["claims_dimensionful_anchor_closed"] is False, "must not claim dimensionful anchor")
    require(guards["forbids_observed_GN_backsolve"] is True, "GN backsolve must be forbidden")

    print("AUDIT_PASS: internal scale lift imported; physical dimensional anchor remains open")


if __name__ == "__main__":
    main()
