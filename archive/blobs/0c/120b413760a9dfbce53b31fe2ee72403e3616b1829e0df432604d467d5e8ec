"""Build the selected Qa/SU3 monad map-construction/source-augmentation gate."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

INPUT = DATA / "typed_monad_data_fill_attempt.candidate.json"
OUTPUT_DATA = DATA / "monad_map_construction_or_source_augmentation.candidate.json"
OUTPUT_CERT = CERTS / "monad_map_construction_or_source_augmentation_certificate.json"
OUTPUT_NOTE = CORPUS / "Selected_Qa_SU3_Monad_Map_Construction_or_Source_Augmentation_v1.md"

SELECTED_SOURCE = OBSIDIAN / "16 Strings, Flux, & M-Theory Encodings" / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md"
SUPPORT_SOURCES = [
    SELECTED_SOURCE,
    OBSIDIAN
    / "18 Theta-Closure & Execution Program"
    / "A_Tiered_Roadmap_for_Calculations_in_Modal_Triplet_Theory__MTT__v2.md",
    OBSIDIAN
    / "18 Theta-Closure & Execution Program"
    / "Theta_Closure_in_Modal_Triplet_Theory_III__Twistor_Action_Matching_and_Independent_Normalization.md",
]

TERM_PATTERNS = {
    "generic_maps": ["generic holomorphic maps", "generic maps"],
    "constant_matrices": ["constant matrices in the left-invariant frame", "constant matrices"],
    "dolbeault": ["dolbeault"],
    "section_ring": ["section ring", "section-ring"],
    "line_bundle_sections": ["line-bundle section", "line bundle section", "sections of line bundles"],
    "effective_cone": ["effective cone"],
    "cech": ["cech", "cech", "čech"],
    "rhoE": ["rho_e", "rhoE"],
}


def vadd(a: list[int], b: list[int]) -> list[int]:
    return [x + y for x, y in zip(a, b)]


def vsub(a: list[int], b: list[int]) -> list[int]:
    return [x - y for x, y in zip(a, b)]


def source_hits() -> dict[str, object]:
    hits: dict[str, list[str]] = {key: [] for key in TERM_PATTERNS}
    present_sources = []
    for path in SUPPORT_SOURCES:
        if not path.exists():
            continue
        present_sources.append(str(path))
        text = path.read_text(encoding="utf-8", errors="ignore").lower()
        for key, patterns in TERM_PATTERNS.items():
            if any(pattern.lower() in text for pattern in patterns):
                hits[key].append(str(path))

    selected_terms = {key: False for key in TERM_PATTERNS}
    if SELECTED_SOURCE.exists():
        selected_text = SELECTED_SOURCE.read_text(encoding="utf-8", errors="ignore").lower()
        selected_terms = {
            key: any(pattern.lower() in selected_text for pattern in patterns)
            for key, patterns in TERM_PATTERNS.items()
        }

    return {
        "root": str(OBSIDIAN),
        "selected_monad_source": str(SELECTED_SOURCE),
        "support_sources_present": present_sources,
        "hits": hits,
        "selected_source_terms": selected_terms,
        "usable_for_monad_map_construction": {
            "selected_source_has_effective_cone": selected_terms["effective_cone"],
            "selected_source_has_line_bundle_sections": selected_terms["line_bundle_sections"],
            "selected_source_has_section_ring": selected_terms["section_ring"],
            "selected_source_has_cech_data": selected_terms["cech"],
            "selected_source_has_rhoE": selected_terms["rhoE"],
        },
    }


def build() -> tuple[dict[str, object], dict[str, object], str]:
    previous = json.loads(INPUT.read_text(encoding="utf-8"))
    monad = previous["partial_packet"]["typed_monad"]
    ell_i = monad["ell_i"]
    kappa_1, kappa_2 = monad["kappa_a"]
    target = vsub(kappa_2, kappa_1)

    charge_table = []
    for index, ell in enumerate(ell_i, start=1):
        f_charge = vsub(ell, kappa_1)
        g_charge = vsub(kappa_2, ell)
        composite = vadd(f_charge, g_charge)
        charge_table.append(
            {
                "i": index,
                "ell_i": ell,
                "required_f_section_charge": f_charge,
                "required_g_section_charge": g_charge,
                "composite_charge_gi_fi": composite,
                "composite_charge_matches_K2_minus_K1": composite == target,
                "f_section_found": False,
                "g_section_found": False,
            }
        )

    scan = source_hits()
    construction_result = {
        "charge_table_computed": True,
        "charge_level_compatibility_passed": all(row["composite_charge_matches_K2_minus_K1"] for row in charge_table),
        "section_data_found": False,
        "explicit_f_g_constructed": False,
        "g_f_zero_checked": False,
        "monad_route_retired": False,
        "source_augmentation_required": True,
        "qa_su3_closed": False,
        "target_fitting_used": False,
    }
    candidate = {
        "candidate": "SelectedQaSU3MonadMapConstructionOrSourceAugmentation",
        "status": "QA_SU3_MONAD_MAP_CONSTRUCTION_BLOCKED_SECTION_RING_OR_SOURCE_AUGMENTATION_REQUIRED",
        "input_statuses": {"typed_monad_fill_attempt": previous["status"]},
        "selected_line_data": {
            "ell_i": ell_i,
            "kappa_1": kappa_1,
            "kappa_2": kappa_2,
            "kappa_2_minus_kappa_1": target,
        },
        "construction_logic": {
            "f_i_requires_section_of": "L_i tensor K1^{-1}",
            "g_i_requires_section_of": "K2 tensor L_i^{-1}",
            "gf_zero_condition": "sum_i g_i*f_i = 0 in H0(K2 tensor K1^{-1})",
            "all_composite_charges_must_equal": target,
        },
        "charge_table": charge_table,
        "source_scan": scan,
        "gate_results": {
            "charge_compatibility": "PASS_ALL_GI_FI_TERMS_HAVE_K2_MINUS_K1_CHARGE",
            "actual_f_sections": "FAIL_NOT_FOUND",
            "actual_g_sections": "FAIL_NOT_FOUND",
            "gf_zero": "FAIL_NO_SECTION_BASIS_OR_COEFFICIENTS",
            "locally_free": "FAIL_NO_EXACT_MAPS",
            "section_ring_or_effective_cone": "FAIL_NOT_FOUND_IN_SELECTED_MONAD_SOURCE",
            "operator_packet": "FAIL_NO_DOLBEAULT_CECH_OR_RHOE_DERIVED_FROM_MONAD",
        },
        "minimal_source_augmentation": [
            "print five typed f_i entries and five typed g_i entries, with the relation proving sum_i g_i*f_i=0",
            "or print the Iwasawa line-bundle section ring: H0 bases and multiplication table for the ten required charges plus K2-K1",
            "or print a direct Dolbeault/Cech/rho_E operator exit derived from the same monad",
        ],
        "construction_result": construction_result,
        "next_required_artifact": "Selected_Qa_SU3_Iwasawa_Line_Bundle_Section_Ring_Interface_v1",
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SelectedQaSU3MonadMapConstructionOrSourceAugmentation",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "selected_line_data": candidate["selected_line_data"],
        "charge_table": charge_table,
        "gate_results": candidate["gate_results"],
        "construction_result": construction_result,
        "source_scan": scan,
        "what_closes": {
            "required_f_and_g_section_charges_computed": True,
            "charge_level_compatibility_passed": construction_result["charge_level_compatibility_passed"],
            "blocked_object_identified_as_section_ring_or_source_augmentation": True,
        },
        "what_remains_open": {
            "actual_f_sections": True,
            "actual_g_sections": True,
            "section_basis_for_all_required_charges": True,
            "multiplication_table_into_K2_minus_K1": True,
            "gf_zero_relation": True,
            "locally_free_exact_map_certificate": True,
            "same_monad_operator_exit": True,
            "qa_su3_packet_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    note = render_note(candidate)
    return candidate, certificate, note


def render_note(candidate: dict[str, object]) -> str:
    lines = [
        "# Selected Qa/SU3 Monad Map Construction or Source Augmentation v1",
        "",
        "## Result",
        "",
        "The printed Iwasawa SU3 monad topology is charge-compatible with typed maps, but it does not yet construct the maps.",
        "For each summand, the required map entries are sections of `L_i tensor K1^{-1}` and `K2 tensor L_i^{-1}`.",
        "Every product `g_i f_i` lands in the same charge `K2-K1 = (-1, 1, 0)`, so the obstruction is not a charge mismatch.",
        "",
        "## Charge Table",
        "",
        "| i | ell_i | f_i charge | g_i charge | g_i f_i charge | compatible |",
        "|---|---|---|---|---|---|",
    ]
    for row in candidate["charge_table"]:
        lines.append(
            f"| {row['i']} | {tuple(row['ell_i'])} | {tuple(row['required_f_section_charge'])} | "
            f"{tuple(row['required_g_section_charge'])} | {tuple(row['composite_charge_gi_fi'])} | "
            f"{'yes' if row['composite_charge_matches_K2_minus_K1'] else 'no'} |"
        )
    lines.extend(
        [
            "",
            "## Gate Verdict",
            "",
            "- charge table computed: yes",
            "- charge-level compatibility passed: yes",
            "- section data found: no",
            "- explicit f,g constructed: no",
            "- g*f=0 checked: no",
            "- monad route retired: no",
            "- source augmentation required: yes",
            "- Qa/SU3 closed: no",
            "- target fitting used: no",
            "",
            "## Minimal Data Needed",
            "",
            "A closure source must provide one of these:",
            "",
            "- five typed `f_i` entries, five typed `g_i` entries, and the relation `sum_i g_i f_i = 0`;",
            "- an Iwasawa line-bundle section ring: bases for all required `H0` spaces and the multiplication table into `H0(K2 tensor K1^{-1})`;",
            "- a direct same-monad Dolbeault/Cech/`rho_E` operator exit.",
            "",
            "## Next Artifact",
            "",
            candidate["next_required_artifact"],
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
