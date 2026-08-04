"""Audit the scalar phase finite-mesh rho_E prototype."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT_DIR = REPO / "certificates"
CERT = CERT_DIR / "iwasawa_scalar_phase_mesh_rhoE_prototype_certificate.json"
OBSTRUCTION = CERT_DIR / "iwasawa_constant_wilson_ansatz_scan_certificate.json"
MESH_VALIDATOR_CERT = CERT_DIR / "iwasawa_rhoE_mesh_validator_certificate.json"
METRIC_VALIDATOR_CERT = CERT_DIR / "iwasawa_rhoE_metric_validator_certificate.json"
ROUTE_C = CERT_DIR / "iwasawa_route_c_finite_solve_scaffold_certificate.json"
PAPER = ROOT / "Iwasawa_Scalar_Phase_Mesh_RhoE_Prototype_v1.md"
SOLVER = REPO / "scripts" / "solve_iwasawa_scalar_phase_mesh.py"
MESH_VALIDATOR = REPO / "scripts" / "validate_iwasawa_rhoE_mesh.py"
METRIC_VALIDATOR = REPO / "scripts" / "validate_iwasawa_rhoE_metric.py"


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


def run_solver(candidate_path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [
            sys.executable,
            str(SOLVER),
            "--mesh-N",
            "1",
            "--modulus",
            "3",
            "--basis-index",
            "0",
            "--emit-candidate",
            str(candidate_path),
        ],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stdout)
    return json.loads(proc.stdout)


def run_validator(script: Path, candidate_path: Path) -> tuple[int, str]:
    proc = subprocess.run(
        [sys.executable, str(script), str(candidate_path)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return proc.returncode, proc.stdout


def main() -> None:
    cert = load_json(CERT)
    obstruction = load_json(OBSTRUCTION)
    mesh_cert = load_json(MESH_VALIDATOR_CERT)
    metric_cert = load_json(METRIC_VALIDATOR_CERT)
    route_c = load_json(ROUTE_C)
    paper = read(PAPER)
    solver_text = read(SOLVER)

    with tempfile.TemporaryDirectory() as temp_dir:
        candidate_path = Path(temp_dir) / "iwasawa_scalar_phase_mesh_rhoE_N1.prototype.json"
        summary = run_solver(candidate_path)
        candidate = load_json(candidate_path)
        mesh_exit, mesh_output = run_validator(MESH_VALIDATOR, candidate_path)
        metric_exit, metric_output = run_validator(METRIC_VALIDATOR, candidate_path)

    expected_system = cert.get("linear_cocycle_system", {})
    actual_system = {
        "unknown_face_values": summary.get("unknown_face_values"),
        "corner_equations": summary.get("corner_equations"),
        "linear_rank": summary.get("linear_rank"),
        "nullity": summary.get("nullity"),
        "target_mismatches": summary.get("target_mismatches"),
        "unknowns_by_generator": summary.get("unknowns_by_generator"),
    }

    expected_candidate = cert.get("prototype_candidate", {})
    actual_candidate = {
        "basis_index": summary.get("candidate_basis_index"),
        "nonzero_entries": summary.get("candidate_nonzero_entries"),
        "nonzero_by_generator": summary.get("candidate_nonzero_by_generator"),
        "linear_row_residuals": summary.get("candidate_row_residuals"),
        "rhoE_mesh_validator_exit": mesh_exit,
        "rhoE_metric_validator_exit": metric_exit,
    }

    scope = cert.get("ansatz_scope", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})
    summary_verdict = summary.get("verdict", {})

    gates = [
        Gate(
            "certificate status",
            "PROTOTYPE"
            if cert.get("status") == "IWASAWA_SCALAR_PHASE_MESH_RHOE_PROTOTYPE_VALIDATED_UNSELECTED"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "dependencies",
            "PASS"
            if obstruction.get("verdict", {}).get("first_nontrivial_scalar_central_wilson_ansatz_retired")
            is True
            and mesh_cert.get("verdict", {}).get("closes_finite_mesh_validator_for_rhoE_candidates")
            is True
            and metric_cert.get("verdict", {}).get("closes_metric_validator_for_rhoE_candidates")
            is True
            and route_c.get("verdict", {}).get("route_c_scaffold_constructed") is True
            else "FAIL",
            "constant obstruction, mesh validator, metric validator, route C imported",
        ),
        Gate(
            "scope",
            "PASS"
            if scope.get("table_valued_boundary_targets") is True
            and scope.get("scalar_fiber_action_only") is True
            and scope.get("non_scalar_family_mixing") is False
            and scope.get("selected_bundle_claim") is False
            else "FAIL",
            str(scope),
        ),
        Gate(
            "solver encodes linear cocycle",
            "PASS"
            if contains_all(
                solver_text,
                [
                    "build_linear_system",
                    "nullspace_basis",
                    "candidate_data",
                    "candidate_is_selected_rho_E",
                ],
            )
            else "FAIL",
            str(SOLVER),
        ),
        Gate(
            "linear system counts",
            "PASS" if actual_system == expected_system else "FAIL",
            str(actual_system),
        ),
        Gate(
            "prototype candidate counts",
            "PASS"
            if actual_candidate
            == {
                "basis_index": expected_candidate.get("basis_index"),
                "nonzero_entries": expected_candidate.get("nonzero_entries"),
                "nonzero_by_generator": expected_candidate.get("nonzero_by_generator"),
                "linear_row_residuals": expected_candidate.get("linear_row_residuals"),
                "rhoE_mesh_validator_exit": expected_candidate.get("rhoE_mesh_validator_exit"),
                "rhoE_metric_validator_exit": expected_candidate.get("rhoE_metric_validator_exit"),
            }
            else "FAIL",
            str(actual_candidate),
        ),
        Gate(
            "rhoE mesh validator pass",
            "PASS" if mesh_exit == 0 and "validation PASS" in mesh_output else "FAIL",
            mesh_output.strip(),
        ),
        Gate(
            "rhoE metric validator pass",
            "PASS" if metric_exit == 0 and "validation PASS" in metric_output else "FAIL",
            metric_output.strip(),
        ),
        Gate(
            "candidate guardrails",
            "PASS"
            if candidate.get("status") == "PROTOTYPE_UNSELECTED"
            and all(value is False for value in candidate.get("guardrails", {}).values())
            else "FAIL",
            str(candidate.get("guardrails", {})),
        ),
        Gate(
            "summary verdict",
            "PASS"
            if summary_verdict.get("nontrivial_scalar_phase_mesh_cocycles_exist") is True
            and summary_verdict.get("candidate_solves_linear_cocycle_equations") is True
            and summary_verdict.get("candidate_is_selected_rho_E") is False
            and summary_verdict.get("candidate_can_mix_families") is False
            else "FAIL",
            str(summary_verdict),
        ),
        Gate(
            "certificate guardrails",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "certificate verdict",
            "PASS"
            if verdict.get("table_valued_route_remains_viable") is True
            and verdict.get("prototype_is_selected") is False
            and "non-scalar" in verdict.get("next_step", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records result",
            "PASS"
            if contains_all(
                paper,
                [
                    "rank = 117",
                    "nullity = 27",
                    "Both validators pass",
                    "It must not be promoted to selected data",
                    "higher auxiliary finite-Heisenberg carrier",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa scalar phase mesh rho_E prototype audit")
    print("===============================================")
    print()
    print(f"unknown_face_values={summary.get('unknown_face_values')}")
    print(f"nullity={summary.get('nullity')}")
    print(f"mesh_validator_exit={mesh_exit}")
    print(f"metric_validator_exit={metric_exit}")
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
