"""Audit the diagonal rank-three finite-mesh rho_E phase prototype."""

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
CERT = CERT_DIR / "iwasawa_diagonal_phase_mesh_rhoE_prototype_certificate.json"
SCALAR_CERT = CERT_DIR / "iwasawa_scalar_phase_mesh_rhoE_prototype_certificate.json"
MESH_VALIDATOR_CERT = CERT_DIR / "iwasawa_rhoE_mesh_validator_certificate.json"
METRIC_VALIDATOR_CERT = CERT_DIR / "iwasawa_rhoE_metric_validator_certificate.json"
PAPER = ROOT / "Iwasawa_Diagonal_Phase_Mesh_RhoE_Prototype_v1.md"
CONSTRUCTOR = REPO / "scripts" / "construct_iwasawa_diagonal_phase_mesh.py"
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


def run_constructor(candidate_path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [
            sys.executable,
            str(CONSTRUCTOR),
            "--mesh-N",
            "1",
            "--modulus",
            "3",
            "--basis-indices",
            "0,1,2",
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
    scalar_cert = load_json(SCALAR_CERT)
    mesh_cert = load_json(MESH_VALIDATOR_CERT)
    metric_cert = load_json(METRIC_VALIDATOR_CERT)
    paper = read(PAPER)
    constructor_text = read(CONSTRUCTOR)

    with tempfile.TemporaryDirectory() as temp_dir:
        candidate_path = Path(temp_dir) / "iwasawa_diagonal_phase_mesh_rhoE_N1.prototype.json"
        summary = run_constructor(candidate_path)
        candidate = load_json(candidate_path)
        mesh_exit, mesh_output = run_validator(MESH_VALIDATOR, candidate_path)
        metric_exit, metric_output = run_validator(METRIC_VALIDATOR, candidate_path)

    expected_system = cert.get("linear_cocycle_system", {})
    actual_system = {
        "unknown_face_values": summary.get("unknown_face_values"),
        "corner_equations": summary.get("corner_equations"),
        "linear_rank": summary.get("linear_rank"),
        "scalar_nullity": summary.get("scalar_nullity"),
        "target_mismatches": summary.get("target_mismatches"),
    }

    expected_candidate = cert.get("prototype_candidate", {})
    actual_candidate = {
        "basis_indices": summary.get("basis_indices"),
        "component_nonzero_entries": summary.get("component_nonzero_entries"),
        "component_row_residuals": summary.get("component_row_residuals"),
        "diagonal_nonzero_face_values": summary.get("diagonal_nonzero_face_values"),
        "diagonal_nonscalar_face_values": summary.get("diagonal_nonscalar_face_values"),
        "nonzero_by_generator": summary.get("nonzero_by_generator"),
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
            if cert.get("status") == "IWASAWA_DIAGONAL_PHASE_MESH_RHOE_PROTOTYPE_VALIDATED_UNSELECTED"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "dependencies",
            "PASS"
            if scalar_cert.get("verdict", {}).get("table_valued_route_remains_viable") is True
            and mesh_cert.get("verdict", {}).get("closes_finite_mesh_validator_for_rhoE_candidates")
            is True
            and metric_cert.get("verdict", {}).get("closes_metric_validator_for_rhoE_candidates")
            is True
            else "FAIL",
            "scalar prototype, mesh validator, metric validator imported",
        ),
        Gate(
            "scope",
            "PASS"
            if scope.get("diagonal_non_scalar_fiber_action") is True
            and scope.get("off_diagonal_family_mixing") is False
            and scope.get("selected_bundle_claim") is False
            else "FAIL",
            str(scope),
        ),
        Gate(
            "constructor encodes diagonal lift",
            "PASS"
            if contains_all(
                constructor_text,
                [
                    "diagonal_matrix",
                    "basis_indices",
                    "diagonal_nonscalar_face_values",
                    "candidate_has_off_diagonal_family_mixing",
                ],
            )
            else "FAIL",
            str(CONSTRUCTOR),
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
                "basis_indices": expected_candidate.get("basis_indices"),
                "component_nonzero_entries": expected_candidate.get("component_nonzero_entries"),
                "component_row_residuals": expected_candidate.get("component_row_residuals"),
                "diagonal_nonzero_face_values": expected_candidate.get("diagonal_nonzero_face_values"),
                "diagonal_nonscalar_face_values": expected_candidate.get("diagonal_nonscalar_face_values"),
                "nonzero_by_generator": expected_candidate.get("nonzero_by_generator"),
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
            if summary_verdict.get("diagonal_rank_three_mesh_cocycle_exists") is True
            and summary_verdict.get("components_solve_linear_cocycle_equations") is True
            and summary_verdict.get("candidate_is_selected_rho_E") is False
            and summary_verdict.get("candidate_has_off_diagonal_family_mixing") is False
            and summary_verdict.get("candidate_distinguishes_fiber_components") is True
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
            if verdict.get("rank_three_table_route_remains_viable") is True
            and verdict.get("prototype_is_selected") is False
            and "nonabelian" in verdict.get("next_step", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records result",
            "PASS"
            if contains_all(
                paper,
                [
                    "diagonal rank-three prototype",
                    "nonscalar face values = 10",
                    "Both validators pass",
                    "It is not selected data",
                    "off-diagonal family mixing",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa diagonal phase mesh rho_E prototype audit")
    print("=================================================")
    print()
    print(f"diagonal_nonzero_face_values={summary.get('diagonal_nonzero_face_values')}")
    print(f"diagonal_nonscalar_face_values={summary.get('diagonal_nonscalar_face_values')}")
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
