from __future__ import annotations

import argparse
import copy
import itertools
import json
from pathlib import Path

import numpy as np
from flint import acb, acb_mat, arb, ctx

import certify_q79_height4_checkpoint_direct_period_reanchor as path_tools
import certify_q79_height4_target_main_hessian_interval as base
import run_q79_height4_stable_fast_reverse_target_main_hessian as reverse


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = "A380ABI"


def authority(path: Path) -> dict[str, str]:
    return {"path": base.relative(path), "sha256": base.sha256(path)}


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser()
    value.add_argument("--index", type=int, required=True)
    value.add_argument("--checkpoint", type=Path, required=True)
    value.add_argument("--canonical-main", type=Path, required=True)
    value.add_argument("--output", type=Path, required=True)
    value.add_argument("--reanchored-checkpoint", type=Path, required=True)
    value.add_argument("--note", type=Path)
    return value


def component(value: acb, row: int) -> arb:
    return value.imag if row >= 5 else value.real


def main() -> int:
    arguments = parser().parse_args()
    for name in ("checkpoint", "canonical_main", "output", "reanchored_checkpoint", "note"):
        path = getattr(arguments, name)
        if path is not None:
            setattr(arguments, name, path.resolve())
    for path in (arguments.checkpoint, arguments.canonical_main):
        if not path.is_file():
            raise FileNotFoundError(f"interior affine-basis input is absent: {path}")

    packet = base.load(arguments.checkpoint)
    if packet.get("schema") not in {
        "MTTQ79TargetMainHessianCheckpoint.v1",
        "MTTQ79ReverseTargetMainHessianCheckpoint.v1",
    }:
        raise ValueError("unsupported Hessian checkpoint schema")
    config = packet["configuration"]
    if int(config["index"]) != arguments.index:
        raise AssertionError("interior affine-basis target changed")
    if config["canonical_main_sha256"] != base.sha256(arguments.canonical_main):
        raise AssertionError("interior affine-basis canonical-main authority is stale")
    selected_main = base.load(arguments.canonical_main)
    if config["selected_root_id"] != selected_main["selected_target"]["root_id"]:
        raise AssertionError("interior affine-basis selected root changed")

    ctx.dps = int(config["dps"])
    parameter = path_tools.checkpoint_parameter(packet)
    system, _rank, _row = base.selected_system(arguments.index, ctx.dps)
    roots, leading = base.pilot.roots_at(system, parameter)
    root_separation = min(
        base.validated.lower(abs(roots[left] - roots[right]))
        for left in range(6)
        for right in range(left)
    )
    if root_separation <= 0.0:
        raise AssertionError("interior branch roots are not interval separated")

    angle = arb.pi() / 7
    rotation = acb(angle.cos(), -angle.sin())
    projected = [rotation * value for value in roots]
    order = sorted(range(6), key=lambda index: float(projected[index].real.mid()))
    projection_gaps = [
        projected[right].real - projected[left].real
        for left, right in zip(order, order[1:])
    ]
    minimum_projection_gap = min(base.validated.lower(value) for value in projection_gaps)
    if minimum_projection_gap <= 0.0:
        raise AssertionError("interior projected branch-root order is unresolved")
    adjacent_pairs = [
        tuple(sorted((left, right))) for left, right in zip(order, order[1:])
    ]

    numerics = selected_main["numerics"]
    columns: list[list[acb]] = []
    diagnostics: list[dict] = []
    for pair in adjacent_pairs:
        values, row = base.handle.direct_cut_periods(
            roots,
            leading,
            pair,
            segments=int(numerics["cut_segments"]),
            tolerance=float(numerics["cut_tolerance"]),
        )
        columns.append(values)
        diagnostics.append(row)

    center = [base.validated.decoded_acb(value) for value in packet["center"][:5]]
    frame = base.validated.LiftErrorFrame(
        fundamental=base.validated.decoded_matrix(packet["lift_fundamental"]),
        coordinate_radii=[arb(value) for value in packet["coordinate_radii"]],
    )
    transported_radius = base.validated.upper(frame.physical_radius())
    transported = [
        value + reverse.zero_centered_complex_ball(transported_radius) for value in center
    ]

    complex_matrix = np.asarray(
        [
            [base.validated.midpoint(columns[column][coordinate]) for column in range(5)]
            for coordinate in range(5)
        ],
        dtype=np.complex128,
    )
    real_matrix = np.vstack((complex_matrix.real, complex_matrix.imag))
    selected_rows = max(
        itertools.combinations(range(10), 5),
        key=lambda rows: abs(float(np.linalg.det(real_matrix[list(rows), :]))),
    )
    matrix = acb_mat(5, 5)
    target = acb_mat(5, 1)
    for output_row, source_row in enumerate(selected_rows):
        coordinate = source_row % 5
        target[output_row, 0] = acb(component(transported[coordinate], source_row))
        for column in range(5):
            matrix[output_row, column] = acb(
                component(columns[column][coordinate], source_row)
            )
    solved = matrix.solve(target)

    coefficients: list[int] = []
    coefficient_rows: list[dict] = []
    for index in range(5):
        value = solved[index, 0]
        integer = int(round(float(value.real.mid())))
        lower = base.validated.lower(value.real)
        upper = base.validated.upper(value.real)
        if (
            not value.imag.contains(0)
            or not value.real.contains(integer)
            or lower <= integer - 0.5
            or upper >= integer + 0.5
        ):
            raise AssertionError("interior affine coordinate does not isolate one integer")
        coefficients.append(integer)
        coefficient_rows.append(
            {
                "coordinate": index + 1,
                "integer": integer,
                "interval": str(value.real),
                "lower": format(lower, ".17g"),
                "upper": format(upper, ".17g"),
            }
        )

    selected: list[acb] = []
    for coordinate in range(5):
        value = acb(0)
        for coefficient, column in zip(coefficients, columns):
            value += acb(coefficient) * column[coordinate]
        selected.append(value)
    overlap = [left.overlaps(right) for left, right in zip(transported, selected)]
    if not all(overlap):
        raise AssertionError("interior affine-basis cycle misses transported enclosure")
    differences = [
        base.validated.upper(abs(left - right)) for left, right in zip(transported, selected)
    ]
    direct_radius = max(base.validated.radius_upper(value) for value in selected)
    if not 0.0 < direct_radius < transported_radius:
        raise ArithmeticError("interior affine-basis reanchor does not reduce radius")

    prior_reanchor = packet.get("affine_chain_basis_reanchor")
    if not prior_reanchor:
        raise AssertionError("interior affine reanchor lacks its selected source chain")
    prior_certificate_path = ROOT / prior_reanchor["certificate"]["path"]
    if authority(prior_certificate_path) != prior_reanchor["certificate"]:
        raise AssertionError("prior affine-basis certificate authority changed")

    intersection = np.zeros((5, 5), dtype=int)
    for index in range(4):
        intersection[index, index + 1] = 1
        intersection[index + 1, index] = -1
    radical = [1, 0, 1, 0, 1]
    if np.linalg.matrix_rank(intersection) != 4 or np.any(
        intersection @ np.asarray(radical)
    ):
        raise AssertionError("interior affine A5 lattice changed")

    certificate = {
        "schema": "MTTQ79HeightFourInteriorAffineChainBasisReanchor.v1",
        "status": "REGULAR_FIBER_AFFINE_H1_INTEGER_COORDINATES_REANCHORED",
        "artifact": ARTIFACT,
        "distinguished_index": arguments.index,
        "selected_root_id": config["selected_root_id"],
        "path_position": packet["position"],
        "interior_parameter": base.pair(parameter),
        "minimum_root_separation_lower": root_separation,
        "affine_homology_theorem": {
            "rank_H1_affine": 5,
            "adjacent_lifted_branch_arcs_form_integral_A5_basis": True,
            "intersection_matrix": intersection.tolist(),
            "intersection_rank": 4,
            "puncture_radical_generator": radical,
        },
        "cut_system": {
            "projection_rotation": "exp(-i*pi/7)",
            "projected_root_order_zero_based": order,
            "minimum_projected_adjacent_gap_lower": minimum_projection_gap,
            "adjacent_direct_pairs_zero_based": [list(value) for value in adjacent_pairs],
            "direct_cut_diagnostics": diagnostics,
        },
        "integer_coordinate_isolation": {
            "selected_square_rows_zero_based": list(selected_rows),
            "verified_interval_solve": True,
            "coordinate_intervals": coefficient_rows,
            "unique_integer_coordinates": coefficients,
            "all_coordinates_isolate_exactly_one_integer": True,
        },
        "reanchor": {
            "transported_lift_physical_radius_upper": transported_radius,
            "direct_lift_maximum_component_radius_upper": direct_radius,
            "radius_reduction_factor": transported_radius / direct_radius,
            "overlap_by_period_coordinate": overlap,
            "transport_direct_difference_uppers": differences,
            "selected_direct_period_balls": [
                base.validated.encoded_acb(value) for value in selected
            ],
        },
        "authority": {
            "input_checkpoint": authority(arguments.checkpoint),
            "prior_affine_chain_basis_reanchor": authority(prior_certificate_path),
            "selected_main_replay_interval": authority(arguments.canonical_main),
            "direct_cut_period_engine": authority(Path(base.handle.__file__).resolve()),
            "cutoff_root_engine": authority(Path(base.pilot.__file__).resolve()),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "selected_cycle_or_source_changed": False,
            "selected_cycle_integrality_consumed": True,
            "puncture_at_infinity_coordinate_retained": True,
            "integer_coordinates_selected_by_verified_interval_solve": True,
            "all_five_affine_period_coordinates_recomputed": True,
            "accumulated_output_rows_and_radii_retained": True,
            "regular_fiber_affine_reanchor_closed": True,
            "target_main_Hessian_interval_closed": False,
            "full_SM_closure_proved": False,
        },
    }
    base.dump(arguments.output, certificate)

    reanchored = copy.deepcopy(packet)
    reanchored["center"][:5] = [
        base.validated.encoded_acb(
            base.validated.SelectedQ79IntervalSystem.midpoint_acb(value)
        )
        for value in selected
    ]
    identity = acb_mat(5, 5)
    for index in range(5):
        identity[index, index] = acb(1)
    reanchored["lift_fundamental"] = base.validated.encoded_matrix(identity)
    reanchored["coordinate_radii"] = [str(value.rad().upper()) for value in selected]
    reanchored["affine_chain_basis_reanchor"] = {
        "certificate": authority(arguments.output),
        "same_position_outputs_and_output_radii_retained": True,
        "five_coordinate_lift_replaced_by_selected_affine_basis_enclosure": True,
    }
    base.dump(arguments.reanchored_checkpoint, reanchored)

    if arguments.note is not None:
        arguments.note.parent.mkdir(parents=True, exist_ok=True)
        arguments.note.write_text(
            f"# MTT q79 Height-Four d{arguments.index:03d} Interior Affine Reanchor\n\n"
            f"At path position `{packet['position']}`, the regular-fiber affine A5 "
            f"basis isolates coordinates `{coefficients}`.  Direct interval "
            f"re-evaluation reduces the lift radius from `{transported_radius:.17g}` "
            f"to `{direct_radius:.17g}` without changing the selected cycle or any "
            "accumulated Hessian output.\n",
            encoding="utf-8",
        )
    print(f"wrote {base.relative(arguments.output)}")
    print(f"wrote {base.relative(arguments.reanchored_checkpoint)}")
    print(
        json.dumps(
            {
                "parameter": base.pair(parameter),
                "projected_order": order,
                "adjacent_pairs": adjacent_pairs,
                "selected_rows": selected_rows,
                "integer_coefficients": coefficients,
                "transported_radius": transported_radius,
                "direct_radius": direct_radius,
                "radius_reduction_factor": transported_radius / direct_radius,
                "maximum_overlap_difference": max(differences),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
