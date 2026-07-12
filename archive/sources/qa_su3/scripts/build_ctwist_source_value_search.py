"""Search candidate values for the Qa/SU3 c-twist Deligne/Cech source."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

INPUT = DATA / "ctwist_deligne_cech_template.candidate.json"
OUTPUT_DATA = DATA / "ctwist_source_value_search.candidate.json"
OUTPUT_CERT = CERTS / "ctwist_source_value_search_certificate.json"

SOURCES = {
    "q79_s3_class_closure": Q79 / "proof_corpus" / "Visible_Twisted_S3_Class_Restriction_Closure_v1.md",
    "strominger_flux_selection": OBSIDIAN
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md",
    "iwasawa_flux_gerbe_quantization": OBSIDIAN
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md",
}


def contains(path: Path, needles: dict[str, str]) -> dict[str, object]:
    if not path.exists():
        return {"path": str(path), "present": False, "terms": {key: False for key in needles}}
    text = path.read_text(encoding="utf-8", errors="ignore").lower()
    return {
        "path": str(path),
        "present": True,
        "terms": {key: needle.lower() in text for key, needle in needles.items()},
    }


def main() -> None:
    template = json.loads(INPUT.read_text(encoding="utf-8"))
    scans = {
        "q79_s3_class_closure": contains(
            SOURCES["q79_s3_class_closure"],
            {
                "torsion_label_m_1": "torsion label m = 1",
                "B_i_zero": "local two-forms B_i = 0",
                "A_ij_zero": "local one-forms A_ij = 0",
                "H_zero": "curvature H = 0",
                "finite_table": "B((a,b),(c,d)) = -c*b/3 mod Z",
                "Freed_Witten_closed": "smooth S3 twisted Freed-Witten check",
            },
        ),
        "strominger_flux_selection": contains(
            SOURCES["strominger_flux_selection"],
            {
                "B_bundle_2_gerbe": "bundle 2--gerbe",
                "fixed_differential_class": "fixed differential cohomology class",
                "Hhat_global": "globally defined curvature",
                "fixed_topological_sector": "fix a topological sector",
                "Bianchi": "Bianchi",
            },
        ),
        "iwasawa_flux_gerbe_quantization": contains(
            SOURCES["iwasawa_flux_gerbe_quantization"],
            {
                "H_definition": "dB -",
                "integral_periods": "integral periods",
                "B_field_gerbe_global": "field gerbe is globally well-defined",
                "Iwasawa": "Iwasawa",
                "Bianchi_componentwise": "Bianchi identity is solved componentwise",
            },
        ),
    }
    value_candidates = [
        {
            "id": "q79_s3_flat_deligne_representative",
            "branch": "q79_visible_S3",
            "source": "q79_s3_class_closure",
            "values": {
                "tau_or_DD_class": "torsion label m=1; finite qutrit central cocycle",
                "B_i": "0",
                "A_ij": "0",
                "H": "0",
                "g_ijk_or_finite_2_cocycle": "exp(2*pi*i*B), B((a,b),(c,d))=-c*b/3 mod Z on F_3^2",
            },
            "passes_local_template_shape": True,
            "passes_same_branch_Qa_SU3_test": False,
            "promotion_status": "REJECT_AS_DIRECT_IMPORT_GUARDRAIL_ONLY",
            "reason": "The values are explicit and useful, but they are selected for q79/S3, not for the Qa/SU3 monad c-twist.",
        },
        {
            "id": "strominger_selected_fixed_differential_class",
            "branch": "MTT_heterotic_flux_Strominger",
            "source": "strominger_flux_selection",
            "values": {
                "tau_or_DD_class": "fixed differential cohomology/topological sector",
                "B_i": "local B-field potentials asserted but not enumerated",
                "A_ij": None,
                "Hhat": "global Green-Schwarz curvature",
                "g_ijk": None,
            },
            "passes_local_template_shape": False,
            "passes_same_branch_Qa_SU3_test": False,
            "promotion_status": "STRUCTURAL_SOURCE_VALUES_PARTIAL",
            "reason": "This is the correct physical selection setting, but the actual cover cocycle and its map to c=+/-1 are not supplied.",
        },
        {
            "id": "iwasawa_flux_quantized_gerbe",
            "branch": "Iwasawa_heterotic_flux",
            "source": "iwasawa_flux_gerbe_quantization",
            "values": {
                "tau_or_DD_class": "integral periods of H / B-field gerbe",
                "B_i": "implicit local B through H=dB-CS",
                "A_ij": None,
                "H": "i(partialbar-partial)J in invariant ansatz",
                "g_ijk": None,
            },
            "passes_local_template_shape": False,
            "passes_same_branch_Qa_SU3_test": False,
            "promotion_status": "IWA_STRUCTURAL_GERBE_NOT_CTWIST_VALUES",
            "reason": "The Iwasawa gerbe is global and quantized, but no finite c-twist class, cover data, or twisted module action is computed.",
        },
    ]
    best = "strominger_selected_fixed_differential_class"
    candidate = {
        "candidate": "SelectedQaSU3CTwistSourceValueSearch",
        "status": "CTWIST_SOURCE_VALUE_SEARCH_PARTIAL_VALUES_FOUND_SAME_BRANCH_OPEN",
        "input_status": template["status"],
        "source_scans": scans,
        "value_candidates": value_candidates,
        "best_current_candidate": best,
        "promotion_gate": {
            "must_supply_same_branch_tau": True,
            "must_supply_cover_or_cover_independent_representative": True,
            "must_map_tau_to_c_twist_values_minus1_plus1": True,
            "must_verify_Freed_Witten_and_Bianchi": True,
            "must_compute_twisted_sections_or_operator_exit": True,
        },
        "gate_results": {
            "explicit_values_found_any_branch": True,
            "explicit_q79_flat_values_found": True,
            "same_branch_Qa_SU3_values_found": False,
            "same_branch_tau_maps_to_required_c_twists": False,
            "Freed_Witten_Bianchi_verified_for_Qa_SU3": False,
            "selected_source_promoted": False,
            "fallback_A01_DE_should_run_in_parallel": True,
        },
        "no_go_condition_refined": "If the selected Strominger/Iwasawa gerbe topological sector has zero or incompatible restriction to the monad c-twist quotient, the gerbe route retires and Qa/SU3 must exit through A01/D_E.",
        "next_required_artifact": "Selected_Qa_SU3_Strominger_Source_to_CTwist_Map_or_NoGo_v1",
        "parallel_fallback": "Selected_Qa_SU3_A01_DE_Operator_Exit_v1",
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SelectedQaSU3CTwistSourceValueSearch",
        "status": "QA_SU3_CTWIST_SOURCE_VALUE_SEARCH_PARTIAL_VALUES_FOUND_SAME_BRANCH_OPEN",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "q79_explicit_flat_deligne_values_identified_as_guardrail": True,
            "strominger_fixed_differential_class_identified_as_best_same_branch_source_family": True,
            "iwasawa_quantized_gerbe_identified_as_structural_support": True,
            "direct_import_rejected": True,
        },
        "what_remains_open": {
            "same_branch_Qa_SU3_tau_or_DD_class": True,
            "same_branch_cover_or_cover_independent_representative": True,
            "map_tau_to_c_twist_values_minus1_plus1": True,
            "Freed_Witten_Bianchi_for_Qa_SU3": True,
            "twisted_section_bases_or_operator_exit": True,
            "qa_su3_packet_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "parallel_fallback": candidate["parallel_fallback"],
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
