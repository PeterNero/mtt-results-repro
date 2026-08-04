"""Audit the class-free q79 R-only reduction and four exact endpoint lines."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "q79_Ronly_classfree_representative_lines"
SCRIPT = ROOT / "scripts" / "certify_q79_Ronly_classfree_representative_lines.py"
BENCHMARK = ROOT / "scripts" / "benchmark_q79_Ronly_representative_v_lines.py"
CERTIFICATE = (
    ROOT
    / "certificates"
    / "Q79_Ronly_ClassFree_Core_and_Representative_Lines_v1.json"
)
THEOREM = Path(__file__).with_name(
    "Q79_Ronly_ClassFree_Core_and_Representative_Lines_v1.md"
)


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def main() -> None:
    data_names = [
        f"space_{space}_h0_g0_class{scalar_class}_inverse_root.msolve.in"
        for space in (5, 6)
        for scalar_class in (1, 2)
    ]
    data_names += [
        f"space{space}_classfree_saturated_hR_core.msolve.in"
        for space in (5, 6)
    ]
    data_names += [
        f"space{space}_class{scalar_class}_u1_1_a_1_v_full_line.packet.json"
        for space in (5, 6)
        for scalar_class in (1, 2)
    ]
    required = [SCRIPT, BENCHMARK, CERTIFICATE, THEOREM] + [
        DATA / name for name in data_names
    ]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        print("Missing files:\n" + "\n".join(missing))
        raise SystemExit(1)

    with tempfile.TemporaryDirectory(prefix="q79-r-only-lines-") as directory:
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
    expected_status = "EXACT_FOUR_CHART_TO_TWO_CORES_AND_FOUR_LINES_CERTIFIED"
    totals = regenerated.get("totals", {})
    checks = regenerated.get("checks", {})
    gates = [
        Gate("all artifacts present", "PASS", f"files={len(required)}"),
        Gate(
            "consolidator reruns",
            "PASS" if completed.returncode == 0 else "FAIL",
            completed.stdout[-180:].strip(),
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
            "packet reproduces exactly",
            "PASS" if regenerated == committed else "FAIL",
            "committed == regenerated",
        ),
        Gate(
            "all exact checks",
            "PASS" if len(checks) == 12 and all(checks.values()) else "FAIL",
            f"{sum(bool(value) for value in checks.values())}/12",
        ),
        Gate(
            "four to two reduction",
            "PASS"
            if totals.get("nominal_scalar_charts") == 4
            and totals.get("class_free_cubic_cores") == 2
            else "FAIL",
            "4 charts -> 2 distinct cores",
        ),
        Gate(
            "literal unit fibers",
            "PASS"
            if totals.get("exactly_closed_fixed_endpoint_fibers") == 400
            else "FAIL",
            "400/400",
        ),
        Gate(
            "remaining line boundary",
            "PASS"
            if totals.get("remaining_unclassified_endpoint_lines") == 39996
            else "FAIL",
            "39,996 remain open",
        ),
        Gate(
            "D rows unused",
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
            if "39,996" in theorem
            and "does not classify" in theorem
            and "400/400" in theorem
            else "FAIL",
            str(THEOREM),
        ),
    ]

    print("q79 R-only class-free and representative-line audit")
    print("====================================================")
    width = max(len(gate.label) for gate in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:4s}  {gate.detail}")
    if any(gate.status == "FAIL" for gate in gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
