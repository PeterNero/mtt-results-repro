"""Build the U1/Y Route-C finite HYM solve or typed Cech payload gate."""

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

INPUTS = {
    "u1y_witness_contract": DATA / "selected_u1y_routec_typed_monad_cech_or_hym_connection_witness.candidate.json",
    "q79_trace_gap_layer": Q79 / "certificates" / "q79_selected_trace_equals_emitted_27mode_operator_or_full_hym_newton_replay_certificate.json",
    "q79_alpha1_kernel": Q79 / "certificates" / "q79_selected_alpha1_tangent_or_retarded_overlap_kernel_certificate.json",
    "q79_physical_alpha1_value_fill": Q79 / "certificates" / "q79_selected_physical_alpha1_source_normalization_or_end0_sector_routing_value_fill_certificate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_finite_hym_connection_solve_or_typed_cech_payload.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_finite_hym_connection_solve_or_typed_cech_payload_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_FiniteHYMConnectionSolve_or_TypedCechPayload_v1.md"

STATUS = "U1Y_ROUTEC_FINITE_HYM_SOLVE_PROMOTES_DE_GAP_LAYER_DOTD_ALPHA1_SOURCE_OPEN"
NEXT = "Selected_U1Y_RouteC_dotDAlpha1_SourceNormalization_or_End0SectorRouting_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def status_of(key: str, data: dict[str, Any]) -> dict[str, Any]:
    return {
        "path": rel(INPUTS[key]),
        "present": INPUTS[key].exists(),
        "status": data.get("status", "UNKNOWN"),
        "next_required_artifact": data.get("next_required_artifact"),
        "guardrails": data.get("guardrails"),
    }


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    parent = load(INPUTS["u1y_witness_contract"])
    q79_trace = load(INPUTS["q79_trace_gap_layer"])
    q79_alpha1 = load(INPUTS["q79_alpha1_kernel"])
    q79_alpha1_value = load(INPUTS["q79_physical_alpha1_value_fill"])

    gap = q79_trace["selected_trace_equality_gap_layer_proof"]
    alpha1_formula = q79_alpha1["analytic_variational_kernel_formula"]

    promoted_payload = {
        "finite_basis_BN": {
            "basis_id": gap["gap_layer"]["basis_id"],
            "basis_dimension": gap["gap_layer"]["basis_dimension"],
            "selected_trace_equality_proved": gap["selected_trace_equality"]["proved"],
        },
        "DE_action": {
            "selected_trace_equality": gap["selected_trace_equality"],
            "D_E_source_flags_are_theorem_derived": gap["gap_layer"]["D_E_source_flags_are_theorem_derived"],
            "D_E_honest_replay_passes_after_theorem_derived_source_flags": gap["gap_layer"]["D_E_honest_replay_passes_after_theorem_derived_source_flags"],
        },
        "riesz_gap": {
            "selected_eta_N": gap["gap_layer"]["selected_eta_N"],
            "eta_threshold": gap["gap_layer"]["eta_threshold"],
            "model_gap_gamma_N": gap["gap_layer"]["model_gap_gamma_N"],
            "selected_gap_lower_bound": gap["gap_layer"]["selected_gap_lower_bound"],
        },
        "reduced_green": {
            "Riesz_Green_layer_closes": gap["gap_layer"]["Riesz_Green_layer_closes"],
            "selected_green_norm_bound": gap["gap_layer"]["selected_green_norm_bound"],
        },
    }

    still_open_payload = {
        "nonidentity_selected_rhoE_boundary_matrices": "projective-flat active trace supports D_E, but boundary matrices are not separately selected as a full operator payload",
        "local_A01_or_discrete_connection_variables": "full connection lift remains open",
        "routec_residual_values": "not promoted beyond D_E gap layer",
        "selection_functional_or_positive_hessian_gap": "positive D_E complement gap closed; full selected connection Hessian/source functional remains open",
        "dotD_alpha1": "same-basis matrices exist, analytic formula proved, selected tangent/source normalization open",
        "primitive_C1_contractions": "canonical finite C1 zero-response no-go imported; selected primitive/non-invariant C1 values open",
    }

    decision = {
        "most_promising_route": "finite_routec_hym_solve",
        "finite_DE_gap_layer_promoted": gap["status"] == "SELECTED_TRACE_EQUALITY_AND_DE_GAP_LAYER_PROVED",
        "finite_basis_BN_closed": True,
        "DE_action_closed_for_gap_layer": True,
        "Riesz_Green_gap_layer_closed": True,
        "full_finite_HYM_connection_solve_closed": False,
        "typed_cech_payload_filled": False,
        "dotD_alpha1_source_closed": False,
        "analytic_alpha1_kernel_formula_proved": alpha1_formula["status"] == "ANALYTIC_FORMULA_PROVED_SELECTED_TANGENT_VALUES_OPEN",
        "selected_alpha1_value_fill_closed": False,
        "End0_sector_routing_values_open": True,
        "primitive_C1_values_computed": False,
        "A_selected_or_b_selected_emitted": False,
        "lambda_12_computable": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    theorem = {
        "name": "U1YRouteCFiniteHYMConnectionSolvePartialPromotionTheorem",
        "proved": True,
        "statement": (
            "Along the finite Route-C/HYM route, the selected 27-mode D_E "
            "gap/Riesz/Green layer can now be promoted locally: the imported q79 "
            "selected trace theorem proves that the emitted D_E formula is the "
            "selected Phi_fin compression on B_N, with selected eta_N below the "
            "gap threshold and a Green norm bound. This does not close the full "
            "finite HYM connection solve: dotD_alpha1, the alpha1 source "
            "normalization or End0-to-sector routing values, full connection lift, "
            "primitive C1 contractions, A_selected, b_selected, lambda_12, and SM "
            "closure remain open."
        ),
    }

    candidate = {
        "candidate": "SelectedU1YRouteCFiniteHYMConnectionSolveOrTypedCechPayload",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            key: status_of(key, data)
            for key, data in {
                "u1y_witness_contract": parent,
                "q79_trace_gap_layer": q79_trace,
                "q79_alpha1_kernel": q79_alpha1,
                "q79_physical_alpha1_value_fill": q79_alpha1_value,
            }.items()
        },
        "promoted_finite_routec_payload": promoted_payload,
        "still_open_finite_routec_payload": still_open_payload,
        "alpha1_frontier": {
            "kernel_status": q79_alpha1["status"],
            "value_fill_status": q79_alpha1_value["status"],
            "analytic_formula": alpha1_formula,
            "next_required_artifact_from_q79": q79_alpha1_value["next_required_artifact"],
        },
        "decision": decision,
        "theorem": theorem,
        "what_closes_now": {
            "selected_trace_equality_for_27mode_DE_imported": True,
            "finite_BN_basis_closed_for_gap_layer": True,
            "DE_action_closed_for_gap_layer": True,
            "Riesz_Green_gap_layer_closed": True,
            "selected_green_norm_bound_imported": True,
            "analytic_alpha1_kernel_imported_as_ready_once_tangent_exists": True,
            "most_promising_route_advanced_without_target_fit": True,
        },
        "what_remains_open": {
            "selected_dotD_alpha1_source": True,
            "selected_alpha1_source_normalization": True,
            "selected_End0_to_sector_functor_values": True,
            "honest_dotD_replay_without_lifted_flags": True,
            "full_HYM_connection_lift": True,
            "finite_operator_payload_beyond_gap_layer": True,
            "selected_primitive_C1_contractions": True,
            "A_selected": True,
            "b_selected": True,
            "lambda_12": True,
            "Yukawa_or_full_SM_closure": True,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
        "guardrails": {
            "claims_full_finite_HYM_connection_solve_closed": False,
            "claims_typed_cech_payload_filled": False,
            "claims_dotD_alpha1_source_closed": False,
            "claims_primitive_C1_values_computed": False,
            "claims_A_selected_or_b_selected": False,
            "claims_lambda12": False,
            "claims_full_sm_closure": False,
            "promotes_dotD_value_matrices_without_alpha1_source": False,
            "uses_observed_or_benchmark_inputs": False,
        },
    }

    cert = {
        "certificate": "SelectedU1YRouteCFiniteHYMConnectionSolveOrTypedCechPayload",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "finite_DE_gap_layer_promoted": decision["finite_DE_gap_layer_promoted"],
        "finite_basis_BN_closed": decision["finite_basis_BN_closed"],
        "DE_action_closed_for_gap_layer": decision["DE_action_closed_for_gap_layer"],
        "Riesz_Green_gap_layer_closed": decision["Riesz_Green_gap_layer_closed"],
        "selected_gap_lower_bound": promoted_payload["riesz_gap"]["selected_gap_lower_bound"],
        "selected_green_norm_bound": promoted_payload["reduced_green"]["selected_green_norm_bound"],
        "analytic_alpha1_kernel_formula_proved": decision["analytic_alpha1_kernel_formula_proved"],
        "dotD_alpha1_source_closed": False,
        "primitive_C1_values_computed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected U1Y Route-C FiniteHYMConnectionSolve or TypedCechPayload v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"finite_DE_gap_layer_promoted = {str(cert['finite_DE_gap_layer_promoted']).lower()}",
        f"DE_action_closed_for_gap_layer = {str(cert['DE_action_closed_for_gap_layer']).lower()}",
        f"Riesz_Green_gap_layer_closed = {str(cert['Riesz_Green_gap_layer_closed']).lower()}",
        f"selected_gap_lower_bound = {cert['selected_gap_lower_bound']}",
        f"selected_green_norm_bound = {cert['selected_green_norm_bound']}",
        f"analytic_alpha1_kernel_formula_proved = {str(cert['analytic_alpha1_kernel_formula_proved']).lower()}",
        f"dotD_alpha1_source_closed = {str(cert['dotD_alpha1_source_closed']).lower()}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "The most promising route advanced: the selected D_E gap/Riesz/Green",
        "layer is now locally promoted from the q79 selected trace theorem.",
        "The full finite HYM solve is still not closed, because the next object",
        "is the selected dotD_alpha1 source normalization or End0-to-sector routing.",
        "",
        "## Promoted Payload",
        "",
        "```json",
        json.dumps(candidate["promoted_finite_routec_payload"], indent=2, sort_keys=True),
        "```",
        "",
        "## Still Open",
        "",
    ]
    for key, value in candidate["still_open_finite_routec_payload"].items():
        lines.append(f"- `{key}`: {value}")
    lines.extend(
        [
            "",
            "## Guardrails",
            "",
            "- This closes only the D_E gap/Riesz/Green layer.",
            "- Do not promote same-basis dotD matrices until alpha1 source normalization or End0-sector routing is selected.",
            "- Do not infer primitive C1, lambda_12, Yukawa, or full SM closure.",
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
