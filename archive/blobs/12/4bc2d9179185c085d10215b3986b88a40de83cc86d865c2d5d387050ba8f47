"""Audit the selected Qa/SU3 same-source V_alpha/S3 packet attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_same_source_valpha_s3_operator_packet_attempt_certificate.json"
CANDIDATE = REPO / "candidate_data" / "selected_qa_su3_same_source_valpha_s3_operator_packet_attempt.candidate.json"
PACKET = REPO / "candidate_data" / "selected_qa_su3_same_source_valpha_s3_operator_packet.current_attempt.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Same_Source_VAlpha_S3_Operator_Packet_Attempt_v1.md"
SCRIPT = REPO / "scripts" / "attempt_selected_qa_su3_same_source_valpha_s3_operator_packet.py"
VALIDATOR = REPO / "scripts" / "validate_selected_qa_su3_same_source_valpha_s3_operator_packet.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def run_attempt() -> dict:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    return json.loads(proc.stdout)


def run_validator() -> dict:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(PACKET)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    prefix = "selected_qa_su3_same_source_valpha_s3_report="
    parsed = None
    for line in proc.stdout.splitlines():
        if line.startswith(prefix):
            parsed = json.loads(line[len(prefix) :])
            break
    return {"exit_code": proc.returncode, "parsed_report": parsed, "stdout": proc.stdout}


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    candidate = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    computed = run_attempt()
    validation = run_validator()
    note = NOTE.read_text(encoding="utf-8")

    parsed = cert["validator_result"]["parsed_report"]
    open_items = parsed["open_items"]
    subvalidators = parsed["subvalidators"]
    guardrails = cert["guardrails"]

    required_fragments = [
        "selected_by_mtt must be true",
        "same_source_valpha_s3_operator must be true",
        "terminal_monad_difference_L3_minus_K2_selector_closed must be true",
        "nonzero_ext_class_selected must be true",
        "Pic0 resolution is not selected or quotiented",
        "same_source_link_valpha_to_s3_proved must be true",
        "chern_weil_row_derived_from_same_source must be true",
        "visible GS source validator did not pass",
        "selected-source promotion validator did not pass",
    ]

    checks = [
        check(
            "certificate status",
            cert["status"] == "SELECTED_QA_SU3_SAME_SOURCE_VALPHA_S3_OPERATOR_PACKET_ATTEMPT_OPEN",
            cert["status"],
        ),
        check(
            "attempt recomputes same result",
            computed["validator_result"]["exit_code"] == cert["validator_result"]["exit_code"]
            and computed["first_open_items"] == cert["first_open_items"],
            computed["status"],
        ),
        check(
            "validator returns open",
            validation["exit_code"] == 2
            and validation["parsed_report"]["status"] == "OPEN"
            and parsed["status"] == "OPEN",
            validation,
        ),
        check(
            "packet carries target V_alpha arithmetic",
            packet["source_skeleton"]["selected_L"] == [1, -2, 0]
            and packet["source_skeleton"]["selected_L2"] == [2, -4, 0]
            and packet["source_skeleton"]["c2_valpha"] == [4, 0, 0],
            packet["source_skeleton"],
        ),
        check(
            "closed S3 support is consumed",
            packet["same_source_merge"]["selected_s3_green_schwarz_visible_support"] is True
            and packet["same_source_merge"]["block_projector_retention_closed"] is True
            and subvalidators["s3_class_restriction"]["exit_code"] == 0,
            packet["same_source_merge"],
        ),
        check(
            "same-source link remains open",
            packet["source_identity"]["same_source_valpha_s3_operator"] is False
            and packet["same_source_merge"]["same_source_link_valpha_to_s3_proved"] is False,
            packet["source_identity"],
        ),
        check(
            "open items include intended blockers",
            all(any(fragment in item for item in open_items) for fragment in required_fragments),
            open_items[:30],
        ),
        check(
            "operator subvalidators keep blocking",
            subvalidators["ordered_source"]["exit_code"] == 2
            and subvalidators["visible_green_schwarz_source"]["exit_code"] == 1
            and subvalidators["selected_source_promotion"]["exit_code"] == 1,
            subvalidators,
        ),
        check(
            "no overclaim",
            guardrails["claims_same_source_binding"] is False
            and guardrails["claims_selected_visible_valpha_source"] is False
            and guardrails["claims_selected_operator_execution"] is False
            and guardrails["uses_observed_flavor_data"] is False,
            guardrails,
        ),
        check(
            "note records current frontier",
            "SelectedQaSU3SameSourceVAlphaS3OperatorPacket.v1" in note
            and "side is genuinely closed" in note
            and "S3" in note
            and "side is not yet selected" in note
            and "V_alpha" in note,
            NOTE,
        ),
        check(
            "candidate matches certificate",
            candidate["attempt_packet"] == cert["attempt_packet"]
            and candidate["validator_result"] == cert["validator_result"],
            candidate["status"],
        ),
    ]

    print("\nSelected Qa/SU3 same-source V_alpha/S3 packet attempt audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
