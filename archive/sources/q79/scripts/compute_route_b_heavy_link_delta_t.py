"""Compute Route B CKM heavy-link Delta_t from selected overlap differences.

This calculator is the executable interface for the five-slot Route B closure
packet identified by scripts/attempt_dual_route_closure.py.

It does not source the five complex numbers.  It only checks that a packet
claims a selected no-proxy source and then evaluates the finite linear map:

    Delta_t = A * selected_overlap_differences + selected_extra_delta_terms
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEPENDENCY = ROOT / "candidate_data" / "dual_route_closure_attempt.candidate.json"
SCHEMA = "RouteBHeavyLinkOverlapDifferencePacket.v1"
BRANCHES = {"current_q79_orientation", "conjugate_q369_orientation"}
VARIABLES = (
    "A_left_delta",
    "B_right_row1_delta",
    "B_right_row2_delta",
    "C_higgs_row1_delta",
    "C_higgs_row2_delta",
)
EXTRA_TERMS = (
    "theta_overlap_variation_delta",
    "explicit_vertex_delta",
    "basis_connection_delta",
)
TOL = 1e-12


class MissingRouteBData(ValueError):
    def __init__(self, missing: list[str]) -> None:
        self.missing = missing
        super().__init__("\n".join(missing))


def parse_complex(value: Any, path: str) -> complex:
    if value is None:
        raise MissingRouteBData([path])
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return complex(value)
    if isinstance(value, str):
        return complex(value.replace("i", "j"))
    if (
        isinstance(value, list)
        and len(value) == 2
        and all(isinstance(part, (int, float)) and not isinstance(part, bool) for part in value)
    ):
        return complex(float(value[0]), float(value[1]))
    raise TypeError(f"{path}: invalid complex entry {value!r}")


def parse_vector(value: Any, path: str) -> list[complex]:
    if value is None:
        raise MissingRouteBData([path])
    if not isinstance(value, list) or len(value) != 2:
        raise TypeError(f"{path} must be a two-entry vector")
    missing: list[str] = []
    parsed: list[complex] = []
    for index, entry in enumerate(value):
        try:
            parsed.append(parse_complex(entry, f"{path}[{index}]"))
        except MissingRouteBData as exc:
            missing.extend(exc.missing)
    if missing:
        raise MissingRouteBData(missing)
    return parsed


def encode_scalar(value: complex) -> float | list[float]:
    real = 0.0 if abs(value.real) < TOL else value.real
    imag = 0.0 if abs(value.imag) < TOL else value.imag
    if imag == 0.0:
        return real
    return [real, imag]


def encode(value: Any) -> Any:
    if isinstance(value, complex):
        return encode_scalar(value)
    if isinstance(value, list):
        return [encode(item) for item in value]
    if isinstance(value, dict):
        return {key: encode(item) for key, item in value.items()}
    return value


def load_coefficients(branch: str) -> list[list[complex]]:
    data = json.loads(DEPENDENCY.read_text(encoding="utf-8"))
    rows = (
        data["routes"]["B_block_factorized_sector_resolved_C1"]["branches"][branch][
            "coefficient_matrix_rows_Delta13_Delta23"
        ]
    )
    return [[parse_complex(entry, "coefficient") for entry in row] for row in rows]


def validate_source(data: dict[str, Any]) -> tuple[bool, list[str]]:
    source = data.get("source")
    if not isinstance(source, dict):
        raise MissingRouteBData(["source"])

    failures: list[str] = []
    selected = source.get("selected_by_mtt") is True
    if source.get("uses_observed_flavor_data") is not False:
        failures.append("source.uses_observed_flavor_data must be false")
    if source.get("uses_benchmark_flavor_entries") is not False:
        failures.append("source.uses_benchmark_flavor_entries must be false")
    if source.get("selected_by_mtt") is not True and data.get("candidate_role") == "SELECTED_DATA":
        failures.append("SELECTED_DATA requires source.selected_by_mtt=true")
    if data.get("candidate_role") == "UNSELECTED_FIXTURE" and source.get("selected_by_mtt") is not False:
        failures.append("UNSELECTED_FIXTURE requires source.selected_by_mtt=false")
    return selected and not failures, failures


def compute(data: dict[str, Any]) -> tuple[dict[str, Any], list[str]]:
    if data.get("status") == "OPEN":
        raise MissingRouteBData(["packet status is OPEN"])
    if data.get("schema") != SCHEMA:
        raise ValueError(f"schema must be {SCHEMA}")
    if data.get("candidate_role") not in {"SELECTED_DATA", "UNSELECTED_FIXTURE"}:
        raise ValueError("candidate_role must be SELECTED_DATA or UNSELECTED_FIXTURE")
    branch = data.get("branch")
    if branch not in BRANCHES:
        raise ValueError(f"branch must be one of {sorted(BRANCHES)}")

    source_selected, failures = validate_source(data)
    differences = data.get("overlap_differences")
    extras = data.get("extra_delta_t_terms")
    if not isinstance(differences, dict):
        raise MissingRouteBData(["overlap_differences"])
    if not isinstance(extras, dict):
        raise MissingRouteBData(["extra_delta_t_terms"])

    missing: list[str] = []
    values: list[complex] = []
    for key in VARIABLES:
        try:
            values.append(parse_complex(differences.get(key), f"overlap_differences.{key}"))
        except MissingRouteBData as exc:
            missing.extend(exc.missing)

    extra_total = [0j, 0j]
    parsed_extras: dict[str, list[complex]] = {}
    for key in EXTRA_TERMS:
        try:
            vector = parse_vector(extras.get(key), f"extra_delta_t_terms.{key}")
        except MissingRouteBData as exc:
            missing.extend(exc.missing)
            continue
        parsed_extras[key] = vector
        extra_total = [a + b for a, b in zip(extra_total, vector)]

    if missing:
        raise MissingRouteBData(missing)

    matrix = load_coefficients(branch)
    overlap_delta = [sum(row[col] * values[col] for col in range(len(values))) for row in matrix]
    delta_t = [a + b for a, b in zip(overlap_delta, extra_total)]
    report = {
        "calculation": "RouteBHeavyLinkDeltaT",
        "branch": branch,
        "candidate_role": data.get("candidate_role"),
        "source_selected_by_mtt": source_selected,
        "difference_variables": list(VARIABLES),
        "overlap_differences": dict(zip(VARIABLES, values)),
        "coefficient_matrix_rows_Delta13_Delta23": matrix,
        "overlap_only_Delta_t": overlap_delta,
        "extra_delta_t_terms": parsed_extras,
        "extra_delta_t_total": extra_total,
        "Delta_t": delta_t,
        "leading_noncommutation_structurally_nonzero": any(abs(entry) > TOL for entry in delta_t),
        "promotes_to_selected_CKM_heavy_link_input": (
            source_selected
            and data.get("candidate_role") == "SELECTED_DATA"
            and any(abs(entry) > TOL for entry in delta_t)
            and not failures
        ),
        "guardrails": {
            "uses_observed_flavor_data": data.get("source", {}).get("uses_observed_flavor_data"),
            "uses_benchmark_flavor_entries": data.get("source", {}).get(
                "uses_benchmark_flavor_entries"
            ),
            "claims_yukawa_magnitudes": False,
            "claims_full_SM_closure": False,
        },
    }
    return report, failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Route B overlap-difference packet")
    args = parser.parse_args()

    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        report, failures = compute(data)
    except MissingRouteBData as exc:
        print("missing Route B heavy-link overlap data")
        print("=======================================")
        for item in exc.missing:
            print(f"- {item}")
        return 2
    except (OSError, json.JSONDecodeError, TypeError, ValueError) as exc:
        print(f"INVALID Route B heavy-link packet: {exc}")
        return 1

    print(json.dumps(encode(report), indent=2, sort_keys=True))
    if failures:
        print("Route B heavy-link packet FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("Route B heavy-link packet PASS")
    if report["promotes_to_selected_CKM_heavy_link_input"]:
        print("packet promotes selected Route B Delta_t")
    else:
        print("packet is algebraically computable but not selected CKM input")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
