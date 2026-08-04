from __future__ import annotations

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
A397F = VALIDATED / "far_residue" / "d057.tail_frobenius.a397f.json"
A397 = VALIDATED / "far_residue" / "d057.full.a397.json"
A405 = VALIDATED / "n3.junction_operator_sweep.a405.json"
A409T = VALIDATED / "n3.junction_reverse_composition.a409t.json"
A409O = VALIDATED / "ol" / "d057.a409o.json"
A409O_CHECKPOINT = VALIDATED / "ol" / "d057.a409o.ckpt.json"
A411 = VALIDATED / "jop" / "trunk.a411.json"
A413 = VALIDATED / "ol" / "all76.a413.json"
OUTPUT = VALIDATED / "ol" / "d057.a412.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79D057FullJunctionPathComposition_A412_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def authority(path: Path) -> dict[str, str]:
    return {"path": str(path.relative_to(ROOT)).replace("\\", "/"), "sha256": sha256(path)}


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


def affine_component_radius(center: acb_mat, generator: acb_mat, row: int) -> float:
    generator_radius = sum(
        (abs(generator[row, column]) for column in range(generator.ncols())), arb(0)
    )
    return validated.radius_upper(center[row, 0]) + validated.upper(generator_radius)


def block_reverse(period: acb_mat, residue: acb_mat, residue_row: int) -> acb_mat:
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


def block_forward(period: acb_mat, residue: acb_mat, residue_row: int) -> acb_mat:
    result = acb_mat(6, 6)
    for row in range(5):
        for col in range(5):
            result[row, col] = period[row, col]
    for col in range(5):
        result[5, col] = -residue[residue_row, col]
    result[5, 5] = acb(1)
    return result


def canonical_disk(row: dict) -> tuple[complex, float]:
    return complex_value(row["full_interval_center"]), float(row["full_interval_radius_upper"])


def main() -> int:
    ctx.dps = 120
    outer = load(A409O)
    checkpoint = load(A409O_CHECKPOINT)
    tail = load(A397F)
    canonical = load(A397)
    sweep = load(A405)
    reverse_theorem = load(A409T)
    trunk = load(A411)
    source_manifest = load(A413)
    if outer.get("artifact") != "A409O" or not outer["strict_scope"]["outer_main_leg_to_common_entry_closed"]:
        raise AssertionError("A412 requires the certified A409O outer leg")
    if tail.get("artifact") != "A397F" or canonical.get("artifact") != "A397":
        raise AssertionError("A412 requires A397F and A397")
    if sweep.get("artifact") != "A405" or trunk.get("artifact") != "A411":
        raise AssertionError("A412 requires A405 and A411")
    if reverse_theorem.get("artifact") != "A409T":
        raise AssertionError("A412 requires the A409T reverse composition theorem")
    if (
        reverse_theorem["theorem"].get("selected_physical_residue_sign_bridge") != "r_phys=-q"
        or reverse_theorem["theorem"].get("reverse_block_operator")
        != "(T_e^(r))^{-1}=[[U_e^{-1},0],[+V_e U_e^{-1},I_8]]"
    ):
        raise AssertionError("A412 requires the A409T physical-residue sign bridge")
    contract = next(
        row for row in source_manifest["target_rows"]
        if int(row["distinguished_index"]) == 57
    )
    if (
        int(contract["A130_raw_chain_coefficient"]) != 4
        or int(contract["canonical_cycle_to_floating_orientation_sign"]) != 1
        or int(contract["endpoint_floating_chain_coefficient"])
        != int(outer["selected_target"]["signed_chain_coefficient"])
    ):
        raise AssertionError("A412 d057 A413 coefficient reconciliation changed")
    if outer["authority"]["completed_correlated_row_checkpoint"]["sha256"] != sha256(A409O_CHECKPOINT):
        raise AssertionError("A412 A409O checkpoint authority is stale")
    if outer["authority"]["A404_common_junction_manifest"]["sha256"] != sweep["authority"]["A404_manifest"]["sha256"]:
        raise AssertionError("A412 outer leg and junction sweep use different A404 manifests")
    if int(outer["selected_target"]["distinguished_index"]) != 57:
        raise AssertionError("A412 outer target changed")
    if outer["selected_target"]["line_chart"] != "y":
        raise AssertionError("A412 d057 unexpectedly requires an A410 transition")

    operator = next(
        row for row in sweep["operators_at_77_entries"] if row["entry"]["label"] == "d057"
    )
    if int(operator["entry_index_zero_based"]) != int(outer["A404_entry"]["entry_index_zero_based"]):
        raise AssertionError("A412 A405 entry differs from A409O")
    entry_period = interval_matrix(operator["period_transport_5_by_5"])
    entry_residue = interval_matrix(operator["integrated_residue_operator_8_by_5"])
    trunk_period = interval_matrix(trunk["period_transport_5_by_5"])
    trunk_residue = interval_matrix(trunk["integrated_residue_operator_8_by_5"])
    if validated.lower(abs(entry_period.det())) <= 0.0 or validated.lower(abs(trunk_period.det())) <= 0.0:
        raise AssertionError("A412 encountered a singular period operator")

    orientation = int(outer["selected_target"]["orientation_sign"])
    coefficient = int(outer["selected_target"]["signed_chain_coefficient"])
    tail_rows = tail["all_eight_endpoint_tails"]["rows"]
    canonical_rows = canonical["residue_rows"]
    if len(checkpoint["centers"]) != 8 or len(checkpoint["frames"]) != 8:
        raise AssertionError("A412 outer checkpoint lost an affine row")

    rows = []
    minimum_overlap_margin = math.inf
    maximum_base_radius = 0.0
    maximum_center_difference = 0.0
    for residue_row in range(8):
        raw_center = [validated.decoded_acb(value) for value in checkpoint["centers"][residue_row]]
        frame = generic.decoded_frame(checkpoint["frames"][residue_row])
        raw_generator = frame.physical_generator_matrix()
        selected_center = [orientation * value for value in raw_center[:5]] + [
            -orientation * raw_center[5]
        ]
        selected_generator = acb_mat(6, 6)
        for row in range(6):
            sign = orientation if row < 5 else -orientation
            for col in range(6):
                selected_generator[row, col] = sign * raw_generator[row, col]
        selected_center[5] += orientation * validated.interval_from_bounds(
            tail_rows[residue_row]["interval_bounds"]
        )

        reverse = block_reverse(entry_period, entry_residue, residue_row)
        hub_center = reverse * column(selected_center)
        hub_generator = reverse * selected_generator
        forward = block_forward(trunk_period, trunk_residue, residue_row)
        base_center = forward * hub_center
        base_generator = forward * hub_generator
        base_radius = affine_component_radius(base_center, base_generator, 5)
        base_midpoint = validated.midpoint(base_center[5, 0])
        expected_center, expected_radius = canonical_disk(canonical_rows[residue_row])
        difference = abs(base_midpoint - expected_center)
        margin = base_radius + expected_radius - difference
        if margin < 0.0:
            raise AssertionError(
                f"A412 row {residue_row} misses canonical A397 by {-margin:.6e}"
            )
        minimum_overlap_margin = min(minimum_overlap_margin, margin)
        maximum_base_radius = max(maximum_base_radius, base_radius)
        maximum_center_difference = max(maximum_center_difference, difference)
        rows.append(
            {
                "residue_index_zero_based": residue_row,
                "hub_affine_center": [encoded_ball(hub_center[row, 0]) for row in range(6)],
                "hub_affine_generator_6_by_6": encoded_matrix(hub_generator),
                "base_affine_center": [encoded_ball(base_center[row, 0]) for row in range(6)],
                "base_affine_generator_6_by_6": encoded_matrix(base_generator),
                "base_residue_total_radius_upper": base_radius,
                "canonical_A397_center": canonical_rows[residue_row]["full_interval_center"],
                "canonical_A397_radius_upper": expected_radius,
                "base_to_canonical_center_difference": difference,
                "overlap_margin": margin,
                "canonical_A397_overlap_certified": True,
                "selected_chain_contribution_center": encoded_ball(
                    coefficient * base_center[5, 0]
                ),
                "selected_chain_contribution_radius_upper": abs(coefficient) * base_radius,
            }
        )

    payload = {
        "schema": "MTTQ79D057FullJunctionPathComposition.v1",
        "status": "D057_FULL_ALTERNATE_JUNCTION_PATH_COMPOSITION_CERTIFIED",
        "artifact": "A412",
        "selected_target": outer["selected_target"],
        "composition": {
            "line_chart": "y",
            "A410_transition_used": False,
            "ordered_segments": [
                "A397F node-to-far-cut Frobenius tail",
                "A409O far-cut-to-A404-entry affine outer leg",
                "A409T/A405 reverse entry-to-common-hub block",
                "A411 common-hub-to-canonical-base terminal block",
            ],
            "residue_sign_bridge": "r_phys=-q",
            "reverse_rule": "(p_e,r_e)->(U_e^-1 p_e,r_e+V_e U_e^-1 p_e)",
            "forward_trunk_rule": "(p_h,r_h)->(U_0 p_h,r_h-V_0 p_h)",
        },
        "residue_rows": rows,
        "summary": {
            "certified_residue_rows": 8,
            "maximum_base_residue_radius_upper": maximum_base_radius,
            "maximum_base_to_A397_center_difference": maximum_center_difference,
            "minimum_A397_overlap_margin": minimum_overlap_margin,
            "all_eight_canonical_A397_overlaps_certified": True,
        },
        "authority": {
            "A397F_local_tail": authority(A397F),
            "A397_canonical_full_residue": authority(A397),
            "A405_entry_operators": authority(A405),
            "A409T_reverse_composition_theorem": authority(A409T),
            "A409O_outer_leg": authority(A409O),
            "A409O_correlated_checkpoint": authority(A409O_CHECKPOINT),
            "A411_terminal_trunk": authority(A411),
            "A413_source_and_orientation_manifest": authority(A413),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "matching_A397F_tail_attached": True,
            "outer_checkpoint_affine_generators_transformed": True,
            "A405_reverse_entry_operator_applied": True,
            "A411_terminal_trunk_applied": True,
            "A413_coefficient_orientation_reconciliation_consumed": True,
            "single_d057_alternate_path_composition_closed": True,
            "independent_canonical_A397_crosscheck_closed": True,
            "A405_operator_coefficient_cross_correlations_retained": False,
            "all_76_outer_thimble_paths_closed": False,
            "integer_chain_combination_at_hub_closed": False,
            "full_correlation_preserving_path_execution_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "generalize the A412 composition to all 76 thimble entries, inserting "
            "A410 y-from-z transitions for the 40 native-z targets"
        ),
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    NOTE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(
        "# MTT q79 d057 Full Junction Path Composition (A412) v1\n\n"
        "A412 composes the independently certified d057 Frobenius tail, outer "
        "affine leg, reverse A405 entry operator, and A411 terminal trunk. The "
        "outer checkpoint generators are transformed through both block maps.\n\n"
        f"All eight resulting base residue disks overlap A397; the minimum overlap "
        f"margin is `{minimum_overlap_margin:.12g}` and the maximum resulting radius "
        f"is `{maximum_base_radius:.12g}`. This closes one alternate-path pilot, not "
        "the 76-term hub sum, Newton inclusion, covariant zero, or full SM closure.\n",
        encoding="utf-8",
    )
    print(f"wrote {OUTPUT.relative_to(ROOT)}")
    print(f"wrote {NOTE.relative_to(ROOT)}")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
