from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "alpha1_operator_emission_overlap_import_certificate.json"
STATUS = "ALPHA1_OPERATOR_EMISSION_OVERLAP_FUNCTIONAL_CLOSED_DRIVER_OPEN"
NEXT = "Selected_U1Y_RouteC_Alpha1_Driver_Replay_from_OrientedOverlap_v1"


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
    require(packet["overlap_normalization"]["normalization"] == "rho_s(T_i)/sqrt(2)", "wrong normalization")
    require(packet["overlap_normalization"]["selected_functional_overlap_normalization_emitted"] is True, "normalization not emitted")
    require(set(packet["emitted_operator_blocks"].keys()) == {"u", "d", "e", "nuD"}, "wrong blocks")
    require(packet["alpha_boundary"]["alpha1_driver_verified"] is False, "driver should remain open")
    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(STATUS in note and NEXT in note and "normalization = rho_s(T_i)/sqrt(2)" in note, "note missing essentials")
    print("AUDIT_PASS: functional operator emission and overlap normalization closed; alpha1 driver remains open")


if __name__ == "__main__":
    main()
