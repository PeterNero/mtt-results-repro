"""Audit the absolute-normalization candidate gate."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "absolute_normalization_candidate_gate_certificate.json"
PAPER = ROOT / "Absolute_Normalization_Candidate_Gate_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def contains_all(text: str, needles: list[str]) -> bool:
    lowered = text.lower()
    return all(needle.lower() in lowered for needle in needles)


def candidate(candidates: list[dict], candidate_id: str) -> dict:
    for item in candidates:
        if item.get("id") == candidate_id:
            return item
    return {}


def main() -> None:
    cert = load_json(CERT)
    paper = read(PAPER)
    sources = {key: Path(value) for key, value in cert.get("source_paths", {}).items()}
    source_text = {key: read(path) for key, path in sources.items()}
    candidates = cert.get("candidates", [])
    verdict = cert.get("verdict", {})

    gates = [
        Gate(
            "certificate status",
            "PASS" if cert.get("status") == "CANDIDATE_GATE_FORMULATED_NO_CLOSURE_YET" else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "source paths present",
            "PASS" if all(path.exists() for path in sources.values()) else "FAIL",
            str([str(path) for path in sources.values() if not path.exists()]),
        ),
        Gate(
            "gate forbids target backsolve",
            "PASS"
            if contains_all(
                " ".join(cert.get("gate_rules", [])),
                ["may not use observed G_N", "target value", "unit convention"],
            )
            else "FAIL",
            str(cert.get("gate_rules", [])),
        ),
        Gate(
            "roadmap has K and GN calibration",
            "PASS"
            if contains_all(
                source_text["roadmap"],
                ["K := \\frac{4\\pi", "Use $G_N$ to fix", "Apply one closure"],
            )
            else "FAIL",
            str(sources["roadmap"]),
        ),
        Gate(
            "Execution I has Vol/g10 combination",
            "PASS"
            if contains_all(
                source_text["execution_i"],
                ["Vol}(X_6)}{g_{10}^2}", "K}{4\\pi", "Different normalization conventions"],
            )
            else "FAIL",
            str(sources["execution_i"]),
        ),
        Gate(
            "Theta IV has GN structure",
            "PASS"
            if contains_all(
                source_text["theta_iv"],
                ["31.8", "G_{10}", "R_1^3", "does not attempt to compute"],
            )
            else "FAIL",
            str(sources["theta_iv"]),
        ),
        Gate(
            "heterotic source has alpha-prime flux loci",
            "PASS"
            if contains_all(
                source_text["heterotic_selection"],
                ["\\alpha'", "fixes $r_3", "fix the ratio $R_1/R", "dH"],
            )
            else "FAIL",
            str(sources["heterotic_selection"]),
        ),
        Gate(
            "finite projection has coherence-scale clues",
            "PASS"
            if contains_all(
                source_text["finite_projection"],
                ["coherence scale", "damping-selected", "admissibility scale"],
            )
            else "FAIL",
            str(sources["finite_projection"]),
        ),
        Gate(
            "candidate count",
            "PASS" if len(candidates) == 7 else "FAIL",
            str(len(candidates)),
        ),
        Gate(
            "forbidden GN candidate",
            "PASS"
            if candidate(candidates, "B_newton_backsolve").get("classification")
            == "FORBIDDEN_FOR_PREDICTING_GN_OR_PLANCK_SCALE"
            else "FAIL",
            str(candidate(candidates, "B_newton_backsolve")),
        ),
        Gate(
            "best candidate selected",
            "PASS"
            if verdict.get("best_candidate") == "E_topological_flux_integer_minimization"
            and candidate(candidates, "E_topological_flux_integer_minimization").get("classification")
            == "BEST_STRUCTURAL_RESEARCH_ROUTE"
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper names recommended path",
            "PASS"
            if contains_all(
                paper,
                [
                    "E + D + F",
                    "Selected_Normalization_Minimization_Functional_v1",
                    "unique minimizer",
                    "no target constants",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
        Gate(
            "no closure overclaim",
            "PASS"
            if verdict.get("absolute_normalization_selected") is False
            else "FAIL",
            str(verdict),
        ),
    ]

    print("Absolute normalization candidate gate audit")
    print("===========================================")
    print()
    print(f"candidates={len(candidates)}")
    print(f"best_candidate={verdict.get('best_candidate')}")
    print()

    width = max(len(gate.label) for gate in gates)
    failures = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:4s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
