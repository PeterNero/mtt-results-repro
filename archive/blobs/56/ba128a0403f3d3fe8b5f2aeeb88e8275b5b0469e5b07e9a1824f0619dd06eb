from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "routec_source_provenance_or_basis_reduction_import_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == "ROUTEC_PROVENANCE_BASIS_SUPPORT_CLOSED_SELECTED_PRIMITIVES_OPEN", "unexpected status")
    require(cert["theorem"]["proved"] is True, "reduction theorem should be proved")
    require(all(cert["closed_now"].values()), "all closed-now checks should pass")
    require(all(cert["still_open"].values()), "all still-open gates should remain true")
    require(packet["provenance_gate"]["closed"] is False, "provenance gate should remain open")
    require(packet["basis_gate"]["closed"] is False, "basis gate should remain open")
    require(packet["provenance_gate"]["minimal_missing_primitive"] == "Phi_fin_selected_payload", "wrong provenance primitive")
    require(packet["basis_gate"]["minimal_missing_primitive"] == "quotient_valid_B_N_basis_certificate", "wrong basis primitive")
    require(packet["R6_honest_replay"]["ready"] is False, "R6 must not be ready")
    require(cert["verdict"]["R1_selected_source_closed"] is False, "R1 must remain open")
    require(cert["verdict"]["R4_selected_basis_closed"] is False, "R4 must remain open")
    require(cert["verdict"]["selected_weylpair_source_provenance_proved"] is False, "Weyl-pair provenance must remain open")
    require("R1 remains blocked" in note and "R4 remains blocked" in note, "note must state both blockers")
    require(all(cert["guardrails"].values()), "all guardrails must hold")

    print("AUDIT_PASS: Route-C provenance/basis support closed; selected primitives remain open")


if __name__ == "__main__":
    main()
