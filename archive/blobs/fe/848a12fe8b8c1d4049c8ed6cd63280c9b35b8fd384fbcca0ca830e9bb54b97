"""Audit physical dotD_alpha1 / End0-to-sector routing attempt."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "candidate_data" / "selected_physical_dotd_alpha1_or_end0_sector_routing.candidate.json"
CERT = ROOT / "certificates" / "selected_physical_dotd_alpha1_or_end0_sector_routing_certificate.json"
PROOF = ROOT / "proof_corpus" / "MTT_Selected_Physical_dotD_alpha1_or_End0_to_Sector_Routing_v1.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    proof = PROOF.read_text(encoding="utf-8")

    require(
        data["status"] == "MTT_SELECTED_EXT_SCALE_DOTD_TANGENT_CLOSED_PHYSICAL_ALPHA1_ROUTING_OPEN",
        "unexpected status",
    )
    require(data["closure_claimed"] is False, "must not claim full closure")
    require(data["target_fitting_used"] is False, "must not use target fitting")
    path_a = data["path_A_straight_selected_Ext_density_scale_tangent"]
    require(path_a["closed"] is True, "Ext-density tangent should close")
    require(path_a["residual_l2"] < 1e-12, "linearized tangent residual too large")
    require(path_a["h_mean_abs"] < 1e-14, "tangent must be zero mean")
    require(path_a["h_l2"] > 0, "tangent should be nontrivial")
    require(path_a["promotion_to_physical_alpha1"] is False, "must not promote tangent to alpha1")
    require("discrete Chern" in path_a["why_not_physical_alpha1"], "alpha1 guardrail missing")
    for label in ["x1", "y1", "x2", "y2"]:
        require(path_a["dotD_direction_summaries"][label]["l2"] > 0, f"{label} dotD tangent should be nonzero")
    path_b = data["path_B_physical_alpha1_or_sector_routing"]
    require(path_b["physical_dotD_alpha1_closed"] is False, "physical alpha1 must remain open")
    require(path_b["sector_routing_closed"] is False, "sector routing must remain open")
    require(path_b["alpha1_discrete_support_from_visible_AH"] is True, "alpha1 support should be imported")
    require(path_b["constants_repo_alpha1_tangent_still_open"] is True, "constants repo should keep alpha1 tangent open")
    require(path_b["q79_sector_charge_and_transfer_still_open"] is True, "q79 sector transfer should remain open")
    boundary = data["operator_payload_boundary"]
    require(boundary["selected_Ext_density_scale_dotD_tangent_extracted"] is True, "selected tangent missing")
    require(boundary["physical_dotD_alpha1_payload_extracted"] is False, "physical dotD must remain open")
    require(boundary["selected_End0_to_sector_routing_values_extracted"] is False, "sector routing must remain open")
    require(boundary["validator_ready"] is False, "must not be validator ready")
    require(cert["selected_Ext_density_scale_tangent_closed"] is True, "certificate should close tangent")
    require(cert["physical_dotD_alpha1_payload_extracted"] is False, "certificate must keep physical dotD open")
    require("not yet physical `dotD_alpha1`" in proof, "proof must state physical alpha1 guardrail")

    print("PASS selected physical dotD alpha1 or End0 sector routing audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
