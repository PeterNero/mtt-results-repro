"""Compute the character-trivial CKM heavy-link vector Delta_t from C1 data.

This is a reduced calculator for the leading CKM gate.  It only needs the
heavy-link entries (13,23) of the selected C1 primitive contractions in the up
and down sectors, not the full 3x3 primitive matrices.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


SECTORS = ("u", "d")
TERMS = (
    "theta_overlap_variation",
    "left_zero_mode_response",
    "right_zero_mode_response",
    "higgs_zero_mode_response",
    "explicit_vertex",
    "basis_connection",
)
TOL = 1e-12


class MissingC1HeavyLinkData(ValueError):
    """Raised when selected C1 heavy-link primitive data are incomplete."""

    def __init__(self, missing: list[str]) -> None:
        self.missing = missing
        super().__init__("\n".join(missing))


def parse_scalar(value: Any, path: str) -> complex:
    if value is None:
        raise MissingC1HeavyLinkData([path])
    if isinstance(value, bool):
        raise TypeError(f"{path}: booleans are not valid numeric entries")
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
    raise TypeError(f"{path}: unsupported scalar entry {value!r}")


def parse_vector(value: Any, path: str) -> list[complex]:
    if value is None:
        raise MissingC1HeavyLinkData([path])
    if not isinstance(value, list) or len(value) != 2:
        raise TypeError(f"{path} must be [entry_13, entry_23]")

    parsed: list[complex] = []
    missing: list[str] = []
    for index, entry in enumerate(value):
        entry_path = f"{path}[{index}]"
        try:
            parsed.append(parse_scalar(entry, entry_path))
        except MissingC1HeavyLinkData as exc:
            missing.extend(exc.missing)
    if missing:
        raise MissingC1HeavyLinkData(missing)
    return parsed


def vector_add(left: list[complex], right: list[complex]) -> list[complex]:
    return [a + b for a, b in zip(left, right)]


def vector_sub(left: list[complex], right: list[complex]) -> list[complex]:
    return [a - b for a, b in zip(left, right)]


def nonzero(vector: list[complex]) -> bool:
    return any(abs(entry) > TOL for entry in vector)


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


def compute(data: dict[str, Any]) -> dict[str, Any]:
    sectors = data.get("sectors", {})
    missing: list[str] = []
    primitive_vectors: dict[str, dict[str, list[complex]]] = {}
    totals = {sector: [0j, 0j] for sector in SECTORS}

    for sector in SECTORS:
        sector_data = sectors.get(sector)
        if not isinstance(sector_data, dict):
            missing.append(f"sectors.{sector}")
            continue
        primitive_vectors[sector] = {}
        for term in TERMS:
            path = f"sectors.{sector}.{term}"
            try:
                vector = parse_vector(sector_data.get(term), path)
            except MissingC1HeavyLinkData as exc:
                missing.extend(exc.missing)
                continue
            primitive_vectors[sector][term] = vector
            totals[sector] = vector_add(totals[sector], vector)

    if missing:
        raise MissingC1HeavyLinkData(missing)

    delta_t = vector_sub(totals["d"], totals["u"])
    return {
        "calculation": "C1HeavyLinkDeltaT",
        "primitive_vectors": primitive_vectors,
        "t_u": totals["u"],
        "t_d": totals["d"],
        "Delta_t": delta_t,
        "character_trivial_leading_noncommutation_pass": nonzero(delta_t),
        "guardrails": {
            "computes_C6_support": False,
            "computes_Jarlskog": False,
            "computes_CKM_angle_magnitudes": False,
            "claims_full_SM_closure": False,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON selected C1 heavy-link primitive packet")
    args = parser.parse_args()

    data = json.loads(args.input.read_text(encoding="utf-8"))
    try:
        output = compute(data)
    except MissingC1HeavyLinkData as exc:
        print("missing selected C1 heavy-link data")
        print("===================================")
        for item in exc.missing:
            print(f"- {item}")
        return 2

    print(json.dumps(encode(output), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
