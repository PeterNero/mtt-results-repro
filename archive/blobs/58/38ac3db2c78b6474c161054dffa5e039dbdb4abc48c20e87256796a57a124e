from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from flint import acb, ctx


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import certify_q79_selected_alignment_E32_handle_combination_interval as handle
import certify_q79_selected_side_beta_defect_transport as validated
from build_selected_q79_E32_weighted_71_and_carrier_decision import (
    coordinate_zero_exclusion,
    serialized_disk,
)


CANDIDATE = ROOT / "candidate_data" / "selected_q79heightfourrefinede32decisions.candidate.json"
CERTIFICATE = ROOT / "certificates" / "selected_q79heightfourrefinede32decisions.certificate.json"
E32_INDEX = 5


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def close(left: float, right: float, tolerance: float = 1.0e-9) -> bool:
    return abs(float(left) - float(right)) <= tolerance


def check_coordinate_replay(stored: dict, replay: dict) -> None:
    if (
        stored["separating_component"] != replay["separating_component"]
        or stored["zero_excluded"] != replay["zero_excluded"]
    ):
        raise AssertionError("A211 coordinate zero-exclusion classification changed")
    for stored_bound, replay_bound in zip(
        stored["coordinate_bounds"], replay["coordinate_bounds"]
    ):
        if stored_bound["component"] != replay_bound["component"]:
            raise AssertionError("A211 coordinate bound order changed")
        if not all(
            close(stored_bound[key], replay_bound[key])
            for key in ("lower", "upper")
        ):
            raise AssertionError("A211 coordinate bound replay mismatch")


def main() -> int:
    ctx.dps = 100
    candidate = load(CANDIDATE)
    certificate = load(CERTIFICATE)
    packet_path = ROOT / candidate["packet"]
    packet = load(packet_path)
    if candidate["artifact"] != "A211" or packet["artifact"] != "A211":
        raise AssertionError("A211 artifact label changed")
    if sha256(packet_path) != candidate["packet_sha256"]:
        raise AssertionError("A211 packet hash mismatch")
    if sha256(ROOT / candidate["note"]) != candidate["note_sha256"]:
        raise AssertionError("A211 proof-note hash mismatch")
    if sha256(CANDIDATE) != certificate["candidate_sha256"]:
        raise AssertionError("A211 candidate hash mismatch")
    if candidate["closure_claimed"] or certificate["closure_claimed"]:
        raise AssertionError("A211 overclaims covariant closure")

    authority = packet["authority"]
    for path_key, hash_key in (
        ("A208_survivor_queue", "A208_survivor_queue_sha256"),
        ("A209_primitive_handle_basis", "A209_primitive_handle_basis_sha256"),
        ("A210_reusable_decisions", "A210_reusable_decisions_sha256"),
        ("selected_beta_packet", "selected_beta_packet_sha256"),
        ("beta_certifier_source", "beta_certifier_source_sha256"),
        ("builder_source", "builder_source_sha256"),
    ):
        path = ROOT / authority[path_key]
        if sha256(path) != authority[hash_key]:
            raise AssertionError(f"A211 authority hash mismatch: {path_key}")
    for relative, digest in authority["all_authority_sha256"].items():
        if sha256(ROOT / relative) != digest:
            raise AssertionError(f"A211 authority inventory mismatch: {relative}")

    beta_rows = packet["beta_interval_selection"]["inventory"]
    if not beta_rows or sum(bool(row["selected"]) for row in beta_rows) != 1:
        raise AssertionError("A211 beta selection is not unique")
    beta_packets = []
    for row in beta_rows:
        path = ROOT / row["path"]
        beta = load(path)
        if sha256(path) != row["sha256"]:
            raise AssertionError("A211 beta inventory hash mismatch")
        radius = beta["endpoint"]["uniform_component_radius_upper"]
        if not close(radius, row["uniform_component_radius_upper"], 1.0e-15):
            raise AssertionError("A211 beta inventory radius mismatch")
        beta_packets.append(beta)
    reference_endpoint = beta_packets[0]["endpoint"]
    reference_center = [
        complex(float(value["real"]), float(value["imaginary"]))
        for value in reference_endpoint["beta_center"]
    ]
    reference_radius = float(reference_endpoint["uniform_component_radius_upper"]) + float(
        reference_endpoint["center_serialization_radius_upper"]
    )
    for row, beta in zip(beta_rows, beta_packets):
        endpoint = beta["endpoint"]
        center = [
            complex(float(value["real"]), float(value["imaginary"]))
            for value in endpoint["beta_center"]
        ]
        displacement = max(
            max(abs(left.real - right.real), abs(left.imag - right.imag))
            for left, right in zip(reference_center, center)
        )
        radius_sum = reference_radius + float(
            endpoint["uniform_component_radius_upper"]
        ) + float(endpoint["center_serialization_radius_upper"])
        overlap = displacement <= radius_sum
        if (
            not close(
                displacement,
                row["maximum_component_center_displacement_from_reference"],
            )
            or overlap != row["same_branch_component_boxes_overlap_reference"]
            or not overlap
        ):
            raise AssertionError("A211 beta same-branch overlap replay mismatch")
    selected_inventory = next(row for row in beta_rows if row["selected"])
    if selected_inventory["path"] != packet["beta_interval_selection"]["selected_path"]:
        raise AssertionError("A211 selected beta path changed")
    if float(selected_inventory["uniform_component_radius_upper"]) != min(
        float(row["uniform_component_radius_upper"]) for row in beta_rows
    ):
        raise AssertionError("A211 did not choose the narrowest certified beta interval")

    a208 = load(ROOT / authority["A208_survivor_queue"])
    a209 = load(ROOT / authority["A209_primitive_handle_basis"])
    a210 = load(ROOT / authority["A210_reusable_decisions"])
    selected_beta = load(ROOT / selected_inventory["path"])
    primitive = {
        row["label"]: validated.interval_from_bounds(row["E32_interval"])
        for row in a209["primitive_E32_handle_intervals"]
    }
    old_by_id = {row["candidate_id"]: row for row in a210["candidate_decisions"]}
    beta_endpoint = selected_beta["endpoint"]
    beta_ball, roundtrip = serialized_disk(
        beta_endpoint["beta_center"][E32_INDEX],
        float(beta_endpoint["uniform_component_radius_upper"])
        + float(beta_endpoint["center_serialization_radius_upper"]),
    )
    if not close(
        roundtrip,
        packet["beta_interval_selection"]["roundtrip_serialization_radius_upper"],
        1.0e-15,
    ):
        raise AssertionError("A211 beta serialization replay mismatch")

    rows = packet["survivor_decisions"]
    expected_candidates = a208["height_four_candidates"][1:]
    if len(rows) != 4 or [row["A132_objective_rank"] for row in rows] != [2, 3, 4, 5]:
        raise AssertionError("A211 survivor order changed")
    rejected = 0
    nonseparated = 0
    for row, source_candidate in zip(rows, expected_candidates):
        rank = int(row["A132_objective_rank"])
        candidate_id = row["candidate_id"]
        if (
            rank != int(source_candidate["A132_objective_rank"])
            or candidate_id != source_candidate["candidate_id"]
        ):
            raise AssertionError("A211 survivor source mapping changed")

        a_path = ROOT / row["direct_A_interval_path"]
        if sha256(a_path) != row["direct_A_interval_sha256"]:
            raise AssertionError("A211 direct-A hash mismatch")
        a_packet = load(a_path)
        if (
            int(a_packet["A132_objective_rank"]) != rank
            or a_packet["candidate_id"] != candidate_id
            or a_packet["handle"] != "A"
        ):
            raise AssertionError("A211 direct-A identity mismatch")
        a_ball = validated.interval_from_bounds(
            a_packet["direct_handle_interval"]["E32_interval"]
        )
        allowed_kinds = {
            2: {"A209_PRIMITIVE_B_A1", "HIGH_ORDER_CANDIDATE_DIRECT_B"},
            3: {"CANDIDATE_DIRECT_B"},
            4: {
                "NEGATIVE_A209_PRIMITIVE_B_B2",
                "HIGH_ORDER_CANDIDATE_DIRECT_B",
            },
            5: {"EXACT_ZERO_B_COMPONENT"},
        }[rank]
        inventory = row["B_interval_inventory"]
        if (
            not inventory
            or sum(bool(option["selected"]) for option in inventory) != 1
            or any(option["kind"] not in allowed_kinds for option in inventory)
        ):
            raise AssertionError("A211 B-handle inventory changed")
        decoded_options = []
        for option in inventory:
            kind = option["kind"]
            if kind == "A209_PRIMITIVE_B_A1":
                option_ball = primitive["B:a1"]
            elif kind == "NEGATIVE_A209_PRIMITIVE_B_B2":
                option_ball = -primitive["B:b2"]
            elif kind == "EXACT_ZERO_B_COMPONENT":
                option_ball = acb(0)
            else:
                option_path = ROOT / option["path"]
                if sha256(option_path) != option["sha256"]:
                    raise AssertionError("A211 candidate-direct B hash mismatch")
                option_packet = load(option_path)
                if (
                    int(option_packet["A132_objective_rank"]) != rank
                    or option_packet["candidate_id"] != candidate_id
                    or option_packet["handle"] != "B"
                ):
                    raise AssertionError("A211 candidate-direct B identity mismatch")
                interval_key = (
                    "refined_handle_interval"
                    if kind == "HIGH_ORDER_CANDIDATE_DIRECT_B"
                    else "direct_handle_interval"
                )
                option_ball = validated.interval_from_bounds(
                    option_packet[interval_key]["E32_interval"]
                )
            option_radius = validated.radius_upper(option_ball)
            if not close(option_radius, option["radius_upper"]):
                raise AssertionError("A211 B-handle inventory radius mismatch")
            decoded_options.append((option, option_ball, option_radius))
        selected_option, b_ball, selected_radius = next(
            decoded for decoded in decoded_options if decoded[0]["selected"]
        )
        if selected_radius != min(decoded[2] for decoded in decoded_options):
            raise AssertionError("A211 did not choose the narrowest B interval")
        if row["B_interval_source"] != selected_option["source"]:
            raise AssertionError("A211 selected B-handle source changed")

        refined_handle = a_ball + b_ball
        old = old_by_id[candidate_id]
        thimble = validated.interval_from_bounds(old["weighted_thimble_interval"])
        residual = beta_ball - (thimble + refined_handle)
        replay = coordinate_zero_exclusion(residual)
        check_coordinate_replay(row["coordinate_zero_exclusion"], replay)
        zero_excluded = not residual.contains(acb(0)) and bool(replay["zero_excluded"])
        if zero_excluded != row["zero_excluded"]:
            raise AssertionError("A211 zero-exclusion replay mismatch")
        if not close(
            validated.radius_upper(refined_handle),
            row["refined_handle_radius_upper"],
        ):
            raise AssertionError("A211 refined handle radius mismatch")
        if not close(
            validated.radius_upper(residual),
            row["refined_residual_radius_upper"],
        ):
            raise AssertionError("A211 refined residual radius mismatch")
        improvement = float(old["handle_radius_upper"]) - validated.radius_upper(
            refined_handle
        )
        if not close(improvement, row["handle_radius_improvement"]):
            raise AssertionError("A211 handle improvement mismatch")
        expected_decision = (
            "REJECTED_BY_REFINED_E32_ZERO_EXCLUSION"
            if zero_excluded
            else "NOT_SEPARATED_BY_REFINED_E32_INTERVAL"
        )
        if row["rigorous_decision"] != expected_decision:
            raise AssertionError("A211 rigorous decision mismatch")
        if zero_excluded:
            rejected += 1
        else:
            nonseparated += 1

    ledger = packet["decision_ledger"]
    if (
        ledger["A207_survivors_entering"] != 4
        or ledger["newly_rejected"] != rejected
        or ledger["refined_E32_nonseparated"] != nonseparated
    ):
        raise AssertionError("A211 decision ledger mismatch")
    if packet["scope"]["covariant_PGL3_zero_and_Jacobian_solved"]:
        raise AssertionError("A211 promotes an E32 gate to covariant closure")
    if packet["scope"]["global_height_four_completeness_over_Z90_proved"]:
        raise AssertionError("A211 promotes the fixed grid to Z90 completeness")
    if not packet["scope"][
        "fixed_carrier_E32_rejection_is_not_a_covariant_branch_no_go"
    ]:
        raise AssertionError("A211 lost the fixed-carrier/covariant guard")

    print("q79 A211 refined height-four survivor E32 decision audit: PASS")
    print(f"closed: four direct-A refinements and {rejected} new survivor rejection(s)")
    print(f"open: {nonseparated} E32-nonseparated survivor(s), full eight-row covariant gate")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
