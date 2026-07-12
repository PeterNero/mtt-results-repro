from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_phifin_subpacket_certificate.json"
STATUS = "POST_ALPHA_PHIFIN_SUBPACKET_BUILT_SELECTED_FINITE_TRACE_OPEN"
NEXT = "Selected_U1Y_RouteC_SelectedFiniteTrace_SourceOrNoGo_v1"


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
    require(packet["decision"]["domain_lock_closed"] is True, "domain lock should close")
    require(packet["decision"]["Phi_fin_constructed"] is False, "Phi_fin must remain open")
    require(packet["decision"]["selected_operator_payload_emitted"] is False, "operator payload must remain open")
    require(packet["stage_checks"][0]["passes"] is True, "domain stage should pass")
    require(all(stage["passes"] is False for stage in packet["stage_checks"][1:]), "later stages should remain open")
    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(STATUS in note and NEXT in note and "not selected source data" in note, "note missing essentials")
    print("AUDIT_PASS: post-alpha Phi_fin subpacket imported without smoke promotion")


if __name__ == "__main__":
    main()
