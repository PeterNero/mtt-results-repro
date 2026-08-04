"""Build the complex-rotated c-twist primitive normalization gate."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"

TRANSGRESSION = DATA / "ctwist_transgression_pairing_computation.candidate.json"
TEMPLATE = DATA / "ctwist_deligne_cech_template.candidate.json"
OUTPUT_DATA = DATA / "complex_rotated_ctwist_normalization.candidate.json"
OUTPUT_CERT = CERTS / "complex_rotated_ctwist_normalization_certificate.json"


def parse_i_unit(text: str) -> complex:
    cleaned = text.strip()
    if cleaned.startswith("(") and cleaned.endswith(")"):
        cleaned = cleaned[1:-1]
    cleaned = cleaned.replace("-0", "0")
    return complex(cleaned)


def is_unit_imaginary(text: str) -> bool:
    value = parse_i_unit(text)
    return abs(value.real) < 1e-12 and abs(abs(value.imag) - 1) < 1e-12


def slant_primitive_rows(transgression: dict) -> list[dict]:
    rows = []
    for item in transgression["slant_pairings"]:
        components = item["central_components"]
        central_axis_count = len(components)
        coefficient = next(iter(components.values())) if central_axis_count == 1 else None
        axis = next(iter(components.keys())) if central_axis_count == 1 else None
        unit_imaginary = coefficient is not None and is_unit_imaginary(coefficient)
        rows.append(
            {
                "base_pair": item["base_pair"],
                "central_axis": axis,
                "coefficient": coefficient,
                "coefficient_is_unit_imaginary": unit_imaginary,
                "primitive_after_complex_polarization": unit_imaginary and axis in {"g5", "g6"},
                "raw_nil_axis_match_required": False,
            }
        )
    return rows


def product_rows(template: dict) -> list[dict]:
    rows = []
    for item in template["product_checks"]:
        rows.append(
            {
                "pair": item["pair"],
                "target": item["target"],
                "c_twist_sum": item["c_twist_sum"],
                "c_twist_target": item["c_twist_target"],
                "opposite_twists_cancel": item["c_twist_sum"] == item["c_twist_target"] == 0,
                "passes_template_typing": item["passes_template_typing"],
            }
        )
    return rows


def main() -> None:
    transgression = json.loads(TRANSGRESSION.read_text(encoding="utf-8"))
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    slants = slant_primitive_rows(transgression)
    products = product_rows(template)
    all_slants_primitive = all(item["primitive_after_complex_polarization"] for item in slants)
    all_products_cancel = all(item["opposite_twists_cancel"] and item["passes_template_typing"] for item in products)
    module_counts = {
        "+1": sum(1 for item in template["module_labels"].values() if item["c_twist"] == 1),
        "-1": sum(1 for item in template["module_labels"].values() if item["c_twist"] == -1),
        "0": sum(1 for item in template["module_labels"].values() if item["c_twist"] == 0),
    }
    conditional_normalization = all_slants_primitive and all_products_cancel
    candidate = {
        "candidate": "SelectedQaSU3ComplexRotatedCTwistNormalization",
        "status": "COMPLEX_ROTATED_CTWIST_PRIMITIVE_NORMALIZATION_CONDITIONAL_PERIOD_OPEN",
        "input_statuses": {
            "transgression": transgression["status"],
            "deligne_cech_template": template["status"],
        },
        "complex_central_polarization": {
            "central_plane": "span_R{g5,g6}",
            "complex_generator": "tau_c = primitive complex-polarized generator in span{g5,g6}",
            "phase_rule": "coefficients +/- i are unit phase rotations of the same primitive central generator",
            "direct_nil_axis_match_required": False,
        },
        "normalization_claim": {
            "proved_in_scaled_iwasawa_frame": "every computed H slant is a unit imaginary multiple of exactly one central basis vector",
            "conditional_period_unit": "if the selected flux/Deligne period unit identifies the scaled central primitive with tau_c, then the module twists are c=+/-1",
            "not_proved_here": "the absolute same-branch period unit or finite quotient selection",
        },
        "slant_primitive_checks": slants,
        "module_twist_counts": module_counts,
        "product_cancellation_checks": products,
        "gate_results": {
            "all_slants_unit_magnitude_in_scaled_frame": all(is_unit_imaginary(item["coefficient"]) for item in slants),
            "all_slants_single_central_axis": all(item["central_axis"] in {"g5", "g6"} for item in slants),
            "all_slants_primitive_after_complex_polarization": all_slants_primitive,
            "raw_nil_axis_match_required_for_ctwist_typing": False,
            "all_monad_products_remain_untwisted": all_products_cancel,
            "conditional_c_plus_minus_one_normalization": conditional_normalization,
            "selected_flux_period_normalization_proved": False,
            "same_branch_finite_quotient_selected": False,
            "Deligne_Cech_source_values_supplied": False,
            "Freed_Witten_Bianchi_for_mapped_module_verified": False,
            "twisted_section_bases_or_operator_exit_supplied": False,
            "full_promotion_to_source": False,
            "closure_claimed": False,
        },
        "interpretation": [
            "The transgression result is strong enough to supply a primitive complex-polarized c-twist generator in the scaled invariant frame.",
            "The Deligne/Cech template already needs only opposite +/- twists and their cancellation to the ordinary target.",
            "Therefore the remaining normalization problem is one scalar period/finite-quotient selection, not a missing central support computation.",
            "This artifact does not close the Qa/SU3 packet because it does not select that absolute period unit.",
        ],
        "next_required_artifact": "Selected_Qa_SU3_CTwist_Period_Normalization_or_A01_Exit_v1",
        "parallel_fallback": "Selected_Qa_SU3_A01_DE_Operator_Exit_v1",
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SelectedQaSU3ComplexRotatedCTwistNormalization",
        "status": "QA_SU3_COMPLEX_ROTATED_CTWIST_PRIMITIVE_NORMALIZATION_CONDITIONAL_PERIOD_OPEN",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "unit_imaginary_slant_coefficients_in_scaled_frame": candidate["gate_results"]["all_slants_unit_magnitude_in_scaled_frame"],
            "single_axis_central_primitive_support": candidate["gate_results"]["all_slants_single_central_axis"],
            "complex_polarized_primitive_generator_available": candidate["gate_results"]["all_slants_primitive_after_complex_polarization"],
            "direct_raw_nil_axis_match_not_required_for_twist_typing": True,
            "conditional_c_plus_minus_one_typing_normalization": conditional_normalization,
            "all_monad_products_remain_untwisted": all_products_cancel,
        },
        "what_remains_open": {
            "selected_flux_period_normalization": True,
            "same_branch_finite_quotient": True,
            "explicit_Deligne_Cech_source_values": True,
            "Freed_Witten_Bianchi_for_mapped_module": True,
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
