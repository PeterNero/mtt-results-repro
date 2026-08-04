"""Build the U1/Y Route-C dotD/alpha1/C1 response emission gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
TEXPAPERS = ROOT.parent
Q79 = TEXPAPERS / "mtt-q79-proof-repro"
NONSM = TEXPAPERS / "mtt-nonsm-constants-no-knob"
PROTOSPINOR = TEXPAPERS / "mtt-protospinor-gr-response-proof"

INPUTS = {
    "u1y_trace_equals_27mode_gate": DATA / "selected_u1y_routec_trace_equals_27mode_or_full_hym_replay.candidate.json",
    "q79_dotd_alpha1_c1_response": Q79 / "certificates" / "q79_selected_dotd_alpha1_c1_response_emission_certificate.json",
    "q79_de_green_dotd_source": Q79 / "certificates" / "q79_selected_de_green_dotd_source_for_primitive_c1_certificate.json",
    "q79_phifin_alpha1_payload": Q79 / "certificates" / "q79_selected_phifin_alpha1_payload_certificate.json",
    "nonsm_phifin_dotd_alpha1_c1": NONSM / "certificates" / "selected_phifin_dotd_alpha1_c1_response_emission_attempt_certificate.json",
    "nonsm_dotd_alpha1_source_driver": NONSM / "certificates" / "selected_dotd_alpha1_source_and_driver_theorem_attempt_certificate.json",
    "nonsm_alpha1_tangent_or_retarded_kernel": NONSM / "certificates" / "selected_alpha1_tangent_or_retarded_overlap_kernel_attempt_certificate.json",
    "nonsm_c1_response_audit": NONSM / "certificates" / "selected_c1_response_operator_emission_audit_import_certificate.json",
    "protospinor_c1_response": PROTOSPINOR / "certificates" / "routec_selected_c1_response_operator_emission_import_certificate.json",
    "protospinor_basis_transport": PROTOSPINOR / "certificates" / "routec_basis_transport_proof_or_counterexample_import_certificate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_dotd_alpha1_c1_response_emission.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_dotd_alpha1_c1_response_emission_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_dotD_Alpha1_C1_Response_Emission_v1.md"

STATUS = "U1Y_ROUTEC_DOTD_ALPHA1_C1_RESPONSE_REDUCED_TANGENT_OPEN"
NEXT = "Selected_U1Y_RouteC_Alpha1_Tangent_or_RetardedOverlap_Kernel_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def read_optional(path: Path) -> dict[str, Any]:
    if path.exists():
        return load(path)
    return {"present": False, "status": "MISSING"}


def status_of(key: str, data: dict[str, Any]) -> dict[str, Any]:
    return {
        "path": rel(INPUTS[key]),
        "present": INPUTS[key].exists(),
        "status": data.get("status", "UNKNOWN"),
        "guardrails": data.get("guardrails"),
        "verdict": data.get("verdict"),
    }


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    trace_gate = load(INPUTS["u1y_trace_equals_27mode_gate"])
    q79_response = load(INPUTS["q79_dotd_alpha1_c1_response"])
    q79_de_green = read_optional(INPUTS["q79_de_green_dotd_source"])
    q79_alpha1 = read_optional(INPUTS["q79_phifin_alpha1_payload"])
    nonsm_response = load(INPUTS["nonsm_phifin_dotd_alpha1_c1"])
    nonsm_source_driver = load(INPUTS["nonsm_dotd_alpha1_source_driver"])
    nonsm_kernel = load(INPUTS["nonsm_alpha1_tangent_or_retarded_kernel"])
    nonsm_c1_audit = load(INPUTS["nonsm_c1_response_audit"])
    protospinor_c1 = read_optional(INPUTS["protospinor_c1_response"])
    protospinor_basis = read_optional(INPUTS["protospinor_basis_transport"])

    closed_prefix = q79_response["dotd_alpha1_frontier"]["closed_finite_prefix"]
    obstruction = q79_response["selected_tangent_or_retarded_kernel_obstruction"]
    response_contract = q79_response["c1_response_emission_contract"]
    source_requirements = obstruction["source_driver_requirements"]
    derivative_checks = obstruction["derivative_payload_checks"]

    decision = {
        "D_E_gap_Riesz_Green_layer_closed": trace_gate["decision"]["DE_gap_Riesz_Green_layer_closed"],
        "same_basis_dotD_alpha1_values_available": closed_prefix["dotD_alpha1_value_matrices_emitted"],
        "dotD_alpha1_has_nonzero_entries": closed_prefix["dotD_alpha1_has_nonzero_entries"],
        "sector_projectors_clean": closed_prefix["sector_projectors_clean"],
        "finite_horizontal_response_diagnostic_passes": closed_prefix["finite_horizontal_response_diagnostic_passes"],
        "selected_dotD_source_theorem_proved": False,
        "same_branch_alpha1_driver_proved": False,
        "selected_alpha1_tangent_or_retarded_kernel_emitted": False,
        "honest_dotD_replay_without_lifted_flags": False,
        "C1_response_operator_emitted": False,
        "A_selected_emitted": False,
        "b_selected_emitted": False,
        "sector_response_matrices_emitted": False,
        "lambda_12_computable": False,
        "Yukawa_or_full_SM_closure": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    lane_classification = {
        "closed_value_prefix": {
            "status": "VALUE_PACKET_AVAILABLE_NOT_SOURCE_THEOREM",
            "scope": closed_prefix,
            "meaning": (
                "The same locked 27-mode B_N basis carries nonzero dotD_alpha1 "
                "value matrices with clean projectors. These are reusable finite "
                "targets for replay, not yet selected first variations."
            ),
        },
        "source_driver_lane": {
            "status": nonsm_source_driver["status"],
            "exact_missing_object": nonsm_source_driver["obstruction"]["exact_missing_object"],
            "requirements": source_requirements,
            "sufficient_next_payload": nonsm_source_driver["sufficient_next_payload"],
        },
        "retarded_kernel_lane": {
            "status": nonsm_kernel["status"],
            "transfer_checks": obstruction["retarded_kernel_route"]["transfer_checks"],
            "decision": obstruction["retarded_kernel_route"]["decision"],
            "next_required_artifact_in_q79": obstruction["retarded_kernel_route"]["next_required_artifact"],
        },
        "c1_response_lane": {
            "status": response_contract["status"],
            "operator_contract": response_contract["operator_contract"],
            "response_lanes": response_contract["response_lanes"],
            "honest_answer": response_contract["honest_answer"],
        },
        "protospinor_import_lane": {
            "c1_response_status": protospinor_c1.get("status", "MISSING"),
            "basis_transport_status": protospinor_basis.get("status", "MISSING"),
            "role": "alignment check only; no U1/Y selected source or alpha1 tangent is imported as proof",
        },
    }

    theorem = {
        "name": "U1YRouteCDotDAlpha1C1ResponseReductionTheorem",
        "proved": True,
        "statement": (
            "On the selected U1/Y Route-C branch, the 27-mode D_E gap/Riesz/Green "
            "layer is closed and same-basis nonzero dotD_alpha1 value matrices are "
            "available. However dotD_alpha1 is a first variation, so the selected "
            "source theorem must emit an operator-level alpha1 tangent or retarded "
            "overlap derivative and prove equality to those value matrices. Because "
            "that theorem is absent, the selected C1 response operator, A_selected, "
            "b_selected, sector response matrices, lambda_12, Yukawa magnitudes, and "
            "full SM closure are not emitted."
        ),
    }

    candidate = {
        "candidate": "SelectedU1YRouteCDotDAlpha1C1ResponseEmission",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "u1y_trace_equals_27mode_gate": status_of("u1y_trace_equals_27mode_gate", trace_gate),
            "q79_dotd_alpha1_c1_response": status_of("q79_dotd_alpha1_c1_response", q79_response),
            "q79_de_green_dotd_source": status_of("q79_de_green_dotd_source", q79_de_green),
            "q79_phifin_alpha1_payload": status_of("q79_phifin_alpha1_payload", q79_alpha1),
            "nonsm_phifin_dotd_alpha1_c1": status_of("nonsm_phifin_dotd_alpha1_c1", nonsm_response),
            "nonsm_dotd_alpha1_source_driver": status_of("nonsm_dotd_alpha1_source_driver", nonsm_source_driver),
            "nonsm_alpha1_tangent_or_retarded_kernel": status_of("nonsm_alpha1_tangent_or_retarded_kernel", nonsm_kernel),
            "nonsm_c1_response_audit": status_of("nonsm_c1_response_audit", nonsm_c1_audit),
            "protospinor_c1_response": status_of("protospinor_c1_response", protospinor_c1),
            "protospinor_basis_transport": status_of("protospinor_basis_transport", protospinor_basis),
        },
        "decision": decision,
        "lane_classification": lane_classification,
        "selected_tangent_or_retarded_kernel_obstruction": obstruction,
        "derivative_payload_checks": derivative_checks,
        "theorem": theorem,
        "what_closes_now": {
            "D_E_gap_layer_carried_forward": True,
            "same_basis_nonzero_dotD_value_packet_carried_forward": True,
            "finite_horizontal_response_diagnostic_classified": True,
            "C1_response_contract_made_validator_ready": True,
            "exact_missing_alpha1_tangent_or_retarded_kernel_identified": True,
            "overpromotion_guardrails_locked": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "operator_level_projector_retention_for_dotD": not source_requirements["R3_operator_level_projector_retention_for_dotD"],
            "selected_alpha1_deformation_parameter": not source_requirements["R4_selected_alpha1_deformation_parameter"],
            "retarded_overlap_derivative_source": not source_requirements["R5_retarded_overlap_derivative_source"],
            "honest_dotD_replay_without_lifted_flags": not source_requirements["R6_honest_dotD_replay_without_lifted_flags"],
            "same_branch_alpha1_driver_theorem": True,
            "selected_dotD_source_theorem": True,
            "selected_Hess_Xi_finite_blocks": True,
            "selected_zero_mode_bases_and_Gram_Schmidt": True,
            "selected_primitive_C1_contractions": True,
            "selected_sector_response_matrices": True,
            "A_selected": True,
            "b_selected": True,
            "lambda_12": True,
            "Yukawa_or_full_SM_closure": True,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
        "guardrails": {
            "claims_selected_dotD_source": False,
            "claims_alpha1_driver": False,
            "claims_C1_response_emitted": False,
            "claims_A_selected_or_b_selected": False,
            "claims_lambda12": False,
            "claims_Yukawa_or_full_SM_closure": False,
            "promotes_diagnostic_lift_as_proof": False,
            "uses_observed_or_benchmark_inputs": False,
            "uses_locked_D_E_only_as_gap_layer_input": True,
        },
    }

    cert = {
        "certificate": "SelectedU1YRouteCDotDAlpha1C1ResponseEmission",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "D_E_gap_Riesz_Green_layer_closed": decision["D_E_gap_Riesz_Green_layer_closed"],
        "same_basis_dotD_alpha1_values_available": decision["same_basis_dotD_alpha1_values_available"],
        "dotD_alpha1_has_nonzero_entries": decision["dotD_alpha1_has_nonzero_entries"],
        "selected_dotD_source_theorem_proved": False,
        "same_branch_alpha1_driver_proved": False,
        "selected_alpha1_tangent_or_retarded_kernel_emitted": False,
        "C1_response_operator_emitted": False,
        "A_selected_emitted": False,
        "b_selected_emitted": False,
        "lambda_12_closed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    checks = candidate["derivative_payload_checks"]
    contract = candidate["lane_classification"]["c1_response_lane"]["operator_contract"]
    lines = [
        "# Selected U1Y Route-C dotD Alpha1 C1 Response Emission v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"D_E_gap_Riesz_Green_layer_closed = {str(cert['D_E_gap_Riesz_Green_layer_closed']).lower()}",
        f"same_basis_dotD_alpha1_values_available = {str(cert['same_basis_dotD_alpha1_values_available']).lower()}",
        f"dotD_alpha1_has_nonzero_entries = {str(cert['dotD_alpha1_has_nonzero_entries']).lower()}",
        f"selected_dotD_source_theorem_proved = {str(cert['selected_dotD_source_theorem_proved']).lower()}",
        f"same_branch_alpha1_driver_proved = {str(cert['same_branch_alpha1_driver_proved']).lower()}",
        f"C1_response_operator_emitted = {str(cert['C1_response_operator_emitted']).lower()}",
        f"lambda_12_closed = {str(cert['lambda_12_closed']).lower()}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "The closed 27-mode `D_E` gap layer carries forward. The same basis also",
        "contains nonzero `dotD_alpha1` value matrices with clean projectors, but",
        "the corpus still lacks the selected first-variation theorem that makes",
        "those matrices source-derived rather than diagnostic.",
        "",
        "## Derivative Payload Checks",
        "",
    ]
    for key, value in checks.items():
        lines.append(f"- `{key}`: `{str(value).lower()}`")
    lines.extend(
        [
            "",
            "## Missing Object",
            "",
            candidate["selected_tangent_or_retarded_kernel_obstruction"]["source_driver_obstruction"]["exact_missing_object"],
            "",
            "## C1 Response Contract",
            "",
            f"- `{contract['name']}`",
            f"- equation: `{contract['operator_equation']}`",
            f"- codomain real dimension: `{contract['codomain_real_dimension']}`",
            "",
            "The contract is now validator-ready as a target shape, but not computable",
            "because `A_selected`, `b_selected`, finite Hessian blocks, selected zero",
            "modes, and primitive C1 contractions are not emitted.",
            "",
            "## Guardrails",
            "",
            "- Do not infer selected `dotD` from the closed `D_E` gap layer.",
            "- Do not promote diagnostic source-lift flags.",
            "- Do not treat the canonical zero C1 response as a mass hierarchy.",
            "- Do not use observed masses, CKM data, benchmark matrices, or target-localized columns.",
            "",
            "## Certificate",
            "",
            "```json",
            json.dumps(cert, indent=2, sort_keys=True),
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    candidate, cert, note = build()
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
