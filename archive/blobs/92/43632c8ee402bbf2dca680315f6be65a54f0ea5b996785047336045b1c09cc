"""Validate finite-mesh rho_E transition data for Iwasawa FE gluing.

This is the coordinate/table analogue of validate_iwasawa_rhoE.py.  It checks
face-transition data on a finite Iwasawa closed cell, after any deck-word or
central-wrap convention has already been absorbed into the supplied face values.

Exit codes:
  0: complete finite-mesh candidate passes the implemented checks
  1: complete finite-mesh candidate fails a mathematical/schema check
  2: candidate is incomplete/open rather than mathematically failed
"""

from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path
from typing import Any


GENERATORS = ("g1", "g2", "g3", "g4", "g5", "g6")
TOL = 1e-9

Node = tuple[int, int, int, int, int, int]
Matrix = list[list[complex]]


class IncompleteData(ValueError):
    """Raised when a candidate leaves a required mesh value open."""


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
    if not isinstance(matrix_data, list) or len(matrix_data) != 3:
        raise ValueError("matrix must have three rows")
    matrix: Matrix = []
    for row in matrix_data:
        if not isinstance(row, list) or len(row) != 3:
            raise ValueError("matrix must be 3x3")
        matrix.append([parse_complex(value) for value in row])
    return matrix


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(3))
            for j in range(3)
        ]
        for i in range(3)
    ]


def identity_matrix() -> Matrix:
    return [
        [1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
        [0.0 + 0.0j, 1.0 + 0.0j, 0.0 + 0.0j],
        [0.0 + 0.0j, 0.0 + 0.0j, 1.0 + 0.0j],
    ]


def det3(matrix: Matrix) -> complex:
    a = matrix
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def max_abs_diff(left: Matrix, right: Matrix) -> float:
    return max(abs(left[i][j] - right[i][j]) for i in range(3) for j in range(3))


def node_key(node: Node) -> str:
    return ",".join(str(value) for value in node)


def parse_node_key(key: str) -> Node:
    parts = key.split(",")
    if len(parts) != 6:
        raise ValueError(f"node key must have six comma-separated integers: {key!r}")
    try:
        node = tuple(int(part) for part in parts)
    except ValueError as exc:
        raise ValueError(f"node key contains a non-integer coordinate: {key!r}") from exc
    return node  # type: ignore[return-value]


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


def validate_mesh_n(value: Any) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value < 1:
        raise IncompleteData("MISSING mesh_N positive integer")
    return value


class MatrixResolver:
    def __init__(self, generator_data: dict[str, Any]) -> None:
        self.generator_data = generator_data
        self.seen: dict[tuple[str, Node], Matrix] = {}

    def matrix(self, generator: str, target: Node) -> Matrix:
        key = (generator, target)
        if key in self.seen:
            return self.seen[key]

        entry = self.generator_data.get(generator)
        if entry is None:
            raise IncompleteData(f"MISSING generator entry: {generator}")

        selected: Any | None = None
        if isinstance(entry, dict):
            values = entry.get("values")
            target_key = node_key(target)
            if isinstance(values, dict) and target_key in values:
                selected = values[target_key]
            elif "matrix" in entry:
                selected = entry
            else:
                raise IncompleteData(
                    f"MISSING {generator} matrix at boundary target {target_key}"
                )
        else:
            selected = entry

        matrix = parse_matrix(selected)
        self.seen[key] = matrix
        return matrix


def path_product(
    node: Node,
    path: tuple[str, ...],
    n: int,
    resolver: MatrixResolver,
) -> tuple[Node, Matrix]:
    current = node
    product_matrix = identity_matrix()
    for generator in path:
        target = reduce_target(current, generator, n)
        product_matrix = matmul(product_matrix, resolver.matrix(generator, target))
        current = target
    return current, product_matrix


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


def validate_mesh_path_independence(
    n: int,
    resolver: MatrixResolver,
) -> list[str]:
    failures: list[str] = []
    for node in all_closed_nodes(n):
        if len(boundary_generators(node, n)) < 2:
            continue

        reference_target: Node | None = None
        reference_product: Matrix | None = None
        reference_path: tuple[str, ...] | None = None

        for target, product_matrix, path in reduction_products(node, n, resolver):
            if reference_target is None:
                reference_target = target
                reference_product = product_matrix
                reference_path = path
                continue

            if target != reference_target:
                failures.append(
                    "corner target mismatch at "
                    f"{node_key(node)} path {path} -> {node_key(target)}, "
                    f"reference {reference_path} -> {node_key(reference_target)}"
                )
                continue

            assert reference_product is not None
            diff = max_abs_diff(product_matrix, reference_product)
            if diff > TOL:
                failures.append(
                    "corner product mismatch at "
                    f"{node_key(node)} path {path} vs {reference_path} "
                    f"max_abs_diff={diff:.3e}"
                )

    return failures


def validate_seen_invertible(resolver: MatrixResolver) -> list[str]:
    failures: list[str] = []
    for (generator, target), matrix in sorted(
        resolver.seen.items(), key=lambda item: (item[0][0], item[0][1])
    ):
        determinant = det3(matrix)
        if abs(determinant) <= TOL:
            failures.append(
                f"{generator} at {node_key(target)} determinant too small: {determinant}"
            )
    return failures


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

    return 0, f"loaded finite mesh_N={n} transition data", n, MatrixResolver(generator_data)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_iwasawa_rhoE_mesh.py <rhoE-mesh-data.json>")
        return 1

    path = Path(argv[1])
    try:
        code, message, n, resolver = load_candidate(path)
        print(message)
        if code != 0:
            return code

        assert n is not None
        assert resolver is not None
        failures = validate_mesh_path_independence(n, resolver)
        failures.extend(validate_seen_invertible(resolver))
    except IncompleteData as exc:
        print(str(exc))
        return 2
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"INVALID finite-mesh rho_E data: {exc}")
        return 1

    if failures:
        print("finite-mesh rho_E validation FAIL")
        for failure in failures[:50]:
            print(f"- {failure}")
        if len(failures) > 50:
            print(f"- ... {len(failures) - 50} more failures")
        return 1

    print("finite-mesh rho_E validation PASS")
    print("boundary face products are invertible and corner path-independent")
    print("metric compatibility, sector maps, and selected D_E remain separate checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
