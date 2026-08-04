"""Validate selected SU(5) qutrit polarization data.

Exit codes:
  0: complete packet passes the implemented finite algebraic checks
  1: complete packet fails a mathematical/schema/guardrail check
  2: packet is incomplete/open rather than mathematically failed

The validator is intentionally finite.  It does not compute zero modes from
geometry.  It checks whether a supplied packet actually proves the sector
transport needed by the SU(5) qutrit heavy-link candidate:

    U_10^dagger C U_bar5 = F

or the conjugate orientation, modulo row/column rephasings and permutations.
Only packets marked SELECTED_DATA with selected-source evidence can promote the
candidate to selected proof data.  UNSELECTED_FIXTURE packets may pass algebra
as smoke tests but cannot promote the candidate.
"""

from __future__ import annotations

import itertools
import json
import math
import sys
from pathlib import Path
from typing import Any


SCHEMA = "SelectedSU5QutritPolarizationData.v1"
TOL = 1e-9
OMEGA = complex(-0.5, math.sqrt(3) / 2.0)
ROLES = {"SELECTED_DATA", "UNSELECTED_FIXTURE"}
SOURCE_KINDS = {
    "typed_monad_cech_cohomology",
    "spectral_galerkin_riesz_zero_modes",
    "selected_gerbe_twisted_bundle",
    "finite_qutrit_smoke_fixture",
}

Matrix = list[list[complex]]


class IncompleteData(ValueError):
    """Raised when a packet is still open."""


def parse_complex(value: Any) -> complex:
    if isinstance(value, bool):
        raise ValueError(f"invalid complex entry {value!r}")
    if isinstance(value, (int, float)):
        return complex(float(value), 0.0)
    if (
        isinstance(value, list)
        and len(value) == 2
        and all(isinstance(part, (int, float)) for part in value)
    ):
        return complex(float(value[0]), float(value[1]))
    raise ValueError(f"invalid complex entry {value!r}")


def parse_matrix(value: Any, label: str) -> Matrix:
    matrix_data = value.get("matrix") if isinstance(value, dict) else value
    if matrix_data is None:
        raise IncompleteData(f"MISSING {label}")
    if not isinstance(matrix_data, list) or len(matrix_data) != 3:
        raise ValueError(f"{label} must have three rows")
    matrix: Matrix = []
    for row in matrix_data:
        if not isinstance(row, list) or len(row) != 3:
            raise ValueError(f"{label} must be 3x3")
        matrix.append([parse_complex(entry) for entry in row])
    return matrix


def identity() -> Matrix:
    return [[1.0 + 0j if row == col else 0j for col in range(3)] for row in range(3)]


def clock() -> Matrix:
    return [[OMEGA**row if row == col else 0j for col in range(3)] for row in range(3)]


def fourier(conjugate: bool = False) -> Matrix:
    omega = OMEGA.conjugate() if conjugate else OMEGA
    scale = 1.0 / math.sqrt(3)
    return [[omega ** (row * col) * scale for col in range(3)] for row in range(3)]


def dagger(matrix: Matrix) -> Matrix:
    return [[matrix[col][row].conjugate() for col in range(3)] for row in range(3)]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return [
        [sum(left[row][mid] * right[mid][col] for mid in range(3)) for col in range(3)]
        for row in range(3)
    ]


def matrix_sub(left: Matrix, right: Matrix) -> Matrix:
    return [[left[row][col] - right[row][col] for col in range(3)] for row in range(3)]


def max_abs(matrix: Matrix) -> float:
    return max(abs(entry) for row in matrix for entry in row)


def approx_equal(left: Matrix, right: Matrix, tol: float = TOL) -> bool:
    return max_abs(matrix_sub(left, right)) <= tol


def matrix_power(matrix: Matrix, power: int) -> Matrix:
    result = identity()
    for _ in range(power):
        result = matmul(result, matrix)
    return result


def det3(matrix: Matrix) -> complex:
    a = matrix
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def is_hermitian(matrix: Matrix) -> bool:
    return approx_equal(matrix, dagger(matrix))


def leading_minor2(matrix: Matrix) -> complex:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def is_positive_definite_hermitian(matrix: Matrix) -> bool:
    if not is_hermitian(matrix):
        return False
    minors = [matrix[0][0], leading_minor2(matrix), det3(matrix)]
    return all(abs(value.imag) <= TOL and value.real > TOL for value in minors)


def is_metric_unitary(basis: Matrix, metric: Matrix) -> bool:
    return approx_equal(matmul(matmul(dagger(basis), metric), basis), identity())


def is_diagonal(matrix: Matrix) -> bool:
    return all(abs(matrix[row][col]) <= TOL for row in range(3) for col in range(3) if row != col)


def validate_qutrit_operators(clock_op: Matrix, shift_op: Matrix) -> bool:
    lhs = matmul(clock_op, shift_op)
    rhs = [[OMEGA * entry for entry in row] for row in matmul(shift_op, clock_op)]
    return (
        approx_equal(matrix_power(clock_op, 3), identity())
        and approx_equal(matrix_power(shift_op, 3), identity())
        and approx_equal(lhs, rhs)
    )


def dephase(matrix: Matrix) -> Matrix | None:
    if any(abs(matrix[0][col]) <= TOL for col in range(3)):
        return None
    if any(abs(matrix[row][0]) <= TOL for row in range(3)):
        return None

    left_phases = [matrix[row][0].conjugate() / abs(matrix[row][0]) for row in range(3)]
    after_left = [[left_phases[row] * matrix[row][col] for col in range(3)] for row in range(3)]
    right_phases = [
        after_left[0][col].conjugate() / abs(after_left[0][col]) for col in range(3)
    ]
    return [
        [after_left[row][col] * right_phases[col] for col in range(3)]
        for row in range(3)
    ]


def permute(matrix: Matrix, rows: tuple[int, ...], cols: tuple[int, ...]) -> Matrix:
    return [[matrix[rows[row]][cols[col]] for col in range(3)] for row in range(3)]


def orientation_mod_rephase_permutation(matrix: Matrix) -> str | None:
    f = dephase(fourier())
    f_star = dephase(fourier(conjugate=True))
    assert f is not None and f_star is not None

    for rows in itertools.permutations(range(3)):
        for cols in itertools.permutations(range(3)):
            dephased = dephase(permute(matrix, rows, cols))
            if dephased is None:
                continue
            if approx_equal(dephased, f):
                return "F"
            if approx_equal(dephased, f_star):
                return "F_conjugate"
    return None


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


def validate_sector(
    sector_data: dict[str, Any],
    basis_key: str,
    expected_polarization: str,
) -> tuple[Matrix, Matrix, list[str], dict[str, Any]]:
    failures: list[str] = []
    basis = parse_matrix(sector_data.get(basis_key), basis_key)
    metric = parse_matrix(sector_data.get("L2_metric"), f"{basis_key}.L2_metric")
    clock_op = parse_matrix(
        sector_data.get("clock_operator_matrix_in_basis"),
        f"{basis_key}.clock_operator_matrix_in_basis",
    )
    shift_op = parse_matrix(
        sector_data.get("shift_operator_matrix_in_basis"),
        f"{basis_key}.shift_operator_matrix_in_basis",
    )

    if sector_data.get("polarization") != expected_polarization:
        failures.append(f"{basis_key} polarization must be {expected_polarization}")
    if not is_positive_definite_hermitian(metric):
        failures.append(f"{basis_key} L2_metric must be positive-definite Hermitian")
    if not is_metric_unitary(basis, metric):
        failures.append(f"{basis_key} must be unitary in its selected metric")
    if not validate_qutrit_operators(clock_op, shift_op):
        failures.append(f"{basis_key} clock/shift operators must satisfy the qutrit relation")

    if expected_polarization == "clock" and not is_diagonal(clock_op):
        failures.append(f"{basis_key} clock-polarized sector must diagonalize clock operator")
    if expected_polarization == "shift" and not is_diagonal(shift_op):
        failures.append(f"{basis_key} shift-polarized sector must diagonalize shift operator")

    report = {
        "polarization": sector_data.get("polarization"),
        "basis_unitary_in_metric": is_metric_unitary(basis, metric),
        "qutrit_relation_passes": validate_qutrit_operators(clock_op, shift_op),
        "clock_operator_diagonal": is_diagonal(clock_op),
        "shift_operator_diagonal": is_diagonal(shift_op),
    }
    return basis, metric, failures, report


def validate_packet(data: dict[str, Any]) -> tuple[list[str], dict[str, Any]]:
    if data.get("status") == "OPEN":
        raise IncompleteData("selected SU5 qutrit polarization packet is OPEN")
    if data.get("schema") != SCHEMA:
        raise ValueError(f"schema must be {SCHEMA}")
    role = data.get("candidate_role")
    if role not in ROLES:
        raise ValueError(f"candidate_role must be one of {sorted(ROLES)}")

    selected_source_promotes, source_failures = source_promotes_selected(data, role)
    failures = list(source_failures)

    sectors = data.get("sector_basis_data")
    if not isinstance(sectors, dict):
        raise IncompleteData("MISSING sector_basis_data")
    if not isinstance(sectors.get("10_M"), dict) or not isinstance(sectors.get("bar5_M"), dict):
        raise IncompleteData("MISSING 10_M or bar5_M sector data")

    u10, _g10, sector_failures_10, report_10 = validate_sector(
        sectors["10_M"], "basis_matrix_U10", "clock"
    )
    ubar5, _gbar5, sector_failures_bar5, report_bar5 = validate_sector(
        sectors["bar5_M"], "basis_matrix_Ubar5", "shift"
    )
    failures.extend(sector_failures_10)
    failures.extend(sector_failures_bar5)

    frame = data.get("shared_family_frame")
    if not isinstance(frame, dict):
        raise IncompleteData("MISSING shared_family_frame")
    if frame.get("coordinate_frame_certified_common") is not True:
        raise IncompleteData("shared family coordinate frame must be certified")
    cross_metric = parse_matrix(
        frame.get("cross_pairing_metric_10_bar5"),
        "shared_family_frame.cross_pairing_metric_10_bar5",
    )

    relative = matmul(matmul(dagger(u10), cross_metric), ubar5)
    orientation = orientation_mod_rephase_permutation(relative)
    if orientation is None:
        failures.append("relative transport is not F or F_conjugate modulo rephase/permutation")

    acceptance = data.get("acceptance_tests")
    if not isinstance(acceptance, dict):
        raise IncompleteData("MISSING acceptance_tests")
    if acceptance.get("relative_transport_equals_F_mod_rephase_permutation") is not True:
        failures.append("acceptance test relative_transport_equals_F_mod_rephase_permutation must be true")
    if acceptance.get("derived_without_observed_flavor_inputs") is not True:
        failures.append("acceptance test derived_without_observed_flavor_inputs must be true")
    if acceptance.get("orientation_selects_F_not_F_conjugate") is True and orientation != "F":
        failures.append("packet claims F orientation but relative transport is not F")

    promotes_to_selected_input = selected_source_promotes and orientation == "F" and not failures
    report = {
        "schema": data.get("schema"),
        "candidate_role": role,
        "sector_10": report_10,
        "sector_bar5": report_bar5,
        "orientation_mod_rephase_permutation": orientation,
        "relative_transport_matches_qutrit_fourier": orientation in {"F", "F_conjugate"},
        "selected_source_promotes": selected_source_promotes,
        "promotes_to_selected_heavy_link_input": promotes_to_selected_input,
        "uses_observed_flavor_inputs": data.get("source", {}).get("uses_observed_flavor_inputs"),
        "uses_benchmark_flavor_inputs": data.get("source", {}).get("uses_benchmark_flavor_inputs"),
    }
    return failures, report


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_selected_su5_qutrit_polarization.py <packet.json>")
        return 1

    path = Path(argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        failures, report = validate_packet(data)
    except IncompleteData as exc:
        print(str(exc))
        return 2
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"INVALID selected SU5 qutrit polarization packet: {exc}")
        return 1

    print(f"polarization_validation_report={json.dumps(report, sort_keys=True)}")
    if failures:
        print("selected SU5 qutrit polarization validation FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("selected SU5 qutrit polarization validation PASS")
    if report["promotes_to_selected_heavy_link_input"]:
        print("packet promotes the SU5 qutrit heavy-link candidate to selected input")
    else:
        print("packet is algebraically valid but does not promote selected MTT data")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
