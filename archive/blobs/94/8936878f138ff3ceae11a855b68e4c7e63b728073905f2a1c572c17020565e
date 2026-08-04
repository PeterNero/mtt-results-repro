"""Construct or block the selected Qa/SU3 monad maps from available data."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
SOURCE_ROOT = OBSIDIAN
MONAD_SOURCE = OBSIDIAN / "16 Strings, Flux, & M-Theory Encodings" / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md"
PREVIOUS = CERTS / "selected_qa_su3_typed_monad_data_fill_attempt_certificate.json"
OUTPUT_CERT = CERTS / "selected_qa_su3_monad_map_construction_or_source_augmentation_certificate.json"


ELL = [
    [-2, 0, 1],
    [-1, 1, -1],
    [1, -1, 0],
    [1, 0, -1],
    [2, 1, 1],
]
KAPPA_1 = [1, 0, 0]
KAPPA_2 = [0, 1, 0]


def sub(a: list[int], b: list[int]) -> list[int]:
    return [x - y for x, y in zip(a, b, strict=True)]


def add(a: list[int], b: list[int]) -> list[int]:
    return [x + y for x, y in zip(a, b, strict=True)]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def scan_source_tree() -> dict[str, Any]:
    hits: dict[str, list[str]] = {
        "section_ring": [],
        "effective_cone": [],
        "line_bundle_sections": [],
        "generic_maps": [],
        "dolbeault": [],
        "cech": [],
    }
    terms = {
        "section_ring": "section ring",
        "effective_cone": "effective cone",
        "line_bundle_sections": "line bundle sections",
        "generic_maps": "generic holomorphic maps",
        "dolbeault": "Dolbeault",
        "cech": "Cech",
    }
    for path in SOURCE_ROOT.rglob("*.md"):
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for key, term in terms.items():
            if term in text:
                hits[key].append(str(path))
    selected_source_tool_hits = {
        key: [path for path in value if Path(path) == MONAD_SOURCE]
        for key, value in hits.items()
        if key in {"section_ring", "effective_cone", "line_bundle_sections"}
    }
    return {
        "root": str(SOURCE_ROOT),
        "hits": {key: sorted(value) for key, value in hits.items()},
        "selected_monad_source": str(MONAD_SOURCE),
        "selected_source_tool_hits": selected_source_tool_hits,
        "usable_for_monad_map_construction": {
            "selected_source_has_section_ring": bool(selected_source_tool_hits.get("section_ring")),
            "selected_source_has_effective_cone": bool(selected_source_tool_hits.get("effective_cone")),
            "selected_source_has_line_bundle_sections": bool(selected_source_tool_hits.get("line_bundle_sections")),
            "generic_maps_only_source": hits["generic_maps"],
            "dolbeault_sources": hits["dolbeault"],
            "cech_sources": hits["cech"],
        },
    }


def build_charge_table() -> list[dict[str, Any]]:
    rows = []
    total_composite_charge = sub(KAPPA_2, KAPPA_1)
    for index, ell in enumerate(ELL, start=1):
        f_charge = sub(ell, KAPPA_1)
        g_charge = sub(KAPPA_2, ell)
        rows.append(
            {
                "i": index,
                "ell_i": ell,
                "required_f_section_charge": f_charge,
                "required_g_section_charge": g_charge,
                "composite_charge_gi_fi": add(g_charge, f_charge),
                "composite_charge_matches_K2_minus_K1": add(g_charge, f_charge) == total_composite_charge,
                "f_section_found": False,
                "g_section_found": False,
            }
        )
    return rows


def main() -> None:
    previous = load(PREVIOUS)
    scan = scan_source_tree()
    charge_table = build_charge_table()
    all_composites_match = all(row["composite_charge_matches_K2_minus_K1"] for row in charge_table)
    any_sections_found = any(row["f_section_found"] or row["g_section_found"] for row in charge_table)
    source_tools = scan["usable_for_monad_map_construction"]

    output = {
        "certificate": "SelectedQaSU3MonadMapConstructionOrSourceAugmentation",
        "status": "QA_SU3_MONAD_MAP_CONSTRUCTION_BLOCKED_SECTION_RING_OR_SOURCE_AUGMENTATION_REQUIRED",
        "input_status": {"typed_monad_fill_attempt": previous["status"]},
        "selected_line_data": {
            "ell_i": ELL,
            "kappa_1": KAPPA_1,
            "kappa_2": KAPPA_2,
            "kappa_2_minus_kappa_1": sub(KAPPA_2, KAPPA_1),
        },
        "charge_table": charge_table,
        "source_scan": scan,
        "construction_logic": {
            "f_i_requires_section_of": "L_i tensor K1^{-1}",
            "g_i_requires_section_of": "K2 tensor L_i^{-1}",
            "gf_zero_condition": "sum_i g_i*f_i = 0 in H0(K2 tensor K1^{-1})",
            "all_composite_charges_match": all_composites_match,
            "why_this_matters": "the monad charges are algebraically compatible, but compatibility is not an explicit map",
        },
        "gate_results": {
            "charge_compatibility": "PASS_ALL_GI_FI_TERMS_HAVE_K2_MINUS_K1_CHARGE"
            if all_composites_match
            else "FAIL_COMPOSITE_CHARGE_MISMATCH",
            "section_ring_or_effective_cone": "FAIL_NOT_FOUND_IN_SELECTED_MONAD_SOURCE"
            if not (
                source_tools["selected_source_has_section_ring"]
                or source_tools["selected_source_has_effective_cone"]
                or source_tools["selected_source_has_line_bundle_sections"]
            )
            else "PARTIAL_SELECTED_SOURCE_TOOL_FOUND",
            "actual_f_sections": "FAIL_NOT_FOUND",
            "actual_g_sections": "FAIL_NOT_FOUND",
            "gf_zero": "FAIL_NO_SECTION_BASIS_OR_COEFFICIENTS",
            "locally_free": "FAIL_NO_EXACT_MAPS",
            "operator_packet": "FAIL_NO_DOLBEAULT_CECH_OR_RHOE_DERIVED_FROM_MONAD",
        },
        "construction_result": {
            "charge_table_computed": True,
            "charge_level_compatibility_passed": all_composites_match,
            "section_data_found": any_sections_found,
            "explicit_f_g_constructed": False,
            "g_f_zero_checked": False,
            "monad_route_retired": False,
            "source_augmentation_required": True,
            "qa_su3_closed": False,
            "target_fitting_used": False,
        },
        "minimal_source_augmentation": {
            "option_A_source_printed_maps": [
                "five typed entries f_i as sections of L_i tensor K1^{-1}",
                "five typed entries g_i as sections of K2 tensor L_i^{-1}",
                "a coefficient relation proving sum_i g_i*f_i = 0",
                "a local-freeness/stability certificate for those exact maps",
            ],
            "option_B_independent_construction_data": [
                "section ring or effective cone for the chosen Iwasawa line-bundle basis",
                "basis of H0 for every required f_i and g_i charge",
                "multiplication table into H0(K2 tensor K1^{-1})",
                "genericity/open-condition test for locally-free cohomology",
            ],
            "option_C_direct_operator_exit": [
                "Dolbeault/Cech matrices derived from the same monad",
                "or a validated rho_E transition packet with selected bundle origin",
            ],
        },
        "next_required_artifact": {
            "name": "Selected_Qa_SU3_Iwasawa_Line_Bundle_Section_Ring_Interface_v1",
            "purpose": "turn the computed charge table into actual section spaces and multiplication maps, or certify that the current corpus lacks the data.",
        },
    }
    text = json.dumps(output, indent=2, sort_keys=True)
    if "--write-certificate" in sys.argv:
        OUTPUT_CERT.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
