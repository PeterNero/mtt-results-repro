"""Build the primitive C1 source-value theorem / noninvariant tensor gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "fill_or_nogo": DATA / "selected_u1y_routec_primitive_c1_atom_payload_fill_or_nogo.candidate.json",
    "missing_leaves": DATA / "selected_u1y_routec_primitive_c1_atom_payload_missing_leaves.json",
    "atom_interface": DATA / "selected_u1y_routec_primitive_c1_atom_emission_interface.candidate.json",
    "source_or_typed_de": DATA / "selected_u1y_routec_selected_source_certificate_or_typed_de_construction.candidate.json",
    "selected_finite_trace": DATA / "selected_u1y_routec_selected_finite_trace_source_or_nogo.candidate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_primitive_c1_sourcevalue_theorem_or_noninvariant_tensor.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_primitive_c1_sourcevalue_theorem_or_noninvariant_tensor_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_Primitive_C1_SourceValue_Theorem_or_NonInvariantTensor_v1.md"
OUTPUT_CONTRACT = DATA / "selected_u1y_routec_primitive_c1_sourcevalue_closure_contract.json"

STATUS = "U1Y_ROUTEC_PRIMITIVE_C1_SOURCEVALUE_THEOREM_OR_NONINVARIANT_TENSOR_GATE_BUILT_OPEN"
NEXT = "Selected_U1Y_RouteC_CanonicalZeroSelection_or_NonInvariantC1Tensor_Fill_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def count_by_kind(leaves: list[dict[str, Any]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for leaf in leaves:
        counts[leaf["kind"]] = counts.get(leaf["kind"], 0) + 1
    return counts


def build() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], str]:
    fill = load(INPUTS["fill_or_nogo"])
    missing = load(INPUTS["missing_leaves"])
    interface = load(INPUTS["atom_interface"])
    source_or_de = load(INPUTS["source_or_typed_de"])
    finite_trace = load(INPUTS["selected_finite_trace"])

    leaves = missing["missing_leaves"]
    leaf_counts = count_by_kind(leaves)
    canonical_zero = fill["canonical_zero_branch"]

    canonical_zero_selection_contract = {
        "route": "canonical_zero_selection",
        "currently_closed": False,
        "hypotheses": {
            "same_source_certificate_emits_canonical_tensor": False,
            "canonical_translation_invariant_tensor_selected_by_MTT": False,
            "selected_basis_transport_preserves_zero_response": False,
            "all_sector_bases_emitted": False,
            "homogeneous_zero_theorem_for_b_selected_emitted": False,
            "no_noninvariant_primitive_correction_survives": False,
            "same_source_id_matches_DE_Green_dotD_overlap": False,
        },
        "would_emit": {
            "all_24_atom_matrices": "zero 3x3 matrices",
            "b_selected": "zero vector by homogeneous-zero theorem",
            "A_selected": "zero matrix assembled from zero sector response blocks",
        },
        "closure_consequence": (
            "This would close the primitive C1 atom payload as a selected zero theorem, "
            "but it would also prove that this primitive C1 channel cannot by itself "
            "generate Yukawa hierarchy. Yukawa closure would then require another selected "
            "source term or a higher-order/nonprimitive channel."
        ),
    }

    noninvariant_tensor_contract = {
        "route": "selected_noninvariant_tensor",
        "currently_closed": False,
        "hypotheses": {
            "same_source_certificate_emits_noninvariant_primitive_tensor": False,
            "basis_transport_terms_emitted": False,
            "theta_overlap_variation_emitted": False,
            "left_right_higgs_zero_mode_responses_emitted": False,
            "explicit_vertex_emitted": False,
            "basis_connection_emitted": False,
            "inhomogeneous_row_emitted_or_zero_theorem": False,
            "validators_pass_without_observed_or_benchmark_inputs": False,
        },
        "would_emit": {
            "all_24_atom_matrices": "selected 3x3 matrices from one source",
            "b_selected": "selected row or selected zero theorem",
            "A_selected": "stacked matrix from the atom assembly theorem",
        },
        "closure_consequence": (
            "This is the only primitive C1 route that can still produce nonzero selected "
            "sector response matrices and therefore remains the primary flavor-closure route."
        ),
    }

    typed_connection_derivation_contract = {
        "route": "typed_monad_cech_or_hym_derivation",
        "currently_closed": False,
        "hypotheses": {
            "typed_f_g_sections_or_HYM_coefficients_emitted": False,
            "selected_Cech_transitions_or_connection_coefficients_emitted": False,
            "selected_zero_mode_bases_and_basis_transport_emitted": False,
            "primitive_overlap_integral_rule_emitted": False,
            "same_source_export_to_atom_payload_validated": False,
        },
        "would_emit": {
            "atom_payload": "direct values for the template",
            "source_certificate": "typed source provenance for all atom entries",
        },
        "closure_consequence": (
            "This route can close either the canonical zero theorem or the noninvariant tensor route, "
            "depending on what the selected typed data compute."
        ),
    }

    contract = {
        "schema": "SelectedU1YRouteCPrimitiveC1SourceValueClosureContract.v1",
        "status": "OPEN_SOURCE_VALUE_THEOREM_REQUIRED",
        "canonical_zero_selection": canonical_zero_selection_contract,
        "selected_noninvariant_tensor": noninvariant_tensor_contract,
        "typed_connection_derivation": typed_connection_derivation_contract,
        "acceptance_tests": [
            "all emitted atom matrices have shape 3x3 for sectors [u,d,e,nuD]",
            "one same_source_id covers source certificate, bases, atoms, and b row/zero theorem",
            "no observed masses, CKM/PMNS entries, benchmark Yukawas, lambda12 diagnostics, or locked columns appear as inputs",
            "canonical zero branch may close only if selected-zero hypotheses are theorem-derived",
            "noninvariant branch may close only if all six atom terms per sector are source-emitted",
        ],
    }

    route_ranking = [
        {
            "rank": 1,
            "route": "selected_noninvariant_tensor",
            "reason": "Only live primitive C1 route that can produce nonzero flavor data.",
            "closed": False,
        },
        {
            "rank": 2,
            "route": "canonical_zero_selection",
            "reason": "Strong finite diagnostic already exists, but selecting it would retire primitive C1 as a Yukawa hierarchy source.",
            "closed": False,
        },
        {
            "rank": 3,
            "route": "typed_connection_derivation",
            "reason": "Most rigorous source route, but currently blocked by typed sections/connection coefficients.",
            "closed": False,
        },
    ]

    decision = {
        "sourcevalue_contract_built": True,
        "canonical_zero_selection_closed": False,
        "canonical_zero_diagnostic_imported": canonical_zero["all_c1_matrices_zero_for_canonical_tensor"],
        "canonical_zero_overpromotion_blocked": True,
        "noninvariant_tensor_route_kept_primary": True,
        "typed_connection_derivation_route_kept_live": True,
        "missing_leaf_count_carried_forward": len(leaves),
        "primitive_C1_atoms_emitted": False,
        "A_selected_computable": False,
        "b_selected_computable": False,
        "lambda_12_computable": False,
        "Yukawa_or_full_SM_closure": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "SelectedU1YRouteCPrimitiveC1SourceValueTheoremOrNonInvariantTensor",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "fill_or_nogo": fill["status"],
            "atom_interface": interface["status"],
            "source_or_typed_de": source_or_de["status"],
            "selected_finite_trace": finite_trace["status"],
        },
        "missing_leaf_counts": leaf_counts,
        "route_ranking": route_ranking,
        "closure_contract_path": rel(OUTPUT_CONTRACT),
        "decision": decision,
        "theorem": {
            "name": "U1YRouteCPrimitiveC1SourceValueFrontierTheorem",
            "proved": True,
            "statement": (
                "The primitive C1 closure problem is now reduced to one source-value "
                "theorem with three legal realizations. Either MTT selects the canonical "
                "translation-invariant zero tensor and proves basis-transport plus a "
                "homogeneous-zero b row, or it emits a selected noninvariant primitive "
                "tensor with all basis-transport and response atoms, or the values are "
                "derived from typed monad/Cech/HYM connection data. The current corpus "
                "does not close any of these routes. The noninvariant tensor route is "
                "ranked primary for flavor closure, because selecting the canonical zero "
                "branch would close primitive C1 as zero and force Yukawa hierarchy to "
                "come from a different selected channel."
            ),
        },
        "what_closes_now": {
            "sourcevalue_closure_contract_written": True,
            "canonical_zero_selection_hypotheses_made_explicit": True,
            "noninvariant_tensor_acceptance_hypotheses_made_explicit": True,
            "typed_connection_derivation_hypotheses_made_explicit": True,
            "route_ranking_for_next_attack": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "canonical_zero_selection_theorem": True,
            "selected_noninvariant_primitive_tensor": True,
            "typed_connection_derivation_values": True,
            "selected_basis_transport": True,
            "inhomogeneous_row_or_homogeneous_zero_theorem": True,
            "A_selected": True,
            "b_selected": True,
            "lambda_12": True,
            "Yukawa_or_full_SM_closure": True,
        },
        "guardrails": {
            "claims_canonical_zero_selected": False,
            "claims_noninvariant_tensor_emitted": False,
            "claims_typed_connection_values_emitted": False,
            "claims_primitive_C1_values": False,
            "claims_A_selected": False,
            "claims_b_selected": False,
            "claims_lambda12": False,
            "claims_Yukawa_or_full_SM_closure": False,
            "uses_observed_data": False,
            "uses_benchmark_data": False,
            "uses_locked_target_columns": False,
            "uses_diagnostic_lambda12_values": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedU1YRouteCPrimitiveC1SourceValueTheoremOrNonInvariantTensor",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "closure_contract_path": rel(OUTPUT_CONTRACT),
        "note_path": rel(OUTPUT_NOTE),
        "sourcevalue_contract_built": True,
        "canonical_zero_selection_closed": False,
        "canonical_zero_diagnostic_imported": True,
        "noninvariant_tensor_route_kept_primary": True,
        "typed_connection_derivation_route_kept_live": True,
        "primitive_C1_atoms_emitted": False,
        "missing_leaf_count": len(leaves),
        "A_selected_computable": False,
        "b_selected_computable": False,
        "lambda_12_computable": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    return candidate, cert, contract, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected U1Y Route-C Primitive C1 SourceValue Theorem or NonInvariantTensor v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"sourcevalue_contract_built = {str(cert['sourcevalue_contract_built']).lower()}",
        f"canonical_zero_selection_closed = {str(cert['canonical_zero_selection_closed']).lower()}",
        f"noninvariant_tensor_route_kept_primary = {str(cert['noninvariant_tensor_route_kept_primary']).lower()}",
        f"typed_connection_derivation_route_kept_live = {str(cert['typed_connection_derivation_route_kept_live']).lower()}",
        f"missing_leaf_count = {cert['missing_leaf_count']}",
        f"A_selected_computable = {str(cert['A_selected_computable']).lower()}",
        f"b_selected_computable = {str(cert['b_selected_computable']).lower()}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "The current source-value theorem is not closed. The canonical zero branch",
        "is a valid diagnostic but remains unselected. The noninvariant tensor route",
        "is now the primary next attack if primitive C1 is to produce flavor data.",
        "",
        "## Route Ranking",
        "",
    ]
    for row in candidate["route_ranking"]:
        lines.append(f"- #{row['rank']} `{row['route']}`: {row['reason']}")
    lines.extend(
        [
            "",
            "## Guardrails",
            "",
            "- Do not promote canonical zero unless its selected-zero hypotheses are theorem-derived.",
            "- If canonical zero is selected, primitive C1 is not the Yukawa hierarchy source.",
            "- Do not fill any atom from observed masses, CKM/PMNS data, benchmark Yukawas, lambda12 diagnostics, or locked columns.",
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
    candidate, cert, contract, note = build()
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_CONTRACT.write_text(json.dumps(contract, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_CONTRACT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
