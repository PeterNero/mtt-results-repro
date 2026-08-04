"""Audit the split line/Cartan HYM no-go packet."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "prove_visible_split_line_hym_no_go.py"
CANDIDATE = REPO / "candidate_data" / "visible_split_line_hym_no_go.candidate.json"
CERT = REPO / "certificates" / "visible_split_line_hym_no_go_certificate.json"
PAPER = ROOT / "Visible_Split_Line_HYM_No_Go_for_Positive_Alpha1_Source_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def main() -> int:
    proc = run([sys.executable, str(SCRIPT)])
    cert = load_json(CERT)
    candidate = load_json(CANDIDATE)
    paper = read(PAPER)
    target = cert.get("target", {})
    no_go = cert.get("algebraic_no_go", {})
    calc = cert.get("calculation_results", {})
    closes = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", str(CERT)),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", str(CANDIDATE)),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", str(PAPER)),
        Gate(
            "status no-go",
            "PASS"
            if cert.get("status")
            == "VISIBLE_SPLIT_LINE_HYM_SOURCE_NO_GO_NONABELIAN_OR_ROUTE_C_REQUIRED"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "candidate mirrors certificate",
            "PASS"
            if candidate.get("status") == cert.get("status")
            and candidate.get("calculation_results") == cert.get("calculation_results")
            else "FAIL",
            str(CANDIDATE),
        ),
        Gate(
            "target row",
            "PASS"
            if target.get("standard_chern_character_row") == [4, 0, 0]
            and "8*(2*pi)^2 alpha_1" in target.get("chern_weil_trace_row", "")
            else "FAIL",
            str(target),
        ),
        Gate(
            "algebraic contradiction",
            "PASS"
            if no_go.get("hym_implies") == "S p=0"
            and no_go.get("target_off_diagonal_entries") == {"S12": 4, "S13": 0, "S23": 0}
            and no_go.get("first_component_contradiction") == "S11*p1 + 4*p2 > 0"
            and no_go.get("split_line_hym_source_exists") is False
            else "FAIL",
            str(no_go),
        ),
        Gate(
            "calculation scoped",
            "PASS"
            if calc.get("split_line_or_cartan_hym_source_ruled_out") is True
            and calc.get("nonabelian_stable_bundle_ruled_out") is False
            and calc.get("route_c_solve_ruled_out") is False
            and closes.get("remaining_source_class_reduced_to_nonabelian_or_route_c") is True
            else "FAIL",
            str({"calc": calc, "closes": closes}),
        ),
        Gate(
            "nonabelian/route-c open",
            "OPEN"
            if still_open.get("selected_nonabelian_stable_bundle_or_sheaf_with_c1_0_ch2_4_alpha1")
            is True
            and still_open.get("selected_route_c_residual_solve_for_same_class") is True
            else "FAIL",
            str(still_open),
        ),
        Gate("guardrails", "PASS" if all(value is False for value in guardrails.values()) else "FAIL", str(guardrails)),
        Gate(
            "paper records theorem",
            "PASS"
            if contains_all(
                paper,
                [
                    "S p = 0",
                    "S11*p1 + 4*p2 > 0",
                    "split line-bundle",
                    "nonabelian stable",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Visible split line HYM no-go audit")
    print("==================================")
    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    failures: list[Gate] = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
