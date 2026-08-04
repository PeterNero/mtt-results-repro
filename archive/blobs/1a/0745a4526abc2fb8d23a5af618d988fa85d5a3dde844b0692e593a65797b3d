from __future__ import annotations

import json
import math
from pathlib import Path

from flint import acb, ctx

from certify_q79_selected_side_beta_defect_transport import (
    SelectedQ79IntervalSystem,
    encoded_acb,
    encoded_matrix,
    lower,
    radius_upper,
)


ROOT = Path(__file__).resolve().parents[1]
OUT = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_genus2_fibration_seed.interval.packet.json"
)

Poly = dict[tuple[int, int], acb]


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def poly_add(left: Poly, right: Poly) -> Poly:
    result = {key: value for key, value in left.items()}
    for key, value in right.items():
        result[key] = result.get(key, acb(0)) + value
    return {key: value for key, value in result.items() if not value.is_zero()}


def poly_scale(value: Poly, scalar: acb | int) -> Poly:
    return {key: coefficient * scalar for key, coefficient in value.items()}


def poly_multiply(left: Poly, right: Poly) -> Poly:
    result: Poly = {}
    for (a_left, b_left), left_value in left.items():
        for (a_right, b_right), right_value in right.items():
            key = (a_left + a_right, b_left + b_right)
            result[key] = result.get(key, acb(0)) + left_value * right_value
    return {key: value for key, value in result.items() if not value.is_zero()}


def poly_power(value: Poly, power: int) -> Poly:
    result: Poly = {(0, 0): acb(1)}
    factor = value
    exponent = power
    while exponent:
        if exponent & 1:
            result = poly_multiply(result, factor)
        exponent >>= 1
        if exponent:
            factor = poly_multiply(factor, factor)
    return result


def line_polynomials(alignment) -> list[Poly]:
    return [
        {
            (1, 0): alignment[row, 0],
            (0, 1): alignment[row, 1],
            (0, 0): alignment[row, 2],
        }
        for row in range(3)
    ]


def aligned_chart_y_coefficients(table: list[dict], line: list[Poly]) -> list[Poly]:
    degree = sum(int(value) for value in table[0]["powers_xyz"])
    coefficients: list[Poly] = [{} for _ in range(degree + 1)]
    for row in table:
        x_power, y_power, z_power = [int(value) for value in row["powers_xyz"]]
        source_coefficient = int(row["coefficient"])
        for index in range(y_power + 1):
            contribution = poly_multiply(
                poly_multiply(
                    poly_power(line[0], y_power - index),
                    poly_power(line[1], x_power + z_power),
                ),
                poly_power(line[2], index),
            )
            scalar = (
                source_coefficient
                * (-1) ** y_power
                * math.comb(y_power, index)
            )
            target = index + z_power
            coefficients[target] = poly_add(
                coefficients[target], poly_scale(contribution, scalar)
            )
    return coefficients


def t_convolution(left: list[Poly], right: list[Poly]) -> list[Poly]:
    result: list[Poly] = [{} for _ in range(len(left) + len(right) - 1)]
    for left_power, left_value in enumerate(left):
        for right_power, right_value in enumerate(right):
            target = left_power + right_power
            result[target] = poly_add(
                result[target], poly_multiply(left_value, right_value)
            )
    return result


def t_subtract(left: list[Poly], *rights: list[Poly]) -> list[Poly]:
    length = max([len(left), *[len(value) for value in rights]])
    result = [dict(left[index]) if index < len(left) else {} for index in range(length)]
    for right in rights:
        for index, value in enumerate(right):
            result[index] = poly_add(result[index], poly_scale(value, -1))
    return result


def encode_poly(value: Poly) -> list[dict]:
    return [
        {
            "a_power": a_power,
            "b_power": b_power,
            "coefficient": encoded_acb(coefficient),
            "coefficient_radius_upper": format(
                radius_upper(coefficient), ".17g"
            ),
        }
        for (a_power, b_power), coefficient in sorted(
            value.items(), reverse=True
        )
    ]


def polynomial_inventory(coefficients: list[Poly]) -> dict:
    all_values = [value for row in coefficients for value in row.values()]
    return {
        "t_degree": len(coefficients) - 1,
        "ascending_t_coefficient_term_counts": [
            len(value) for value in coefficients
        ],
        "maximum_a_degree": max(
            (key[0] for row in coefficients for key in row), default=0
        ),
        "maximum_b_degree": max(
            (key[1] for row in coefficients for key in row), default=0
        ),
        "maximum_coefficient_radius_upper": format(
            max((radius_upper(value) for value in all_values), default=0.0),
            ".17g",
        ),
    }


def main() -> int:
    ctx.dps = 100
    system = SelectedQ79IntervalSystem(dps=100)
    alignment = system.alignment
    determinant = alignment.det()
    if lower(abs(determinant)) <= 0:
        raise AssertionError("selected alignment determinant contains zero")

    line = line_polynomials(alignment)
    tables = system.evaluator.tables
    f6 = aligned_chart_y_coefficients(tables["F6"], line)
    g3 = aligned_chart_y_coefficients(tables["G3"], line)
    q2 = aligned_chart_y_coefficients(tables["Q2"], line)
    h4 = aligned_chart_y_coefficients(tables["H4"], line)
    if [len(f6), len(g3), len(q2), len(h4)] != [7, 4, 3, 5]:
        raise AssertionError("selected-alignment fiber degrees changed")

    residual = t_subtract(f6, t_convolution(g3, g3), t_convolution(q2, h4))
    residual_values = [value for row in residual for value in row.values()]
    if not residual_values or not all(value.contains(0) for value in residual_values):
        raise AssertionError("interval splitting identity does not contain zero")
    maximum_residual_radius = max(radius_upper(value) for value in residual_values)

    packet = {
        "schema": "MTTQ79SelectedAlignmentGenusTwoFibrationSeedInterval.v1",
        "status": "SELECTED_SIDE_ALIGNMENT_INTERVAL_FIBRATION_SEED_EMITTED",
        "source": {
            "alignment_constructor": (
                "SelectedQ79IntervalSystem: A0*exp(lambda_selected*T)"
            ),
            "carrier_side": "A125/A126 selected side before the transverse wall",
            "line": "L=A*[a,b,1]^T and L0*x+L1*y+L2*z=0",
            "fiber_chart": (
                "x=1, t=z/x, y=-(L0+L2*t)/L1; homogeneous "
                "L1^degree scaling retained"
            ),
            "alignment_interval": encoded_matrix(alignment),
            "alignment_determinant": encoded_acb(determinant),
            "alignment_determinant_absolute_lower": format(
                lower(abs(determinant)), ".17g"
            ),
        },
        "fiber_polynomials": {
            "coefficient_order": "ascending powers of t",
            "coefficient_encoding": "sparse ACB polynomial in a,b",
            "F6": [encode_poly(value) for value in f6],
            "G3": [encode_poly(value) for value in g3],
            "Q2": [encode_poly(value) for value in q2],
            "H4": [encode_poly(value) for value in h4],
            "inventory": {
                "F6": polynomial_inventory(f6),
                "G3": polynomial_inventory(g3),
                "Q2": polynomial_inventory(q2),
                "H4": polynomial_inventory(h4),
            },
        },
        "splitting_identity": {
            "formula": "F6=G3^2+Q2*H4",
            "coefficient_balls_checked": len(residual_values),
            "every_residual_coefficient_contains_zero": True,
            "maximum_residual_coefficient_radius_upper": format(
                maximum_residual_radius, ".17g"
            ),
        },
        "basis_invariance": {
            "statement": (
                "For any independently certified integral endpoint basis "
                "B'=B*U with U in GL(92,Z), image(Pi_B')=image(Pi_B). "
                "Therefore endpoint membership may be computed directly at "
                "this alignment; transporting A119's identity basis is not "
                "logically required."
            ),
            "same_residue_row_basis_required": True,
            "complete_integral_endpoint_basis_required": True,
        },
        "strict_scope": {
            "selected_alignment_interval_used": True,
            "observed_SM_values_used": False,
            "critical_values_isolated": False,
            "endpoint_integral_H2_basis_emitted": False,
            "endpoint_period_rows_emitted": 0,
            "integral_branch_selected": False,
        },
    }
    dump(OUT, packet)
    print(f"wrote {OUT.relative_to(ROOT)}")
    print(
        "selected-alignment interval fibration seed: "
        f"det lower={lower(abs(determinant)):.6e}, "
        f"splitting balls={len(residual_values)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
