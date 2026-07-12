"""Audit Route A physical values / Route B row-execution diagnostic attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_routeaphysicalemissionvalues_or_routebrowexecution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTE_A = PACKET_DIR / "route_a_physical_value_emission_attempt.packet.json"
ROUTE_B = PACKET_DIR / "route_b_replay_rank_diagnostics.packet.json"
RESULT = PACKET_DIR / "row_execution_closure_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_RouteAPhysicalEmissionValues_or_RouteBRowExecution_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_routeaphysicalemissionvalues_or_routebrowexecution.py"

STATUS = "MTT_SELECTED_ROUTEA_PHYSICALVALUES_OR_ROUTEB_ROWEXECUTION_BUILT_REPLAY_RANK_DIAGNOSTICS_OPEN"
NEXT = "MTT_Selected_RouteBIndependentPrimitiveRows_or_RouteAPhiFinBoundaryEmission_v1"


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
    require("support only" in note, "note misses support guardrail")

    require(route_a["status"] == "ROUTE_A_PHYSICAL_VALUES_NOT_EMITTED", "Route A status mismatch")
    require(len(route_a["slot_attempts"]) == 5, "Route A slot attempt count mismatch")
    for item in route_a["slot_attempts"]:
        require(item["attempted_now"] is False, f"Route A attempted unexpectedly: {item['name']}")
        require(item["value_emitted"] is False, f"Route A emitted unexpectedly: {item['name']}")
    require(route_a["all_route_a_values_emitted"] is False, "Route A overemitted")
    require(route_a["lane_closes_now"] is False, "Route A overclosed")

    require(route_b["status"] == "ROUTE_B_REPLAY_RANK_DIAGNOSTICS_COMPUTED_NOT_INDEPENDENT_EXECUTION", "Route B status mismatch")
    require(route_b["diagnostic_level"] == "replay_support_only", "Route B diagnostic level mismatch")
    for sector, item in route_b["sector_diagnostics"].items():
        require(item["rank"] >= 2, f"{sector} rank too small")
        require(item["frobenius_norm_sq"] > 0.0, f"{sector} zero norm")
        require(item["C33_nonzero"] is True, f"{sector} C33 zero")
        require(item["selected_by_independent_galerkin_execution"] is False, f"{sector} overpromoted")
    tests = route_b["diagnostic_tests_pass"]
    require(tests["all_sector_matrices_nonzero"] is True, "sector nonzero diagnostic failed")
    require(tests["all_C33_nonzero"] is True, "C33 diagnostic failed")
    require(tests["all_sector_ranks_at_least_two"] is True, "rank diagnostic failed")
    require(tests["phase_shift_cross_commutator_nonzero"] is True, "commutator diagnostic failed")
    require(route_b["cross_lane_commutators"]["u_d_commutator_norm_sq"] > 0.0, "u/d commutator zero")
    require(route_b["cross_lane_commutators"]["u_e_commutator_norm_sq"] == 0.0, "u/e same-lane commutator nonzero")
    require(route_b["cross_lane_commutators"]["d_nuD_commutator_norm_sq"] == 0.0, "d/nuD same-lane commutator nonzero")
    require(route_b["independent_rows_executed_now"] is False, "Route B rows overexecuted")
    require(route_b["selected_source_verified"] is False, "Route B source oververified")
    require(route_b["can_promote_to_route_b_closure"] is False, "Route B overpromoted")

    require(result["route_b_replay_rank_diagnostics_computed"] is True, "result diagnostic missing")
    require(result["route_b_diagnostic_tests_pass"] is True, "result diagnostics did not pass")
    require(result["route_a_physical_values_emitted"] is False, "result Route A overemitted")
    require(result["route_b_independent_rows_executed"] is False, "result Route B overexecuted")
    require(result["route_b_selected_source_verified"] is False, "result source oververified")
    require(result["unpatched_dynamic_C1_packet_closed"] is False, "result dynamic C1 overclosed")
    require(result["true_SM_equivalence_closed"] is False, "result true SM overclosed")
    require(result["no_knob_closed"] is False, "result no-knob overclosed")

    closure = data["closure_decision"]
    require(closure["route_b_replay_rank_diagnostics_computed"] is True, "candidate diagnostic missing")
    require(closure["route_a_physical_values_emitted"] is False, "candidate Route A overemitted")
    require(closure["route_b_independent_rows_executed"] is False, "candidate Route B overexecuted")
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
