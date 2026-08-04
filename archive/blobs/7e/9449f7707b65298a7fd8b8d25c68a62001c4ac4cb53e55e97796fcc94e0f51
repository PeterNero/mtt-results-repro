from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "alpha1_terminal_baseorder_ahbinding_import_certificate.json"
STATUS = "ALPHA1_TERMINAL_BASEORDER_AHBINDING_PROVED_BRANCHCOHERENCE_OPEN"
NEXT = "Selected_U1Y_RouteC_BranchCoherence_Selector_or_FiniteValidatorReplay_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(all(cert["checks"].values()), "all checks should pass")
    binding = packet["baseorder_binding"]
    require(binding["same_L3_K2_identity"] is True, "same L3-K2 identity not proved")
    require(binding["selected_L"] == [1, -2, 0], "wrong L")
    require(binding["selected_L2"] == [2, -4, 0], "wrong L2")
    slot_map = packet["slot_map"]["finite_structural_route"]
    require(slot_map["10_M_clock"] == "I_3", "wrong 10M clock")
    require(slot_map["bar5_M_shift"] == "F", "wrong bar5 shift")
    require(slot_map["phase"] == ["u", "e"], "wrong phase")
    require(slot_map["shift"] == ["d", "nuD"], "wrong shift")
    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(STATUS in note and NEXT in note and "U_10 = I_3" in note, "note missing essentials")
    print("AUDIT_PASS: terminal base-order/AH-binding imported; branch coherence remains open")


if __name__ == "__main__":
    main()
