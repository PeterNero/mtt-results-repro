"""Validate finite reduced Green-operator data for Iwasawa slots.

This validator checks the finite inverse-on-the-complement contract that comes
after a Riesz projector and gap/error certificate. It accepts or rejects
proposed Galerkin Green-operator data; it does not construct the selected
operator or prove that a toy matrix is the MTT-selected one.

Exit codes:
  0: complete reduced-Green candidate passes implemented checks
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


class IncompleteData(ValueError):
    """Raised when a required Green-operator slot value is still open."""


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


def mat_sub(left: Matrix, right: Matrix) -> Matrix:
    if len(left) != len(right) or len(left[0]) != len(right[0]):
        raise ValueError("matrix dimensions differ")
    return [
        [left[row][col] - right[row][col] for col in range(len(left[0]))]
        for row in range(len(left))
    ]


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
    slots = data.get("green_slots")
    if not isinstance(slots, dict):
        return 2, "MISSING green_slots object", None
    missing = [sector for sector in SECTORS if slots.get(sector) is None]
    if missing:
        return 2, f"MISSING Green slot entries: {', '.join(missing)}", None
    return 0, "loaded sector-specific finite reduced-Green slots", slots


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

    if not is_positive_definite_hermitian(gram):
        failures.append(f"{sector} gram_matrix is not positive-definite Hermitian")
    if not is_hermitian(stiffness):
        failures.append(f"{sector} stiffness_matrix is not Hermitian")

    if max_abs_diff(matmul(projector, projector), projector) > TOL:
        failures.append(f"{sector} Riesz projector is not idempotent")
    if max_abs_diff(matmul(adjoint(projector), gram), matmul(gram, projector)) > TOL:
        failures.append(f"{sector} Riesz projector is not Gram-self-adjoint")
    projector_rank = rank(projector)
    if projector_rank != expected_cluster:
        failures.append(
            f"{sector} Riesz projector rank {projector_rank} != {expected_cluster}"
        )

    expected_complement = mat_sub(identity(dimension), projector)
    complement_diff = max_abs_diff(complement, expected_complement)
    if complement_diff > TOL:
        failures.append(
            f"{sector} complement_projector != I-P max_abs_diff={complement_diff:.3e}"
        )
    if max_abs_diff(matmul(complement, complement), complement) > TOL:
        failures.append(f"{sector} complement projector is not idempotent")
    if max_abs_diff(matmul(adjoint(complement), gram), matmul(gram, complement)) > TOL:
        failures.append(f"{sector} complement projector is not Gram-self-adjoint")
    if max_abs_diff(matmul(projector, complement), [[0.0j for _ in range(dimension)] for _ in range(dimension)]) > TOL:
        failures.append(f"{sector} P Q is nonzero")
    if max_abs_diff(matmul(complement, projector), [[0.0j for _ in range(dimension)] for _ in range(dimension)]) > TOL:
        failures.append(f"{sector} Q P is nonzero")

    if max_abs_diff(matmul(adjoint(green), gram), matmul(gram, green)) > TOL:
        failures.append(f"{sector} reduced Green operator is not Gram-self-adjoint")
    if max_abs_diff(matmul(green, projector), [[0.0j for _ in range(dimension)] for _ in range(dimension)]) > TOL:
        failures.append(f"{sector} reduced Green does not annihilate P on the right")
    if max_abs_diff(matmul(projector, green), [[0.0j for _ in range(dimension)] for _ in range(dimension)]) > TOL:
        failures.append(f"{sector} reduced Green does not annihilate P on the left")
    if max_abs_diff(matmul(complement, green), green) > TOL:
        failures.append(f"{sector} Q R != R")
    if max_abs_diff(matmul(green, complement), green) > TOL:
        failures.append(f"{sector} R Q != R")

    operator = matmul(inverse(gram), stiffness)
    ar_diff = max_abs_diff(matmul(operator, green), complement)
    if ar_diff > TOL:
        failures.append(f"{sector} A R != Q max_abs_diff={ar_diff:.3e}")
    ra_diff = max_abs_diff(matmul(green, operator), complement)
    if ra_diff > TOL:
        failures.append(f"{sector} R A != Q max_abs_diff={ra_diff:.3e}")

    complement_gap = parse_float(
        slot.get("complement_gap"),
        f"{sector}.complement_gap",
        positive=True,
    )
    truncation_error = parse_float(
        slot.get("truncation_error_bound"),
        f"{sector}.truncation_error_bound",
    )
    green_norm_bound = parse_float(
        slot.get("green_norm_bound"),
        f"{sector}.green_norm_bound",
        positive=True,
    )
    if complement_gap <= truncation_error + TOL:
        failures.append(
            f"{sector} complement gap not larger than truncation error: "
            f"gamma={complement_gap:.3e}, eta={truncation_error:.3e}"
        )
    else:
        spectral_bound = 1.0 / (complement_gap - truncation_error)
        if green_norm_bound + TOL < spectral_bound:
            failures.append(
                f"{sector} green_norm_bound={green_norm_bound:.3e} "
                f"< 1/(gamma-eta)={spectral_bound:.3e}"
            )

    if slot.get("selected_source_verified") is not True:
        failures.append(f"{sector} selected_source_verified is not true")
    if slot.get("riesz_gap_verified") is not True:
        failures.append(f"{sector} riesz_gap_verified is not true")
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
            raise IncompleteData(f"MISSING {sector} Green slot object")
        failures.extend(validate_slot(sector, entry))
    return failures


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_iwasawa_reduced_green.py <reduced-green-data.json>")
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
        print(f"INVALID reduced-Green data: {exc}")
        return 1

    if failures:
        print("reduced-Green validation FAIL")
        for failure in failures[:50]:
            print(f"- {failure}")
        if len(failures) > 50:
            print(f"- ... {len(failures) - 50} more failures")
        return 1

    print("reduced-Green validation PASS")
    print("finite complement projector and inverse-on-complement identities are consistent")
    print("dotD_alpha1, horizontal responses, and overlap matrices remain separate checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
