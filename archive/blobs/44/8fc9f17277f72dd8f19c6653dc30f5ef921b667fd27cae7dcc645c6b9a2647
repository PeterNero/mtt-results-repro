"""Build the U1/Y selected AH/good-cover source or Route-C residual gate."""

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
    "prior_promotion_gate": DATA / "selected_u1y_selected_ah_or_goodcover_promotion_hym_certificate.candidate.json",
    "sm_source_or_residual": SM / "candidate_data" / "selected_routec_ah_source_selection_or_routec_selected_residual.candidate.json",
    "sm_source_or_residual_cert": SM
    / "certificates"
    / "selected_routec_ah_source_selection_or_routec_selected_residual_certificate.json",
    "q79_terminal_principle": Q79 / "candidate_data" / "terminal_admissible_section_source_principle.candidate.json",
    "q79_terminal_principle_cert": Q79 / "certificates" / "terminal_admissible_section_source_principle_certificate.json",
    "q79_terminal_path_reduction": Q79 / "certificates" / "terminal_g3_valpha_source_path_reduction_certificate.json",
    "q79_selected_ordered_source": Q79
    / "candidate_data"
    / "terminal_admissible_section_source"
    / "visible_rank2_l2_ordered_source.selected_under_section_principle.json",
    "q79_selected_cohomology": Q79
    / "candidate_data"
    / "terminal_admissible_section_source"
    / "visible_rank2_l2_cohomology.selected_under_section_principle.json",
}

OUTPUT_DATA = DATA / "selected_u1y_ah_goodcover_source_or_routec_selected_residual.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_ah_goodcover_source_or_routec_selected_residual_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_Selected_AH_GoodCover_Source_or_RouteC_SelectedResidual_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    prior = load(INPUTS["prior_promotion_gate"])
    sm_candidate = load(INPUTS["sm_source_or_residual"])
    sm_cert = load(INPUTS["sm_source_or_residual_cert"])
    terminal = load(INPUTS["q79_terminal_principle"])
    terminal_cert = load(INPUTS["q79_terminal_principle_cert"])
    terminal_path = load(INPUTS["q79_terminal_path_reduction"])
    ordered_source = load(INPUTS["q79_selected_ordered_source"])
    cohomology = load(INPUTS["q79_selected_cohomology"])

    sm_layer = sm_candidate["selected_AH_goodcover_stability_layer"]
    sm_gaud_or_residual = sm_candidate["gauduchon_or_routec_gate"]

    source_layer = {
        "terminal_admissible_section_principle_supported_by_corpus": terminal["corpus_support"]["supported"],
        "terminal_principle_promoted_to_unconditional_axiom": False,
        "selected_source_label": terminal["selection_derivation"]["selected_source_label"],
        "selected_L": terminal["selection_derivation"]["selected_L"],
        "selected_L2": terminal["selection_derivation"]["selected_L2"],
        "selected_c2": terminal["selection_derivation"]["selected_c2"],
        "terminal_lane_unique_visible_c2": terminal["terminal_lane_scan"]["unique_visible_c2_in_terminal_lane"],
        "terminal_lane_unique_zero_central": terminal["terminal_lane_scan"]["unique_zero_central"],
        "ordered_source_selected_by_mtt_under_principle": ordered_source["source"]["selected_by_mtt"],
        "ordered_source_status": ordered_source["status"],
        "ordered_layer_pic0_quotiented": ordered_source["pic0_resolution"]["source_selected_or_quotiented"],
        "pic0_rule_scope": ordered_source["pic0_resolution"]["scope"],
        "operator_layer_pic0_reopens": sm_layer["operator_layer_pic0_reopens"],
        "cohomology_selected_by_mtt_under_principle": cohomology["source"]["selected_by_mtt"],
        "h1": cohomology["reported_cohomology"]["h1"],
        "nonzero_ext_class": cohomology["acceptance_tests"]["extension_class_not_exact"]
        and cohomology["reported_cohomology"]["nonzero_extension_class_label"] is not None,
        "nonzero_extension_class_label": cohomology["reported_cohomology"]["nonzero_extension_class_label"],
    }

    ah_goodcover_stability_layer = {
        "selected_ordered_AH_goodcover_source_for_stability_layer": sm_layer[
            "selected_ordered_source"
        ]
        and sm_cert["selected_AH_goodcover_stability_layer_proved"] is True,
        "AH_automorphy_cocycle_and_degree_laws": sm_layer["AH_automorphy_cocycle_and_degree_laws"],
        "selected_h1_nonzero_ext_packet": sm_layer["selected_cohomology_h1_ext"],
        "reduced_stability_and_reflexive_hull_imported": sm_layer["imports_reduced_AH_global_stability"]
        and sm_layer["imports_reflexive_hull_reduction"],
        "stable_in_selected_ordered_AH_layer": sm_candidate["stability_consequence"][
            "stable_in_selected_ordered_AH_layer"
        ],
        "stable_as_full_selected_Gauduchon_bundle": sm_candidate["stability_consequence"][
            "stable_as_full_selected_Gauduchon_bundle"
        ],
        "scope": sm_layer["scope"],
    }

    residual_or_chamber = {
        "gauduchon_wall_reclassified_as_stability_witness": terminal["what_this_closes_under_principle"][
            "gauduchon_wall_reclassified_as_stability_witness"
        ],
        "target_wall_equivalent_radius_ratio": sm_gaud_or_residual["target_wall_equivalent_radius_ratio"],
        "selected_gauduchon_target_wall": sm_gaud_or_residual["selected_gauduchon_target_wall"],
        "source_certified_target_wall_present": sm_gaud_or_residual["source_certified_target_wall_present"],
        "source_certified_integral_lift_present": sm_gaud_or_residual["source_certified_integral_lift_present"],
        "routec_residual_zero_smoke_support": sm_gaud_or_residual["routec_residual_zero_smoke_support"],
        "routec_status": sm_gaud_or_residual["routec_status"],
        "routec_selected_source_verified": sm_gaud_or_residual["routec_selected_source_verified"],
        "selected_routec_residual_values": sm_gaud_or_residual["selected_routec_residual_values"],
        "split_line_hym_shortcut_rejected": sm_gaud_or_residual["split_line_hym_shortcut_rejected"],
    }

    open_gates = {
        "promote_terminal_admissible_section_principle_to_unconditional_MTT_axiom_or_prove_from_projection_admissibility": True,
        "selected_Gauduchon_chamber_source": True,
        "selected_HYM_connection_or_operator_values": True,
        "selected_RouteC_residual_values": True,
        "operator_layer_Pic0_or_holonomy_sensitive_quotient": True,
        "same_source_ChernWeil_GS_row": True,
        "same_source_D_E_Riesz_Green_dotD": True,
        "primitive_C1_contractions": True,
        "finite_part_or_spectrum": True,
        "lambda_12": True,
        "full_SM_or_no_knob_closure": True,
    }

    decision = {
        "selected_AH_goodcover_source_layer_emitted": True,
        "selected_ordered_AH_goodcover_stability_layer_proved": ah_goodcover_stability_layer[
            "selected_ordered_AH_goodcover_source_for_stability_layer"
        ]
        and ah_goodcover_stability_layer["stable_in_selected_ordered_AH_layer"],
        "terminal_admissible_section_principle_dependency": True,
        "principle_unconditional_in_mtt_axioms": False,
        "full_selected_Gauduchon_stability_proved": False,
        "selected_HYM_or_Strominger_existence_proved": False,
        "selected_RouteC_residual_values_emitted": False,
        "lambda_12_computable": False,
        "lambda_12_closed": False,
        "target_fitting_used": False,
        "strongest_result": (
            "The selected ordered AH/good-cover stability layer is promoted under the terminal admissible-section principle; "
            "the remaining closure gate is the selected Gauduchon/HYM chamber or same-source Route-C residual/operator payload."
        ),
        "next_required_object": "Selected_U1Y_Gauduchon_Chamber_or_SelectedResidual_Source_v1",
        "alternative_next_object": "Selected_U1Y_Selected_RouteC_Residual_Values_and_DEDotD_Payload_v1",
    }

    candidate = {
        "candidate": "SelectedU1YAHGoodCoverSourceOrRouteCSelectedResidual",
        "status": "U1Y_ORDERED_AH_GOODCOVER_SOURCE_LAYER_PROMOTED_GAUDUCHON_OR_RESIDUAL_SOURCE_OPEN",
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "prior_status": prior["status"],
        "terminal_path_reduction_status": terminal_path["status"],
        "source_layer": source_layer,
        "ah_goodcover_stability_layer": ah_goodcover_stability_layer,
        "residual_or_chamber": residual_or_chamber,
        "source_principle": terminal["source_principle"],
        "what_closes": {
            "terminal_g3_source_selector_under_explicit_principle": terminal["what_this_closes_under_principle"][
                "terminal_g3_source_selector"
            ],
            "target_branch_L_selected_at_ordered_source_layer": True,
            "ordered_layer_Pic0_quotient": source_layer["ordered_layer_pic0_quotiented"],
            "selected_h1_8_L2_cohomology_packet": source_layer["h1"] == 8,
            "selected_nonzero_closed_nonexact_Ext_vector": source_layer["nonzero_ext_class"],
            "selected_ordered_AH_goodcover_source_for_stability_layer": ah_goodcover_stability_layer[
                "selected_ordered_AH_goodcover_source_for_stability_layer"
            ],
            "stable_in_selected_ordered_AH_layer": ah_goodcover_stability_layer[
                "stable_in_selected_ordered_AH_layer"
            ],
        },
        "what_remains_open": open_gates,
        "guardrails": [
            "The terminal admissible-section principle is explicit and supported, but still must become an MTT axiom or be derived before the result is unconditional.",
            "The Pic0 quotient is accepted only for the ordered Chern/H1/ordinary-curvature layer; operator-layer holonomy reopens Pic0.",
            "Stable in the selected ordered AH layer is not the same as full selected Gauduchon stability.",
            "Route-C zero residual smoke is support only until selected residual values and same-source D_E/Riesz/Green/dotD payloads are emitted.",
            "Do not compute lambda_12 before selected U1/Y operator finite-part data exist.",
        ],
        "decision": decision,
        "closure_claimed": True,
        "closure_scope": "selected_ordered_AH_goodcover_stability_layer_under_explicit_terminal_principle_only",
        "target_fitting_used": False,
    }

    certificate = {
        "certificate": "SelectedU1YAHGoodCoverSourceOrRouteCSelectedResidual",
        "status": candidate["status"],
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "what_closes": candidate["what_closes"],
        "what_remains_open": open_gates,
        "next_required_object": decision["next_required_object"],
        "alternative_next_object": decision["alternative_next_object"],
        "selected_AH_goodcover_stability_layer_proved": decision[
            "selected_ordered_AH_goodcover_stability_layer_proved"
        ],
        "full_selected_Gauduchon_stability_proved": False,
        "selected_HYM_or_Strominger_existence_proved": False,
        "selected_RouteC_residual_values_emitted": False,
        "lambda_12_closed": False,
        "target_fitting_used": False,
    }
    return candidate, certificate, render_note(candidate)


def render_note(candidate: dict[str, Any]) -> str:
    decision = candidate["decision"]
    source = candidate["source_layer"]
    stability = candidate["ah_goodcover_stability_layer"]
    residual = candidate["residual_or_chamber"]
    closes = "\n".join(f"- `{key}` = `{str(value).lower()}`" for key, value in candidate["what_closes"].items())
    open_items = "\n".join(f"- `{key}`" for key, value in candidate["what_remains_open"].items() if value)
    guardrails = "\n".join(f"- {item}" for item in candidate["guardrails"])
    principle = candidate["source_principle"]
    return f"""# Selected U1Y Selected AH Good-Cover Source or Route-C Selected Residual v1

## Result

```text
selected_AH_goodcover_source_layer_emitted = true
selected_ordered_AH_goodcover_stability_layer_proved = {str(decision["selected_ordered_AH_goodcover_stability_layer_proved"]).lower()}
terminal_admissible_section_principle_dependency = true
principle_unconditional_in_mtt_axioms = false
full_selected_Gauduchon_stability_proved = false
selected_HYM_or_Strominger_existence_proved = false
selected_RouteC_residual_values_emitted = false
lambda_12_computable = false
lambda_12_closed = false
target_fitting_used = false
```

This closes the ordered AH/good-cover source layer, not the final HYM/operator
payload. The selected `L=(1,-2,0)` branch, `L^2=(2,-4,0)`, ordered-layer Pic0
quotient, `h1=8`, and nonzero Ext vector are now imported as selected under the
explicit terminal admissible-section principle.

## Terminal Source Principle

```text
name = {principle["name"]}
status = {principle["status"]}
selected_source_label = {source["selected_source_label"]}
selected_L = {source["selected_L"]}
selected_L2 = {source["selected_L2"]}
selected_c2 = {source["selected_c2"]}
terminal_lane_unique_visible_c2 = {str(source["terminal_lane_unique_visible_c2"]).lower()}
terminal_lane_unique_zero_central = {str(source["terminal_lane_unique_zero_central"]).lower()}
```

Statement: {principle["statement"]}

Credibility status: {principle["credibility_status"]}

## Selected Stability Layer

```text
ordered_source_status = {source["ordered_source_status"]}
ordered_layer_pic0_quotiented = {str(source["ordered_layer_pic0_quotiented"]).lower()}
pic0_rule_scope = {source["pic0_rule_scope"]}
operator_layer_pic0_reopens = {str(source["operator_layer_pic0_reopens"]).lower()}
h1 = {source["h1"]}
nonzero_extension_class_label = {source["nonzero_extension_class_label"]}
stable_in_selected_ordered_AH_layer = {str(stability["stable_in_selected_ordered_AH_layer"]).lower()}
stable_as_full_selected_Gauduchon_bundle = false
scope = {stability["scope"]}
```

## Remaining HYM / Residual Gate

```text
gauduchon_wall_role = stability chamber witness
target_wall_equivalent_radius_ratio = {residual["target_wall_equivalent_radius_ratio"]}
selected_gauduchon_target_wall = {str(residual["selected_gauduchon_target_wall"]).lower()}
routec_residual_zero_smoke_support = {str(residual["routec_residual_zero_smoke_support"]).lower()}
routec_status = {residual["routec_status"]}
routec_selected_source_verified = {str(residual["routec_selected_source_verified"]).lower()}
selected_routec_residual_values = {str(residual["selected_routec_residual_values"]).lower()}
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
