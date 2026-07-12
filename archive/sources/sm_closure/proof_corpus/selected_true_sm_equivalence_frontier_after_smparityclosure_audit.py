"""Audit true-SM-equivalence frontier after SM-parity closure."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_true_sm_equivalence_frontier_after_smparityclosure"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
FRONTIER = PACKET_DIR / "true_sm_equivalence_frontier_matrix.packet.json"
PLAN = PACKET_DIR / "next_executable_superset_plan.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_TrueSMEquivalenceFrontier_AfterSMParityClosure_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_TRUE_SM_EQUIVALENCE_FRONTIER_AFTER_SMPARITYCLOSURE_BUILT"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    frontier = load(FRONTIER)
    plan = load(PLAN)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(frontier["starting_point"]["SM_parity_closed"] is True, "SM parity should start closed")
    require(frontier["starting_point"]["true_SM_equivalence_closed"] is False, "true equivalence overclaimed")
    require(frontier["starting_point"]["no_knob_closed"] is False, "no-knob overclaimed")
    require(frontier["starting_point"]["current_SM_parity_blockers"] == [], "SM-parity blockers should be empty")
    require(frontier["guardrails"]["do_not_reopen_SM_parity_as_if_failed"] is True, "SM-parity guard missing")
    require(frontier["guardrails"]["observed_data_used_as_selector"] is False, "observed selector violation")
    require(frontier["guardrails"]["target_fitting_used"] is False, "target fitting violation")
    require(frontier["guardrails"]["no_knob_claimed"] is False, "no-knob overclaimed")

    gates = {gate["id"]: gate for gate in frontier["true_equivalence_gates"]}
    for gate in [
        "precision_empirical_replay_suite",
        "local_qft_observable_functor",
        "qm_gr_measurement_and_born_record_interfaces",
        "actual_qasu3_operator_packet_upgrade",
        "no_knob_constants",
    ]:
        require(gate in gates, f"missing gate: {gate}")
    require(gates["precision_empirical_replay_suite"]["status"] == "OPEN_PRIMARY_NEXT", "primary gate mismatch")
    require("superset_strategy" in gates["precision_empirical_replay_suite"], "primary gate missing superset strategy")

    require(plan["selected_next_gate"] == "precision_empirical_replay_suite", "selected next gate mismatch")
    require(len(plan["work_items"]) == 5, "work item count mismatch")
    require(plan["parallel_superset_lane"]["id"] == "actual_qasu3_operator_packet_upgrade", "parallel lane mismatch")
    require(plan["observed_data_used_as_selector"] is False, "plan observed selector violation")
    require(plan["target_fitting_used"] is False, "plan target fitting violation")

    require(data["closure_decision"]["SM_parity_closed"] is True, "candidate SM-parity flag mismatch")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "candidate true equivalence overclaimed")
    require(data["closure_decision"]["no_knob_closed"] is False, "candidate no-knob overclaimed")
    require(data["what_closes_now"]["precision_empirical_replay_suite_selected_as_next_gate"] is True, "next gate flag missing")
    require(cert["selected_next_gate"] == "precision_empirical_replay_suite", "cert next gate mismatch")
    require("superset strategy" in note, "note missing superset strategy")
    require("precision_empirical_replay_suite" in note, "note missing next gate")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
