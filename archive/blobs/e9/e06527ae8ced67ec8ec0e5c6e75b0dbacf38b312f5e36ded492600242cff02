"""Audit the visible rho_E source ansatz search."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "visible_rhoE_source_ansatz_search_certificate.json"
CANDIDATE = REPO / "candidate_data" / "visible_rhoE_source_ansatz_search.candidate.json"
PAPER = REPO / "proof_corpus" / "Visible_RhoE_Source_Ansatz_Search_v1.md"
SCRIPT = REPO / "scripts" / "search_visible_rhoE_source_ansatz.py"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def check(name: str, condition: bool, detail: str) -> tuple[str, bool, str]:
    return name, condition, detail


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


def main() -> int:
    cert = load_json(CERT)
    candidate = load_json(CANDIDATE)
    paper = PAPER.read_text(encoding="utf-8")
    rerun = run_script()

    results = cert.get("calculation_results", {})
    ordinary = candidate.get("ordinary_constant_carrier_analysis", {})
    scalar = candidate.get("scalar_phase_analysis", {})
    n2 = scalar.get("mesh_N2_prime_fields", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    checks = [
        check(
            "certificate status",
            cert.get("status")
            == "VISIBLE_RHOE_SOURCE_ANSATZ_SEARCH_NARROWS_TO_SELECTED_RESPONSE_OR_TWISTED_SOURCE",
            str(cert.get("status")),
        ),
        check(
            "candidate status",
            candidate.get("status") == cert.get("status"),
            str(candidate.get("status")),
        ),
        check(
            "rerun agrees",
            rerun.get("status") == candidate.get("status")
            and rerun.get("calculation_results") == candidate.get("calculation_results"),
            str(rerun.get("status")),
        ),
        check(
            "ordinary constant carriers blocked",
            results.get("ordinary_constant_carriers_blocked") is True
            and ordinary.get("ordinary_constant_carriers_blocked") is True,
            str(ordinary.get("ordinary_constant_carriers_blocked")),
        ),
        check(
            "central absorption blocked",
            results.get("qutrit_projective_central_absorption_as_ordinary_rhoE_blocked")
            is True
            and ordinary.get("mesh_N1", {}).get("qutrit_central_absorption_possible")
            is False
            and ordinary.get("mesh_N2", {}).get("qutrit_central_absorption_possible")
            is False,
            str(results.get("qutrit_projective_central_absorption_as_ordinary_rhoE_blocked")),
        ),
        check(
            "constant perfect carrier route blocked",
            results.get("perfect_non_solvable_constant_carrier_route_blocked") is True,
            str(results.get("perfect_non_solvable_constant_carrier_route_blocked")),
        ),
        check(
            "N2 scalar F2/F3 blocked",
            scalar.get("N2_F2_F3_scalar_phase_tables_coboundary") is True
            and n2.get("2", {}).get("flat_solution_dimension") == 428
            and n2.get("2", {}).get("source_key_coboundary_rank") == 428
            and n2.get("3", {}).get("flat_solution_dimension") == 428
            and n2.get("3", {}).get("source_key_coboundary_rank") == 428,
            str(n2),
        ),
        check(
            "selected scaffold available",
            results.get("selected_gerbe_fourier_type_available") is True
            and results.get("selected_block_factorized_finite_scaffold_available") is True,
            str(results),
        ),
        check(
            "next object identified",
            results.get("next_object_identified")
            == "selected_D_E_dotD_response_or_fixed_gerbe_period_representative",
            str(results.get("next_object_identified")),
        ),
        check(
            "guardrails",
            guardrails.get("claims_selected_visible_operator_source") is False
            and guardrails.get("claims_selected_D_E_constructed") is False
            and guardrails.get("claims_full_SM_closure") is False
            and guardrails.get("uses_observed_flavor_data") is False
            and guardrails.get("uses_benchmark_flavor_entries") is False,
            str(guardrails),
        ),
        check(
            "paper records verdict",
            "construct the selected de_response packet directly" in paper
            and "not another constant ordinary rho_E table" in paper,
            "paper verdict present",
        ),
        check(
            "recommended action",
            "selected de_response packet" in verdict.get("recommended_next_action", ""),
            str(verdict),
        ),
    ]

    print("Visible rho_E source ansatz search audit")
    print("=========================================")
    failures = 0
    for name, ok, detail in checks:
        print(f"{name:42} {'PASS' if ok else 'FAIL'}  {detail}")
        if not ok:
            failures += 1
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
