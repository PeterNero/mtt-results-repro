"""Audit CONST-EW-02 B14 scale-law/covariance import."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b14_scalelaw_projection_or_phi_ew_import"
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
    h2 = load(BASE / "selected_h2_scalelaw_import.packet.json")
    cov = load(BASE / "selected_covariance_phi_ew_import.packet.json")
    gap = load(BASE / "projection_gap_after_import.packet.json")
    boundary = load(BASE / "weak_mixing_b14_boundary.packet.json")
    cert = load(CERT)

    for name, packet in [
        ("candidate", candidate),
        ("h2", h2),
        ("cov", cov),
        ("gap", gap),
        ("boundary", boundary),
        ("cert", cert),
    ]:
        require(packet["observed_data_used_as_selector"] is False, f"{name} used observed selector")
        require(packet["target_fitting_used"] is False, f"{name} used target fitting")
        require(packet["closure_claimed"] is False, f"{name} claimed closure")

    require(candidate["theorem"]["proved"] is True, "B14 theorem did not prove")
    require(candidate["strict_xL_emitted_now"] is False, "xL incorrectly emitted")
    require(cert["strict_xL_emitted_now"] is False, "certificate overclaims xL")
    require(cert["electroweak_projection_selected"] is False, "EW projection incorrectly selected")
    require(cert["Phi_EW_product_map_selected"] is False, "Phi_EW product map incorrectly selected")

    imported = h2["imported_selection"]
    require(imported["scale_law"] == "H2", "H2 not imported")
    require(imported["selected_horizontal_scale_law_closed"] is True, "horizontal scale law not closed")
    require(math.isclose(float(imported["R_star"]), float(cert["R_star"]), rel_tol=0.0, abs_tol=1e-12), "R_star mismatch")
    require(h2["electroweak_projection_selected"] is False, "H2 projected to EW too early")
    require(h2["emits_xL"] is False, "H2 import emitted xL")

    imported_cov = cov["imported_covariance"]
    require(imported_cov["selected_character"] == "q_64=15", "wrong selected character")
    require(imported_cov["selected_channel"] == "E_15 K_64", "wrong selected channel")
    require(imported_cov["G_11"] == 1.0, "G_11 should be 1")
    require(imported_cov["D_raw_norm_squared_d_Q"] == 1.0, "d_Q should be 1")
    require(cov["phi_ew_product_map_selected"] is False, "Phi_EW map selected too early")
    require(cov["emits_xL"] is False, "covariance import emitted xL")
    require("projection map Phi_EW(rho_UV, branch data)->xL" in cov["what_it_does_not_remove"], "missing Phi_EW blocker")

    require(gap["now_source_verified"]["selected_horizontal_scale_law_H2"] is True, "H2 source verification missing")
    require(gap["now_source_verified"]["selected_G_11"] is True, "G11 source verification missing")
    require(gap["now_source_verified"]["selected_D_raw_norm_squared_d_Q"] is True, "d_Q source verification missing")
    require(gap["not_source_verified"]["H2_to_electroweak_log_projection"] is True, "H2->EW gap not preserved")
    require(gap["not_source_verified"]["Phi_EW_to_xL_product_map"] is True, "Phi_EW gap not preserved")

    require(boundary["closed_now"]["selected_H2_scale_law"] is True, "H2 not closed in boundary")
    require(boundary["closed_now"]["selected_G11_and_Draw_covariance"] is True, "covariance not closed in boundary")
    require(boundary["still_open"]["actual_xL_source_emission"] is True, "xL not left open")
    require(boundary["still_open"]["physical_weak_angle_closure"] is True, "weak-angle closure not left open")

    print("CONST-EW-02 B14 scale-law/covariance import audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
