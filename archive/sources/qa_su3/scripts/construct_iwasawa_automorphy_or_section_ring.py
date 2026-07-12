"""Attempt the Iwasawa automorphy/section-ring construction for Qa/SU3."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = CERTS / "iwasawa_line_bundle_section_ring_interface_certificate.json"
TEMPLATE = CERTS / "iwasawa_automorphy_section_ring.template.json"
OUTPUT_DATA = DATA / "iwasawa_automorphy_or_section_ring_construction.candidate.json"
OUTPUT_CERT = CERTS / "iwasawa_automorphy_or_section_ring_construction_certificate.json"
OUTPUT_NOTE = CORPUS / "Selected_Qa_SU3_Iwasawa_Automorphy_or_Section_Ring_Construction_v1.md"


def charge_key(charge: list[int]) -> str:
    return f"({charge[0]},{charge[1]},{charge[2]})"


def build_symbolic_rank_one_relation(required_spaces: list[dict[str, object]]) -> dict[str, object]:
    f_spaces = [space for space in required_spaces if str(space["id"]).startswith("F")]
    g_spaces = [space for space in required_spaces if str(space["id"]).startswith("G")]
    terms = []
    for f_space, g_space in zip(f_spaces, g_spaces, strict=True):
        i = str(f_space["id"])[1:]
        product_charge = [f_space["charge"][j] + g_space["charge"][j] for j in range(3)]
        terms.append(
            {
                "i": int(i),
                "term": f"m{i}*u{i}*v{i}",
                "f_charge": f_space["charge"],
                "g_charge": g_space["charge"],
                "product_charge": product_charge,
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


def route_assessment(previous: dict[str, object], template: dict[str, object]) -> dict[str, str]:
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


def build() -> tuple[dict[str, object], dict[str, object], str]:
    previous = json.loads(PREVIOUS.read_text(encoding="utf-8"))
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    spaces = previous["required_section_spaces"]
    relation = build_symbolic_rank_one_relation(spaces)
    routes = route_assessment(previous, template)
    product_charges = {charge_key(term["product_charge"]) for term in relation["terms"]}
    all_products_land_in_p = product_charges == {"(-1,1,0)"}
    construction_result = {
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
    }
    candidate = {
        "candidate": "SelectedQaSU3IwasawaAutomorphyOrSectionRingConstruction",
        "status": "QA_SU3_IWASAWA_AUTOMORPHY_SECTION_RING_CONSTRUCTION_SYMBOLIC_ONLY_VALUES_OPEN",
        "input_status": {"section_ring_interface": previous["status"]},
        "template_path": str(TEMPLATE.relative_to(ROOT)),
        "required_section_spaces": spaces,
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
        "construction_result": construction_result,
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
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": candidate["candidate"],
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "template_path": candidate["template_path"],
        "route_assessment": routes,
        "symbolic_rank_one_relation": relation,
        "product_charge_check": candidate["product_charge_check"],
        "automorphy_packet_required": candidate["automorphy_packet_required"],
        "gate_results": candidate["gate_results"],
        "construction_result": construction_result,
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    return candidate, certificate, render_note(candidate)


def render_note(candidate: dict[str, object]) -> str:
    return f"""# Selected Qa/SU3 Iwasawa Automorphy or Section Ring Construction v1

## Purpose

This artifact tries the next construction step after the line-bundle section-ring interface. It tests literal scalar constants, torus-style theta/Appell-Humbert transfer, and the Iwasawa automorphy/section-ring construction.

## Route Decision

```text
literal constant route: rejected, because all required section charges are nonzero
torus theta shortcut: rejected until an Iwasawa transfer theorem is supplied
selected source direct route: blocked, because section data are not printed
automorphy route: open, requires factor-of-automorphy cocycle
direct operator exit: open, if Dolbeault/Cech/rho_E packet is supplied
```

## Symbolic Rank-One Relation

If every required section space is one-dimensional, and if products are nonzero,

```text
eF_i * eG_i = m_i eP
```

then the monad condition reduces to:

```text
{candidate["symbolic_rank_one_relation"]["relation"]}
```

All five products land in the expected target charge:

```text
P = K2 - K1 = (-1,1,0)
```

So we now have a symbolic construction pattern. This is not closure, because the section dimensions, bases, multiplication constants, and local-freeness test are still not selected.

## Required Automorphy Packet

The needed object is:

```text
a_q(gamma1 gamma2, z) = a_q(gamma1, gamma2.z) a_q(gamma2, z)
s_q(gamma.z) = a_q(gamma,z) s_q(z)
a_p a_q = a_(p+q)
```

for every required charge `q`, plus section bases and multiplication constants.

## Verdict

```text
all products land in P: yes
symbolic rank-one relation built: yes
literal constant route retired: yes
torus theta shortcut retired until transfer theorem: yes
automorphy schema built: yes
actual automorphy factors found: no
section dimensions found: no
explicit f,g constructed: no
g*f=0 proved: no
Qa/SU3 closed: no
target fitting used: no
```

Next artifact:

```text
{candidate["next_required_artifact"]["name"]}
```
"""


def main() -> None:
    candidate, certificate, note = build()
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
