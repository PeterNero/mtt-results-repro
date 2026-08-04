"""Formulate the finite H^1(X,L^2) gate for the rank-two V_alpha route."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"

RANK2_CERT = CERTIFICATES / "visible_rank2_extension_valpha_route_certificate.json"
CANDIDATE = CANDIDATE_DATA / "visible_rank2_l2_ext_h1_gate.candidate.json"
CERTIFICATE = CERTIFICATES / "visible_rank2_l2_ext_h1_gate_certificate.json"
TEMPLATE = CERTIFICATES / "visible_rank2_l2_cohomology_data.template.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def square_coeffs(vector: list[int]) -> list[int]:
    x, y, z = vector
    return [2 * x * y, 2 * x * z, 2 * y * z]


def analyze() -> dict[str, Any]:
    rank2 = load_json(RANK2_CERT)
    line_classes = rank2.get("finite_line_class_solutions", [])
    preferred_l = [1, -2, 0]
    preferred = next(
        item for item in line_classes if item.get("l_vector_abc") == preferred_l
    )
    l2_vector = [2 * value for value in preferred_l]
    l2_square = square_coeffs(l2_vector)

    candidate_summaries = []
    for item in line_classes:
        vector = item["l_vector_abc"]
        l2 = [2 * value for value in vector]
        candidate_summaries.append(
            {
                "l_vector_abc": vector,
                "c1_L_squared_vector_abc": l2,
                "c1_L_squared_square_alpha_coeffs": square_coeffs(l2),
                "c2_extension_alpha_coeffs": item["c2_extension_alpha_coeffs"],
                "h1_data_required": "finite Cech/Dolbeault cochain matrices d0,d1 plus a closed non-exact C1 vector",
            }
        )

    template = {
        "schema": "VisibleRank2L2CohomologyData.v1",
        "status": "OPEN",
        "candidate_role": "SELECTED_DATA",
        "target": {
            "extension_sequence": "0 -> L -> V_alpha -> L^{-1} -> 0",
            "l_vector_abc": preferred_l,
            "c1_L_squared_vector_abc": l2_vector,
            "c1_L_squared_square_alpha_coeffs": l2_square,
            "c2_extension_alpha_coeffs": preferred["c2_extension_alpha_coeffs"],
        },
        "source": {
            "source_kind": None,
            "selected_by_mtt": None,
            "fixture_only": None,
            "source_certificate": None,
            "uses_observed_flavor_inputs": False,
            "uses_benchmark_flavor_inputs": False,
        },
        "cochain_complex": {
            "field": "exact rational complex numbers; entries are q or [real_q, imag_q]",
            "basis_labels_C0": None,
            "basis_labels_C1": None,
            "basis_labels_C2": None,
            "d0": None,
            "d1": None,
        },
        "reported_cohomology": {
            "rank_d0": None,
            "rank_d1": None,
            "dim_ker_d1": None,
            "h1": None,
            "nonzero_extension_class_label": None,
            "extension_class_vector_C1": None,
        },
        "acceptance_tests": {
            "d1_d0_zero": None,
            "h1_positive": None,
            "extension_class_closed": None,
            "extension_class_not_exact": None,
            "derived_without_observed_flavor_inputs": True,
        },
    }
    write_json(TEMPLATE, template)

    route_ready = (
        rank2.get("status")
        == "VISIBLE_RANK2_EXTENSION_VALPHA_ROUTE_FORMULATED_EXT_STABILITY_OPEN"
        and len(line_classes) == 4
    )

    report = {
        "calculation": "VisibleRank2L2ExtH1Gate",
        "status": (
            "VISIBLE_RANK2_L2_EXT_H1_VALIDATOR_FORMULATED_DATA_OPEN"
            if route_ready
            else "VISIBLE_RANK2_L2_EXT_H1_GATE_NOT_VERIFIED"
        ),
        "generated_by": "scripts/analyze_visible_rank2_l2_ext_h1_gate.py",
        "validator": "scripts/validate_visible_rank2_l2_cohomology.py",
        "input_certificate": RANK2_CERT.name,
        "template": "certificates/visible_rank2_l2_cohomology_data.template.json",
        "preferred_first_target": {
            "l_vector_abc": preferred_l,
            "c1_L_squared_vector_abc": l2_vector,
            "c1_L_squared_square_alpha_coeffs": l2_square,
            "c2_extension_alpha_coeffs": preferred["c2_extension_alpha_coeffs"],
        },
        "all_rank2_ext_targets": candidate_summaries,
        "finite_computation_contract": {
            "cochain_complex": "C0 --d0--> C1 --d1--> C2 for the selected holomorphic line bundle L^2",
            "computed_h1_formula": "h1 = dim ker(d1) - rank(d0)",
            "nonzero_ext_class_test": "eta in ker(d1) and eta not in im(d0)",
            "validator_exit_0": "complete packet passes finite algebraic checks",
            "validator_exit_2": "packet is open/incomplete rather than mathematically failed",
        },
        "why_current_data_do_not_compute_h1": {
            "topological_c1_is_not_enough": True,
            "holomorphic_representative_required": True,
            "needed_data": [
                "selected holomorphic line bundle representative for L^2",
                "Cech transition functions or Dolbeault operator for L^2",
                "finite cochain bases C0,C1,C2",
                "differentials d0,d1 with d1*d0=0",
                "closed non-exact C1 vector representing the extension class",
                "source certificate proving the data are selected by MTT and not a fixture",
            ],
        },
        "calculation_results": {
            "rank2_route_imported": route_ready,
            "validator_formulated": True,
            "open_template_written": True,
            "topological_L2_targets_computed": len(candidate_summaries),
            "H1_value_computed_from_selected_data": False,
            "selected_nonzero_ext_class_constructed": False,
            "stability_proved": False,
            "selected_hym_source_constructed": False,
        },
        "what_this_closes": {
            "exact_finite_input_format_for_H1_X_L_squared": True,
            "exact_nonzero_Ext_acceptance_test": True,
            "preferred_first_L2_target_for_next_fill": True,
            "false_topology_only_H1_claim_blocked": True,
        },
        "still_open": {
            "fill_template_with_selected_Cech_or_Dolbeault_data": True,
            "compute_actual_h1_for_L_squared": True,
            "select_nonzero_extension_class": True,
            "prove_non_split_extension_stability": True,
            "prove_HYM_or_Route_C_residual": True,
            "derive_same_total_source_D_E_dotD_Riesz_Green": True,
            "primitive_C1_contractions": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_H1_value_computed": False,
            "claims_extension_class_exists": False,
            "claims_stability_proved": False,
            "claims_selected_hym_source_exists": False,
            "claims_selected_D_E_dotD_constructed": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The Ext target is now executable as a finite cochain calculation, "
                "but the current selected corpus still does not contain the Cech "
                "or Dolbeault matrices for L^2. The next real closure step is to "
                "fill visible_rank2_l2_cohomology_data.template.json from selected "
                "geometry and pass the validator with h1>0 and a closed non-exact "
                "extension vector."
            ),
            "next_action": (
                "Construct the selected holomorphic L^2 data for l=(1,-2,0), "
                "fill d0,d1 and an extension class vector, then run "
                "scripts/validate_visible_rank2_l2_cohomology.py."
            ),
        },
    }
    return report


def main() -> int:
    report = analyze()
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "VisibleRank2L2ExtH1Gate",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "validator": report["validator"],
        "candidate_data": "candidate_data/visible_rank2_l2_ext_h1_gate.candidate.json",
        "input_certificate": report["input_certificate"],
        "template": report["template"],
        "preferred_first_target": report["preferred_first_target"],
        "all_rank2_ext_targets": report["all_rank2_ext_targets"],
        "finite_computation_contract": report["finite_computation_contract"],
        "why_current_data_do_not_compute_h1": report["why_current_data_do_not_compute_h1"],
        "calculation_results": report["calculation_results"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write_json(CERTIFICATE, certificate)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["status"] == "VISIBLE_RANK2_L2_EXT_H1_VALIDATOR_FORMULATED_DATA_OPEN" else 1


if __name__ == "__main__":
    raise SystemExit(main())
