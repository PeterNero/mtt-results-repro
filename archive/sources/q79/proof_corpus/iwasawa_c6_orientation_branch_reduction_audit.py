"""Audit the Iwasawa C6 orientation branch reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "iwasawa_c6_orientation_branch_reduction_certificate.json"
PAPER = ROOT / "Iwasawa_C6_Orientation_Branch_Reduction_v1.md"
SCRIPT = REPO / "scripts" / "analyze_iwasawa_c6_orientation_branch_reduction.py"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def run_analysis() -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stdout)
    return json.loads(proc.stdout)


def main() -> None:
    cert = load_json(CERT)
    paper = read(PAPER)
    analysis = run_analysis()
    calc = cert.get("calculation_results", {})
    closed = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    expected_branches = [
        "Q1_L1_R2_E2",
        "Q1_L2_R2_E1",
        "Q2_L1_R1_E2",
        "Q2_L2_R1_E1",
    ]
    expected_patterns = [
        [79, 79, 79, 79],
        [79, 79, 369, 369],
        [369, 369, 79, 79],
        [369, 369, 369, 369],
    ]
    expected_coherent_patterns = [
        [79, 79, 79, 79],
        [369, 369, 369, 369],
    ]

    gates = [
        Gate(
            "certificate status",
            "PASS"
            if cert.get("status") == "IWASAWA_C6_ORIENTATION_BRANCH_REDUCED_UNIQUE_BRANCH_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "branch count reduction",
            "PASS"
            if analysis.get("input_open_independent_C6_sign_choices") == 16
            and analysis.get("branch_count_after_qutrit_pairing_rule") == 4
            else "FAIL",
            str(
                (
                    analysis.get("input_open_independent_C6_sign_choices"),
                    analysis.get("branch_count_after_qutrit_pairing_rule"),
                )
            ),
        ),
        Gate(
            "branch names",
            "PASS" if analysis.get("branch_names") == expected_branches else "FAIL",
            str(analysis.get("branch_names")),
        ),
        Gate(
            "label patterns",
            "PASS"
            if analysis.get("left_representative_label_patterns") == expected_patterns
            else "FAIL",
            str(analysis.get("left_representative_label_patterns")),
        ),
        Gate(
            "conditional coherent pair",
            "PASS"
            if analysis.get("electroweak_doublet_coherent_branch_count") == 2
            and analysis.get("electroweak_doublet_coherent_label_patterns")
            == expected_coherent_patterns
            else "FAIL",
            str(analysis.get("electroweak_doublet_coherent_label_patterns")),
        ),
        Gate(
            "certificate calculation results",
            "PASS"
            if calc.get("input_open_independent_C6_sign_choices") == 16
            and calc.get("branch_count_after_qutrit_pairing_rule") == 4
            and calc.get("left_representative_label_patterns") == expected_patterns
            and calc.get("electroweak_doublet_coherent_label_patterns")
            == expected_coherent_patterns
            else "FAIL",
            str(calc),
        ),
        Gate(
            "closed reduction",
            "PASS" if all(value is True for value in closed.values()) else "FAIL",
            str(closed),
        ),
        Gate(
            "still open",
            "PASS" if all(value is True for value in still_open.values()) else "FAIL",
            str(still_open),
        ),
        Gate(
            "guardrails",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("C6_orientation_space_reduced") is True
            and verdict.get("independent_channel_orientation_knobs_removed") is True
            and verdict.get("unique_branch_selected") is False
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records reduction",
            "PASS"
            if contains_all(
                paper,
                [
                    "2^4 = 16",
                    "s_left+s_right=0 mod 3",
                    "Q1_L1_R2_E2",
                    "[369, 369, 369, 369]",
                    "unique MTT branch among global conjugates",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa C6 orientation branch-reduction audit")
    print("=============================================")
    print()
    print(f"branch_count={analysis.get('branch_count_after_qutrit_pairing_rule')}")
    print(
        "electroweak_doublet_coherent_branch_count="
        f"{analysis.get('electroweak_doublet_coherent_branch_count')}"
    )
    print(f"label_patterns={analysis.get('left_representative_label_patterns')}")
    print()

    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    failures = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
