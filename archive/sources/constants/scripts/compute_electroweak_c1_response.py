"""Compute the selected electroweak C1 response map from primitive data.

The input supplies raw per-v1 electroweak threshold response vectors.  The
calculator removes the universal trace, converts the trace-free vector to the
selected (chi1, chi2) basis, and reports the weak 1-2 split.

It deliberately refuses null primitive terms.  This script is a calculator, not
a source of physics input.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any


FACTORS = ("U1", "SU2", "SU3")
TERMS = (
    "local_determinant",
    "torsion_curvature",
    "bundle_index",
    "scheme_counterterm",
    "basis_transport",
)


class MissingPrimitiveData(ValueError):
    """Raised when selected electroweak threshold primitives are incomplete."""

    def __init__(self, missing: list[str]) -> None:
        self.missing = missing
        super().__init__("\n".join(missing))


def parse_scalar(value: Any, path: str) -> float:
    if value is None:
        raise MissingPrimitiveData([path])
    if isinstance(value, bool):
        raise TypeError(f"{path} cannot be boolean")
    if isinstance(value, (int, float)):
        return float(value)
    raise TypeError(f"{path} must be a real number")


def parse_vector(value: Any, path: str) -> list[float]:
    if value is None:
        raise MissingPrimitiveData([path])
    if not isinstance(value, list) or len(value) != 3:
        raise TypeError(f"{path} must be a three-entry vector")
    return [parse_scalar(entry, f"{path}[{idx}]") for idx, entry in enumerate(value)]


def add(left: list[float], right: list[float]) -> list[float]:
    return [a + b for a, b in zip(left, right)]


def trace_free(raw: list[float]) -> list[float]:
    mean = sum(raw) / 3.0
    return [entry - mean for entry in raw]


def compute(data: dict[str, Any]) -> dict[str, Any]:
    selected = data.get("selected_values", {})
    v1_tilde = parse_scalar(selected.get("v1_tilde"), "selected_values.v1_tilde")

    primitives = data.get("raw_response_per_v1", {}).get("terms", {})
    missing: list[str] = []
    raw = [0.0, 0.0, 0.0]
    for term in TERMS:
        path = f"raw_response_per_v1.terms.{term}"
        try:
            raw = add(raw, parse_vector(primitives.get(term), path))
        except MissingPrimitiveData as exc:
            missing.extend(exc.missing)

    if missing:
        raise MissingPrimitiveData(missing)

    projected = trace_free(raw)
    m1 = projected[0]
    m2 = -projected[2]
    lambda_12 = projected[0] - projected[1]
    c1 = v1_tilde * m1
    c2 = v1_tilde * m2
    delta_g_12 = v1_tilde * lambda_12 / (4.0 * math.pi)

    return {
        "raw_response_per_v1": dict(zip(FACTORS, raw)),
        "trace_free_response_per_v1": dict(zip(FACTORS, projected)),
        "P_EW_alpha1": {"m1": m1, "m2": m2},
        "lambda_12": lambda_12,
        "c_coefficients": {"c1": c1, "c2": c2},
        "Delta_G_12": delta_g_12,
        "checks": {
            "trace_free_sum": sum(projected),
            "lambda_12_equals_raw_U1_minus_SU2": lambda_12 - (raw[0] - raw[1]),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON file with selected electroweak C1 primitive response")
    args = parser.parse_args()

    data = json.loads(args.input.read_text(encoding="utf-8"))
    try:
        output = compute(data)
    except MissingPrimitiveData as exc:
        print("missing electroweak C1 primitive response data")
        print("================================================")
        for item in exc.missing:
            print(f"- {item}")
        return 2

    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

