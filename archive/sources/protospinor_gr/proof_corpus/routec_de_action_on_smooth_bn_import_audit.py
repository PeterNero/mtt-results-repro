from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "routec_de_action_on_smooth_bn_import_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == "ROUTEC_DE_ACTION_ON_SMOOTH_BN_IMPORTED_SOURCE_PROMOTION_OPEN", "unexpected status")
    require(cert["theorem"]["proved"] is True, "D_E import theorem should be proved")
    require(all(cert["closed_now"].values()), "all closed-now checks should pass")
    require(all(cert["validator_checks"].values()), "all validator checks should pass")
    require(all(cert["still_open_checks"].values()), "all still-open checks should pass")
    require(cert["verdict"]["D_E_matrix_on_27_mode_BN_built"] is True, "D_E matrix should be built")
    require(cert["verdict"]["honest_source_promotes"] is False, "honest source must not promote")
    require(cert["verdict"]["full_selected_DE_action_closed"] is False, "full selected D_E must remain open")
    require(cert["verdict"]["sector_projectors_closed"] is False, "sector projectors must remain open")
    require(cert["verdict"]["dotD_alpha1_closed"] is False, "dotD must remain open")
    require(cert["verdict"]["R6_honest_replay_ready"] is False, "R6 must remain open")
    require(
        cert["verdict"]["next_required_artifact"] == "MTT_Selected_RouteC_Sector_Projectors_and_DotD_on_Smooth_BN_v1",
        "wrong next artifact",
    )
    require(packet["validation"]["matrix_consistency"]["domain_dimension"] == 27, "wrong domain dimension")
    require(packet["validation"]["matrix_consistency"]["family_kernel_dimension"] == 3, "wrong family kernel")
    require(packet["validation"]["matrix_consistency"]["higgs_kernel_dimension"] == 1, "wrong Higgs kernel")
    require("diagnostic q79 validator passes" in note and "Boundary" in note, "note must state result and boundary")

    print("AUDIT_PASS: D_E action on smooth BN imported; source promotion remains open")


if __name__ == "__main__":
    main()
