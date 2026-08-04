"""Build the Iwasawa line-bundle section-ring interface for Qa/SU3."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
SELECTED_SOURCE = OBSIDIAN / "16 Strings, Flux, & M-Theory Encodings" / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md"
PREVIOUS = CERTS / "selected_qa_su3_monad_map_construction_or_source_augmentation_certificate.json"
TEMPLATE = CERTS / "selected_qa_su3_iwasawa_line_bundle_section_ring.template.json"
OUTPUT_CERT = CERTS / "selected_qa_su3_iwasawa_line_bundle_section_ring_interface_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def is_zero(charge: list[int]) -> bool:
    return all(x == 0 for x in charge)


def scan_selected_source() -> dict[str, Any]:
    terms = {
        "constant_matrices": "constant matrices in the left-invariant frame",
        "generic_holomorphic_maps": "generic holomorphic maps",
        "section_ring": "section ring",
        "effective_cone": "effective cone",
        "automorphy": "automorphy",
        "transition": "transition",
        "theta_function": "theta function",
        "factor_of_automorphy": "factor of automorphy",
        "Cech": "Cech",
        "rho_E": "rho_E",
    }
    if not SELECTED_SOURCE.exists():
        return {"path": str(SELECTED_SOURCE), "present": False, "terms": {key: False for key in terms}}
    text = SELECTED_SOURCE.read_text(encoding="utf-8", errors="ignore")
    return {
        "path": str(SELECTED_SOURCE),
        "present": True,
        "terms": {key: term in text for key, term in terms.items()},
    }


def main() -> None:
    previous = load(PREVIOUS)
    template = load(TEMPLATE)
    spaces = template["required_section_spaces"]
    nonzero_charge_spaces = [space for space in spaces if not is_zero(space["charge"])]
    zero_charge_spaces = [space for space in spaces if is_zero(space["charge"])]
    source_scan = scan_selected_source()

    constant_scalar_test = {
        "interpretation": "literal scalar constants are degree-zero sections",
        "required_spaces": len(spaces),
        "zero_charge_spaces": [space["id"] for space in zero_charge_spaces],
        "nonzero_charge_spaces": [space["id"] for space in nonzero_charge_spaces],
        "literal_constant_entries_can_fill_all_required_spaces": len(nonzero_charge_spaces) == 0,
        "verdict": "FAIL_LITERAL_CONSTANT_ENTRIES_HAVE_WRONG_CHARGE"
        if nonzero_charge_spaces
        else "PASS_ALL_REQUIRED_CHARGES_ZERO",
    }

    interface_requirements = {
        "section_space_data": [
            "basis for H0(X,O(q)) for each required charge q",
            "dimension for each required section space",
            "zero/nonzero certificate for each required section space",
        ],
        "multiplication_data": [
            "bilinear product F_i x G_i -> P for each i",
            "basis coordinates in P",
            "coefficient vector proving sum_i g_i*f_i = 0",
        ],
        "constant_frame_data": [
            "definition of left-invariant frame for charged line-bundle sections",
            "transition or automorphy factors showing global well-definedness",
            "proof that constant frame coefficients represent sections of nonzero charges",
        ],
        "genericity_data": [
            "locally-free/open-condition test for the exact maps",
            "stability/HYM source certificate for the exact maps, not just generic unnamed maps",
        ],
    }

    source_has_construction_data = any(
        source_scan["terms"][key]
        for key in ("section_ring", "effective_cone", "automorphy", "theta_function", "factor_of_automorphy", "Cech", "rho_E")
    )

    output = {
        "certificate": "SelectedQaSU3IwasawaLineBundleSectionRingInterface",
        "status": "QA_SU3_IWASAWA_LINE_BUNDLE_SECTION_RING_INTERFACE_BUILT_VALUES_OPEN",
        "input_status": {"monad_map_gate": previous["status"]},
        "template_path": str(TEMPLATE.relative_to(ROOT)),
        "selected_source_scan": source_scan,
        "required_section_spaces": spaces,
        "constant_scalar_test": constant_scalar_test,
        "interface_requirements": interface_requirements,
        "gate_results": {
            "required_charge_list": "PASS_EXTRACTED_FROM_MONAD_MAP_GATE",
            "literal_constant_scalar_interpretation": constant_scalar_test["verdict"],
            "selected_source_section_ring_data": "FAIL_NOT_PRINTED"
            if not source_has_construction_data
            else "PARTIAL_SOURCE_TERMS_FOUND",
            "gf_zero_relation": "FAIL_MULTIPLICATION_TABLE_OPEN",
            "locally_free_condition": "FAIL_EXACT_MAPS_OPEN",
            "operator_exit": "FAIL_NO_DOLBEAULT_CECH_OR_RHOE_EXIT",
        },
        "interface_result": {
            "interface_built": True,
            "required_spaces_count": len(spaces),
            "all_required_charges_nonzero_under_literal_constant_test": len(nonzero_charge_spaces) == len(spaces),
            "literal_constant_map_route_blocked": bool(nonzero_charge_spaces),
            "selected_source_has_section_construction_data": source_has_construction_data,
            "explicit_maps_constructed": False,
            "qa_su3_closed": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": {
            "name": "Selected_Qa_SU3_Iwasawa_Automorphy_or_Section_Ring_Construction_v1",
            "must_choose": [
                "derive an automorphy/transition-factor model for charged sections on the compact Iwasawa quotient",
                "or source-print the section bases and multiplication table",
                "or retire the phrase constant matrices for nonzero line-bundle charges as insufficiently typed",
            ],
        },
    }
    text = json.dumps(output, indent=2, sort_keys=True)
    if "--write-certificate" in sys.argv:
        OUTPUT_CERT.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
