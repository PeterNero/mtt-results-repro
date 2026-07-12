from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "routec_weylpair_source_to_c1_transfer_import_certificate.json"
STATUS = "ROUTEC_WEYLPAIR_SOURCE_TO_C1_TRANSFER_IMPORTED_CONDITIONAL_EXACT_ROUTING_OPEN"
NEXT_ARTIFACT = "MTT_Selected_RouteC_WeylPair_SectorRouting_Source_Lemma_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["theorem"]["proved"] is True, "transfer import theorem should be proved")
    require(all(cert["input_checks"].values()), "all input checks should pass")
    require(all(cert["transfer_checks"].values()), "all transfer checks should pass")
    require(all(cert["selected_open_checks"].values()), "all selected-open checks should pass")
    require(all(cert["reduction_checks"].values()), "all reduction checks should pass")
    require(all(cert["guardrail_checks"].values()), "all guardrail checks should pass")

    verdict = cert["verdict"]
    require(verdict["conditional_transfer_map_exact"] is True, "conditional transfer should be exact")
    require(verdict["phase_column_reproduced"] is True, "phase column should reproduce")
    require(verdict["shift_column_reproduced"] is True, "shift column should reproduce")
    require(verdict["selected_sector_routing_proved"] is False, "sector routing must remain open")
    require(verdict["selected_normalization_proved"] is False, "normalization must remain open")
    require(verdict["conditional_A_promoted_to_A_selected"] is False, "A must not be promoted")
    require(verdict["b_selected_emitted"] is False, "b_selected must remain open")
    require(verdict["observed_flavor_data_used"] is False, "observed data must not be used")
    require(verdict["next_required_artifact"] == NEXT_ARTIFACT, "wrong next artifact")

    transfer = packet["conditional_transfer_map"]
    require(transfer["phase_residual"] == 0.0 and transfer["shift_residual"] == 0.0, "residuals not exact")
    require(
        "conditional source-to-C1 transfer map is now imported" in note
        and "remaining blocker is not the transfer calculation" in note
        and NEXT_ARTIFACT in note,
        "note must state transfer reduction and next gate",
    )

    print("AUDIT_PASS: conditional Weyl-pair source-to-C1 transfer imported; sector routing remains open")


if __name__ == "__main__":
    main()
