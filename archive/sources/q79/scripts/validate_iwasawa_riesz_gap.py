"""Validate finite Riesz projector and gap/error data for Iwasawa slots.

This validator checks the finite spectral certificate that comes after a
sector-specific D_E action has been assembled. It accepts or rejects proposed
Galerkin spectral data; it does not construct the selected operator or prove
that a toy matrix is the MTT-selected one.

Exit codes:
  0: complete Riesz/gap candidate passes implemented checks
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
    """Raised when a required spectral slot value is still open."""


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


def parse_float(value: Any, label: str, *, positive: bool = False) -> float:
    if value is None:
        raise IncompleteData(f"MISSING {label}")
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise ValueError(f"{label} must be numeric")
    result = float(value)
    if positive and result <= TOL:
        raise ValueError(f"{label} must be positive")
    if not positive and result < -TOL:
        raise ValueError(f"{label} must be nonnegative")
    return result


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


def vector_sub(left: Vector, right: Vector) -> Vector:
    if len(left) != len(right):
        raise ValueError("vector dimensions differ")
    return [left[idx] - right[idx] for idx in range(len(left))]


def vector_scale(value: complex, vector: Vector) -> Vector:
    return [value * item for item in vector]


def columns_to_matrix(columns: list[Vector]) -> Matrix:
    if not columns:
        raise ValueError("at least one column is required")
    height = len(columns[0])
    if any(len(column) != height for column in columns):
        raise ValueError("columns must have equal height")
    return [[columns[col][row] for col in range(len(columns))] for row in range(height)]


def identity(size: int) -> Matrix:
    return [
        [1.0 + 0.0j if row == col else 0.0 + 0.0j for col in range(size)]
        for row in range(size)
    ]


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


def parse_float_list(entry: Any, *, size: int, label: str, nonnegative: bool = True) -> list[float]:
    if entry is None:
        raise IncompleteData(f"MISSING {label}")
    if not isinstance(entry, list) or len(entry) != size:
        raise ValueError(f"{label} must have length {size}")
    values: list[float] = []
    for idx, value in enumerate(entry):
        parsed = parse_float(value, f"{label}[{idx}]")
        if nonnegative and parsed < -TOL:
            raise ValueError(f"{label}[{idx}] must be nonnegative")
        values.append(parsed)
    return values


def expected_projector(eigenvectors: list[Vector], gram: Matrix) -> Matrix:
    vector_matrix = columns_to_matrix(eigenvectors)
    return matmul(matmul(vector_matrix, adjoint(vector_matrix)), gram)


def load_candidate(path: Path) -> tuple[int, str, dict[str, Any] | None]:
    data = json.loads(path.read_text(encoding="utf-8"))
    slots = data.get("spectral_slots")
    if not isinstance(slots, dict):
        return 2, "MISSING spectral_slots object", None
    missing = [sector for sector in SECTORS if slots.get(sector) is None]
    if missing:
        return 2, f"MISSING spectral slot entries: {', '.join(missing)}", None
    return 0, "loaded sector-specific finite Riesz/gap spectral slots", slots


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

    if not is_positive_definite_hermitian(gram):
        failures.append(f"{sector} gram_matrix is not positive-definite Hermitian")
    if not is_hermitian(stiffness):
        failures.append(f"{sector} stiffness_matrix is not Hermitian")

    eigenvalues = parse_float_list(
        slot.get("low_eigenvalues"),
        size=expected_cluster,
        label=f"{sector}.low_eigenvalues",
    )
    residual_bounds = parse_float_list(
        slot.get("residual_norms"),
        size=expected_cluster,
        label=f"{sector}.residual_norms",
    )
    vector_data = slot.get("cluster_eigenvectors")
    if vector_data is None:
        raise IncompleteData(f"MISSING {sector}.cluster_eigenvectors")
    if not isinstance(vector_data, list) or len(vector_data) != expected_cluster:
        raise ValueError(
            f"{sector}.cluster_eigenvectors must have length {expected_cluster}"
        )
    eigenvectors = [parse_vector(vector, size=dimension) for vector in vector_data]

    for i, left in enumerate(eigenvectors):
        for j, right in enumerate(eigenvectors):
            expected = 1.0 if i == j else 0.0
            value = inner(gram, left, right)
            if abs(value - expected) > TOL:
                failures.append(
                    f"{sector} cluster Gram[{i},{j}]={value} != {expected}"
                )

    computed_residuals: list[float] = []
    for idx, vector in enumerate(eigenvectors):
        lhs = matvec(stiffness, vector)
        rhs = vector_scale(eigenvalues[idx], matvec(gram, vector))
        residual = max_abs_vector(vector_sub(lhs, rhs))
        computed_residuals.append(residual)
        if residual > residual_bounds[idx] + TOL:
            failures.append(
                f"{sector} eigenpair {idx} residual={residual:.3e} "
                f"> reported bound {residual_bounds[idx]:.3e}"
            )

    if max_abs_diff(matmul(projector, projector), projector) > TOL:
        failures.append(f"{sector} Riesz projector is not idempotent")
    if max_abs_diff(matmul(adjoint(projector), gram), matmul(gram, projector)) > TOL:
        failures.append(f"{sector} Riesz projector is not Gram-self-adjoint")
    projector_rank = rank(projector)
    if projector_rank != expected_cluster:
        failures.append(
            f"{sector} Riesz projector rank {projector_rank} != {expected_cluster}"
        )

    projected = expected_projector(eigenvectors, gram)
    projector_diff = max_abs_diff(projector, projected)
    if projector_diff > TOL:
        failures.append(
            f"{sector} Riesz projector does not match cluster span max_abs_diff={projector_diff:.3e}"
        )

    for idx, vector in enumerate(eigenvectors):
        residual = max_abs_vector(vector_sub(matvec(projector, vector), vector))
        if residual > TOL:
            failures.append(f"{sector} projector does not fix eigenvector {idx}")

    contour_radius = parse_float(
        slot.get("contour_radius"),
        f"{sector}.contour_radius",
        positive=True,
    )
    complement_gap = parse_float(
        slot.get("complement_gap"),
        f"{sector}.complement_gap",
        positive=True,
    )
    truncation_error = parse_float(
        slot.get("truncation_error_bound"),
        f"{sector}.truncation_error_bound",
    )
    epsilon_low = max(
        abs(eigenvalues[idx]) + residual_bounds[idx]
        for idx in range(expected_cluster)
    )
    if epsilon_low + truncation_error >= contour_radius - TOL:
        failures.append(
            f"{sector} low cluster is not inside contour: "
            f"epsilon_low+eta={epsilon_low + truncation_error:.3e}, "
            f"tau={contour_radius:.3e}"
        )
    if contour_radius >= complement_gap - truncation_error - TOL:
        failures.append(
            f"{sector} contour is not below complement gap: "
            f"tau={contour_radius:.3e}, gamma-eta={complement_gap - truncation_error:.3e}"
        )

    if slot.get("selected_source_verified") is not True:
        failures.append(f"{sector} selected_source_verified is not true")
    if slot.get("operator_data_verified") is not True:
        failures.append(f"{sector} operator_data_verified is not true")
    if slot.get("boundary_conditions_verified") is not True:
        failures.append(f"{sector} boundary_conditions_verified is not true")

    return failures


def validate_slots(slots: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    for sector in SECTORS:
        entry = slots.get(sector)
        if not isinstance(entry, dict):
            raise IncompleteData(f"MISSING {sector} spectral slot object")
        failures.extend(validate_slot(sector, entry))
    return failures


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_iwasawa_riesz_gap.py <riesz-gap-data.json>")
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
        print(f"INVALID Riesz/gap data: {exc}")
        return 1

    if failures:
        print("Riesz/gap validation FAIL")
        for failure in failures[:50]:
            print(f"- {failure}")
        if len(failures) > 50:
            print(f"- ... {len(failures) - 50} more failures")
        return 1

    print("Riesz/gap validation PASS")
    print("finite projectors, low eigenpairs, and gap/error inequalities are consistent")
    print("selected D_E origin, dotD_alpha1, Green operators, and overlap matrices remain separate checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
