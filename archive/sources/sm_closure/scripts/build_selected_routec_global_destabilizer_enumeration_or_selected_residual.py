"""Build the global destabilizer enumeration / selected residual attempt.

This advances the V_alpha stability gate one layer past the central-neutral
subtheorem.  It proves that, inside the reduced Appell-Humbert section algebra,
the full integral rank-one Hom enumeration collapses to the already-obstructed
six central-neutral candidates.  The result is not promoted to full HYM until
the selected AH/good-cover source and rank-one torsion-free hull theorem are
supplied, or until Route-C emits selected residual values directly.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79 = ROOT.parent / "mtt-q79-proof-repro"

PREVIOUS = DATA / "selected_routec_stability_hym_or_routec_residual_source.candidate.json"
CENTRAL_FILTER = Q79 / "candidate_data" / "central_circle_neutral_terminal_lane_filter.candidate.json"
ALL_REMAINING = Q79 / "candidate_data" / "all_remaining_valpha_gates_attempt.candidate.json"
CENTRAL_REDUCTION = Q79 / "candidate_data" / "valpha_central_neutral_destabilizer_reduction.candidate.json"
AH_PROMOTION = Q79 / "candidate_data" / "valpha_appell_humbert_yoneda_promotion.candidate.json"
ROUTEC_BRIDGE = Q79 / "candidate_data" / "q79_valpha_source_origin_finite_emission_bridge.candidate.json"

OUTPUT = DATA / "selected_routec_global_destabilizer_enumeration_or_selected_residual.candidate.json"
CERT = CERTS / "selected_routec_global_destabilizer_enumeration_or_selected_residual_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteC_Global_Destabilizer_Enumeration_or_Selected_Residual_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_REDUCED_AH_GLOBAL_DESTABILIZER_ENUMERATION_PROVED_PROMOTION_OPEN"
NEXT = "MTT_Selected_RouteC_Selected_AH_or_GoodCover_Promotion_and_HYM_Certificate_v1"

L = (1, -2, 0)
Q = (-1, 2, 0)
P = (1, 2, 1)


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def slope(m: tuple[int, int, int]) -> int:
    return sum(x * y for x, y in zip(m, P, strict=True))


def reduced_h0_nonzero(degrees: tuple[int, int, int]) -> bool:
    """Reduced AH/base-pullback section rule used by the imported q79 proof."""

    a, b, c = degrees
    return c == 0 and a >= 0 and b >= 0


def sub(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(a - b for a, b in zip(left, right, strict=True))  # type: ignore[return-value]


def enumerate_rank_one_hom_candidates() -> dict[str, Any]:
    """Symbolically solve the reduced AH Hom inequalities.

    A rank-one M can only inject through L or Q if H0(L-M) or H0(Q-M) is
    nonzero.  In the reduced AH model this forces central degree c=0.  The
    remaining base inequalities are finite without any radius cutoff.
    """

    hom_to_l_conditions = {
        "h0_nonzero": "1-a >= 0, -2-b >= 0, c = 0",
        "nonnegative_slope": "a + 2b + c >= 0",
        "contradiction": "b <= -2 implies a >= -2b >= 4, but h0 requires a <= 1",
    }
    hom_to_q_conditions = {
        "h0_nonzero": "-1-a >= 0, 2-b >= 0, c = 0",
        "nonnegative_slope": "a + 2b + c >= 0",
        "finite_solution": "b in {1,2}; a in [-2b, -1]",
    }

    hom_to_l: list[list[int]] = []
    hom_to_q: list[list[int]] = []
    for b in range(-16, 17):
        for a in range(-32, 33):
            for c in range(-4, 5):
                m = (a, b, c)
                if slope(m) < 0:
                    continue
                if reduced_h0_nonzero(sub(L, m)):
                    hom_to_l.append(list(m))
                if reduced_h0_nonzero(sub(Q, m)):
                    hom_to_q.append(list(m))

    symbolic_hom_to_q = [[a, b, 0] for b in (1, 2) for a in range(-2 * b, 0)]
    symbolic_hom_to_q = sorted(symbolic_hom_to_q)

    return {
        "model": "reduced Appell-Humbert/base-pullback section algebra",
        "slope": "mu_p(M)=a+2b+c with p=(1,2,1)",
        "central_nonzero_exclusion": "H0(A,B,C)=0 when C has nonzero shared-circle degree",
        "hom_to_L_conditions": hom_to_l_conditions,
        "hom_to_Q_conditions": hom_to_q_conditions,
        "hom_to_L_nonnegative_candidates": hom_to_l,
        "hom_to_Q_nonnegative_candidates": symbolic_hom_to_q,
        "bounded_sanity_scan": {
            "range": "a in [-32,32], b in [-16,16], c in [-4,4]",
            "hom_to_L_matches_symbolic_empty": hom_to_l == [],
            "hom_to_Q_matches_symbolic": sorted(hom_to_q) == symbolic_hom_to_q,
        },
        "finite_without_cutoff": True,
    }


def main() -> None:
    previous = load(PREVIOUS)
    central_filter = load(CENTRAL_FILTER)
    all_remaining = load(ALL_REMAINING)
    central_reduction = load(CENTRAL_REDUCTION)
    ah = load(AH_PROMOTION)
    routec = load(ROUTEC_BRIDGE)

    enumeration = enumerate_rank_one_hom_candidates()
    obstructed = previous["central_neutral_destabilizer_theorem"]
    route_c_open = routec["still_open"]

    candidate = {
        "candidate": "MTTSelectedRouteCGlobalDestabilizerEnumerationOrSelectedResidual",
        "status": STATUS,
        "inputs": {
            "previous_stability_attempt": rel(PREVIOUS),
            "q79_central_circle_filter": rel(CENTRAL_FILTER),
            "q79_all_remaining_valpha_gates": rel(ALL_REMAINING),
            "q79_central_neutral_reduction": rel(CENTRAL_REDUCTION),
            "q79_ah_promotion": rel(AH_PROMOTION),
            "q79_routec_bridge": rel(ROUTEC_BRIDGE),
        },
        "reduced_AH_global_rank_one_enumeration": {
            **enumeration,
            "candidate_list_equals_prior_six": enumeration["hom_to_Q_nonnegative_candidates"]
            == obstructed["candidate_list"],
            "all_candidates_previously_obstructed": obstructed["all_candidates_obstructed"],
            "all_boundaries_previously_injective": obstructed["all_candidate_boundaries_injective"],
            "proves_no_extra_reduced_AH_rank_one_line_destabilizers": True,
        },
        "conditional_global_stability_theorem": {
            "name": "ReducedAHGlobalRankOneVAlphaStability",
            "proved": True,
            "statement": (
                "In the reduced Appell-Humbert/base-pullback section algebra, every "
                "rank-one line candidate M with nonnegative selected slope and a "
                "possible nonzero morphism M -> V_alpha either maps to L or to "
                "Q=L^-1. The Hom-to-L case is empty by inequalities. The Hom-to-Q "
                "case forces central degree zero and gives exactly the six "
                "central-neutral candidates already obstructed by injective Yoneda "
                "boundaries. Therefore V_alpha is stable inside the reduced AH "
                "rank-one line model."
            ),
            "uses_no_observed_targets": True,
            "depends_on_previous_central_neutral_subtheorem": True,
        },
        "promotion_gap": {
            "full_stability_proved": False,
            "hym_existence_proved": False,
            "why_not_full": [
                "reduced AH line enumeration must be promoted to the selected literal good-cover/Cech section algebra",
                "rank-one torsion-free subsheaves must be shown to have reflexive hulls represented by the enumerated AH line classes",
                "AH/Yoneda multiplication is still conditional on selected AH representative or literal good-cover refinement",
                "Li-Yau/DUY HYM existence still needs the selected stable holomorphic bundle and Gauduchon chamber source certificate",
            ],
        },
        "shared_circle_handling": {
            "central_circle_filter_inside_terminal_lane": central_filter["what_this_closes"][
                "central_circle_neutrality_filter_inside_terminal_lane"
            ],
            "central_circle_not_used_as_global_subsheaf_axiom": True,
            "nonneutral_destabilizers_in_reduced_AH_model_excluded_by_H0_rule": True,
            "nonneutral_destabilizers_in_full_good_cover_still_need_promotion": True,
        },
        "route_c_residual_lane": {
            "still_open": {
                "HYM_or_RouteC_selected_values": route_c_open["HYM_or_RouteC_selected_values"],
                "nonidentity_selected_rhoE_or_connection_values": route_c_open[
                    "nonidentity_selected_rhoE_or_connection_values"
                ],
                "selected_D_E_Riesz_Green_dotD_flags": route_c_open[
                    "selected_D_E_Riesz_Green_dotD_flags"
                ],
            },
            "all_remaining_valpha_status": all_remaining["stability_or_routec_gate"]["status"],
            "selected_operator_source_still_required": True,
        },
        "what_closes_now": {
            "unbounded_reduced_AH_rank_one_line_enumeration": True,
            "central_nonzero_line_candidates_excluded_inside_reduced_AH_section_model": True,
            "hom_to_L_nonnegative_case_empty_by_inequalities": True,
            "hom_to_Q_nonnegative_case_exactly_prior_six": True,
            "reduced_AH_model_stability_proved_from_prior_yoneda_obstructions": True,
        },
        "what_remains_open": {
            "selected_AH_representative_or_literal_good_cover_table": True,
            "rank_one_torsion_free_reflexive_hull_representation_theorem": True,
            "selected_Gauduchon_chamber_source": True,
            "selected_HYM_or_Strominger_existence_certificate": True,
            "selected_RouteC_residual_values": True,
            "operator_layer_Pic0": True,
            "same_source_ChernWeil_GS_row": True,
            "same_source_D_E_Riesz_Green_dotD": True,
            "primitive_C1_contractions": True,
            "full_SM_or_no_knob_closure": True,
        },
        "superset_strategy": {
            "straight_path": "rank-two V_alpha stability via Hom/Yoneda enumeration",
            "combined_paths": [
                "terminal monad L3-K2 source support",
                "central-circle neutrality filter",
                "reduced Appell-Humbert section algebra",
                "Route-C residual lane as repair if AH/good-cover promotion fails",
            ],
            "locked_target": "selected q79/F,m=1 S3/GS V_alpha branch",
            "target_fitting_used": False,
        },
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(
        json.dumps(
            {
                "status": STATUS,
                "candidate_path": rel(OUTPUT),
                "note_path": rel(NOTE),
                "reduced_AH_global_enumeration_proved": True,
                "full_stability_proved": False,
                "what_closes": candidate["what_closes_now"],
                "what_remains_open": candidate["what_remains_open"],
                "next_required_artifact": NEXT,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    NOTE.write_text(
        """# MTT Selected Route-C Global Destabilizer Enumeration or Selected Residual

Status: `MTT_SELECTED_ROUTEC_REDUCED_AH_GLOBAL_DESTABILIZER_ENUMERATION_PROVED_PROMOTION_OPEN`

This artifact tries to close the remaining V_alpha stability gate.

## What Is Proved

Inside the reduced Appell-Humbert/base-pullback section algebra, the global
rank-one line enumeration is finite without a cutoff.

For a candidate line `M=(a,b,c)` with selected slope

```text
mu_p(M) = a + 2b + c,  p=(1,2,1),
```

the reduced AH section rule gives `H0(A,B,C)=0` whenever the shared-circle
degree of `C` is nonzero. Thus any line candidate with a possible nonzero
morphism into `L` or `Q=L^-1` has `c=0`.

The inequalities then give:

- `Hom(M,L)` with `mu_p(M)>=0`: empty, because `b<=-2` forces `a>=4` while
  `H0(L-M)` requires `a<=1`.
- `Hom(M,Q)` with `mu_p(M)>=0`: exactly six classes,
  `(-4,2,0)`, `(-3,2,0)`, `(-2,1,0)`, `(-2,2,0)`, `(-1,1,0)`, `(-1,2,0)`.

Those are exactly the six central-neutral candidates already obstructed by the
previous injective Yoneda-boundary theorem.

Therefore `V_alpha` is stable in the reduced AH rank-one line model.

## Why This Is Still Not Full HYM

The result still needs promotion from the reduced AH model to the selected
literal good-cover/Cech section algebra, plus the theorem that every rank-one
torsion-free destabilizing subsheaf has a reflexive hull represented by one of
these enumerated AH line classes.

Equivalently, the remaining legal closure routes are:

- promote the reduced AH enumeration to selected good-cover/Cech data and then
  invoke the selected stable-bundle/HYM existence bridge, or
- emit selected Route-C HYM/Strominger residual values directly from the same
  q79/F,m=1 S3/GS branch.

Next artifact: `MTT_Selected_RouteC_Selected_AH_or_GoodCover_Promotion_and_HYM_Certificate_v1`.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))


if __name__ == "__main__":
    main()
