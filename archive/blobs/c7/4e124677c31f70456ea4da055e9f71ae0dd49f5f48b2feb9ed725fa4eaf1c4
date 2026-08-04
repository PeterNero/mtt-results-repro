from __future__ import annotations

import json
import math
from pathlib import Path

from flint import acb, ctx

from build_q79_selected_alignment_fibration_seed import (
    Poly,
    encode_poly,
    line_polynomials,
    poly_add,
    poly_multiply,
    poly_power,
    poly_scale,
    polynomial_inventory,
    t_convolution,
    t_subtract,
)
from certify_q79_selected_side_beta_defect_transport import (
    SelectedQ79IntervalSystem,
    encoded_acb,
    encoded_matrix,
    lower,
    radius_upper,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_zchart_genus2_fibration_seed.interval.packet.json"
)


def aligned_chart_z_coefficients(
    table: list[dict], line: list[Poly]
) -> list[Poly]:
    degree = sum(int(value) for value in table[0]["powers_xyz"])
    coefficients: list[Poly] = [{} for _ in range(degree + 1)]
    for row in table:
        x_power, y_power, z_power = [
            int(value) for value in row["powers_xyz"]
        ]
        source_coefficient = int(row["coefficient"])
        for index in range(z_power + 1):
            contribution = poly_multiply(
                poly_multiply(
                    poly_power(line[2], x_power + y_power),
                    poly_power(line[0], z_power - index),
                ),
                poly_power(line[1], index),
            )
            scalar = (
                source_coefficient
                * (-1) ** z_power
                * math.comb(z_power, index)
            )
            target = y_power + index
            coefficients[target] = poly_add(
                coefficients[target], poly_scale(contribution, scalar)
            )
    return coefficients


def main() -> int:
    ctx.dps = 100
    system = SelectedQ79IntervalSystem(dps=100)
    alignment = system.alignment
    determinant = alignment.det()
    if lower(abs(determinant)) <= 0:
        raise AssertionError("selected alignment determinant contains zero")
    line = line_polynomials(alignment)
    tables = system.evaluator.tables
    f6 = aligned_chart_z_coefficients(tables["F6"], line)
    g3 = aligned_chart_z_coefficients(tables["G3"], line)
    q2 = aligned_chart_z_coefficients(tables["Q2"], line)
    h4 = aligned_chart_z_coefficients(tables["H4"], line)
    if [len(f6), len(g3), len(q2), len(h4)] != [7, 4, 3, 5]:
        raise AssertionError("selected z-chart fiber degrees changed")
    residual = t_subtract(
        f6, t_convolution(g3, g3), t_convolution(q2, h4)
    )
    residual_values = [value for row in residual for value in row.values()]
    if not residual_values or not all(
        value.contains(0) for value in residual_values
    ):
        raise AssertionError("z-chart interval splitting identity failed")
    payload = {
        "schema": "MTTQ79SelectedAlignmentGenusTwoZChartFibrationSeedInterval.v1",
        "status": "SELECTED_ALIGNMENT_Z_LINE_CHART_INTERVAL_FIBRATION_SEED_EMITTED",
        "source": {
            "alignment_constructor": "SelectedQ79IntervalSystem: A0*exp(lambda_selected*T)",
            "carrier_side": "A125/A126 selected side before the transverse wall",
            "line": "L=A*[a,b,1]^T and L0*x+L1*y+L2*z=0",
            "line_chart": "z",
            "fiber_chart": "x=1, t=y/x, z=-(L0+L1*t)/L2; homogeneous L2^degree scaling retained",
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
                max(radius_upper(value) for value in residual_values), ".17g"
            ),
        },
        "projective_covariance": {
            "source_theorem": "A123 Q79ProjectiveLineChartCovarianceTheorem",
            "transition_from_y": "t_z=-(L0+L2*t_y)/L1",
            "hyperelliptic_scaling": "U_z=(L2/L1)^3*U_y",
            "residue_form_transition_residual_zero": True,
        },
        "strict_scope": {
            "selected_alignment_interval_used": True,
            "observed_SM_values_used": False,
            "z_chart_period_rows_emitted": 0,
        },
    }
    OUTPUT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
