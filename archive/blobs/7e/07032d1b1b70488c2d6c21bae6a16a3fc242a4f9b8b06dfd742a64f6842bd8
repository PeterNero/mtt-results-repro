"""Audit Selected_PhiFin_S2_Selected_Operator_and_Truncation_Source_Theorem_Attempt_v1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = (
    REPO
    / "certificates"
    / "selected_phifin_s2_selected_operator_and_truncation_source_theorem_attempt_certificate.json"
)
PACKET = (
    REPO
    / "candidate_data"
    / "selected_phifin_s2_selected_operator_and_truncation_source_theorem_attempt.candidate.json"
)
NOTE = (
    REPO
    / "proof_corpus"
    / "Selected_PhiFin_S2_Selected_Operator_and_Truncation_Source_Theorem_Attempt_v1.md"
)
SCRIPT = (
    REPO
    / "scripts"
    / "attempt_selected_phifin_s2_selected_operator_and_truncation_source_theorem.py"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(name: str, condition: bool, detail: object) -> bool:
    status = "PASS" if condition else "FAIL"
    print(f"{status}: {name} -- {detail}")
    return condition


def main() -> int:
    cert = load(CERT)
    packet = load(PACKET)
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    script_cert = json.loads(proc.stdout)
    trunc = packet["selected_truncation_status"]
    blockers = packet["blockers"]
    verdict = packet["verdict"]

    ok = True
    ok &= check(
        "certificate status",
        cert["status"] == "SELECTED_PHIFIN_S2_SELECTED_OPERATOR_TRUNCATION_THEOREM_ATTEMPT_BLOCKED",
        cert["status"],
    )
    ok &= check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    ok &= check(
        "attempt correctly not proved",
        packet["theorem_attempt"]["proved"] is False
        and verdict["selected_operator_truncation_theorem_proved"] is False
        and verdict["negative_result_proved"] is True,
        packet["theorem_attempt"],
    )
    ok &= check(
        "model gap retained but selected gap open",
        trunc["model_active_gamma_N"] > 0
        and trunc["model_active_epsilon_N"] == 0.0
        and trunc["model_active_gap_condition_passes"] is True
        and trunc["selected_gamma_N"] is None
        and trunc["selected_gap_condition_passes"] is False,
        trunc,
    )
    ok &= check(
        "I3 I4 I5 blockers present",
        blockers["I3_smooth_BN_convergence_and_truncation"]["current_artifact_says_open"] is True
        and blockers["I4_selected_D_E_action_and_source_flags"]["honest_D_E_promotes"] is False
        and blockers["I5_dotD_alpha1_source_and_C1_response"]["honest_dotD_promotes"] is False,
        blockers,
    )
    ok &= check(
        "minimal payload remains open",
        all(value == "OPEN" for value in packet["minimal_payload_to_close"].values()),
        packet["minimal_payload_to_close"],
    )
    ok &= check(
        "guardrails",
        cert["guardrails"]["does_not_relabel_model_active_as_selected"] is True
        and cert["guardrails"]["does_not_claim_selected_truncation_error"] is True
        and cert["guardrails"]["does_not_claim_honest_replay_passes"] is True,
        cert["guardrails"],
    )
    ok &= check(
        "note records no promotion",
        "cannot be promoted" in note
        and "full-minus-model norm bound" in note,
        NOTE,
    )

    print("\nSelected PhiFin S2 selected-operator/truncation theorem attempt audit")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
