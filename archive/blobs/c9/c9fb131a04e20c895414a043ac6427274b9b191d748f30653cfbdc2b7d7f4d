"""Audit the executable same-source fusion packet attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "same_source_monad_gs_operator_fusion_attempt_certificate.json"
CANDIDATE = REPO / "candidate_data" / "same_source_monad_gs_operator_fusion_attempt.candidate.json"
PACKET = REPO / "candidate_data" / "same_source_monad_gs_operator_fusion.current_attempt.json"
NOTE = REPO / "proof_corpus" / "Same_Source_Monad_GS_Operator_Fusion_Attempt_v1.md"
SCRIPT = REPO / "scripts" / "attempt_same_source_monad_gs_operator_fusion_packet.py"
VALIDATOR = REPO / "scripts" / "validate_same_source_monad_gs_operator_fusion_packet.py"


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
    prefix = "same_source_monad_gs_operator_fusion_report="
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
    guardrails = cert["guardrails"]

    required_open_fragments = [
        "selected_by_mtt must be true",
        "same_source_for_ordered_L_pic0_GS_and_DE must be true",
        "source_lane_selector is not closed",
        "Pic0 resolution is not selected or quotiented",
        "visible_green_schwarz_row_derived_from_same_source must be true",
        "projector_retention_verified must be true",
        "route_c_residuals_pass must be true",
        "selected-source promotion validator did not pass",
    ]

    checks = [
        check(
            "certificate status",
            cert["status"]
            == "SAME_SOURCE_MONAD_GS_OPERATOR_FUSION_ATTEMPT_OPEN_SELECTED_SOURCE_MISSING",
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
            "packet has target arithmetic",
            packet["ordered_source"]["selected_L"] == [1, -2, 0]
            and packet["ordered_source"]["selected_L2"] == [2, -4, 0],
            packet["ordered_source"],
        ),
        check(
            "current packet is not selected",
            packet["source_identity"]["selected_by_mtt"] is False
            and packet["source_identity"]["same_source_for_ordered_L_pic0_GS_and_DE"] is False
            and packet["source_identity"]["fixture_only"] is True,
            packet["source_identity"],
        ),
        check(
            "open items include same-source blockers",
            all(any(fragment in item for item in open_items) for fragment in required_open_fragments),
            open_items[:25],
        ),
        check(
            "subvalidators executed",
            "ordered_source" in parsed["subvalidators"]
            and "selected_source_promotion" in parsed["subvalidators"]
            and parsed["subvalidators"]["ordered_source"]["exit_code"] == 2
            and parsed["subvalidators"]["selected_source_promotion"]["exit_code"] == 1,
            parsed["subvalidators"],
        ),
        check(
            "no overclaim",
            guardrails["claims_selected_source"] is False
            and guardrails["claims_pic0_resolved"] is False
            and guardrails["claims_D_E_dotD_constructed"] is False
            and guardrails["uses_lifted_flags_as_proof"] is False,
            guardrails,
        ),
        check(
            "note records executable attempt",
            "SameSourceMonadGSOperatorFusionPacket.v1" in note
            and "correctly refuses" in note
            and "Selected_Qa_SU3_Visible_SM_Bundle_Operator_Source_v1" in note,
            NOTE,
        ),
        check(
            "candidate matches certificate",
            candidate["attempt_packet"] == cert["attempt_packet"]
            and candidate["validator_result"] == cert["validator_result"],
            candidate["status"],
        ),
    ]

    print("\nSame-source monad/GS/operator fusion attempt audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
