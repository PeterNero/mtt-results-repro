"""Build the U1/Y Route-C selected source certificate or typed D_E gate."""

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
SM = TEXPAPERS / "mtt-sm-parity-closure"

INPUTS = {
    "u1y_visible_operator_or_primitive_c1_gate": DATA / "selected_u1y_routec_selected_visible_operator_source_or_primitive_c1_contractions.candidate.json",
    "q79_routec_source_or_typed_de": Q79 / "certificates" / "q79_routec_selected_source_certificate_or_typed_de_construction_certificate.json",
    "q79_typed_monad_cech_or_hym_witness": Q79 / "certificates" / "q79_typed_monad_cech_or_hym_connection_witness_certificate.json",
    "q79_finite_connection_solve_execution": Q79 / "certificates" / "q79_selected_finite_connection_solve_execution_certificate.json",
    "sm_orientation_carrying_de_dotd_source": SM / "certificates" / "selected_orientation_carrying_de_dotd_source_certificate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_selected_source_certificate_or_typed_de_construction.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_selected_source_certificate_or_typed_de_construction_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_SelectedSourceCertificate_or_TypedDEConstruction_v1.md"

STATUS = "U1Y_ROUTEC_SELECTED_SOURCE_OR_TYPED_DE_REDUCED_CONNECTION_WITNESS_OPEN"
NEXT = "Selected_U1Y_RouteC_TypedMonadCech_or_HYMConnectionWitness_v1"


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
        "next_required_artifact": data.get("next_required_artifact") or data.get("primary_next_artifact"),
        "guardrails": data.get("guardrails"),
    }


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    local_parent = load(INPUTS["u1y_visible_operator_or_primitive_c1_gate"])
    q79_source = load(INPUTS["q79_routec_source_or_typed_de"])
    q79_witness = load(INPUTS["q79_typed_monad_cech_or_hym_witness"])
    q79_finite = load(INPUTS["q79_finite_connection_solve_execution"])
    sm_source = load(INPUTS["sm_orientation_carrying_de_dotd_source"])

    finite_summary = q79_finite["finite_connection_execution_import_summary"]
    witness_search = q79_witness["corpus_witness_search_summary"]
    witness_attempt = q79_witness["selected_connection_witness_attempt"]
    smoke_nogo = q79_witness["routec_smoke_promotion_nogo"]
    minimal_payload = q79_witness["minimal_actual_witness_payload"]

    route_evaluation = q79_source["route_evaluation"]
    selected_connection_contract = q79_source["selected_connection_witness_contract"]
    typed_de_contract = q79_source["typed_de_witness_contract"]

    decision = {
        "selected_routec_source_certificate_closed": False,
        "typed_DE_construction_closed": False,
        "selected_connection_witness_values_absent": witness_attempt["status"].endswith("VALUES_ABSENT"),
        "typed_monad_cech_witness_constructed": False,
        "selected_hym_connection_constructed": False,
        "identity_rhoE_smoke_promoted": False,
        "finite_connection_prefix_values_present": finite_summary["status"] == "FINITE_PREFIX_VALUES_IMPORTED_SOURCE_PROMOTION_OPEN",
        "finite_prefix_has_nonidentity_rhoE_candidate": finite_summary["nonidentity_rhoE"]["nonidentity_projective_rhoE_candidate_built"],
        "finite_prefix_DE_on_27_mode_BN_emitted": finite_summary["DE"]["D_E_matrix_on_27_mode_BN_emitted"],
        "finite_prefix_dotD_alpha1_same_basis_emitted": finite_summary["dotD"]["dotD_alpha1_matrix_in_same_basis_emitted"],
        "finite_prefix_canonical_C1_engine_built": finite_summary["C1"]["primitive_C1_contraction_engine_built"],
        "current_routec_arithmetic_no_hidden_obstruction_under_hypothetical_flags": local_parent["decision"]["current_routec_arithmetic_passes_if_selected_flags_supplied"],
        "selected_finite_connection_solve_closed": False,
        "primitive_C1_values_computed": False,
        "A_selected_or_b_selected_emitted": False,
        "lambda_12_computable": False,
        "full_SM_closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    reduction = {
        "local_parent_gate": {
            "status": local_parent["status"],
            "next_required_artifact": local_parent["next_required_artifact"],
            "primitive_c1_missing_atom_count": local_parent["decision"]["primitive_c1_missing_atom_count"],
            "subvalidators": {
                "selected_ordered_source": local_parent["decision"]["selected_ordered_source_subvalidator_passes"],
                "selected_s3_class_restriction": local_parent["decision"]["selected_s3_class_subvalidator_passes"],
            },
        },
        "q79_source_or_typed_DE_reduction": {
            "status": q79_source["status"],
            "next_required_artifact": q79_source["next_required_artifact"],
            "route_evaluation": route_evaluation,
            "selected_connection_witness_contract": selected_connection_contract,
            "typed_DE_witness_contract": typed_de_contract,
            "what_remains_open": q79_source["what_remains_open"],
        },
        "q79_witness_search": {
            "status": q79_witness["status"],
            "search_status": witness_search["status"],
            "best_next_route_from_hunt": witness_search["best_next_route_from_hunt"],
            "selected_D_E_source_found": witness_search["selected_D_E_source_found"],
            "not_recovered_witness_values": witness_search["not_recovered_witness_values"],
            "selected_connection_witness_attempt": witness_attempt,
            "routec_smoke_promotion_nogo": smoke_nogo,
            "minimal_actual_witness_payload": minimal_payload,
        },
        "finite_connection_prefix": {
            "status": q79_finite["status"],
            "prefix_status": finite_summary["status"],
            "smooth_BN": finite_summary["smooth_BN"],
            "nonidentity_rhoE": finite_summary["nonidentity_rhoE"],
            "DE": finite_summary["DE"],
            "dotD": finite_summary["dotD"],
            "C1": finite_summary["C1"],
            "first_HYM_correction": finite_summary["first_HYM_correction"],
            "honest_replay_cutset": q79_finite["honest_replay_cutset"],
            "next_required_artifact": q79_finite["next_required_artifact"],
        },
        "sm_orientation_source_alignment": {
            "status": sm_source["status"],
            "primary_next_artifact": sm_source["primary_next_artifact"],
            "what_closes": sm_source["what_closes"],
            "what_remains_open": sm_source["what_remains_open"],
        },
    }

    theorem = {
        "name": "U1YRouteCSelectedSourceCertificateOrTypedDEConstructionReductionTheorem",
        "proved": True,
        "statement": (
            "The selected U1/Y Route-C source-certificate gate is reduced to an "
            "actual selected connection witness. The imported q79 and SM parity "
            "certificates classify all current routes: selected source certificate, "
            "typed monad/Cech D_E, direct HYM connection, and finite Route-C solve. "
            "Finite 27-mode prefix values exist and show that the arithmetic and "
            "validator plumbing are ready, but they do not prove selected source "
            "provenance, selected trace equality, typed f/g Cech data, HYM "
            "connection coefficients, same-source Chern-Weil/GS row, or the 24 "
            "primitive C1 matrices. Therefore no closure follows yet; the next "
            "honest object is explicit typed monad/Cech data or a selected "
            "HYM/Route-C connection/residual witness emitted from the same branch."
        ),
    }

    candidate = {
        "candidate": "SelectedU1YRouteCSelectedSourceCertificateOrTypedDEConstruction",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            key: status_of(key, data)
            for key, data in {
                "u1y_visible_operator_or_primitive_c1_gate": local_parent,
                "q79_routec_source_or_typed_de": q79_source,
                "q79_typed_monad_cech_or_hym_witness": q79_witness,
                "q79_finite_connection_solve_execution": q79_finite,
                "sm_orientation_carrying_de_dotd_source": sm_source,
            }.items()
        },
        "decision": decision,
        "reduction": reduction,
        "theorem": theorem,
        "what_closes_now": {
            "all_current_source_or_typed_DE_routes_classified": True,
            "finite_prefix_values_imported_as_nonclosing_support": True,
            "identity_rhoE_smoke_rejected_as_source": True,
            "generic_constant_maps_phrase_rejected_as_typed_witness": True,
            "selected_connection_witness_contract_localized": True,
            "selected_trace_and_source_provenance_blocker_preserved": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "actual_typed_f_i_sections": True,
            "actual_typed_g_i_sections": True,
            "Cech_transitions_and_cocycle_data": True,
            "g_after_f_zero_and_exactness_certificate": True,
            "selected_HYM_connection_coefficients": True,
            "selected_RouteC_residual_values": True,
            "selected_trace_equality_to_27mode_operator": True,
            "theorem_derived_selected_source_flags": True,
            "same_source_ChernWeil_GS_row": True,
            "honest_selected_DE_Riesz_Green_dotD": True,
            "all_24_primitive_C1_3x3_matrices": True,
            "A_selected": True,
            "b_selected": True,
            "lambda_12": True,
            "Yukawa_or_full_SM_closure": True,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
        "guardrails": {
            "claims_selected_routec_source_certificate": False,
            "claims_typed_DE_construction": False,
            "claims_actual_selected_connection_witness_constructed": False,
            "claims_selected_HYM_connection_constructed": False,
            "claims_selected_finite_connection_solve_closed": False,
            "claims_primitive_C1_values_computed": False,
            "claims_A_selected_or_b_selected": False,
            "claims_lambda12": False,
            "claims_full_sm_closure": False,
            "promotes_diagnostic_selected_flags": False,
            "promotes_identity_rhoE_smoke": False,
            "uses_observed_or_benchmark_inputs": False,
        },
    }

    cert = {
        "certificate": "SelectedU1YRouteCSelectedSourceCertificateOrTypedDEConstruction",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "selected_connection_witness_values_absent": decision["selected_connection_witness_values_absent"],
        "finite_connection_prefix_values_present": decision["finite_connection_prefix_values_present"],
        "finite_prefix_DE_on_27_mode_BN_emitted": decision["finite_prefix_DE_on_27_mode_BN_emitted"],
        "finite_prefix_dotD_alpha1_same_basis_emitted": decision["finite_prefix_dotD_alpha1_same_basis_emitted"],
        "finite_prefix_canonical_C1_engine_built": decision["finite_prefix_canonical_C1_engine_built"],
        "selected_routec_source_certificate_closed": False,
        "typed_DE_construction_closed": False,
        "selected_finite_connection_solve_closed": False,
        "primitive_C1_values_computed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    finite = candidate["reduction"]["finite_connection_prefix"]
    witness = candidate["reduction"]["q79_witness_search"]
    lines = [
        "# Selected U1Y Route-C SelectedSourceCertificate or TypedDEConstruction v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"selected_connection_witness_values_absent = {str(cert['selected_connection_witness_values_absent']).lower()}",
        f"finite_connection_prefix_values_present = {str(cert['finite_connection_prefix_values_present']).lower()}",
        f"finite_prefix_DE_on_27_mode_BN_emitted = {str(cert['finite_prefix_DE_on_27_mode_BN_emitted']).lower()}",
        f"finite_prefix_dotD_alpha1_same_basis_emitted = {str(cert['finite_prefix_dotD_alpha1_same_basis_emitted']).lower()}",
        f"finite_prefix_canonical_C1_engine_built = {str(cert['finite_prefix_canonical_C1_engine_built']).lower()}",
        f"selected_routec_source_certificate_closed = {str(cert['selected_routec_source_certificate_closed']).lower()}",
        f"typed_DE_construction_closed = {str(cert['typed_DE_construction_closed']).lower()}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "This gate is a reduction, not a closure claim. The finite prefix has real",
        "operator values, but the same-source selected connection witness is still",
        "missing. The next proof object must emit typed monad/Cech data or a selected",
        "HYM/Route-C connection/residual witness from the selected branch.",
        "",
        "## Imported Finite Prefix",
        "",
        f"- basis: `{finite['smooth_BN']['basis_id']}`",
        f"- dimension: `{finite['smooth_BN']['dimension']}`",
        f"- complement gap: `{finite['smooth_BN']['complement_gap']}`",
        f"- nonidentity rhoE candidate built: `{finite['nonidentity_rhoE']['nonidentity_projective_rhoE_candidate_built']}`",
        f"- D_E on B_N emitted: `{finite['DE']['D_E_matrix_on_27_mode_BN_emitted']}`",
        f"- dotD alpha1 same basis emitted: `{finite['dotD']['dotD_alpha1_matrix_in_same_basis_emitted']}`",
        f"- canonical C1 contraction engine built: `{finite['C1']['primitive_C1_contraction_engine_built']}`",
        "",
        "## Missing Witness Values",
        "",
    ]
    for key, missing in witness["not_recovered_witness_values"].items():
        if missing:
            lines.append(f"- `{key}`")
    lines.extend(
        [
            "",
            "## Guardrails",
            "",
            "- Do not promote finite prefix values into selected source provenance.",
            "- Do not promote identity or diagnostic rhoE smoke.",
            "- Do not treat generic constant-map wording as typed monad/Cech sections.",
            "- Do not infer primitive C1, lambda_12, Yukawa, or SM closure from this gate.",
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
