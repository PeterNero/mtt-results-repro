from __future__ import annotations

import json
import math
from pathlib import Path

import mpmath as mp
import sympy as sp
from flint import acb, acb_poly, ctx

from certify_q79_selected_side_beta_defect_transport import (
    SelectedQ79IntervalSystem,
    encoded_acb,
    lower,
    midpoint,
    radius_upper,
)


ROOT = Path(__file__).resolve().parents[1]
MODEL = (
    ROOT
    / "candidate_data"
    / "selected_q79k3perioddomainxihessianexecutionormarkedmodelgerbecertificate"
    / "explicit_splitting_conic_K3_model.packet.json"
)
IDENTITY_FIBRATION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2lefschetzperiodreduction"
    / "explicit_genus2_fibration.packet.json"
)
IDENTITY_DISCRIMINANT = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2lefschetzperiodreduction"
    / "degree90_nodal_discriminant_certificate.packet.json"
)
OUT = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_dual_discriminant.interval.packet.json"
)

ACBPoly = dict[int, acb]
EllipticPair = tuple[ACBPoly, ACBPoly]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def source_expression(table: list[dict], variables: tuple[sp.Symbol, ...]) -> sp.Expr:
    value = sp.Integer(0)
    for row in table:
        monomial = sp.Integer(row["coefficient"])
        for variable, power in zip(variables, row["powers_xyz"]):
            monomial *= variable ** int(power)
        value += monomial
    return sp.expand(value)


def reduce_on_elliptic_curve(
    expression: sp.Expr, a: sp.Symbol, b: sp.Symbol
) -> tuple[sp.Expr, sp.Expr]:
    reduced = sp.rem(
        sp.Poly(sp.expand(expression), b, domain=sp.QQ_I.frac_field(a)),
        sp.Poly(b**2 - a**3 + a, b, domain=sp.QQ_I.frac_field(a)),
    ).as_expr()
    polynomial = sp.Poly(sp.cancel(reduced), b, domain=sp.QQ_I.frac_field(a))
    p_value = sp.cancel(polynomial.coeff_monomial(1))
    q_value = sp.cancel(polynomial.coeff_monomial(b))
    if not sp.Poly(p_value, a).is_univariate or not sp.Poly(q_value, a).is_univariate:
        raise AssertionError("elliptic reduction did not produce polynomials")
    return sp.expand(p_value), sp.expand(q_value)


def poly_add(left: ACBPoly, right: ACBPoly) -> ACBPoly:
    result = dict(left)
    for degree, value in right.items():
        result[degree] = result.get(degree, acb(0)) + value
    return {degree: value for degree, value in result.items() if not value.is_zero()}


def poly_scale(value: ACBPoly, scalar: acb | int) -> ACBPoly:
    return {degree: coefficient * scalar for degree, coefficient in value.items()}


def poly_multiply(left: ACBPoly, right: ACBPoly) -> ACBPoly:
    result: ACBPoly = {}
    for left_degree, left_value in left.items():
        for right_degree, right_value in right.items():
            degree = left_degree + right_degree
            result[degree] = result.get(degree, acb(0)) + left_value * right_value
    return {degree: value for degree, value in result.items() if not value.is_zero()}


def poly_shift(value: ACBPoly, degree: int) -> ACBPoly:
    return {source + degree: coefficient for source, coefficient in value.items()}


def pair_add(left: EllipticPair, right: EllipticPair) -> EllipticPair:
    return poly_add(left[0], right[0]), poly_add(left[1], right[1])


def pair_scale(value: EllipticPair, scalar: acb | int) -> EllipticPair:
    return poly_scale(value[0], scalar), poly_scale(value[1], scalar)


def pair_multiply(left: EllipticPair, right: EllipticPair) -> EllipticPair:
    # b^2=a^3-a in the affine square-elliptic coordinate ring.
    p_product = poly_multiply(left[0], right[0])
    q_product = poly_multiply(left[1], right[1])
    q_relation = poly_add(poly_shift(q_product, 3), poly_scale(poly_shift(q_product, 1), -1))
    return (
        poly_add(p_product, q_relation),
        poly_add(
            poly_multiply(left[0], right[1]),
            poly_multiply(left[1], right[0]),
        ),
    )


def pair_power(value: EllipticPair, power: int) -> EllipticPair:
    result: EllipticPair = ({0: acb(1)}, {})
    factor = value
    exponent = power
    while exponent:
        if exponent & 1:
            result = pair_multiply(result, factor)
        exponent >>= 1
        if exponent:
            factor = pair_multiply(factor, factor)
    return result


def encode_poly(value: ACBPoly, maximum_degree: int) -> list[dict]:
    return [
        {
            "degree": degree,
            "coefficient": encoded_acb(value.get(degree, acb(0))),
            "radius_upper": format(
                radius_upper(value.get(degree, acb(0))), ".17g"
            ),
        }
        for degree in range(maximum_degree + 1)
    ]


def poly_evaluate(value: ACBPoly, argument: acb) -> acb:
    result = acb(0)
    for degree in range(max(value, default=-1), -1, -1):
        result = result * argument + value.get(degree, acb(0))
    return result


def poly_derivative(value: ACBPoly) -> ACBPoly:
    return {
        degree - 1: coefficient * degree
        for degree, coefficient in value.items()
        if degree > 0
    }


def main() -> int:
    ctx.dps = 100
    mp.mp.dps = 100
    model = load(MODEL)
    identity_fibration = load(IDENTITY_FIBRATION)
    identity_discriminant = load(IDENTITY_DISCRIMINANT)
    x, y, z, t, l0, l1, l2, a, b = sp.symbols(
        "x y z t l0 l1 l2 a b"
    )
    f6 = source_expression(model["coefficient_tables"]["F6"], (x, y, z))

    binary_y = sp.expand(
        f6.subs({x: l1, y: -(l0 + l2 * t), z: l1 * t})
    )
    chart_discriminant = sp.discriminant(binary_y, t)
    quotient, remainder = sp.div(
        sp.Poly(chart_discriminant, l0, l1, l2),
        sp.Poly(l1**30, l0, l1, l2),
    )
    if remainder.as_expr() != 0:
        raise AssertionError("chart discriminant lacks the L1^30 factor")
    dual = sp.Poly(quotient, l0, l1, l2, domain=sp.ZZ)
    if dual.total_degree() != 30:
        raise AssertionError("dual sextic discriminant degree changed")

    identity_pullback = sp.expand(dual.as_expr().subs({l0: a, l1: b, l2: 1}))
    identity_p, identity_q = reduce_on_elliptic_curve(identity_pullback, a, b)
    expected_raw = sp.discriminant(
        sum(
            sp.sympify(value) * t ** (6 - index)
            for index, value in enumerate(
                identity_fibration["fiber_chart"][
                    "f_coefficients_t_descending"
                ]
            )
        ),
        t,
    )
    expected_p, expected_q = reduce_on_elliptic_curve(expected_raw, a, b)
    if sp.expand(identity_p - expected_p) != 0 or sp.expand(identity_q - expected_q) != 0:
        raise AssertionError("dual pullback does not reproduce A111")
    stored_p = sp.sympify(
        identity_discriminant["discriminant_on_E"]["P45"]
    )
    stored_q = sp.sympify(
        identity_discriminant["discriminant_on_E"]["Q43"]
    )
    if sp.expand(identity_p - stored_p) != 0 or sp.expand(identity_q - stored_q) != 0:
        raise AssertionError("dual pullback disagrees with stored A111 rows")

    system = SelectedQ79IntervalSystem(dps=100)
    alignment = system.alignment
    line: list[EllipticPair] = [
        (
            {0: alignment[row, 2], 1: alignment[row, 0]},
            {0: alignment[row, 1]},
        )
        for row in range(3)
    ]
    selected: EllipticPair = ({}, {})
    for powers, integer_coefficient in dual.terms():
        contribution: EllipticPair = ({0: acb(int(integer_coefficient))}, {})
        for source, power in zip(line, powers):
            contribution = pair_multiply(contribution, pair_power(source, power))
        selected = pair_add(selected, contribution)
    p_selected, q_selected = selected
    p_degree = max(p_selected, default=-1)
    q_degree = max(q_selected, default=-1)
    if p_degree > 45 or q_degree > 43:
        raise AssertionError("selected dual pullback exceeds the degree-90 section")

    p_squared = poly_multiply(p_selected, p_selected)
    q_squared = poly_multiply(q_selected, q_selected)
    norm = poly_add(
        p_squared,
        poly_scale(
            poly_add(poly_shift(q_squared, 3), poly_scale(poly_shift(q_squared, 1), -1)),
            -1,
        ),
    )
    norm_degree = max(norm, default=-1)
    if norm_degree != 90 or lower(abs(norm[90])) <= 0:
        raise AssertionError("selected discriminant norm is not degree 90")

    roots = acb_poly([norm.get(index, acb(0)) for index in range(91)]).roots(
        tol=1.0e-45,
        maxprec=4096,
    )
    if len(roots) != 90 or not all(root.is_finite() for root in roots):
        raise AssertionError("selected norm root isolation failed")
    minimum_root_separation = math.inf
    for first, left_root in enumerate(roots):
        for right_root in roots[:first]:
            minimum_root_separation = min(
                minimum_root_separation,
                lower(abs(left_root - right_root)),
            )
    if minimum_root_separation <= 0:
        raise AssertionError("selected norm root balls overlap")

    elliptic_parameter = mp.mpf("0.5")
    period_length = mp.sqrt(2) * mp.ellipk(elliptic_parameter)
    sn = mp.ellipfun("sn")
    cn = mp.ellipfun("cn")
    dn = mp.ellipfun("dn")

    def elliptic_ab(z_value: mp.mpc) -> tuple[mp.mpc, mp.mpc]:
        argument = mp.sqrt(2) * z_value
        sn_value = sn(argument, elliptic_parameter)
        cn_value = cn(argument, elliptic_parameter)
        dn_value = dn(argument, elliptic_parameter)
        return (
            -1 + 2 / sn_value**2,
            -2 * mp.sqrt(2) * cn_value * dn_value / sn_value**3,
        )

    critical_points = []
    critical_w_centers: list[complex] = []
    critical_w_radii: list[float] = []
    norm_derivative = poly_derivative(norm)
    minimum_norm_derivative_lower = math.inf
    minimum_q_value_lower = math.inf
    minimum_b_value_lower = math.inf
    minimum_opposite_sheet_factor_lower = math.inf
    maximum_elliptic_relation_radius = 0.0
    maximum_discriminant_value_radius = 0.0
    for point_index, root in enumerate(
        sorted(roots, key=lambda value: (midpoint(value).real, midpoint(value).imag)),
        start=1,
    ):
        p_value = poly_evaluate(p_selected, root)
        q_value = poly_evaluate(q_selected, root)
        q_lower = lower(abs(q_value))
        if q_lower <= 0:
            raise AssertionError("Q43_A vanishes on a selected norm root ball")
        b_value = -p_value / q_value
        b_lower = lower(abs(b_value))
        derivative_lower = lower(abs(poly_evaluate(norm_derivative, root)))
        opposite_sheet_factor = p_value - b_value * q_value
        opposite_lower = lower(abs(opposite_sheet_factor))
        if b_lower <= 0:
            raise AssertionError("a is not a local coordinate at a critical point")
        if derivative_lower <= 0:
            raise AssertionError("selected norm root is not certified simple")
        if opposite_lower <= 0:
            raise AssertionError("both elliptic sheets meet the discriminant")
        elliptic_relation = b_value**2 - root**3 + root
        discriminant_value = p_value + b_value * q_value
        if not elliptic_relation.contains(0):
            raise AssertionError("critical lift misses the elliptic curve")
        if not discriminant_value.contains(0):
            raise AssertionError("critical lift misses the dual discriminant")
        minimum_q_value_lower = min(minimum_q_value_lower, q_lower)
        minimum_b_value_lower = min(minimum_b_value_lower, b_lower)
        minimum_norm_derivative_lower = min(
            minimum_norm_derivative_lower, derivative_lower
        )
        minimum_opposite_sheet_factor_lower = min(
            minimum_opposite_sheet_factor_lower, opposite_lower
        )
        maximum_elliptic_relation_radius = max(
            maximum_elliptic_relation_radius,
            radius_upper(elliptic_relation),
        )
        maximum_discriminant_value_radius = max(
            maximum_discriminant_value_radius,
            radius_upper(discriminant_value),
        )

        a_center_complex = midpoint(root)
        b_center_complex = midpoint(b_value)
        a_center = mp.mpc(a_center_complex.real, a_center_complex.imag)
        b_center = mp.mpc(b_center_complex.real, b_center_complex.imag)
        inverse_argument = mp.asin(mp.sqrt(2 / (a_center + 1)))
        z_value = mp.ellipf(inverse_argument, elliptic_parameter) / mp.sqrt(2)
        _, inverse_b = elliptic_ab(z_value)
        if abs(inverse_b - b_center) > abs(-inverse_b - b_center):
            z_value = -z_value
        w_value = z_value / period_length
        w_value -= mp.nint(mp.re(w_value)) + 1j * mp.nint(mp.im(w_value))

        a_radius = mp.mpf(str(radius_upper(root)))
        cubic_center = a_center**3 - a_center
        cubic_variation = a_radius * (3 * (abs(a_center) + a_radius) ** 2 + 1)
        cubic_lower = abs(cubic_center) - cubic_variation
        if cubic_lower <= 0:
            raise AssertionError("elliptic inverse branch contains b=0")
        inverse_derivative_upper = 1 / (
            2 * period_length * mp.sqrt(cubic_lower)
        )
        w_radius = a_radius * inverse_derivative_upper + mp.mpf("1e-80")
        w_center = complex(w_value)
        critical_w_centers.append(w_center)
        critical_w_radii.append(float(w_radius))
        critical_points.append(
            {
                "root_id": f"selected_{point_index:03d}",
                "a": encoded_acb(root),
                "b": encoded_acb(b_value),
                "canonical_uniformizing_lift": {
                    "real": format(w_center.real, ".17g"),
                    "imaginary": format(w_center.imag, ".17g"),
                    "radius_upper": format(float(w_radius), ".17g"),
                },
                "Q43_A_value_absolute_lower": format(q_lower, ".17g"),
                "b_absolute_lower": format(b_lower, ".17g"),
                "norm_derivative_absolute_lower": format(
                    derivative_lower, ".17g"
                ),
                "opposite_sheet_factor_absolute_lower": format(
                    opposite_lower, ".17g"
                ),
                "elliptic_relation": encoded_acb(elliptic_relation),
                "dual_discriminant_value": encoded_acb(discriminant_value),
            }
        )

    minimum_torus_separation = math.inf
    shifts = [complex(real, imaginary) for real in (-1, 0, 1) for imaginary in (-1, 0, 1)]
    for first, left_center in enumerate(critical_w_centers):
        for second in range(first):
            right_center = critical_w_centers[second]
            distance = min(abs(left_center - right_center + shift) for shift in shifts)
            lower_distance = distance - critical_w_radii[first] - critical_w_radii[second]
            minimum_torus_separation = min(minimum_torus_separation, lower_distance)
    if minimum_torus_separation <= 0:
        raise AssertionError("selected critical-value balls overlap on E_i")

    # The y-line chart used by the fibration seed degenerates exactly at
    # L1=A[1,:]*(a,b,1)=0. Isolate its three zeros so every later path can
    # certify that it remains inside this chart.
    chart_a = alignment[1, 0]
    chart_b = alignment[1, 1]
    chart_constant = alignment[1, 2]
    if lower(abs(chart_b)) <= 0:
        raise AssertionError("selected y-chart coefficient of b contains zero")
    chart_norm = {
        0: chart_constant**2,
        1: acb(2) * chart_a * chart_constant + chart_b**2,
        2: chart_a**2,
        3: -(chart_b**2),
    }
    chart_roots = acb_poly(
        [chart_norm[index] for index in range(4)]
    ).roots(tol=1.0e-50, maxprec=2048)
    if len(chart_roots) != 3 or not all(root.is_finite() for root in chart_roots):
        raise AssertionError("selected y-chart zero isolation failed")
    chart_zero_rows = []
    chart_w_centers: list[complex] = []
    chart_w_radii: list[float] = []
    for chart_index, root in enumerate(
        sorted(chart_roots, key=lambda value: (midpoint(value).real, midpoint(value).imag)),
        start=1,
    ):
        b_value = -(chart_a * root + chart_constant) / chart_b
        chart_value = chart_a * root + chart_b * b_value + chart_constant
        elliptic_relation = b_value**2 - root**3 + root
        if not chart_value.contains(0) or not elliptic_relation.contains(0):
            raise AssertionError("selected line-chart zero lift is inconsistent")
        a_center_complex = midpoint(root)
        b_center_complex = midpoint(b_value)
        a_center = mp.mpc(a_center_complex.real, a_center_complex.imag)
        b_center = mp.mpc(b_center_complex.real, b_center_complex.imag)
        inverse_argument = mp.asin(mp.sqrt(2 / (a_center + 1)))
        z_value = mp.ellipf(inverse_argument, elliptic_parameter) / mp.sqrt(2)
        _, inverse_b = elliptic_ab(z_value)
        if abs(inverse_b - b_center) > abs(-inverse_b - b_center):
            z_value = -z_value
        w_value = z_value / period_length
        w_value -= mp.nint(mp.re(w_value)) + 1j * mp.nint(mp.im(w_value))
        a_radius = mp.mpf(str(radius_upper(root)))
        cubic_center = a_center**3 - a_center
        cubic_variation = a_radius * (3 * (abs(a_center) + a_radius) ** 2 + 1)
        cubic_lower = abs(cubic_center) - cubic_variation
        if cubic_lower <= 0:
            raise AssertionError("line-chart zero inverse meets an elliptic branch")
        w_radius = a_radius / (
            2 * period_length * mp.sqrt(cubic_lower)
        ) + mp.mpf("1e-80")
        w_center = complex(w_value)
        chart_w_centers.append(w_center)
        chart_w_radii.append(float(w_radius))
        chart_zero_rows.append(
            {
                "chart_zero_id": f"L1_zero_{chart_index}",
                "a": encoded_acb(root),
                "b": encoded_acb(b_value),
                "canonical_uniformizing_lift": {
                    "real": format(w_center.real, ".17g"),
                    "imaginary": format(w_center.imag, ".17g"),
                    "radius_upper": format(float(w_radius), ".17g"),
                },
                "L1_value": encoded_acb(chart_value),
                "elliptic_relation": encoded_acb(elliptic_relation),
            }
        )

    minimum_chart_zero_to_critical = math.inf
    for chart_center, chart_radius in zip(chart_w_centers, chart_w_radii):
        for critical_center, critical_radius in zip(
            critical_w_centers, critical_w_radii
        ):
            distance = min(
                abs(chart_center - critical_center + shift) for shift in shifts
            )
            minimum_chart_zero_to_critical = min(
                minimum_chart_zero_to_critical,
                distance - chart_radius - critical_radius,
            )
    if minimum_chart_zero_to_critical <= 0:
        raise AssertionError("a critical value lies on the selected y-chart wall")

    packet = {
        "schema": "MTTQ79SelectedAlignmentDualDiscriminantInterval.v1",
        "status": "SELECTED_ALIGNMENT_90_SIMPLE_NODAL_CRITICAL_VALUES_INTERVAL_CERTIFIED",
        "dual_discriminant": {
            "construction": (
                "Disc_t F(L1,-L0-L2*t,L1*t)=L1^30*D30(L0,L1,L2)"
            ),
            "homogeneous_degree": dual.total_degree(),
            "term_count": len(dual.terms()),
            "integer_coefficient_rows": [
                {
                    "powers_L0_L1_L2": list(powers),
                    "coefficient": int(coefficient),
                }
                for powers, coefficient in dual.terms()
            ],
            "identity_pullback_exactly_reproduces_A111_P45_Q43": True,
        },
        "selected_alignment_pullback": {
            "formula": "D30(A*[a,b,1])=P45_A(a)+b*Q43_A(a)",
            "P_degree": p_degree,
            "Q_degree": q_degree,
            "P_coefficients_ascending": encode_poly(p_selected, 45),
            "Q_coefficients_ascending": encode_poly(q_selected, 43),
            "coefficient_balls_from_selected_alignment": True,
        },
        "norm90": {
            "formula": "N90_A=P45_A^2-(a^3-a)*Q43_A^2",
            "degree": norm_degree,
            "coefficients_ascending": encode_poly(norm, 90),
            "leading_coefficient_absolute_lower": format(
                lower(abs(norm[90])), ".17g"
            ),
            "isolated_root_count": len(roots),
            "minimum_pairwise_root_ball_separation_lower": format(
                minimum_root_separation, ".17g"
            ),
            "roots": [encoded_acb(root) for root in roots],
        },
        "critical_points_on_E": {
            "count": len(critical_points),
            "lift_formula": "b=-P45_A(a)/Q43_A(a)",
            "minimum_Q43_A_value_absolute_lower": format(
                minimum_q_value_lower, ".17g"
            ),
            "minimum_b_value_absolute_lower": format(
                minimum_b_value_lower, ".17g"
            ),
            "minimum_norm_derivative_absolute_lower": format(
                minimum_norm_derivative_lower, ".17g"
            ),
            "minimum_opposite_sheet_factor_absolute_lower": format(
                minimum_opposite_sheet_factor_lower, ".17g"
            ),
            "maximum_elliptic_relation_radius_upper": format(
                maximum_elliptic_relation_radius, ".17g"
            ),
            "maximum_dual_discriminant_value_radius_upper": format(
                maximum_discriminant_value_radius, ".17g"
            ),
            "uniformization": (
                "a=-1+2/sn(sqrt(2)*L*w|1/2)^2 with the b-selected inverse"
            ),
            "minimum_pairwise_torus_ball_separation_lower": format(
                minimum_torus_separation, ".17g"
            ),
            "points": critical_points,
        },
        "selected_y_line_chart_zeros": {
            "equation": "L1=A[1,0]*a+A[1,1]*b+A[1,2]=0",
            "count": len(chart_zero_rows),
            "minimum_torus_distance_to_critical_balls_lower": format(
                minimum_chart_zero_to_critical, ".17g"
            ),
            "points": chart_zero_rows,
        },
        "strict_scope": {
            "selected_alignment_interval_used": True,
            "projective_chart_artifact_L1_power_removed_exactly": True,
            "identity_A111_crosscheck_exact": True,
            "ninety_selected_alignment_critical_a_values_isolated": True,
            "critical_b_lifts_emitted": True,
            "ninety_simple_discriminant_zeros_certified": True,
            "nodal_fiber_count": 90,
            "nodal_fiber_tubes_certified": False,
            "endpoint_period_rows_emitted": 0,
            "observed_SM_values_used": False,
        },
    }
    dump(OUT, packet)
    print(f"wrote {OUT.relative_to(ROOT)}")
    print(
        "selected dual discriminant: "
        f"D terms={len(dual.terms())}, P/Q degrees={p_degree}/{q_degree}, "
        f"N roots={len(roots)}, separation>={minimum_root_separation:.3e}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
