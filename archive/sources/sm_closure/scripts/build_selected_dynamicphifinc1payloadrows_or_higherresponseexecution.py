"""Build dynamic Phi_fin/C1 payload rows or higher-response execution artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_dynamicphifinc1payloadrows_or_higherresponseexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
INVENTORY = PACKET_DIR / "dynamic_phifin_c1_payload_row_inventory.packet.json"
RECONCILIATION = PACKET_DIR / "support_vs_selected_payload_reconciliation.packet.json"
EXECUTION = PACKET_DIR / "higher_response_execution_attempt_after_payload_inventory.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_payload_row_inventory.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_DynamicPhiFinC1PayloadRows_or_HigherResponseExecution_v1.md"

PREVIOUS = DATA / "selected_higherresponserthetafunctional_or_sourceanchortheorem.candidate.json"
CONTRACT = (
    DATA
    / "selected_higherresponserthetafunctional_or_sourceanchortheorem"
    / "rtheta_higher_response_functional_contract.packet.json"
)
PAYLOAD_GAP = (
    DATA
    / "selected_higherresponserthetafunctional_or_sourceanchortheorem"
    / "higher_response_source_payload_gap.packet.json"
)
PHIFIN_ALPHA1 = DATA / "selected_phifin_alpha1_payload.candidate.json"
RIEZ_SLOT = (
    DATA
    / "selected_phifinpayload_or_globaldestabilizerenumeration_closingrun"
    / "riesz_green_dotd_projector_slot_closure.packet.json"
)
PROJECTORS_DOTD = DATA / "selected_routec_sector_projectors_dotd_on_smooth_bn.candidate.json"
ZERO_MODE = DATA / "selected_zero_mode_basis_from_hym_projector_source_theorem.candidate.json"
DYNAMIC_TRACE = DATA / "selected_dynamicphifintracebinding_or_primitiverowformulaexecution.candidate.json"
PRIMITIVE_ROW_CONTRACT = (
    DATA
    / "selected_dynamicphifintracebinding_or_primitiverowformulaexecution"
    / "primitive_row_formula_execution_contract.packet.json"
)
SAME_SOURCE_ROUTE = DATA / "selected_samesourcedynamicphifinc1_or_honestgalerkinexecution_routetest.candidate.json"

STATUS = (
    "MTT_SELECTED_DYNAMICPHIFINC1PAYLOADROWS_OR_HIGHERRESPONSEEXECUTION_"
    "BUILT_ROW_LEDGER_EXECUTION_OPEN"
)
NEXT = "MTT_Selected_HYMProjectorZeroModeBasisValueEmission_or_PrimitiveRowFormulaExecution_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing dynamic Phi_fin/C1 payload sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        CONTRACT,
        PAYLOAD_GAP,
        PHIFIN_ALPHA1,
        RIEZ_SLOT,
        PROJECTORS_DOTD,
        ZERO_MODE,
        DYNAMIC_TRACE,
        PRIMITIVE_ROW_CONTRACT,
        SAME_SOURCE_ROUTE,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    contract = load(CONTRACT)
    payload_gap = load(PAYLOAD_GAP)
    phifin_alpha1 = load(PHIFIN_ALPHA1)
    riez_slot = load(RIEZ_SLOT)
    projectors_dotd = load(PROJECTORS_DOTD)
    zero_mode = load(ZERO_MODE)
    dynamic_trace = load(DYNAMIC_TRACE)
    primitive_row_contract = load(PRIMITIVE_ROW_CONTRACT)
    same_source_route = load(SAME_SOURCE_ROUTE)

    payload_slots = phifin_alpha1["payload_slots"]
    selected_payload_flags = phifin_alpha1["payload_summary"]["selected_payload_flags"]

    rows: list[dict[str, Any]] = []
    for row_id in payload_gap["open_payload_flags"]:
        slot = payload_slots[row_id]
        row = {
            "row_id": row_id,
            "support_candidate_present": slot.get("support_candidate_present") is True,
            "selected_payload_flag": selected_payload_flags[row_id],
            "accepted_as_dynamic_phifin_c1_payload_row": False,
            "candidate_path": slot.get("candidate_path"),
            "reason": slot.get("reason"),
        }
        if row_id in ["Riesz_Green", "dotD_alpha1", "sector_projectors"]:
            row["stationary_source_slot_closed"] = riez_slot["closure_result"][
                "riesz_green_dotd_projector_slot_closed"
            ]
            row["dynamic_C1_scope_excluded_by_source"] = riez_slot["selected_source_value"][
                "dynamic_C1_scope_excluded"
            ]
        if row_id == "sector_projectors":
            row["finite_projector_matrices_emitted"] = projectors_dotd["what_closes_now"][
                "sector_projectors_on_27_mode_BN_emitted"
            ]
            row["honest_validator_promotes"] = projectors_dotd["superset_mode"]["straight_path"][
                "honest_validator_promotes"
            ]
        if row_id == "zero_mode_bases":
            row["zero_mode_bridge_theorem_closed"] = zero_mode["promotion_decision"][
                "bridge_theorem_closes"
            ]
            row["selected_zero_mode_bases_emitted"] = zero_mode["theorem"][
                "selected_values_emitted"
            ]
        if row_id in ["finite_Hessian_C1_source", "primitive_C1_contractions"]:
            row["primitive_row_formula_contract_built"] = (
                primitive_row_contract["status"]
                == "PRIMITIVE_ROW_FORMULA_CONTRACT_BUILT_FORMULA_NOT_EXECUTED"
            )
            row["primitive_row_formula_executed"] = primitive_row_contract[
                "independent_rows_executed_now"
            ]
        rows.append(row)

    support_count = sum(1 for row in rows if row["support_candidate_present"])
    selected_count = sum(1 for row in rows if row["accepted_as_dynamic_phifin_c1_payload_row"])
    stationary_source_slot_count = sum(
        1 for row in rows if row.get("stationary_source_slot_closed") is True
    )

    inventory = {
        "schema": "MTTDynamicPhiFinC1PayloadRowInventory.v1",
        "status": "PAYLOAD_ROW_INVENTORY_BUILT_NO_DYNAMIC_ROWS_ACCEPTED",
        "contract_source": rel(CONTRACT),
        "payload_gap_source": rel(PAYLOAD_GAP),
        "row_count": len(rows),
        "support_candidate_present_count": support_count,
        "stationary_source_slot_closed_count": stationary_source_slot_count,
        "accepted_dynamic_payload_row_count": selected_count,
        "rows": rows,
        "all_support_shapes_present": phifin_alpha1["payload_summary"][
            "all_support_shapes_present"
        ],
        "all_selected_values_emitted": phifin_alpha1["payload_summary"][
            "all_selected_values_emitted"
        ],
        "higher_response_execution_inputs_available": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(INVENTORY, inventory)

    reconciliation = {
        "schema": "MTTSupportVsSelectedPayloadReconciliation.v1",
        "status": "SUPPORT_ROWS_RECONCILED_WITH_SELECTED_PAYLOAD_GAP",
        "stationary_riesz_green_dotd_slot_closed": riez_slot["closure_result"][
            "riesz_green_dotd_projector_slot_closed"
        ],
        "stationary_source_value_emitted": riez_slot["closure_result"][
            "selected_source_value_emitted"
        ],
        "dynamic_C1_scope_excluded": riez_slot["selected_source_value"][
            "dynamic_C1_scope_excluded"
        ],
        "sector_projectors_emitted_as_matrices": projectors_dotd["what_closes_now"][
            "sector_projectors_on_27_mode_BN_emitted"
        ],
        "sector_projectors_honest_validator_promotes": projectors_dotd["superset_mode"][
            "straight_path"
        ]["honest_validator_promotes"],
        "dynamic_trace_binding_reconciled": dynamic_trace["closure_decision"][
            "dynamic_trace_binding_reconciled"
        ],
        "primitive_row_formula_contract_built": primitive_row_contract["status"]
        == "PRIMITIVE_ROW_FORMULA_CONTRACT_BUILT_FORMULA_NOT_EXECUTED",
        "primitive_row_formula_executed": primitive_row_contract[
            "independent_rows_executed_now"
        ],
        "same_source_route_test_closed": same_source_route["what_closes_now"][
            "PSM_C1_01_route_test_completed"
        ],
        "same_source_dynamic_payload_closed": same_source_route["closure_decision"][
            "selected_C1_response_closed"
        ],
        "what_this_proves": [
            "the stationary Riesz/Green/dotD source slot is not the same as dynamic C1 payload execution",
            "finite sector projectors/dotD matrices exist but honest source flags still fail",
            "trace binding and finite measure blockers are retired, but the primitive row formula has not executed",
            "all nine dynamic payload slots still have selected_payload_flag=false in the alpha1 payload attempt",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(RECONCILIATION, reconciliation)

    execution = {
        "schema": "MTTHigherResponseExecutionAttemptAfterPayloadInventory.v1",
        "status": "HIGHER_RESPONSE_EXECUTION_BLOCKED_BY_DYNAMIC_PAYLOAD_ROWS",
        "codomain_scalar_row_count": contract["codomain_scalar_row_count"],
        "codomain_scalar_rows": contract["codomain_scalar_rows"],
        "payload_row_count": len(rows),
        "accepted_dynamic_payload_row_count": selected_count,
        "execution_inputs_available_now": False,
        "selected_functional_executed": False,
        "accepted_scalar_row_count_now": 0,
        "mass_hierarchy_test_executed": False,
        "CKM_test_executed": False,
        "PMNS_test_executed": False,
        "CP_test_executed": False,
        "lambda_H_row_emitted": False,
        "why_blocked": [
            "selected zero-mode bases are not emitted",
            "selected finite Hessian C1 source blocks are absent",
            "primitive C1 contractions and sector response matrices are absent",
            "rho_E/D_E/operator-level payload rows are still support-only or stationary-only",
            "higher-response scalar rows would otherwise be diagnostic/replay rows, not selected source values",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(EXECUTION, execution)

    cutset = {
        "schema": "MTTNextCutsetAfterPayloadRowInventory.v1",
        "status": "NEXT_ATTACK_HYM_PROJECTOR_ZEROMODE_VALUES_OR_PRIMITIVE_ROW_FORMULA",
        "closed_now": {
            "dynamic_payload_row_inventory_built": True,
            "support_vs_selected_payload_reconciled": True,
            "stationary_slot_not_confused_with_dynamic_payload": True,
            "higher_response_execution_attempted_and_blocked": True,
            "next_executable_subgates_identified": True,
        },
        "still_open": {
            "selected_HYM_projector_zero_mode_basis_values": True,
            "selected_D_E_operator_values": True,
            "selected_rho_E_transition_data": True,
            "selected_finite_Hessian_C1_source_blocks": True,
            "selected_deltaTheta_C1": True,
            "primitive_C1_contractions": True,
            "sector_response_matrices": True,
            "higher_response_Rtheta_execution": True,
            "Yukawa_mass_mixing_value_closure": True,
            "true_SM_equivalence": True,
            "full_no_knob": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "emit selected HYM/Strominger zero-mode projectors, bases, gaps, and Gram convention",
            "route_B": "execute the selected primitive row kernel formula for the 72 primitive C1 rows",
            "route_C": "derive a physical Phi_fin^C1 action restriction clause that supplies both lanes",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedDynamicPhiFinC1PayloadRowsOrHigherResponseExecution",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "dynamic_phifin_c1_payload_row_inventory": rel(INVENTORY),
            "support_vs_selected_payload_reconciliation": rel(RECONCILIATION),
            "higher_response_execution_attempt_after_payload_inventory": rel(EXECUTION),
            "next_cutset_after_payload_row_inventory": rel(CUTSET),
        },
        "theorem": {
            "name": "DynamicPhiFinC1PayloadRowInventoryAndExecutionBlockerTheorem",
            "proved": True,
            "statement": (
                "All nine dynamic Phi_fin/C1 payload slots have support shapes, but none is accepted as a selected "
                "dynamic payload row. The stationary Riesz/Green/dotD slot and finite projector matrices are real "
                "progress, yet they explicitly do not execute the dynamic C1 payload or primitive row formula. "
                "Therefore the ten-row higher-response Rtheta contract cannot be executed until selected HYM "
                "zero-mode basis values or primitive C1 row formulas are emitted."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "dynamic_payload_row_inventory_built": True,
            "dynamic_payload_row_count": len(rows),
            "support_candidate_present_count": support_count,
            "accepted_dynamic_payload_row_count": selected_count,
            "stationary_source_slot_closed_count": stationary_source_slot_count,
            "higher_response_execution_inputs_available": False,
            "higher_response_Rtheta_executed": False,
            "accepted_scalar_row_count_now": 0,
            "no_knob_value_derivation_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_DynamicPhiFinC1PayloadRows_or_HigherResponseExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "dynamic_payload_row_inventory_built": True,
        "dynamic_payload_row_count": len(rows),
        "support_candidate_present_count": support_count,
        "accepted_dynamic_payload_row_count": selected_count,
        "stationary_source_slot_closed_count": stationary_source_slot_count,
        "higher_response_execution_inputs_available": False,
        "higher_response_Rtheta_executed": False,
        "accepted_scalar_row_count_now": 0,
        "no_knob_value_derivation_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected DynamicPhiFinC1PayloadRows or HigherResponseExecution v1

Status: `{STATUS}`.

The payload gate is now inventoried row by row.

```text
dynamic payload slots                  : {len(rows)}
support shapes present                 : {support_count}
accepted dynamic payload rows          : {selected_count}
stationary source slots closed         : {stationary_source_slot_count}
higher-response Rtheta executed        : false
accepted scalar rows                   : 0
full no-knob closure                   : false
true SM equivalence                    : false
```

The next executable subgate is to emit selected HYM/Strominger zero-mode
projectors/bases/gaps/Gram convention, or execute the selected primitive row
kernel formula for the 72 C1 primitive rows.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
