"""Audit the concrete value-slot manifest for final dynamic C1 closure."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_physicalsourceemissionvalues_or_honestgalerkinexecution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTE_A = PACKET_DIR / "route_a_emission_value_slots.packet.json"
ROUTE_B = PACKET_DIR / "route_b_honest_execution_workorder.packet.json"
RESULT = PACKET_DIR / "closure_attempt_result.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhysicalSourceEmissionValues_or_HonestGalerkinExecution_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_physicalsourceemissionvalues_or_honestgalerkinexecution.py"

STATUS = "MTT_SELECTED_PHYSICALSOURCEEMISSIONVALUES_OR_HONESTGALERKINEXECUTION_BUILT_VALUE_SLOTS_OPEN"
NEXT = "MTT_Selected_RouteAPhysicalEmissionValues_or_RouteBRowExecution_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def guardrails(payload: dict, label: str) -> None:
    require(payload["observed_data_used_as_selector"] is False, f"{label}: observed selector used")
    require(payload["target_fitting_used"] is False, f"{label}: target fitting used")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    route_a = load(ROUTE_A)
    route_b = load(ROUTE_B)
    result = load(RESULT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("concrete value slots" in note, "note misses value slots")

    require(route_a["status"] == "ROUTE_A_VALUE_SLOTS_DECLARED_VALUES_NOT_EMITTED", "Route A status mismatch")
    require(len(route_a["slots"]) == 5, "Route A slot count mismatch")
    for item in route_a["slots"]:
        require(item["value"] is None, f"Route A slot unexpectedly filled: {item['name']}")
        require(item["theorem_derived"] is False, f"Route A theorem overclaim: {item['name']}")
        require(item["same_branch"] is False, f"Route A same-branch overclaim: {item['name']}")
        require(item["selected_source_verified"] is False, f"Route A source overclaim: {item['name']}")
    require(route_a["all_values_emitted_now"] is False, "Route A values overemitted")
    require(route_a["lane_closes_now"] is False, "Route A lane overclosed")
    require(route_a["if_all_values_emit"]["A_selected"] == [[12.0, 0.0], [0.0, 12.0]], "Route A if-close A mismatch")

    require(route_b["status"] == "ROUTE_B_EXECUTION_WORKORDER_DECLARED_ROWS_NOT_EXECUTED", "Route B status mismatch")
    require(route_b["strict_coordinate_target"]["total_real_coordinates"] == 72, "Route B coordinate count mismatch")
    require(len(route_b["row_blocks_to_emit"]) == 5, "Route B block count mismatch")
    expected_counts = {
        "selected_zero_mode_bases": 9,
        "primitive_three_by_three_contraction_terms": 72,
        "linear_response_matrices": 36,
        "hessian_source_vector": 2,
        "C33_nonzero_family_rank_tests": None,
    }
    for block in route_b["row_blocks_to_emit"]:
        require(block["row_count"] == expected_counts[block["name"]], f"Route B row count mismatch: {block['name']}")
        require(block["executed_now"] is False, f"Route B block unexpectedly executed: {block['name']}")
        require(block["selected_source_verified"] is False, f"Route B block source overclaim: {block['name']}")
    require(route_b["all_rows_executed_now"] is False, "Route B rows overexecuted")
    require(route_b["lane_closes_now"] is False, "Route B lane overclosed")

    require(result["status"] == "NO_FINAL_VALUES_EMITTED_CLOSURE_OBJECT_NOW_PRECISE", "result status mismatch")
    require(result["route_a_value_slots_filled"] is False, "result Route A overfilled")
    require(result["route_b_honest_rows_executed"] is False, "result Route B overexecuted")
    require(result["unpatched_dynamic_C1_packet_closed"] is False, "result dynamic C1 overclosed")
    require(result["true_SM_equivalence_closed"] is False, "result true SM overclosed")
    require(result["no_knob_closed"] is False, "result no-knob overclosed")
    require(result["locked_if_close_values"]["deltaTheta_C1"] == [1.0, 1.0], "locked delta mismatch")

    closure = data["closure_decision"]
    require(closure["value_slots_manifest_built"] is True, "manifest not built")
    require(closure["route_a_values_emitted"] is False, "candidate Route A overemitted")
    require(closure["route_b_rows_executed"] is False, "candidate Route B overexecuted")
    require(closure["unpatched_dynamic_C1_packet_closed"] is False, "candidate dynamic C1 overclosed")
    require(closure["true_SM_equivalence_closed"] is False, "candidate true SM overclosed")
    require(closure["no_knob_closed"] is False, "candidate no-knob overclosed")

    for label, payload in [
        ("candidate", data),
        ("route_a", route_a),
        ("route_b", route_b),
        ("result", result),
        ("certificate", cert),
    ]:
        guardrails(payload, label)

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
