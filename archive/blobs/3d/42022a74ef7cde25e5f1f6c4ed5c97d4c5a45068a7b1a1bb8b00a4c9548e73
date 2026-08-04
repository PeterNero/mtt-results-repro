from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "routec_selected_primitive_emission_search_import_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == "ROUTEC_SELECTED_PRIMITIVE_EMISSION_SEARCH_IMPORTED_NO_LEGAL_EMISSION_FOUND", "unexpected status")
    require(cert["theorem"]["proved"] is True, "search import theorem should be proved")
    require(all(cert["closed_now"].values()), "all closed-now checks should pass")
    require(all(cert["blockers"].values()), "all blocker checks should pass")
    require(all(cert["guardrails"].values()), "all guardrails must hold")
    require(cert["verdict"]["selected_primitives_found"] is False, "selected primitives must not be found")
    require(cert["verdict"]["R1_promotes"] is False, "R1 must not promote")
    require(cert["verdict"]["R4_promotes"] is False, "R4 must not promote")
    require(cert["verdict"]["R6_ready"] is False, "R6 must not be ready")
    require(
        cert["verdict"]["next_required_artifact"] == "MTT_Selected_RouteC_NonIdentity_RhoE_and_BN_Construction_v1",
        "wrong next artifact",
    )
    require(packet["search_results"]["Phi_fin_payload"]["selected_values_emitted"] is False, "Phi_fin should be absent")
    require(packet["search_results"]["B_N_basis"]["required_success_gates_pass"] is False, "B_N should not pass")
    require("formal-lift algebra can" in note and "Still absent" in note, "note must state import boundary")

    print("AUDIT_PASS: selected primitive emission search imported; no legal emission found")


if __name__ == "__main__":
    main()
