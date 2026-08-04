from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

import numpy as np
from flint import acb, arb, ctx

import certify_q79_height4_checkpoint_direct_period_reanchor as direct
import certify_q79_height4_target_main_hessian_interval as base
import run_q79_height4_stable_fast_reverse_target_main_hessian as reverse


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser()
    value.add_argument("--index", type=int, required=True)
    value.add_argument("--checkpoint", type=Path, required=True)
    value.add_argument("--canonical-main", type=Path, required=True)
    value.add_argument("--output", type=Path, required=True)
    return value


def main() -> int:
    arguments = parser().parse_args()
    arguments.checkpoint = arguments.checkpoint.resolve()
    arguments.canonical_main = arguments.canonical_main.resolve()
    arguments.output = arguments.output.resolve()
    packet = base.load(arguments.checkpoint)
    selected_main = base.load(arguments.canonical_main)
    config = packet["configuration"]
    if int(config["index"]) != arguments.index:
        raise AssertionError("lattice diagnostic target changed")
    ctx.dps = int(config["dps"])
    system, _rank, _row = base.selected_system(arguments.index, ctx.dps)
    parameter = direct.checkpoint_parameter(packet)
    roots, leading = base.pilot.roots_at(system, parameter)
    transported_center = [
        base.validated.decoded_acb(value) for value in packet["center"][:5]
    ]
    transported_frame = base.validated.LiftErrorFrame(
        fundamental=base.validated.decoded_matrix(packet["lift_fundamental"]),
        coordinate_radii=[arb(value) for value in packet["coordinate_radii"]],
    )
    transported_radius = base.validated.upper(transported_frame.physical_radius())
    transported_balls = [
        value + reverse.zero_centered_complex_ball(transported_radius)
        for value in transported_center
    ]
    target = np.asarray(
        [base.validated.midpoint(value) for value in transported_center],
        dtype=np.complex128,
    )
    numerics = selected_main["numerics"]
    pair_cycles = []
    failed_pairs = []
    for pair in itertools.combinations(range(len(roots)), 2):
        try:
            balls, _diagnostics = base.handle.direct_cut_periods(
                roots,
                leading,
                pair,
                segments=int(numerics["cut_segments"]),
                tolerance=float(numerics["cut_tolerance"]),
            )
        except (ArithmeticError, AssertionError, ValueError) as error:
            failed_pairs.append(
                {"pair_zero_based": list(pair), "reason": f"{type(error).__name__}: {error}"}
            )
            continue
        pair_cycles.append({"pair_zero_based": list(pair), "balls": balls})

    accepted = []
    for basis in itertools.combinations(pair_cycles, 4):
        columns = np.asarray(
            [
                [base.validated.midpoint(value) for value in cycle["balls"]]
                for cycle in basis
            ],
            dtype=np.complex128,
        ).T
        real_system = np.vstack((columns.real, columns.imag))
        real_target = np.concatenate((target.real, target.imag))
        coefficients, _residuals, rank, singular_values = np.linalg.lstsq(
            real_system, real_target, rcond=None
        )
        if rank != 4 or singular_values[-1] <= 1.0e-10:
            continue
        integers = np.rint(coefficients).astype(int)
        rounding_error = float(np.max(abs(coefficients - integers)))
        if rounding_error > 1.0e-7 or int(np.max(abs(integers))) > 32:
            continue
        combination = []
        for coordinate in range(5):
            value = acb(0)
            for coefficient, cycle in zip(integers, basis):
                value += acb(int(coefficient)) * cycle["balls"][coordinate]
            combination.append(value)
        overlap = [
            transported.overlaps(candidate)
            for transported, candidate in zip(transported_balls, combination)
        ]
        if not all(overlap):
            continue
        centers = np.asarray(
            [base.validated.midpoint(value) for value in combination],
            dtype=np.complex128,
        )
        accepted.append(
            {
                "basis_pairs_zero_based": [cycle["pair_zero_based"] for cycle in basis],
                "integer_coefficients": [int(value) for value in integers],
                "coefficient_l1_norm": int(np.sum(abs(integers))),
                "coefficient_rounding_error": rounding_error,
                "basis_minimum_singular_value": float(singular_values[-1]),
                "maximum_center_difference": float(np.max(abs(target - centers))),
                "centers": [base.pair(value) for value in centers],
                "balls": [base.validated.encoded_acb(value) for value in combination],
            }
        )
    accepted.sort(
        key=lambda row: (
            row["maximum_center_difference"],
            row["coefficient_l1_norm"],
            row["basis_pairs_zero_based"],
            row["integer_coefficients"],
        )
    )

    clusters: list[dict] = []
    for candidate_index, candidate in enumerate(accepted):
        centers = np.asarray(
            [base.complex_value(value) for value in candidate["centers"]],
            dtype=np.complex128,
        )
        selected_cluster = None
        for cluster in clusters:
            representative = np.asarray(
                [base.complex_value(value) for value in cluster["representative_centers"]],
                dtype=np.complex128,
            )
            if float(np.max(abs(centers - representative))) <= 1.0e-9:
                selected_cluster = cluster
                break
        if selected_cluster is None:
            selected_cluster = {
                "cluster_index": len(clusters),
                "representative_candidate_index": candidate_index,
                "representative_centers": candidate["centers"],
                "member_candidate_indices": [],
            }
            clusters.append(selected_cluster)
        selected_cluster["member_candidate_indices"].append(candidate_index)
    for cluster in clusters:
        cluster["member_count"] = len(cluster["member_candidate_indices"])

    output = {
        "schema": "MTTQ79HeightFourDirectPeriodLatticeDiagnostic.v1",
        "distinguished_index": arguments.index,
        "parameter": base.pair(parameter),
        "transported_radius_upper": transported_radius,
        "pair_cycle_count": len(pair_cycles),
        "failed_pairs": failed_pairs,
        "accepted_candidate_count": len(accepted),
        "candidate_cluster_count_at_1e_minus_9": len(clusters),
        "clusters": clusters,
        "accepted_candidates": accepted,
        "strict_scope": {
            "diagnostic_only": True,
            "homology_selection_promoted": False,
            "direct_period_reanchor_closed": False,
        },
    }
    base.dump(arguments.output, output)
    print(f"wrote {base.relative(arguments.output)}")
    print(
        json.dumps(
            {
                "accepted_candidate_count": len(accepted),
                "cluster_count": len(clusters),
                "cluster_sizes": [row["member_count"] for row in clusters],
                "best_candidates": accepted[:10],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
