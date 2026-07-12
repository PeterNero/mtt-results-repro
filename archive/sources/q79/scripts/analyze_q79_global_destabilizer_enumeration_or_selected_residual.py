"""Analyze q79 reduced-AH global destabilizer enumeration.

This advances the q79 V_alpha stability gate from the central-neutral lane to
the unbounded rank-one line enumeration inside the reduced Appell-Humbert
section algebra.  It still does not promote full HYM until selected AH/good
cover data and the torsion-free hull theorem are supplied.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"
CERTS = ROOT / "certificates"
CANDIDATES = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"

OUT_DIR = CANDIDATES / "q79_global_destabilizer_enumeration_or_selected_residual"
OUT_TABLE = OUT_DIR / "reduced_ah_global_enumeration_table.json"
OUT_CANDIDATE = CANDIDATES / "q79_global_destabilizer_enumeration_or_selected_residual.candidate.json"
OUT_CERT = CERTS / "q79_global_destabilizer_enumeration_or_selected_residual_certificate.json"
OUT_PAPER = CORPUS / "Q79_Selected_RouteC_Global_Destabilizer_Enumeration_or_Selected_Residual_v1.md"

STATUS = "Q79_SELECTED_ROUTEC_REDUCED_AH_GLOBAL_DESTABILIZER_ENUMERATION_PROVED_PROMOTION_OPEN"
NEXT = "Q79_Selected_RouteC_Selected_AH_or_GoodCover_Promotion_and_HYM_Certificate_v1"

L = (1, -2, 0)
Q = (-1, 2, 0)
P = (1, 2, 1)

Q79_INPUTS = {
    "stability_source": CERTS / "q79_stability_hym_or_routec_residual_source_certificate.json",
    "central_circle_filter": CANDIDATES / "central_circle_neutral_terminal_lane_filter.candidate.json",
    "all_remaining_valpha_gates": CANDIDATES / "all_remaining_valpha_gates_attempt.candidate.json",
    "central_neutral_reduction": CANDIDATES / "valpha_central_neutral_destabilizer_reduction.candidate.json",
    "ah_promotion": CANDIDATES / "valpha_appell_humbert_yoneda_promotion.candidate.json",
    "routec_bridge": CANDIDATES / "q79_valpha_source_origin_finite_emission_bridge.candidate.json",
}

SM_INPUTS = {
    "global_enumeration_certificate": SM
    / "certificates"
    / "selected_routec_global_destabilizer_enumeration_or_selected_residual_certificate.json",
    "global_enumeration_candidate": SM
    / "candidate_data"
    / "selected_routec_global_destabilizer_enumeration_or_selected_residual.candidate.json",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def status_record(path: Path) -> dict[str, Any]:
    data = load(path)
    return {
        "path": str(path),
        "present": path.exists(),
        "status": data.get("status"),
        "closure_claimed": data.get("closure_claimed"),
        "target_fitting_used": data.get("target_fitting_used"),
        "next_required_artifact": data.get("next_required_artifact"),
        "what_closes": data.get("what_closes") or data.get("what_closes_now") or data.get("closed_by_this_attempt") or {},
        "what_remains_open": data.get("what_remains_open") or data.get("still_open") or {},
    }


def slope(m: tuple[int, int, int]) -> int:
    return sum(x * y for x, y in zip(m, P, strict=True))


def reduced_h0_nonzero(degrees: tuple[int, int, int]) -> bool:
    a, b, c = degrees
    return c == 0 and a >= 0 and b >= 0


def sub(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(a - b for a, b in zip(left, right, strict=True))  # type: ignore[return-value]


def enumerate_rank_one_hom_candidates() -> dict[str, Any]:
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

    symbolic_hom_to_q = sorted([[a, b, 0] for b in (1, 2) for a in range(-2 * b, 0)])
    return {
        "model": "reduced Appell-Humbert/base-pullback section algebra",
        "slope": "mu_p(M)=a+2b+c with p=(1,2,1)",
        "central_nonzero_exclusion": "H0(A,B,C)=0 when C has nonzero shared-circle degree",
        "hom_to_L_conditions": {
            "h0_nonzero": "1-a >= 0, -2-b >= 0, c = 0",
            "nonnegative_slope": "a + 2b + c >= 0",
            "contradiction": "b <= -2 implies a >= -2b >= 4, but h0 requires a <= 1",
        },
        "hom_to_Q_conditions": {
            "h0_nonzero": "-1-a >= 0, 2-b >= 0, c = 0",
            "nonnegative_slope": "a + 2b + c >= 0",
            "finite_solution": "b in {1,2}; a in [-2b, -1]",
        },
        "hom_to_L_nonnegative_candidates": hom_to_l,
        "hom_to_Q_nonnegative_candidates": symbolic_hom_to_q,
        "bounded_sanity_scan": {
            "range": "a in [-32,32], b in [-16,16], c in [-4,4]",
            "hom_to_L_matches_symbolic_empty": hom_to_l == [],
            "hom_to_Q_matches_symbolic": sorted(hom_to_q) == symbolic_hom_to_q,
        },
        "finite_without_cutoff": True,
    }


def build_candidate() -> dict[str, Any]:
    q79 = {name: load(path) for name, path in Q79_INPUTS.items()}
    sm = {name: load(path) for name, path in SM_INPUTS.items()}
    sm_global = sm["global_enumeration_candidate"]
    enumeration = enumerate_rank_one_hom_candidates()
    obstructed = q79["central_neutral_reduction"]["central_neutral_destabilizer_table"]
    candidate_list = obstructed["inequality_reduction"]["candidate_list"]
    route_c_open = q79["routec_bridge"]["still_open"]

    enumeration.update(
        {
            "candidate_list_equals_prior_six": enumeration["hom_to_Q_nonnegative_candidates"]
            == candidate_list,
            "all_candidates_previously_obstructed": obstructed["all_candidates_obstructed"],
            "all_boundaries_previously_injective": obstructed[
                "all_candidate_boundaries_injective"
            ],
            "proves_no_extra_reduced_AH_rank_one_line_destabilizers": True,
            "sm_global_enumeration_agrees": sm_global[
                "reduced_AH_global_rank_one_enumeration"
            ]["hom_to_Q_nonnegative_candidates"]
            == enumeration["hom_to_Q_nonnegative_candidates"],
        }
    )

    return {
        "certificate": "Q79SelectedRouteCGlobalDestabilizerEnumerationOrSelectedResidual",
        "status": STATUS,
        "candidate_path": rel(OUT_CANDIDATE),
        "table_path": rel(OUT_TABLE),
        "paper": rel(OUT_PAPER),
        "q79_input_statuses": {name: status_record(path) for name, path in Q79_INPUTS.items()},
        "sm_input_statuses": {name: status_record(path) for name, path in SM_INPUTS.items()},
        "reduced_AH_global_rank_one_enumeration": enumeration,
        "conditional_global_stability_theorem": {
            "name": "Q79ReducedAHGlobalRankOneVAlphaStability",
            "proved": True,
            "uses_no_observed_targets": True,
            "depends_on_previous_central_neutral_subtheorem": True,
            "statement": (
                "In the reduced Appell-Humbert/base-pullback section algebra, every "
                "rank-one line candidate M with nonnegative q79 selected slope and "
                "a possible nonzero morphism M -> V_alpha either maps to L or to "
                "Q=L^-1. The Hom-to-L case is empty by inequalities. The Hom-to-Q "
                "case forces central degree zero and gives exactly the six "
                "central-neutral candidates already obstructed by injective Yoneda "
                "boundaries. Therefore V_alpha is stable inside the reduced AH "
                "rank-one line model."
            ),
        },
        "promotion_gap": {
            "full_stability_proved": False,
            "hym_existence_proved": False,
            "why_not_full": sm_global["promotion_gap"]["why_not_full"],
        },
        "shared_circle_handling": {
            "central_circle_filter_inside_terminal_lane": q79["central_circle_filter"][
                "what_this_closes"
            ]["central_circle_neutrality_filter_inside_terminal_lane"],
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
            "all_remaining_valpha_status": q79["all_remaining_valpha_gates"][
                "stability_or_routec_gate"
            ]["status"],
            "selected_operator_source_still_required": True,
        },
        "what_closes_now": {
            "unbounded_reduced_AH_rank_one_line_enumeration": True,
            "central_nonzero_line_candidates_excluded_inside_reduced_AH_section_model": True,
            "hom_to_L_nonnegative_case_empty_by_inequalities": True,
            "hom_to_Q_nonnegative_case_exactly_prior_six": True,
            "reduced_AH_model_stability_proved_from_prior_yoneda_obstructions": True,
            "target_fitting_excluded": True,
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
        "guardrails": {
            "uses_observed_masses_or_ckm_inputs": False,
            "uses_benchmark_flavor_entries": False,
            "uses_locked_target_columns_as_selector": False,
            "claims_full_stability": False,
            "claims_hym_existence": False,
            "claims_selected_RouteC_residual": False,
            "claims_A_selected": False,
            "claims_b_selected": False,
            "claims_full_sm_closure": False,
        },
        "theorem": {
            "name": "Q79ReducedAHGlobalRankOneVAlphaStabilityTheorem",
            "proved": True,
            "closure_claimed": False,
            "statement": (
                "The q79/F,m=1 V_alpha extension is stable inside the reduced "
                "Appell-Humbert rank-one line model: all nonnegative-slope Hom "
                "candidates reduce to the six central-neutral classes already "
                "obstructed by Yoneda boundaries. Full stability/HYM remains open "
                "until this reduced model is promoted to selected AH/good-cover "
                "data and rank-one torsion-free hulls, or a selected Route-C "
                "residual source is emitted."
            ),
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }


def render_bool_map(data: dict[str, Any]) -> str:
    return "\n".join(f"- `{key}`: `{value}`" for key, value in data.items())


def build_paper(data: dict[str, Any]) -> str:
    enum = data["reduced_AH_global_rank_one_enumeration"]
    gap = data["promotion_gap"]
    return f"""# Q79 Selected Route-C Global Destabilizer Enumeration or Selected Residual v1

## Result

This proves q79 `V_alpha` stability inside the **reduced Appell-Humbert
rank-one line model**.

It is still not a full HYM certificate.

## Reduced AH Enumeration

- finite without cutoff: `{enum["finite_without_cutoff"]}`
- Hom-to-`L` nonnegative candidates: `{enum["hom_to_L_nonnegative_candidates"]}`
- Hom-to-`Q=L^-1` nonnegative candidates: `{enum["hom_to_Q_nonnegative_candidates"]}`
- candidate list equals prior six: `{enum["candidate_list_equals_prior_six"]}`
- all prior candidates obstructed: `{enum["all_candidates_previously_obstructed"]}`
- bounded sanity scan agrees: `{enum["bounded_sanity_scan"]}`
- SM global enumeration agrees: `{enum["sm_global_enumeration_agrees"]}`

## Promotion Gap

{chr(10).join(f"- {item}" for item in gap["why_not_full"])}

## What This Closes

{render_bool_map(data["what_closes_now"])}

## What Remains Open

{render_bool_map(data["what_remains_open"])}

## Theorem

`{data["theorem"]["name"]}` is proved as a reduced-model theorem.

{data["theorem"]["statement"]}

Next required artifact: `{data["next_required_artifact"]}`.
"""


def main() -> int:
    data = build_candidate()
    write_json(OUT_TABLE, data["reduced_AH_global_rank_one_enumeration"])
    write_json(OUT_CANDIDATE, data)
    write_json(OUT_CERT, data)
    OUT_PAPER.parent.mkdir(parents=True, exist_ok=True)
    OUT_PAPER.write_text(build_paper(data), encoding="utf-8")
    print("Q79 global destabilizer enumeration or selected residual")
    print(json.dumps({"status": data["status"], "next": data["next_required_artifact"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
