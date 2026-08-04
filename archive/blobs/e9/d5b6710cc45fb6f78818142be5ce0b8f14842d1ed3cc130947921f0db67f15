from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path

from flint import acb, ctx


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_q79_selected_alignment_dual_discriminant as dual
import certify_q79_height4_d087_full_residue_main_interval as node_engine
import certify_q79_selected_side_beta_defect_transport as validated
import explore_q79_height4_covariant_floating_probe as probe


PERIOD_DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
)
PROBE = PERIOD_DIRECTORY / "covariant_floating_probe"
VALIDATED = PROBE / "validated_transport"
PACKET = VALIDATED / "n3.lower_b_contour_homotopy.a401.json"
N3 = PROBE / "cplx" / "n3ud" / "probe.packet.json"
FAN = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_distinguished_radial_fan.interval.packet.json"
)
DUAL = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_dual_discriminant.interval.packet.json"
)
RECTANGLE = (0.65, 0.82, -0.1, 0.0)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def normalize(value: acb) -> acb:
    center = probe.midpoint(value)
    return value + acb(-math.floor(center.real), -math.floor(center.imag + 0.5))


def clearance(value: acb) -> float:
    xmin, xmax, ymin, ymax = RECTANGLE
    rlo, rhi = validated.lower(value.real), validated.upper(value.real)
    ilo, ihi = validated.lower(value.imag), validated.upper(value.imag)
    dx = xmin - rhi if rhi < xmin else rlo - xmax if rlo > xmax else 0.0
    dy = ymin - ihi if ihi < ymin else ilo - ymax if ilo > ymax else 0.0
    return math.nextafter(math.hypot(dx, dy), -math.inf)


def separation(left: acb, right: acb) -> float:
    return min(
        validated.lower(abs(left - right + acb(dx, dy)))
        for dx in (-1, 0, 1)
        for dy in (-1, 0, 1)
    )


def discriminant_degree(n3: dict) -> tuple[int, float]:
    source = load(DUAL)
    alignment = probe.point_matrix(
        [[complex_value(value) for value in row] for row in n3["alignment"]]
    )
    lines: list[dual.EllipticPair] = [
        (
            {0: alignment[row, 2], 1: alignment[row, 0]},
            {0: alignment[row, 1]},
        )
        for row in range(3)
    ]
    selected: dual.EllipticPair = ({}, {})
    for row in source["dual_discriminant"]["integer_coefficient_rows"]:
        contribution: dual.EllipticPair = ({0: acb(int(row["coefficient"]))}, {})
        for factor, power in zip(lines, row["powers_L0_L1_L2"]):
            contribution = dual.pair_multiply(
                contribution, dual.pair_power(factor, int(power))
            )
        selected = dual.pair_add(selected, contribution)
    p_value, q_value = selected
    norm = dual.poly_add(
        dual.poly_multiply(p_value, p_value),
        dual.poly_scale(
            dual.poly_add(
                dual.poly_shift(dual.poly_multiply(q_value, q_value), 3),
                dual.poly_scale(
                    dual.poly_shift(dual.poly_multiply(q_value, q_value), 1), -1
                ),
            ),
            -1,
        ),
    )
    degrees = [
        index for index, coefficient in norm.items() if validated.lower(abs(coefficient)) > 0
    ]
    degree = max(degrees)
    return degree, validated.lower(abs(norm[degree]))


def main() -> int:
    ctx.dps = 90
    packet = load(PACKET)
    n3 = load(N3)
    fan = load(FAN)["distinguished_positive_meridians"]
    require(
        packet["schema"] == "MTTQ79HeightFourLowerBContourHomotopy.v1",
        "A401 schema changed",
    )
    require(packet["artifact"] == "A401", "A401 artifact changed")
    require(packet["theorem"]["proved"], "A401 theorem is not marked proved")
    root_by_index = {int(row["distinguished_index"]): row["root_id"] for row in fan}
    require(len(root_by_index) == 90, "distinguished fan count changed")
    stored_rows = {
        int(row["distinguished_index"]): row
        for row in packet["critical_value_certificate"]["nodes"]
    }
    require(set(stored_rows) == set(range(1, 91)), "A401 node inventory changed")
    floating_centers, _diagnostics = probe.continued_critical_centers(
        probe.complex_matrix(n3["alignment"])
    )
    system = node_engine.exact_target_system(90)
    balls = []
    clearances = []
    new_indices = []
    for index in range(1, 91):
        path = VALIDATED / f"d{index:03d}.n3.node.refined.json"
        if path.exists():
            source = load(path)
            parameter = validated.decoded_acb(source["certified_node"]["parameter_ball"])
            diagnostics = source["certified_node"]["node_diagnostics"]
        else:
            parameter, _root, diagnostics = node_engine.fast_certify_node(
                system,
                floating_centers[root_by_index[index]],
                epsilon=1.0e-5,
                iterations=3,
            )
            new_indices.append(index)
        require(
            float(diagnostics["jacobian_determinant_absolute_lower"]) > 0.0,
            f"d{index:03d} simplicity gate failed",
        )
        normalized = normalize(parameter)
        stored = validated.decoded_acb(stored_rows[index]["normalized_parameter_ball"])
        require(normalized.overlaps(stored), f"d{index:03d} normalized box replay changed")
        value_clearance = clearance(normalized)
        require(value_clearance > 0.0, f"d{index:03d} meets the homotopy rectangle")
        require(
            value_clearance
            >= float(stored_rows[index]["rectangle_clearance_lower"]),
            f"d{index:03d} clearance is overreported",
        )
        balls.append(normalized)
        clearances.append(value_clearance)
    minimum_separation = min(
        separation(left, right)
        for right_index, right in enumerate(balls)
        for left in balls[:right_index]
    )
    require(minimum_separation > 0.0, "A401 node boxes overlap on the torus")
    minimum_clearance = min(clearances)
    summary = packet["critical_value_certificate"]
    require(new_indices == summary["new_interval_Newton_nodes"], "A401 new-node set changed")
    require(
        minimum_separation
        >= float(summary["minimum_pairwise_torus_separation_lower"]),
        "A401 pairwise separation is overreported",
    )
    require(
        minimum_clearance
        >= float(packet["contour_homotopy"]["minimum_critical_value_clearance_lower"]),
        "A401 rectangle clearance is overreported",
    )
    degree, leading_lower = discriminant_degree(n3)
    require(degree == 90 and leading_lower > 0.0, "A401 degree-90 certificate failed")
    require(degree == len(balls), "A401 node boxes do not saturate the degree")
    for label, authority in packet["authority"].items():
        path = ROOT / authority["path"]
        require(path.exists(), f"A401 authority missing: {label}")
        require(sha256(path) == authority["sha256"], f"A401 authority stale: {label}")
    scope = packet["strict_scope"]
    require(scope["all_90_simple_n3_critical_values_interval_certified"], "A401 roots open")
    require(scope["straight_to_lower_B_contour_homotopy_closed"], "A401 homotopy open")
    require(not scope["joint_beta_minus_B_handle_transport_executed"], "A401 overclaims transport")
    require(not scope["covariant_zero_proved"], "A401 overclaims a zero")
    print(
        "PASS: A401 independently certifies all 90 simple critical values and "
        f"the B-contour homotopy; minimum clearance {minimum_clearance:.6e}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
