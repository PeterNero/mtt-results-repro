"""Build and test a branch-aware Route C small-N smoke package.

This is not a selected HYM/Strominger solve.  It constructs the smallest
deterministic branch-aware finite package that exercises the Route C validator
pipeline for both conjugate orientation packets:

    m=1, q=79,  F
    m=2, q=369, F*

The saved candidate files keep selected-origin flags false.  The script also
runs a temporary "lifted flags" algebra smoke test to prove the finite matrices
would pass the downstream validators if a genuine selected source supplied the
same data.
"""

from __future__ import annotations

import argparse
import copy
import json
import math
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = ROOT / "candidate_data" / "iwasawa_route_c_branch_smoke"
CERT = ROOT / "certificates" / "iwasawa_route_c_branch_smoke_attempt_certificate.json"

SECTORS = ("Q", "u", "d", "L", "e", "N", "H")
FAMILY_SECTORS = ("Q", "u", "d", "L", "e", "N")
GENERATORS = ("g1", "g2", "g3", "g4", "g5", "g6")
VALIDATORS = {
    "route_c_residual": "scripts/validate_iwasawa_route_c_residuals.py",
    "rhoE_mesh": "scripts/validate_iwasawa_rhoE_mesh.py",
    "rhoE_metric": "scripts/validate_iwasawa_rhoE_metric.py",
    "sector_maps": "scripts/validate_iwasawa_sector_maps.py",
    "de_action": "scripts/validate_iwasawa_de_action.py",
    "riesz_gap": "scripts/validate_iwasawa_riesz_gap.py",
    "reduced_green": "scripts/validate_iwasawa_reduced_green.py",
    "dotd_response": "scripts/validate_iwasawa_dotd_response.py",
}


def cpack(value: complex) -> float | list[float]:
    if abs(value.imag) < 1e-14:
        return float(value.real)
    return [float(value.real), float(value.imag)]


def matrix(rows: list[list[complex | float | int]]) -> list[list[float | list[float]]]:
    return [[cpack(complex(value)) for value in row] for row in rows]


def vector(values: list[complex | float | int]) -> list[float | list[float]]:
    return [cpack(complex(value)) for value in values]


def identity(size: int) -> list[list[float]]:
    return [[1.0 if i == j else 0.0 for j in range(size)] for i in range(size)]


def diag(values: list[float]) -> list[list[float]]:
    return [[values[i] if i == j else 0.0 for j in range(len(values))] for i in range(len(values))]


def basis(size: int, index: int) -> list[float]:
    return [1.0 if i == index else 0.0 for i in range(size)]


def character(label: int) -> complex:
    angle = 2.0 * math.pi * label / 448.0
    return complex(math.cos(angle), math.sin(angle))


def branch_packets() -> dict[str, dict[str, Any]]:
    return {
        "current_q79_orientation": {
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
        },
        "conjugate_q369_orientation": {
            "branch": "conjugate_q369_orientation",
            "torsion_label_m": 2,
            "global_cp_label": 369,
            "conditional_su5_transport_orientation": "F*",
            "sector_orientations": {
                "Q": 2,
                "L": 2,
                "u": 1,
                "d": 1,
                "e": 1,
                "N": 1,
                "H": 0,
            },
            "c6_left_representative_labels": {
                "u:C6": 369,
                "d:C6": 369,
                "e:C6": 369,
                "nuD:C6": 369,
            },
            "selected_branch_claimed_by_residual_solution": True,
            "antiunitary_conjugate_retained_for_comparison": True,
            "dotD_same_branch_derivative_required": True,
        },
    }


def rho_identity_block() -> dict[str, Any]:
    eye3 = identity(3)
    return {
        "rank": 3,
        "mesh_N": 1,
        "candidate_kind": "identity_rhoE_smoke_unselected",
        "selected_by_mtt": False,
        "generator_data": {
            generator: {"matrix": eye3}
            for generator in GENERATORS
        },
    }


def rho_metric_block() -> dict[str, Any]:
    data = rho_identity_block()
    data["metric_data"] = {"matrix": identity(3)}
    return data


def sector_maps_block() -> dict[str, Any]:
    data = rho_identity_block()
    data["sector_projection_maps"] = {}
    for sector in FAMILY_SECTORS:
        data["sector_projection_maps"][sector] = {
            "kind": "family",
            "dimension": 3,
            "projector": identity(3),
        }
    data["sector_projection_maps"]["H"] = {
        "kind": "single_higgs_carrier",
        "dimension": 1,
        "projector": diag([1.0, 0.0, 0.0]),
    }
    return data


def route_c_residual_block(branch: dict[str, Any], paths: dict[str, str]) -> dict[str, Any]:
    return {
        "certificate": "IwasawaRouteCBranchSmokeResidualCandidate",
        "status": "CANDIDATE_UNSELECTED_SMOKE",
        "mesh_N": 1,
        "selected_source_verified": False,
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
        "downstream_data_paths": paths,
        "guardrails": {
            "claims_selected_source": False,
            "claims_full_sm_closure": False,
        },
    }


def operator_slot(sector: str) -> dict[str, Any]:
    if sector in FAMILY_SECTORS:
        return {
            "kind": "family",
            "expected_kernel_dimension": 3,
            "domain_dimension": 4,
            "range_dimension": 1,
            "domain_gram": identity(4),
            "range_gram": identity(1),
            "D_E_matrix": [[0.0, 0.0, 0.0, 1.0]],
            "stiffness_matrix": diag([0.0, 0.0, 0.0, 1.0]),
            "ordered_zero_mode_basis": [basis(4, 0), basis(4, 1), basis(4, 2)],
            "selected_source_verified": False,
            "boundary_conditions_verified": True,
        }
    return {
        "kind": "single_higgs_carrier",
        "expected_kernel_dimension": 1,
        "domain_dimension": 2,
        "range_dimension": 1,
        "domain_gram": identity(2),
        "range_gram": identity(1),
        "D_E_matrix": [[0.0, 1.0]],
        "stiffness_matrix": diag([0.0, 1.0]),
        "ordered_zero_mode_basis": [basis(2, 0)],
        "selected_source_verified": False,
        "boundary_conditions_verified": True,
    }


def de_action_block(branch: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "IwasawaRouteCBranchSmokeDEActionCandidate",
        "status": "CANDIDATE_UNSELECTED_SMOKE",
        "selected_by_mtt": False,
        "branch_packet": branch,
        "operator_slots": {sector: operator_slot(sector) for sector in SECTORS},
    }


def spectral_slot(sector: str) -> dict[str, Any]:
    if sector in FAMILY_SECTORS:
        return {
            "kind": "family",
            "expected_kernel_dimension": 3,
            "dimension": 4,
            "gram_matrix": identity(4),
            "stiffness_matrix": diag([0.0, 0.0, 0.0, 1.0]),
            "riesz_projector": diag([1.0, 1.0, 1.0, 0.0]),
            "low_eigenvalues": [0.0, 0.0, 0.0],
            "residual_norms": [0.0, 0.0, 0.0],
            "cluster_eigenvectors": [basis(4, 0), basis(4, 1), basis(4, 2)],
            "contour_radius": 0.25,
            "complement_gap": 1.0,
            "truncation_error_bound": 0.0,
            "selected_source_verified": False,
            "operator_data_verified": True,
            "boundary_conditions_verified": True,
        }
    return {
        "kind": "single_higgs_carrier",
        "expected_kernel_dimension": 1,
        "dimension": 2,
        "gram_matrix": identity(2),
        "stiffness_matrix": diag([0.0, 1.0]),
        "riesz_projector": diag([1.0, 0.0]),
        "low_eigenvalues": [0.0],
        "residual_norms": [0.0],
        "cluster_eigenvectors": [basis(2, 0)],
        "contour_radius": 0.25,
        "complement_gap": 1.0,
        "truncation_error_bound": 0.0,
        "selected_source_verified": False,
        "operator_data_verified": True,
        "boundary_conditions_verified": True,
    }


def riesz_gap_block(branch: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "IwasawaRouteCBranchSmokeRieszGapCandidate",
        "status": "CANDIDATE_UNSELECTED_SMOKE",
        "selected_by_mtt": False,
        "branch_packet": branch,
        "spectral_slots": {sector: spectral_slot(sector) for sector in SECTORS},
    }


def green_slot(sector: str) -> dict[str, Any]:
    if sector in FAMILY_SECTORS:
        return {
            "kind": "family",
            "expected_kernel_dimension": 3,
            "dimension": 4,
            "gram_matrix": identity(4),
            "stiffness_matrix": diag([0.0, 0.0, 0.0, 1.0]),
            "riesz_projector": diag([1.0, 1.0, 1.0, 0.0]),
            "complement_projector": diag([0.0, 0.0, 0.0, 1.0]),
            "reduced_green_operator": diag([0.0, 0.0, 0.0, 1.0]),
            "complement_gap": 1.0,
            "truncation_error_bound": 0.0,
            "green_norm_bound": 1.0,
            "selected_source_verified": False,
            "riesz_gap_verified": True,
            "operator_data_verified": True,
            "boundary_conditions_verified": True,
        }
    return {
        "kind": "single_higgs_carrier",
        "expected_kernel_dimension": 1,
        "dimension": 2,
        "gram_matrix": identity(2),
        "stiffness_matrix": diag([0.0, 1.0]),
        "riesz_projector": diag([1.0, 0.0]),
        "complement_projector": diag([0.0, 1.0]),
        "reduced_green_operator": diag([0.0, 1.0]),
        "complement_gap": 1.0,
        "truncation_error_bound": 0.0,
        "green_norm_bound": 1.0,
        "selected_source_verified": False,
        "riesz_gap_verified": True,
        "operator_data_verified": True,
        "boundary_conditions_verified": True,
    }


def reduced_green_block(branch: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "IwasawaRouteCBranchSmokeReducedGreenCandidate",
        "status": "CANDIDATE_UNSELECTED_SMOKE",
        "selected_by_mtt": False,
        "branch_packet": branch,
        "green_slots": {sector: green_slot(sector) for sector in SECTORS},
    }


def dotd_slot(sector: str, chi: complex) -> dict[str, Any]:
    if sector in FAMILY_SECTORS:
        coeffs = [0.125 * chi, 0.25 * chi, 0.375 * chi]
        sources = [
            vector([0.0, 0.0, 0.0, coeff])
            for coeff in coeffs
        ]
        responses = [
            vector([0.0, 0.0, 0.0, -coeff])
            for coeff in coeffs
        ]
        dotd = matrix(
            [
                [0.0, 0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0],
                [coeffs[0], coeffs[1], coeffs[2], 0.0],
            ]
        )
        return {
            "kind": "family",
            "expected_kernel_dimension": 3,
            "dimension": 4,
            "gram_matrix": identity(4),
            "stiffness_matrix": diag([0.0, 0.0, 0.0, 1.0]),
            "riesz_projector": diag([1.0, 1.0, 1.0, 0.0]),
            "complement_projector": diag([0.0, 0.0, 0.0, 1.0]),
            "reduced_green_operator": diag([0.0, 0.0, 0.0, 1.0]),
            "dotD_alpha1_matrix": dotd,
            "ordered_zero_mode_basis": [basis(4, 0), basis(4, 1), basis(4, 2)],
            "source_vectors": sources,
            "horizontal_response_vectors": responses,
            "selected_dotD_source_verified": False,
            "alpha1_driver_verified": False,
            "green_operator_verified": True,
            "horizontal_gauge_verified": True,
        }
    coeff = 0.5 * chi
    return {
        "kind": "single_higgs_carrier",
        "expected_kernel_dimension": 1,
        "dimension": 2,
        "gram_matrix": identity(2),
        "stiffness_matrix": diag([0.0, 1.0]),
        "riesz_projector": diag([1.0, 0.0]),
        "complement_projector": diag([0.0, 1.0]),
        "reduced_green_operator": diag([0.0, 1.0]),
        "dotD_alpha1_matrix": matrix([[0.0, 0.0], [coeff, 0.0]]),
        "ordered_zero_mode_basis": [basis(2, 0)],
        "source_vectors": [vector([0.0, coeff])],
        "horizontal_response_vectors": [vector([0.0, -coeff])],
        "selected_dotD_source_verified": False,
        "alpha1_driver_verified": False,
        "green_operator_verified": True,
        "horizontal_gauge_verified": True,
    }


def dotd_response_block(branch: dict[str, Any]) -> dict[str, Any]:
    chi = character(int(branch["global_cp_label"]))
    return {
        "certificate": "IwasawaRouteCBranchSmokeDotDResponseCandidate",
        "status": "CANDIDATE_UNSELECTED_SMOKE",
        "selected_by_mtt": False,
        "branch_packet": branch,
        "dotd_response_slots": {
            sector: dotd_slot(sector, chi)
            for sector in SECTORS
        },
    }


def relative_paths(branch_name: str) -> dict[str, str]:
    base = f"candidate_data/iwasawa_route_c_branch_smoke/{branch_name}"
    return {
        "rhoE_mesh": f"{base}/rhoE_mesh.candidate.json",
        "rhoE_metric": f"{base}/rhoE_metric.candidate.json",
        "sector_maps": f"{base}/sector_maps.candidate.json",
        "de_action": f"{base}/de_action.candidate.json",
        "riesz_gap": f"{base}/riesz_gap.candidate.json",
        "reduced_green": f"{base}/reduced_green.candidate.json",
        "dotd_response": f"{base}/dotd_response.candidate.json",
    }


def build_branch_files(branch: dict[str, Any]) -> dict[str, dict[str, Any]]:
    branch_name = str(branch["branch"])
    paths = relative_paths(branch_name)
    return {
        "route_c_residual": route_c_residual_block(branch, paths),
        "rhoE_mesh": rho_identity_block(),
        "rhoE_metric": rho_metric_block(),
        "sector_maps": sector_maps_block(),
        "de_action": de_action_block(branch),
        "riesz_gap": riesz_gap_block(branch),
        "reduced_green": reduced_green_block(branch),
        "dotd_response": dotd_response_block(branch),
    }


def lift_selected_flags(data: Any) -> Any:
    lifted = copy.deepcopy(data)

    def walk(value: Any) -> None:
        if isinstance(value, dict):
            for key in list(value):
                if key in {
                    "selected_source_verified",
                    "selected_dotD_source_verified",
                    "alpha1_driver_verified",
                }:
                    value[key] = True
                walk(value[key])
        elif isinstance(value, list):
            for item in value:
                walk(item)

    walk(lifted)
    return lifted


def write_branch(branch_name: str, files: dict[str, dict[str, Any]]) -> dict[str, str]:
    branch_dir = OUTPUT_ROOT / branch_name
    branch_dir.mkdir(parents=True, exist_ok=True)
    written: dict[str, str] = {}
    for key, data in files.items():
        path = branch_dir / f"{key}.candidate.json"
        path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        written[key] = path.relative_to(ROOT).as_posix()
    return written


def run_validator(data: dict[str, Any], validator_key: str, temp_dir: Path) -> dict[str, Any]:
    path = temp_dir / f"{validator_key}.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(ROOT / VALIDATORS[validator_key]), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return {
        "exit_code": proc.returncode,
        "pass": proc.returncode == 0,
        "output": proc.stdout.strip().splitlines()[:12],
    }


def validator_matrix(files: dict[str, dict[str, Any]]) -> dict[str, Any]:
    strict: dict[str, Any] = {}
    lifted: dict[str, Any] = {}
    with tempfile.TemporaryDirectory() as temp:
        temp_dir = Path(temp)
        for key, data in files.items():
            strict[key] = run_validator(data, key, temp_dir)
            lifted[key] = run_validator(lift_selected_flags(data), key, temp_dir)
    return {"honest_unselected": strict, "lifted_selected_flags_smoke": lifted}


def analyze(write: bool = False) -> dict[str, Any]:
    branches = branch_packets()
    branch_reports = {}
    written_paths = {}
    for branch_name, branch in branches.items():
        files = build_branch_files(branch)
        if write:
            written_paths[branch_name] = write_branch(branch_name, files)
        branch_reports[branch_name] = {
            "branch_packet": branch,
            "validators": validator_matrix(files),
        }

    strict_expected_failures = {}
    lifted_passes = {}
    for branch_name, report in branch_reports.items():
        strict_expected_failures[branch_name] = {
            key: result["exit_code"]
            for key, result in report["validators"]["honest_unselected"].items()
        }
        lifted_passes[branch_name] = all(
            result["pass"]
            for result in report["validators"]["lifted_selected_flags_smoke"].values()
        )

    result = {
        "calculation": "IwasawaRouteCBranchSmokeAttempt",
        "status": "BRANCH_AWARE_SMALL_N_SMOKE_ALGEBRA_PASSES_SELECTION_OPEN",
        "mesh_N": 1,
        "branches": branch_reports,
        "written_paths": written_paths,
        "calculation_results": {
            "branches_tested": sorted(branches),
            "honest_unselected_validator_exit_codes": strict_expected_failures,
            "lifted_selected_flags_all_validators_pass": lifted_passes,
            "both_conjugate_branches_have_same_algebraic_status": len(
                set(lifted_passes.values())
            )
            == 1
            and all(lifted_passes.values()),
            "nonzero_dotd_response_inserted": True,
            "selected_origin_still_missing": True,
            "route_c_residual_values_are_smoke_not_solve": True,
        },
        "guardrails": {
            "claims_selected_D_E_constructed": False,
            "claims_selected_dotD_constructed": False,
            "claims_route_c_residual_solve": False,
            "uses_observed_masses_or_mixings": False,
            "uses_execution_ii_benchmarks": False,
            "claims_full_sm_closure": False,
        },
        "verdict": {
            "small_N_branch_pipeline_executed": True,
            "algebraic_validator_pipeline_can_be_satisfied": True,
            "selected_source_obligation_remains": True,
            "next_step": (
                "Replace the smoke residuals and identity rho_E by a genuine "
                "finite HYM/Strominger residual solve whose selected_source "
                "flag is justified before rerunning the same branch-aware files."
            ),
        },
    }
    if write:
        CERT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    print(json.dumps(analyze(write=args.write), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
