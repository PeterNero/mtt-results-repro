from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "alpha1_partial_sourceidentity_closure_theorem_certificate.json"
STATUS = "ALPHA1_SOURCEIDENTITY_CLOSED_NORMALIZATION_OR_TYPED_DERIVATIVE_OPEN"
NEXT = "MTT_Selected_SourceStrengthCoordinate_or_TypedBNRetardedDerivative_Theorem_v1"


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
    source_identity = packet["closed_field"]["source_identity"]
    require(source_identity["selected_emitted"] is True, "source identity should be selected")
    require(source_identity["theorem_derived"] is True, "source identity should be theorem-derived")
    require(source_identity["same_source"] is True, "source identity should be same-source")
    tangent = packet["theorem_derived_but_not_selected"]["tangent_equality"]
    require(tangent["theorem_derived"] is True, "tangent should be theorem-derived")
    require(tangent["selected_emitted"] is False, "tangent must not be selected physical coordinate yet")
    require(tangent["residual_l2"] <= tangent["tolerance"], "tangent residual too large")
    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(STATUS in note and NEXT in note and "source_identity = selected" in note, "note missing essentials")
    print("AUDIT_PASS: alpha1 source identity closed; normalization or typed derivative remains open")


if __name__ == "__main__":
    main()
