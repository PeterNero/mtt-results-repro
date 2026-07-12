"""Validate finite dotD_alpha1 and horizontal response data for Iwasawa slots.

This validator checks the finite zero-mode response contract

    dotPsi_i = - R Q dotD Psi_i

after sector projectors and reduced Green operators are supplied. It accepts or
rejects proposed response data; it does not construct the selected dotD source
or prove that a toy matrix is the MTT-selected one.

Exit codes:
  0: complete dotD/response candidate passes implemented checks
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
EXPECTED_CLUSTER_DIMENSION = {sector: 3 for sector in FAMILY_SECTORS} | {"H": 1}
EXPECTED_KIND = {sector: "family" for sector in FAMILY_SECTORS} | {
    "H": "single_higgs_carrier"
}
TOL = 1e-9

Matrix = list[list[complex]]
Vector = list[complex]


class IncompleteData(ValueError):
    """Raised when a required dotD/response slot value is still open."""


def parse_complex(value: Any) -> complex:
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return complex(float(value), 0.0)
    if (
        isinstance(value, list)
        and len(value) == 2
        and all(isinstance(part, (int, float)) and not isinstance(part, bool) for part in value)
    ):
        return complex(float(value[0]), float(value[1]))
    raise ValueError(f"invalid complex entry {value!r}")


def require_int(value: Any, label: str) -> int:
    if value is None:
        raise IncompleteData(f"MISSING {label}")
    if not isinstance(value, int) or isinstance(value, bool) or value < 1:
        raise ValueError(f"{label} must be a positive integer")
    return value


def parse_matrix(entry: Any, *, rows: int | None = None, cols: int | None = None) -> Matrix:
    if entry is None:
        raise IncompleteData("MISSING matrix")
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


def parse_vector_list(entry: Any, *, count: int, size: int, label: str) -> list[Vector]:
    if entry is None:
        raise IncompleteData(f"MISSING {label}")
    if not isinstance(entry, list) or len(entry) != count:
        raise ValueError(f"{label} must have length {count}")
    return [parse_vector(vector, size=size) for vector in entry]


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


def vector_add(left: Vector, right: Vector) -> Vector:
    if len(left) != len(right):
        raise ValueError("vector dimensions differ")
    return [left[idx] + right[idx] for idx in range(len(left))]


def vector_sub(left: Vector, right: Vector) -> Vector:
    if len(left) != len(right):
        raise ValueError("vector dimensions differ")
    return [left[idx] - right[idx] for idx in range(len(left))]


def vector_neg(vector: Vector) -> Vector:
    return [-value for value in vector]


def identity(size: int) -> Matrix:
    return [
        [1.0 + 0.0j if row == col else 0.0 + 0.0j for col in range(size)]
        for row in range(size)
    ]


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


def inner(gram: Matrix, left: Vector, right: Vector) -> complex:
    gright = matvec(gram, right)
    return sum(left[idx].conjugate() * gright[idx] for idx in range(len(left)))


def inverse(matrix: Matrix) -> Matrix:
    if len(matrix) != len(matrix[0]):
        raise ValueError("matrix is not square")
    size = len(matrix)
    work = [matrix[row][:] + identity(size)[row] for row in range(size)]
    pivot_row = 0
    for col in range(size):
        pivot = None
        for row in range(pivot_row, size):
            if abs(work[row][col]) > TOL:
                pivot = row
                break
        if pivot is None:
            raise ValueError("matrix is singular")
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][col]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for row in range(size):
            if row == pivot_row or abs(work[row][col]) <= TOL:
                continue
            factor = work[row][col]
            work[row] = [
                work[row][idx] - factor * work[pivot_row][idx]
                for idx in range(2 * size)
            ]
        pivot_row += 1
    return [row[size:] for row in work]


def load_candidate(path: Path) -> tuple[int, str, dict[str, Any] | None]:
    data = json.loads(path.read_text(encoding="utf-8"))
    slots = data.get("dotd_response_slots")
    if not isinstance(slots, dict):
        return 2, "MISSING dotd_response_slots object", None
    missing = [sector for sector in SECTORS if slots.get(sector) is None]
    if missing:
        return 2, f"MISSING dotD response slot entries: {', '.join(missing)}", None
    return 0, "loaded sector-specific finite dotD response slots", slots


def validate_slot(sector: str, slot: dict[str, Any]) -> list[str]:
    failures: list[str] = []

    if slot.get("kind") != EXPECTED_KIND[sector]:
        failures.append(
            f"{sector} kind {slot.get('kind')!r} != {EXPECTED_KIND[sector]!r}"
        )
    expected_cluster = EXPECTED_CLUSTER_DIMENSION[sector]
    if slot.get("expected_kernel_dimension") != expected_cluster:
        failures.append(
            f"{sector} expected_kernel_dimension {slot.get('expected_kernel_dimension')!r} "
            f"!= {expected_cluster}"
        )

    dimension = require_int(slot.get("dimension"), f"{sector}.dimension")
    gram = parse_matrix(slot.get("gram_matrix"), rows=dimension, cols=dimension)
    stiffness = parse_matrix(slot.get("stiffness_matrix"), rows=dimension, cols=dimension)
    projector = parse_matrix(slot.get("riesz_projector"), rows=dimension, cols=dimension)
    complement = parse_matrix(slot.get("complement_projector"), rows=dimension, cols=dimension)
    green = parse_matrix(slot.get("reduced_green_operator"), rows=dimension, cols=dimension)
    dotd = parse_matrix(slot.get("dotD_alpha1_matrix"), rows=dimension, cols=dimension)
    zero_modes = parse_vector_list(
        slot.get("ordered_zero_mode_basis"),
        count=expected_cluster,
        size=dimension,
        label=f"{sector}.ordered_zero_mode_basis",
    )
    source_vectors = parse_vector_list(
        slot.get("source_vectors"),
        count=expected_cluster,
        size=dimension,
        label=f"{sector}.source_vectors",
    )
    response_vectors = parse_vector_list(
        slot.get("horizontal_response_vectors"),
        count=expected_cluster,
        size=dimension,
        label=f"{sector}.horizontal_response_vectors",
    )

    if not is_positive_definite_hermitian(gram):
        failures.append(f"{sector} gram_matrix is not positive-definite Hermitian")
    if not is_hermitian(stiffness):
        failures.append(f"{sector} stiffness_matrix is not Hermitian")

    operator = matmul(inverse(gram), stiffness)

    zero = [[0.0j for _ in range(dimension)] for _ in range(dimension)]
    if max_abs_diff(matmul(projector, projector), projector) > TOL:
        failures.append(f"{sector} Riesz projector is not idempotent")
    if max_abs_diff(matmul(complement, complement), complement) > TOL:
        failures.append(f"{sector} complement projector is not idempotent")
    if max_abs_diff(matmul(projector, complement), zero) > TOL:
        failures.append(f"{sector} P Q is nonzero")
    if max_abs_diff(matmul(complement, projector), zero) > TOL:
        failures.append(f"{sector} Q P is nonzero")

    for i, left in enumerate(zero_modes):
        for j, right in enumerate(zero_modes):
            expected = 1.0 if i == j else 0.0
            value = inner(gram, left, right)
            if abs(value - expected) > TOL:
                failures.append(
                    f"{sector} zero-mode Gram[{i},{j}]={value} != {expected}"
                )

    for idx, psi in enumerate(zero_modes):
        p_residual = max_abs_vector(vector_sub(matvec(projector, psi), psi))
        q_residual = max_abs_vector(matvec(complement, psi))
        if p_residual > TOL:
            failures.append(f"{sector} projector does not fix zero mode {idx}")
        if q_residual > TOL:
            failures.append(f"{sector} complement does not annihilate zero mode {idx}")

        expected_source = matvec(complement, matvec(dotd, psi))
        source_diff = max_abs_vector(vector_sub(source_vectors[idx], expected_source))
        if source_diff > TOL:
            failures.append(f"{sector} source vector {idx} != Q dotD psi max_abs_diff={source_diff:.3e}")
        source_q_diff = max_abs_vector(vector_sub(matvec(complement, source_vectors[idx]), source_vectors[idx]))
        if source_q_diff > TOL:
            failures.append(f"{sector} source vector {idx} is not in complement")

        expected_response = vector_neg(matvec(green, source_vectors[idx]))
        response_diff = max_abs_vector(vector_sub(response_vectors[idx], expected_response))
        if response_diff > TOL:
            failures.append(
                f"{sector} response vector {idx} != -R source max_abs_diff={response_diff:.3e}"
            )
        horizontal = max_abs_vector(matvec(projector, response_vectors[idx]))
        if horizontal > TOL:
            failures.append(f"{sector} response vector {idx} violates P dotPsi=0")
        complement_response = max_abs_vector(
            vector_sub(matvec(complement, response_vectors[idx]), response_vectors[idx])
        )
        if complement_response > TOL:
            failures.append(f"{sector} response vector {idx} is not in complement")
        equation_residual = max_abs_vector(
            vector_add(matvec(operator, response_vectors[idx]), source_vectors[idx])
        )
        if equation_residual > TOL:
            failures.append(
                f"{sector} first-order equation residual {idx}={equation_residual:.3e}"
            )
        for jdx, psi_j in enumerate(zero_modes):
            value = inner(gram, psi_j, response_vectors[idx])
            if abs(value) > TOL:
                failures.append(
                    f"{sector} horizontal inner product response {idx} vs psi {jdx} = {value}"
                )

    if slot.get("selected_dotD_source_verified") is not True:
        failures.append(f"{sector} selected_dotD_source_verified is not true")
    if slot.get("alpha1_driver_verified") is not True:
        failures.append(f"{sector} alpha1_driver_verified is not true")
    if slot.get("green_operator_verified") is not True:
        failures.append(f"{sector} green_operator_verified is not true")
    if slot.get("horizontal_gauge_verified") is not True:
        failures.append(f"{sector} horizontal_gauge_verified is not true")

    return failures


def validate_slots(slots: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    for sector in SECTORS:
        entry = slots.get(sector)
        if not isinstance(entry, dict):
            raise IncompleteData(f"MISSING {sector} dotD response slot object")
        failures.extend(validate_slot(sector, entry))
    return failures


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_iwasawa_dotd_response.py <dotd-response-data.json>")
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
        print(f"INVALID dotD response data: {exc}")
        return 1

    if failures:
        print("dotD response validation FAIL")
        for failure in failures[:50]:
            print(f"- {failure}")
        if len(failures) > 50:
            print(f"- ... {len(failures) - 50} more failures")
        return 1

    print("dotD response validation PASS")
    print("finite dotD sources and horizontal zero-mode responses are consistent")
    print("primitive overlap contractions and Yukawa matrices remain separate checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
