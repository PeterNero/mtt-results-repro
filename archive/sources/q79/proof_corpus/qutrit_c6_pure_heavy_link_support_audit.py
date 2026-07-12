"""Audit the pure qutrit/C6 heavy-link support calculation."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "qutrit_c6_pure_heavy_link_support_certificate.json"
PAPER = ROOT / "Qutrit_C6_Pure_Heavy_Link_Support_v1.md"
SCRIPT = REPO / "scripts" / "analyze_qutrit_c6_pure_heavy_link_support.py"


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
    supports = analysis.get("conjugate_pair_supports", {})
    consequence = analysis.get("pure_c6_consequence", {})
    not_ruled_out = analysis.get("not_ruled_out", {})
    guardrails = analysis.get("guardrails", {})
    verdict = analysis.get("verdict", {})
    closed = cert.get("what_this_closes", {})
    cert_open = cert.get("still_open", {})
    cert_guardrails = cert.get("guardrails", {})
    cert_verdict = cert.get("verdict", {})

    identity_support = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    gates = [
        Gate(
            "certificate status",
            "PASS"
            if cert.get("status")
            == "QUTRIT_C6_PURE_HEAVY_LINK_SUPPORT_OBSTRUCTED_DIFFERENTIAL_RESPONSE_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "script exists",
            "PASS" if SCRIPT.exists() and "heavy_link_entries_13_23" in read(SCRIPT) else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "conjugate supports diagonal",
            "PASS"
            if supports.get("1+2", {}).get("support_matrix") == identity_support
            and supports.get("2+1", {}).get("support_matrix") == identity_support
            and supports.get("1+2", {}).get("fixed_dimension") == 1
            and supports.get("2+1", {}).get("fixed_dimension") == 1
            else "FAIL",
            str(supports),
        ),
        Gate(
            "heavy links zero",
            "PASS"
            if supports.get("1+2", {}).get("heavy_link_entries_13_23") == [0, 0]
            and supports.get("2+1", {}).get("heavy_link_entries_13_23") == [0, 0]
            and consequence.get("pure_finite_qutrit_C6_delta_c") == [0, 0]
            else "FAIL",
            str(consequence),
        ),
        Gate(
            "pure C6 cannot close",
            "PASS"
            if consequence.get("conjugate_pair_support_is_diagonal") is True
            and consequence.get("conjugate_pair_heavy_links_zero") is True
            and consequence.get("pure_finite_qutrit_C6_can_close_leading_CKM_gate") is False
            else "FAIL",
            str(consequence),
        ),
        Gate(
            "certificate calculation results",
            "PASS"
            if calc.get("support_1_plus_2") == identity_support
            and calc.get("support_2_plus_1") == identity_support
            and calc.get("conjugate_pair_heavy_links_zero") is True
            and calc.get("pure_finite_qutrit_C6_delta_c") == [0, 0]
            and calc.get("pure_finite_qutrit_C6_can_close_leading_CKM_gate") is False
            else "FAIL",
            str(calc),
        ),
        Gate(
            "not ruled out",
            "PASS" if all(value is True for value in not_ruled_out.values()) else "FAIL",
            str(not_ruled_out),
        ),
        Gate(
            "analysis guardrails",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "closed fields",
            "PASS" if all(value is True for value in closed.values()) else "FAIL",
            str(closed),
        ),
        Gate(
            "still open",
            "PASS" if all(value is True for value in cert_open.values()) else "FAIL",
            str(cert_open),
        ),
        Gate(
            "certificate guardrails",
            "PASS" if all(value is False for value in cert_guardrails.values()) else "FAIL",
            str(cert_guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("pure_finite_qutrit_C6_heavy_link_obstructed") is True
            and verdict.get("c6_only_route_retired_for_leading_heavy_links") is True
            and cert_verdict.get("pure_finite_qutrit_C6_heavy_link_obstructed") is True
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records result",
            "PASS"
            if contains_all(
                paper,
                [
                    "unique invariant support for each conjugate nontrivial pair",
                    "M_13 = 0",
                    "Delta_c = c_d - c_u = (0,0)",
                    "global q79 phase + qutrit finite pairing -> CKM heavy-link support",
                    "selected differential response",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Qutrit C6 pure heavy-link support audit")
    print("=======================================")
    print()
    print(f"support_1+2={supports.get('1+2', {}).get('support_matrix')}")
    print(f"support_2+1={supports.get('2+1', {}).get('support_matrix')}")
    print(f"pure_delta_c={consequence.get('pure_finite_qutrit_C6_delta_c')}")
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
