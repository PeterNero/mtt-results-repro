"""Validate projective finite-mesh rho_E transition data.

This is the twisted analogue of validate_iwasawa_rhoE_mesh.py.  It checks the
same Iwasawa closed-cell corner reductions, but accepts corner products that
agree up to a scalar central factor:

    product(path_2) product(path_1)^(-1) = lambda I.

This is appropriate for projective bundles, magnetic translations, gerbe/B-field
twists, or discrete torsion candidates.  It does not prove the twist is selected
by MTT; it only validates the finite projective gluing law.

Exit codes:
  0: candidate passes projective mesh checks
  1: complete candidate fails a mathematical/schema check
  2: candidate is incomplete/open rather than mathematically failed
"""

from __future__ import annotations

import json
import math
import sys
from collections import Counter
from pathlib import Path
from typing import Any

from validate_iwasawa_rhoE_mesh import (
    GENERATORS,
    IncompleteData,
    Matrix,
    MatrixResolver,
    Node,
    all_closed_nodes,
    boundary_generators,
    det3,
    identity_matrix,
    max_abs_diff,
    parse_matrix,
    reduce_target,
    validate_mesh_n,
)


TOL = 1e-8


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(3))
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


def reduction_products(
    node: Node,
    n: int,
    resolver: MatrixResolver,
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
        next_product = matmul(product_matrix, resolver.matrix(generator, target))
        results.extend(
            reduction_products(
                target,
                n,
                resolver,
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


def phase_label(value: complex, max_order: int = 24) -> str:
    if abs(value) <= TOL:
        return "zero"
    unit = value / abs(value)
    angle = math.atan2(unit.imag, unit.real)
    if angle < 0:
        angle += 2.0 * math.pi
    best_order = 1
    best_index = 0
    best_error = float("inf")
    for order in range(1, max_order + 1):
        index = round(order * angle / (2.0 * math.pi)) % order
        root = complex(
            math.cos(2.0 * math.pi * index / order),
            math.sin(2.0 * math.pi * index / order),
        )
        error = abs(unit - root)
        if error < best_error:
            best_error = error
            best_order = order
            best_index = index
    if best_error <= 1e-6:
        return f"zeta_{best_order}^{best_index}"
    return f"angle={angle:.12f}"


def load_candidate(path: Path) -> tuple[int, str, int | None, MatrixResolver | None]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("rank") != 3:
        return 2, "MISSING rank=3 bundle declaration", None, None
    generator_data = data.get("generator_data")
    if not isinstance(generator_data, dict):
        return 2, "MISSING generator_data object", None, None
    missing = [name for name in GENERATORS if generator_data.get(name) is None]
    if missing:
        return 2, f"MISSING generator entries: {', '.join(missing)}", None, None
    try:
        n = validate_mesh_n(data.get("mesh_N"))
    except IncompleteData as exc:
        return 2, str(exc), None, None
    return 0, f"loaded finite mesh_N={n} projective transition data", n, MatrixResolver(generator_data)


def validate_seen_invertible(resolver: MatrixResolver) -> list[str]:
    failures: list[str] = []
    for (generator, target), matrix in sorted(
        resolver.seen.items(), key=lambda item: (item[0][0], item[0][1])
    ):
        determinant = det3(matrix)
        if abs(determinant) <= TOL:
            failures.append(f"{generator} at {target} determinant too small: {determinant}")
    return failures


def projective_corner_report(n: int, resolver: MatrixResolver) -> tuple[list[str], dict[str, Any]]:
    failures: list[str] = []
    target_mismatch_count = 0
    strict_mismatch_count = 0
    projective_mismatch_count = 0
    nontrivial_central_twist_count = 0
    max_strict_product_error = 0.0
    max_centrality_error = 0.0
    max_scalar_modulus_error = 0.0
    phase_histogram: Counter[str] = Counter()
    identity = identity_matrix()

    for node in all_closed_nodes(n):
        if len(boundary_generators(node, n)) < 2:
            continue
        products = reduction_products(node, n, resolver)
        reference_target, reference_product, reference_path = products[0]
        inverse_reference = matrix_inverse(reference_product)
        for target, product_matrix, path in products[1:]:
            if target != reference_target:
                target_mismatch_count += 1
                failures.append(
                    f"corner target mismatch at {node} path {path} -> {target}, "
                    f"reference {reference_path} -> {reference_target}"
                )
                continue

            strict_error = max_abs_diff(product_matrix, reference_product)
            max_strict_product_error = max(max_strict_product_error, strict_error)
            if strict_error > TOL:
                strict_mismatch_count += 1

            ratio = matmul(product_matrix, inverse_reference)
            scalar, centrality_error = scalar_central_error(ratio)
            max_centrality_error = max(max_centrality_error, centrality_error)
            max_scalar_modulus_error = max(max_scalar_modulus_error, abs(abs(scalar) - 1.0))
            if centrality_error > TOL or abs(abs(scalar) - 1.0) > TOL:
                projective_mismatch_count += 1
                failures.append(
                    f"noncentral projective mismatch at {node} path {path} vs "
                    f"{reference_path}: centrality_error={centrality_error:.3e}, "
                    f"|lambda|-1={abs(abs(scalar) - 1.0):.3e}"
                )
            else:
                phase_histogram[phase_label(scalar)] += 1
                if max_abs_diff(ratio, identity) > TOL:
                    nontrivial_central_twist_count += 1

    report = {
        "target_mismatch_count": target_mismatch_count,
        "strict_mismatch_count": strict_mismatch_count,
        "projective_mismatch_count": projective_mismatch_count,
        "nontrivial_central_twist_count": nontrivial_central_twist_count,
        "max_strict_product_error": max_strict_product_error,
        "max_centrality_error": max_centrality_error,
        "max_scalar_modulus_error": max_scalar_modulus_error,
        "central_phase_histogram": dict(sorted(phase_histogram.items())),
        "strict_vector_bundle_gluing_passes": strict_mismatch_count == 0
        and target_mismatch_count == 0,
        "projective_gerbe_gluing_passes": projective_mismatch_count == 0
        and target_mismatch_count == 0,
        "central_twist_is_nontrivial": nontrivial_central_twist_count > 0,
    }
    return failures, report


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_iwasawa_projective_rhoE_mesh.py <rhoE-projective-data.json>")
        return 1

    path = Path(argv[1])
    try:
        code, message, n, resolver = load_candidate(path)
        print(message)
        if code != 0:
            return code
        assert n is not None
        assert resolver is not None
        failures, report = projective_corner_report(n, resolver)
        failures.extend(validate_seen_invertible(resolver))
    except IncompleteData as exc:
        print(str(exc))
        return 2
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"INVALID projective finite-mesh rho_E data: {exc}")
        return 1

    print(f"projective_report={json.dumps(report, sort_keys=True)}")
    if failures:
        print("projective finite-mesh rho_E validation FAIL")
        for failure in failures[:50]:
            print(f"- {failure}")
        if len(failures) > 50:
            print(f"- ... {len(failures) - 50} more failures")
        return 1

    print("projective finite-mesh rho_E validation PASS")
    print("corner products agree up to scalar central phases")
    print("selected gerbe/B-field origin, twisted Bianchi compatibility, and D_E remain separate checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
