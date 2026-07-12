from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "gr_tt_aint_z64_identity_source_hunt_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    require(
        cert["status"] == "GR_TT_AINT_Z64_IDENTITY_NOT_SOURCED_CLOSURE_STRAIN_ROUTE_REMAINS",
        "unexpected status",
    )
    source = cert["source_tests"]
    verdict = cert["verdict"]
    guards = cert["guardrails"]

    require(source["gr_reduction_has_einstein_normalization"] is True, "GR source should have EH normalization")
    require(source["qg_has_graviton_tt_or_projected_graviton"] is True, "QG source should have projected graviton framework")
    require(source["qg_has_aint_gap_but_not_z64_identity"] is True, "QG Aint should not source Z64 identity")
    require(source["central_circle_links_gravity_structurally"] is True, "central circle gravity clue should be present")
    require(source["existing_gr_cert_rejects_z64_as_gr_substitute"] is True, "existing GR cert should reject Z64 substitute")
    require(source["conditional_bridge_not_usable_as_gr_gap"] is True, "conditional bridge should not be GR gap")
    require(verdict["z64_is_best_structural_clue"] is True, "Z64 should remain best clue")
    require(verdict["z64_closes_gr_gap_now"] is False, "Z64 must not close GR gap now")
    require(verdict["closure_strain_route_still_primary_for_gr"] is True, "closure strain should remain primary")
    require(guards["claims_GR_TT_Aint_equals_Z64"] is False, "must not claim GR TT Aint equals Z64")
    require(guards["forbids_structural_central_circle_language_as_operator_identity"] is True, "operator identity guard required")

    print("AUDIT_PASS: GR TT Aint/Z64 identity not sourced; closure-strain route remains primary")


if __name__ == "__main__":
    main()
