from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "routec_sector_projectors_dotd_on_smooth_bn_import_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    residuals = packet["projector_residuals"]

    require(cert["status"] == "ROUTEC_SECTOR_PROJECTORS_DOTD_ON_SMOOTH_BN_IMPORTED_SOURCE_PROMOTION_OPEN", "unexpected status")
    require(cert["theorem"]["proved"] is True, "projectors/dotD import theorem should be proved")
    require(all(cert["closed_now"].values()), "all closed-now checks should pass")
    require(all(cert["algebra_checks"].values()), "all algebra checks should pass")
    require(all(cert["still_open_checks"].values()), "all still-open checks should pass")
    require(all(residuals[sector]["rank_trace"] == 3.0 for sector in ("Q", "u", "d", "L", "e", "N")), "wrong family ranks")
    require(residuals["H"]["rank_trace"] == 1.0, "wrong Higgs rank")
    require(cert["verdict"]["sector_projectors_built"] is True, "sector projectors should be built")
    require(cert["verdict"]["dotD_alpha1_on_same_basis_built"] is True, "dotD should be built")
    require(cert["verdict"]["selected_dotD_source_promotes"] is False, "selected dotD source must remain open")
    require(cert["verdict"]["alpha1_driver_promotes"] is False, "alpha1 driver must remain open")
    require(cert["verdict"]["primitive_C1_overlap_contractions_closed"] is False, "C1 overlaps must remain open")
    require(cert["verdict"]["R6_honest_replay_ready"] is False, "R6 must remain open")
    require(
        cert["verdict"]["next_required_artifact"] == "MTT_Selected_RouteC_C1_Primitive_Response_or_Selected_Source_Proof_v1",
        "wrong next artifact",
    )
    require("finite horizontal-response algebra" in note and "Boundary" in note, "note must state result and boundary")

    print("AUDIT_PASS: sector projectors/dotD imported; selected source promotion remains open")


if __name__ == "__main__":
    main()
