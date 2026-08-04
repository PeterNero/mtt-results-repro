"""Audit the four-route qutrit flat-torsion label selector."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "iwasawa_torsion_label_four_route_selector_certificate.json"
PAPER = ROOT / "Iwasawa_Torsion_Label_Four_Route_Selector_v1.md"
SCRIPT = REPO / "scripts" / "analyze_iwasawa_torsion_label_four_route_selector.py"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def contains_all_ci(text: str, needles: list[str]) -> bool:
    lowered = text.lower()
    return all(needle.lower() in lowered for needle in needles)


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


def route_by_name(report: dict[str, Any], name: str) -> dict[str, Any]:
    for route in report.get("route_reports", []):
        if route.get("route") == name:
            return route
    return {}


def labels(route: dict[str, Any]) -> list[int]:
    return list(route.get("candidate_labels", []))


def main() -> None:
    cert = load_json(CERT)
    paper = read(PAPER)
    script_text = read(SCRIPT)
    report = run_script()

    calc = cert.get("calculation_results", {})
    closed = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})
    consensus = report.get("consensus", {})

    corpus = route_by_name(report, "corpus")
    topology = route_by_name(report, "topological")
    projector = route_by_name(report, "projector_zero_mode")
    orientation = route_by_name(report, "orientation")

    gates = [
        Gate(
            "certificate status",
            "PASS"
            if cert.get("status")
            == "IWASAWA_TORSION_LABEL_FOUR_ROUTE_CONVERGES_NONTRIVIAL_PAIR_UNIQUE_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "script present",
            "PASS"
            if SCRIPT.exists()
            and contains_all_ci(
                script_text,
                [
                    "corpus_route",
                    "topology_route",
                    "projector_route",
                    "orientation_route",
                ],
            )
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "route names",
            "PASS"
            if {route.get("route") for route in report.get("route_reports", [])}
            == {"corpus", "topological", "projector_zero_mode", "orientation"}
            else "FAIL",
            str([route.get("route") for route in report.get("route_reports", [])]),
        ),
        Gate(
            "corpus route",
            "PASS"
            if labels(corpus) == [1, 2]
            and corpus.get("rejects_trivial_m0") is True
            and corpus.get("selects_unique_label") is False
            else "FAIL",
            str(corpus),
        ),
        Gate(
            "topology route",
            "PASS"
            if labels(topology) == [1, 2]
            and topology.get("rejects_trivial_m0") is True
            and topology.get("selects_unique_label") is False
            and topology.get("evidence", {}).get("trivial_label_commutator_rank") == 0
            else "FAIL",
            str(topology),
        ),
        Gate(
            "projector route",
            "PASS"
            if labels(projector) == [1, 2]
            and projector.get("rejects_trivial_m0") is True
            and projector.get("selects_unique_label") is False
            and projector.get("evidence", {}).get("family_central_twist_nontrivial") is True
            else "FAIL",
            str(projector),
        ),
        Gate(
            "orientation route",
            "PASS"
            if labels(orientation) == [1, 2]
            and orientation.get("rejects_trivial_m0") is True
            and orientation.get("selects_unique_label") is False
            and orientation.get("evidence", {}).get("unique_orientation_convention_selected")
            is False
            else "FAIL",
            str(orientation),
        ),
        Gate(
            "consensus",
            "PASS"
            if consensus.get("all_four_routes_agree_on_candidate_set") is True
            and consensus.get("all_four_routes_reject_trivial_m0") is True
            and consensus.get("common_candidate_labels") == [1, 2]
            and consensus.get("unique_label_selected_by_any_route") is False
            and consensus.get("selected_torsion_label") is None
            else "FAIL",
            str(consensus),
        ),
        Gate(
            "certificate calculation results",
            "PASS"
            if calc.get("corpus_route_candidate_labels") == [1, 2]
            and calc.get("topological_route_candidate_labels") == [1, 2]
            and calc.get("projector_zero_mode_route_candidate_labels") == [1, 2]
            and calc.get("orientation_route_candidate_labels") == [1, 2]
            and calc.get("all_four_routes_agree_on_candidate_set") is True
            and calc.get("unique_label_selected_by_any_route") is False
            and calc.get("selected_torsion_label") is None
            else "FAIL",
            str(calc),
        ),
        Gate(
            "closed fields",
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
            if verdict.get("four_routes_arrive_at_same_conclusion") is True
            and verdict.get("same_conclusion") == "m is nontrivial: m in {1,2}"
            and verdict.get("unique_torsion_label_selected") is False
            and verdict.get("can_promote_twisted_source_now") is False
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records result",
            "PASS"
            if contains_all_ci(
                paper,
                [
                    "All four routes agree",
                    "m in {1,2}",
                    "do not prove",
                    "selected orientation convention",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa torsion-label four-route selector audit")
    print("===============================================")
    print()
    print(f"common_candidate_labels={consensus.get('common_candidate_labels')}")
    print(f"selected_torsion_label={consensus.get('selected_torsion_label')}")
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
