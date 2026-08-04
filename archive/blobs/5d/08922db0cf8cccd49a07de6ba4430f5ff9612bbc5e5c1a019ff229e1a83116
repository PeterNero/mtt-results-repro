"""Audit the visible active F3 image recovery obstruction."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "analyze_visible_active_f3_image_recovery.py"
CANDIDATE = REPO / "candidate_data" / "visible_active_f3_image_recovery_obstruction.candidate.json"
CERT = REPO / "certificates" / "visible_active_f3_image_recovery_obstruction_certificate.json"
PAPER = ROOT / "Visible_Active_F3_Image_Recovery_Obstruction_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def run_constructor() -> tuple[int, str]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return proc.returncode, proc.stdout


def main() -> None:
    code, output = run_constructor()
    cert = load_json(CERT)
    paper = read(PAPER)
    enumeration = cert.get("enumeration", {})
    guardrails = cert.get("guardrails", {})
    theorem = cert.get("theorem", {})
    source_hits = cert.get("source_hits", {})

    assignments = enumeration.get("all_assignments", [])
    all_divisor_failures_present = (
        isinstance(assignments, list)
        and len(assignments) == 9
        and all(item.get("all_three_coordinate_divisors_DD_zero") is False for item in assignments)
    )

    gates = [
        Gate(
            "constructor exits 0",
            "PASS" if code == 0 else "FAIL",
            output[:900],
        ),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", str(CANDIDATE)),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", str(CERT)),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", str(PAPER)),
        Gate(
            "status blocks naive coordinate route",
            "PASS"
            if cert.get("status")
            == "VISIBLE_ACTIVE_F3_IMAGE_RECOVERY_NAIVE_COORDINATE_ROUTE_BLOCKED"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "source hits present",
            "PASS"
            if all(all(section.values()) for section in source_hits.values())
            else "FAIL",
            str(source_hits),
        ),
        Gate(
            "nine coordinate assignments enumerated",
            "PASS" if enumeration.get("coordinate_tangent_assignment_count") == 9 else "FAIL",
            str(enumeration.get("coordinate_tangent_assignment_count")),
        ),
        Gate(
            "no assignment passes all divisors",
            "PASS"
            if enumeration.get("assignments_with_all_divisors_DD_zero") == 0
            and all_divisor_failures_present
            else "FAIL",
            str(
                {
                    "pass_count": enumeration.get("assignments_with_all_divisors_DD_zero"),
                    "best_failure_count": enumeration.get("best_failing_divisor_count"),
                }
            ),
        ),
        Gate(
            "curves split case distinguished",
            "PASS" if enumeration.get("split_assignments_with_all_curves_DD_zero") == 6 else "FAIL",
            str(enumeration.get("split_assignments_with_all_curves_DD_zero")),
        ),
        Gate(
            "theorem records pigeonhole proof",
            "PASS"
            if "same coordinate factor" in " ".join(theorem.get("proof", []))
            and "distinct coordinate factors" in " ".join(theorem.get("proof", []))
            else "FAIL",
            str(theorem),
        ),
        Gate(
            "guardrails prevent overclaim",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "paper states correct frontier",
            "PASS"
            if all(
                needle in paper
                for needle in [
                    "naive coordinate divisor active-image route",
                    "active F3^2 images for S1,S2,S3,Cij",
                    "does not close Freed-Witten",
                ]
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Visible active F3 image recovery obstruction audit")
    print("===================================================")
    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    failures: list[Gate] = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
