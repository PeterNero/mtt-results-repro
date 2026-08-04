"""Audit the three-lane selected U1/Y source-solve attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_visible_bundle_or_routec_source_solve_attempt.py"
DATA = REPO / "candidate_data" / "selected_u1y_visible_bundle_or_routec_source_solve_attempt.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_visible_bundle_or_routec_source_solve_attempt_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_Visible_Bundle_or_RouteC_Source_Solve_Attempt_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(name: str, condition: bool, detail: object) -> None:
    if condition:
        print(f"PASS: {name} -- {detail}")
        return
    print(f"FAIL: {name} -- {detail}")
    raise SystemExit(1)


def lane(data: dict, name: str) -> dict:
    for item in data["lanes"]:
        if item["name"] == name:
            return item
    raise KeyError(name)


def main() -> int:
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(proc.stdout)
    check("builder exits cleanly", proc.returncode == 0, proc.returncode)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    lane_a = lane(data, "LaneA_TypedMonad_SectionRing")
    lane_b = lane(data, "LaneB_RouteC_FiniteCochain")
    lane_c = lane(data, "LaneC_ProjectiveGerbe_LocalSystem")

    check(
        "status exact",
        data["status"] == "VISIBLE_BUNDLE_OR_ROUTEC_SOURCE_SOLVE_ATTEMPT_EXECUTED_FINITE_COHCHAIN_ROUTE_PRIORITIZED",
        data["status"],
    )
    check(
        "schema exact",
        data["schema"] == "SelectedQaSU3RouteCSourceSolve.v1"
        and "selected_visible_sm_bundle_or_sheaf_model" in data["required_fields"],
        data["required_fields"],
    )
    check(
        "all lanes executed but source not closed",
        data["decision"]["all_three_lanes_executed"] is True
        and data["decision"]["source_solve_closed"] is False
        and cert["source_solve_closed"] is False,
        data["decision"],
    )
    check(
        "lane B selected as next executable route",
        data["decision"]["best_next_lane"] == "LaneB_RouteC_FiniteCochain"
        and cert["best_next_lane"] == "LaneB_RouteC_FiniteCochain"
        and data["decision"]["next_artifact_to_build"] == "Selected_U1Y_RouteC_Finite_Cochain_Source_Construct_v1",
        cert,
    )
    check(
        "lane A remains blocked at section-ring data",
        lane_a["status"] == "PARTIAL_SELECTED_SOURCE_SOLVE"
        and lane_a["blockers"]["section_ring"] == "FAIL_INTERFACE_ONLY_VALUES_OPEN"
        and lane_a["blockers"]["operator_exit"] == "FAIL_NOT_AVAILABLE",
        lane_a["blockers"],
    )
    check(
        "lane B has residual shape but lacks source verification",
        lane_b["status"] == "PARTIAL_SELECTED_SOURCE_SOLVE"
        and lane_b["filled_fields"]["route_c_residual_packet_with_selected_source_verified"][
            "honest_residual_zero_shape_available"
        ]
        is True
        and lane_b["filled_fields"]["route_c_residual_packet_with_selected_source_verified"][
            "honest_selected_source_verified"
        ]
        is False,
        lane_b["filled_fields"]["route_c_residual_packet_with_selected_source_verified"],
    )
    check(
        "lane C retains gerbe route as partial but response open",
        lane_c["status"] == "PARTIAL_SELECTED_SOURCE_SOLVE"
        and lane_c["evidence"]["twist_cancellation_table_filled"] is True
        and lane_c["blockers"]["finite_response"] is False,
        lane_c,
    )
    check(
        "lambda and full closure not claimed",
        cert["full_sm_or_lambda12_closed"] is False
        and data["target_fitting_used"] is False,
        cert,
    )
    check(
        "note records next construct and guardrails",
        "Selected_U1Y_RouteC_Finite_Cochain_Source_Construct_v1" in note
        and "source_solve_closed = false" in note
        and "formal-lift selected flags" in note,
        NOTE,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
