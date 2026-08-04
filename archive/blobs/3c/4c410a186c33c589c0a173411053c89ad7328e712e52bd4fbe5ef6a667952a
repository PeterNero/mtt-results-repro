"""Compute the hypercharge-normalized electroweak threshold split.

The selected hypercharge embedding used here is

    Y = (1/6) Q_a - (1/2) Q_c,

so determinant / inverse-coupling threshold pieces combine as

    p_Y = (1/36) p_a + (1/4) p_c.

This script performs only the accounting.  It refuses to compute when the
selected determinant inputs are absent.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any


class MissingHyperchargeData(ValueError):
    """Raised when required selected threshold entries are missing."""

    def __init__(self, missing: list[str]) -> None:
        self.missing = missing
        super().__init__("\n".join(missing))


def parse_real(value: Any, path: str) -> float:
    if value is None:
        raise MissingHyperchargeData([path])
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{path} must be a real number")
    number = float(value)
    if not math.isfinite(number):
        raise ValueError(f"{path} must be finite")
    return number


def compute(data: dict[str, Any]) -> dict[str, Any]:
    threshold = data.get("selected_hypercharge_normalized_threshold", {})
    missing: list[str] = []

    def required(path: str) -> float | None:
        current: Any = threshold
        for part in path.split("."):
            if not isinstance(current, dict) or part not in current:
                missing.append(f"selected_hypercharge_normalized_threshold.{path}")
                return None
            current = current[part]
        try:
            return parse_real(current, f"selected_hypercharge_normalized_threshold.{path}")
        except MissingHyperchargeData as exc:
            missing.extend(exc.missing)
            return None

    p_a = required("stack_thresholds.Qa_SU3_stack")
    p_c = required("stack_thresholds.Qc_circle_stack")
    p_su2 = required("stack_thresholds.SU2_stack")
    v1_tilde = required("selected_values.v1_tilde")

    if missing:
        raise MissingHyperchargeData(missing)

    assert p_a is not None
    assert p_c is not None
    assert p_su2 is not None
    assert v1_tilde is not None

    p_y = (p_a / 36.0) + (p_c / 4.0)
    lambda_12 = p_y - p_su2
    delta_g_12 = v1_tilde * lambda_12 / (4.0 * math.pi)

    return {
        "hypercharge_threshold": {
            "p_Y": p_y,
            "formula": "p_Y = p_a/36 + p_c/4",
            "inputs": {
                "p_a": p_a,
                "p_c": p_c,
                "p_SU2": p_su2,
            },
        },
        "weak_split": {
            "lambda_12": lambda_12,
            "Delta_G_12": delta_g_12,
            "formula": "lambda_12 = p_Y - p_SU2",
        },
        "embedding": {
            "Y": "Y = (1/6) Q_a - (1/2) Q_c",
            "threshold_combination": "p_Y = (1/36) p_a + (1/4) p_c",
        },
        "checks": {
            "lambda_12_equals_pY_minus_pSU2": lambda_12 - (p_y - p_su2),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON file with selected hypercharge threshold data")
    args = parser.parse_args()

    data = json.loads(args.input.read_text(encoding="utf-8"))
    try:
        output = compute(data)
    except MissingHyperchargeData as exc:
        print("missing selected hypercharge-normalized threshold data")
        print("=======================================================")
        for item in exc.missing:
            print(f"- {item}")
        return 2

    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
