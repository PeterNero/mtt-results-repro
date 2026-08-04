from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "dotd_alpha1_transport_derivative_import_certificate.json"
STATUS = "DOTD_ALPHA1_TRANSPORT_DERIVATIVE_IMPORTED_DRIVER_NORMALIZATION_OPEN"
NEXT = "MTT_Selected_Alpha1_SourceStrength_Normalization_or_Driver_Theorem_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim full closure")
    require(all(cert["checks"].values()), "all checks should pass")
    formula = packet["transport_derivative_formula"]
    require(formula["dU_dalpha"] == "-(du/dalpha) ad(T3) U", "wrong dU/dalpha formula")
    require(formula["dotD_h"] == "dotD_h=(dh) ad(T3)", "wrong dotD formula")
    require(formula["identity"] == "D_sel(delta psi)+dotD_h psi_sel=0", "wrong response identity")
    require(packet["validator_boundary"]["mathematical_dotd_matrices_pass_if_flags_are_theorem_derived"] is True, "validator math not ready")
    require(packet["driver_audit"]["alpha1_driver_verified_now"] is False, "driver should remain open")
    require(packet["pin_down_kernel"]["current_evaluation"]["selected_value_emitted_now"] is False, "selected value should remain open")
    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(STATUS in note and NEXT in note and "dU/dalpha" in note, "note missing essentials")
    print("AUDIT_PASS: dotD alpha1 transport derivative imported; driver normalization remains open")


if __name__ == "__main__":
    main()
