from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_hym_alpha1_frontier_synthesis_certificate.json"
STATUS = "POST_ALPHA_HYM_ALPHA1_FRONTIER_SYNTHESIZED_PRIMITIVE_C1_FULLRESPONSE_OPEN"
NEXT = "Selected_U1Y_RouteC_Primitive_C1_or_FullResponse_SelectedEmission_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(cert["theorem"]["proved"] is True, "frontier synthesis theorem should be proved")
    require(all(cert["closed_support"].values()), "closed support should pass")
    require(all(cert["no_longer_primary_blockers"].values()), "retired blockers should pass")
    require(all(cert["current_open"].values()), "current open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")

    decision = cert["frontier_decision"]
    require(decision["frontier_is_HYM_existence"] is False, "HYM existence should not be live frontier")
    require(decision["frontier_is_alpha1_driver"] is False, "alpha1 driver should not be live frontier")
    require(decision["frontier_is_raw_BN_or_rhoE_scaffold"] is False, "raw scaffold should not be live frontier")
    require(decision["frontier_is_primitive_C1_or_full_response_emission"] is True, "wrong frontier")
    require(decision["next_required_artifact"] == NEXT, "wrong next artifact")

    require(packet["current_open"]["selected_A_selected_emission"] is True, "A_selected boundary lost")
    require(packet["current_open"]["selected_b_selected_or_homogeneous_zero_theorem"] is True, "b_selected boundary lost")
    require(STATUS in note and NEXT in note and "alpha1 driver and honest dotD replay" in note, "note missing essentials")
    print("AUDIT_PASS: HYM/alpha1 frontier synthesized; primitive C1/full response remains open")


if __name__ == "__main__":
    main()
