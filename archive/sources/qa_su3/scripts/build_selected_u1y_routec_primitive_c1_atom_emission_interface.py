"""Build the primitive C1 atom emission interface and assembly theorem."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "post_alpha_gate": DATA / "selected_u1y_routec_primitive_c1_contractions_or_lambda12_gate.candidate.json",
    "source_or_typed_de": DATA / "selected_u1y_routec_selected_source_certificate_or_typed_de_construction.candidate.json",
    "typed_witness_contract": DATA / "selected_u1y_routec_typed_monad_cech_or_hym_connection_witness.candidate.json",
    "finite_hym_solve": DATA / "selected_u1y_routec_finite_hym_connection_solve_or_typed_cech_payload.candidate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_primitive_c1_atom_emission_interface.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_primitive_c1_atom_emission_interface_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_Primitive_C1_Atom_Emission_Interface_v1.md"
OUTPUT_TEMPLATE = DATA / "selected_u1y_routec_primitive_c1_atom_payload.template.json"

STATUS = "U1Y_ROUTEC_PRIMITIVE_C1_ATOM_EMISSION_INTERFACE_BUILT_VALUES_OPEN"
NEXT = "Selected_U1Y_RouteC_PrimitiveC1_AtomPayload_Fill_or_NoGo_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def zero_matrix() -> list[list[None]]:
    return [[None, None, None], [None, None, None], [None, None, None]]


def build() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], str]:
    post_alpha = load(INPUTS["post_alpha_gate"])
    source_or_de = load(INPUTS["source_or_typed_de"])
    witness = load(INPUTS["typed_witness_contract"])
    finite = load(INPUTS["finite_hym_solve"])

    atom_table = post_alpha["atom_table"]
    terms = next(iter(atom_table.values()))["required_terms"]

    atom_payload: dict[str, Any] = {
        "schema": "SelectedU1YRouteCPrimitiveC1AtomPayload.v1",
        "status": "OPEN_SELECTED_VALUES_REQUIRED",
        "source_certificate": None,
        "same_source_id": None,
        "basis_id": None,
        "basis_dimension_per_sector": 3,
        "sectors": {},
        "guardrails": {
            "observed_data_used": False,
            "benchmark_data_used": False,
            "locked_target_columns_used": False,
            "diagnostic_lambda12_values_used": False,
        },
    }
    for sector, row in atom_table.items():
        atom_payload["sectors"][sector] = {
            "slots": row["slots"],
            "basis_left": None,
            "basis_right": None,
            "basis_higgs": None,
            "atoms": {term: zero_matrix() for term in terms},
            "all_atoms_emitted": False,
        }

    assembly_rules = {
        "matrix_shape": "3x3 per sector in selected zero-mode bases",
        "sector_response_matrix": "C_s = sum_{term in required_terms} C_{s,term}",
        "required_terms": terms,
        "A_selected": (
            "Stack the vectorized selected sector response matrices in the fixed sector "
            "order [u,d,e,nuD], using the selected left/right zero-mode basis order."
        ),
        "b_selected": (
            "Stack the selected inhomogeneous source/constant terms emitted by the same "
            "payload. If a theorem proves the primitive C1 problem homogeneous, this row "
            "must be emitted explicitly as the zero vector by that same theorem."
        ),
        "acceptance_equation": "A_selected x = b_selected, with A_selected and b_selected both emitted from the atom payload",
        "no_fitting_rule": "No entry may be chosen from observed masses, CKM/PMNS data, benchmark Yukawas, lambda12 diagnostics, or locked target columns.",
    }

    source_requirements = {
        "same_source_certificate": True,
        "selected_zero_mode_bases": True,
        "selected_theta_overlap_derivative": True,
        "selected_left_zero_mode_response": True,
        "selected_right_zero_mode_response": True,
        "selected_higgs_zero_mode_response": True,
        "selected_explicit_vertex": True,
        "selected_basis_connection": True,
        "selected_inhomogeneous_row_or_zero_theorem": True,
        "selected_basis_order_and_sector_order": True,
    }

    decision = {
        "interface_built": True,
        "post_alpha_prefix_closed": post_alpha["decision"]["alpha1_and_honest_dotD_prefix_closed"],
        "assembly_theorem_proved": True,
        "atom_payload_template_written": True,
        "primitive_C1_atoms_emitted": False,
        "emitted_atom_count": 0,
        "missing_atom_count": 24,
        "A_selected_computable": False,
        "b_selected_computable": False,
        "lambda_12_computable": False,
        "Yukawa_or_full_SM_closure": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "SelectedU1YRouteCPrimitiveC1AtomEmissionInterface",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "post_alpha_gate": post_alpha["status"],
            "source_or_typed_de": source_or_de["status"],
            "typed_witness_contract": witness["status"],
            "finite_hym_solve": finite["status"],
        },
        "source_requirements": source_requirements,
        "atom_payload_template": rel(OUTPUT_TEMPLATE),
        "assembly_rules": assembly_rules,
        "sector_order": ["u", "d", "e", "nuD"],
        "term_order": terms,
        "decision": decision,
        "theorem": {
            "name": "U1YRouteCPrimitiveC1AtomAssemblyTheorem",
            "proved": True,
            "statement": (
                "Given one selected same-source primitive C1 atom payload in the locked "
                "sector bases, the sector response matrix C_s is the additive sum of its "
                "six source-emitted atoms: theta-overlap variation, left/right/Higgs "
                "zero-mode responses, explicit vertex, and basis connection. Stacking "
                "the four vectorized C_s blocks in sector order [u,d,e,nuD], together "
                "with the same-source inhomogeneous row or explicit homogeneous-zero "
                "theorem, computes A_selected and b_selected without target fitting. "
                "The current artifact proves only this assembly rule and template; it "
                "does not emit the values."
            ),
        },
        "what_closes_now": {
            "primitive_C1_payload_schema": True,
            "sector_and_term_order_fixed": True,
            "A_selected_b_selected_assembly_rule": True,
            "same_source_no_fitting_acceptance_rule": True,
        },
        "what_remains_open": {
            "fill_24_atom_matrices": True,
            "same_source_certificate": True,
            "selected_inhomogeneous_row_or_zero_theorem": True,
            "A_selected": True,
            "b_selected": True,
            "lambda_12": True,
            "Yukawa_or_full_SM_closure": True,
        },
        "guardrails": {
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
        "certificate": "SelectedU1YRouteCPrimitiveC1AtomEmissionInterface",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "template_path": rel(OUTPUT_TEMPLATE),
        "note_path": rel(OUTPUT_NOTE),
        "assembly_theorem_proved": True,
        "primitive_C1_atoms_emitted": False,
        "missing_atom_count": 24,
        "A_selected_computable": False,
        "b_selected_computable": False,
        "lambda_12_computable": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    return candidate, cert, atom_payload, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected U1Y Route-C Primitive C1 Atom Emission Interface v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"assembly_theorem_proved = {str(cert['assembly_theorem_proved']).lower()}",
        f"primitive_C1_atoms_emitted = {str(cert['primitive_C1_atoms_emitted']).lower()}",
        f"missing_atom_count = {cert['missing_atom_count']}",
        f"A_selected_computable = {str(cert['A_selected_computable']).lower()}",
        f"b_selected_computable = {str(cert['b_selected_computable']).lower()}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "This artifact fixes the primitive C1 value interface. It proves how a",
        "selected same-source atom payload would assemble into sector response",
        "matrices and then into `A_selected` and `b_selected`; it does not emit",
        "the atom values.",
        "",
        "## Sector Order",
        "",
    ]
    for sector in candidate["sector_order"]:
        lines.append(f"- `{sector}`")
    lines.extend(["", "## Term Order", ""])
    for term in candidate["term_order"]:
        lines.append(f"- `{term}`")
    lines.extend(
        [
            "",
            "## Assembly",
            "",
            f"- `{candidate['assembly_rules']['sector_response_matrix']}`",
            f"- `{candidate['assembly_rules']['A_selected']}`",
            f"- `{candidate['assembly_rules']['b_selected']}`",
            "",
            "## Guardrails",
            "",
            "- Do not fill atoms from masses, CKM/PMNS data, benchmark Yukawas, lambda12 diagnostics, or locked target columns.",
            "- Do not call `A_selected` or `b_selected` computable until all atom matrices and the inhomogeneous row are emitted by one selected source.",
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
    candidate, cert, atom_payload, note = build()
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_TEMPLATE.write_text(json.dumps(atom_payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_TEMPLATE)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
