"""Audit Step60 dynamic payload inventory import / HYM primitive frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step60_dynamicpayload_inventory_import_or_hymprimitive_frontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
IMPORT_PACKET = PACKET_DIR / "step60_dynamic_payload_inventory_import.packet.json"
CUTSET = PACKET_DIR / "step60_next_hymprimitive_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step60_DynamicPayloadInventoryImport_or_HYMPrimitiveFrontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP60_DYNAMIC_PAYLOAD_INVENTORY_IMPORTED_HYM_PRIMITIVE_FRONTIER_OPEN"
NEXT = "MTT_Selected_HYMProjectorZeroModeBasisValueEmission_or_PrimitiveRowFormulaExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)
    data = load(DATA)
    packet = load(IMPORT_PACKET)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem missing")
    for item in [data, packet, cutset, cert]:
        require(item.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(item.get("target_fitting_used") is False, "target fitting violation")

    require(packet["dynamic_payload_row_count"] == 9, "payload count mismatch")
    require(packet["support_candidate_present_count"] == 9, "support count mismatch")
    require(packet["stationary_source_slot_closed_count"] == 3, "stationary count mismatch")
    require(packet["accepted_dynamic_payload_row_count"] == 0, "dynamic payload rows overaccepted")
    require(packet["higher_response_execution_inputs_available"] is False, "execution inputs overclaimed")
    require(packet["higher_response_Rtheta_executed"] is False, "higher response overexecuted")
    require(packet["accepted_scalar_row_count_now"] == 0, "scalar rows overaccepted")
    require(cutset["closed_now"]["dynamic_payload_row_inventory_imported"] is True, "inventory import missing")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")

    decision = data["closure_decision"]
    require(decision["dynamic_payload_row_inventory_built"] is True, "decision inventory missing")
    require(decision["dynamic_payload_row_count"] == 9, "decision payload count mismatch")
    require(decision["support_candidate_present_count"] == 9, "decision support count mismatch")
    require(decision["stationary_source_slot_closed_count"] == 3, "decision stationary count mismatch")
    require(decision["accepted_dynamic_payload_row_count"] == 0, "decision payload rows overaccepted")
    require(decision["accepted_scalar_row_count_now"] == 0, "decision scalar rows overaccepted")
    for key in [
        "higher_response_execution_inputs_available",
        "higher_response_Rtheta_executed",
        "no_knob_value_derivation_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"candidate overclosed: {key}")
        require(cert[key] is False, f"certificate overclosed: {key}")
    for phrase in [
        "dynamic payload slots                  : 9",
        "support shapes present                 : 9",
        "accepted dynamic payload rows          : 0",
        "stationary source slots closed         : 3",
        NEXT,
    ]:
        require(phrase in note, f"note missing: {phrase}")
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
