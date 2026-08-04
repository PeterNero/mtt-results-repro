"""Audit the C6 common-holonomy branch-pair reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "iwasawa_c6_common_holonomy_branch_pair_certificate.json"
PAPER = ROOT / "Iwasawa_C6_Common_Holonomy_Branch_Pair_v1.md"
SOURCE = ROOT / "18 Theta-Closure & Execution Program_v3_corrected.md"
SCRIPT = REPO / "scripts" / "analyze_iwasawa_c6_common_holonomy_branch_pair.py"


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
    source = read(SOURCE)
    analysis = run_analysis()
    calc = cert.get("calculation_results", {})
    closed = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    expected_pair = ["Q1_L1_R2_E2", "Q2_L2_R1_E1"]
    expected_rejected = ["Q1_L2_R2_E1", "Q2_L1_R1_E2"]
    expected_patterns = [[79, 79, 79, 79], [369, 369, 369, 369]]

    gates = [
        Gate(
            "certificate status",
            "PASS"
            if cert.get("status")
            == "IWASAWA_C6_COMMON_HOLONOMY_REDUCES_TO_GLOBAL_CONJUGATE_PAIR"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "corpus source",
            "PASS"
            if contains_all(
                source,
                [
                    "L_{12}\\otimes L_{23}\\otimes L_{31}\\cong\\mathbb C",
                    "quark and lepton phases may not be assigned independently",
                ],
            )
            else "FAIL",
            str(SOURCE),
        ),
        Gate(
            "branch pair reduction",
            "PASS"
            if analysis.get("input_branch_count") == 4
            and analysis.get("common_holonomy_branch_count") == 2
            and analysis.get("rejected_mixed_quark_lepton_branch_count") == 2
            else "FAIL",
            str(
                (
                    analysis.get("input_branch_count"),
                    analysis.get("common_holonomy_branch_count"),
                    analysis.get("rejected_mixed_quark_lepton_branch_count"),
                )
            ),
        ),
        Gate(
            "surviving pair",
            "PASS"
            if analysis.get("common_holonomy_branch_names") == expected_pair
            else "FAIL",
            str(analysis.get("common_holonomy_branch_names")),
        ),
        Gate(
            "rejected mixed branches",
            "PASS"
            if analysis.get("rejected_mixed_branch_names") == expected_rejected
            else "FAIL",
            str(analysis.get("rejected_mixed_branch_names")),
        ),
        Gate(
            "global label patterns",
            "PASS"
            if analysis.get("global_conjugate_label_patterns") == expected_patterns
            else "FAIL",
            str(analysis.get("global_conjugate_label_patterns")),
        ),
        Gate(
            "certificate calculation results",
            "PASS"
            if calc.get("common_holonomy_branch_names") == expected_pair
            and calc.get("rejected_mixed_branch_names") == expected_rejected
            and calc.get("global_conjugate_label_patterns") == expected_patterns
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
            if verdict.get("C6_branch_space_now_global_conjugate_pair") is True
            and verdict.get("independent_quark_lepton_phase_knob_removed") is True
            and verdict.get("unique_orientation_convention_selected") is False
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records branch pair",
            "PASS"
            if contains_all(
                paper,
                [
                    "quark and lepton phases may not be assigned independently",
                    "Q1_L2_R2_E1  rejected",
                    "[79, 79, 79, 79]",
                    "which global conjugate convention is selected",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa C6 common-holonomy branch-pair audit")
    print("============================================")
    print()
    print(f"surviving_pair={analysis.get('common_holonomy_branch_names')}")
    print(f"label_patterns={analysis.get('global_conjugate_label_patterns')}")
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
