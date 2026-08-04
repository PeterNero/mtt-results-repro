from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import deque
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from flint import acb, arb, ctx

import certify_q79_height4_target_tail_hessian_interval as base


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = "A381Q"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def outward(value: float) -> float:
    return math.nextafter(float(value), math.inf)


def require_finite_ball(value: acb, label: str) -> acb:
    midpoint = base.validated.midpoint(value)
    radius = base.validated.radius_upper(value)
    if not (
        math.isfinite(midpoint.real)
        and math.isfinite(midpoint.imag)
        and math.isfinite(radius)
    ):
        raise ArithmeticError(f"nonfinite interval ball: {label}")
    return value


@dataclass(frozen=True)
class DualBall:
    value: acb
    derivative: acb

    @classmethod
    def constant(cls, value: object) -> "DualBall":
        return cls(acb(value), acb(0))

    def coerce(self, other: object) -> "DualBall":
        return other if isinstance(other, DualBall) else self.constant(other)

    def __neg__(self) -> "DualBall":
        return DualBall(-self.value, -self.derivative)

    def __add__(self, other: object) -> "DualBall":
        right = self.coerce(other)
        return DualBall(
            self.value + right.value,
            self.derivative + right.derivative,
        )

    def __radd__(self, other: object) -> "DualBall":
        return self + other

    def __sub__(self, other: object) -> "DualBall":
        return self + (-self.coerce(other))

    def __rsub__(self, other: object) -> "DualBall":
        return self.coerce(other) - self

    def __mul__(self, other: object) -> "DualBall":
        right = self.coerce(other)
        return DualBall(
            self.value * right.value,
            self.derivative * right.value + self.value * right.derivative,
        )

    def __rmul__(self, other: object) -> "DualBall":
        return self * other

    def reciprocal(self) -> "DualBall":
        return DualBall(
            1 / self.value,
            -self.derivative / self.value**2,
        )

    def __truediv__(self, other: object) -> "DualBall":
        return self * self.coerce(other).reciprocal()

    def __rtruediv__(self, other: object) -> "DualBall":
        return self.coerce(other) / self

    def __pow__(self, power: int) -> "DualBall":
        if power < 0:
            return (self.reciprocal()) ** (-power)
        result = self.constant(1)
        for _index in range(power):
            result *= self
        return result


def dual_sqrt(value: DualBall) -> DualBall:
    root = require_finite_ball(value.value.sqrt(), "dual square root")
    derivative = require_finite_ball(
        value.derivative / (2 * root), "dual square-root derivative"
    )
    return DualBall(root, derivative)


def dual_polynomial(coefficients: list[DualBall], point: DualBall) -> DualBall:
    result = DualBall.constant(0)
    for coefficient in reversed(coefficients):
        result = result * point + coefficient
    return result


def evaluate_model_box(
    model: base.TM,
    left: float,
    right: float,
    center_x: float,
) -> acb:
    argument = arb(
        format((left + right) / 2.0 - center_x, ".17g"),
        format((right - left) / 2.0, ".17g"),
    )
    value = model.evaluate_polynomial(argument)
    return require_finite_ball(base.tail.exact_ball(
        base.tail.nodal.midpoint(value),
        outward(
            base.validated.radius_upper(value)
            + base.validated.upper(model.remainder)
        ),
    ), "Taylor-model box evaluation")


def evaluate_dual_models(
    models: list[base.DualTM],
    left: float,
    right: float,
    center_x: float,
) -> list[DualBall]:
    return [
        DualBall(
            evaluate_model_box(model.value, left, right, center_x),
            evaluate_model_box(model.derivative, left, right, center_x),
        )
        for model in models
    ]


def rotated_square_root(value: DualBall, rotation: acb) -> DualBall:
    rotated_root = require_finite_ball(
        (rotation * value.value).sqrt(), "rotated square root"
    )
    rotation_root = require_finite_ball(rotation.sqrt(), "rotation square root")
    return DualBall(
        require_finite_ball(
            rotated_root / rotation_root, "unrotated square root"
        ),
        require_finite_ball(
            rotation * value.derivative / (2 * rotated_root * rotation_root),
            "rotated square-root derivative",
        ),
    )


def period_enclosure_dual(
    factor: list[DualBall],
    *,
    theta_segments: int,
) -> tuple[list[DualBall], dict]:
    q0, q1, *quartic = factor
    center = -q1 / 2
    discriminant = q1**2 - 4 * q0
    discriminant_lower = base.validated.lower(abs(discriminant.value))
    if discriminant_lower <= 0.0:
        raise ZeroDivisionError("quadrature segment contains the nodal discriminant")
    half = dual_sqrt(discriminant) / 2
    total = [DualBall.constant(0), DualBall.constant(0)]
    previous_root: acb | None = None
    minimum_half_plane_margin = math.inf
    minimum_sign_margin = math.inf
    for segment in range(theta_segments):
        left = math.pi * segment / theta_segments
        right = math.pi * (segment + 1) / theta_segments
        theta_box = acb(
            arb(
                format((left + right) / 2.0, ".17g"),
                format((right - left) / 2.0, ".17g"),
            )
        )
        point = center + half * theta_box.cos()
        quartic_value = dual_polynomial(quartic, point)
        rotation_rows = [
            (rotation, base.validated.lower((rotation * quartic_value.value).real))
            for rotation in base.tail.rotations()
        ]
        rotation, margin = max(rotation_rows, key=lambda row: row[1])
        if margin <= 0.0:
            raise ArithmeticError("quartic image has no square-root half-plane")
        minimum_half_plane_margin = min(minimum_half_plane_margin, margin)

        left_point = center + half * acb(format(math.cos(left), ".17g"))
        left_root = rotated_square_root(
            dual_polynomial(quartic, left_point), rotation
        ).value
        sign = 1
        if previous_root is not None:
            same_upper = base.validated.upper(abs(left_root - previous_root))
            opposite_lower = base.validated.lower(abs(left_root + previous_root))
            opposite_upper = base.validated.upper(abs(left_root + previous_root))
            same_lower = base.validated.lower(abs(left_root - previous_root))
            if same_upper < opposite_lower:
                sign = 1
                sign_margin = opposite_lower - same_upper
            elif opposite_upper < same_lower:
                sign = -1
                sign_margin = same_lower - opposite_upper
            else:
                raise ArithmeticError("quadrature square-root sign is not separated")
            minimum_sign_margin = min(minimum_sign_margin, sign_margin)
        denominator = sign * rotated_square_root(quartic_value, rotation)
        width = acb(format(right - left, ".17g"))
        for power in range(2):
            total[power] += acb(0, 2) * point**power * width / denominator
        right_point = center + half * acb(format(math.cos(right), ".17g"))
        previous_root = sign * rotated_square_root(
            dual_polynomial(quartic, right_point), rotation
        ).value
    return total, {
        "quadratic_discriminant_absolute_lower": discriminant_lower,
        "minimum_quartic_half_plane_margin": minimum_half_plane_margin,
        "minimum_square_root_sign_margin": (
            None if not math.isfinite(minimum_sign_margin) else minimum_sign_margin
        ),
    }


def orient_periods(
    periods: list[DualBall],
    reference: list[acb],
) -> tuple[list[DualBall], int, float]:
    plus = max(
        base.validated.upper(abs(period.value - target))
        for period, target in zip(periods, reference)
    )
    minus = max(
        base.validated.upper(abs(-period.value - target))
        for period, target in zip(periods, reference)
    )
    sign = 1 if plus <= minus else -1
    selected = min(plus, minus)
    rejected = max(
        base.validated.lower(abs(-acb(sign) * period.value - target))
        for period, target in zip(periods, reference)
    )
    if selected >= rejected:
        raise ArithmeticError("outer quadrature period orientation is not separated")
    return [sign * period for period in periods], sign, rejected - selected


def constant_dual_models(
    prototype: base.TM,
    values: list[DualBall],
) -> list[base.DualTM]:
    return [
        base.DualTM(
            prototype.constant(value.value, prototype.order, prototype.radius),
            prototype.constant(
                value.derivative, prototype.order, prototype.radius
            ),
        )
        for value in values
    ]


def zero_centered_ball(radius: float) -> acb:
    return acb(
        arb(0, format(outward(radius), ".17g")),
        arb(0, format(outward(radius), ".17g")),
    )


def node_segment_contribution(
    factors: list[base.DualTM],
    residue_rows: list[tuple[base.DualTM, base.DualTM]],
    path: base.DualTM,
    *,
    node_width: float,
    center_x: float,
    series_terms: int,
) -> tuple[list[acb], list[acb], dict]:
    factor_boxes = evaluate_dual_models(factors, 0.0, node_width, center_x)
    prototype = factors[0].value
    boxed_factors = constant_dual_models(prototype, factor_boxes)
    periods, diagnostics = base.period_models(
        boxed_factors, series_terms=series_terms
    )
    boxed_rows = [
        (
            constant_dual_models(
                prototype,
                [
                    DualBall(
                        evaluate_model_box(constant.value, 0.0, node_width, center_x),
                        evaluate_model_box(
                            constant.derivative, 0.0, node_width, center_x
                        ),
                    )
                ],
            )[0],
            constant_dual_models(
                prototype,
                [
                    DualBall(
                        evaluate_model_box(linear.value, 0.0, node_width, center_x),
                        evaluate_model_box(
                            linear.derivative, 0.0, node_width, center_x
                        ),
                    )
                ],
            )[0],
        )
        for constant, linear in residue_rows
    ]
    integrands = [
        path * (constant * periods[0] + linear * periods[1])
        for constant, linear in boxed_rows
    ]
    values = [
        zero_centered_ball(
            node_width * base.validated.upper(value.value.absolute_bound())
        )
        for value in integrands
    ]
    derivatives = [
        zero_centered_ball(
            node_width * base.validated.upper(value.derivative.absolute_bound())
        )
        for value in integrands
    ]
    return values, derivatives, {
        "node_width": node_width,
        "node_value_radius_upper": max(
            base.validated.radius_upper(value) for value in values
        ),
        "node_derivative_radius_upper": max(
            base.validated.radius_upper(value) for value in derivatives
        ),
        **diagnostics,
    }


def integrate_direction(
    system: base.validated.SelectedQ79IntervalSystem,
    factor_models: list[base.TM],
    node_parameter: acb,
    node_root: acb,
    selected_direction: int,
    reference: list[acb],
    *,
    epsilon: float,
    order: int,
    outer_segments: int,
    theta_segments: int,
    node_width: float,
    series_terms: int,
    fixed_intervals: list[tuple[float, float]] | None,
) -> tuple[list[acb], list[acb], list[tuple[float, float]], dict]:
    parameter_s, _root_s, node_diagnostics = base.node_directional_derivative(
        system, node_parameter, node_root, selected_direction
    )
    _factor_s, factors, elliptic, factor_diagnostics = (
        base.factor_derivative_models(
            system,
            factor_models,
            node_parameter,
            parameter_s,
            selected_direction,
            epsilon=epsilon,
            order=order,
        )
    )
    residue_rows = base.residue_dual_rows(system, elliptic, selected_direction)
    prototype = factors[0].value
    path = base.DualTM.constant(
        prototype,
        acb(0, 1) * node_parameter,
        acb(0, 1) * parameter_s,
    )
    center_x = float(factor_diagnostics["declared_center_x"])
    node_values, node_derivatives, node_diagnostics_extra = node_segment_contribution(
        factors,
        residue_rows,
        path,
        node_width=node_width,
        center_x=center_x,
        series_terms=series_terms,
    )
    values = node_values.copy()
    derivatives = node_derivatives.copy()

    if fixed_intervals is None:
        ratio = (epsilon / node_width) ** (1.0 / outer_segments)
        edges = [node_width * ratio**index for index in range(outer_segments)]
        edges.append(epsilon)
        pending = deque(reversed(list(zip(edges[:-1], edges[1:]))))
    else:
        pending = deque(fixed_intervals)
    accepted_intervals: list[tuple[float, float]] = []
    current_reference = reference
    subdivisions = 0
    minimum_half_plane_margin = math.inf
    minimum_orientation_margin = math.inf
    maximum_value_integrand = 0.0
    maximum_derivative_integrand = 0.0
    while pending:
        left, right = pending.popleft()
        try:
            factor_boxes = evaluate_dual_models(factors, left, right, center_x)
            periods, period_diagnostics = period_enclosure_dual(
                factor_boxes, theta_segments=theta_segments
            )
            periods, _sign, orientation_margin = orient_periods(
                periods, current_reference
            )
        except (ArithmeticError, ZeroDivisionError):
            if right - left <= 1.0e-16:
                raise
            middle = (left + right) / 2.0
            pending.appendleft((left, middle))
            pending.appendleft((middle, right))
            subdivisions += 1
            if subdivisions > 200000:
                raise ArithmeticError("adaptive tail quadrature exceeded subdivision budget")
            continue
        current_reference = [period.value for period in periods]
        row_boxes = [
            (
                DualBall(
                    evaluate_model_box(constant.value, left, right, center_x),
                    evaluate_model_box(constant.derivative, left, right, center_x),
                ),
                DualBall(
                    evaluate_model_box(linear.value, left, right, center_x),
                    evaluate_model_box(linear.derivative, left, right, center_x),
                ),
            )
            for constant, linear in residue_rows
        ]
        path_ball = DualBall(
            evaluate_model_box(path.value, left, right, center_x),
            evaluate_model_box(path.derivative, left, right, center_x),
        )
        width = acb(format(right - left, ".17g"))
        for residue_index, (constant, linear) in enumerate(row_boxes):
            integrand = path_ball * (
                constant * periods[0] + linear * periods[1]
            )
            require_finite_ball(
                integrand.value,
                f"regular integrand row {residue_index} value",
            )
            require_finite_ball(
                integrand.derivative,
                f"regular integrand row {residue_index} derivative",
            )
            values[residue_index] += width * integrand.value
            derivatives[residue_index] += width * integrand.derivative
            maximum_value_integrand = max(
                maximum_value_integrand,
                base.validated.upper(abs(integrand.value)),
            )
            maximum_derivative_integrand = max(
                maximum_derivative_integrand,
                base.validated.upper(abs(integrand.derivative)),
            )
        accepted_intervals.append((left, right))
        minimum_half_plane_margin = min(
            minimum_half_plane_margin,
            float(period_diagnostics["minimum_quartic_half_plane_margin"]),
        )
        minimum_orientation_margin = min(
            minimum_orientation_margin, orientation_margin
        )

    sliver = float(factor_diagnostics["endpoint_coordinate_sliver_width_upper"])
    for residue_index in range(8):
        values[residue_index] += zero_centered_ball(
            sliver * maximum_value_integrand
        )
        derivatives[residue_index] += zero_centered_ball(
            sliver * maximum_derivative_integrand
        )
    return values, derivatives, accepted_intervals, {
        **node_diagnostics,
        **factor_diagnostics,
        "adaptive_regular_interval_count": len(accepted_intervals),
        "adaptive_subdivision_count": subdivisions,
        "regular_cover_lower": min(left for left, _right in accepted_intervals),
        "regular_cover_upper": max(right for _left, right in accepted_intervals),
        "regular_cover_total_width": sum(
            right - left for left, right in accepted_intervals
        ),
        "minimum_quartic_half_plane_margin": minimum_half_plane_margin,
        "minimum_outer_orientation_margin": minimum_orientation_margin,
        "maximum_value_integrand_absolute_upper": maximum_value_integrand,
        "maximum_derivative_integrand_absolute_upper": maximum_derivative_integrand,
        **node_diagnostics_extra,
    }


def execute(arguments: argparse.Namespace) -> dict:
    paths = base.output_paths(arguments.index)
    main_packet = base.load(paths["main"])
    tail_packet = base.load(paths["tail"])
    system, rank, row = base.main_hessian.selected_system(
        arguments.index, arguments.dps
    )
    epsilon = float(main_packet["selected_target"]["endpoint_cutoff_epsilon"])
    node_parameter = base.validated.decoded_acb(
        main_packet["certified_node"]["parameter_ball"]
    )
    node_root = base.validated.decoded_acb(
        main_packet["certified_node"]["double_root_ball"]
    )
    factor_models, factor_disk = base.tail.factor_taylor_models(
        system,
        node_parameter,
        node_root,
        epsilon=epsilon,
        order=arguments.order,
    )
    reference = [
        base.validated.interval_from_bounds(value)
        for value in main_packet["near_node_direct_cycle_interval"][
            "initial_period_intervals"
        ][:2]
    ]
    ordinary_by_direction = []
    hessian_columns = []
    diagnostics = []
    fixed_intervals = None
    intervals_by_direction = []
    for selected_direction in range(8):
        values, derivatives, intervals, direction_diagnostics = integrate_direction(
            system,
            factor_models,
            node_parameter,
            node_root,
            selected_direction,
            reference,
            epsilon=epsilon,
            order=arguments.order,
            outer_segments=arguments.outer_segments,
            theta_segments=arguments.theta_segments,
            node_width=arguments.node_width,
            series_terms=arguments.series_terms,
            fixed_intervals=fixed_intervals,
        )
        if fixed_intervals is None:
            fixed_intervals = intervals
        intervals_by_direction.append(intervals)
        ordinary_by_direction.append(values)
        hessian_columns.append(derivatives)
        diagnostics.append(direction_diagnostics)
        print(
            f"d{arguments.index:03d} quadrature tail direction="
            f"{selected_direction + 1}/8 intervals={len(intervals)} radius="
            f"{max(base.validated.radius_upper(value) for value in derivatives):.3e}",
            flush=True,
        )

    ordinary = ordinary_by_direction[0]
    inter_direction_overlap = [
        all(
            ordinary[residue_index].overlaps(values[residue_index])
            for values in ordinary_by_direction[1:]
        )
        for residue_index in range(8)
    ]
    if not all(inter_direction_overlap):
        raise AssertionError("ordinary quadrature tail depends on deformation label")
    canonical_centers = np.asarray(
        [
            base.complex_value(value)
            for value in tail_packet["all_eight_endpoint_tails"]["interval_centers"]
        ],
        dtype=np.complex128,
    )
    canonical_radii = np.asarray(
        tail_packet["all_eight_endpoint_tails"]["interval_radius_uppers"],
        dtype=np.float64,
    )
    ordinary_centers = np.asarray(
        [base.validated.midpoint(value) for value in ordinary], dtype=np.complex128
    )
    ordinary_radii = np.asarray(
        [base.validated.radius_upper(value) for value in ordinary], dtype=np.float64
    )
    if not (
        bool(np.all(np.isfinite(ordinary_centers)))
        and bool(np.all(np.isfinite(ordinary_radii)))
    ):
        raise ArithmeticError("nonfinite ordinary differentiated-tail rows")
    plus = float(np.max(abs(ordinary_centers - canonical_centers)))
    minus = float(np.max(abs(-ordinary_centers - canonical_centers)))
    branch_sign = 1 if plus <= minus else -1
    ordinary = [acb(branch_sign) * value for value in ordinary]
    ordinary_centers *= branch_sign
    hessian_columns = [
        [acb(branch_sign) * value for value in column]
        for column in hessian_columns
    ]
    differences = abs(ordinary_centers - canonical_centers)
    overlap = differences <= ordinary_radii + canonical_radii
    if not bool(np.all(overlap)):
        raise AssertionError("quadrature tail does not overlap canonical tail")
    hessian = np.empty((8, 8), dtype=np.complex128)
    hessian_radii = np.empty((8, 8), dtype=np.float64)
    for column in range(8):
        for residue_index in range(8):
            hessian[residue_index, column] = base.validated.midpoint(
                hessian_columns[column][residue_index]
            )
            hessian_radii[residue_index, column] = base.validated.radius_upper(
                hessian_columns[column][residue_index]
            )
    if not (
        bool(np.all(np.isfinite(hessian)))
        and bool(np.all(np.isfinite(hessian_radii)))
    ):
        raise ArithmeticError("nonfinite differentiated-tail Hessian enclosure")
    payload = {
        "schema": "MTTQ79HeightFourTargetTailHessianQuadratureInterval.v1",
        "status": "TARGET_A135_DUAL_QUADRATURE_TAIL_AND_COMPLEX_8_BY_8_HESSIAN_INTERVAL_CERTIFIED",
        "artifact": ARTIFACT,
        "selected_target": {
            "distinguished_index": arguments.index,
            "A219_contribution_rank": rank,
            "root_id": row["root_id"],
            "line_chart": system.line_chart,
            "signed_chain_coefficient": int(row["signed_coefficient"]),
            "endpoint_cutoff_epsilon": epsilon,
            "quadrature_branch_sign_against_canonical_tail": branch_sign,
        },
        "tail_residue_rows": [
            {
                "residue_index_zero_based": index,
                "interval_center": base.pair(ordinary_centers[index]),
                "component_radius_upper": float(ordinary_radii[index]),
                "canonical_center_difference": float(differences[index]),
                "canonical_intervals_overlap": bool(overlap[index]),
            }
            for index in range(8)
        ],
        "complex_tail_Hessian_8_by_8": [
            [
                {
                    "row_zero_based": residue_index,
                    "column_zero_based": column,
                    "interval_center": base.pair(hessian[residue_index, column]),
                    "component_radius_upper": float(
                        hessian_radii[residue_index, column]
                    ),
                }
                for column in range(8)
            ]
            for residue_index in range(8)
        ],
        "A135_dual_quadrature_method": {
            "identity": "differentiate the certified A135 x-theta interval quadrature",
            "node_segment_method": "local Frobenius-Cauchy uniform bound",
            "regular_segment_method": "adaptive radial boxes and rotated half-plane square-root continuation",
            "outer_seed_segments": arguments.outer_segments,
            "theta_segments": arguments.theta_segments,
            "node_width": arguments.node_width,
            "factor_disk": factor_disk,
            "direction_diagnostics": diagnostics,
            "accepted_radial_intervals": [
                {"lower": left, "upper": right}
                for left, right in (fixed_intervals or [])
            ],
            "accepted_radial_intervals_by_direction": [
                {
                    "direction_zero_based": direction,
                    "intervals": [
                        {"lower": left, "upper": right}
                        for left, right in intervals
                    ],
                }
                for direction, intervals in enumerate(intervals_by_direction)
            ],
        },
        "summary": {
            "certified_tail_rows": 8,
            "certified_tail_Hessian_entries": 64,
            "maximum_tail_row_component_radius_upper": float(
                np.max(ordinary_radii)
            ),
            "maximum_tail_Hessian_component_radius_upper": float(
                np.max(hessian_radii)
            ),
            "tail_Hessian_product_box_frobenius_radius_upper": float(
                np.linalg.norm(hessian_radii)
            ),
            "all_canonical_tail_intervals_overlap": bool(np.all(overlap)),
            "maximum_canonical_tail_center_difference": float(
                np.max(differences)
            ),
            "ordinary_rows_overlap_across_all_eight_dual_executions": all(
                inter_direction_overlap
            ),
        },
        "authority": {
            name: {"path": relative(path), "sha256": sha256(path)}
            for name, path in {
                "canonical_main_interval": paths["main"],
                "canonical_tail_interval": paths["tail"],
                "A378_Hessian_integrand_source": base.A378,
                "A135_tail_engine": Path(base.tail.__file__).resolve(),
                "A381_dual_factor_engine": Path(base.__file__).resolve(),
                "builder_source": Path(__file__).resolve(),
            }.items()
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "moving_node_implicit_derivative_interval_closed": True,
            "moving_Hensel_factor_derivative_interval_closed": True,
            "A135_dual_quadrature_tail_Hessian_interval_closed": True,
            "target_tail_Hessian_interval_closed": True,
            "target_Frobenius_tail_Hessian_interval_closed": False,
            "target_main_Hessian_interval_closed": False,
            "target_full_Hessian_interval_closed": False,
            "full_76_target_chain_Hessian_interval_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": "splice this A135 quadrature Hessian to the matching main Hessian",
    }
    base.dump(paths["output"], payload)
    paths["note"].write_text(
        f"# MTT q79 Height-Four d{arguments.index:03d} A135 Dual-Quadrature Tail Hessian (A381Q) v1\n\n"
        "A381Q differentiates the already-certified A135 radial/theta interval "
        "quadrature. It is the rigorous fallback when a single global log-free "
        "Frobenius disk cannot separate the nodal quadratic from the quartic.\n\n"
        f"The maximum Hessian component radius is "
        f"`{np.max(hessian_radii):.12g}` and all ordinary rows overlap the "
        "canonical tail certificate.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(paths['output'])}")
    print(f"wrote {relative(paths['note'])}")
    print(json.dumps(payload["summary"], indent=2))
    return payload


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser()
    value.add_argument("--index", type=int, required=True)
    value.add_argument("--dps", type=int, default=100)
    value.add_argument("--order", type=int, default=24)
    value.add_argument("--outer-segments", type=int, default=128)
    value.add_argument("--theta-segments", type=int, default=32)
    value.add_argument("--node-width", type=float, default=1.0e-10)
    value.add_argument("--series-terms", type=int, default=10)
    return value


def main() -> int:
    arguments = parser().parse_args()
    if not 1 <= arguments.index <= 90:
        raise ValueError("index must lie in [1,90]")
    ctx.dps = arguments.dps
    execute(arguments)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
