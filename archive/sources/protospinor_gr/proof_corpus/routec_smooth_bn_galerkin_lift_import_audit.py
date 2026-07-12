from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "routec_smooth_bn_galerkin_lift_import_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == "ROUTEC_SMOOTH_BN_GALERKIN_LIFT_IMPORTED_SELECTED_DE_STILL_OPEN", "unexpected status")
    require(cert["theorem"]["proved"] is True, "smooth BN lift import theorem should be proved")
    require(all(cert["closed_now"].values()), "all closed-now checks should pass")
    require(all(cert["numeric_checks"].values()), "all numeric checks should pass")
    require(all(cert["still_open_checks"].values()), "all still-open checks should pass")
    require(packet["summary"]["dimension"] == 27, "wrong basis dimension")
    require(packet["summary"]["zero_cluster"]["dimension"] == 3, "wrong zero cluster dimension")
    require(abs(packet["summary"]["complement_gap"] - 4.386490844928603) < 1e-12, "wrong complement gap")
    require(cert["verdict"]["smooth_BN_scaffold_built"] is True, "smooth scaffold should be built")
    require(cert["verdict"]["selected_D_E_action_closed"] is False, "selected D_E must remain open")
    require(cert["verdict"]["full_BN_payload_gate_closed"] is False, "full B_N gate must remain open")
    require(cert["verdict"]["R6_honest_replay_ready"] is False, "R6 must remain open")
    require(
        cert["verdict"]["next_required_artifact"] == "MTT_Selected_RouteC_DE_Action_on_Smooth_BN_v1",
        "wrong next artifact",
    )
    require("complement gap" in note and "Boundary" in note, "note must state result and boundary")

    print("AUDIT_PASS: smooth BN Galerkin scaffold imported; selected D_E remains open")


if __name__ == "__main__":
    main()
