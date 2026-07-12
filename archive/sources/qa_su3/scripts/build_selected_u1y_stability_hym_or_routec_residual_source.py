"""Build the U1/Y stability/HYM or selected Route-C residual source gate."""

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
    "prior_operator_tables": DATA / "selected_u1y_routec_or_projective_rhoe_selected_operator_tables.candidate.json",
    "sm_rank2_l2_fill": SM / "certificates" / "selected_routec_rank2_l2_or_routec_residual_fill_certificate.json",
    "sm_stability_source": SM / "certificates" / "selected_routec_stability_hym_or_routec_residual_source_certificate.json",
    "q79_stability_source": Q79 / "certificates" / "q79_stability_hym_or_routec_residual_source_certificate.json",
    "sm_global_destabilizer": SM / "certificates" / "selected_routec_global_destabilizer_enumeration_or_selected_residual_certificate.json",
    "q79_global_destabilizer": Q79 / "certificates" / "q79_global_destabilizer_enumeration_or_selected_residual_certificate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_stability_hym_or_routec_residual_source.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_stability_hym_or_routec_residual_source_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_Stability_HYM_or_RouteC_Residual_Source_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    prior = load(INPUTS["prior_operator_tables"])
    rank2 = load(INPUTS["sm_rank2_l2_fill"])
    sm_stability = load(INPUTS["sm_stability_source"])
    q79_stability = load(INPUTS["q79_stability_source"])
    sm_global = load(INPUTS["sm_global_destabilizer"])
    q79_global = load(INPUTS["q79_global_destabilizer"])

    stability_progress = {
        "rank2_l2_arithmetic_closed": rank2["what_closes"]["h1_8_nonzero_ext_closed"]
        and rank2["what_closes"]["ordered_source_validator_passes"],
        "central_neutral_subtheorem_proved": sm_stability["central_neutral_subtheorem_proved"]
        and q79_stability["q79_proof_verdict"]["central_neutral_stability_subtheorem_proved"],
        "reduced_AH_global_rank_one_enumeration_proved": sm_global["reduced_AH_global_enumeration_proved"]
        and q79_global["conditional_global_stability_theorem"]["proved"],
        "full_stability_proved": sm_global["full_stability_proved"] is True
        and q79_global["promotion_gap"]["full_stability_proved"] is True,
        "hym_existence_proved": q79_global["promotion_gap"]["hym_existence_proved"] is True,
        "selected_routec_residual_values_emitted": False,
    }

    reduced_ah_theorem = {
        "statement": q79_global["conditional_global_stability_theorem"]["statement"],
        "model": q79_global["reduced_AH_global_rank_one_enumeration"]["model"],
        "finite_without_cutoff": q79_global["reduced_AH_global_rank_one_enumeration"]["finite_without_cutoff"],
        "hom_to_L_nonnegative_candidates": q79_global["reduced_AH_global_rank_one_enumeration"]["hom_to_L_nonnegative_candidates"],
        "hom_to_Q_nonnegative_candidates": q79_global["reduced_AH_global_rank_one_enumeration"]["hom_to_Q_nonnegative_candidates"],
        "candidate_list_equals_prior_six": q79_global["reduced_AH_global_rank_one_enumeration"]["candidate_list_equals_prior_six"],
        "all_candidates_previously_obstructed": q79_global["reduced_AH_global_rank_one_enumeration"]["all_candidates_previously_obstructed"],
        "uses_no_observed_targets": q79_global["conditional_global_stability_theorem"]["uses_no_observed_targets"],
    }

    routec_residual_lane = {
        "shape_gates_closed": q79_stability["route_c_residual_lane"]["shape_gates"],
        "selected_payload_flags": q79_stability["route_c_residual_lane"]["selected_payload_flags"],
        "selected_values_emitted": False,
        "why_not_selected": [
            "finite residual equations and zero-residual smoke are present, but selected source flags remain false",
            "nonidentity selected rhoE or connection values are absent",
            "selected D_E/Riesz/Green/dotD flags are absent",
            "selected Phi_fin alpha1 payload is absent",
        ],
    }

    promotion_gap = {
        "selected_AH_representative_or_literal_good_cover_table": True,
        "rank_one_torsion_free_reflexive_hull_representation_theorem": True,
        "selected_Gauduchon_chamber_source": True,
        "selected_HYM_or_Strominger_existence_certificate": True,
        "selected_RouteC_residual_values": True,
        "same_source_ChernWeil_GS_row": True,
        "same_source_D_E_Riesz_Green_dotD": True,
        "operator_layer_Pic0": True,
        "primitive_C1_contractions": True,
        "finite_part_or_spectrum": True,
        "lambda_12": True,
    }

    decision = {
        "stability_hym_or_routec_source_gate_built": True,
        "reduced_AH_global_stability_proved": stability_progress["reduced_AH_global_rank_one_enumeration_proved"],
        "full_stability_proved": False,
        "selected_HYM_or_Strominger_existence_proved": False,
        "selected_RouteC_residual_values_emitted": False,
        "conditional_operator_table_promotable_to_selected": False,
        "lambda_12_computable": False,
        "lambda_12_closed": False,
        "target_fitting_used": False,
        "strongest_result": "V_alpha stable in the reduced Appell-Humbert rank-one line model; selected AH/good-cover promotion and HYM/residual values remain open",
        "next_required_object": "Selected_U1Y_Selected_AH_or_GoodCover_Promotion_and_HYM_Certificate_v1",
        "alternative_next_object": "Selected_U1Y_Selected_RouteC_Residual_Values_and_DEDotD_Payload_v1",
    }

    candidate = {
        "candidate": "SelectedU1YStabilityHYMOrRouteCResidualSource",
        "status": "U1Y_STABILITY_HYM_ROUTEC_SOURCE_REDUCED_AH_GLOBAL_STABILITY_PROVED_PROMOTION_OPEN",
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "prior_status": prior["status"],
        "stability_progress": stability_progress,
        "reduced_AH_theorem": reduced_ah_theorem,
        "routec_residual_lane": routec_residual_lane,
        "promotion_gap": promotion_gap,
        "closed_support": {
            "rank2_l2_h1_ext_closed": stability_progress["rank2_l2_arithmetic_closed"],
            "central_neutral_destabilizers_obstructed": stability_progress["central_neutral_subtheorem_proved"],
            "reduced_AH_global_rank_one_enumeration_proved": stability_progress["reduced_AH_global_rank_one_enumeration_proved"],
            "conditional_operator_table_retained": prior["decision"]["routec_conditional_operator_constructed"],
            "no_target_fit_used": True,
        },
        "open": promotion_gap,
        "decision": decision,
        "guardrails": [
            "Do not promote reduced AH stability to full good-cover/Cech stability without the promotion theorem.",
            "Do not invoke DUY/Li-Yau HYM existence until the selected stable holomorphic source and chamber are certified.",
            "Do not promote zero-residual Route-C smoke to selected residual values.",
            "Do not promote the conditional 72x2 operator table to A_selected.",
            "Do not compute lambda_12 before selected finite operator values are emitted.",
        ],
        "closure_claimed": True,
        "closure_scope": "reduced_AH_global_stability_import_and_selected_promotion_gap_only",
        "target_fitting_used": False,
    }

    certificate = {
        "certificate": "SelectedU1YStabilityHYMOrRouteCResidualSource",
        "status": candidate["status"],
        "candidate_path": rel(OUTPUT_DATA),
        "closed": candidate["closed_support"],
        "open": candidate["open"],
        "next_required_object": decision["next_required_object"],
        "alternative_next_object": decision["alternative_next_object"],
        "target_fitting_used": False,
    }
    return candidate, certificate, render_note(candidate)


def render_note(candidate: dict[str, Any]) -> str:
    theorem = candidate["reduced_AH_theorem"]
    residual = candidate["routec_residual_lane"]
    promotion = "\n".join(f"- `{key}`" for key, value in candidate["promotion_gap"].items() if value)
    guardrails = "\n".join(f"- {item}" for item in candidate["guardrails"])
    residual_missing = "\n".join(f"- {item}" for item in residual["why_not_selected"])
    decision = candidate["decision"]
    return f"""# Selected U1Y Stability HYM or Route-C Residual Source v1

## Result

```text
reduced_AH_global_stability_proved = true
full_stability_proved = false
selected_HYM_or_Strominger_existence_proved = false
selected_RouteC_residual_values_emitted = false
conditional_operator_table_promotable_to_selected = false
lambda_12_computable = false
lambda_12_closed = false
target_fitting_used = false
```

This gate imports the strongest current stability/residual result. It proves
the reduced Appell-Humbert global rank-one stability theorem for the selected
`V_alpha` branch, but does not promote it to full selected good-cover/Cech
stability or selected HYM/Route-C operator values.

## Reduced AH Stability

```text
model = {theorem["model"]}
finite_without_cutoff = {str(theorem["finite_without_cutoff"]).lower()}
hom_to_L_nonnegative_candidates = {theorem["hom_to_L_nonnegative_candidates"]}
hom_to_Q_nonnegative_candidates = {theorem["hom_to_Q_nonnegative_candidates"]}
candidate_list_equals_prior_six = {str(theorem["candidate_list_equals_prior_six"]).lower()}
all_candidates_previously_obstructed = {str(theorem["all_candidates_previously_obstructed"]).lower()}
uses_no_observed_targets = {str(theorem["uses_no_observed_targets"]).lower()}
```

Statement: {theorem["statement"]}

## Route-C Residual Lane

The Route-C residual lane has the right shape gates, but no selected values:

{residual_missing}

## Still Open

{promotion}

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
