from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from pathlib import Path

from flint import acb, acb_poly, arb, ctx

import certify_q79_height4_d087_full_residue_main_interval as main_certificate
import certify_q79_selected_alignment_E32_handle_combination_interval as handle
import certify_q79_selected_alignment_single_E32_thimble_nodal_factor as nodal
import certify_q79_selected_alignment_single_E32_thimble_tail_interval as tail
import certify_q79_selected_side_beta_defect_transport as validated


ROOT = main_certificate.ROOT
NODE = main_certificate.NODE_OUTPUT
THIMBLE = main_certificate.THIMBLE
OUTPUT = (
    main_certificate.PROBE_DIRECTORY
    / "validated_transport"
    / "d087.n3.tail8.interval.json"
)
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourD087FullResidueTailInterval_A221_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def residue_coefficients(
    system: validated.SelectedQ79IntervalSystem,
    parameter: acb,
) -> list[tuple[acb, acb]]:
    a_value, b_value, line, _line_derivative = system.ab_line_data(parameter)
    elliptic = [a_value, b_value, acb(1)]
    rows = []
    for generator in system.generators:
        variation = validated.matrix_vector(
            system.alignment * generator, elliptic
        )
        if system.line_chart == "z":
            constant = line[2] * (
                variation[0] * line[2] - variation[2] * line[0]
            )
            linear = line[2] * (
                variation[1] * line[2] - variation[2] * line[1]
            )
        else:
            constant = -line[1] * (
                variation[0] * line[1] - variation[1] * line[0]
            )
            linear = -line[1] * (
                variation[2] * line[1] - variation[1] * line[2]
            )
        rows.append(
            (
                system.period_length * constant,
                system.period_length * linear,
            )
        )
    return rows


def all_row_node_segment_bound(
    factor: list[acb],
    system: validated.SelectedQ79IntervalSystem,
    parameter_box: acb,
    node_parameter: acb,
    width: float,
) -> tuple[list[acb], dict]:
    q0, q1, *quartic = factor
    center = -q1 / acb(2)
    discriminant = q1**2 - acb(4) * q0
    half_upper = math.sqrt(validated.upper(abs(discriminant))) / 2.0
    point_upper = validated.upper(abs(center)) + half_upper
    point_box = tail.exact_ball(nodal.midpoint(center), half_upper)
    quartic_value = nodal.polynomial(quartic, point_box)
    quartic_lower = validated.lower(abs(quartic_value))
    if quartic_lower <= 0:
        raise AssertionError("node-segment quartic bound meets zero")
    period_0_upper = 2.0 * math.pi / math.sqrt(quartic_lower)
    period_1_upper = period_0_upper * point_upper
    path_scale = validated.upper(abs(acb(0, 1) * node_parameter))
    contributions = []
    rows = []
    for residue_index, (constant, linear) in enumerate(
        residue_coefficients(system, parameter_box)
    ):
        residue_upper = (
            validated.upper(abs(constant)) * period_0_upper
            + validated.upper(abs(linear)) * period_1_upper
        )
        integrand_upper = path_scale * residue_upper
        radius = width * integrand_upper
        contribution = acb(
            arb(0, format(radius, ".17g")),
            arb(0, format(radius, ".17g")),
        )
        contributions.append(contribution)
        rows.append(
            {
                "residue_index_zero_based": residue_index,
                "integrand_absolute_upper": integrand_upper,
                "contribution_radius_upper": validated.radius_upper(
                    contribution
                ),
            }
        )
    return contributions, {
        "half_difference_absolute_upper": half_upper,
        "quartic_on_cut_absolute_lower": quartic_lower,
        "period_I0_absolute_upper": period_0_upper,
        "period_I1_absolute_upper": period_1_upper,
        "row_bounds": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--epsilon", type=float, default=1.0e-5)
    parser.add_argument("--node-width", type=float, default=1.0e-10)
    parser.add_argument("--outer-segments", type=int, default=48)
    parser.add_argument("--theta-segments", type=int, default=32)
    parser.add_argument("--factor-order", type=int, default=32)
    parser.add_argument("--dps", type=int, default=100)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    arguments = parser.parse_args()
    started = time.perf_counter()
    if not 0 < arguments.node_width < arguments.epsilon:
        raise ValueError("node width must lie in (0, epsilon)")
    ctx.dps = arguments.dps

    node_packet = load(NODE)
    thimble = load(THIMBLE)
    if node_packet["selected_target"]["root_id"] != "selected_085":
        raise AssertionError("A220 node identity changed")
    node_parameter = validated.decoded_acb(
        node_packet["certified_node"]["parameter_ball"]
    )
    node_root = validated.decoded_acb(
        node_packet["certified_node"]["double_root_ball"]
    )
    factor_packet = node_packet["certified_node"]["factor_diagnostics"]
    node_values = [
        validated.decoded_acb(value)
        for value in factor_packet["monic_quadratic_coefficients_ascending"][:2]
        + factor_packet["quartic_coefficients_ascending"]
    ]
    system = main_certificate.exact_target_system(arguments.dps)
    factor_models, factor_disk_diagnostics = tail.factor_taylor_models(
        system,
        node_parameter,
        node_root,
        epsilon=arguments.epsilon,
        order=arguments.factor_order,
    )

    cutoff_parameter = nodal.midpoint(node_parameter) * acb(
        format(1.0 - arguments.epsilon, ".17g")
    )
    cutoff_coefficients, _derivative = nodal.fiber_coefficients(
        system, cutoff_parameter
    )
    cutoff_roots = acb_poly(cutoff_coefficients).roots(
        tol=1.0e-45, maxprec=4096
    )
    if len(cutoff_roots) != 6:
        raise AssertionError("A221 cutoff root isolation failed")
    cutoff_pair = nodal.closest_pair(cutoff_roots)
    cutoff_periods, cutoff_diagnostics = handle.direct_cut_periods(
        cutoff_roots,
        cutoff_coefficients[6],
        cutoff_pair,
        segments=arguments.theta_segments,
        tolerance=1.0e-35,
    )
    reference = cutoff_periods[:2]

    node_factor = tail.evaluate_factor_models(
        factor_models,
        0.0,
        arguments.node_width,
        factor_disk_diagnostics["center_x"],
    )
    node_x_box = arb(
        format(arguments.node_width / 2.0, ".17g"),
        format(arguments.node_width / 2.0, ".17g"),
    )
    node_parameter_box = node_parameter * (acb(1) - acb(node_x_box))
    node_contributions, node_bound = all_row_node_segment_bound(
        node_factor,
        system,
        node_parameter_box,
        node_parameter,
        arguments.node_width,
    )
    totals = list(node_contributions)
    rows = []
    previous_factor: list[acb] | None = None
    ratio = (arguments.epsilon / arguments.node_width) ** (
        1.0 / arguments.outer_segments
    )
    edges = [
        arguments.node_width * ratio**index
        for index in range(arguments.outer_segments)
    ]
    edges.append(arguments.epsilon)
    intervals = list(zip(edges[:-1], edges[1:]))
    for reverse_index, (x_left, x_right) in enumerate(reversed(intervals)):
        factor = tail.evaluate_factor_models(
            factor_models,
            x_left,
            x_right,
            factor_disk_diagnostics["center_x"],
        )
        x_box = arb(
            format((x_left + x_right) / 2.0, ".17g"),
            format((x_right - x_left) / 2.0, ".17g"),
        )
        parameter_box = node_parameter * (acb(1) - acb(x_box))
        periods, period_diagnostics = tail.period_enclosure(
            factor, theta_segments=arguments.theta_segments
        )
        periods, sign, selected_difference, rejected_difference = (
            tail.orient_periods(periods, reference)
        )
        reference = periods
        width = acb(format(x_right - x_left, ".17g"))
        row_integrals = []
        for residue_index, (constant, linear) in enumerate(
            residue_coefficients(system, parameter_box)
        ):
            integrand = acb(0, 1) * node_parameter * (
                constant * periods[0] + linear * periods[1]
            )
            contribution = width * integrand
            totals[residue_index] += contribution
            row_integrals.append(
                {
                    "residue_index_zero_based": residue_index,
                    "integrand_interval": handle.complex_interval(integrand),
                    "contribution_interval": handle.complex_interval(
                        contribution
                    ),
                }
            )
        overlap = (
            [True for _ in range(7)]
            if previous_factor is None
            else [
                previous_factor[index].overlaps(factor[index])
                for index in range(7)
            ]
        )
        rows.append(
            {
                "reverse_index_from_cutoff": reverse_index,
                "x_interval": {"lower": x_left, "upper": x_right},
                "maximum_factor_radius_upper": max(
                    validated.radius_upper(value) for value in factor
                ),
                **period_diagnostics,
                "selected_period_sign": sign,
                "selected_orientation_difference_upper": selected_difference,
                "opposite_orientation_difference_lower": rejected_difference,
                "factor_overlap_with_node_side_neighbor": bool(all(overlap)),
                "row_integrals": row_integrals,
            }
        )
        previous_factor = factor
        if (reverse_index + 1) % 8 == 0:
            print(
                "certified d087 n3 all-row tail "
                f"segments={reverse_index + 1}/{arguments.outer_segments} "
                f"radius={max(validated.radius_upper(value) for value in totals):.3e}",
                flush=True,
            )
    if previous_factor is None or not all(
        previous_factor[index].overlaps(node_factor[index])
        for index in range(7)
    ):
        raise AssertionError("A221 factor chain does not overlap the node segment")

    radii = [validated.radius_upper(value) for value in totals]
    output = arguments.output
    if not output.is_absolute():
        output = ROOT / output
    payload = {
        "schema": "MTTQ79HeightFourD087FullResidueTailInterval.v1",
        "status": "D087_N3_ALL_EIGHT_NODE_TO_CUTOFF_RESIDUE_TAILS_INTERVAL_CERTIFIED",
        "selected_target": {
            "distinguished_index": 87,
            "root_id": "selected_085",
            "line_chart": "y",
            "endpoint_cutoff_epsilon": arguments.epsilon,
            "cutoff_pair_zero_based": list(cutoff_pair),
        },
        "cutoff_direct_period_reference": {
            **cutoff_diagnostics,
            "I0_I1_intervals": [
                handle.complex_interval(value) for value in cutoff_periods[:2]
            ],
        },
        "quantitative_Hensel_disk": factor_disk_diagnostics,
        "node_segment": {
            "x_interval": {"lower": 0.0, "upper": arguments.node_width},
            "absolute_bounds": node_bound,
            "contribution_intervals": [
                handle.complex_interval(value) for value in node_contributions
            ],
        },
        "regular_segments": rows,
        "all_eight_endpoint_tails": {
            "intervals": [handle.complex_interval(value) for value in totals],
            "interval_centers": [
                main_certificate.encoded_complex(handle.midpoint(value))
                for value in totals
            ],
            "interval_radius_uppers": radii,
            "maximum_interval_radius_upper": max(radii),
        },
        "authority": {
            name: {"path": relative(path), "sha256": sha256(path)}
            for name, path in {
                "A220_target_node": NODE,
                "n3_d087_cache": THIMBLE,
                "target_system_source": Path(main_certificate.__file__).resolve(),
                "tail_engine": Path(tail.__file__).resolve(),
                "source": Path(__file__).resolve(),
            }.items()
        },
        "numerics": {
            "dps": arguments.dps,
            "factor_order": arguments.factor_order,
            "outer_segments": arguments.outer_segments,
            "theta_segments": arguments.theta_segments,
            "node_width": arguments.node_width,
            "elapsed_seconds": time.perf_counter() - started,
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "target_node_consumed": True,
            "quantitative_Hensel_disk_closed": True,
            "all_eight_node_to_cutoff_tail_intervals_closed": True,
            "full_d087_period_vector_interval_closed": False,
            "covariant_zero_proved": False,
        },
        "next_required_artifact": (
            "splice these eight oriented tail balls to A220's eight validated "
            "main balls and test containment of the n3 floating d087 vector"
        ),
    }
    dump(output, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four d087 Full-Residue Tail Interval (A221) v1\n\n"
        "The A220 target node and its quantitative Hensel factor are reused at "
        "the n3 alignment. The desingularized vanishing periods are enclosed "
        "on a geometric node-to-cutoff partition, and all eight PGL(3) residue "
        "contractions are integrated on the same certified branch.\n\n"
        f"All eight local tails are enclosed; the maximum complex-disk radius "
        f"is `{max(radii):.12g}` across `{arguments.outer_segments}` regular "
        "segments plus the absolute node segment. The full d087 splice and "
        "the covariant interval Newton theorem remain open.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(output)}")
    print(f"wrote {relative(NOTE)}")
    print(
        json.dumps(
            {
                "maximum_tail_radius": max(radii),
                "row_radii": radii,
                "regular_segments": len(rows),
                "elapsed_seconds": time.perf_counter() - started,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
