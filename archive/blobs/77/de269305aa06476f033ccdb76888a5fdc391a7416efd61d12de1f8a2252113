"""Audit Selected_PhiFin_S2_Source_Promotion_Criterion_v1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_phifin_s2_source_promotion_criterion_certificate.json"
PACKET = REPO / "candidate_data" / "selected_phifin_s2_source_promotion_criterion.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_PhiFin_S2_Source_Promotion_Criterion_v1.md"
SCRIPT = REPO / "scripts" / "prove_selected_phifin_s2_source_promotion_criterion.py"


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
    evaluation = packet["current_branch_evaluation"]
    payload = packet["necessary_and_sufficient_payload_for_promotion"]

    ok = True
    ok &= check(
        "certificate status",
        cert["status"] == "SELECTED_PHIFIN_S2_SOURCE_PROMOTION_CRITERION_PROVED_VALUES_OPEN",
        cert["status"],
    )
    ok &= check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    ok &= check(
        "criterion proved",
        packet["criterion"]["proved"] is True
        and cert["what_closes_now"]["S2_source_promotion_criterion_proved"] is True,
        packet["criterion"],
    )
    ok &= check(
        "current scaffold support retained",
        evaluation["fixed_selected_smooth_source_available"] is True
        and evaluation["abstract_finite_trace_existence_available"] is True
        and evaluation["S1_projective_rhoE_trace_filled"] is True
        and evaluation["S2_same_basis_scaffold_available"] is True,
        evaluation,
    )
    ok &= check(
        "promotion rejected now",
        packet["verdict"]["source_promotion_now_allowed"] is False
        and evaluation["S2_D_E_selected_source_verified"] is False
        and evaluation["S2_dotD_selected_source_verified"] is False
        and evaluation["S2_dotD_alpha1_driver_verified"] is False
        and evaluation["selected_gap_error_certificate_emitted"] is False,
        packet["verdict"],
    )
    ok &= check(
        "payload criterion requires real values",
        payload["actual_D_E_matrix_entries_emitted"] is True
        and payload["actual_Riesz_projector_entries_emitted"] is True
        and payload["actual_reduced_Green_entries_emitted"] is True
        and payload["actual_dotD_alpha1_entries_emitted"] is True
        and payload["honest_validator_replay_without_lifted_flags"] is True,
        payload,
    )
    ok &= check(
        "guardrails",
        cert["guardrails"]["does_not_promote_lifted_flags"] is True
        and cert["guardrails"]["does_not_claim_selected_D_E_values_emitted"] is True
        and cert["guardrails"]["does_not_claim_selected_gap_error_emitted"] is True
        and cert["guardrails"]["does_not_use_observed_or_benchmark_inputs"] is True,
        cert["guardrails"],
    )
    ok &= check(
        "note records next gate",
        "Selected_PhiFin_S2_Value_Emission_with_Gap_Error_and_Honest_Replay_v1" in note
        and "manual flag choice" in note,
        NOTE,
    )

    print("\nSelected PhiFin S2 source-promotion criterion audit")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
