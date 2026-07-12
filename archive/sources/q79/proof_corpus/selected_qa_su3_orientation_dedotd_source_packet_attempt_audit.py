"""Audit the selected Qa/SU3 orientation D_E/dotD source packet attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_orientation_dedotd_source_attempt_certificate.json"
CANDIDATE = REPO / "candidate_data" / "selected_qa_su3_orientation_dedotd_source_attempt.candidate.json"
PACKET = REPO / "candidate_data" / "selected_qa_su3_orientation_dedotd_source.current_attempt.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Orientation_DEDotD_Source_Packet_Attempt_v1.md"
SCRIPT = REPO / "scripts" / "attempt_selected_qa_su3_orientation_dedotd_source_packet.py"
VALIDATOR = REPO / "scripts" / "validate_selected_qa_su3_orientation_dedotd_source_packet.py"


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
    prefix = "selected_qa_su3_orientation_dedotd_source_report="
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
    calc = cert["calculation_results"]
    guardrails = cert["guardrails"]

    required_open = [
        "selected_by_mtt must be true",
        "visible_bundle_or_twisted_gerbe_source must be true",
        "pic0_selected_or_quotiented must be true",
        "freed_witten_and_projector_retention must be true",
        "selection_justified_by_source must be true",
        "same_branch_derivative_verified must be true",
        "selected_D_E_action validator did not pass",
        "selected_reduced_green validator did not pass",
        "selected_dotD_alpha1 validator did not pass",
    ]

    checks = [
        check(
            "certificate status",
            cert["status"] == "SELECTED_QA_SU3_ORIENTATION_DEDOTD_SOURCE_ATTEMPT_OPEN_SOURCE_FLAGS",
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
            "current packet is q79 conditional branch",
            packet["branch_selection"]["selected_torsion_label_m"] == 1
            and packet["branch_selection"]["global_cp_label"] == 79
            and packet["branch_selection"]["selection_justified_by_source"] is False,
            packet["branch_selection"],
        ),
        check(
            "finite paths are wired into validators",
            packet["operator_data"]["selected_D_E_action"].endswith("de_action.candidate.json")
            and packet["operator_data"]["selected_reduced_green"].endswith("reduced_green.candidate.json")
            and packet["operator_data"]["selected_dotD_alpha1"].endswith("dotd_response.candidate.json")
            and set(subvalidators) == {
                "selected_D_E_action",
                "selected_reduced_green",
                "selected_dotD_alpha1",
            },
            packet["operator_data"],
        ),
        check(
            "both conjugate branch packets checked",
            calc["both_branch_packets_exist"] is True
            and calc["q79_finite_equations_blocked_only_by_source_flags"] is True
            and calc["q369_finite_equations_blocked_only_by_source_flags"] is True,
            calc,
        ),
        check(
            "open items include intended blockers",
            all(any(fragment in item for item in open_items) for fragment in required_open),
            open_items,
        ),
        check(
            "subvalidators fail only at source layer",
            cert["subvalidator_exit_codes"] == {
                "selected_D_E_action": 1,
                "selected_dotD_alpha1": 1,
                "selected_reduced_green": 1,
            }
            and any(
                "selected_source_verified is not true" in line
                for line in subvalidators["selected_D_E_action"]["output_head"]
            )
            and any(
                "selected_dotD_source_verified is not true" in line
                for line in subvalidators["selected_dotD_alpha1"]["output_head"]
            ),
            subvalidators,
        ),
        check(
            "no overclaim",
            guardrails["claims_selected_source_origin"] is False
            and guardrails["claims_unique_m_label_now"] is False
            and guardrails["claims_selected_D_E_or_dotD"] is False
            and guardrails["uses_observed_cp_sign_or_masses"] is False
            and guardrails["claims_full_sm_closure"] is False,
            guardrails,
        ),
        check(
            "note records frontier",
            "orientation-carrying source gate is now executable" in note
            and "remaining blocker is not the finite matrix shape" in note
            and "selected_source_verified" in note
            and "SelectedQaSU3OrientationCarryingDEDotDSource.v1" in note,
            NOTE,
        ),
        check(
            "candidate matches certificate",
            candidate["attempt_packet"] == cert["attempt_packet"]
            and candidate["validator_result"] == cert["validator_result"],
            candidate["status"],
        ),
    ]

    print("\nSelected Qa/SU3 orientation D_E/dotD source packet attempt audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
