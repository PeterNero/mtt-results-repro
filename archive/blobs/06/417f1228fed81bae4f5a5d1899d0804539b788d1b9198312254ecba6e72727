from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

from flint import acb, acb_mat, acb_poly, arb, ctx

import certify_q79_selected_alignment_E32_handle_combination_interval as handle
import certify_q79_selected_alignment_single_E32_thimble_nodal_factor as nodal
import certify_q79_selected_side_beta_defect_transport as validated
from q79genus2_period_transport import FORM_NAMES


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
PERIOD_DIRECTORY = DIRECTORY / "selected_alignment_thimble_periods"
DEFAULT_INDEX = 4


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def decoded_acb(value: dict[str, str]) -> acb:
    return acb(arb(value["real"]), arb(value["imaginary"]))


def exact_ball(center: acb, radius: float) -> acb:
    return acb(
        arb(str(center.real.mid()), format(radius, ".17g")),
        arb(str(center.imag.mid()), format(radius, ".17g")),
    )


def factor_product(values: list[acb]) -> list[acb]:
    q0, q1, *h = values
    result = [acb(0) for _ in range(7)]
    for q_degree, q_value in enumerate((q0, q1, acb(1))):
        for h_degree, h_value in enumerate(h):
            result[q_degree + h_degree] += q_value * h_value
    return result


def factor_jacobian(values: list[acb]) -> acb_mat:
    q0, q1, *h = values
    jacobian = acb_mat(7, 7)
    for degree in range(7):
        if degree <= 4:
            jacobian[degree, 0] = h[degree]
        if 0 <= degree - 1 <= 4:
            jacobian[degree, 1] = h[degree - 1]
        for h_degree in range(5):
            q_degree = degree - h_degree
            if q_degree == 0:
                jacobian[degree, 2 + h_degree] = q0
            elif q_degree == 1:
                jacobian[degree, 2 + h_degree] = q1
            elif q_degree == 2:
                jacobian[degree, 2 + h_degree] = acb(1)
    return jacobian


def midpoint_factor(
    system: validated.SelectedQ79IntervalSystem,
    parameter: acb,
    node_root: acb,
) -> tuple[list[acb], dict]:
    coefficients, _derivative = nodal.fiber_coefficients(system, nodal.midpoint(parameter))
    roots = acb_poly(coefficients).roots(tol=1.0e-55, maxprec=8192)
    if len(roots) != 6:
        raise AssertionError("midpoint sextic root isolation failed")
    distance_rows = sorted(
        (
            validated.upper(abs(root - node_root)),
            validated.lower(abs(root - node_root)),
            index,
        )
        for index, root in enumerate(roots)
    )
    selected = [distance_rows[0][2], distance_rows[1][2]]
    if max(distance_rows[0][0], distance_rows[1][0]) >= distance_rows[2][1]:
        raise AssertionError("local colliding pair is not separated from the other roots")
    first, second = roots[selected[0]], roots[selected[1]]
    q0 = first * second
    q1 = -(first + second)
    h = [acb(0) for _ in range(5)]
    h[4] = coefficients[6]
    h[3] = coefficients[5] - q1 * h[4]
    h[2] = coefficients[4] - q1 * h[3] - q0 * h[4]
    h[1] = coefficients[3] - q1 * h[2] - q0 * h[3]
    h[0] = coefficients[2] - q1 * h[1] - q0 * h[2]
    values = [q0, q1, *h]
    residual = [
        left - right for left, right in zip(factor_product(values), coefficients)
    ]
    if not all(value.contains(0) for value in residual):
        raise AssertionError("midpoint factorization residual excludes zero")
    return [nodal.midpoint(value) for value in values], {
        "selected_root_indices_zero_based": selected,
        "second_to_third_node_distance_gap_lower": (
            distance_rows[2][1] - max(distance_rows[0][0], distance_rows[1][0])
        ),
    }


def parametric_factor_box(
    system: validated.SelectedQ79IntervalSystem,
    node_parameter: acb,
    node_root: acb,
    x_left: float,
    x_right: float,
    *,
    node_values: list[acb] | None = None,
) -> tuple[list[acb], acb, dict]:
    x_midpoint = (x_left + x_right) / 2
    x_radius = (x_right - x_left) / 2
    x_box = arb(format(x_midpoint, ".17g"), format(x_radius, ".17g"))
    parameter_box = node_parameter * (acb(1) - acb(x_box))
    coefficients, _derivative = nodal.fiber_coefficients(system, parameter_box)
    if node_values is not None and x_left == 0.0:
        center = [nodal.midpoint(value) for value in node_values]
        pair_diagnostics = {"selected_root_indices_zero_based": None}
    else:
        center, pair_diagnostics = midpoint_factor(
            system, nodal.midpoint(parameter_box), node_root
        )
    residual = [
        left - right for left, right in zip(factor_product(center), coefficients)
    ]
    target = acb_mat([[value] for value in residual])
    point_correction = system.verified_solve(factor_jacobian(center), target)
    radii = [
        max(4.0 * validated.upper(abs(point_correction[index, 0])), 1.0e-70)
        for index in range(7)
    ]
    attempts = []
    for attempt in range(12):
        boxes = [exact_ball(value, radius) for value, radius in zip(center, radii)]
        try:
            correction = system.verified_solve(factor_jacobian(boxes), target)
        except ZeroDivisionError:
            radii = [2.0 * value for value in radii]
            continue
        images = [center[index] - correction[index, 0] for index in range(7)]
        inclusion = [
            boxes[index].contains_interior(images[index]) for index in range(7)
        ]
        attempts.append(
            {
                "attempt": attempt + 1,
                "maximum_box_radius": max(radii),
                "maximum_newton_image_radius": max(
                    validated.radius_upper(value) for value in images
                ),
                "all_interior": bool(all(inclusion)),
            }
        )
        if all(inclusion):
            enclosures = [
                exact_ball(
                    nodal.midpoint(image),
                    max(1.25 * validated.radius_upper(image), 1.0e-70),
                )
                for image in images
            ]
            final_residual = [
                left - right
                for left, right in zip(factor_product(enclosures), coefficients)
            ]
            if not all(value.contains(0) for value in final_residual):
                # The interval-Newton image is authoritative; dependency in a
                # direct substitution can be wider without invalidating it.
                residual_contains_zero = False
            else:
                residual_contains_zero = True
            return enclosures, parameter_box, {
                "x_interval": {"lower": x_left, "upper": x_right},
                "parameter_radius_upper": validated.radius_upper(parameter_box),
                "maximum_factor_radius_upper": max(
                    validated.radius_upper(value) for value in enclosures
                ),
                "parametric_interval_newton_inclusion": True,
                "factor_substitution_residual_contains_zero": residual_contains_zero,
                "attempts": attempts,
                **pair_diagnostics,
            }
        radii = [2.0 * value for value in radii]
    raise ArithmeticError(
        "parametric Hensel inclusion failed on "
        f"[{x_left:.3e},{x_right:.3e}]: "
        f"point_corrections={[validated.upper(abs(point_correction[index, 0])) for index in range(7)]!r}; "
        f"attempts={attempts!r}"
    )


def validated_ab_models_from_node_path(
    system: validated.SelectedQ79IntervalSystem,
    node_parameter: acb,
    center_x: float,
    radius: arb,
    order: int,
) -> tuple[validated.TaylorModel, validated.TaylorModel, dict]:
    parameter_center = node_parameter * acb(format(1.0 - center_x, ".17g"))
    a_value, b_value, _line, _line_derivative = system.ab_line_data(parameter_center)
    direction = -node_parameter
    scale = acb(0, 1) * direction * system.period_length
    a_coefficients = [acb(0) for _ in range(order + 1)]
    b_coefficients = [acb(0) for _ in range(order + 1)]
    a_coefficients[0] = a_value
    b_coefficients[0] = b_value
    for degree in range(order):
        a_coefficients[degree + 1] = (
            acb(2) * scale * b_coefficients[degree] / acb(degree + 1)
        )
        a_squared = sum(
            (
                a_coefficients[index] * a_coefficients[degree - index]
                for index in range(degree + 1)
            ),
            acb(0),
        )
        b_coefficients[degree + 1] = scale * (
            acb(3) * a_squared - acb(int(degree == 0))
        ) / acb(degree + 1)
    a_candidate = validated.TaylorModel(a_coefficients, radius).midpoint_polynomial()
    b_candidate = validated.TaylorModel(b_coefficients, radius).midpoint_polynomial()
    residual_a = a_candidate.derivative_polynomial() - acb(2) * scale * b_candidate
    residual_b = b_candidate.derivative_polynomial() - scale * (
        acb(3) * a_candidate**2 - 1
    )
    residual_bound = max(
        residual_a.absolute_bound(),
        residual_b.absolute_bound(),
        key=lambda value: validated.upper(value),
    )
    initial_error = arb(
        str(max(validated.radius_upper(a_value), validated.radius_upper(b_value)))
    )
    error = initial_error
    for _ in range(16):
        a_bound = a_candidate.absolute_bound() + error
        lipschitz = max(
            acb(2).real * abs(scale),
            acb(6).real * abs(scale) * a_bound,
            key=lambda value: validated.upper(value),
        )
        growth = (lipschitz * radius).exp()
        defect = (
            residual_bound * radius
            if validated.upper(lipschitz) == 0
            else residual_bound * (growth - arb(1)) / lipschitz
        )
        updated = growth * initial_error + defect
        if validated.upper(updated) <= validated.upper(error) * (1.0 + 1.0e-12):
            error = updated
            break
        error = updated
    else:
        raise ArithmeticError("node-path elliptic Taylor enclosure did not stabilize")
    return (
        a_candidate.copy_with_remainder(error),
        b_candidate.copy_with_remainder(error),
        {
            "elliptic_ODE_residual_upper": validated.upper(residual_bound),
            "elliptic_uniform_remainder_upper": validated.upper(error),
            "parameter_center": nodal.encoded_acb(parameter_center),
            "parameter_direction": nodal.encoded_acb(direction),
        },
    )


def factor_taylor_models(
    system: validated.SelectedQ79IntervalSystem,
    node_parameter: acb,
    node_root: acb,
    *,
    epsilon: float,
    order: int,
) -> tuple[list[validated.TaylorModel], dict]:
    center_x = epsilon / 2
    radius = arb(format(epsilon / 2, ".17g"))
    a_model, b_model, elliptic_diagnostics = validated_ab_models_from_node_path(
        system, node_parameter, center_x, radius, order
    )
    prototype = a_model
    one = prototype.constant(1, order, radius)
    zero = prototype.constant(0, order, radius)
    elliptic = [a_model, b_model, one]
    da_dw = acb(2) * system.period_length * b_model
    db_dw = system.period_length * (acb(3) * a_model**2 - 1)
    line = validated.tm_matrix_vector(system.alignment, elliptic)
    line_derivative = validated.tm_matrix_vector(
        system.alignment, [da_dw, db_dw, zero]
    )
    f_models, _f_derivative = validated.aligned_tm_coefficients_and_derivative(
        system.evaluator.tables["F6"],
        line,
        line_derivative,
        chart=system.line_chart,
    )
    parameter_center = nodal.midpoint(node_parameter) * acb(
        format(1.0 - center_x, ".17g")
    )
    center_values, pair_diagnostics = midpoint_factor(
        system, parameter_center, node_root
    )
    coefficient_rows = [
        [acb(0) for _ in range(order + 1)] for _ in range(7)
    ]
    for index, value in enumerate(center_values):
        coefficient_rows[index][0] = value
    center_jacobian = factor_jacobian(center_values)

    for degree in range(1, order + 1):
        known_values = [
            validated.TaylorModel(row[: degree + 1], arb(0))
            for row in coefficient_rows
        ]
        known_product = factor_product_models(known_values)
        right = acb_mat(7, 1)
        for equation in range(7):
            right[equation, 0] = (
                f_models[equation].coefficients[degree]
                - known_product[equation].coefficients[degree]
            )
        solved = center_jacobian.solve(right)
        for index in range(7):
            coefficient_rows[index][degree] = solved[index, 0]

    candidates = [
        validated.TaylorModel(coefficients, radius)
        for coefficients in coefficient_rows
    ]
    residual_models = [
        left - right
        for left, right in zip(factor_product_models(candidates), f_models)
    ]
    residual_norm = max(
        (value.absolute_bound() for value in residual_models),
        key=lambda value: validated.upper(value),
    )
    jacobian_models = factor_jacobian_models(candidates)
    inverse_norm, inverse_defect = validated.tm_verified_inverse_bound(
        jacobian_models
    )
    inverse_upper = validated.upper(inverse_norm)
    eta = inverse_upper * validated.upper(residual_norm)
    correction_radius = max(2.0 * eta, 1.0e-70)
    self_map = eta + 2.0 * inverse_upper * correction_radius**2
    contraction = 4.0 * inverse_upper * correction_radius
    if self_map > correction_radius or contraction >= 1.0:
        raise ArithmeticError(
            "Taylor-Hensel radii inequality failed: "
            f"eta={eta:.3e}, radius={correction_radius:.3e}, "
            f"self_map={self_map:.3e}, contraction={contraction:.3e}"
        )
    certified = [
        candidate.copy_with_remainder(arb(format(correction_radius, ".17g")))
        for candidate in candidates
    ]
    return certified, {
        "center_x": center_x,
        "disk_radius": epsilon / 2,
        "order": order,
        "factor_residual_infinity_norm_upper": validated.upper(residual_norm),
        "factor_jacobian_inverse_infinity_norm_upper": inverse_upper,
        "factor_jacobian_inverse_defect_upper": inverse_defect,
        "newton_eta_upper": eta,
        "uniform_factor_correction_radius": correction_radius,
        "self_map_bound_upper": self_map,
        "contraction_bound_upper": contraction,
        "quantitative_Hensel_disk_closed": True,
        **elliptic_diagnostics,
        **pair_diagnostics,
    }


def factor_product_models(
    values: list[validated.TaylorModel],
) -> list[validated.TaylorModel]:
    q0, q1, *h = values
    one = q0.constant(1, q0.order, q0.radius)
    zero = q0.constant(0, q0.order, q0.radius)
    result = [zero for _ in range(7)]
    for q_degree, q_value in enumerate((q0, q1, one)):
        for h_degree, h_value in enumerate(h):
            result[q_degree + h_degree] += q_value * h_value
    return result


def factor_jacobian_models(
    values: list[validated.TaylorModel],
) -> list[list[validated.TaylorModel]]:
    q0, q1, *h = values
    zero = q0.constant(0, q0.order, q0.radius)
    one = q0.constant(1, q0.order, q0.radius)
    result = [[zero for _ in range(7)] for _ in range(7)]
    for degree in range(7):
        if degree <= 4:
            result[degree][0] = h[degree]
        if 0 <= degree - 1 <= 4:
            result[degree][1] = h[degree - 1]
        for h_degree in range(5):
            q_degree = degree - h_degree
            if q_degree == 0:
                result[degree][2 + h_degree] = q0
            elif q_degree == 1:
                result[degree][2 + h_degree] = q1
            elif q_degree == 2:
                result[degree][2 + h_degree] = one
    return result


def evaluate_factor_models(
    models: list[validated.TaylorModel],
    x_left: float,
    x_right: float,
    center_x: float,
) -> list[acb]:
    argument = arb(
        format((x_left + x_right) / 2 - center_x, ".17g"),
        format((x_right - x_left) / 2, ".17g"),
    )
    result = []
    for model in models:
        value = model.evaluate_polynomial(argument)
        result.append(
            exact_ball(
                nodal.midpoint(value),
                validated.radius_upper(value) + validated.upper(model.remainder),
            )
        )
    return result


def rotations() -> list[acb]:
    return [
        acb(
            format(math.cos(index * math.pi / 8), ".17g"),
            format(math.sin(index * math.pi / 8), ".17g"),
        )
        for index in range(16)
    ]


def period_enclosure(
    factor: list[acb], *, theta_segments: int
) -> tuple[list[acb], dict]:
    q0, q1, *quartic = factor
    center = -q1 / acb(2)
    discriminant = q1**2 - acb(4) * q0
    discriminant_lower = validated.lower(abs(discriminant))
    if discriminant_lower <= 0:
        raise ZeroDivisionError("regular period segment contains the nodal discriminant")
    half = discriminant.sqrt() / acb(2)
    total = [acb(0), acb(0)]
    previous_root: acb | None = None
    minimum_half_plane_margin = math.inf
    minimum_sign_margin = math.inf
    for segment in range(theta_segments):
        left = math.pi * segment / theta_segments
        right = math.pi * (segment + 1) / theta_segments
        theta_box = acb(
            arb(
                format((left + right) / 2, ".17g"),
                format((right - left) / 2, ".17g"),
            )
        )
        point_box = center + half * theta_box.cos()
        remainder_box = nodal.polynomial(quartic, point_box)
        rotation_rows = [
            (rotation, validated.lower((rotation * remainder_box).real))
            for rotation in rotations()
        ]
        rotation, margin = max(rotation_rows, key=lambda row: row[1])
        if margin <= 0:
            raise ArithmeticError("quartic image does not fit a square-root half-plane")
        minimum_half_plane_margin = min(minimum_half_plane_margin, margin)
        rotation_root = rotation.sqrt()

        def square_root(theta: acb) -> acb:
            point = center + half * theta.cos()
            return (rotation * nodal.polynomial(quartic, point)).sqrt() / rotation_root

        candidate = square_root(acb(format(left, ".17g")))
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
                raise ArithmeticError("quartic square-root sign is not separated")
            minimum_sign_margin = min(minimum_sign_margin, sign_margin)
        denominator = acb(sign) * (
            rotation * remainder_box
        ).sqrt() / rotation_root
        width = acb(format(right - left, ".17g"))
        for power in range(2):
            total[power] += acb(0, 2) * point_box**power * width / denominator
        previous_root = acb(sign) * square_root(acb(format(right, ".17g")))
    return total, {
        "quadratic_discriminant_absolute_lower": discriminant_lower,
        "minimum_quartic_half_plane_margin": minimum_half_plane_margin,
        "minimum_square_root_sign_margin": (
            None if not math.isfinite(minimum_sign_margin) else minimum_sign_margin
        ),
        "maximum_period_radius_upper": max(
            validated.radius_upper(value) for value in total
        ),
    }


def orient_periods(
    periods: list[acb], reference: list[acb]
) -> tuple[list[acb], int, float, float]:
    plus_upper = max(
        validated.upper(abs(value - target))
        for value, target in zip(periods, reference)
    )
    minus_upper = max(
        validated.upper(abs(-value - target))
        for value, target in zip(periods, reference)
    )
    sign = 1 if plus_upper <= minus_upper else -1
    selected_upper = min(plus_upper, minus_upper)
    rejected_lower = max(
        validated.lower(abs(-acb(sign) * value - target))
        for value, target in zip(periods, reference)
    )
    if selected_upper >= rejected_lower:
        raise AssertionError("period orientation is not interval-separated")
    return [acb(sign) * value for value in periods], sign, selected_upper, rejected_lower


def e32_residue_coefficients(
    system: validated.SelectedQ79IntervalSystem, parameter: acb
) -> tuple[acb, acb]:
    a_value, b_value, line, _line_derivative = system.ab_line_data(parameter)
    elliptic = [a_value, b_value, acb(1)]
    generator = system.generators[FORM_NAMES.index("E32")]
    variation = validated.matrix_vector(system.alignment * generator, elliptic)
    if system.line_chart == "z":
        constant = line[2] * (variation[0] * line[2] - variation[2] * line[0])
        linear = line[2] * (variation[1] * line[2] - variation[2] * line[1])
    else:
        constant = -line[1] * (
            variation[0] * line[1] - variation[1] * line[0]
        )
        linear = -line[1] * (
            variation[2] * line[1] - variation[1] * line[2]
        )
    return system.period_length * constant, system.period_length * linear


def node_segment_bound(
    factor: list[acb],
    system: validated.SelectedQ79IntervalSystem,
    parameter_box: acb,
    node_parameter: acb,
    width: float,
) -> tuple[acb, dict]:
    q0, q1, *quartic = factor
    center = -q1 / acb(2)
    discriminant = q1**2 - acb(4) * q0
    half_upper = math.sqrt(validated.upper(abs(discriminant))) / 2
    center_upper = validated.upper(abs(center))
    point_upper = center_upper + half_upper
    point_box = exact_ball(nodal.midpoint(center), half_upper)
    quartic_value = nodal.polynomial(quartic, point_box)
    quartic_lower = validated.lower(abs(quartic_value))
    if quartic_lower <= 0:
        raise AssertionError("node-segment quartic bound meets zero")
    period_0_upper = 2 * math.pi / math.sqrt(quartic_lower)
    period_1_upper = period_0_upper * point_upper
    constant, linear = e32_residue_coefficients(system, parameter_box)
    residue_upper = (
        validated.upper(abs(constant)) * period_0_upper
        + validated.upper(abs(linear)) * period_1_upper
    )
    integrand_upper = validated.upper(abs(acb(0, 1) * node_parameter)) * residue_upper
    radius = width * integrand_upper
    contribution = acb(arb(0, format(radius, ".17g")), arb(0, format(radius, ".17g")))
    return contribution, {
        "half_difference_absolute_upper": half_upper,
        "quartic_on_cut_absolute_lower": quartic_lower,
        "period_I0_absolute_upper": period_0_upper,
        "period_I1_absolute_upper": period_1_upper,
        "E32_integrand_absolute_upper": integrand_upper,
        "contribution_radius_upper": validated.radius_upper(contribution),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--distinguished-index", type=int, default=DEFAULT_INDEX)
    parser.add_argument("--epsilon", type=float, default=1.0e-5)
    parser.add_argument("--node-width", type=float, default=1.0e-10)
    parser.add_argument("--outer-segments", type=int, default=48)
    parser.add_argument("--theta-segments", type=int, default=32)
    parser.add_argument("--factor-order", type=int, default=32)
    parser.add_argument("--dps", type=int, default=100)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    if not 0 < arguments.node_width < arguments.epsilon:
        raise ValueError("node width must lie in (0, epsilon)")
    ctx.dps = arguments.dps

    source_path = nodal.candidate_path(arguments.distinguished_index)
    source = load(source_path)
    node_path = PERIOD_DIRECTORY / (
        f"d{arguments.distinguished_index:03d}_{source['root_id']}.nodal_factor.interval.packet.json"
    )
    if not node_path.exists():
        raise FileNotFoundError("run the selected nodal-factor certifier first")
    node_packet = load(node_path)
    if node_packet["selected_thimble"]["line_chart"] != source["line_chart"]:
        raise AssertionError("nodal-factor and floating source charts differ")
    node_parameter = decoded_acb(node_packet["certified_node"]["parameter_ball"])
    node_root = decoded_acb(node_packet["certified_node"]["double_root_ball"])
    factor_packet = node_packet["local_weierstrass_factor"]
    node_values = [
        decoded_acb(value)
        for value in factor_packet["monic_quadratic_coefficients_ascending"][:2]
        + factor_packet["quartic_coefficients_ascending"]
    ]
    system = validated.SelectedQ79IntervalSystem(
        dps=arguments.dps, line_chart=source["line_chart"]
    )
    factor_models, factor_disk_diagnostics = factor_taylor_models(
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
    cutoff_roots = acb_poly(cutoff_coefficients).roots(tol=1.0e-55, maxprec=8192)
    cutoff_pair = nodal.closest_pair(cutoff_roots)
    cutoff_periods, cutoff_diagnostics = handle.direct_cut_periods(
        cutoff_roots,
        cutoff_coefficients[6],
        cutoff_pair,
        segments=arguments.theta_segments,
        tolerance=1.0e-35,
    )
    reference = cutoff_periods[:2]

    node_factor = evaluate_factor_models(
        factor_models,
        0.0,
        arguments.node_width,
        factor_disk_diagnostics["center_x"],
    )
    node_x_box = arb(
        format(arguments.node_width / 2, ".17g"),
        format(arguments.node_width / 2, ".17g"),
    )
    node_parameter_box = node_parameter * (acb(1) - acb(node_x_box))
    node_factor_diagnostics = {
        "x_interval": {"lower": 0.0, "upper": arguments.node_width},
        "maximum_factor_radius_upper": max(
            validated.radius_upper(value) for value in node_factor
        ),
        "source": "single quantitative Taylor-Hensel disk",
    }
    node_contribution, node_bound = node_segment_bound(
        node_factor,
        system,
        node_parameter_box,
        node_parameter,
        arguments.node_width,
    )
    total = node_contribution
    rows = []
    previous_factor: list[acb] | None = None
    ratio = (arguments.epsilon / arguments.node_width) ** (
        1.0 / arguments.outer_segments
    )
    edges = [arguments.node_width * ratio**index for index in range(arguments.outer_segments)]
    edges.append(arguments.epsilon)
    intervals = list(zip(edges[:-1], edges[1:]))
    # Start at the cutoff, whose direct-cut orientation is also used by the
    # validated main-segment engine, and continue that sign toward the node.
    for reverse_index, (x_left, x_right) in enumerate(reversed(intervals)):
        factor = evaluate_factor_models(
            factor_models,
            x_left,
            x_right,
            factor_disk_diagnostics["center_x"],
        )
        x_box = arb(
            format((x_left + x_right) / 2, ".17g"),
            format((x_right - x_left) / 2, ".17g"),
        )
        parameter_box = node_parameter * (acb(1) - acb(x_box))
        factor_diagnostics = {
            "x_interval": {"lower": x_left, "upper": x_right},
            "parameter_radius_upper": validated.radius_upper(parameter_box),
            "maximum_factor_radius_upper": max(
                validated.radius_upper(value) for value in factor
            ),
            "source": "single quantitative Taylor-Hensel disk",
        }
        periods, period_diagnostics = period_enclosure(
            factor, theta_segments=arguments.theta_segments
        )
        periods, sign, selected_difference, rejected_difference = orient_periods(
            periods, reference
        )
        reference = periods
        constant, linear = e32_residue_coefficients(system, parameter_box)
        integrand = acb(0, 1) * node_parameter * (
            constant * periods[0] + linear * periods[1]
        )
        contribution = acb(format(x_right - x_left, ".17g")) * integrand
        total += contribution
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
                **factor_diagnostics,
                **period_diagnostics,
                "selected_period_sign": sign,
                "selected_orientation_difference_upper": selected_difference,
                "opposite_orientation_difference_lower": rejected_difference,
                "factor_overlap_with_node_side_neighbor": bool(all(overlap)),
                "E32_integrand_interval": handle.complex_interval(integrand),
                "E32_contribution_interval": handle.complex_interval(contribution),
            }
        )
        previous_factor = factor
        if (reverse_index + 1) % 8 == 0:
            print(
                "certified E32 tail "
                f"segments={reverse_index + 1}/{arguments.outer_segments} "
                f"x=[{x_left:.3e},{arguments.epsilon:.3e}] "
                f"radius={validated.radius_upper(total):.3e}",
                flush=True,
            )

    if previous_factor is None or not all(
        previous_factor[index].overlaps(node_factor[index]) for index in range(7)
    ):
        raise AssertionError("Taylor-Hensel factor chain does not overlap the node segment")

    output = arguments.output
    if output is None:
        output = PERIOD_DIRECTORY / (
            f"d{arguments.distinguished_index:03d}_{source['root_id']}.E32_tail.interval.packet.json"
        )
    elif not output.is_absolute():
        output = ROOT / output
    floating_full = handle.complex_value(
        source["execution"]["period_values"][FORM_NAMES.index("E32")]
    )
    payload = {
        "schema": "MTTQ79SelectedAlignmentSingleE32ThimbleTailInterval.v1",
        "status": "SELECTED_E32_NODE_TO_EPSILON_TAIL_INTERVAL_CERTIFIED",
        "authority": {
            "floating_candidate": relative(source_path),
            "floating_candidate_sha256": sha256(source_path),
            "nodal_factor": relative(node_path),
            "nodal_factor_sha256": sha256(node_path),
            "builder_source": relative(Path(__file__)),
            "builder_source_sha256": sha256(Path(__file__)),
        },
        "selected_thimble": {
            "distinguished_index": arguments.distinguished_index,
            "root_id": source["root_id"],
            "line_chart": source["line_chart"],
            "endpoint_cutoff_epsilon": arguments.epsilon,
            "cutoff_pair_zero_based": list(cutoff_pair),
        },
        "cutoff_direct_period_reference": {
            **cutoff_diagnostics,
            "I0_I1_intervals": [handle.complex_interval(value) for value in cutoff_periods[:2]],
        },
        "node_segment": {
            "x_interval": {"lower": 0.0, "upper": arguments.node_width},
            "factor_certificate": node_factor_diagnostics,
            "absolute_bound": node_bound,
            "contribution_interval": handle.complex_interval(node_contribution),
        },
        "quantitative_Hensel_disk": factor_disk_diagnostics,
        "regular_segments": rows,
        "E32_endpoint_tail": {
            "interval": handle.complex_interval(total),
            "interval_center": handle.complex_pair(handle.midpoint(total)),
            "interval_radius_upper": validated.radius_upper(total),
            "floating_full_value_diagnostic_only": handle.complex_pair(floating_full),
        },
        "scope": {
            "observed_SM_values_used": False,
            "parametric_Hensel_chain_closed": True,
            "desingularized_period_Riemann_enclosures_closed": True,
            "node_absolute_bound_closed": True,
            "endpoint_tail_interval_closed": True,
            "floating_value_used_as_bound": False,
            "full_E32_thimble_interval_closed": False,
        },
        "next_required_artifact": "splice this tail interval to the validated E32 main-segment interval",
    }
    dump(output, payload)
    print(f"wrote {relative(output)}")
    print(
        json.dumps(
            {
                "distinguished_index": arguments.distinguished_index,
                "tail_center": handle.complex_pair(handle.midpoint(total)),
                "tail_radius": validated.radius_upper(total),
                "node_bound_radius": validated.radius_upper(node_contribution),
                "regular_segments": len(rows),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
