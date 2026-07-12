"""Audit Selected_dotD_alpha1_Source_Derivative_Payload_Attempt_v1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
SCRIPT = ROOT / "scripts" / "attempt_selected_dotd_alpha1_source_derivative_payload.py"
PACKET = DATA / "selected_dotd_alpha1_source_derivative_payload_attempt.candidate.json"
CERT = CERTS / "selected_dotd_alpha1_source_derivative_payload_attempt_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_dotD_alpha1_Source_Derivative_Payload_Attempt_v1.md"


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

    expected = "SELECTED_DOTD_ALPHA1_SOURCE_DERIVATIVE_PAYLOAD_ATTEMPT_BUILT_SOURCE_TANGENT_OPEN"
    check("certificate status", cert["status"] == expected, cert["status"])
    check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    check("theorem not overclaimed", cert["theorem"]["proved"] is False, cert["theorem"])

    checks = packet["derivative_payload_checks"]
    check(
        "available prefix retained",
        checks["D0_locked_basis_and_D_E_gap_available"]
        and checks["D1_same_basis_dotD_values_available"]
        and checks["D2_diagnostic_horizontal_response_available"]
        and checks["D3_source_level_projective_support_available"],
        checks,
    )
    check(
        "selected derivative requirements remain open",
        checks["D4_operator_level_selected_projector_retention_for_dotD"] is False
        and checks["D5_selected_alpha1_tangent_parameter"] is False
        and checks["D6_retarded_overlap_derivative_formula"] is False
        and checks["D7_sector_equality_from_selected_derivative_to_dotD_matrices"] is False
        and checks["D8_honest_dotD_replay_without_lifted_flags"] is False,
        checks,
    )

    audit = packet["external_source_audit"]
    check(
        "source-origin reduction only",
        audit["source_origin_reduction"]["reduced_to_selected_phifin_alpha1_payload"]
        and audit["source_origin_reduction"]["same_branch_dotD_alpha1_derivative_open"],
        audit["source_origin_reduction"],
    )
    check(
        "alpha1 payload support is not selected payload",
        audit["alpha1_payload_attempt"]["dotD_support_present"]
        and audit["alpha1_payload_attempt"]["dotD_selected_payload_flag"] is False
        and audit["alpha1_payload_attempt"][
            "finite_hessian_c1_selected_payload_flag"
        ]
        is False
        and audit["alpha1_payload_attempt"][
            "operator_level_projective_rhoE_promoted"
        ]
        is False,
        audit["alpha1_payload_attempt"],
    )
    check(
        "operator identity remains source-level",
        audit["operator_identity_subpacket"]["source_level_not_operator_level"]
        and audit["operator_identity_subpacket"]["closure_claimed"] is False
        and audit["operator_identity_subpacket"][
            "selected_visible_operator_source_closed"
        ]
        is False
        and audit["operator_identity_subpacket"][
            "actual_selected_dotD_alpha1_operator_open"
        ],
        audit["operator_identity_subpacket"],
    )
    check(
        "matter-slot/operator packets are contracts or no-go scaffolds",
        audit["same_source_matter_slot_packet"]["closure_claimed"] is False
        and audit["same_source_matter_slot_packet"][
            "selected_DE_dotD_Riesz_Green_values_open"
        ]
        and audit["same_source_operatorpacket_fill_or_nogo"][
            "current_scaffolds_support_only"
        ]
        and audit["same_source_operatorpacket_fill_or_nogo"]["closure_claimed"]
        is False,
        {
            "matter": audit["same_source_matter_slot_packet"],
            "nogo": audit["same_source_operatorpacket_fill_or_nogo"],
        },
    )
    check(
        "dotD honest replay remains source-gated",
        audit["dotD_honest_replay"]["same_basis_matrix_emitted"]
        and audit["dotD_honest_replay"][
            "honest_fails_only_by_source_driver_flags"
        ]
        and audit["dotD_honest_replay"]["honest_replay_without_lifted_flags_open"],
        audit["dotD_honest_replay"],
    )
    check(
        "classification is honest",
        packet["classification"]["not_missing_finite_values"]
        and packet["classification"]["missing_selected_tangent_object"]
        and packet["classification"]["missing_variational_identity"]
        and packet["classification"]["missing_honest_replay_without_lift"],
        packet["classification"],
    )
    check(
        "next artifact narrowed",
        cert["minimal_closure_contract"]["name"]
        == "Selected_alpha1_Tangent_or_Retarded_Overlap_Kernel_v1"
        and "retarded-overlap derivative formula d/d alpha1 Phi_fin(alpha1)|selected"
        in cert["minimal_closure_contract"]["must_emit"],
        cert["minimal_closure_contract"],
    )
    check(
        "guardrails retained",
        cert["guardrails"]["does_not_promote_dotD_flags"]
        and cert["guardrails"]["does_not_use_diagnostic_lift_as_proof"]
        and cert["guardrails"]["does_not_treat_support_level_gerbe_as_operator_derivative"]
        and cert["guardrails"]["does_not_claim_alpha1_driver"]
        and cert["guardrails"]["does_not_claim_C1_or_b_selected"]
        and cert["guardrails"]["does_not_claim_Yukawa_or_SM_closure"],
        cert["guardrails"],
    )
    note = NOTE.read_text(encoding="utf-8")
    check("note records retarded-overlap gap", "retarded-overlap derivative" in note, NOTE)

    print("\nSelected dotD alpha1 source derivative payload attempt audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
