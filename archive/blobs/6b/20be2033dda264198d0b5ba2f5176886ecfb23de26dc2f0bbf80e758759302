from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path

from flint import acb, acb_mat, arb, ctx


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import certify_q79_selected_side_base_lift_interval as serializer
import certify_q79_selected_side_beta_defect_transport as validated
import run_q79_augmented_beta_transport as augmented


VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
DIRECTORY = VALIDATED / "ol"
A383 = VALIDATED / "n3.rank3.handle_hessian.interval.json"
A383_A_CHECKPOINT = VALIDATED / "n3.handleA.hessian.checkpoint.json"
A411 = VALIDATED / "jop" / "trunk.a411.json"
SOURCE = DIRECTORY / "ha.src.a418.json"
CHECKPOINT = DIRECTORY / "ha.a418.ckpt.json"
PACKET = DIRECTORY / "ha.a418.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def interval_entry(value: dict) -> acb:
    center = value["center"]
    radius = float(value["component_radius_upper"])
    real = float(center["real"])
    imaginary = float(center["imaginary"])
    serialization = max(math.ulp(real), math.ulp(imaginary), 1.0e-300)
    outward = math.nextafter(radius + serialization, math.inf)
    return acb(
        arb(format(real, ".17g"), format(outward, ".17g")),
        arb(format(imaginary, ".17g"), format(outward, ".17g")),
    )


def interval_matrix(rows: list[list[dict]]) -> acb_mat:
    return acb_mat([[interval_entry(value) for value in row] for row in rows])


def column(values: list[acb]) -> acb_mat:
    result = acb_mat(len(values), 1)
    for row, value in enumerate(values):
        result[row, 0] = value
    return result


def main() -> int:
    # A418 is an exact replay of a 100 dps FLINT serialization.  Rebuilding
    # those balls at a different working precision changes printed endpoints
    # by outward-rounding ulps even though the intervals still enclose one
    # another.
    ctx.dps = 100
    packet = load(PACKET)
    source = load(SOURCE)
    checkpoint = load(CHECKPOINT)
    handle = load(A383)
    handle_checkpoint = load(A383_A_CHECKPOINT)
    trunk = load(A411)
    if packet.get("artifact") != "A418":
        raise AssertionError("A418 artifact changed")
    if packet.get("schema") != "MTTQ79HeightFourAHandleOuterHubAffine.v1":
        raise AssertionError("A418 schema changed")
    if "dps=100" not in checkpoint.get("path_name", ""):
        raise AssertionError("A418 checkpoint working precision changed")
    for label, entry in packet["authority"].items():
        path = ROOT / entry["path"]
        if not path.is_file() or sha256(path) != entry["sha256"]:
            raise AssertionError(f"A418 authority stale: {label}")

    base_periods = [
        validated.decoded_acb(value)
        for value in handle_checkpoint["configuration"]["initial_periods"]
    ]
    hub_periods = [
        validated.interval_from_bounds(value) for value in source["y_chart_base_lift"]
    ]
    trunk_period = interval_matrix(trunk["period_transport_5_by_5"])
    trunk_residue = interval_matrix(trunk["integrated_residue_operator_8_by_5"])
    replay = trunk_period * column(hub_periods)
    if any(not replay[row, 0].overlaps(base_periods[row]) for row in range(5)):
        raise AssertionError("A418 source no longer replays the A383 base periods")

    final_center = [validated.decoded_acb(value) for value in checkpoint["center"]]
    frame = validated.LiftErrorFrame(
        fundamental=validated.decoded_matrix(checkpoint["lift_fundamental"]),
        coordinate_radii=[arb(value) for value in checkpoint["coordinate_radii"]],
    )
    final_generator = augmented.dynamic_generator_matrix(frame)
    expected_center = hub_periods + final_center[5:13]
    expected_generator = acb_mat(13, 13)
    for row in range(5):
        expected_generator[row, row] = acb(hub_periods[row].rad())
    for row in range(5, 13):
        for col in range(13):
            expected_generator[row, col] = final_generator[row, col]
    stored_centers = packet["hub_outer_affine_center_13"]
    stored_generator = packet["hub_outer_affine_generator_13_by_13"]
    if len(stored_centers) != 13 or len(stored_generator) != 13:
        raise AssertionError("A418 affine payload dimension changed")
    for row in range(13):
        expected_center_bounds = (
            source["y_chart_base_lift"][row]
            if row < 5
            else serializer.complex_interval(expected_center[row])
        )
        if stored_centers[row]["interval_bounds"] != expected_center_bounds:
            raise AssertionError(f"A418 center row {row} does not replay")
        if len(stored_generator[row]) != 13:
            raise AssertionError("A418 generator is not 13 by 13")
        for col in range(13):
            if row < 5 and col == row:
                bounds = stored_generator[row][col]["interval_bounds"]
                if bounds["imaginary"] != {"lower": "0", "upper": "0"}:
                    raise AssertionError(f"A418 source generator {row} is not real")
                if bounds["real"]["lower"] != bounds["real"]["upper"]:
                    raise AssertionError(f"A418 source generator {row} is not a point")
                stored_radius = float(arb(bounds["real"]["lower"]))
                source_bounds = source["y_chart_base_lift"][row]
                real_radius = (
                    arb(source_bounds["real"]["upper"])
                    - arb(source_bounds["real"]["lower"])
                ) / arb(2)
                imaginary_radius = (
                    arb(source_bounds["imaginary"]["upper"])
                    - arb(source_bounds["imaginary"]["lower"])
                ) / arb(2)
                minimum_source_radius = (real_radius**2 + imaginary_radius**2).sqrt()
                maximum_source_radius = validated.interval_from_bounds(
                    source_bounds
                ).rad()
                if not (
                    stored_radius >= validated.upper(minimum_source_radius)
                    and stored_radius <= validated.upper(maximum_source_radius)
                ):
                    raise AssertionError(
                        f"A418 source generator {row} does not enclose its source ball"
                    )
                continue
            if stored_generator[row][col]["interval_bounds"] != serializer.complex_interval(
                expected_generator[row, col]
            ):
                raise AssertionError(f"A418 generator ({row},{col}) does not replay")

    radii = []
    for row in range(13):
        if row < 5:
            stored_radius = arb(
                stored_generator[row][row]["interval_bounds"]["real"]["lower"]
            )
            radii.append(validated.upper(stored_radius) + validated.upper(abs(stored_radius)))
        else:
            radii.append(
                validated.radius_upper(expected_center[row])
                + validated.upper(
                    sum(
                        (abs(expected_generator[row, col]) for col in range(13)),
                        arb(0),
                    )
                )
            )
    if any(
        not math.isclose(
            radii[row],
            float(packet["hub_outer_component_total_radius_uppers"][row]),
            rel_tol=3.0e-13,
            abs_tol=1.0e-300,
        )
        for row in range(13)
    ):
        raise AssertionError("A418 component radii do not replay")

    base_to_hub = -(trunk_residue * column(hub_periods))
    a383_centers = [
        validated.decoded_acb(value) for value in handle_checkpoint["center"][5:13]
    ]
    a383_radii = [
        validated.upper(arb(value)) for value in handle_checkpoint["output_radii"][:8]
    ]
    differences = []
    margins = []
    for row in range(8):
        recomposed = final_center[5 + row] + base_to_hub[row, 0]
        difference = abs(validated.midpoint(recomposed) - validated.midpoint(a383_centers[row]))
        margin = (
            radii[5 + row]
            + validated.radius_upper(base_to_hub[row, 0])
            + a383_radii[row]
            - difference
        )
        if margin < 0.0:
            raise AssertionError(f"A418 row {row} no longer overlaps A383")
        differences.append(difference)
        margins.append(margin)
    crosscheck = packet["A383_A_handle_crosscheck"]
    if not math.isclose(
        max(differences),
        float(crosscheck["maximum_center_difference"]),
        rel_tol=3.0e-13,
        abs_tol=1.0e-300,
    ):
        raise AssertionError("A418 A383 center crosscheck does not replay")
    stored_margin = float(crosscheck["minimum_overlap_margin"])
    if not crosscheck["all_eight_rows_overlap"] or stored_margin <= 0.0:
        raise AssertionError("A418 stored A383 overlap certificate is not positive")
    # The persisted source decoder widens each hub ball by serialization ulps,
    # so its independently recomputed margin can be slightly larger than the
    # pre-serialization summary.  The stored value must remain conservative;
    # the proof gate is the freshly recomputed positive margin above.
    if stored_margin > math.nextafter(min(margins), math.inf):
        raise AssertionError("A418 stored A383 margin is not conservative")
    scope = packet["strict_scope"]
    for key in (
        "selected_A_handle_hub_period_source_derived",
        "selected_hub_entry_endpoint_path_executed",
        "full_13_state_affine_frame_retained",
        "independent_A383_full_A_handle_crosscheck_closed",
    ):
        if not scope[key]:
            raise AssertionError(f"A418 closure flag false: {key}")
    for key in (
        "attached_to_all_76_thimble_hub_sum",
        "exact_period_boundary_zero_applied",
        "beta_minus_B_block_attached",
        "full_common_relative_chain_transport_executed",
        "interval_Newton_existence_and_uniqueness_closed",
        "covariant_zero_proved",
        "full_SM_closure_proved",
    ):
        if scope[key]:
            raise AssertionError(f"A418 overclaims: {key}")
    if scope["observed_SM_values_used"]:
        raise AssertionError("observed SM values entered A418")
    print(
        "PASS: A418 replays the selected A-handle 13-state hub path; "
        f"minimum A383 overlap {min(margins):.6g}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
