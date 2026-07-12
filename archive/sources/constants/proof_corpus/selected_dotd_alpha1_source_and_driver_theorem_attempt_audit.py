"""Audit Selected_dotD_alpha1_Source_and_Driver_Theorem_Attempt_v1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
SCRIPT = ROOT / "scripts" / "attempt_selected_dotd_alpha1_source_and_driver_theorem.py"
PACKET = DATA / "selected_dotd_alpha1_source_and_driver_theorem_attempt.candidate.json"
CERT = CERTS / "selected_dotd_alpha1_source_and_driver_theorem_attempt_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_dotD_alpha1_Source_and_Driver_Theorem_Attempt_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(label: str, condition: bool, detail: object) -> None:
    status = "PASS" if condition else "FAIL"
    print(f"{status}: {label} -- {detail}")
    if not condition:
        raise SystemExit(1)


def main() -> int:
    packet = load(PACKET)
    cert = load(CERT)
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    check("script runs", proc.returncode == 0, proc.stdout)
    script_cert = json.loads(proc.stdout)

    expected = "SELECTED_DOTD_ALPHA1_SOURCE_AND_DRIVER_THEOREM_NOT_PROVED_CRITERION_SHARPENED"
    check("certificate status", cert["status"] == expected, cert["status"])
    check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    check("theorem not overclaimed", cert["theorem"]["proved"] is False, cert["theorem"])

    req = packet["requirements"]
    check(
        "closed prefix requirements",
        req["R0_selected_D_E_gap_layer"]
        and req["R1_selected_projective_rhoE_trace"]
        and req["R2_same_basis_dotD_value_packet"],
        req,
    )
    check(
        "remaining requirements open",
        req["R3_operator_level_projector_retention_for_dotD"] is False
        and req["R4_selected_alpha1_deformation_parameter"] is False
        and req["R5_retarded_overlap_derivative_source"] is False
        and req["R6_honest_dotD_replay_without_lifted_flags"] is False,
        req,
    )
    support = packet["current_support"]
    check(
        "diagnostic support not proof",
        support["honest_dotD_replay"]["diagnostic_lift_validator_passes"]
        and support["honest_dotD_replay"]["fails_only_by_source_driver_flags"]
        and support["honest_dotD_replay"]["closure_claimed"] is False,
        support["honest_dotD_replay"],
    )
    check(
        "operator source remains open",
        support["operator_identity_subpacket"]["source_level_support_only"]
        and support["operator_identity_subpacket"]["subpacket_closed"] is False
        and support["operator_identity_subpacket"]["operator_level_projective_rhoE_still_open"],
        support["operator_identity_subpacket"],
    )
    check(
        "obstruction exact",
        packet["obstruction"]["not_a_shape_problem"]
        and packet["obstruction"]["not_a_gap_problem"]
        and "alpha1 deformation" in packet["obstruction"]["why_D_E_lock_does_not_imply_dotD"],
        packet["obstruction"],
    )
    check(
        "next payload exact",
        cert["sufficient_next_payload"]["name"]
        == "Selected_dotD_alpha1_Source_Derivative_Payload_v1"
        and "retarded overlap derivative or equivalent variational formula"
        in cert["sufficient_next_payload"]["must_supply"],
        cert["sufficient_next_payload"],
    )
    check(
        "guardrails retained",
        cert["guardrails"]["does_not_promote_dotD_flags"]
        and cert["guardrails"]["does_not_use_diagnostic_lift_as_proof"]
        and cert["guardrails"]["does_not_claim_alpha1_driver"]
        and cert["guardrails"]["does_not_claim_A_selected_or_b_selected"]
        and cert["guardrails"]["does_not_claim_Yukawa_or_SM_closure"]
        and cert["guardrails"]["does_not_use_observed_or_benchmark_inputs"],
        cert["guardrails"],
    )
    note = NOTE.read_text(encoding="utf-8")
    check("note records obstruction", "alpha1 tangent/driver" in note, NOTE)

    print("\nSelected dotD alpha1 source and driver theorem attempt audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
