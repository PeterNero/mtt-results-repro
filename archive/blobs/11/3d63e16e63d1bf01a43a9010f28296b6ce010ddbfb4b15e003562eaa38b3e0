from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_operator_source_identity_pic0_split_certificate.json"
STATUS = "POST_ALPHA_OPERATOR_SOURCE_IDENTITY_REDUCED_PHIFIN_OPEN"
NEXT = "Selected_U1Y_RouteC_FiniteEmissionMorphism_PhiFin_Subpacket_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(all(cert["checks"].values()), "all certificate checks should pass")
    split = packet["pic0_residual_split"]
    require(split["route_decision"]["primary_next_artifact"] == NEXT, "wrong primary next artifact")
    require(split["pic0_lane"]["can_close_bridge_alone"] is False, "Pic0 alone must not close")
    require(split["residual_lane"]["can_close_bridge_with_pic0_side_condition"] is True, "residual lane should be primary with Pic0 side condition")
    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(STATUS in note and NEXT in note and "Pic0 is demoted to a side condition" in note, "note missing essentials")
    print("AUDIT_PASS: post-alpha operator-source identity reduced to Phi_fin")


if __name__ == "__main__":
    main()
