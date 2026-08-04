"""Import the q79 VAlpha/S3 integral-lift gap and selector obstruction."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
Q79_REPO = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
Q79_CERTS = Q79_REPO / "certificates"

PREVIOUS_IMPORT = CERTS / "selected_qa_su3_valpha_s3_mod3_compatibility_import_certificate.json"
Q79_APPELL = Q79_CERTS / "visible_rank2_l2_appell_humbert_automorphy_certificate.json"
Q79_PULLBACK = Q79_CERTS / "visible_rank2_l2_pullback_cech_attempt_certificate.json"
Q79_GAP = Q79_CERTS / "visible_rank2_l2_integral_lift_source_gap_certificate.json"
Q79_SELECTOR = Q79_CERTS / "visible_rank2_l2_selector_obstruction_certificate.json"

OUTPUT_CERT = CERTS / "selected_qa_su3_valpha_s3_integral_lift_gap_import_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    previous = load(PREVIOUS_IMPORT)
    appell = load(Q79_APPELL)
    pullback = load(Q79_PULLBACK)
    gap = load(Q79_GAP)
    selector = load(Q79_SELECTOR)

    output = {
        "certificate": "SelectedQaSU3VAlphaS3IntegralLiftGapImport",
        "status": "QA_SU3_VALPHA_S3_INTEGRAL_LIFT_GAP_IMPORTED_SOURCE_SELECTOR_REQUIRED",
        "inputs": {
            "previous_mod3_import": str(PREVIOUS_IMPORT.relative_to(ROOT)),
            "q79_appell_humbert": str(Q79_APPELL),
            "q79_pullback_cech": str(Q79_PULLBACK),
            "q79_integral_lift_gap": str(Q79_GAP),
            "q79_selector_obstruction": str(Q79_SELECTOR),
        },
        "closed_now": {
            "explicit_integral_appell_humbert_model_exists": appell[
                "what_this_closes"
            ]["explicit_nonflat_factor_of_automorphy_for_L2_2_minus4_0"],
            "ordinary_integral_c1_matrix_realized": appell["what_this_closes"][
                "ordinary_integral_c1_matrix_realized"
            ],
            "conditional_h1_positive_for_base_pullback_model": pullback[
                "what_this_closes"
            ]["conditional_h1_positive_for_base_pullback_model"],
            "h1_8_packet_has_no_remaining_algebraic_obstruction_after_source": gap[
                "what_this_closes"
            ]["existing_h1_8_packet_has_no_remaining_algebraic_obstruction_after_source"],
            "finite_mod3_qutrit_data_no_go_for_target_vs_swapped_integral_lift": gap[
                "what_this_closes"
            ]["finite_mod3_qutrit_data_no_go_for_target_vs_swapped_integral_lift"],
            "no_hidden_selector_in_current_topology_h1_qutrit_or_appell_humbert_data": selector[
                "what_this_closes"
            ]["no_hidden_selector_in_current_topology_h1_qutrit_or_appell_humbert_data"],
            "pic0_neutrality_not_selected_by_current_curvature_topology_data": selector[
                "what_this_closes"
            ]["pic0_neutrality_not_selected_by_current_curvature_topology_data"],
            "gap_reduced_to_new_symmetry_breaking_source": selector[
                "what_this_closes"
            ]["proof_target_reduced_to_new_symmetry_breaking_source"],
        },
        "selected_integral_candidate": {
            "target_L": gap["sufficient_source_contract"]["must_fix_target_not_swapped"][
                "target_L"
            ],
            "target_L2_degrees": gap["sufficient_source_contract"][
                "must_fix_target_not_swapped"
            ]["target_L2_degrees"],
            "swapped_L": gap["sufficient_source_contract"][
                "must_fix_target_not_swapped"
            ]["swapped_L"],
            "swapped_L2_degrees": gap["sufficient_source_contract"][
                "must_fix_target_not_swapped"
            ]["swapped_L2_degrees"],
            "ordered_integral_c1_matrix_required": gap["sufficient_source_contract"][
                "ordered_integral_c1_matrix_required"
            ],
            "base_order_contract": gap["sufficient_source_contract"][
                "must_tie_base_factor_order_to_source"
            ],
        },
        "cohomology_after_source": {
            "candidate_role_now": gap["existing_h1_packet"]["candidate_role"],
            "h1": gap["existing_h1_packet"]["h1"],
            "conditional_promoted_exit_code": gap["existing_h1_packet"][
                "conditional_promoted_validation"
            ]["exit_code"],
            "conditional_promoted_selected_source_promotes": gap[
                "existing_h1_packet"
            ]["conditional_promoted_validation"]["parsed_report"][
                "selected_source_promotes"
            ],
            "conditional_promoted_nonzero_ext_class": gap["existing_h1_packet"][
                "conditional_promoted_validation"
            ]["parsed_report"]["nonzero_ext_class"],
        },
        "selector_obstruction": {
            "theorem": selector["obstruction_theorem"]["theorem"],
            "valid_for_selector_inputs": selector["obstruction_theorem"][
                "valid_for_selector_inputs"
            ],
            "does_not_apply_if_new_source_supplies": selector["obstruction_theorem"][
                "does_not_apply_if_new_source_supplies"
            ],
            "target_and_swapped_degenerate_under_current_closed_invariants": selector[
                "no_breaking_source_available"
            ],
            "pic0_needs_holonomy_sensitive_source_or_gauge_fixing": selector[
                "pic0_invariance"
            ]["needs_holonomy_sensitive_source_or_gauge_fixing"],
        },
        "not_closed": {
            "selected_ordered_integral_Cech_automorphy_D_E_source": selector[
                "still_open"
            ]["selected_ordered_integral_Cech_automorphy_D_E_source"],
            "selected_target_wall_r1_over_r2_sqrt2": selector["still_open"][
                "selected_target_wall_r1_over_r2_sqrt2"
            ],
            "selected_or_quotiented_Pic0_character": selector["still_open"][
                "selected_or_quotiented_Pic0_character"
            ],
            "same_source_D_E_dotD_Hessian_base_ordering": selector["still_open"][
                "same_source_D_E_dotD_Hessian_base_ordering"
            ],
            "nonzero_Ext_class_selection": selector["still_open"][
                "nonzero_Ext_class_selection"
            ],
            "non_split_stability": selector["still_open"]["non_split_stability"],
            "full_SM_closure": selector["still_open"]["full_SM_closure"],
        },
        "next_source_options": [
            "selected target Gauduchon wall r1:r2=sqrt(2):1",
            "selected ordered integral Cech/automorphy/D_E source",
            "same-source D_E/dotD/Hessian term ordering the base factors",
            "holonomy-sensitive source selecting or quotienting Pic0 characters",
        ],
        "guardrails": {
            "claims_integral_source_selected": False,
            "claims_target_selector_proved": False,
            "claims_neutral_pic0_selected": False,
            "claims_selected_D_E_dotD_Hessian_constructed": False,
            "claims_full_SM_closure": False,
            "uses_observed_masses_or_mixings": False,
        },
        "relation_to_previous_gate": {
            "previous_status": previous["status"],
            "mod3_bridge_is_real": previous["closed_now"][
                "q79_mod3_compatibility_imported"
            ],
            "this_import_says_mod3_bridge_cannot_be_the_selector": True,
        },
        "honest_answer": (
            "The ordinary integral V_alpha L^2 automorphy model and h1=8 packet "
            "exist. The remaining failure is not cohomology existence; it is a "
            "source-selector theorem that must break target-vs-swapped and Pic0 "
            "degeneracy."
        ),
    }

    cert_text = json.dumps(output, indent=2, sort_keys=True)
    if "--write-certificate" in sys.argv:
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
