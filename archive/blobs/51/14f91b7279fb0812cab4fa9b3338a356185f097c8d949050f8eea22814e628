"""Audit the exact q79 fixed-u1 u2/Laurent-line acceleration theorem."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VERIFIER = ROOT / "scripts" / "verify_q79_Ronly_u2_laurent_line_acceleration.py"
CERTIFICATE = ROOT / "certificates" / "Q79_Ronly_U2_Laurent_Line_Acceleration_v1.json"
THEOREM = Path(__file__).with_name("Q79_Ronly_U2_Laurent_Line_Acceleration_v1.md")


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def main() -> None:
    required = [VERIFIER, CERTIFICATE, THEOREM]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        print("Missing files:\n" + "\n".join(missing))
        raise SystemExit(1)

    with tempfile.TemporaryDirectory(prefix="q79-u2-laurent-line-") as directory:
        output = Path(directory) / "certificate.json"
        completed = subprocess.run(
            [sys.executable, str(VERIFIER), "--output", str(output)],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        regenerated = (
            json.loads(output.read_text(encoding="utf-8"))
            if completed.returncode == 0 and output.is_file()
            else {}
        )

    committed = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    coordinate = regenerated.get("canonical_coordinate_bijection", {})
    laurent = regenerated.get("Laurent_line_isomorphism", {})
    reduction = regenerated.get("solver_reduction_per_fixed_nonzero_u1", {})
    checks = regenerated.get("checks", {})
    theorem = THEOREM.read_text(encoding="utf-8")
    gates = [
        Gate("all artifacts present", "PASS", f"files={len(required)}"),
        Gate(
            "verifier reruns",
            "PASS" if completed.returncode == 0 else "FAIL",
            completed.stdout[-160:].strip(),
        ),
        Gate(
            "certificate reproduces",
            "PASS" if regenerated == committed else "FAIL",
            "committed == regenerated",
        ),
        Gate(
            "exact status",
            "PASS"
            if regenerated.get("status")
            == "EXACT_FIXED_U1_U2_LAURENT_LINE_COMPRESSION_CERTIFIED"
            else "FAIL",
            "coordinate compression",
        ),
        Gate(
            "canonical u2 bijection",
            "PASS"
            if len(coordinate.get("forward_table", [])) == 100
            and len(coordinate.get("inverse_table", {})) == 100
            else "FAIL",
            "100 canonical pairs <-> 100 nonzero u2 values",
        ),
        Gate(
            "Laurent inverse checks",
            "PASS" if laurent.get("finite_inverse_checks") == 10_000 else "FAIL",
            "10000/10000",
        ),
        Gate(
            "workload reduction",
            "PASS"
            if reduction.get("old_canonical_fixed_fibers") == 20_000
            and reduction.get("new_symbolic_u3_lines") == 200
            and reduction.get("fixed_fibers_represented_per_symbolic_line") == 100
            else "FAIL",
            "20000 fixed fibers -> 200 symbolic lines",
        ),
        Gate(
            "all exact checks",
            "PASS" if len(checks) == 10 and all(checks.values()) else "FAIL",
            f"{sum(bool(value) for value in checks.values())}/10",
        ),
        Gate(
            "zero fit parameters",
            "PASS" if regenerated.get("new_continuous_fit_parameters") == 0 else "FAIL",
            "zero",
        ),
        Gate(
            "theorem retains boundary",
            "PASS"
            if "not an emptiness result" in theorem
            and "complete `R/y/D` closure must be proved separately" in theorem
            else "FAIL",
            str(THEOREM),
        ),
    ]

    print("q79 u2 Laurent-line acceleration audit")
    print("========================================")
    width = max(len(gate.label) for gate in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:4s}  {gate.detail}")
    if any(gate.status == "FAIL" for gate in gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
