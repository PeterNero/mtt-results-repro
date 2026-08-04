"""Compute finite C1 response matrices from selected primitive contractions.

The script deliberately refuses incomplete primitive data. It is a calculator,
not a source of physics input.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


SECTORS = ("u", "d", "e", "nuD")
TERMS = (
    "theta_overlap_variation",
    "left_zero_mode_response",
    "right_zero_mode_response",
    "higgs_zero_mode_response",
    "explicit_vertex",
    "basis_connection",
)


class MissingPrimitiveData(ValueError):
    """Raised when the selected primitive contraction data are incomplete."""

    def __init__(self, missing: list[str]) -> None:
        self.missing = missing
        super().__init__("\n".join(missing))


def parse_scalar(value: Any) -> complex:
    if isinstance(value, bool):
        raise TypeError("booleans are not valid numeric matrix entries")
    if isinstance(value, (int, float)):
        return complex(value)
    if isinstance(value, str):
        return complex(value.replace("i", "j"))
    if (
        isinstance(value, list)
        and len(value) == 2
        and all(isinstance(part, (int, float)) for part in value)
    ):
        return complex(float(value[0]), float(value[1]))
    raise TypeError(f"unsupported scalar entry: {value!r}")


def parse_matrix(value: Any, path: str) -> list[list[complex]]:
    if value is None:
        raise MissingPrimitiveData([path])
    if not isinstance(value, list) or len(value) != 3:
        raise TypeError(f"{path} must be a 3x3 matrix")
    matrix: list[list[complex]] = []
    for row_index, row in enumerate(value):
        if not isinstance(row, list) or len(row) != 3:
            raise TypeError(f"{path}[{row_index}] must have three entries")
        matrix.append([parse_scalar(entry) for entry in row])
    return matrix


def zero_matrix() -> list[list[complex]]:
    return [[0j for _ in range(3)] for _ in range(3)]


def add_matrix(left: list[list[complex]], right: list[list[complex]]) -> list[list[complex]]:
    return [
        [left[row][col] + right[row][col] for col in range(3)]
        for row in range(3)
    ]


def c33(matrix: list[list[complex]]) -> complex:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def det3(matrix: list[list[complex]]) -> complex:
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def compute_response(data: dict[str, Any]) -> dict[str, list[list[complex]]]:
    sectors = data.get("sectors", data)
    missing: list[str] = []
    result: dict[str, list[list[complex]]] = {}

    for sector in SECTORS:
        sector_data = sectors.get(sector)
        if not isinstance(sector_data, dict):
            missing.append(f"sectors.{sector}")
            continue

        total = zero_matrix()
        for term in TERMS:
            path = f"sectors.{sector}.{term}"
            try:
                total = add_matrix(total, parse_matrix(sector_data.get(term), path))
            except MissingPrimitiveData as exc:
                missing.extend(exc.missing)
        result[sector] = total

    if missing:
        raise MissingPrimitiveData(missing)
    return result


def summarize(matrices: dict[str, list[list[complex]]]) -> dict[str, Any]:
    tests: dict[str, Any] = {
        f"C33_M_{sector}": c33(matrix)
        for sector, matrix in matrices.items()
    }
    if "u" in matrices and "d" in matrices:
        tests["Delta_v_ud"] = [
            matrices["d"][0][2] - matrices["u"][0][2],
            matrices["d"][1][2] - matrices["u"][1][2],
        ]
    tests["det_M"] = {sector: det3(matrix) for sector, matrix in matrices.items()}
    return tests


def encode_scalar(value: complex) -> float | list[float]:
    real = 0.0 if abs(value.real) < 1e-12 else value.real
    imag = 0.0 if abs(value.imag) < 1e-12 else value.imag
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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON file with selected primitive contractions")
    args = parser.parse_args()

    data = json.loads(args.input.read_text(encoding="utf-8"))
    try:
        matrices = compute_response(data)
    except MissingPrimitiveData as exc:
        print("missing primitive contraction data")
        print("==================================")
        for item in exc.missing:
            print(f"- {item}")
        return 2

    output = {
        "computed_matrices": {f"M_{sector}_C1_alpha1": matrix for sector, matrix in matrices.items()},
        "computed_tests": summarize(matrices),
    }
    print(json.dumps(encode(output), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
