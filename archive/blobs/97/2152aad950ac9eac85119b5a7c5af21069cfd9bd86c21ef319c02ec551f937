"""Validate finite H^1(X,L^2) data for the visible rank-two Ext route.

Exit codes:
  0: complete packet passes the implemented cochain and Ext checks
  1: complete packet fails a mathematical/schema/guardrail check
  2: packet is incomplete/open rather than mathematically failed

The validator is intentionally finite. It does not invent line-bundle
transition functions or a Dolbeault operator. It checks a supplied
Cech/Dolbeault cochain complex

    C0 --d0--> C1 --d1--> C2

and computes h1 = dim ker(d1) - rank(d0). A nonzero Ext class must be a closed
C1 vector not lying in im(d0).
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


SCHEMA = "VisibleRank2L2CohomologyData.v1"
ROLES = {"SELECTED_DATA", "UNSELECTED_FIXTURE"}
SOURCE_KINDS = {
    "typed_cech_line_bundle",
    "dolbeault_line_bundle",
    "monad_resolved_line_bundle",
    "finite_fixture",
}

QComplex = tuple[Fraction, Fraction]
Matrix = list[list[QComplex]]
Vector = list[QComplex]


class IncompleteData(ValueError):
    """Raised when a packet is still open."""


def qzero() -> QComplex:
    return (Fraction(0), Fraction(0))


def qone() -> QComplex:
    return (Fraction(1), Fraction(0))


def is_zero(value: QComplex) -> bool:
    return value[0] == 0 and value[1] == 0


def qadd(left: QComplex, right: QComplex) -> QComplex:
    return (left[0] + right[0], left[1] + right[1])


def qsub(left: QComplex, right: QComplex) -> QComplex:
    return (left[0] - right[0], left[1] - right[1])


def qmul(left: QComplex, right: QComplex) -> QComplex:
    return (left[0] * right[0] - left[1] * right[1], left[0] * right[1] + left[1] * right[0])


def qdiv(left: QComplex, right: QComplex) -> QComplex:
    norm = right[0] * right[0] + right[1] * right[1]
    if norm == 0:
        raise ZeroDivisionError("division by zero complex rational")
    return (
        (left[0] * right[0] + left[1] * right[1]) / norm,
        (left[1] * right[0] - left[0] * right[1]) / norm,
    )


def parse_fraction(value: Any) -> Fraction:
    if isinstance(value, bool):
        raise ValueError(f"invalid rational entry {value!r}")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, float):
        return Fraction(str(value))
    if isinstance(value, str):
        return Fraction(value)
    raise ValueError(f"invalid rational entry {value!r}")


def parse_complex(value: Any) -> QComplex:
    if isinstance(value, list):
        if len(value) != 2:
            raise ValueError(f"complex entry list must be [real, imag], got {value!r}")
        return (parse_fraction(value[0]), parse_fraction(value[1]))
    return (parse_fraction(value), Fraction(0))


def parse_matrix(entry: Any, label: str) -> Matrix:
    matrix_data = entry.get("matrix") if isinstance(entry, dict) else entry
    if matrix_data is None:
        raise IncompleteData(f"MISSING {label}")
    if not isinstance(matrix_data, list):
        raise ValueError(f"{label} must be a list of rows")
    matrix: Matrix = []
    width: int | None = None
    for row in matrix_data:
        if not isinstance(row, list):
            raise ValueError(f"{label} rows must be lists")
        parsed = [parse_complex(value) for value in row]
        if width is None:
            width = len(parsed)
        elif len(parsed) != width:
            raise ValueError(f"{label} rows must have equal length")
        matrix.append(parsed)
    return matrix


def parse_vector(entry: Any, label: str) -> Vector:
    vector_data = entry.get("vector") if isinstance(entry, dict) else entry
    if vector_data is None:
        raise IncompleteData(f"MISSING {label}")
    if not isinstance(vector_data, list):
        raise ValueError(f"{label} must be a list")
    return [parse_complex(value) for value in vector_data]


def matrix_shape(matrix: Matrix) -> tuple[int, int]:
    if not matrix:
        return (0, 0)
    return (len(matrix), len(matrix[0]))


def matmul(left: Matrix, right: Matrix) -> Matrix:
    left_rows, left_cols = matrix_shape(left)
    right_rows, right_cols = matrix_shape(right)
    if left_cols != right_rows:
        raise ValueError(f"matrix shape mismatch {left_rows}x{left_cols} times {right_rows}x{right_cols}")
    return [
        [
            sum_q(qmul(left[row][mid], right[mid][col]) for mid in range(left_cols))
            for col in range(right_cols)
        ]
        for row in range(left_rows)
    ]


def matvec(matrix: Matrix, vector: Vector) -> Vector:
    rows, cols = matrix_shape(matrix)
    if cols != len(vector):
        raise ValueError(f"matrix/vector shape mismatch {rows}x{cols} times {len(vector)}")
    return [sum_q(qmul(matrix[row][col], vector[col]) for col in range(cols)) for row in range(rows)]


def sum_q(values: Any) -> QComplex:
    total = qzero()
    for value in values:
        total = qadd(total, value)
    return total


def is_zero_matrix(matrix: Matrix) -> bool:
    return all(is_zero(value) for row in matrix for value in row)


def is_zero_vector(vector: Vector) -> bool:
    return all(is_zero(value) for value in vector)


def rank(matrix: Matrix) -> int:
    if not matrix:
        return 0
    rows = [row[:] for row in matrix]
    row_count = len(rows)
    col_count = len(rows[0])
    pivot_row = 0
    for col in range(col_count):
        pivot = None
        for row in range(pivot_row, row_count):
            if not is_zero(rows[row][col]):
                pivot = row
                break
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        pivot_value = rows[pivot_row][col]
        rows[pivot_row] = [qdiv(value, pivot_value) for value in rows[pivot_row]]
        for row in range(row_count):
            if row == pivot_row or is_zero(rows[row][col]):
                continue
            factor = rows[row][col]
            rows[row] = [
                qsub(rows[row][entry_col], qmul(factor, rows[pivot_row][entry_col]))
                for entry_col in range(col_count)
            ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def append_column(matrix: Matrix, column: Vector) -> Matrix:
    rows, _cols = matrix_shape(matrix)
    if rows != len(column):
        raise ValueError("column length does not match matrix row count")
    return [row[:] + [column[index]] for index, row in enumerate(matrix)]


def source_promotes_selected(data: dict[str, Any], role: str) -> tuple[bool, list[str]]:
    source = data.get("source")
    if not isinstance(source, dict):
        raise IncompleteData("MISSING source object")
    if source.get("source_kind") not in SOURCE_KINDS:
        raise ValueError(f"source.source_kind must be one of {sorted(SOURCE_KINDS)}")

    failures: list[str] = []
    if source.get("uses_observed_flavor_inputs") is not False:
        failures.append("source.uses_observed_flavor_inputs must be false")
    if source.get("uses_benchmark_flavor_inputs") is not False:
        failures.append("source.uses_benchmark_flavor_inputs must be false")

    if role == "UNSELECTED_FIXTURE":
        if source.get("selected_by_mtt") is not False:
            failures.append("UNSELECTED_FIXTURE source.selected_by_mtt must be false")
        if source.get("fixture_only") is not True:
            failures.append("UNSELECTED_FIXTURE source.fixture_only must be true")
        return False, failures

    if source.get("selected_by_mtt") is not True:
        failures.append("SELECTED_DATA source.selected_by_mtt must be true")
    if source.get("fixture_only") is not False:
        failures.append("SELECTED_DATA source.fixture_only must be false")
    if not isinstance(source.get("source_certificate"), str) or not source.get("source_certificate"):
        failures.append("SELECTED_DATA requires source.source_certificate")
    return len(failures) == 0, failures


def validate_packet(data: dict[str, Any]) -> tuple[list[str], dict[str, Any]]:
    if data.get("status") == "OPEN":
        raise IncompleteData("visible rank-two L2 cohomology packet is OPEN")
    if data.get("schema") != SCHEMA:
        raise ValueError(f"schema must be {SCHEMA}")
    role = data.get("candidate_role")
    if role not in ROLES:
        raise ValueError(f"candidate_role must be one of {sorted(ROLES)}")

    target = data.get("target")
    if not isinstance(target, dict):
        raise IncompleteData("MISSING target object")
    if target.get("extension_sequence") != "0 -> L -> V_alpha -> L^{-1} -> 0":
        raise ValueError("target.extension_sequence must be the visible rank-two extension sequence")
    if target.get("c2_extension_alpha_coeffs") != [4, 0, 0]:
        raise ValueError("target.c2_extension_alpha_coeffs must be [4, 0, 0]")

    source_selected, source_failures = source_promotes_selected(data, role)
    failures = list(source_failures)

    complex_data = data.get("cochain_complex")
    if not isinstance(complex_data, dict):
        raise IncompleteData("MISSING cochain_complex object")
    d0 = parse_matrix(complex_data.get("d0"), "cochain_complex.d0")
    d1 = parse_matrix(complex_data.get("d1"), "cochain_complex.d1")
    dim_c1, dim_c0 = matrix_shape(d0)
    dim_c2, d1_cols = matrix_shape(d1)
    if d1_cols != dim_c1:
        raise ValueError("d1 column count must equal d0 row count")

    d1d0 = matmul(d1, d0)
    if not is_zero_matrix(d1d0):
        failures.append("cochain condition d1*d0=0 fails")

    rank_d0 = rank(d0)
    rank_d1 = rank(d1)
    dim_ker_d1 = dim_c1 - rank_d1
    h1 = dim_ker_d1 - rank_d0
    if h1 < 0:
        failures.append("computed h1 is negative; the complex/rank data are inconsistent")

    reported = data.get("reported_cohomology")
    if not isinstance(reported, dict):
        raise IncompleteData("MISSING reported_cohomology object")
    if reported.get("rank_d0") != rank_d0:
        failures.append(f"reported rank_d0={reported.get('rank_d0')} but computed {rank_d0}")
    if reported.get("rank_d1") != rank_d1:
        failures.append(f"reported rank_d1={reported.get('rank_d1')} but computed {rank_d1}")
    if reported.get("dim_ker_d1") != dim_ker_d1:
        failures.append(f"reported dim_ker_d1={reported.get('dim_ker_d1')} but computed {dim_ker_d1}")
    if reported.get("h1") != h1:
        failures.append(f"reported h1={reported.get('h1')} but computed {h1}")

    ext_vector = parse_vector(reported.get("extension_class_vector_C1"), "reported_cohomology.extension_class_vector_C1")
    if len(ext_vector) != dim_c1:
        raise ValueError("extension_class_vector_C1 length must equal dim C1")
    closed = is_zero_vector(matvec(d1, ext_vector))
    exact = rank(append_column(d0, ext_vector)) == rank_d0
    nonzero_ext = closed and not exact

    if not closed:
        failures.append("extension class vector is not d1-closed")
    if exact:
        failures.append("extension class vector lies in im(d0), so it is exact")
    if h1 <= 0:
        failures.append("computed h1 must be positive to construct a non-split extension")

    acceptance = data.get("acceptance_tests")
    if not isinstance(acceptance, dict):
        raise IncompleteData("MISSING acceptance_tests object")
    expected_acceptance = {
        "d1_d0_zero": is_zero_matrix(d1d0),
        "h1_positive": h1 > 0,
        "extension_class_closed": closed,
        "extension_class_not_exact": not exact,
        "derived_without_observed_flavor_inputs": True,
    }
    for key, value in expected_acceptance.items():
        if acceptance.get(key) is not value:
            failures.append(f"acceptance_tests.{key} must be {value}")

    promotes = source_selected and nonzero_ext and h1 > 0 and not failures
    report = {
        "schema": data.get("schema"),
        "candidate_role": role,
        "dimensions": {"C0": dim_c0, "C1": dim_c1, "C2": dim_c2},
        "rank_d0": rank_d0,
        "rank_d1": rank_d1,
        "dim_ker_d1": dim_ker_d1,
        "h1": h1,
        "d1_d0_zero": is_zero_matrix(d1d0),
        "extension_class_closed": closed,
        "extension_class_exact": exact,
        "nonzero_ext_class": nonzero_ext,
        "selected_source_promotes": source_selected,
        "promotes_to_non_split_V_alpha_input": promotes,
        "uses_observed_flavor_inputs": data.get("source", {}).get("uses_observed_flavor_inputs"),
        "uses_benchmark_flavor_inputs": data.get("source", {}).get("uses_benchmark_flavor_inputs"),
    }
    return failures, report


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_visible_rank2_l2_cohomology.py <cohomology-data.json>")
        return 1

    path = Path(argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        failures, report = validate_packet(data)
    except IncompleteData as exc:
        print(str(exc))
        return 2
    except (OSError, json.JSONDecodeError, ValueError, ZeroDivisionError) as exc:
        print(f"INVALID visible rank-two L2 cohomology packet: {exc}")
        return 1

    print(f"visible_rank2_l2_h1_report={json.dumps(report, sort_keys=True)}")
    if failures:
        print("visible rank-two L2 cohomology validation FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("visible rank-two L2 cohomology validation PASS")
    if report["promotes_to_non_split_V_alpha_input"]:
        print("packet promotes the rank-two route to a selected non-split V_alpha input")
    else:
        print("packet is algebraically valid but does not promote selected MTT data")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
