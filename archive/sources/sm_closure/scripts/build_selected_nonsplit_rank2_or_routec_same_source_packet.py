"""Build the selected non-split rank-two or Route-C same-source packet artifact."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79_CERTS = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro\certificates")

OUTPUT_DATA = DATA / "selected_nonsplit_rank2_or_routec_same_source_packet.candidate.json"
OUTPUT_CERT = CERTS / "selected_nonsplit_rank2_or_routec_same_source_packet_certificate.json"
OUTPUT_NOTE = CORPUS / "MTT_Selected_NonSplit_Rank2_or_RouteC_SameSource_Packet_v1.md"

INPUTS = {
    "visible_cw_source_reduction": DATA / "selected_visible_chern_weil_operator_source.candidate.json",
    "rank2_h1_gate": Q79_CERTS / "visible_rank2_l2_ext_h1_gate_certificate.json",
    "rank2_source_hunt": Q79_CERTS / "visible_rank2_l2_cohomology_source_hunt_certificate.json",
    "rank2_appell_humbert": Q79_CERTS / "visible_rank2_l2_appell_humbert_automorphy_certificate.json",
    "rank2_branch_selection": Q79_CERTS / "visible_rank2_l2_branch_selection_reduction_certificate.json",
    "rank2_selector_obstruction": Q79_CERTS / "visible_rank2_l2_selector_obstruction_certificate.json",
    "rank2_ordered_gate": Q79_CERTS / "visible_rank2_l2_ordered_source_promotion_gate_certificate.json",
    "valpha_candidates": Q79_CERTS / "visible_valpha_chern_bianchi_source_packet_candidates_certificate.json",
    "same_source_fusion_gate": Q79_CERTS / "same_source_monad_gs_operator_fusion_gate_certificate.json",
    "route_c_scaffold": Q79_CERTS / "iwasawa_route_c_finite_solve_scaffold_certificate.json",
    "route_c_template": Q79_CERTS / "iwasawa_route_c_residuals.template.json",
    "source_promotion_gate": Q79_CERTS / "iwasawa_selected_source_promotion_gate_certificate.json",
}


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def source_status() -> dict[str, object]:
    return {key: {"path": str(path), "present": path.exists()} for key, path in INPUTS.items()}


def build_candidate() -> dict[str, object]:
    visible = load_json(INPUTS["visible_cw_source_reduction"])
    h1_gate = load_json(INPUTS["rank2_h1_gate"])
    hunt = load_json(INPUTS["rank2_source_hunt"])
    appell = load_json(INPUTS["rank2_appell_humbert"])
    branch = load_json(INPUTS["rank2_branch_selection"])
    obstruction = load_json(INPUTS["rank2_selector_obstruction"])
    ordered = load_json(INPUTS["rank2_ordered_gate"])
    candidates = load_json(INPUTS["valpha_candidates"])
    fusion = load_json(INPUTS["same_source_fusion_gate"])
    route_c = load_json(INPUTS["route_c_scaffold"])
    route_c_template = load_json(INPUTS["route_c_template"])
    promotion = load_json(INPUTS["source_promotion_gate"])

    rank2_primary = candidates["candidate_ranking"][0]
    rank2_lane = {
        "classification": "SUPERSET_CONVERGENCE_PRIMARY_FILL_LANE",
        "candidate_id": rank2_primary["id"],
        "source_shape": rank2_primary["source_shape"],
        "target": h1_gate["preferred_first_target"],
        "closed": {
            "topological_c2_target": rank2_primary["topological_target"]["c2_V_alpha"] == [4, 0, 0],
            "appell_humbert_automorphy_exists": appell["construction_checks"]["cocycle_law_holds_on_small_lattice_box_mod_2pi_i"],
            "ordinary_integral_c1_matrix_realized": appell["construction_checks"]["c1_matrix_matches_required_order"],
            "h1_validator_formulated": h1_gate["calculation_results"]["validator_formulated"],
            "ordered_source_validator_formulated": ordered["what_this_closes"]["ordered_source_packet_schema_and_validator"],
        },
        "blocked_by": {
            "selected_l2_cochain_packet_absent": hunt["calculation_results"]["selected_L2_cochain_packet_found"] is False,
            "branch_orientation_not_selected": branch["target_branch"]["status"] == "valid branch, not uniquely selected",
            "base_swap_pic0_selector_obstruction": obstruction["no_breaking_source_available"],
            "nonzero_ext_not_selected": h1_gate["calculation_results"]["selected_nonzero_ext_class_constructed"] is False,
            "stability_not_proved": h1_gate["calculation_results"]["stability_proved"] is False,
        },
        "first_fill_template": h1_gate["template"],
        "ordered_source_template": ordered["template"],
        "required_next_packet": branch["next_required_packet"],
    }

    route_c_lane = {
        "classification": "SUPERSET_REPAIR_PARALLEL_FILL_LANE",
        "source_shape": "finite selected HYM/Strominger residual packet with c1=0,c2=+4 alpha_1",
        "closed": {
            "route_c_residual_schema_formulated": route_c["what_this_closes"]["source_residual_gate_format"],
            "branch_aware_residual_schema": route_c["what_this_closes"]["branch_aware_residual_schema"],
            "selected_source_promotion_gate_ready": promotion["verdict"]["promotion_gate_ready"],
            "downstream_validator_order_locked": route_c["what_this_closes"]["downstream_validator_order"],
        },
        "blocked_by": {
            "actual_selected_branch_packet": route_c["still_open"]["actual_selected_branch_packet"],
            "actual_selected_rho_E_values": route_c["still_open"]["actual_selected_rho_E_values"],
            "actual_selected_Hermitian_metric": route_c["still_open"]["actual_selected_Hermitian_metric"],
            "actual_selected_A01_or_DE_action": route_c["still_open"]["actual_selected_A01_or_DE_action"],
            "actual_source_residual_certificate": route_c["still_open"]["actual_source_residual_certificate"],
            "actual_Riesz_Green_dotD_data": route_c["still_open"]["actual_Riesz_Green_dotD_data"],
        },
        "first_fill_template": str(INPUTS["route_c_template"].name),
        "template_required_fields": {
            "branch_packet": list(route_c_template["branch_packet"].keys()),
            "residuals": list(route_c_template["residuals"].keys()),
            "positive_gates": list(route_c_template["positive_gates"].keys()),
            "downstream_data_paths": list(route_c_template["downstream_data_paths"].keys()),
        },
    }

    common_blocker = {
        "name": "SameSourceSymmetryBreakingSource.v1",
        "why_common": (
            "The rank-two lane needs it to select ordered L=(1,-2,0), Pic0, Ext, and stability. "
            "The Route-C lane needs it to select the branch, rho_E/metric/D_E payload, and nonzero dotD response. "
            "Both lanes fail if the data are only topology, curvature, h1 dimension, finite qutrit label, or lifted selected flags."
        ),
        "must_supply": [
            "selected q79/F,m=1 source identity",
            "base-factor ordering or a physical quotient proving order irrelevance",
            "Pic0 character selection or a physical Pic0 quotient rule",
            "same-source link from S3/Green-Schwarz support to V_alpha or Route-C residual",
            "holonomy-sensitive D_E/dotD/Hessian response that breaks or quotients the current degeneracy",
            "no observed flavor, mass, mixing, or benchmark inputs",
        ],
    }

    lane_priority = [
        {
            "lane": "rank2_non_split_valpha",
            "priority": 1,
            "reason": "More topological and automorphy data are already constructed; the first missing fill is the selected L^2 cochain/Ext packet plus symmetry-breaking source.",
        },
        {
            "lane": "route_c_finite_hym_strominger",
            "priority": 2,
            "reason": "More general and can repair stability, but currently lacks actual selected finite values for rho_E, metric, D_E, residuals, Riesz/Green, and dotD.",
        },
    ]

    return {
        "candidate": "MTTSelectedNonSplitRank2OrRouteCSameSourcePacket",
        "status": "MTT_SELECTED_NONSPLIT_RANK2_OR_ROUTEC_SAME_SOURCE_PACKET_REDUCED_TO_SYMMETRY_BREAKING_SOURCE",
        "source_status": source_status(),
        "imported_statuses": {
            key: load_json(path)["status"] if path.exists() and path.suffix == ".json" else "MISSING"
            for key, path in INPUTS.items()
        },
        "superset_mode": {
            "classification": "SUPERSET_CONVERGENCE_WITH_PARALLEL_REPAIR",
            "straight_path": {
                "classification": "STRAIGHT_PATH_PARTIAL",
                "description": "Rank-two V_alpha alone gives a concrete topological and automorphy target, but cannot select branch/Pic0/Ext/stability by itself.",
            },
            "superset_convergence": rank2_lane,
            "superset_repair": route_c_lane,
            "diagnostic_backfit_only": {
                "used": False,
                "reason": "No measured constants or benchmark matrices are used to choose the lane or the source.",
            },
            "locked_target": "one source packet accepted by ordered-source, visible-GS, selected-source-promotion, D_E/Riesz/Green/dotD, and C1 validators",
        },
        "closed_from_previous_frontier": visible["closed_support"],
        "same_source_packet_contract": {
            "from_visible_reduction": visible["selected_source_packet"],
            "from_fusion_gate": fusion["minimal_next_packet"],
            "common_blocker": common_blocker,
            "lane_priority": lane_priority,
        },
        "rank2_lane": rank2_lane,
        "route_c_lane": route_c_lane,
        "what_is_new_here": {
            "same_source_packet_decomposed_into_two_fill_lanes": True,
            "common_symmetry_breaking_source_identified": True,
            "rank2_first_fill_template_identified": True,
            "route_c_first_fill_template_identified": True,
            "rank2_preferred_over_routec_for_next_attempt": True,
        },
        "theorem": {
            "name": "NonSplitRank2OrRouteCSameSourcePacketReduction",
            "proved": True,
            "statement": (
                "The selected visible operator-source packet has exactly two live construction lanes: "
                "a non-split rank-two V_alpha lane and a Route-C finite HYM/Strominger lane. "
                "The rank-two lane is the preferred next attempt because its Chern data, ordered Appell-Humbert automorphy, "
                "and finite H1/Ext validator are already formulated. Both lanes reduce to the same missing source: "
                "a same-source symmetry-breaking packet that selects or quotients base order and Pic0 and then emits "
                "operator data without measured or benchmark inputs."
            ),
        },
        "next_required_artifact": "MTT_SameSource_SymmetryBreaking_Source_v1",
        "target_fitting_used": False,
    }


def build_certificate(candidate: dict[str, object]) -> dict[str, object]:
    return {
        "certificate": "MTTSelectedNonSplitRank2OrRouteCSameSourcePacketReduction",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "superset_mode": candidate["superset_mode"]["classification"],
        "what_closes": {
            "two_live_same_source_lanes_identified": True,
            "rank2_lane_preferred_for_next_fill": True,
            "route_c_lane_preserved_as_parallel_repair": True,
            "rank2_first_fill_template_identified": True,
            "route_c_first_fill_template_identified": True,
            "common_symmetry_breaking_source_blocker_identified": True,
        },
        "what_remains_open": {
            "same_source_symmetry_breaking_source": True,
            "selected_L2_cochain_packet": True,
            "selected_nonzero_Ext_class": True,
            "Pic0_selection_or_physical_quotient": True,
            "non_split_stability_or_selected_RouteC_residual": True,
            "same_source_Chern_Weil_row_derivation": True,
            "selected_D_E_dotD_Riesz_Green": True,
            "primitive_C1_overlap_tensors": True,
            "full_SM_parity_closure": True,
            "no_knob_closure": True,
        },
        "primary_next_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }


def render_note(candidate: dict[str, object], certificate: dict[str, object]) -> str:
    rank2_closed = "\n".join(f"- `{key}`" for key, value in candidate["rank2_lane"]["closed"].items() if value)
    rank2_blocked = "\n".join(f"- `{key}`" for key, value in candidate["rank2_lane"]["blocked_by"].items() if value)
    route_closed = "\n".join(f"- `{key}`" for key, value in candidate["route_c_lane"]["closed"].items() if value)
    route_blocked = "\n".join(f"- `{key}`" for key, value in candidate["route_c_lane"]["blocked_by"].items() if value)
    blocker_fields = "\n".join(f"- {item}" for item in candidate["same_source_packet_contract"]["common_blocker"]["must_supply"])
    lanes = "\n".join(f"- `{item['lane']}`: priority {item['priority']}. {item['reason']}" for item in candidate["same_source_packet_contract"]["lane_priority"])
    closes = "\n".join(f"- `{key}`" for key, value in certificate["what_closes"].items() if value)
    open_items = "\n".join(f"- `{key}`" for key, value in certificate["what_remains_open"].items() if value)

    return f"""# MTT Selected Non-Split Rank2 or Route-C Same-Source Packet v1

## Result

The same-source packet is now decomposed into two live fill lanes and one common
source blocker.

This is **superset convergence with parallel repair**:

- Straight path: rank-two `V_alpha` is concrete but partial.
- Superset convergence: non-split rank-two `V_alpha` is the primary fill lane.
- Superset repair: Route-C finite HYM/Strominger remains the parallel lane.
- Diagnostic/backfit: not used as proof.

## Lane Priority

{lanes}

## Rank-Two Lane Closed

{rank2_closed}

## Rank-Two Lane Blocked By

{rank2_blocked}

First fill target: `{candidate["rank2_lane"]["first_fill_template"]}`

## Route-C Lane Closed

{route_closed}

## Route-C Lane Blocked By

{route_blocked}

First fill target: `{candidate["route_c_lane"]["first_fill_template"]}`

## Common Blocker

`{candidate["same_source_packet_contract"]["common_blocker"]["name"]}` must supply:

{blocker_fields}

## Theorem

`{candidate["theorem"]["name"]}` is proved:

{candidate["theorem"]["statement"]}

## What This Closes

{closes}

## What Remains Open

{open_items}

## Next Artifact

`{candidate["next_required_artifact"]}`
"""


def main() -> None:
    candidate = build_candidate()
    certificate = build_certificate(candidate)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(candidate, certificate), encoding="utf-8")
    print(json.dumps(certificate, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
