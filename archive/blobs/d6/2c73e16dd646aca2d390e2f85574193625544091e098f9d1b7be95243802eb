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


VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
DIRECTORY = VALIDATED / "ol"
A413 = DIRECTORY / "all76.a413.json"
PACKET = DIRECTORY / "hub.a417.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def decode_ball(value: dict) -> acb:
    return validated.interval_from_bounds(value["interval_bounds"])


def source_path(index: int) -> Path:
    return DIRECTORY / ("d057.a412.json" if index == 57 else f"d{index:03d}.a415.json")


def same_bounds(stored: dict, source: dict) -> bool:
    return stored["interval_bounds"] == source["interval_bounds"]


def interval_hull(values: list[acb]) -> acb:
    if not values:
        raise ValueError("cannot form an empty complex interval hull")
    return validated.interval_from_bounds(
        {
            "real": {
                "lower": format(min(validated.lower(value.real) for value in values), ".17g"),
                "upper": format(max(validated.upper(value.real) for value in values), ".17g"),
            },
            "imaginary": {
                "lower": format(
                    min(validated.lower(value.imag) for value in values), ".17g"
                ),
                "upper": format(
                    max(validated.upper(value.imag) for value in values), ".17g"
                ),
            },
        }
    )


def decoded_generator(row: dict, key: str) -> acb_mat:
    return acb_mat(
        [
            [decode_ball(value) for value in matrix_row]
            for matrix_row in row[key]
        ]
    )


def independently_align_A415_generators(
    index: int,
    source: dict,
    generators: list[acb_mat],
) -> tuple[list[acb_mat], list[float], dict]:
    checkpoint_authority = source["authority"]["A414_correlated_checkpoint"]
    checkpoint_path = ROOT / checkpoint_authority["path"]
    if not checkpoint_path.is_file() or sha256(checkpoint_path) != checkpoint_authority["sha256"]:
        raise AssertionError(f"A417 A414 checkpoint stale for d{index:03d}")
    checkpoint = load(checkpoint_path)
    frames = checkpoint["frames"]
    centers = checkpoint["centers"]
    if len(frames) != 8 or len(centers) != 8:
        raise AssertionError(f"A417 A414 row inventory changed for d{index:03d}")
    for residue_row in range(1, 8):
        if centers[residue_row][:5] != centers[0][:5]:
            raise AssertionError(f"A417 A414 period centers split for d{index:03d}")
        for row in range(5):
            if (
                frames[residue_row]["fundamental"][row][:5]
                != frames[0]["fundamental"][row][:5]
            ):
                raise AssertionError(
                    f"A417 A414 period fundamental split for d{index:03d}"
                )
    coordinate_radii = [
        [arb(value) for value in frame["coordinate_radii"][:5]]
        for frame in frames
    ]
    if any(
        validated.lower(value) <= 0.0
        for radii in coordinate_radii
        for value in radii
    ):
        raise AssertionError(f"A417 A414 period radius is not positive for d{index:03d}")
    common_radii = [
        arb(
            format(
                max(
                    validated.upper(coordinate_radii[row][column])
                    for row in range(8)
                ),
                ".17g",
            )
        )
        for column in range(5)
    ]
    aligned = []
    for residue_row in range(8):
        matrix = acb_mat(6, 6)
        for row in range(6):
            for column in range(6):
                matrix[row, column] = (
                    generators[residue_row][row, column]
                    * (common_radii[column] / coordinate_radii[residue_row][column])
                    if column < 5
                    else generators[residue_row][row, column]
                )
        aligned.append(matrix)
    return (
        aligned,
        [validated.upper(value) for value in common_radii],
        {
            "path": checkpoint_authority["path"],
            "sha256": checkpoint_authority["sha256"],
        },
    )


def aggregate(blocks: list[dict], coefficient_name: str) -> tuple[list[acb], list[float]]:
    centers = [acb(0) for _ in range(13)]
    generator_radii = [arb(0) for _ in range(13)]
    for block in blocks:
        coefficient = int(block[coefficient_name])
        absolute = arb(abs(coefficient))
        center = [decode_ball(value) for value in block["hub_center_13"]]
        period = [
            [decode_ball(value) for value in row]
            for row in block["period_generator_5_by_5"]
        ]
        residue = [
            [decode_ball(value) for value in row]
            for row in block["residue_from_period_generator_8_by_5"]
        ]
        local = [
            decode_ball(value)
            for value in block["residue_local_generator_diagonal_8"]
        ]
        for row in range(13):
            centers[row] += coefficient * center[row]
            if row < 5:
                generator_radii[row] += absolute * sum(
                    (abs(period[row][column]) for column in range(5)), arb(0)
                )
            else:
                residue_row = row - 5
                generator_radii[row] += absolute * (
                    sum(
                        (abs(residue[residue_row][column]) for column in range(5)),
                        arb(0),
                    )
                    + abs(local[residue_row])
                )
    radii = [
        validated.radius_upper(centers[row]) + validated.upper(generator_radii[row])
        for row in range(13)
    ]
    return centers, radii


def require_aggregate(
    packet: dict,
    key: str,
    coefficient_name: str,
    *,
    expected_centers: list[acb] | None = None,
) -> tuple[list[acb], list[float]]:
    centers, radii = aggregate(packet["independent_target_affine_blocks"], coefficient_name)
    persisted_centers = centers if expected_centers is None else expected_centers
    stored = packet[key]
    if len(stored["center_13"]) != 13 or len(stored["component_total_radius_uppers"]) != 13:
        raise AssertionError(f"A417 {key} dimension changed")
    for row in range(13):
        if stored["center_13"][row]["interval_bounds"] != serializer.complex_interval(
            persisted_centers[row]
        ):
            raise AssertionError(f"A417 {key} center {row} does not replay")
        if not math.isclose(
            radii[row],
            float(stored["component_total_radius_uppers"][row]),
            rel_tol=3.0e-13,
            abs_tol=1.0e-300,
        ):
            raise AssertionError(f"A417 {key} radius {row} does not replay")
    return persisted_centers, radii


def main() -> int:
    ctx.dps = 120
    packet = load(PACKET)
    manifest = load(A413)
    if packet.get("artifact") != "A417":
        raise AssertionError("A417 artifact changed")
    if packet.get("schema") != "MTTQ79HeightFourAll76ThimbleHubAffineSum.v1":
        raise AssertionError("A417 schema changed")
    for label, entry in packet["authority"].items():
        if label == "target_hub_packets":
            continue
        path = ROOT / entry["path"]
        if not path.is_file() or sha256(path) != entry["sha256"]:
            raise AssertionError(f"A417 fixed authority stale: {label}")

    contracts = {
        int(row["distinguished_index"]): row for row in manifest["target_rows"]
    }
    blocks = packet["independent_target_affine_blocks"]
    authorities = packet["authority"]["target_hub_packets"]
    if len(contracts) != 76 or len(blocks) != 76 or len(authorities) != 76:
        raise AssertionError("A417 target inventory changed")
    blocks_by_index = {int(row["distinguished_index"]): row for row in blocks}
    authority_by_index = {
        int(row["distinguished_index"]): row for row in authorities
    }
    if set(blocks_by_index) != set(contracts) or set(authority_by_index) != set(contracts):
        raise AssertionError("A417 target index set changed")

    for index in sorted(contracts):
        contract = contracts[index]
        block = blocks_by_index[index]
        path = source_path(index)
        source = load(path)
        authority = authority_by_index[index]
        if sha256(path) != authority["sha256"]:
            raise AssertionError(f"A417 source authority stale for d{index:03d}")
        if int(block["raw_coefficient"]) != int(contract["endpoint_floating_chain_coefficient"]):
            raise AssertionError(f"A417 raw coefficient changed for d{index:03d}")
        if int(block["effective_coefficient"]) != int(contract["PL_corrected_effective_chain_coefficient"]):
            raise AssertionError(f"A417 effective coefficient changed for d{index:03d}")
        if int(block["PL_wall_delta"]) != int(contract["Picard_Lefschetz_wall_delta"]):
            raise AssertionError(f"A417 PL delta changed for d{index:03d}")
        rows = source["residue_rows"]
        center_key = "hub_affine_center" if index == 57 else "hub_center"
        generator_key = "hub_affine_generator_6_by_6"
        source_centers = [
            [decode_ball(value) for value in row[center_key]] for row in rows
        ]
        generators = [
            decoded_generator(row, generator_key) for row in rows
        ]
        if index == 57:
            aligned_generators = generators
            common_radii: list[float] = []
            expected_mode = "A412_EXISTING_COMMON_AFFINE_FRAME"
            expected_checkpoint = None
        else:
            (
                aligned_generators,
                common_radii,
                expected_checkpoint,
            ) = independently_align_A415_generators(index, source, generators)
            expected_mode = (
                "A414_COMMON_PERIOD_FUNDAMENTAL_COMPONENTWISE_MAX_RADIUS_ENVELOPE"
            )
        expected_centers = [
            interval_hull(
                [source_centers[residue_row][period_row] for residue_row in range(8)]
            )
            for period_row in range(5)
        ] + [source_centers[residue_row][5] for residue_row in range(8)]
        for row in range(13):
            if block["hub_center_13"][row]["interval_bounds"] != serializer.complex_interval(
                expected_centers[row]
            ):
                raise AssertionError(f"A417 center source changed for d{index:03d} row {row}")
        for row in range(5):
            for column in range(5):
                expected = interval_hull(
                    [
                        aligned_generators[residue_row][row, column]
                        for residue_row in range(8)
                    ]
                )
                if block["period_generator_5_by_5"][row][column][
                    "interval_bounds"
                ] != serializer.complex_interval(expected):
                    raise AssertionError(f"A417 period generator changed for d{index:03d}")
        for row in range(8):
            for column in range(5):
                if block["residue_from_period_generator_8_by_5"][row][column][
                    "interval_bounds"
                ] != serializer.complex_interval(aligned_generators[row][5, column]):
                    raise AssertionError(f"A417 residue generator changed for d{index:03d}")
            if block["residue_local_generator_diagonal_8"][row][
                "interval_bounds"
            ] != serializer.complex_interval(aligned_generators[row][5, 5]):
                raise AssertionError(f"A417 local residue generator changed for d{index:03d}")
        alignment = block["period_alignment"]
        if alignment.get("mode") != expected_mode:
            raise AssertionError(f"A417 period alignment mode changed for d{index:03d}")
        if len(alignment["common_period_coordinate_radius_uppers_5"]) != len(
            common_radii
        ) or any(
            not math.isclose(
                float(stored),
                expected,
                rel_tol=3.0e-13,
                abs_tol=1.0e-300,
            )
            for stored, expected in zip(
                alignment["common_period_coordinate_radius_uppers_5"],
                common_radii,
            )
        ):
            raise AssertionError(f"A417 common period radii changed for d{index:03d}")
        if expected_checkpoint is not None:
            if alignment.get("A414_checkpoint") != expected_checkpoint:
                raise AssertionError(
                    f"A417 alignment checkpoint changed for d{index:03d}"
                )
            if not alignment["eight_period_centers_identical_in_checkpoint"]:
                raise AssertionError(
                    f"A417 common period-center flag false for d{index:03d}"
                )
            if not alignment[
                "eight_top_left_fundamental_blocks_identical_in_checkpoint"
            ]:
                raise AssertionError(
                    f"A417 common period-fundamental flag false for d{index:03d}"
                )

    raw_centers, _raw_radii = require_aggregate(packet, "raw_76_sum", "raw_coefficient")
    d065 = blocks_by_index[65]
    d065_center = [decode_ball(value) for value in d065["hub_center_13"]]
    corrected_symbolic_centers = [
        raw_centers[row] + 3 * d065_center[row] for row in range(13)
    ]
    corrected_centers, corrected_radii = require_aggregate(
        packet,
        "PL_corrected_76_sum",
        "effective_coefficient",
        expected_centers=corrected_symbolic_centers,
    )
    if packet["PL_corrected_76_sum"].get("same_source_coefficient_identity_error") != 0:
        raise AssertionError("A417 same-source coefficient identity is not exact")
    summary = packet["summary"]
    if int(summary["certified_target_blocks"]) != 76:
        raise AssertionError("A417 summary target count changed")
    if int(summary["native_y_blocks"]) != 36 or int(summary["native_z_blocks"]) != 40:
        raise AssertionError("A417 chart inventory changed")
    if int(summary["A415_common_period_envelopes"]) != 75:
        raise AssertionError("A417 common-period envelope count changed")
    if not math.isclose(
        max(corrected_radii[5:]),
        float(summary["maximum_PL_corrected_residue_radius_upper"]),
        rel_tol=3.0e-13,
    ):
        raise AssertionError("A417 residue-radius summary changed")
    scope = packet["strict_scope"]
    for key in (
        "all_76_certified_hub_paths_consumed",
        "all_per_target_period_residue_correlations_retained",
        "A414_row_period_frames_aligned_to_common_coordinate_envelopes",
        "independent_target_blocks_combined_by_Minkowski_sum",
        "PL_d065_same_source_correlation_retained",
    ):
        if not scope[key]:
            raise AssertionError(f"A417 closure flag false: {key}")
    for key in (
        "A_handle_hub_block_attached",
        "exact_period_boundary_zero_applied_to_full_hub_sum",
        "beta_minus_B_block_attached",
        "full_common_relative_chain_transport_executed",
        "interval_Newton_existence_and_uniqueness_closed",
        "covariant_zero_proved",
        "full_SM_closure_proved",
    ):
        if scope[key]:
            raise AssertionError(f"A417 overclaims: {key}")
    if scope["observed_SM_values_used"]:
        raise AssertionError("observed SM values entered A417")
    print(
        "PASS: A417 replays all 76 hub affine blocks and the correlated d065 PL correction; "
        f"maximum residue radius {max(corrected_radii[5:]):.6g}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
