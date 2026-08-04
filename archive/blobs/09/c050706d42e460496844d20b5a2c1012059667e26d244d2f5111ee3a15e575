"""Build the electroweak Qa-stack selected trace-equality/full-formula gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "qastack_threshold_prefix": DATA / "selected_electroweak_qastack_threshold_operator_from_nonidentity_rhoe_quotientbn.candidate.json",
    "routec_trace_equals_27mode": DATA / "selected_u1y_routec_trace_equals_27mode_or_full_hym_replay.candidate.json",
    "routec_finite_hym_solve": DATA / "selected_u1y_routec_finite_hym_connection_solve_or_typed_cech_payload.candidate.json",
    "u1y_localdet_gaplayer": DATA / "selected_electroweak_u1y_localdeterminant_from_27mode_de_gaplayer.candidate.json",
    "factorized_attempt": DATA / "selected_electroweak_u1y_factorized_threshold_operator_source_attempt.candidate.json",
    "matrix_payload": DATA / "selected_electroweak_u1y_factorized_threshold_operator_source_attempt.matrix.json",
    "regularization_bridge": DATA / "selected_electroweak_qastack_sourceidentity_and_prow_regularization.candidate.json",
}

OUTPUT_DATA = DATA / "selected_electroweak_qastack_selected_traceequality_or_full_threshold_formula.candidate.json"
OUTPUT_CERT = CERTS / "selected_electroweak_qastack_selected_traceequality_or_full_threshold_formula_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Electroweak_QaStack_SelectedTraceEquality_or_FullThresholdOperatorFormula_v1.md"

STATUS = "ELECTROWEAK_QASTACK_TRACEEQUALITY_IMPORTED_QUOTIENT_FUNCTOR_AND_ABASE_IDENTITY_OPEN"
NEXT = "Selected_Electroweak_QaStack_QuotientFunctor_and_AbaseIdentity_Theorem_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    prefix = load(INPUTS["qastack_threshold_prefix"])
    trace = load(INPUTS["routec_trace_equals_27mode"])
    finite_hym = load(INPUTS["routec_finite_hym_solve"])
    localdet = load(INPUTS["u1y_localdet_gaplayer"])
    factorized = load(INPUTS["factorized_attempt"])
    matrix = load(INPUTS["matrix_payload"])
    regularization = load(INPUTS["regularization_bridge"])

    trace_decision = trace["decision"]
    gap = trace["finite_trace_route"]["gap_layer"]
    finite_decision = finite_hym["decision"]
    prefix_tests = prefix["threshold_adapter_tests"]

    imported_trace_layer = {
        "basis_id": gap["basis_id"],
        "basis_dimension": gap["basis_dimension"],
        "selected_trace_equality_for_27mode_DE": trace_decision["selected_trace_equality_for_27mode_DE"],
        "DE_gap_Riesz_Green_layer_closed": trace_decision["DE_gap_Riesz_Green_layer_closed"],
        "D_E_source_flags_theorem_derived": gap["D_E_source_flags_are_theorem_derived"],
        "D_E_honest_replay_passes_after_theorem_flags": gap["D_E_honest_replay_passes_after_theorem_derived_source_flags"],
        "selected_eta_N": trace_decision["selected_eta_N"],
        "eta_threshold": trace_decision["eta_threshold"],
        "model_gap_gamma_N": gap["model_gap_gamma_N"],
        "selected_gap_lower_bound": trace_decision["selected_gap_lower_bound"],
        "selected_green_norm_bound": trace_decision["selected_green_norm_bound"],
        "finite_HYM_DE_gap_layer_promoted": finite_decision["finite_DE_gap_layer_promoted"],
        "finite_HYM_full_connection_solve_closed": finite_decision["full_finite_HYM_connection_solve_closed"],
        "finite_HYM_dotD_alpha1_source_closed": finite_decision["dotD_alpha1_source_closed"],
    }

    threshold_formula_tests = {
        "selected_trace_equality_for_DE_gap_layer": {
            "passed": imported_trace_layer["selected_trace_equality_for_27mode_DE"] is True
            and imported_trace_layer["DE_gap_Riesz_Green_layer_closed"] is True,
            "scope": "selected 27-mode D_E gap/Riesz/Green layer only",
            "reason": "Route-C proves the emitted 27-mode D_E formula is the selected Phi_fin compression on B_N for the gap layer.",
        },
        "full_selected_threshold_operator_formula": {
            "passed": False,
            "reason": "The imported theorem identifies D_E on B_N for the gap layer, not the full electroweak threshold operator on the Qa-stack quotient row.",
            "known_missing": [
                "operator formula after restriction from B_N to V/<s>",
                "same-source finite-part determinant functional for the quotient row",
                "full HYM/Route-C connection lift beyond D_E gap layer",
            ],
        },
        "quotient_functor_BN_to_Pperp_shared_line": {
            "passed": False,
            "reason": "No source theorem yet constructs the functor/restriction carrying the selected 27-mode B_N operator to the electroweak Pperp/shared-line quotient domain.",
            "localdet_gate_status": localdet["status"],
        },
        "exact_A_base_tensor_I3_identity": {
            "passed": False,
            "reason": "A_base tensor I_3 is constructed as a target row, but the selected B_N operator has not been proved equal to it before quotienting.",
            "constructed_A_base_tensor_I3_available": factorized["decision"]["factorized_operator_matrix_constructed"],
            "constructed_quotient_logdet": matrix["quotient_operator"]["logdet"],
        },
        "Qa_stack_weights_and_scale_policy": {
            "passed": False,
            "reason": "The p-row regularization bridge remains conditional on source-emitted Qa-stack index weights and determinant scale.",
            "conditional_regularization_bridge": regularization["decision"]["p_row_regularization_bridge_conditional_closed"],
        },
    }

    all_closed = all(test["passed"] for test in threshold_formula_tests.values())
    true_frontier = [
        "construct the quotient functor/restriction from selected B_N to V/<s> or Pperp/shared-line domain",
        "prove the restricted operator is exactly A_base tensor I_3 before quotient",
        "derive post-quotient determinant identity without importing the constructed benchmark row as proof",
        "emit Qa-stack index weights and determinant scale from the same source",
    ]

    candidate = {
        "candidate": "SelectedElectroweakQaStackSelectedTraceEqualityOrFullThresholdFormula",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_status": prefix["status"],
        "imported_trace_layer": imported_trace_layer,
        "threshold_formula_tests": threshold_formula_tests,
        "frontier_reclassification": {
            "old_broad_blocker": "selected trace equality or full threshold operator formula",
            "resolved_part": "selected trace equality for the 27-mode D_E gap/Riesz/Green layer",
            "not_resolved": "full electroweak Qa-stack threshold operator formula",
            "true_frontier": true_frontier,
        },
        "decision": {
            "selected_DE_gap_trace_equality_closed": True,
            "DE_gap_Riesz_Green_layer_closed": True,
            "full_threshold_operator_formula_closed": all_closed,
            "quotient_functor_closed": False,
            "A_base_tensor_I3_identity_closed": False,
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
            "name": "SelectedDETraceEqualityDoesNotByItselfPromoteTheQaStackThresholdRow",
            "proved": True,
            "statement": (
                "The selected q79/F,m=1 Route-C trace theorem closes the emitted "
                "27-mode D_E gap/Riesz/Green layer on B_N. This removes selected "
                "D_E trace equality as a broad blocker, but it does not identify "
                "the electroweak Qa-stack threshold determinant. The remaining "
                "promotion requires a same-source quotient functor from B_N to "
                "the shared-line/Pperp quotient domain, an exact identity with "
                "A_base tensor I_3, and source-emitted Qa-stack weights and scale."
            ),
        },
        "minimal_next_payload": {
            "name": NEXT,
            "must_emit": true_frontier,
            "acceptance_rule": (
                "The next payload must use the selected B_N/D_E theorem as input, "
                "not as the result to be proved. It must derive the quotient row "
                "and determinant identity from the same source, without observed "
                "electroweak data, benchmark residuals, or lifted validator flags."
            ),
        },
        "what_closes": {
            "selected_trace_equality_for_DE_gap_layer": True,
            "selected_DE_gap_Riesz_Green_layer": True,
            "broad_trace_equality_blocker_reclassified": True,
            "full_threshold_identity_cutset_sharpened": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "full_selected_threshold_operator_formula": True,
            "quotient_functor_BN_to_Pperp_shared_line": True,
            "exact_A_base_tensor_I3_identity": True,
            "post_quotient_determinant_identity": True,
            "Qa_stack_index_weights_and_scale_policy": True,
            "selected_p_a": True,
            "lambda_12": True,
            "measured_electroweak_closure": True,
        },
        "guardrails": {
            "claims_full_threshold_formula": False,
            "promotes_constructed_A_base_as_selected": False,
            "promotes_quotient_logdet_as_p_a": False,
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
        "certificate": "SelectedElectroweakQaStackSelectedTraceEqualityOrFullThresholdFormula",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "selected_DE_gap_trace_equality_closed": True,
        "full_threshold_operator_formula_closed": False,
        "quotient_functor_closed": False,
        "A_base_tensor_I3_identity_closed": False,
        "selected_p_a_promoted": False,
        "lambda_12_closed": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected Electroweak QaStack SelectedTraceEquality or FullThresholdOperatorFormula v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        "selected_DE_gap_trace_equality_closed = true",
        "full_threshold_operator_formula_closed = false",
        "quotient_functor_closed = false",
        "A_base_tensor_I3_identity_closed = false",
        "selected_p_a_promoted = false",
        "lambda_12_closed = false",
        f"next_required_artifact = {candidate['decision']['next_required_artifact']}",
        "```",
        "",
        "The broad trace-equality blocker is now split. The selected 27-mode `D_E`",
        "trace equality is closed for the gap/Riesz/Green layer on `B_N`; that is",
        "real progress. It still does not identify the electroweak Qa-stack",
        "threshold determinant.",
        "",
        "## Imported Trace Layer",
        "",
        "```json",
        json.dumps(candidate["imported_trace_layer"], indent=2, sort_keys=True),
        "```",
        "",
        "## Tests",
        "",
        "```json",
        json.dumps(candidate["threshold_formula_tests"], indent=2, sort_keys=True),
        "```",
        "",
        "## Reclassification",
        "",
        "```json",
        json.dumps(candidate["frontier_reclassification"], indent=2, sort_keys=True),
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
            "Acceptance rule:",
            "",
            candidate["minimal_next_payload"]["acceptance_rule"],
            "",
            "## Guardrails",
            "",
            "- The constructed `A_base tensor I_3` row is not promoted as selected.",
            "- The quotient logdet is not promoted as `p_a`.",
            "- No observed electroweak data, target residuals, or lifted validator flags are used.",
            "- `lambda_12` and measured electroweak closure remain open.",
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
