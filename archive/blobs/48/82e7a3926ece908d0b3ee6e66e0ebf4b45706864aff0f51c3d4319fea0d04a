"""Build the visible V_alpha Chern/Bianchi source-packet candidate ledger.

The previous gates leave a very specific missing object: a selected visible
source whose Chern/Bianchi data realize c1=0, c2=+4 alpha_1, and whose same
source also supplies the operator data used later for flavor.  This script does
not claim that object exists.  It assembles the live candidates from already
audited certificates, ranks the next branch, and records the exact fields that
must be filled before promotion is allowed.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"

RANK2_EXT = CERTIFICATES / "visible_rank2_extension_valpha_route_certificate.json"
L2_H1 = CERTIFICATES / "visible_rank2_l2_ext_h1_gate_certificate.json"
INTEGRAL_ROW = CERTIFICATES / "visible_integral_chern_source_candidate_certificate.json"
SPLIT_NO_GO = CERTIFICATES / "visible_split_line_hym_no_go_certificate.json"
SIGN_GATE = CERTIFICATES / "visible_stable_source_sign_gate_certificate.json"
TERMINAL_SIGN = CERTIFICATES / "terminal_map_dual_extension_sign_certificate.json"
TWISTED_S3 = CERTIFICATES / "visible_twisted_s3_class_restriction_closure_certificate.json"
CONSTANTS_GR = CERTIFICATES / "constants_gr_cross_repo_clues_certificate.json"

CANDIDATE = CANDIDATE_DATA / "visible_valpha_chern_bianchi_source_packet_candidates.candidate.json"
CERTIFICATE = CERTIFICATES / "visible_valpha_chern_bianchi_source_packet_candidates_certificate.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def status_of(data: dict[str, Any]) -> str | None:
    return data.get("status")


def open_field(label: str, requirement: str) -> dict[str, Any]:
    return {"label": label, "status": "OPEN", "requirement": requirement}


def formulated_field(label: str, evidence: str) -> dict[str, Any]:
    return {"label": label, "status": "FORMULATED", "evidence": evidence}


def preferred_line_solution(rank2: dict[str, Any]) -> dict[str, Any]:
    for item in rank2.get("finite_line_class_solutions", []):
        if item.get("l_vector_abc") == [1, -2, 0]:
            return item
    raise ValueError("preferred L=(1,-2,0) solution missing")


def build_packet_interface(constants_gr: dict[str, Any]) -> dict[str, Any]:
    imported = constants_gr.get("useful_imports_for_q79_sm_closure", {})
    source_discipline = imported.get("selected_source_packet_discipline", {})
    imported_fields = source_discipline.get("core_fields_to_reuse_for_visible_valpha", [])
    visible_fields = [
        "source_certificate",
        "selected_holomorphic_structure_for_L_squared",
        "finite_Cech_or_Dolbeault_cochain_packet",
        "nonzero_closed_nonexact_Ext_vector",
        "non_split_extension_and_stability_certificate",
        "Chern_Bianchi_Freed_Witten_packet_for_c2_4_alpha1",
        "HYM_or_Strominger_or_Route_C_residual_certificate",
        "same_source_D_E_operator_block",
        "same_source_dotD_alpha1_response",
        "Riesz_projector_and_reduced_Green_packet",
        "trace_action_normalization",
        "SM_sector_projector_retention",
    ]
    return {
        "schema": "VisibleVAlphaSourcePacket.v1",
        "imported_method_fields": imported_fields,
        "visible_required_fields": visible_fields,
        "promotion_rule": (
            "A candidate is selected only if every visible required field is "
            "filled from the same MTT branch and no observed/benchmark SM "
            "flavor inputs are used."
        ),
        "hard_acceptance_tests": [
            "H^1(X,L^2) validator exits 0 for selected data with h1>0",
            "the selected Ext vector is closed and not exact",
            "the extension is non-split and stable in the selected chamber",
            "Chern/Bianchi/Freed-Witten data realize c1=0,c2=+4 alpha_1 on the same source",
            "HYM/Strominger residual or Route-C finite residual is certified",
            "D_E, dotD_alpha1, Riesz projector, and Green operator are derived from the same source",
            "sector projectors and SM dictionary are recomputed or protected for the total source",
        ],
    }


def analyze() -> dict[str, Any]:
    rank2 = load_json(RANK2_EXT)
    l2_h1 = load_json(L2_H1)
    integral = load_json(INTEGRAL_ROW)
    split = load_json(SPLIT_NO_GO)
    sign = load_json(SIGN_GATE)
    terminal_sign = load_json(TERMINAL_SIGN)
    twisted = load_json(TWISTED_S3)
    constants_gr = load_json(CONSTANTS_GR)

    preferred = preferred_line_solution(rank2)
    integral_candidate = integral.get("integral_candidate", {})
    integral_ch2 = integral_candidate.get("standard_chern_character_label", {}).get("row")

    prerequisites = {
        "rank2_extension_route": status_of(rank2)
        == "VISIBLE_RANK2_EXTENSION_VALPHA_ROUTE_FORMULATED_EXT_STABILITY_OPEN",
        "l2_h1_gate": status_of(l2_h1)
        == "VISIBLE_RANK2_L2_EXT_H1_VALIDATOR_FORMULATED_DATA_OPEN",
        "integral_alpha1_row": status_of(integral)
        == "VISIBLE_INTEGRAL_CHERN_CLASS_CANDIDATE_CLOSED_HYM_SOURCE_OPEN",
        "split_line_no_go": status_of(split)
        == "VISIBLE_SPLIT_LINE_HYM_SOURCE_NO_GO_NONABELIAN_OR_ROUTE_C_REQUIRED",
        "stable_source_sign_gate": status_of(sign)
        == "VISIBLE_STABLE_SOURCE_SIGN_CONVENTION_GATE_CLOSED_SOURCE_OPEN",
        "terminal_g3_dual_extension_sign": status_of(terminal_sign)
        == "TERMINAL_MAP_DUAL_EXTENSION_SIGN_PROVED_SELECTOR_OPEN",
        "twisted_s3_class_restriction": status_of(twisted)
        == "VISIBLE_TWISTED_S3_CLASS_RESTRICTION_CLOSED_OPERATOR_SOURCE_OPEN",
        "cross_repo_method_ledger": status_of(constants_gr)
        == "CONSTANTS_GR_CROSS_REPO_CLUES_FORMULATED_IMPORTS_METHOD_NOT_DATA",
    }

    source_packet_interface = build_packet_interface(constants_gr)

    rank2_candidate = {
        "id": "rank2_non_split_extension_preferred_L_1_-2_0",
        "rank": 1,
        "candidate_kind": "non_split_rank_two_extension",
        "live_role": "primary_next_branch",
        "source_shape": "0 -> L -> V_alpha -> L^-1 -> 0",
        "topological_target": {
            "l_vector_abc": [1, -2, 0],
            "c1_L_squared_vector_abc": [2, -4, 0],
            "c1_L_squared_square_alpha_coeffs": [-16, 0, 0],
            "c1_V_alpha": [0, 0, 0],
            "c2_V_alpha": preferred.get("c2_extension_alpha_coeffs"),
            "c3_V_alpha": 0,
            "ch2_math": [-4, 0, 0],
        },
        "already_audited_support": {
            "hits_c2_4_alpha1": preferred.get("c2_extension_alpha_coeffs") == [4, 0, 0],
            "negative_slope_chamber_witness": preferred.get("slope_chamber_witness", {}),
            "split_no_go_avoided_by_non_split_route": True,
            "l2_h1_validator_available": True,
            "stable_source_sign_compatible": True,
            "terminal_g3_dual_sign_and_order_closed": terminal_sign.get(
                "what_this_closes", {}
            ).get("target_L2_matrix_order_binding_conditional_on_terminal_g3")
            is True,
        },
        "source_packet_fields": {
            "line_bundle_cochain_packet": open_field(
                "selected L^2 cochain packet",
                "fill certificates/visible_rank2_l2_cohomology_data.template.json",
            ),
            "nonzero_ext_class": open_field(
                "nonzero Ext class",
                "validator must prove a closed non-exact C1 vector",
            ),
            "non_split_stability": open_field(
                "non-split stability",
                "prove no positive-slope line subsheaf destabilizes the selected extension",
            ),
            "chern_bianchi_data": formulated_field(
                "Chern/Bianchi target",
                "rank-two c2 arithmetic and integral alpha1 row are both audited",
            ),
            "hym_or_route_c_residual": open_field(
                "HYM/Strominger or Route-C residual",
                "construct selected connection or finite residual solve for the same bundle",
            ),
            "same_source_operator_data": open_field(
                "same-source D_E/dotD/Riesz/Green",
                "derive operators from this selected V_alpha inside the total visible source",
            ),
        },
        "promotion_status": "OPEN",
        "why_primary": (
            "It is the smallest nonabelian route that matches the visible c2 target, "
            "does not reuse the rejected split abelian HYM shortcut, and already has "
            "an executable H^1/Ext validator."
        ),
    }

    abelian_candidate = {
        "id": "abelian_two_line_flux_row",
        "rank": 2,
        "candidate_kind": "split_integral_line_flux_row",
        "live_role": "Chern_Bianchi_support_template_only",
        "source_shape": "L_(1,2,0) direct_sum L_(-1,-2,0)",
        "topological_target": {
            "vectors_n123": integral_candidate.get("vectors_n123"),
            "total_c1_vector": integral_candidate.get("total_c1_vector"),
            "standard_chern_character_row": integral_ch2,
            "Tr_F_squared_row": integral_candidate.get("Tr_F_squared_row"),
        },
        "already_audited_support": {
            "integral_alpha1_row_exists": integral.get("calculation_results", {}).get(
                "integral_chern_character_candidate_exists"
            )
            is True,
            "standard_label_4": integral_ch2 == [4, 0, 0],
            "total_pairwise_cancellation_occurs": integral.get("hym_primitivity_gate", {}).get(
                "total_pairwise_cancellation_occurs"
            )
            is True,
        },
        "source_packet_fields": {
            "individual_hym_primitivity": {
                "label": "split HYM/primitivity",
                "status": "FAILED_FOR_SELECTED_SOURCE",
                "reason": integral.get("hym_primitivity_gate", {}).get(
                    "why_pairwise_cancellation_is_insufficient"
                ),
            },
            "same_source_operator_data": open_field(
                "same-source D_E/dotD/Riesz/Green",
                "not available because the split HYM source is rejected",
            ),
        },
        "promotion_status": "REJECTED_AS_FINAL_SOURCE",
        "why_retained": (
            "It fixes the integral row and trace normalization to be matched by a "
            "genuine nonabelian stable source or Route-C solve."
        ),
    }

    route_c_candidate = {
        "id": "direct_route_c_finite_hym_strominger_solve",
        "rank": 3,
        "candidate_kind": "direct_residual_solve_for_same_class",
        "live_role": "parallel_fallback_branch",
        "source_shape": "finite selected HYM/Strominger residual packet with c1=0,c2=+4 alpha_1",
        "topological_target": {
            "required_c1": [0, 0, 0],
            "required_c2": [4, 0, 0],
            "required_alpha2_alpha3_support": [0, 0],
        },
        "already_audited_support": {
            "split_line_hym_no_go_points_here": True,
            "source_packet_discipline_imported": True,
            "same_branch_guardrail_imported": True,
        },
        "source_packet_fields": {
            "connection_or_residual": open_field(
                "selected connection/residual",
                "provide finite residual matrices and certified error bounds",
            ),
            "chern_bianchi_data": open_field(
                "source-derived Chern/Bianchi row",
                "derive the alpha1 row from the same residual packet, not as a target insert",
            ),
            "same_source_operator_data": open_field(
                "same-source D_E/dotD/Riesz/Green",
                "derive the operator block after the residual source is selected",
            ),
        },
        "promotion_status": "OPEN",
        "why_not_primary": (
            "It may be more general than the rank-two extension route, but currently "
            "has less finite data because no selected residual matrices are present."
        ),
    }

    twisted_transfer_candidate = {
        "id": "twisted_s3_or_gerbe_source_transfer",
        "rank": 4,
        "candidate_kind": "twisted_class_source_transfer",
        "live_role": "conditional_support_branch",
        "source_shape": "use the closed S3 class/restriction infrastructure as a twist or obstruction-control layer",
        "topological_target": {
            "required_visible_row": "same c1=0,c2=+4 alpha_1 source row",
            "class_restriction_status": status_of(twisted),
        },
        "already_audited_support": {
            "finite_and_smooth_class_restriction_closed": prerequisites[
                "twisted_s3_class_restriction"
            ],
            "can_constrain_projector_or_Freed_Witten_gates": True,
        },
        "source_packet_fields": {
            "map_to_visible_valpha": open_field(
                "twist-to-V_alpha map",
                "prove the S3/gerbe representative selects the visible bundle or residual source",
            ),
            "operator_retention": open_field(
                "projector/operator retention",
                "show D_E/dotD and sector projectors survive the twist transfer",
            ),
        },
        "promotion_status": "OPEN",
        "why_not_primary": (
            "The S3 class machinery is real support, but it is not yet a visible "
            "V_alpha source or Ext packet."
        ),
    }

    candidates = [
        rank2_candidate,
        abelian_candidate,
        route_c_candidate,
        twisted_transfer_candidate,
    ]

    prerequisites_met = all(prerequisites.values())
    report = {
        "calculation": "VisibleVAlphaChernBianchiSourcePacketCandidates",
        "status": (
            "VISIBLE_VALPHA_CHERN_BIANCHI_SOURCE_PACKET_CANDIDATES_BUILT_SOURCE_OPEN"
            if prerequisites_met
            else "VISIBLE_VALPHA_CHERN_BIANCHI_SOURCE_PACKET_CANDIDATES_NOT_VERIFIED"
        ),
        "generated_by": "scripts/build_visible_valpha_chern_bianchi_source_packet_candidates.py",
        "input_certificates": {
            "visible_rank2_extension_valpha_route": RANK2_EXT.name,
            "visible_rank2_l2_ext_h1_gate": L2_H1.name,
            "visible_integral_chern_source_candidate": INTEGRAL_ROW.name,
            "visible_split_line_hym_no_go": SPLIT_NO_GO.name,
            "visible_stable_source_sign_gate": SIGN_GATE.name,
            "terminal_map_dual_extension_sign": TERMINAL_SIGN.name,
            "visible_twisted_s3_class_restriction_closure": TWISTED_S3.name,
            "constants_gr_cross_repo_clues": CONSTANTS_GR.name,
        },
        "input_statuses": {
            "visible_rank2_extension_valpha_route": status_of(rank2),
            "visible_rank2_l2_ext_h1_gate": status_of(l2_h1),
            "visible_integral_chern_source_candidate": status_of(integral),
            "visible_split_line_hym_no_go": status_of(split),
            "visible_stable_source_sign_gate": status_of(sign),
            "terminal_map_dual_extension_sign": status_of(terminal_sign),
            "visible_twisted_s3_class_restriction_closure": status_of(twisted),
            "constants_gr_cross_repo_clues": status_of(constants_gr),
        },
        "prerequisite_gates": prerequisites,
        "source_packet_interface": source_packet_interface,
        "candidate_ranking": candidates,
        "best_current_route": {
            "candidate_id": rank2_candidate["id"],
            "reason": rank2_candidate["why_primary"],
            "next_executable_artifact": "certificates/visible_rank2_l2_cohomology_data.template.json",
            "next_validator": "scripts/validate_visible_rank2_l2_cohomology.py",
            "closed_before_next_step": [
                "terminal g3 Hom type is the dual K2-L3=(-1,2,0)",
                "physical rank-two extension line is L=L3-K2=(1,-2,0)",
                "ordered L^2 matrix is (2,-4,0) in the Appell-Humbert/Cech basis",
            ],
        },
        "calculation_results": {
            "candidate_count": len(candidates),
            "primary_candidate_is_rank2_non_split_extension": True,
            "terminal_g3_sign_order_closed_before_source_selection": prerequisites[
                "terminal_g3_dual_extension_sign"
            ],
            "abelian_row_retained_only_as_chern_bianchi_support": True,
            "route_c_kept_as_parallel_fallback": True,
            "twisted_s3_kept_as_conditional_support": True,
            "selected_visible_valpha_source_constructed": False,
            "actual_H1_X_L_squared_computed": False,
            "selected_nonzero_ext_class_constructed": False,
            "stability_proved": False,
            "same_source_D_E_dotD_Riesz_Green_constructed": False,
        },
        "what_this_closes": {
            "visible_valpha_candidate_hierarchy": prerequisites_met,
            "direct_abelian_shortcut_demoted_to_support_template": True,
            "exact_source_packet_fields_for_promotion": True,
            "next_executable_rank2_fill_target_identified": True,
            "route_c_and_twisted_fallbacks_preserved_without_overclaim": True,
        },
        "still_open": {
            "fill_visible_rank2_l2_cohomology_template": True,
            "compute_actual_h1_for_L_squared": True,
            "select_nonzero_extension_class": True,
            "prove_non_split_extension_stability": True,
            "derive_source_Chern_Weil_representative": True,
            "prove_HYM_or_Route_C_residual": True,
            "derive_same_total_source_D_E_dotD_Riesz_Green": True,
            "coherent_spectral_projectors": True,
            "primitive_C1_contractions": True,
            "Yukawa_and_CKM_magnitude_closure": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_selected_visible_valpha_source": False,
            "claims_actual_H1_value": False,
            "claims_nonzero_Ext_class": False,
            "claims_stability_proved": False,
            "claims_split_abelian_source_promoted": False,
            "claims_selected_D_E_dotD_constructed": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The live source program is now narrowed to an explicit candidate "
                "hierarchy. The primary branch is the non-split rank-two extension "
                "with L=(1,-2,0). The abelian two-line row remains valuable as an "
                "integral Chern/Bianchi support template, but it is rejected as the "
                "final HYM source. Route-C and twisted/S3 transfer remain fallback "
                "branches, not closed sources."
            ),
            "next_action": (
                "Fill the selected L^2 cochain packet for L=(1,-2,0), validate "
                "h1>0 and a closed non-exact Ext vector, then use that selected "
                "extension to attack stability and HYM/Route-C residuals."
            ),
        },
    }
    return report


def main() -> int:
    report = analyze()
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "VisibleVAlphaChernBianchiSourcePacketCandidates",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": "candidate_data/visible_valpha_chern_bianchi_source_packet_candidates.candidate.json",
        "input_certificates": report["input_certificates"],
        "input_statuses": report["input_statuses"],
        "prerequisite_gates": report["prerequisite_gates"],
        "source_packet_interface": report["source_packet_interface"],
        "candidate_ranking": report["candidate_ranking"],
        "best_current_route": report["best_current_route"],
        "calculation_results": report["calculation_results"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write_json(CERTIFICATE, certificate)
    print(json.dumps(report, indent=2, sort_keys=True))
    return (
        0
        if report["status"]
        == "VISIBLE_VALPHA_CHERN_BIANCHI_SOURCE_PACKET_CANDIDATES_BUILT_SOURCE_OPEN"
        else 1
    )


if __name__ == "__main__":
    raise SystemExit(main())
