"""Validate a selected same-source alpha1 normalization packet."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = [
    "source_identity",
    "source_strength_coordinate",
    "normalization_functional",
    "tangent_equality",
    "sector_dotd_equality",
]

FORBIDDEN_PROVENANCE = {
    "coordinate_convention_only",
    "support_shape_only",
    "diagnostic_lift",
    "observed_sm_data",
    "benchmark_matrix",
    "retarded_pattern_only",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(data: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []

    if data.get("schema") != "MTTSelectedSameSourceAlpha1NormalizationPacket.v1":
        errors.append("packet: wrong schema")
    if data.get("branch_id") != "q79/F,m=1/S3_GS/RouteC_or_same_visible_source":
        errors.append("packet: branch_id is not the locked selected branch id")
    if data.get("forbidden_inputs_used"):
        errors.append("packet: forbidden_inputs_used is nonempty")

    for name in REQUIRED_FIELDS:
        item = data.get(name)
        if not isinstance(item, dict):
            errors.append(f"{name}: missing field object")
            continue
        if item.get("selected_emitted") is not True:
            errors.append(f"{name}: selected_emitted is not true")
        provenance = item.get("provenance")
        if provenance in FORBIDDEN_PROVENANCE:
            errors.append(f"{name}: forbidden provenance {provenance}")
        if item.get("same_source") is not True:
            errors.append(f"{name}: same_source is not true")
        if item.get("theorem_derived") is not True:
            errors.append(f"{name}: theorem_derived is not true")

    source_coord = data.get("source_strength_coordinate", {})
    if source_coord.get("lambda_alpha1") != 1.0:
        errors.append("source_strength_coordinate: lambda_alpha1 is not 1.0")

    norm = data.get("normalization_functional", {})
    if norm.get("N_alpha1_h_ext") != 1.0:
        errors.append("normalization_functional: N_alpha1_h_ext is not 1.0")

    tangent = data.get("tangent_equality", {})
    residual = tangent.get("residual_l2")
    tolerance = tangent.get("tolerance", 1e-12)
    if not isinstance(residual, (int, float)) or residual > tolerance:
        errors.append("tangent_equality: residual_l2 is missing or above tolerance")

    sector = data.get("sector_dotd_equality", {})
    if sector.get("honest_validator_exit_code") != 0:
        errors.append("sector_dotd_equality: honest validator did not pass")
    if sector.get("diagnostic_lift_used_as_proof") is not False:
        errors.append("sector_dotd_equality: diagnostic lift is used as proof")

    promotion = data.get("promotion_result", {})
    if promotion.get("selected_value_emitted") is not True:
        errors.append("promotion_result: selected_value_emitted is not true")
    if promotion.get("alpha1_driver_verified") is not True:
        errors.append("promotion_result: alpha1_driver_verified is not true")
    if promotion.get("target_fitting_used") is not False:
        errors.append("promotion_result: target_fitting_used is not false")

    return not errors, errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_samesource_alpha1_normalization_packet.py <packet.json>")
        return 2
    path = Path(argv[1])
    data = load(path)
    ok, errors = validate(data)
    print(
        json.dumps(
            {
                "validator": "validate_samesource_alpha1_normalization_packet",
                "path": str(path),
                "ok": ok,
                "errors": errors,
                "required_fields": REQUIRED_FIELDS,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
