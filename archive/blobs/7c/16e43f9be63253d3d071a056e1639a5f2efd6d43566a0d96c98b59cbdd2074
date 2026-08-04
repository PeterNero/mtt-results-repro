"""Attempt the Iwasawa automorphy/section-ring construction for Qa/SU3."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
PREVIOUS = CERTS / "selected_qa_su3_iwasawa_line_bundle_section_ring_interface_certificate.json"
TEMPLATE = CERTS / "selected_qa_su3_iwasawa_automorphy_section_ring.template.json"
OUTPUT_CERT = CERTS / "selected_qa_su3_iwasawa_automorphy_or_section_ring_construction_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def charge_key(charge: list[int]) -> str:
    return f"({charge[0]},{charge[1]},{charge[2]})"


def build_symbolic_rank_one_relation(required_spaces: list[dict[str, Any]]) -> dict[str, Any]:
    f_spaces = [space for space in required_spaces if space["id"].startswith("F")]
    g_spaces = [space for space in required_spaces if space["id"].startswith("G")]
    terms = []
    for f_space, g_space in zip(f_spaces, g_spaces, strict=True):
        i = f_space["id"][1:]
        terms.append(
            {
                "i": int(i),
                "term": f"m{i}*u{i}*v{i}",
                "f_charge": f_space["charge"],
                "g_charge": g_space["charge"],
                "product_charge": [
                    f_space["charge"][j] + g_space["charge"][j] for j in range(3)
                ],
            }
        )
    return {
        "assumptions": [
            "each F_i section space is one-dimensional with basis eF_i",
            "each G_i section space is one-dimensional with basis eG_i",
            "product space P is one-dimensional with basis eP",
            "multiplication eF_i*eG_i = m_i eP is known",
        ],
        "terms": terms,
        "relation": "m1*u1*v1 + m2*u2*v2 + m3*u3*v3 + m4*u4*v4 + m5*u5*v5 = 0",
        "constructive_example_if_m1_m2_nonzero": {
            "u1": 1,
            "v1": "m2",
            "u2": 1,
            "v2": "-m1",
            "u3": 0,
            "v3": 0,
            "u4": 0,
            "v4": 0,
            "u5": 0,
            "v5": 0,
        },
        "actual_closure_status": "SYMBOLIC_ONLY_MULTIPLICATION_CONSTANTS_AND_NONZERO_SECTIONS_OPEN",
    }


def route_assessment(previous: dict[str, Any], template: dict[str, Any]) -> dict[str, Any]:
    prev_result = previous["interface_result"]
    literal_blocked = prev_result["literal_constant_map_route_blocked"]
    selected_source_has_data = prev_result["selected_source_has_section_construction_data"]
    torus_shortcut_allowed = template["external_literature_guardrail"]["torus_appell_humbert_shortcut_allowed"]
    return {
        "literal_constant_route": "REJECTED_NONZERO_CHARGES" if literal_blocked else "OPEN",
        "selected_source_direct_route": "OPEN_SOURCE_HAS_PARTIAL_DATA"
        if selected_source_has_data
        else "BLOCKED_SELECTED_SOURCE_DOES_NOT_PRINT_SECTION_DATA",
        "torus_theta_shortcut": "OPEN_TRANSFER_THEOREM_REQUIRED"
        if torus_shortcut_allowed
        else "REJECTED_NO_IWASAWA_TRANSFER_THEOREM",
        "automorphy_route": "OPEN_REQUIRES_FACTOR_OF_AUTOMORPHY_COCYCLE",
        "abstract_rank_one_section_ring_route": "CONDITIONAL_SYMBOLIC_RELATION_AVAILABLE_VALUES_OPEN",
        "direct_operator_exit": "OPEN_IF_DOLBEAULT_CECH_OR_RHOE_PACKET_SUPPLIED",
    }


def main() -> None:
    previous = load(PREVIOUS)
    template = load(TEMPLATE)
    required_spaces = previous["required_section_spaces"]
    relation = build_symbolic_rank_one_relation(required_spaces)
    routes = route_assessment(previous, template)
    product_charges = {charge_key(term["product_charge"]) for term in relation["terms"]}
    all_products_land_in_p = product_charges == {"(-1,1,0)"}

    output = {
        "certificate": "SelectedQaSU3IwasawaAutomorphyOrSectionRingConstruction",
        "status": "QA_SU3_IWASAWA_AUTOMORPHY_SECTION_RING_CONSTRUCTION_SYMBOLIC_ONLY_VALUES_OPEN",
        "input_status": {"section_ring_interface": previous["status"]},
        "template_path": str(TEMPLATE.relative_to(ROOT)),
        "external_literature_signal": {
            "iwasawa_geometry_source": {
                "url": "https://academic.oup.com/imrn/article-pdf/2020/23/9420/34659449/rny230.pdf",
                "used_for": "Iwasawa as compact complex homogeneous quotient signal; not used as section-ring data",
            },
            "picard_parallelizable_source": {
                "url": "https://arxiv.org/abs/2106.08550",
                "used_for": "Picard groups on compact complex parallelizable quotients are nontrivial research objects; not a ready Iwasawa section basis",
            },
        },
        "required_section_spaces": required_spaces,
        "route_assessment": routes,
        "symbolic_rank_one_relation": relation,
        "product_charge_check": {
            "product_charges": sorted(product_charges),
            "expected_product_charge": "(-1,1,0)",
            "all_products_land_in_P": all_products_land_in_p,
        },
        "automorphy_packet_required": template["automorphy_model"],
        "gate_results": {
            "literal_constant_route": "FAIL_REJECTED_NONZERO_CHARGES",
            "torus_theta_shortcut": "FAIL_REJECTED_NO_TRANSFER_THEOREM",
            "abstract_charge_and_relation": "PASS_SYMBOLIC_RANK_ONE_RELATION_BUILT",
            "automorphy_cocycle": "FAIL_NOT_SUPPLIED",
            "section_space_dimensions": "FAIL_NOT_SUPPLIED",
            "multiplication_constants": "FAIL_NOT_SUPPLIED",
            "gf_zero_actual_coefficients": "FAIL_SYMBOLIC_ONLY",
            "locally_free": "FAIL_NO_EXACT_MAPS",
            "operator_exit": "FAIL_NO_DOLBEAULT_CECH_OR_RHOE_EXIT",
        },
        "construction_result": {
            "all_products_land_in_P": all_products_land_in_p,
            "symbolic_rank_one_relation_built": True,
            "literal_constant_route_retired": True,
            "torus_theta_shortcut_retired_until_transfer_theorem": True,
            "automorphy_schema_built": True,
            "actual_automorphy_factors_found": False,
            "section_dimensions_found": False,
            "explicit_f_g_constructed": False,
            "g_f_zero_proved": False,
            "qa_su3_closed": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": {
            "name": "Selected_Qa_SU3_Iwasawa_Automorphy_Cocycle_Data_or_NoGo_v1",
            "must_supply": [
                "factor-of-automorphy a_q for each required charge q",
                "section basis solving s_q(gamma.z)=a_q(gamma,z)s_q(z)",
                "multiplication constants m_i into P",
                "nonzero coefficient choice satisfying the symbolic relation",
                "locally-free certificate for the exact maps",
            ],
        },
    }
    text = json.dumps(output, indent=2, sort_keys=True)
    if "--write-certificate" in sys.argv:
        OUTPUT_CERT.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
