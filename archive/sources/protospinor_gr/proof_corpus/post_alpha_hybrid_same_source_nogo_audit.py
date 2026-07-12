from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_hybrid_same_source_nogo_certificate.json"
STATUS = "POST_ALPHA_HYBRID_SAMESOURCE_NOGO_REDUCED_SOURCE_IDENTITY_BRIDGE_OPEN"
NEXT = "Selected_U1Y_RouteC_OperatorSourceIdentity_Bridge_Subpacket_v1"


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
    require(packet["alpha_reconciliation"]["alpha_closed_locally"] is True, "local alpha should remain closed")
    require(packet["hybrid_packet"]["selected_emitted_count"] == 0, "expected zero selected emissions")
    require(packet["hybrid_packet"]["support_present_count"] == 6, "expected six support fields")
    require(packet["same_source_fill_nogo"]["fill_summary"]["required_fields"] == 7, "expected seven fields")
    require(packet["same_source_fill_nogo"]["current_source_nogo"]["mathematical_impossibility_claimed"] is False, "must not claim impossibility")
    require(packet["minimal_subpacket_plan"]["minimal_first_subpacket"] == NEXT, "wrong first subpacket")
    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(STATUS in note and NEXT in note and "mathematical impossibility = false" in note, "note missing essentials")
    print("AUDIT_PASS: post-alpha hybrid same-source no-go reduced to source-identity bridge")


if __name__ == "__main__":
    main()
