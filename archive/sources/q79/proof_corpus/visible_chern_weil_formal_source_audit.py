"""Audit the formal visible Chern-Weil source construction."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "construct_visible_chern_weil_formal_source.py"
CANDIDATE = REPO / "candidate_data" / "visible_chern_weil_formal_source.candidate.json"
CERT = REPO / "certificates" / "visible_chern_weil_formal_source_certificate.json"
PAPER = ROOT / "Visible_Chern_Weil_Formal_Source_v1.md"


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
    source = cert.get("formal_trace_free_source", {})
    calc = cert.get("calculation_results", {})
    closes = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})

    gates = [
        Gate("constructor exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", str(CERT)),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", str(CANDIDATE)),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", str(PAPER)),
        Gate(
            "status formal row realized",
            "PASS"
            if cert.get("status")
            == "VISIBLE_CHERN_WEIL_FORMAL_SOURCE_ROW_REALIZED_SELECTION_OPEN"
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
            "trace-free formal source",
            "PASS"
            if source.get("rank") == 2
            and source.get("trace_free") is True
            and source.get("matches_required_row") is True
            and source.get("trace_F_squared", {}).get("row")
            == ["8*r3^2/(r1^2*r2^2) + 4*r3^2", "0", "0"]
            else "FAIL",
            str(source),
        ),
        Gate(
            "row obstruction retired",
            "PASS"
            if calc.get("no_algebraic_chern_weil_row_obstruction") is True
            and closes.get("formal_trace_free_Chern_Weil_row_realizability") is True
            else "FAIL",
            str({"calc": calc, "closes": closes}),
        ),
        Gate(
            "selection remains open",
            "OPEN"
            if still_open.get("integral_quantized_bundle_or_sheaf_class") is True
            and still_open.get("stable_visible_bundle_or_sheaf_model") is True
            and still_open.get("HYM_or_Route_C_residual") is True
            and still_open.get("sector_D_E_dotD_Riesz_Green") is True
            else "FAIL",
            str(still_open),
        ),
        Gate("guardrails", "PASS" if all(value is False for value in guardrails.values()) else "FAIL", str(guardrails)),
        Gate(
            "paper records scope",
            "PASS"
            if contains_all(
                paper,
                [
                    "formal trace-free Chern-Weil row realizability",
                    "Tr F^2",
                    "integral quantized bundle or sheaf class",
                    "not yet a selected",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Visible Chern-Weil formal source audit")
    print("=======================================")
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
