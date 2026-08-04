"""Build the Qa/SU3 c-twist Deligne/Cech source template."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
DATA = ROOT / "candidate_data"

INPUT = DATA / "minimal_gerbe_source_candidate_or_nogo.candidate.json"
OUTPUT_DATA = DATA / "ctwist_deligne_cech_template.candidate.json"
OUTPUT_CERT = CERTS / "ctwist_deligne_cech_template_certificate.json"


def module_label(name: str, charge: list[int]) -> dict[str, object]:
    c = charge[2]
    return {
        "name": name,
        "charge": charge,
        "ordinary_ab_charge": charge[:2],
        "c_twist": c,
        "module": "ordinary" if c == 0 else f"twisted_module_T_{c:+d}",
        "requires_gerbe_action": c != 0,
    }


def main() -> None:
    prior = json.loads(INPUT.read_text(encoding="utf-8"))
    spaces = [
        ("F1", [-3, 0, 1]),
        ("F2", [-2, 1, -1]),
        ("F3", [0, -1, 0]),
        ("F4", [0, 0, -1]),
        ("F5", [1, 1, 1]),
        ("G1", [2, 1, -1]),
        ("G2", [1, 0, 1]),
        ("G3", [-1, 2, 0]),
        ("G4", [-1, 1, 1]),
        ("G5", [-2, 0, -1]),
        ("P", [-1, 1, 0]),
    ]
    modules = {name: module_label(name, charge) for name, charge in spaces}
    products = [
        {"pair": ["F1", "G1"], "target": "P"},
        {"pair": ["F2", "G2"], "target": "P"},
        {"pair": ["F3", "G3"], "target": "P"},
        {"pair": ["F4", "G4"], "target": "P"},
        {"pair": ["F5", "G5"], "target": "P"},
    ]
    product_checks = []
    for item in products:
        left = modules[item["pair"][0]]
        right = modules[item["pair"][1]]
        target = modules[item["target"]]
        product_checks.append(
            {
                **item,
                "ordinary_ab_sum": [
                    left["ordinary_ab_charge"][0] + right["ordinary_ab_charge"][0],
                    left["ordinary_ab_charge"][1] + right["ordinary_ab_charge"][1],
                ],
                "ordinary_ab_target": target["ordinary_ab_charge"],
                "c_twist_sum": left["c_twist"] + right["c_twist"],
                "c_twist_target": target["c_twist"],
                "passes_template_typing": left["c_twist"] + right["c_twist"] == target["c_twist"]
                and [
                    left["ordinary_ab_charge"][0] + right["ordinary_ab_charge"][0],
                    left["ordinary_ab_charge"][1] + right["ordinary_ab_charge"][1],
                ]
                == target["ordinary_ab_charge"],
            }
        )
    template = {
        "candidate": "SelectedQaSU3CTwistDeligneCechTemplate",
        "status": "CTWIST_DELIGNE_CECH_TEMPLATE_BUILT_VALUES_OPEN",
        "input_status": prior["status"],
        "deligne_2_gerbe_template": {
            "good_cover": "U_i",
            "local_two_forms": "B_i on U_i",
            "overlap_one_forms": "A_ij on U_i cap U_j",
            "triple_overlap_functions": "g_ijk: U_i cap U_j cap U_k -> U(1)",
            "curvature": "H with H|U_i = d B_i",
            "cocycle_equations": [
                "B_j - B_i = d A_ij",
                "A_ij + A_jk + A_ki = g_ijk^{-1} d g_ijk",
                "delta g = 1 on quadruple overlaps",
                "DD(T_c) = c * tau for c in {-1,0,+1}",
            ],
        },
        "twisted_module_template": {
            "transition_law": "s_j = h_ij^(c) s_i",
            "projective_failure": "h_ij^(c) h_jk^(c) h_ki^(c) = g_ijk^c",
            "dual_module_rule": "T_c^vee = T_-c",
            "product_rule": "T_c tensor T_d -> T_(c+d)",
            "ordinary_target_rule": "T_0 is an ordinary untwisted module",
        },
        "module_labels": modules,
        "product_checks": product_checks,
        "required_source_values": {
            "tau_or_DD_class": None,
            "explicit_good_cover": None,
            "B_i": None,
            "A_ij": None,
            "g_ijk": None,
            "h_ij_for_T_plus": None,
            "h_ij_for_T_minus": None,
            "ordinary_ab_line_bundle_factors": None,
            "twisted_section_bases": None,
            "multiplication_constants": None,
        },
        "promotion_tests": {
            "Deligne_Cech_cocycle_identities_verified": False,
            "integrality_or_flat_torsion_class_verified": False,
            "maps_to_required_c_twists": False,
            "Freed_Witten_cancellation_verified": False,
            "Green_Schwarz_Bianchi_verified": False,
            "twisted_projector_retention_verified": False,
            "operator_exit_supplied": False,
        },
        "what_is_solved": [
            "The exact data shape for a same-branch c-twist source is specified.",
            "The +/-1 twisted modules and T_c tensor T_-c -> T_0 product rule are encoded.",
            "All five monad products pass the Deligne/Cech template typing test.",
        ],
        "what_is_not_solved": [
            "The actual selected Deligne/Cech representative is not supplied.",
            "No source values, section bases, multiplication constants, Bianchi/Freed-Witten proof, or operator exit are supplied.",
        ],
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SelectedQaSU3CTwistDeligneCechTemplate",
        "status": "QA_SU3_CTWIST_DELIGNE_CECH_TEMPLATE_BUILT_VALUES_OPEN",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "Deligne_Cech_source_data_schema": True,
            "twisted_module_transition_law_schema": True,
            "all_five_monad_products_pass_template_typing": all(
                item["passes_template_typing"] for item in product_checks
            ),
            "same_branch_source_values_still_required": True,
        },
        "what_remains_open": {
            **template["promotion_tests"],
            "selected_source_values": True,
            "qa_su3_packet_closed": False,
        },
        "next_required_artifact": "Selected_Qa_SU3_CTwist_Source_Value_Search_v1",
        "parallel_fallback": "Selected_Qa_SU3_A01_DE_Operator_Exit_v1",
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    data_text = json.dumps(template, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
