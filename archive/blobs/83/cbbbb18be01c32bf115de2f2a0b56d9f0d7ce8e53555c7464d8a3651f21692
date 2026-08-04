"""Validate a smooth selected lift of the finite S3 twisted source.

The finite S3 twisted Chan-Paton cancellation is already closed.  This gate is
stricter: it asks whether that finite class has been promoted to a selected
smooth Deligne/Cech, B-field, worldvolume-flux, or twisted Chan-Paton source
with the necessary same-branch consistency checks.

Exit codes:
  0: smooth selected S3 source lift passes
  1: complete packet fails guardrail or mathematical checks
  2: packet is deliberately open/incomplete
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"

SCHEMA = "VisibleTwistedS3SmoothSourceLift.v1"
SOURCE_KINDS = {
    "Deligne_Cech_gerbe",
    "B_field_period_table",
    "worldvolume_flux",
    "twisted_Chan_Paton",
    "flat_Deligne_Cech_gerbe_plus_twisted_CP",
}
EXPECTED_DEPENDENCIES = {
    "visible_twisted_s3_finite_cp_cancellation_certificate.json": "VISIBLE_TWISTED_S3_FINITE_CP_CANCELLATION_CLOSED_SMOOTH_SOURCE_OPEN",
    "time_oriented_m1_flat_gerbe_promotion_certificate.json": "TIME_ORIENTED_M1_FLAT_GERBE_PROMOTION_CONDITIONAL_CLOSED_SELECTION_OPEN",
    "visible_twisted_s3_source_packet_attempt_certificate.json": "VISIBLE_TWISTED_S3_SOURCE_PACKET_ATTEMPT_BLOCKED_SELECTED_SOURCE_OPEN",
    "time_oriented_m1_green_schwarz_gate_certificate.json": "TIME_ORIENTED_M1_GREEN_SCHWARZ_GATE_PRESERVATION_CLOSED_VISIBLE_SOURCE_OPEN",
    "time_oriented_m1_visible_green_schwarz_curvature_closure_certificate.json": "TIME_ORIENTED_M1_VISIBLE_GS_CURVATURE_CLOSED_OPERATOR_SOURCE_OPEN",
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


def validate_finite_inputs(packet: dict[str, Any], failures: list[str]) -> None:
    finite = packet.get("finite_inputs")
    if not isinstance(finite, dict):
        raise IncompleteData("MISSING finite_inputs")
    for key in (
        "finite_S3_CP_cancellation_closed",
        "conditional_flat_gerbe_representative_exists",
        "qutrit_projective_module_compatible",
        "ordinary_matter_curves_retained",
    ):
        require(finite.get(key) is True, failures, f"finite_inputs.{key} must be true")
    require(
        finite.get("central_phase_label") == "zeta_3^2",
        failures,
        "finite_inputs.central_phase_label must be zeta_3^2",
    )


def validate_smooth_source(packet: dict[str, Any], failures: list[str]) -> None:
    source = packet.get("smooth_source")
    if not isinstance(source, dict):
        raise IncompleteData("MISSING smooth_source")
    if source.get("source_kind") not in SOURCE_KINDS:
        failures.append(f"smooth_source.source_kind must be one of {sorted(SOURCE_KINDS)}")
    for key in (
        "source_selected_by_mtt",
        "selected_cover_or_scaffold_verified",
        "good_cover_data_supplied",
        "deligne_cech_representative_constructed",
        "fixed_differential_cohomology_class",
        "restricts_to_selected_S3_worldvolume",
        "map_to_qutrit_central_cocycle_verified",
        "smooth_twisted_CP_or_worldvolume_flux_constructed",
    ):
        require(source.get(key) is True, failures, f"smooth_source.{key} must be true")
    require(source.get("curvature_H_form") == "0", failures, "smooth_source.curvature_H_form must be 0")
    require(
        isinstance(source.get("source_certificate"), str)
        and source.get("source_certificate", "").endswith(".json"),
        failures,
        "smooth_source.source_certificate must name a JSON certificate",
    )


def validate_consistency(packet: dict[str, Any], failures: list[str]) -> None:
    consistency = packet.get("consistency")
    if not isinstance(consistency, dict):
        raise IncompleteData("MISSING consistency")
    for key in (
        "green_schwarz_flat_H_preservation_closed",
        "green_schwarz_bianchi_verified_for_smooth_S3_source",
        "freed_witten_verified_for_smooth_S3_source",
        "twisted_projector_retention_verified",
        "block_factorized_family_higgs_projectors_retained",
    ):
        require(consistency.get(key) is True, failures, f"consistency.{key} must be true")


def validate_guardrails(packet: dict[str, Any], failures: list[str]) -> None:
    require(packet.get("selected_stack") == "S3", failures, "selected_stack must be S3")
    require(packet.get("fixture_only") is False, failures, "fixture_only must be false")
    require(
        packet.get("uses_observed_flavor_data") is False,
        failures,
        "uses_observed_flavor_data must be false",
    )
    require(
        packet.get("uses_benchmark_flavor_entries") is False,
        failures,
        "uses_benchmark_flavor_entries must be false",
    )
    require(
        packet.get("uses_projective_prototype_as_selected") is False,
        failures,
        "uses_projective_prototype_as_selected must be false",
    )


def validate(packet: dict[str, Any]) -> tuple[int, list[str], dict[str, Any]]:
    if packet.get("status") == "OPEN":
        raise IncompleteData("visible twisted S3 smooth source lift packet is OPEN")
    if packet.get("schema") != SCHEMA:
        raise ValueError(f"schema must be {SCHEMA}")

    failures, dependencies = dependency_report()
    validate_guardrails(packet, failures)
    validate_branch(packet, failures)
    validate_finite_inputs(packet, failures)
    validate_smooth_source(packet, failures)
    validate_consistency(packet, failures)

    report = {
        "schema": packet.get("schema"),
        "selected_stack": packet.get("selected_stack"),
        "dependency_statuses": dependencies,
        "source_kind": packet.get("smooth_source", {}).get("source_kind"),
        "source_selected_by_mtt": packet.get("smooth_source", {}).get("source_selected_by_mtt"),
        "selected_cover_or_scaffold_verified": packet.get("smooth_source", {}).get(
            "selected_cover_or_scaffold_verified"
        ),
        "freed_witten_verified": packet.get("consistency", {}).get(
            "freed_witten_verified_for_smooth_S3_source"
        ),
        "projector_retention_verified": packet.get("consistency", {}).get(
            "twisted_projector_retention_verified"
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
        print(f"INVALID visible twisted S3 smooth source lift packet: {exc}")
        return 1

    print(f"visible_twisted_s3_smooth_source_lift_report={json.dumps(report, sort_keys=True)}")
    if failures:
        print("visible twisted S3 smooth source lift FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("visible twisted S3 smooth source lift PASS")
    print("smooth selected S3 source lift, Freed-Witten gate, and projector retention pass")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
