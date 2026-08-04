from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_candidate_routes_certificate.json"
STATUS = "POST_ALPHA_CANDIDATE_ROUTES_BUILT_SELECTION_AND_SPECTRA_OPEN"
NEXT = "MTT_Selected_RouteC_Primitive_Source_Selection_Theorem_or_U1_Direct_Operator_Row_v1"


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
    primitive = packet["primitive_c1_candidate_route"]
    require(primitive["minimal_active_shift"] == [1, 1], "active shift should be (1,1)")
    require(primitive["candidate_count"] == 4, "expected four candidate families")
    require(primitive["selected_by_theorem"] is False, "candidate matrices must remain unselected")
    require(packet["lambda12_candidate_route"]["operator_source_status"] == "U1_HYPERCHARGE_OPERATOR_SPECTRUM_SOURCE_PACKET_BUILT_SPECTRUM_OPEN", "wrong U1 source status")
    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(STATUS in note and NEXT in note and "selected by theorem = false" in note, "note missing essentials")
    print("AUDIT_PASS: post-alpha candidate routes imported without selected promotion")


if __name__ == "__main__":
    main()
