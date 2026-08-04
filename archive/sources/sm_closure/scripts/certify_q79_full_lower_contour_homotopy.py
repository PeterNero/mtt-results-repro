from __future__ import annotations

import argparse
import cmath
import concurrent.futures
import json
import math
from pathlib import Path

from flint import acb, arb, ctx

from certify_q79_selected_side_beta_defect_transport import (
    ROOT,
    SelectedQ79IntervalSystem,
    TaylorModel,
    aligned_tm_coefficients_and_derivative,
    midpoint,
    quotient_reduce,
    tm_matrix_vector,
    upper,
    validated_ab_taylor_models,
)


DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
)
DEFAULT_OUTPUT = (
    DIRECTORY / "pgl3_selected_local_lower_contour_homotopy.interval.packet.json"
)

WORKER_SYSTEM: SelectedQ79IntervalSystem | None = None


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def taylor_determinant(matrix: list[list[TaylorModel]]) -> TaylorModel:
    work = [[value for value in row] for row in matrix]
    size = len(work)
    determinant = work[0][0].constant(
        1, work[0][0].order, work[0][0].radius
    )
    sign = 1
    for column in range(size):
        pivot_row = max(
            range(column, size),
            key=lambda row: work[row][column].absolute_lower(),
        )
        if not work[pivot_row][column].absolute_lower() > 0:
            raise ZeroDivisionError("Taylor determinant pivot contains zero")
        if pivot_row != column:
            work[column], work[pivot_row] = work[pivot_row], work[column]
            sign = -sign
        pivot = work[column][column]
        determinant *= pivot
        for row in range(column + 1, size):
            factor = work[row][column] / pivot
            for index in range(column + 1, size):
                work[row][index] -= factor * work[column][index]
    return sign * determinant


def taylor_obstruction_models(
    system: SelectedQ79IntervalSystem,
    start: complex,
    direction: complex,
    length: float,
    order: int,
) -> dict[str, TaylorModel]:
    radius = arb(format(length, ".17g"))
    a_value, b_value, _residual, _remainder = validated_ab_taylor_models(
        system, start, direction, radius, order
    )
    prototype = a_value
    one = prototype.constant(1, order, radius)
    zero = prototype.constant(0, order, radius)
    elliptic = [a_value, b_value, one]
    da_dw = acb(2) * system.period_length * b_value
    db_dw = system.period_length * (acb(3) * a_value**2 - 1)
    elliptic_derivative = [da_dw, db_dw, zero]
    line = tm_matrix_vector(system.alignment, elliptic)
    line_derivative = tm_matrix_vector(
        system.alignment, elliptic_derivative
    )
    f_coefficients, _ = aligned_tm_coefficients_and_derivative(
        system.evaluator.tables["F6"],
        line,
        line_derivative,
        chart="y",
    )
    g_coefficients, _ = aligned_tm_coefficients_and_derivative(
        system.evaluator.tables["G3"],
        line,
        line_derivative,
        chart="y",
    )
    q_coefficients, _ = aligned_tm_coefficients_and_derivative(
        system.evaluator.tables["Q2"],
        line,
        line_derivative,
        chart="y",
    )

    polynomial_derivative = [
        index * f_coefficients[index] for index in range(1, 7)
    ]
    reduction = [[zero for _ in range(11)] for _ in range(11)]
    for power in range(6):
        if power:
            for index, coefficient in enumerate(f_coefficients):
                reduction[index + power - 1][power] += power * coefficient
        for index, coefficient in enumerate(polynomial_derivative):
            reduction[index + power][power] -= acb("0.5") * coefficient
    for power in range(5):
        for index, coefficient in enumerate(f_coefficients):
            reduction[index + power][6 + power] += coefficient

    q0, q1, q2 = q_coefficients
    q_discriminant = q1**2 - 4 * q2 * q0
    root_sum = -q1 / q2
    root_product = q0 / q2
    relation_constant = -root_product
    relation_linear = root_sum
    g0, g1 = quotient_reduce(
        g_coefficients, relation_constant, relation_linear
    )
    g_norm = g0**2 + root_sum * g0 * g1 + root_product * g1**2
    return {
        "reduction_determinant": taylor_determinant(reduction),
        "y_chart_scale": line[1],
        "q_leading_coefficient": q2,
        "q_discriminant": q_discriminant,
        "g_on_q_norm": g_norm,
    }


def taylor_relative_radius(value: TaylorModel) -> float:
    center = midpoint(value.coefficients[0])
    if center == 0:
        return math.inf
    serialized_center = acb(
        format(center.real, ".17g"),
        format(center.imag, ".17g"),
    )
    tail = value.remainder + abs(value.coefficients[0] - serialized_center)
    power = value.radius
    for coefficient in value.coefficients[1:]:
        tail += abs(coefficient) * power
        power *= value.radius
    denominator = math.nextafter(abs(center), -math.inf)
    if denominator <= 0:
        return math.inf
    return math.nextafter(upper(tail) / denominator, math.inf)


def certify_segment(
    system: SelectedQ79IntervalSystem,
    left: complex,
    right: complex,
    *,
    depth: int,
    maximum_depth: int,
    relative_radius_gate: float,
    taylor_order: int,
) -> list[dict]:
    length = abs(right - left)
    direction = (right - left) / length
    try:
        values = taylor_obstruction_models(
            system, left, direction, length, taylor_order
        )
        accepted = all(value.absolute_lower() > 0 for value in values.values())
        accepted = accepted and all(
            taylor_relative_radius(value) < relative_radius_gate
            for value in values.values()
        )
    except (ZeroDivisionError, ValueError):
        values = {}
        accepted = False
    if accepted:
        return [
            {
                "start": {"real": left.real, "imaginary": left.imag},
                "end": {"real": right.real, "imaginary": right.imag},
                "depth": depth,
                "taylor_order": taylor_order,
                "winding_sectors": {
                    **{
                        name: {
                            "reference": {
                                "real": midpoint(value.coefficients[0]).real,
                                "imaginary": midpoint(value.coefficients[0]).imag,
                            },
                            "half_width": math.nextafter(
                                math.asin(
                                    min(1.0, taylor_relative_radius(value))
                                ),
                                math.inf,
                            ),
                        }
                        for name, value in values.items()
                    },
                },
                "absolute_lower_bounds": {
                    name: value.absolute_lower()
                    for name, value in values.items()
                },
                "relative_radius_upper_bounds": {
                    name: taylor_relative_radius(value)
                    for name, value in values.items()
                },
            }
        ]
    if depth >= maximum_depth:
        raise ArithmeticError(
            "boundary obstruction enclosure did not separate from zero at "
            f"{left!r}->{right!r}"
        )
    middle = (left + right) / 2.0
    return certify_segment(
        system,
        left,
        middle,
        depth=depth + 1,
        maximum_depth=maximum_depth,
        relative_radius_gate=relative_radius_gate,
        taylor_order=taylor_order,
    ) + certify_segment(
        system,
        middle,
        right,
        depth=depth + 1,
        maximum_depth=maximum_depth,
        relative_radius_gate=relative_radius_gate,
        taylor_order=taylor_order,
    )


def winding_certificate(leaves: list[dict], name: str) -> dict:
    sectors = [leaf["winding_sectors"][name] for leaf in leaves]
    references = [
        complex(value["reference"]["real"], value["reference"]["imaginary"])
        for value in sectors
    ]
    half_widths = [float(value["half_width"]) for value in sectors]
    total_angle = 0.0
    minimum_overlap_margin = math.inf
    for index in range(len(references)):
        following = (index + 1) % len(references)
        change = cmath.phase(references[following] / references[index])
        overlap_width = half_widths[index] + half_widths[following]
        overlap_margin = overlap_width - abs(change)
        minimum_overlap_margin = min(minimum_overlap_margin, overlap_margin)
        if not overlap_width < math.pi:
            raise ArithmeticError(f"{name} adjacent sectors are not unique")
        if overlap_margin <= 0:
            raise ArithmeticError(f"{name} adjacent sectors do not overlap")
        total_angle += change
    winding = int(round(total_angle / (2.0 * math.pi)))
    integer_residual = abs(total_angle - 2.0 * math.pi * winding)
    if integer_residual > 1.0e-7:
        raise ArithmeticError(f"{name} sector winding misses its integer")
    return {
        "winding_number": winding,
        "total_reference_argument_change": total_angle,
        "integer_residual": integer_residual,
        "minimum_adjacent_sector_overlap_margin": minimum_overlap_margin,
        "maximum_sector_half_width": max(half_widths),
    }


def initialize_worker(dps: int) -> None:
    global WORKER_SYSTEM
    ctx.dps = dps
    WORKER_SYSTEM = SelectedQ79IntervalSystem(dps=dps)


def certify_boundary_chunk(arguments: tuple) -> list[dict]:
    if WORKER_SYSTEM is None:
        raise RuntimeError("boundary worker was not initialized")
    (
        left,
        right,
        maximum_depth,
        relative_radius_gate,
        taylor_order,
    ) = arguments
    return certify_segment(
        WORKER_SYSTEM,
        left,
        right,
        depth=0,
        maximum_depth=maximum_depth,
        relative_radius_gate=relative_radius_gate,
        taylor_order=taylor_order,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--dps", type=int, default=90)
    parser.add_argument("--maximum-depth", type=int, default=30)
    parser.add_argument("--relative-radius-gate", type=float, default=0.5)
    parser.add_argument("--taylor-order", type=int, default=10)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--initial-subdivisions", type=int, default=16)
    parser.add_argument("--real-left", type=float, default=0.65)
    parser.add_argument("--real-right", type=float, default=0.82)
    parser.add_argument("--imaginary-bottom", type=float, default=-0.1)
    parser.add_argument("--allow-obstructed", action="store_true")
    arguments = parser.parse_args()
    ctx.dps = arguments.dps
    if not arguments.real_left < arguments.real_right:
        raise ValueError("real-left must be smaller than real-right")
    if not arguments.imaginary_bottom < 0:
        raise ValueError("imaginary-bottom must be negative")
    domain_left = arguments.real_left
    domain_right = arguments.real_right
    bottom = arguments.imaginary_bottom
    corners = [
        domain_left + 0j,
        domain_right + 0j,
        domain_right + bottom * 1j,
        domain_left + bottom * 1j,
        domain_left + 0j,
    ]
    tasks = []
    for left, right in zip(corners, corners[1:]):
        for index in range(arguments.initial_subdivisions):
            chunk_left = left + (right - left) * (
                index / arguments.initial_subdivisions
            )
            chunk_right = left + (right - left) * (
                (index + 1) / arguments.initial_subdivisions
            )
            tasks.append(
                (
                    chunk_left,
                    chunk_right,
                    arguments.maximum_depth,
                    arguments.relative_radius_gate,
                    arguments.taylor_order,
                )
            )
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=arguments.workers,
        initializer=initialize_worker,
        initargs=(arguments.dps,),
    ) as executor:
        chunks = list(executor.map(certify_boundary_chunk, tasks))
    leaves = [leaf for chunk in chunks for leaf in chunk]
    names = [
        "reduction_determinant",
        "y_chart_scale",
        "q_leading_coefficient",
        "q_discriminant",
        "g_on_q_norm",
    ]
    windings = {
        name: winding_certificate(leaves, name)
        for name in names
    }
    family_winding_zero = all(
        windings[name]["winding_number"] == 0
        for name in ["reduction_determinant", "y_chart_scale"]
    )
    coordinate_windings_zero = all(
        windings[name]["winding_number"] == 0
        for name in ["y_chart_scale", "q_leading_coefficient"]
    )
    finite_flat_divisor_regular = all(
        windings[name]["winding_number"] == 0
        for name in [
            "q_leading_coefficient",
            "g_on_q_norm",
        ]
    )
    q_discriminant_winding = windings["q_discriminant"]["winding_number"]
    if q_discriminant_winding > 0:
        raise ArithmeticError(
            "clockwise q-discriminant boundary has positive winding"
        )
    q_collision_count = -q_discriminant_winding
    homotopy_certified = family_winding_zero and finite_flat_divisor_regular
    selected_local_domain = (
        abs(domain_left - 0.65) < 1e-15
        and abs(domain_right - 0.82) < 1e-15
        and abs(bottom + 0.1) < 1e-15
    )
    schema = (
        "MTTQ79LocalLowerContourHomotopyIntervalCertificate.v1"
        if selected_local_domain
        else "MTTQ79FullLowerContourHomotopyIntervalCertificate.v2"
    )
    status_prefix = "LOCAL_LOWER" if selected_local_domain else "FULL_LOWER"
    packet = {
        "schema": schema,
        "status": (
            f"{status_prefix}_CONTOUR_HOMOTOPY_INTERVAL_CERTIFIED"
            if homotopy_certified
            else f"{status_prefix}_CONTOUR_HOMOTOPY_OBSTRUCTED"
        ),
        "domain": {
            "real_interval": [
                format(domain_left, ".17g"),
                format(domain_right, ".17g"),
            ],
            "imaginary_interval": [
                format(bottom, ".17g"),
                "0",
            ],
            "elliptic_pole_exclusion": (
                "w=1/4+i/4+i*lambda has real part strictly between "
                "consecutive half-integer-free bounds, "
                "strictly separated from the real coordinates of the "
                "Z+iZ pole lattice"
            ),
            "boundary_orientation": "clockwise",
        },
        "boundary_cover": {
            "leaf_count": len(leaves),
            "maximum_depth": max(leaf["depth"] for leaf in leaves),
            "relative_radius_gate": arguments.relative_radius_gate,
            "taylor_order": arguments.taylor_order,
            "worker_count": arguments.workers,
            "initial_subdivisions_per_side": arguments.initial_subdivisions,
            "minimum_absolute_lower_bounds": {
                name: min(leaf["absolute_lower_bounds"][name] for leaf in leaves)
                for name in names
            },
            "leaves": leaves,
        },
        "argument_principle": windings,
        "finite_flat_divisor_theorem": {
            "applies": finite_flat_divisor_regular,
            "statement": (
                "Nonvanishing q leading coefficient makes O[t]/(Q2) a "
                "finite flat rank-two algebra throughout the strip. "
                "Nonvanishing norm of G3 in that algebra makes G3 a unit, "
                "so U=G3 defines a finite flat symmetric degree-two divisor "
                "on the smooth hyperelliptic family. Zeros of the Q2 "
                "discriminant only exchange the two root labels; the divisor, "
                "its Abel-Jacobi class and the quotient-trace source extend "
                "holomorphically through them."
            ),
            "q_discriminant_zero_count_with_multiplicity": q_collision_count,
            "individual_q_roots_globally_labelled": q_collision_count == 0,
            "symmetric_divisor_and_quotient_trace_extend": (
                finite_flat_divisor_regular
            ),
        },
        "decision": {
            "smooth_genus_two_family_on_closed_lower_strip": family_winding_zero,
            "y_and_q_coordinate_windings_zero": coordinate_windings_zero,
            "q_roots_remain_distinct": q_collision_count == 0,
            "finite_flat_symmetric_divisor_preserved": (
                finite_flat_divisor_regular
            ),
            "straight_and_local_lower_contours_homotopic_in_smooth_family": (
                homotopy_certified and selected_local_domain
            ),
            "straight_and_full_lower_contours_homotopic_in_smooth_family": (
                homotopy_certified and not selected_local_domain
            ),
            "normal_function_endpoint_branch_preserved": (
                homotopy_certified
            ),
        },
        "observed_SM_values_used": False,
    }
    dump(arguments.output, packet)
    print(
        json.dumps(
            {
                "leaf_count": len(leaves),
                "maximum_depth": packet["boundary_cover"]["maximum_depth"],
                "minimum_absolute_lower_bounds": packet["boundary_cover"][
                    "minimum_absolute_lower_bounds"
                ],
                "windings": windings,
            },
            indent=2,
            sort_keys=True,
        )
    )
    if not homotopy_certified and not arguments.allow_obstructed:
        raise AssertionError(
            "the local lower strip contains a family or divisor obstruction"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
