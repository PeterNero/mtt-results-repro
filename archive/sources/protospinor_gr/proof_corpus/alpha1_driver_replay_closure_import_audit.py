from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "alpha1_driver_replay_closure_import_certificate.json"
STATUS = "ALPHA1_DRIVER_REPLAY_CLOSED_PRIMITIVE_C1_LAMBDA_OPEN"
NEXT = "Selected_U1Y_RouteC_Primitive_C1_Contractions_or_Lambda12_Gate_v1"


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
    value = packet["promoted_value"]
    require(value["selected_value_emitted_by_this_theorem"] is True, "selected value not emitted")
    require(value["N_alpha1_h_ext"] == 1.0, "wrong N alpha1 value")
    require(value["du_dalpha1"] == "h_ext", "wrong alpha derivative")
    replay = packet["honest_dotd_replay"]
    require(replay["selected_dotD_source_verified"] is True, "selected dotD source not verified")
    require(replay["alpha1_driver_verified"] is True, "alpha1 driver not verified")
    require(replay["honest_dotD_validator_closed"] is True, "honest dotD replay not closed")
    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(STATUS in note and NEXT in note and "honest dotD replay = PASS" in note, "note missing essentials")
    print("AUDIT_PASS: alpha1 driver and honest dotD replay closed; primitive C1/lambda remain open")


if __name__ == "__main__":
    main()
