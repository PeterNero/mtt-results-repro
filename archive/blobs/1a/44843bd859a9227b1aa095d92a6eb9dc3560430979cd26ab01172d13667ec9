from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "alpha1_orientation_selector_nogo_import_certificate.json"
STATUS = "ALPHA1_ORIENTATION_SELECTOR_HYM_REPLAY_NOGO_TERMINAL_GRADING_OPEN"
NEXT = "Selected_U1Y_RouteC_TerminalMonad_MatterSlot_SectionRing_SourceSelector_v1"


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
    require(packet["hym_replay_orientation_no_go"]["stationary_hym_replay_cannot_select_orientation"] is True, "no-go not proved")
    route = packet["positive_route"]["source_selector_to_prove"]
    require(route["forced_label_inside_lane"] == "L3-K2", "wrong forced label")
    require(route["forced_value"] == [1, -2, 0], "wrong forced value")
    require(packet["readout_tests"]["locked_c1_partition_readout"]["allowed_as_selected_source"] is False, "locked target selector must be forbidden")
    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(STATUS in note and NEXT in note and "forced label = L3-K2" in note, "note missing essentials")
    print("AUDIT_PASS: HYM orientation no-go imported; terminal grading route remains open")


if __name__ == "__main__":
    main()
