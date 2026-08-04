from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path

import numpy as np
from flint import ctx


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import certify_q79_selected_side_beta_defect_transport as validated


VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
SOURCE = VALIDATED / "far_source" / "d027.1em03.json"
MAIN = VALIDATED / "far_residue" / "d027.main.a406m.json"
REFERENCE = VALIDATED / "far_residue" / "d027.tail_segmented.a406r.json"
NODE = VALIDATED / "d027.n3.node.refined.json"
PACKET = VALIDATED / "far_residue" / "d027.tail_frobenius.a406f.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def finite_nonnegative(value: object, label: str) -> float:
    result = float(value)
    require(math.isfinite(result) and result >= 0.0, f"A406F invalid {label}")
    return result


def main() -> int:
    packet = load(PACKET)
    source = load(SOURCE)
    main_packet = load(MAIN)
    reference = load(REFERENCE)
    node = load(NODE)
    require(packet["artifact"] == "A406F", "A406F artifact label changed")
    require(
        packet["schema"] == "MTTQ79HeightFourD027FarCutFrobeniusTailInterval.v1",
        "A406F schema changed",
    )
    require(
        packet["status"] == "D027_FAR_CUT_FROBENIUS_TAIL_ALL_EIGHT_ROWS_CERTIFIED",
        "A406F status changed",
    )

    target = packet["selected_target"]
    expected_target = {
        "distinguished_index": 27,
        "root_id": "selected_011",
        "A219_contribution_rank": 15,
        "signed_chain_coefficient": -2,
    }
    for key, expected in expected_target.items():
        actual = target[key]
        if isinstance(expected, int):
            actual = int(actual)
        require(actual == expected, f"A406F target changed: {key}")
    require(float(target["endpoint_cutoff_epsilon"]) == 1.0e-3, "A406F cutoff changed")
    require(
        set(int(value) for value in target["near_node_colliding_pair_zero_based"])
        == {1, 2},
        "A406F colliding pair changed",
    )
    require(source["artifact"] == "A380FS", "A406F far source changed")
    require(main_packet["artifact"] == "A406M", "A406F main source changed")
    require(reference["artifact"] == "A406R", "A406F branch reference changed")
    require(int(node["selected_target"]["distinguished_index"]) == 27, "A406F node changed")

    numerics = packet["numerics"]
    dps = int(numerics["dps"])
    order = int(numerics["Taylor_order"])
    terms = int(numerics["Frobenius_series_terms"])
    require(dps >= 90 and order >= 48, "A406F precision/order gate failed")
    require(8 <= terms <= order // 2, "A406F series-term gate failed")
    ctx.dps = dps

    tail = packet["all_eight_endpoint_tails"]
    rows = tail["rows"]
    require(len(rows) == 8, "A406F did not persist eight rows")
    centers: list[complex] = []
    radii: list[float] = []
    for index, row in enumerate(rows):
        require(int(row["residue_index_zero_based"]) == index, "A406F rows reordered")
        ball = validated.interval_from_bounds(row["interval_bounds"])
        center = validated.midpoint(ball)
        radius = validated.radius_upper(ball)
        require(center == complex_value(row["interval_center"]), f"A406F row {index} center does not round-trip")
        require(
            math.isclose(radius, float(row["interval_radius_upper"]), rel_tol=2.0e-15, abs_tol=1.0e-300),
            f"A406F row {index} radius does not round-trip",
        )
        require(math.isfinite(radius) and radius > 0.0, f"A406F row {index} radius invalid")
        centers.append(center)
        radii.append(radius)
    centers_array = np.asarray(centers, dtype=np.complex128)
    radii_array = np.asarray(radii, dtype=np.float64)
    stored_centers = np.asarray([complex_value(value) for value in tail["interval_centers"]])
    stored_radii = np.asarray(tail["interval_radius_uppers"], dtype=np.float64)
    require(bool(np.array_equal(centers_array, stored_centers)), "A406F center table changed")
    require(bool(np.array_equal(radii_array, stored_radii)), "A406F radius table changed")
    require(
        math.isclose(float(tail["maximum_interval_radius_upper"]), float(np.max(radii_array)), rel_tol=2.0e-15),
        "A406F maximum radius does not replay",
    )

    reference_tail = reference["all_eight_endpoint_tails"]
    reference_centers = np.asarray(
        [complex_value(value) for value in reference_tail["interval_centers"]],
        dtype=np.complex128,
    )
    reference_radii = np.asarray(reference_tail["interval_radius_uppers"], dtype=np.float64)
    sign = int(target["Frobenius_branch_sign_against_A406R"])
    require(sign in {-1, 1}, "A406F branch sign is not binary")
    raw_centers = sign * centers_array
    plus_overlap = abs(raw_centers - reference_centers) <= radii_array + reference_radii
    minus_overlap = abs(-raw_centers - reference_centers) <= radii_array + reference_radii
    require(bool(np.all(plus_overlap)) != bool(np.all(minus_overlap)), "A406F branch is not uniquely selected")
    replayed_sign = 1 if bool(np.all(plus_overlap)) else -1
    require(replayed_sign == sign, "A406F branch sign does not replay")
    differences = abs(centers_array - reference_centers)
    require(bool(np.all(differences <= radii_array + reference_radii)), "A406F misses A406R")
    comparison = packet["comparison_to_A406R_segmented_reference"]
    require(comparison["all_eight_intervals_overlap"], "A406F aggregate overlap false")
    require(int(comparison["unique_branch_sign"]) == sign, "A406F aggregate sign changed")
    expected_comparison = {
        "segmented_maximum_radius_upper": float(np.max(reference_radii)),
        "Frobenius_maximum_radius_upper": float(np.max(radii_array)),
        "radius_tightening_factor": float(np.max(reference_radii) / np.max(radii_array)),
        "maximum_center_difference": float(np.max(differences)),
    }
    for key, expected in expected_comparison.items():
        require(math.isclose(float(comparison[key]), expected, rel_tol=2.0e-14), f"A406F comparison changed: {key}")

    hensel = packet["quantitative_Hensel_disk"]
    require(hensel["quantitative_Hensel_disk_closed"], "A406F Hensel disk open")
    require(int(hensel["order"]) == order, "A406F Hensel order changed")
    require(set(int(value) for value in hensel["selected_root_indices_zero_based"]) == {1, 2}, "A406F Hensel pair changed")
    require(math.isclose(float(hensel["center_x"]), 5.0e-4, abs_tol=1.0e-18), "A406F Hensel center changed")
    require(math.isclose(float(hensel["disk_radius"]), 5.0e-4, abs_tol=1.0e-18), "A406F Hensel radius changed")
    correction = finite_nonnegative(hensel["uniform_factor_correction_radius"], "factor correction")
    require(finite_nonnegative(hensel["self_map_bound_upper"], "self-map") <= correction, "A406F self-map gate failed")
    require(finite_nonnegative(hensel["contraction_bound_upper"], "contraction") < 1.0, "A406F contraction gate failed")
    require(float(hensel["second_to_third_node_distance_gap_lower"]) > 0.0, "A406F pair isolation failed")

    integral = packet["Frobenius_integral_diagnostics"]
    require(int(integral["direction_zero_based"]) == 0, "A406F direction changed")
    require(int(integral["series_terms"]) == terms, "A406F series length changed")
    require(integral["period_connection_identity"] == "D_s P=C_s P", "A406F connection identity changed")
    require(integral["period_connection_identity_overlaps_all_five_rows"], "A406F connection replay failed")
    require(integral["Cauchy_domain_geometry"] == "closed complex disk", "A406F Cauchy domain changed")
    require(
        integral["Cauchy_quartic_bound_method"]
        == "constant-lower-minus-polynomial-disk-majorant",
        "A406F disk majorant changed",
    )
    require(0.0 < float(integral["nodal_series_ratio_upper"]) < 0.5, "A406F strong nodal-series gate failed")
    require(float(integral["quartic_absolute_lower_on_Cauchy_disk"]) > 0.0, "A406F Cauchy disk meets a zero")
    rho = float(integral["Cauchy_radius"])
    coefficient_uppers = [
        float(value)
        for value in integral["quartic_local_coefficient_absolute_uppers"]
    ]
    constant_lower = float(integral["quartic_local_constant_absolute_lower"])
    variation = sum(
        coefficient_uppers[degree] * rho**degree
        for degree in range(1, len(coefficient_uppers))
    )
    require(
        float(integral["quartic_absolute_lower_on_Cauchy_disk"])
        <= constant_lower - variation + 2.0e-13,
        "A406F quartic disk lower bound does not replay",
    )
    replayed_ratio = float(integral["delta_absolute_upper"]) / (4.0 * rho**2)
    require(
        float(integral["nodal_series_ratio_upper"]) >= replayed_ratio,
        "A406F nodal ratio is not outward",
    )
    require(float(integral["node_deformation_jacobian_determinant_absolute_lower"]) > 0.0, "A406F node deformation singular")
    require(float(integral["factor_derivative_solve_neumann_norm"]) < 1.0, "A406F derivative solve open")
    require([int(row["period_power"]) for row in integral["period_remainders"]] == list(range(5)), "A406F period powers changed")

    for label, entry in packet["authority"].items():
        path = ROOT / entry["path"]
        require(path.is_file(), f"A406F authority missing: {label}")
        require(sha256(path) == entry["sha256"], f"A406F authority stale: {label}")
    scope = packet["strict_scope"]
    for key in (
        "same_selected_d027_geometry_used",
        "same_far_cut_epsilon_used",
        "quantitative_Hensel_factor_disk_closed",
        "finite_Frobenius_period_series_with_Cauchy_tail_used",
        "disk_specific_Cauchy_majorant_used",
        "full_precision_interval_round_trip_used",
        "all_eight_far_cut_tail_rows_interval_closed",
    ):
        require(scope[key], f"A406F strict gate false: {key}")
    require(not scope["A406R_segmented_reference_used_as_bound"], "A406F promotes A406R as a bound")
    require(not scope["full_d027_splice_closed"], "A406F overclaims the full splice")
    require(not scope["covariant_zero_proved"], "A406F overclaims a zero")
    require(not scope["full_SM_closure_proved"], "A406F overclaims SM closure")
    require(not scope["observed_SM_values_used"], "observed SM data entered A406F")
    print(
        "PASS: A406F independently replays the serialized d027 Hensel/Frobenius "
        f"tail and tightens A406R by {np.max(reference_radii) / np.max(radii_array):.6g}x"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
