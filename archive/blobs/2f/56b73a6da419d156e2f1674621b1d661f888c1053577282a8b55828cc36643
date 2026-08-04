from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from flint import acb, acb_mat, acb_poly, arb, ctx

import certify_q79_height4_d087_full_residue_main_interval as n3_engine
import certify_q79_selected_side_base_lift_interval as base


ROOT = Path(__file__).resolve().parents[1]
PERIOD_DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
)
PROBE = PERIOD_DIRECTORY / "covariant_floating_probe"
N3 = PROBE / "cplx" / "n3ud" / "probe.packet.json"
A219 = PROBE / "rank3_complex_PGL3_floating_boundary.packet.json"
SOURCE = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
    / "pgl3_projective_ychart_broyden_04.exploratory.json"
)
OUTPUT = PROBE / "validated_transport" / "n3.rank3.base_lift.interval.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourRank3BaseLiftInterval_A375_v1.md"
ARTIFACT = "A375"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dps", type=int, default=80)
    parser.add_argument("--winding-edges", type=int, default=64)
    arguments = parser.parse_args()
    ctx.dps = arguments.dps

    system = n3_engine.exact_target_system(arguments.dps)
    evaluator = system.evaluator
    elliptic = [acb(0, -1), acb(1, 1), acb(1)]
    line = base.matrix_vector(system.alignment, elliptic)
    f_coefficients = base.aligned_coefficients(evaluator.tables["F6"], line, chart="z")
    g_coefficients = base.aligned_coefficients(evaluator.tables["G3"], line, chart="z")
    q_coefficients = base.aligned_coefficients(evaluator.tables["Q2"], line, chart="z")
    f_roots = acb_poly(f_coefficients).roots(tol=1.0e-50, maxprec=8192)
    q_roots = acb_poly(q_coefficients).roots(tol=1.0e-50, maxprec=8192)
    if len(f_roots) != 6 or len(q_roots) != 2:
        raise AssertionError("n3 base-fiber root isolation failed")
    q_roots.sort(key=lambda value: (base.midpoint(value).real, base.midpoint(value).imag))

    source = load(SOURCE)
    winding_reference = base.exact_acb(source["final_winding_reference"])
    midpoint_distances = [abs(base.midpoint(root - winding_reference)) for root in f_roots]
    winding_index = int(np.argmin(midpoint_distances))
    winding_root = f_roots[winding_index]
    selected_distance_upper = base.upper(abs(winding_root - winding_reference))
    next_distance_lower = min(
        base.lower(abs(root - winding_reference))
        for index, root in enumerate(f_roots)
        if index != winding_index
    )
    if selected_distance_upper >= next_distance_lower:
        raise AssertionError("the continued n3 winding root is not interval-separated")
    clearances = [
        base.lower(abs(winding_root - root))
        for index, root in enumerate(f_roots)
        if index != winding_index
    ] + [base.lower(abs(winding_root - root)) for root in q_roots]
    winding_clearance_lower = min(clearances)
    if winding_clearance_lower <= 0.0:
        raise AssertionError("the n3 winding root ball is not isolated")
    winding_radius = arb(format(min(0.1, 0.15 * winding_clearance_lower), ".17g"))
    outer = acb(20, 7)

    integrator = base.CertifiedPathIntegrator(f_coefficients, dps=arguments.dps)
    states = []
    for root in q_roots:
        sheet = base.polynomial(g_coefficients, root)
        sheet, periods = integrator.integrate_segment(
            root, outer, sheet, [acb(0) for _ in range(5)]
        )
        states.append([sheet, periods])
    direct_difference_upper = base.upper(abs(states[0][0] - states[1][0]))
    direct_sum_lower = base.lower(abs(states[0][0] + states[1][0]))
    if direct_difference_upper >= direct_sum_lower:
        raise AssertionError("n3 direct outer paths are not on the same sheet")

    circle_start = winding_root + acb(winding_radius)
    sheet, periods = states[1]
    sheet, periods = integrator.integrate_segment(outer, circle_start, sheet, periods)
    vertices = []
    for index in range(arguments.winding_edges + 1):
        angle = arb.pi() * arb(-2 * index) / arb(arguments.winding_edges)
        vertices.append(winding_root + acb(angle.cos(), angle.sin()) * acb(winding_radius))
    for start, end in zip(vertices, vertices[1:]):
        sheet, periods = integrator.integrate_segment(start, end, sheet, periods)
    sheet, periods = integrator.integrate_segment(circle_start, outer, sheet, periods)
    states[1] = [sheet, periods]

    outer_cancellation_upper = base.upper(abs(states[0][0] + states[1][0]))
    outer_sheet_lower = min(base.lower(abs(states[0][0])), base.lower(abs(states[1][0])))
    if outer_cancellation_upper >= 1.0e-20 * max(1.0, outer_sheet_lower):
        raise AssertionError("n3 opposite outer sheets did not cancel rigorously")
    z_lift = [-(left + right) for left, right in zip(states[0][1], states[1][1])]

    alpha = -line[0] / line[1]
    beta = -line[2] / line[1]
    common = -(line[1] ** 2) / (line[2] ** 2)
    z_from_y = acb_mat(5, 5)
    for power in range(5):
        for index in range(power + 1):
            z_from_y[power, index] = (
                common
                * acb(math.comb(power, index))
                * alpha ** (power - index)
                * beta**index
            )
    y_lift_matrix = z_from_y.solve(acb_mat([[value] for value in z_lift]))
    y_lift = [y_lift_matrix[index, 0] for index in range(5)]
    maximum_radius = max(base.radius_upper(value) for value in [*z_lift, *y_lift])

    n3 = load(N3)
    floating = np.asarray(
        [
            complex_value(value)
            for value in n3["moving_beta"]["diagnostics"]["base_abel_jacobi_lift"]
        ],
        dtype=np.complex128,
    )
    rigorous_centers = np.asarray([base.midpoint(value) for value in y_lift])
    floating_difference = float(np.max(abs(floating - rigorous_centers)))
    if floating_difference >= 2.0e-6:
        raise AssertionError("rigorous n3 base lift disagrees with the independent floating check")

    payload = {
        "schema": "MTTQ79HeightFourRank3BaseLiftInterval.v1",
        "status": "N3_RANK3_BASE_ABEL_JACOBI_LIFT_INTERVAL_CERTIFIED",
        "artifact": ARTIFACT,
        "branch_selection": {
            "route": "A131 selected winding root continued to exact n3 alignment",
            "fixed_winding_reference": base.complex_interval(winding_reference),
            "selected_root_to_reference_distance_upper": selected_distance_upper,
            "next_root_to_reference_distance_lower": next_distance_lower,
            "root_label_separation_margin_lower": next_distance_lower
            - selected_distance_upper,
            "winding_clearance_lower": winding_clearance_lower,
            "winding_radius": str(winding_radius),
            "clockwise_winding_edges": arguments.winding_edges,
        },
        "path": {
            "source_chart": "z",
            "target_chart": "y",
            "outer_point": {"real": "20", "imaginary": "7"},
            "direct_outer_paths_same_sheet": True,
            "opposite_outer_sheet_cancellation_upper": outer_cancellation_upper,
            "minimum_square_root_half_plane_margin": integrator.minimum_half_plane_margin,
            "minimum_branch_sign_separation_margin": integrator.minimum_sign_margin,
            "certified_segment_count": integrator.segment_count,
            "maximum_subdivision_depth": integrator.maximum_depth,
            "rigorous_integral_count": integrator.integral_count,
        },
        "z_chart_base_lift": [base.complex_interval(value) for value in z_lift],
        "y_chart_base_lift": [base.complex_interval(value) for value in y_lift],
        "summary": {
            "maximum_component_ball_radius_upper": maximum_radius,
            "floating_center_maximum_difference_diagnostic_only": floating_difference,
        },
        "authority": {
            name: {"path": relative(path), "sha256": sha256(path)}
            for name, path in {
                "n3_ultra_probe": N3,
                "A219_profile_boundary": A219,
                "n3_exact_fibration": n3_engine.FIBRATION,
                "selected_winding_reference_source": SOURCE,
                "n3_interval_system": Path(n3_engine.__file__).resolve(),
                "base_lift_interval_engine": Path(base.__file__).resolve(),
                "builder_source": Path(__file__).resolve(),
            }.items()
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "exact_n3_interval_system_used": True,
            "continued_winding_root_interval_separated": True,
            "square_root_branch_continuation_closed": True,
            "opposite_infinity_sheet_cancellation_closed": True,
            "exact_projective_chart_transport_closed": True,
            "rank3_base_Abel_Jacobi_lift_interval_closed": True,
            "rank3_anchored_beta_interval_closed": False,
            "interval_Jacobian_certificate": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "run the inhomogeneous validated beta transport from this exact n3 "
            "base-lift interval on the selected wall-free contour"
        ),
    }
    dump(OUTPUT, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four Rank-3 Base Lift Interval (A375) v1\n\n"
        "A375 certifies the selected Abel-Jacobi base lift directly on the exact "
        "n3 interval alignment. The previously selected winding-root label remains "
        "unique by a strict interval distance margin, and the clockwise winding, "
        "opposite-sheet cancellation, and exact z-to-y chart transport are all "
        "enclosed.\n\n"
        f"The maximum component-ball radius is `{maximum_radius:.12g}`. The "
        "independent floating center agrees to "
        f"`{floating_difference:.12g}` but is not used as an error bound.\n\n"
        "This closes the initial-value object required by the rank-3 beta "
        "transport; it does not itself prove the endpoint beta or the covariant zero.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
