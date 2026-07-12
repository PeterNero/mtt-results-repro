"""Compute the leading CKM heavy-link gate from a selected support packet.

The packet supplies:

    t_u, t_d = character-trivial heavy-link vectors,
    c_u, c_d = selected C6 heavy-link vectors,
    chi_q    = selected q79 or conjugate C6 character.

The calculator evaluates:

    Delta_v = (t_d - t_u) + chi_q (c_d - c_u).

It refuses missing entries.  It is a calculator for selected data, not a source
of flavor input.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any


TOL = 1e-12


class MissingHeavyLinkData(ValueError):
    """Raised when the selected heavy-link packet is incomplete."""

    def __init__(self, missing: list[str]) -> None:
        self.missing = missing
        super().__init__("\n".join(missing))


def parse_scalar(value: Any, path: str) -> complex:
    if value is None:
        raise MissingHeavyLinkData([path])
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
        raise MissingHeavyLinkData([path])
    if not isinstance(value, list) or len(value) != 2:
        raise TypeError(f"{path} must be a two-entry heavy-link vector")

    parsed: list[complex] = []
    missing: list[str] = []
    for index, entry in enumerate(value):
        entry_path = f"{path}[{index}]"
        try:
            parsed.append(parse_scalar(entry, entry_path))
        except MissingHeavyLinkData as exc:
            missing.extend(exc.missing)
    if missing:
        raise MissingHeavyLinkData(missing)
    return parsed


def character(label: int, modulus: int) -> complex:
    angle = 2.0 * math.pi * label / modulus
    return complex(math.cos(angle), math.sin(angle))


def vector_sub(left: list[complex], right: list[complex]) -> list[complex]:
    return [a - b for a, b in zip(left, right)]


def vector_add(left: list[complex], right: list[complex]) -> list[complex]:
    return [a + b for a, b in zip(left, right)]


def vector_mul(scalar: complex, vector: list[complex]) -> list[complex]:
    return [scalar * entry for entry in vector]


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


def packet_entries(data: dict[str, Any]) -> tuple[list[complex], list[complex], list[complex], list[complex]]:
    inputs = data.get("inputs", {})
    trivial = inputs.get("character_trivial_heavy_link", {})
    c6 = inputs.get("c6_heavy_link", {})

    missing: list[str] = []
    parsed: dict[str, list[complex]] = {}
    paths = {
        "t_u": ("inputs.character_trivial_heavy_link.u.entries", trivial.get("u", {}).get("entries")),
        "t_d": ("inputs.character_trivial_heavy_link.d.entries", trivial.get("d", {}).get("entries")),
        "c_u": ("inputs.c6_heavy_link.u.entries", c6.get("u", {}).get("entries")),
        "c_d": ("inputs.c6_heavy_link.d.entries", c6.get("d", {}).get("entries")),
    }
    for key, (path, value) in paths.items():
        try:
            parsed[key] = parse_vector(value, path)
        except MissingHeavyLinkData as exc:
            missing.extend(exc.missing)

    if missing:
        raise MissingHeavyLinkData(missing)

    return parsed["t_u"], parsed["t_d"], parsed["c_u"], parsed["c_d"]


def compute(data: dict[str, Any]) -> dict[str, Any]:
    phase = data.get("phase_branch", {})
    modulus = int(phase.get("modulus", 448))
    selected_label = int(phase.get("selected_label", 79))
    chi_q = character(selected_label, modulus)
    t_u, t_d, c_u, c_d = packet_entries(data)

    delta_t = vector_sub(t_d, t_u)
    delta_c = vector_sub(c_d, c_u)
    c6_part = vector_mul(chi_q, delta_c)
    delta_v = vector_add(delta_t, c6_part)

    return {
        "calculation": "CKMHeavyLinkGate",
        "phase": {
            "modulus": modulus,
            "selected_label": selected_label,
            "chi_q": chi_q,
            "unit_modulus": abs(abs(chi_q) - 1.0) < TOL,
        },
        "inputs": {
            "t_u": t_u,
            "t_d": t_d,
            "c_u": c_u,
            "c_d": c_d,
        },
        "derived": {
            "Delta_t": delta_t,
            "Delta_c": delta_c,
            "chi_q_Delta_c": c6_part,
            "Delta_v": delta_v,
        },
        "gate": {
            "c6_affects_leading_gate": nonzero(delta_c),
            "leading_noncommutation_pass": nonzero(delta_v),
            "exact_cancellation_between_trivial_and_c6_parts": nonzero(delta_c)
            and not nonzero(delta_v),
            "condition": "Delta_v = Delta_t + chi_q Delta_c != (0,0)",
        },
        "guardrails": {
            "computes_jarlskog": False,
            "computes_ckm_angle_magnitudes": False,
            "computes_yukawa_magnitudes": False,
            "claims_full_sm_closure": False,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON selected heavy-link packet")
    args = parser.parse_args()

    data = json.loads(args.input.read_text(encoding="utf-8"))
    try:
        output = compute(data)
    except MissingHeavyLinkData as exc:
        print("missing selected heavy-link data")
        print("================================")
        for item in exc.missing:
            print(f"- {item}")
        return 2

    print(json.dumps(encode(output), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
