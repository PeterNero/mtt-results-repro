"""Validate candidate constant rho_E transition matrices for Iwasawa gluing.

Exit codes:
  0: complete candidate passes the implemented algebraic checks
  1: complete candidate fails a check
  2: candidate is incomplete/open rather than mathematically failed
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


GENERATORS = ("g1", "g2", "g3", "g4", "g5", "g6")
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


def det3(matrix: Matrix) -> complex:
    a = matrix
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def max_abs_diff(left: Matrix, right: Matrix) -> float:
    return max(abs(left[i][j] - right[i][j]) for i in range(3) for j in range(3))


def product(*matrices: Matrix) -> Matrix:
    if not matrices:
        raise ValueError("empty product")
    result = matrices[0]
    for matrix in matrices[1:]:
        result = matmul(result, matrix)
    return result


def load_candidate(path: Path) -> tuple[int, str, dict[str, Matrix] | None]:
    data = json.loads(path.read_text(encoding="utf-8"))
    generator_data = data.get("generator_data")
    if not isinstance(generator_data, dict):
        return 2, "MISSING generator_data object", None

    missing = [name for name in GENERATORS if generator_data.get(name) is None]
    if missing:
        return 2, f"MISSING generator entries: {', '.join(missing)}", None

    matrices: dict[str, Matrix] = {}
    try:
        for name in GENERATORS:
            matrices[name] = parse_matrix(generator_data[name])
    except ValueError as exc:
        return 1, f"INVALID matrix data: {exc}", None

    return 0, "loaded complete generator matrices", matrices


def validate_constant_matrices(matrices: dict[str, Matrix]) -> list[str]:
    failures: list[str] = []

    for name in GENERATORS:
        determinant = det3(matrices[name])
        if abs(determinant) <= TOL:
            failures.append(f"{name} determinant too small: {determinant}")

    r1 = matrices["g1"]
    r2 = matrices["g2"]
    r3 = matrices["g3"]
    r4 = matrices["g4"]
    r5 = matrices["g5"]
    r6 = matrices["g6"]

    relations: list[tuple[str, Matrix, Matrix]] = [
        ("g1 g2 = g2 g1", product(r1, r2), product(r2, r1)),
        ("g3 g4 = g4 g3", product(r3, r4), product(r4, r3)),
        ("g1 g3 = g5 g3 g1", product(r1, r3), product(r5, r3, r1)),
        ("g1 g4 = g6 g4 g1", product(r1, r4), product(r6, r4, r1)),
        ("g2 g3 = g6 g3 g2", product(r2, r3), product(r6, r3, r2)),
        ("g5 g2 g4 = g4 g2", product(r5, r2, r4), product(r4, r2)),
    ]

    for central_name, central_matrix in (("g5", r5), ("g6", r6)):
        for name in GENERATORS:
            relations.append(
                (
                    f"{central_name} {name} = {name} {central_name}",
                    product(central_matrix, matrices[name]),
                    product(matrices[name], central_matrix),
                )
            )

    for label, left, right in relations:
        diff = max_abs_diff(left, right)
        if diff > TOL:
            failures.append(f"{label} failed with max_abs_diff={diff:.3e}")

    return failures


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_iwasawa_rhoE.py <rhoE-data.json>")
        return 1

    path = Path(argv[1])
    code, message, matrices = load_candidate(path)
    print(message)
    if code != 0:
        return code

    assert matrices is not None
    failures = validate_constant_matrices(matrices)
    if failures:
        print("rho_E validation FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("rho_E validation PASS")
    print("constant generator matrices are invertible and satisfy implemented Iwasawa relations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
