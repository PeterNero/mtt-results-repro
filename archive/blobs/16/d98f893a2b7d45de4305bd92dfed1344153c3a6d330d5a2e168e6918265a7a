from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_primitive_c1_gate_import_certificate.json"
STATUS = "POST_ALPHA_PRIMITIVE_C1_LAMBDA12_GATE_OPEN"
NEXT = "Selected_U1Y_RouteC_PrimitiveC1_AtomEmission_or_SelectedLambda12_SpectralTable_v1"


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
    prefix = packet["post_alpha_prefix"]
    require(prefix["alpha1_driver_verified"] is True, "alpha1 prefix not closed")
    require(prefix["honest_dotD_validator_closed"] is True, "honest dotD not closed")
    require(packet["primitive_status"]["atom_count"] == 24, "wrong atom count")
    require(packet["primitive_status"]["missing_atom_count"] == 24, "wrong missing atom count")
    require(packet["lambda12_status"]["lambda_12_closed"] is False, "lambda12 should remain open")
    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(STATUS in note and NEXT in note and "missing atoms = 24" in note, "note missing essentials")
    print("AUDIT_PASS: post-alpha primitive C1/lambda gate sharpened")


if __name__ == "__main__":
    main()
