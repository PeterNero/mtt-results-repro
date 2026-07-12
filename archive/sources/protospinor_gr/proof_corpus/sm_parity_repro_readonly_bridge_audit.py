from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "sm_parity_repro_readonly_bridge_certificate.json"
STATUS = "SM_PARITY_REPRO_READONLY_BRIDGE_IMPORTED_PARITY_CLOSED_NOKNOB_OPEN"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "bridge must not claim full closure")
    require(cert["theorem"]["proved"] is True, "bridge theorem should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")

    summary = packet["repro_summary"]
    require(summary["SM_parity_closed"] is True, "SM parity should be true in repro")
    require(summary["true_SM_equivalence_closed"] is False, "true equivalence overclaimed")
    require(summary["no_knob_closed"] is False, "no-knob overclaimed")
    require(summary["qasu3_status"] == "QASU3_PARITY_INTERFACE_REPLACEMENT_ACCEPTED_ACTUAL_OPERATOR_PACKET_OPEN", "Qa/SU3 status drift")

    require(packet["what_remains_open"]["actual_QaSU3_D_E_or_rho_E_operator_packet"] is True, "Qa/SU3 operator gate lost")
    require(packet["what_remains_open"]["dynamic_C1_source_map_selection_in_this_GR_response_chain"] is True, "dynamic C1 gate lost")
    require(packet["guardrails"]["does_not_close_dynamic_C1_source_map_gate"] is True, "dynamic C1 guardrail missing")
    require(packet["guardrails"]["does_not_import_repro_as_no_knob_closure"] is True, "no-knob guardrail missing")
    require(len(packet["repro_hashes"]) == 5, "expected five repro hashes")

    require(STATUS in note and "SM parity closure       = TRUE" in note and "no-knob closure         = FALSE" in note, "note missing essentials")
    print("AUDIT_PASS: SM parity repro bridge imported as parity-tier only; no-knob and dynamic C1 gates remain open")


if __name__ == "__main__":
    main()
