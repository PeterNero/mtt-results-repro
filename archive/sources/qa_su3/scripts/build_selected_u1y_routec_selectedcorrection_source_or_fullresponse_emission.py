"""Build the selected correction-source or full-response emission gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
TEXPAPERS = ROOT.parent
SM = TEXPAPERS / "mtt-sm-parity-closure"
Q79 = TEXPAPERS / "mtt-q79-proof-repro"
CONSTANTS = TEXPAPERS / "mtt-nonsm-constants-no-knob"

INPUTS = {
    "local_primitive_higherorder_gate": DATA / "selected_u1y_routec_primitiveclass_c1observable_or_higherorder_fullresponse_sourceemission.candidate.json",
    "sm_correction_source_gate": SM / "candidate_data" / "selected_routec_correction_source_emission_or_selected_galerkin_values.candidate.json",
    "sm_correction_source_cert": SM / "certificates" / "selected_routec_correction_source_emission_or_selected_galerkin_values_certificate.json",
    "sm_basis_transport_counterexample": SM / "candidate_data" / "selected_routec_basis_transport_primitive_source_proof_or_counterexample.candidate.json",
    "constants_selected_correction_gate": CONSTANTS / "certificates" / "selected_correction_emission_gate_certificate.json",
    "q79_weylpair_aselected": Q79 / "candidate_data" / "q79_routec_weylpair_aselected_assembly_or_source_proof.candidate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_selectedcorrection_source_or_fullresponse_emission.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_selectedcorrection_source_or_fullresponse_emission_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_SelectedCorrectionMatrixSource_or_FullResponseEmission_v1.md"

STATUS = "U1Y_ROUTEC_SELECTED_CORRECTION_EMISSION_REDUCED_NONIDENTITY_RHOE_BN_OPEN"
NEXT = "Selected_U1Y_RouteC_NonIdentity_RhoE_and_QuotientValid_BN_Construction_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    local_gate = load(INPUTS["local_primitive_higherorder_gate"])
    sm_gate = load(INPUTS["sm_correction_source_gate"])
    sm_cert = load(INPUTS["sm_correction_source_cert"])
    sm_counter = load(INPUTS["sm_basis_transport_counterexample"])
    constants_gate = load(INPUTS["constants_selected_correction_gate"])
    q79_weyl = load(INPUTS["q79_weylpair_aselected"])

    diagnostic = constants_gate["diagnostic_representative"]
    selected_payload_audit = sm_gate["selected_payload_audit"]
    selected_galerkin_audit = sm_gate["selected_galerkin_values_audit"]
    primitive_counter = sm_counter["source_attempt"]
    q79_conditional = q79_weyl["conditional_solve"]

    reduction = {
        "diagnostic_splitter_exists": constants_gate["closed_now"]["diagnostic_qutrit_splitter_exists"],
        "diagnostic_splitter_not_promoted": constants_gate["closed_now"]["diagnostic_splitter_not_promoted"],
        "mass_mixing_cp_diagnostic_tests_nonzero": constants_gate["closed_now"][
            "mass_mixing_cp_diagnostic_tests_nonzero"
        ],
        "strict_primitive_search_found_no_legal_emission": constants_gate["closed_now"][
            "strict_primitive_search_found_no_legal_emission"
        ],
        "primitive_only_span_counterexample": primitive_counter["counterexample_proved"],
        "formal_lift_rejected_as_proof": constants_gate["closed_now"]["formal_lift_rejected_as_proof"],
        "honest_galerkin_selected_values_emit_correction": sm_gate["source_emission_attempt"][
            "any_representative_label_emitted_by_selected_inputs"
        ],
        "selected_payload_values_emitted": selected_payload_audit["selected_values_emitted"],
        "selected_correction_matrices_emitted": selected_galerkin_audit[
            "selected_correction_matrices_emitted"
        ],
        "q79_conditional_A_solve_exact_support": q79_conditional["closed_now"]["solve_consistent"],
        "q79_conditional_A_promoted": q79_weyl["decision"]["conditional_A_promoted_to_A_selected"],
        "next_construction": NEXT,
    }

    required_payload = {
        "selected_source_certificate": {
            "required": True,
            "current_status": "open",
            "description": "Same q79/F,m=1 branch must select the non-identity rho_E/B_N source.",
        },
        "nonidentity_rho_E": {
            "required": True,
            "current_status": "open",
            "description": "Projective/twisted transition data or equivalent operator row; identity smoke is forbidden.",
        },
        "quotient_valid_B_N": {
            "required": True,
            "current_status": "open",
            "description": "Non-invariant finite Galerkin basis respecting the fixed-fiber quotient and selected sector maps.",
        },
        "selected_D_E_Riesz_Green_dotD": {
            "required": True,
            "current_status": "open",
            "description": "Honest replay without lifted selected_source, selected_dotD_source, or alpha1-driver flags.",
        },
        "selected_deltaTheta_C1_solution": {
            "required": True,
            "current_status": "open",
            "description": "Finite Hessian/source solve emitting correction matrices, not a diagnostic label search.",
        },
        "primitive_C1_contractions_or_full_response_matrices": {
            "required": True,
            "current_status": "open",
            "description": "Sector matrices for u,d,e,nuD that pass mass, commutator, and CP audits.",
        },
        "b_selected_or_homogeneous_zero_theorem": {
            "required": True,
            "current_status": "open",
            "description": "The inhomogeneous row must be source-emitted or proved zero by theorem.",
        },
    }

    acceptance_tests = {
        "mass_splitting": {
            "required": "nonzero traceless part of selected H_s^(r)",
            "diagnostic_value": diagnostic["mass_split_traceless_norm_sq"],
            "selected_status": "open",
        },
        "CKM_or_PMNS_commutator": {
            "required": "selected Hermitian corrections not simultaneously diagonalizable",
            "diagnostic_values": {
                "ckm_commutator_norm_sq": diagnostic["ckm_commutator_norm_sq"],
                "pmns_commutator_norm_sq": diagnostic["pmns_commutator_norm_sq"],
            },
            "selected_status": "open",
        },
        "CP_odd": {
            "required": "selected nonzero CP-odd invariant",
            "diagnostic_value": diagnostic["cp_odd_trace_commutator_cubed_imag"],
            "selected_status": "open",
        },
    }

    decision = {
        "selected_correction_matrix_source_closed": False,
        "selected_full_response_emission_closed": False,
        "diagnostic_splitter_promoted": False,
        "formal_lift_promoted": False,
        "primitive_only_route_retired_for_splitter": True,
        "nonidentity_rhoE_and_BN_required": True,
        "A_selected_computable": False,
        "b_selected_computable": False,
        "lambda_12_computable": False,
        "Yukawa_CKM_PMNS_CP_or_full_SM_closure": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "SelectedU1YRouteCSelectedCorrectionMatrixSourceOrFullResponseEmission",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "local_primitive_higherorder_gate": local_gate["status"],
            "sm_correction_source_gate": sm_gate["status"],
            "sm_correction_source_cert": sm_cert["status"],
            "sm_basis_transport_counterexample": sm_counter["status"],
            "constants_selected_correction_gate": constants_gate["status"],
            "q79_weylpair_aselected": q79_weyl["status"],
        },
        "reduction": reduction,
        "diagnostic_representative_support_only": diagnostic,
        "required_payload": required_payload,
        "acceptance_tests": acceptance_tests,
        "decision": decision,
        "theorem": {
            "name": "U1YRouteCSelectedCorrectionEmissionReductionTheorem",
            "proved": True,
            "statement": (
                "The selected correction/full-response gate has no algebraic splitter "
                "obstruction: a qutrit/Weyl diagnostic splitter passes mass-splitting, "
                "commutator, and CP-odd tests without observed targets, and the q79 "
                "Weyl-pair packet gives an exact conditional A solve. However the "
                "diagnostic splitter is not selected, the formal Galerkin lift is not "
                "proof, primitive-only emission is insufficient, and no current same-source "
                "payload emits selected correction matrices. The gate therefore reduces "
                "to constructing non-identity rho_E and quotient-valid B_N from the same "
                "q79/F,m=1 branch, followed by an honest selected deltaTheta/C1 solve."
            ),
        },
        "what_closes_now": {
            "selected_correction_gate_reduced": True,
            "diagnostic_splitter_recorded_support_only": True,
            "primitive_only_route_retired_for_splitter": True,
            "formal_lift_rejected_as_proof": True,
            "nonidentity_rhoE_BN_payload_contract_built": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_nonidentity_rho_E": True,
            "selected_quotient_valid_B_N": True,
            "selected_D_E_Riesz_Green_dotD": True,
            "selected_deltaTheta_C1_solution": True,
            "selected_primitive_C1_contractions_or_full_response_matrices": True,
            "A_selected": True,
            "b_selected": True,
            "lambda_12": True,
            "Yukawa_CKM_PMNS_CP_or_full_SM_closure": True,
        },
        "guardrails": {
            "claims_selected_correction_matrix_source": False,
            "claims_selected_full_response_emission": False,
            "claims_diagnostic_splitter_selected": False,
            "claims_formal_lift_as_proof": False,
            "claims_A_selected": False,
            "claims_b_selected": False,
            "claims_lambda12": False,
            "claims_Yukawa_CKM_PMNS_CP_or_full_SM_closure": False,
            "uses_observed_data": False,
            "uses_benchmark_data": False,
            "uses_locked_target_columns": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedU1YRouteCSelectedCorrectionMatrixSourceOrFullResponseEmission",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "selected_correction_gate_reduced": True,
        "diagnostic_splitter_recorded_support_only": True,
        "primitive_only_route_retired_for_splitter": True,
        "nonidentity_rhoE_and_BN_required": True,
        "selected_correction_matrix_source_closed": False,
        "selected_full_response_emission_closed": False,
        "A_selected_computable": False,
        "b_selected_computable": False,
        "lambda_12_computable": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    red = candidate["reduction"]
    diag = candidate["diagnostic_representative_support_only"]
    return f"""# Selected U1Y Route-C SelectedCorrectionMatrixSource or FullResponseEmission v1

## Result

```text
status = {candidate["status"]}
selected_correction_gate_reduced = true
diagnostic_splitter_recorded_support_only = true
primitive_only_route_retired_for_splitter = true
nonidentity_rhoE_and_BN_required = true
selected_correction_matrix_source_closed = false
selected_full_response_emission_closed = false
next_required_artifact = {candidate["next_required_artifact"]}
```

The algebraic possibility problem is no longer the main blocker. A diagnostic
qutrit/Weyl splitter exists and passes the intended mass, mixing, and CP tests
without observed targets. It is still support only.

## Diagnostic Values

- candidate count: `{diag["candidate_count"]}`
- CKM commutator norm squared: `{diag["ckm_commutator_norm_sq"]}`
- PMNS commutator norm squared: `{diag["pmns_commutator_norm_sq"]}`
- CP-odd trace commutator cubed imaginary part: `{diag["cp_odd_trace_commutator_cubed_imag"]}`
- selected by source: `False`

## Reduction

- primitive-only route retired for this splitter: `{red["primitive_only_span_counterexample"]}`
- formal lift rejected as proof: `{red["formal_lift_rejected_as_proof"]}`
- selected payload values emitted: `{red["selected_payload_values_emitted"]}`
- selected correction matrices emitted: `{red["selected_correction_matrices_emitted"]}`
- q79 conditional A solve exact support: `{red["q79_conditional_A_solve_exact_support"]}`

## Required Payload

The next construction must emit, from the same q79/F,m=1 branch:

- non-identity `rho_E`,
- quotient-valid non-invariant `B_N`,
- selected `D_E`, Riesz/Green, and `dotD`,
- selected `deltaTheta_C1` solve,
- primitive C1 contractions or full response matrices,
- `b_selected` or a homogeneous-zero theorem.

## Guardrails

Do not use the diagnostic splitter, formal lift, observed masses, CKM, PMNS,
CP, benchmark entries, or diagnostic `lambda_12` values as selected proof data.

## Certificate

```json
{json.dumps(cert, indent=2, sort_keys=True)}
```
"""


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    candidate, cert, note = build()
    write_json(OUTPUT_DATA, candidate)
    write_json(OUTPUT_CERT, cert)
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    for path in [OUTPUT_DATA, OUTPUT_CERT, OUTPUT_NOTE]:
        print(f"wrote {rel(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
