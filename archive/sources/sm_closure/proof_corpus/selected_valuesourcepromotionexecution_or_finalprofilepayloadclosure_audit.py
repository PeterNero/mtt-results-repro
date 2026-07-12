"""Audit value-source promotion execution / final profile-payload closure."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_valuesourcepromotionexecution_or_finalprofilepayloadclosure"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTES = PACKET_DIR / "three_route_promotion_execution.packet.json"
NECESSARY = PACKET_DIR / "necessary_conditions_for_final_promotion.packet.json"
FINAL = PACKET_DIR / "final_profile_payload_closure_gate.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ValueSourcePromotionExecution_or_FinalProfilePayloadClosure_v1.md"

STATUS = (
    "MTT_SELECTED_VALUESOURCEPROMOTIONEXECUTION_OR_FINALPROFILEPAYLOADCLOSURE_"
    "THREE_ROUTE_GATE_EXECUTED_FINAL_VALUES_OPEN"
)
NEXT_ARTIFACT = "MTT_Selected_FinalProfileLikelihoodOrDynamicPayloadValues_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def guard(packet: dict[str, Any], label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    routes = load(ROUTES)
    necessary = load(NECESSARY)
    final = load(FINAL)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", candidate),
        ("routes", routes),
        ("necessary", necessary),
        ("final", final),
        ("cert", cert),
    ]:
        guard(packet, label)

    require(candidate["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["theorem"]["name"] == "ValueSourcePromotionExecutionOrFinalProfilePayloadClosureTheorem", "theorem")
    require(cert["theorem_proved"] is True, "cert theorem")
    require(candidate["next_required_artifact"] == NEXT_ARTIFACT, "candidate next")
    require(final["next_required_artifact"] == NEXT_ARTIFACT, "final next")
    require(cert["next_required_artifact"] == NEXT_ARTIFACT, "cert next")

    require(routes["status"] == "THREE_ROUTES_EXECUTED_NO_FINAL_PROMOTION", "routes status")
    require(routes["route_count"] == 3, "route count")
    require(routes["support_closed_route_count"] == 3, "support route count")
    require(routes["promoted_route_count"] == 0, "route overpromoted")
    by_route = {route["route"]: route for route in routes["routes"]}
    for key in [
        "A_full_profile_likelihood",
        "B_selected_threshold_response_functional",
        "C_actual_dynamic_QaSU3_payload",
    ]:
        require(by_route[key]["attempted"] is True, f"{key} not attempted")
        require(by_route[key]["support_closed"] is True, f"{key} support not closed")
        require(by_route[key]["promoted"] is False, f"{key} overpromoted")
        require(len(by_route[key]["promotion_blockers"]) >= 4, f"{key} blockers not sharp")

    require(necessary["status"] == "NECESSARY_CONDITIONS_ENUMERATED", "necessary status")
    require(len(necessary["conditions"]) == 4, "condition count")
    require(necessary["satisfied_condition_count"] == 0, "necessary over-satisfied")
    require(necessary["unsatisfied_condition_count"] == 4, "necessary unsatisfied count")

    closed = final["closed_do_not_reopen"]
    require(closed["accepted_precision_source_value_frontier_attacked"] is True, "source frontier")
    require(closed["closed_replay_source_value_class_count"] == 8, "replay class count")
    require(closed["operator_source_slots_closed"] == 8, "source slots")
    require(closed["dynamic_QaSU3_first_response_layer_replayed"] is True, "first response")
    require(closed["partial_QaSU3_payload_filled"] is True, "partial payload")
    require(closed["threshold_response_functional_contract_closed"] is True, "threshold contract")
    require(len(final["exit_set"]) == 3, "exit set count")
    require(final["accepted_true_equivalence_precision_rows"] == 0, "true rows overclaim")
    require(final["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(final["full_no_knob_closed"] is False, "no-knob overclosed")

    decision = candidate["closure_decision"]
    require(decision["value_source_promotion_execution_closed"] is True, "decision execution")
    require(decision["three_route_gate_executed"] is True, "decision gate")
    require(decision["route_count"] == 3, "decision route count")
    require(decision["support_closed_route_count"] == 3, "decision support routes")
    require(decision["promoted_route_count"] == 0, "decision promoted routes")
    require(decision["necessary_condition_count"] == 4, "decision condition count")
    require(decision["satisfied_necessary_condition_count"] == 0, "decision satisfied")
    require(decision["unsatisfied_necessary_condition_count"] == 4, "decision unsatisfied")
    for key in [
        "accepted_full_profile_likelihood_closed",
        "selected_threshold_response_functional_instantiated",
        "actual_dynamic_QaSU3_payload_values_closed",
        "selected_C1_response_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"{key} overclosed")

    for phrase in [
        "routes executed                                  3",
        "routes with support closed                       3",
        "promoted routes                                  0",
        "accepted true-equivalence precision rows         0",
        "actual dynamic Qa/SU3 payload values             false",
        NEXT_ARTIFACT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
