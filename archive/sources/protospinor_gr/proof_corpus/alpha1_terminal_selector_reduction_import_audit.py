from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "alpha1_terminal_selector_reduction_import_certificate.json"
STATUS = "ALPHA1_TERMINAL_SELECTOR_REDUCED_BASEORDER_AHBINDING_SLOTMAP_OPEN"
NEXT = "Selected_U1Y_RouteC_TerminalMonad_BaseOrder_AHBinding_SMSlotMap_v1"


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
    candidate = packet["terminal_candidate"]
    require(candidate["forced_label"] == "L3-K2", "wrong terminal label")
    require(candidate["forced_value"] == [1, -2, 0], "wrong terminal value")
    require(candidate["forced_double"] == [2, -4, 0], "wrong terminal double")
    require(packet["ordered_layer_pic0_result"]["ordered_layer_pic0_removed_as_blocker"] is True, "ordered Pic0 blocker not removed")
    require(packet["ordered_layer_pic0_result"]["operator_layer_pic0_closed"] is False, "operator Pic0 must remain open")
    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(STATUS in note and NEXT in note and "forced label = L3-K2" in note, "note missing essentials")
    print("AUDIT_PASS: terminal selector reduced to base-order/AH-binding/slot-map packet")


if __name__ == "__main__":
    main()
