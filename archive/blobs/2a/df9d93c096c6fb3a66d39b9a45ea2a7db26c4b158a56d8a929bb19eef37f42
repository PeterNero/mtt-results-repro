"""Validate selected physical boundary/first-variation source-emission packets."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = [
    "physical_first_variation_identity",
    "physical_measure_equals_trace_frobenius_pairing",
    "phase_R_Z_source_selection",
    "shift_R_X_source_selection",
    "same_source_b_selected_emission",
    "no_extra_physical_boundary_or_source_term",
]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def evidence_count(packet: dict[str, Any]) -> int:
    evidence = packet.get("attached_source_evidence", [])
    return len(evidence) if isinstance(evidence, list) else 0


def validate(packet: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if packet.get("observed_data_used_as_selector") is not False:
        errors.append("observed_data_used_as_selector must be false")
    if packet.get("target_fitting_used") is not False:
        errors.append("target_fitting_used must be false")
    if packet.get("locked_target_values_used_as_source") is not False:
        errors.append("locked_target_values_used_as_source must be false")
    if packet.get("residual_projector_replay_used_as_source") is not False:
        errors.append("residual_projector_replay_used_as_source must be false")
    if packet.get("benchmark_values_used_as_source") is not False:
        errors.append("benchmark_values_used_as_source must be false")
    if packet.get("same_branch") is not True:
        errors.append("same_branch must be true")
    if packet.get("theorem_derived") is not True:
        errors.append("theorem_derived must be true")

    missing = [field for field in REQUIRED_FIELDS if packet.get(field) is not True]
    if missing:
        errors.append("missing physical-source fields: " + ", ".join(missing))
    if evidence_count(packet) < 6:
        errors.append("attached_source_evidence must contain at least six sources")
    return not errors, errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_selected_physical_boundary_firstvariation_source.py <packet.json>", file=sys.stderr)
        return 2
    path = Path(argv[1])
    ok, errors = validate(load(path))
    if ok:
        print(f"PASS {path}")
        return 0
    for error in errors:
        print(f"ERROR {error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
