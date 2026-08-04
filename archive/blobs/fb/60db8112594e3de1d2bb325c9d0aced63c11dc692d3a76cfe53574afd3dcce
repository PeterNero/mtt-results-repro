"""Build the primitive C1 atom-payload fill/no-go gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "atom_interface": DATA / "selected_u1y_routec_primitive_c1_atom_emission_interface.candidate.json",
    "atom_template": DATA / "selected_u1y_routec_primitive_c1_atom_payload.template.json",
    "selected_finite_trace": DATA / "selected_u1y_routec_selected_finite_trace_source_or_nogo.candidate.json",
    "source_or_typed_de": DATA / "selected_u1y_routec_selected_source_certificate_or_typed_de_construction.candidate.json",
    "finite_hym_solve": DATA / "selected_u1y_routec_finite_hym_connection_solve_or_typed_cech_payload.candidate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_primitive_c1_atom_payload_fill_or_nogo.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_primitive_c1_atom_payload_fill_or_nogo_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_Primitive_C1_AtomPayload_Fill_or_NoGo_v1.md"
OUTPUT_MISSING = DATA / "selected_u1y_routec_primitive_c1_atom_payload_missing_leaves.json"

STATUS = "U1Y_ROUTEC_PRIMITIVE_C1_ATOMPAYLOAD_FILL_NOGO_CURRENT_CORPUS_VALUES_OPEN"
NEXT = "Selected_U1Y_RouteC_PrimitiveC1_SourceValue_Theorem_or_SelectedNonInvariantTensor_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def is_open_matrix(matrix: object) -> bool:
    return (
        isinstance(matrix, list)
        and len(matrix) == 3
        and all(isinstance(row, list) and len(row) == 3 and all(value is None for value in row) for row in matrix)
    )


def build_missing_leaves(template: dict[str, Any], terms: list[str]) -> list[dict[str, Any]]:
    leaves: list[dict[str, Any]] = []
    for sector, row in template["sectors"].items():
        leaves.extend(
            [
                {"path": f"sectors.{sector}.basis_left", "kind": "selected_basis", "required": row["slots"]["left"]},
                {"path": f"sectors.{sector}.basis_right", "kind": "selected_basis", "required": row["slots"]["right"]},
                {"path": f"sectors.{sector}.basis_higgs", "kind": "selected_basis", "required": row["slots"]["higgs"]},
            ]
        )
        for term in terms:
            leaves.append(
                {
                    "path": f"sectors.{sector}.atoms.{term}",
                    "kind": "primitive_c1_atom_matrix",
                    "shape": "3x3",
                    "required_source": "same selected source as D_E/Riesz/Green/dotD and overlap normalization",
                }
            )
        leaves.append(
            {
                "path": f"sectors.{sector}.inhomogeneous_row_or_homogeneous_zero_theorem",
                "kind": "b_selected_source",
                "shape": "3",
                "required_source": "same selected source as primitive atoms",
            }
        )
    return leaves


def build() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], str]:
    interface = load(INPUTS["atom_interface"])
    template = load(INPUTS["atom_template"])
    finite_trace = load(INPUTS["selected_finite_trace"])
    source_or_de = load(INPUTS["source_or_typed_de"])
    finite_hym = load(INPUTS["finite_hym_solve"])

    terms = interface["term_order"]
    sectors = interface["sector_order"]
    open_atom_count = sum(
        is_open_matrix(template["sectors"][sector]["atoms"][term])
        for sector in sectors
        for term in terms
    )
    missing_leaves = build_missing_leaves(template, terms)
    canonical_zero = finite_trace["smooth_27mode_lane"]["c1"]

    canonical_zero_branch = {
        "branch": "canonical_translation_invariant_tensor_zero_response",
        "all_c1_matrices_zero_for_canonical_tensor": canonical_zero["all_c1_matrices_zero_for_canonical_tensor"],
        "canonical_tensor_zero_response_result_proved_finitely": canonical_zero[
            "canonical_tensor_zero_response_result_proved_finitely"
        ],
        "primitive_engine_built": canonical_zero["primitive_engine_built"],
        "accepted_as_selected_atom_payload": False,
        "why_rejected": [
            "zero response is proved only for the canonical translation-invariant tensor branch",
            "the current corpus does not emit this branch as the selected primitive C1 tensor",
            "selected basis-transport/noninvariant primitive terms remain open",
            "same-source inhomogeneous row or homogeneous-zero theorem is absent",
        ],
    }

    fill_attempt = {
        "payload_schema": template["schema"],
        "basis_id_present": template["basis_id"] is not None,
        "same_source_id_present": template["same_source_id"] is not None,
        "source_certificate_present": template["source_certificate"] is not None,
        "open_atom_matrices": open_atom_count,
        "filled_atom_matrices": 24 - open_atom_count,
        "basis_leaf_count_missing": 12,
        "b_row_or_zero_theorem_missing_count": 4,
        "total_missing_leaf_count": len(missing_leaves),
        "can_compute_A_selected": False,
        "can_compute_b_selected": False,
    }

    decision = {
        "fill_attempt_executed": True,
        "current_corpus_supplies_selected_atom_payload": False,
        "canonical_zero_branch_tested": True,
        "canonical_zero_branch_rejected_as_closure": True,
        "primitive_C1_atoms_emitted": False,
        "emitted_atom_count": 0,
        "missing_atom_count": 24,
        "missing_leaf_count": len(missing_leaves),
        "A_selected_computable": False,
        "b_selected_computable": False,
        "lambda_12_computable": False,
        "Yukawa_or_full_SM_closure": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    missing_packet = {
        "schema": "SelectedU1YRouteCPrimitiveC1AtomPayloadMissingLeaves.v1",
        "status": "CURRENT_CORPUS_VALUES_OPEN",
        "source_requirements": interface["source_requirements"],
        "sector_order": sectors,
        "term_order": terms,
        "missing_leaves": missing_leaves,
        "minimal_closing_options": [
            "emit the selected noninvariant primitive C1 tensor and basis transport from the same selected source",
            "or prove the canonical translation-invariant zero tensor is selected, including same-source bases and homogeneous-zero row",
            "or derive all six atom matrices per sector directly from a typed monad/Cech/HYM connection witness",
        ],
    }

    candidate = {
        "candidate": "SelectedU1YRouteCPrimitiveC1AtomPayloadFillOrNoGo",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "atom_interface": interface["status"],
            "selected_finite_trace": finite_trace["status"],
            "source_or_typed_de": source_or_de["status"],
            "finite_hym_solve": finite_hym["status"],
        },
        "fill_attempt": fill_attempt,
        "canonical_zero_branch": canonical_zero_branch,
        "missing_leaves_path": rel(OUTPUT_MISSING),
        "decision": decision,
        "theorem": {
            "name": "U1YRouteCPrimitiveC1AtomPayloadCurrentCorpusNoGo",
            "proved": True,
            "statement": (
                "Applying the primitive C1 atom-emission interface to the current corpus "
                "does not fill the payload. The canonical finite tensor branch proves a "
                "zero-response result, but it is not emitted as the selected same-source "
                "primitive C1 atom payload and lacks the selected basis-transport plus "
                "inhomogeneous-row or homogeneous-zero theorem required to compute "
                "A_selected and b_selected. Therefore the current corpus gives a no-go "
                "for primitive C1 closure while preserving three legal closing options: "
                "select the canonical zero branch, emit a selected noninvariant primitive "
                "tensor/basis-transport branch, or derive the atoms from typed monad/Cech/"
                "HYM connection witness data."
            ),
        },
        "what_closes_now": {
            "current_payload_fill_attempt_executed": True,
            "canonical_zero_branch_audited": True,
            "canonical_zero_overpromotion_blocked": True,
            "minimal_missing_leaf_packet_written": True,
            "next_closing_options_identified": True,
        },
        "what_remains_open": {
            "selected_same_source_atom_payload": True,
            "selected_basis_transport": True,
            "selected_noninvariant_primitive_C1_tensor_or_selected_zero_theorem": True,
            "inhomogeneous_row_or_homogeneous_zero_theorem": True,
            "A_selected": True,
            "b_selected": True,
            "lambda_12": True,
            "Yukawa_or_full_SM_closure": True,
        },
        "guardrails": {
            "claims_primitive_C1_values": False,
            "claims_canonical_zero_branch_selected": False,
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
        "certificate": "SelectedU1YRouteCPrimitiveC1AtomPayloadFillOrNoGo",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "missing_leaves_path": rel(OUTPUT_MISSING),
        "note_path": rel(OUTPUT_NOTE),
        "fill_attempt_executed": True,
        "current_corpus_supplies_selected_atom_payload": False,
        "canonical_zero_branch_tested": True,
        "canonical_zero_branch_selected": False,
        "primitive_C1_atoms_emitted": False,
        "missing_atom_count": 24,
        "missing_leaf_count": len(missing_leaves),
        "A_selected_computable": False,
        "b_selected_computable": False,
        "lambda_12_computable": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    return candidate, cert, missing_packet, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected U1Y Route-C Primitive C1 AtomPayload Fill or NoGo v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"fill_attempt_executed = {str(cert['fill_attempt_executed']).lower()}",
        f"current_corpus_supplies_selected_atom_payload = {str(cert['current_corpus_supplies_selected_atom_payload']).lower()}",
        f"canonical_zero_branch_tested = {str(cert['canonical_zero_branch_tested']).lower()}",
        f"canonical_zero_branch_selected = {str(cert['canonical_zero_branch_selected']).lower()}",
        f"missing_atom_count = {cert['missing_atom_count']}",
        f"missing_leaf_count = {cert['missing_leaf_count']}",
        f"A_selected_computable = {str(cert['A_selected_computable']).lower()}",
        f"b_selected_computable = {str(cert['b_selected_computable']).lower()}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "The current corpus does not fill the primitive C1 atom payload. The canonical",
        "zero-response branch is real but remains diagnostic until it is selected by the",
        "same source and paired with selected bases plus the homogeneous-zero or",
        "inhomogeneous-row theorem.",
        "",
        "## Legal Closing Options",
        "",
    ]
    for option in [
        "select the canonical zero branch with same-source bases and homogeneous-zero row",
        "emit a selected noninvariant primitive C1 tensor and basis-transport branch",
        "derive all atoms directly from typed monad/Cech/HYM connection witness data",
    ]:
        lines.append(f"- {option}")
    lines.extend(
        [
            "",
            "## Guardrails",
            "",
            "- Do not promote canonical zero C1 matrices unless the selected branch theorem emits them.",
            "- Do not compute `A_selected`, `b_selected`, Yukawas, or `lambda_12` from diagnostic zero matrices.",
            "- Do not use observed data, benchmark Yukawas, locked target columns, or lambda12 diagnostics to fill atoms.",
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
    candidate, cert, missing_packet, note = build()
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_MISSING.write_text(json.dumps(missing_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_MISSING)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
