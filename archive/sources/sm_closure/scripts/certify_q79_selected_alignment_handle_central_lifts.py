from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np
from flint import acb, acb_series, arb, ctx

from certify_q79_selected_alignment_single_root_tubes import (
    coefficient_at,
    elliptic_flow,
    selected_transformed_coefficients,
)


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
FIBRATION = DIRECTORY / "selected_alignment_genus2_fibration_seed.interval.packet.json"
HANDLES = DIRECTORY / "selected_alignment_handle_monodromy"
OUTPUT = DIRECTORY / "selected_alignment_handle_central_lifts.interval.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def lower(value: arb) -> float:
    return math.nextafter(float(value.lower()), -math.inf)


def strict_sign(value: arb, label: str) -> int:
    if value.lower() > 0:
        return 1
    if value.upper() < 0:
        return -1
    raise AssertionError(f"interval sign unresolved: {label}: {value}")


def main() -> int:
    ctx.dps = 80
    fibration = load(FIBRATION)
    # The s^6 coefficient equals F6(t=2+3i,w). Its nonvanishing is exactly
    # the common reciprocal-chart condition, and its square-root winding fixes
    # the hyperelliptic central lift missed by branch-point braiding alone.
    leading = selected_transformed_coefficients(fibration)[6]
    taylor_order = 4
    flow = [leading]
    for _ in range(taylor_order):
        flow.append(elliptic_flow(flow[-1]))

    tau = acb(0, 1)
    period_length = acb("0.5").elliptic_k() * acb(2).sqrt()
    period_square = period_length**2
    period_cube = period_length**3

    def ab_at(w_value: acb) -> tuple[acb, acb]:
        series = acb_series([w_value, acb(1)], 2).elliptic_p(tau)
        return series[0] / period_square, series[1] / (2 * period_cube)

    def value_at(w_value: complex) -> acb:
        w = acb(format(w_value.real, ".17g"), format(w_value.imag, ".17g"))
        a_value, b_value = ab_at(w)
        return coefficient_at(leading, a_value, b_value)

    def enclosure_over_segment(w0: complex, w1: complex) -> acb:
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
        a_box, b_box = ab_at(w_box)
        w_midpoint = acb(
            format(midpoint.real, ".17g"), format(midpoint.imag, ".17g")
        )
        a_midpoint, b_midpoint = ab_at(w_midpoint)
        derivatives: list[acb] = []
        for order, polynomial in enumerate(flow):
            use_box = order == taylor_order
            derivatives.append(
                period_length**order
                * coefficient_at(
                    polynomial,
                    a_box if use_box else a_midpoint,
                    b_box if use_box else b_midpoint,
                )
            )
        half_length = arb(format(abs(w1 - w0) / 2 + 4e-16, ".17g"))
        variation = sum(
            abs(derivatives[order]) * half_length**order / math.factorial(order)
            for order in range(1, taylor_order + 1)
        )
        radius = math.nextafter(float(variation.upper()), math.inf)
        return derivatives[0] + acb(arb(0, radius), arb(0, radius))

    def polygon_winding(values: list[acb], ray_denominator: int) -> tuple[int, float, float]:
        angle = arb.pi() / ray_denominator
        rotation = acb(angle.cos(), -angle.sin())
        rotated = [rotation * value for value in values]
        winding = 0
        minimum_endpoint_imaginary = math.inf
        minimum_crossing_real = math.inf
        for index, (left, right) in enumerate(zip(rotated, rotated[1:])):
            y0 = left.imag
            y1 = right.imag
            sign0 = strict_sign(y0, f"ray {ray_denominator} segment {index} left")
            sign1 = strict_sign(y1, f"ray {ray_denominator} segment {index} right")
            minimum_endpoint_imaginary = min(
                minimum_endpoint_imaginary, lower(abs(y0)), lower(abs(y1))
            )
            if sign0 == sign1:
                continue
            parameter = -y0 / (y1 - y0)
            if not parameter.lower() > 0 or not parameter.upper() < 1:
                raise AssertionError("central-lift ray crossing parameter unresolved")
            x_crossing = left.real + parameter * (right.real - left.real)
            x_sign = strict_sign(x_crossing, "central-lift ray crossing real part")
            minimum_crossing_real = min(minimum_crossing_real, lower(abs(x_crossing)))
            if x_sign > 0:
                winding += 1 if sign0 < sign1 else -1
        return winding, minimum_endpoint_imaginary, minimum_crossing_real

    rows: list[dict] = []
    for name in ("A", "B"):
        packet_path = HANDLES / f"handle_{name}.packet.json"
        packet = load(packet_path)
        trajectory_path = ROOT / packet["trajectory"]["path"]
        if sha256(trajectory_path) != packet["trajectory"]["sha256"]:
            raise AssertionError(f"selected handle {name} trajectory hash")
        with np.load(trajectory_path) as data:
            w = data["w"]
        values = [value_at(complex(point)) for point in w]
        minimum_nonzero = math.inf
        refined_values: list[acb] = [values[0]]
        additional_subsegments = 0

        def certify_segment(
            w0: complex,
            w1: complex,
            value0: acb,
            value1: acb,
            depth: int = 0,
        ) -> tuple[list[acb], float, int]:
            enclosure = enclosure_over_segment(w0, w1)
            margin = lower(abs(enclosure))
            if margin > 0:
                return [value1], margin, 0
            if depth >= 14:
                raise AssertionError(
                    f"selected handle {name} leading coefficient unresolved"
                )
            midpoint = (w0 + w1) / 2
            midpoint_value = value_at(midpoint)
            left_values, left_margin, left_extra = certify_segment(
                w0, midpoint, value0, midpoint_value, depth + 1
            )
            right_values, right_margin, right_extra = certify_segment(
                midpoint, w1, midpoint_value, value1, depth + 1
            )
            return (
                [*left_values, *right_values],
                min(left_margin, right_margin),
                1 + left_extra + right_extra,
            )

        for segment_index in range(len(w) - 1):
            segment_values, segment_margin, segment_extra = certify_segment(
                complex(w[segment_index]),
                complex(w[segment_index + 1]),
                values[segment_index],
                values[segment_index + 1],
            )
            refined_values.extend(segment_values)
            minimum_nonzero = min(minimum_nonzero, segment_margin)
            additional_subsegments += segment_extra

        winding_data = None
        for denominator in (13, 17, 19, 23, 29, 31):
            try:
                winding_data = (
                    denominator,
                    *polygon_winding(refined_values, denominator),
                )
                break
            except AssertionError:
                continue
        if winding_data is None:
            raise AssertionError(f"selected handle {name} has no certified ray")
        denominator, winding, endpoint_gap, crossing_gap = winding_data
        lift = 1 if winding % 2 == 0 else -1
        endpoint_difference = abs(values[-1] - values[0])
        if not endpoint_difference.contains(0):
            raise AssertionError(f"selected handle {name} endpoint coefficient mismatch")
        rows.append(
            {
                "handle": name,
                "trajectory_segments": len(w) - 1,
                "certified_coefficient_subsegments": len(refined_values) - 1,
                "additional_certificate_subsegments": additional_subsegments,
                "leading_coefficient": "q6(w)=F6(t=2+3i,w)",
                "minimum_leading_coefficient_absolute_lower": format(minimum_nonzero, ".17g"),
                "certified_ray_rotation": f"exp(-i*pi/{denominator})",
                "minimum_rotated_endpoint_imaginary_absolute_lower": format(endpoint_gap, ".17g"),
                "minimum_ray_crossing_real_absolute_lower": (
                    format(crossing_gap, ".17g") if crossing_gap < math.inf else None
                ),
                "leading_coefficient_winding_number": winding,
                "hyperelliptic_central_lift": lift,
                "endpoint_periodicity_contains_zero": True,
            }
        )

    payload = {
        "schema": "MTTQ79SelectedAlignmentHandleCentralLiftsInterval.v1",
        "status": "SELECTED_ALIGNMENT_HANDLE_CENTRAL_LIFTS_CERTIFIED",
        "authority": {
            "fibration_sha256": sha256(FIBRATION),
            "handle_A_packet_sha256": sha256(HANDLES / "handle_A.packet.json"),
            "handle_B_packet_sha256": sha256(HANDLES / "handle_B.packet.json"),
            "certifier_source_sha256": sha256(Path(__file__)),
        },
        "theorem": {
            "name": "Q79SelectedAlignmentHyperellipticCentralLiftTheorem",
            "statement": "For a reciprocal sextic u^2=sum q_k s^k with q6 nonzero along a closed base loop, the central deck lift is (-1)^wind(q6). The interval Taylor cover proves q6 nonzero on both selected handle loops and the certified ray crossing count computes the winding exactly.",
            "proved": True,
        },
        "handles": rows,
        "selected_lifts": {row["handle"]: row["hyperelliptic_central_lift"] for row in rows},
        "strict_scope": {
            "period_values_used": 0,
            "central_lifts_selected_by_period_fit": False,
            "observed_SM_values_used": False,
        },
    }
    OUTPUT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"wrote {OUTPUT.relative_to(ROOT)}")
    print(json.dumps(payload["selected_lifts"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
