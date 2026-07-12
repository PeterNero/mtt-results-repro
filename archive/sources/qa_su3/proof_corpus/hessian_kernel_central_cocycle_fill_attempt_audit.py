"""Audit the Hessian/kernel central-cocycle fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "hessian_kernel_central_cocycle_fill_attempt_certificate.json"
DATA = REPO / "candidate_data" / "hessian_kernel_central_cocycle_fill_attempt.candidate.json"
PACKET = REPO / "candidate_data" / "hessian_kernel_central_cocycle_fill_attempt.current_packet.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Hessian_Kernel_Central_Cocycle_Fill_Attempt_v1.md"
SCRIPT = REPO / "scripts" / "attempt_fill_hessian_kernel_central_cocycle_derivation.py"
VALIDATOR = REPO / "scripts" / "validate_hessian_kernel_central_cocycle_derivation.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    val = subprocess.run(
        [sys.executable, str(VALIDATOR), str(PACKET)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    fill = data["fill_result"]
    twists = packet["tau_extraction"]["module_twist_values"]
    checks = [
        check("status", cert["status"] == "QA_SU3_HESSIAN_KERNEL_CENTRAL_COCYCLE_FILL_ATTEMPT_PARTIAL_TAU_BLOCKED_SELECTED_HESSIAN_KERNEL", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("validator refuses current packet", val.returncode == 2 and data["attempt_packet_validator_result"]["exit_code"] == 2, val.stdout),
        check("tau labels filled", fill["module_tau_labels_filled_from_c_charge"] is True and twists["F1"] == 1 and twists["G1"] == -1 and twists["P"] == 0, twists),
        check("all twists cancel", fill["tau_twist_cancellation_passes"] is True and all(twists[f"F{i}"] + twists[f"G{i}"] == 0 for i in range(1, 6)), twists),
        check("Pi rule is algebraic only", fill["algebraic_Pi_tw_rule_filled"] is True and "not derived" in packet["twist_projection"]["Pi_tw_matrix_or_rule"], packet["twist_projection"]),
        check("H/G values open", fill["selected_Qa_SU3_H_sel_matrix_found"] is False and fill["selected_Qa_SU3_G_ret_found"] is False, fill),
        check("tau not extracted from H/G", fill["tau_extracted_from_H_sel_G_ret"] is False and packet["tau_extraction"]["period_selected_by_H_sel_G_ret"] is False, packet["tau_extraction"]),
        check("q79 guardrail only", fill["q79_s3_guardrail_source_packet_closed"] is True and fill["q79_z64_hessian_kernel_guardrail_closed"] is True and packet["guardrails"]["no_q79_direct_import"] is True, fill),
        check("response open", fill["same_source_response_payload_filled"] is False and all(value is None for value in packet["response_payload"].values()), packet["response_payload"]),
        check("no closure", cert["closure_claimed"] is False and fill["qa_su3_packet_closed"] is False and fill["validator_passed"] is False, fill),
        check("no target fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False and packet["guardrails"]["no_target_fitting"] is True, packet["guardrails"]),
        check("note records next", data["next_required_artifact"] in note and "H_sel/G_ret" in note, NOTE),
    ]
    print("\nSelected Qa/SU3 Hessian/kernel central-cocycle fill attempt audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
