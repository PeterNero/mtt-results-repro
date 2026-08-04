from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from flint import acb, acb_mat, acb_poly, arb, ctx

import certify_q79_selected_side_beta_defect_transport as validated
from q79genus2_period_transport import FORM_NAMES


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
PERIOD_DIRECTORY = DIRECTORY / "selected_alignment_thimble_periods"
HOMOLOGY = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2picardlefschetzmonodromyexecution"
    / "numerical_monodromy_exploration.packet.json"
)
ORIENTATION = PERIOD_DIRECTORY / "selected_alignment_thimble_orientation_synchronization.packet.json"
HANDLES = PERIOD_DIRECTORY / "selected_alignment_primitive_handle_periods.packet.json"
A133 = PERIOD_DIRECTORY / "selected_alignment_height4_frozen_carrier_refinement_and_interval_cutset.packet.json"
DEFAULT_OUTPUT = PERIOD_DIRECTORY / "selected_alignment_E32_handle_combination.interval.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def midpoint(value: acb) -> complex:
    return complex(float(value.real.mid()), float(value.imag.mid()))


def radius_upper(value: acb) -> float:
    return validated.upper(value.rad())


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def complex_pair(value: complex) -> dict[str, str]:
    return {
        "real": format(float(value.real), ".17g"),
        "imaginary": format(float(value.imag), ".17g"),
    }


def complex_interval(value: acb) -> dict[str, dict[str, str]]:
    return {
        "real": {
            "lower": format(validated.lower(value.real), ".17g"),
            "upper": format(validated.upper(value.real), ".17g"),
        },
        "imaginary": {
            "lower": format(validated.lower(value.imag), ".17g"),
            "upper": format(validated.upper(value.imag), ".17g"),
        },
    }


def selected_base_roots(
    system: validated.SelectedQ79IntervalSystem,
) -> tuple[list[acb], acb]:
    _a, _b, line, line_derivative = system.ab_line_data(acb(0))
    coefficients, _derivative = validated.aligned_coefficients_and_derivative(
        system.evaluator.tables["F6"], line, line_derivative, chart="y"
    )
    roots = acb_poly(coefficients).roots(tol=1e-55, maxprec=8192)
    if len(roots) != 6:
        raise AssertionError("selected base sextic root isolation failed")
    rotation = complex(np.exp(-1j * np.pi / 7))
    roots.sort(key=lambda value: (rotation * midpoint(value)).real)
    minimum_separation = min(
        validated.lower(abs(roots[left] - roots[right]))
        for left in range(6)
        for right in range(left)
    )
    if minimum_separation <= 0:
        raise AssertionError("selected base root balls overlap")
    return roots, coefficients[6]


def rotations() -> list[acb]:
    return [
        acb(
            format(math.cos(index * math.pi / 8), ".17g"),
            format(math.sin(index * math.pi / 8), ".17g"),
        )
        for index in range(16)
    ]


def direct_cut_periods(
    roots: list[acb],
    leading: acb,
    pair: tuple[int, int],
    *,
    segments: int,
    tolerance: float,
) -> tuple[list[acb], dict]:
    first, second = roots[pair[0]], roots[pair[1]]
    center = (first + second) / acb(2)
    half = (second - first) / acb(2)
    others = [root for index, root in enumerate(roots) if index not in pair]
    total = [acb(0) for _ in range(5)]
    previous_root: acb | None = None
    minimum_half_plane_margin = math.inf
    minimum_sign_margin = math.inf
    integral_count = 0

    for segment in range(segments):
        left = math.pi * segment / segments
        right = math.pi * (segment + 1) / segments
        theta_box = acb(
            arb(
                format((left + right) / 2, ".17g"),
                format((right - left) / 2, ".17g"),
            )
        )
        point_box = center + half * theta_box.cos()
        remainder_box = leading
        for root in others:
            remainder_box *= point_box - root
        rotation_rows = [
            (rotation, validated.lower((rotation * remainder_box).real))
            for rotation in rotations()
        ]
        rotation, margin = max(rotation_rows, key=lambda row: row[1])
        if margin <= 0:
            raise AssertionError("cut remainder does not fit a square-root half-plane")
        minimum_half_plane_margin = min(minimum_half_plane_margin, margin)
        rotation_root = rotation.sqrt()

        def root(theta: acb, analytic: bool) -> acb:
            point = center + half * theta.cos()
            remainder = leading
            for other in others:
                remainder *= point - other
            rotated = rotation * remainder
            if analytic and not rotated.real.lower() > 0:
                return acb("nan")
            return rotated.sqrt(analytic=analytic) / rotation_root

        candidate = root(acb(format(left, ".17g")), False)
        sign = 1
        if previous_root is not None:
            same_upper = validated.upper(abs(candidate - previous_root))
            opposite_lower = validated.lower(abs(candidate + previous_root))
            opposite_upper = validated.upper(abs(candidate + previous_root))
            same_lower = validated.lower(abs(candidate - previous_root))
            if same_upper < opposite_lower:
                sign = 1
                sign_margin = opposite_lower - same_upper
            elif opposite_upper < same_lower:
                sign = -1
                sign_margin = same_lower - opposite_upper
            else:
                raise AssertionError("cut square-root sign is not interval-separated")
            minimum_sign_margin = min(minimum_sign_margin, sign_margin)

        width = right - left

        def integrand(parameter: acb, analytic: bool, power: int) -> acb:
            theta = acb(format(left, ".17g")) + parameter * acb(
                format(width, ".17g")
            )
            point = center + half * theta.cos()
            denominator = root(theta, analytic)
            if not denominator.is_finite():
                return denominator
            return (
                acb(0, 2 * sign)
                * point**power
                * acb(format(width, ".17g"))
                / denominator
            )

        for power in range(5):
            addition = acb.integral(
                lambda parameter, analytic, p=power: integrand(
                    parameter, analytic, p
                ),
                acb(0),
                acb(1),
                rel_tol=tolerance,
                abs_tol=tolerance,
                depth_limit=20,
                eval_limit=200000,
            )
            if not addition.is_finite():
                raise ArithmeticError("nonfinite direct cut integral")
            total[power] += addition
            integral_count += 1
        previous_root = acb(sign) * root(acb(format(right, ".17g")), False)

    return total, {
        "pair_zero_based": list(pair),
        "theta_segments": segments,
        "integral_count": integral_count,
        "minimum_half_plane_margin": minimum_half_plane_margin,
        "minimum_sign_margin": (
            None if not math.isfinite(minimum_sign_margin) else minimum_sign_margin
        ),
        "period_centers": [complex_pair(midpoint(value)) for value in total],
        "maximum_component_radius": max(radius_upper(value) for value in total),
    }


def reference_sigma_periods() -> tuple[np.ndarray, np.ndarray]:
    packet = load(ORIENTATION)
    marked = np.asarray(
        [
            [complex_value(value) for value in row]
            for row in packet["marked_base_period_matrix"]
        ],
        dtype=np.complex128,
    )
    if marked.shape != (5, 4):
        raise AssertionError("marked base period shape changed")
    sigma3 = -marked[:, 0] + marked[:, 2]
    sigma4 = marked[:, 3]
    return sigma3, sigma4


def orient_cut(
    interval_periods: list[acb], reference: np.ndarray
) -> tuple[list[acb], int, float, float]:
    centers = np.asarray([midpoint(value) for value in interval_periods])
    plus = float(np.max(np.abs(centers - reference)))
    minus = float(np.max(np.abs(-centers - reference)))
    sign = 1 if plus <= minus else -1
    selected = plus if sign == 1 else minus
    rejected = minus if sign == 1 else plus
    if rejected <= 1000 * max(selected, 1.0e-15):
        raise AssertionError("base cut orientation is not numerically separated")
    return [acb(sign) * value for value in interval_periods], sign, selected, rejected


def homogeneous_builder(
    original,
    system: validated.SelectedQ79IntervalSystem,
    start: complex,
    direction: complex,
    step: float,
    order: int,
):
    matrix, forcing, diagnostics = original(system, start, direction, step, order)
    zero = forcing[0].constant(0, forcing[0].order, forcing[0].radius)
    return matrix, [zero for _ in forcing], diagnostics


def validated_handle_transport(
    system: validated.SelectedQ79IntervalSystem,
    initial_periods: list[acb],
    *,
    order: int,
    initial_step: float,
    minimum_step: float,
) -> dict:
    center = [system.midpoint_acb(value) for value in initial_periods] + [
        acb(0) for _ in range(8)
    ]
    identity = acb_mat(5, 5)
    for index in range(5):
        identity[index, index] = acb(1)
    lift_frame = validated.LiftErrorFrame(
        fundamental=identity,
        coordinate_radii=[value.rad().upper() for value in initial_periods],
    )
    integral_radius = arb(0)
    start = 0 + 0j
    endpoint = 0 - 1j
    direction = (endpoint - start) / abs(endpoint - start)
    position = 0.0
    proposed = initial_step
    accepted: list[dict] = []
    rejected = 0
    minimum_accepted = math.inf
    original = validated.build_taylor_system
    validated.build_taylor_system = lambda *args, **kwargs: homogeneous_builder(
        original, *args, **kwargs
    )
    try:
        while position < 1.0:
            step = min(proposed, 1.0 - position)
            parameter_start = start + direction * position
            try:
                next_center, next_frame, next_radius, diagnostics = (
                    validated.validated_flow_step(
                        system,
                        parameter_start,
                        direction,
                        step,
                        center,
                        lift_frame,
                        integral_radius,
                        order=order,
                    )
                )
                if diagnostics["transformed_lift_correction"] > 1.0e-7:
                    raise ArithmeticError("handle lift correction exceeds budget")
                if diagnostics["beta_increment_error"] > 1.0e-5:
                    raise ArithmeticError("handle integral increment exceeds budget")
            except (ArithmeticError, ZeroDivisionError, ValueError):
                rejected += 1
                proposed = step / 2
                if proposed < minimum_step:
                    raise
                continue
            center = next_center
            lift_frame = next_frame
            integral_radius = next_radius
            position = min(1.0, position + step)
            minimum_accepted = min(minimum_accepted, step)
            accepted.append(
                {
                    "start_position": float(position - step),
                    "end_position": float(position),
                    "step": float(step),
                    **diagnostics,
                }
            )
            quality = max(
                diagnostics["reduction_neumann_norm"],
                diagnostics["fundamental_inverse_neumann_norm"],
            )
            proposed = min(initial_step, step * (1.5 if quality < 0.25 else 1.15))
            if len(accepted) % 25 == 0 or position == 1.0:
                print(
                    "validated A-handle "
                    f"steps={len(accepted)} position={position:.12g} "
                    f"step={step:.3e} radius={validated.upper(integral_radius):.3e}",
                    flush=True,
                )
    finally:
        validated.build_taylor_system = original

    return {
        "center": [complex_pair(midpoint(value)) for value in center],
        "uniform_integral_radius_upper": validated.upper(integral_radius),
        "lift_radius_upper": validated.upper(lift_frame.physical_radius()),
        "accepted_step_count": len(accepted),
        "rejected_step_count": rejected,
        "minimum_accepted_step": minimum_accepted,
        "steps": accepted,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--dps", type=int, default=90)
    parser.add_argument("--cut-segments", type=int, default=24)
    parser.add_argument("--cut-tolerance", type=float, default=1.0e-35)
    parser.add_argument("--order", type=int, default=32)
    parser.add_argument("--initial-step", type=float, default=0.01)
    parser.add_argument("--minimum-step", type=float, default=1.0e-8)
    arguments = parser.parse_args()
    ctx.dps = arguments.dps

    a133 = load(A133)
    target = a133["minimal_strict_interval_target"]
    if target["form"] != "E32":
        raise AssertionError("A133 separating row changed")
    handle_coordinates = a133["height_four_seed"]["primitive_handle_coordinates"]
    if handle_coordinates != [-1, 0, 1, 1, 0, 0, 0, 0]:
        raise AssertionError("A133 selected handle combination changed")

    system = validated.SelectedQ79IntervalSystem(dps=arguments.dps)
    roots, leading = selected_base_roots(system)
    sigma3_raw, sigma3_diagnostics = direct_cut_periods(
        roots,
        leading,
        (3, 4),
        segments=arguments.cut_segments,
        tolerance=arguments.cut_tolerance,
    )
    sigma4_raw, sigma4_diagnostics = direct_cut_periods(
        roots,
        leading,
        (1, 4),
        segments=arguments.cut_segments,
        tolerance=arguments.cut_tolerance,
    )
    sigma3_reference, sigma4_reference = reference_sigma_periods()
    sigma3, sign3, selected3, rejected3 = orient_cut(
        sigma3_raw, sigma3_reference
    )
    sigma4, sign4, selected4, rejected4 = orient_cut(
        sigma4_raw, sigma4_reference
    )
    initial_combination = [left + right for left, right in zip(sigma3, sigma4)]
    reference_combination = sigma3_reference + sigma4_reference
    initial_center_difference = float(
        np.max(
            np.abs(
                np.asarray([midpoint(value) for value in initial_combination])
                - reference_combination
            )
        )
    )
    if initial_center_difference >= 2.0e-7:
        raise AssertionError("rigorous base-cycle center disagrees with A131 marking")

    execution = validated_handle_transport(
        system,
        initial_combination,
        order=arguments.order,
        initial_step=arguments.initial_step,
        minimum_step=arguments.minimum_step,
    )
    e32_index = FORM_NAMES.index("E32")
    result_center = complex_value(execution["center"][5 + e32_index])
    result_radius = float(execution["uniform_integral_radius_upper"])

    handle_packet = load(HANDLES)
    handle_matrix = np.asarray(
        [
            [complex_value(value) for value in row]
            for row in handle_packet["primitive_handle_period_matrix"]
        ],
        dtype=np.complex128,
    )
    expected = handle_matrix[e32_index] @ np.asarray(handle_coordinates)
    center_difference = float(abs(result_center - expected))
    if center_difference >= 5.0e-7:
        raise AssertionError("validated handle center disagrees with A131")

    payload = {
        "schema": "MTTQ79SelectedAlignmentE32HandleCombinationInterval.v1",
        "status": "SELECTED_E32_HEIGHT4_HANDLE_COMBINATION_INTERVAL_CERTIFIED",
        "authority": {
            "A133_packet": relative(A133),
            "A133_packet_sha256": sha256(A133),
            "homology_convention": relative(HOMOLOGY),
            "homology_convention_sha256": sha256(HOMOLOGY),
            "orientation_packet": relative(ORIENTATION),
            "orientation_packet_sha256": sha256(ORIENTATION),
            "floating_handle_packet": relative(HANDLES),
            "floating_handle_packet_sha256": sha256(HANDLES),
            "validated_transport_engine": relative(
                ROOT / "scripts" / "certify_q79_selected_side_beta_defect_transport.py"
            ),
            "validated_transport_engine_sha256": sha256(
                ROOT / "scripts" / "certify_q79_selected_side_beta_defect_transport.py"
            ),
            "builder_source": relative(Path(__file__)),
            "builder_source_sha256": sha256(Path(__file__)),
        },
        "selected_chain": {
            "handle_coordinates": handle_coordinates,
            "identity": "-A:a1+A:a2+A:b2 = A:(sigma3+sigma4)",
            "path": "w(s)=(1+i)/4+s",
            "form": "E32",
        },
        "base_cycle_interval": {
            "sigma3": {
                **sigma3_diagnostics,
                "selected_orientation_sign": sign3,
                "selected_reference_maximum_difference": selected3,
                "opposite_reference_maximum_difference": rejected3,
            },
            "sigma4": {
                **sigma4_diagnostics,
                "selected_orientation_sign": sign4,
                "selected_reference_maximum_difference": selected4,
                "opposite_reference_maximum_difference": rejected4,
            },
            "combined_period_intervals": [
                complex_interval(value) for value in initial_combination
            ],
            "maximum_combined_component_radius": max(
                radius_upper(value) for value in initial_combination
            ),
            "A131_marked_center_maximum_difference": initial_center_difference,
        },
        "validated_transport": execution,
        "E32_handle_combination": {
            "interval": {
                "center": complex_pair(result_center),
                "uniform_radius_upper": result_radius,
            },
            "A131_floating_center": complex_pair(expected),
            "A131_center_difference": center_difference,
            "strict_A133_total_period_budget": target[
                "strict_required_period_combination_radius_upper"
            ],
        },
        "scope": {
            "observed_SM_values_used": False,
            "base_cycle_integrals_rigorous": True,
            "homogeneous_Gauss_Manin_transport_rigorous": True,
            "selected_handle_combination_interval_closed": True,
            "selected_thimble_combination_interval_closed": False,
            "full_E32_combined_period_interval_closed": False,
            "fixed_carrier_separation_closed": False,
        },
    }
    output = arguments.output
    if not output.is_absolute():
        output = ROOT / output
    dump(output, payload)
    print(f"wrote {relative(output)}")
    print(
        json.dumps(
            {
                "E32_handle_center": complex_pair(result_center),
                "E32_handle_radius": result_radius,
                "A131_center_difference": center_difference,
                "accepted_steps": execution["accepted_step_count"],
                "rejected_steps": execution["rejected_step_count"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
