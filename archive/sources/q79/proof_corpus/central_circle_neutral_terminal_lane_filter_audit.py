"""Audit the central-circle-neutral terminal lane filter."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "prove_central_circle_neutral_terminal_lane_filter.py"
CERT = REPO / "certificates" / "central_circle_neutral_terminal_lane_filter_certificate.json"
CANDIDATE = REPO / "candidate_data" / "central_circle_neutral_terminal_lane_filter.candidate.json"
PAPER = ROOT / "Central_Circle_Neutral_Terminal_Lane_Filter_v1.md"


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

    support = cert.get("corpus_support", {})
    terminal = cert.get("terminal_lane_filter", {})
    theorem = cert.get("conditional_theorem", {})
    closes = cert.get("what_this_closes", {})
    does_not_close = cert.get("what_this_does_not_close", {})
    guardrails = cert.get("guardrails", {})

    selected = terminal.get("selected_by_filter", {})

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", CERT),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", CANDIDATE),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", PAPER),
        Gate(
            "status selector open",
            "PASS"
            if cert.get("status")
            == "CENTRAL_CIRCLE_NEUTRAL_TERMINAL_LANE_FILTER_PROVED_SELECTOR_OPEN"
            else "FAIL",
            cert.get("status"),
        ),
        Gate(
            "candidate mirrors cert",
            "PASS"
            if candidate.get("status") == cert.get("status")
            and candidate.get("conditional_theorem") == theorem
            else "FAIL",
            candidate.get("status"),
        ),
        Gate(
            "central corpus supports filter",
            "PASS"
            if support.get("supported") is True
            and all(support.get("checks", {}).values())
            else "FAIL",
            support,
        ),
        Gate(
            "unique zero central label",
            "PASS"
            if terminal.get("unique_zero_central") is True
            and terminal.get("zero_central_labels") == ["L3-K2"]
            else "FAIL",
            terminal.get("zero_central_labels"),
        ),
        Gate(
            "filter forces target",
            "PASS"
            if terminal.get("filter_forces_target") is True
            and selected.get("value") == [1, -2, 0]
            and selected.get("double_value") == [2, -4, 0]
            and selected.get("dual_matches_printed_g_type") is True
            else "FAIL",
            selected,
        ),
        Gate(
            "conditional theorem proved",
            "PASS"
            if theorem.get("proved") is True
            and "terminal monad differences L_i-K2" in theorem.get("statement", "")
            else "FAIL",
            theorem,
        ),
        Gate(
            "closes only central filter",
            "PASS"
            if closes.get("central_circle_neutrality_filter_inside_terminal_lane") is True
            and closes.get("central_neutrality_no_longer_an_unchecked_subassumption")
            is True
            else "FAIL",
            closes,
        ),
        Gate(
            "does not overclose selector",
            "PASS"
            if does_not_close.get("actual_terminal_monad_lane_source_principle") is False
            and does_not_close.get("same_source_D_E_dotD_Riesz_Green") is False
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
            "paper records theorem",
            "PASS"
            if contains_all(
                paper,
                [
                    "central-circle-neutral filter",
                    "unique zero-central terminal difference is L3-K2",
                    "does not prove that MTT selects the terminal lane",
                    "Terminal_Map_Source_Principle_and_Base_Order.v1",
                ],
            )
            else "FAIL",
            PAPER,
        ),
    ]

    print("Central-circle-neutral terminal lane filter audit")
    print("================================================")
    width = max(len(gate.label) for gate in gates)
    failures: list[Gate] = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:4s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
