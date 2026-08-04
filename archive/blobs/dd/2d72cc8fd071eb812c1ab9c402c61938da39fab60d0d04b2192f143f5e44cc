"""Import the q79 post-S3 visible operator-source cut set."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
Q79_CERTS = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro\certificates")

S3_LADDER = CERTS / "selected_qa_su3_m1_s3_source_origin_ladder_certificate.json"
GS_CURVATURE = Q79_CERTS / "time_oriented_m1_visible_green_schwarz_curvature_closure_certificate.json"
POST_S3_SOURCE = Q79_CERTS / "visible_operator_source_after_s3_closure_certificate.json"
ORIENTATION_BRIDGE = Q79_CERTS / "iwasawa_orientation_de_dotd_bridge_certificate.json"
ORIENTATION_ATTEMPT = Q79_CERTS / "selected_qa_su3_orientation_dedotd_source_attempt_certificate.json"

OUTPUT_CERT = CERTS / "selected_qa_su3_m1_operator_cutset_certificate.json"
OUTPUT_TEMPLATE = CERTS / "selected_qa_su3_m1_cw_operator_source.template.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def cw_operator_source_template() -> dict[str, Any]:
    return {
        "schema": "SelectedQaSU3M1ChernWeilOperatorSource.v1",
        "status": "OPEN_SELECTED_QA_SU3_M1_CW_OPERATOR_SOURCE_REQUIRED",
        "purpose": (
            "Derive the visible Tr_F^2 alpha_1 row from a selected q79/F,m=1 "
            "visible bundle, sheaf, or Route-C source and use that same source "
            "to fill spectral projectors, D_E, Riesz/Green, dotD, and C1 data."
        ),
        "accepted_prerequisites": {
            "selected_S3_twisted_source": "selected_qa_su3_m1_s3_source_origin_ladder_certificate.json",
            "visible_Green_Schwarz_curvature_row": "time_oriented_m1_visible_green_schwarz_curvature_closure_certificate.json",
            "finite_q79_q369_branch_packets_reach_validators": "selected_qa_su3_orientation_dedotd_source_attempt_certificate.json",
        },
        "must_supply": {
            "selected_visible_bundle_or_sheaf_model": None,
            "chern_weil_derivation_of_visible_TrF_row": None,
            "HYM_or_Route_C_residual_with_selected_source_verified": None,
            "coherent_spectral_zero_mode_projectors": None,
            "sector_D_E_action_matrices": None,
            "Riesz_projector_and_reduced_Green": None,
            "same_branch_dotD_alpha1_response": None,
            "antiunitary_equivalence_or_retarded_branch_selection": None,
            "primitive_C1_contractions": None,
        },
        "acceptance_tests": [
            "The visible Tr_F row is derived from the selected source, not inserted as a symbolic curvature row only.",
            "Exactly one branch is selected, or q79/q369 are proved antiunitarily equivalent until a retarded condition selects the branch.",
            "D_E, Riesz/Green, dotD, and C1 data cite the same selected source and branch.",
            "No observed flavor data or CP sign are used to choose the branch.",
        ],
        "forbidden_shortcuts": [
            "Do not treat Green-Schwarz curvature closure as selected operator-source closure.",
            "Do not turn selected_source_verified flags on without a source certificate.",
            "Do not choose q79 over q369 from the measured CKM phase.",
        ],
    }


def main() -> None:
    s3_ladder = load(S3_LADDER)
    gs = load(GS_CURVATURE)
    post_s3 = load(POST_S3_SOURCE)
    orientation = load(ORIENTATION_BRIDGE)
    orientation_attempt = load(ORIENTATION_ATTEMPT)
    template = cw_operator_source_template()

    output = {
        "certificate": "SelectedQaSU3M1OperatorCutset",
        "status": "QA_SU3_M1_OPERATOR_CUTSET_IMPORTED_CW_SOURCE_OPEN",
        "inputs": {
            "local_s3_source_origin_ladder": str(S3_LADDER.relative_to(ROOT)),
            "q79_visible_gs_curvature_closure": str(GS_CURVATURE),
            "q79_visible_operator_source_after_s3_closure": str(POST_S3_SOURCE),
            "q79_orientation_de_dotd_bridge": str(ORIENTATION_BRIDGE),
            "q79_orientation_dedotd_source_attempt": str(ORIENTATION_ATTEMPT),
        },
        "closed_now": {
            "selected_s3_source_support_closed": post_s3["calculation_results"][
                "selected_s3_support_now_closed"
            ],
            "old_s3_gerbe_fw_projector_blockers_retired": post_s3[
                "calculation_results"
            ]["old_s3_gerbe_fw_projector_blockers_retired"],
            "visible_green_schwarz_curvature_row_closed": gs[
                "calculation_results"
            ]["visible_green_schwarz_curvature_verified"],
            "visible_gs_zero_symbolic_bianchi_residual": gs["what_this_closes"][
                "zero_Bianchi_residual_for_required_symbolic_row"
            ],
            "finite_q79_and_q369_reach_validator_layer": orientation_attempt[
                "calculation_results"
            ]["both_branch_packets_exist"]
            and orientation_attempt["calculation_results"][
                "q79_finite_equations_blocked_only_by_source_flags"
            ]
            and orientation_attempt["calculation_results"][
                "q369_finite_equations_blocked_only_by_source_flags"
            ],
            "orientation_reduced_to_conjugate_pair": orientation[
                "calculation_results"
            ]["conjugate_pair_only"],
        },
        "cut_set": {
            "selected_visible_bundle_or_sheaf_model": post_s3[
                "still_open_cut_set"
            ]["selected_visible_bundle_or_sheaf_model"],
            "Chern_Weil_row_derived_from_selected_source": post_s3[
                "still_open_cut_set"
            ]["Chern_Weil_row_derived_from_selected_source"],
            "HYM_or_Route_C_residual_for_visible_source": post_s3[
                "still_open_cut_set"
            ]["HYM_or_Route_C_residual_for_visible_source"],
            "coherent_spectral_zero_mode_projectors": post_s3[
                "still_open_cut_set"
            ]["coherent_spectral_zero_mode_projectors"],
            "selected_D_E_dotD_Riesz_Green": post_s3["still_open_cut_set"][
                "selected_D_E_dotD_Riesz_Green"
            ],
            "same_branch_dotD_alpha1_driver": orientation["still_open"][
                "selected_dotD_same_branch_derivative"
            ],
            "antiunitary_equivalence_or_retarded_branch_selection": orientation[
                "still_open"
            ]["antiunitary_equivalence_or_retarded_branch_selection_proof"],
            "primitive_C1_contractions": post_s3["still_open_cut_set"][
                "primitive_C1_contractions"
            ],
        },
        "branch_status": {
            "branch_packets": orientation["branch_packets"],
            "unique_m1_vs_m2_selection_open": orientation["still_open"][
                "unique_m1_vs_m2_selection"
            ],
            "orientation_attempt_first_open_items": orientation_attempt[
                "first_open_items"
            ],
            "subvalidator_exit_codes": orientation_attempt["subvalidator_exit_codes"],
        },
        "relation_to_s3_ladder": {
            "previous_status": s3_ladder["status"],
            "s3_ladder_removed_from_source_origin_gap": s3_ladder[
                "relation_to_deresponse_gate"
            ]["removed_from_source_origin_gap"],
            "this_import_removes_symbolic_GS_curvature_from_cut_set": True,
            "this_import_leaves_selected_CW_operator_source_as_first_gate": True,
        },
        "next_object": {
            "name": "Selected_Qa_SU3_M1_Chern_Weil_Operator_Source_v1",
            "template": str(OUTPUT_TEMPLATE.relative_to(ROOT)),
            "role": post_s3["verdict"]["next_action"],
        },
        "guardrails": {
            "claims_selected_visible_operator_source_constructed": post_s3[
                "guardrails"
            ]["claims_selected_visible_operator_source_constructed"],
            "claims_chern_weil_row_derived_from_selected_bundle": post_s3[
                "guardrails"
            ]["claims_chern_weil_row_derived_from_selected_bundle"],
            "claims_coherent_spectral_projectors_constructed": post_s3[
                "guardrails"
            ]["claims_coherent_spectral_projectors_constructed"],
            "claims_selected_D_E_dotD_constructed": post_s3["guardrails"][
                "claims_selected_D_E_dotD_constructed"
            ],
            "claims_full_SM_closure": post_s3["guardrails"][
                "claims_full_SM_closure"
            ],
            "uses_observed_flavor_data": post_s3["guardrails"][
                "uses_observed_flavor_data"
            ],
        },
        "honest_answer": (
            "The visible Green-Schwarz curvature equation is closed at the "
            "symbolic curvature level, and both q79/q369 branch packets reach "
            "the finite validator layer. The remaining cut set is the selected "
            "Chern-Weil/operator source and same-branch spectral D_E/dotD data."
        ),
    }

    cert_text = json.dumps(output, indent=2, sort_keys=True)
    if "--write-certificate" in sys.argv:
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_TEMPLATE.write_text(
            json.dumps(template, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print(cert_text)


if __name__ == "__main__":
    main()
