"""Audit the full U1/Y closure execution ladder."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_full_closure_execution_attempt.py"
DATA = REPO / "candidate_data" / "selected_u1y_full_closure_execution_attempt.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_full_closure_execution_attempt_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_Full_Closure_Execution_Attempt_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(name: str, condition: bool, detail: object) -> None:
    if condition:
        print(f"PASS: {name} -- {detail}")
        return
    print(f"FAIL: {name} -- {detail}")
    raise SystemExit(1)


def main() -> int:
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(proc.stdout)
    check("builder exits cleanly", proc.returncode == 0, proc.returncode)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    summary = data["execution_summary"]
    steps = data["steps"]
    first = data["first_blocker"]

    check(
        "status exact",
        data["status"] == "U1Y_FULL_CLOSURE_LADDER_EXECUTED_SOURCE_SOLVE_REMAINS_FIRST_BLOCKER",
        data["status"],
    )
    check(
        "all seven steps executed",
        summary["all_steps_executed"] is True and len(steps) == 7 and all(step["closed"] is False for step in steps),
        {"summary": summary, "step_count": len(steps)},
    )
    check(
        "source layer closed but full closure not claimed",
        summary["terminal_source_layer_closed"] is True
        and summary["selected_visible_bundle_or_routec_source_exists"] is False
        and summary["full_sm_or_no_knob_closure"] is False,
        summary,
    )
    check(
        "first blocker exact",
        first["name"] == "Selected_U1Y_Visible_Bundle_or_RouteC_Source_Solve_v1"
        and first["schema"] == "SelectedQaSU3RouteCSourceSolve.v1"
        and "selected_visible_sm_bundle_or_sheaf_model" in first["must_supply"],
        first,
    )
    check(
        "lambda remains blocked",
        data["what_remains_open"]["lambda_12"] is True
        and cert["lambda_12_closed"] is False
        and cert["full_closure_achieved"] is False,
        cert,
    )
    check(
        "note records full ladder and first blocker",
        "All planned closure steps have now been executed" in note
        and "Selected_U1Y_Visible_Bundle_or_RouteC_Source_Solve_v1" in note
        and "lambda_12_closed = false" in note,
        NOTE,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
