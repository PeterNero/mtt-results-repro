"""Audit the Route C finite selected-connection solve scaffold."""

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
CERT = CERT_DIR / "iwasawa_route_c_finite_solve_scaffold_certificate.json"
PAPER = ROOT / "Iwasawa_Route_C_Finite_Selected_Connection_Solve_Scaffold_v1.md"
SCRIPT = REPO / "scripts" / "scaffold_iwasawa_route_c_solver.py"
RESIDUAL_VALIDATOR = REPO / "scripts" / "validate_iwasawa_route_c_residuals.py"
RESIDUAL_TEMPLATE = CERT_DIR / "iwasawa_route_c_residuals.template.json"
SOURCE_HUNT = CERT_DIR / "selected_de_source_hunt_certificate.json"


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


def run_scaffold() -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), "--mesh-N", "1"],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stdout)
    return json.loads(proc.stdout)


def run_residual_template() -> tuple[int, str]:
    proc = subprocess.run(
        [sys.executable, str(RESIDUAL_VALIDATOR), str(RESIDUAL_TEMPLATE)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return proc.returncode, proc.stdout


def branch_schema_smoke() -> tuple[int, int, str]:
    branch = {
        "branch": "current_q79_orientation",
        "torsion_label_m": 1,
        "global_cp_label": 79,
        "conditional_su5_transport_orientation": "F",
        "sector_orientations": {
            "Q": 1,
            "L": 1,
            "u": 2,
            "d": 2,
            "e": 2,
            "N": 2,
            "H": 0,
        },
        "c6_left_representative_labels": {
            "u:C6": 79,
            "d:C6": 79,
            "e:C6": 79,
            "nuD:C6": 79,
        },
        "selected_branch_claimed_by_residual_solution": True,
        "antiunitary_conjugate_retained_for_comparison": True,
        "dotD_same_branch_derivative_required": True,
    }
    candidate = {
        "certificate": "RouteCBranchSchemaSmoke",
        "status": "SMOKE_CLOSED",
        "mesh_N": 1,
        "selected_source_verified": True,
        "no_observed_flavor_inputs": True,
        "uses_execution_ii_benchmarks": False,
        "uses_diagnostic_h1_three_as_selected": False,
        "branch_packet": branch,
        "residuals": {
            name: {"value": 0.0, "tolerance": 1e-9}
            for name in (
                "rho_cocycle",
                "metric_compatibility",
                "integrability_F02",
                "hym_primitive",
                "bianchi_alpha1",
                "strominger_residual",
                "mtt_gradient",
            )
        },
        "positive_gates": {
            "mtt_hessian_min_eigenvalue": {
                "value": 1.0,
                "strict_lower_bound": 0.0,
            },
            "riesz_gap_min": {"value": 1.0, "strict_lower_bound": 0.0},
        },
        "downstream_data_paths": {
            "rhoE_mesh": "candidate_data/rhoE.json",
            "rhoE_metric": "candidate_data/metric.json",
            "sector_maps": "candidate_data/sectors.json",
            "de_action": "candidate_data/de.json",
            "riesz_gap": "candidate_data/riesz.json",
            "reduced_green": "candidate_data/green.json",
            "dotd_response": "candidate_data/dotd.json",
        },
    }
    bad_candidate = json.loads(json.dumps(candidate))
    bad_candidate["branch_packet"]["torsion_label_m"] = 2

    with tempfile.TemporaryDirectory() as temp_dir:
        good_path = Path(temp_dir) / "good.json"
        bad_path = Path(temp_dir) / "bad.json"
        good_path.write_text(json.dumps(candidate), encoding="utf-8")
        bad_path.write_text(json.dumps(bad_candidate), encoding="utf-8")
        good = subprocess.run(
            [sys.executable, str(RESIDUAL_VALIDATOR), str(good_path)],
            cwd=REPO,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        bad = subprocess.run(
            [sys.executable, str(RESIDUAL_VALIDATOR), str(bad_path)],
            cwd=REPO,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
    return good.returncode, bad.returncode, bad.stdout


def main() -> None:
    cert = load_json(CERT)
    residual_template = load_json(RESIDUAL_TEMPLATE)
    source_hunt = load_json(SOURCE_HUNT)
    paper = read(PAPER)
    scaffold = run_scaffold()
    residual_code, residual_output = run_residual_template()
    branch_good_code, branch_bad_code, branch_bad_output = branch_schema_smoke()

    counts = cert.get("mesh_N1_counts", {})
    script_counts = scaffold.get("mesh", {})
    unknown_blocks = cert.get("unknown_blocks", {})
    residual_gates = " ".join(cert.get("source_residual_gates", []))
    pipeline = cert.get("downstream_validator_pipeline", [])
    open_items = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    gates = [
        Gate(
            "certificate status",
            "FORMULATED"
            if cert.get("status")
            == "IWASAWA_ROUTE_C_FINITE_SOLVE_SCAFFOLD_FORMULATED_SELECTED_VALUES_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "source hunt dependency",
            "PASS"
            if source_hunt.get("hunt_result", {}).get("selected_D_E_source_found")
            is False
            and source_hunt.get("verdict", {}).get("route_c_should_be_built_next")
            is True
            else "FAIL",
            str(source_hunt.get("verdict", {})),
        ),
        Gate(
            "scaffold script counts",
            "PASS" if counts == script_counts else "FAIL",
            str(script_counts),
        ),
        Gate(
            "mesh N1 accounting",
            "PASS"
            if counts.get("closed_cell_nodes") == 64
            and counts.get("boundary_face_incidences") == 192
            and counts.get("unique_rho_boundary_matrices_table_ansatz") == 144
            and counts.get("rank3_bundle_dofs_identity_smoke") == 3
            else "FAIL",
            str(counts),
        ),
        Gate(
            "unknown blocks",
            "PASS"
            if set(unknown_blocks)
            == {
                "branch_packet",
                "rho_E",
                "Hermitian_metric",
                "sector_projectors",
                "A01_or_DE_action",
                "dotD_alpha1",
            }
            else "FAIL",
            str(unknown_blocks),
        ),
        Gate(
            "source residual gates",
            "PASS"
            if contains_all(
                residual_gates,
                [
                    "branch packet",
                    "antiunitary conjugate",
                    "same-branch derivative",
                    "cocycle",
                    "metric compatibility",
                    "integrability",
                    "HYM",
                    "Bianchi",
                    "selection gradient",
                    "Hessian/Riesz gap",
                    "no observed flavor",
                ],
            )
            else "FAIL",
            residual_gates,
        ),
        Gate(
            "residual validator exists",
            "PASS"
            if RESIDUAL_VALIDATOR.exists()
            and contains_all(
                read(RESIDUAL_VALIDATOR),
                [
                    "REQUIRED_RESIDUALS",
                    "EXPECTED_BRANCH_PACKETS",
                    "validate_branch_packet",
                    "antiunitary_conjugate_retained_for_comparison",
                    "integrability_F02",
                    "hym_primitive",
                    "mtt_hessian_min_eigenvalue",
                    "no_observed_flavor_inputs",
                ],
            )
            else "FAIL",
            str(RESIDUAL_VALIDATOR),
        ),
        Gate(
            "open template stays open",
            "PASS"
            if residual_template.get("status") == "OPEN"
            and isinstance(residual_template.get("branch_packet"), dict)
            and residual_template["branch_packet"].get(
                "antiunitary_conjugate_retained_for_comparison"
            )
            is True
            and residual_code == 2
            and "OPEN" in residual_output
            else "FAIL",
            residual_output.strip(),
        ),
        Gate(
            "branch schema smoke tests",
            "PASS"
            if branch_good_code == 0
            and branch_bad_code == 1
            and "branch_packet.torsion_label_m" in branch_bad_output
            else "FAIL",
            f"good={branch_good_code}, bad={branch_bad_code}, bad_output={branch_bad_output.strip()}",
        ),
        Gate(
            "validator pipeline",
            "PASS"
            if pipeline
            == [
                "validate_iwasawa_route_c_residuals.py",
                "validate_iwasawa_rhoE_mesh.py",
                "validate_iwasawa_rhoE_metric.py",
                "validate_iwasawa_sector_maps.py",
                "validate_iwasawa_de_action.py",
                "validate_iwasawa_riesz_gap.py",
                "validate_iwasawa_reduced_green.py",
                "validate_iwasawa_dotd_response.py",
            ]
            else "FAIL",
            str(pipeline),
        ),
        Gate(
            "still open",
            "OPEN"
            if all(value is True for value in open_items.values())
            else "FAIL",
            str(open_items),
        ),
        Gate(
            "guardrails",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("route_c_scaffold_constructed") is True
            and verdict.get("route_c_residual_schema_is_branch_aware") is True
            and verdict.get("selected_values_open") is True
            and "small-N nonlinear residual search" in verdict.get("next_step", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records scaffold",
            "PASS"
            if contains_all(
                paper,
                [
                    "Finite Mesh Accounting",
                    "Branch Packet Gate",
                    "antiunitary conjugate branch",
                    "Source Residual Gate",
                    "Validator Order",
                    "This closes",
                    "It leaves open",
                    "N=1 or N=2",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa Route C finite solve scaffold audit")
    print("===========================================")
    print()
    print(f"mesh_N1_counts={counts}")
    print(f"residual_template_exit={residual_code}")
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
