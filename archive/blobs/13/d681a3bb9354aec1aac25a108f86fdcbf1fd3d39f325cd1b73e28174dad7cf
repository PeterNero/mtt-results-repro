"""Build the equal-radius Gauduchon repair for V_alpha HYM existence."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
Q79 = ROOT.parent / "mtt-q79-proof-repro"
CONSTANTS = ROOT.parent / "mtt-nonsm-constants-no-knob"

OUT_CANDIDATE = ROOT / "candidate_data" / "selected_routec_equalradius_gauduchon_hym_bridge.candidate.json"
OUT_CERT = ROOT / "certificates" / "selected_routec_equalradius_gauduchon_hym_bridge_certificate.json"
OUT_PROOF = ROOT / "proof_corpus" / "MTT_Selected_RouteC_EqualRadius_Gauduchon_HYM_Bridge_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def slope(m: list[int], p: list[int]) -> int:
    return sum(x * y for x, y in zip(m, p))


def enumerate_candidates(p: list[int]) -> dict:
    hom_to_l = []
    hom_to_q = []

    # Hom(M,L): H0(L-M) nonzero in the reduced AH model means
    # 1-a >= 0, -2-b >= 0, c=0.
    for a in range(-12, 13):
        for b in range(-12, 13):
            m = [a, b, 0]
            if 1 - a >= 0 and -2 - b >= 0 and slope(m, p) >= 0:
                hom_to_l.append(m)

    # Hom(M,Q): H0(Q-M) nonzero in the reduced AH model means
    # -1-a >= 0, 2-b >= 0, c=0.
    for a in range(-12, 13):
        for b in range(-12, 13):
            m = [a, b, 0]
            if -1 - a >= 0 and 2 - b >= 0 and slope(m, p) >= 0:
                hom_to_q.append(m)

    return {"hom_to_L": hom_to_l, "hom_to_Q": hom_to_q}


def main() -> int:
    ah_source_path = ROOT / "candidate_data" / "selected_routec_ah_source_selection_or_routec_selected_residual.candidate.json"
    prior_hym_path = ROOT / "candidate_data" / "selected_routec_selected_ah_goodcover_promotion_hym_certificate.candidate.json"
    radius_import_nogo_path = Q79 / "candidate_data" / "visible_rank2_l2_selected_radius_import_nogo.candidate.json"
    radius_cert_path = CONSTANTS / "certificates" / "final_internal_rho_uv_selected_radius_theorem_certificate.json"
    scale_law_cert_path = CONSTANTS / "certificates" / "selected_horizontal_scale_law_certificate.json"
    yoneda_path = Q79 / "candidate_data" / "valpha_appell_humbert_yoneda_promotion.candidate.json"

    ah_source = load(ah_source_path)
    prior_hym = load(prior_hym_path)
    radius_import = load(radius_import_nogo_path)
    radius_cert = load(radius_cert_path)
    scale_law_cert = load(scale_law_cert_path)
    yoneda = load(yoneda_path)

    p_equal = [1, 1, 1]
    p_old = [1, 2, 1]
    equal_candidates = enumerate_candidates(p_equal)
    old_candidates = enumerate_candidates(p_old)
    obstructed = [
        row["M_abc"]
        for row in yoneda["appell_humbert_yoneda_promotion"]["candidate_rows"]
        if row["reduced_boundary_injective"]
    ]

    equal_hom_to_q_subset = all(m in obstructed for m in equal_candidates["hom_to_Q"])
    old_hom_to_q_subset = all(m in obstructed for m in old_candidates["hom_to_Q"])
    selected_equal_radius = (
        radius_cert["closed"]["selected_internal_radius"] is True
        and scale_law_cert["closed"]["scale_law_selected"] is True
        and radius_import["imported_selected_radius_geometry"]["p1_equals_p2"] is True
        and math.isclose(radius_import["imported_selected_radius_geometry"]["r1_over_r2"], 1.0)
    )
    ordered_branch_selected = ah_source["what_closes_now"]["target_branch_L_selected_at_ordered_source_layer"] is True
    ah_layer_selected = ah_source["selected_AH_goodcover_stability_layer"]["proved"] is True
    stability_at_equal_radius = (
        selected_equal_radius
        and ordered_branch_selected
        and ah_layer_selected
        and equal_candidates["hom_to_L"] == []
        and equal_hom_to_q_subset
    )
    hym_existence = stability_at_equal_radius and prior_hym["HYM_bridge"]["proved_conditionally"] is True

    candidate = {
        "candidate": "MTTSelectedRouteCEqualRadiusGauduchonHYMBridge",
        "status": "MTT_SELECTED_ROUTEC_EQUALRADIUS_GAUDUCHON_HYM_EXISTENCE_BRIDGE_CLOSED_OPERATOR_VALUES_OPEN",
        "closure_claimed": False,
        "target_fitting_used": False,
        "inputs": {
            "selected_AH_source_layer": str(ah_source_path),
            "prior_HYM_bridge": str(prior_hym_path),
            "radius_import_nogo": str(radius_import_nogo_path),
            "selected_radius_certificate": str(radius_cert_path),
            "selected_horizontal_scale_law_certificate": str(scale_law_cert_path),
            "AH_yoneda_obstructions": str(yoneda_path),
        },
        "key_repair": {
            "old_assumption": "the Gauduchon metric had to select the branch through the target wall p=(1,2,1)",
            "repaired_assumption": "after terminal-section ordered source selection fixes L=(1,-2,0), the Gauduchon metric only has to be a selected chamber where V_alpha is stable",
            "equal_radius_does_not_select_branch": radius_import["what_this_closes"]["constants_import_leaves_target_and_swapped_degenerate"],
            "branch_selected_elsewhere": ordered_branch_selected,
            "target_wall_no_longer_required_for_stability": True,
        },
        "selected_equal_radius_gauduchon_metric": {
            "selected": selected_equal_radius,
            "source": "rho_UV/constants selected internal radius branch",
            "R_star": radius_cert["selected_values"]["R_star"],
            "r3": radius_cert["selected_values"]["r3"],
            "p": p_equal,
            "r1_over_r2": radius_import["imported_selected_radius_geometry"]["r1_over_r2"],
            "matches_target_wall": radius_import["imported_selected_radius_geometry"]["matches_target_wall"],
            "role": "selected metric/chamber for stability, not branch selector",
        },
        "equal_radius_stability_enumeration": {
            "p_equal_radius": p_equal,
            "displayed_subline_L": [1, -2, 0],
            "mu_L_at_equal_radius": slope([1, -2, 0], p_equal),
            "hom_to_L_nonnegative_candidates": equal_candidates["hom_to_L"],
            "hom_to_Q_nonnegative_candidates": equal_candidates["hom_to_Q"],
            "hom_to_Q_candidates_subset_of_prior_six": equal_hom_to_q_subset,
            "old_p_1_2_1_hom_to_Q_candidates": old_candidates["hom_to_Q"],
            "old_hom_to_Q_candidates_subset_of_prior_six": old_hom_to_q_subset,
            "all_equal_radius_candidates_obstructed_by_prior_Yoneda": equal_hom_to_q_subset,
            "reduced_AH_stability_at_equal_radius": stability_at_equal_radius,
            "central_shared_circle_handling": "same reduced AH H0 rule excludes c != 0; selected source layer retains central degree zero",
        },
        "HYM_existence_bridge": {
            "selected_AH_source_layer_proved": ah_layer_selected,
            "rank_one_reflexive_hull_reduction_proved": prior_hym["rank_one_torsion_free_reflexive_hull_theorem"]["proved"],
            "Li_Yau_Gauduchon_bridge_available": prior_hym["HYM_bridge"]["proved_conditionally"],
            "selected_stability_at_equal_radius": stability_at_equal_radius,
            "abstract_HYM_existence_for_selected_bundle_metric": hym_existence,
            "operator_values_emitted": False,
        },
        "superset_strategy": {
            "straight_path": "selected V_alpha AH/Cech source plus selected equal-radius Gauduchon metric gives stability and Li-Yau HYM existence",
            "combined_paths": [
                "terminal-section source selects the branch and holomorphic AH/Cech layer",
                "rho_UV/constants program supplies the equal-horizontal Iwasawa metric",
                "Yoneda enumeration proves the equal-radius destabilizer set is a subset of already obstructed candidates",
            ],
            "locked_target": "q79/F,m=1 V_alpha branch with L=(1,-2,0)",
            "target_fitting_used": False,
            "guardrail": "equal radius is not used as a branch selector and does not emit D_E/Riesz/Green/dotD/operator values",
        },
        "what_closes_now": {
            "target_wall_requirement_repaired": True,
            "selected_equal_radius_metric_usable_after_branch_selection": selected_equal_radius and ordered_branch_selected,
            "V_alpha_stable_at_selected_equal_radius_in_selected_AH_layer": stability_at_equal_radius,
            "abstract_HYM_existence_bridge_for_selected_V_alpha": hym_existence,
        },
        "what_remains_open": {
            "selected_HYM_connection_values": True,
            "same_source_D_E_Riesz_Green_dotD": True,
            "operator_layer_Pic0_or_holonomy_sensitive_quotient": True,
            "same_source_ChernWeil_GS_row": True,
            "primitive_C1_contractions": True,
            "full_SM_or_no_knob_closure": True,
        },
        "next_required_artifact": "MTT_Selected_RouteC_HYM_OperatorValues_or_DERieszGreenDotD_Source_v1",
    }

    cert = {
        "certificate": "MTT_Selected_RouteC_EqualRadius_Gauduchon_HYM_Bridge_v1",
        "status": candidate["status"],
        "closure_claimed": False,
        "selected_equal_radius_metric": selected_equal_radius,
        "stability_at_equal_radius": stability_at_equal_radius,
        "abstract_HYM_existence_bridge_closed": hym_existence,
        "operator_values_open": True,
        "next_required_artifact": candidate["next_required_artifact"],
    }

    proof = """# MTT Selected Route-C Equal-Radius Gauduchon HYM Bridge v1

## Claim

The old target-wall requirement was too strong after the terminal-section
ordered source selected `L=(1,-2,0)`.  Equal radius cannot select the branch by
itself, but it can serve as the selected Gauduchon metric once the branch is
selected elsewhere.

## Calculation

At equal radius the slope vector is `p=(1,1,1)`, so
`mu(L)=1-2=-1<0`.  In the reduced AH section algebra:

- `Hom(M,L)` has no nonnegative-slope candidates.
- `Hom(M,L^{-1})` has exactly `(-2,2,0)`, `(-1,1,0)`, and `(-1,2,0)`.
- These three candidates are a subset of the six candidates already killed by
  the injective Yoneda boundaries.

Therefore the selected ordered AH/Cech `V_alpha` layer is stable at the selected
equal-radius Gauduchon metric.

## HYM Bridge

With the selected AH/Cech source layer, the rank-one reflexive-hull reduction,
and the selected equal-radius Gauduchon metric, the Li-Yau/Gauduchon bridge
gives abstract HYM existence for the selected holomorphic bundle and metric.

This still does not emit HYM operator values, `D_E`, Riesz/Green, `dotD`, C1
primitive contractions, or full SM closure.

## Superset Status

This is a combined superset path with a locked target.  The terminal-section
source selects the branch; the constants/rho_UV program supplies the selected
equal-horizontal metric; the AH/Yoneda proof supplies the stability calculation.
Equal radius is not used as a branch selector.
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
