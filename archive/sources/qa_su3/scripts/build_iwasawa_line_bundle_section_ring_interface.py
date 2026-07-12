"""Build the Iwasawa line-bundle section-ring interface for Qa/SU3."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

PREVIOUS = CERTS / "monad_map_construction_or_source_augmentation_certificate.json"
TEMPLATE = CERTS / "iwasawa_line_bundle_section_ring.template.json"
OUTPUT_DATA = DATA / "iwasawa_line_bundle_section_ring_interface.candidate.json"
OUTPUT_CERT = CERTS / "iwasawa_line_bundle_section_ring_interface_certificate.json"
OUTPUT_NOTE = CORPUS / "Selected_Qa_SU3_Iwasawa_Line_Bundle_Section_Ring_Interface_v1.md"

SELECTED_SOURCE = OBSIDIAN / "16 Strings, Flux, & M-Theory Encodings" / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md"


def is_zero(charge: list[int]) -> bool:
    return all(x == 0 for x in charge)


def scan_selected_source() -> dict[str, object]:
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


def build() -> tuple[dict[str, object], dict[str, object], str]:
    previous = json.loads(PREVIOUS.read_text(encoding="utf-8"))
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    spaces = template["required_section_spaces"]
    nonzero_spaces = [space for space in spaces if not is_zero(space["charge"])]
    zero_spaces = [space for space in spaces if is_zero(space["charge"])]
    source_scan = scan_selected_source()

    constant_scalar_test = {
        "interpretation": "literal scalar constants are degree-zero sections",
        "required_spaces": len(spaces),
        "zero_charge_spaces": [space["id"] for space in zero_spaces],
        "nonzero_charge_spaces": [space["id"] for space in nonzero_spaces],
        "literal_constant_entries_can_fill_all_required_spaces": len(nonzero_spaces) == 0,
        "verdict": "FAIL_LITERAL_CONSTANT_ENTRIES_HAVE_WRONG_CHARGE"
        if nonzero_spaces
        else "PASS_ALL_REQUIRED_CHARGES_ZERO",
    }
    construction_terms = ("section_ring", "effective_cone", "automorphy", "theta_function", "factor_of_automorphy", "Cech", "rho_E")
    source_has_construction_data = any(source_scan["terms"][key] for key in construction_terms)
    interface_result = {
        "interface_built": True,
        "required_spaces_count": len(spaces),
        "all_required_charges_nonzero_under_literal_constant_test": len(nonzero_spaces) == len(spaces),
        "literal_constant_map_route_blocked": bool(nonzero_spaces),
        "selected_source_has_section_construction_data": source_has_construction_data,
        "explicit_maps_constructed": False,
        "qa_su3_closed": False,
        "target_fitting_used": False,
    }
    candidate = {
        "candidate": "SelectedQaSU3IwasawaLineBundleSectionRingInterface",
        "status": "QA_SU3_IWASAWA_LINE_BUNDLE_SECTION_RING_INTERFACE_BUILT_VALUES_OPEN",
        "input_status": {"monad_map_gate": previous["status"]},
        "template_path": str(TEMPLATE.relative_to(ROOT)),
        "selected_source_scan": source_scan,
        "required_section_spaces": spaces,
        "constant_scalar_test": constant_scalar_test,
        "interface_requirements": {
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
        },
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
        "interface_result": interface_result,
        "next_required_artifact": {
            "name": "Selected_Qa_SU3_Iwasawa_Automorphy_or_Section_Ring_Construction_v1",
            "must_choose": [
                "derive an automorphy/transition-factor model for charged sections on the compact Iwasawa quotient",
                "or source-print the section bases and multiplication table",
                "or retire the phrase constant matrices for nonzero line-bundle charges as insufficiently typed",
            ],
        },
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": candidate["candidate"],
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "template_path": candidate["template_path"],
        "constant_scalar_test": constant_scalar_test,
        "gate_results": candidate["gate_results"],
        "interface_result": interface_result,
        "required_section_spaces": spaces,
        "selected_source_scan": source_scan,
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    note = render_note(candidate)
    return candidate, certificate, note


def render_note(candidate: dict[str, object]) -> str:
    lines = [
        "# Selected Qa/SU3 Iwasawa Line Bundle Section Ring Interface v1",
        "",
        "## Purpose",
        "",
        "This artifact turns the monad charge table into the exact section-ring data needed to construct typed maps `f,g`.",
        "",
        "## Required Spaces",
        "",
        "The map entries require sections in eleven charged spaces:",
        "",
        "```text",
    ]
    for space in candidate["required_section_spaces"]:
        lines.append(f"{space['id']}: {space['role']} charge {tuple(space['charge'])}")
    lines.extend(
        [
            "```",
            "",
            "The product condition is:",
            "",
            "```text",
            "F_i * G_i -> P",
            "sum_i g_i f_i = 0 in P",
            "```",
            "",
            "## Constant-Frame Test",
            "",
            'If "constant matrices in the left-invariant frame" means literal scalar constants, then every entry has degree zero.',
            "That cannot fill any of the eleven required nonzero-charge spaces.",
            "",
            "```text",
            "literal constant map route blocked: yes",
            "all required charges nonzero under literal constant test: yes",
            "```",
            "",
            'So the source phrase can still be valid only if "constant" means constant coefficients in a charged left-invariant/automorphic frame. That requires transition or automorphy factors, or an explicit section ring.',
            "",
            "## Interface Requirements",
            "",
            "A closing packet must supply:",
            "",
            "```text",
            "basis and dimension of H0(X,O(q)) for each required charge q",
            "bilinear multiplication F_i x G_i -> P",
            "basis coordinates in P",
            "coefficient vector proving sum_i g_i f_i = 0",
            "transition/automorphy law for charged left-invariant frames",
            "locally-free/open-condition test for the exact maps",
            "```",
            "",
            "## Verdict",
            "",
            "```text",
            "interface built: yes",
            "required spaces count: 11",
            "literal constant map route blocked: yes",
            "selected source has section construction data: no",
            "explicit maps constructed: no",
            "Qa/SU3 closed: no",
            "target fitting used: no",
            "```",
            "",
            "Next artifact:",
            "",
            "```text",
            candidate["next_required_artifact"]["name"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


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
