"""Solve scalar phase finite-mesh rho_E cocycle equations.

This is a deliberately small Route C prototype.  It linearizes the finite
corner path-independence equations for table-valued scalar phases:

    rho_E(g,target) = omega**phi(g,target) I_3,
    phi(g,target) in F_p.

The result is not selected MTT bundle data.  It is a no-proxy finite cocycle
prototype that exercises the table-valued rho_E and metric validators after the
constant scalar-central Wilson ansatz has been retired.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from collections import Counter
from pathlib import Path
from typing import Iterable


GENERATORS = ("g1", "g2", "g3", "g4", "g5", "g6")

Node = tuple[int, int, int, int, int, int]
FaceKey = tuple[str, Node]


def node_key(node: Node) -> str:
    return ",".join(str(value) for value in node)


def boundary_generators(node: Node, n: int) -> list[str]:
    return [GENERATORS[index] for index, value in enumerate(node) if value == n]


def reduce_target(node: Node, generator: str, n: int) -> Node:
    x1, x2, y1, y2, t1, t2 = node
    if generator == "g1" and x1 == n:
        return (0, x2, y1, y2, (t1 - y1) % n, (t2 - y2) % n)
    if generator == "g2" and x2 == n:
        return (x1, 0, y1, y2, (t1 + y2) % n, (t2 - y1) % n)
    if generator == "g3" and y1 == n:
        return (x1, x2, 0, y2, t1, t2)
    if generator == "g4" and y2 == n:
        return (x1, x2, y1, 0, t1, t2)
    if generator == "g5" and t1 == n:
        return (x1, x2, y1, y2, 0, t2)
    if generator == "g6" and t2 == n:
        return (x1, x2, y1, y2, t1, 0)
    raise ValueError(f"generator {generator} does not reduce node {node}")


def all_closed_nodes(n: int) -> list[Node]:
    return list(itertools.product(range(n + 1), repeat=6))  # type: ignore[return-value]


def reduction_paths(
    node: Node,
    n: int,
    path: tuple[FaceKey, ...] = (),
) -> list[tuple[Node, tuple[FaceKey, ...]]]:
    generators = boundary_generators(node, n)
    if not generators:
        return [(node, path)]

    results: list[tuple[Node, tuple[FaceKey, ...]]] = []
    for generator in generators:
        target = reduce_target(node, generator, n)
        results.extend(reduction_paths(target, n, path + ((generator, target),)))
    return results


def collect_unknowns(n: int) -> list[FaceKey]:
    unknowns: dict[FaceKey, int] = {}
    order: list[FaceKey] = []
    for node in all_closed_nodes(n):
        if len(boundary_generators(node, n)) < 2:
            continue
        for _, path in reduction_paths(node, n):
            for key in path:
                if key not in unknowns:
                    unknowns[key] = len(order)
                    order.append(key)
    return order


def build_linear_system(n: int, modulus: int) -> tuple[list[FaceKey], list[list[int]], int]:
    unknown_order = collect_unknowns(n)
    unknown_index = {key: index for index, key in enumerate(unknown_order)}
    rows: list[list[int]] = []
    target_mismatches = 0

    for node in all_closed_nodes(n):
        if len(boundary_generators(node, n)) < 2:
            continue

        paths = reduction_paths(node, n)
        reference_target, reference_path = paths[0]
        for target, path in paths[1:]:
            if target != reference_target:
                target_mismatches += 1

            row = [0] * len(unknown_order)
            for key in path:
                row[unknown_index[key]] = (row[unknown_index[key]] + 1) % modulus
            for key in reference_path:
                row[unknown_index[key]] = (row[unknown_index[key]] - 1) % modulus
            rows.append(row)

    return unknown_order, rows, target_mismatches


def rref_mod(rows: list[list[int]], modulus: int, ncols: int) -> tuple[list[list[int]], list[int]]:
    matrix = [row[:] for row in rows if any(value % modulus for value in row)]
    rank = 0
    pivots: list[int] = []

    for col in range(ncols):
        pivot_row = None
        for row_index in range(rank, len(matrix)):
            if matrix[row_index][col] % modulus:
                pivot_row = row_index
                break
        if pivot_row is None:
            continue

        matrix[rank], matrix[pivot_row] = matrix[pivot_row], matrix[rank]
        inverse = pow(matrix[rank][col] % modulus, -1, modulus)
        matrix[rank] = [(value * inverse) % modulus for value in matrix[rank]]

        for row_index in range(len(matrix)):
            if row_index == rank:
                continue
            factor = matrix[row_index][col] % modulus
            if factor:
                matrix[row_index] = [
                    (matrix[row_index][j] - factor * matrix[rank][j]) % modulus
                    for j in range(ncols)
                ]

        pivots.append(col)
        rank += 1

    return matrix, pivots


def nullspace_basis(rows: list[list[int]], modulus: int, ncols: int) -> tuple[list[list[int]], list[int]]:
    rref, pivots = rref_mod(rows, modulus, ncols)
    pivot_set = set(pivots)
    free_columns = [col for col in range(ncols) if col not in pivot_set]
    basis: list[list[int]] = []

    for free_col in free_columns:
        vector = [0] * ncols
        vector[free_col] = 1
        for row_index, pivot_col in enumerate(pivots):
            vector[pivot_col] = (-rref[row_index][free_col]) % modulus
        basis.append(vector)

    return basis, pivots


def residual_count(rows: Iterable[list[int]], vector: list[int], modulus: int) -> int:
    return sum(
        1
        for row in rows
        if sum(coeff * value for coeff, value in zip(row, vector)) % modulus != 0
    )


def phase_entry(exponent: int, modulus: int) -> int | list[float]:
    angle = 2.0 * math.pi * (exponent % modulus) / modulus
    real = math.cos(angle)
    imag = math.sin(angle)
    if abs(imag) < 1e-15:
        return round(real, 15)
    return [round(real, 15), round(imag, 15)]


def scalar_matrix(exponent: int, modulus: int) -> dict[str, list[list[object]]]:
    phase = phase_entry(exponent, modulus)
    return {
        "matrix": [
            [phase, 0, 0],
            [0, phase, 0],
            [0, 0, phase],
        ]
    }


def identity_metric() -> dict[str, list[list[int]]]:
    return {"matrix": [[1, 0, 0], [0, 1, 0], [0, 0, 1]]}


def candidate_data(
    mesh_n: int,
    modulus: int,
    unknown_order: list[FaceKey],
    vector: list[int],
    basis_index: int,
) -> dict[str, object]:
    generator_data: dict[str, dict[str, dict[str, object]]] = {
        generator: {"values": {}} for generator in GENERATORS
    }
    for (generator, target), exponent in zip(unknown_order, vector):
        generator_data[generator]["values"][node_key(target)] = scalar_matrix(
            exponent,
            modulus,
        )

    return {
        "prototype": "IwasawaScalarPhaseMeshRhoE",
        "status": "PROTOTYPE_UNSELECTED",
        "rank": 3,
        "mesh_N": mesh_n,
        "field": f"F{modulus}",
        "basis_index": basis_index,
        "generator_data": generator_data,
        "metric_data": identity_metric(),
        "guardrails": {
            "claims_selected_rho_E": False,
            "claims_selected_D_E": False,
            "claims_family_mixing": False,
            "uses_observed_flavor_data": False,
        },
    }


def solve(mesh_n: int, modulus: int, basis_index: int) -> tuple[dict[str, object], dict[str, object]]:
    unknown_order, rows, target_mismatches = build_linear_system(mesh_n, modulus)
    basis, pivots = nullspace_basis(rows, modulus, len(unknown_order))
    nullity = len(unknown_order) - len(pivots)

    if basis:
        selected_index = basis_index % len(basis)
        vector = basis[selected_index]
    else:
        selected_index = -1
        vector = [0] * len(unknown_order)

    nonzero_by_generator = {
        generator: sum(
            1
            for (face_generator, _), value in zip(unknown_order, vector)
            if face_generator == generator and value % modulus
        )
        for generator in GENERATORS
    }
    unknowns_by_generator = Counter(generator for generator, _ in unknown_order)
    phase_histogram = Counter(value % modulus for value in vector)
    row_residuals = residual_count(rows, vector, modulus)

    summary: dict[str, object] = {
        "calculation": "IwasawaScalarPhaseMeshRhoEPrototypeSolve",
        "mesh_N": mesh_n,
        "field": f"F{modulus}",
        "rank": 3,
        "unknown_face_values": len(unknown_order),
        "corner_equations": len(rows),
        "linear_rank": len(pivots),
        "nullity": nullity,
        "target_mismatches": target_mismatches,
        "unknowns_by_generator": dict(sorted(unknowns_by_generator.items())),
        "candidate_basis_index": selected_index,
        "candidate_nonzero_entries": sum(1 for value in vector if value % modulus),
        "candidate_nonzero_by_generator": nonzero_by_generator,
        "candidate_phase_histogram": {
            str(phase): count for phase, count in sorted(phase_histogram.items())
        },
        "candidate_row_residuals": row_residuals,
        "verdict": {
            "nontrivial_scalar_phase_mesh_cocycles_exist": bool(basis)
            and any(value % modulus for value in vector),
            "finite_corner_targets_path_independent": target_mismatches == 0,
            "candidate_solves_linear_cocycle_equations": row_residuals == 0,
            "candidate_is_selected_rho_E": False,
            "candidate_can_mix_families": False,
            "next_step": "Use this only as a finite table-valued cocycle prototype; selected rho_E still requires typed Cech/monad, HYM/Strominger, or non-scalar quotient data.",
        },
    }
    candidate = candidate_data(mesh_n, modulus, unknown_order, vector, selected_index)
    return summary, candidate


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mesh-N", type=int, default=1, help="closed-cell subdivision N")
    parser.add_argument("--modulus", type=int, default=3, help="finite phase field modulus")
    parser.add_argument("--basis-index", type=int, default=0, help="nullspace basis vector index")
    parser.add_argument(
        "--emit-candidate",
        type=Path,
        help="optional path for the generated rho_E/metric prototype JSON",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.mesh_N < 1:
        raise SystemExit("mesh_N must be positive")
    if args.modulus < 2:
        raise SystemExit("modulus must be at least 2")

    summary, candidate = solve(args.mesh_N, args.modulus, args.basis_index)
    if args.emit_candidate:
        args.emit_candidate.write_text(
            json.dumps(candidate, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
