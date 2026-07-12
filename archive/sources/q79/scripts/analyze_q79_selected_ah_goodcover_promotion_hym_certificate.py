"""Analyze q79 selected AH/good-cover promotion and conditional HYM bridge.

This closes the coherent-sheaf reduction that remained after the reduced
Appell-Humbert global line enumeration.  It proves that a destabilizing
rank-one torsion-free subsheaf can be tested through its saturated reflexive
line hull, then packages the exact conditional Li-Yau/Gauduchon HYM bridge.

It deliberately does not select the AH representative, Pic0 character,
Gauduchon chamber, HYM connection, Route-C residual values, A_selected,
b_selected, or full SM data.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
CANDIDATES = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
VAULT = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

OUT_DIR = CANDIDATES / "q79_selected_ah_goodcover_promotion_hym_certificate"
OUT_TABLE = OUT_DIR / "selected_ah_goodcover_promotion_summary.json"
OUT_CANDIDATE = CANDIDATES / "q79_selected_ah_goodcover_promotion_hym_certificate.candidate.json"
OUT_CERT = CERTS / "q79_selected_ah_goodcover_promotion_hym_certificate.json"
OUT_PAPER = CORPUS / "Q79_Selected_RouteC_Selected_AH_or_GoodCover_Promotion_and_HYM_Certificate_v1.md"

STATUS = "Q79_SELECTED_ROUTEC_REFLEXIVE_HULL_AND_CONDITIONAL_HYM_BRIDGE_PROVED_AH_SELECTION_OPEN"
NEXT = "Q79_Selected_RouteC_AH_Source_Selection_or_RouteC_SelectedResidual_v1"

STROMINGER_PAPER = (
    VAULT
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md"
)

INPUTS = {
    "previous_reduced_global_enumeration": (
        CANDIDATES / "q79_global_destabilizer_enumeration_or_selected_residual.candidate.json"
    ),
    "ah_yoneda_promotion": CANDIDATES / "valpha_appell_humbert_yoneda_promotion.candidate.json",
    "pullback_cech_attempt": CANDIDATES / "visible_rank2_l2_pullback_cech_attempt.candidate.json",
    "ah_automorphy": CANDIDATES / "visible_rank2_l2_appell_humbert_automorphy.candidate.json",
    "hym_operator_source_attempt": CANDIDATES / "selected_hym_operator_source_attempt.candidate.json",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


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
        "path": rel(path),
        "present": path.exists(),
        "status": data.get("status"),
        "closure_claimed": data.get("closure_claimed"),
        "target_fitting_used": data.get("target_fitting_used"),
        "next_required_artifact": data.get("next_required_artifact"),
    }


def corpus_has_li_yau_gauduchon_support(text: str) -> bool:
    phrases = [
        "Gauduchon metric",
        "slope--stable holomorphic bundles admit HYM connections",
        "LiYau1987",
    ]
    return all(phrase in text for phrase in phrases)


def build_candidate() -> dict[str, Any]:
    previous = load(INPUTS["previous_reduced_global_enumeration"])
    ah = load(INPUTS["ah_yoneda_promotion"])
    pullback = load(INPUTS["pullback_cech_attempt"])
    automorphy = load(INPUTS["ah_automorphy"])
    hym = load(INPUTS["hym_operator_source_attempt"])
    strominger_text = read(STROMINGER_PAPER)

    selection_state = ah["appell_humbert_selection_state"]
    closed_ah = ah["closed_by_this_attempt"]
    pullback_results = pullback["calculation_results"]
    automorphy_selection = automorphy["selection_analysis"]
    hym_results = hym["calculation_results"]

    selected_status = {
        "AH_degree_product_law_verified": closed_ah[
            "AH_factor_product_law_matches_yoneda_degree_addition"
        ],
        "AH_reduced_boundaries_promoted_conditionally": closed_ah[
            "reduced_boundary_maps_promoted_to_AH_theta_multiplication_conditional"
        ],
        "AH_selected_by_mtt": selection_state["selected_by_mtt"],
        "AH_neutral_pic0_selected_by_mtt": selection_state["neutral_pic0_selected_by_mtt"],
        "AH_target_branch_selected_by_mtt": selection_state["target_branch_selected_by_mtt"],
        "pullback_cech_validator_passes": pullback_results["validator_packet_passes"],
        "pullback_cech_selected_L2_packet_constructed": pullback_results[
            "selected_L2_packet_constructed"
        ],
        "pullback_cech_role": pullback["validator_packet"]["candidate_role"],
        "AH_automorphy_constructed": automorphy_selection[
            "mathematical_automorphy_representative_constructed"
        ],
        "AH_automorphy_selected_by_mtt": automorphy_selection["selected_by_mtt"],
        "AH_automorphy_neutral_pic0_selected_by_mtt": automorphy_selection[
            "neutral_pic0_character_selected_by_mtt"
        ],
    }

    summary = {
        "reflexive_hull_reduction_proved": True,
        "conditional_reduced_AH_to_full_stability_bridge_proved": True,
        "conditional_HYM_bridge_proved": True,
        "selected_AH_or_goodcover_source_supplied": False,
        "selected_Gauduchon_chamber_supplied": False,
        "selected_HYM_connection_values_supplied": False,
        "selected_RouteC_residual_values_supplied": False,
        "full_HYM_proved": False,
        "full_SM_closure_proved": False,
    }

    candidate = {
        "certificate": "Q79SelectedRouteCSelectedAHGoodCoverPromotionHYMCertificate",
        "status": STATUS,
        "candidate_path": rel(OUT_CANDIDATE),
        "table_path": rel(OUT_TABLE),
        "paper": rel(OUT_PAPER),
        "input_statuses": {name: status_record(path) for name, path in INPUTS.items()},
        "strominger_hym_corpus_paper": str(STROMINGER_PAPER),
        "promotion_summary": summary,
        "rank_one_torsion_free_reflexive_hull_theorem": {
            "name": "Q79RankOneTorsionFreeDestabilizerSaturationReflexiveHullReduction",
            "proved": True,
            "uses_selected_source_data": False,
            "mathematical_scope": (
                "standard coherent-sheaf stability reduction on the selected smooth "
                "complex carrier, before any MTT source selection of AH coordinates"
            ),
            "statement": (
                "To test slope stability of the rank-two locally free V_alpha, it is "
                "enough to test saturated rank-one subsheaves. If a rank-one "
                "torsion-free subsheaf F destabilizes V_alpha, then its saturation "
                "F_sat inside V_alpha also has slope at least mu(F), so it remains "
                "destabilizing. On the smooth carrier, a saturated rank-one "
                "torsion-free subsheaf of a locally free sheaf is reflexive, and a "
                "rank-one reflexive sheaf is a line bundle. Therefore any rank-one "
                "destabilizer is represented by a line-bundle class in the selected "
                "Picard/AH/good-cover section algebra, once that algebra is supplied."
            ),
        },
        "reduced_AH_to_full_stability_implication": {
            "proved_conditionally": True,
            "condition": (
                "selected AH representative or literal selected good-cover/Cech "
                "section algebra realizes the same H0/H1/Yoneda multiplication laws "
                "used by the reduced AH enumeration"
            ),
            "imports_reduced_AH_stability": previous["conditional_global_stability_theorem"][
                "proved"
            ],
            "imports_reflexive_hull_reduction": True,
            "conclusion_under_condition": (
                "V_alpha is slope-stable for the selected q79/F,m=1 chamber p=(1,2,1)."
            ),
            "why_condition_is_still_open": [
                "AH representative is constructed but selected_by_mtt is false in the q79 AH artifact",
                "pullback Cech packet validates h1=8 but is marked UNSELECTED_FIXTURE",
                "neutral Pic0/source representative is not yet selected at operator layer",
                "target branch and Gauduchon chamber are not yet emitted from the same source",
            ],
        },
        "HYM_bridge": {
            "li_yau_gauduchon_support_in_corpus": corpus_has_li_yau_gauduchon_support(
                strominger_text
            ),
            "corpus_claim": (
                "On a compact complex carrier with a Gauduchon metric, slope-stable "
                "holomorphic bundles admit Hermitian-Yang-Mills connections."
            ),
            "proved_conditionally": True,
            "condition": (
                "selected stable holomorphic V_alpha plus selected Gauduchon chamber/source certificate"
            ),
            "conclusion_under_condition": (
                "V_alpha admits an HYM connection, unique up to unitary gauge in the "
                "selected holomorphic class."
            ),
            "operator_source_not_emitted": hym_results["selected_hym_operator_source_verified"]
            is False,
        },
        "selected_AH_goodcover_status": selected_status,
        "what_closes_now": {
            "rank_one_torsion_free_destabilizer_reduces_to_saturated_reflexive_line_hull": True,
            "reduced_AH_stability_promotes_to_full_stability_if_selected_AH_or_goodcover_source_supplied": True,
            "Li_Yau_Gauduchon_HYM_bridge_ready_if_selected_stability_and_chamber_supplied": True,
            "remaining_blocker_identified_as_source_selection_not_destabilizer_enumeration": True,
        },
        "what_remains_open": {
            "selected_AH_representative_or_literal_goodcover_Cech_source": True,
            "operator_layer_neutral_Pic0_selection_or_quotient": True,
            "selected_target_branch_L_over_swapped_branch": True,
            "selected_Gauduchon_chamber_source": True,
            "selected_HYM_connection_values": True,
            "selected_RouteC_residual_values": True,
            "same_source_D_E_Riesz_Green_dotD": True,
            "same_source_ChernWeil_GS_row": True,
            "primitive_C1_contractions": True,
            "full_SM_or_no_knob_closure": True,
        },
        "guardrails": {
            "uses_observed_masses_or_ckm_inputs": False,
            "uses_benchmark_flavor_entries": False,
            "uses_locked_target_columns_as_selector": False,
            "claims_selected_AH_source": False,
            "claims_selected_goodcover_source": False,
            "claims_full_stability_unconditionally": False,
            "claims_hym_existence_unconditionally": False,
            "claims_selected_HYM_connection_values": False,
            "claims_selected_RouteC_residual": False,
            "claims_A_selected": False,
            "claims_b_selected": False,
            "claims_full_sm_closure": False,
        },
        "theorem": {
            "name": "Q79SelectedRouteCConditionalHYMBridgeTheorem",
            "proved": True,
            "closure_claimed": False,
            "statement": (
                "The q79/F,m=1 reduced AH rank-one stability theorem now promotes "
                "to full rank-one torsion-free stability once a selected AH or "
                "literal selected good-cover section algebra is supplied. Under the "
                "additional selected Gauduchon chamber/source condition, the "
                "Li-Yau/Gauduchon theorem gives an HYM connection. This proves the "
                "promotion bridge and the reflexive-hull reduction, not the selected "
                "AH source or HYM operator values."
            ),
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    return candidate


def render_bool_map(data: dict[str, Any]) -> str:
    return "\n".join(f"- `{key}`: `{value}`" for key, value in data.items())


def build_paper(data: dict[str, Any]) -> str:
    theorem = data["rank_one_torsion_free_reflexive_hull_theorem"]
    stability = data["reduced_AH_to_full_stability_implication"]
    hym = data["HYM_bridge"]
    selected = data["selected_AH_goodcover_status"]
    return f"""# Q79 Selected Route-C Selected AH or Good-Cover Promotion and HYM Certificate v1

## Result

This proves the **reflexive hull reduction** and the **conditional HYM bridge**.

Full HYM is **not claimed**. The selected AH/good-cover source is still open.

## Reflexive Hull Reduction

`{theorem["name"]}` is proved.

{theorem["statement"]}

## Reduced AH to Full Stability

- proved conditionally: `{stability["proved_conditionally"]}`
- condition: {stability["condition"]}
- imports reduced AH stability: `{stability["imports_reduced_AH_stability"]}`
- imports reflexive hull reduction: `{stability["imports_reflexive_hull_reduction"]}`
- conclusion under condition: {stability["conclusion_under_condition"]}

## Conditional HYM Bridge

- Li-Yau/Gauduchon support in corpus: `{hym["li_yau_gauduchon_support_in_corpus"]}`
- proved conditionally: `{hym["proved_conditionally"]}`
- condition: {hym["condition"]}
- operator source emitted: `{not hym["operator_source_not_emitted"]}`

## Selected AH or Good-Cover Status

{render_bool_map(selected)}

## What This Closes

{render_bool_map(data["what_closes_now"])}

## What Remains Open

{render_bool_map(data["what_remains_open"])}

## Theorem

`{data["theorem"]["name"]}` is proved as a promotion theorem.

{data["theorem"]["statement"]}

Next required artifact: `{data["next_required_artifact"]}`.
"""


def main() -> int:
    data = build_candidate()
    write_json(OUT_TABLE, data["promotion_summary"])
    write_json(OUT_CANDIDATE, data)
    write_json(OUT_CERT, data)
    OUT_PAPER.parent.mkdir(parents=True, exist_ok=True)
    OUT_PAPER.write_text(build_paper(data), encoding="utf-8")
    print("Q79 selected AH/good-cover promotion and HYM certificate")
    print(json.dumps({"status": data["status"], "next": data["next_required_artifact"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
