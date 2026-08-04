"""Build the Qa/SU3 Cech/Dolbeault matrix packet scaffold."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"

OPERATOR_GATE = DATA / "a01_de_operator_exit_gate.candidate.json"
SOURCE_PACKET = DATA / "source_augmentation_packet.candidate.json"
TWISTED_GATE = DATA / "twisted_section_ring_and_gerbe_source_gate.candidate.json"
OUTPUT_DATA = DATA / "cech_dolbeault_matrix_packet_scaffold.candidate.json"
OUTPUT_CERT = CERTS / "cech_dolbeault_matrix_packet_scaffold_certificate.json"


def main() -> None:
    operator_gate = json.loads(OPERATOR_GATE.read_text(encoding="utf-8"))
    source = json.loads(SOURCE_PACKET.read_text(encoding="utf-8"))
    twisted = json.loads(TWISTED_GATE.read_text(encoding="utf-8"))
    product_tests = source["product_tests"]
    formal_basis = {
        item["id"]: {
            "basis_label": f"e_{item['id']}",
            "charge": item["charge"],
            "role": item["role"],
            "selected_basis_supplied": False,
        }
        for item in source["required_section_spaces"]
    }
    product_blocks = []
    for idx, item in enumerate(product_tests, start=1):
        f_id, g_id = item["pair"]
        product_blocks.append(
            {
                "pair": item["pair"],
                "target": "P",
                "formal_f_coefficient": f"a_{idx}",
                "formal_g_coefficient": f"b_{idx}",
                "formal_multiplication_constant": f"mu_{idx}",
                "typed_product": f"mu_{idx}*a_{idx}*b_{idx}*e_P",
                "target_charge_verified": item["lands_in_P"],
                "selected_multiplication_constant_supplied": item["multiplication_constant"] is not None,
                "selected_basis_labels": [formal_basis[f_id]["basis_label"], formal_basis[g_id]["basis_label"], formal_basis["P"]["basis_label"]],
            }
        )
    gf_equation_terms = [block["typed_product"].replace("*e_P", "") for block in product_blocks]
    gf_equation = " + ".join(gf_equation_terms) + " = 0"
    selected_values_supplied = all(block["selected_multiplication_constant_supplied"] for block in product_blocks)
    candidate = {
        "candidate": "SelectedQaSU3CechDolbeaultMatrixPacketScaffold",
        "status": "CECH_DOLBEAULT_MATRIX_PACKET_SCAFFOLD_BUILT_SELECTED_VALUES_OPEN",
        "input_statuses": {
            "operator_gate": operator_gate["status"],
            "source_packet": source["status"],
            "twisted_section_gate": twisted["status"],
        },
        "formal_basis": formal_basis,
        "product_blocks": product_blocks,
        "monad_matrix_shape": {
            "f_vector": ["a_1", "a_2", "a_3", "a_4", "a_5"],
            "g_vector": ["b_1", "b_2", "b_3", "b_4", "b_5"],
            "multiplication_constants": ["mu_1", "mu_2", "mu_3", "mu_4", "mu_5"],
            "gf_zero_equation": gf_equation,
            "minimal_formal_dimension_assumption": "one formal generator per typed space only as a scaffold; not a selected basis claim",
        },
        "promotion_requirements": {
            "replace_formal_basis_with_selected_section_or_cochain_bases": True,
            "replace_mu_i_with_selected_multiplication_constants": True,
            "replace_a_i_b_i_with_selected_f_g_matrix_entries": True,
            "verify_gf_zero_from_selected_values": True,
            "construct_same_source_DE_dotD_or_rhoE": True,
            "run_operator_exit_gate": True,
        },
        "gate_results": {
            "eleven_formal_spaces_indexed": len(formal_basis) == 11,
            "five_typed_product_blocks_indexed": len(product_blocks) == 5,
            "all_products_target_P_by_charge": all(block["target_charge_verified"] for block in product_blocks),
            "gf_zero_equation_derived": True,
            "selected_bases_supplied": False,
            "selected_multiplication_constants_supplied": selected_values_supplied,
            "selected_f_g_entries_supplied": False,
            "selected_DE_or_rhoE_supplied": False,
            "matrix_packet_promoted": False,
            "closure_claimed": False,
        },
        "decision": {
            "result": "Formal finite matrix scaffold built; selected values remain open.",
            "why": "The source packet gives exactly five typed products into P, so the monad obstruction is now the selected scalar/matrix equation Sum_i mu_i a_i b_i = 0 plus selected operator data.",
            "do_not_do": "Do not choose arbitrary a_i,b_i,mu_i to satisfy the equation; that would be a convenience solve, not selected MTT data.",
        },
        "next_required_artifact": "Selected_Qa_SU3_Selected_Multiplication_Constants_or_DE_Source_v1",
        "parallel_search_artifact": "Selected_Qa_SU3_Central_Period_Selector_Search_v1",
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SelectedQaSU3CechDolbeaultMatrixPacketScaffold",
        "status": "QA_SU3_CECH_DOLBEAULT_MATRIX_PACKET_SCAFFOLD_BUILT_SELECTED_VALUES_OPEN",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "eleven_formal_spaces_indexed": candidate["gate_results"]["eleven_formal_spaces_indexed"],
            "five_typed_product_blocks_indexed": candidate["gate_results"]["five_typed_product_blocks_indexed"],
            "all_products_target_P_by_charge": candidate["gate_results"]["all_products_target_P_by_charge"],
            "gf_zero_equation_derived": True,
            "operator_gate_next_input_shape_prepared": True,
        },
        "what_remains_open": {
            "selected_section_or_cochain_bases": True,
            "selected_multiplication_constants": True,
            "selected_f_g_matrix_entries": True,
            "selected_DE_dotD_or_rhoE": True,
            "qa_su3_packet_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "parallel_search_artifact": candidate["parallel_search_artifact"],
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
