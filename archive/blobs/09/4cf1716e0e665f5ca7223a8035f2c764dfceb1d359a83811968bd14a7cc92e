"""Audit the N=1 finite solvable carrier obstruction."""

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
CERT = CERT_DIR / "iwasawa_n1_solvable_carrier_obstruction_certificate.json"
PHASE_CERT = CERT_DIR / "iwasawa_n1_phase_coboundary_obstruction_certificate.json"
PROMOTION_CERT = CERT_DIR / "iwasawa_selected_source_promotion_gate_certificate.json"
PAPER = ROOT / "Iwasawa_N1_Solvable_Carrier_Obstruction_v1.md"
SCRIPT = REPO / "scripts" / "analyze_iwasawa_n1_solvable_carrier_obstruction.py"


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
    phase_cert = load_json(PHASE_CERT)
    promotion_cert = load_json(PROMOTION_CERT)
    paper = read(PAPER)
    script_text = read(SCRIPT)
    analysis = run_analysis()

    certified_primes = cert.get("certified_scope", {}).get("certified_phase_primes", [])
    examples = analysis.get("covered_matrix_carrier_examples", {})
    cert_examples = cert.get("covered_matrix_carrier_examples", {})
    all_examples_covered = all(
        examples.get(name, {}).get("certified_by_phase_primes") is True
        for name in cert_examples
    )
    phase_results_ok = all(
        entry.get("flat_solution_space_equals_source_key_coboundaries") is True
        for entry in analysis.get("phase_results", [])
    )

    gates = [
        Gate(
            "certificate status",
            "PROVED"
            if cert.get("status") == "IWASAWA_N1_SOLVABLE_CARRIER_OBSTRUCTION_PROVED"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "dependencies",
            "PASS"
            if phase_cert.get("verdict", {}).get("phase_ansatz_retired_as_source_level_route_at_N1")
            is True
            and promotion_cert.get("verdict", {}).get("promotion_gate_ready") is True
            else "FAIL",
            "phase obstruction and promotion gate",
        ),
        Gate(
            "analysis script",
            "PASS"
            if contains_all(
                script_text,
                [
                    "derived quotient",
                    "finite solvable carrier",
                    "S3_permutation",
                    "does_not_rule_out_perfect_or_non_solvable_carriers",
                ],
            )
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "certified primes",
            "PASS" if analysis.get("certified_primes") == certified_primes else "FAIL",
            str(analysis.get("certified_primes")),
        ),
        Gate(
            "phase zero H1 imported",
            "PASS"
            if analysis.get("phase_zero_h1_primes") == certified_primes and phase_results_ok
            else "FAIL",
            str(analysis.get("phase_zero_h1_primes")),
        ),
        Gate(
            "covered carrier examples",
            "PASS" if all_examples_covered else "FAIL",
            str(examples),
        ),
        Gate(
            "derived-series lift recorded",
            "PASS"
            if analysis.get("derived_series_lift", {}).get(
                "requires_zero_h1_for_all_abelian_composition_primes"
            )
            is True
            and "derived quotient" in analysis.get("derived_series_lift", {}).get("statement", "")
            else "FAIL",
            str(analysis.get("derived_series_lift", {})),
        ),
        Gate(
            "global verdict",
            "PASS"
            if analysis.get("global_verdict", {}).get(
                "all_listed_solvable_matrix_carriers_blocked_at_N1_source_level"
            )
            is True
            and analysis.get("global_verdict", {}).get(
                "does_not_rule_out_perfect_or_non_solvable_carriers"
            )
            is True
            and analysis.get("global_verdict", {}).get(
                "does_not_rule_out_selected_D_E_response_promotion"
            )
            is True
            else "FAIL",
            str(analysis.get("global_verdict", {})),
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
            "PASS" if all(value is False for value in cert.get("guardrails", {}).values()) else "FAIL",
            str(cert.get("guardrails", {})),
        ),
        Gate(
            "paper records obstruction",
            "PASS"
            if contains_all(
                paper,
                [
                    "The first matrix carriers one naturally reaches for are usually solvable",
                    "At the first nontrivial abelian derived quotient",
                    "does not evade the source-level obstruction",
                    "perfect/non-solvable carriers",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa N=1 solvable carrier obstruction audit")
    print("==============================================")
    print()
    print(f"certified_primes={analysis.get('certified_primes')}")
    print(f"covered_examples={sorted(examples)}")
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
