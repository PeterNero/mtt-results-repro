"""Audit the monad-difference Pic0/source-switch reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "prove_monad_difference_pic0_switch_reduction.py"
CERT = REPO / "certificates" / "monad_difference_pic0_switch_reduction_certificate.json"
CANDIDATE = REPO / "candidate_data" / "monad_difference_pic0_switch_reduction.candidate.json"
PAPER = ROOT / "Monad_Difference_Pic0_Source_Switch_Reduction_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: object


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def run_script() -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def main() -> int:
    proc = run_script()
    cert = load(CERT)
    candidate = load(CANDIDATE)
    paper = read(PAPER)

    by_case = {case.get("case"): case for case in cert.get("switch_table", [])}
    closes = cert.get("what_this_closes", {})
    does_not_close = cert.get("what_this_does_not_close", {})
    guardrails = cert.get("guardrails", {})
    comparison = cert.get("comparison_to_constants", {})

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", CERT),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", CANDIDATE),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", PAPER),
        Gate(
            "status reduction proved",
            "PASS"
            if cert.get("status")
            == "MONAD_DIFFERENCE_PIC0_SWITCH_REDUCTION_PROVED_SOURCE_OPEN"
            else "FAIL",
            cert.get("status"),
        ),
        Gate(
            "candidate mirrors certificate",
            "PASS"
            if candidate.get("status") == cert.get("status")
            and candidate.get("switch_table") == cert.get("switch_table")
            else "FAIL",
            candidate.get("status"),
        ),
        Gate(
            "none case open",
            "OPEN" if by_case.get("none", {}).get("validator_status") == "OPEN" else "FAIL",
            by_case.get("none"),
        ),
        Gate(
            "Pic0 only still needs source",
            "OPEN"
            if by_case.get("pic0_only", {}).get("validator_status") == "OPEN"
            and "source.selected_by_mtt is not true"
            in by_case.get("pic0_only", {}).get("open_items", [])
            and "Pic0 resolution rule missing"
            not in by_case.get("pic0_only", {}).get("open_items", [])
            else "FAIL",
            by_case.get("pic0_only"),
        ),
        Gate(
            "source only still needs Pic0",
            "OPEN"
            if by_case.get("source_only", {}).get("validator_status") == "OPEN"
            and "Pic0 resolution rule missing"
            in by_case.get("source_only", {}).get("open_items", [])
            and "source.selected_by_mtt is not true"
            not in by_case.get("source_only", {}).get("open_items", [])
            else "FAIL",
            by_case.get("source_only"),
        ),
        Gate(
            "both switches pass",
            "PASS"
            if by_case.get("source_and_pic0", {}).get("exit_code") == 0
            and by_case.get("source_and_pic0", {}).get("open_items") == []
            else "FAIL",
            by_case.get("source_and_pic0"),
        ),
        Gate(
            "constants agrees",
            "PASS" if comparison.get("constants_agrees") is True else "FAIL",
            comparison,
        ),
        Gate(
            "closes exact reduction",
            "PASS"
            if closes.get("source_switch_is_independently_required") is True
            and closes.get("pic0_switch_is_independently_required") is True
            and closes.get("ordered_source_matrix_not_the_blocker") is True
            else "FAIL",
            closes,
        ),
        Gate(
            "does not overclose",
            "PASS"
            if does_not_close.get("actual_MTT_selection_of_L3_minus_K2") is False
            and does_not_close.get("actual_Pic0_selection_or_physical_quotient") is False
            and does_not_close.get("full_SM_closure") is False
            else "FAIL",
            does_not_close,
        ),
        Gate(
            "guardrails",
            "PASS" if guardrails and all(value is False for value in guardrails.values()) else "FAIL",
            guardrails,
        ),
        Gate(
            "paper records switch theorem",
            "PASS"
            if contains_all(
                paper,
                [
                    "two-switch reduction",
                    "Pic0-only",
                    "source-only",
                    "both switches pass",
                    "not a proof of either switch",
                ],
            )
            else "FAIL",
            PAPER,
        ),
    ]

    print("Monad-difference Pic0/source-switch reduction audit")
    print("===================================================")
    width = max(len(gate.label) for gate in gates)
    failures: list[Gate] = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:4s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
