from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "routec_weylpair_matter_slot_blocksector_import_certificate.json"
STATUS = "ROUTEC_WEYLPAIR_MATTERSLOT_BLOCKSECTOR_IMPORTED_HYBRID_PACKET_NEXT"
NEXT_ARTIFACT = "MTT_Selected_RouteC_Hybrid_MatterSlot_Galerkin_Source_Packet_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["theorem"]["proved"] is True, "matter-slot/block-sector import should be proved")
    require(all(cert["input_checks"].values()), "all input checks should pass")
    require(all(cert["theorem_checks"].values()), "all theorem checks should pass")
    require(all(cert["route_checks"].values()), "all route checks should pass")
    require(all(cert["clue_checks"].values()), "all clue checks should pass")
    require(all(cert["hybrid_checks"].values()), "all hybrid checks should pass")
    require(all(cert["guardrail_checks"].values()), "all guardrail checks should pass")

    verdict = cert["verdict"]
    require(verdict["hybrid_packet_identified"] is True, "hybrid packet should be identified")
    require(verdict["monolithic_su5_shortcut_rejected"] is True, "SU5 shortcut should be rejected")
    require(verdict["selected_matter_slot_source_closed"] is False, "matter-slot source must remain open")
    require(verdict["selected_blocksector_source_closed"] is False, "block-sector source must remain open")
    require(verdict["conditional_A_promoted_to_A_selected"] is False, "A must not be promoted")
    require(verdict["observed_flavor_data_used"] is False, "observed data must not be used")
    require(verdict["next_required_artifact"] == NEXT_ARTIFACT, "wrong next artifact")

    require(
        packet["hybrid_closing_packet"]["recommended_strategy"]
        == "HYBRID_SELECTED_HYM_ORIGIN_THEN_GALERKIN_ZERO_MODES",
        "wrong hybrid strategy",
    )
    require(
        "hybrid packet" in note and "selected HYM/Strominger source" in note and NEXT_ARTIFACT in note,
        "note must state hybrid next gate",
    )

    print("AUDIT_PASS: matter-slot/block-sector reduction imported; hybrid packet is next")


if __name__ == "__main__":
    main()
