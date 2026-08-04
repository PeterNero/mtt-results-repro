"""Audit the discrete gerbe holonomy candidate calculation."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT_DIR = REPO / "certificates"
CERT = CERT_DIR / "iwasawa_discrete_gerbe_holonomy_candidate_certificate.json"
PAPER = ROOT / "Iwasawa_Discrete_Gerbe_Holonomy_Candidate_v1.md"
SCRIPT = REPO / "scripts" / "analyze_iwasawa_discrete_gerbe_holonomy.py"
SOURCE_HUNT = CERT_DIR / "iwasawa_projective_twist_source_hunt_certificate.json"


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


def run_script() -> dict[str, Any]:
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
    source_hunt = load_json(SOURCE_HUNT)
    paper = read(PAPER)
    script_text = read(SCRIPT)
    report = run_script()
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    gates = [
        Gate(
            "certificate status",
            "OPEN"
            if cert.get("status")
            == "IWASAWA_DISCRETE_GERBE_HOLONOMY_CANDIDATE_MAP_CLOSED_SELECTION_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "source-hunt dependency",
            "PASS"
            if source_hunt.get("verdict", {}).get("projective_route_corpus_aligned") is True
            else "FAIL",
            str(SOURCE_HUNT),
        ),
        Gate(
            "script formula",
            "PASS"
            if contains_all(
                script_text,
                [
                    "B((a,b),(a',b')) = -a' b / 3",
                    "coboundary_2",
                    "matches_qutrit_projective_cocycle",
                ],
            )
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "finite bianchi",
            "PASS"
            if report.get("discrete_bianchi_residual_zero") is True
            and report.get("discrete_bianchi_residual_count") == 0
            else "FAIL",
            str(report.get("discrete_bianchi_residual_count")),
        ),
        Gate(
            "nontrivial torsion",
            "PASS"
            if report.get("commutator_rank_over_F3") == 2
            and report.get("nontrivial_discrete_torsion") is True
            else "FAIL",
            str(report),
        ),
        Gate(
            "holonomy map",
            "PASS"
            if report.get("matches_qutrit_projective_cocycle") is True
            and report.get("elementary_square_holonomies", {}).get("Z_then_X")
            == "zeta_3^2"
            else "FAIL",
            str(report.get("elementary_square_holonomies", {})),
        ),
        Gate(
            "what this closes",
            "PASS" if all(cert.get("what_this_closes", {}).values()) else "FAIL",
            str(cert.get("what_this_closes", {})),
        ),
        Gate(
            "still open",
            "OPEN" if all(cert.get("still_open", {}).values()) else "FAIL",
            str(cert.get("still_open", {})),
        ),
        Gate(
            "guardrails",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("candidate_holonomy_map_closed") is True
            and verdict.get("selection_remains_open") is True
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records calculation",
            "PASS"
            if contains_all(
                paper,
                [
                    "B((a,b),(a',b')) = -a' b / 3 mod Z",
                    "dB = 0",
                    "Deligne/Cech",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa discrete gerbe holonomy candidate audit")
    print("===============================================")
    print()
    print(f"discrete_bianchi_residual_count={report.get('discrete_bianchi_residual_count')}")
    print(f"commutator_rank_over_F3={report.get('commutator_rank_over_F3')}")
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
