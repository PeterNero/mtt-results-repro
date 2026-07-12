"""Build Step 45 alpha1-to-Rtheta row execution attempt.

Step44 admitted alpha1 as a one-universal source anchor at the source/operator
tier.  This builder reruns the Rtheta scalar-row gate with that fact imported,
so the active blocker is no longer "no universal anchor selected".  It remains
strict: alpha1 may normalize the selected source branch, but it does not become
a value row unless the selected Rtheta coefficient evaluator is supplied.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step45_alpha1rthetarow_execution_attempt_or_coefficientmapfrontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ANCHOR_IMPORT = PACKET_DIR / "step45_alpha1_anchor_import_into_rtheta_gate.packet.json"
ROW_ATTEMPT = PACKET_DIR / "step45_alpha1_to_rtheta_row_execution_attempt.packet.json"
COEFF_MAP_FRONTIER = PACKET_DIR / "step45_selected_coefficient_map_frontier.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step45_Alpha1RThetaRowExecutionAttempt_or_CoefficientMapFrontier_v1.md"

STEP44 = DATA / "selected_step44_alpha1universalanchor_admission_or_rthetarowexecution.candidate.json"
STEP42_VALUE = (
    DATA
    / "selected_step42_executable_value_replay_solution_or_noknobrowfrontier"
    / "step42_executable_value_replay_solution.packet.json"
)
SOURCE_DOMAIN = (
    DATA
    / "selected_rthetascalarvaluefunctionalsource_or_noknobnumericalrows"
    / "rtheta_scalar_value_functional_source_packet.packet.json"
)
EVALUATOR_GATE = (
    DATA
    / "selected_rtheta_valueevaluatorexecution_or_thresholdresponseinstantiation"
    / "rtheta_value_evaluator_execution_gate.packet.json"
)
COEFF_FUNCTIONAL = (
    DATA
    / "selected_rtheta_coefficientfunctional_or_universalanchorselection"
    / "rtheta_coefficient_functional_skeleton.packet.json"
)
INTERNAL_ATTEMPT = DATA / "selected_internalrthetascalarrowemission_or_universalanchorselection.candidate.json"

STATUS = "MTT_SELECTED_STEP45_ALPHA1_RTHETA_ROW_EXECUTION_ATTEMPT_BUILT_ANCHOR_BLOCKER_RETIRED_COEFFICIENT_MAP_OPEN"
NEXT = "MTT_Selected_Alpha1ToRThetaCoefficientMap_or_InternalScalarRows_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def diag_rows(value_rows: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for sector, values_key in [("u", "diag_abs_Y_u"), ("d", "diag_abs_Y_d"), ("e", "diag_abs_Y_e")]:
        for index, value in enumerate(value_rows[values_key], start=1):
            rows.append(
                {
                    "row_id": f"{sector}.gen{index}.admitted_replay_value",
                    "coefficient_slot": f"theta_coeff.{sector}.gen{index}",
                    "sector": sector,
                    "generation": index,
                    "admitted_replay_value": value,
                    "accepted_as_internal_Rtheta_value": False,
                    "why_not_accepted": (
                        "Step42 value is an admitted replay/profile input. Step45 requires a "
                        "selected alpha1-to-Rtheta coefficient map before it can be promoted."
                    ),
                }
            )
    return rows


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [STEP44, STEP42_VALUE, SOURCE_DOMAIN, EVALUATOR_GATE, COEFF_FUNCTIONAL, INTERNAL_ATTEMPT]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step45 inputs: " + ", ".join(missing))

    step44 = load(STEP44)
    step42_value = load(STEP42_VALUE)
    source_domain = load(SOURCE_DOMAIN)
    evaluator_gate = load(EVALUATOR_GATE)
    coeff_functional = load(COEFF_FUNCTIONAL)
    internal_attempt = load(INTERNAL_ATTEMPT)

    step44_decision = step44["closure_decision"]
    source_anchor_imported = (
        step44_decision["alpha1_one_universal_source_anchor_admitted_at_source_tier"] is True
        and step44_decision["selected_universal_source_anchor_count_at_source_tier"] == 1
        and step44_decision["effective_fitted_parameter_count"] == 0
    )
    rtheta_domain_ready = (
        source_domain["source_domain_closed"] is True
        and evaluator_gate["Pi_Rtheta_closed"] is True
        and evaluator_gate["coefficient_functional_skeleton_closed"] is True
        and coeff_functional["coefficient_functional_readiness_closed"] is True
        and coeff_functional["charged_functional_row_count"] == 9
    )
    stale_no_anchor_blocker_retired = (
        source_anchor_imported
        and internal_attempt["closure_decision"]["universal_anchor_selected"] is False
        and internal_attempt["closure_decision"]["accepted_internal_scalar_row_count"] == 0
    )

    coefficient_map_closed = (
        evaluator_gate["selected_threshold_response_functional_instantiated"] is True
        and evaluator_gate["magnitude_bearing_projection_weights_closed"] is True
        and evaluator_gate["accepted_coefficient_value_count"] == 9
        and evaluator_gate["accepted_lambda_H_value"] is True
    )
    admitted_rows = diag_rows(step42_value["value_rows"])
    accepted_rows = admitted_rows if coefficient_map_closed else []

    anchor_import = {
        "schema": "MTTStep45Alpha1AnchorImportIntoRThetaGate.v1",
        "status": "ALPHA1_SOURCE_ANCHOR_IMPORTED_STALE_NO_ANCHOR_BLOCKER_RETIRED",
        "step44_source": rel(STEP44),
        "anchor_name": "alpha1_source_strength_anchor",
        "selected_source_anchor_count_after_import": 1,
        "selected_value_anchor_count": 0,
        "effective_fitted_parameter_count": 0,
        "source_anchor_imported_into_rtheta_gate": source_anchor_imported,
        "stale_no_universal_anchor_blocker_retired": stale_no_anchor_blocker_retired,
        "guardrail": (
            "The old direct-emission statement that no universal anchor is selected is superseded "
            "for the active branch. Alpha1 is still source-tier only; it is not a value fit."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(ANCHOR_IMPORT, anchor_import)

    row_attempt = {
        "schema": "MTTStep45Alpha1ToRThetaRowExecutionAttempt.v1",
        "status": "ALPHA1_TO_RTHETA_ROW_EXECUTION_ATTEMPTED_COEFFICIENT_MAP_OPEN",
        "rtheta_domain_ready": rtheta_domain_ready,
        "coefficient_functional_skeleton_closed": coeff_functional["coefficient_functional_readiness_closed"],
        "charged_functional_row_count": coeff_functional["charged_functional_row_count"],
        "alpha1_source_anchor_available": source_anchor_imported,
        "admitted_replay_rows_checked_as_postchecks": admitted_rows,
        "accepted_internal_Rtheta_row_count": len(accepted_rows),
        "accepted_internal_Rtheta_rows": accepted_rows,
        "lambda_H_replay_postcheck": step42_value["value_rows"]["lambda_H"],
        "lambda_H_accepted_as_internal_Rtheta_row": False,
        "coefficient_map_closed": coefficient_map_closed,
        "why_values_still_rejected": [
            "selected alpha1-to-Rtheta coefficient map is not emitted",
            "magnitude-bearing projection weights are not closed",
            "selected threshold response functional is not instantiated",
            "Step42 replay values remain postchecks, not selectors",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(ROW_ATTEMPT, row_attempt)

    frontier = {
        "schema": "MTTStep45SelectedCoefficientMapFrontier.v1",
        "status": "ONLY_SELECTED_COEFFICIENT_MAP_REMAINS_FOR_ONE_ANCHOR_ROW_CLOSURE",
        "closed_now": {
            "alpha1_source_anchor_imported_into_Rtheta_gate": source_anchor_imported,
            "stale_no_anchor_blocker_retired": stale_no_anchor_blocker_retired,
            "Rtheta_domain_and_coefficient_functional_available": rtheta_domain_ready,
            "admitted_replay_rows_demoted_to_postchecks": True,
        },
        "still_open": {
            "selected_alpha1_to_Rtheta_coefficient_map": True,
            "magnitude_bearing_projection_weights": True,
            "selected_threshold_response_functional_instantiation": True,
            "accepted_internal_Rtheta_coefficient_rows": True,
            "lambda_H_internal_row": True,
            "minimal_parameter_closure": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "minimal_next_theorem": {
            "name": "SelectedAlpha1ToRThetaCoefficientMapTheorem",
            "statement": (
                "For each selected family projector row P_s,g, derive the coefficient value "
                "theta_coeff.s.gen from the same alpha1-normalized source branch through Rtheta, "
                "then use Step42 rows only as postchecks."
            ),
            "required_outputs": [
                "nine charged coefficient values",
                "one lambda_H row",
                "proof that no observed value selected the map",
                "comparison residuals against Step42 as validation only",
            ],
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(COEFF_MAP_FRONTIER, frontier)

    candidate = {
        "candidate": "MTTSelectedStep45Alpha1RThetaRowExecutionAttemptOrCoefficientMapFrontier",
        "status": STATUS,
        "inputs": {
            "step44": rel(STEP44),
            "step42_value": rel(STEP42_VALUE),
            "source_domain": rel(SOURCE_DOMAIN),
            "evaluator_gate": rel(EVALUATOR_GATE),
            "coefficient_functional": rel(COEFF_FUNCTIONAL),
            "internal_attempt": rel(INTERNAL_ATTEMPT),
        },
        "output_packets": {
            "alpha1_anchor_import_into_rtheta_gate": rel(ANCHOR_IMPORT),
            "alpha1_to_rtheta_row_execution_attempt": rel(ROW_ATTEMPT),
            "selected_coefficient_map_frontier": rel(COEFF_MAP_FRONTIER),
        },
        "theorem": {
            "name": "Step45Alpha1RThetaGateContractionTheorem",
            "proved": stale_no_anchor_blocker_retired and rtheta_domain_ready,
            "statement": (
                "After Step44, the active Rtheta scalar-row gate can no longer cite lack of a "
                "universal source anchor as the blocker. The alpha1 source anchor is imported into "
                "the selected Rtheta gate, while value rows remain open until the selected "
                "alpha1-to-Rtheta coefficient map emits magnitude-bearing rows."
            ),
        },
        "closure_decision": {
            "alpha1_source_anchor_imported_into_Rtheta_gate": source_anchor_imported,
            "stale_no_universal_anchor_blocker_retired": stale_no_anchor_blocker_retired,
            "Rtheta_domain_and_coefficient_functional_ready": rtheta_domain_ready,
            "selected_alpha1_to_Rtheta_coefficient_map_closed": coefficient_map_closed,
            "accepted_internal_Rtheta_coefficient_row_count": len(accepted_rows),
            "accepted_internal_scalar_row_count": len(accepted_rows),
            "selected_lambda_H_row_closed": False,
            "minimal_parameter_closure_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": stale_no_anchor_blocker_retired and rtheta_domain_ready,
        "minimal_parameter_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step45_Alpha1RThetaRowExecutionAttempt_or_CoefficientMapFrontier_v1",
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
        f"""# MTT Selected Step45 Alpha1RThetaRowExecutionAttempt or CoefficientMapFrontier v1

Status: `{STATUS}`.

Step45 imports the Step44 `alpha1_source_strength_anchor` into the active
`Rtheta` scalar-row gate.

```text
alpha1 source anchor imported into Rtheta gate : {str(source_anchor_imported).lower()}
stale no-anchor blocker retired                : {str(stale_no_anchor_blocker_retired).lower()}
Rtheta domain/coefficient functional ready      : {str(rtheta_domain_ready).lower()}
accepted internal Rtheta coefficient rows       : {len(accepted_rows)}
lambda_H internal row closed                    : false
```

This is progress, but it is not minimal-parameter value closure. The admitted
Step42 value rows are now explicit postchecks only. The live missing theorem is:

`{NEXT}`

It must derive the nine charged coefficient values and `lambda_H` from the
same alpha1-normalized selected branch through `Rtheta`, with observed values
used only after the fact for validation.
""",
        encoding="utf-8",
    )

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
