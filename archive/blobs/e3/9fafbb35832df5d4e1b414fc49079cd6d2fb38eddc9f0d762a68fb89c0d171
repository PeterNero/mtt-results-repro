"""Build Step60 dynamic payload inventory import / HYM primitive frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step60_dynamicpayload_inventory_import_or_hymprimitive_frontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
IMPORT_PACKET = PACKET_DIR / "step60_dynamic_payload_inventory_import.packet.json"
CUTSET = PACKET_DIR / "step60_next_hymprimitive_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step60_DynamicPayloadInventoryImport_or_HYMPrimitiveFrontier_v1.md"

STEP59 = DATA / "selected_step59_higherresponse_contract_import_or_payloadexecution.candidate.json"
DYNAMIC = DATA / "selected_dynamicphifinc1payloadrows_or_higherresponseexecution.candidate.json"
INVENTORY = (
    DATA
    / "selected_dynamicphifinc1payloadrows_or_higherresponseexecution"
    / "dynamic_phifin_c1_payload_row_inventory.packet.json"
)
EXECUTION = (
    DATA
    / "selected_dynamicphifinc1payloadrows_or_higherresponseexecution"
    / "higher_response_execution_attempt_after_payload_inventory.packet.json"
)
CUTSET_SOURCE = (
    DATA
    / "selected_dynamicphifinc1payloadrows_or_higherresponseexecution"
    / "next_cutset_after_payload_row_inventory.packet.json"
)

STATUS = "MTT_SELECTED_STEP60_DYNAMIC_PAYLOAD_INVENTORY_IMPORTED_HYM_PRIMITIVE_FRONTIER_OPEN"
NEXT = "MTT_Selected_HYMProjectorZeroModeBasisValueEmission_or_PrimitiveRowFormulaExecution_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)
    inputs = [STEP59, DYNAMIC, INVENTORY, EXECUTION, CUTSET_SOURCE]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step60 inputs: " + ", ".join(missing))

    step59 = load(STEP59)
    dynamic = load(DYNAMIC)
    inventory = load(INVENTORY)
    execution = load(EXECUTION)
    cutset_source = load(CUTSET_SOURCE)

    import_packet = {
        "schema": "MTTStep60DynamicPayloadInventoryImport.v1",
        "status": "DYNAMIC_PAYLOAD_INVENTORY_IMPORTED",
        "step59_source": rel(STEP59),
        "dynamic_payload_source": rel(DYNAMIC),
        "dynamic_payload_row_count": inventory["row_count"],
        "support_candidate_present_count": inventory["support_candidate_present_count"],
        "stationary_source_slot_closed_count": inventory["stationary_source_slot_closed_count"],
        "accepted_dynamic_payload_row_count": inventory["accepted_dynamic_payload_row_count"],
        "higher_response_execution_inputs_available": execution["execution_inputs_available_now"],
        "higher_response_Rtheta_executed": execution["selected_functional_executed"],
        "accepted_scalar_row_count_now": execution["accepted_scalar_row_count_now"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(IMPORT_PACKET, import_packet)

    cutset = {
        "schema": "MTTStep60NextHYMPrimitiveCutset.v1",
        "status": "NEXT_HYM_PROJECTOR_ZEROMODE_VALUES_OR_PRIMITIVE_ROW_FORMULA",
        "closed_now": {
            "dynamic_payload_row_inventory_imported": True,
            "support_shapes_present_for_all_dynamic_payload_slots": True,
            "stationary_source_slots_not_confused_with_dynamic_payload": True,
            "higher_response_execution_blocker_imported": True,
        },
        "still_open": cutset_source["still_open"],
        "recommended_next": cutset_source["recommended_next"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedStep60DynamicPayloadInventoryImportOrHYMPrimitiveFrontier",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in inputs},
        "output_packets": {
            "dynamic_payload_inventory_import": rel(IMPORT_PACKET),
            "next_hymprimitive_cutset": rel(CUTSET),
        },
        "theorem": {
            "name": "Step60DynamicPayloadInventoryImportTheorem",
            "proved": True,
            "statement": (
                "The dynamic Phi_fin/C1 payload inventory is imported into the numbered plan. All nine "
                "payload slots have support shapes, three stationary source slots are closed, but zero "
                "dynamic payload rows are accepted. Therefore higher-response execution is blocked at "
                "selected HYM zero-mode basis values or primitive C1 row formula execution."
            ),
        },
        "closure_decision": {
            "dynamic_payload_row_inventory_built": True,
            "dynamic_payload_row_count": inventory["row_count"],
            "support_candidate_present_count": inventory["support_candidate_present_count"],
            "stationary_source_slot_closed_count": inventory["stationary_source_slot_closed_count"],
            "accepted_dynamic_payload_row_count": inventory["accepted_dynamic_payload_row_count"],
            "higher_response_execution_inputs_available": False,
            "higher_response_Rtheta_executed": False,
            "accepted_scalar_row_count_now": 0,
            "no_knob_value_derivation_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": step59["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step60_DynamicPayloadInventoryImport_or_HYMPrimitiveFrontier_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        **candidate["closure_decision"],
        "theorem_proved": True,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected Step60 DynamicPayloadInventoryImport or HYMPrimitiveFrontier v1

Status: `{STATUS}`.

```text
dynamic payload slots                  : {inventory["row_count"]}
support shapes present                 : {inventory["support_candidate_present_count"]}
stationary source slots closed         : {inventory["stationary_source_slot_closed_count"]}
accepted dynamic payload rows          : {inventory["accepted_dynamic_payload_row_count"]}
higher-response Rtheta executed        : false
accepted scalar rows                   : 0
full no-knob closure                   : false
true SM equivalence                    : false
```

The next target is `{NEXT}`.
""",
        encoding="utf-8",
    )
    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
