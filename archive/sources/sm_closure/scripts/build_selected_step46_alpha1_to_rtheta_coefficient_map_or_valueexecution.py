"""Build Step46 selected alpha1-to-Rtheta coefficient map.

This is the constructive object after Step45.  It binds the admitted alpha1
source anchor to the selected Rtheta coefficient skeleton and threshold
response contract.  The result is a typed ten-row map, not a fitted numerical
table: observed/replay values are postchecks only, and row values are accepted
only when the selected threshold/profile/magnitude-bearing arguments exist.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step46_alpha1_to_rtheta_coefficient_map_or_valueexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
MAP_PACKET = PACKET_DIR / "step46_selected_alpha1_to_rtheta_coefficient_map.packet.json"
ARGUMENT_AUDIT = PACKET_DIR / "step46_map_argument_closure_audit.packet.json"
VALUE_ATTEMPT = PACKET_DIR / "step46_value_execution_attempt.packet.json"
NEXT_FRONTIER = PACKET_DIR / "step46_next_value_execution_frontier.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step46_Alpha1ToRThetaCoefficientMap_or_ValueExecution_v1.md"

STEP45 = DATA / "selected_step45_alpha1rthetarow_execution_attempt_or_coefficientmapfrontier.candidate.json"
ANCHOR = (
    DATA
    / "selected_step44_alpha1universalanchor_admission_or_rthetarowexecution"
    / "step44_alpha1_source_anchor_admission.packet.json"
)
COEFF_FUNCTIONAL = (
    DATA
    / "selected_rtheta_coefficientfunctional_or_universalanchorselection"
    / "rtheta_coefficient_functional_skeleton.packet.json"
)
EVALUATOR_GATE = (
    DATA
    / "selected_rtheta_valueevaluatorexecution_or_thresholdresponseinstantiation"
    / "rtheta_value_evaluator_execution_gate.packet.json"
)
THRESHOLD_CONTRACT = (
    DATA
    / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition"
    / "selected_threshold_response_functional_contract.packet.json"
)
HIGHER_CONTRACT = (
    DATA
    / "selected_higherresponserthetafunctional_or_sourceanchortheorem"
    / "rtheta_higher_response_functional_contract.packet.json"
)
MAGNITUDE_DECISION = (
    DATA
    / "selected_magnitudebearingprojectionweights_or_thresholdrowsderivation"
    / "magnitude_weights_or_threshold_rows_decision.packet.json"
)
SAMEBRANCH_GAP = (
    DATA
    / "selected_samebranchthresholdmassschemerows_or_sourceanchorconstruction"
    / "same_branch_internal_source_row_gap.packet.json"
)
STEP42_VALUE = (
    DATA
    / "selected_step42_executable_value_replay_solution_or_noknobrowfrontier"
    / "step42_executable_value_replay_solution.packet.json"
)

STATUS = "MTT_SELECTED_STEP46_ALPHA1_TO_RTHETA_COEFFICIENT_MAP_CONSTRUCTED_VALUE_EXECUTION_OPEN"
NEXT = "MTT_Selected_Alpha1RThetaMapArgumentFill_or_InternalValueRows_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def replay_lookup(value_rows: dict[str, Any]) -> dict[str, float]:
    lookup: dict[str, float] = {}
    for sector, key in [("u", "diag_abs_Y_u"), ("d", "diag_abs_Y_d"), ("e", "diag_abs_Y_e")]:
        for generation, value in enumerate(value_rows[key], start=1):
            lookup[f"theta_coeff.{sector}.gen{generation}"] = value
    lookup["lambda_H"] = value_rows["lambda_H"]
    return lookup


def row_formula(row: dict[str, Any], anchor_name: str) -> str:
    return (
        f"{row['coefficient_slot']} = Rtheta_alpha1("
        f"anchor={anchor_name}, Pi_Rtheta, projector={row['spectral_projector_ref']}, "
        f"family_eigenvalue={row['family_eigenvalue']}, "
        f"sector={row['sector']}, threshold_mass_profile_arg=Xi_{row['sector']}.gen{row['generation']})"
    )


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [
        STEP45,
        ANCHOR,
        COEFF_FUNCTIONAL,
        EVALUATOR_GATE,
        THRESHOLD_CONTRACT,
        HIGHER_CONTRACT,
        MAGNITUDE_DECISION,
        SAMEBRANCH_GAP,
        STEP42_VALUE,
    ]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step46 inputs: " + ", ".join(missing))

    step45 = load(STEP45)
    anchor_packet = load(ANCHOR)
    coeff = load(COEFF_FUNCTIONAL)
    evaluator = load(EVALUATOR_GATE)
    threshold_contract = load(THRESHOLD_CONTRACT)
    higher_contract = load(HIGHER_CONTRACT)
    magnitude = load(MAGNITUDE_DECISION)
    samebranch_gap = load(SAMEBRANCH_GAP)
    step42_value = load(STEP42_VALUE)

    anchor = anchor_packet["anchor"]
    map_domain_closed = (
        step45["closure_decision"]["alpha1_source_anchor_imported_into_Rtheta_gate"] is True
        and anchor_packet["admitted_at_source_tier"] is True
        and evaluator["Pi_Rtheta_closed"] is True
        and evaluator["coefficient_functional_skeleton_closed"] is True
        and coeff["coefficient_functional_readiness_closed"] is True
        and threshold_contract["closure_claimed"] is True
        and higher_contract["contract_closed"] is True
    )

    argument_closure = {
        "alpha1_source_anchor": True,
        "Pi_Rtheta": evaluator["Pi_Rtheta_closed"],
        "coefficient_functional_skeleton": coeff["coefficient_functional_readiness_closed"],
        "threshold_response_contract": threshold_contract["closure_claimed"],
        "higher_response_ten_row_codomain": higher_contract["contract_closed"],
        "magnitude_bearing_projection_weights": evaluator["magnitude_bearing_projection_weights_closed"],
        "selected_threshold_response_instantiation": evaluator[
            "selected_threshold_response_functional_instantiated"
        ],
        "generation_resolved_threshold_source_rows": magnitude[
            "generation_resolved_threshold_source_rows_closed"
        ],
        "selected_internal_threshold_mass_derivation": samebranch_gap[
            "selected_internal_Rtheta_threshold_mass_derivation_closed"
        ],
    }
    map_arguments_closed = all(argument_closure.values())

    replay_values = replay_lookup(step42_value["value_rows"])
    charged_rows = []
    for row in coeff["charged_functional_rows"]:
        slot = row["coefficient_slot"]
        charged_rows.append(
            {
                "row_id": row["row_id"],
                "coefficient_slot": slot,
                "sector": row["sector"],
                "generation": row["generation"],
                "spectral_projector_ref": row["spectral_projector_ref"],
                "family_eigenvalue": row["family_eigenvalue"],
                "map_formula": row_formula(row, anchor["name"]),
                "required_unfilled_argument": f"Xi_{row['sector']}.gen{row['generation']}",
                "admitted_replay_postcheck_value": replay_values[slot],
                "accepted_as_internal_value_row": False,
            }
        )
    higgs_row = {
        "row_id": "lambda_H.alpha1_rtheta_map",
        "coefficient_slot": "lambda_H",
        "sector": "H",
        "generation": None,
        "spectral_projector_ref": "H.P_scalar",
        "family_eigenvalue": None,
        "map_formula": (
            f"lambda_H = Rtheta_alpha1(anchor={anchor['name']}, Pi_Rtheta, "
            "Higgs_projector=H.P_scalar, threshold_mass_profile_arg=Xi_H.lambda)"
        ),
        "required_unfilled_argument": "Xi_H.lambda",
        "admitted_replay_postcheck_value": replay_values["lambda_H"],
        "accepted_as_internal_value_row": False,
    }

    selected_map = {
        "schema": "MTTStep46SelectedAlpha1ToRThetaCoefficientMap.v1",
        "status": "SELECTED_ALPHA1_TO_RTHETA_MAP_CONSTRUCTED_VALUES_OPEN",
        "map_symbol": "Rtheta_alpha1",
        "source_anchor": {
            "name": anchor["name"],
            "lambda_alpha1": anchor["lambda_alpha1"],
            "N_alpha1_h_ext": anchor["N_alpha1_h_ext"],
            "du_dalpha1_equals_h_ext": anchor["du_dalpha1_equals_h_ext"],
            "selected_dotD_source_verified": anchor["selected_dotD_source_verified"],
            "alpha1_driver_verified": anchor["alpha1_driver_verified"],
            "honest_dotD_alpha1_replay": anchor["honest_dotD_alpha1_replay"],
        },
        "map_domain_closed": map_domain_closed,
        "construction_rule": (
            "Rtheta_alpha1 is the unique typed composition of the admitted alpha1 source anchor, "
            "Pi_Rtheta, the selected family/projector coefficient skeleton, and the selected "
            "threshold-response codomain contract. It is constructed before comparing to Step42 "
            "values; Step42 rows are postchecks only."
        ),
        "charged_rows": charged_rows,
        "higgs_row": higgs_row,
        "codomain_row_count": len(charged_rows) + 1,
        "accepted_value_row_count": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": map_domain_closed,
    }
    write_json(MAP_PACKET, selected_map)

    missing_arguments = [key for key, value in argument_closure.items() if value is not True]
    argument_audit = {
        "schema": "MTTStep46MapArgumentClosureAudit.v1",
        "status": "MAP_CONSTRUCTED_EXECUTION_ARGUMENTS_OPEN",
        "argument_closure": argument_closure,
        "map_domain_closed": map_domain_closed,
        "all_value_execution_arguments_closed": map_arguments_closed,
        "missing_arguments": missing_arguments,
        "why_values_do_not_execute": [
            "the map exists as a typed selected composition",
            "magnitude-bearing Xi_s,g arguments are not selected",
            "selected threshold-response instantiation is still false",
            "same-branch internal threshold/mass derivation is still false",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(ARGUMENT_AUDIT, argument_audit)

    accepted_rows = charged_rows + [higgs_row] if map_arguments_closed else []
    value_attempt = {
        "schema": "MTTStep46ValueExecutionAttempt.v1",
        "status": "VALUE_EXECUTION_ATTEMPTED_ZERO_ROWS_ACCEPTED",
        "selected_map_constructed": map_domain_closed,
        "all_value_execution_arguments_closed": map_arguments_closed,
        "accepted_internal_value_rows": accepted_rows,
        "accepted_internal_value_row_count": len(accepted_rows),
        "accepted_charged_coefficient_row_count": len(charged_rows) if map_arguments_closed else 0,
        "lambda_H_internal_row_closed": map_arguments_closed,
        "postcheck_values_available": True,
        "postcheck_values_used_as_selectors": False,
        "minimal_parameter_closure_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(VALUE_ATTEMPT, value_attempt)

    next_frontier = {
        "schema": "MTTStep46NextValueExecutionFrontier.v1",
        "status": "MAP_CLOSED_FILL_ARGUMENTS_NEXT",
        "closed_now": {
            "selected_alpha1_to_Rtheta_coefficient_map": map_domain_closed,
            "alpha1_anchor_bound_to_Rtheta_gate": True,
            "ten_row_codomain_ledger_constructed": True,
            "Step42_values_classified_as_postchecks": True,
        },
        "still_open": {
            "magnitude_bearing_Xi_sg_arguments": True,
            "selected_threshold_response_instantiation": True,
            "same_branch_internal_threshold_mass_derivation": True,
            "accepted_internal_value_rows": True,
            "minimal_parameter_closure": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(NEXT_FRONTIER, next_frontier)

    candidate = {
        "candidate": "MTTSelectedStep46Alpha1ToRThetaCoefficientMapOrValueExecution",
        "status": STATUS,
        "inputs": {
            "step45": rel(STEP45),
            "anchor": rel(ANCHOR),
            "coefficient_functional": rel(COEFF_FUNCTIONAL),
            "evaluator_gate": rel(EVALUATOR_GATE),
            "threshold_contract": rel(THRESHOLD_CONTRACT),
            "higher_contract": rel(HIGHER_CONTRACT),
            "magnitude_decision": rel(MAGNITUDE_DECISION),
            "samebranch_gap": rel(SAMEBRANCH_GAP),
            "step42_value": rel(STEP42_VALUE),
        },
        "output_packets": {
            "selected_alpha1_to_rtheta_coefficient_map": rel(MAP_PACKET),
            "map_argument_closure_audit": rel(ARGUMENT_AUDIT),
            "value_execution_attempt": rel(VALUE_ATTEMPT),
            "next_value_execution_frontier": rel(NEXT_FRONTIER),
        },
        "theorem": {
            "name": "SelectedAlpha1ToRThetaCoefficientMapConstructionTheorem",
            "proved": map_domain_closed,
            "statement": (
                "The admitted alpha1 source anchor, Pi_Rtheta, selected coefficient skeleton, "
                "threshold-response contract, and ten-row higher-response codomain determine a typed "
                "selected coefficient map Rtheta_alpha1. This constructs the map without observed "
                "values as selectors. It does not emit numerical rows until the magnitude-bearing "
                "threshold/profile arguments Xi_s,g and Xi_H are selected."
            ),
        },
        "closure_decision": {
            "selected_alpha1_to_Rtheta_coefficient_map_constructed": map_domain_closed,
            "all_value_execution_arguments_closed": map_arguments_closed,
            "accepted_internal_Rtheta_coefficient_row_count": len(charged_rows) if map_arguments_closed else 0,
            "accepted_internal_scalar_row_count": len(accepted_rows),
            "selected_lambda_H_row_closed": map_arguments_closed,
            "minimal_parameter_closure_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": map_domain_closed,
        "minimal_parameter_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step46_Alpha1ToRThetaCoefficientMap_or_ValueExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        **candidate["closure_decision"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected Step46 Alpha1ToRThetaCoefficientMap or ValueExecution v1

Status: `{STATUS}`.

Constructed map:

`Rtheta_alpha1`

```text
selected alpha1 -> Rtheta coefficient map constructed : {str(map_domain_closed).lower()}
ten-row codomain ledger constructed                   : true
all value-execution arguments closed                  : {str(map_arguments_closed).lower()}
accepted internal charged coefficient rows            : {value_attempt["accepted_charged_coefficient_row_count"]}
selected lambda_H internal row                        : {str(map_arguments_closed).lower()}
```

This closes the map-construction blocker. It does not close numerical value
execution: the unfilled arguments are `{", ".join(missing_arguments)}`.

Step42 values are retained only as postchecks. They do not select the map,
the branch, or any coefficient row.

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
