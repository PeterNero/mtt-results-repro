"""Build the electroweak Qa-stack quotient-functor/A_base identity gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "trace_formula_gate": DATA / "selected_electroweak_qastack_selected_traceequality_or_full_threshold_formula.candidate.json",
    "pperp_policy": DATA / "selected_u1_quotient_projector_pperp_and_trace_policy.candidate.json",
    "quotient_determinant_lemma": DATA / "selected_electroweak_u1y_quotientdeterminant_lemma.candidate.json",
    "factorized_attempt": DATA / "selected_electroweak_u1y_factorized_threshold_operator_source_attempt.candidate.json",
    "matrix_payload": DATA / "selected_electroweak_u1y_factorized_threshold_operator_source_attempt.matrix.json",
    "determinant_weighting_nogo": DATA / "selected_electroweak_u1y_determinantfunctional_weighting_or_nogo.candidate.json",
    "regularization_bridge": DATA / "selected_electroweak_qastack_sourceidentity_and_prow_regularization.candidate.json",
}

OUTPUT_DATA = DATA / "selected_electroweak_qastack_quotient_functor_and_abase_identity.candidate.json"
OUTPUT_CERT = CERTS / "selected_electroweak_qastack_quotient_functor_and_abase_identity_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Electroweak_QaStack_QuotientFunctor_and_AbaseIdentity_Theorem_v1.md"

STATUS = "ELECTROWEAK_QASTACK_QUOTIENT_FUNCTOR_CONDITIONAL_ABASE_IDENTITY_SOURCE_OPEN"
NEXT = "Selected_Electroweak_QaStack_DeterminantFunctional_SourceTheorem_or_SelectedAbaseEmission_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    trace_gate = load(INPUTS["trace_formula_gate"])
    pperp = load(INPUTS["pperp_policy"])
    quotient = load(INPUTS["quotient_determinant_lemma"])
    factorized = load(INPUTS["factorized_attempt"])
    matrix = load(INPUTS["matrix_payload"])
    weighting = load(INPUTS["determinant_weighting_nogo"])
    regularization = load(INPUTS["regularization_bridge"])

    pperp_decision = pperp["decision"]
    quotient_decision = quotient["decision"]
    factor_decision = factorized["decision"]
    source_identity = factorized["source_identity"]

    algebraic_functor = {
        "Pperp_policy_closed_index_only": pperp_decision["U1_operator_trace_uses_P_perp"],
        "shared_vector_selected": pperp_decision["explicit_U1_shared_vector_s"],
        "rank3_to_quotient_rank": quotient["rank_accounting"],
        "tensor_identity_quotient_lemma_proved": quotient_decision["algebraic_quotient_determinant_lemma_proved"],
        "factorized_matrix_constructed": factor_decision["factorized_operator_matrix_constructed"],
        "quotient_matrix_constructed": factor_decision["quotient_operator_matrix_constructed"],
        "raw_formula": factorized["constructed_operator_summary"]["raw_formula"],
        "quotient_formula": factorized["constructed_operator_summary"]["quotient_formula"],
        "quotient_logdet": quotient_decision["quotient_logdet"],
        "matches_previous_Pperp_weighted_value": quotient_decision["matches_previous_Pperp_weighted_value"],
    }

    source_tests = {
        "selected_BN_to_tensor_identity_functor": {
            "passed": False,
            "reason": "The selected B_N/D_E gap theorem gives the gap operator, but no theorem maps that selected B_N operator to the tensor-identity threshold functor.",
            "trace_gate_status": trace_gate["status"],
        },
        "exact_A_base_tensor_I3_emitted_by_source": {
            "passed": source_identity["factorized_matrix_emitted_by_prior_source"] is True,
            "reason": "The matrix is constructed, but the prior source does not emit it as the selected threshold operator.",
            "constructed_here": source_identity["factorized_matrix_constructed_here"],
            "emitted_by_prior_source": source_identity["factorized_matrix_emitted_by_prior_source"],
        },
        "same_source_Pperp_domain": {
            "passed": source_identity["same_source_as_Pperp_trace_policy"] is True,
            "reason": "The Pperp domain policy is same-source support for the carrier quotient, but only at index/trace-policy level.",
        },
        "determinant_functional_source_theorem": {
            "passed": weighting["decision"]["determinant_functional_source_theorem_found"],
            "reason": "The current weighting gate proves a current-source no-go for promoting Pperp weighting as determinant finite part.",
            "conditional_Pperp_weighted_logdet": weighting["decision"]["conditional_Pperp_weighted_logdet"],
        },
        "Qa_stack_weights_and_scale": {
            "passed": False,
            "reason": "The regularization bridge is still conditional on source-emitted Qa-stack weights and determinant scale.",
            "regularization_bridge_conditional": regularization["decision"]["p_row_regularization_bridge_conditional_closed"],
        },
    }

    candidate = {
        "candidate": "SelectedElectroweakQaStackQuotientFunctorAndAbaseIdentity",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_status": trace_gate["status"],
        "algebraic_functor": algebraic_functor,
        "source_tests": source_tests,
        "decision": {
            "tensor_identity_quotient_functor_closed": True,
            "Pperp_domain_policy_closed": True,
            "quotient_determinant_lemma_closed": True,
            "factorized_matrix_constructed": True,
            "selected_BN_to_threshold_functor_closed": False,
            "A_base_tensor_I3_identity_closed": False,
            "determinant_functional_source_theorem_closed": False,
            "Qa_stack_weights_and_scale_policy_closed": False,
            "selected_p_a_promoted": False,
            "lambda_12_closed": False,
            "measured_electroweak_closure": False,
            "current_source_nogo_proved": True,
            "mathematical_impossibility_claimed": False,
            "target_fitting_used": False,
            "next_required_artifact": NEXT,
        },
        "theorem": {
            "name": "TensorIdentityQuotientFunctorIsAlgebraicButNotYetSelectedAbaseEmission",
            "proved": True,
            "statement": (
                "For an emitted operator of the form A_base tensor I_3 on the "
                "rank-3 carrier, the selected shared-line quotient functor is "
                "algebraically closed by P_perp and the quotient determinant "
                "lemma, giving A_base tensor I_(V_3/<s>) and logdet "
                f"{quotient_decision['quotient_logdet']}. The present source "
                "does not yet prove that the selected 27-mode B_N/D_E operator "
                "is exactly this A_base tensor I_3 threshold row, nor that the "
                "P_perp quotient logdet is the selected Qa-stack determinant "
                "finite part with source-emitted weights and scale."
            ),
        },
        "minimal_next_payload": {
            "name": NEXT,
            "must_emit": [
                "same-source theorem identifying selected B_N/D_E threshold row with A_base tensor I_3",
                "or a replacement selected determinant-functional theorem directly on B_N",
                "source-emitted finite zeta/heat/torsion finite-part policy on V/<s>",
                "source-emitted Qa-stack index weights and determinant scale",
                "same-scheme SU2 row or exact cancellation theorem if lambda_12 is computed",
            ],
        },
        "what_closes": {
            "conditional_tensor_identity_quotient_functor": True,
            "conditional_quotient_logdet": True,
            "Pperp_domain_policy_as_index": True,
            "A_base_matrix_construction_recorded": True,
            "source_identity_gap_sharpened": True,
        },
        "what_remains_open": {
            "selected_BN_to_threshold_functor": True,
            "selected_A_base_tensor_I3_emission": True,
            "selected_determinant_functional_on_V_mod_s": True,
            "Qa_stack_weights_and_scale": True,
            "selected_p_a": True,
            "lambda_12": True,
            "measured_electroweak_closure": True,
        },
        "guardrails": {
            "promotes_tensor_identity_model_as_selected": False,
            "promotes_A_base_matrix_as_selected": False,
            "promotes_Pperp_weighting_as_finite_part": False,
            "promotes_selected_p_a": False,
            "claims_lambda12": False,
            "claims_measured_electroweak_closure": False,
            "uses_observed_electroweak_data": False,
            "target_fitting_used": False,
            "uses_lifted_validator_flags": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedElectroweakQaStackQuotientFunctorAndAbaseIdentity",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "tensor_identity_quotient_functor_closed": True,
        "selected_BN_to_threshold_functor_closed": False,
        "A_base_tensor_I3_identity_closed": False,
        "determinant_functional_source_theorem_closed": False,
        "selected_p_a_promoted": False,
        "lambda_12_closed": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected Electroweak QaStack QuotientFunctor and AbaseIdentity Theorem v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        "tensor_identity_quotient_functor_closed = true",
        "selected_BN_to_threshold_functor_closed = false",
        "A_base_tensor_I3_identity_closed = false",
        "determinant_functional_source_theorem_closed = false",
        "selected_p_a_promoted = false",
        "lambda_12_closed = false",
        f"next_required_artifact = {candidate['decision']['next_required_artifact']}",
        "```",
        "",
        "This closes the algebraic quotient functor only for the already-constructed",
        "`A_base tensor I_3` tensor-identity model. It does not yet prove that the",
        "selected `B_N/D_E` threshold source emits that model.",
        "",
        "## Algebraic Functor",
        "",
        "```json",
        json.dumps(candidate["algebraic_functor"], indent=2, sort_keys=True),
        "```",
        "",
        "## Source Tests",
        "",
        "```json",
        json.dumps(candidate["source_tests"], indent=2, sort_keys=True),
        "```",
        "",
        "## Theorem",
        "",
        candidate["theorem"]["statement"],
        "",
        "## Minimal Next Payload",
        "",
        f"Next artifact: `{candidate['minimal_next_payload']['name']}`.",
        "",
    ]
    for item in candidate["minimal_next_payload"]["must_emit"]:
        lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "## Guardrails",
            "",
            "- The tensor-identity model is not promoted as selected threshold data.",
            "- `P_perp` weighting is not promoted as a determinant finite-part theorem.",
            "- `p_a`, `lambda_12`, and measured electroweak closure remain open.",
            "- No observed electroweak data, target residuals, or lifted flags are used.",
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
    DATA.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    PROOF.mkdir(parents=True, exist_ok=True)
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
