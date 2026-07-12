"""Audit the post-source dynamic Qa/SU3 or C1 response frontier artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_dynamicqasu3_or_c1response_postsourcefrontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
RECONCILIATION = PACKET_DIR / "postsource_reconciliation.packet.json"
FRONTIER = PACKET_DIR / "dynamic_qasu3_c1_frontier.packet.json"
ROUTES = PACKET_DIR / "three_route_closure_contract.packet.json"
NEXT = PACKET_DIR / "next_executable_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_DynamicQaSU3_or_C1Response_PostSourceFrontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_DYNAMICQASU3_OR_C1RESPONSE_POSTSOURCEFRONTIER_BUILT_VALUES_OPEN"
NEXT_ARTIFACT = "MTT_Selected_SameSourceDynamicPhiFinC1_or_HonestGalerkinExecution_RouteTest_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    recon = load(RECONCILIATION)
    frontier = load(FRONTIER)
    routes = load(ROUTES)
    next_work = load(NEXT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag mismatch")
    require(data["next_required_artifact"] == NEXT_ARTIFACT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT_ARTIFACT, "cert next mismatch")

    for key, value in recon["closed_support"].items():
        require(value is True, f"closed support false: {key}")
    require(recon["guardrails"]["SM_parity_reopened"] is False, "SM parity reopened")
    require(recon["guardrails"]["finite_source_slots_reopened"] is False, "source slots reopened")
    require(recon["guardrails"]["actual_dynamic_QaSU3_operator_packet_closed"] is False, "dynamic Qa/SU3 overclosed")
    require(recon["guardrails"]["selected_C1_response_closed"] is False, "C1 overclosed")
    require(recon["guardrails"]["true_SM_equivalence_closed"] is False, "true equivalence overclosed")
    for phrase in [
        "SM-parity blocker",
        "missing finite source slot",
        "Qa/SU3 source-slot count still below eight",
    ]:
        require(phrase in recon["stale_language_retired"]["do_not_use"], f"stale phrase missing: {phrase}")

    require(frontier["starting_point"]["SM_parity_closed_frozen"] is True, "frontier SM parity not frozen")
    require(frontier["starting_point"]["finite_operator_source_slot_layer_closed_frozen"] is True, "frontier source slots not frozen")
    require(frontier["starting_point"]["source_slots_closed"] == 8, "source slots closed mismatch")
    require(frontier["starting_point"]["source_slots_remaining"] == 0, "source slots remaining mismatch")
    require(frontier["current_best_reduction"]["blocker_type"] == "dynamic selected value/source promotion", "blocker type mismatch")
    require(frontier["current_best_reduction"]["not_blocker_type"] == "SM-parity replay or finite source-slot assembly", "not blocker mismatch")
    for key in [
        "actual_dynamic_QaSU3_operator_packet",
        "selected_differentiated_PhiFinC1_source_map",
        "selected_A_selected",
        "selected_b_selected",
        "selected_deltaTheta_C1",
        "selected_sector_response_matrices",
    ]:
        require(frontier["open_dynamic_targets"][key] is True, f"open target missing: {key}")
    closure = frontier["closure_decision"]
    require(closure["postsource_frontier_built"] is True, "frontier not built")
    for key in [
        "actual_dynamic_QaSU3_operator_packet_closed",
        "selected_C1_response_closed",
        "A_selected_promoted",
        "b_selected_promoted",
        "deltaTheta_C1_promoted",
        "sector_response_matrices_promoted",
        "true_SM_equivalence_closed",
        "no_knob_closed",
    ]:
        require(closure[key] is False, f"overclosed: {key}")

    require(routes["route_closes_now"] is False, "route overclosed")
    route_ids = [route["id"] for route in routes["routes"]]
    require(route_ids == [
        "route_A_same_source_dynamic_PhiFinC1",
        "route_B_honest_selected_Galerkin_C1_execution",
        "route_C_superset_bridge",
    ], "route IDs mismatch")
    require(routes["routes"][0]["status"] == "OPEN_PRIMARY", "route A should be primary")
    require("selected differentiated Phi_fin^C1 applies Q_residual to phase/shift legs" in routes["routes"][0]["must_emit"], "route A emission missing")
    require("selected zero-mode basis and primitive 3x3 terms" in routes["routes"][1]["must_emit"], "route B emission missing")
    require("a theorem that identifies the dynamic HYM/End0/C1 packet with the selected C1 response target" in routes["routes"][2]["must_emit"], "route C bridge missing")

    require(next_work["next_required_artifact"] == NEXT_ARTIFACT, "next packet mismatch")
    require(next_work["first_action"] == "build Route A source-rule test with Route B readiness sidecar", "first action mismatch")
    require(len(next_work["work_items"]) == 3, "work item count mismatch")

    require(data["closure_claimed"] is False, "candidate should not claim closure")
    require(data["closure_decision"]["postsource_frontier_built"] is True, "candidate frontier flag missing")
    require(data["what_closes_now"]["stale_source_slot_language_retired"] is True, "stale language not retired")
    require(data["what_remains_open"]["actual_dynamic_QaSU3_operator_packet"] is True, "dynamic target missing")
    require(data["what_remains_open"]["selected_b_selected"] is True, "b target missing")

    require("first post-SM-parity frontier artifact" in note, "note post parity statement missing")
    require("Dynamic selected operator/value emission" in note, "note live blocker missing")
    require("No route closes here" in note, "note no closure missing")
    require(NEXT_ARTIFACT in note, "note next missing")

    for packet in [data, recon, frontier, routes, next_work, cert]:
        require(packet.get("observed_data_used_as_selector") is False or packet.get("guardrails", {}).get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False or packet.get("guardrails", {}).get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
