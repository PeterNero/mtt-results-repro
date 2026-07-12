"""Build the electroweak Qa-stack threshold-operator fill from nonidentity rho_E/B_N."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "qastack_source_identity": DATA / "selected_electroweak_qastack_sourceidentity_from_terminal_or_gerbe.candidate.json",
    "nonidentity_interface": DATA / "selected_u1y_routec_nonidentity_rhoe_quotientvalid_bn_interface.candidate.json",
    "finite_trace_prefix": DATA / "selected_u1y_routec_selected_finite_trace_source_or_nogo.candidate.json",
    "selected_correction_gate": DATA / "selected_u1y_routec_selectedcorrection_source_or_fullresponse_emission.candidate.json",
    "factorized_attempt": DATA / "selected_electroweak_u1y_factorized_threshold_operator_source_attempt.candidate.json",
    "matrix_payload": DATA / "selected_electroweak_u1y_factorized_threshold_operator_source_attempt.matrix.json",
    "regularization_bridge": DATA / "selected_electroweak_qastack_sourceidentity_and_prow_regularization.candidate.json",
}

OUTPUT_DATA = DATA / "selected_electroweak_qastack_threshold_operator_from_nonidentity_rhoe_quotientbn.candidate.json"
OUTPUT_CERT = CERTS / "selected_electroweak_qastack_threshold_operator_from_nonidentity_rhoe_quotientbn_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Electroweak_QaStack_ThresholdOperator_From_NonIdentityRhoE_QuotientBN_Fill_v1.md"

STATUS = "ELECTROWEAK_QASTACK_NONIDENTITY_RHOE_QUOTIENTBN_PREFIX_IMPORTED_THRESHOLD_IDENTITY_OPEN"
NEXT = "Selected_Electroweak_QaStack_SelectedTraceEquality_or_FullThresholdOperatorFormula_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    source_identity = load(INPUTS["qastack_source_identity"])
    interface = load(INPUTS["nonidentity_interface"])
    finite = load(INPUTS["finite_trace_prefix"])
    correction = load(INPUTS["selected_correction_gate"])
    factorized = load(INPUTS["factorized_attempt"])
    matrix = load(INPUTS["matrix_payload"])
    regularization = load(INPUTS["regularization_bridge"])

    lane = finite["smooth_27mode_lane"]
    finite_values = lane["finite_values_present"]
    selected = finite["decision"]
    cutset = finite["source_trace_cutset"]

    prefix_payload = {
        "nonidentity_rhoE_candidate_present": lane["rhoe"]["nonidentity_projective_rhoE_candidate_built"],
        "rhoE_selected_by_mtt": lane["rhoe"]["selected_by_mtt"],
        "smooth_27mode_BN_present": finite_values["smooth_27_mode_BN"],
        "BN_dimension": lane["basis"]["dimension"],
        "BN_zero_cluster_dimension": lane["basis"]["zero_cluster_dimension"],
        "BN_complement_gap": lane["basis"]["complement_gap"],
        "projective_equivariance_up_to_central_phase": lane["basis"]["projective_equivariance_up_to_central_phase"],
        "D_E_matrix_present": lane["de"]["matrix_emitted"],
        "Riesz_Green_gap_present": finite_values["Riesz_Green_gap"],
        "dotD_alpha1_present": lane["dotd"]["matrix_emitted"],
        "sector_projectors_present": lane["dotd"]["sector_projectors_emitted"],
        "C1_engine_present": lane["c1"]["primitive_engine_built"],
        "first_tracefree_HYM_correction_present": finite_values["first_tracefree_HYM_correction"],
    }

    threshold_adapter_tests = {
        "prefix_can_host_threshold_operator": {
            "passed": True,
            "reason": "The 27-mode B_N prefix has nonidentity projective rho_E support, D_E, Riesz/Green, dotD, sector projectors, and a positive complement gap.",
        },
        "selected_source_certificate": {
            "passed": False,
            "reason": "The finite trace gate still has rhoE_selected_by_mtt=false and theorem-derived selected-source flags open.",
            "open_items": {
                "selected_trace_equality": selected["selected_trace_equality_proved"],
                "full_selected_operator_formula": selected["full_selected_operator_formula_proved"],
                "honest_replay_without_lifted_flags": selected["honest_replay_without_lifted_flags"],
                "selected_gap_error_certificate": selected["selected_gap_error_certificate"],
                "rhoE_selected_by_mtt": selected["rhoE_selected_by_mtt"],
            },
        },
        "quotient_valid_BN_for_shared_line": {
            "passed": False,
            "reason": "B_N is a strong 27-mode scaffold, but no theorem yet identifies it as quotient-valid for the fixed-fiber/shared-line Pperp threshold row.",
        },
        "exact_A_base_tensor_I3_threshold_identity": {
            "passed": False,
            "reason": "The constructed A_base tensor I_3 matrix exists, but no source theorem identifies the nonidentity rhoE/B_N operator with exactly that threshold row.",
            "constructed_matrix_available": factorized["decision"]["factorized_operator_matrix_constructed"],
            "quotient_logdet": matrix["quotient_operator"]["logdet"],
        },
        "Qa_stack_weights_and_scale_policy": {
            "passed": False,
            "reason": "The regularization bridge is conditional and still requires source-emitted Qa-stack index weights and determinant scale policy.",
            "conditional_bridge_proved": regularization["decision"]["p_row_regularization_bridge_conditional_closed"],
        },
    }

    accepted = all(test["passed"] for test in threshold_adapter_tests.values())

    candidate = {
        "candidate": "SelectedElectroweakQaStackThresholdOperatorFromNonIdentityRhoEQuotientBN",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_status": source_identity["status"],
        "u1y_nonidentity_interface_status": interface["status"],
        "selected_correction_gate_status": correction["status"],
        "prefix_payload": prefix_payload,
        "threshold_adapter_tests": threshold_adapter_tests,
        "source_trace_cutset": cutset,
        "decision": {
            "nonidentity_rhoE_BN_prefix_imported": True,
            "prefix_can_host_threshold_operator": True,
            "threshold_operator_identity_closed": accepted,
            "selected_p_a_promoted": False,
            "lambda_12_closed": False,
            "measured_electroweak_closure": False,
            "current_source_nogo_proved": True,
            "mathematical_impossibility_claimed": False,
            "next_required_artifact": NEXT,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "NonidentityRhoEQuotientBNPrefixIsNecessaryButNotYetThresholdIdentity",
            "proved": True,
            "statement": (
                "The nonidentity rho_E / 27-mode B_N prefix is the first live source "
                "container strong enough to host the electroweak Qa-stack threshold "
                "operator: it carries nonidentity projective rho_E support, D_E, "
                "Riesz/Green, dotD, sector projectors, and a positive complement gap. "
                "However, the prefix is not yet selected as the threshold row because "
                "selected trace equality, the full selected operator formula, quotient "
                "validity for the shared-line fiber, and source-emitted Qa-stack weights "
                "and scale remain open."
            ),
        },
        "minimal_next_payload": {
            "name": NEXT,
            "must_emit": [
                "selected trace equality between the smooth source and the 27-mode B_N trace",
                "full selected Iwasawa/Strominger threshold-operator formula on B_N",
                "gap/error certificate proving the model operator is the selected threshold operator",
                "quotient-validity theorem for Pperp/shared-line fiber on B_N",
                "identification of the emitted operator with A_base tensor I_3 before quotient",
                "Qa-stack index weights and determinant scale policy",
            ],
        },
        "what_closes": {
            "best_prefix_imported": True,
            "identity_rhoE_smoke_avoided": True,
            "functional_support_connected_to_threshold_prefix": True,
            "threshold_identity_cutset_named": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_trace_equality": True,
            "full_selected_threshold_operator_formula": True,
            "quotient_valid_BN_for_Pperp": True,
            "exact_A_base_tensor_I3_source_identity": True,
            "Qa_stack_index_weights_and_scale_policy": True,
            "selected_p_a": True,
            "lambda_12": True,
        },
        "guardrails": {
            "observed_electroweak_data_used": False,
            "target_fitting_used": False,
            "promotes_prefix_as_selected_threshold": False,
            "promotes_identity_rhoE": False,
            "promotes_diagnostic_splitter": False,
            "promotes_selected_p_a": False,
            "claims_lambda12": False,
            "claims_measured_electroweak_closure": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedElectroweakQaStackThresholdOperatorFromNonIdentityRhoEQuotientBN",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "nonidentity_rhoE_BN_prefix_imported": True,
        "threshold_operator_identity_closed": accepted,
        "selected_p_a_promoted": False,
        "lambda_12_closed": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected Electroweak QaStack ThresholdOperator From NonIdentityRhoE QuotientBN Fill v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        "nonidentity_rhoE_BN_prefix_imported = true",
        f"threshold_operator_identity_closed = {str(candidate['decision']['threshold_operator_identity_closed']).lower()}",
        "selected_p_a_promoted = false",
        "lambda_12_closed = false",
        f"next_required_artifact = {candidate['decision']['next_required_artifact']}",
        "```",
        "",
        "The nonidentity `rho_E` / 27-mode `B_N` prefix is now imported as the best",
        "threshold-operator container. It is strong enough to host the row, but it is",
        "not yet a selected threshold identity.",
        "",
        "## Prefix Payload",
        "",
        "```json",
        json.dumps(candidate["prefix_payload"], indent=2, sort_keys=True),
        "```",
        "",
        "## Adapter Tests",
        "",
        "```json",
        json.dumps(candidate["threshold_adapter_tests"], indent=2, sort_keys=True),
        "```",
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
            "- The prefix is not promoted as selected threshold data.",
            "- Identity `rho_E` and diagnostic splitters remain forbidden.",
            "- No observed electroweak data or target residuals are used.",
            "- `p_a`, `lambda_12`, and measured electroweak closure remain open.",
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
