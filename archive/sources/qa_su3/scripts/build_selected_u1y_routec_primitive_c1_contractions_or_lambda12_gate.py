"""Build the post-alpha primitive C1 contractions / lambda12 gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "alpha1_driver_replay": DATA / "selected_u1y_routec_alpha1_driver_replay_from_oriented_overlap.candidate.json",
    "operator_emission_overlap": DATA / "selected_u1y_routec_operator_emission_overlap_from_terminal_slotmap.candidate.json",
    "visible_operator_or_primitive_c1": DATA / "selected_u1y_routec_selected_visible_operator_source_or_primitive_c1_contractions.candidate.json",
    "dotd_alpha1_c1_response": DATA / "selected_u1y_routec_dotd_alpha1_c1_response_emission.candidate.json",
    "electroweak_lambda12_gate": DATA / "dual_attack_local_determinant_or_omega0_source.candidate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_primitive_c1_contractions_or_lambda12_gate.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_primitive_c1_contractions_or_lambda12_gate_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_Primitive_C1_Contractions_or_Lambda12_Gate_v1.md"

STATUS = "U1Y_ROUTEC_PRIMITIVE_C1_LAMBDA12_GATE_POST_ALPHA_OPEN"
NEXT = "Selected_U1Y_RouteC_PrimitiveC1_AtomEmission_or_SelectedLambda12_SpectralTable_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    alpha = load(INPUTS["alpha1_driver_replay"])
    emission = load(INPUTS["operator_emission_overlap"])
    primitive = load(INPUTS["visible_operator_or_primitive_c1"])
    dotd_c1 = load(INPUTS["dotd_alpha1_c1_response"])
    lambda_gate = load(INPUTS["electroweak_lambda12_gate"])

    primitive_lane = primitive["reduction"]["primitive_c1_lane"]
    sector_slots = primitive_lane["sector_slots"]
    terms = primitive_lane["terms"]
    missing_atoms = primitive_lane["missing_atoms"]

    post_alpha_prefix = {
        "alpha1_driver_verified": alpha["decision"]["alpha1_driver_verified"],
        "honest_dotD_validator_closed": alpha["decision"]["honest_dotD_validator_closed"],
        "du_dalpha1_equals_h_ext": alpha["decision"]["du_dalpha1_equals_h_ext_emitted"],
        "selected_overlap_normalization_emitted": emission["decision"]["selected_overlap_normalization_emitted"],
        "same_branch_functional_operator_emission_closed": emission["decision"][
            "same_branch_functional_operator_emission_closed"
        ],
        "dotD_C1_old_gate_status": dotd_c1["status"],
    }

    atom_table: dict[str, dict[str, Any]] = {}
    for sector, slots in sector_slots.items():
        atom_table[sector] = {
            "slots": slots,
            "required_terms": terms,
            "missing_terms": [atom for atom in missing_atoms if atom.startswith(f"sectors.{sector}.")],
            "all_terms_emitted": False,
        }

    primitive_status = {
        "atom_count": primitive_lane["atom_count"],
        "missing_atom_count": primitive_lane["missing_atom_count"],
        "all_primitive_atoms_emitted": False,
        "A_selected_emitted": False,
        "b_selected_emitted": False,
        "sector_response_matrices_emitted": False,
        "reason": (
            "The post-alpha finite response is now ready, but no selected primitive C1 "
            "atom table emits theta-overlap variations, zero-mode responses, explicit vertices, "
            "or basis-connection terms for u,d,e,nuD."
        ),
    }

    lambda12_status = {
        "lambda_12_closed": False,
        "lambda_12_computable_from_this_gate": False,
        "electroweak_lane_A_lambda12_closed": lambda_gate["decision"]["lane_A_lambda12_closed"],
        "diagnostic_values_not_proof": lambda_gate["lane_A_local_determinant"]["diagnostics_not_proof"],
        "reason": (
            "lambda_12 remains a selected spectral/local-determinant table problem. The "
            "post-alpha C1 stack does not emit a selected U1/hypercharge determinant spectrum "
            "or a full Delta_a^sel vector."
        ),
    }

    decision = {
        "post_alpha_gate_built": True,
        "alpha1_and_honest_dotD_prefix_closed": all(post_alpha_prefix[key] is True for key in [
            "alpha1_driver_verified",
            "honest_dotD_validator_closed",
            "du_dalpha1_equals_h_ext",
            "selected_overlap_normalization_emitted",
            "same_branch_functional_operator_emission_closed",
        ]),
        "primitive_C1_contractions_closed": False,
        "A_selected_emitted": False,
        "b_selected_emitted": False,
        "lambda_12_closed": False,
        "lambda_12_computable": False,
        "Yukawa_or_full_SM_closure": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    theorem = {
        "name": "U1YRouteCPrimitiveC1Lambda12PostAlphaGate",
        "proved": True,
        "statement": (
            "After the alpha1 driver replay closes, the next obstruction is no longer "
            "dotD provenance. The selected branch has oriented functional operator emission, "
            "overlap normalization, du/dalpha1=h_ext, and honest dotD replay. What remains "
            "for flavor/SM closure is the primitive C1 atom table: for each of u,d,e,nuD, "
            "the selected source must emit theta-overlap variation, left/right/Higgs zero-mode "
            "responses, explicit vertex, and basis-connection terms. Without those 24 atoms, "
            "A_selected, b_selected, sector response matrices, Yukawa magnitudes, and lambda_12 "
            "are not computable. Separately, electroweak lambda_12 still requires a selected "
            "local determinant/spectral table, not diagnostic near-hit values."
        ),
    }

    candidate = {
        "candidate": "SelectedU1YRouteCPrimitiveC1ContractionsOrLambda12Gate",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "post_alpha_prefix": post_alpha_prefix,
        "atom_table": atom_table,
        "primitive_status": primitive_status,
        "lambda12_status": lambda12_status,
        "decision": decision,
        "theorem": theorem,
        "what_closes_now": {
            "post_alpha_prefix_carried_forward": decision["alpha1_and_honest_dotD_prefix_closed"],
            "primitive_C1_atom_contract_sharpened": True,
            "lambda12_separated_from_alpha1_and_C1": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "all_24_primitive_C1_atoms": True,
            "A_selected": True,
            "b_selected": True,
            "sector_response_matrices": True,
            "Yukawa_magnitudes": True,
            "selected_lambda12_spectral_table": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_primitive_C1_contractions": False,
            "claims_A_selected": False,
            "claims_b_selected": False,
            "claims_lambda12": False,
            "claims_Yukawa_or_full_SM_closure": False,
            "uses_diagnostic_lambda12_values": False,
            "uses_observed_data": False,
            "uses_benchmark_data": False,
            "uses_locked_C1_columns": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
        "observed_data_used": False,
    }

    cert = {
        "certificate": "SelectedU1YRouteCPrimitiveC1ContractionsOrLambda12Gate",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "alpha1_and_honest_dotD_prefix_closed": decision["alpha1_and_honest_dotD_prefix_closed"],
        "primitive_C1_contractions_closed": False,
        "primitive_atom_count": primitive_status["atom_count"],
        "primitive_missing_atom_count": primitive_status["missing_atom_count"],
        "A_selected_emitted": False,
        "b_selected_emitted": False,
        "lambda_12_closed": False,
        "lambda_12_computable": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "observed_data_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected U1Y Route-C Primitive C1 Contractions or Lambda12 Gate v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"alpha1_and_honest_dotD_prefix_closed = {str(cert['alpha1_and_honest_dotD_prefix_closed']).lower()}",
        f"primitive_C1_contractions_closed = {str(cert['primitive_C1_contractions_closed']).lower()}",
        f"primitive_missing_atom_count = {cert['primitive_missing_atom_count']} / {cert['primitive_atom_count']}",
        f"A_selected_emitted = {str(cert['A_selected_emitted']).lower()}",
        f"b_selected_emitted = {str(cert['b_selected_emitted']).lower()}",
        f"lambda_12_closed = {str(cert['lambda_12_closed']).lower()}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "The dotD/alpha prefix is now closed, so the remaining work is cleanly",
        "about selected primitive C1 atoms and a separate selected lambda12 spectral table.",
        "",
        "## Primitive Atom Table",
        "",
    ]
    for sector, row in candidate["atom_table"].items():
        lines.append(f"- `{sector}`: {len(row['missing_terms'])} missing atoms")
    lines.extend(
        [
            "",
            "Required terms per sector:",
            "",
        ]
    )
    for term in next(iter(candidate["atom_table"].values()))["required_terms"]:
        lines.append(f"- `{term}`")
    lines.extend(
        [
            "",
            "## Lambda12 Boundary",
            "",
            candidate["lambda12_status"]["reason"],
            "",
            "## Theorem",
            "",
            candidate["theorem"]["statement"],
            "",
            "## Guardrails",
            "",
            "- Do not treat closed `alpha1` or dotD replay as primitive C1 closure.",
            "- Do not derive `lambda_12` from diagnostic near-hit values.",
            "- Do not use observed masses, CKM data, benchmark Yukawas, or locked C1 columns.",
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
