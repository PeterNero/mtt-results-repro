"""Validate the selected S3 class/restriction packet for the twisted route.

This is the sharpened post-cover-gauge-reduction gate.  The good cover itself
is not a selected physical knob; the packet must instead prove that the fixed
q79/F,m=1 flat class restricts to S3 and is cancelled by the same-branch
twisted Chan-Paton module, with W3/spinC and projector retention verified.

Exit codes:
  0: selected S3 class/restriction packet passes
  1: complete packet fails mathematical checks
  2: packet is deliberately open/incomplete
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"

SCHEMA = "VisibleTwistedS3ClassRestrictionPacket.v1"
EXPECTED_DEPENDENCIES = {
    "iwasawa_deligne_cover_gauge_reduction_certificate.json": "IWASAWA_DELIGNE_COVER_GAUGE_REDUCTION_CLOSED_CLASS_RESTRICTION_OPEN",
    "time_oriented_fixed_gerbe_representative_certificate.json": "TIME_ORIENTED_FIXED_GERBE_REPRESENTATIVE_CLOSED_SOURCE_PACKET_OPEN",
    "time_oriented_m1_gerbe_period_table_certificate.json": "TIME_ORIENTED_M1_FINITE_GERBE_PERIOD_TABLE_CLOSED_OPERATOR_SOURCE_OPEN",
    "time_oriented_m1_deck_cech_lift_certificate.json": "TIME_ORIENTED_M1_DECK_CECH_LIFT_CLOSED_GEOMETRIC_OPERATOR_SOURCE_OPEN",
    "time_oriented_m1_flat_gerbe_promotion_certificate.json": "TIME_ORIENTED_M1_FLAT_GERBE_PROMOTION_CONDITIONAL_CLOSED_SELECTION_OPEN",
    "visible_complex_worldvolume_spinc_gate_certificate.json": "VISIBLE_COMPLEX_WORLDVOLUME_SPINC_W3_CLOSED_DD_IMAGES_OPEN",
    "visible_twisted_s3_finite_cp_cancellation_certificate.json": "VISIBLE_TWISTED_S3_FINITE_CP_CANCELLATION_CLOSED_SMOOTH_SOURCE_OPEN",
}


class IncompleteData(ValueError):
    """Raised for deliberately open packets."""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, failures: list[str], message: str) -> None:
    if not condition:
        failures.append(message)


def dependency_report() -> tuple[list[str], dict[str, str | None]]:
    failures: list[str] = []
    report: dict[str, str | None] = {}
    for name, expected in EXPECTED_DEPENDENCIES.items():
        path = CERTIFICATES / name
        if not path.exists():
            failures.append(f"missing dependency certificate {name}")
            report[name] = None
            continue
        status = load_json(path).get("status")
        report[name] = status
        if status != expected:
            failures.append(f"{name} status must be {expected}, got {status}")
    return failures, report


def validate_branch(packet: dict[str, Any], failures: list[str]) -> None:
    branch = packet.get("branch")
    if not isinstance(branch, dict):
        raise IncompleteData("MISSING branch")
    require(branch.get("q") == 79, failures, "branch.q must be 79")
    require(branch.get("orientation") == "F", failures, "branch.orientation must be F")
    require(branch.get("torsion_label_m") == 1, failures, "branch.torsion_label_m must be 1")
    require(
        branch.get("same_branch_q79_f_m1") is True,
        failures,
        "branch.same_branch_q79_f_m1 must be true",
    )


def validate_class(packet: dict[str, Any], failures: list[str]) -> None:
    data = packet.get("class_data")
    if not isinstance(data, dict):
        raise IncompleteData("MISSING class_data")
    for key in (
        "cover_choice_auxiliary_not_selected_knob",
        "fixed_smooth_flat_gerbe_class",
        "same_class_as_finite_m1_deck_cocycle",
        "map_to_qutrit_central_cocycle_verified",
    ):
        require(data.get(key) is True, failures, f"class_data.{key} must be true")
    require(data.get("curvature_H_form") == "0", failures, "class_data.curvature_H_form must be 0")
    require(
        data.get("central_phase_label") == "zeta_3^2",
        failures,
        "class_data.central_phase_label must be zeta_3^2",
    )
    require(
        isinstance(data.get("differential_cohomology_class_certificate"), str)
        and data.get("differential_cohomology_class_certificate", "").endswith(".json"),
        failures,
        "class_data.differential_cohomology_class_certificate must name a JSON certificate",
    )


def validate_restriction(packet: dict[str, Any], failures: list[str]) -> None:
    restriction = packet.get("s3_restriction")
    if not isinstance(restriction, dict):
        raise IncompleteData("MISSING s3_restriction")
    for key in (
        "S3_pullback_table_supplied",
        "S3_B_restriction_nonzero_ordinary_DD",
        "twisted_CP_module_supplied",
        "twisted_CP_DD_matches_B_restriction",
        "finite_total_twisted_DD_class_zero",
        "W3_spinC_zero",
        "smooth_Freed_Witten_cancellation_verified",
    ):
        require(restriction.get(key) is True, failures, f"s3_restriction.{key} must be true")
    require(
        restriction.get("S3_active_image_rank_over_F3") == 2,
        failures,
        "s3_restriction.S3_active_image_rank_over_F3 must be 2",
    )


def validate_projectors(packet: dict[str, Any], failures: list[str]) -> None:
    projectors = packet.get("projector_retention")
    if not isinstance(projectors, dict):
        raise IncompleteData("MISSING projector_retention")
    for key in (
        "block_factorized_projectors_supplied",
        "projector_retention_proved_for_selected_source",
        "family_higgs_blocks_retained",
    ):
        require(projectors.get(key) is True, failures, f"projector_retention.{key} must be true")


def validate_guardrails(packet: dict[str, Any], failures: list[str]) -> None:
    require(packet.get("selected_stack") == "S3", failures, "selected_stack must be S3")
    require(packet.get("fixture_only") is False, failures, "fixture_only must be false")
    for key in (
        "uses_observed_flavor_data",
        "uses_benchmark_flavor_entries",
        "uses_projective_prototype_as_selected",
    ):
        require(packet.get(key) is False, failures, f"{key} must be false")


def validate(packet: dict[str, Any]) -> tuple[int, list[str], dict[str, Any]]:
    if packet.get("status") == "OPEN":
        raise IncompleteData("visible twisted S3 class/restriction packet is OPEN")
    if packet.get("schema") != SCHEMA:
        raise ValueError(f"schema must be {SCHEMA}")

    failures, dependencies = dependency_report()
    validate_guardrails(packet, failures)
    validate_branch(packet, failures)
    validate_class(packet, failures)
    validate_restriction(packet, failures)
    validate_projectors(packet, failures)
    report = {
        "schema": packet.get("schema"),
        "selected_stack": packet.get("selected_stack"),
        "dependency_statuses": dependencies,
        "fixed_smooth_flat_gerbe_class": packet.get("class_data", {}).get(
            "fixed_smooth_flat_gerbe_class"
        ),
        "S3_pullback_table_supplied": packet.get("s3_restriction", {}).get(
            "S3_pullback_table_supplied"
        ),
        "smooth_Freed_Witten_cancellation_verified": packet.get("s3_restriction", {}).get(
            "smooth_Freed_Witten_cancellation_verified"
        ),
        "projector_retention_proved": packet.get("projector_retention", {}).get(
            "projector_retention_proved_for_selected_source"
        ),
        "passes": not failures,
    }
    return (0 if not failures else 1), failures, report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        packet = load_json(args.packet)
        code, failures, report = validate(packet)
    except IncompleteData as exc:
        print(str(exc))
        return 2
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"INVALID visible twisted S3 class/restriction packet: {exc}")
        return 1

    print(f"visible_twisted_s3_class_restriction_report={json.dumps(report, sort_keys=True)}")
    if failures:
        print("visible twisted S3 class/restriction FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("visible twisted S3 class/restriction PASS")
    print("selected S3 class, restriction, Freed-Witten, and projectors pass")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
