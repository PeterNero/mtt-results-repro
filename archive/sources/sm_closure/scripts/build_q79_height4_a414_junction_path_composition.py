from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

from flint import acb, acb_mat, arb, ctx

import certify_q79_height4_target_full_residue_interval as generic
import certify_q79_selected_side_base_lift_interval as serializer
import certify_q79_selected_side_beta_defect_transport as validated


ROOT = Path(__file__).resolve().parents[1]
VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
A405 = VALIDATED / "n3.junction_operator_sweep.a405.json"
A409T = VALIDATED / "n3.junction_reverse_composition.a409t.json"
A410 = VALIDATED / "pt" / "a410.json"
A411 = VALIDATED / "jop" / "trunk.a411.json"
A413 = VALIDATED / "ol" / "all76.a413.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def authority(path: Path) -> dict[str, str]:
    return {"path": str(path.relative_to(ROOT)).replace("\\", "/"), "sha256": sha256(path)}


def resolve(path: str) -> Path:
    return ROOT / Path(path)


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def interval_entry(value: dict) -> acb:
    center = complex_value(value["center"])
    radius = float(value["component_radius_upper"])
    serialization = max(math.ulp(center.real), math.ulp(center.imag), 1.0e-300)
    outward = math.nextafter(radius + serialization, math.inf)
    return acb(
        arb(format(center.real, ".17g"), format(outward, ".17g")),
        arb(format(center.imag, ".17g"), format(outward, ".17g")),
    )


def interval_matrix(rows: list[list[dict]]) -> acb_mat:
    return acb_mat([[interval_entry(value) for value in row] for row in rows])


def bounds_matrix(rows: list[list[dict]]) -> acb_mat:
    return acb_mat(
        [[validated.interval_from_bounds(value["interval_bounds"]) for value in row] for row in rows]
    )


def column(values: list[acb]) -> acb_mat:
    result = acb_mat(len(values), 1)
    for row, value in enumerate(values):
        result[row, 0] = value
    return result


def encoded_ball(value: acb) -> dict:
    bounds = serializer.complex_interval(value)
    persisted = validated.interval_from_bounds(bounds)
    center = validated.midpoint(persisted)
    return {
        "interval_bounds": bounds,
        "interval_center": {
            "real": format(center.real, ".17g"),
            "imaginary": format(center.imag, ".17g"),
        },
        "interval_radius_upper": validated.radius_upper(persisted),
    }


def encoded_matrix(matrix: acb_mat) -> list[list[dict]]:
    return [
        [encoded_ball(matrix[row, col]) for col in range(matrix.ncols())]
        for row in range(matrix.nrows())
    ]


def component_radius(center: acb_mat, generator: acb_mat, row: int) -> float:
    generator_radius = sum(
        (abs(generator[row, col]) for col in range(generator.ncols())), arb(0)
    )
    return validated.radius_upper(center[row, 0]) + validated.upper(generator_radius)


def chart_block(transition: acb_mat | None) -> acb_mat:
    result = acb_mat(6, 6)
    if transition is None:
        for row in range(5):
            result[row, row] = acb(1)
    else:
        for row in range(5):
            for col in range(5):
                result[row, col] = transition[row, col]
    result[5, 5] = acb(1)
    return result


def reverse_block(period: acb_mat, residue: acb_mat, residue_row: int) -> acb_mat:
    inverse = period.inv()
    coupling = residue * inverse
    result = acb_mat(6, 6)
    for row in range(5):
        for col in range(5):
            result[row, col] = inverse[row, col]
    for col in range(5):
        result[5, col] = coupling[residue_row, col]
    result[5, 5] = acb(1)
    return result


def forward_block(period: acb_mat, residue: acb_mat, residue_row: int) -> acb_mat:
    result = acb_mat(6, 6)
    for row in range(5):
        for col in range(5):
            result[row, col] = period[row, col]
    for col in range(5):
        result[5, col] = -residue[residue_row, col]
    result[5, 5] = acb(1)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--index", type=int, required=True)
    arguments = parser.parse_args()
    ctx.dps = 120
    outer_path = VALIDATED / "ol" / f"d{arguments.index:03d}.a414.json"
    checkpoint_path = VALIDATED / "ol" / f"d{arguments.index:03d}.a414.ckpt.json"
    output = VALIDATED / "ol" / f"d{arguments.index:03d}.a415.json"
    note = ROOT / "proof_corpus" / f"MTT_q79D{arguments.index:03d}FullJunctionComposition_A415_v1.md"
    outer = load(outer_path)
    checkpoint = load(checkpoint_path)
    source_manifest = load(A413)
    sweep = load(A405)
    reverse_theorem = load(A409T)
    transitions = load(A410)
    trunk = load(A411)
    if outer.get("artifact") != "A414" or not outer["strict_scope"]["outer_main_leg_to_common_entry_closed"]:
        raise AssertionError("A415 requires a certified A414 outer leg")
    if reverse_theorem.get("artifact") != "A409T":
        raise AssertionError("A415 requires A409T")
    if (
        reverse_theorem["theorem"].get("selected_physical_residue_sign_bridge") != "r_phys=-q"
        or reverse_theorem["theorem"].get("reverse_block_operator")
        != "(T_e^(r))^{-1}=[[U_e^{-1},0],[+V_e U_e^{-1},I_8]]"
    ):
        raise AssertionError("A415 requires the A409T physical-residue sign bridge")
    contract = next(
        row for row in source_manifest["target_rows"]
        if int(row["distinguished_index"]) == arguments.index
    )
    tail_path = resolve(contract["authority"]["canonical_tail"]["path"])
    full_path = resolve(contract["authority"]["canonical_full"]["path"])
    if contract["authority"]["canonical_tail"]["sha256"] != sha256(tail_path):
        raise AssertionError("A415 canonical tail authority is stale")
    if contract["authority"]["canonical_full"]["sha256"] != sha256(full_path):
        raise AssertionError("A415 canonical full authority is stale")
    if outer["authority"]["completed_correlated_row_checkpoint"]["sha256"] != sha256(checkpoint_path):
        raise AssertionError("A415 A414 checkpoint authority is stale")
    tail = load(tail_path)
    canonical = load(full_path)
    operator = next(
        row for row in sweep["operators_at_77_entries"]
        if row["entry"].get("kind") == "selected_thimble_entry"
        and int(row["entry"]["distinguished_index"]) == arguments.index
    )
    entry_period = interval_matrix(operator["period_transport_5_by_5"])
    entry_residue = interval_matrix(operator["integrated_residue_operator_8_by_5"])
    trunk_period = interval_matrix(trunk["period_transport_5_by_5"])
    trunk_residue = interval_matrix(trunk["integrated_residue_operator_8_by_5"])
    transition_row = next(
        (
            row for row in transitions["native_z_entry_transitions"]
            if int(row["distinguished_index"]) == arguments.index
        ),
        None,
    )
    if (contract["line_chart"] == "z") != (transition_row is not None):
        raise AssertionError("A415 A410 transition assignment changed")
    y_from_native = (
        bounds_matrix(transition_row["y_periods_from_z_periods_5_by_5"])
        if transition_row is not None
        else None
    )
    chart = chart_block(y_from_native)
    transport_orientation = int(outer["selected_target"]["transport_orientation_sign"])
    endpoint_coefficient = int(contract["endpoint_floating_chain_coefficient"])
    tail_intervals = tail["all_eight_endpoint_tails"]["intervals"]
    canonical_rows = canonical["residue_rows"]
    rows = []
    radii = []
    differences = []
    margins = []
    for residue_row in range(8):
        raw_center = [validated.decoded_acb(value) for value in checkpoint["centers"][residue_row]]
        frame = generic.decoded_frame(checkpoint["frames"][residue_row])
        raw_generator = frame.physical_generator_matrix()
        selected_center = [transport_orientation * value for value in raw_center[:5]] + [
            -transport_orientation * raw_center[5]
        ]
        selected_generator = acb_mat(6, 6)
        for row in range(6):
            sign = transport_orientation if row < 5 else -transport_orientation
            for col in range(6):
                selected_generator[row, col] = sign * raw_generator[row, col]
        selected_center[5] += transport_orientation * validated.interval_from_bounds(
            tail_intervals[residue_row]
        )
        common_entry_center = chart * column(selected_center)
        common_entry_generator = chart * selected_generator
        reverse = reverse_block(entry_period, entry_residue, residue_row)
        hub_center = reverse * common_entry_center
        hub_generator = reverse * common_entry_generator
        forward = forward_block(trunk_period, trunk_residue, residue_row)
        base_center = forward * hub_center
        base_generator = forward * hub_generator
        radius = component_radius(base_center, base_generator, 5)
        center = validated.midpoint(base_center[5, 0])
        expected = complex_value(canonical_rows[residue_row]["full_interval_center"])
        expected_radius = float(canonical_rows[residue_row]["full_interval_radius_upper"])
        difference = abs(center - expected)
        margin = radius + expected_radius - difference
        if margin < 0.0:
            raise AssertionError(
                f"A415 d{arguments.index:03d} row {residue_row} misses canonical by {-margin:.6e}"
            )
        component_radii = [component_radius(base_center, base_generator, row) for row in range(6)]
        rows.append(
            {
                "residue_index_zero_based": residue_row,
                "common_y_entry_center": [encoded_ball(common_entry_center[row, 0]) for row in range(6)],
                "common_y_entry_affine_generator_6_by_6": encoded_matrix(
                    common_entry_generator
                ),
                "hub_center": [encoded_ball(hub_center[row, 0]) for row in range(6)],
                "hub_affine_generator_6_by_6": encoded_matrix(hub_generator),
                "base_center": [encoded_ball(base_center[row, 0]) for row in range(6)],
                "base_affine_generator_6_by_6": encoded_matrix(base_generator),
                "base_component_total_radius_uppers": component_radii,
                "base_residue_total_radius_upper": radius,
                "canonical_full_residue_center": canonical_rows[residue_row]["full_interval_center"],
                "canonical_full_residue_radius_upper": expected_radius,
                "base_to_canonical_center_difference": difference,
                "overlap_margin": margin,
                "canonical_overlap_certified": True,
                "selected_chain_contribution_center": encoded_ball(endpoint_coefficient * base_center[5, 0]),
                "selected_chain_contribution_radius_upper": abs(endpoint_coefficient) * radius,
            }
        )
        radii.append(radius)
        differences.append(difference)
        margins.append(margin)
    payload = {
        "schema": "MTTQ79HeightFourA414JunctionPathComposition.v1",
        "status": "ONE_A414_FULL_ALTERNATE_JUNCTION_PATH_COMPOSITION_CERTIFIED",
        "artifact": "A415",
        "selected_target": outer["selected_target"],
        "composition": {
            "residue_sign_bridge": "r_phys=-q",
            "native_line_chart": contract["line_chart"],
            "A410_y_from_z_transition_applied": transition_row is not None,
            "ordered_segments": [
                "canonical node-to-cutoff local tail",
                "A414 cutoff-to-A404-entry affine outer leg",
                "A410 native-z-to-common-y transition when required",
                "A409T/A405 reverse entry-to-hub block",
                "A411 hub-to-canonical-base terminal block",
            ],
        },
        "residue_rows": rows,
        "summary": {
            "certified_residue_rows": 8,
            "maximum_base_residue_radius_upper": max(radii),
            "maximum_base_to_canonical_center_difference": max(differences),
            "minimum_canonical_overlap_margin": min(margins),
            "all_eight_canonical_overlaps_certified": True,
        },
        "authority": {
            "A405_entry_operators": authority(A405),
            "A409T_reverse_composition_theorem": authority(A409T),
            "A410_native_z_transitions": authority(A410),
            "A411_terminal_trunk": authority(A411),
            "A413_source_manifest": authority(A413),
            "A414_outer_leg": authority(outer_path),
            "A414_correlated_checkpoint": authority(checkpoint_path),
            "canonical_local_tail": authority(tail_path),
            "canonical_full_residue": authority(full_path),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "matching_local_tail_attached": True,
            "native_chart_to_common_y_reconciled": True,
            "outer_checkpoint_affine_generators_transformed": True,
            "entry_hub_and_base_affine_generators_serialized": True,
            "A405_reverse_entry_operator_applied": True,
            "A411_terminal_trunk_applied": True,
            "single_target_alternate_path_composition_closed": True,
            "independent_canonical_full_residue_crosscheck_closed": True,
            "all_76_outer_thimble_paths_closed": False,
            "integer_chain_combination_at_hub_closed": False,
            "full_correlation_preserving_path_execution_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "execute and audit A414/A415 for the remaining A413 targets, then sum "
            "their orientation-reconciled hub states with the handle and PL wall"
        ),
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    note.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    note.write_text(
        f"# MTT q79 d{arguments.index:03d} Full Junction Composition (A415) v1\n\n"
        f"A415 composes the native-{contract['line_chart']} cutoff source and local "
        "tail through the common-y junction and terminal trunk. "
        f"A410 was {'applied' if transition_row is not None else 'not required'}.\n\n"
        f"All eight base residues overlap the canonical full certificate; minimum "
        f"margin `{min(margins):.12g}`, maximum radius `{max(radii):.12g}`. The "
        "remaining targets, hub sum, Newton inclusion, and covariant zero remain open.\n",
        encoding="utf-8",
    )
    print(f"wrote {output.relative_to(ROOT)}")
    print(f"wrote {note.relative_to(ROOT)}")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
