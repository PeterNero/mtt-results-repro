from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "routec_nonidentity_rhoe_bn_construction_import_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == "ROUTEC_NONIDENTITY_RHOE_NUMERICAL_PACKET_IMPORTED_BN_STILL_OPEN", "unexpected status")
    require(cert["theorem"]["proved"] is True, "nonidentity rhoE import theorem should be proved")
    require(all(cert["closed_now"].values()), "all closed-now checks should pass")
    require(all(cert["numeric_checks"].values()), "all numeric checks should pass")
    require(all(cert["still_open_checks"].values()), "all still-open checks should pass")
    require(all(cert["guardrails"].values()), "all guardrails must hold")
    require(cert["verdict"]["nonidentity_rhoE_numeric_packet_built"] is True, "rhoE packet should be built")
    require(cert["verdict"]["R2_metric_connection_numeric_gate_closed"] is True, "R2 numeric gate should close")
    require(cert["verdict"]["R2_source_promotion_closed"] is False, "R2 source promotion must remain open")
    require(cert["verdict"]["R4_BN_payload_closed"] is False, "R4 must remain open")
    require(cert["verdict"]["R6_honest_replay_ready"] is False, "R6 must remain open")
    require(
        cert["verdict"]["next_required_artifact"] == "MTT_Selected_RouteC_Smooth_BN_Galerkin_Lift_v1",
        "wrong next artifact",
    )
    require(packet["rho_E_candidate"]["numeric_gates"]["passes_numeric_packet_gate"] is True, "rhoE gate should pass")
    require(packet["B_N_scaffold"]["passes_B_N_payload_gate"] is False, "B_N payload must remain open")
    require("Heisenberg/Weyl" in note and "Boundary" in note, "note must state result and boundary")

    print("AUDIT_PASS: non-identity rhoE packet imported; smooth B_N remains open")


if __name__ == "__main__":
    main()
