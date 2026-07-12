"""Audit the Fourier-rotated finite-mesh rho_E sector prototype."""

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
CERT = CERT_DIR / "iwasawa_rotated_phase_mesh_rhoE_sector_prototype_certificate.json"
DIAGONAL_CERT = CERT_DIR / "iwasawa_diagonal_phase_mesh_rhoE_prototype_certificate.json"
MESH_VALIDATOR_CERT = CERT_DIR / "iwasawa_rhoE_mesh_validator_certificate.json"
METRIC_VALIDATOR_CERT = CERT_DIR / "iwasawa_rhoE_metric_validator_certificate.json"
SECTOR_VALIDATOR_CERT = CERT_DIR / "iwasawa_sector_projection_validator_certificate.json"
PAPER = ROOT / "Iwasawa_Rotated_Phase_Mesh_RhoE_Sector_Prototype_v1.md"
CONSTRUCTOR = REPO / "scripts" / "construct_iwasawa_rotated_phase_mesh.py"
MESH_VALIDATOR = REPO / "scripts" / "validate_iwasawa_rhoE_mesh.py"
METRIC_VALIDATOR = REPO / "scripts" / "validate_iwasawa_rhoE_metric.py"
SECTOR_VALIDATOR = REPO / "scripts" / "validate_iwasawa_sector_maps.py"


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
    diagonal_cert = load_json(DIAGONAL_CERT)
    mesh_cert = load_json(MESH_VALIDATOR_CERT)
    metric_cert = load_json(METRIC_VALIDATOR_CERT)
    sector_cert = load_json(SECTOR_VALIDATOR_CERT)
    paper = read(PAPER)
    constructor_text = read(CONSTRUCTOR)

    with tempfile.TemporaryDirectory() as temp_dir:
        candidate_path = Path(temp_dir) / "iwasawa_rotated_phase_mesh_rhoE_sector_N1.prototype.json"
        summary = run_constructor(candidate_path)
        candidate = load_json(candidate_path)
        mesh_exit, mesh_output = run_validator(MESH_VALIDATOR, candidate_path)
        metric_exit, metric_output = run_validator(METRIC_VALIDATOR, candidate_path)
        sector_exit, sector_output = run_validator(SECTOR_VALIDATOR, candidate_path)

    expected_candidate = cert.get("prototype_candidate", {})
    actual_candidate = {
        "basis_indices": summary.get("basis_indices"),
        "rotated_offdiagonal_face_values": summary.get("rotated_offdiagonal_face_values"),
        "rhoE_mesh_validator_exit": mesh_exit,
        "rhoE_metric_validator_exit": metric_exit,
        "sector_projection_validator_exit": sector_exit,
        "family_projectors": expected_candidate.get("family_projectors"),
        "higgs_projector": expected_candidate.get("higgs_projector"),
    }
    expected_subset = {
        "basis_indices": expected_candidate.get("basis_indices"),
        "rotated_offdiagonal_face_values": expected_candidate.get("rotated_offdiagonal_face_values"),
        "rhoE_mesh_validator_exit": expected_candidate.get("rhoE_mesh_validator_exit"),
        "rhoE_metric_validator_exit": expected_candidate.get("rhoE_metric_validator_exit"),
        "sector_projection_validator_exit": expected_candidate.get("sector_projection_validator_exit"),
        "family_projectors": expected_candidate.get("family_projectors"),
        "higgs_projector": expected_candidate.get("higgs_projector"),
    }

    scope = cert.get("ansatz_scope", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})
    summary_verdict = summary.get("verdict", {})
    max_commutator = float(summary.get("rotated_max_pairwise_commutator_abs", 1.0))

    gates = [
        Gate(
            "certificate status",
            "PROTOTYPE"
            if cert.get("status") == "IWASAWA_ROTATED_PHASE_MESH_RHOE_SECTOR_PROTOTYPE_VALIDATED_UNSELECTED"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "dependencies",
            "PASS"
            if diagonal_cert.get("verdict", {}).get("rank_three_table_route_remains_viable") is True
            and mesh_cert.get("verdict", {}).get("closes_finite_mesh_validator_for_rhoE_candidates")
            is True
            and metric_cert.get("verdict", {}).get("closes_metric_validator_for_rhoE_candidates")
            is True
            and sector_cert.get("verdict", {}).get("closes_sector_projection_validator_for_candidate_data")
            is True
            else "FAIL",
            "diagonal prototype, mesh, metric, sector validators imported",
        ),
        Gate(
            "scope",
            "PASS"
            if scope.get("offdiagonal_entries_in_standard_basis") is True
            and scope.get("simultaneously_diagonalizable") is True
            and scope.get("genuine_nonabelian_commutators") is False
            and scope.get("physical_family_mixing_claim") is False
            else "FAIL",
            str(scope),
        ),
        Gate(
            "constructor encodes Fourier rotation",
            "PASS"
            if contains_all(
                constructor_text,
                [
                    "fourier_unitary",
                    "conjugate",
                    "sector_maps",
                    "genuine_nonabelian_commutator_found",
                ],
            )
            else "FAIL",
            str(CONSTRUCTOR),
        ),
        Gate(
            "prototype candidate counts",
            "PASS" if actual_candidate == expected_subset else "FAIL",
            str(actual_candidate),
        ),
        Gate(
            "commutator guard",
            "PASS"
            if max_commutator < 1e-8
            and summary_verdict.get("genuine_nonabelian_commutator_found") is False
            else "FAIL",
            f"max_commutator={max_commutator:.3e}",
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
            "sector validator pass",
            "PASS" if sector_exit == 0 and "validation PASS" in sector_output else "FAIL",
            sector_output.strip(),
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
            if summary_verdict.get("offdiagonal_coordinate_basis_rhoE_exists") is True
            and summary_verdict.get("simultaneously_diagonalizable_by_fourier") is True
            and summary_verdict.get("candidate_is_selected_rho_E") is False
            and summary_verdict.get("candidate_proves_physical_family_mixing") is False
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
            if verdict.get("finite_validator_stack_exercised_through_sector_maps") is True
            and verdict.get("prototype_is_selected") is False
            and "basis test" in verdict.get("next_step", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records result",
            "PASS"
            if contains_all(
                paper,
                [
                    "off-diagonal face values = 10",
                    "All three validators pass",
                    "simultaneously diagonalizable = true",
                    "genuine nonabelian commutator found = false",
                    "not physical family mixing",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa rotated phase mesh rho_E sector prototype audit")
    print("=======================================================")
    print()
    print(f"rotated_offdiagonal_face_values={summary.get('rotated_offdiagonal_face_values')}")
    print(f"max_commutator={max_commutator:.3e}")
    print(f"mesh_validator_exit={mesh_exit}")
    print(f"metric_validator_exit={metric_exit}")
    print(f"sector_validator_exit={sector_exit}")
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
