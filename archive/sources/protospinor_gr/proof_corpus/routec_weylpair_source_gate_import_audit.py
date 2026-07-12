from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "routec_weylpair_source_gate_import_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == "ROUTEC_WEYLPAIR_SOURCE_GATE_IMPORTED_ASELECTED_SOURCE_OPEN", "unexpected status")
    require(cert["theorem"]["proved"] is True, "Weyl-pair gate import theorem should be proved")
    require(all(cert["closed_now"].values()), "all closed-now checks should pass")
    require(all(cert["still_open"].values()), "all still-open gates should remain true")
    require(cert["span_test"]["target_in_span"] is True, "Weyl pair should span locked splitter")
    require(cert["span_test"]["relative_residual"] < 1.0e-12, "Weyl-pair residual too large")
    require(cert["span_test"]["columns"] == ["phase_packet", "shift_packet"], "unexpected Weyl columns")
    require(set(packet["enriched_weyl_pair_packet"]["source_directions"]) == {"phase_packet", "shift_packet"}, "missing source directions")
    require(cert["source_contract"]["operator_emission_status_imported"]["A_selected_currently_emitted"] is False, "A_selected must remain open")
    require(cert["source_contract"]["operator_emission_status_imported"]["b_selected_currently_emitted"] is False, "b_selected must remain open")
    require(cert["theorem_gate"]["status"] == "ALGEBRAIC_GATE_BUILT_SOURCE_PROOF_OPEN", "theorem gate boundary changed")
    require(cert["verdict"]["selected_source_provenance_proved"] is False, "source provenance must remain open")
    require(cert["verdict"]["full_SM_or_no_knob_closure"] is False, "SM closure must remain open")
    require("phase_packet: u,e = I + Z" in note, "note must identify phase packet")
    require("shift_packet: d,nuD = I + X" in note, "note must identify shift packet")
    require(all(cert["guardrails"].values()), "all guardrails must hold")

    print("AUDIT_PASS: Weyl-pair source gate imported; A_selected/source proof remains open")


if __name__ == "__main__":
    main()
