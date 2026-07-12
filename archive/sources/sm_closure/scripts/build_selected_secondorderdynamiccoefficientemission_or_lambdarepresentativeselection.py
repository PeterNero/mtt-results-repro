"""Build second-order dynamic coefficient emission / lambda representative gate.

The selected static coefficient orbit gives two representatives, but the current
dynamic first-response packets do not carry them.  This artifact identifies the
exact second-order rows required to promote the lambda lift dynamically:

    phase correction: lambda_static * Z on u/e
    shift correction: lambda_static * X on d/nuD

The current selected Phi_fin/C1 payload inventory has support shapes but zero
accepted dynamic payload rows, so these second-order coefficient rows are not
yet emitted.  This is a blocked-emission theorem with a precise next cutset, not
a full closure theorem.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_secondorderdynamiccoefficientemission_or_lambdarepresentativeselection"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
REQUIRED_ROWS = PACKET_DIR / "second_order_coefficient_required_rows.packet.json"
EMISSION_ATTEMPT = PACKET_DIR / "second_order_dynamic_emission_attempt.packet.json"
REPRESENTATIVE_DECISION = PACKET_DIR / "lambda_representative_selection_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_second_order_dynamic_coefficient_attempt.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_SecondOrderDynamicCoefficientEmission_or_LambdaRepresentativeSelection_v1.md"

DYNAMIC_ORIENTATION = DATA / "selected_dynamicorientation_or_physicalmatrixpromotion.candidate.json"
STATIC_ORBIT = (
    DATA
    / "selected_staticlambdaorbitquotient_or_dynamicorientationfrontier"
    / "selected_static_lambda_orbit.packet.json"
)
COEFF_SEARCH = (
    DATA
    / "selected_postsourceweylcoefficientlift_or_secondorderflavorcandidate"
    / "minimal_weyl_coefficient_lift_search.packet.json"
)
FORMAL110 = (
    DATA
    / "selected_postsourceformal110_observableaudit_or_fullsmgap"
    / "formal110_sector_matrix_observables.packet.json"
)
PAYLOAD_INVENTORY = (
    DATA
    / "selected_dynamicphifinc1payloadrows_or_higherresponseexecution"
    / "dynamic_phifin_c1_payload_row_inventory.packet.json"
)
PAYLOAD_RECONCILIATION = (
    DATA
    / "selected_dynamicphifinc1payloadrows_or_higherresponseexecution"
    / "support_vs_selected_payload_reconciliation.packet.json"
)
HIGHER_ATTEMPT = (
    DATA
    / "selected_dynamicphifinc1payloadrows_or_higherresponseexecution"
    / "higher_response_execution_attempt_after_payload_inventory.packet.json"
)

STATUS = "MTT_SELECTED_SECONDORDER_DYNAMIC_COEFFICIENT_EMISSION_BUILT_REQUIRED_ROWS_IDENTIFIED_EMISSION_OPEN"
NEXT = "MTT_Selected_PureWeylCoefficientRows_or_PrimitiveC1FormulaExecution_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def inventory_by_row(inventory: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {row["row_id"]: row for row in inventory["rows"]}


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    dynamic_orientation = load(DYNAMIC_ORIENTATION)
    static_orbit = load(STATIC_ORBIT)
    coeff_search = load(COEFF_SEARCH)
    formal110 = load(FORMAL110)
    inventory = load(PAYLOAD_INVENTORY)
    reconciliation = load(PAYLOAD_RECONCILIATION)
    higher_attempt = load(HIGHER_ATTEMPT)
    rows_by_id = inventory_by_row(inventory)

    required_payload_rows = [
        "zero_mode_bases",
        "finite_Hessian_C1_source",
        "primitive_C1_contractions",
    ]
    required_row_status = {
        row_id: {
            "support_candidate_present": rows_by_id[row_id]["support_candidate_present"],
            "accepted_as_dynamic_phifin_c1_payload_row": rows_by_id[row_id][
                "accepted_as_dynamic_phifin_c1_payload_row"
            ],
            "reason": rows_by_id[row_id]["reason"],
        }
        for row_id in required_payload_rows
    }
    all_required_rows_accepted = all(
        item["accepted_as_dynamic_phifin_c1_payload_row"] for item in required_row_status.values()
    )

    required = {
        "schema": "MTTSecondOrderCoefficientRequiredRows.v1",
        "status": "PURE_WEYL_COEFFICIENT_ROWS_IDENTIFIED",
        "static_lambda_orbit": static_orbit["selected_static_lambda_orbit"],
        "first_response_rows": {
            "phase_first_response": "I + Z on u,e",
            "shift_first_response": "I + X on d,nuD",
            "formal110_twofold_degeneracy": formal110["global_observable_decision"][
                "twofold_degeneracy_remains_all_sectors"
            ],
        },
        "second_order_rows_required": {
            "phase_coefficient_row": "lambda_static * Z on u,e",
            "shift_coefficient_row": "lambda_static * X on d,nuD",
            "same_source_rule": "same lambda_static on phase and shift legs",
            "orbit_representatives": static_orbit["selected_static_lambda_orbit"],
        },
        "dynamic_payload_rows_required": required_payload_rows,
        "dynamic_payload_row_status": required_row_status,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(REQUIRED_ROWS, required)

    emission_attempt = {
        "schema": "MTTSecondOrderDynamicCoefficientEmissionAttempt.v1",
        "status": "EMISSION_BLOCKED_SELECTED_DYNAMIC_PAYLOAD_ROWS_ABSENT",
        "accepted_dynamic_payload_row_count": inventory["accepted_dynamic_payload_row_count"],
        "support_candidate_present_count": inventory["support_candidate_present_count"],
        "all_support_shapes_present": inventory["all_support_shapes_present"],
        "higher_response_execution_inputs_available": inventory[
            "higher_response_execution_inputs_available"
        ],
        "primitive_row_formula_executed": reconciliation["primitive_row_formula_executed"],
        "same_source_dynamic_payload_closed": reconciliation["same_source_dynamic_payload_closed"],
        "selected_functional_executed": higher_attempt["selected_functional_executed"],
        "all_required_rows_accepted": all_required_rows_accepted,
        "second_order_coefficient_rows_emitted": False,
        "why_blocked": [
            "zero-mode bases are not emitted as selected dynamic payload values",
            "finite Hessian/C1 source blocks are support-only",
            "primitive C1 contractions and sector response matrices are absent",
            "higher-response execution is blocked by dynamic payload rows",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(EMISSION_ATTEMPT, emission_attempt)

    surviving_branches = [
        branch
        for branch in coeff_search["branches"]
        if branch["branch_id"] in static_orbit["survivor_branch_ids"]
    ]
    representative_decision = {
        "schema": "MTTLambdaRepresentativeSelectionDecision.v1",
        "status": "STATIC_ORBIT_RETAINED_NO_DYNAMIC_REPRESENTATIVE_SELECTED",
        "survivor_branch_ids": static_orbit["survivor_branch_ids"],
        "surviving_lambdas": static_orbit["selected_static_lambda_orbit"],
        "candidate_physical_signatures": [
            {
                "branch_id": branch["branch_id"],
                "lambda_static": branch["phase_additive_lambda"],
                "hermitian_spectrum_each_sector": branch["hermitian_spectrum_each_sector"],
                "cp_odd_exact_magnitude": branch["cp_odd_exact_magnitude"],
                "cp_odd_orientation": branch["cp_odd_orientation"],
            }
            for branch in surviving_branches
        ],
        "individual_lambda_selected": False,
        "coexistence_or_equivalence_proved": False,
        "selected_second_order_physical_matrix_promoted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(REPRESENTATIVE_DECISION, representative_decision)

    cutset = {
        "schema": "MTTNextCutsetAfterSecondOrderDynamicCoefficientAttempt.v1",
        "status": "NEXT_ATTACK_PURE_WEYL_COEFFICIENT_ROWS_OR_PRIMITIVE_C1_FORMULA",
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "The required pure Weyl coefficient rows are now identified, but current dynamic "
                "Phi_fin/C1 payload rows do not emit them.  The next artifact must execute the "
                "primitive C1 row formula or zero-mode/Hessian payload enough to emit lambda_static*Z/X."
            ),
        },
        "minimal_tasks": [
            "emit selected zero-mode basis values for the q79/F,m=1 source branch",
            "execute finite Hessian C1 source blocks in the selected dynamic payload",
            "compute primitive C1 contractions that isolate pure Z and pure X coefficient rows",
            "rerun lambda representative/coexistence and physical matrix promotion only after these rows exist",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedSecondOrderDynamicCoefficientEmissionOrLambdaRepresentativeSelection",
        "status": STATUS,
        "inputs": {
            "dynamic_orientation_candidate": rel(DYNAMIC_ORIENTATION),
            "selected_static_lambda_orbit": rel(STATIC_ORBIT),
            "coefficient_search": rel(COEFF_SEARCH),
            "formal110_observables": rel(FORMAL110),
            "dynamic_payload_inventory": rel(PAYLOAD_INVENTORY),
            "support_vs_selected_payload_reconciliation": rel(PAYLOAD_RECONCILIATION),
            "higher_response_execution_attempt": rel(HIGHER_ATTEMPT),
        },
        "output_packets": {
            "second_order_coefficient_required_rows": rel(REQUIRED_ROWS),
            "second_order_dynamic_emission_attempt": rel(EMISSION_ATTEMPT),
            "lambda_representative_selection_decision": rel(REPRESENTATIVE_DECISION),
            "next_cutset_after_second_order_dynamic_coefficient_attempt": rel(CUTSET),
        },
        "theorem": {
            "name": "SecondOrderDynamicCoefficientEmissionFrontierTheorem",
            "proved": inventory["accepted_dynamic_payload_row_count"] == 0
            and all_required_rows_accepted is False
            and higher_attempt["selected_functional_executed"] is False,
            "statement": (
                "The selected static lambda orbit requires second-order pure Weyl coefficient rows "
                "lambda_static*Z and lambda_static*X beyond the first-response I+Z/I+X packets. "
                "The current dynamic Phi_fin/C1 payload inventory contains support shapes but zero "
                "accepted dynamic payload rows, with zero-mode bases, finite Hessian C1 source blocks, "
                "and primitive C1 contractions still unexecuted.  Therefore no individual lambda "
                "representative or second-order physical matrix is selected now."
            ),
        },
        "what_closes_now": {
            "pure_Z_X_coefficient_rows_identified": True,
            "second_order_dynamic_emission_attempted": True,
            "blocking_dynamic_payload_rows_named": True,
            "lambda_representative_selection_kept_open_without_overclaim": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_zero_mode_basis_values": True,
            "selected_finite_Hessian_C1_source_blocks": True,
            "primitive_C1_contractions": True,
            "pure_Weyl_coefficient_rows_lambda_Z_lambda_X": True,
            "individual_lambda_representative_selection_or_coexistence": True,
            "selected_second_order_physical_matrix_promotion": True,
            "accepted_Yukawa_CKM_PMNS_RG_threshold_value_rows": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "closure_decision": {
            "second_order_coefficient_rows_emitted": False,
            "individual_lambda_value_selected": False,
            "selected_second_order_physical_matrices_promoted": False,
            "accepted_value_layer_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": dynamic_orientation["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_SecondOrderDynamicCoefficientEmission_or_LambdaRepresentativeSelection_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": candidate["theorem"]["proved"],
        "pure_Z_X_coefficient_rows_identified": True,
        "accepted_dynamic_payload_row_count": inventory["accepted_dynamic_payload_row_count"],
        "second_order_coefficient_rows_emitted": False,
        "individual_lambda_value_selected": False,
        "selected_second_order_physical_matrices_promoted": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected SecondOrderDynamicCoefficientEmission or LambdaRepresentativeSelection v1

Status: `{STATUS}`.

The selected static lambda orbit requires pure Weyl coefficient rows:

```text
phase correction : lambda_static * Z on u,e
shift correction : lambda_static * X on d,nuD
lambda orbit     : {static_orbit["selected_static_lambda_orbit"]}
```

Current dynamic payload status:

```text
support shapes present            : {str(inventory["all_support_shapes_present"]).lower()}
accepted dynamic payload rows      : {inventory["accepted_dynamic_payload_row_count"]}
primitive row formula executed     : {str(reconciliation["primitive_row_formula_executed"]).lower()}
higher response functional executed: {str(higher_attempt["selected_functional_executed"]).lower()}
second-order coefficient rows emitted : false
individual lambda selected         : false
full SM closure                    : false
```

So the missing object is not another branch search.  It is selected execution of
the dynamic payload rows that can emit `lambda_static*Z` and `lambda_static*X`:
zero-mode basis values, finite Hessian C1 source blocks, and primitive C1
contractions.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
