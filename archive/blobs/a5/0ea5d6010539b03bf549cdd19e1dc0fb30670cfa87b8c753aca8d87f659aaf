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
FAR_SOURCE = VALIDATED / "far_source" / "d057.1em03.json"
MAIN = VALIDATED / "far_residue" / "d057.main.a397.json"
SEGMENTED = VALIDATED / "far_residue" / "d057.tail.a397.json"
NODE = VALIDATED / "d057.n3.node.refined.json"
PACKET = VALIDATED / "far_residue" / "d057.tail_frobenius.a397f.json"


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
    require(math.isfinite(result) and result >= 0.0, f"A397F invalid {label}")
    return result


def main() -> int:
    packet = load(PACKET)
    source = load(FAR_SOURCE)
    main_packet = load(MAIN)
    segmented = load(SEGMENTED)
    node = load(NODE)
    require(packet["artifact"] == "A397F", "A397F artifact label changed")
    require(
        packet["schema"] == "MTTQ79HeightFourD057FarCutFrobeniusTailInterval.v1",
        "A397F schema changed",
    )
    require(
        packet["status"] == "D057_FAR_CUT_FROBENIUS_TAIL_ALL_EIGHT_ROWS_CERTIFIED",
        "A397F status changed",
    )
    numerics = packet["numerics"]
    dps = int(numerics["dps"])
    order = int(numerics["Taylor_order"])
    terms = int(numerics["Frobenius_series_terms"])
    require(dps >= 90 and order >= 48, "A397F precision/order gate failed")
    require(8 <= terms <= order // 2, "A397F series-term gate failed")
    ctx.dps = dps

    target = packet["selected_target"]
    require(int(target["distinguished_index"]) == 57, "A397F target changed")
    require(target["root_id"] == "selected_008", "A397F root changed")
    require(int(target["A219_contribution_rank"]) == 13, "A397F rank changed")
    require(int(target["signed_chain_coefficient"]) == 4, "A397F coefficient changed")
    epsilon = float(target["endpoint_cutoff_epsilon"])
    require(epsilon == 1.0e-3, "A397F cutoff changed")
    require(
        set(int(value) for value in target["near_node_colliding_pair_zero_based"])
        == {3, 4},
        "A397F selected colliding pair changed",
    )
    require(source["artifact"] == "A380FS", "A397F far source changed")
    require(
        main_packet["schema"]
        == "MTTQ79HeightFourD057FarCutResidueMainInterval.v1"
        and main_packet["status"]
        == "D057_FAR_CUT_ALL_EIGHT_MAIN_RESIDUE_ROWS_INTERVAL_CERTIFIED",
        "A397F main packet changed",
    )
    require(
        int(source["selected_target"]["distinguished_index"])
        == int(main_packet["selected_target"]["distinguished_index"])
        == int(target["distinguished_index"]),
        "A397F target authorities disagree",
    )
    require(
        int(node["selected_target"]["distinguished_index"]) == 57,
        "A397F certified node identity changed",
    )

    tail = packet["all_eight_endpoint_tails"]
    rows = tail["rows"]
    require(len(rows) == 8, "A397F did not persist eight rows")
    centers: list[complex] = []
    radii: list[float] = []
    for index, row in enumerate(rows):
        require(int(row["residue_index_zero_based"]) == index, "A397F rows reordered")
        ball = validated.interval_from_bounds(row["interval_bounds"])
        center = validated.midpoint(ball)
        radius = validated.radius_upper(ball)
        stored_center = complex_value(row["interval_center"])
        stored_radius = float(row["interval_radius_upper"])
        require(center == stored_center, f"A397F row {index} center does not round-trip")
        require(
            math.isclose(radius, stored_radius, rel_tol=2.0e-15, abs_tol=1.0e-300),
            f"A397F row {index} radius does not round-trip",
        )
        require(radius > 0.0 and math.isfinite(radius), f"A397F row {index} radius invalid")
        centers.append(center)
        radii.append(radius)
    centers_array = np.asarray(centers, dtype=np.complex128)
    radii_array = np.asarray(radii, dtype=np.float64)
    stored_centers = np.asarray(
        [complex_value(value) for value in tail["interval_centers"]],
        dtype=np.complex128,
    )
    stored_radii = np.asarray(tail["interval_radius_uppers"], dtype=np.float64)
    require(bool(np.array_equal(centers_array, stored_centers)), "A397F center table changed")
    require(bool(np.array_equal(radii_array, stored_radii)), "A397F radius table changed")
    maximum_radius = float(np.max(radii_array))
    require(
        math.isclose(
            float(tail["maximum_interval_radius_upper"]),
            maximum_radius,
            rel_tol=2.0e-15,
            abs_tol=1.0e-300,
        ),
        "A397F maximum radius does not replay",
    )

    generic = segmented["all_eight_endpoint_tails"]
    generic_centers = np.asarray(
        [complex_value(value) for value in generic["interval_centers"]],
        dtype=np.complex128,
    )
    generic_radii = np.asarray(generic["interval_radius_uppers"], dtype=np.float64)
    sign = int(target["Frobenius_branch_sign_against_segmented_tail"])
    require(sign in {-1, 1}, "A397F branch sign is not binary")
    raw_centers = sign * centers_array
    plus_overlap = abs(raw_centers - generic_centers) <= radii_array + generic_radii
    minus_overlap = abs(-raw_centers - generic_centers) <= radii_array + generic_radii
    require(
        bool(np.all(plus_overlap)) != bool(np.all(minus_overlap)),
        "A397F branch sign is not uniquely separated",
    )
    replayed_sign = 1 if bool(np.all(plus_overlap)) else -1
    require(replayed_sign == sign, "A397F stored branch sign does not replay")
    differences = abs(centers_array - generic_centers)
    require(
        bool(np.all(differences <= radii_array + generic_radii)),
        "A397F does not overlap the independent segmented enclosure",
    )
    for index, row in enumerate(rows):
        require(row["segmented_tail_interval_overlaps"], f"A397F row {index} overlap flag false")
        require(
            math.isclose(
                float(row["segmented_tail_center_difference"]),
                float(differences[index]),
                rel_tol=2.0e-14,
                abs_tol=1.0e-300,
            ),
            f"A397F row {index} overlap difference changed",
        )

    comparison = packet["comparison_to_segmented_tail"]
    generic_maximum = float(np.max(generic_radii))
    require(comparison["all_eight_intervals_overlap"], "A397F aggregate overlap flag false")
    require(int(comparison["unique_branch_sign"]) == sign, "A397F aggregate sign changed")
    replay = {
        "segmented_maximum_radius_upper": generic_maximum,
        "Frobenius_maximum_radius_upper": maximum_radius,
        "radius_tightening_factor": generic_maximum / maximum_radius,
        "maximum_center_difference": float(np.max(differences)),
    }
    for key, expected in replay.items():
        require(
            math.isclose(float(comparison[key]), expected, rel_tol=2.0e-14, abs_tol=1.0e-300),
            f"A397F comparison does not replay {key}",
        )

    hensel = packet["quantitative_Hensel_disk"]
    require(hensel["quantitative_Hensel_disk_closed"], "A397F Hensel disk open")
    require(int(hensel["order"]) == order, "A397F Hensel order changed")
    require(
        set(int(value) for value in hensel["selected_root_indices_zero_based"]) == {3, 4},
        "A397F Hensel pair changed",
    )
    require(
        math.isclose(float(hensel["center_x"]), epsilon / 2.0, rel_tol=0.0, abs_tol=1.0e-18)
        and math.isclose(float(hensel["disk_radius"]), epsilon / 2.0, rel_tol=0.0, abs_tol=1.0e-18),
        "A397F Hensel disk does not cover the selected tail",
    )
    correction = finite_nonnegative(hensel["uniform_factor_correction_radius"], "factor correction")
    self_map = finite_nonnegative(hensel["self_map_bound_upper"], "self-map bound")
    contraction = finite_nonnegative(hensel["contraction_bound_upper"], "contraction")
    require(correction > 0.0 and self_map <= correction, "A397F Hensel self-map gate failed")
    require(contraction < 1.0, "A397F Hensel contraction gate failed")
    require(float(hensel["second_to_third_node_distance_gap_lower"]) > 0.0, "A397F pair isolation failed")
    for key in (
        "factor_residual_infinity_norm_upper",
        "factor_jacobian_inverse_defect_upper",
        "newton_eta_upper",
        "elliptic_ODE_residual_upper",
        "elliptic_uniform_remainder_upper",
    ):
        finite_nonnegative(hensel[key], key)
    require(float(hensel["factor_jacobian_inverse_infinity_norm_upper"]) > 0.0, "A397F inverse norm invalid")

    integral = packet["Frobenius_integral_diagnostics"]
    require(int(integral["direction_zero_based"]) == 0, "A397F direction changed")
    require(int(integral["series_terms"]) == terms, "A397F series length changed")
    require(integral["period_connection_identity"] == "D_s P=C_s P", "A397F connection identity changed")
    require(integral["period_connection_identity_overlaps_all_five_rows"], "A397F connection replay failed")
    require(0.0 < float(integral["nodal_series_ratio_upper"]) < 1.0, "A397F nodal series diverges")
    require(float(integral["quartic_absolute_lower_on_Cauchy_disk"]) > 0.0, "A397F Cauchy disk meets a zero")
    require(float(integral["node_deformation_jacobian_determinant_absolute_lower"]) > 0.0, "A397F node deformation singular")
    require(float(integral["factor_derivative_solve_neumann_norm"]) < 1.0, "A397F derivative solve open")
    remainders = integral["period_remainders"]
    require([int(row["period_power"]) for row in remainders] == list(range(5)), "A397F period powers changed")
    for row in remainders:
        for key in (
            "value_Cauchy_tail_upper",
            "derivative_Cauchy_tail_upper",
            "base_Cauchy_bound_upper",
            "derivative_Cauchy_bound_upper",
        ):
            finite_nonnegative(row[key], f"period {row['period_power']} {key}")
    for key in (
        "maximum_integrand_value_remainder_upper",
        "maximum_integrand_derivative_remainder_upper",
        "maximum_period_connection_interval_difference_upper",
        "factor_derivative_solution_remainder",
        "endpoint_coordinate_sliver_width_upper",
    ):
        finite_nonnegative(integral[key], key)

    for label, entry in packet["authority"].items():
        path = ROOT / entry["path"]
        require(path.is_file(), f"A397F authority missing: {label}")
        require(sha256(path) == entry["sha256"], f"A397F authority stale: {label}")
    scope = packet["strict_scope"]
    for key in (
        "same_selected_d057_geometry_used",
        "same_far_cut_epsilon_used",
        "quantitative_Hensel_factor_disk_closed",
        "finite_Frobenius_period_series_with_Cauchy_tail_used",
        "full_precision_interval_round_trip_used",
        "all_eight_far_cut_tail_rows_interval_closed",
    ):
        require(scope[key], f"A397F strict gate false: {key}")
    require(not scope["segmented_tail_used_as_bound"], "A397F promotes the coarse overlap bound")
    require(not scope["full_d057_splice_closed"], "A397F overclaims the full splice")
    require(not scope["covariant_zero_proved"], "A397F overclaims a covariant zero")
    require(not scope["full_SM_closure_proved"], "A397F overclaims SM closure")
    require(not scope["observed_SM_values_used"], "observed SM data entered A397F")
    print(
        "PASS: A397F independently replays the serialized Hensel/Frobenius "
        f"tail and tightens the segmented enclosure by {generic_maximum / maximum_radius:.6g}x"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
