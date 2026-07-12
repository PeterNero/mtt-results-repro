"""Audit the visible rank-two extension route for V_alpha."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "analyze_visible_rank2_extension_valpha_route.py"
CANDIDATE = REPO / "candidate_data" / "visible_rank2_extension_valpha_route.candidate.json"
CERT = REPO / "certificates" / "visible_rank2_extension_valpha_route_certificate.json"
PAPER = ROOT / "Visible_Rank2_Extension_VAlpha_Route_v1.md"


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

    schema = cert.get("rank2_extension_schema", {})
    line_classes = cert.get("finite_line_class_solutions", [])
    split_scope = cert.get("why_split_no_go_not_violated", {})
    stability = cert.get("stability_contract", {})
    calc = cert.get("calculation_results", {})
    closes = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})

    expected_classes = {
        (1, -2, 0),
        (-1, 2, 0),
        (2, -1, 0),
        (-2, 1, 0),
    }
    actual_classes = {tuple(item.get("l_vector_abc", [])) for item in line_classes}

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", str(CERT)),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", str(CANDIDATE)),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", str(PAPER)),
        Gate(
            "status rank2 route",
            "PASS"
            if cert.get("status")
            == "VISIBLE_RANK2_EXTENSION_VALPHA_ROUTE_FORMULATED_EXT_STABILITY_OPEN"
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
            "extension schema",
            "PASS"
            if schema.get("sequence") == "0 -> L -> V_alpha -> L^{-1} -> 0"
            and schema.get("c1") == [0, 0, 0]
            and schema.get("c3") == 0
            and schema.get("target_c2") == [4, 0, 0]
            and schema.get("formula_c2") == "c2(V_alpha)=-l^2"
            else "FAIL",
            str(schema),
        ),
        Gate(
            "finite line classes",
            "PASS"
            if actual_classes == expected_classes
            and all(item.get("c2_extension_alpha_coeffs") == [4, 0, 0] for item in line_classes)
            else "FAIL",
            str(line_classes),
        ),
        Gate(
            "slope witnesses",
            "PASS"
            if all(
                item.get("slope_chamber_witness", {}).get("necessary_subline_slope_negative")
                is True
                and item.get("slope_chamber_witness", {}).get("mu_L") == -1
                for item in line_classes
            )
            else "FAIL",
            str(line_classes),
        ),
        Gate(
            "split no-go respected",
            "PASS"
            if split_scope.get("split_limit_forbidden") is True
            and "non-split extension" in split_scope.get("extension_route_difference", "")
            else "FAIL",
            str(split_scope),
        ),
        Gate(
            "stability contract",
            "OPEN"
            if stability.get("not_sufficient") is True
            and "nonzero extension class in H^1(X,L^2)" in stability.get(
                "missing_sufficient_inputs", []
            )
            and "proof no other positive-slope line subsheaf injects into V_alpha"
            in stability.get("missing_sufficient_inputs", [])
            else "FAIL",
            str(stability),
        ),
        Gate(
            "calculation scoped",
            "PASS"
            if calc.get("rank2_extension_topological_classes_found") is True
            and calc.get("number_of_primitive_line_classes") == 4
            and calc.get("non_split_extension_constructed") is False
            and calc.get("stability_proved") is False
            else "FAIL",
            str(calc),
        ),
        Gate(
            "still open",
            "OPEN"
            if still_open.get("compute_H1_X_L_squared_for_candidate_classes") is True
            and still_open.get("select_nonzero_extension_class") is True
            and still_open.get("derive_same_total_source_D_E_dotD_Riesz_Green") is True
            else "FAIL",
            str(still_open),
        ),
        Gate(
            "closes route arithmetic",
            "PASS"
            if closes.get("minimal_rank2_extension_c2_arithmetic") is True
            and closes.get("exact_next_ext_stability_inputs_identified") is True
            else "FAIL",
            str(closes),
        ),
        Gate(
            "guardrails",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "paper records theorem",
            "PASS"
            if contains_all(
                paper,
                [
                    "0 -> L -> V_alpha -> L^{-1} -> 0",
                    "xy = -2",
                    "H^1(X,L^2)",
                    "limit remains forbidden",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Visible rank-two extension V_alpha route audit")
    print("==============================================")
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
