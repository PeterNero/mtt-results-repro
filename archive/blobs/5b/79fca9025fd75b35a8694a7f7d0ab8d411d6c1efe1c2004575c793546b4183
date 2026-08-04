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
EXPLORATION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2handlemonodromycandidate"
    / "handle_monodromy_exploration.packet.json"
)
OUTPUT = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2handlemonodromycandidate"
    / "handle_continuous_root_tube_certificate.packet.json"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def upper(value: arb) -> float:
    return math.nextafter(float(value.upper()), math.inf)


def lower(value: arb) -> float:
    return math.nextafter(float(value.lower()), -math.inf)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--handle", choices=("A", "B"), default=None)
    args = parser.parse_args()

    ctx.dps = 55
    fibration = load(FIBRATION)
    exploration = load(EXPLORATION)

    a, b, t, s = sp.symbols("a b t s")
    t_coefficients = [
        sp.sympify(value)
        for value in fibration["fiber_chart"]["f_coefficients_t_descending"]
    ]
    f_ab = sum(
        coefficient * t ** (6 - index)
        for index, coefficient in enumerate(t_coefficients)
    )
    transformed_raw = sp.Poly(
        sp.expand(s**6 * f_ab.subs(t, 2 + 3 * sp.I + 1 / s)), s
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

    coefficient_terms = [expression_terms(expression) for expression in transformed]
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
        real_midpoint = (w0.real + w1.real) / 2
        imaginary_midpoint = (w0.imag + w1.imag) / 2
        real_radius = abs(w1.real - w0.real) / 2 + 3e-16
        imaginary_radius = abs(w1.imag - w0.imag) / 2 + 3e-16
        w_box = acb(
            arb(format(real_midpoint, ".17g"), format(real_radius, ".17g")),
            arb(format(imaginary_midpoint, ".17g"), format(imaginary_radius, ".17g")),
        )
        box_series = acb_series([w_box, acb(1)], 2).elliptic_p(tau)
        a_box = box_series[0] / period_square
        b_box = box_series[1] / (2 * period_cube)

        w_midpoint = acb(
            format(real_midpoint, ".17g"), format(imaginary_midpoint, ".17g")
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
        taylor_data: tuple[list[list[acb]], float],
        center: complex,
    ) -> list[acb]:
        derivative_rows_descending, half_length = taylor_data
        derivative_rows_ascending = [
            list(reversed(row)) for row in derivative_rows_descending
        ]
        c = acb(format(center.real, ".17g"), format(center.imag, ".17g"))
        translated: list[acb] = []
        for k in range(7):
            translated_derivatives: list[acb] = []
            for derivative_row in derivative_rows_ascending:
                derivative_value = acb(0)
                for j in range(k, 7):
                    derivative_value += (
                        derivative_row[j]
                        * math.comb(j, k)
                        * c ** (j - k)
                    )
                translated_derivatives.append(derivative_value)
            half_length_ball = arb(format(half_length, ".17g"))
            variation_ball = sum(
                abs(translated_derivatives[derivative_order])
                * half_length_ball**derivative_order
                / math.factorial(derivative_order)
                for derivative_order in range(1, taylor_order + 1)
            )
            variation = upper(variation_ball)
            inflation = acb(arb(0, variation), arb(0, variation))
            translated.append(translated_derivatives[0] + inflation)
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
        relative = lower(margin_lower / denominator)
        return accepted, relative

    def certify_interval_with_subdivision(
        w0: complex,
        w1: complex,
        center: complex,
        radius: float,
        translated: list[acb],
        depth: int = 0,
        maximum_depth: int = 8,
    ) -> tuple[float, int, int] | None:
        accepted, relative = rouche_margin(translated, radius)
        if accepted:
            return relative, depth, 1
        if depth >= maximum_depth:
            return None
        midpoint = (w0 + w1) / 2
        left = certify_interval_with_subdivision(
            w0,
            midpoint,
            center,
            radius,
            translated_coefficients(
                coefficient_taylor_data_over_segment(w0, midpoint), center
            ),
            depth + 1,
            maximum_depth,
        )
        if left is None:
            return None
        right = certify_interval_with_subdivision(
            midpoint,
            w1,
            center,
            radius,
            translated_coefficients(
                coefficient_taylor_data_over_segment(midpoint, w1), center
            ),
            depth + 1,
            maximum_depth,
        )
        if right is None:
            return None
        return min(left[0], right[0]), max(left[1], right[1]), left[2] + right[2]

    handle_certificates: list[dict] = []
    selected_handles = [
        row
        for row in exploration["handles"]
        if args.handle is None or row["name"] == args.handle
    ]
    for handle in selected_handles:
        trajectory_path = ROOT / handle["trajectory"]["path"]
        if hashlib.sha256(trajectory_path.read_bytes()).hexdigest() != handle["trajectory"]["sha256"]:
            raise AssertionError("trajectory hash mismatch")
        data = np.load(trajectory_path)
        w = data["w"]
        roots = data["roots"]
        point_radii = data["root_radius_uppers"]
        available_segment_count = len(w) - 1
        segment_start = args.start
        segment_stop = available_segment_count
        if args.limit is not None:
            segment_stop = min(segment_stop, segment_start + args.limit)
        if not 0 <= segment_start <= segment_stop:
            raise AssertionError("invalid segment range")
        segment_count = segment_stop - segment_start

        minimum_relative_margin = math.inf
        minimum_tube_separation = math.inf
        maximum_radius_to_separation = 0.0
        maximum_subdivision_depth = 0
        segments_requiring_subdivision = 0
        additional_root_subinterval_certificates = 0
        certified_segments = 0
        for segment_index in range(segment_start, segment_stop):
            w0 = complex(w[segment_index])
            w1 = complex(w[segment_index + 1])
            coefficient_taylor_data = coefficient_taylor_data_over_segment(
                w0, w1
            )
            centers = (roots[segment_index] + roots[segment_index + 1]) / 2
            tube_radii: list[float] = []
            segment_relative_margin = math.inf
            segment_subdivision_depth = 0
            for root_index in range(6):
                center = complex(centers[root_index])
                endpoint_radius = max(
                    abs(roots[segment_index, root_index] - center)
                    + point_radii[segment_index, root_index]
                    + 4e-15
                    * (1 + abs(roots[segment_index, root_index]) + abs(center)),
                    abs(roots[segment_index + 1, root_index] - center)
                    + point_radii[segment_index + 1, root_index]
                    + 4e-15
                    * (1 + abs(roots[segment_index + 1, root_index]) + abs(center)),
                )
                endpoint_radius = math.nextafter(float(endpoint_radius), math.inf)
                nearest_center = min(
                    abs(center - centers[other])
                    for other in range(6)
                    if other != root_index
                )
                nearest_center_lower = nearest_center - 8e-15 * (
                    1 + abs(center) + max(abs(value) for value in centers)
                )
                maximum_radius = 0.44 * nearest_center_lower
                translated = translated_coefficients(coefficient_taylor_data, center)
                accepted_radius = None
                accepted_relative = None
                candidate_radii: list[tuple[float, float]] = []
                for factor in (
                    1.2,
                    1.5,
                    2,
                    3,
                    4,
                    6,
                    8,
                    12,
                    16,
                    24,
                    32,
                    48,
                    64,
                    96,
                    128,
                    192,
                    256,
                    384,
                    512,
                ):
                    radius = max(
                        math.nextafter(float(endpoint_radius) * factor, math.inf),
                        1e-30,
                    )
                    if radius >= maximum_radius:
                        break
                    candidate_radii.append((factor, radius))
                    accepted, relative = rouche_margin(translated, radius)
                    if accepted:
                        accepted_radius = radius
                        accepted_relative = relative
                        break
                if accepted_radius is None:
                    for _, radius in sorted(
                        candidate_radii,
                        key=lambda row: abs(math.log(row[0] / 6)),
                    ):
                        certificate = certify_interval_with_subdivision(
                            w0, w1, center, radius, translated
                        )
                        if certificate is None:
                            continue
                        accepted_radius = radius
                        accepted_relative = certificate[0]
                        segment_subdivision_depth = max(
                            segment_subdivision_depth, certificate[1]
                        )
                        additional_root_subinterval_certificates += certificate[2] - 1
                        break
                if accepted_radius is None or accepted_relative is None:
                    _, diagnostic_relative = rouche_margin(
                        translated, maximum_radius * 0.99
                    )
                    raise AssertionError(
                        f"Rouche tube failed: handle={handle['name']} "
                        f"segment={segment_index} root={root_index} "
                        f"endpoint_radius={endpoint_radius:.6g} max={maximum_radius:.6g} "
                        f"relative_at_0.99max={diagnostic_relative:.6g} "
                        f"q0_upper={upper(abs(translated[0])):.6g} "
                        f"q1_lower={lower(abs(translated[1])):.6g}"
                    )
                tube_radii.append(accepted_radius)
                segment_relative_margin = min(segment_relative_margin, accepted_relative)

            tube_separation = min(
                abs(centers[left] - centers[right])
                - tube_radii[left]
                - tube_radii[right]
                - 8e-15 * (1 + abs(centers[left]) + abs(centers[right]))
                for left in range(6)
                for right in range(left)
            )
            if tube_separation <= 0:
                raise AssertionError(
                    f"tube disks overlap: handle={handle['name']} segment={segment_index}"
                )
            minimum_center_separation = min(
                abs(centers[left] - centers[right])
                for left in range(6)
                for right in range(left)
            )
            maximum_radius_to_separation = max(
                maximum_radius_to_separation,
                max(tube_radii) / minimum_center_separation,
            )
            if segment_subdivision_depth > 0:
                segments_requiring_subdivision += 1
            maximum_subdivision_depth = max(
                maximum_subdivision_depth, segment_subdivision_depth
            )
            minimum_relative_margin = min(
                minimum_relative_margin, segment_relative_margin
            )
            minimum_tube_separation = min(minimum_tube_separation, tube_separation)
            certified_segments += 1
            if certified_segments % 500 == 0:
                print(
                    f"handle {handle['name']}: {certified_segments}/{segment_count} tubes",
                    flush=True,
                )

        complete = segment_start == 0 and certified_segments == available_segment_count
        handle_certificates.append(
            {
                "name": handle["name"],
                "trajectory_path": handle["trajectory"]["path"],
                "trajectory_sha256": handle["trajectory"]["sha256"],
                "segments_available": len(w) - 1,
                "segment_start": segment_start,
                "segments_certified": certified_segments,
                "complete": complete,
                "minimum_Rouche_relative_margin": format(minimum_relative_margin, ".17g"),
                "minimum_pairwise_tube_separation": format(minimum_tube_separation, ".17g"),
                "maximum_tube_radius_to_center_separation": format(
                    maximum_radius_to_separation, ".17g"
                ),
                "segments_requiring_certificate_subdivision": segments_requiring_subdivision,
                "maximum_certificate_subdivision_depth": maximum_subdivision_depth,
                "additional_root_subinterval_certificates": additional_root_subinterval_certificates,
            }
        )

    payload = {
        "schema": "MTTQ79GenusTwoHandleContinuousRootTubeCertificate.v1",
        "status": (
            "TWO_HANDLE_CONTINUOUS_ROOT_TUBES_CLOSED"
            if len(handle_certificates) == 2
            and all(row["complete"] for row in handle_certificates)
            else "PARTIAL_HANDLE_ROOT_TUBE_EXECUTION"
        ),
        "authority": {
            "fibration_sha256": hashlib.sha256(FIBRATION.read_bytes()).hexdigest(),
            "exploration_sha256": hashlib.sha256(EXPLORATION.read_bytes()).hexdigest(),
            "python_flint_version": "0.9.0",
        },
        "method": {
            "segment_parameter_enclosure": "rectangular acb box containing each normalized-torus path segment",
            "root_tube": "fixed disk D(c,R) for each labeled strand over one segment",
            "Rouche_test": "inf|q1|*R > sup|q0| + sum_{k=2}^6 sup|qk|*R^k for p(c+x)=sum qk*x^k",
            "adaptive_refinement": "failed segment-level interval tests are bisected, with one fixed root disk retained over every child subinterval",
            "isotopy_reason": "six disks are pairwise disjoint and convex; both the true strand and recorded PL strand lie in the same disk over the segment",
        },
        "handles": handle_certificates,
        "acceptance": {
            "A_continuous_braid_isotopy_certified": any(
                row["name"] == "A" and row["complete"] for row in handle_certificates
            ),
            "B_continuous_braid_isotopy_certified": any(
                row["name"] == "B" and row["complete"] for row in handle_certificates
            ),
        },
    }
    if args.limit is None and args.handle is None:
        dump(OUTPUT, payload)
        print(f"wrote {OUTPUT}")
    else:
        print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
