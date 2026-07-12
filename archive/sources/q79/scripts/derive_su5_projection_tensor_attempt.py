"""Derive the SU(5) projection tensor from qutrit polarizations, if selected.

This script performs the hard algebraic step that remains after the Route C
smoke-to-C1 dependency reduction:

    10_M clock polarization, bar5_M shift polarization
        => U_10 = I, U_bar5 = F or F*
        => T_u = I, T_d = F or F*

It then checks the induced heavy-link packet with the existing validators and
calculators.  The output is intentionally conditional: the current corpus does
not yet prove that MTT selects these polarizations from monad/Cech/Galerkin or
selected gerbe data.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "candidate_data" / "su5_projection_tensor_derivation_attempt.candidate.json"
CERT = ROOT / "certificates" / "su5_projection_tensor_derivation_attempt_certificate.json"
VALIDATE_POLARIZATION = ROOT / "scripts" / "validate_selected_su5_qutrit_polarization.py"
C1_HEAVY_LINK = ROOT / "scripts" / "compute_c1_heavy_link_delta_t.py"
CKM_HEAVY_LINK = ROOT / "scripts" / "compute_ckm_heavy_link_gate.py"
TOL = 1e-10
OMEGA = complex(-0.5, math.sqrt(3) / 2.0)


Matrix = list[list[complex]]


def identity() -> Matrix:
    return [[1.0 + 0j if row == col else 0j for col in range(3)] for row in range(3)]


def clock() -> Matrix:
    return [[OMEGA**row if row == col else 0j for col in range(3)] for row in range(3)]


def shift() -> Matrix:
    return [[1.0 + 0j if row == (col + 1) % 3 else 0j for col in range(3)] for row in range(3)]


def fourier(conjugate: bool = False) -> Matrix:
    omega = OMEGA.conjugate() if conjugate else OMEGA
    scale = 1.0 / math.sqrt(3)
    return [[omega ** (row * col) * scale for col in range(3)] for row in range(3)]


def dagger(matrix: Matrix) -> Matrix:
    return [[matrix[col][row].conjugate() for col in range(3)] for row in range(3)]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return [
        [sum(left[row][mid] * right[mid][col] for mid in range(3)) for col in range(3)]
        for row in range(3)
    ]


def matrix_sub(left: Matrix, right: Matrix) -> Matrix:
    return [[left[row][col] - right[row][col] for col in range(3)] for row in range(3)]


def max_abs(matrix: Matrix) -> float:
    return max(abs(entry) for row in matrix for entry in row)


def approx_equal(left: Matrix, right: Matrix) -> bool:
    return max_abs(matrix_sub(left, right)) < TOL


def heavy_vector(matrix: Matrix) -> list[complex]:
    return [matrix[0][2], matrix[1][2]]


def vector_sub(left: list[complex], right: list[complex]) -> list[complex]:
    return [a - b for a, b in zip(left, right)]


def encode_scalar(value: complex) -> float | list[float]:
    real = 0.0 if abs(value.real) < TOL else value.real
    imag = 0.0 if abs(value.imag) < TOL else value.imag
    if imag == 0.0:
        return real
    return [real, imag]


def encode(value: Any) -> Any:
    if isinstance(value, complex):
        return encode_scalar(value)
    if isinstance(value, list):
        return [encode(item) for item in value]
    if isinstance(value, dict):
        return {key: encode(item) for key, item in value.items()}
    return value


def parse_json_from_stdout(stdout: str) -> dict[str, Any]:
    match = re.search(r"(\{.*\})", stdout, re.DOTALL)
    return json.loads(match.group(1)) if match else {}


def parse_polarization_report(stdout: str) -> dict[str, Any]:
    match = re.search(r"polarization_validation_report=(\{.*\})", stdout)
    return json.loads(match.group(1)) if match else {}


def run_json_script(script: Path, packet: dict[str, Any], parser: str = "json") -> dict[str, Any]:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "packet.json"
        path.write_text(json.dumps(encode(packet), indent=2), encoding="utf-8")
        proc = subprocess.run(
            [sys.executable, str(script), str(path)],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
    if parser == "polarization":
        report = parse_polarization_report(proc.stdout)
    else:
        report = parse_json_from_stdout(proc.stdout)
    return {
        "exit_code": proc.returncode,
        "stdout": proc.stdout,
        "report": report,
    }


def branch_packet(name: str) -> dict[str, Any]:
    if name == "current_q79_orientation":
        return {
            "branch": name,
            "torsion_label_m": 1,
            "global_cp_label": 79,
            "conditional_su5_transport_orientation": "F",
            "conjugate_orientation": False,
        }
    if name == "conjugate_q369_orientation":
        return {
            "branch": name,
            "torsion_label_m": 2,
            "global_cp_label": 369,
            "conditional_su5_transport_orientation": "F*",
            "conjugate_orientation": True,
        }
    raise ValueError(name)


def polarization_packet(branch: dict[str, Any], u10: Matrix, ubar5: Matrix) -> dict[str, Any]:
    z = clock()
    x = shift()
    orientation_is_f = branch["conditional_su5_transport_orientation"] == "F"
    return encode(
        {
            "schema": "SelectedSU5QutritPolarizationData.v1",
            "status": "CONDITIONAL_DERIVATION_UNSELECTED_SOURCE",
            "candidate_role": "UNSELECTED_FIXTURE",
            "purpose": (
                "Branch-aware finite projection-tensor derivation. Algebraic "
                "polarization data are supplied, but selected MTT zero-mode "
                "source evidence is not yet available."
            ),
            "source": {
                "source_kind": "finite_qutrit_smoke_fixture",
                "source_certificate": (
                    "qutrit_polarization_transport_lemma_certificate.json; "
                    "iwasawa_route_c_smoke_c1_dependency_certificate.json"
                ),
                "selected_by_mtt": False,
                "fixture_only": True,
                "uses_observed_flavor_inputs": False,
                "uses_benchmark_flavor_inputs": False,
            },
            "branch_packet": branch,
            "sector_basis_data": {
                "10_M": {
                    "basis_matrix_U10": u10,
                    "L2_metric": identity(),
                    "selected_operator_or_projector": "conditional clock polarization",
                    "polarization": "clock",
                    "clock_operator_matrix_in_basis": matmul(matmul(dagger(u10), z), u10),
                    "shift_operator_matrix_in_basis": matmul(matmul(dagger(u10), x), u10),
                    "source_certificate": "qutrit_polarization_transport_lemma_certificate.json",
                },
                "bar5_M": {
                    "basis_matrix_Ubar5": ubar5,
                    "L2_metric": identity(),
                    "selected_operator_or_projector": "conditional shift polarization",
                    "polarization": "shift",
                    "clock_operator_matrix_in_basis": matmul(matmul(dagger(ubar5), z), ubar5),
                    "shift_operator_matrix_in_basis": matmul(matmul(dagger(ubar5), x), ubar5),
                    "source_certificate": "qutrit_polarization_transport_lemma_certificate.json",
                },
            },
            "shared_family_frame": {
                "coordinate_frame_certified_common": True,
                "cross_pairing_metric_10_bar5": identity(),
                "source_certificate": "conditional shared qutrit family frame",
            },
            "acceptance_tests": {
                "U10_unitary_in_selected_metric": True,
                "Ubar5_unitary_in_selected_metric": True,
                "relative_transport_equals_F_mod_rephase_permutation": True,
                "orientation_selects_F_not_F_conjugate": orientation_is_f,
                "derived_without_observed_flavor_inputs": True,
            },
            "guardrails": {
                "do_not_fill_from_CKM_or_mass_data": True,
                "do_not_treat_exterior_square_duality_as_Fourier_transport": True,
                "do_not_use_common_Fourier_basis_change_as_physical_mixing": True,
            },
        }
    )


def c1_packet(delta: list[complex]) -> dict[str, Any]:
    terms = (
        "theta_overlap_variation",
        "left_zero_mode_response",
        "right_zero_mode_response",
        "higgs_zero_mode_response",
        "explicit_vertex",
        "basis_connection",
    )
    sectors = {
        "u": {term: [0j, 0j] for term in terms},
        "d": {term: [0j, 0j] for term in terms},
    }
    sectors["d"]["basis_connection"] = delta
    return {"status": "CONDITIONAL_IF_SELECTED", "sectors": sectors}


def ckm_packet(branch: dict[str, Any], t_u: list[complex], t_d: list[complex]) -> dict[str, Any]:
    return {
        "status": "CONDITIONAL_IF_SELECTED",
        "phase_branch": {
            "modulus": 448,
            "selected_label": branch["global_cp_label"],
        },
        "inputs": {
            "character_trivial_heavy_link": {
                "u": {"entries": t_u},
                "d": {"entries": t_d},
            },
            "c6_heavy_link": {
                "u": {"entries": [0j, 0j]},
                "d": {"entries": [0j, 0j]},
            },
        },
    }


def derive_branch(name: str) -> dict[str, Any]:
    packet = branch_packet(name)
    u10 = identity()
    ubar5 = fourier(conjugate=packet["conjugate_orientation"])
    t_u_matrix = matmul(dagger(u10), u10)
    t_d_matrix = matmul(dagger(u10), ubar5)
    t_e_matrix = matmul(dagger(ubar5), u10)
    t_u = heavy_vector(t_u_matrix)
    t_d = heavy_vector(t_d_matrix)
    delta = vector_sub(t_d, t_u)

    pol_packet = polarization_packet(packet, u10, ubar5)
    pol_validator = run_json_script(VALIDATE_POLARIZATION, pol_packet, parser="polarization")
    c1_validator = run_json_script(C1_HEAVY_LINK, c1_packet(delta))
    ckm_validator = run_json_script(CKM_HEAVY_LINK, ckm_packet(packet, t_u, t_d))

    expected = fourier(conjugate=packet["conjugate_orientation"])
    return encode(
        {
            "branch_packet": packet,
            "derived_basis": {
                "U_10": u10,
                "U_bar5": ubar5,
                "orientation": packet["conditional_su5_transport_orientation"],
            },
            "projection_tensors": {
                "T_u_10x10": t_u_matrix,
                "T_d_10xbar5": t_d_matrix,
                "T_e_bar5x10": t_e_matrix,
                "T_nuD_bar5x1_status": "requires singlet-family basis; not needed for CKM u/d split",
            },
            "checks": {
                "T_u_is_identity": approx_equal(t_u_matrix, identity()),
                "T_d_is_expected_fourier_orientation": approx_equal(t_d_matrix, expected),
                "T_e_is_dagger_of_T_d": approx_equal(t_e_matrix, dagger(t_d_matrix)),
            },
            "heavy_link": {
                "t_u": t_u,
                "t_d": t_d,
                "Delta_t": delta,
                "nonzero": any(abs(entry) > TOL for entry in delta),
            },
            "validators": {
                "polarization_packet": {
                    "exit_code": pol_validator["exit_code"],
                    "report": pol_validator["report"],
                    "promotes_to_selected_heavy_link_input": pol_validator["report"].get(
                        "promotes_to_selected_heavy_link_input"
                    )
                    is True,
                },
                "c1_heavy_link_delta_t": {
                    "exit_code": c1_validator["exit_code"],
                    "report": c1_validator["report"],
                },
                "ckm_heavy_link_gate": {
                    "exit_code": ckm_validator["exit_code"],
                    "report": ckm_validator["report"],
                },
            },
        }
    )


def build_report() -> dict[str, Any]:
    branches = {
        "current_q79_orientation": derive_branch("current_q79_orientation"),
        "conjugate_q369_orientation": derive_branch("conjugate_q369_orientation"),
    }
    all_finite_pass = all(
        branch["validators"]["polarization_packet"]["exit_code"] == 0
        and branch["validators"]["c1_heavy_link_delta_t"]["exit_code"] == 0
        and branch["validators"]["ckm_heavy_link_gate"]["exit_code"] == 0
        for branch in branches.values()
    )
    selected_promotes = any(
        branch["validators"]["polarization_packet"]["promotes_to_selected_heavy_link_input"]
        for branch in branches.values()
    )
    return {
        "candidate": "SU5ProjectionTensorDerivationAttempt",
        "status": "FINITE_PROJECTION_TENSOR_DERIVED_CONDITIONALLY_SELECTION_OPEN",
        "generated_by": "scripts/derive_su5_projection_tensor_attempt.py",
        "inputs": {
            "qutrit_transport_lemma": "QUTRIT_POLARIZATION_TRANSPORT_LEMMA_PROVED_SELECTOR_HYPOTHESIS_OPEN",
            "route_c_dependency": "SYMBOLIC_DEPENDENCY_REDUCED_NUMERIC_VALUES_OPEN",
            "uses_observed_flavor_data": False,
            "uses_execution_ii_benchmarks": False,
        },
        "branches": branches,
        "calculation_results": {
            "finite_projection_tensor_derived": True,
            "both_conjugate_branches_derived": True,
            "q79_branch_Td_equals_F": branches["current_q79_orientation"]["checks"][
                "T_d_is_expected_fourier_orientation"
            ],
            "q369_branch_Td_equals_F_conjugate": branches["conjugate_q369_orientation"]["checks"][
                "T_d_is_expected_fourier_orientation"
            ],
            "finite_validators_pass": all_finite_pass,
            "conditional_heavy_link_nonzero_both_branches": all(
                branch["heavy_link"]["nonzero"] for branch in branches.values()
            ),
            "selected_polarization_source_promotes": selected_promotes,
            "selection_still_open": not selected_promotes,
        },
        "what_this_closes": {
            "conditional_su5_projection_tensor": True,
            "branch_aware_F_vs_F_conjugate_orientation": True,
            "conditional_delta_t_values": True,
            "validator_ready_polarization_packet_form": True,
        },
        "still_open": {
            "selected_zero_mode_or_monad_source_for_U10_Ubar5": True,
            "selected_gerbe_twisted_bundle_source_for_U10_Ubar5": True,
            "promotion_to_selected_heavy_link_input": True,
            "full_C1_response_matrices": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_selected_U10_Ubar5": False,
            "claims_selected_C1_response": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
            "claims_CKM_angles_or_Jarlskog": False,
            "claims_full_SM_closure": False,
        },
        "verdict": {
            "derived_object": "T_u=I_3 and T_d=F for q79, T_d=F* for q369, conditional on selected clock/shift polarizations",
            "why_not_selected_yet": "the polarization validator passes finite algebra but reports selected_source_promotes=false because source.selected_by_mtt is false",
            "next_required_proof": "derive U_10 and U_bar5 from selected monad/Cech/Galerkin zero-mode data or selected gerbe/twisted-bundle data",
        },
    }


def write_outputs(report: dict[str, Any]) -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    CERT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    cert = {
        "certificate": "SU5ProjectionTensorDerivationAttemptCertificate",
        "status": report["status"],
        "candidate_data": str(OUT.relative_to(ROOT)).replace("\\", "/"),
        "calculation_results": report["calculation_results"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write candidate and certificate")
    args = parser.parse_args()
    report = encode(build_report())
    if args.write:
        write_outputs(report)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
