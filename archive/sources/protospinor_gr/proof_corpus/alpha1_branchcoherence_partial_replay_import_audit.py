from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "alpha1_branchcoherence_partial_replay_import_certificate.json"
STATUS = "ALPHA1_BRANCHCOHERENCE_PARTIAL_REPLAY_CLOSED_ORIENTATION_SELECTOR_OPEN"
NEXT = "Selected_U1Y_RouteC_MatterSlot_OrientationSelector_from_HYM_FiniteReplay_v1"


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
    require(packet["what_closes_now"]["stationary_HYM_finite_validator_replay"] is True, "stationary replay should close")
    require(packet["what_closes_now"]["rho_s_validator_ready_promoted"] is True, "rho_s should be validator-ready")
    contract = packet["orientation_selector_contract"]
    require(contract["must_emit"]["phase_sectors"] == ["u", "e"], "wrong phase sectors")
    require(contract["must_emit"]["shift_sectors"] == ["d", "nuD"], "wrong shift sectors")
    require(contract["must_emit"]["normalization"] == "rho_s(T_i)/sqrt(2) in the selected oriented matter slots", "wrong normalization")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(STATUS in note and NEXT in note and "rho_s validator-ready = true" in note, "note missing essentials")
    print("AUDIT_PASS: branch-coherence partial replay closed; orientation selector remains open")


if __name__ == "__main__":
    main()
