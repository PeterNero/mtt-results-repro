"""Audit the constant rank-three scalar-central Wilson rho_E obstruction."""

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
CERT = CERT_DIR / "iwasawa_constant_wilson_ansatz_scan_certificate.json"
RHOE_VALIDATOR = CERT_DIR / "iwasawa_rhoE_validator_certificate.json"
ROUTE_C = CERT_DIR / "iwasawa_route_c_finite_solve_scaffold_certificate.json"
PAPER = ROOT / "Iwasawa_Constant_Wilson_RhoE_Ansatz_Obstruction_v1.md"
SCRIPT = REPO / "scripts" / "scan_iwasawa_constant_wilson_ansatz.py"


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


def run_scan() -> dict[str, Any]:
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
    rhoe_validator = load_json(RHOE_VALIDATOR)
    route_c = load_json(ROUTE_C)
    paper = read(PAPER)
    script = read(SCRIPT)
    scan = run_scan()

    expected_counts = cert.get("expected_scan_counts", {})
    scan_counts = {
        "total_vector_assignments": scan.get("total_vector_assignments"),
        "trivial_phase_solution_count": scan.get("trivial_phase_solution_count"),
        "nontrivial_scalar_central_solutions": scan.get("nontrivial_scalar_central_solutions"),
        "central_phase_solution_counts": scan.get("central_phase_solution_counts"),
    }
    expected_subset = {
        "total_vector_assignments": expected_counts.get("total_vector_assignments"),
        "trivial_phase_solution_count": expected_counts.get("trivial_phase_solution_count"),
        "nontrivial_scalar_central_solutions": expected_counts.get("nontrivial_scalar_central_solutions"),
        "central_phase_solution_counts": expected_counts.get("central_phase_solution_counts"),
    }

    scope = cert.get("ansatz_scope", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})
    scan_verdict = scan.get("verdict", {})

    gates = [
        Gate(
            "certificate status",
            "OBSTRUCTED"
            if cert.get("status") == "IWASAWA_CONSTANT_WILSON_SCALAR_CENTRAL_ANSATZ_OBSTRUCTED"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "dependencies",
            "PASS"
            if rhoe_validator.get("validator_script") == "scripts/validate_iwasawa_rhoE.py"
            and route_c.get("residual_validator") == "scripts/validate_iwasawa_route_c_residuals.py"
            else "FAIL",
            f"rhoE={rhoe_validator.get('status')} routeC={route_c.get('status')}",
        ),
        Gate(
            "ansatz scope is narrow",
            "PASS"
            if scope.get("rank") == 3
            and scope.get("scalar_central_only") is True
            and scope.get("constant_generators_only") is True
            and scope.get("coordinate_dependent_or_table_valued_rhoE") is False
            and scope.get("general_non_scalar_central_3x3_matrices") is False
            else "FAIL",
            str(scope),
        ),
        Gate(
            "script encodes symplectic scan",
            "PASS"
            if contains_all(
                script,
                [
                    "symplectic",
                    "relation_passes",
                    "cross_pairing_matrix",
                    "nontrivial_scalar_central_solutions",
                ],
            )
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "scan counts",
            "PASS" if scan_counts == expected_subset else "FAIL",
            str(scan_counts),
        ),
        Gate(
            "nontrivial phases absent",
            "PASS"
            if scan.get("central_phase_solution_counts", {}).get("0,0") == 321
            and all(
                count == 0
                for phase, count in scan.get("central_phase_solution_counts", {}).items()
                if phase != "0,0"
            )
            else "FAIL",
            str(scan.get("central_phase_solution_counts", {})),
        ),
        Gate(
            "scan verdict scope",
            "PASS"
            if scan_verdict.get("nontrivial_rank3_scalar_central_constant_weyl_rhoE_exists") is False
            and scan_verdict.get("closes_all_constant_3x3_rhoE") is False
            and scan_verdict.get("closes_coordinate_dependent_or_table_valued_rhoE") is False
            else "FAIL",
            str(scan_verdict),
        ),
        Gate(
            "guardrails",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "certificate verdict",
            "PASS"
            if verdict.get("first_nontrivial_scalar_central_wilson_ansatz_retired") is True
            and verdict.get("route_c_still_required") is True
            and "coordinate-dependent/table-valued rho_E" in verdict.get("next_step", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records obstruction",
            "PASS"
            if contains_all(
                paper,
                [
                    "Iwasawa Relation Reduction",
                    "nontrivial scalar-central solutions = 0",
                    "does not rule out",
                    "coordinate/table-valued rho_E",
                    "higher auxiliary finite-Heisenberg carrier",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa constant Wilson ansatz scan audit")
    print("=========================================")
    print()
    print(f"trivial_phase_solution_count={scan.get('trivial_phase_solution_count')}")
    print(f"nontrivial_scalar_central_solutions={scan.get('nontrivial_scalar_central_solutions')}")
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
