from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "alpha1_source_strength_normalization_gate_certificate.json"
STATUS = "ALPHA1_SOURCE_STRENGTH_NORMALIZATION_GATE_REDUCED_SOURCEIDENTITY_OR_RETARDED_KERNEL_OPEN"
NEXT = "MTT_Selected_SameSource_Alpha1_Normalization_SourceIdentity_or_RetardedKernel_Value_v1"


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
    require(packet["conditional_value_candidate"]["lambda_alpha1_candidate"] == 1.0, "lambda candidate should be one")
    require(packet["fill_summary"]["candidate_values_filled"] == packet["fill_summary"]["required_fields"], "not all candidate fields filled")
    require(packet["fill_summary"]["selected_emitted_fields"] == 0, "selected fields should remain zero")
    require(packet["validator_report"]["ok"] is False, "validator should fail honestly")
    require(packet["validator_report"]["exit_code"] == 1, "validator exit code should be one")
    for field in [
        "source_identity",
        "source_strength_coordinate",
        "normalization_functional",
        "tangent_equality",
        "sector_dotd_equality",
    ]:
        require(field in packet["failed_fields"], f"missing failed field {field}")
    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(STATUS in note and NEXT in note and "lambda_alpha1 candidate = 1" in note, "note missing essentials")
    print("AUDIT_PASS: alpha1 source-strength normalization gate reduced; selected value remains open")


if __name__ == "__main__":
    main()
