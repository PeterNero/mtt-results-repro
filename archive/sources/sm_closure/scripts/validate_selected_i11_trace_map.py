"""Validate selected I11 trace-map dynamic-extension packets."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = [
    "selected_minimizer_identifier",
    "finite_phi_fin_trace_operator",
    "c1_response_coordinate_map",
    "selected_normalization_boundary_clause",
    "dynamic_c1_flags_verified",
]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def evidence_count(packet: dict[str, Any]) -> int:
    evidence = packet.get("attached_certificate_evidence", [])
    return len(evidence) if isinstance(evidence, list) else 0


def validate(packet: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if packet.get("observed_data_used_as_selector") is not False:
        errors.append("observed_data_used_as_selector must be false")
    if packet.get("target_fitting_used") is not False:
        errors.append("target_fitting_used must be false")
    if packet.get("free_axiom_patch_used") is not False:
        errors.append("free_axiom_patch_used must be false")
    if packet.get("same_branch") is not True:
        errors.append("same_branch must be true")
    if packet.get("closure_claimed") is not False:
        errors.append("closure_claimed must be false for trace-map field gates")

    missing = [field for field in REQUIRED_FIELDS if packet.get(field) is not True]
    if missing:
        errors.append("missing I11 trace-map fields: " + ", ".join(missing))
    if evidence_count(packet) < 5:
        errors.append("at least five trace-map evidence entries are required")
    return not errors, errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_selected_i11_trace_map.py <packet.json>", file=sys.stderr)
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
