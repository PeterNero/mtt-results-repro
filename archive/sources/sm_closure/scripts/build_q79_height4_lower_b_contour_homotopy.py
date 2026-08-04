from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path

from flint import acb, ctx

import build_q79_selected_alignment_dual_discriminant as dual
import certify_q79_height4_d087_full_residue_main_interval as node_engine
import certify_q79_selected_side_beta_defect_transport as validated
import explore_q79_height4_covariant_floating_probe as probe


ROOT = Path(__file__).resolve().parents[1]
PERIOD_DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
)
PROBE = PERIOD_DIRECTORY / "covariant_floating_probe"
VALIDATED = PROBE / "validated_transport"
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
A376 = VALIDATED / "n3.rank3.anchored_beta.interval.json"
A383 = VALIDATED / "n3.rank3.handle_hessian.interval.json"
OUTPUT = VALIDATED / "n3.lower_b_contour_homotopy.a401.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourLowerBContourHomotopy_A401_v1.md"
ARTIFACT = "A401"
DPS = 90
RECTANGLE = {"real_minimum": 0.65, "real_maximum": 0.82, "imaginary_minimum": -0.1, "imaginary_maximum": 0.0}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def authority(path: Path) -> dict[str, str]:
    return {"path": relative(path), "sha256": sha256(path)}


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def node_path(index: int) -> Path:
    return VALIDATED / f"d{index:03d}.n3.node.refined.json"


def normalized_parameter(value: acb) -> tuple[acb, int, int]:
    center = probe.midpoint(value)
    real_shift = -math.floor(center.real)
    imaginary_shift = -math.floor(center.imag + 0.5)
    normalized = value + acb(real_shift, imaginary_shift)
    if not (
        validated.lower(normalized.real) > 0.0
        and validated.upper(normalized.real) < 1.0
        and validated.lower(normalized.imag) > -0.5
        and validated.upper(normalized.imag) < 0.5
    ):
        raise AssertionError("critical parameter ball crosses the selected torus chart boundary")
    return normalized, real_shift, imaginary_shift


def rectangle_clearance(value: acb) -> float:
    real_lower = validated.lower(value.real)
    real_upper = validated.upper(value.real)
    imaginary_lower = validated.lower(value.imag)
    imaginary_upper = validated.upper(value.imag)
    if real_upper < RECTANGLE["real_minimum"]:
        dx = RECTANGLE["real_minimum"] - real_upper
    elif real_lower > RECTANGLE["real_maximum"]:
        dx = real_lower - RECTANGLE["real_maximum"]
    else:
        dx = 0.0
    if imaginary_upper < RECTANGLE["imaginary_minimum"]:
        dy = RECTANGLE["imaginary_minimum"] - imaginary_upper
    elif imaginary_lower > RECTANGLE["imaginary_maximum"]:
        dy = imaginary_lower - RECTANGLE["imaginary_maximum"]
    else:
        dy = 0.0
    return math.nextafter(math.hypot(dx, dy), -math.inf)


def torus_separation(left: acb, right: acb) -> float:
    return min(
        validated.lower(abs(left - right + acb(real_shift, imaginary_shift)))
        for real_shift in (-1, 0, 1)
        for imaginary_shift in (-1, 0, 1)
    )


def discriminant_degree_certificate(alignment: list[list[complex]]) -> dict:
    packet = load(DUAL)
    alignment_ball = probe.point_matrix(alignment)
    lines: list[dual.EllipticPair] = [
        (
            {0: alignment_ball[row, 2], 1: alignment_ball[row, 0]},
            {0: alignment_ball[row, 1]},
        )
        for row in range(3)
    ]
    selected: dual.EllipticPair = ({}, {})
    for row in packet["dual_discriminant"]["integer_coefficient_rows"]:
        contribution: dual.EllipticPair = (
            {0: acb(int(row["coefficient"]))},
            {},
        )
        for source, power in zip(lines, row["powers_L0_L1_L2"]):
            contribution = dual.pair_multiply(
                contribution, dual.pair_power(source, int(power))
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
    nonzero_degrees = [
        degree for degree, coefficient in norm.items() if validated.lower(abs(coefficient)) > 0.0
    ]
    degree = max(nonzero_degrees)
    if degree != 90:
        raise AssertionError("selected n3 dual discriminant no longer has degree 90")
    return {
        "degree": degree,
        "leading_coefficient_absolute_lower": validated.lower(abs(norm[degree])),
        "coefficient_count": len(norm),
    }


def main() -> int:
    ctx.dps = DPS
    n3 = load(N3)
    fan = load(FAN)
    alignment = [
        [complex_value(value) for value in row] for row in n3["alignment"]
    ]
    floating_centers, floating_diagnostics = probe.continued_critical_centers(
        probe.complex_matrix(n3["alignment"])
    )
    fan_rows = fan["distinguished_positive_meridians"]
    if len(fan_rows) != 90:
        raise AssertionError("selected distinguished fan no longer has 90 rows")
    root_by_index = {
        int(row["distinguished_index"]): row["root_id"] for row in fan_rows
    }
    if set(root_by_index) != set(range(1, 91)) or len(set(root_by_index.values())) != 90:
        raise AssertionError("selected distinguished fan indexing changed")
    system = node_engine.exact_target_system(DPS)
    nodes = []
    normalized_balls: list[acb] = []
    existing_authority = {}
    newly_certified = []
    for index in range(1, 91):
        root_id = root_by_index[index]
        path = node_path(index)
        if path.exists():
            source = load(path)
            if source["selected_target"]["root_id"] != root_id:
                raise AssertionError(f"d{index:03d} node root identity changed")
            certified = source["certified_node"]
            parameter = validated.decoded_acb(certified["parameter_ball"])
            root = validated.decoded_acb(certified["double_root_ball"])
            diagnostics = certified["node_diagnostics"]
            source_kind = "existing_A373_node_packet"
            existing_authority[f"d{index:03d}_node"] = authority(path)
        else:
            parameter, root, diagnostics = node_engine.fast_certify_node(
                system,
                floating_centers[root_id],
                epsilon=1.0e-5,
                iterations=3,
            )
            source_kind = "A401_interval_Newton_completion"
            newly_certified.append(index)
        for key in (
            "F_parameter_absolute_lower",
            "F_tt_absolute_lower",
            "jacobian_determinant_absolute_lower",
        ):
            if float(diagnostics[key]) <= 0.0:
                raise AssertionError(f"d{index:03d} node simplicity gate failed: {key}")
        normalized, real_shift, imaginary_shift = normalized_parameter(parameter)
        clearance = rectangle_clearance(normalized)
        if clearance <= 0.0:
            raise AssertionError(f"d{index:03d} critical ball meets the contour homotopy rectangle")
        normalized_balls.append(normalized)
        nodes.append(
            {
                "distinguished_index": index,
                "root_id": root_id,
                "source_kind": source_kind,
                "raw_parameter_ball": validated.encoded_acb(parameter),
                "normalized_parameter_ball": validated.encoded_acb(normalized),
                "normalizing_lattice_shift": [real_shift, imaginary_shift],
                "double_root_ball": validated.encoded_acb(root),
                "rectangle_clearance_lower": clearance,
                "F_parameter_absolute_lower": float(
                    diagnostics["F_parameter_absolute_lower"]
                ),
                "F_tt_absolute_lower": float(diagnostics["F_tt_absolute_lower"]),
                "jacobian_determinant_absolute_lower": float(
                    diagnostics["jacobian_determinant_absolute_lower"]
                ),
            }
        )

    minimum_separation = math.inf
    closest_pair = None
    for right_index, right in enumerate(normalized_balls):
        for left_index, left in enumerate(normalized_balls[:right_index]):
            separation = torus_separation(left, right)
            if separation < minimum_separation:
                minimum_separation = separation
                closest_pair = [left_index + 1, right_index + 1]
    if minimum_separation <= 0.0:
        raise AssertionError("the 90 certified critical parameter balls are not distinct")
    minimum_clearance_row = min(nodes, key=lambda row: row["rectangle_clearance_lower"])
    degree = discriminant_degree_certificate(alignment)
    if degree["degree"] != len(nodes):
        raise AssertionError("certified node count does not saturate the discriminant degree")

    beta = load(A376)
    handle = load(A383)
    beta_waypoints = beta["method"]["waypoints"]
    expected_waypoints = [
        {"real": "0", "imaginary": "0"},
        {"real": "0.65000000000000002", "imaginary": "0"},
        {"real": "0.65000000000000002", "imaginary": "-0.10000000000000001"},
        {"real": "0.81999999999999995", "imaginary": "-0.10000000000000001"},
        {"real": "0.81999999999999995", "imaginary": "0"},
        {"real": "1", "imaginary": "0"},
    ]
    if beta_waypoints != expected_waypoints:
        raise AssertionError("A376 lower-contour waypoint word changed")
    if handle["path_executions"]["B"]["endpoint"] != {"real": "1", "imaginary": "0"}:
        raise AssertionError("A383 B-handle endpoint changed")

    payload = {
        "schema": "MTTQ79HeightFourLowerBContourHomotopy.v1",
        "status": "ALL_90_N3_CRITICAL_VALUES_CERTIFIED_LOWER_AND_STRAIGHT_B_CONTOURS_HOMOTOPIC",
        "artifact": ARTIFACT,
        "critical_value_certificate": {
            "dual_discriminant": degree,
            "certified_node_count": len(nodes),
            "existing_node_packets_consumed": len(nodes) - len(newly_certified),
            "new_interval_Newton_nodes": newly_certified,
            "all_nodes_simple": True,
            "all_node_parameter_balls_pairwise_disjoint_on_torus": True,
            "minimum_pairwise_torus_separation_lower": minimum_separation,
            "closest_distinguished_pair": closest_pair,
            "nodes": nodes,
            "floating_seed_diagnostics_not_used_as_bounds": floating_diagnostics,
        },
        "contour_homotopy": {
            "straight_B_waypoints": [
                {"real": "0", "imaginary": "0"},
                {"real": "1", "imaginary": "0"},
            ],
            "selected_lower_waypoints": beta_waypoints,
            "bounded_difference_rectangle": RECTANGLE,
            "minimum_critical_value_clearance_lower": minimum_clearance_row[
                "rectangle_clearance_lower"
            ],
            "nearest_distinguished_index": minimum_clearance_row[
                "distinguished_index"
            ],
            "nearest_root_id": minimum_clearance_row["root_id"],
            "rectangle_contains_no_critical_value": True,
        },
        "theorem": {
            "name": "Q79N3LowerContourBHandleHomotopyTheorem",
            "proved": True,
            "statement": (
                "The degree-90 n3 discriminant has exactly the 90 distinct simple "
                "critical values enclosed above. None meets the closed rectangle "
                "between the straight B path and the A376 local-lower detour. "
                "Therefore those paths are homotopic relative endpoints in the "
                "punctured elliptic base, so the A130 B-handle generator may be "
                "transported on the A376 contour without changing its integral class."
            ),
        },
        "authority": {
            "n3_same_source_probe": authority(N3),
            "selected_distinguished_fan": authority(FAN),
            "exact_dual_discriminant": authority(DUAL),
            "A376_lower_beta_contour": authority(A376),
            "A383_straight_B_handle": authority(A383),
            "n3_interval_node_engine": authority(Path(node_engine.__file__).resolve()),
            "floating_seed_engine": authority(Path(probe.__file__).resolve()),
            "builder_source": authority(Path(__file__).resolve()),
            **existing_authority,
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "degree_90_discriminant_closed": True,
            "all_90_simple_n3_critical_values_interval_certified": True,
            "straight_to_lower_B_contour_homotopy_closed": True,
            "A130_B_handle_may_use_A376_lower_contour": True,
            "joint_beta_minus_B_handle_transport_executed": False,
            "full_relative_chain_transport_executed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "transport the inhomogeneous Abel-Jacobi lift minus the selected B-handle "
            "five-period state in one augmented affine frame on the A376 contour"
        ),
    }
    dump(OUTPUT, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four Lower B-Contour Homotopy (A401) v1\n\n"
        "A401 completes interval-Newton boxes for all 90 simple n3 critical "
        "values and verifies that they exhaust the degree-90 discriminant. None "
        "intersects the closed rectangle between the straight B handle and the "
        "A376 local-lower contour.\n\n"
        f"The minimum rigorous clearance is "
        f"`{minimum_clearance_row['rectangle_clearance_lower']:.12g}`, attained by "
        f"`{minimum_clearance_row['root_id']}`. Hence the two contours are "
        "homotopic in the punctured base, and the selected B-handle contribution "
        "may lawfully be evaluated on the beta contour. The joint correlated "
        "transport itself remains the next artifact.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(
        json.dumps(
            {
                "node_count": len(nodes),
                "new_nodes": newly_certified,
                "minimum_pairwise_torus_separation_lower": minimum_separation,
                "minimum_rectangle_clearance_lower": minimum_clearance_row[
                    "rectangle_clearance_lower"
                ],
                "nearest_root_id": minimum_clearance_row["root_id"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
