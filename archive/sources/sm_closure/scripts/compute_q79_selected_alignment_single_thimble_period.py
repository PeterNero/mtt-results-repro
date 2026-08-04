from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import time
from pathlib import Path

import numpy as np
from flint import acb, arb

from q79_selected_alignment_period_transport import (
    Q79SelectedAlignmentPeriodRootTransport,
    execute_selected_alignment_thimble_period,
)
from q79_selected_alignment_genus2_root_transport import decode_acb
from q79genus2_root_transport import midpoint, radius_upper


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
Y_FIBRATION = DIRECTORY / "selected_alignment_genus2_fibration_seed.interval.packet.json"
Z_FIBRATION = DIRECTORY / "selected_alignment_zchart_genus2_fibration_seed.interval.packet.json"
FAN = DIRECTORY / "selected_alignment_distinguished_radial_fan.interval.packet.json"
HOMOLOGY = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2picardlefschetzmonodromyexecution"
    / "numerical_monodromy_exploration.packet.json"
)
TRAJECTORY_DIRECTORY = DIRECTORY / "selected_alignment_meridian_monodromy"
OUTPUT_DIRECTORY = DIRECTORY / "selected_alignment_thimble_periods"
IDENTITY_ENGINE = ROOT / "scripts" / "q79genus2_period_transport.py"
SELECTED_ADAPTER = ROOT / "scripts" / "q79_selected_alignment_period_transport.py"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def decode_complex(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--distinguished-index", type=int, required=True)
    parser.add_argument("--epsilon", type=float, default=1.0e-5)
    parser.add_argument("--inner-order", type=int, default=160)
    parser.add_argument("--dps", type=int, default=70)
    parser.add_argument("--root-step-ratio", type=float, default=0.12)
    parser.add_argument("--rtol", type=float, default=2.0e-10)
    parser.add_argument("--atol", type=float, default=2.0e-13)
    parser.add_argument("--local-direct-cutoff", type=float, default=0.0)
    parser.add_argument("--local-outer-order", type=int, default=32)
    parser.add_argument("--tail-outer-order", type=int, default=24)
    parser.add_argument(
        "--gauss-manin-chart",
        choices=("t", "frozen_reciprocal"),
        default="t",
    )
    parser.add_argument("--period-omitted-real", type=float)
    parser.add_argument("--period-omitted-imag", type=float)
    parser.add_argument("--line-chart", choices=("y", "z"), default="y")
    parser.add_argument("--no-save", action="store_true")
    return parser.parse_args()


def adapt_reciprocal_trajectory(
    source: Path,
    stem: str,
    common_omitted: complex,
    period_omitted: complex,
) -> tuple[Path, float, float]:
    with np.load(source) as saved:
        w_values = np.asarray(saved["w"], dtype=np.complex128)
        roots = np.asarray(saved["roots"], dtype=np.complex128)
        radii = np.asarray(
            saved["root_radius_uppers"], dtype=np.float64
        )
    shift = common_omitted - period_omitted
    denominators = 1 + shift * roots
    clearance = np.abs(denominators) - abs(shift) * radii
    minimum_clearance = float(np.min(clearance))
    if minimum_clearance <= 0:
        raise AssertionError("reciprocal chart transform meets a root ball")
    transformed_roots = roots / denominators
    transformed_radii = radii / clearance**2
    directory = OUTPUT_DIRECTORY / "adapted_reciprocal_trajectories"
    directory.mkdir(parents=True, exist_ok=True)
    tag = (
        f"{period_omitted.real:+.8g}_{period_omitted.imag:+.8g}i"
        .replace("+", "p")
        .replace("-", "m")
        .replace(".", "d")
    )
    output = directory / f"{stem}.omitted_{tag}.trajectory.npz"
    np.savez_compressed(
        output,
        w=w_values,
        roots=transformed_roots,
        root_radius_uppers=transformed_radii,
    )
    return output, minimum_clearance, float(np.max(transformed_radii))


def adapt_y_to_z_approach_trajectory(
    source: Path,
    stem: str,
    critical_center: complex,
    homology_convention: dict,
    common_omitted: complex,
) -> tuple[Path, dict[str, str | int]]:
    with np.load(source) as saved:
        w_values = np.asarray(saved["w"], dtype=np.complex128)
        roots_y = np.asarray(saved["roots"], dtype=np.complex128)
        radii_y = np.asarray(
            saved["root_radius_uppers"], dtype=np.float64
        )
    distances = np.abs(w_values - critical_center)
    minimum = float(np.min(distances))
    candidates = np.flatnonzero(distances <= minimum * 1.001)
    if not len(candidates):
        raise AssertionError("selected y trajectory has no approach point")
    index = int(candidates[0])
    w_value = complex(w_values[index])
    transport = Q79SelectedAlignmentPeriodRootTransport(
        Z_FIBRATION,
        homology_convention,
        omitted=common_omitted,
        dps=80,
    )
    a_value, b_value = transport.ab_at(w_value)
    alignment_packet = load(Z_FIBRATION)
    alignment = [
        [decode_acb(value) for value in row]
        for row in alignment_packet["source"]["alignment_interval"]
    ]
    elliptic = [a_value, b_value, acb(1)]
    line = [
        sum(
            (alignment[row][column] * elliptic[column] for column in range(3)),
            acb(0),
        )
        for row in range(3)
    ]
    line_1_lower = float(abs(line[1]).lower())
    line_2_lower = float(abs(line[2]).lower())
    if min(line_1_lower, line_2_lower) <= 0:
        raise AssertionError("projective y/z chart overlap is not certified")
    omitted_ball = acb(
        format(common_omitted.real, ".17g"),
        format(common_omitted.imag, ".17g"),
    )
    transformed_centers: list[complex] = []
    transformed_radii: list[float] = []
    for root, radius in zip(roots_y[index], radii_y[index]):
        root_ball = acb(
            arb(format(root.real, ".17g"), format(radius, ".17g")),
            arb(format(root.imag, ".17g"), format(radius, ".17g")),
        )
        t_y = omitted_ball + 1 / root_ball
        t_z = -(line[0] + line[2] * t_y) / line[1]
        s_z = 1 / (t_z - omitted_ball)
        transformed_centers.append(midpoint(s_z))
        transformed_radii.append(radius_upper(s_z))
    minimum_separation = min(
        abs(transformed_centers[left] - transformed_centers[right])
        - transformed_radii[left]
        - transformed_radii[right]
        for left in range(6)
        for right in range(left)
    )
    if minimum_separation <= 0:
        raise AssertionError("transformed z-chart approach balls overlap")
    directory = OUTPUT_DIRECTORY / "adapted_line_chart_approaches"
    directory.mkdir(parents=True, exist_ok=True)
    output = directory / f"{stem}.y_to_z_approach.trajectory.npz"
    np.savez_compressed(
        output,
        w=np.asarray([w_value], dtype=np.complex128),
        roots=np.asarray([transformed_centers], dtype=np.complex128),
        root_radius_uppers=np.asarray(
            [transformed_radii], dtype=np.float64
        ),
    )
    return output, {
        "source_approach_index": index,
        "line_L1_absolute_lower": format(line_1_lower, ".17g"),
        "line_L2_absolute_lower": format(line_2_lower, ".17g"),
        "transformed_root_ball_minimum_separation_lower": format(
            minimum_separation, ".17g"
        ),
        "transformed_root_ball_maximum_radius_upper": format(
            max(transformed_radii), ".17g"
        ),
    }


def align_z_execution_orientation(
    execution: dict,
    orientation_reference: dict,
    homology_convention: dict,
) -> dict[str, str | int]:
    def value(pair: dict[str, str]) -> complex:
        return complex(float(pair["real"]), float(pair["imaginary"]))

    reference_periods = np.asarray(
        [
            value(row["value"])
            for row in orientation_reference["execution"][
                "base_fiber_propagated_periods"
            ]
        ],
        dtype=np.complex128,
    )
    z_periods = np.asarray(
        [
            value(row["value"])
            for row in execution["base_fiber_propagated_periods"]
        ],
        dtype=np.complex128,
    )
    reference_chart = orientation_reference.get("line_chart", "y")
    if reference_chart == "z":
        expected_z = reference_periods
        reference_route = "existing oriented z-chart baseline"
    else:
        transport = Q79SelectedAlignmentPeriodRootTransport(
            Y_FIBRATION,
            homology_convention,
            omitted=2 + 3j,
            dps=80,
        )
        a_value, b_value = [
            midpoint(value) for value in transport.ab_at(transport.base)
        ]
        y_packet = load(Y_FIBRATION)
        alignment = np.asarray(
            [
                [midpoint(decode_acb(value)) for value in row]
                for row in y_packet["source"]["alignment_interval"]
            ],
            dtype=np.complex128,
        )
        line = alignment @ np.asarray([a_value, b_value, 1 + 0j])
        alpha = -line[0] / line[1]
        gamma = -line[2] / line[1]
        common = -(line[1] ** 2) / (line[2] ** 2)
        transition = np.zeros((5, 5), dtype=np.complex128)
        for power in range(5):
            for index in range(power + 1):
                transition[power, index] = (
                    common
                    * math.comb(power, index)
                    * alpha ** (power - index)
                    * gamma**index
                )
        expected_z = transition @ reference_periods
        reference_route = "A123 y-to-z five-period transition"
    plus = float(np.max(abs(z_periods - expected_z)))
    minus = float(np.max(abs(z_periods + expected_z)))
    sign = 1 if plus <= minus else -1
    if sign == -1:
        for pair in execution["period_values"]:
            pair["real"] = format(-float(pair["real"]), ".17g")
            pair["imaginary"] = format(-float(pair["imaginary"]), ".17g")
        for row in execution["base_fiber_propagated_periods"]:
            pair = row["value"]
            pair["real"] = format(-float(pair["real"]), ".17g")
            pair["imaginary"] = format(-float(pair["imaginary"]), ".17g")
        for pair in execution[
            "base_fiber_holomorphic_periods_dt_over_u_and_t_dt_over_u"
        ]:
            pair["real"] = format(-float(pair["real"]), ".17g")
            pair["imaginary"] = format(-float(pair["imaginary"]), ".17g")
    return {
        "selected_sign": sign,
        "reference_route": reference_route,
        "plus_sign_maximum_base_transition_residual": format(plus, ".17g"),
        "minus_sign_maximum_base_transition_residual": format(minus, ".17g"),
        "opposite_sign_residual_ratio": format(
            max(plus, minus) / max(min(plus, minus), np.finfo(float).tiny),
            ".17g",
        ),
    }


def main() -> int:
    arguments = parse_args()
    if not 1 <= arguments.distinguished_index <= 90:
        raise ValueError("distinguished index must lie in 1,...,90")
    started = time.perf_counter()
    fan = load(FAN)
    homology = load(HOMOLOGY)
    row = next(
        value
        for value in fan["distinguished_positive_meridians"]
        if value["distinguished_index"] == arguments.distinguished_index
    )
    fibration = Y_FIBRATION if arguments.line_chart == "y" else Z_FIBRATION
    stem = f"d{arguments.distinguished_index:03d}_{row['root_id']}"
    output_path = OUTPUT_DIRECTORY / f"{stem}.thimble_period.candidate.json"
    orientation_reference = None
    if arguments.line_chart == "z":
        if not output_path.exists():
            raise FileNotFoundError(
                "z-chart execution requires the preceding y-chart packet for orientation"
            )
        orientation_reference = load(output_path)
    trajectory_packet_path = TRAJECTORY_DIRECTORY / f"{stem}.packet.json"
    source_trajectory_packet = load(trajectory_packet_path)
    trajectory_path = ROOT / source_trajectory_packet["trajectory"]["path"]
    if sha256(trajectory_path) != source_trajectory_packet["trajectory"]["sha256"]:
        raise AssertionError("selected trajectory hash mismatch")
    common_omitted = decode_complex(
        source_trajectory_packet["branch_chart"]["common_omitted_point"]
    )
    if common_omitted != 2 + 3j:
        raise AssertionError("selected reciprocal chart changed")
    omitted_arguments = (
        arguments.period_omitted_real,
        arguments.period_omitted_imag,
    )
    if (omitted_arguments[0] is None) != (omitted_arguments[1] is None):
        raise ValueError("both period omitted-point coordinates are required")
    period_omitted = (
        common_omitted
        if omitted_arguments[0] is None
        else complex(omitted_arguments[0], omitted_arguments[1])
    )
    trajectory_packet = copy.deepcopy(source_trajectory_packet)
    transform_clearance = None
    transformed_radius = None
    line_chart_transform = None
    if arguments.line_chart == "z":
        if period_omitted != common_omitted:
            raise ValueError("z line-chart execution uses the common omitted point")
        if arguments.gauss_manin_chart != "t":
            raise ValueError("z line-chart execution currently uses t periods")
        trajectory_path, line_chart_transform = adapt_y_to_z_approach_trajectory(
            trajectory_path,
            stem,
            decode_complex(row["canonical_lift"]),
            homology["homology_convention"],
            common_omitted,
        )
    elif period_omitted != common_omitted:
        if arguments.gauss_manin_chart != "frozen_reciprocal":
            raise ValueError("an alternate omitted point requires reciprocal periods")
        trajectory_path, transform_clearance, transformed_radius = (
            adapt_reciprocal_trajectory(
                trajectory_path,
                stem,
                common_omitted,
                period_omitted,
            )
        )

    execution = execute_selected_alignment_thimble_period(
        fibration_path=fibration,
        homology_convention=homology["homology_convention"],
        trajectory_path=trajectory_path,
        trajectory_packet=trajectory_packet,
        critical_center=decode_complex(row["canonical_lift"]),
        omitted=period_omitted,
        epsilon=arguments.epsilon,
        inner_order=arguments.inner_order,
        dps=arguments.dps,
        root_step_ratio=arguments.root_step_ratio,
        rtol=arguments.rtol,
        atol=arguments.atol,
        gauss_manin_chart=arguments.gauss_manin_chart,
        local_direct_cutoff=arguments.local_direct_cutoff,
        local_outer_order=arguments.local_outer_order,
        tail_outer_order=arguments.tail_outer_order,
    )
    orientation_alignment = None
    if arguments.line_chart == "z":
        orientation_alignment = align_z_execution_orientation(
            execution,
            orientation_reference,
            homology["homology_convention"],
        )
    packet = {
        "schema": "MTTQ79SelectedAlignmentSingleThimblePeriodCandidate.v1",
        "status": "SELECTED_ALIGNMENT_THIMBLE_PERIOD_FLOATING_CANDIDATE_COMPUTED",
        "distinguished_index": arguments.distinguished_index,
        "root_id": row["root_id"],
        "critical_center": row["canonical_lift"],
        "line_chart": arguments.line_chart,
        "Gauss_Manin_chart": arguments.gauss_manin_chart,
        "period_omitted_point": {
            "real": format(period_omitted.real, ".17g"),
            "imaginary": format(period_omitted.imag, ".17g"),
        },
        "orientation_alignment": orientation_alignment,
        "authority": {
            "fibration_sha256": sha256(fibration),
            "distinguished_fan_sha256": sha256(FAN),
            "homology_convention_sha256": sha256(HOMOLOGY),
            "trajectory_packet_sha256": sha256(trajectory_packet_path),
            "source_trajectory_npz_sha256": source_trajectory_packet[
                "trajectory"
            ]["sha256"],
            "period_chart_trajectory_npz_sha256": sha256(trajectory_path),
            "unchanged_identity_period_engine_sha256": sha256(IDENTITY_ENGINE),
            "selected_period_adapter_sha256": sha256(SELECTED_ADAPTER),
        },
        "execution": execution,
        "elapsed_seconds": format(time.perf_counter() - started, ".17g"),
        "strict_scope": {
            "same_selected_carrier_as_A127_beta": True,
            "A128_certified_trajectory_consumed": True,
            "A123_projective_line_chart_covariance_consumed": (
                arguments.line_chart == "z"
            ),
            "line_chart_transform_certificate": line_chart_transform,
            "reciprocal_ball_transform_minimum_denominator_clearance": (
                None
                if transform_clearance is None
                else format(transform_clearance, ".17g")
            ),
            "reciprocal_ball_transform_maximum_radius_upper": (
                None
                if transformed_radius is None
                else format(transformed_radius, ".17g")
            ),
            "observed_SM_values_used": False,
            "floating_period_candidate_only": True,
            "interval_period_enclosure": False,
        },
    }
    if not arguments.no_save:
        OUTPUT_DIRECTORY.mkdir(parents=True, exist_ok=True)
        output_path.write_text(
            json.dumps(packet, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        print(f"wrote {output_path}")
    print(json.dumps(packet, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
