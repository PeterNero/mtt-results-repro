"""Audit the H-threshold cycle-break cutset for the strict tenth K row."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hthresholdcyclebreakcutset_or_tenthkrowfrontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
CUTSET = PACKET_DIR / "h_threshold_cycle_break_cutset.packet.json"
ROUTE_MATRIX = PACKET_DIR / "tenth_k_row_route_matrix.packet.json"
NEXT_WORKORDER = PACKET_DIR / "next_tenth_k_row_source_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HThresholdCycleBreakCutset_or_TenthKRowFrontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_HTHRESHOLDCYCLEBREAKCUTSET_OR_TENTHKROWFRONTIER_"
    "CLOSED_LOOP_BOUNDARY_STRICT_H_ROW_OPEN"
)
NEXT = "MTT_Selected_TenthHThresholdKRowSource_or_LargeThresholdRGPrimitiveTheorem_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure flag")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cutset = load(CUTSET)
    route_matrix = load(ROUTE_MATRIX)
    workorder = load(NEXT_WORKORDER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("cutset", cutset),
        ("route matrix", route_matrix),
        ("workorder", workorder),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "certificate next")
    require(data["theorem"]["proved"] is True, "candidate theorem")
    require(cert["theorem_proved"] is True, "certificate theorem")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")

    decision = data["closure_decision"]
    require(decision["accepted_selected_K_source_row_count"] == 9, "strict K count")
    require(decision["selected_K_threshold_row_count_required"] == 10, "required K count")
    require(decision["cycle_break_cutset_closed"] is True, "cutset closed")
    require(decision["strict_H_K_threshold_row_emitted"] is False, "H row overclaim")
    require(decision["strict_Omega_lambda_scalar_execution_closed"] is False, "Omega overclaim")
    require(decision["full_no_knob_closed"] is False, "full no-knob overclaim")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclaim decision")
    require(decision["controlled_empirical_10_of_10_available"] is True, "empirical availability")
    require(
        decision["controlled_empirical_10_of_10_selected_for_no_knob"] is False,
        "empirical no-knob overclaim",
    )
    for key in [
        "direct_H_K_row_exit_accepted",
        "selected_large_threshold_RG_exit_accepted",
        "universal_primitive_crossuse_exit_accepted",
    ]:
        require(decision[key] is False, f"exit overaccepted {key}")

    require(cutset["status"] == "H_THRESHOLD_LOOP_BOUNDARY_RECORDED_TENTH_ROW_OPEN", "cutset status")
    require(cutset["accepted_selected_K_source_row_count"] == 9, "cutset K count")
    require(cutset["selected_K_threshold_row_count_required"] == 10, "cutset required")
    require(cutset["strict_H_K_threshold_row_emitted"] is False, "cutset H row")
    require(cutset["controlled_empirical_layer_available"] is True, "cutset empirical layer")
    require(
        cutset["controlled_empirical_layer_selected_for_no_knob"] is False,
        "cutset empirical no-knob",
    )
    exits = {route["route_id"]: route for route in cutset["cycle_break_exits"]}
    require(set(exits) == {"direct_H_K_row", "selected_large_threshold_RG", "universal_primitive_crossuse"}, "exit set")
    for route in exits.values():
        require(route["currently_emitted"] is False, f"route emitted {route['route_id']}")
        require("acceptance_test" in route and route["acceptance_test"], f"route acceptance {route['route_id']}")

    forbidden = set(cutset["forbidden_repeats"])
    for phrase in [
        "row-local brute force without new selected source values",
        "diagonal HYM or pure trace degeneracy as a value source",
        "B_Huv support promoted directly to Herm(2) value rows",
        "lambda_H(M_t) inversion treated as source selection",
        "controlled one-parameter calibration counted as no-knob closure",
    ]:
        require(phrase in forbidden, f"missing forbidden repeat {phrase}")

    require(route_matrix["status"] == "THREE_STRICT_EXITS_DEFINED_NONE_ACCEPTED", "route status")
    route_decision = route_matrix["route_decision"]
    require(route_decision["controlled_empirical_10_of_10_available"] is True, "route empirical")
    require(route_decision["strict_no_knob_10_of_10_available"] is False, "route no-knob")
    for key in [
        "direct_H_K_row_accepted",
        "selected_large_threshold_RG_accepted",
        "universal_primitive_crossuse_accepted",
        "strict_tenth_K_row_accepted",
    ]:
        require(route_decision[key] is False, f"route overaccepted {key}")

    require(workorder["status"] == "NEXT_WORKORDER_ATTACK_CYCLE_BREAK_EXITS_ONLY", "workorder status")
    require(workorder["next_required_artifact"] == NEXT, "workorder next")
    require(len(workorder["allowed_next_constructions"]) == 3, "allowed constructions")
    require("conditional ten-K theorem trigger" in workorder["minimum_payload"], "minimum trigger")
    require(
        "lambda_H(M_t) inversion treated as source selection" in workorder["not_allowed_as_next_step"],
        "workorder forbidden inversion",
    )

    for phrase in [
        "HThresholdCycleBreakCutsetTheorem",
        "Strict selected K rows: `9/10`",
        "Controlled empirical layer selected for no-knob: `false`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: H-threshold cycle-break cutset closed; strict tenth H K row remains the next target."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
