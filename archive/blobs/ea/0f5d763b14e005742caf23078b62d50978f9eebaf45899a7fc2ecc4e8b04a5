"""Validate the next alpha1 provenance certificate.

The certificate may close through either lane:

1. selected visible/Route-C source identity with same-branch alpha1 derivative;
2. typed B_N retarded alpha1 derivative with transfer normalization.

Either lane must be theorem-derived, same-branch, and free of observed-data or
lifted-flag promotion.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


FORBIDDEN_PROVENANCE = {
    "support_shape_only",
    "diagnostic_lift",
    "observed_sm_data",
    "benchmark_matrix",
    "retarded_pattern_only",
    "coordinate_convention_only",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def field_ok(field: dict[str, Any], errors: list[str], prefix: str) -> bool:
    ok = True
    if field.get("selected_emitted") is not True:
        errors.append(f"{prefix}: selected_emitted is not true")
        ok = False
    if field.get("same_branch") is not True:
        errors.append(f"{prefix}: same_branch is not true")
        ok = False
    if field.get("theorem_derived") is not True:
        errors.append(f"{prefix}: theorem_derived is not true")
        ok = False
    provenance = field.get("provenance")
    if provenance in FORBIDDEN_PROVENANCE:
        errors.append(f"{prefix}: forbidden provenance {provenance}")
        ok = False
    return ok


def validate_lane_a(lane: dict[str, Any], errors: list[str]) -> bool:
    required = [
        "source_identity",
        "visible_routec_operator_source",
        "phi_fin_payload",
        "same_branch_alpha1_derivative",
        "dotd_validator_replay",
    ]
    ok = True
    for name in required:
        item = lane.get(name)
        if not isinstance(item, dict):
            errors.append(f"lane_A.{name}: missing field object")
            ok = False
            continue
        ok = field_ok(item, errors, f"lane_A.{name}") and ok
    replay = lane.get("dotd_validator_replay", {})
    if replay.get("honest_validator_exit_code") != 0:
        errors.append("lane_A.dotd_validator_replay: honest validator did not pass")
        ok = False
    return ok


def validate_lane_b(lane: dict[str, Any], errors: list[str]) -> bool:
    required = [
        "retarded_source_selector",
        "typed_bn_alpha1_derivative",
        "selected_transfer_normalization",
        "sector_dotd_equality",
        "dotd_validator_replay",
    ]
    ok = True
    for name in required:
        item = lane.get(name)
        if not isinstance(item, dict):
            errors.append(f"lane_B.{name}: missing field object")
            ok = False
            continue
        ok = field_ok(item, errors, f"lane_B.{name}") and ok
    replay = lane.get("dotd_validator_replay", {})
    if replay.get("honest_validator_exit_code") != 0:
        errors.append("lane_B.dotd_validator_replay: honest validator did not pass")
        ok = False
    return ok


def validate(data: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if data.get("schema") != "MTTVisibleRouteCSourceIdentityOrTypedBNRetardedDerivative.v1":
        errors.append("certificate: wrong schema")
    if data.get("branch_id") != "q79/F,m=1/S3_GS/RouteC_or_same_visible_source":
        errors.append("certificate: wrong branch_id")
    if data.get("forbidden_inputs_used"):
        errors.append("certificate: forbidden_inputs_used is nonempty")

    lane_a_errors: list[str] = []
    lane_b_errors: list[str] = []
    lane_a_ok = validate_lane_a(data.get("lane_A_visible_routec_source_identity", {}), lane_a_errors)
    lane_b_ok = validate_lane_b(data.get("lane_B_typed_bn_retarded_derivative", {}), lane_b_errors)

    if not (lane_a_ok or lane_b_ok):
        errors.append("certificate: neither lane validates")
        errors.extend(lane_a_errors)
        errors.extend(lane_b_errors)

    promotion = data.get("promotion_result", {})
    if lane_a_ok or lane_b_ok:
        if promotion.get("selected_value_emitted") is not True:
            errors.append("promotion_result: selected_value_emitted is not true")
        if promotion.get("alpha1_driver_verified") is not True:
            errors.append("promotion_result: alpha1_driver_verified is not true")
    if promotion.get("target_fitting_used") is not False:
        errors.append("promotion_result: target_fitting_used is not false")

    return not errors, errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_visible_routec_sourceidentity_or_typedbn_derivative.py <certificate.json>")
        return 2
    path = Path(argv[1])
    data = load(path)
    ok, errors = validate(data)
    print(
        json.dumps(
            {
                "validator": "validate_visible_routec_sourceidentity_or_typedbn_derivative",
                "path": str(path),
                "ok": ok,
                "errors": errors,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
