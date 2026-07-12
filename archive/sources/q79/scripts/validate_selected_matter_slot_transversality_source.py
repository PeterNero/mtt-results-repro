"""Validate a selected matter-slot transversality source packet.

Exit codes:
  0: complete packet proves the selected source gate;
  1: complete packet fails a selected-source, branch, or transport check;
  2: packet is explicitly open/incomplete.

This validator sits upstream of the finite SU(5) qutrit polarization validator.
It asks whether MTT has actually sourced the matter-slot transversality claim:

    10_M  = selected clock-polarized qutrit slot,
    bar5_M = selected shift-polarized qutrit slot.

It deliberately refuses Route C smoke data whose finite matrices are consistent
but whose selected-origin flags are still absent.
"""

from __future__ import annotations

import itertools
import json
import math
import sys
from pathlib import Path
from typing import Any


SCHEMA = "SelectedMatterSlotTransversalitySource.v1"
TOL = 1e-9
OMEGA = complex(-0.5, math.sqrt(3) / 2.0)
SOURCE_KINDS = {
    "route_c_spectral_galerkin",
    "typed_monad_cech_cohomology",
    "selected_gerbe_projector_retention",
    "spectral_galerkin_riesz_zero_modes",
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


def approx_equal(left: Matrix, right: Matrix) -> bool:
    return max_abs(matrix_sub(left, right)) <= TOL


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


def require_bool(
    condition: bool,
    failures: list[str],
    message: str,
) -> None:
    if not condition:
        failures.append(message)


def validate_source(data: dict[str, Any], failures: list[str]) -> dict[str, Any]:
    source = data.get("source")
    if not isinstance(source, dict):
        raise IncompleteData("MISSING source")
    if source.get("source_kind") not in SOURCE_KINDS:
        raise ValueError(f"source.source_kind must be one of {sorted(SOURCE_KINDS)}")

    require_bool(source.get("selected_by_mtt") is True, failures, "source.selected_by_mtt must be true")
    require_bool(source.get("fixture_only") is False, failures, "source.fixture_only must be false")
    require_bool(
        isinstance(source.get("source_certificate"), str) and bool(source.get("source_certificate")),
        failures,
        "source.source_certificate is required",
    )
    require_bool(
        source.get("uses_observed_flavor_inputs") is False,
        failures,
        "source must not use observed flavor inputs",
    )
    require_bool(
        source.get("uses_benchmark_flavor_inputs") is False,
        failures,
        "source must not use benchmark flavor inputs",
    )
    return {
        "source_kind": source.get("source_kind"),
        "selected_by_mtt": source.get("selected_by_mtt"),
        "fixture_only": source.get("fixture_only"),
    }


def validate_branch(data: dict[str, Any], failures: list[str]) -> dict[str, Any]:
    branch = data.get("branch")
    if not isinstance(branch, dict):
        raise IncompleteData("MISSING branch")
    require_bool(branch.get("q") == 79, failures, "branch.q must be 79 for the retarded selected representative")
    require_bool(branch.get("orientation") == "F", failures, "branch.orientation must be F")
    require_bool(
        branch.get("retarded_q79_branch_selected") is True,
        failures,
        "retarded_q79_branch_selected must be true",
    )
    require_bool(
        branch.get("antiunitary_conjugate_retained") is True,
        failures,
        "antiunitary_conjugate_retained must be true",
    )
    return {
        "q": branch.get("q"),
        "orientation": branch.get("orientation"),
        "retarded_q79_branch_selected": branch.get("retarded_q79_branch_selected"),
    }


def validate_route_c(data: dict[str, Any], failures: list[str]) -> dict[str, Any]:
    source = data.get("source", {})
    route_c = data.get("route_c_evidence", {})
    if source.get("source_kind") != "route_c_spectral_galerkin":
        return {"checked": False}
    if not isinstance(route_c, dict):
        raise IncompleteData("MISSING route_c_evidence")
    required = [
        "selected_origin_verified",
        "honest_route_c_residual_pass",
        "honest_de_action_pass",
        "honest_riesz_gap_pass",
        "honest_reduced_green_pass",
        "honest_dotd_response_pass",
    ]
    for key in required:
        require_bool(route_c.get(key) is True, failures, f"route_c_evidence.{key} must be true")
    return {key: route_c.get(key) for key in required} | {"checked": True}


def validate_matter_slots(data: dict[str, Any], failures: list[str]) -> dict[str, Any]:
    matter = data.get("matter_slot_source")
    if not isinstance(matter, dict):
        raise IncompleteData("MISSING matter_slot_source")
    require_bool(
        matter.get("common_family_frame_verified") is True,
        failures,
        "matter_slot_source.common_family_frame_verified must be true",
    )
    require_bool(
        matter.get("L2_metrics_selected") is True,
        failures,
        "matter_slot_source.L2_metrics_selected must be true",
    )
    require_bool(
        matter.get("projector_retention_selected") is True,
        failures,
        "matter_slot_source.projector_retention_selected must be true",
    )
    require_bool(
        matter.get("zero_mode_basis_selected") is True,
        failures,
        "matter_slot_source.zero_mode_basis_selected must be true",
    )

    slots = matter.get("slots")
    if not isinstance(slots, dict):
        raise IncompleteData("MISSING matter_slot_source.slots")
    slot_10 = slots.get("10_M")
    slot_bar5 = slots.get("bar5_M")
    if not isinstance(slot_10, dict) or not isinstance(slot_bar5, dict):
        raise IncompleteData("MISSING 10_M or bar5_M slot")

    require_bool(slot_10.get("dimension") == 3, failures, "10_M dimension must be 3")
    require_bool(slot_bar5.get("dimension") == 3, failures, "bar5_M dimension must be 3")
    require_bool(slot_10.get("polarization") == "clock", failures, "10_M polarization must be clock")
    require_bool(slot_bar5.get("polarization") == "shift", failures, "bar5_M polarization must be shift")
    require_bool(
        slot_10.get("selected_source_verified") is True,
        failures,
        "10_M selected_source_verified must be true",
    )
    require_bool(
        slot_bar5.get("selected_source_verified") is True,
        failures,
        "bar5_M selected_source_verified must be true",
    )

    u10 = parse_matrix(slot_10.get("basis_matrix_U10"), "10_M.basis_matrix_U10")
    ubar5 = parse_matrix(slot_bar5.get("basis_matrix_Ubar5"), "bar5_M.basis_matrix_Ubar5")
    cross_metric = parse_matrix(
        matter.get("cross_pairing_metric_10_bar5"),
        "matter_slot_source.cross_pairing_metric_10_bar5",
    )
    relative = matmul(matmul(dagger(u10), cross_metric), ubar5)
    orientation = orientation_mod_rephase_permutation(relative)
    require_bool(orientation == "F", failures, "relative U_10^dagger C Ubar5 must be F")
    return {
        "common_family_frame_verified": matter.get("common_family_frame_verified"),
        "L2_metrics_selected": matter.get("L2_metrics_selected"),
        "projector_retention_selected": matter.get("projector_retention_selected"),
        "zero_mode_basis_selected": matter.get("zero_mode_basis_selected"),
        "relative_transport_orientation": orientation,
    }


def validate_packet(data: dict[str, Any]) -> tuple[list[str], dict[str, Any]]:
    if data.get("status") == "OPEN":
        raise IncompleteData("selected matter-slot transversality source packet is OPEN")
    if data.get("schema") != SCHEMA:
        raise ValueError(f"schema must be {SCHEMA}")

    failures: list[str] = []
    source_report = validate_source(data, failures)
    branch_report = validate_branch(data, failures)
    route_c_report = validate_route_c(data, failures)
    matter_report = validate_matter_slots(data, failures)

    guardrails = data.get("guardrails", {})
    if not isinstance(guardrails, dict):
        raise IncompleteData("MISSING guardrails")
    require_bool(
        guardrails.get("claims_full_sm_closure") is False,
        failures,
        "guardrail claims_full_sm_closure must be false",
    )
    require_bool(
        guardrails.get("uses_common_fourier_gauge_as_physical_mixing") is False,
        failures,
        "common Fourier gauge must not be used as physical mixing",
    )
    require_bool(
        guardrails.get("uses_observed_flavor_data") is False,
        failures,
        "observed flavor data must not be used",
    )
    require_bool(
        guardrails.get("uses_benchmark_flavor_entries") is False,
        failures,
        "benchmark flavor entries must not be used",
    )

    report = {
        "schema": data.get("schema"),
        "source": source_report,
        "branch": branch_report,
        "route_c_evidence": route_c_report,
        "matter_slot_source": matter_report,
        "selected_source_verified": len(failures) == 0,
        "promotes_su5_matter_slot_transversality": len(failures) == 0,
    }
    return failures, report


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_selected_matter_slot_transversality_source.py <packet.json>")
        return 1
    path = Path(argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        failures, report = validate_packet(data)
    except IncompleteData as exc:
        print(str(exc))
        return 2
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"INVALID selected matter-slot source packet: {exc}")
        return 1

    print(f"matter_slot_source_validation_report={json.dumps(report, sort_keys=True)}")
    if failures:
        print("selected matter-slot source validation FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("selected matter-slot source validation PASS")
    print("packet promotes SU(5) matter-slot transversality to selected input")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
