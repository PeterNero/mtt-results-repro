"""Import the q79 time-oriented m=1 de_response target reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
Q79_REPO = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
Q79_CERTS = Q79_REPO / "certificates"
Q79_CANDIDATES = Q79_REPO / "candidate_data"
Q79_SCRIPTS = Q79_REPO / "scripts"

PREVIOUS = CERTS / "selected_qa_su3_symmetry_breaking_route_triage_certificate.json"
Q79_TARGET = Q79_CERTS / "time_oriented_m1_deresponse_target_certificate.json"
Q79_TARGET_CANDIDATE = Q79_CANDIDATES / "time_oriented_m1_deresponse_target.candidate.json"
Q79_DOTD_VALIDATOR = Q79_SCRIPTS / "validate_iwasawa_dotd_response.py"
Q79_Q79_DOTD = (
    Q79_CANDIDATES
    / "iwasawa_route_c_branch_smoke"
    / "current_q79_orientation"
    / "dotd_response.candidate.json"
)
Q79_Q369_DOTD = (
    Q79_CANDIDATES
    / "iwasawa_route_c_branch_smoke"
    / "conjugate_q369_orientation"
    / "dotd_response.candidate.json"
)

OUTPUT_CERT = CERTS / "selected_qa_su3_m1_deresponse_target_import_certificate.json"
OUTPUT_TEMPLATE = CERTS / "selected_qa_su3_m1_selected_source_origin.template.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(Q79_DOTD_VALIDATOR), str(path)],
        cwd=Q79_REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    failures = [
        line[2:]
        for line in proc.stdout.splitlines()
        if line.startswith("- ")
    ]
    return {
        "path": str(path),
        "exit_code": proc.returncode,
        "stdout_head": proc.stdout.splitlines()[:24],
        "failures": failures,
    }


def source_origin_template() -> dict[str, Any]:
    return {
        "schema": "SelectedQaSU3M1SelectedSourceOrigin.v1",
        "status": "OPEN_SELECTED_QA_SU3_M1_SELECTED_SOURCE_ORIGIN_REQUIRED",
        "purpose": (
            "Turn the coherent conditional m=1 de_response target into repo-level "
            "selected D_E/dotD/Riesz/Green proof data by supplying the genuine "
            "selected visible bundle or twisted-gerbe source origin."
        ),
        "must_supply": {
            "selected_visible_SM_bundle_or_twisted_source": None,
            "Freed_Witten_and_projector_retention": None,
            "full_Deligne_Cech_or_B_field_period_table": None,
            "repo_level_selected_D_E_files": None,
            "repo_level_selected_Riesz_Green_files": None,
            "repo_level_selected_dotD_alpha1_files": None,
            "selected_source_promotion_pass_report": None,
            "selected_HYM_or_Strominger_operator_source_pass_report": None,
            "Pic0_selection_or_quotient_rule": None,
            "primitive_C1_contraction_inputs": None,
        },
        "acceptance_tests": [
            "The selected source is not fixture-only and is selected before flavor data are evaluated.",
            "The selected source justifies selected_source_verified for Route-C residual, D_E, Riesz/gap, reduced Green, and dotD response packets.",
            "Every dotD slot has selected_dotD_source_verified and alpha1_driver_verified true for source reasons.",
            "Freed-Witten cancellation and projector retention are verified on the same branch.",
            "No observed CP sign, masses, CKM/PMNS entries, or benchmark flavor matrices are inputs.",
        ],
        "forbidden_shortcuts": [
            "Do not copy temporary lifted selected-source flags into repo data without a source certificate.",
            "Do not treat coherent validator shape as physical source selection.",
            "Do not select q=79 by observed CP sign.",
        ],
    }


def main() -> None:
    previous = load(PREVIOUS)
    target = load(Q79_TARGET)
    candidate = load(Q79_TARGET_CANDIDATE)
    q79_dotd = run_validator(Q79_Q79_DOTD)
    q369_dotd = run_validator(Q79_Q369_DOTD)
    template = source_origin_template()

    conditional = candidate["conditional_lifted_consistency_check"]
    current = candidate["current_honest_packets"]

    output = {
        "certificate": "SelectedQaSU3M1DeResponseTargetImport",
        "status": "QA_SU3_M1_DERESPONSE_TARGET_IMPORTED_SELECTED_SOURCE_ORIGIN_OPEN",
        "inputs": {
            "previous_route_triage": str(PREVIOUS.relative_to(ROOT)),
            "q79_m1_deresponse_target": str(Q79_TARGET),
            "q79_m1_deresponse_candidate": str(Q79_TARGET_CANDIDATE),
            "q79_dotd_smoke": str(Q79_Q79_DOTD),
            "q369_dotd_smoke": str(Q79_Q369_DOTD),
        },
        "closed_now": {
            "m1_representative_fixed": target["calculation_results"][
                "m1_representative_fixed"
            ],
            "de_response_is_right_next_gate_on_m1": target["what_this_closes"][
                "de_response_is_the_right_next_gate_on_m1"
            ],
            "finite_validator_stack_has_no_additional_algebraic_blocker": target[
                "what_this_closes"
            ]["finite_validator_stack_has_no_additional_algebraic_blocker"],
            "remaining_blocker_is_source_origin_not_matrix_shape": target[
                "what_this_closes"
            ]["remaining_blocker_is_source_origin_not_matrix_shape"],
            "conditional_lifted_hym_gate_passes": target["calculation_results"][
                "conditional_lifted_hym_gate_passes"
            ],
            "conditional_lifted_promotion_passes": target["calculation_results"][
                "conditional_lifted_promotion_passes"
            ],
            "honest_current_hym_source_fails_without_selected_source": target[
                "calculation_results"
            ]["honest_current_hym_source_fails"],
            "honest_current_promotion_fails_without_selected_source": target[
                "calculation_results"
            ]["honest_current_promotion_fails"],
        },
        "fixed_representative": target["fixed_representative_input"],
        "conditional_lifted_consistency": {
            "purpose": conditional["purpose"],
            "lifted_flags_are_not_written_as_proof_data": conditional[
                "lifted_flags_are_not_written_as_proof_data"
            ],
            "hym_operator_source_gate": conditional["hym_operator_source_gate"],
            "promotion_gate": conditional["promotion_gate"],
        },
        "current_honest_packet_failures": {
            "expected_to_fail_without_selected_source": current[
                "expected_to_fail_without_selected_source"
            ],
            "selected_hym_operator_source_attempt_exit_code": current[
                "selected_hym_operator_source_attempt"
            ]["exit_code"],
            "selected_source_promotion_attempt_exit_code": current[
                "selected_source_promotion_attempt"
            ]["exit_code"],
            "q79_dotd_response_validator": q79_dotd,
            "q369_dotd_response_validator": q369_dotd,
        },
        "not_closed": {
            "selected_visible_SM_bundle_or_twisted_source": target["still_open"][
                "actual_selected_visible_SM_bundle_or_twisted_source"
            ],
            "Freed_Witten_and_projector_retention": target["still_open"][
                "Freed_Witten_and_projector_retention"
            ],
            "full_Deligne_Cech_or_B_field_period_table": target["still_open"][
                "full_Deligne_Cech_or_B_field_period_table"
            ],
            "repo_level_selected_D_E_dotD_data": target["still_open"][
                "repo_level_selected_D_E_dotD_data"
            ],
            "selected_C1_primitive_contractions": target["still_open"][
                "selected_C1_primitive_contractions"
            ],
            "Yukawa_magnitudes_and_CKM_angles": target["still_open"][
                "Yukawa_magnitudes_and_CKM_angles"
            ],
            "full_SM_closure": target["still_open"]["full_SM_closure"],
        },
        "next_object": {
            "name": "Selected_Qa_SU3_M1_Selected_Source_Origin_v1",
            "template": str(OUTPUT_TEMPLATE.relative_to(ROOT)),
            "role": target["verdict"]["next_closing_object"],
        },
        "relation_to_route_triage": {
            "previous_status": previous["status"],
            "primary_route": previous["route_ranking"][0]["route"],
            "this_import_fills_primary_route_to_conditional_source_origin_gate": True,
        },
        "guardrails": {
            "claims_selected_source_constructed": False,
            "claims_repo_level_selected_D_E_dotD_data": False,
            "claims_lifted_flags_are_physical_proof": False,
            "claims_full_SM_closure": False,
            "uses_observed_cp_sign_or_flavor_data": False,
        },
        "honest_answer": target["verdict"]["honest_answer"],
    }

    cert_text = json.dumps(output, indent=2, sort_keys=True)
    if "--write-certificate" in sys.argv:
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_TEMPLATE.write_text(
            json.dumps(template, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print(cert_text)


if __name__ == "__main__":
    main()
