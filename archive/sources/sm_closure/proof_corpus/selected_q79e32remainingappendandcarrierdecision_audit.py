from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

from flint import acb, arb, ctx


ROOT = Path(__file__).resolve().parents[1]
PERIOD_DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
)
A134 = PERIOD_DIRECTORY / "selected_alignment_height4_E32_handle_interval_and_thimble_cutset.packet.json"
A176 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_successor_A176.packet.json"
A206 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_successor_A206.packet.json"
FINAL = PERIOD_DIRECTORY / "selected_alignment_E32_weighted_71_thimble_and_frozen_carrier_decision.packet.json"
HANDLE = PERIOD_DIRECTORY / "selected_alignment_E32_handle_combination.interval.packet.json"
ORIENTATION = PERIOD_DIRECTORY / "selected_alignment_thimble_orientation_synchronization.packet.json"
BETA = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
    / "pgl3_selected_side_beta.local_lower.order40_step003.interval.packet.json"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def close(left: float, right: float, tolerance: float = 1.0e-16) -> bool:
    return math.isclose(float(left), float(right), rel_tol=2.0e-12, abs_tol=tolerance)


def lower(value: arb) -> float:
    return float(value.lower())


def coordinate_zero_distance_lower(value: acb) -> tuple[str, float]:
    distances = []
    for name, component in (("real", value.real), ("imaginary", value.imag)):
        component_lower = float(component.lower())
        component_upper = float(component.upper())
        if component_lower > 0.0:
            distance = math.nextafter(component_lower, -math.inf)
        elif component_upper < 0.0:
            distance = math.nextafter(-component_upper, -math.inf)
        else:
            distance = 0.0
        distances.append((name, distance))
    return max(distances, key=lambda row: row[1])


def radius_upper(value: acb) -> float:
    return float(value.rad().upper())


def midpoint(value: acb) -> complex:
    return complex(float(value.real.mid()), float(value.imag.mid()))


def interval_from_bounds(value: dict) -> acb:
    real_lower = arb(value["real"]["lower"])
    real_upper = arb(value["real"]["upper"])
    imag_lower = arb(value["imaginary"]["lower"])
    imag_upper = arb(value["imaginary"]["upper"])
    real_midpoint = (real_lower + real_upper) / arb(2)
    imag_midpoint = (imag_lower + imag_upper) / arb(2)
    real_radius = (real_upper - real_lower) / arb(2)
    imag_radius = (imag_upper - imag_lower) / arb(2)
    return acb(
        arb(str(real_midpoint.mid()), str(real_radius.upper())),
        arb(str(imag_midpoint.mid()), str(imag_radius.upper())),
    )


def serialized_disk(center: dict[str, str], radius: float) -> acb:
    real = float(center["real"])
    imaginary = float(center["imaginary"])
    inflated = radius + max(2.0 * math.ulp(real), 2.0 * math.ulp(imaginary))
    return acb(
        arb(center["real"], format(inflated, ".17g")),
        arb(center["imaginary"], format(inflated, ".17g")),
    )


def successor_path(artifact: str) -> Path:
    return PERIOD_DIRECTORY / f"selected_alignment_E32_clearance_ranked_successor_{artifact}.packet.json"


def audit_native_successor(predecessor_path: Path, artifact: str) -> tuple[Path, dict]:
    predecessor = load(predecessor_path)
    packet_path = successor_path(artifact)
    packet = load(packet_path)
    assert packet["schema"] == "MTTQ79SelectedE32ClearanceRankedAppendSuccessor.v1"
    assert packet["artifact"] == artifact
    assert packet["append_only_predecessor"]["sha256"] == sha256(predecessor_path)
    for authority in packet["authority"]:
        path = ROOT / authority["path"]
        assert sha256(path) == authority["sha256"], authority["path"]
    new = packet["new_accepted_full_interval"]
    index = int(new["distinguished_index"])
    chart = new["line_chart"]
    assert chart == "z"
    assert int(predecessor["clearance_ranked_queues"][chart][0]["distinguished_index"]) == index
    assert int(predecessor["clearance_ranked_queues"][chart][0]["coefficient"]) == int(new["coefficient"])
    old_ledger = predecessor["weighted_budget_ledger"]
    ledger = packet["weighted_budget_ledger"]
    cost = abs(int(new["coefficient"])) * (
        float(new["full_interval_radius_upper"]) + float(new["A131_center_difference"])
    )
    assert close(new["weighted_radius_plus_displacement_cost"], cost)
    assert int(ledger["selected_support_closed"]) == int(old_ledger["selected_support_closed"]) + 1
    assert int(ledger["selected_l1_closed"]) == int(old_ledger["selected_l1_closed"]) + abs(int(new["coefficient"]))
    assert int(ledger["remaining_support"]) == int(old_ledger["remaining_support"]) - 1
    assert int(ledger["remaining_l1_weight"]) == int(old_ledger["remaining_l1_weight"]) - abs(int(new["coefficient"]))
    assert close(ledger["remaining_budget"], float(old_ledger["remaining_budget"]) - cost)
    assert float(ledger["remaining_budget"]) > 0

    root_id = new["root_id"]
    stem = PERIOD_DIRECTORY / f"d{index:03d}_{root_id}"
    main = load(Path(f"{stem}.E32_main.interval.packet.json"))
    tail = load(Path(f"{stem}.E32_tail.interval.packet.json"))
    full = load(Path(f"{stem}.E32_full.interval.packet.json"))
    scan = load(Path(f"{stem}.E32_detour_scan.packet.json"))
    route = scan["ranked_routes"][0]
    assert main["scope"]["uncompressed_physical_generator_zonotope_consumed"]
    assert main["scope"]["certified_tail_cutoff_period_reuse_consumed"]
    assert main["polygonal_homotopy"]["relative_homotopy_class_equals_original_radial_path"]
    assert close(main["polygonal_homotopy"]["detour_fraction"], route["detour_fraction"])
    assert close(main["polygonal_homotopy"]["detour_signed_right_offset"], route["detour_offset"])
    assert close(main["polygonal_homotopy"]["return_fraction"], route["return_fraction"])
    assert tail["scope"]["endpoint_tail_interval_closed"]
    assert full["scope"]["single_full_E32_thimble_interval_closed"]
    assert full["full_E32_thimble"]["floating_candidate_contained"]
    assert full["A134_radius_ledger"]["fallback_met"]
    return packet_path, packet


def main() -> int:
    ctx.dps = 100
    predecessor_path = A176
    native_packets = []
    for number in range(177, 206):
        predecessor_path, packet = audit_native_successor(predecessor_path, f"A{number}")
        native_packets.append(packet)

    a205 = native_packets[-1]
    ledger_205 = a205["weighted_budget_ledger"]
    assert int(ledger_205["selected_support_closed"]) == 70
    assert int(ledger_205["selected_l1_closed"]) == 119
    assert int(ledger_205["remaining_support"]) == 1
    assert int(ledger_205["remaining_l1_weight"]) == 4
    assert a205["clearance_ranked_queues"]["y"] == []
    assert a205["clearance_ranked_queues"]["z"] == []
    assert [int(row["distinguished_index"]) for row in a205["partial_interval_diagnostics"]] == [47]

    a206 = load(A206)
    assert a206["schema"] == "MTTQ79SelectedE32PartialFinalAppend.v1"
    assert a206["artifact"] == "A206"
    assert a206["append_only_predecessor"]["sha256"] == sha256(predecessor_path)
    for authority in a206["authority"]:
        path = ROOT / authority["path"]
        assert sha256(path) == authority["sha256"], authority["path"]
    new = a206["new_accepted_full_interval"]
    assert int(new["distinguished_index"]) == 47
    assert new["root_id"] == "selected_058"
    assert int(new["coefficient"]) == 4
    assert new["promoted_from_partial_diagnostic"]
    assert a206["partial_interval_diagnostics"] == []
    ledger_206 = a206["weighted_budget_ledger"]
    assert (
        int(ledger_206["selected_support_closed"]),
        int(ledger_206["selected_l1_closed"]),
        int(ledger_206["remaining_support"]),
        int(ledger_206["remaining_l1_weight"]),
    ) == (71, 123, 0, 0)
    assert float(ledger_206["remaining_budget"]) > 0
    assert a206["scope"]["all_71_single_thimble_intervals_closed"]
    assert not a206["scope"]["weighted_71_thimble_interval_closed"]

    main_47 = load(PERIOD_DIRECTORY / "d047_selected_058.E32_main.interval.packet.json")
    tail_47 = load(PERIOD_DIRECTORY / "d047_selected_058.E32_tail.interval.packet.json")
    full_47 = load(PERIOD_DIRECTORY / "d047_selected_058.E32_full.interval.packet.json")
    geometry_47 = main_47["polygonal_homotopy"]
    assert main_47["selected_thimble"]["line_chart"] == "y"
    assert main_47["scope"]["uncompressed_physical_generator_zonotope_consumed"]
    assert main_47["scope"]["certified_tail_cutoff_period_reuse_consumed"]
    assert main_47["scope"]["refined_endpoint_tail_cutoff_payload_contained"]
    assert main_47["scope"]["refined_tail_main_transport_reuse_promoted"]
    assert len(tail_47["regular_segments"]) == 768
    assert geometry_47["relative_homotopy_class_equals_original_radial_path"]
    assert close(geometry_47["detour_fraction"], 0.45)
    assert close(geometry_47["detour_signed_right_offset"], 0.01)
    assert close(geometry_47["return_fraction"], 0.86)
    assert float(geometry_47["other_critical_ball_clearance_lower"]) > 0.0124
    assert tail_47["scope"]["endpoint_tail_interval_closed"]
    assert full_47["scope"]["single_full_E32_thimble_interval_closed"]
    assert full_47["full_E32_thimble"]["floating_candidate_contained"]
    assert full_47["A134_radius_ledger"]["fallback_met"]

    final = load(FINAL)
    assert final["artifact"] == "A207"
    assert final["schema"] == "MTTQ79SelectedE32Weighted71ThimbleAndFrozenCarrierDecision.v1"
    for authority in final["authority"]:
        path = ROOT / authority["path"]
        assert sha256(path) == authority["sha256"], authority["path"]
    assert final["selected_manifest"]["support"] == 71
    assert final["selected_manifest"]["coefficient_l1_norm"] == 123

    a134 = load(A134)
    accepted = {
        int(row["distinguished_index"]): row
        for row in a206["accepted_full_intervals"]
    }
    orientation = load(ORIENTATION)
    orientation_signs = [int(value) for value in orientation["column_signs"]]
    assert len(orientation_signs) == 90
    assert set(orientation_signs) <= {-1, 1}
    assert orientation["strict_scope"]["all_90_A130_canonical_vanishing_vectors_used"]
    weighted = acb(0)
    recurrence_steps = 0
    for row in a134["selected_E32_decomposition"]["primitive_thimble_chain"]:
        index = int(row["distinguished_index"])
        coefficient = int(row["coefficient"])
        accepted_row = accepted[index]
        full_path = PERIOD_DIRECTORY / f"d{index:03d}_{accepted_row['root_id']}.E32_full.interval.packet.json"
        full = load(full_path)
        orientation_sign = orientation_signs[index - 1]
        reported = next(
            item
            for item in final["selected_manifest"]["summands"]
            if int(item["distinguished_index"]) == index
        )
        assert int(reported["canonical_orientation_sign"]) == orientation_sign
        assert int(reported["oriented_raw_interval_coefficient"]) == coefficient * orientation_sign
        weighted += acb(coefficient * orientation_sign) * interval_from_bounds(
            full["full_E32_thimble"]["interval"]
        )
        main_path = PERIOD_DIRECTORY / f"d{index:03d}_{accepted_row['root_id']}.E32_main.interval.packet.json"
        recurrence_steps += int(load(main_path)["validated_main_transport"]["accepted_step_count"])

    reported_center = final["weighted_thimble_combination"]["interval_center"]
    assert abs(
        midpoint(weighted)
        - complex(float(reported_center["real"]), float(reported_center["imaginary"]))
    ) < 1.0e-14
    assert close(radius_upper(weighted), final["weighted_thimble_combination"]["interval_radius_upper"])
    a131_thimble = acb(
        a134["selected_E32_decomposition"]["A131_floating_thimble_combination_center"]["real"],
        a134["selected_E32_decomposition"]["A131_floating_thimble_combination_center"]["imaginary"],
    )
    assert weighted.contains(a131_thimble)

    handle_packet = load(HANDLE)
    handle_row = handle_packet["E32_handle_combination"]["interval"]
    handle_ball = serialized_disk(handle_row["center"], float(handle_row["uniform_radius_upper"]))
    period = weighted + handle_ball
    beta = load(BETA)["endpoint"]
    beta_ball = serialized_disk(
        beta["beta_center"][5],
        float(beta["uniform_component_radius_upper"])
        + float(beta["center_serialization_radius_upper"]),
    )
    residual = beta_ball - period
    separating_component, residual_lower = coordinate_zero_distance_lower(residual)
    assert not residual.contains(acb(0))
    assert residual_lower > 0
    assert close(residual_lower, final["frozen_carrier_residual"]["absolute_value_lower"])
    assert separating_component == final["frozen_carrier_residual"]["separating_component"]
    assert close(radius_upper(residual), final["frozen_carrier_residual"]["interval_radius_upper"])
    assert final["frozen_carrier_residual"]["zero_excluded"]
    assert final["scope"]["weighted_71_thimble_interval_closed"]
    assert final["scope"]["fixed_carrier_exact_separation_closed"]
    assert final["scope"]["frozen_height_four_carrier_rejected_by_E32_zero_exclusion"]
    assert not final["scope"]["covariant_alignment_zero_solved_on_this_carrier"]
    assert not final["scope"]["observed_SM_values_used"]

    candidate = load(ROOT / "candidate_data" / "selected_q79e32weighted71thimbleandfrozencarrierdecision.candidate.json")
    certificate = load(ROOT / "certificates" / "selected_q79e32weighted71thimbleandfrozencarrierdecision.certificate.json")
    assert candidate["packet_sha256"] == sha256(FINAL)
    assert certificate["candidate_sha256"] == sha256(
        ROOT / "candidate_data" / "selected_q79e32weighted71thimbleandfrozencarrierdecision.candidate.json"
    )
    assert candidate["closure_claimed"] and certificate["closure_claimed"]

    print("q79 E32 remaining append and carrier decision audit: PASS")
    print("closed: A177-A205 native-z appends, A206 d047 partial promotion")
    print(f"closed: weighted 71-thimble interval after {recurrence_steps} accepted zonotope steps")
    print(f"closed: frozen-carrier E32 zero exclusion lower bound {residual_lower:.16g}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
