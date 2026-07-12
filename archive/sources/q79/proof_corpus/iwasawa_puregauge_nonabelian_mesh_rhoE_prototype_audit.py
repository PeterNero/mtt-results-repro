"""Audit the pure-gauge nonabelian finite-mesh rho_E prototype."""

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
CERT = CERT_DIR / "iwasawa_puregauge_nonabelian_mesh_rhoE_prototype_certificate.json"
ROTATED_CERT = CERT_DIR / "iwasawa_rotated_phase_mesh_rhoE_sector_prototype_certificate.json"
MESH_VALIDATOR_CERT = CERT_DIR / "iwasawa_rhoE_mesh_validator_certificate.json"
METRIC_VALIDATOR_CERT = CERT_DIR / "iwasawa_rhoE_metric_validator_certificate.json"
SECTOR_VALIDATOR_CERT = CERT_DIR / "iwasawa_sector_projection_validator_certificate.json"
PAPER = ROOT / "Iwasawa_PureGauge_Nonabelian_Mesh_RhoE_Prototype_v1.md"
CONSTRUCTOR = REPO / "scripts" / "construct_iwasawa_puregauge_nonabelian_mesh.py"
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
    rotated_cert = load_json(ROTATED_CERT)
    mesh_cert = load_json(MESH_VALIDATOR_CERT)
    metric_cert = load_json(METRIC_VALIDATOR_CERT)
    sector_cert = load_json(SECTOR_VALIDATOR_CERT)
    paper = read(PAPER)
    constructor_text = read(CONSTRUCTOR)

    with tempfile.TemporaryDirectory() as temp_dir:
        candidate_path = Path(temp_dir) / "iwasawa_puregauge_nonabelian_mesh_rhoE_N1.prototype.json"
        summary = run_constructor(candidate_path)
        candidate = load_json(candidate_path)
        mesh_exit, mesh_output = run_validator(MESH_VALIDATOR, candidate_path)
        metric_exit, metric_output = run_validator(METRIC_VALIDATOR, candidate_path)
        sector_exit, sector_output = run_validator(SECTOR_VALIDATOR, candidate_path)

    expected_equivalence = cert.get("source_equivalence", {})
    actual_equivalence = {
        "closed_nodes": summary.get("closed_nodes"),
        "face_keys": summary.get("face_keys"),
        "components": summary.get("source_equivalence_components"),
        "component_size_histogram": summary.get("component_size_histogram"),
        "face_keys_by_generator": summary.get("face_keys_by_generator"),
    }

    expected_candidate = cert.get("prototype_candidate", {})
    actual_candidate = {
        "nonidentity_face_values": summary.get("nonidentity_face_values"),
        "offdiagonal_face_values": summary.get("offdiagonal_face_values"),
        "max_pairwise_commutator_abs": summary.get("max_pairwise_commutator_abs"),
        "rhoE_mesh_validator_exit": mesh_exit,
        "rhoE_metric_validator_exit": metric_exit,
        "sector_projection_validator_exit": sector_exit,
        "family_projectors": expected_candidate.get("family_projectors"),
        "higgs_projector": expected_candidate.get("higgs_projector"),
    }
    expected_candidate_subset = {
        "nonidentity_face_values": expected_candidate.get("nonidentity_face_values"),
        "offdiagonal_face_values": expected_candidate.get("offdiagonal_face_values"),
        "max_pairwise_commutator_abs": expected_candidate.get("max_pairwise_commutator_abs"),
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

    gates = [
        Gate(
            "certificate status",
            "PROTOTYPE"
            if cert.get("status") == "IWASAWA_PUREGAUGE_NONABELIAN_MESH_RHOE_PROTOTYPE_VALIDATED_UNSELECTED"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "dependencies",
            "PASS"
            if rotated_cert.get("verdict", {}).get("finite_validator_stack_exercised_through_sector_maps")
            is True
            and mesh_cert.get("verdict", {}).get("closes_finite_mesh_validator_for_rhoE_candidates")
            is True
            and metric_cert.get("verdict", {}).get("closes_metric_validator_for_rhoE_candidates")
            is True
            and sector_cert.get("verdict", {}).get("closes_sector_projection_validator_for_candidate_data")
            is True
            else "FAIL",
            "rotated prototype, mesh, metric, sector validators imported",
        ),
        Gate(
            "scope",
            "PASS"
            if scope.get("noncommuting_face_matrices") is True
            and scope.get("pure_gauge_flat") is True
            and scope.get("common_rank_one_higgs_line") is True
            and scope.get("selected_bundle_claim") is False
            and scope.get("physical_family_mixing_claim") is False
            else "FAIL",
            str(scope),
        ),
        Gate(
            "constructor encodes pure gauge",
            "PASS"
            if contains_all(
                constructor_text,
                [
                    "source_equivalence",
                    "pauli_block_group",
                    "matmul(adjoint(node_gauge[source]), node_gauge[target])",
                    "noncommuting_face_matrices_exist",
                ],
            )
            else "FAIL",
            str(CONSTRUCTOR),
        ),
        Gate(
            "source equivalence counts",
            "PASS" if actual_equivalence == expected_equivalence else "FAIL",
            str(actual_equivalence),
        ),
        Gate(
            "prototype candidate counts",
            "PASS" if actual_candidate == expected_candidate_subset else "FAIL",
            str(actual_candidate),
        ),
        Gate(
            "noncommuting guard",
            "PASS"
            if summary.get("max_pairwise_commutator_abs") == 2.0
            and summary_verdict.get("noncommuting_face_matrices_exist") is True
            and summary_verdict.get("pure_gauge_flat_cocycle") is True
            else "FAIL",
            f"max_commutator={summary.get('max_pairwise_commutator_abs')}",
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
            if summary_verdict.get("candidate_is_selected_rho_E") is False
            and summary_verdict.get("candidate_proves_physical_family_mixing") is False
            and "nontrivial D_E response" in summary_verdict.get("next_step", "")
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
            if verdict.get("finite_validator_stack_handles_noncommuting_tables") is True
            and verdict.get("prototype_is_selected") is False
            and "D_E" in verdict.get("next_step", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records result",
            "PASS"
            if contains_all(
                paper,
                [
                    "max pairwise commutator = 2.0",
                    "All three pass",
                    "pure gauge and unselected",
                    "can carry noncommuting table data",
                    "not merely pure gauge",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa pure-gauge nonabelian mesh rho_E prototype audit")
    print("========================================================")
    print()
    print(f"components={summary.get('source_equivalence_components')}")
    print(f"nonidentity_face_values={summary.get('nonidentity_face_values')}")
    print(f"offdiagonal_face_values={summary.get('offdiagonal_face_values')}")
    print(f"max_commutator={summary.get('max_pairwise_commutator_abs')}")
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
