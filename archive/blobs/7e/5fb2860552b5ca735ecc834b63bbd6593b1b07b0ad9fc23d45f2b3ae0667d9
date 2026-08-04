"""Validate a future selected visible Green-Schwarz curvature packet.

This validator is intentionally narrow.  It checks a coefficient-level
Bianchi equation in a declared finite curvature basis after all coefficients
have already been supplied by a selected same-branch source.
"""

from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


SCHEMA = "TimeOrientedM1VisibleGreenSchwarzCurvature.v1"
EXPECTED_FLAT_GERBE_CERT = "time_oriented_m1_flat_gerbe_promotion_certificate.json"
EXPECTED_GS_GATE_CERT = "time_oriented_m1_green_schwarz_gate_certificate.json"
EXPECTED_REQUIREMENT_CERT = "time_oriented_m1_visible_green_schwarz_requirement_certificate.json"
ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def fraction(value: Any) -> Fraction:
    if isinstance(value, bool):
        raise ValueError("booleans are not numeric coefficients")
    if isinstance(value, int):
        return Fraction(value, 1)
    if isinstance(value, str):
        return Fraction(value)
    raise ValueError(f"unsupported coefficient {value!r}")


def coefficient_vector(packet: dict[str, Any], key: str, length: int) -> list[Fraction]:
    values = packet.get(key)
    if not isinstance(values, list) or len(values) != length:
        raise ValueError(f"{key} must be a list of length {length}")
    return [fraction(value) for value in values]


def symbolic_vectors_match_requirement(packet: dict[str, Any], length: int) -> tuple[bool, list[str]]:
    messages: list[str] = []
    if packet.get("symbolic_row_source_certificate") != EXPECTED_REQUIREMENT_CERT:
        messages.append(f"symbolic_row_source_certificate must be {EXPECTED_REQUIREMENT_CERT}")
        return False, messages
    requirement = load_json(ROOT / "certificates" / EXPECTED_REQUIREMENT_CERT)
    required_rows = {
        "dH_coefficients": requirement.get("known_rows", {}).get("dH"),
        "tr_R_plus_squared_coefficients": requirement.get("known_rows", {}).get(
            "Tr_R_plus_squared"
        ),
        "tr_F_visible_squared_coefficients": requirement.get(
            "derived_required_visible_row", {}
        ).get("Tr_F_visible_squared"),
        "bianchi_residual_coefficients": requirement.get(
            "derived_required_visible_row", {}
        ).get("residual_if_supplied"),
    }
    for key, expected in required_rows.items():
        actual = packet.get(key)
        if not isinstance(actual, list) or len(actual) != length:
            messages.append(f"{key} must be a list of length {length}")
        elif actual != expected:
            messages.append(f"{key} must match {EXPECTED_REQUIREMENT_CERT}")
    return not messages, messages


def validate(packet: dict[str, Any]) -> tuple[int, list[str]]:
    messages: list[str] = []
    if packet.get("schema") != SCHEMA:
        messages.append(f"schema must be {SCHEMA}")
    if packet.get("status") == "OPEN":
        messages.append("packet is OPEN; fill selected same-branch curvature coefficients first")
        return 2, messages

    required_true = [
        "selected_by_mtt",
        "same_branch_as_q79_m1",
        "alpha_prime_over_4_absorbed",
        "flat_m1_torsion_curvature_zero",
        "bianchi_residual_zero",
    ]
    for key in required_true:
        if packet.get(key) is not True:
            messages.append(f"{key} must be true")

    for key in ("uses_observed_flavor_data", "uses_benchmark_flavor_entries"):
        if packet.get(key) is not False:
            messages.append(f"{key} must be false")

    if packet.get("flat_gerbe_certificate") != EXPECTED_FLAT_GERBE_CERT:
        messages.append(f"flat_gerbe_certificate must be {EXPECTED_FLAT_GERBE_CERT}")
    if packet.get("green_schwarz_gate_certificate") != EXPECTED_GS_GATE_CERT:
        messages.append(f"green_schwarz_gate_certificate must be {EXPECTED_GS_GATE_CERT}")

    basis = packet.get("curvature_basis")
    if not isinstance(basis, list) or not basis or not all(isinstance(item, str) for item in basis):
        messages.append("curvature_basis must be a nonempty list of names")
        return 1, messages

    if packet.get("coefficient_domain") == "symbolic_iwasawa_alpha_rows":
        ok, symbolic_messages = symbolic_vectors_match_requirement(packet, len(basis))
        messages.extend(symbolic_messages)
    else:
        try:
            dH = coefficient_vector(packet, "dH_coefficients", len(basis))
            tr_r = coefficient_vector(packet, "tr_R_plus_squared_coefficients", len(basis))
            tr_f = coefficient_vector(packet, "tr_F_visible_squared_coefficients", len(basis))
            claimed = coefficient_vector(packet, "bianchi_residual_coefficients", len(basis))
        except ValueError as exc:
            messages.append(str(exc))
            return 1, messages

        computed = [dH_i - (r_i - f_i) for dH_i, r_i, f_i in zip(dH, tr_r, tr_f)]
        if computed != claimed:
            messages.append(
                "bianchi_residual_coefficients must equal dH - (TrRplus^2 - TrFvisible^2)"
            )
        if any(value != 0 for value in computed):
            messages.append(f"Bianchi residual is nonzero: {[str(value) for value in computed]}")

    source_cert = packet.get("selected_visible_source_certificate")
    if not isinstance(source_cert, str) or not source_cert.endswith(".json"):
        messages.append("selected_visible_source_certificate must name a selected source certificate")

    return (0 if not messages else 1), messages


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    code, messages = validate(load_json(args.packet))
    if code == 0:
        print("visible Green-Schwarz curvature PASS")
    else:
        print("visible Green-Schwarz curvature NOT CLOSED")
        for message in messages:
            print(f"- {message}")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
