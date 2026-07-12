"""Reduce the V_alpha/S3/DEDotD frontier to one source packet.

This synthesis consumes the latest q79 certificates and checks which blockers
are genuinely still independent.  The result is intentionally conservative:
the proof does not construct the selected source, but it proves that the old
S3, finite-branch, curvature-row, and H1-algebra blockers are no longer the
critical path.  The remaining object is a single selected V_alpha
Chern-Weil/operator-source packet.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
CANDIDATES = ROOT / "candidate_data"

CONSTANTS_IMPORT = CERTS / "constants_m1_cw_source_route_import_certificate.json"
S3_CLOSURE = CERTS / "visible_twisted_s3_class_restriction_closure_certificate.json"
GS_CURVATURE = CERTS / "time_oriented_m1_visible_green_schwarz_curvature_closure_certificate.json"
GS_SOURCE_ATTEMPT = CERTS / "time_oriented_m1_visible_gs_source_attempt_certificate.json"
VALPHA_S3_PACKET = CERTS / "selected_qa_su3_same_source_valpha_s3_operator_packet_attempt_certificate.json"
ORIENTATION_DEDOTD = CERTS / "selected_qa_su3_orientation_dedotd_source_attempt_certificate.json"
ANTIUNITARY = CERTS / "orientation_branch_antiunitary_equivalence_certificate.json"
PARITY = CERTS / "orientation_observable_parity_certificate.json"
ORDERED_SOURCE_GATE = CERTS / "visible_rank2_l2_ordered_source_promotion_gate_certificate.json"
SELECTOR_OBSTRUCTION = CERTS / "visible_rank2_l2_selector_obstruction_certificate.json"
TWO_BLOCK_REDUCTION = CERTS / "valpha_s3_two_block_source_selector_reduction_certificate.json"

OUT_CANDIDATE = CANDIDATES / "valpha_operator_source_critical_path.candidate.json"
OUT_CERT = CERTS / "valpha_operator_source_critical_path_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def status(path: Path) -> str:
    return load(path).get("status", "UNKNOWN")


def require_all_true(values: dict[str, bool]) -> bool:
    return all(value is True for value in values.values())


def count_open_items(cert: dict[str, Any]) -> int:
    open_items = cert.get("first_open_items", [])
    if isinstance(open_items, list):
        return len(open_items)
    return 0


def analyze() -> dict[str, Any]:
    constants = load(CONSTANTS_IMPORT)
    s3 = load(S3_CLOSURE)
    gs_curvature = load(GS_CURVATURE)
    gs_source = load(GS_SOURCE_ATTEMPT)
    valpha_s3 = load(VALPHA_S3_PACKET)
    orientation = load(ORIENTATION_DEDOTD)
    antiunitary = load(ANTIUNITARY)
    parity = load(PARITY)
    ordered_gate = load(ORDERED_SOURCE_GATE)
    obstruction = load(SELECTOR_OBSTRUCTION)
    two_block = load(TWO_BLOCK_REDUCTION)

    retired = {
        "constants_and_q79_target_aligned": constants["closed_now"][
            "rank2_ext_target_matches_q79_pullback_target"
        ],
        "h1_8_ext_algebra_compatible_after_source": constants["closed_now"][
            "q79_h1_8_packet_compatible_with_constants_template"
        ],
        "selected_s3_class_restriction_closed": s3["calculation_results"][
            "selected_S3_class_restriction_packet_constructed"
        ],
        "s3_freed_witten_and_block_projectors_closed": (
            s3["calculation_results"]["smooth_Freed_Witten_cancellation_closed"]
            and s3["calculation_results"]["block_sector_projector_retention_closed"]
        ),
        "visible_gs_curvature_row_closed": gs_curvature["calculation_results"][
            "visible_green_schwarz_curvature_verified"
        ],
        "finite_branch_pair_antiunitary_closed": antiunitary["what_this_closes"][
            "q79_q369_finite_operator_conjugacy"
        ],
        "cp_even_observable_parity_closed": parity["finite_operator_parity"][
            "finite_parity_closed"
        ],
        "two_block_mod3_shape_is_integral_shadow": two_block["what_this_closes"][
            "two_block_finite_shape_is_mod3_shadow_of_ordered_integral_L2"
        ],
    }

    still_open = {
        "selected_visible_bundle_or_sheaf_model": constants["still_open"][
            "selected_visible_bundle_or_sheaf_model"
        ],
        "selected_ordered_integral_source": ordered_gate["still_open"][
            "selected_ordered_integral_source_certificate"
        ],
        "terminal_monad_lane_selector": "terminal_monad_difference_L3_minus_K2_selector_closed must be true"
        in valpha_s3.get("first_open_items", []),
        "pic0_selection_or_quotient": (
            ordered_gate["still_open"]["pic0_selection_or_quotient_rule"]
            and obstruction["still_open"]["selected_or_quotiented_Pic0_character"]
        ),
        "nonzero_ext_and_stability": (
            "nonzero_ext_class_selected must be true"
            in valpha_s3.get("first_open_items", [])
            and "non_split_stability_proved must be true"
            in valpha_s3.get("first_open_items", [])
        ),
        "chern_weil_row_from_same_source": gs_source["still_open"][
            "Chern_Weil_derivation_from_selected_source"
        ],
        "hym_or_routec_residual": gs_source["still_open"][
            "HYM_or_Route_C_residual_for_visible_source"
        ],
        "selected_D_E_dotD_Riesz_Green": (
            orientation["what_this_does_not_close"]["selected_D_E_or_dotD_source_flags"]
            is False
            and constants["still_open"]["same_source_D_E_dotD_Riesz_Green"]
        ),
        "coherent_spectral_projectors": (
            "coherent_spectral_zero_mode_projectors_closed must be true"
            in valpha_s3.get("first_open_items", [])
        ),
        "primitive_C1_contractions": valpha_s3["what_this_does_not_close"][
            "primitive_C1_contractions"
        ]
        is False,
    }

    no_hidden_selector = (
        obstruction["status"] == "VISIBLE_RANK2_L2_SELECTOR_OBSTRUCTION_PROVED_SOURCE_REQUIRED"
        and two_block["selector_status"]["current_closed_selector_can_choose_target"] is False
    )
    same_source_attempt_open_count = count_open_items(valpha_s3)
    orientation_attempt_open_count = count_open_items(orientation)
    gs_source_rejected_only_as_source = (
        gs_source["calculation_results"]["required_visible_TrF_row_inserted"] is True
        and gs_source["calculation_results"]["visible_green_schwarz_source_verified"] is False
        and gs_source["attempted_source"]["selected_by_mtt"] is False
    )

    critical_packet_contract = {
        "name": "Selected_VAlpha_ChernWeil_Operator_Source.v1",
        "must_supply": [
            "selected q79/F,m=1 visible source identity",
            "rank-two V_alpha model with L=L3-K2=(1,-2,0) and L2=(2,-4,0)",
            "selected or physically quotiented Pic0 character",
            "selected nonzero H1(X,L2) extension class and non-split stability/HYM witness",
            "Chern-Weil derivation of the required visible TrF^2 alpha1 row from the same source",
            "HYM/Strominger or Route-C residual with selected_source_verified true",
            "typed transition/rhoE data feeding sector D_E action packets",
            "same-branch reduced Green and dotD_alpha1 response packets",
            "coherent spectral zero-mode projector retention",
            "primitive C1/Yukawa overlap contractions",
        ],
        "would_unlock_validators": [
            "validate_visible_rank2_l2_ordered_source_packet.py",
            "validate_time_oriented_m1_visible_gs_source.py",
            "validate_iwasawa_selected_source_promotion.py",
            "validate_selected_qa_su3_orientation_dedotd_source_packet.py",
            "validate_selected_qa_su3_same_source_valpha_s3_operator_packet.py",
        ],
    }

    reduction_closed = (
        require_all_true(retired)
        and require_all_true(still_open)
        and no_hidden_selector
        and same_source_attempt_open_count > 0
        and orientation_attempt_open_count > 0
        and gs_source_rejected_only_as_source
    )

    status_value = (
        "VALPHA_OPERATOR_SOURCE_CRITICAL_PATH_REDUCED_TO_SINGLE_PACKET_OPEN"
        if reduction_closed
        else "VALPHA_OPERATOR_SOURCE_CRITICAL_PATH_REDUCTION_INCONSISTENT"
    )

    return {
        "calculation": "VAlphaOperatorSourceCriticalPath",
        "status": status_value,
        "generated_by": "scripts/reduce_valpha_operator_source_critical_path.py",
        "input_statuses": {
            "constants_import": status(CONSTANTS_IMPORT),
            "s3_class_restriction_closure": status(S3_CLOSURE),
            "visible_gs_curvature": status(GS_CURVATURE),
            "visible_gs_source_attempt": status(GS_SOURCE_ATTEMPT),
            "same_source_valpha_s3_packet_attempt": status(VALPHA_S3_PACKET),
            "orientation_dedotd_attempt": status(ORIENTATION_DEDOTD),
            "antiunitary_equivalence": status(ANTIUNITARY),
            "observable_parity": status(PARITY),
            "ordered_source_gate": status(ORDERED_SOURCE_GATE),
            "selector_obstruction": status(SELECTOR_OBSTRUCTION),
            "two_block_source_selector_reduction": status(TWO_BLOCK_REDUCTION),
        },
        "retired_blockers": retired,
        "remaining_independent_obligations": still_open,
        "machine_open_counts": {
            "same_source_valpha_s3_open_items": same_source_attempt_open_count,
            "orientation_dedotd_open_items": orientation_attempt_open_count,
        },
        "source_row_diagnosis": {
            "visible_gs_attempt_has_required_row": gs_source["calculation_results"][
                "required_visible_TrF_row_inserted"
            ],
            "visible_gs_attempt_rejected_as_unselected_source": gs_source_rejected_only_as_source,
            "finite_D_E_Green_dotD_shape_reaches_validator_layer": orientation[
                "calculation_results"
            ]["q79_finite_equations_blocked_only_by_source_flags"],
            "q369_conjugate_reaches_same_layer": orientation["calculation_results"][
                "q369_finite_equations_blocked_only_by_source_flags"
            ],
        },
        "critical_packet_contract": critical_packet_contract,
        "what_this_closes": {
            "critical_path_is_not_h1_algebra": retired["h1_8_ext_algebra_compatible_after_source"],
            "critical_path_is_not_s3_freed_witten_or_block_projectors": retired[
                "s3_freed_witten_and_block_projectors_closed"
            ],
            "critical_path_is_not_visible_gs_curvature_row": retired[
                "visible_gs_curvature_row_closed"
            ],
            "critical_path_is_not_finite_q79_q369_matrix_shape": retired[
                "finite_branch_pair_antiunitary_closed"
            ],
            "critical_path_is_not_two_block_mod3_shape": retired[
                "two_block_mod3_shape_is_integral_shadow"
            ],
            "remaining_cut_set_collapsed_to_selected_source_packet": reduction_closed,
        },
        "what_this_does_not_close": {
            "selected_visible_valpha_source": False,
            "Pic0_selection_or_quotient": False,
            "nonzero_Ext_class_and_stability": False,
            "same_source_Chern_Weil_derivation": False,
            "selected_D_E_dotD_Riesz_Green": False,
            "primitive_C1_contractions": False,
            "full_SM_closure": False,
        },
        "guardrails": {
            "claims_selected_source_constructed": False,
            "claims_pic0_resolved": False,
            "claims_D_E_dotD_constructed": False,
            "claims_primitive_C1_contractions": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The frontier is now a single selected-source problem.  The "
                "q79 repo has retired H1 arithmetic, S3 class/Freed-Witten, "
                "visible GS curvature, finite two-block mod-3 shape, and "
                "q79/q369 finite matrix shape as independent blockers.  The "
                "open validators all ask for one source packet that selects "
                "V_alpha, resolves Pic0, derives the Chern-Weil row, and emits "
                "same-branch D_E/Riesz/Green/dotD plus primitive contractions."
            ),
            "next_action": (
                "Build Selected_VAlpha_ChernWeil_Operator_Source.v1 rather than "
                "another arithmetic search: it must be a selected rank-two "
                "V_alpha HYM/Route-C source on q79/F,m=1 with L3-K2, Pic0 "
                "resolution, stability, Chern-Weil derivation, and operator data."
            ),
        },
    }


def main() -> int:
    report = analyze()
    write(OUT_CANDIDATE, report)
    cert = {
        "certificate": "VAlphaOperatorSourceCriticalPath",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": str(OUT_CANDIDATE.relative_to(ROOT)),
        "input_statuses": report["input_statuses"],
        "retired_blockers": report["retired_blockers"],
        "remaining_independent_obligations": report["remaining_independent_obligations"],
        "machine_open_counts": report["machine_open_counts"],
        "source_row_diagnosis": report["source_row_diagnosis"],
        "critical_packet_contract": report["critical_packet_contract"],
        "what_this_closes": report["what_this_closes"],
        "what_this_does_not_close": report["what_this_does_not_close"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write(OUT_CERT, cert)
    print(json.dumps(report, indent=2, sort_keys=True))
    return (
        0
        if report["status"]
        == "VALPHA_OPERATOR_SOURCE_CRITICAL_PATH_REDUCED_TO_SINGLE_PACKET_OPEN"
        else 1
    )


if __name__ == "__main__":
    raise SystemExit(main())
