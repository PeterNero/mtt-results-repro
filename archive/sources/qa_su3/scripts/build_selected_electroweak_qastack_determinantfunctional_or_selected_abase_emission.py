"""Build the determinant-functional source theorem or selected A_base emission gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "quotient_functor_gate": DATA / "selected_electroweak_qastack_quotient_functor_and_abase_identity.candidate.json",
    "determinant_template": DATA / "selected_electroweak_u1y_determinant_functional_source_theorem.template.json",
    "determinant_weighting_nogo": DATA / "selected_electroweak_u1y_determinantfunctional_weighting_or_nogo.candidate.json",
    "quotient_determinant_lemma": DATA / "selected_electroweak_u1y_quotientdeterminant_lemma.candidate.json",
    "factorized_attempt": DATA / "selected_electroweak_u1y_factorized_threshold_operator_source_attempt.candidate.json",
    "localdet_gaplayer": DATA / "selected_electroweak_u1y_localdeterminant_from_27mode_de_gaplayer.candidate.json",
    "regularization_bridge": DATA / "selected_electroweak_qastack_sourceidentity_and_prow_regularization.candidate.json",
    "u1_su2_threshold_index": DATA / "u1_su2_threshold_index_source_theorem.candidate.json",
}

OUTPUT_DATA = DATA / "selected_electroweak_qastack_determinantfunctional_or_selected_abase_emission.candidate.json"
OUTPUT_CERT = CERTS / "selected_electroweak_qastack_determinantfunctional_or_selected_abase_emission_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Electroweak_QaStack_DeterminantFunctional_SourceTheorem_or_SelectedAbaseEmission_v1.md"

STATUS = "ELECTROWEAK_QASTACK_DETERMINANTFUNCTIONAL_OR_SELECTED_ABASE_EMISSION_GATE_BUILT_VALUES_OPEN"
NEXT = "Selected_Electroweak_QaStack_Minimal_SelectedFinitePart_Payload_Fill_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    quotient_gate = load(INPUTS["quotient_functor_gate"])
    template = load(INPUTS["determinant_template"])
    weighting = load(INPUTS["determinant_weighting_nogo"])
    quotient = load(INPUTS["quotient_determinant_lemma"])
    factorized = load(INPUTS["factorized_attempt"])
    localdet = load(INPUTS["localdet_gaplayer"])
    regularization = load(INPUTS["regularization_bridge"])
    threshold_index = load(INPUTS["u1_su2_threshold_index"])

    quotient_logdet = quotient["decision"]["quotient_logdet"]
    source_identity = factorized["source_identity"]
    weighting_decision = weighting["decision"]
    quotient_decision = quotient["decision"]
    regularization_decision = regularization["decision"]

    route_a_selected_abase_emission = {
        "name": "selected_A_base_tensor_I3_emission",
        "purpose": "Promote the constructed tensor-identity row as the selected electroweak Qa-stack threshold operator.",
        "already_available": {
            "matrix_constructed": factorized["decision"]["factorized_operator_matrix_constructed"],
            "quotient_matrix_constructed": factorized["decision"]["quotient_operator_matrix_constructed"],
            "same_source_as_27mode_DE_gap_layer": source_identity["same_source_as_27mode_DE_gap_layer"],
            "same_source_as_Pperp_trace_policy": source_identity["same_source_as_Pperp_trace_policy"],
            "Pperp_quotient_functor_closed_for_tensor_identity": quotient_gate["decision"]["tensor_identity_quotient_functor_closed"],
            "quotient_logdet": quotient_logdet,
        },
        "missing_selected_fields": {
            "factorized_matrix_emitted_by_prior_source": source_identity["factorized_matrix_emitted_by_prior_source"],
            "selected_source_emission_closed": factorized["decision"]["selected_source_emission_closed"],
            "hypercharge_index_Dynkin_weights_closed": factorized["decision"]["hypercharge_index_Dynkin_weights_closed"],
            "typed_convention_map_closed": factorized["decision"]["typed_convention_map_closed"],
            "Qa_stack_weights_and_scale_policy_closed": regularization_decision["source_identity_closed"],
        },
        "route_closed_now": False,
        "blocker": "The exact matrix is constructed and quotient algebra is closed, but the same branch has not emitted it as selected source data.",
    }

    route_b_direct_bn_functional = {
        "name": "direct_selected_determinant_functional_on_BN",
        "purpose": "Avoid proving A_base identity by emitting the finite-part determinant functional directly on selected B_N.",
        "already_available": {
            "selected_27mode_DE_gap_trace_equality": localdet["closed_27mode_prefix"]["selected_trace_equality_for_27mode_DE"],
            "positive_model_complement_spectrum_available": localdet["decision"]["positive_model_complement_spectrum_available"],
            "Pperp_domain_policy_closed": weighting["selected_support"]["Pperp_domain_policy_closed"],
            "conditional_Pperp_weighted_logdet": weighting_decision["conditional_Pperp_weighted_logdet"],
            "determinant_template_schema": template["schema"],
        },
        "missing_selected_fields": {
            "determinant_functional_source_theorem_found": weighting_decision["determinant_functional_source_theorem_found"],
            "sector_restriction_to_V_mod_s": template["functional_components"]["sector_restriction_to_V_mod_s"],
            "kernel_policy": template["functional_components"]["kernel_policy"],
            "H_zero_cluster_policy": template["functional_components"]["H_zero_cluster_policy"],
            "regularization_finite_part": template["functional_components"]["regularization_finite_part"],
            "hypercharge_index_Dynkin_weights": template["functional_components"]["hypercharge_index_Dynkin_weights"],
            "same_scheme_SU2_row_or_cancellation": template["functional_components"]["same_scheme_SU2_row_or_cancellation"],
        },
        "route_closed_now": False,
        "blocker": "The selected B_N gap layer and conditional spectrum exist, but no same-source theorem defines the determinant finite part on V/<s>.",
    }

    route_comparison = {
        "recommended_next_route": "direct_selected_determinant_functional_on_BN",
        "reason": (
            "Route B needs a finite-part functional on an already selected B_N/D_E gap layer, "
            "whereas Route A must additionally prove equality to the separately constructed "
            "A_base tensor I_3 matrix. Route A remains a useful validator once Route B emits "
            "a finite-part table."
        ),
        "route_a_can_close_if": [
            "same source emits exact A_base tensor I_3",
            "source emits hypercharge/index/Dynkin or Qa-stack determinant weights",
            "source emits internal determinant scale",
        ],
        "route_b_can_close_if": [
            "same source defines finite positive zeta/logdet on V/<s>",
            "source specifies zero-cluster/kernel policy",
            "source specifies index weights and scale",
            "same-scheme SU2 row or cancellation is supplied before lambda_12",
        ],
    }

    minimal_payload = {
        "schema": "SelectedElectroweakQaStackMinimalSelectedFinitePartPayload.v1",
        "must_emit": {
            "source_identity": {
                "selected_by_mtt": None,
                "same_branch_q79_F_m1": None,
                "no_observed_or_benchmark_inputs": None,
                "source_certificate": None,
            },
            "domain_and_operator": {
                "selected_B_N_basis_id": "F3xF3_gerbe_twisted_fourier_N1_rank3",
                "sector_restriction_to_V_mod_s": None,
                "operator_choice": "A_base_tensor_I3_emission_or_direct_BN_finite_part",
                "positive_eigenvalue_table_on_V_mod_s": None,
                "kernel_policy": None,
                "H_zero_cluster_policy": None,
            },
            "finite_part": {
                "regularization": None,
                "index_weights": None,
                "determinant_scale": None,
                "p_a_value": None,
            },
            "electroweak_completion_only_after_payload": {
                "same_scheme_SU2_row_or_cancellation": None,
                "lambda12_formula": None,
            },
        },
        "forbidden": template["forbidden_inputs"]
        + [
            "promote constructed A_base matrix without source emission",
            "promote Pperp trace index as determinant finite part",
            "compute lambda_12 before same-scheme SU2 row or cancellation",
        ],
    }

    candidate = {
        "candidate": "SelectedElectroweakQaStackDeterminantFunctionalOrSelectedAbaseEmission",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_status": quotient_gate["status"],
        "route_a_selected_abase_emission": route_a_selected_abase_emission,
        "route_b_direct_bn_functional": route_b_direct_bn_functional,
        "route_comparison": route_comparison,
        "minimal_next_payload": minimal_payload,
        "decision": {
            "route_a_selected_abase_emission_closed": False,
            "route_b_direct_bn_functional_closed": False,
            "minimal_selected_finite_part_payload_written": True,
            "conditional_quotient_logdet_carried": quotient_logdet,
            "conditional_quotient_logdet_promoted": False,
            "Pperp_weighting_promoted": False,
            "selected_p_a_promoted": False,
            "lambda_12_closed": False,
            "measured_electroweak_closure": False,
            "current_source_nogo_proved": True,
            "mathematical_impossibility_claimed": False,
            "target_fitting_used": False,
            "next_required_artifact": NEXT,
        },
        "theorem": {
            "name": "ElectroweakQaStackFinitePartClosureRequiresOneOfTwoSelectedSourceTheorems",
            "proved": True,
            "statement": (
                "Given the closed selected 27-mode D_E gap layer, Pperp domain policy, "
                "and tensor-identity quotient lemma, electroweak Qa-stack p_a can be "
                "promoted only by one of two selected same-source theorems: either "
                "the source emits the exact A_base tensor I_3 threshold row, or it "
                "emits a direct finite zeta/heat/torsion determinant functional on "
                "the selected B_N quotient domain V/<s>. The current source emits "
                "neither theorem, so the conditional logdet remains support only."
            ),
        },
        "what_closes": {
            "two_legal_closure_routes_separated": True,
            "minimal_selected_finite_part_payload_written": True,
            "recommended_route_ranked": True,
            "forbidden_shortcuts_carried": True,
        },
        "what_remains_open": {
            "selected_A_base_tensor_I3_emission": True,
            "direct_selected_BN_finite_part_theorem": True,
            "selected_index_weights": True,
            "selected_determinant_scale": True,
            "same_scheme_SU2_row_or_cancellation": True,
            "selected_p_a": True,
            "lambda_12": True,
        },
        "guardrails": {
            "promotes_conditional_logdet": False,
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
        "certificate": "SelectedElectroweakQaStackDeterminantFunctionalOrSelectedAbaseEmission",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "route_a_selected_abase_emission_closed": False,
        "route_b_direct_bn_functional_closed": False,
        "minimal_selected_finite_part_payload_written": True,
        "conditional_quotient_logdet_carried": quotient_logdet,
        "selected_p_a_promoted": False,
        "lambda_12_closed": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected Electroweak QaStack DeterminantFunctional SourceTheorem or SelectedAbaseEmission v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        "route_a_selected_abase_emission_closed = false",
        "route_b_direct_bn_functional_closed = false",
        "minimal_selected_finite_part_payload_written = true",
        f"conditional_quotient_logdet_carried = {candidate['decision']['conditional_quotient_logdet_carried']}",
        "selected_p_a_promoted = false",
        "lambda_12_closed = false",
        f"next_required_artifact = {candidate['decision']['next_required_artifact']}",
        "```",
        "",
        "Both legal closure routes are now explicit. Route A promotes the constructed",
        "`A_base tensor I_3` row only if it is emitted by the selected source. Route B",
        "bypasses `A_base` by emitting the determinant finite part directly on selected",
        "`B_N` over `V/<s>`. Route B is ranked as the better next attack.",
        "",
        "## Route A",
        "",
        "```json",
        json.dumps(candidate["route_a_selected_abase_emission"], indent=2, sort_keys=True),
        "```",
        "",
        "## Route B",
        "",
        "```json",
        json.dumps(candidate["route_b_direct_bn_functional"], indent=2, sort_keys=True),
        "```",
        "",
        "## Minimal Next Payload",
        "",
        "```json",
        json.dumps(candidate["minimal_next_payload"], indent=2, sort_keys=True),
        "```",
        "",
        "## Theorem",
        "",
        candidate["theorem"]["statement"],
        "",
        "## Guardrails",
        "",
        "- The conditional quotient logdet is not promoted.",
        "- The constructed `A_base` matrix is not promoted as selected.",
        "- `P_perp` remains a domain/trace policy, not a finite-part theorem.",
        "- `p_a`, `lambda_12`, and measured electroweak closure remain open.",
        "",
        "## Certificate",
        "",
        "```json",
        json.dumps(cert, indent=2, sort_keys=True),
        "```",
        "",
    ]
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
