from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
from flint import acb, ctx

import certify_q79_selected_alignment_E32_handle_combination_interval as handle
import certify_q79_selected_side_beta_defect_transport as validated
from build_selected_q79_E32_weighted_71_and_carrier_decision import (
    coordinate_zero_exclusion,
    serialized_disk,
)


ROOT = Path(__file__).resolve().parents[1]
PERIOD_DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
)
A208 = PERIOD_DIRECTORY / "selected_alignment_height4_survivor_queue_and_E32_priority.packet.json"
A209 = PERIOD_DIRECTORY / "selected_alignment_E32_primitive_handle_basis.intervals.packet.json"
A207 = PERIOD_DIRECTORY / "selected_alignment_E32_weighted_71_thimble_and_frozen_carrier_decision.packet.json"
ORIENTATION = PERIOD_DIRECTORY / "selected_alignment_thimble_orientation_synchronization.packet.json"
PERIODS = PERIOD_DIRECTORY / "selected_alignment_full_integral_basis_period_table.packet.json"
BETA = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
    / "pgl3_selected_side_beta.local_lower.order40_step003.interval.packet.json"
)
PACKET = PERIOD_DIRECTORY / "selected_alignment_height4_survivor_E32_decisions.packet.json"
CANDIDATE = ROOT / "candidate_data" / "selected_q79heightfoursurvivore32decisions.candidate.json"
CERTIFICATE = ROOT / "certificates" / "selected_q79heightfoursurvivore32decisions.certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79HeightFourSurvivorE32Decisions_A210_v1.md"
E32_INDEX = 5


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def exact_point(center: dict[str, str]) -> acb:
    return acb(center["real"], center["imaginary"])


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def full_packet_path(index: int) -> Path:
    rows = list(PERIOD_DIRECTORY.glob(f"d{index:03d}_*.E32_full.interval.packet.json"))
    if len(rows) != 1:
        raise AssertionError(f"d{index:03d}: expected one full interval, found {len(rows)}")
    return rows[0]


def main() -> int:
    ctx.dps = 100
    a208 = load(A208)
    a209 = load(A209)
    a207 = load(A207)
    orientation = [int(value) for value in load(ORIENTATION)["column_signs"]]
    period_matrix = np.asarray(
        [
            [complex_value(value) for value in row]
            for row in load(PERIODS)["period_matrix_rows"]
        ],
        dtype=np.complex128,
    )
    if len(orientation) != 90 or period_matrix.shape != (8, 92):
        raise AssertionError("A131 orientation or period dimensions changed")
    handle_by_id = {
        row["candidate_id"]: row
        for row in a209["height_four_candidate_handle_combinations"]
    }
    if set(handle_by_id) != {
        row["candidate_id"] for row in a208["height_four_candidates"]
    }:
        raise AssertionError("A208/A209 candidate identities differ")

    beta_endpoint = load(BETA)["endpoint"]
    beta_center = beta_endpoint["beta_center"][E32_INDEX]
    beta_radius = float(beta_endpoint["uniform_component_radius_upper"])
    beta_serialization = float(beta_endpoint["center_serialization_radius_upper"])
    beta_ball, beta_roundtrip = serialized_disk(
        beta_center, beta_radius + beta_serialization
    )

    authority_paths = {A208, A209, A207, ORIENTATION, PERIODS, BETA, Path(__file__)}
    required_indices = {
        int(chain_row["distinguished_index"])
        for candidate_row in a208["height_four_candidates"]
        for chain_row in candidate_row["primitive_thimble_chain"]
    }
    unused_indices = sorted(set(range(1, 91)) - required_indices)
    if len(required_indices) != 86 or unused_indices != [6, 7, 8, 9]:
        raise AssertionError("A208 fixed-grid thimble union changed")
    decision_rows = []
    for candidate_row in a208["height_four_candidates"]:
        candidate_id = candidate_row["candidate_id"]
        thimble_ball = acb(0)
        summands = []
        for chain_row in candidate_row["primitive_thimble_chain"]:
            index = int(chain_row["distinguished_index"])
            coefficient = int(chain_row["coefficient"])
            path = full_packet_path(index)
            authority_paths.add(path)
            packet = load(path)
            if not packet["scope"]["single_full_E32_thimble_interval_closed"]:
                raise AssertionError(f"d{index:03d} full interval gate is open")
            interval = validated.interval_from_bounds(
                packet["full_E32_thimble"]["interval"]
            )
            oriented_coefficient = coefficient * orientation[index - 1]
            thimble_ball += acb(oriented_coefficient) * interval
            summands.append(
                {
                    "distinguished_index": index,
                    "coefficient": coefficient,
                    "canonical_orientation_sign": orientation[index - 1],
                    "oriented_raw_interval_coefficient": oriented_coefficient,
                    "full_interval_path": relative(path),
                    "full_interval_sha256": sha256(path),
                    "full_interval_radius_upper": validated.radius_upper(interval),
                }
            )

        handle_row = handle_by_id[candidate_id]
        handle_ball = validated.interval_from_bounds(handle_row["E32_interval"])
        combined_period = thimble_ball + handle_ball
        ell = np.asarray(
            candidate_row["effective_coordinates_Z90"] + [0, 0], dtype=np.float64
        )
        expected_full = period_matrix[E32_INDEX] @ ell
        expected_handle = complex_value(handle_row["A131_floating_center"])
        expected_thimble = expected_full - expected_handle
        thimble_center_difference = abs(handle.midpoint(thimble_ball) - expected_thimble)
        combined_center_difference = abs(handle.midpoint(combined_period) - expected_full)
        if not thimble_ball.contains(acb(format(expected_thimble.real, ".17g"), format(expected_thimble.imag, ".17g"))):
            raise AssertionError("survivor thimble interval misses the A131 center")
        if not combined_period.contains(acb(format(expected_full.real, ".17g"), format(expected_full.imag, ".17g"))):
            raise AssertionError("survivor full interval misses the A131 center")

        residual = beta_ball - combined_period
        separation = coordinate_zero_exclusion(residual)
        zero_excluded = not residual.contains(acb(0)) and bool(separation["zero_excluded"])
        if candidate_row["A132_objective_rank"] == 1:
            rigorous_decision = "REJECTED_BY_A207_SHARPER_DIRECT_HANDLE_INTERVAL"
            if not a207["scope"]["frozen_height_four_carrier_rejected_by_E32_zero_exclusion"]:
                raise AssertionError("A207 direct rejection changed")
        else:
            rigorous_decision = (
                "REJECTED_BY_E32_ZERO_EXCLUSION"
                if zero_excluded
                else "NOT_SEPARATED_BY_CURRENT_E32_INTERVAL"
            )
        decision_rows.append(
            {
                "candidate_id": candidate_id,
                "A132_objective_rank": candidate_row["A132_objective_rank"],
                "A207_prior_status": candidate_row["A207_decision"],
                "primitive_thimble_support": candidate_row["primitive_thimble_support"],
                "primitive_thimble_l1_norm": candidate_row["primitive_thimble_l1_norm"],
                "summands": summands,
                "weighted_thimble_interval": handle.complex_interval(thimble_ball),
                "weighted_thimble_center": handle.complex_pair(handle.midpoint(thimble_ball)),
                "weighted_thimble_radius_upper": validated.radius_upper(thimble_ball),
                "weighted_thimble_A131_center_difference": thimble_center_difference,
                "handle_interval": handle_row["E32_interval"],
                "handle_radius_upper": handle_row["E32_interval_radius_upper"],
                "full_period_interval": handle.complex_interval(combined_period),
                "full_period_center": handle.complex_pair(handle.midpoint(combined_period)),
                "full_period_radius_upper": validated.radius_upper(combined_period),
                "full_period_A131_center_difference": combined_center_difference,
                "residual_interval": handle.complex_interval(residual),
                "residual_center": handle.complex_pair(handle.midpoint(residual)),
                "residual_radius_upper": validated.radius_upper(residual),
                "coordinate_zero_exclusion": separation,
                "current_aggregate_zero_excluded": zero_excluded,
                "rigorous_decision": rigorous_decision,
            }
        )

    survivor_rows = decision_rows[1:]
    rejected_survivors = [
        row
        for row in survivor_rows
        if row["rigorous_decision"] == "REJECTED_BY_E32_ZERO_EXCLUSION"
    ]
    nonseparated_survivors = [
        row
        for row in survivor_rows
        if row["rigorous_decision"] == "NOT_SEPARATED_BY_CURRENT_E32_INTERVAL"
    ]
    packet = {
        "schema": "MTTQ79SelectedAlignmentHeightFourSurvivorE32Decisions.v1",
        "status": (
            "ALL_A132_FIXED_GRID_HEIGHT4_ROWS_REJECTED"
            if not nonseparated_survivors
            else "A132_FIXED_GRID_HEIGHT4_E32_DECISIONS_PARTIAL_SURVIVORS_REMAIN"
        ),
        "artifact": "A210",
        "authority": {
            "A208_survivor_queue": relative(A208),
            "A208_survivor_queue_sha256": sha256(A208),
            "A209_handle_basis": relative(A209),
            "A209_handle_basis_sha256": sha256(A209),
            "A207_direct_decision": relative(A207),
            "A207_direct_decision_sha256": sha256(A207),
            "orientation_packet": relative(ORIENTATION),
            "orientation_packet_sha256": sha256(ORIENTATION),
            "period_table": relative(PERIODS),
            "period_table_sha256": sha256(PERIODS),
            "refined_beta_packet": relative(BETA),
            "refined_beta_packet_sha256": sha256(BETA),
            "builder_source": relative(Path(__file__)),
            "builder_source_sha256": sha256(Path(__file__)),
            "all_interval_authority_sha256": {
                relative(path): sha256(path) for path in sorted(authority_paths)
            },
        },
        "refined_beta_E32": {
            "center": beta_center,
            "source_radius_upper": beta_radius,
            "source_serialization_radius_upper": beta_serialization,
            "roundtrip_serialization_radius_upper": beta_roundtrip,
            "inflated_radius_upper": validated.radius_upper(beta_ball),
        },
        "candidate_decisions": decision_rows,
        "decision_ledger": {
            "fixed_grid_height_four_rows": len(decision_rows),
            "required_primitive_thimble_union_support": len(required_indices),
            "unused_uncertified_primitive_thimble_indices": unused_indices,
            "previously_rejected_by_A207": 1,
            "newly_rejected_survivors": len(rejected_survivors),
            "current_E32_nonseparated_survivors": len(nonseparated_survivors),
            "nonseparated_candidate_ids": [
                row["candidate_id"] for row in nonseparated_survivors
            ],
            "all_A132_fixed_grid_height_four_rows_rejected": not nonseparated_survivors,
        },
        "scope": {
            "observed_SM_values_used": False,
            "all_86_fixed_grid_required_E32_thimble_intervals_available": True,
            "four_unused_primitive_thimble_intervals_not_required": True,
            "all_five_A132_fixed_grid_height_four_rows_aggregated": True,
            "A207_sharper_direct_decision_preserved": True,
            "E32_nonseparation_is_not_exact_membership": True,
            "global_height_four_completeness_over_Z90_proved": False,
            "covariant_PGL3_zero_and_Jacobian_solved": False,
        },
        "next_required_artifact": (
            "sharpen the handle/beta/thimble intervals or execute the full eight-row "
            "covariant interval-Newton gate for each E32-nonseparated survivor"
            if nonseparated_survivors
            else "record the A132 finite-grid height-four no-go and begin an authorized broader CVP search"
        ),
    }
    dump(PACKET, packet)

    table = []
    for row in decision_rows:
        table.append(
            "| {rank} | `{candidate}` | {center} | {radius:.9g} | {decision} |".format(
                rank=row["A132_objective_rank"],
                candidate=row["candidate_id"],
                center=row["residual_center"],
                radius=row["residual_radius_upper"],
                decision=row["rigorous_decision"],
            )
        )
    note = f"""# MTT Selected q79 Height-Four Survivor E32 Decisions A210 v1

## Result

A210 applies the A207 E32 interval logic to every height-four row retained by
A208. It combines canonically oriented raw-thimble intervals, the A209 primitive
handle combinations, and the same refined beta interval.

| A132 rank | candidate | residual center | radius | decision |
|---:|---|---|---:|---|
{chr(10).join(table)}

The ledger now has one preserved A207 rejection, {len(rejected_survivors)} new
survivor rejection(s), and {len(nonseparated_survivors)} E32-nonseparated
survivor(s). Nonseparation means only that the current E32 interval contains
zero; it is not promoted to equality or to a covariant solution.

The result is complete for the five rows emitted by the finite A132 grid, not
for all of `Z^90`. No observed Standard Model value is used.
"""
    NOTE.write_text(note, encoding="utf-8")
    candidate = {
        "schema": "MTTSelectedQ79HeightFourSurvivorE32Decisions.v1",
        "status": packet["status"],
        "artifact": "A210",
        "packet": relative(PACKET),
        "packet_sha256": sha256(PACKET),
        "note": relative(NOTE),
        "note_sha256": sha256(NOTE),
        "what_closes": {
            "all_five_fixed_grid_height_four_E32_aggregates": True,
            "new_survivor_zero_exclusions": len(rejected_survivors),
        },
        "what_remains_open": {
            "E32_nonseparated_survivors": len(nonseparated_survivors),
            "global_height_four_completeness_over_Z90": True,
            "covariant_PGL3_zero_and_Jacobian": True,
        },
        "closure_claimed": False,
        "observed_SM_values_used": False,
        "next_required_artifact": packet["next_required_artifact"],
    }
    dump(CANDIDATE, candidate)
    certificate = {
        "schema": "MTTCertificate.v1",
        "certificate": "MTTSelectedQ79HeightFourSurvivorE32Decisions",
        "candidate_path": relative(CANDIDATE),
        "candidate_sha256": sha256(CANDIDATE),
        "status": candidate["status"],
        "closure_claimed": False,
        "observed_SM_values_used": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }
    dump(CERTIFICATE, certificate)
    print(f"wrote {relative(PACKET)}")
    print(f"wrote {relative(CANDIDATE)}")
    print(f"wrote {relative(CERTIFICATE)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(packet["decision_ledger"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
