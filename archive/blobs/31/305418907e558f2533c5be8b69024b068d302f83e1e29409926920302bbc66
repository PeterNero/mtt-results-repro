"""Audit the exact finite-algebra D closure of eight q79 symbolic lines."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "q79_Ronly_symbolic_finite_algebra_D_closure"
PARENTS = ROOT / "candidate_data" / "q79_Ronly_classfree_representative_lines"
VERIFIER = ROOT / "scripts" / "verify_q79_Ronly_symbolic_affine_quadratic_exception_D_unit_general.py"
CERTIFIER = ROOT / "scripts" / "certify_q79_Ronly_symbolic_finite_algebra_D_closure_v3.py"
CERTIFICATE = ROOT / "certificates" / "Q79_Ronly_Symbolic_Finite_Algebra_D_Closure_v3.json"
THEOREM = Path(__file__).with_name("Q79_Ronly_Symbolic_Finite_Algebra_D_Closure_v3.md")
SPECS = (
    (5, 1, 18, 2, 18, 24),
    (5, 2, 2, 6, 18, 36),
    (5, 2, 5, 3, 18, 45),
    (5, 2, 14, 6, 19, 37),
    (6, 1, 47, 6, 18, 56),
    (6, 2, 32, 2, 18, 92),
    (6, 2, 46, 6, 18, 79),
    (6, 2, 47, 1, 18, 26),
)


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT))


def main() -> None:
    required = [VERIFIER, CERTIFIER, CERTIFICATE, THEOREM]
    line_paths = []
    for space, scalar_class, a_value, _, _, _ in SPECS:
        stem = f"space{space}_class{scalar_class}_u1_001_a_{a_value:03d}_symbolic_v"
        line_paths.extend(
            [
                DATA / f"{stem}.input.packet.json",
                DATA / f"{stem}.msolve.in",
                DATA / f"{stem}.msolve.out",
                DATA / f"{stem}.msolve.log",
                DATA / f"{stem}.D_unit.certificate.json",
            ]
        )
    required.extend(line_paths)
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        print("Missing files:\n" + "\n".join(missing))
        raise SystemExit(1)

    regenerated_lines = []
    committed_lines = []
    line_runs = []
    with tempfile.TemporaryDirectory(prefix="q79-symbolic-finite-algebra-") as directory:
        temporary = Path(directory)
        for space, scalar_class, a_value, _, _, _ in SPECS:
            stem = f"space{space}_class{scalar_class}_u1_001_a_{a_value:03d}_symbolic_v"
            output = temporary / f"{stem}.json"
            command = [
                sys.executable,
                str(VERIFIER),
                "--parent",
                relative(PARENTS / f"space_{space}_h0_g0_class{scalar_class}_inverse_root.msolve.in"),
                "--symbolic-input",
                relative(DATA / f"{stem}.msolve.in"),
                "--input-packet",
                relative(DATA / f"{stem}.input.packet.json"),
                "--basis-output",
                relative(DATA / f"{stem}.msolve.out"),
                "--basis-log",
                relative(DATA / f"{stem}.msolve.log"),
                "--space",
                str(space),
                "--output",
                str(output),
            ]
            completed = subprocess.run(
                command,
                cwd=ROOT,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                check=False,
            )
            line_runs.append(completed)
            regenerated_lines.append(
                json.loads(output.read_text(encoding="utf-8"))
                if completed.returncode == 0 and output.is_file()
                else {}
            )
            committed_lines.append(
                json.loads((DATA / f"{stem}.D_unit.certificate.json").read_text(encoding="utf-8"))
            )

        summary_output = temporary / "summary.json"
        summary_run = subprocess.run(
            [sys.executable, str(CERTIFIER), "--output", str(summary_output)],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        regenerated_summary = (
            json.loads(summary_output.read_text(encoding="utf-8"))
            if summary_run.returncode == 0 and summary_output.is_file()
            else {}
        )

    committed_summary = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    theorem = THEOREM.read_text(encoding="utf-8")
    summaries = regenerated_summary.get("line_certificates", [])
    observed = [
        (
            row.get("space_index"),
            row.get("scalar_class"),
            row.get("a"),
            row.get("quotient_dimension"),
            row.get("D_unit_row"),
            row.get("D_multiplication_determinant"),
        )
        for row in summaries
    ]
    checks = regenerated_summary.get("checks", {})
    gates = [
        Gate("all artifacts present", "PASS", f"files={len(required)}"),
        Gate(
            "eight line verifiers rerun",
            "PASS" if all(run.returncode == 0 for run in line_runs) else "FAIL",
            "; ".join(run.stdout.splitlines()[-2] for run in line_runs),
        ),
        Gate(
            "all line certificates reproduce",
            "PASS" if regenerated_lines == committed_lines else "FAIL",
            "eight committed == regenerated",
        ),
        Gate(
            "summary certifier reruns",
            "PASS" if summary_run.returncode == 0 else "FAIL",
            summary_run.stdout[-180:].strip(),
        ),
        Gate(
            "summary certificate reproduces",
            "PASS" if regenerated_summary == committed_summary else "FAIL",
            "committed == regenerated",
        ),
        Gate(
            "exact symbolic status",
            "PASS"
            if regenerated_summary.get("status")
            == "EXACT_EIGHT_SYMBOLIC_LINES_AND_SIGN_PARTNERS_CLOSED_BY_D"
            else "FAIL",
            "eight canonical plus eight partners",
        ),
        Gate(
            "dimension and determinant table",
            "PASS" if observed == list(SPECS) else "FAIL",
            str(observed),
        ),
        Gate(
            "sixteen signed lines",
            "PASS"
            if regenerated_summary.get("signed_closure", {}).get("total_symbolic_lines_closed")
            == 16
            else "FAIL",
            "16",
        ),
        Gate(
            "all consolidated checks",
            "PASS" if len(checks) == 10 and all(checks.values()) else "FAIL",
            f"{sum(bool(value) for value in checks.values())}/10",
        ),
        Gate(
            "zero fit parameters",
            "PASS"
            if regenerated_summary.get("new_continuous_fit_parameters") == 0
            else "FAIL",
            "zero",
        ),
        Gate(
            "claim boundary retained",
            "PASS"
            if "all four space-6 canonical exceptions" in theorem
            and "remains `138/140`" in theorem
            and "No continuous fit parameter" in theorem
            else "FAIL",
            str(THEOREM),
        ),
    ]

    print("q79 symbolic finite-algebra D-closure v3 audit")
    print("================================================")
    width = max(len(gate.label) for gate in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:4s}  {gate.detail}")
    if any(gate.status == "FAIL" for gate in gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
