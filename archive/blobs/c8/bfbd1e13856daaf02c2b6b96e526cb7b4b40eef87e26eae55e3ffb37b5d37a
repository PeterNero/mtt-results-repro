"""Validate a Route C finite selected-connection residual certificate.

This is the source-side gate before the existing rho_E, D_E, Riesz, Green, and
dotD validators. It checks residual/tolerance bookkeeping and guardrails; it
does not solve the nonlinear HYM/Strominger equations.

Exit codes:
  0: complete residual certificate passes implemented checks
  1: complete candidate fails a mathematical/schema check
  2: candidate is incomplete/open rather than mathematically failed
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_RESIDUALS = (
    "rho_cocycle",
    "metric_compatibility",
    "integrability_F02",
    "hym_primitive",
    "bianchi_alpha1",
    "strominger_residual",
    "mtt_gradient",
)
REQUIRED_POSITIVE_GATES = (
    "mtt_hessian_min_eigenvalue",
    "riesz_gap_min",
)
TOL = 1e-12
EXPECTED_BRANCH_PACKETS = {
    "current_q79_orientation": {
        "torsion_label_m": 1,
        "global_cp_label": 79,
        "conditional_su5_transport_orientation": "F",
        "sector_orientations": {
            "Q": 1,
            "L": 1,
            "u": 2,
            "d": 2,
            "e": 2,
            "N": 2,
            "H": 0,
        },
        "c6_left_representative_labels": {
            "u:C6": 79,
            "d:C6": 79,
            "e:C6": 79,
            "nuD:C6": 79,
        },
    },
    "conjugate_q369_orientation": {
        "torsion_label_m": 2,
        "global_cp_label": 369,
        "conditional_su5_transport_orientation": "F*",
        "sector_orientations": {
            "Q": 2,
            "L": 2,
            "u": 1,
            "d": 1,
            "e": 1,
            "N": 1,
            "H": 0,
        },
        "c6_left_representative_labels": {
            "u:C6": 369,
            "d:C6": 369,
            "e:C6": 369,
            "nuD:C6": 369,
        },
    },
}


class IncompleteData(ValueError):
    """Raised when a residual certificate is still open."""


def parse_float(value: Any, label: str, *, positive: bool = False) -> float:
    if value is None:
        raise IncompleteData(f"MISSING {label}")
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise ValueError(f"{label} must be numeric")
    parsed = float(value)
    if positive and parsed <= TOL:
        raise ValueError(f"{label} must be positive")
    if not positive and parsed < -TOL:
        raise ValueError(f"{label} must be nonnegative")
    return parsed


def require_bool(data: dict[str, Any], key: str, expected: bool) -> list[str]:
    if data.get(key) is not expected:
        return [f"{key} must be {expected}"]
    return []


def validate_residual(name: str, entry: Any) -> list[str]:
    if entry is None:
        raise IncompleteData(f"MISSING residual {name}")
    if not isinstance(entry, dict):
        raise ValueError(f"residual {name} must be an object")
    value = parse_float(entry.get("value"), f"{name}.value")
    tolerance = parse_float(entry.get("tolerance"), f"{name}.tolerance", positive=True)
    if value > tolerance + TOL:
        return [f"{name} residual {value:.3e} exceeds tolerance {tolerance:.3e}"]
    return []


def validate_positive_gate(name: str, entry: Any) -> list[str]:
    if entry is None:
        raise IncompleteData(f"MISSING positive gate {name}")
    if not isinstance(entry, dict):
        raise ValueError(f"positive gate {name} must be an object")
    value = parse_float(entry.get("value"), f"{name}.value")
    lower_bound = parse_float(entry.get("strict_lower_bound"), f"{name}.strict_lower_bound")
    if value <= lower_bound + TOL:
        return [f"{name} value {value:.3e} is not above {lower_bound:.3e}"]
    return []


def validate_branch_packet(entry: Any) -> list[str]:
    if entry is None:
        raise IncompleteData("MISSING branch_packet")
    if not isinstance(entry, dict):
        raise ValueError("branch_packet must be an object")

    failures: list[str] = []
    branch = entry.get("branch")
    if branch not in EXPECTED_BRANCH_PACKETS:
        return [
            "branch_packet.branch must be current_q79_orientation or "
            "conjugate_q369_orientation"
        ]

    expected = EXPECTED_BRANCH_PACKETS[branch]
    for key in (
        "torsion_label_m",
        "global_cp_label",
        "conditional_su5_transport_orientation",
    ):
        if entry.get(key) != expected[key]:
            failures.append(
                f"branch_packet.{key} {entry.get(key)!r} != {expected[key]!r}"
            )

    for key in ("sector_orientations", "c6_left_representative_labels"):
        if entry.get(key) != expected[key]:
            failures.append(f"branch_packet.{key} does not match {branch}")

    if entry.get("selected_branch_claimed_by_residual_solution") is not True:
        failures.append(
            "branch_packet.selected_branch_claimed_by_residual_solution must be true"
        )
    if entry.get("antiunitary_conjugate_retained_for_comparison") is not True:
        failures.append(
            "branch_packet.antiunitary_conjugate_retained_for_comparison must be true"
        )
    if entry.get("dotD_same_branch_derivative_required") is not True:
        failures.append("branch_packet.dotD_same_branch_derivative_required must be true")

    return failures


def validate_candidate(data: dict[str, Any]) -> list[str]:
    if data.get("status") == "OPEN":
        raise IncompleteData("Route C residual certificate is OPEN")
    if data.get("mesh_N") is None:
        raise IncompleteData("MISSING mesh_N")
    if not isinstance(data.get("mesh_N"), int) or data["mesh_N"] < 1:
        raise ValueError("mesh_N must be a positive integer")

    failures: list[str] = []
    failures.extend(require_bool(data, "selected_source_verified", True))
    failures.extend(require_bool(data, "no_observed_flavor_inputs", True))
    failures.extend(require_bool(data, "uses_execution_ii_benchmarks", False))
    failures.extend(require_bool(data, "uses_diagnostic_h1_three_as_selected", False))
    failures.extend(validate_branch_packet(data.get("branch_packet")))

    residuals = data.get("residuals")
    if not isinstance(residuals, dict):
        raise IncompleteData("MISSING residuals object")
    for name in REQUIRED_RESIDUALS:
        failures.extend(validate_residual(name, residuals.get(name)))

    positive_gates = data.get("positive_gates")
    if not isinstance(positive_gates, dict):
        raise IncompleteData("MISSING positive_gates object")
    for name in REQUIRED_POSITIVE_GATES:
        failures.extend(validate_positive_gate(name, positive_gates.get(name)))

    downstream = data.get("downstream_data_paths")
    if not isinstance(downstream, dict):
        raise IncompleteData("MISSING downstream_data_paths object")
    for key in (
        "rhoE_mesh",
        "rhoE_metric",
        "sector_maps",
        "de_action",
        "riesz_gap",
        "reduced_green",
        "dotd_response",
    ):
        if not isinstance(downstream.get(key), str) or not downstream[key]:
            failures.append(f"downstream_data_paths.{key} must be a nonempty path string")

    return failures


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_iwasawa_route_c_residuals.py <route-c-residuals.json>")
        return 1

    try:
        data = json.loads(Path(argv[1]).read_text(encoding="utf-8"))
        failures = validate_candidate(data)
    except IncompleteData as exc:
        print(str(exc))
        return 2
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"INVALID Route C residual certificate: {exc}")
        return 1

    if failures:
        print("Route C residual validation FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Route C residual validation PASS")
    print("source residuals, positivity gates, and guardrails are consistent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
