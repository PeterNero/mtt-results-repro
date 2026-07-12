from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_selected_finite_trace_certificate.json"
STATUS = "POST_ALPHA_SELECTED_FINITE_TRACE_NOGO_27MODE_PREFIX_OPEN"
NEXT = "Selected_U1Y_RouteC_TraceEquals27Mode_or_FullHYMReplay_v1"


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
    require(packet["old_smoke_lane"]["status"] == "REJECTED_AS_SELECTED_TRACE", "old smoke should be rejected")
    require(packet["smooth_27mode_lane"]["status"] == "PREFIX_VALUES_EXECUTED_SOURCE_TRACE_OPEN", "wrong prefix status")
    require(packet["decision"]["Phi_fin_closed"] is False, "Phi_fin must remain open")
    require(packet["decision"]["smooth_27mode_prefix_values_present"] is True, "prefix values should be present")
    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(STATUS in note and NEXT in note and "Phi_fin closed = false" in note, "note missing essentials")
    print("AUDIT_PASS: post-alpha selected finite trace imported without Phi_fin promotion")


if __name__ == "__main__":
    main()
