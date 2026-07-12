"""Build the Qa/SU3 finite selected-connection solve packet attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
Q79_REPO = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

PREVIOUS = CERTS / "selected_qa_su3_twisted_section_basis_or_operator_exit_construction_certificate.json"
Q79_TEMPLATE = Q79_REPO / "certificates" / "iwasawa_route_c_residuals.template.json"
Q79_SMOKE_CERT = Q79_REPO / "certificates" / "iwasawa_route_c_branch_smoke_attempt_certificate.json"
Q79_CURRENT_RESIDUAL = (
    Q79_REPO
    / "candidate_data"
    / "iwasawa_route_c_branch_smoke"
    / "current_q79_orientation"
    / "route_c_residual.candidate.json"
)
Q79_CONJUGATE_RESIDUAL = (
    Q79_REPO
    / "candidate_data"
    / "iwasawa_route_c_branch_smoke"
    / "conjugate_q369_orientation"
    / "route_c_residual.candidate.json"
)
Q79_VALIDATOR = Q79_REPO / "scripts" / "validate_iwasawa_route_c_residuals.py"

OUTPUT_TEMPLATE = CERTS / "selected_qa_su3_finite_selected_connection_solve_packet.template.json"
OUTPUT_CERT = CERTS / "selected_qa_su3_finite_selected_connection_solve_packet_attempt_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(Q79_VALIDATOR), str(path)],
        cwd=Q79_REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return {
        "exit_code": proc.returncode,
        "output": [line for line in proc.stdout.strip().splitlines() if line],
    }


def make_template(q79_template: dict[str, Any]) -> dict[str, Any]:
    template = dict(q79_template)
    template["certificate"] = "SelectedQaSU3FiniteSelectedConnectionSolvePacketTemplate"
    template["status"] = "OPEN_SELECTED_QA_SU3_FINITE_SELECTED_CONNECTION_SOLVE_PACKET_REQUIRED"
    template["purpose"] = (
        "No-knob fill-in slot for the selected finite Route C connection solve "
        "that must promote the gerbe and curvature source into rho_E, D_E, "
        "Riesz, Green, dotD, and primitive C1 data."
    )
    template["source_requirements"] = {
        "same_branch_as_selected_gerbe": True,
        "q79_F_m1_or_conjugate_q369_Fstar_branch_packet": True,
        "selected_visible_SM_bundle_or_sheaf_model": None,
        "finite_rhoE_transition_data_not_identity_smoke": None,
        "selected_HYM_or_Strominger_residual_solution": None,
        "projector_retention_for_qutrit_matter_slots": None,
        "primitive_C1_contractions": None,
    }
    return template


def main() -> None:
    previous = load(PREVIOUS)
    q79_template = load(Q79_TEMPLATE)
    smoke = load(Q79_SMOKE_CERT)
    current_residual = load(Q79_CURRENT_RESIDUAL)
    conjugate_residual = load(Q79_CONJUGATE_RESIDUAL)
    current_validator = run_validator(Q79_CURRENT_RESIDUAL)
    conjugate_validator = run_validator(Q79_CONJUGATE_RESIDUAL)
    template = make_template(q79_template)

    honest_current_rejects_selection = (
        current_validator["exit_code"] == 1
        and any("selected_source_verified must be True" in line for line in current_validator["output"])
    )
    honest_conjugate_rejects_selection = (
        conjugate_validator["exit_code"] == 1
        and any("selected_source_verified must be True" in line for line in conjugate_validator["output"])
    )
    all_lifted_smoke_passes = all(smoke["calculation_results"]["lifted_selected_flags_all_validators_pass"].values())
    all_honest_unselected_rejected = all(
        branch["route_c_residual"] == 1
        and branch["de_action"] == 1
        and branch["riesz_gap"] == 1
        and branch["reduced_green"] == 1
        and branch["dotd_response"] == 1
        for branch in smoke["calculation_results"]["honest_unselected_validator_exit_codes"].values()
    )

    output = {
        "certificate": "SelectedQaSU3FiniteSelectedConnectionSolvePacketAttempt",
        "status": "QA_SU3_FINITE_SELECTED_CONNECTION_SOLVE_PACKET_ATTEMPT_BUILT_SELECTED_SOURCE_OPEN",
        "inputs": {
            "previous_gate": str(PREVIOUS.relative_to(ROOT)),
            "q79_route_c_template": str(Q79_TEMPLATE),
            "q79_route_c_validator": str(Q79_VALIDATOR),
            "q79_branch_smoke_attempt": str(Q79_SMOKE_CERT),
            "q79_current_residual_candidate": str(Q79_CURRENT_RESIDUAL),
            "q79_conjugate_residual_candidate": str(Q79_CONJUGATE_RESIDUAL),
        },
        "template_written": str(OUTPUT_TEMPLATE.relative_to(ROOT)),
        "branch_packets_available": {
            "current_q79_orientation": current_residual["branch_packet"],
            "conjugate_q369_orientation": conjugate_residual["branch_packet"],
        },
        "validator_results": {
            "current_q79_orientation_honest_unselected": current_validator,
            "conjugate_q369_orientation_honest_unselected": conjugate_validator,
        },
        "closed_now": {
            "finite_route_c_packet_schema": True,
            "branch_aware_residual_contract": True,
            "q79_and_conjugate_branch_packets_available": True,
            "honest_unselected_smoke_rejected_by_source_gate": honest_current_rejects_selection
            and honest_conjugate_rejects_selection
            and all_honest_unselected_rejected,
            "algebraic_downstream_validators_are_reachable_if_source_is_selected": all_lifted_smoke_passes,
        },
        "not_closed": {
            "selected_source_verified": current_residual["selected_source_verified"] is False,
            "selected_visible_SM_bundle_or_sheaf_model": True,
            "finite_rhoE_from_selected_bundle": True,
            "HYM_Strominger_residual_solve": True,
            "same_branch_D_E_dotD_Riesz_Green": True,
            "primitive_C1_contractions": True,
            "full_Qa_SU3_or_SM_closure": True,
        },
        "attempt_result": {
            "current_smoke_can_be_promoted": False,
            "current_smoke_useful_as_validator_fixture": True,
            "target_fitting_used": False,
            "uses_observed_masses_or_mixings": smoke["guardrails"]["uses_observed_masses_or_mixings"],
            "uses_execution_ii_benchmarks": smoke["guardrails"]["uses_execution_ii_benchmarks"],
            "next_gate_is_computation_not_reclassification": True,
        },
        "next_required_computation": {
            "name": "Selected_Qa_SU3_Finite_Selected_Connection_Source_Solve_v1",
            "must_output": [
                "selected visible SM bundle or sheaf model on q79/F,m=1, or the conjugate branch with antiunitary comparison",
                "finite rho_E transition data derived from that source",
                "Hermitian metric and HYM/Strominger residuals below tolerance",
                "positive MTT Hessian and positive Riesz gap",
                "sector D_E action matrices with selected_source_verified true",
                "Riesz projectors, reduced Green operators, and dotD_alpha1 responses",
                "primitive C1 contractions, still without observed flavor data",
            ],
        },
        "gate_result": {
            "selected_connection_packet_closed": False,
            "packet_template_ready": True,
            "proof_obligation_is_single_selected_source_solve": True,
            "no_false_closure": previous["gate_result"]["qa_su3_fully_closed"] is False,
        },
    }

    cert_text = json.dumps(output, indent=2, sort_keys=True)
    template_text = json.dumps(template, indent=2, sort_keys=True)
    if "--write-certificate" in sys.argv:
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_TEMPLATE.write_text(template_text + "\n", encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
