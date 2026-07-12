from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "routec_weylpair_source_provenance_import_certificate.json"
STATUS = "ROUTEC_WEYLPAIR_SOURCE_PROVENANCE_IMPORTED_SOURCE_CARRIER_CLOSED_C1_TRANSFER_OPEN"
NEXT_ARTIFACT = "MTT_Selected_RouteC_WeylPair_SourceToC1_Transfer_Map_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["theorem"]["proved"] is True, "source provenance import should be proved")
    require(all(cert["input_checks"].values()), "all input checks should pass")
    require(all(cert["carrier_checks"].values()), "all carrier checks should pass")
    require(all(cert["active_checks"].values()), "all active checks should pass")
    require(all(cert["transfer_open_checks"].values()), "all transfer-open checks should pass")
    require(all(cert["lemma_checks"].values()), "all lemma checks should pass")
    require(all(cert["guardrail_checks"].values()), "all guardrail checks should pass")

    verdict = cert["verdict"]
    require(
        verdict["source_level_phase_Z_carrier_provenance_closed"] is True,
        "phase carrier should close",
    )
    require(
        verdict["source_level_shift_X_carrier_provenance_closed"] is True,
        "shift carrier should close",
    )
    require(verdict["active_shift_1_1_provenance_closed"] is True, "active shift should close")
    require(verdict["operator_level_C1_transfer_map_emitted"] is False, "transfer must remain open")
    require(verdict["conditional_A_promoted_to_A_selected"] is False, "A must not be promoted")
    require(verdict["b_selected_emitted"] is False, "b_selected must remain open")
    require(verdict["honest_selected_deltaTheta_solve_run"] is False, "selected solve must remain open")
    require(verdict["observed_flavor_data_used"] is False, "observed data must not be used")
    require(verdict["next_required_artifact"] == NEXT_ARTIFACT, "wrong next artifact")

    require(packet["c1_transfer_map"]["selected_source_to_C1_response_map_emitted"] is False, "lost transfer gap")
    require(
        "source-level Weyl-pair provenance is now imported" in note
        and "remaining blocker is the transfer map" in note
        and NEXT_ARTIFACT in note,
        "note must state reduction and next gate",
    )

    print("AUDIT_PASS: Weyl-pair source carrier imported; C1 transfer map remains open")


if __name__ == "__main__":
    main()
