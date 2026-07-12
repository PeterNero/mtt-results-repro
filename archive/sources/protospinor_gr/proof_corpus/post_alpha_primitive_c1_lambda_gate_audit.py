from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_primitive_c1_lambda_gate_certificate.json"
STATUS = "POST_ALPHA_PRIMITIVE_C1_LAMBDA_GATE_BUILT_VALUES_OPEN"
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
    require(cert["primitive_C1_contractions_closed"] is False, "primitive C1 should remain open")
    require(cert["missing_atom_count"] == 24, "wrong missing atom count")
    require(cert["lambda12_computable"] is False, "lambda12 should remain open")
    require(all(cert["checks"].values()), "all checks should pass")
    require(packet["theorem"]["proved"] is True, "theorem should prove gate")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(packet["primitive_status"]["missing_atom_count"] == 24, "primitive status mismatch")
    require(packet["lambda12_status"]["lambda_12_computable_from_this_gate"] is False, "lambda12 overclaimed")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(STATUS in note and NEXT in note and "0 / 24" in note, "note missing essentials")
    print("AUDIT_PASS: primitive C1/lambda gate imported; 24 atoms and lambda12 remain open")


if __name__ == "__main__":
    main()
