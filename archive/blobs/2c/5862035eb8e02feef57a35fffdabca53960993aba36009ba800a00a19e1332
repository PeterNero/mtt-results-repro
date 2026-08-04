"""Validate a same-source matter-slot/overlap operator packet.

This validator intentionally rejects support-only, fixture-only, lifted-flag,
or locked-target-selected fields.  It is the promotion gate for turning the
conditional Weyl-pair operator into selected A_selected/b_selected data.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = [
    "source_identity",
    "matter_slot_charge",
    "singlet_neutrino_rule",
    "operator_values",
    "overlap_transfer",
    "normalization",
    "primitive_contractions",
]

FORBIDDEN_PROVENANCE = {
    "lifted_flag",
    "unselected_fixture",
    "locked_target_selection",
    "observed_sm_data",
    "benchmark_matrix",
    "support_shape_only",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(data: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    payload = data.get("attempted_selected_packet", {})
    fields = payload.get("fields", {})

    for name in REQUIRED_FIELDS:
        item = fields.get(name)
        if not isinstance(item, dict):
            errors.append(f"{name}: missing field object")
            continue
        if item.get("selected_emitted") is not True:
            errors.append(f"{name}: selected_emitted is not true")
        provenance = item.get("provenance")
        if provenance in FORBIDDEN_PROVENANCE:
            errors.append(f"{name}: forbidden provenance {provenance}")
        if not item.get("same_source"):
            errors.append(f"{name}: same_source is not true")
        if not item.get("theorem_derived"):
            errors.append(f"{name}: theorem_derived is not true")

    packet = payload.get("packet_flags", {})
    if packet.get("one_same_source") is not True:
        errors.append("packet: one_same_source is not true")
    if packet.get("observed_data_used") is not False:
        errors.append("packet: observed_data_used is not false")
    if packet.get("target_fitting_used") is not False:
        errors.append("packet: target_fitting_used is not false")
    if packet.get("promote_to_A_selected") is not True:
        errors.append("packet: promote_to_A_selected is not true")
    if packet.get("promote_to_b_selected") is not True:
        errors.append("packet: promote_to_b_selected is not true")

    return not errors, errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_samesource_matter_slot_overlap_operator_packet.py <packet.json>")
        return 2
    path = Path(argv[1])
    data = load(path)
    ok, errors = validate(data)
    report = {
        "validator": "validate_samesource_matter_slot_overlap_operator_packet",
        "path": str(path),
        "ok": ok,
        "errors": errors,
        "required_fields": REQUIRED_FIELDS,
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
