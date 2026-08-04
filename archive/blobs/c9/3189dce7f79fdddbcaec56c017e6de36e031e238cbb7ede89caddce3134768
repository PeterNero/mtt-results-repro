"""Validate selected PSM-C1-02 source-promotion packets."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_SOURCE_FIELDS = [
    "source_owner_id",
    "selected_measure_pairing",
    "selected_quadrature_rule",
    "admissible_c1_variation_space",
    "phase_R_Z_source",
    "shift_R_X_source",
    "b_selected_source",
    "sector_row_assembly",
    "independence_guard",
]

REQUIRED_ROW_COUNTS = {
    "primitive_kernel_rows": 72,
    "hessian_b_source_rows": 2,
    "sector_assembly_rows": 36,
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(packet: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if packet.get("active_label") != "PSM-C1-02":
        errors.append("active_label must be PSM-C1-02")
    if packet.get("observed_data_used_as_selector") is not False:
        errors.append("observed_data_used_as_selector must be false")
    if packet.get("target_fitting_used") is not False:
        errors.append("target_fitting_used must be false")
    if packet.get("locked_target_values_used_as_source") is not False:
        errors.append("locked_target_values_used_as_source must be false")
    if packet.get("free_axiom_patch_used") is not False:
        errors.append("free_axiom_patch_used must be false for unpatched source promotion")
    if packet.get("same_branch") is not True:
        errors.append("same_branch must be true")

    fields = packet.get("source_fields", {})
    if not isinstance(fields, dict):
        return False, errors + ["source_fields must be an object"]

    for field in REQUIRED_SOURCE_FIELDS:
        item = fields.get(field)
        if not isinstance(item, dict):
            errors.append(f"{field}: missing source field")
            continue
        if item.get("selected_emitted") is not True:
            errors.append(f"{field}: selected_emitted must be true")
        if item.get("theorem_derived") is not True:
            errors.append(f"{field}: theorem_derived must be true")
        if item.get("source_owner_verified") is not True:
            errors.append(f"{field}: source_owner_verified must be true")
        if item.get("same_branch") is not True:
            errors.append(f"{field}: same_branch must be true")

    row_counts = packet.get("row_counts", {})
    for key, expected in REQUIRED_ROW_COUNTS.items():
        if row_counts.get(key) != expected:
            errors.append(f"{key}: expected {expected}")

    if packet.get("strict_110_row_payload_validator_passes") is not True:
        errors.append("strict_110_row_payload_validator_passes must be true")
    if packet.get("emitted_before_residual_replay") is not True:
        errors.append("emitted_before_residual_replay must be true")

    return not errors, errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_selected_psm_c1_02_source_promotion_packet.py <packet.json>", file=sys.stderr)
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
