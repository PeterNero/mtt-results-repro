"""Construct a projective magnetic-translation rho_E carrier prototype.

This is a string/QM-inspired Route C stress test.  It uses the qutrit clock and
shift matrices

    X Z = omega Z X

as finite magnetic translations.  On the Iwasawa N=1 face graph this gives
projective path independence: corner products agree up to a central U(1) phase,
not strictly as ordinary vector-bundle transition functions.

Therefore this candidate is deliberately not selected rho_E data.  It is a
prototype for a possible twisted bundle / gerbe / discrete-torsion route.  The
ordinary rho_E mesh validator should reject it, while the projective diagnostic
below records a nontrivial central twist.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from collections import Counter
from pathlib import Path
from typing import Any


GENERATORS = ("g1", "g2", "g3", "g4", "g5", "g6")
TOL = 1e-8

Node = tuple[int, int, int, int, int, int]
Matrix = list[list[complex]]


def serialize_complex(value: complex) -> int | float | list[float]:
    real = 0.0 if abs(value.real) < 1e-14 else round(value.real, 15)
    imag = 0.0 if abs(value.imag) < 1e-14 else round(value.imag, 15)
    if imag == 0.0:
        if abs(real - round(real)) < 1e-14:
            return int(round(real))
        return real
    return [real, imag]


def serialize_matrix(matrix: Matrix) -> dict[str, list[list[int | float | list[float]]]]:
    return {"matrix": [[serialize_complex(value) for value in row] for row in matrix]}


def identity_matrix() -> Matrix:
    return [
        [1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
        [0.0 + 0.0j, 1.0 + 0.0j, 0.0 + 0.0j],
        [0.0 + 0.0j, 0.0 + 0.0j, 1.0 + 0.0j],
    ]


def zero_matrix() -> Matrix:
    return [[0.0 + 0.0j for _ in range(3)] for _ in range(3)]


def clock_matrix() -> Matrix:
    omega = complex(math.cos(2.0 * math.pi / 3.0), math.sin(2.0 * math.pi / 3.0))
    return [
        [1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
        [0.0 + 0.0j, omega, 0.0 + 0.0j],
        [0.0 + 0.0j, 0.0 + 0.0j, omega**2],
    ]


def shift_matrix() -> Matrix:
    return [
        [0.0 + 0.0j, 1.0 + 0.0j, 0.0 + 0.0j],
        [0.0 + 0.0j, 0.0 + 0.0j, 1.0 + 0.0j],
        [1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
    ]


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


def commutator(left: Matrix, right: Matrix) -> Matrix:
    return [
        [
            matmul(left, right)[i][j] - matmul(right, left)[i][j]
            for j in range(3)
        ]
        for i in range(3)
    ]


def matrix_inverse(matrix: Matrix) -> Matrix:
    size = len(matrix)
    work = [
        matrix[row][:]
        + [1.0 + 0.0j if row == col else 0.0 + 0.0j for col in range(size)]
        for row in range(size)
    ]
    for col in range(size):
        pivot = None
        for row in range(col, size):
            if abs(work[row][col]) > 1e-12:
                pivot = row
                break
        if pivot is None:
            raise ValueError("matrix is singular")
        work[col], work[pivot] = work[pivot], work[col]
        scale = work[col][col]
        work[col] = [value / scale for value in work[col]]
        for row in range(size):
            if row == col:
                continue
            factor = work[row][col]
            if abs(factor) > 1e-12:
                work[row] = [
                    work[row][idx] - factor * work[col][idx]
                    for idx in range(2 * size)
                ]
    return [row[size:] for row in work]


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


def generator_matrices() -> dict[str, Matrix]:
    identity = identity_matrix()
    return {
        "g1": shift_matrix(),
        "g2": clock_matrix(),
        "g3": identity,
        "g4": identity,
        "g5": identity,
        "g6": identity,
    }


def reduction_products(
    node: Node,
    n: int,
    matrices: dict[str, Matrix],
    accumulated: Matrix | None = None,
    path: tuple[str, ...] = (),
) -> list[tuple[Node, Matrix, tuple[str, ...]]]:
    product_matrix = identity_matrix() if accumulated is None else accumulated
    generators = boundary_generators(node, n)
    if not generators:
        return [(node, product_matrix, path)]

    results: list[tuple[Node, Matrix, tuple[str, ...]]] = []
    for generator in generators:
        target = reduce_target(node, generator, n)
        next_product = matmul(product_matrix, matrices[generator])
        results.extend(
            reduction_products(
                target,
                n,
                matrices,
                next_product,
                path + (generator,),
            )
        )
    return results


def scalar_central_error(matrix: Matrix) -> tuple[complex, float]:
    scalar = sum(matrix[i][i] for i in range(3)) / 3.0
    scalar_matrix = [
        [scalar if i == j else 0.0 + 0.0j for j in range(3)]
        for i in range(3)
    ]
    return scalar, max_abs_diff(matrix, scalar_matrix)


def phase_label(value: complex) -> str:
    angle = math.atan2(value.imag, value.real)
    if angle < 0:
        angle += 2.0 * math.pi
    index = round(3.0 * angle / (2.0 * math.pi)) % 3
    return f"omega^{index}"


def projective_diagnostic(mesh_n: int) -> dict[str, Any]:
    matrices = generator_matrices()
    identity = identity_matrix()
    zero = zero_matrix()

    target_mismatch_count = 0
    strict_mismatch_count = 0
    projective_mismatch_count = 0
    nontrivial_central_twist_count = 0
    max_strict_product_error = 0.0
    max_centrality_error = 0.0
    central_phase_histogram: Counter[str] = Counter()

    for node in all_closed_nodes(mesh_n):
        if len(boundary_generators(node, mesh_n)) < 2:
            continue
        products = reduction_products(node, mesh_n, matrices)
        reference_target, reference_product, _ = products[0]
        inverse_reference = matrix_inverse(reference_product)
        for target, product_matrix, _ in products[1:]:
            if target != reference_target:
                target_mismatch_count += 1
                continue
            strict_error = max_abs_diff(product_matrix, reference_product)
            max_strict_product_error = max(max_strict_product_error, strict_error)
            if strict_error > TOL:
                strict_mismatch_count += 1

            ratio = matmul(product_matrix, inverse_reference)
            scalar, centrality_error = scalar_central_error(ratio)
            max_centrality_error = max(max_centrality_error, centrality_error)
            if centrality_error > TOL:
                projective_mismatch_count += 1
            else:
                label = phase_label(scalar)
                central_phase_histogram[label] += 1
                if max_abs_diff(ratio, identity) > TOL:
                    nontrivial_central_twist_count += 1

    x_matrix = matrices["g1"]
    z_matrix = matrices["g2"]
    max_commutator_abs = max_abs_diff(commutator(x_matrix, z_matrix), zero)

    return {
        "mesh_N": mesh_n,
        "closed_nodes": len(all_closed_nodes(mesh_n)),
        "target_mismatch_count": target_mismatch_count,
        "strict_mismatch_count": strict_mismatch_count,
        "projective_mismatch_count": projective_mismatch_count,
        "nontrivial_central_twist_count": nontrivial_central_twist_count,
        "max_strict_product_error": max_strict_product_error,
        "max_centrality_error": max_centrality_error,
        "central_phase_histogram": dict(sorted(central_phase_histogram.items())),
        "max_pairwise_commutator_abs": max_commutator_abs,
        "strict_vector_bundle_gluing_passes": strict_mismatch_count == 0
        and target_mismatch_count == 0,
        "projective_gerbe_gluing_passes": projective_mismatch_count == 0
        and target_mismatch_count == 0,
        "central_twist_is_nontrivial": nontrivial_central_twist_count > 0,
    }


def build_candidate(mesh_n: int) -> dict[str, object]:
    matrices = generator_matrices()
    return {
        "prototype": "IwasawaProjectiveMagneticCarrier",
        "status": "PROTOTYPE_TWISTED_UNSELECTED",
        "rank": 3,
        "mesh_N": mesh_n,
        "carrier": "qutrit clock-shift magnetic translations",
        "twist_interpretation": "projective U(3) transitions; ordinary rho_E gluing fails unless a selected gerbe/B-field twist is supplied",
        "generator_data": {
            generator: serialize_matrix(matrix)
            for generator, matrix in matrices.items()
        },
        "metric_data": serialize_matrix(identity_matrix()),
        "guardrails": {
            "claims_selected_rho_E": False,
            "claims_selected_gerbe_twist": False,
            "claims_selected_D_E": False,
            "claims_physical_family_mixing": False,
            "uses_observed_flavor_data": False,
        },
    }


def construct(mesh_n: int) -> tuple[dict[str, Any], dict[str, object]]:
    diagnostic = projective_diagnostic(mesh_n)
    summary = {
        "calculation": "IwasawaProjectiveMagneticCarrierConstruct",
        "status": "PROJECTIVE_TWIST_PROTOTYPE_UNSELECTED",
        "carrier": "qutrit clock-shift magnetic translations",
        "string_theory_interpretation": "twisted bundle / gerbe / discrete torsion candidate",
        "quantum_mechanics_interpretation": "finite magnetic translations with central phase commutator",
        "diagnostic": diagnostic,
        "verdict": {
            "ordinary_rhoE_source_candidate": False,
            "strict_mesh_validator_should_fail": not diagnostic[
                "strict_vector_bundle_gluing_passes"
            ],
            "projective_gerbe_gluing_holds": diagnostic[
                "projective_gerbe_gluing_passes"
            ],
            "central_twist_nontrivial": diagnostic["central_twist_is_nontrivial"],
            "next_step": "Promote only if MTT supplies selected gerbe/B-field/Bianchi data, or translate the central twist into selected D_E/dotD response data.",
        },
    }
    return summary, build_candidate(mesh_n)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mesh-N", type=int, default=1)
    parser.add_argument(
        "--emit-candidate",
        type=Path,
        help="optional path for the generated projective carrier JSON",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.mesh_N != 1:
        raise SystemExit("this projective prototype is currently certified only at mesh N=1")
    summary, candidate = construct(args.mesh_N)
    if args.emit_candidate:
        args.emit_candidate.write_text(
            json.dumps(candidate, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
