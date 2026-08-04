from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

from flint import acb, acb_mat, arb, ctx

import certify_q79_selected_side_base_lift_interval as serializer
import certify_q79_selected_side_beta_defect_transport as validated


ROOT = Path(__file__).resolve().parents[1]
VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
DIRECTORY = VALIDATED / "ol"
A403 = VALIDATED / "n3.common_junction_edge_ledger.a403.json"
A409T = VALIDATED / "n3.junction_reverse_composition.a409t.json"
A413 = DIRECTORY / "all76.a413.json"
OUTPUT = DIRECTORY / "hub.a417.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourAll76ThimbleHubAffineSum_A417_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def authority(path: Path) -> dict[str, str]:
    return {"path": relative(path), "sha256": sha256(path)}


def decode_ball(value: dict) -> acb:
    return validated.interval_from_bounds(value["interval_bounds"])


def encoded_ball(value: acb) -> dict:
    bounds = serializer.complex_interval(value)
    persisted = validated.interval_from_bounds(bounds)
    center = validated.midpoint(persisted)
    return {
        "interval_bounds": bounds,
        "interval_center": {
            "real": format(center.real, ".17g"),
            "imaginary": format(center.imag, ".17g"),
        },
        "interval_radius_upper": validated.radius_upper(persisted),
    }


def encoded_matrix(matrix: acb_mat) -> list[list[dict]]:
    return [
        [encoded_ball(matrix[row, col]) for col in range(matrix.ncols())]
        for row in range(matrix.nrows())
    ]


def packet_path(index: int) -> Path:
    return DIRECTORY / ("d057.a412.json" if index == 57 else f"d{index:03d}.a415.json")


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


def align_A415_period_coordinates(
    index: int,
    packet: dict,
    generators: list[acb_mat],
) -> tuple[list[acb_mat], dict]:
    checkpoint_authority = packet["authority"]["A414_correlated_checkpoint"]
    checkpoint_path = ROOT / checkpoint_authority["path"]
    if not checkpoint_path.is_file() or sha256(checkpoint_path) != checkpoint_authority["sha256"]:
        raise AssertionError(f"d{index:03d} A414 alignment checkpoint is stale")
    checkpoint = load(checkpoint_path)
    frames = checkpoint["frames"]
    centers = checkpoint["centers"]
    if len(frames) != 8 or len(centers) != 8:
        raise AssertionError(f"d{index:03d} A414 row inventory changed")

    reference_center = centers[0][:5]
    reference_fundamental = frames[0]["fundamental"]
    coordinate_radii: list[list[arb]] = []
    for residue_row in range(8):
        if centers[residue_row][:5] != reference_center:
            raise AssertionError(f"d{index:03d} A414 period centers are not common")
        for row in range(5):
            if (
                frames[residue_row]["fundamental"][row][:5]
                != reference_fundamental[row][:5]
            ):
                raise AssertionError(
                    f"d{index:03d} A414 period fundamental block is not common"
                )
        radii = [arb(value) for value in frames[residue_row]["coordinate_radii"][:5]]
        if any(validated.lower(value) <= 0.0 for value in radii):
            raise AssertionError(f"d{index:03d} A414 period radius is not positive")
        coordinate_radii.append(radii)

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
    return aligned, {
        "mode": "A414_COMMON_PERIOD_FUNDAMENTAL_COMPONENTWISE_MAX_RADIUS_ENVELOPE",
        "A414_checkpoint": authority(checkpoint_path),
        "common_period_coordinate_radius_uppers_5": [
            validated.upper(value) for value in common_radii
        ],
        "eight_period_centers_identical_in_checkpoint": True,
        "eight_top_left_fundamental_blocks_identical_in_checkpoint": True,
    }


def extract_block(
    index: int, packet: dict
) -> tuple[list[acb], acb_mat, acb_mat, list[acb], dict]:
    rows = packet["residue_rows"]
    if len(rows) != 8:
        raise AssertionError(f"d{index:03d} lost an A417 residue row")
    center_key = "hub_affine_center" if index == 57 else "hub_center"
    generator_key = "hub_affine_generator_6_by_6"
    centers_by_row = [[decode_ball(value) for value in row[center_key]] for row in rows]
    generators = [
        acb_mat([[decode_ball(value) for value in matrix_row] for matrix_row in row[generator_key]])
        for row in rows
    ]
    if any(len(center) != 6 for center in centers_by_row):
        raise AssertionError(f"d{index:03d} hub center dimension changed")
    if index == 57:
        aligned_generators = generators
        alignment = {
            "mode": "A412_EXISTING_COMMON_AFFINE_FRAME",
            "common_period_coordinate_radius_uppers_5": [],
        }
    else:
        aligned_generators, alignment = align_A415_period_coordinates(
            index, packet, generators
        )

    center = [
        interval_hull([centers_by_row[row][period_row] for row in range(8)])
        for period_row in range(5)
    ] + [centers_by_row[row][5] for row in range(8)]
    period_generator = acb_mat(5, 5)
    residue_from_period = acb_mat(8, 5)
    residue_local = []
    for row in range(5):
        for column in range(5):
            period_generator[row, column] = interval_hull(
                [
                    aligned_generators[residue_row][row, column]
                    for residue_row in range(8)
                ]
            )
        if any(
            not aligned_generators[residue_row][row, 5].contains(0)
            for residue_row in range(8)
        ):
            raise AssertionError(
                f"d{index:03d} local residue error enters a period row"
            )
    for row in range(8):
        for column in range(5):
            residue_from_period[row, column] = aligned_generators[row][5, column]
        residue_local.append(aligned_generators[row][5, 5])
    alignment["maximum_period_center_midpoint_spread"] = max(
        abs(
            validated.midpoint(centers_by_row[row][period_row])
            - validated.midpoint(centers_by_row[0][period_row])
        )
        for row in range(8)
        for period_row in range(5)
    )
    alignment["maximum_aligned_period_generator_midpoint_spread"] = max(
        abs(
            validated.midpoint(aligned_generators[row][period_row, column])
            - validated.midpoint(aligned_generators[0][period_row, column])
        )
        for row in range(8)
        for period_row in range(5)
        for column in range(5)
    )
    return center, period_generator, residue_from_period, residue_local, alignment


def block_component_generator_radius(block: dict, row: int) -> arb:
    coefficient = abs(int(block["coefficient"]))
    if row < 5:
        matrix = block["period_generator"]
        return arb(coefficient) * sum(
            (abs(matrix[row, column]) for column in range(5)), arb(0)
        )
    residue_row = row - 5
    matrix = block["residue_from_period"]
    return arb(coefficient) * (
        sum((abs(matrix[residue_row, column]) for column in range(5)), arb(0))
        + abs(block["residue_local"][residue_row])
    )


def aggregate(blocks: list[dict], coefficient_name: str) -> tuple[list[acb], list[float]]:
    centers = [acb(0) for _ in range(13)]
    generator_radii = [arb(0) for _ in range(13)]
    for source in blocks:
        coefficient = int(source[coefficient_name])
        scaled = {**source, "coefficient": coefficient}
        for row in range(13):
            centers[row] += coefficient * source["center"][row]
            generator_radii[row] += block_component_generator_radius(scaled, row)
    total_radii = [
        validated.radius_upper(centers[row]) + validated.upper(generator_radii[row])
        for row in range(13)
    ]
    return centers, total_radii


def decode_serialized_block(block: dict) -> dict:
    return {
        "distinguished_index": int(block["distinguished_index"]),
        "line_chart": block["line_chart"],
        "raw_coefficient": int(block["raw_coefficient"]),
        "PL_wall_delta": int(block["PL_wall_delta"]),
        "effective_coefficient": int(block["effective_coefficient"]),
        "center": [decode_ball(value) for value in block["hub_center_13"]],
        "period_generator": acb_mat(
            [
                [decode_ball(value) for value in row]
                for row in block["period_generator_5_by_5"]
            ]
        ),
        "residue_from_period": acb_mat(
            [
                [decode_ball(value) for value in row]
                for row in block["residue_from_period_generator_8_by_5"]
            ]
        ),
        "residue_local": [
            decode_ball(value)
            for value in block["residue_local_generator_diagonal_8"]
        ],
        "period_alignment": block["period_alignment"],
    }


def main() -> int:
    ctx.dps = 120
    junction = load(A403)
    reverse = load(A409T)
    manifest = load(A413)
    if not junction["strict_scope"]["aggregate_common_trunk_cancellation_proved"]:
        raise AssertionError("A417 requires A403 zero-trunk closure")
    if not reverse["strict_scope"]["selected_physical_residue_sign_bridge_proved"]:
        raise AssertionError("A417 requires the A409T physical-residue bridge")
    contracts = manifest["target_rows"]
    if len(contracts) != 76 or len({int(row["distinguished_index"]) for row in contracts}) != 76:
        raise AssertionError("A417 requires all 76 unique A413 targets")

    blocks = []
    packet_authority = []
    pl_targets = []
    for contract in sorted(contracts, key=lambda row: int(row["distinguished_index"])):
        index = int(contract["distinguished_index"])
        path = packet_path(index)
        if not path.is_file():
            raise FileNotFoundError(f"A417 missing certified hub packet {path.name}")
        packet = load(path)
        expected_artifact = "A412" if index == 57 else "A415"
        if packet.get("artifact") != expected_artifact:
            raise AssertionError(f"d{index:03d} hub artifact changed")
        scope = packet["strict_scope"]
        if not scope["single_d057_alternate_path_composition_closed" if index == 57 else "single_target_alternate_path_composition_closed"]:
            raise AssertionError(f"d{index:03d} alternate path is not closed")
        raw = int(contract["endpoint_floating_chain_coefficient"])
        effective = int(contract["PL_corrected_effective_chain_coefficient"])
        delta = int(contract["Picard_Lefschetz_wall_delta"])
        if effective != raw + delta:
            raise AssertionError(f"d{index:03d} PL coefficient identity changed")
        if delta:
            pl_targets.append(index)
        (
            center,
            period_generator,
            residue_from_period,
            residue_local,
            period_alignment,
        ) = extract_block(index, packet)
        blocks.append(
            {
                "distinguished_index": index,
                "line_chart": contract["line_chart"],
                "raw_coefficient": raw,
                "PL_wall_delta": delta,
                "effective_coefficient": effective,
                "center": center,
                "period_generator": period_generator,
                "residue_from_period": residue_from_period,
                "residue_local": residue_local,
                "period_alignment": period_alignment,
            }
        )
        packet_authority.append(
            {
                "distinguished_index": index,
                "artifact": expected_artifact,
                **authority(path),
            }
        )
    if pl_targets != [65]:
        raise AssertionError("A417 expected exactly the selected d065 PL correction")

    serialized_blocks = []
    for block in blocks:
        serialized_blocks.append(
            {
                "distinguished_index": block["distinguished_index"],
                "line_chart": block["line_chart"],
                "raw_coefficient": block["raw_coefficient"],
                "PL_wall_delta": block["PL_wall_delta"],
                "effective_coefficient": block["effective_coefficient"],
                "hub_center_13": [encoded_ball(value) for value in block["center"]],
                "period_generator_5_by_5": encoded_matrix(block["period_generator"]),
                "residue_from_period_generator_8_by_5": encoded_matrix(
                    block["residue_from_period"]
                ),
                "residue_local_generator_diagonal_8": [
                    encoded_ball(value) for value in block["residue_local"]
                ],
                "period_alignment": block["period_alignment"],
            }
        )
    persisted_blocks = [
        decode_serialized_block(block) for block in serialized_blocks
    ]
    raw_centers, raw_radii = aggregate(persisted_blocks, "raw_coefficient")
    direct_effective_centers, effective_radii = aggregate(
        persisted_blocks, "effective_coefficient"
    )
    d065 = next(
        block for block in persisted_blocks if block["distinguished_index"] == 65
    )
    effective_centers = [
        raw_centers[row] + 3 * d065["center"][row] for row in range(13)
    ]
    direct_center_midpoint_differences = [
        abs(
            validated.midpoint(effective_centers[row])
            - validated.midpoint(direct_effective_centers[row])
        )
        for row in range(13)
    ]

    payload = {
        "schema": "MTTQ79HeightFourAll76ThimbleHubAffineSum.v1",
        "status": "ALL_76_THIMBLE_HUB_AFFINE_BLOCKS_AND_SAME_SOURCE_PL_CORRECTION_CLOSED",
        "artifact": "A417",
        "coordinate_order": [
            "period_0",
            "period_1",
            "period_2",
            "period_3",
            "period_4",
            *[f"residue_{index}" for index in range(8)],
        ],
        "independent_target_affine_blocks": serialized_blocks,
        "raw_76_sum": {
            "center_13": [encoded_ball(value) for value in raw_centers],
            "component_total_radius_uppers": raw_radii,
        },
        "PL_corrected_76_sum": {
            "center_13": [encoded_ball(value) for value in effective_centers],
            "component_total_radius_uppers": effective_radii,
            "identity": "C_76_PL=C_76_raw+3*C_d065 using the same d065 affine block",
            "same_source_coefficient_identity_error": 0,
            "maximum_direct_effective_center_midpoint_replay_difference": max(
                direct_center_midpoint_differences
            ),
        },
        "summary": {
            "certified_target_blocks": len(blocks),
            "native_y_blocks": sum(block["line_chart"] == "y" for block in blocks),
            "native_z_blocks": sum(block["line_chart"] == "z" for block in blocks),
            "shared_period_source_coordinates_per_target": 5,
            "independent_residue_remainder_coordinates_per_target": 8,
            "maximum_PL_corrected_period_radius_upper": max(effective_radii[:5]),
            "maximum_PL_corrected_residue_radius_upper": max(effective_radii[5:]),
            "PL_correction_target": 65,
            "PL_correction_delta": 3,
            "A415_common_period_envelopes": sum(
                block["period_alignment"]["mode"]
                == "A414_COMMON_PERIOD_FUNDAMENTAL_COMPONENTWISE_MAX_RADIUS_ENVELOPE"
                for block in blocks
            ),
            "maximum_common_period_center_midpoint_spread": max(
                block["period_alignment"]["maximum_period_center_midpoint_spread"]
                for block in blocks
            ),
            "maximum_aligned_period_generator_midpoint_spread": max(
                block["period_alignment"][
                    "maximum_aligned_period_generator_midpoint_spread"
                ]
                for block in blocks
            ),
        },
        "authority": {
            "A403_zero_trunk_theorem": authority(A403),
            "A409T_physical_residue_bridge": authority(A409T),
            "A413_source_manifest": authority(A413),
            "builder_source": authority(Path(__file__).resolve()),
            "target_hub_packets": packet_authority,
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "all_76_certified_hub_paths_consumed": True,
            "all_per_target_period_residue_correlations_retained": True,
            "A414_row_period_frames_aligned_to_common_coordinate_envelopes": True,
            "independent_target_blocks_combined_by_Minkowski_sum": True,
            "PL_d065_same_source_correlation_retained": True,
            "A_handle_hub_block_attached": False,
            "exact_period_boundary_zero_applied_to_full_hub_sum": False,
            "beta_minus_B_block_attached": False,
            "full_common_relative_chain_transport_executed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "construct the selected A-handle outer hub block in the same 13-state "
            "coordinate convention, apply the A403 exact period-boundary zero, "
            "then splice the result to the correlated A402 beta-minus-B block"
        ),
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(
        "# MTT q79 Height-Four All-76 Thimble Hub Affine Sum (A417) v1\n\n"
        "A417 consumes every certified A412/A415 hub state and assembles one "
        "13-coordinate affine block per selected thimble. Five source-error "
        "coordinates are shared across that thimble's periods and eight residue "
        "rows; the eight row remainders remain independent.\n\n"
        "The Picard-Lefschetz correction is applied as the same d065 block with "
        "coefficient delta `+3`, not as an independent interval copy. The A-handle, "
        "exact aggregate period cancellation, A402 splice, Newton inclusion, "
        "covariant zero, and full SM closure remain open.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
