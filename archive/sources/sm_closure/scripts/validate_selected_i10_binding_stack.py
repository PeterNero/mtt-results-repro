"""Validate selected I10/I1/I5 binding-stack packets."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = [
    "selected_minimizer_trace_payload_verified",
    "selected_c1_response_payload_verified",
    "defect_functional_minimizer_payload_verified",
    "first_variation_identity_verified",
    "hessian_or_coercivity_verified",
    "boundary_cancellation_verified",
    "normalization_compatibility_verified",
]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def evidence_count(packet: dict[str, Any]) -> int:
    evidence = packet.get("attached_binding_evidence", [])
    return len(evidence) if isinstance(evidence, list) else 0


def validate(packet: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if packet.get("observed_data_used_as_selector") is not False:
        errors.append("observed_data_used_as_selector must be false")
    if packet.get("target_fitting_used") is not False:
        errors.append("target_fitting_used must be false")
    if packet.get("benchmark_or_measured_values_used_as_source") is not False:
        errors.append("benchmark_or_measured_values_used_as_source must be false")
    if packet.get("free_axiom_patch_used") is not False:
        errors.append("free_axiom_patch_used must be false")
    if packet.get("same_branch") is not True:
        errors.append("same_branch must be true")

    missing = [field for field in REQUIRED_FIELDS if packet.get(field) is not True]
    if missing:
        errors.append("missing I10 binding fields: " + ", ".join(missing))
    if evidence_count(packet) < 7:
        errors.append("at least seven binding evidence entries are required")
    return not errors, errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_selected_i10_binding_stack.py <packet.json>", file=sys.stderr)
        return 2
    ok, errors = validate(load(Path(argv[1])))
    if ok:
        print(f"PASS {argv[1]}")
        return 0
    for error in errors:
        print(f"ERROR {error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
