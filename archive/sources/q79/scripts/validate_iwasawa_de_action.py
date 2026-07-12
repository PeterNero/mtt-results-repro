"""Validate finite sector-specific D_E action data for Iwasawa Galerkin slots.

This validator checks the first finite operator contract needed after rho_E,
metric, and sector projectors are supplied.  It does not construct the selected
operator; it accepts or rejects a proposed finite matrix realization.

Exit codes:
  0: complete D_E action candidate passes implemented checks
  1: complete candidate fails a mathematical/schema check
  2: candidate is incomplete/open rather than mathematically failed
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


FAMILY_SECTORS = ("Q", "u", "d", "L", "e", "N")
SECTORS = FAMILY_SECTORS + ("H",)
EXPECTED_KERNEL_DIMENSION = {sector: 3 for sector in FAMILY_SECTORS} | {"H": 1}
EXPECTED_KIND = {sector: "family" for sector in FAMILY_SECTORS} | {
    "H": "single_higgs_carrier"
}
TOL = 1e-9

Matrix = list[list[complex]]
Vector = list[complex]


class IncompleteData(ValueError):
    """Raised when a required operator slot value is still open."""


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


def parse_matrix(entry: Any, *, rows: int | None = None, cols: int | None = None) -> Matrix:
    matrix_data = entry.get("matrix") if isinstance(entry, dict) else entry
    if not isinstance(matrix_data, list) or not matrix_data:
        raise ValueError("matrix must be a nonempty row list")
    matrix: Matrix = []
    width: int | None = None
    for row in matrix_data:
        if not isinstance(row, list) or not row:
            raise ValueError("matrix rows must be nonempty lists")
        if width is None:
            width = len(row)
        elif len(row) != width:
            raise ValueError("matrix rows must have equal length")
        matrix.append([parse_complex(value) for value in row])
    if rows is not None and len(matrix) != rows:
        raise ValueError(f"matrix has {len(matrix)} rows, expected {rows}")
    if cols is not None and len(matrix[0]) != cols:
        raise ValueError(f"matrix has {len(matrix[0])} columns, expected {cols}")
    return matrix


def parse_vector(entry: Any, *, size: int) -> Vector:
    if not isinstance(entry, list) or len(entry) != size:
        raise ValueError(f"vector must have length {size}")
    return [parse_complex(value) for value in entry]


def adjoint(matrix: Matrix) -> Matrix:
    return [[matrix[j][i].conjugate() for j in range(len(matrix))] for i in range(len(matrix[0]))]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    if not left or not right or len(left[0]) != len(right):
        raise ValueError("incompatible matrix dimensions")
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(len(right)))
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def matvec(matrix: Matrix, vector: Vector) -> Vector:
    if not matrix or len(matrix[0]) != len(vector):
        raise ValueError("incompatible matrix/vector dimensions")
    return [sum(row[idx] * vector[idx] for idx in range(len(vector))) for row in matrix]


def inner(gram: Matrix, left: Vector, right: Vector) -> complex:
    gright = matvec(gram, right)
    return sum(left[idx].conjugate() * gright[idx] for idx in range(len(left)))


def max_abs_diff(left: Matrix, right: Matrix) -> float:
    if len(left) != len(right) or len(left[0]) != len(right[0]):
        raise ValueError("matrix dimensions differ")
    return max(
        abs(left[i][j] - right[i][j])
        for i in range(len(left))
        for j in range(len(left[0]))
    )


def max_abs_vector(vector: Vector) -> float:
    return max((abs(value) for value in vector), default=0.0)


def is_hermitian(matrix: Matrix) -> bool:
    return len(matrix) == len(matrix[0]) and max_abs_diff(matrix, adjoint(matrix)) <= TOL


def is_positive_definite_hermitian(matrix: Matrix) -> bool:
    if not is_hermitian(matrix):
        return False
    size = len(matrix)
    lower = [[0.0 + 0.0j for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(i + 1):
            value = matrix[i][j] - sum(
                lower[i][k] * lower[j][k].conjugate() for k in range(j)
            )
            if i == j:
                if abs(value.imag) > TOL or value.real <= TOL:
                    return False
                lower[i][j] = value.real ** 0.5
            else:
                if abs(lower[j][j]) <= TOL:
                    return False
                lower[i][j] = value / lower[j][j]
    return True


def rank(matrix: Matrix) -> int:
    work = [row[:] for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    pivot_row = 0
    for col in range(cols):
        pivot = None
        for row in range(pivot_row, rows):
            if abs(work[row][col]) > TOL:
                pivot = row
                break
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][col]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row or abs(work[row][col]) <= TOL:
                continue
            factor = work[row][col]
            work[row] = [
                work[row][idx] - factor * work[pivot_row][idx]
                for idx in range(cols)
            ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def require_int(value: Any, label: str) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value < 1:
        raise IncompleteData(f"MISSING {label} positive integer")
    return value


def load_candidate(path: Path) -> tuple[int, str, dict[str, Any] | None]:
    data = json.loads(path.read_text(encoding="utf-8"))
    slots = data.get("operator_slots")
    if not isinstance(slots, dict):
        return 2, "MISSING operator_slots object", None
    missing = [sector for sector in SECTORS if slots.get(sector) is None]
    if missing:
        return 2, f"MISSING operator slot entries: {', '.join(missing)}", None
    return 0, "loaded sector-specific finite D_E operator slots", slots


def validate_slot(sector: str, slot: dict[str, Any]) -> list[str]:
    failures: list[str] = []

    if slot.get("kind") != EXPECTED_KIND[sector]:
        failures.append(
            f"{sector} kind {slot.get('kind')!r} != {EXPECTED_KIND[sector]!r}"
        )
    if slot.get("expected_kernel_dimension") != EXPECTED_KERNEL_DIMENSION[sector]:
        failures.append(
            f"{sector} expected_kernel_dimension {slot.get('expected_kernel_dimension')!r} "
            f"!= {EXPECTED_KERNEL_DIMENSION[sector]}"
        )

    domain_dim = require_int(slot.get("domain_dimension"), f"{sector}.domain_dimension")
    range_dim = require_int(slot.get("range_dimension"), f"{sector}.range_dimension")
    domain_gram = parse_matrix(slot.get("domain_gram"), rows=domain_dim, cols=domain_dim)
    range_gram = parse_matrix(slot.get("range_gram"), rows=range_dim, cols=range_dim)
    operator = parse_matrix(slot.get("D_E_matrix"), rows=range_dim, cols=domain_dim)
    stiffness = parse_matrix(slot.get("stiffness_matrix"), rows=domain_dim, cols=domain_dim)

    if not is_positive_definite_hermitian(domain_gram):
        failures.append(f"{sector} domain_gram is not positive-definite Hermitian")
    if not is_positive_definite_hermitian(range_gram):
        failures.append(f"{sector} range_gram is not positive-definite Hermitian")

    computed_stiffness = matmul(matmul(adjoint(operator), range_gram), operator)
    diff = max_abs_diff(computed_stiffness, stiffness)
    if diff > TOL:
        failures.append(f"{sector} stiffness mismatch max_abs_diff={diff:.3e}")
    if not is_hermitian(stiffness):
        failures.append(f"{sector} stiffness_matrix is not Hermitian")

    kernel_dim = domain_dim - rank(operator)
    expected_kernel = EXPECTED_KERNEL_DIMENSION[sector]
    if kernel_dim != expected_kernel:
        failures.append(f"{sector} kernel dimension {kernel_dim} != {expected_kernel}")

    basis_data = slot.get("ordered_zero_mode_basis")
    if not isinstance(basis_data, list):
        raise IncompleteData(f"MISSING {sector}.ordered_zero_mode_basis")
    if len(basis_data) != expected_kernel:
        failures.append(
            f"{sector} zero-mode basis length {len(basis_data)} != {expected_kernel}"
        )
    basis = [parse_vector(vector, size=domain_dim) for vector in basis_data]

    for idx, vector in enumerate(basis):
        residual = max_abs_vector(matvec(operator, vector))
        if residual > TOL:
            failures.append(f"{sector} zero-mode {idx} residual={residual:.3e}")

    for i, left in enumerate(basis):
        for j, right in enumerate(basis):
            expected = 1.0 if i == j else 0.0
            value = inner(domain_gram, left, right)
            if abs(value - expected) > TOL:
                failures.append(
                    f"{sector} zero-mode Gram[{i},{j}]={value} != {expected}"
                )

    if slot.get("selected_source_verified") is not True:
        failures.append(f"{sector} selected_source_verified is not true")
    if slot.get("boundary_conditions_verified") is not True:
        failures.append(f"{sector} boundary_conditions_verified is not true")

    return failures


def validate_slots(slots: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    for sector in SECTORS:
        entry = slots.get(sector)
        if not isinstance(entry, dict):
            raise IncompleteData(f"MISSING {sector} operator slot object")
        failures.extend(validate_slot(sector, entry))
    return failures


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_iwasawa_de_action.py <de-action-data.json>")
        return 1

    path = Path(argv[1])
    try:
        code, message, slots = load_candidate(path)
        print(message)
        if code != 0:
            return code
        assert slots is not None
        failures = validate_slots(slots)
    except IncompleteData as exc:
        print(str(exc))
        return 2
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"INVALID D_E action data: {exc}")
        return 1

    if failures:
        print("D_E action validation FAIL")
        for failure in failures[:50]:
            print(f"- {failure}")
        if len(failures) > 50:
            print(f"- ... {len(failures) - 50} more failures")
        return 1

    print("D_E action validation PASS")
    print("finite sector operators, Gram matrices, stiffness matrices, and zero-mode bases are consistent")
    print("selected origin, dotD_alpha1, Green operators, and overlap matrices remain separate checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
