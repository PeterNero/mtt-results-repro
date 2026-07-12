"""Compute the selected local determinant response from gauge-sector spectra.

The input is a selected, finite or zeta-regularized spectral table for the
three gauge factors.  This script performs only the determinant accounting:

    p_a = sum_j multiplicity_j * index_weight_j * log(lambda_j / mu^2)

It is deliberately not a spectrum generator.  If the selected spectra are not
present, it refuses to return a physics number.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any


FACTORS = ("U1", "SU2", "SU3")


class MissingSpectrumData(ValueError):
    """Raised when the selected determinant spectra are incomplete."""

    def __init__(self, missing: list[str]) -> None:
        self.missing = missing
        super().__init__("\n".join(missing))


def parse_positive(value: Any, path: str) -> float:
    if value is None:
        raise MissingSpectrumData([path])
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{path} must be a positive real number")
    number = float(value)
    if not math.isfinite(number) or number <= 0.0:
        raise ValueError(f"{path} must be positive and finite")
    return number


def parse_real(value: Any, path: str) -> float:
    if value is None:
        raise MissingSpectrumData([path])
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{path} must be a real number")
    number = float(value)
    if not math.isfinite(number):
        raise ValueError(f"{path} must be finite")
    return number


def parse_modes(value: Any, path: str) -> list[dict[str, float]]:
    if value is None:
        raise MissingSpectrumData([path])
    if not isinstance(value, list) or not value:
        raise TypeError(f"{path} must be a nonempty list of spectral modes")

    modes: list[dict[str, float]] = []
    for index, mode in enumerate(value):
        mode_path = f"{path}[{index}]"
        if not isinstance(mode, dict):
            raise TypeError(f"{mode_path} must be an object")
        modes.append(
            {
                "eigenvalue": parse_positive(mode.get("eigenvalue"), f"{mode_path}.eigenvalue"),
                "multiplicity": parse_real(mode.get("multiplicity", 1.0), f"{mode_path}.multiplicity"),
                "index_weight": parse_real(mode.get("index_weight"), f"{mode_path}.index_weight"),
            }
        )
    return modes


def trace_free(raw: list[float]) -> list[float]:
    mean = sum(raw) / 3.0
    return [entry - mean for entry in raw]


def factor_response(modes: list[dict[str, float]], reference_scale_squared: float) -> float:
    total = 0.0
    for mode in modes:
        total += (
            mode["multiplicity"]
            * mode["index_weight"]
            * math.log(mode["eigenvalue"] / reference_scale_squared)
        )
    return total


def compute(data: dict[str, Any]) -> dict[str, Any]:
    determinant = data.get("selected_local_determinant", {})
    reference_scale_squared = parse_positive(
        determinant.get("reference_scale_squared"),
        "selected_local_determinant.reference_scale_squared",
    )
    spectra = determinant.get("gauge_factor_spectra", {})

    missing: list[str] = []
    raw: list[float] = []
    mode_counts: dict[str, int] = {}
    for factor in FACTORS:
        path = f"selected_local_determinant.gauge_factor_spectra.{factor}"
        try:
            modes = parse_modes(spectra.get(factor), path)
        except MissingSpectrumData as exc:
            missing.extend(exc.missing)
            continue
        raw.append(factor_response(modes, reference_scale_squared))
        mode_counts[factor] = len(modes)

    if missing:
        raise MissingSpectrumData(missing)

    projected = trace_free(raw)
    return {
        "local_determinant_response_per_v1": dict(zip(FACTORS, raw)),
        "trace_free_response_per_v1": dict(zip(FACTORS, projected)),
        "lambda_12": raw[0] - raw[1],
        "mode_counts": mode_counts,
        "checks": {
            "trace_free_sum": sum(projected),
            "lambda_12_equals_raw_U1_minus_SU2": (raw[0] - raw[1]) - (projected[0] - projected[1]),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON file with selected determinant spectra")
    args = parser.parse_args()

    data = json.loads(args.input.read_text(encoding="utf-8"))
    try:
        output = compute(data)
    except MissingSpectrumData as exc:
        print("missing selected local determinant spectrum data")
        print("================================================")
        for item in exc.missing:
            print(f"- {item}")
        return 2

    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
