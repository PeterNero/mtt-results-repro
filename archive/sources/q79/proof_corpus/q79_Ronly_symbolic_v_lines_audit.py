"""Audit the four exact symbolic-v q79 R-only unit ideals."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "q79_Ronly_symbolic_v_lines"
SCRIPT = ROOT / "scripts" / "certify_q79_Ronly_symbolic_v_lines.py"
EMITTER = ROOT / "scripts" / "emit_q79_Ronly_symbolic_v_line.py"
CERTIFICATE = ROOT / "certificates" / "Q79_Ronly_Symbolic_V_Lines_v1.json"
THEOREM = Path(__file__).with_name("Q79_Ronly_Symbolic_V_Lines_v1.md")


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def main() -> None:
    artifact_names = []
    for space in (5, 6):
        for scalar_class in (1, 2):
            stem = f"space{space}_class{scalar_class}_u1_001_a_001_symbolic_v"
            artifact_names.extend(
                [
                    f"{stem}.input.packet.json",
                    f"{stem}.msolve.in",
                    f"{stem}.msolve.log",
                    f"{stem}.msolve.out",
                ]
            )
    required = [SCRIPT, EMITTER, CERTIFICATE, THEOREM] + [
        DATA / name for name in artifact_names
    ]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        print("Missing files:\n" + "\n".join(missing))
        raise SystemExit(1)

    with tempfile.TemporaryDirectory(prefix="q79-symbolic-v-lines-") as directory:
        regenerated_path = Path(directory) / "certificate.json"
        completed = subprocess.run(
            [sys.executable, str(SCRIPT), "--output", str(regenerated_path)],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        regenerated = (
            json.loads(regenerated_path.read_text(encoding="utf-8"))
            if completed.returncode == 0 and regenerated_path.is_file()
            else {}
        )

    committed = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    theorem = THEOREM.read_text(encoding="utf-8")
    expected_status = "EXACT_FOUR_SYMBOLIC_V_LINES_UNIT_OVER_ALGEBRAIC_CLOSURE"
    checks = regenerated.get("checks", {})
    totals = regenerated.get("totals", {})
    records = regenerated.get("line_records", [])
    gates = [
        Gate("all artifacts present", "PASS", f"files={len(required)}"),
        Gate(
            "certifier reruns",
            "PASS" if completed.returncode == 0 else "FAIL",
            completed.stdout[-200:].strip(),
        ),
        Gate(
            "committed status",
            "PASS" if committed.get("status") == expected_status else "FAIL",
            expected_status,
        ),
        Gate(
            "regenerated status",
            "PASS" if regenerated.get("status") == expected_status else "FAIL",
            expected_status,
        ),
        Gate(
            "certificate reproduces",
            "PASS" if regenerated == committed else "FAIL",
            "committed == regenerated",
        ),
        Gate(
            "all exact checks",
            "PASS" if len(checks) == 12 and all(checks.values()) else "FAIL",
            f"{sum(bool(value) for value in checks.values())}/12",
        ),
        Gate(
            "four symbolic line records",
            "PASS"
            if len(records) == 4
            and all(row.get("result") == "UNIT_IDEAL_OVER_F101" for row in records)
            else "FAIL",
            "4/4 literal unit ideals",
        ),
        Gate(
            "solver exits are exact",
            "PASS"
            if all(row.get("execution", {}).get("exit_status") == 0 for row in records)
            else "FAIL",
            "four exit-zero logs",
        ),
        Gate(
            "finite points subsumed",
            "PASS" if totals.get("finite_F101_points_subsumed") == 400 else "FAIL",
            "400 predecessor fibers",
        ),
        Gate(
            "line accounting unchanged",
            "PASS"
            if totals.get("remaining_unclassified_endpoint_lines") == 39996
            else "FAIL",
            "39,996 remain open",
        ),
        Gate(
            "no D rows",
            "PASS" if checks.get("no_D_terminal_row_is_used") else "FAIL",
            "R-only",
        ),
        Gate(
            "no fit parameters",
            "PASS"
            if regenerated.get("new_continuous_fit_parameters") == 0
            else "FAIL",
            "zero",
        ),
        Gate(
            "claim boundary saved",
            "PASS"
            if "characteristic-101" in theorem
            and "39,996" in theorem
            and "does not classify" in theorem
            else "FAIL",
            str(THEOREM),
        ),
    ]

    print("q79 R-only symbolic-v line audit")
    print("==================================")
    width = max(len(gate.label) for gate in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:4s}  {gate.detail}")
    if any(gate.status == "FAIL" for gate in gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
