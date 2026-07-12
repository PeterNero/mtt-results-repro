"""Build the U1/Y selected AH/good-cover promotion and HYM bridge gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
TEXPAPERS = ROOT.parent
SM = TEXPAPERS / "mtt-sm-parity-closure"
Q79 = TEXPAPERS / "mtt-q79-proof-repro"

INPUTS = {
    "prior_u1y_stability_gate": DATA / "selected_u1y_stability_hym_or_routec_residual_source.candidate.json",
    "sm_ah_goodcover_hym_bridge": SM
    / "certificates"
    / "selected_routec_selected_ah_goodcover_promotion_hym_certificate_certificate.json",
    "sm_ah_goodcover_hym_candidate": SM
    / "candidate_data"
    / "selected_routec_selected_ah_goodcover_promotion_hym_certificate.candidate.json",
    "q79_ah_yoneda_promotion": Q79 / "certificates" / "valpha_appell_humbert_yoneda_promotion_certificate.json",
    "q79_gauduchon_wall_gate": Q79 / "certificates" / "selected_gauduchon_wall_radius_gate_certificate.json",
    "q79_hym_operator_validator": Q79 / "certificates" / "selected_hym_operator_source_validator_certificate.json",
    "q79_hym_operator_attempt": Q79 / "certificates" / "selected_hym_operator_source_attempt_certificate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_selected_ah_or_goodcover_promotion_hym_certificate.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_selected_ah_or_goodcover_promotion_hym_certificate_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_Selected_AH_or_GoodCover_Promotion_and_HYM_Certificate_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    prior = load(INPUTS["prior_u1y_stability_gate"])
    sm_cert = load(INPUTS["sm_ah_goodcover_hym_bridge"])
    sm_candidate = load(INPUTS["sm_ah_goodcover_hym_candidate"])
    ah_yoneda = load(INPUTS["q79_ah_yoneda_promotion"])
    gauduchon = load(INPUTS["q79_gauduchon_wall_gate"])
    hym_validator = load(INPUTS["q79_hym_operator_validator"])
    hym_attempt = load(INPUTS["q79_hym_operator_attempt"])

    selected_ah_goodcover_status = dict(sm_candidate["selected_AH_goodcover_status"])
    ah_guardrails = ah_yoneda["guardrails"]
    gauduchon_open = gauduchon["still_open"]

    bridge = {
        "rank_one_torsion_free_reflexive_hull_theorem_proved": sm_cert["reflexive_hull_reduction_proved"] is True
        and sm_candidate["rank_one_torsion_free_reflexive_hull_theorem"]["proved"] is True,
        "reduced_AH_stability_imported": prior["decision"]["reduced_AH_global_stability_proved"] is True,
        "conditional_AH_to_full_stability_bridge_proved": sm_candidate["reduced_AH_to_full_stability_implication"][
            "proved_conditionally"
        ]
        is True,
        "conditional_HYM_bridge_proved": sm_cert["conditional_HYM_bridge_proved"] is True
        and sm_candidate["HYM_bridge"]["proved_conditionally"] is True,
        "full_stability_proved": False,
        "full_HYM_proved": False,
        "selected_HYM_operator_source_verified": hym_validator["verdict"]["selected_hym_operator_source_verified"] is True
        and hym_attempt["calculation_results"]["selected_hym_operator_source_verified"] is True,
    }

    source_selection = {
        "AH_representative_constructed": selected_ah_goodcover_status["AH_automorphy_constructed"],
        "AH_degree_product_law_verified": selected_ah_goodcover_status["AH_degree_product_law_verified"],
        "AH_reduced_boundaries_promoted_conditionally": selected_ah_goodcover_status[
            "AH_reduced_boundaries_promoted_conditionally"
        ],
        "AH_selected_by_mtt": selected_ah_goodcover_status["AH_selected_by_mtt"],
        "AH_automorphy_selected_by_mtt": selected_ah_goodcover_status["AH_automorphy_selected_by_mtt"],
        "AH_neutral_pic0_selected_by_mtt": selected_ah_goodcover_status["AH_neutral_pic0_selected_by_mtt"],
        "AH_target_branch_selected_by_mtt": selected_ah_goodcover_status["AH_target_branch_selected_by_mtt"],
        "literal_goodcover_table_selected": ah_guardrails["claims_raw_finite_good_cover_table_supplied"],
        "pullback_cech_fixture_only": selected_ah_goodcover_status["pullback_cech_role"] == "UNSELECTED_FIXTURE",
    }

    gauduchon_status = {
        "target_wall_equivalent_radius_ratio": gauduchon["wall_dictionary"]["target_wall"]["equivalent_radius_ratio"],
        "target_wall_source_certified": gauduchon["current_source_status"]["source_certified_target_wall_present"],
        "integral_lift_source_certified": gauduchon["current_source_status"]["source_certified_integral_lift_present"],
        "nonabelian_or_route_c_wall_source_live": any(
            item["id"] == "construct_new_nonabelian_or_route_c_wall_source" and item["status"] == "LIVE"
            for item in gauduchon["route_evaluation"]
        ),
        "integral_cech_or_de_lift_live": any(
            item["id"] == "integral_cech_de_lift_of_finite_qutrit_class" and item["status"] == "LIVE"
            for item in gauduchon["route_evaluation"]
        ),
        "selected_Gauduchon_chamber_source_proved": False,
    }

    open_gates = {
        "selected_AH_representative_or_literal_goodcover_Cech_source": True,
        "operator_layer_neutral_Pic0_selection_or_quotient": True,
        "selected_target_branch_L_over_swapped_branch": True,
        "selected_Gauduchon_chamber_source": True,
        "selected_HYM_connection_values": True,
        "selected_HYM_operator_source_values": True,
        "selected_RouteC_residual_values": True,
        "same_source_ChernWeil_GS_row": True,
        "same_source_D_E_Riesz_Green_dotD": True,
        "primitive_C1_contractions": True,
        "finite_part_or_spectrum": True,
        "lambda_12": True,
        "full_SM_or_no_knob_closure": True,
    }

    decision = {
        "selected_AH_goodcover_promotion_gate_built": True,
        "rank_one_torsion_free_reflexive_hull_theorem_proved": bridge[
            "rank_one_torsion_free_reflexive_hull_theorem_proved"
        ],
        "conditional_AH_to_full_stability_bridge_proved": bridge["conditional_AH_to_full_stability_bridge_proved"],
        "conditional_HYM_bridge_proved": bridge["conditional_HYM_bridge_proved"],
        "selected_AH_or_goodcover_source_emitted": False,
        "selected_Gauduchon_chamber_source_proved": False,
        "full_stability_proved": False,
        "full_HYM_proved": False,
        "selected_HYM_operator_source_verified": False,
        "selected_RouteC_residual_values_emitted": False,
        "lambda_12_computable": False,
        "lambda_12_closed": False,
        "target_fitting_used": False,
        "strongest_result": (
            "Rank-one torsion-free destabilizers reduce to reflexive line hulls, and reduced AH stability "
            "promotes to full stability plus Li-Yau/HYM only after selected AH/good-cover and Gauduchon sources are supplied."
        ),
        "next_required_object": "Selected_U1Y_Selected_AH_GoodCover_Source_or_RouteC_SelectedResidual_v1",
        "alternative_next_object": "Selected_U1Y_Selected_RouteC_Residual_Values_and_DEDotD_Payload_v1",
    }

    candidate = {
        "candidate": "SelectedU1YSelectedAHOrGoodCoverPromotionHYMCertificate",
        "status": "U1Y_SELECTED_AH_GOODCOVER_REFLEXIVE_HULL_AND_CONDITIONAL_HYM_BRIDGE_PROVED_SOURCE_SELECTION_OPEN",
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "prior_status": prior["status"],
        "bridge": bridge,
        "source_selection": source_selection,
        "gauduchon_status": gauduchon_status,
        "hym_operator_gate": {
            "validator_formulated": hym_validator["verdict"]["validator_formulated"],
            "selected_hym_operator_source_verified": False,
            "attempt_status": hym_attempt["status"],
            "next_required_input": hym_attempt["verdict"]["next_required_input"],
        },
        "rank_one_torsion_free_reflexive_hull_theorem": sm_candidate[
            "rank_one_torsion_free_reflexive_hull_theorem"
        ],
        "conditional_HYM_bridge": sm_candidate["HYM_bridge"],
        "what_closes": {
            "rank_one_torsion_free_destabilizer_reduces_to_reflexive_line_hull": bridge[
                "rank_one_torsion_free_reflexive_hull_theorem_proved"
            ],
            "reduced_AH_stability_promotes_conditionally_once_selected_source_is_supplied": bridge[
                "conditional_AH_to_full_stability_bridge_proved"
            ],
            "Li_Yau_HYM_bridge_ready_if_selected_stability_and_Gauduchon_chamber_supplied": bridge[
                "conditional_HYM_bridge_proved"
            ],
            "remaining_blocker_identified_as_source_selection_not_destabilizer_enumeration": True,
        },
        "what_remains_open": open_gates,
        "guardrails": [
            "Do not treat an unselected AH representative as MTT-selected source data.",
            "Do not treat the pullback Cech validator fixture as a selected good-cover table.",
            "Do not apply HYM existence as an unconditional operator-source certificate.",
            "Do not compute lambda_12 until same-source U1/Y operator values and finite determinant data are emitted.",
            "Do not use observed electroweak data or benchmark flavor entries to choose the missing source.",
        ],
        "decision": decision,
        "closure_claimed": True,
        "closure_scope": "reflexive_hull_reduction_and_conditional_AH_HYM_bridge_only",
        "target_fitting_used": False,
        "open_gate_crosscheck": {
            "gauduchon_still_open": any(gauduchon_open.values()),
            "sm_cert_full_hym_proved": sm_cert["full_HYM_proved"],
            "q79_ah_claims_selected_AH_source": ah_guardrails["claims_MTT_selected_AH_source"],
        },
    }

    certificate = {
        "certificate": "SelectedU1YSelectedAHOrGoodCoverPromotionHYMCertificate",
        "status": candidate["status"],
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "what_closes": candidate["what_closes"],
        "what_remains_open": open_gates,
        "next_required_object": decision["next_required_object"],
        "alternative_next_object": decision["alternative_next_object"],
        "full_stability_proved": False,
        "full_HYM_proved": False,
        "lambda_12_closed": False,
        "target_fitting_used": False,
    }
    return candidate, certificate, render_note(candidate)


def render_note(candidate: dict[str, Any]) -> str:
    decision = candidate["decision"]
    bridge = candidate["bridge"]
    source = candidate["source_selection"]
    gauduchon = candidate["gauduchon_status"]
    closes = "\n".join(f"- `{key}` = `{str(value).lower()}`" for key, value in candidate["what_closes"].items())
    open_items = "\n".join(f"- `{key}`" for key, value in candidate["what_remains_open"].items() if value)
    guardrails = "\n".join(f"- {item}" for item in candidate["guardrails"])
    theorem_statement = candidate["rank_one_torsion_free_reflexive_hull_theorem"]["statement"]
    return f"""# Selected U1Y Selected AH or Good-Cover Promotion and HYM Certificate v1

## Result

```text
rank_one_torsion_free_reflexive_hull_theorem_proved = {str(decision["rank_one_torsion_free_reflexive_hull_theorem_proved"]).lower()}
conditional_AH_to_full_stability_bridge_proved = {str(decision["conditional_AH_to_full_stability_bridge_proved"]).lower()}
conditional_HYM_bridge_proved = {str(decision["conditional_HYM_bridge_proved"]).lower()}
selected_AH_or_goodcover_source_emitted = false
selected_Gauduchon_chamber_source_proved = false
full_stability_proved = false
full_HYM_proved = false
selected_HYM_operator_source_verified = false
lambda_12_computable = false
lambda_12_closed = false
target_fitting_used = false
```

This artifact closes the honest promotion bridge, not the selected source
itself. The destabilizer problem is no longer the main blocker: rank-one
torsion-free destabilizers reduce to line-bundle reflexive hulls, and the
reduced AH enumeration can promote once the selected AH/good-cover source is
emitted.

## Reflexive-Hull Reduction

{theorem_statement}

## Selected Source Status

```text
AH_representative_constructed = {str(source["AH_representative_constructed"]).lower()}
AH_degree_product_law_verified = {str(source["AH_degree_product_law_verified"]).lower()}
AH_reduced_boundaries_promoted_conditionally = {str(source["AH_reduced_boundaries_promoted_conditionally"]).lower()}
AH_selected_by_mtt = {str(source["AH_selected_by_mtt"]).lower()}
AH_neutral_pic0_selected_by_mtt = {str(source["AH_neutral_pic0_selected_by_mtt"]).lower()}
AH_target_branch_selected_by_mtt = {str(source["AH_target_branch_selected_by_mtt"]).lower()}
literal_goodcover_table_selected = {str(source["literal_goodcover_table_selected"]).lower()}
pullback_cech_fixture_only = {str(source["pullback_cech_fixture_only"]).lower()}
```

## HYM and Chamber Gate

```text
conditional_HYM_bridge_proved = {str(bridge["conditional_HYM_bridge_proved"]).lower()}
full_HYM_proved = false
target_wall_equivalent_radius_ratio = {gauduchon["target_wall_equivalent_radius_ratio"]}
target_wall_source_certified = {str(gauduchon["target_wall_source_certified"]).lower()}
integral_lift_source_certified = {str(gauduchon["integral_lift_source_certified"]).lower()}
selected_Gauduchon_chamber_source_proved = false
```

## What Closes

{closes}

## Still Open

{open_items}

## Guardrails

{guardrails}

## Decision

```text
strongest_result = {decision["strongest_result"]}
next_required_object = {decision["next_required_object"]}
alternative_next_object = {decision["alternative_next_object"]}
```
"""


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    missing = [str(path) for path in INPUTS.values() if not path.exists()]
    if missing:
        print("Missing inputs:")
        print("\n".join(missing))
        return 1
    candidate, certificate, note = build()
    write_json(OUTPUT_DATA, candidate)
    write_json(OUTPUT_CERT, certificate)
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(f"Wrote {OUTPUT_DATA}")
    print(f"Wrote {OUTPUT_CERT}")
    print(f"Wrote {OUTPUT_NOTE}")
    print(certificate["status"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
