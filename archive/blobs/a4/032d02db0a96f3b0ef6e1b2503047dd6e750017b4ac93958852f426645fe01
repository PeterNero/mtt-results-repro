"""Construct a diagonal rank-three finite-mesh rho_E phase prototype.

This lifts three independent scalar finite-mesh cocycles into the diagonal
entries of a rank-three transition table:

    rho_E(g,target)=diag(omega**phi_1, omega**phi_2, omega**phi_3).

It is still a prototype, not selected data.  Its purpose is to test that the
table-valued Route C branch can carry distinguishable rank-three fiber
components while remaining compatible with the existing mesh and metric gates.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from solve_iwasawa_scalar_phase_mesh import (
    GENERATORS,
    build_linear_system,
    identity_metric,
    node_key,
    nullspace_basis,
    phase_entry,
    residual_count,
)


def parse_indices(value: str) -> list[int]:
    indices = [int(part.strip()) for part in value.split(",") if part.strip()]
    if len(indices) != 3:
        raise argparse.ArgumentTypeError("expected exactly three comma-separated indices")
    return indices


def diagonal_matrix(exponents: list[int], modulus: int) -> dict[str, list[list[object]]]:
    phases = [phase_entry(exponent, modulus) for exponent in exponents]
    return {
        "matrix": [
            [phases[0], 0, 0],
            [0, phases[1], 0],
            [0, 0, phases[2]],
        ]
    }


def construct(mesh_n: int, modulus: int, basis_indices: list[int]) -> tuple[dict[str, object], dict[str, object]]:
    unknown_order, rows, target_mismatches = build_linear_system(mesh_n, modulus)
    basis, pivots = nullspace_basis(rows, modulus, len(unknown_order))
    if len(basis) < 3:
        raise ValueError("need at least three scalar cocycle basis vectors")

    selected_indices = [index % len(basis) for index in basis_indices]
    vectors = [basis[index] for index in selected_indices]

    generator_data: dict[str, dict[str, dict[str, object]]] = {
        generator: {"values": {}} for generator in GENERATORS
    }
    diagonal_tuples: list[tuple[int, int, int]] = []
    for face_index, (generator, target) in enumerate(unknown_order):
        exponents = [vector[face_index] % modulus for vector in vectors]
        diagonal_tuples.append(tuple(exponents))  # type: ignore[arg-type]
        generator_data[generator]["values"][node_key(target)] = diagonal_matrix(
            exponents,
            modulus,
        )

    nonzero_face_values = [
        index for index, exponents in enumerate(diagonal_tuples) if any(exponents)
    ]
    nonscalar_face_values = [
        index for index, exponents in enumerate(diagonal_tuples) if len(set(exponents)) > 1
    ]
    nonzero_by_generator = {
        generator: sum(
            1
            for index in nonzero_face_values
            if unknown_order[index][0] == generator
        )
        for generator in GENERATORS
    }
    nonscalar_by_generator = {
        generator: sum(
            1
            for index in nonscalar_face_values
            if unknown_order[index][0] == generator
        )
        for generator in GENERATORS
    }

    component_residuals = [
        residual_count(rows, vector, modulus) for vector in vectors
    ]
    component_nonzero_entries = [
        sum(1 for value in vector if value % modulus) for vector in vectors
    ]
    tuple_histogram = Counter(
        ",".join(str(value) for value in exponents)
        for exponents in diagonal_tuples
    )

    summary: dict[str, object] = {
        "calculation": "IwasawaDiagonalPhaseMeshRhoEPrototypeConstruct",
        "mesh_N": mesh_n,
        "field": f"F{modulus}",
        "rank": 3,
        "unknown_face_values": len(unknown_order),
        "corner_equations": len(rows),
        "linear_rank": len(pivots),
        "scalar_nullity": len(unknown_order) - len(pivots),
        "target_mismatches": target_mismatches,
        "basis_indices": selected_indices,
        "component_nonzero_entries": component_nonzero_entries,
        "component_row_residuals": component_residuals,
        "diagonal_nonzero_face_values": len(nonzero_face_values),
        "diagonal_nonscalar_face_values": len(nonscalar_face_values),
        "nonzero_by_generator": nonzero_by_generator,
        "nonscalar_by_generator": nonscalar_by_generator,
        "diagonal_tuple_histogram": dict(sorted(tuple_histogram.items())),
        "verdict": {
            "diagonal_rank_three_mesh_cocycle_exists": len(nonscalar_face_values) > 0,
            "components_solve_linear_cocycle_equations": all(
                residual == 0 for residual in component_residuals
            ),
            "candidate_is_selected_rho_E": False,
            "candidate_has_off_diagonal_family_mixing": False,
            "candidate_distinguishes_fiber_components": len(nonscalar_face_values) > 0,
            "next_step": "Use diagonal data only as a non-scalar table-valued prototype; selected closure needs typed Cech/monad or HYM/Strominger source data and off-diagonal sector response.",
        },
    }

    candidate: dict[str, object] = {
        "prototype": "IwasawaDiagonalPhaseMeshRhoE",
        "status": "PROTOTYPE_UNSELECTED",
        "rank": 3,
        "mesh_N": mesh_n,
        "field": f"F{modulus}",
        "basis_indices": selected_indices,
        "generator_data": generator_data,
        "metric_data": identity_metric(),
        "guardrails": {
            "claims_selected_rho_E": False,
            "claims_selected_D_E": False,
            "claims_off_diagonal_family_mixing": False,
            "uses_observed_flavor_data": False,
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
        help="optional path for the generated diagonal rho_E/metric prototype JSON",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.mesh_N < 1:
        raise SystemExit("mesh_N must be positive")
    if args.modulus < 2:
        raise SystemExit("modulus must be at least 2")

    summary, candidate = construct(args.mesh_N, args.modulus, args.basis_indices)
    if args.emit_candidate:
        args.emit_candidate.write_text(
            json.dumps(candidate, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
