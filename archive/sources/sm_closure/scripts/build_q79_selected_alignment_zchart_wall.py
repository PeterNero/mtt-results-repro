from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import mpmath as mp
from flint import acb, acb_poly, ctx

from certify_q79_selected_side_beta_defect_transport import (
    SelectedQ79IntervalSystem,
    encoded_acb,
    lower,
    midpoint,
    radius_upper,
)


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
DUAL = DIRECTORY / "selected_alignment_dual_discriminant.interval.packet.json"
Z_FIBRATION = DIRECTORY / "selected_alignment_zchart_genus2_fibration_seed.interval.packet.json"
A123 = (
    ROOT
    / "candidate_data"
    / "selected_q79projectivelinechartcovarianceandellzerocontinuation"
    / "projective_line_chart_covariance_theorem.packet.json"
)
OUTPUT = DIRECTORY / "selected_alignment_zchart_wall.interval.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def torus_distance(left: complex, right: complex) -> float:
    return min(
        abs(left - right + complex(horizontal, vertical))
        for horizontal in (-1, 0, 1)
        for vertical in (-1, 0, 1)
    )


def main() -> int:
    ctx.dps = 100
    mp.mp.dps = 100
    dual = load(DUAL)
    z_fibration = load(Z_FIBRATION)
    a123 = load(A123)
    if not a123["theorem"]["proved"]:
        raise AssertionError("A123 projective covariance theorem is unavailable")
    if z_fibration["source"]["line_chart"] != "z":
        raise AssertionError("selected z-chart fibration source changed")

    system = SelectedQ79IntervalSystem(dps=100, line_chart="z")
    alignment = system.alignment
    chart_a = alignment[2, 0]
    chart_b = alignment[2, 1]
    chart_constant = alignment[2, 2]
    if lower(abs(chart_b)) <= 0:
        raise AssertionError("selected z-chart coefficient of b contains zero")
    chart_norm = [
        chart_constant**2,
        acb(2) * chart_a * chart_constant + chart_b**2,
        chart_a**2,
        -(chart_b**2),
    ]
    roots = acb_poly(chart_norm).roots(tol=1.0e-50, maxprec=2048)
    if len(roots) != 3 or not all(root.is_finite() for root in roots):
        raise AssertionError("selected z-chart zero isolation failed")

    elliptic_parameter = mp.mpf("0.5")
    period_length = mp.sqrt(2) * mp.ellipk(elliptic_parameter)
    sn = mp.ellipfun("sn")
    cn = mp.ellipfun("cn")
    dn = mp.ellipfun("dn")

    def elliptic_ab(z_value: mp.mpc) -> tuple[mp.mpc, mp.mpc]:
        argument = mp.sqrt(2) * z_value
        sn_value = sn(argument, elliptic_parameter)
        return (
            -1 + 2 / sn_value**2,
            -2
            * mp.sqrt(2)
            * cn(argument, elliptic_parameter)
            * dn(argument, elliptic_parameter)
            / sn_value**3,
        )

    rows = []
    centers: list[complex] = []
    radii: list[float] = []
    for index, root in enumerate(
        sorted(roots, key=lambda value: (midpoint(value).real, midpoint(value).imag)),
        start=1,
    ):
        b_value = -(chart_a * root + chart_constant) / chart_b
        chart_value = chart_a * root + chart_b * b_value + chart_constant
        elliptic_relation = b_value**2 - root**3 + root
        if not chart_value.contains(0) or not elliptic_relation.contains(0):
            raise AssertionError("selected z-chart zero lift is inconsistent")

        a_midpoint = midpoint(root)
        b_midpoint = midpoint(b_value)
        a_center = mp.mpc(a_midpoint.real, a_midpoint.imag)
        b_center = mp.mpc(b_midpoint.real, b_midpoint.imag)
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
            raise AssertionError("z-chart zero inverse meets an elliptic branch")
        w_radius = a_radius / (2 * period_length * mp.sqrt(cubic_lower)) + mp.mpf(
            "1e-80"
        )
        center = complex(w_value)
        radius = float(w_radius)
        centers.append(center)
        radii.append(radius)
        rows.append(
            {
                "chart_zero_id": f"L2_zero_{index}",
                "a": encoded_acb(root),
                "b": encoded_acb(b_value),
                "canonical_uniformizing_lift": {
                    "real": format(center.real, ".17g"),
                    "imaginary": format(center.imag, ".17g"),
                    "radius_upper": format(radius, ".17g"),
                },
                "L2_value": encoded_acb(chart_value),
                "elliptic_relation": encoded_acb(elliptic_relation),
            }
        )

    pairwise = min(
        torus_distance(centers[left], centers[right]) - radii[left] - radii[right]
        for left in range(3)
        for right in range(left)
    )
    critical_rows = dual["critical_points_on_E"]["points"]
    critical_clearance = math.inf
    for center, radius in zip(centers, radii):
        for critical in critical_rows:
            lift = critical["canonical_uniformizing_lift"]
            critical_center = complex(float(lift["real"]), float(lift["imaginary"]))
            critical_radius = float(lift["radius_upper"])
            critical_clearance = min(
                critical_clearance,
                torus_distance(center, critical_center) - radius - critical_radius,
            )
    if pairwise <= 0 or critical_clearance <= 0:
        raise AssertionError("selected z-chart wall balls are not separated")

    payload = {
        "schema": "MTTQ79SelectedAlignmentZChartWallInterval.v1",
        "status": "SELECTED_ALIGNMENT_Z_CHART_WALL_INTERVAL_CERTIFIED",
        "authority": [
            {"path": relative(path), "sha256": sha256(path)}
            for path in (DUAL, Z_FIBRATION, A123, Path(__file__))
        ],
        "selected_z_line_chart_zeros": {
            "equation": "L2=A[2,0]*a+A[2,1]*b+A[2,2]=0",
            "count": len(rows),
            "minimum_pairwise_torus_ball_separation_lower": format(pairwise, ".17g"),
            "minimum_torus_distance_to_critical_balls_lower": format(
                critical_clearance, ".17g"
            ),
            "points": rows,
        },
        "projective_covariance": {
            "source_theorem": "A123 Q79ProjectiveLineChartCovarianceTheorem",
            "native_z_fibration_seed_consumed": True,
            "z_chart_regular_domain": "L2 != 0",
        },
        "scope": {
            "selected_alignment_interval_used": True,
            "three_z_chart_wall_points_isolated": True,
            "z_chart_walls_separated_from_all_ninety_nodal_values": True,
            "period_values_used": False,
            "observed_SM_values_used": False,
        },
    }
    OUTPUT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"wrote {relative(OUTPUT)}")
    print(
        "selected z-chart wall: "
        f"zeros=3, pairwise>{pairwise:.3e}, critical-clearance>{critical_clearance:.3e}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
