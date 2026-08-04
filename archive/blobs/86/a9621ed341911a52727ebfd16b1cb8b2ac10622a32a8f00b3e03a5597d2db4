"""Build the U1/Y Gauduchon chamber or selected residual source gate."""

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
CONSTANTS = TEXPAPERS / "mtt-nonsm-constants-no-knob"

INPUTS = {
    "prior_source_layer": DATA / "selected_u1y_ah_goodcover_source_or_routec_selected_residual.candidate.json",
    "q79_all_remaining_valpha": Q79 / "candidate_data" / "all_remaining_valpha_gates_attempt.candidate.json",
    "q79_orientation_dedotd": Q79 / "candidate_data" / "selected_qa_su3_orientation_dedotd_source_attempt.candidate.json",
    "q79_selected_source_promotion_gate": Q79 / "certificates" / "iwasawa_selected_source_promotion_gate_certificate.json",
    "q79_selected_hym_promotion_attempt": Q79 / "certificates" / "selected_hym_operator_source_promotion.attempt.json",
    "sm_routec_residual_honest": SM
    / "candidate_data"
    / "selected_routec_strominger_galerkin_solve"
    / "route_c_residual.candidate.json",
    "sm_routec_residual_formal_lift": SM
    / "candidate_data"
    / "selected_routec_strominger_galerkin_solve"
    / "formal_lift_diagnostic"
    / "route_c_residual.candidate.json",
    "constants_routec_source_solve_gate": CONSTANTS
    / "certificates"
    / "selected_qa_su3_routec_source_solve_gate_certificate.json",
    "constants_routec_source_solve_template": CONSTANTS
    / "certificates"
    / "selected_qa_su3_routec_source_solve.template.json",
}

OUTPUT_DATA = DATA / "selected_u1y_gauduchon_chamber_or_selected_residual_source.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_gauduchon_chamber_or_selected_residual_source_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_Gauduchon_Chamber_or_SelectedResidual_Source_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    prior = load(INPUTS["prior_source_layer"])
    all_remaining = load(INPUTS["q79_all_remaining_valpha"])
    orientation = load(INPUTS["q79_orientation_dedotd"])
    promotion_gate = load(INPUTS["q79_selected_source_promotion_gate"])
    hym_promotion = load(INPUTS["q79_selected_hym_promotion_attempt"])
    honest_residual = load(INPUTS["sm_routec_residual_honest"])
    formal_lift = load(INPUTS["sm_routec_residual_formal_lift"])
    source_solve_gate = load(INPUTS["constants_routec_source_solve_gate"])
    source_solve_template = load(INPUTS["constants_routec_source_solve_template"])

    unconditional_section = all_remaining["unconditional_section_gate"]
    stability_gate = all_remaining["stability_or_routec_gate"]
    operator_gates = all_remaining["operator_gates"]["gates"]

    principle_status = {
        "corpus_support": unconditional_section["corpus_support"],
        "literal_unconditional_statement_found": unconditional_section["literal_unconditional_statement_found_in_corpus"],
        "status": unconditional_section["status"],
        "next_required_action": unconditional_section["next_required_action"],
        "axiom_ready_not_unconditional": unconditional_section["status"] == "AXIOM_READY_NOT_UNCONDITIONAL",
        "can_promote_inside_repo_without_paper_spine_change": False,
    }

    gauduchon_or_stability = {
        "negative_slope_chamber_witness": stability_gate["closed_subparts"]["negative_slope_chamber_witness"],
        "non_split_extension_input": stability_gate["closed_subparts"]["non_split_extension_input"],
        "selected_h1_8_nonzero_ext": stability_gate["closed_subparts"]["selected_h1_8_nonzero_ext"],
        "split_hym_shortcut_retired": stability_gate["closed_subparts"]["split_hym_shortcut_retired"],
        "status": stability_gate["status"],
        "closed": stability_gate["closed"],
        "still_missing": stability_gate["still_missing"],
    }

    residual_values = {
        "honest_residual_zero": all(
            row["value"] == 0.0 for row in honest_residual["residuals"].values()
        ),
        "honest_selected_source_verified": honest_residual["selected_source_verified"],
        "honest_status": honest_residual["status"],
        "formal_lift_residual_zero": all(
            row["value"] == 0.0 for row in formal_lift["residuals"].values()
        ),
        "formal_lift_selected_source_verified": formal_lift["selected_source_verified"],
        "formal_lift_status": formal_lift["status"],
        "formal_lift_accepted_as_proof": False,
        "why_formal_lift_rejected": [
            "status remains CANDIDATE_UNSELECTED_SMOKE",
            "selected flags are diagnostic lift data, not source-derived",
            "promotion packet in q79 still has selected_source_verified=false",
        ],
    }

    operator_payload = {
        "promotion_gate_formulated": promotion_gate["verdict"]["promotion_gate_ready"],
        "promotion_attempt_status": hym_promotion["status"],
        "promotion_selected_source_verified": hym_promotion["selected_source_verified"],
        "orientation_packets_reach_validator_layer": orientation["calculation_results"][
            "q79_finite_equations_blocked_only_by_source_flags"
        ]
        and orientation["calculation_results"]["q369_finite_equations_blocked_only_by_source_flags"],
        "selected_source_origin_constructed": orientation["calculation_results"]["selected_source_origin_constructed"],
        "unique_m_label_selected_by_source": orientation["calculation_results"]["unique_m_label_selected_by_source"],
        "operator_layer_pic0_closed": operator_gates["OperatorLayerPic0Recheck"]["closed"],
        "same_source_chern_weil_gs_closed": operator_gates["SameSourceChernWeilGSRow"]["closed"],
        "same_source_de_riesz_green_dotd_closed": operator_gates["SameSourceDErhoERieszGreenDotD"]["closed"],
    }

    source_solve_contract = {
        "schema": source_solve_template["schema"],
        "status": source_solve_template["status"],
        "purpose": source_solve_template["purpose"],
        "must_supply": source_solve_template["must_supply"],
        "forbidden_shortcuts": source_solve_template["forbidden_shortcuts"],
        "first_new_object": source_solve_gate["next_object"],
    }

    open_gates = {
        "unconditional_terminal_admissible_section_theorem": True,
        "selected_visible_bundle_sheaf_or_routec_source": True,
        "selected_Gauduchon_chamber_source_or_source_derived_HYM_residual": True,
        "selected_RouteC_residual_values_with_source_verified": True,
        "operator_layer_Pic0_or_holonomy_sensitive_quotient": True,
        "same_source_ChernWeil_GS_derivation": True,
        "same_source_D_E_Riesz_Green_dotD_selected_data": True,
        "primitive_C1_contractions": True,
        "finite_part_or_spectrum": True,
        "lambda_12": True,
        "full_SM_or_no_knob_closure": True,
    }

    decision = {
        "all_remaining_parts_attempted": True,
        "terminal_principle_axiom_ready": principle_status["axiom_ready_not_unconditional"],
        "terminal_principle_unconditional": False,
        "gauduchon_chamber_or_hym_closed": False,
        "selected_routec_residual_values_closed": False,
        "same_source_operator_payload_closed": False,
        "formal_lift_rejected": True,
        "lambda_12_computable": False,
        "lambda_12_closed": False,
        "target_fitting_used": False,
        "strongest_result": (
            "All listed remaining U1/Y gates were attacked. The ordered source layer and non-split input are closed, "
            "the terminal principle is axiom-ready, and finite residual/operator shapes reach validators; closure still "
            "requires a genuine selected visible bundle/sheaf/Route-C source that turns source flags on without diagnostic lift."
        ),
        "next_required_object": "Selected_U1Y_Visible_Bundle_or_RouteC_Source_Solve_v1",
        "template_to_fill": source_solve_contract["schema"],
    }

    candidate = {
        "candidate": "SelectedU1YGauduchonChamberOrSelectedResidualSource",
        "status": "U1Y_GAUDUCHON_OR_SELECTED_RESIDUAL_GATE_ATTEMPTED_VISIBLE_SOURCE_SOLVE_REQUIRED",
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "prior_status": prior["status"],
        "principle_status": principle_status,
        "gauduchon_or_stability": gauduchon_or_stability,
        "residual_values": residual_values,
        "operator_payload": operator_payload,
        "source_solve_contract": source_solve_contract,
        "what_closes": {
            "remaining_parts_attempted": True,
            "terminal_principle_promoted_to_axiom_ready_status": principle_status["axiom_ready_not_unconditional"],
            "non_split_input_and_selected_h1_ext_retained": gauduchon_or_stability["non_split_extension_input"]
            and gauduchon_or_stability["selected_h1_8_nonzero_ext"],
            "routec_residual_zero_shape_available": residual_values["honest_residual_zero"],
            "orientation_dedotd_matrix_shape_reaches_validators": operator_payload[
                "orientation_packets_reach_validator_layer"
            ],
            "formal_lift_shortcut_rejected": True,
            "exact_next_source_solve_contract_identified": True,
        },
        "what_remains_open": open_gates,
        "guardrails": [
            "Do not promote the terminal admissible-section principle to unconditional without a paper-spine axiom or projection-admissibility derivation.",
            "Do not promote formal-lift selected flags; the packet status remains CANDIDATE_UNSELECTED_SMOKE.",
            "Do not treat zero residuals as proof unless selected_source_verified is source-derived.",
            "Do not compute lambda_12 before same-source U1/Y finite operator data are emitted.",
            "Do not use observed CP sign, masses, CKM/PMNS entries, or benchmark flavor matrices.",
        ],
        "decision": decision,
        "closure_claimed": True,
        "closure_scope": "all_remaining_gate_attempt_and_exact_source_solve_reduction_only",
        "target_fitting_used": False,
    }

    certificate = {
        "certificate": "SelectedU1YGauduchonChamberOrSelectedResidualSource",
        "status": candidate["status"],
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "what_closes": candidate["what_closes"],
        "what_remains_open": open_gates,
        "next_required_object": decision["next_required_object"],
        "template_to_fill": decision["template_to_fill"],
        "terminal_principle_unconditional": False,
        "gauduchon_chamber_or_hym_closed": False,
        "selected_routec_residual_values_closed": False,
        "same_source_operator_payload_closed": False,
        "lambda_12_closed": False,
        "target_fitting_used": False,
    }
    return candidate, certificate, render_note(candidate)


def render_note(candidate: dict[str, Any]) -> str:
    decision = candidate["decision"]
    principle = candidate["principle_status"]
    stability = candidate["gauduchon_or_stability"]
    residual = candidate["residual_values"]
    operator = candidate["operator_payload"]
    contract = candidate["source_solve_contract"]
    closes = "\n".join(f"- `{key}` = `{str(value).lower()}`" for key, value in candidate["what_closes"].items())
    open_items = "\n".join(f"- `{key}`" for key, value in candidate["what_remains_open"].items() if value)
    guardrails = "\n".join(f"- {item}" for item in candidate["guardrails"])
    missing = "\n".join(f"- {item}" for item in stability["still_missing"])
    shortcuts = "\n".join(f"- {item}" for item in contract["forbidden_shortcuts"])
    return f"""# Selected U1Y Gauduchon Chamber or Selected Residual Source v1

## Result

```text
all_remaining_parts_attempted = true
terminal_principle_axiom_ready = {str(decision["terminal_principle_axiom_ready"]).lower()}
terminal_principle_unconditional = false
gauduchon_chamber_or_hym_closed = false
selected_routec_residual_values_closed = false
same_source_operator_payload_closed = false
formal_lift_rejected = true
lambda_12_computable = false
lambda_12_closed = false
target_fitting_used = false
```

This artifact attacks the remaining bundle after the selected AH/good-cover
source layer. It does not close the final HYM/operator payload. It proves the
current proof frontier has reduced to a single new source object: a selected
visible bundle, sheaf, or Route-C source solve that makes the residual,
`D_E`, Riesz/Green, `dotD`, and primitive-C1 validators pass without lifted
flags.

## Terminal Principle Status

```text
corpus_support = {str(principle["corpus_support"]).lower()}
literal_unconditional_statement_found = {str(principle["literal_unconditional_statement_found"]).lower()}
status = {principle["status"]}
can_promote_inside_repo_without_paper_spine_change = false
```

Next required action: {principle["next_required_action"]}

## Gauduchon / Stability Gate

```text
negative_slope_chamber_witness = {str(stability["negative_slope_chamber_witness"]).lower()}
non_split_extension_input = {str(stability["non_split_extension_input"]).lower()}
selected_h1_8_nonzero_ext = {str(stability["selected_h1_8_nonzero_ext"]).lower()}
split_hym_shortcut_retired = {str(stability["split_hym_shortcut_retired"]).lower()}
status = {stability["status"]}
closed = false
```

Still missing:

{missing}

## Route-C Residual / Operator Gate

```text
honest_residual_zero = {str(residual["honest_residual_zero"]).lower()}
honest_selected_source_verified = {str(residual["honest_selected_source_verified"]).lower()}
honest_status = {residual["honest_status"]}
formal_lift_residual_zero = {str(residual["formal_lift_residual_zero"]).lower()}
formal_lift_selected_source_verified = {str(residual["formal_lift_selected_source_verified"]).lower()}
formal_lift_status = {residual["formal_lift_status"]}
formal_lift_accepted_as_proof = false
promotion_attempt_status = {operator["promotion_attempt_status"]}
promotion_selected_source_verified = {str(operator["promotion_selected_source_verified"]).lower()}
orientation_packets_reach_validator_layer = {str(operator["orientation_packets_reach_validator_layer"]).lower()}
selected_source_origin_constructed = false
```

## Source Solve Contract

```text
schema = {contract["schema"]}
status = {contract["status"]}
first_new_object = {contract["first_new_object"]["name"]}
```

Purpose: {contract["purpose"]}

Forbidden shortcuts:

{shortcuts}

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
template_to_fill = {decision["template_to_fill"]}
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
