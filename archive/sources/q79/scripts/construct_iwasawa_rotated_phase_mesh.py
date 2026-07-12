"""Construct a Fourier-rotated diagonal finite-mesh rho_E prototype.

The diagonal phase prototype distinguishes the three fiber components but is
diagonal in the chosen basis.  This script conjugates it by the rank-three
Fourier unitary.  The resulting matrices are generally off diagonal in the
standard basis and still pass the mesh/metric validators.  A compatible
rank-one Higgs projector is included for the sector-map validator.

This remains a simultaneously diagonalizable prototype, not physical flavor
mixing and not selected MTT data.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

from construct_iwasawa_diagonal_phase_mesh import construct, parse_indices


FAMILY_SECTORS = ("Q", "u", "d", "L", "e", "N")
TOL = 1e-9

Matrix = list[list[complex]]


def parse_complex(value: Any) -> complex:
    if isinstance(value, (int, float)):
        return complex(float(value), 0.0)
    if (
        isinstance(value, list)
        and len(value) == 2
        and all(isinstance(part, (int, float)) for part in value)
    ):
        return complex(float(value[0]), float(value[1]))
    raise ValueError(f"invalid complex entry {value!r}")


def parse_matrix(entry: Any) -> Matrix:
    matrix_data = entry.get("matrix") if isinstance(entry, dict) else entry
    return [[parse_complex(value) for value in row] for row in matrix_data]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(3))
            for j in range(3)
        ]
        for i in range(3)
    ]


def adjoint(matrix: Matrix) -> Matrix:
    return [[matrix[j][i].conjugate() for j in range(3)] for i in range(3)]


def max_abs_diff(left: Matrix, right: Matrix) -> float:
    return max(abs(left[i][j] - right[i][j]) for i in range(3) for j in range(3))


def max_offdiag_abs(matrix: Matrix) -> float:
    return max(abs(matrix[i][j]) for i in range(3) for j in range(3) if i != j)


def serialize_complex(value: complex) -> int | float | list[float]:
    real = 0.0 if abs(value.real) < 1e-14 else value.real
    imag = 0.0 if abs(value.imag) < 1e-14 else value.imag
    real = round(real, 15)
    imag = round(imag, 15)
    if imag == 0.0:
        if abs(real - round(real)) < 1e-14:
            return int(round(real))
        return real
    return [real, imag]


def serialize_matrix(matrix: Matrix) -> dict[str, list[list[int | float | list[float]]]]:
    return {
        "matrix": [
            [serialize_complex(value) for value in row]
            for row in matrix
        ]
    }


def identity_matrix() -> Matrix:
    return [
        [1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
        [0.0 + 0.0j, 1.0 + 0.0j, 0.0 + 0.0j],
        [0.0 + 0.0j, 0.0 + 0.0j, 1.0 + 0.0j],
    ]


def basis_projector(index: int) -> Matrix:
    matrix = [[0.0 + 0.0j for _ in range(3)] for _ in range(3)]
    matrix[index][index] = 1.0 + 0.0j
    return matrix


def fourier_unitary() -> Matrix:
    omega = complex(math.cos(2.0 * math.pi / 3.0), math.sin(2.0 * math.pi / 3.0))
    scale = 1.0 / math.sqrt(3.0)
    return [
        [scale * omega ** (row * col) for col in range(3)]
        for row in range(3)
    ]


def conjugate(unitary: Matrix, matrix: Matrix) -> Matrix:
    return matmul(matmul(unitary, matrix), adjoint(unitary))


def commutator(left: Matrix, right: Matrix) -> Matrix:
    return [
        [
            matmul(left, right)[i][j] - matmul(right, left)[i][j]
            for j in range(3)
        ]
        for i in range(3)
    ]


def sector_maps(unitary: Matrix) -> dict[str, dict[str, object]]:
    identity = serialize_matrix(identity_matrix())
    higgs_projector = serialize_matrix(conjugate(unitary, basis_projector(2)))
    maps: dict[str, dict[str, object]] = {
        sector: {
            "kind": "family",
            "dimension": 3,
            "projector": identity,
        }
        for sector in FAMILY_SECTORS
    }
    maps["H"] = {
        "kind": "single_higgs_carrier",
        "dimension": 1,
        "projector": higgs_projector,
    }
    return maps


def rotate_candidate(
    mesh_n: int,
    modulus: int,
    basis_indices: list[int],
) -> tuple[dict[str, object], dict[str, object]]:
    diagonal_summary, diagonal_candidate = construct(mesh_n, modulus, basis_indices)
    unitary = fourier_unitary()

    rotated_generator_data: dict[str, dict[str, dict[str, object]]] = {}
    rotated_matrices: list[Matrix] = []
    for generator, entry in diagonal_candidate["generator_data"].items():  # type: ignore[index]
        values = entry["values"]  # type: ignore[index]
        rotated_values: dict[str, object] = {}
        for target_key, matrix_entry in values.items():
            rotated = conjugate(unitary, parse_matrix(matrix_entry))
            rotated_values[target_key] = serialize_matrix(rotated)
            rotated_matrices.append(rotated)
        rotated_generator_data[generator] = {"values": rotated_values}

    offdiag_values = [
        matrix for matrix in rotated_matrices if max_offdiag_abs(matrix) > 1e-9
    ]
    max_offdiag = max((max_offdiag_abs(matrix) for matrix in rotated_matrices), default=0.0)
    max_commutator = 0.0
    for index, left in enumerate(rotated_matrices):
        for right in rotated_matrices[index + 1 :]:
            max_commutator = max(max_commutator, max_abs_diff(commutator(left, right), [[0j] * 3 for _ in range(3)]))

    candidate: dict[str, object] = {
        "prototype": "IwasawaFourierRotatedPhaseMeshRhoE",
        "status": "PROTOTYPE_UNSELECTED",
        "rank": 3,
        "mesh_N": mesh_n,
        "field": f"F{modulus}",
        "basis_indices": basis_indices,
        "generator_data": rotated_generator_data,
        "metric_data": {"matrix": [[1, 0, 0], [0, 1, 0], [0, 0, 1]]},
        "sector_projection_maps": sector_maps(unitary),
        "guardrails": {
            "claims_selected_rho_E": False,
            "claims_selected_D_E": False,
            "claims_physical_family_mixing": False,
            "uses_observed_flavor_data": False,
        },
    }

    summary: dict[str, object] = {
        "calculation": "IwasawaFourierRotatedPhaseMeshRhoEPrototypeConstruct",
        "mesh_N": mesh_n,
        "field": f"F{modulus}",
        "rank": 3,
        "basis_indices": basis_indices,
        "diagonal_source": {
            "unknown_face_values": diagonal_summary["unknown_face_values"],
            "corner_equations": diagonal_summary["corner_equations"],
            "linear_rank": diagonal_summary["linear_rank"],
            "scalar_nullity": diagonal_summary["scalar_nullity"],
            "diagonal_nonscalar_face_values": diagonal_summary["diagonal_nonscalar_face_values"],
        },
        "rotated_offdiagonal_face_values": len(offdiag_values),
        "rotated_max_offdiag_abs": max_offdiag,
        "rotated_max_pairwise_commutator_abs": max_commutator,
        "higgs_projector": {
            "rank": 1,
            "basis": "Fourier-rotated third diagonal component",
        },
        "sector_projection_format": {
            "family_projectors": "identity rank-three projectors",
            "higgs_projector": "Fourier-rotated rank-one projector",
        },
        "verdict": {
            "offdiagonal_coordinate_basis_rhoE_exists": len(offdiag_values) > 0,
            "simultaneously_diagonalizable_by_fourier": True,
            "genuine_nonabelian_commutator_found": max_commutator > 1e-8,
            "candidate_is_selected_rho_E": False,
            "candidate_proves_physical_family_mixing": False,
            "next_step": "Replace this basis-rotated abelian prototype by noncommuting typed Cech/monad or HYM/Strominger transition data.",
        },
    }
    return summary, candidate


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mesh-N", type=int, default=1, help="closed-cell subdivision N")
    parser.add_argument("--modulus", type=int, default=3, help="finite phase field modulus")
    parser.add_argument(
        "--basis-indices",
        type=parse_indices,
        default=[0, 1, 2],
        help="three scalar nullspace basis indices, such as 0,1,2",
    )
    parser.add_argument(
        "--emit-candidate",
        type=Path,
        help="optional path for the generated rotated rho_E/metric/sector prototype JSON",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.mesh_N < 1:
        raise SystemExit("mesh_N must be positive")
    if args.modulus < 2:
        raise SystemExit("modulus must be at least 2")

    summary, candidate = rotate_candidate(args.mesh_N, args.modulus, args.basis_indices)
    if args.emit_candidate:
        args.emit_candidate.write_text(
            json.dumps(candidate, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
