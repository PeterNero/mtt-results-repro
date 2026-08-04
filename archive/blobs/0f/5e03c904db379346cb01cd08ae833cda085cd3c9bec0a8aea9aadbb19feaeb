from __future__ import annotations

import hashlib
import json
from pathlib import Path

from flint import acb, ctx

import certify_q79_selected_alignment_E32_handle_combination_interval as handle
import certify_q79_selected_alignment_E32_primitive_handle_basis_intervals as basis
import certify_q79_selected_alignment_E32_survivor_direct_handle_interval as direct
import certify_q79_selected_alignment_E32_survivor_refined_handle_interval as refined
import certify_q79_selected_side_beta_defect_transport as validated
from build_selected_q79_E32_weighted_71_and_carrier_decision import (
    coordinate_zero_exclusion,
    serialized_disk,
)


ROOT = basis.ROOT
PERIOD_DIRECTORY = basis.PERIOD_DIRECTORY
A208 = PERIOD_DIRECTORY / "selected_alignment_height4_survivor_queue_and_E32_priority.packet.json"
A209 = PERIOD_DIRECTORY / "selected_alignment_E32_primitive_handle_basis.intervals.packet.json"
A210 = PERIOD_DIRECTORY / "selected_alignment_height4_survivor_E32_decisions.packet.json"
OLD_BETA = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
    / "pgl3_selected_side_beta.local_lower.order40_step003.interval.packet.json"
)
NEW_BETA = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
    / "pgl3_selected_side_beta.local_lower.order44_step002.interval.packet.json"
)
PACKET = PERIOD_DIRECTORY / "selected_alignment_height4_refined_E32_decisions.packet.json"
CANDIDATE = ROOT / "candidate_data" / "selected_q79heightfourrefinede32decisions.candidate.json"
CERTIFICATE = ROOT / "certificates" / "selected_q79heightfourrefinede32decisions.certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79HeightFourRefinedE32Decisions_A211_v1.md"
E32_INDEX = 5
REFINED_HANDLE_ORDER = 44
REFINED_HANDLE_STEP = 0.005


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


def selected_beta() -> tuple[Path, dict, list[dict]]:
    candidates = []
    for path in (OLD_BETA, NEW_BETA):
        if not path.exists():
            continue
        packet = load(path)
        radius = float(packet["endpoint"]["uniform_component_radius_upper"])
        serialization = float(
            packet["endpoint"]["center_serialization_radius_upper"]
        )
        candidates.append(
            {
                "path": path,
                "packet": packet,
                "radius": radius,
                "total_component_radius": radius + serialization,
            }
        )
    if not candidates:
        raise FileNotFoundError("no selected-side beta interval packet exists")
    reference = candidates[0]
    reference_center = [
        complex_value(value)
        for value in reference["packet"]["endpoint"]["beta_center"]
    ]
    for row in candidates:
        center = [
            complex_value(value)
            for value in row["packet"]["endpoint"]["beta_center"]
        ]
        radius_sum = (
            reference["total_component_radius"] + row["total_component_radius"]
        )
        maximum_component_displacement = max(
            max(abs(left.real - right.real), abs(left.imag - right.imag))
            for left, right in zip(reference_center, center)
        )
        row["maximum_component_center_displacement_from_reference"] = (
            maximum_component_displacement
        )
        row["same_branch_component_boxes_overlap_reference"] = (
            maximum_component_displacement <= radius_sum
        )
        if not row["same_branch_component_boxes_overlap_reference"]:
            raise AssertionError("certified beta candidates do not enclose the same branch")
    winner = min(candidates, key=lambda row: row["radius"])
    inventory = [
        {
            "path": relative(row["path"]),
            "sha256": sha256(row["path"]),
            "uniform_component_radius_upper": row["radius"],
            "maximum_component_center_displacement_from_reference": row[
                "maximum_component_center_displacement_from_reference"
            ],
            "same_branch_component_boxes_overlap_reference": row[
                "same_branch_component_boxes_overlap_reference"
            ],
            "selected": row is winner,
        }
        for row in candidates
    ]
    return winner["path"], winner["packet"], inventory


def direct_ball(rank: int, handle_name: str, candidate_id: str) -> tuple[acb, Path]:
    path = direct.output_path(rank, handle_name, candidate_id)
    packet = load(path)
    if not packet["scope"]["candidate_specific_direct_handle_E32_interval_closed"]:
        raise AssertionError("direct survivor handle interval is open")
    return validated.interval_from_bounds(
        packet["direct_handle_interval"]["E32_interval"]
    ), path


def refined_ball(rank: int, candidate_id: str) -> tuple[acb, Path]:
    path = refined.output_path(
        rank,
        "B",
        candidate_id,
        REFINED_HANDLE_ORDER,
        REFINED_HANDLE_STEP,
    )
    packet = load(path)
    if not packet["scope"][
        "candidate_specific_refined_handle_E32_interval_closed"
    ]:
        raise AssertionError("refined survivor B-handle interval is open")
    return validated.interval_from_bounds(
        packet["refined_handle_interval"]["E32_interval"]
    ), path


def main() -> int:
    ctx.dps = 100
    a208 = load(A208)
    a209 = load(A209)
    a210 = load(A210)
    beta_path, beta_packet, beta_inventory = selected_beta()
    primitive = {
        row["label"]: validated.interval_from_bounds(row["E32_interval"])
        for row in a209["primitive_E32_handle_intervals"]
    }
    old_by_id = {row["candidate_id"]: row for row in a210["candidate_decisions"]}
    beta_endpoint = beta_packet["endpoint"]
    beta_center = beta_endpoint["beta_center"][E32_INDEX]
    beta_radius = float(beta_endpoint["uniform_component_radius_upper"])
    beta_serialization = float(beta_endpoint["center_serialization_radius_upper"])
    beta_ball, beta_roundtrip = serialized_disk(
        beta_center, beta_radius + beta_serialization
    )

    authority_paths = {A208, A209, A210, beta_path, Path(__file__)}
    rows = []
    for candidate in a208["height_four_candidates"][1:]:
        rank = int(candidate["A132_objective_rank"])
        candidate_id = candidate["candidate_id"]
        a_ball, a_path = direct_ball(rank, "A", candidate_id)
        authority_paths.add(a_path)
        if rank == 2:
            b_options = [
                {
                    "kind": "A209_PRIMITIVE_B_A1",
                    "ball": primitive["B:a1"],
                    "source": "A209 primitive B:a1 interval",
                    "path": None,
                }
            ]
            refined_path = refined.output_path(
                rank,
                "B",
                candidate_id,
                REFINED_HANDLE_ORDER,
                REFINED_HANDLE_STEP,
            )
            if refined_path.exists():
                candidate_ball, candidate_path = refined_ball(rank, candidate_id)
                authority_paths.add(candidate_path)
                b_options.append(
                    {
                        "kind": "HIGH_ORDER_CANDIDATE_DIRECT_B",
                        "ball": candidate_ball,
                        "source": relative(candidate_path),
                        "path": candidate_path,
                    }
                )
        elif rank == 3:
            b_ball, b_path = direct_ball(rank, "B", candidate_id)
            authority_paths.add(b_path)
            b_options = [
                {
                    "kind": "CANDIDATE_DIRECT_B",
                    "ball": b_ball,
                    "source": relative(b_path),
                    "path": b_path,
                }
            ]
        elif rank == 4:
            b_options = [
                {
                    "kind": "NEGATIVE_A209_PRIMITIVE_B_B2",
                    "ball": -primitive["B:b2"],
                    "source": "negative A209 primitive B:b2 interval",
                    "path": None,
                }
            ]
            refined_path = refined.output_path(
                rank,
                "B",
                candidate_id,
                REFINED_HANDLE_ORDER,
                REFINED_HANDLE_STEP,
            )
            if refined_path.exists():
                candidate_ball, candidate_path = refined_ball(rank, candidate_id)
                authority_paths.add(candidate_path)
                b_options.append(
                    {
                        "kind": "HIGH_ORDER_CANDIDATE_DIRECT_B",
                        "ball": candidate_ball,
                        "source": relative(candidate_path),
                        "path": candidate_path,
                    }
                )
        elif rank == 5:
            b_options = [
                {
                    "kind": "EXACT_ZERO_B_COMPONENT",
                    "ball": acb(0),
                    "source": "exact zero B component",
                    "path": None,
                }
            ]
        else:
            raise AssertionError("unexpected A208 survivor rank")
        b_winner = min(b_options, key=lambda row: validated.radius_upper(row["ball"]))
        b_ball = b_winner["ball"]
        b_source = b_winner["source"]
        b_inventory = [
            {
                "kind": option["kind"],
                "source": option["source"],
                "path": (
                    None if option["path"] is None else relative(option["path"])
                ),
                "sha256": (
                    None if option["path"] is None else sha256(option["path"])
                ),
                "radius_upper": validated.radius_upper(option["ball"]),
                "selected": option is b_winner,
            }
            for option in b_options
        ]
        handle_ball = a_ball + b_ball
        old = old_by_id[candidate_id]
        old_handle_center = complex_value(old["full_period_center"]) - complex_value(
            old["weighted_thimble_center"]
        )
        if not handle_ball.contains(
            acb(
                format(old_handle_center.real, ".17g"),
                format(old_handle_center.imag, ".17g"),
            )
        ):
            raise AssertionError("refined handle ball misses the A209/A131 center")
        thimble_ball = validated.interval_from_bounds(old["weighted_thimble_interval"])
        full_period = thimble_ball + handle_ball
        residual = beta_ball - full_period
        separation = coordinate_zero_exclusion(residual)
        zero_excluded = not residual.contains(acb(0)) and bool(separation["zero_excluded"])
        rows.append(
            {
                "candidate_id": candidate_id,
                "A132_objective_rank": rank,
                "direct_A_interval_path": relative(a_path),
                "direct_A_interval_sha256": sha256(a_path),
                "B_interval_source": b_source,
                "B_interval_inventory": b_inventory,
                "refined_handle_interval": handle.complex_interval(handle_ball),
                "refined_handle_center": handle.complex_pair(handle.midpoint(handle_ball)),
                "refined_handle_radius_upper": validated.radius_upper(handle_ball),
                "A210_handle_radius_upper": old["handle_radius_upper"],
                "handle_radius_improvement": (
                    float(old["handle_radius_upper"])
                    - validated.radius_upper(handle_ball)
                ),
                "weighted_thimble_interval": old["weighted_thimble_interval"],
                "refined_full_period_interval": handle.complex_interval(full_period),
                "refined_residual_interval": handle.complex_interval(residual),
                "refined_residual_center": handle.complex_pair(handle.midpoint(residual)),
                "refined_residual_radius_upper": validated.radius_upper(residual),
                "coordinate_zero_exclusion": separation,
                "zero_excluded": zero_excluded,
                "rigorous_decision": (
                    "REJECTED_BY_REFINED_E32_ZERO_EXCLUSION"
                    if zero_excluded
                    else "NOT_SEPARATED_BY_REFINED_E32_INTERVAL"
                ),
            }
        )

    rejected = [row for row in rows if row["zero_excluded"]]
    nonseparated = [row for row in rows if not row["zero_excluded"]]
    packet = {
        "schema": "MTTQ79SelectedAlignmentHeightFourRefinedE32Decisions.v1",
        "status": "HEIGHT4_SURVIVOR_DIRECT_HANDLE_AND_BETA_REFINEMENT_APPLIED",
        "artifact": "A211",
        "authority": {
            "A208_survivor_queue": relative(A208),
            "A208_survivor_queue_sha256": sha256(A208),
            "A209_primitive_handle_basis": relative(A209),
            "A209_primitive_handle_basis_sha256": sha256(A209),
            "A210_reusable_decisions": relative(A210),
            "A210_reusable_decisions_sha256": sha256(A210),
            "selected_beta_packet": relative(beta_path),
            "selected_beta_packet_sha256": sha256(beta_path),
            "beta_certifier_source": relative(Path(validated.__file__).resolve()),
            "beta_certifier_source_sha256": sha256(
                Path(validated.__file__).resolve()
            ),
            "builder_source": relative(Path(__file__)),
            "builder_source_sha256": sha256(Path(__file__)),
            "all_authority_sha256": {
                relative(path): sha256(path)
                for path in sorted(authority_paths, key=lambda item: str(item))
            },
        },
        "beta_interval_selection": {
            "inventory": beta_inventory,
            "selected_path": relative(beta_path),
            "selected_uniform_component_radius_upper": beta_radius,
            "center": beta_center,
            "source_serialization_radius_upper": beta_serialization,
            "roundtrip_serialization_radius_upper": beta_roundtrip,
        },
        "survivor_decisions": rows,
        "decision_ledger": {
            "A207_survivors_entering": 4,
            "newly_rejected": len(rejected),
            "refined_E32_nonseparated": len(nonseparated),
            "rejected_candidate_ids": [row["candidate_id"] for row in rejected],
            "nonseparated_candidate_ids": [
                row["candidate_id"] for row in nonseparated
            ],
        },
        "scope": {
            "observed_SM_values_used": False,
            "candidate_specific_direct_A_intervals_used": True,
            "rank3_direct_B_combination_used": True,
            "rank2_and_rank4_primitive_B_intervals_are_already_direct": True,
            "high_order_rank2_rank4_B_intervals_selected_when_narrower": True,
            "E32_nonseparation_is_not_exact_membership": True,
            "fixed_carrier_E32_rejection_is_not_a_covariant_branch_no_go": True,
            "covariant_PGL3_zero_and_Jacobian_solved": False,
            "global_height_four_completeness_over_Z90_proved": False,
        },
        "next_required_artifact": (
            "execute the full eight-row covariant F(A,m) and Jacobian on the "
            "E32-nonseparated rows first; any global branch claim must also cover "
            "fixed-carrier-rejected rows and branches omitted by the finite Kannan grid"
        ),
    }
    dump(PACKET, packet)

    table = []
    for row in rows:
        table.append(
            "| {rank} | `{candidate}` | {handle_radius:.9g} | {residual_radius:.9g} | {decision} |".format(
                rank=row["A132_objective_rank"],
                candidate=row["candidate_id"],
                handle_radius=row["refined_handle_radius_upper"],
                residual_radius=row["refined_residual_radius_upper"],
                decision=row["rigorous_decision"],
            )
        )
    note = f"""# MTT Selected q79 Height-Four Refined E32 Decisions A211 v1

## Result

A211 replaces A210's correlated primitive-handle sums with direct survivor
transports. It uses direct A combinations for all four survivors, a direct
`B:a1+B:b2` combination for rank 3, and chooses the narrowest certified B
enclosure for ranks 2 and 4 from the primitive and high-order candidate-direct
transports. It also chooses the narrowest certified selected-side beta interval
without changing its center or branch.

| A132 rank | candidate | handle radius | residual radius | decision |
|---:|---|---:|---:|---|
{chr(10).join(table)}

The refinement rejects {len(rejected)} additional fixed-grid survivor(s) and
leaves {len(nonseparated)} E32-nonseparated. Nonseparation is not equality and
is not promoted to a covariant solution. Conversely, fixed-carrier rejection
does not rule out a zero at another PGL3 alignment. No observed Standard Model
value is used.
"""
    NOTE.write_text(note, encoding="utf-8")
    candidate_packet = {
        "schema": "MTTSelectedQ79HeightFourRefinedE32Decisions.v1",
        "status": packet["status"],
        "artifact": "A211",
        "packet": relative(PACKET),
        "packet_sha256": sha256(PACKET),
        "note": relative(NOTE),
        "note_sha256": sha256(NOTE),
        "what_closes": {
            "four_direct_A_handle_combinations": True,
            "rank3_direct_B_handle_combination": True,
            "rank2_rank4_high_order_B_selection": True,
            "refined_survivor_E32_decisions": True,
            "new_survivor_rejections": len(rejected),
        },
        "what_remains_open": {
            "refined_E32_nonseparated_survivors": len(nonseparated),
            "covariant_PGL3_zero_and_Jacobian": True,
            "global_height_four_completeness_over_Z90": True,
        },
        "closure_claimed": False,
        "observed_SM_values_used": False,
        "next_required_artifact": packet["next_required_artifact"],
    }
    dump(CANDIDATE, candidate_packet)
    certificate = {
        "schema": "MTTCertificate.v1",
        "certificate": "MTTSelectedQ79HeightFourRefinedE32Decisions",
        "candidate_path": relative(CANDIDATE),
        "candidate_sha256": sha256(CANDIDATE),
        "status": candidate_packet["status"],
        "closure_claimed": False,
        "observed_SM_values_used": False,
        "next_required_artifact": candidate_packet["next_required_artifact"],
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
