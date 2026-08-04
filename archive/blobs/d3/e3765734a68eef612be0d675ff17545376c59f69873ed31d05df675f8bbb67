from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp
from flint import acb, acb_series, arb, ctx


ROOT = Path(__file__).resolve().parents[1]
FIBRATION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2lefschetzperiodreduction"
    / "explicit_genus2_fibration.packet.json"
)
LOCAL_DATA = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2localroottrajectoryexecution"
)
DISTINGUISHED_DATA = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2distinguishedmeridianexecution"
)
FALLBACK_ROOT_IDS = {"a34", "a41"}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def upper(value: arb) -> float:
    return math.nextafter(float(value.upper()), math.inf)


def lower(value: arb) -> float:
    return math.nextafter(float(value.lower()), -math.inf)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root-id", required=True)
    parser.add_argument("--distinguished-index", type=int, default=None)
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--limit", type=int, default=None)
    args = parser.parse_args()
    distinguished = args.distinguished_index is not None
    data_dir = DISTINGUISHED_DATA if distinguished else LOCAL_DATA
    stem = (
        f"d{args.distinguished_index:03d}_{args.root_id}"
        if distinguished
        else args.root_id
    )
    packet_path = data_dir / f"{stem}.trajectory.packet.json"
    trajectory_packet = load(packet_path)
    trajectory_path = ROOT / trajectory_packet["trajectory"]["path"]
    if sha256(trajectory_path) != trajectory_packet["trajectory"]["sha256"]:
        raise AssertionError("local trajectory hash mismatch")
    if distinguished and trajectory_packet.get("distinguished_index") != args.distinguished_index:
        raise AssertionError("distinguished trajectory index mismatch")
    if not distinguished and not trajectory_packet["homology"]["matches_A113_candidate_matrix"]:
        raise AssertionError("local trajectory does not match A113")

    ctx.dps = 55
    fibration = load(FIBRATION)
    a, b, t, s = sp.symbols("a b t s")
    t_coefficients = [
        sp.sympify(value)
        for value in fibration["fiber_chart"]["f_coefficients_t_descending"]
    ]
    f_ab = sum(
        coefficient * t ** (6 - index)
        for index, coefficient in enumerate(t_coefficients)
    )
    if distinguished:
        chart = trajectory_packet["branch_chart"]["coordinate"]
        if chart == "s_0=1/t":
            omitted = 0
        elif chart == "s_minus1=1/(t+1)":
            omitted = -1
        else:
            raise AssertionError(f"unsupported distinguished branch chart: {chart}")
    else:
        omitted = -1 if args.root_id in FALLBACK_ROOT_IDS else 0
    transformed_raw = sp.Poly(
        sp.expand(s**6 * f_ab.subs(t, omitted + 1 / s)), s
    ).all_coeffs()
    transformed = [
        sp.expand(sp.rem(expression, b**2 - a**3 + a, b))
        for expression in transformed_raw
    ]

    def expression_terms(expression: sp.Expr) -> list[tuple[int, int, str, str]]:
        rows: list[tuple[int, int, str, str]] = []
        for (a_power, b_power), coefficient in sp.Poly(
            expression, a, b, domain=sp.QQ_I
        ).terms():
            rows.append(
                (
                    a_power,
                    b_power,
                    str(sp.re(coefficient)),
                    str(sp.im(coefficient)),
                )
            )
        return rows

    elliptic_relation = b**2 - a**3 + a

    def elliptic_flow(expression: sp.Expr) -> sp.Expr:
        derivative = 2 * b * sp.diff(expression, a) + (3 * a**2 - 1) * sp.diff(
            expression, b
        )
        return sp.expand(sp.rem(derivative, elliptic_relation, b))

    taylor_order = 4
    flow_expressions = [transformed]
    for _ in range(taylor_order):
        flow_expressions.append(
            [elliptic_flow(expression) for expression in flow_expressions[-1]]
        )
    coefficient_flow_terms = [
        [expression_terms(expression) for expression in derivative_order]
        for derivative_order in flow_expressions
    ]

    tau = acb(0, 1)
    period_length = acb("0.5").elliptic_k() * acb(2).sqrt()
    period_square = period_length**2
    period_cube = period_length**3

    def coefficient_at(
        terms: list[tuple[int, int, str, str]], a_value: acb, b_value: acb
    ) -> acb:
        value = acb(0)
        for a_power, b_power, real, imaginary in terms:
            value += acb(real, imaginary) * a_value**a_power * b_value**b_power
        return value

    def coefficient_taylor_data_over_segment(
        w0: complex, w1: complex
    ) -> tuple[list[list[acb]], float]:
        midpoint = (w0 + w1) / 2
        w_box = acb(
            arb(
                format(midpoint.real, ".17g"),
                format(abs(w1.real - w0.real) / 2 + 3e-16, ".17g"),
            ),
            arb(
                format(midpoint.imag, ".17g"),
                format(abs(w1.imag - w0.imag) / 2 + 3e-16, ".17g"),
            ),
        )
        box_series = acb_series([w_box, acb(1)], 2).elliptic_p(tau)
        a_box = box_series[0] / period_square
        b_box = box_series[1] / (2 * period_cube)

        w_midpoint = acb(
            format(midpoint.real, ".17g"), format(midpoint.imag, ".17g")
        )
        midpoint_series = acb_series([w_midpoint, acb(1)], 2).elliptic_p(tau)
        a_midpoint = midpoint_series[0] / period_square
        b_midpoint = midpoint_series[1] / (2 * period_cube)
        half_length = abs(w1 - w0) / 2 + 4e-16

        derivative_rows: list[list[acb]] = []
        for derivative_order, terms_row in enumerate(coefficient_flow_terms):
            use_box = derivative_order == taylor_order
            a_value = a_box if use_box else a_midpoint
            b_value = b_box if use_box else b_midpoint
            derivative_rows.append(
                [
                    period_length**derivative_order
                    * coefficient_at(terms, a_value, b_value)
                    for terms in terms_row
                ]
            )
        return derivative_rows, half_length

    def translated_coefficients(
        taylor_data: tuple[list[list[acb]], float], center: complex
    ) -> list[acb]:
        derivative_rows_descending, half_length = taylor_data
        derivative_rows = [list(reversed(row)) for row in derivative_rows_descending]
        c = acb(format(center.real, ".17g"), format(center.imag, ".17g"))
        translated: list[acb] = []
        for k in range(7):
            translated_derivatives: list[acb] = []
            for derivative_row in derivative_rows:
                value = acb(0)
                for j in range(k, 7):
                    value += derivative_row[j] * math.comb(j, k) * c ** (j - k)
                translated_derivatives.append(value)
            half_length_ball = arb(format(half_length, ".17g"))
            variation_ball = sum(
                abs(translated_derivatives[order])
                * half_length_ball**order
                / math.factorial(order)
                for order in range(1, taylor_order + 1)
            )
            variation = upper(variation_ball)
            translated.append(
                translated_derivatives[0]
                + acb(arb(0, variation), arb(0, variation))
            )
        return translated

    def rouche_margin(translated: list[acb], radius: float) -> tuple[bool, float]:
        radius_ball = arb(format(radius, ".17g"))
        linear = abs(translated[1]) * radius_ball
        remainder = abs(translated[0])
        for power in range(2, 7):
            remainder += abs(translated[power]) * radius_ball**power
        margin_lower = linear.lower() - remainder.upper()
        accepted = bool(margin_lower > 0)
        linear_lower = linear.lower()
        if linear_lower <= 0:
            return False, -math.inf
        denominator = linear.upper() if accepted else linear_lower
        return accepted, lower(margin_lower / denominator)

    def certify_subdivision(
        w0: complex,
        w1: complex,
        center: complex,
        radius: float,
        translated: list[acb],
        depth: int = 0,
    ) -> tuple[float, int, int] | None:
        accepted, relative = rouche_margin(translated, radius)
        if accepted:
            return relative, depth, 1
        if depth >= 8:
            return None
        midpoint = (w0 + w1) / 2
        left = certify_subdivision(
            w0,
            midpoint,
            center,
            radius,
            translated_coefficients(
                coefficient_taylor_data_over_segment(w0, midpoint), center
            ),
            depth + 1,
        )
        if left is None:
            return None
        right = certify_subdivision(
            midpoint,
            w1,
            center,
            radius,
            translated_coefficients(
                coefficient_taylor_data_over_segment(midpoint, w1), center
            ),
            depth + 1,
        )
        if right is None:
            return None
        return min(left[0], right[0]), max(left[1], right[1]), left[2] + right[2]

    with np.load(trajectory_path) as data:
        w = data["w"]
        roots = data["roots"]
        point_radii = data["root_radius_uppers"]

    available = len(w) - 1
    segment_start = args.start
    segment_stop = available if args.limit is None else min(available, args.start + args.limit)
    if not 0 <= segment_start < segment_stop <= available:
        raise AssertionError("invalid local tube segment range")

    factors = (1.2, 1.5, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128)
    minimum_relative_margin = math.inf
    minimum_tube_separation = math.inf
    maximum_subdivision_depth = 0
    segments_requiring_subdivision = 0
    additional_root_subintervals = 0
    for completed, segment_index in enumerate(range(segment_start, segment_stop), 1):
        w0 = complex(w[segment_index])
        w1 = complex(w[segment_index + 1])
        taylor_data = coefficient_taylor_data_over_segment(w0, w1)
        centers = (roots[segment_index] + roots[segment_index + 1]) / 2
        tube_radii: list[float] = []
        segment_margin = math.inf
        segment_depth = 0
        for root_index in range(6):
            center = complex(centers[root_index])
            endpoint_radius = max(
                abs(roots[segment_index, root_index] - center)
                + point_radii[segment_index, root_index]
                + 4e-15 * (1 + abs(roots[segment_index, root_index]) + abs(center)),
                abs(roots[segment_index + 1, root_index] - center)
                + point_radii[segment_index + 1, root_index]
                + 4e-15 * (1 + abs(roots[segment_index + 1, root_index]) + abs(center)),
            )
            endpoint_radius = math.nextafter(float(endpoint_radius), math.inf)
            nearest_center = min(
                abs(center - centers[other])
                for other in range(6)
                if other != root_index
            )
            nearest_lower = nearest_center - 8e-15 * (
                1 + abs(center) + max(abs(value) for value in centers)
            )
            maximum_radius = 0.44 * nearest_lower
            translated = translated_coefficients(taylor_data, center)
            candidates: list[tuple[float, float]] = []
            accepted_radius = None
            accepted_relative = None
            accepted_certificate: tuple[float, int, int] | None = None
            for factor in factors:
                radius = max(
                    math.nextafter(endpoint_radius * factor, math.inf), 1e-30
                )
                if radius >= maximum_radius:
                    break
                candidates.append((factor, radius))
                accepted, relative = rouche_margin(translated, radius)
                if accepted:
                    accepted_radius = radius
                    accepted_relative = relative
                    accepted_certificate = (relative, 0, 1)
                    break
            if accepted_radius is None:
                for _, radius in sorted(
                    candidates, key=lambda row: abs(math.log(row[0] / 6))
                ):
                    certificate = certify_subdivision(
                        w0, w1, center, radius, translated
                    )
                    if certificate is not None:
                        accepted_radius = radius
                        accepted_relative = certificate[0]
                        accepted_certificate = certificate
                        break
            if (
                accepted_radius is None
                or accepted_relative is None
                or accepted_certificate is None
            ):
                raise AssertionError(
                    f"local Rouche tube failed: path={stem} "
                    f"segment={segment_index} strand={root_index} "
                    f"endpoint_radius={endpoint_radius:.6g} max={maximum_radius:.6g} "
                    f"q0_upper={upper(abs(translated[0])):.6g} "
                    f"q1_lower={lower(abs(translated[1])):.6g}"
                )
            tube_radii.append(accepted_radius)
            segment_margin = min(segment_margin, accepted_relative)
            segment_depth = max(segment_depth, accepted_certificate[1])
            additional_root_subintervals += accepted_certificate[2] - 1

        separation = min(
            abs(centers[left] - centers[right])
            - tube_radii[left]
            - tube_radii[right]
            - 8e-15 * (1 + abs(centers[left]) + abs(centers[right]))
            for left in range(6)
            for right in range(left)
        )
        if separation <= 0:
            raise AssertionError("local root-tube disks overlap")
        if segment_depth > 0:
            segments_requiring_subdivision += 1
        maximum_subdivision_depth = max(maximum_subdivision_depth, segment_depth)
        minimum_relative_margin = min(minimum_relative_margin, segment_margin)
        minimum_tube_separation = min(minimum_tube_separation, separation)
        if completed % 5000 == 0:
            print(
                f"{stem}: {completed}/{segment_stop - segment_start} segments",
                flush=True,
            )

    complete = segment_start == 0 and segment_stop == available
    payload = {
        "schema": (
            "MTTQ79GenusTwoSingleDistinguishedContinuousRootTubeCertificate.v1"
            if distinguished
            else "MTTQ79GenusTwoSingleLocalContinuousRootTubeCertificate.v1"
        ),
        "status": (
            (
                "DISTINGUISHED_CONTINUOUS_ROOT_TUBES_CLOSED"
                if distinguished
                else "LOCAL_CONTINUOUS_ROOT_TUBES_CLOSED"
            )
            if complete
            else "PARTIAL_LOCAL_ROOT_TUBE_EXECUTION"
        ),
        "root_id": args.root_id,
        "distinguished_index": args.distinguished_index,
        "authority": {
            "fibration_sha256": sha256(FIBRATION),
            "trajectory_packet_sha256": sha256(packet_path),
            "trajectory_sha256": sha256(trajectory_path),
            "python_flint_version": "0.9.0",
        },
        "branch_chart": {
            "omitted_t_value": omitted,
            "coordinate": "s=1/(t-c)",
        },
        "certificate": {
            "segments_available": available,
            "segment_start": segment_start,
            "segments_certified": segment_stop - segment_start,
            "complete": complete,
            "minimum_Rouche_relative_margin": format(
                minimum_relative_margin, ".17g"
            ),
            "minimum_pairwise_tube_separation": format(
                minimum_tube_separation, ".17g"
            ),
            "segments_requiring_certificate_subdivision": segments_requiring_subdivision,
            "maximum_certificate_subdivision_depth": maximum_subdivision_depth,
            "additional_root_subinterval_certificates": additional_root_subintervals,
        },
        "method": {
            "Rouche_test": "inf|q1|*R > sup|q0| + sum_{k=2}^6 sup|qk|*R^k",
            "coefficient_enclosure": "fourth-order elliptic-flow Taylor model with Arb interval remainder",
            "isotopy_reason": "six fixed disks per segment are pairwise disjoint and convex; true and recorded PL strands share each disk",
        },
        "acceptance": {
            "continuous_local_braid_isotopy_certified": complete,
            "promotion_ready": complete,
        },
    }
    output = (
        data_dir / f"{stem}.root_tube_certificate.packet.json"
        if complete
        else data_dir
        / (
            f"{stem}.root_tube_certificate."
            f"{segment_start}_{segment_stop}.partial.packet.json"
        )
    )
    dump(output, payload)
    print(f"wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
