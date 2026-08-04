"""Validate the selected S3 twisted D7 source packet.

This is the visible-worldvolume specialization of the twisted-source program.
It prevents the already-closed S3 selector from being promoted to a physical
twisted D7 source unless the packet also supplies selected differential
cohomology/worldvolume evidence, Freed-Witten compatibility, and projector
retention.

Exit codes:
  0: the selected S3 source packet passes
  1: a complete packet fails guardrail or mathematical checks
  2: the packet is deliberately open/incomplete
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"

SCHEMA = "VisibleTwistedS3SourcePacket.v1"
SOURCE_KINDS = {
    "Deligne_Cech_gerbe",
    "B_field_period_table",
    "worldvolume_flux",
    "twisted_Chan_Paton",
    "finite_HYM_Strominger_twisted_solve",
}
EXPECTED_STATUSES = {
    "visible_twisted_d7_equivariant_embedding_selector_certificate.json": "VISIBLE_TWISTED_D7_EQUIVARIANT_EMBEDDING_SELECTOR_S3_CLOSED_SOURCE_OPEN",
    "visible_twisted_chan_paton_rescue_certificate.json": "VISIBLE_TWISTED_CP_MINIMAL_COORDINATE_RESCUE_REDUCED_SELECTION_OPEN",
    "time_oriented_m1_gerbe_period_table_certificate.json": "TIME_ORIENTED_M1_FINITE_GERBE_PERIOD_TABLE_CLOSED_OPERATOR_SOURCE_OPEN",
    "time_oriented_m1_deck_cech_lift_certificate.json": "TIME_ORIENTED_M1_DECK_CECH_LIFT_CLOSED_GEOMETRIC_OPERATOR_SOURCE_OPEN",
    "time_oriented_m1_flat_gerbe_promotion_certificate.json": "TIME_ORIENTED_M1_FLAT_GERBE_PROMOTION_CONDITIONAL_CLOSED_SELECTION_OPEN",
    "time_oriented_m1_freed_witten_cycle_gate_certificate.json": "TIME_ORIENTED_M1_FREED_WITTEN_CYCLE_GATE_FORMULATED_SELECTED_CYCLES_OPEN",
    "time_oriented_m1_qutrit_line_cycle_restrictions_certificate.json": "TIME_ORIENTED_M1_QUTRIT_LINE_CYCLE_RESTRICTIONS_CLOSED_VISIBLE_CYCLE_LIST_OPEN",
    "visible_complex_worldvolume_spinc_gate_certificate.json": "VISIBLE_COMPLEX_WORLDVOLUME_SPINC_W3_CLOSED_DD_IMAGES_OPEN",
    "time_oriented_m1_green_schwarz_gate_certificate.json": "TIME_ORIENTED_M1_GREEN_SCHWARZ_GATE_PRESERVATION_CLOSED_VISIBLE_SOURCE_OPEN",
}


class IncompleteData(ValueError):
    """Raised when the packet is a deliberate open template."""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, failures: list[str], message: str) -> None:
    if not condition:
        failures.append(message)


def dependency_report() -> tuple[list[str], dict[str, str | None]]:
    failures: list[str] = []
    report: dict[str, str | None] = {}
    for name, expected in EXPECTED_STATUSES.items():
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


def validate_selector(packet: dict[str, Any], failures: list[str]) -> None:
    selector = packet.get("selector_evidence")
    if not isinstance(selector, dict):
        raise IncompleteData("MISSING selector_evidence")
    require(
        selector.get("equivariant_selector_certificate")
        == "visible_twisted_d7_equivariant_embedding_selector_certificate.json",
        failures,
        "selector_evidence.equivariant_selector_certificate is wrong",
    )
    require(
        selector.get("minimal_equivariant_twisted_D7_stack_selector") == "S3",
        failures,
        "minimal equivariant twisted D7 stack selector must be S3",
    )
    require(
        selector.get("selected_stack_by_mtt") is True,
        failures,
        "selector_evidence.selected_stack_by_mtt must be true",
    )
    require(
        selector.get("S1_S2_require_extra_selected_orientation_breaking_source") is True,
        failures,
        "S1/S2 must remain rejected without an extra selected source",
    )


def validate_finite_gerbe(packet: dict[str, Any], failures: list[str]) -> None:
    finite = packet.get("finite_gerbe_evidence")
    if not isinstance(finite, dict):
        raise IncompleteData("MISSING finite_gerbe_evidence")
    require(finite.get("period_denominator") == 3, failures, "period_denominator must be 3")
    require(
        finite.get("central_phase_label") == "zeta_3^2",
        failures,
        "central_phase_label must be zeta_3^2 on the q79/F,m=1 branch",
    )
    require(finite.get("base_group") == "F_3^2", failures, "base_group must be F_3^2")
    require(
        finite.get("qutrit_commutator_matches_m1_twist") is True,
        failures,
        "finite qutrit commutator must match the m=1 twist",
    )
    for key in (
        "finite_period_table_closed",
        "deck_cech_lift_closed",
        "conditional_flat_gerbe_closed",
        "finite_projective_CP_module_matches_m1_twist",
    ):
        require(finite.get(key) is True, failures, f"finite_gerbe_evidence.{key} must be true")


def validate_worldvolume(packet: dict[str, Any], failures: list[str]) -> None:
    worldvolume = packet.get("worldvolume_evidence")
    if not isinstance(worldvolume, dict):
        raise IncompleteData("MISSING worldvolume_evidence")
    require(packet.get("selected_stack") == "S3", failures, "selected_stack must be S3")
    require(worldvolume.get("twisted_projective_D7_stack") == "S3", failures, "twisted stack must be S3")
    require(
        sorted(worldvolume.get("active_pair", [])) == ["T1", "T2"],
        failures,
        "active_pair must be T1,T2",
    )
    require(
        worldvolume.get("S3_active_image_rank_over_F3") == 2,
        failures,
        "S3 active image rank must be 2",
    )
    require(
        worldvolume.get("rank_two_DD_requires_twisted_source") is True,
        failures,
        "rank-two DD restriction must be handled by a twisted source",
    )
    require(
        worldvolume.get("ordinary_DD_zero_D7_stacks") == ["S1", "S2"],
        failures,
        "ordinary DD-zero D7 stacks must be S1,S2",
    )
    require(
        worldvolume.get("ordinary_DD_zero_matter_curves") == ["C12", "C23", "C31"],
        failures,
        "ordinary DD-zero matter curves must be C12,C23,C31",
    )
    require(
        worldvolume.get("W3_spinC_zero_for_visible_cycles") is True,
        failures,
        "visible cycles must have W3/spinC zero evidence",
    )


def validate_source(packet: dict[str, Any], failures: list[str]) -> None:
    source = packet.get("source_evidence")
    if not isinstance(source, dict):
        raise IncompleteData("MISSING source_evidence")
    if source.get("source_kind") not in SOURCE_KINDS:
        failures.append(f"source_evidence.source_kind must be one of {sorted(SOURCE_KINDS)}")
    for key in (
        "source_selected_by_mtt",
        "fixed_differential_cohomology_class",
        "geometric_Deligne_Cech_or_worldvolume_flux_source_constructed",
        "physical_worldvolume_flux_or_twisted_CP_source_constructed",
        "map_to_central_cocycle_verified",
    ):
        require(source.get(key) is True, failures, f"source_evidence.{key} must be true")
    require(
        isinstance(source.get("source_certificate"), str)
        and source.get("source_certificate", "").endswith(".json"),
        failures,
        "source_evidence.source_certificate must name a JSON certificate",
    )


def validate_consistency(packet: dict[str, Any], failures: list[str]) -> None:
    consistency = packet.get("consistency_evidence")
    if not isinstance(consistency, dict):
        raise IncompleteData("MISSING consistency_evidence")
    for key in (
        "green_schwarz_flat_H_preservation_gate_closed",
        "green_schwarz_bianchi_verified_for_S3_source",
        "freed_witten_verified_for_S3_source",
        "twisted_projector_retention_verified",
    ):
        require(consistency.get(key) is True, failures, f"consistency_evidence.{key} must be true")


def validate_guardrails(packet: dict[str, Any], failures: list[str]) -> None:
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
        raise IncompleteData("visible twisted S3 source packet is OPEN")
    if packet.get("schema") != SCHEMA:
        raise ValueError(f"schema must be {SCHEMA}")

    failures, deps = dependency_report()
    validate_guardrails(packet, failures)
    validate_branch(packet, failures)
    validate_selector(packet, failures)
    validate_finite_gerbe(packet, failures)
    validate_worldvolume(packet, failures)
    validate_source(packet, failures)
    validate_consistency(packet, failures)

    downstream = packet.get("downstream_not_required_for_source_gate", {})
    report = {
        "schema": packet.get("schema"),
        "selected_stack": packet.get("selected_stack"),
        "dependency_statuses": deps,
        "source_kind": packet.get("source_evidence", {}).get("source_kind"),
        "source_selected_by_mtt": packet.get("source_evidence", {}).get("source_selected_by_mtt"),
        "fixed_differential_cohomology_class": packet.get("source_evidence", {}).get(
            "fixed_differential_cohomology_class"
        ),
        "freed_witten_verified": packet.get("consistency_evidence", {}).get(
            "freed_witten_verified_for_S3_source"
        ),
        "projector_retention_verified": packet.get("consistency_evidence", {}).get(
            "twisted_projector_retention_verified"
        ),
        "downstream_open": {
            "selected_visible_operator_source": downstream.get("selected_visible_operator_source_open"),
            "selected_D_E_dotD": downstream.get("selected_D_E_dotD_open"),
            "primitive_C1_contractions": downstream.get("primitive_C1_contractions_open"),
        },
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
        print(f"INVALID visible twisted S3 source packet: {exc}")
        return 1

    print(f"visible_twisted_s3_source_report={json.dumps(report, sort_keys=True)}")
    if failures:
        print("visible twisted S3 source FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("visible twisted S3 source PASS")
    print("selected S3 twisted D7 source, Freed-Witten gate, and projector retention pass")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
