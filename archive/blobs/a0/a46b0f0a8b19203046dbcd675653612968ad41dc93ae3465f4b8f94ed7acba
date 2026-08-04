from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "routec_weylpair_sector_charge_import_certificate.json"
STATUS = "ROUTEC_WEYLPAIR_SECTOR_CHARGE_IMPORTED_STRUCTURAL_MATCH_SOURCE_OPEN"
NEXT_ARTIFACT = "MTT_Selected_RouteC_WeylPair_MatterSlot_or_BlockSector_Source_Theorem_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["theorem"]["proved"] is True, "sector-charge import should be proved")
    require(all(cert["input_checks"].values()), "all input checks should pass")
    require(all(cert["route_a_checks"].values()), "all route A checks should pass")
    require(all(cert["route_b_checks"].values()), "all route B checks should pass")
    require(all(cert["current_data_checks"].values()), "all current-data checks should pass")
    require(all(cert["certificate_checks"].values()), "all certificate checks should pass")
    require(all(cert["guardrail_checks"].values()), "all guardrail checks should pass")

    verdict = cert["verdict"]
    require(verdict["su5_e6_structural_match_identified"] is True, "structural match should be identified")
    require(verdict["selected_su5_source_proved"] is False, "selected SU5 source must remain open")
    require(
        verdict["selected_singlet_neutrino_shift_rule_proved"] is False,
        "singlet neutrino rule must remain open",
    )
    require(verdict["selected_block_route_pair_split_proved"] is False, "block route split must remain open")
    require(verdict["sector_charge_certificate_closed"] is False, "certificate must remain source-open")
    require(verdict["conditional_A_promoted_to_A_selected"] is False, "A must not be promoted")
    require(verdict["observed_flavor_data_used"] is False, "observed data must not be used")
    require(verdict["next_required_artifact"] == NEXT_ARTIFACT, "wrong next artifact")

    result = packet["certificate_result"]
    require(result["phase_route_required"] == ["u", "e"], "phase route mismatch")
    require(result["shift_route_required"] == ["d", "nuD"], "shift route mismatch")
    require(
        "strongest\nstructural match" in note
        and "certificate remains source-open" in note
        and NEXT_ARTIFACT in note,
        "note must state reduction and next artifact",
    )

    print("AUDIT_PASS: sector-charge structural match imported; matter-slot/block-sector theorem is next")


if __name__ == "__main__":
    main()
