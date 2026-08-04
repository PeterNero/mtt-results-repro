from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_sectorrouting_sourcepacket_certificate.json"
STATUS = "POST_ALPHA_SECTORROUTING_REDUCED_HYBRID_GALERKIN_SOURCE_PACKET_OPEN"
NEXT = "Selected_U1Y_RouteC_Hybrid_Galerkin_Overlap_Source_Packet_v1"


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
    exact = packet["routing_search"]["exact_rows_relative_to_locked_columns"]
    require(len(exact) == 1, "expected exactly one locked-column route")
    require(exact[0]["phase_route"] == ["u", "e"], "phase route mismatch")
    require(exact[0]["shift_route"] == ["d", "nuD"], "shift route mismatch")
    require(packet["routing_search"]["source_data_independently_selects_route"] is False, "source must not independently select route yet")
    require(packet["structural_matter_support"]["nuD_singlet_rule_closed"] is False, "nuD singlet rule should remain open")
    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(STATUS in note and NEXT in note and "This is not selected proof" in note, "note missing essentials")
    print("AUDIT_PASS: post-alpha sector routing reduced to hybrid source packet")


if __name__ == "__main__":
    main()
