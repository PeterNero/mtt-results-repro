"""Audit Selected_PhiFin_S2_Value_Emission_with_Gap_Error_and_Honest_Replay_v1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = (
    REPO
    / "certificates"
    / "selected_phifin_s2_value_emission_with_gap_error_honest_replay_certificate.json"
)
PACKET = (
    REPO
    / "candidate_data"
    / "selected_phifin_s2_value_emission_with_gap_error_honest_replay.candidate.json"
)
NOTE = (
    REPO
    / "proof_corpus"
    / "Selected_PhiFin_S2_Value_Emission_with_Gap_Error_and_Honest_Replay_v1.md"
)
SCRIPT = REPO / "scripts" / "build_selected_phifin_s2_value_emission_with_gap_error_honest_replay.py"


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
    payload = packet["same_basis_value_payload"]
    gap = packet["gap_error_replay"]
    replay = packet["honest_replay"]
    criterion = packet["criterion_evaluation"]

    ok = True
    ok &= check(
        "certificate status",
        cert["status"]
        == "SELECTED_PHIFIN_S2_VALUE_EMISSION_REPLAY_BUILT_BLOCKED_BY_SELECTED_PROVENANCE",
        cert["status"],
    )
    ok &= check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    ok &= check(
        "same 27-mode basis",
        payload["basis_id"] == "F3xF3_gerbe_twisted_fourier_N1_rank3"
        and payload["basis_dimension"] == 27
        and payload["zero_cluster_dimension"] == 3,
        payload,
    )
    ok &= check(
        "D_E and dotD values located",
        payload["D_E_slots"]["Q"]["D_E_matrix_shape"] == [24, 27]
        and payload["D_E_slots"]["H"]["D_E_matrix_shape"] == [26, 27]
        and payload["dotD_alpha1_slots"]["Q"]["dotD_alpha1_matrix_shape"] == [27, 27]
        and payload["sector_projector_ranks"]["Q"] == 3.0,
        {
            "D_E_Q": payload["D_E_slots"]["Q"],
            "dotD_Q": payload["dotD_alpha1_slots"]["Q"],
        },
    )
    ok &= check(
        "model-active gap recorded but not selected",
        gap["model_active_gap_gamma_N"] > 0
        and gap["model_active_residual_epsilon_N"] == 0.0
        and gap["model_active_epsilon_below_gap"] is True
        and gap["selected_gap_error_certificate_emitted"] is False,
        gap,
    )
    ok &= check(
        "honest replay cutset",
        replay["D_E_fails_only_by_source_flags"] is True
        and replay["dotD_fails_only_by_source_driver_flags"] is True
        and replay["honest_replay_without_lifted_flags_passes"] is False,
        replay,
    )
    ok &= check(
        "criterion remains blocked",
        criterion["actual_D_E_matrix_entries_emitted"] is True
        and criterion["actual_dotD_alpha1_entries_emitted"] is True
        and criterion["selected_positive_gap_gamma_N_emitted"] is False
        and criterion["honest_validator_replay_without_lifted_flags"] is False
        and criterion["selected_source_promotion_allowed_by_criterion"] is False,
        criterion,
    )
    ok &= check(
        "guardrails",
        cert["guardrails"]["does_not_claim_selected_S2_value_emission"] is True
        and cert["guardrails"]["does_not_claim_full_selected_gap_error"] is True
        and cert["guardrails"]["diagnostic_lift_not_used_as_proof"] is True,
        cert["guardrails"],
    )
    ok &= check(
        "note records next theorem",
        "Selected_PhiFin_S2_Selected_Operator_and_Truncation_Source_Theorem_v1" in note
        and "diagnostic lift" in note,
        NOTE,
    )

    print("\nSelected PhiFin S2 value-emission replay audit")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
