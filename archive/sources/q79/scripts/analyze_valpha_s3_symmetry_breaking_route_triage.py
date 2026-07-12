"""Rank the remaining V_alpha/S3 symmetry-breaking routes.

After the two-block source-selector reduction, the finite and integral shadow
arithmetic is sharp.  This gate chooses the next computational target: an
orientation-carrying selected D_E/dotD source, because it can in principle
break both the m=1/m=2 conjugate fork and the target-vs-swapped L2 branch.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "candidate_data"
CERTS = ROOT / "certificates"

SELECTOR = CERTS / "valpha_s3_two_block_source_selector_reduction_certificate.json"
ORIENTATION = CERTS / "iwasawa_orientation_de_dotd_bridge_certificate.json"
M1_TARGET = CERTS / "time_oriented_m1_deresponse_target_certificate.json"
RADIUS_NOGO = CERTS / "visible_rank2_l2_selected_radius_import_nogo_certificate.json"
WALL = CERTS / "selected_gauduchon_wall_radius_gate_certificate.json"
DOTD_VALIDATOR = CERTS / "iwasawa_dotd_response_validator_certificate.json"
SAME_SOURCE_ATTEMPT = CERTS / "selected_qa_su3_same_source_valpha_s3_operator_packet_attempt_certificate.json"

OUT_CANDIDATE = CANDIDATES / "valpha_s3_symmetry_breaking_route_triage.candidate.json"
OUT_CERT = CERTS / "valpha_s3_symmetry_breaking_route_triage_certificate.json"
OUT_TEMPLATE = CERTS / "selected_qa_su3_orientation_carrying_de_dotd_source.template.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def build_template(orientation: dict[str, Any], dotd: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema": "SelectedQaSU3OrientationCarryingDEDotDSource.v1",
        "status": "OPEN",
        "purpose": (
            "Promote the coherent q79/F m=1 de_response target to selected "
            "proof data by supplying the genuine source origin and repo-level "
            "D_E/dotD/Riesz/Green packets."
        ),
        "branch_selection": {
            "selected_torsion_label_m": None,
            "allowed_torsion_labels": orientation["selection_contract"][
                "must_select_exactly_one_torsion_label_m"
            ],
            "global_cp_label": None,
            "must_bind_m_to_global_cp_label": orientation["selection_contract"][
                "must_bind_m_to_global_cp_label"
            ],
            "do_not_use_observed_cp_sign": True,
        },
        "source_origin": {
            "selected_by_mtt": None,
            "source_certificate": None,
            "source_kind": None,
            "visible_bundle_or_twisted_gerbe_source": None,
            "freed_witten_and_projector_retention": None,
            "pic0_selected_or_quotiented": None,
        },
        "operator_data": {
            "selected_D_E_action": None,
            "selected_dotD_alpha1": None,
            "selected_reduced_green": None,
            "same_branch_derivative_verified": None,
            "sector_D_E_Riesz_Green_dotD_packets": None,
        },
        "validator_contract": {
            "dotd_validator": "scripts/validate_iwasawa_dotd_response.py",
            "supported_format": dotd["supported_format_v1"],
            "must_feed_existing_D_E_dotD_validators": orientation[
                "selection_contract"
            ]["must_feed_existing_D_E_dotD_validators"],
        },
        "forbidden_shortcuts": [
            "Do not use observed CP sign to choose between conjugate packets.",
            "Do not promote temporary lifted selected-source flags as proof data.",
            "Do not use benchmark flavor matrices or measured masses/mixings.",
            "Do not treat finite two-block compatibility as source selection.",
        ],
    }


def main() -> int:
    selector = load(SELECTOR)
    orientation = load(ORIENTATION)
    m1 = load(M1_TARGET)
    radius = load(RADIUS_NOGO)
    wall = load(WALL)
    dotd = load(DOTD_VALIDATOR)
    same_source = load(SAME_SOURCE_ATTEMPT)
    template = build_template(orientation, dotd)

    report = {
        "calculation": "VAlphaS3SymmetryBreakingRouteTriage",
        "status": "VALPHA_S3_SYMMETRY_BREAKING_TRIAGE_DE_DOTD_PRIMARY_SOURCE_OPEN",
        "inputs": {
            "two_block_source_selector": str(SELECTOR.relative_to(ROOT)),
            "orientation_de_dotd_bridge": str(ORIENTATION.relative_to(ROOT)),
            "m1_deresponse_target": str(M1_TARGET.relative_to(ROOT)),
            "selected_radius_import_nogo": str(RADIUS_NOGO.relative_to(ROOT)),
            "gauduchon_wall_gate": str(WALL.relative_to(ROOT)),
            "dotd_validator": str(DOTD_VALIDATOR.relative_to(ROOT)),
            "same_source_attempt": str(SAME_SOURCE_ATTEMPT.relative_to(ROOT)),
        },
        "closed_now": {
            "two_block_selector_reduction_closed": selector["what_this_closes"][
                "full_valpha_mod3_requirement_reduced_to_source_selector"
            ],
            "equal_radius_import_rejected_as_target_wall": radius["what_this_closes"][
                "constants_import_does_not_match_target_wall"
            ],
            "orientation_dependencies_compared": orientation["what_this_closes"][
                "orientation_dependencies_compared"
            ],
            "m_label_to_q_label_conditional_map_formulated": orientation[
                "what_this_closes"
            ]["m_label_to_q_label_conditional_map_formulated"],
            "finite_dotD_response_validator_ready": dotd["what_this_closes"][
                "finite_dotD_response_validator"
            ],
            "m1_deresponse_stack_coherent_conditionally": m1["what_this_closes"][
                "finite_validator_stack_has_no_additional_algebraic_blocker"
            ],
            "same_source_packet_open_items_machine_reported": same_source[
                "what_this_closes"
            ]["open_fields_are_machine_reported"],
        },
        "wall_route": {
            "target_radius_condition": wall["wall_dictionary"]["target_wall"][
                "equivalent_radius_ratio"
            ],
            "target_p_ratio": wall["wall_dictionary"]["target_wall"]["p1:p2"],
            "equal_radius_import_condition": radius["visible_slope_dictionary"][
                "constants_import_condition"
            ],
            "equal_radius_matches_target": radius["imported_selected_radius_geometry"][
                "matches_target_wall"
            ],
            "status": "LIVE_BUT_CURRENT_EQUAL_RADIUS_IMPORT_BLOCKED",
        },
        "de_dotd_route": {
            "status": "PRIMARY_LIVE_ROUTE_SOURCE_OPEN",
            "branch_packets": orientation["branch_packets"],
            "selection_contract": orientation["selection_contract"],
            "m1_target_status": m1["status"],
            "dotd_validator_status": dotd["status"],
            "first_missing_data": orientation["verdict"]["first_missing_data"],
            "template": str(OUT_TEMPLATE.relative_to(ROOT)),
        },
        "route_ranking": [
            {
                "rank": 1,
                "route": "selected_orientation_carrying_D_E_dotD",
                "status": "PRIMARY_LIVE_ROUTE_SOURCE_OPEN",
                "reason": (
                    "It can break the m=1/m=2 conjugate fork and the visible "
                    "target-vs-swapped branch while feeding the existing finite "
                    "D_E/dotD validators."
                ),
            },
            {
                "rank": 2,
                "route": "non_equal_radius_gauduchon_wall",
                "status": "LIVE_BUT_CURRENT_CORPUS_BLOCKED",
                "reason": "Target wall needs r1:r2=sqrt(2):1; current selected radius import is equal-horizontal.",
            },
            {
                "rank": 3,
                "route": "ordered_integral_cech_automorphy_source",
                "status": "LIVE_AS_SOURCE_CERTIFICATE_GAP",
                "reason": "Integral model and h1=8 exist, but source selection/Pic0/base ordering remain open.",
            },
            {
                "rank": 4,
                "route": "holonomy_sensitive_pic0_rule_only",
                "status": "NECESSARY_BUT_NOT_SUFFICIENT_ALONE",
                "reason": "Pic0 must be selected or quotiented, but that alone does not choose the branch or build D_E/dotD.",
            },
        ],
        "not_closed": {
            "actual_selected_D_E_action": dotd["still_open"][
                "actual_selected_D_E_action"
            ],
            "actual_selected_dotD_alpha1_operator": dotd["still_open"][
                "actual_selected_dotD_alpha1_operator"
            ],
            "selected_orientation_carrying_source": orientation["still_open"][
                "selected_orientation_carrying_D_E"
            ],
            "unique_m1_vs_m2_selection": orientation["still_open"][
                "unique_m1_vs_m2_selection"
            ],
            "selected_or_quotiented_Pic0_character": selector["still_open"][
                "selected_or_quotiented_Pic0_character"
            ],
            "full_SM_closure": selector["still_open"]["full_SM_closure"],
        },
        "guardrails": {
            "claims_selected_D_E_or_dotD_constructed": False,
            "claims_unique_m_label_now": False,
            "claims_equal_radius_selects_target": False,
            "claims_pic0_resolved": False,
            "claims_full_SM_closure": False,
            "uses_observed_cp_sign_or_masses": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The next best route is selected orientation-carrying D_E/dotD. "
                "The finite two-block and integral-shadow work identify the target; "
                "the m=1 de_response stack is conditionally coherent; and the "
                "equal-radius wall import is not the target wall. What remains is "
                "the genuine selected source origin."
            ),
            "next_action": (
                "Fill SelectedQaSU3OrientationCarryingDEDotDSource.v1 with an "
                "actual selected visible bundle/twisted-gerbe source and repo-level "
                "D_E/dotD/Riesz/Green data."
            ),
        },
    }

    write(OUT_TEMPLATE, template)
    write(OUT_CANDIDATE, report)
    cert = {
        "certificate": "VAlphaS3SymmetryBreakingRouteTriage",
        "status": report["status"],
        "analysis_script": "scripts/analyze_valpha_s3_symmetry_breaking_route_triage.py",
        "candidate_data": str(OUT_CANDIDATE.relative_to(ROOT)),
        "template": str(OUT_TEMPLATE.relative_to(ROOT)),
        "closed_now": report["closed_now"],
        "wall_route": report["wall_route"],
        "de_dotd_route": report["de_dotd_route"],
        "route_ranking": report["route_ranking"],
        "not_closed": report["not_closed"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write(OUT_CERT, cert)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
