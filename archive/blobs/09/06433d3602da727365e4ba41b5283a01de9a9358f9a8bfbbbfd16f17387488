"""Import and rank the remaining VAlpha/S3 symmetry-breaking routes."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
Q79_REPO = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
Q79_CERTS = Q79_REPO / "certificates"

PREVIOUS = CERTS / "selected_qa_su3_valpha_s3_integral_lift_gap_import_certificate.json"
Q79_WALL = Q79_CERTS / "selected_gauduchon_wall_radius_gate_certificate.json"
Q79_RADIUS_NOGO = Q79_CERTS / "visible_rank2_l2_selected_radius_import_nogo_certificate.json"
Q79_DOTD_BRIDGE = Q79_CERTS / "iwasawa_orientation_de_dotd_bridge_certificate.json"
Q79_DOTD_VALIDATOR = Q79_CERTS / "iwasawa_dotd_response_validator_certificate.json"

OUTPUT_CERT = CERTS / "selected_qa_su3_symmetry_breaking_route_triage_certificate.json"
OUTPUT_TEMPLATE = CERTS / "selected_qa_su3_orientation_carrying_de_dotd_source.template.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def de_dotd_template() -> dict[str, Any]:
    return {
        "schema": "SelectedQaSU3OrientationCarryingDEDotDSource.v1",
        "status": "OPEN_SELECTED_QA_SU3_ORIENTATION_CARRYING_DE_DOTD_SOURCE_REQUIRED",
        "purpose": (
            "Supply the selected D_E/dotD operator package that breaks the "
            "target-vs-swapped and m=1 versus m=2 conjugate ambiguity without "
            "using observed CP sign, masses, or benchmark flavor entries."
        ),
        "must_supply": {
            "selected_torsion_label_m": None,
            "global_cp_label_bound_to_m": None,
            "sector_orientation_packet": None,
            "selected_D_E_action": None,
            "selected_reduced_Green_operator": None,
            "selected_dotD_alpha1_operator": None,
            "proof_dotD_is_same_branch_derivative": None,
            "zero_mode_basis_and_horizontal_projectors": None,
            "dotD_response_validator_pass_report": None,
            "Pic0_selection_or_quotient_rule": None,
        },
        "acceptance_tests": [
            "Exactly one of m=1 or m=2 is selected before comparing to observed CP data.",
            "The selected branch binds m=1 to q=79 or m=2 to q=369 through the same packet.",
            "D_E domains, zero-mode bases, projectors, reduced Green operators, and dotD_alpha1 are all same-branch.",
            "The finite dotD response validator passes on selected, not toy, data.",
            "The packet either selects or quotients flat Pic0 characters.",
            "No observed masses, CKM/PMNS entries, or benchmark flavor matrices are inputs.",
        ],
        "forbidden_shortcuts": [
            "Do not select m=1 because q=79 is the desired branch.",
            "Do not use observed CP sign to choose between conjugate packets.",
            "Do not use toy dotD slots as selected operator data.",
            "Do not import the equal-radius constants solution as the target wall.",
        ],
    }


def main() -> None:
    previous = load(PREVIOUS)
    wall = load(Q79_WALL)
    radius_nogo = load(Q79_RADIUS_NOGO)
    dotd_bridge = load(Q79_DOTD_BRIDGE)
    dotd_validator = load(Q79_DOTD_VALIDATOR)
    template = de_dotd_template()

    output = {
        "certificate": "SelectedQaSU3SymmetryBreakingRouteTriage",
        "status": "QA_SU3_SYMMETRY_BREAKING_TRIAGE_DE_DOTD_PRIMARY_WALL_OPEN",
        "inputs": {
            "previous_integral_lift_gap": str(PREVIOUS.relative_to(ROOT)),
            "q79_gauduchon_wall_gate": str(Q79_WALL),
            "q79_selected_radius_import_nogo": str(Q79_RADIUS_NOGO),
            "q79_orientation_de_dotd_bridge": str(Q79_DOTD_BRIDGE),
            "q79_dotd_response_validator": str(Q79_DOTD_VALIDATOR),
        },
        "closed_now": {
            "target_wall_dictionary_imported": wall["what_this_closes"][
                "abstract_p_wall_translated_to_iwasawa_radii"
            ],
            "target_wall_requires_r1_over_r2_sqrt2": wall["what_this_closes"][
                "target_wall_requires_r1_over_r2_sqrt2"
            ],
            "equal_radius_constants_import_rejected_as_target_wall": radius_nogo[
                "what_this_closes"
            ]["constants_import_does_not_match_target_wall"],
            "orientation_dependencies_compared": dotd_bridge["what_this_closes"][
                "orientation_dependencies_compared"
            ],
            "m_label_to_q_label_conditional_map_formulated": dotd_bridge[
                "what_this_closes"
            ]["m_label_to_q_label_conditional_map_formulated"],
            "finite_dotD_response_validator_ready": dotd_validator["what_this_closes"][
                "finite_dotD_response_validator"
            ],
            "source_vector_and_horizontal_response_gates_ready": dotd_validator[
                "what_this_closes"
            ]["source_vector_gate"]
            and dotd_validator["what_this_closes"]["horizontal_response_gate"],
        },
        "route_ranking": [
            {
                "rank": 1,
                "route": "selected_orientation_carrying_D_E_dotD",
                "status": "PRIMARY_LIVE_ROUTE_SOURCE_OPEN",
                "reason": (
                    "It can in principle break both the m=1/m=2 conjugate fork "
                    "and the visible target-vs-swapped source ambiguity, and the "
                    "finite dotD response validator is already formulated."
                ),
                "next_template": str(OUTPUT_TEMPLATE.relative_to(ROOT)),
            },
            {
                "rank": 2,
                "route": "non_equal_radius_gauduchon_wall",
                "status": "LIVE_BUT_CURRENT_CORPUS_BLOCKED",
                "reason": (
                    "The target wall requires r1:r2=sqrt(2):1, while current "
                    "selected radius imports are equal-horizontal and leave "
                    "target and swapped degenerate."
                ),
            },
            {
                "rank": 3,
                "route": "ordered_integral_cech_automorphy_source",
                "status": "LIVE_AS_SOURCE_CERTIFICATE_GAP",
                "reason": previous["honest_answer"],
            },
            {
                "rank": 4,
                "route": "holonomy_sensitive_pic0_rule_only",
                "status": "NECESSARY_BUT_NOT_SUFFICIENT_ALONE",
                "reason": (
                    "A Pic0 rule is required, but by itself it does not select "
                    "the target branch or provide D_E/dotD operator data."
                ),
            },
        ],
        "wall_route": {
            "target_radius_condition": wall["wall_dictionary"]["target_wall"][
                "equivalent_radius_ratio"
            ],
            "target_p_ratio": wall["wall_dictionary"]["target_wall"]["p1:p2"],
            "target_selects_unique_negative": wall["wall_dictionary"]["target_wall"][
                "selects_target_as_unique_negative"
            ],
            "constants_import_condition": radius_nogo["visible_slope_dictionary"][
                "constants_import_condition"
            ],
            "constants_matches_target_wall": radius_nogo[
                "imported_selected_radius_geometry"
            ]["matches_target_wall"],
            "constants_no_go_theorem": radius_nogo["no_go_theorem"]["theorem"],
        },
        "de_dotd_route": {
            "branch_packets": dotd_bridge["branch_packets"],
            "selection_contract": dotd_bridge["selection_contract"],
            "first_missing_data": dotd_bridge["verdict"]["first_missing_data"],
            "dotd_validator_status": dotd_validator["status"],
            "dotd_supported_format": dotd_validator["supported_format_v1"],
        },
        "not_closed": {
            "unique_m1_vs_m2_selection": dotd_bridge["still_open"][
                "unique_m1_vs_m2_selection"
            ],
            "selected_orientation_carrying_D_E": dotd_bridge["still_open"][
                "selected_orientation_carrying_D_E"
            ],
            "selected_dotD_same_branch_derivative": dotd_bridge["still_open"][
                "selected_dotD_same_branch_derivative"
            ],
            "actual_selected_dotD_response": dotd_validator["verdict"][
                "closes_actual_selected_dotD_response"
            ]
            is False,
            "source_certified_r1_over_r2_sqrt2_wall": wall["still_open"][
                "source_certified_r1_over_r2_sqrt2_wall"
            ],
            "selected_or_quotiented_Pic0_character": previous["not_closed"][
                "selected_or_quotiented_Pic0_character"
            ],
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_unique_m_label_now": False,
            "claims_selected_DE_or_dotD_constructed": False,
            "claims_equal_radius_selects_target": False,
            "claims_target_wall_selected": False,
            "claims_pic0_resolved": False,
            "claims_full_SM_closure": False,
            "uses_observed_cp_sign_or_masses": False,
        },
        "honest_answer": (
            "The cleanest next route is not another finite quotient search. "
            "The equal-radius wall import is ruled out as the target selector, "
            "while the D_E/dotD route has an executable validator and a precise "
            "source packet to fill."
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
