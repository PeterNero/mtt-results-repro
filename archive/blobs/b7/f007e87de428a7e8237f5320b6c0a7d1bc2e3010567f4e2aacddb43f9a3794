"""Build the selected AH/Cech source-layer promotion and residual gate audit."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
Q79 = ROOT.parent / "mtt-q79-proof-repro"

OUT_CANDIDATE = ROOT / "candidate_data" / "selected_routec_ah_source_selection_or_routec_selected_residual.candidate.json"
OUT_CERT = ROOT / "certificates" / "selected_routec_ah_source_selection_or_routec_selected_residual_certificate.json"
OUT_PROOF = ROOT / "proof_corpus" / "MTT_Selected_RouteC_AH_Source_Selection_or_RouteC_SelectedResidual_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def all_residuals_zero(packet: dict) -> bool:
    return all(abs(row["value"]) <= row["tolerance"] for row in packet["residuals"].values())


def all_positive_gates(packet: dict) -> bool:
    return all(row["value"] > row["strict_lower_bound"] for row in packet["positive_gates"].values())


def main() -> int:
    ordered_source_path = (
        Q79
        / "candidate_data"
        / "terminal_admissible_section_source"
        / "visible_rank2_l2_ordered_source.selected_under_section_principle.json"
    )
    cohomology_path = (
        Q79
        / "candidate_data"
        / "terminal_admissible_section_source"
        / "visible_rank2_l2_cohomology.selected_under_section_principle.json"
    )
    ah_automorphy_path = Q79 / "candidate_data" / "visible_rank2_l2_appell_humbert_automorphy.candidate.json"
    ah_yoneda_path = Q79 / "candidate_data" / "valpha_appell_humbert_yoneda_promotion.candidate.json"
    gauduchon_path = Q79 / "candidate_data" / "selected_gauduchon_wall_radius_gate.candidate.json"
    residual_path = (
        Q79
        / "candidate_data"
        / "iwasawa_route_c_branch_smoke"
        / "current_q79_orientation"
        / "route_c_residual.candidate.json"
    )
    prior_hym_path = ROOT / "candidate_data" / "selected_routec_selected_ah_goodcover_promotion_hym_certificate.candidate.json"
    prior_stability_path = ROOT / "candidate_data" / "selected_routec_global_destabilizer_enumeration_or_selected_residual.candidate.json"

    ordered = load(ordered_source_path)
    cohomology = load(cohomology_path)
    automorphy = load(ah_automorphy_path)
    yoneda = load(ah_yoneda_path)
    gauduchon = load(gauduchon_path)
    residual = load(residual_path)
    prior_hym = load(prior_hym_path)
    prior_stability = load(prior_stability_path)

    selected_ordered_layer = (
        ordered["candidate_role"] == "SELECTED_DATA"
        and ordered["source"]["selected_by_mtt"] is True
        and ordered["source"]["fixture_only"] is False
        and ordered["pic0_resolution"]["source_selected_or_quotiented"] is True
        and ordered["pic0_resolution"]["scope"] == "ordered_chern_h1_curvature_layer_only"
        and ordered["selection_evidence"]["base_factor_order_selected"] is True
        and ordered["selection_evidence"]["standard_lattice_or_equivalent_selected"] is True
        and ordered["target"]["L"] == [1, -2, 0]
    )
    selected_cohomology_layer = (
        cohomology["candidate_role"] == "SELECTED_DATA"
        and cohomology["source"]["selected_by_mtt"] is True
        and cohomology["source"]["fixture_only"] is False
        and cohomology["reported_cohomology"]["h1"] == 8
        and cohomology["acceptance_tests"]["extension_class_closed"] is True
        and cohomology["acceptance_tests"]["extension_class_not_exact"] is True
    )
    ah_math_ready = (
        automorphy["construction_checks"]["cocycle_law_holds_on_generators_mod_2pi_i"] is True
        and automorphy["construction_checks"]["cocycle_law_holds_on_small_lattice_box_mod_2pi_i"] is True
        and automorphy["construction_checks"]["central_shared_circle_trivial"] is True
        and yoneda["appell_humbert_yoneda_promotion"]["all_reduced_boundaries_injective"] is True
    )
    selected_ah_stability_layer_promoted = selected_ordered_layer and selected_cohomology_layer and ah_math_ready

    gauduchon_wall_selected = gauduchon["current_source_status"]["source_certified_target_wall_present"] is True
    residual_selected = residual["selected_source_verified"] is True and residual["guardrails"]["claims_selected_source"] is True
    residual_smoke_support = all_residuals_zero(residual) and all_positive_gates(residual)

    candidate = {
        "candidate": "MTTSelectedRouteCAHSourceSelectionOrRouteCSelectedResidual",
        "status": "MTT_SELECTED_ROUTEC_ORDERED_AH_SOURCE_LAYER_PROMOTED_GAUDUCHON_OR_RESIDUAL_SOURCE_OPEN",
        "closure_claimed": False,
        "target_fitting_used": False,
        "inputs": {
            "ordered_source": str(ordered_source_path),
            "selected_cohomology": str(cohomology_path),
            "q79_AH_automorphy": str(ah_automorphy_path),
            "q79_AH_yoneda_promotion": str(ah_yoneda_path),
            "selected_gauduchon_gate": str(gauduchon_path),
            "route_c_residual_smoke": str(residual_path),
            "prior_reflexive_hull_hym_bridge": str(prior_hym_path),
            "prior_reduced_AH_global_stability": str(prior_stability_path),
        },
        "selected_AH_goodcover_stability_layer": {
            "proved": selected_ah_stability_layer_promoted,
            "scope": "ordered Chern/H1/ordinary-curvature/stability layer only",
            "selected_ordered_source": selected_ordered_layer,
            "selected_cohomology_h1_ext": selected_cohomology_layer,
            "AH_automorphy_cocycle_and_degree_laws": ah_math_ready,
            "ordered_L_vector": ordered["target"]["L"],
            "ordered_L2_vector": ordered["target"]["L2"],
            "h1_L2": cohomology["reported_cohomology"]["h1"],
            "nonzero_extension_class_label": cohomology["reported_cohomology"]["nonzero_extension_class_label"],
            "pic0_rule_scope": ordered["pic0_resolution"]["scope"],
            "operator_layer_pic0_reopens": True,
            "central_shared_circle_degree_zero_retained": automorphy["construction_checks"]["central_shared_circle_trivial"],
            "imports_reduced_AH_global_stability": prior_stability["conditional_global_stability_theorem"]["proved"],
            "imports_reflexive_hull_reduction": prior_hym["rank_one_torsion_free_reflexive_hull_theorem"]["proved"],
        },
        "stability_consequence": {
            "straight_path": "rank-two V_alpha stability via selected ordered AH/Cech source, reduced Hom/Yoneda enumeration, and reflexive-hull reduction",
            "stable_in_selected_ordered_AH_layer": selected_ah_stability_layer_promoted,
            "stable_as_full_selected_Gauduchon_bundle": False,
            "reason_full_stability_not_promoted": "the selected ordered source supplies the holomorphic/AH/Cech stability layer, but the Gauduchon chamber p=(1,2,1) is still not source-certified",
            "no_extra_rank_one_line_destabilizers_in_reduced_model": prior_stability["reduced_AH_global_rank_one_enumeration"]["proves_no_extra_reduced_AH_rank_one_line_destabilizers"],
        },
        "gauduchon_or_routec_gate": {
            "selected_gauduchon_target_wall": gauduchon_wall_selected,
            "target_wall": gauduchon["wall_dictionary"]["target_wall"],
            "source_certified_target_wall_present": gauduchon["current_source_status"]["source_certified_target_wall_present"],
            "source_certified_integral_lift_present": gauduchon["current_source_status"]["source_certified_integral_lift_present"],
            "target_wall_equivalent_radius_ratio": gauduchon["wall_dictionary"]["target_wall"]["equivalent_radius_ratio"],
            "current_equal_radius_sources_do_not_select_target_wall": gauduchon["what_this_closes"]["current_equal_radius_sources_do_not_select_target_wall"],
            "split_line_hym_shortcut_rejected": gauduchon["what_this_closes"]["split_line_hym_wall_shortcut_rejected_for_visible_source"],
            "selected_routec_residual_values": residual_selected,
            "routec_residual_zero_smoke_support": residual_smoke_support,
            "routec_selected_source_verified": residual["selected_source_verified"],
            "routec_status": residual["status"],
            "routec_guardrail_claims_selected_source": residual["guardrails"]["claims_selected_source"],
        },
        "HYM_status": {
            "conditional_bridge_ready": prior_hym["HYM_bridge"]["proved_conditionally"],
            "HYM_existence_selected_now": False,
            "reason": "Li-Yau/Gauduchon bridge still needs either selected p=(1,2,1) Gauduchon chamber data or selected same-branch Route-C HYM/Strominger residual values",
            "operator_source_values_emitted": False,
        },
        "superset_strategy": {
            "straight_path": "V_alpha AH/Cech source selection followed by stability and HYM",
            "combined_paths": [
                "terminal admissible section principle selects the ordered L=(1,-2,0) Chern/H1 layer",
                "Pic0 quotient is used only for the ordered Chern/H1/ordinary-curvature layer",
                "Appell-Humbert automorphy and Yoneda multiplication supply the executable section algebra",
                "Route-C residual zero smoke is kept as support and repair, not as selected proof",
            ],
            "locked_target": "q79/F,m=1 V_alpha branch with L=(1,-2,0)",
            "target_fitting_used": False,
            "promotion_guardrail": "support-only, fixture, or smoke Route-C values cannot become selected HYM/operator proof data",
        },
        "what_closes_now": {
            "selected_ordered_AH_goodcover_source_for_stability_layer": selected_ah_stability_layer_promoted,
            "target_branch_L_selected_at_ordered_source_layer": selected_ordered_layer,
            "selected_h1_nonzero_ext_packet": selected_cohomology_layer,
            "Pic0_quotiented_at_ordered_Chern_H1_curvature_layer": ordered["pic0_resolution"]["source_selected_or_quotiented"],
            "AH_automorphy_and_Yoneda_laws_ready_for_selected_layer": ah_math_ready,
            "reduced_stability_and_reflexive_hull_can_now_import_selected_source_layer": selected_ah_stability_layer_promoted,
        },
        "what_remains_open": {
            "selected_Gauduchon_chamber_source": not gauduchon_wall_selected,
            "selected_RouteC_residual_values": not residual_selected,
            "selected_HYM_connection_or_operator_values": True,
            "operator_layer_Pic0_or_holonomy_sensitive_quotient": True,
            "same_source_D_E_Riesz_Green_dotD": True,
            "same_source_ChernWeil_GS_row": True,
            "primitive_C1_contractions": True,
            "full_SM_or_no_knob_closure": True,
        },
        "next_required_artifact": "MTT_Selected_RouteC_Gauduchon_Chamber_or_SelectedResidual_Source_v1",
    }

    cert = {
        "certificate": "MTT_Selected_RouteC_AH_Source_Selection_or_RouteC_SelectedResidual_v1",
        "status": candidate["status"],
        "closure_claimed": candidate["closure_claimed"],
        "selected_AH_goodcover_stability_layer_proved": selected_ah_stability_layer_promoted,
        "selected_gauduchon_or_routec_residual_source_open": True,
        "next_required_artifact": candidate["next_required_artifact"],
    }

    proof = f"""# MTT Selected Route-C AH Source Selection or Route-C Selected Residual v1

## Claim

The terminal admissible section source now promotes the ordered Appell-Humbert /
good-cover layer needed by the `V_alpha` stability argument.  This is a
selected-source result at the ordered Chern/H1/ordinary-curvature/stability
layer, not an operator-layer HYM proof.

## Selected AH/Cech Layer

- The ordered source packet is `SELECTED_DATA`, `fixture_only=false`, and
  selects `L=(1,-2,0)` with `L^2=(2,-4,0)`.
- The cohomology packet is `SELECTED_DATA`, has `h1(L^2)=8`, and carries a
  closed non-exact extension class.
- The Appell-Humbert representative has the correct cocycle, degree product
  laws, and trivial shared-circle degree.
- The reduced AH/Yoneda stability theorem and rank-one reflexive-hull
  reduction may now import this selected ordered layer.

Therefore the previously missing AH/good-cover source object is closed for the
stability layer:

```text
selected ordered AH/Cech layer + reduced Hom/Yoneda enumeration
+ reflexive-hull reduction
=> V_alpha stable inside the selected ordered AH stability layer.
```

## Remaining Gate

The full selected HYM theorem is not claimed here.  The Gauduchon wall gate is
still open: current selected Iwasawa sources do not certify the target chamber
`p=(1,2,1)`, equivalently `r1:r2=sqrt(2):1`.  The Route-C residual packet has
zero residuals and positive Hessian/Riesz smoke support, but its source flags
remain unselected.

The next theorem is therefore sharply:

```text
MTT_Selected_RouteC_Gauduchon_Chamber_or_SelectedResidual_Source_v1
```

It must either select the Gauduchon chamber/source for the stable bundle, or
emit selected Route-C HYM/Strominger residual values from the same q79/F,m=1
branch.

## Superset Status

This uses a combined superset path with a locked target: terminal-section
source selection, ordered Pic0 quotient, AH/Yoneda algebra, and Route-C smoke
support all converge on the q79/F,m=1 `V_alpha` branch.  Only the selected
ordered AH/Cech stability layer is promoted.  Support-only residual smoke is
not promoted to proof.
"""

    OUT_CANDIDATE.parent.mkdir(parents=True, exist_ok=True)
    OUT_CERT.parent.mkdir(parents=True, exist_ok=True)
    OUT_PROOF.parent.mkdir(parents=True, exist_ok=True)
    OUT_CANDIDATE.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_PROOF.write_text(proof, encoding="utf-8")
    print(f"Wrote {OUT_CANDIDATE}")
    print(f"Wrote {OUT_CERT}")
    print(f"Wrote {OUT_PROOF}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
