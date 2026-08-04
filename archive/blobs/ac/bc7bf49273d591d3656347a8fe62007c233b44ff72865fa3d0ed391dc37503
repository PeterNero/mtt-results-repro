"""Build the finite cochain packet or D_E response acceptance gate."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"

SELECTED_VALUES_GATE = DATA / "selected_multiplication_constants_or_de_source_gate.candidate.json"
SCAFFOLD = DATA / "cech_dolbeault_matrix_packet_scaffold.candidate.json"
OPERATOR_GATE = DATA / "a01_de_operator_exit_gate.candidate.json"
OUTPUT_DATA = DATA / "finite_cochain_packet_or_de_response_gate.candidate.json"
OUTPUT_CERT = CERTS / "finite_cochain_packet_or_de_response_gate_certificate.json"


def requirement(name: str, lane: str, present: bool, formula: str, reason: str) -> dict[str, object]:
    return {"name": name, "lane": lane, "present_now": present, "formula_or_check": formula, "reason": reason}


def main() -> None:
    selected_gate = json.loads(SELECTED_VALUES_GATE.read_text(encoding="utf-8"))
    scaffold = json.loads(SCAFFOLD.read_text(encoding="utf-8"))
    operator_gate = json.loads(OPERATOR_GATE.read_text(encoding="utf-8"))
    spaces = list(scaffold["formal_basis"])
    pairs = [block["pair"] for block in scaffold["product_blocks"]]
    gf_equation = scaffold["monad_matrix_shape"]["gf_zero_equation"]
    cochain_lane = [
        requirement("selected_finite_basis_for_each_space", "finite_cochain", False, "basis(S) for S in F1..F5,G1..G5,P", "Without selected bases, product coefficients are coordinate choices."),
        requirement("selected_differentials", "finite_cochain", False, "d1*d0 = 0", "Cech/Dolbeault matrices must form an actual finite complex."),
        requirement("selected_product_tables", "finite_cochain", False, "m_i: F_i x G_i -> P", "The coefficients mu_i must be read from product tables, not assigned."),
        requirement("selected_map_entries", "finite_cochain", False, "f_i=a_i, g_i=b_i in selected bases", "The monad maps must be entries in the same selected bases."),
        requirement("post_selection_monad_check", "finite_cochain", False, gf_equation, "Only after selection may g*f=0 be tested as a proof condition."),
    ]
    operator_lane = [
        requirement("selected_DE_or_stiffness_operator", "operator_response", False, "A = G^{-1} K", "A nontrivial operator must replace identity rho_E or diagonal phase fixtures."),
        requirement("selected_projectors_and_green_operator", "operator_response", False, "P^2=P, Q=I-P, A R Q = Q", "The response must live on the horizontal complement."),
        requirement("selected_dotD", "operator_response", False, "s_i = Q dotD psi_i", "The source vectors cannot be texture knobs."),
        requirement("horizontal_response", "operator_response", False, "dotPsi_i = -R Q dotD psi_i", "The linearized zero-mode response must be derived."),
        requirement("first_order_equation", "operator_response", False, "A dotPsi_i + s_i = 0 and P dotPsi_i = 0", "The operator response must satisfy the finite equations."),
    ]
    bridge_checks = [
        requirement("same_source_identifier", "bridge", False, "source_id(cochain)=source_id(operator)", "The product tables and D_E/dotD response must be from the same branch."),
        requirement("same_selected_bases_or_explicit_change_of_basis", "bridge", False, "B^{-1} m_i B and B^{-1} D_E B agree", "Cochain and operator coordinates must be comparable."),
        requirement("same_gf_zero_packet", "bridge", False, gf_equation, "The selected entries must satisfy the already-derived monad equation."),
        requirement("admissibility_retention", "bridge", False, "Freed-Witten, GS/Bianchi, stability/local-freeness, projector retention", "A finite packet must remain admissible after selection."),
    ]
    all_requirements = cochain_lane + operator_lane + bridge_checks
    candidate = {
        "candidate": "SelectedQaSU3FiniteCochainPacketOrDEResponseGate",
        "status": "FINITE_COCHAIN_PACKET_OR_DE_RESPONSE_GATE_BUILT_SELECTED_SOURCE_OPEN",
        "input_statuses": {
            "selected_values_gate": selected_gate["status"],
            "cech_dolbeault_scaffold": scaffold["status"],
            "a01_de_operator_gate": operator_gate["status"],
        },
        "spaces": spaces,
        "required_space_count": len(spaces),
        "typed_product_pairs": pairs,
        "typed_product_pair_count": len(pairs),
        "gf_zero_equation": gf_equation,
        "finite_cochain_lane": cochain_lane,
        "operator_response_lane": operator_lane,
        "bridge_checks": bridge_checks,
        "acceptance_algorithm": [
            "Load selected source certificate for the Qa/SU3 branch.",
            "Load finite bases for F1..F5, G1..G5, and P, or an explicit cochain complex whose cohomology bases select them.",
            "Compute product tables m_i: F_i x G_i -> P and extract mu_i in the selected bases.",
            "Read f and g map entries in those same bases and verify g*f=0.",
            "Independently load D_E/dotD/rho_E, projectors, and Green/Riesz data from the same source.",
            "Verify source vectors s_i=Q dotD psi_i, responses dotPsi_i=-R s_i, and A dotPsi_i+s_i=0.",
            "Run Freed-Witten, Green-Schwarz/Bianchi, stability/local-freeness, and projector-retention checks.",
        ],
        "gate_results": {
            "eleven_spaces_carried_forward": len(spaces) == 11,
            "five_product_pairs_carried_forward": len(pairs) == 5,
            "cochain_acceptance_contract_built": len(cochain_lane) == 5,
            "operator_response_contract_built": len(operator_lane) == 5,
            "same_source_bridge_contract_built": len(bridge_checks) == 4,
            "selected_finite_cochain_packet_supplied": False,
            "selected_DE_dotD_response_supplied": False,
            "selected_source_promoted": False,
            "closure_claimed": False,
        },
        "decision": {
            "result": "Two-lane acceptance gate built; selected source data remain open.",
            "why": "The finite cochain lane can select mu_i and f,g, while the operator lane can independently select D_E/dotD response. Closure requires both to agree or one to imply the other with an explicit bridge.",
            "next_move": "Attempt an actual selected finite source solve: either construct the cochain product tables first, or derive D_E/dotD and back out the same packet entries.",
        },
        "next_required_artifact": "Selected_Qa_SU3_Selected_Finite_Source_Solve_v1",
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SelectedQaSU3FiniteCochainPacketOrDEResponseGate",
        "status": "QA_SU3_FINITE_COCHAIN_PACKET_OR_DE_RESPONSE_GATE_BUILT_SELECTED_SOURCE_OPEN",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "finite_cochain_acceptance_contract": candidate["gate_results"]["cochain_acceptance_contract_built"],
            "operator_response_acceptance_contract": candidate["gate_results"]["operator_response_contract_built"],
            "same_source_bridge_contract": candidate["gate_results"]["same_source_bridge_contract_built"],
            "eleven_spaces_and_five_products_carried_forward": candidate["gate_results"]["eleven_spaces_carried_forward"] and candidate["gate_results"]["five_product_pairs_carried_forward"],
        },
        "what_remains_open": {
            "selected_source_certificate": True,
            "selected_finite_cochain_packet": True,
            "selected_product_tables_and_mu_i": True,
            "selected_DE_dotD_response": True,
            "same_source_bridge_execution": True,
            "qa_su3_packet_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
