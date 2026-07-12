from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "routec_weylpair_sector_routing_source_import_certificate.json"
STATUS = "ROUTEC_WEYLPAIR_SECTOR_ROUTING_IMPORTED_LOCKED_TARGET_UNIQUE_SOURCE_CERT_OPEN"
NEXT_ARTIFACT = "MTT_Selected_RouteC_WeylPair_SectorCharge_or_Chirality_Certificate_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["theorem"]["proved"] is True, "sector-routing import should be proved")
    require(all(cert["input_checks"].values()), "all input checks should pass")
    require(all(cert["routing_checks"].values()), "all routing checks should pass")
    require(all(cert["support_checks"].values()), "all support checks should pass")
    require(all(cert["lemma_checks"].values()), "all lemma checks should pass")
    require(all(cert["guardrail_checks"].values()), "all guardrail checks should pass")

    verdict = cert["verdict"]
    require(verdict["all_two_two_routes_enumerated"] is True, "routes should be enumerated")
    require(verdict["locked_columns_pick_intended_route_uniquely"] is True, "locked route should be unique")
    require(verdict["selected_source_sector_routing_proved"] is False, "source routing must remain open")
    require(
        verdict["selected_sector_charge_or_chirality_certificate_emitted"] is False,
        "sector charge/chirality cert must remain open",
    )
    require(verdict["conditional_A_promoted_to_A_selected"] is False, "A must not be promoted")
    require(verdict["observed_flavor_data_used"] is False, "observed data must not be used")
    require(verdict["next_required_artifact"] == NEXT_ARTIFACT, "wrong next artifact")

    exact = packet["routing_search"]["exact_rows_relative_to_locked_columns"]
    require(exact[0]["phase_route"] == ["u", "e"], "phase route mismatch")
    require(exact[0]["shift_route"] == ["d", "nuD"], "shift route mismatch")
    require(
        "target-column uniqueness" in note
        and "not independent selected-source routing" in note
        and NEXT_ARTIFACT in note,
        "note must state boundary and next artifact",
    )

    print("AUDIT_PASS: sector-routing attempt imported; sector charge/chirality certificate is next")


if __name__ == "__main__":
    main()
