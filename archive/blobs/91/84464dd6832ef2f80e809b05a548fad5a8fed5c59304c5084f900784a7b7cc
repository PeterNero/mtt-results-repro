from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "alpha1_terminal_orientation_bridge_import_certificate.json"
STATUS = "ALPHA1_TERMINAL_ORIENTATION_ORDERED_SELECTOR_CLOSED_OPERATOR_EMISSION_OPEN"
NEXT = "Selected_U1Y_RouteC_OperatorEmission_and_OverlapNormalization_from_TerminalSlotMap_v1"


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
    orientation = packet["ordered_orientation"]
    require(orientation["closed"] is True, "ordered orientation should close")
    require(orientation["phase_sectors"] == ["u", "e"], "wrong phase sectors")
    require(orientation["shift_sectors"] == ["d", "nuD"], "wrong shift sectors")
    require(packet["replay_bridge"]["rho_s_validator_ready"] is True, "rho_s should remain validator-ready")
    require(packet["emission_gap"]["same_branch_selected_operator_emission"] is False, "operator emission must remain open")
    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(STATUS in note and NEXT in note and "10_M clock = u,e" in note, "note missing essentials")
    print("AUDIT_PASS: terminal ordered orientation closed; operator emission remains open")


if __name__ == "__main__":
    main()
