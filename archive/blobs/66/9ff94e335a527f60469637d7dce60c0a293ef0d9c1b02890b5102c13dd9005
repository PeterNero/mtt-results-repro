from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from flint import acb, acb_series, arb, ctx


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
FIBRATION = DIRECTORY / "selected_alignment_genus2_fibration_seed.interval.packet.json"
MONODROMY = DIRECTORY / "selected_alignment_meridian_monodromy"
OUTPUT = DIRECTORY / "selected_alignment_continuous_root_tubes"
OMITTED = 2 + 3j

Poly = dict[tuple[int, int], acb]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def upper(value: arb) -> float:
    return math.nextafter(float(value.upper()), math.inf)


def lower(value: arb) -> float:
    return math.nextafter(float(value.lower()), -math.inf)


def decode_acb(value: dict[str, str]) -> acb:
    return acb(arb(value["real"]), arb(value["imaginary"]))


def poly_add_term(value: Poly, key: tuple[int, int], coefficient: acb) -> None:
    value[key] = value.get(key, acb(0)) + coefficient


def reduce_elliptic(value: Poly) -> Poly:
    """Reduce modulo b^2=a^3-a while retaining interval coefficients."""
    result: Poly = {}
    for (a_power, b_power), coefficient in value.items():
        quotient, remainder = divmod(b_power, 2)
        for index in range(quotient + 1):
            scalar = math.comb(quotient, index) * (-1) ** (quotient - index)
            target = (a_power + quotient + 2 * index, remainder)
            poly_add_term(result, target, coefficient * scalar)
    return {key: coefficient for key, coefficient in result.items() if not coefficient.is_zero()}


def elliptic_flow(value: Poly) -> Poly:
    derivative: Poly = {}
    for (a_power, b_power), coefficient in value.items():
        if a_power:
            poly_add_term(
                derivative,
                (a_power - 1, b_power + 1),
                coefficient * (2 * a_power),
            )
        if b_power:
            poly_add_term(
                derivative,
                (a_power + 2, b_power - 1),
                coefficient * (3 * b_power),
            )
            poly_add_term(
                derivative,
                (a_power, b_power - 1),
                coefficient * (-b_power),
            )
    return reduce_elliptic(derivative)


def coefficient_at(value: Poly, a_value: acb, b_value: acb) -> acb:
    result = acb(0)
    for (a_power, b_power), coefficient in value.items():
        result += coefficient * a_value**a_power * b_value**b_power
    return result


def selected_transformed_coefficients(packet: dict) -> list[Poly]:
    source: list[Poly] = []
    for row in packet["fiber_polynomials"]["F6"]:
        polynomial: Poly = {}
        for term in row:
            poly_add_term(
                polynomial,
                (int(term["a_power"]), int(term["b_power"])),
                decode_acb(term["coefficient"]),
            )
        source.append(polynomial)
    if len(source) != 7:
        raise AssertionError("selected F6 coefficient inventory changed")

    omitted = acb(format(OMITTED.real, ".17g"), format(OMITTED.imag, ".17g"))
    transformed: list[Poly] = [{} for _ in range(7)]
    for t_power, polynomial in enumerate(source):
        for inverse_power in range(t_power + 1):
            s_power = 6 - inverse_power
            scalar = math.comb(t_power, inverse_power) * omitted ** (
                t_power - inverse_power
            )
            for key, coefficient in polynomial.items():
                poly_add_term(transformed[s_power], key, coefficient * scalar)
    return [reduce_elliptic(polynomial) for polynomial in transformed]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--distinguished-index", type=int, required=True)
    parser.add_argument("--root-id", required=True)
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--limit", type=int, default=None)
    arguments = parser.parse_args()

    stem = f"d{arguments.distinguished_index:03d}_{arguments.root_id}"
    packet_path = MONODROMY / f"{stem}.packet.json"
    monodromy = load(packet_path)
    if (
        monodromy["root_id"] != arguments.root_id
        or monodromy["distinguished_index"] != arguments.distinguished_index
    ):
        raise AssertionError("selected monodromy identity mismatch")
    if monodromy["branch_chart"]["coordinate"] != "s=1/(t-(2+3i))":
        raise AssertionError("selected common reciprocal chart changed")
    trajectory_path = ROOT / monodromy["trajectory"]["path"]
    if sha256(trajectory_path) != monodromy["trajectory"]["sha256"]:
        raise AssertionError("selected trajectory hash mismatch")

    ctx.dps = 70
    fibration = load(FIBRATION)
    transformed = selected_transformed_coefficients(fibration)
    taylor_order = 4
    flow_rows: list[list[Poly]] = [transformed]
    for _ in range(taylor_order):
        flow_rows.append([elliptic_flow(value) for value in flow_rows[-1]])

    tau = acb(0, 1)
    period_length = acb("0.5").elliptic_k() * acb(2).sqrt()
    period_square = period_length**2
    period_cube = period_length**3

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
            format(midpoint.real, ".17g"),
            format(midpoint.imag, ".17g"),
        )
        midpoint_series = acb_series([w_midpoint, acb(1)], 2).elliptic_p(tau)
        a_midpoint = midpoint_series[0] / period_square
        b_midpoint = midpoint_series[1] / (2 * period_cube)
        half_length = abs(w1 - w0) / 2 + 4e-16

        derivative_rows: list[list[acb]] = []
        for derivative_order, polynomial_row in enumerate(flow_rows):
            use_box = derivative_order == taylor_order
            a_value = a_box if use_box else a_midpoint
            b_value = b_box if use_box else b_midpoint
            derivative_rows.append(
                [
                    period_length**derivative_order
                    * coefficient_at(polynomial, a_value, b_value)
                    for polynomial in polynomial_row
                ]
            )
        return derivative_rows, half_length

    def translated_coefficients(
        taylor_data: tuple[list[list[acb]], float], center: complex
    ) -> list[acb]:
        derivative_rows, half_length = taylor_data
        center_ball = acb(
            format(center.real, ".17g"), format(center.imag, ".17g")
        )
        translated: list[acb] = []
        for target_power in range(7):
            translated_derivatives: list[acb] = []
            for derivative_row in derivative_rows:
                value = acb(0)
                for source_power in range(target_power, 7):
                    value += (
                        derivative_row[source_power]
                        * math.comb(source_power, target_power)
                        * center_ball ** (source_power - target_power)
                    )
                translated_derivatives.append(value)
            half_length_ball = arb(format(half_length, ".17g"))
            variation = sum(
                abs(translated_derivatives[order])
                * half_length_ball**order
                / math.factorial(order)
                for order in range(1, taylor_order + 1)
            )
            variation_upper = upper(variation)
            translated.append(
                translated_derivatives[0]
                + acb(
                    arb(0, variation_upper),
                    arb(0, variation_upper),
                )
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
    if roots.shape != (len(w), 6) or point_radii.shape != (len(w), 6):
        raise AssertionError("selected trajectory array shape mismatch")

    available = len(w) - 1
    segment_start = arguments.start
    segment_stop = (
        available
        if arguments.limit is None
        else min(available, arguments.start + arguments.limit)
    )
    if not 0 <= segment_start < segment_stop <= available:
        raise AssertionError("invalid selected tube segment range")

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
                + 4e-15
                * (1 + abs(roots[segment_index + 1, root_index]) + abs(center)),
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
            candidates: list[float] = []
            accepted_radius = None
            accepted_certificate: tuple[float, int, int] | None = None
            for factor in factors:
                radius = max(
                    math.nextafter(endpoint_radius * factor, math.inf), 1e-30
                )
                if radius >= maximum_radius:
                    break
                candidates.append(radius)
                accepted, relative = rouche_margin(translated, radius)
                if accepted:
                    accepted_radius = radius
                    accepted_certificate = (relative, 0, 1)
                    break
            if accepted_radius is None:
                for radius in sorted(candidates, key=lambda value: abs(math.log(value / max(endpoint_radius * 6, 1e-300)))):
                    certificate = certify_subdivision(
                        w0, w1, center, radius, translated
                    )
                    if certificate is not None:
                        accepted_radius = radius
                        accepted_certificate = certificate
                        break
            if accepted_radius is None or accepted_certificate is None:
                raise AssertionError(
                    f"selected Rouche tube failed: path={stem} "
                    f"segment={segment_index} strand={root_index} "
                    f"endpoint_radius={endpoint_radius:.6g} max={maximum_radius:.6g} "
                    f"q0_upper={upper(abs(translated[0])):.6g} "
                    f"q1_lower={lower(abs(translated[1])):.6g}"
                )
            tube_radii.append(accepted_radius)
            segment_margin = min(segment_margin, accepted_certificate[0])
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
            raise AssertionError("selected root-tube disks overlap")
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
        "schema": "MTTQ79SelectedAlignmentSingleContinuousRootTubeCertificate.v1",
        "status": (
            "SELECTED_ALIGNMENT_CONTINUOUS_ROOT_TUBES_CLOSED"
            if complete
            else "PARTIAL_SELECTED_ALIGNMENT_ROOT_TUBE_EXECUTION"
        ),
        "root_id": arguments.root_id,
        "distinguished_index": arguments.distinguished_index,
        "authority": {
            "fibration_sha256": sha256(FIBRATION),
            "monodromy_packet_sha256": sha256(packet_path),
            "trajectory_sha256": sha256(trajectory_path),
            "python_flint_version": "0.9.0",
        },
        "branch_chart": {
            "omitted_t_value": {"real": "2", "imaginary": "3"},
            "coordinate": "s=1/(t-(2+3i))",
        },
        "certificate": {
            "segments_available": available,
            "segment_start": segment_start,
            "segments_certified": segment_stop - segment_start,
            "complete": complete,
            "minimum_Rouche_relative_margin": format(minimum_relative_margin, ".17g"),
            "minimum_pairwise_tube_separation": format(minimum_tube_separation, ".17g"),
            "segments_requiring_certificate_subdivision": segments_requiring_subdivision,
            "maximum_certificate_subdivision_depth": maximum_subdivision_depth,
            "additional_root_subinterval_certificates": additional_root_subintervals,
        },
        "method": {
            "elliptic_curve": "b^2=a^3-a",
            "elliptic_flow": "D=2*b*d/da+(3*a^2-1)*d/db",
            "Rouche_test": "inf|q1|*R > sup|q0| + sum_{k=2}^6 sup|qk|*R^k",
            "coefficient_enclosure": "fourth-order elliptic-flow Taylor model with Arb interval remainder and interval selected-alignment coefficients",
            "isotopy_reason": "six fixed disks per segment are pairwise disjoint and convex; true and recorded PL strands share each disk",
        },
        "acceptance": {
            "continuous_selected_braid_isotopy_certified": complete,
            "promotion_ready": complete,
        },
    }
    output = (
        OUTPUT / f"{stem}.root_tube_certificate.packet.json"
        if complete
        else OUTPUT
        / (
            f"{stem}.root_tube_certificate."
            f"{segment_start}_{segment_stop}.partial.packet.json"
        )
    )
    dump(output, payload)
    print(f"wrote {output.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
