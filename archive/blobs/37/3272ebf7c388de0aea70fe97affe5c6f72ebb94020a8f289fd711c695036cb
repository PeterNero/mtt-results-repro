from __future__ import annotations

import argparse
import copy
import itertools
import json
from pathlib import Path

import numpy as np
from flint import acb, acb_mat, arb, ctx

import certify_q79_height4_target_main_hessian_interval as base
import run_q79_height4_stable_fast_reverse_target_main_hessian as reverse


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = "A380DR"


def authority(path: Path) -> dict[str, str]:
    return {"path": base.relative(path), "sha256": base.sha256(path)}


def checkpoint_parameter(packet: dict) -> complex:
    config = packet["configuration"]
    start = base.complex_value(config["start"])
    endpoint = base.complex_value(config["endpoint"])
    distance = abs(endpoint - start)
    if distance <= 0.0:
        raise ArithmeticError("checkpoint path has zero length")
    position = float(packet["position"])
    if not 0.0 <= position <= distance:
        raise AssertionError("checkpoint position lies outside its path")
    return start + (endpoint - start) * (position / distance)


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser()
    value.add_argument("--index", type=int, required=True)
    value.add_argument("--checkpoint", type=Path, required=True)
    value.add_argument("--canonical-main", type=Path, required=True)
    value.add_argument("--output", type=Path)
    value.add_argument("--reanchored-checkpoint", type=Path)
    return value


def main() -> int:
    arguments = parser().parse_args()
    arguments.checkpoint = arguments.checkpoint.resolve()
    arguments.canonical_main = arguments.canonical_main.resolve()
    if arguments.output is not None:
        arguments.output = arguments.output.resolve()
    if arguments.reanchored_checkpoint is not None:
        arguments.reanchored_checkpoint = arguments.reanchored_checkpoint.resolve()
    for path in (arguments.checkpoint, arguments.canonical_main):
        if not path.is_file():
            raise FileNotFoundError(f"direct-period reanchor input is absent: {path}")
    packet = base.load(arguments.checkpoint)
    if packet.get("schema") not in {
        "MTTQ79TargetMainHessianCheckpoint.v1",
        "MTTQ79ReverseTargetMainHessianCheckpoint.v1",
    }:
        raise ValueError("unsupported Hessian checkpoint schema")
    config = packet["configuration"]
    if int(config["index"]) != arguments.index:
        raise AssertionError("checkpoint target identity changed")
    if config["canonical_main_sha256"] != base.sha256(arguments.canonical_main):
        raise AssertionError("checkpoint canonical-main authority is stale")
    selected_main = base.load(arguments.canonical_main)
    if config["selected_root_id"] != selected_main["selected_target"]["root_id"]:
        raise AssertionError("checkpoint root identity changed")

    dps = int(config["dps"])
    ctx.dps = dps
    system, _rank, _row = base.selected_system(arguments.index, dps)
    parameter = checkpoint_parameter(packet)
    roots, leading = base.pilot.roots_at(system, parameter)
    cut_pair = tuple(
        int(value)
        for value in selected_main["selected_target"][
            "near_node_colliding_pair_zero_based"
        ]
    )
    if len(cut_pair) != 2:
        raise AssertionError("selected cut pair changed")
    root_separation = min(
        base.validated.lower(abs(roots[left] - roots[right]))
        for left in range(len(roots))
        for right in range(left)
    )
    if root_separation <= 0.0:
        raise AssertionError("interior roots are not interval-separated")
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
    numerics = selected_main["numerics"]
    candidates = []
    pair_cycles = []
    failed_pairs = []
    for pair in itertools.combinations(range(len(roots)), 2):
        try:
            direct_balls, diagnostics = base.handle.direct_cut_periods(
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
        if len(direct_balls) != 5:
            raise AssertionError("direct-period engine did not return five coordinates")
        pair_cycles.append(
            {
                "pair_zero_based": list(pair),
                "balls": direct_balls,
                "diagnostics": diagnostics,
            }
        )
        for sign in (1, -1):
            oriented = [acb(sign) * value for value in direct_balls]
            overlap = [
                transported.overlaps(direct)
                for transported, direct in zip(transported_balls, oriented)
            ]
            differences = [
                base.validated.upper(abs(transported - direct))
                for transported, direct in zip(transported_balls, oriented)
            ]
            candidates.append(
                {
                    "pair_zero_based": list(pair),
                    "basis_pairs_zero_based": [list(pair)],
                    "integer_coefficients": [sign],
                    "orientation_sign": sign,
                    "balls": oriented,
                    "overlap": overlap,
                    "differences": differences,
                    "diagnostics": diagnostics,
                }
            )
    accepted = [candidate for candidate in candidates if all(candidate["overlap"])]
    if not accepted:
        target = np.asarray(
            [base.validated.midpoint(value) for value in transported_center],
            dtype=np.complex128,
        )
        combination_candidates = []
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
                transported.overlaps(direct)
                for transported, direct in zip(transported_balls, combination)
            ]
            differences = [
                base.validated.upper(abs(transported - direct))
                for transported, direct in zip(transported_balls, combination)
            ]
            if all(overlap):
                combination_candidates.append(
                    {
                        "pair_zero_based": None,
                        "basis_pairs_zero_based": [
                            cycle["pair_zero_based"] for cycle in basis
                        ],
                        "integer_coefficients": [int(value) for value in integers],
                        "orientation_sign": None,
                        "balls": combination,
                        "overlap": overlap,
                        "differences": differences,
                        "coefficient_rounding_error": rounding_error,
                        "basis_minimum_singular_value": float(singular_values[-1]),
                        "diagnostics": [cycle["diagnostics"] for cycle in basis],
                    }
                )
        accepted.extend(combination_candidates)
    if len(accepted) != 1:
        if accepted:
            accepted.sort(
                key=lambda candidate: (
                    sum(abs(value) for value in candidate["integer_coefficients"]),
                    candidate["basis_pairs_zero_based"],
                    candidate["integer_coefficients"],
                )
            )
            chosen = accepted[0]
            equivalent = all(
                all(
                    left.overlaps(right)
                    for left, right in zip(chosen["balls"], candidate["balls"])
                )
                for candidate in accepted[1:]
            )
            if equivalent:
                accepted = [chosen]
                chosen["equivalent_integer_representations"] = len(
                    combination_candidates
                )
        if len(accepted) == 1:
            pass
        else:
            ranked = sorted(
                candidates,
                key=lambda candidate: (
                    -sum(candidate["overlap"]),
                    max(candidate["differences"]),
                ),
            )
            print(
                json.dumps(
                    {
                        "accepted_candidate_count": len(accepted),
                        "best_candidates": [
                            {
                                "pair_zero_based": candidate["pair_zero_based"],
                                "orientation_sign": candidate["orientation_sign"],
                                "overlap_count": sum(candidate["overlap"]),
                                "maximum_difference_upper": max(candidate["differences"]),
                            }
                            for candidate in ranked[:5]
                        ],
                        "failed_pairs": failed_pairs,
                    },
                    indent=2,
                )
            )
            raise AssertionError(
                "direct-period reanchor does not select one integral-cycle enclosure"
            )
    selected = accepted[0]
    direct_radius = max(
        base.validated.radius_upper(value) for value in selected["balls"]
    )
    if direct_radius <= 0.0:
        raise ArithmeticError("direct-period reanchor radius is not positive")

    output = arguments.output or arguments.checkpoint.parent / f"a{arguments.index:03d}.dr.json"
    reanchored_path = (
        arguments.reanchored_checkpoint
        or arguments.checkpoint.parent / f"a{arguments.index:03d}.rc.json"
    )
    certificate = {
        "schema": "MTTQ79HeightFourCheckpointDirectPeriodReanchor.v1",
        "status": "FIVE_COORDINATE_INTERIOR_DIRECT_PERIOD_REANCHOR_CERTIFIED",
        "artifact": ARTIFACT,
        "distinguished_index": arguments.index,
        "checkpoint_schema": packet["schema"],
        "path_position": packet["position"],
        "interior_parameter": base.pair(parameter),
        "selected_root_id": config["selected_root_id"],
        "near_node_cut_pair_zero_based": list(cut_pair),
        "interior_overlap_selected_pair_zero_based": selected["pair_zero_based"],
        "interior_integral_cycle_basis_pairs_zero_based": selected[
            "basis_pairs_zero_based"
        ],
        "interior_integral_cycle_coefficients": selected["integer_coefficients"],
        "minimum_root_separation_lower": root_separation,
        "selected_cycle_orientation_sign": selected["orientation_sign"],
        "all_five_transport_direct_intervals_overlap": True,
        "overlap_by_coordinate": selected["overlap"],
        "transport_direct_difference_uppers": selected["differences"],
        "transported_lift_physical_radius_upper": transported_radius,
        "direct_lift_maximum_component_radius_upper": direct_radius,
        "radius_reduction_factor": transported_radius / direct_radius,
        "direct_period_balls": [
            base.validated.encoded_acb(value) for value in selected["balls"]
        ],
        "direct_cut_diagnostics": selected["diagnostics"],
        "rejected_direct_pair_count": len(failed_pairs),
        "authority": {
            "input_checkpoint": authority(arguments.checkpoint),
            "selected_main_replay_interval": authority(arguments.canonical_main),
            "direct_cut_period_engine": authority(Path(base.handle.__file__).resolve()),
            "cutoff_root_engine": authority(Path(base.pilot.__file__).resolve()),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "all_five_affine_period_coordinates_recomputed": True,
            "puncture_lift_coordinates_retained": True,
            "integral_cycle_selected_by_unique_interval_overlap": True,
            "interior_direct_period_reanchor_closed": True,
            "target_main_Hessian_interval_closed": False,
            "full_SM_closure_proved": False,
        },
    }
    base.dump(output, certificate)

    reanchored = copy.deepcopy(packet)
    reanchored["center"][:5] = [
        base.validated.encoded_acb(
            base.validated.SelectedQ79IntervalSystem.midpoint_acb(value)
        )
        for value in selected["balls"]
    ]
    identity = acb_mat(5, 5)
    for index in range(5):
        identity[index, index] = acb(1)
    reanchored["lift_fundamental"] = base.validated.encoded_matrix(identity)
    reanchored["coordinate_radii"] = [
        str(value.rad().upper()) for value in selected["balls"]
    ]
    reanchored["direct_period_reanchor"] = {
        "certificate": authority(output),
        "same_position_outputs_and_output_radii_retained": True,
        "five_coordinate_lift_replaced_by_unique_overlapping_direct_enclosure": True,
    }
    base.dump(reanchored_path, reanchored)
    print(f"wrote {base.relative(output)}")
    print(f"wrote {base.relative(reanchored_path)}")
    print(json.dumps({
        "orientation_sign": selected["orientation_sign"],
        "transported_radius": transported_radius,
        "direct_radius": direct_radius,
        "radius_reduction_factor": transported_radius / direct_radius,
        "maximum_overlap_difference": max(selected["differences"]),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
