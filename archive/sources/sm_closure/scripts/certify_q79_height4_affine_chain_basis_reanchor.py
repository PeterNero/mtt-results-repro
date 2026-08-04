from __future__ import annotations

import argparse
import copy
import itertools
import json
import math
from pathlib import Path

import numpy as np
from flint import acb, acb_mat, arb, ctx

import certify_q79_height4_target_main_hessian_interval as base
import run_q79_height4_stable_fast_reverse_target_main_hessian as reverse


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = "A380AB"


def authority(path: Path) -> dict[str, str]:
    return {"path": base.relative(path), "sha256": base.sha256(path)}


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser()
    value.add_argument("--index", type=int, required=True)
    value.add_argument("--initial-checkpoint", type=Path, required=True)
    value.add_argument("--canonical-main", type=Path, required=True)
    value.add_argument("--output", type=Path, required=True)
    value.add_argument("--reanchored-checkpoint", type=Path, required=True)
    value.add_argument("--note", type=Path)
    return value


def real_component(value: acb, row: int) -> arb:
    coordinate = row % 5
    return value.imag if row >= 5 else value.real


def main() -> int:
    arguments = parser().parse_args()
    arguments.initial_checkpoint = arguments.initial_checkpoint.resolve()
    arguments.canonical_main = arguments.canonical_main.resolve()
    arguments.output = arguments.output.resolve()
    arguments.reanchored_checkpoint = arguments.reanchored_checkpoint.resolve()
    arguments.note = (
        arguments.note.resolve()
        if arguments.note is not None
        else ROOT
        / "proof_corpus"
        / (
            f"MTT_q79HeightFourD{arguments.index:03d}"
            "AffineChainBasisReanchor_A380AB_v1.md"
        )
    )
    for path in (arguments.initial_checkpoint, arguments.canonical_main):
        if not path.is_file():
            raise FileNotFoundError(f"affine-basis reanchor input is absent: {path}")

    checkpoint = base.load(arguments.initial_checkpoint)
    if checkpoint.get("schema") != "MTTQ79ReverseTargetMainHessianCheckpoint.v1":
        raise ValueError("affine-basis reanchor requires a reverse initial checkpoint")
    config = checkpoint["configuration"]
    if int(config["index"]) != arguments.index:
        raise AssertionError("affine-basis target identity changed")
    if float(checkpoint["position"]) != 0.0 or checkpoint["accepted_steps"]:
        raise AssertionError("affine-basis reanchor must be applied at the smooth base")
    if config["canonical_main_sha256"] != base.sha256(arguments.canonical_main):
        raise AssertionError("canonical-main authority is stale")

    selected_main = base.load(arguments.canonical_main)
    if config["selected_root_id"] != selected_main["selected_target"]["root_id"]:
        raise AssertionError("selected root identity changed")
    ctx.dps = int(config["dps"])
    system, _rank, _row = base.selected_system(arguments.index, ctx.dps)
    roots, leading = base.pilot.roots_at(system, 0.0 + 0.0j)
    if len(roots) != 6:
        raise AssertionError("affine genus-two branch-root count changed")

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
        raise AssertionError("base branch-root projected order is not interval separated")
    adjacent_pairs = [
        tuple(sorted((left, right))) for left, right in zip(order, order[1:])
    ]

    numerics = selected_main["numerics"]
    columns: list[list[acb]] = []
    diagnostics: list[dict] = []
    for pair in adjacent_pairs:
        values, row_diagnostics = base.handle.direct_cut_periods(
            roots,
            leading,
            pair,
            segments=int(numerics["cut_segments"]),
            tolerance=float(numerics["cut_tolerance"]),
        )
        if len(values) != 5:
            raise AssertionError("affine-chain period column count changed")
        columns.append(values)
        diagnostics.append(row_diagnostics)

    transported_center = [
        base.validated.decoded_acb(value) for value in checkpoint["center"][:5]
    ]
    transported_frame = base.validated.LiftErrorFrame(
        fundamental=base.validated.decoded_matrix(checkpoint["lift_fundamental"]),
        coordinate_radii=[arb(value) for value in checkpoint["coordinate_radii"]],
    )
    transported_radius = base.validated.upper(transported_frame.physical_radius())
    transported_balls = [
        value + reverse.zero_centered_complex_ball(transported_radius)
        for value in transported_center
    ]

    complex_matrix = np.asarray(
        [
            [base.validated.midpoint(columns[column][coordinate]) for column in range(5)]
            for coordinate in range(5)
        ],
        dtype=np.complex128,
    )
    real_matrix = np.vstack((complex_matrix.real, complex_matrix.imag))
    row_candidates = list(itertools.combinations(range(10), 5))
    selected_rows = max(
        row_candidates,
        key=lambda rows: abs(float(np.linalg.det(real_matrix[list(rows), :]))),
    )

    interval_matrix = acb_mat(5, 5)
    interval_target = acb_mat(5, 1)
    for output_row, source_row in enumerate(selected_rows):
        coordinate = source_row % 5
        interval_target[output_row, 0] = acb(
            real_component(transported_balls[coordinate], source_row)
        )
        for column in range(5):
            interval_matrix[output_row, column] = acb(
                real_component(columns[column][coordinate], source_row)
            )
    coefficient_balls = interval_matrix.solve(interval_target)

    integer_coefficients: list[int] = []
    coefficient_rows: list[dict] = []
    for index in range(5):
        value = coefficient_balls[index, 0]
        if not value.imag.contains(0):
            raise AssertionError("real affine coordinate acquired an imaginary part")
        integer = int(round(float(value.real.mid())))
        lower = base.validated.lower(value.real)
        upper = base.validated.upper(value.real)
        if not value.real.contains(integer):
            raise AssertionError("selected affine integer is outside its interval")
        if not lower > integer - 0.5 or not upper < integer + 0.5:
            raise AssertionError("affine coordinate interval does not isolate one integer")
        integer_coefficients.append(integer)
        coefficient_rows.append(
            {
                "coordinate": index + 1,
                "integer": integer,
                "interval": str(value.real),
                "lower": format(lower, ".17g"),
                "upper": format(upper, ".17g"),
                "distance_to_nearest_competing_integer_lower": format(
                    min(lower - (integer - 1), (integer + 1) - upper), ".17g"
                ),
            }
        )

    selected_balls: list[acb] = []
    for coordinate in range(5):
        value = acb(0)
        for coefficient, column in zip(integer_coefficients, columns):
            value += acb(coefficient) * column[coordinate]
        selected_balls.append(value)
    overlap = [
        transported.overlaps(selected)
        for transported, selected in zip(transported_balls, selected_balls)
    ]
    if not all(overlap):
        raise AssertionError("selected affine-chain period misses transported source")
    differences = [
        base.validated.upper(abs(transported - selected))
        for transported, selected in zip(transported_balls, selected_balls)
    ]
    direct_radius = max(base.validated.radius_upper(value) for value in selected_balls)
    if not 0.0 < direct_radius < transported_radius:
        raise ArithmeticError("affine-chain reanchor does not reduce the lift radius")

    intersection = np.zeros((5, 5), dtype=int)
    for index in range(4):
        intersection[index, index + 1] = 1
        intersection[index + 1, index] = -1
    radical = np.asarray([1, 0, 1, 0, 1], dtype=int)
    if np.linalg.matrix_rank(intersection) != 4 or np.any(intersection @ radical):
        raise AssertionError("affine A5 intersection lattice changed")

    certificate = {
        "schema": "MTTQ79HeightFourAffineChainBasisReanchor.v1",
        "status": "SELECTED_AFFINE_H1_INTEGER_COORDINATES_AND_REANCHOR_CERTIFIED",
        "artifact": ARTIFACT,
        "distinguished_index": arguments.index,
        "selected_root_id": config["selected_root_id"],
        "base_parameter": base.pair(0.0 + 0.0j),
        "affine_homology_theorem": {
            "curve": "u^2=P_6(t) with the two points over infinity removed",
            "compact_genus": 2,
            "points_removed_at_infinity": 2,
            "rank_H1_compact": 4,
            "rank_H1_affine": 5,
            "reason": (
                "the puncture exact sequence adds rank |D|-1=1, and the lifts "
                "of the five adjacent branch arcs give the integral A5 chain basis"
            ),
            "intersection_matrix": intersection.tolist(),
            "intersection_rank": 4,
            "puncture_radical_generator": radical.tolist(),
            "five_direct_cycles_are_an_integral_affine_basis": True,
        },
        "base_cut_system": {
            "projection_rotation": "exp(-i*pi/7)",
            "projected_root_order_zero_based": order,
            "minimum_projected_adjacent_gap_lower": minimum_projection_gap,
            "adjacent_direct_pairs_zero_based": [list(value) for value in adjacent_pairs],
            "direct_cut_diagnostics": diagnostics,
        },
        "integer_coordinate_isolation": {
            "real_embedding_row_convention": (
                "rows 0..4 are real period coordinates; rows 5..9 are imaginary"
            ),
            "selected_square_rows_zero_based": list(selected_rows),
            "selected_midpoint_determinant_absolute": abs(
                float(np.linalg.det(real_matrix[list(selected_rows), :]))
            ),
            "verified_interval_solve": True,
            "coordinate_intervals": coefficient_rows,
            "unique_integer_coordinates": integer_coefficients,
            "all_coordinates_isolate_exactly_one_integer": True,
        },
        "reanchor": {
            "transported_lift_physical_radius_upper": transported_radius,
            "direct_lift_maximum_component_radius_upper": direct_radius,
            "radius_reduction_factor": transported_radius / direct_radius,
            "overlap_by_period_coordinate": overlap,
            "transport_direct_difference_uppers": differences,
            "selected_direct_period_balls": [
                base.validated.encoded_acb(value) for value in selected_balls
            ],
        },
        "authority": {
            "reverse_initial_checkpoint": authority(arguments.initial_checkpoint),
            "selected_main_replay_interval": authority(arguments.canonical_main),
            "direct_cut_period_engine": authority(Path(base.handle.__file__).resolve()),
            "cutoff_root_engine": authority(Path(base.pilot.__file__).resolve()),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "compact_Sp4Z_class_alone_used_as_full_affine_source": False,
            "puncture_at_infinity_coordinate_retained": True,
            "selected_cycle_integrality_consumed": True,
            "integer_coordinates_selected_by_verified_interval_solve": True,
            "all_five_affine_period_coordinates_recomputed": True,
            "smooth_base_affine_reanchor_closed": True,
            "target_main_Hessian_interval_closed": False,
            "full_SM_closure_proved": False,
        },
    }
    base.dump(arguments.output, certificate)

    reanchored = copy.deepcopy(checkpoint)
    reanchored["center"][:5] = [
        base.validated.encoded_acb(
            base.validated.SelectedQ79IntervalSystem.midpoint_acb(value)
        )
        for value in selected_balls
    ]
    identity = acb_mat(5, 5)
    for index in range(5):
        identity[index, index] = acb(1)
    reanchored["lift_fundamental"] = base.validated.encoded_matrix(identity)
    reanchored["coordinate_radii"] = [
        str(value.rad().upper()) for value in selected_balls
    ]
    reanchored["affine_chain_basis_reanchor"] = {
        "certificate": authority(arguments.output),
        "same_position_outputs_and_output_radii_retained": True,
        "five_coordinate_lift_replaced_by_selected_affine_basis_enclosure": True,
    }
    base.dump(arguments.reanchored_checkpoint, reanchored)

    note = f"""# MTT q79 Height-Four d{arguments.index:03d} Affine-Chain Basis Reanchor (A380AB) v1

The smooth fiber is the affine genus-two curve `u^2=P_6(t)` with its two
points over infinity removed.  Its integral first homology has rank five, not
four: compact `H_1` contributes four coordinates and the puncture exact
sequence contributes one.  The five lifted adjacent branch arcs in projected
order `{order}` form the integral affine `A5` chain basis.  Its antisymmetric
intersection matrix has rank four and radical generator `(1,0,1,0,1)`.

Arb recomputes all five direct period columns and solves the real rows
`{list(selected_rows)}` against the independently transported terminal affine
source.  The five coefficient intervals each isolate one and only one integer,
giving

```
{integer_coefficients}
```

in the oriented direct-cut basis.  This supplies the puncture coordinate that
compact `Sp(4,Z)` monodromy cannot see.  Re-evaluating that exact integral
cycle reduces the five-period lift radius from `{transported_radius:.17g}` to
`{direct_radius:.17g}`, a factor `{transported_radius / direct_radius:.17g}`.
No observed Standard Model value enters the selection.

This closes the smooth-base affine source and reanchor.  It does not by itself
close the subsequent 72-row Hessian transport or the final interval-Newton
chart.
"""
    arguments.note.parent.mkdir(parents=True, exist_ok=True)
    arguments.note.write_text(note, encoding="utf-8")

    print(f"wrote {base.relative(arguments.output)}")
    print(f"wrote {base.relative(arguments.reanchored_checkpoint)}")
    print(f"wrote {base.relative(arguments.note)}")
    print(
        json.dumps(
            {
                "projected_order": order,
                "adjacent_pairs": adjacent_pairs,
                "selected_rows": selected_rows,
                "integer_coefficients": integer_coefficients,
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
