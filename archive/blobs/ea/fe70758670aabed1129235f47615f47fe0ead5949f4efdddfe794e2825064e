from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_trace_equals_27mode_certificate.json"
STATUS = "POST_ALPHA_TRACE_EQUALS_27MODE_DE_GAP_LAYER_CLOSED_DOTD_C1_OPEN"
NEXT = "Selected_U1Y_RouteC_dotD_Alpha1_C1_Response_Emission_v1"


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
    require(packet["decision"]["DE_gap_Riesz_Green_layer_closed"] is True, "DE gap layer should close")
    require(packet["decision"]["dotD_alpha1_C1_closed"] is False, "dotD/C1 must remain open")
    require(packet["decision"]["A_selected_or_b_selected_closed"] is False, "A/b must remain open")
    require(packet["alpha_reconciliation"]["alpha_closed_locally"] is True, "local alpha should remain closed")
    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(STATUS in note and NEXT in note and "selected trace equality for 27-mode D_E = true" in note, "note missing essentials")
    print("AUDIT_PASS: post-alpha trace equals 27-mode DE gap layer closed with C1 boundary open")


if __name__ == "__main__":
    main()
