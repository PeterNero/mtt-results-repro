from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PERIOD_DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
)
A139 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_fourth_full_interval.packet.json"
ARTIFACTS = (
    "A140",
    "A141",
    "A142",
    "A143",
    "A144",
    "A145",
    "A146",
    "A147",
    "A148",
    "A149",
    "A150",
    "A151",
    "A152",
    "A153",
    "A154",
    "A155",
    "A156",
    "A157",
    "A158",
    "A159",
    "A160",
    "A161",
    "A162",
    "A163",
    "A164",
    "A165",
    "A166",
    "A167",
    "A168",
    "A169",
    "A170",
    "A171",
    "A172",
    "A173",
    "A174",
    "A175",
    "A176",
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def close(left: float, right: float, tolerance: float = 2e-18) -> bool:
    return math.isclose(left, right, rel_tol=1e-13, abs_tol=tolerance)


def successor_path(artifact: str) -> Path:
    return PERIOD_DIRECTORY / f"selected_alignment_E32_clearance_ranked_successor_{artifact}.packet.json"


def audit_successor(predecessor_path: Path, artifact: str) -> tuple[Path, dict]:
    packet_path = successor_path(artifact)
    predecessor = load(predecessor_path)
    packet = load(packet_path)
    assert packet["artifact"] == artifact
    assert packet["schema"] == "MTTQ79SelectedE32ClearanceRankedAppendSuccessor.v1"
    assert packet["status"] == "SELECTED_FULL_E32_THIMBLE_INTERVAL_SUCCESSOR_CLOSED_BATCH_EXECUTION_OPEN"
    assert packet["append_only_predecessor"]["path"] == str(
        predecessor_path.relative_to(ROOT)
    ).replace("\\", "/")
    assert packet["append_only_predecessor"]["sha256"] == sha256(predecessor_path)
    old_ids = sorted(
        int(row["distinguished_index"])
        for row in predecessor["accepted_full_intervals"]
    )
    assert packet["append_only_predecessor"]["accepted_distinguished_indices"] == old_ids
    for authority in packet["authority"]:
        path = ROOT / authority["path"]
        assert path.exists(), authority["path"]
        assert sha256(path) == authority["sha256"], authority["path"]

    new = packet["new_accepted_full_interval"]
    index = int(new["distinguished_index"])
    chart = new["line_chart"]
    assert predecessor["clearance_ranked_queues"][chart][0]["distinguished_index"] == index
    assert predecessor["clearance_ranked_queues"][chart][0]["coefficient"] == new["coefficient"]
    new_ids = sorted(
        int(row["distinguished_index"])
        for row in packet["accepted_full_intervals"]
    )
    assert new_ids == sorted(old_ids + [index])
    assert not any(
        int(row["distinguished_index"]) == index
        for queue_chart in ("y", "z")
        for row in packet["clearance_ranked_queues"][queue_chart]
    )
    assert new["fallback_margin"] > 0
    expected_cost = abs(int(new["coefficient"])) * (
        float(new["full_interval_radius_upper"])
        + float(new["A131_center_difference"])
    )
    assert close(new["weighted_radius_plus_displacement_cost"], expected_cost)
    old_ledger = predecessor["weighted_budget_ledger"]
    ledger = packet["weighted_budget_ledger"]
    assert ledger["selected_support_closed"] == old_ledger["selected_support_closed"] + 1
    assert ledger["selected_l1_closed"] == old_ledger["selected_l1_closed"] + abs(new["coefficient"])
    assert ledger["remaining_support"] == old_ledger["remaining_support"] - 1
    assert ledger["remaining_l1_weight"] == old_ledger["remaining_l1_weight"] - abs(new["coefficient"])
    assert close(
        ledger["certified_radius_plus_displacement_cost"],
        old_ledger["certified_radius_plus_displacement_cost"] + expected_cost,
    )
    assert close(
        ledger["remaining_budget"],
        old_ledger["remaining_budget"] - expected_cost,
    )
    assert close(
        ledger["A134_initial_remaining_budget"]
        - ledger["certified_radius_plus_displacement_cost"],
        ledger["remaining_budget"],
    )
    assert ledger["remaining_budget"] > 0
    assert packet["scope"]["selected_full_interval_count"] == len(new_ids)
    assert packet["scope"]["new_queue_head_full_interval_closed"]
    assert packet["scope"]["all_accepted_intervals_meet_uniform_fallback"]
    assert packet["scope"]["covariant_z_chart_interval_adapter_closed"] == any(
        row["line_chart"] == "z" for row in packet["accepted_full_intervals"]
    )
    assert not packet["scope"]["weighted_71_thimble_interval_closed"]
    assert not packet["scope"]["observed_SM_values_used"]

    suffix = artifact.lower()
    frontier_path = PERIOD_DIRECTORY / f"U6_frontier_after_{artifact}.packet.json"
    note_path = ROOT / "proof_corpus" / f"MTT_Selected_q79E32ClearanceRankedSuccessor_{artifact}_v1.md"
    candidate_path = ROOT / "candidate_data" / f"selected_q79e32clearancerankedsuccessor{suffix}.candidate.json"
    certificate_path = ROOT / "certificates" / f"selected_q79e32clearancerankedsuccessor{suffix}.certificate.json"
    frontier = load(frontier_path)
    candidate = load(candidate_path)
    certificate = load(certificate_path)
    assert frontier["artifact"] == artifact
    assert frontier["selected_support_closed"] == ledger["selected_support_closed"]
    assert frontier["selected_l1_closed"] == ledger["selected_l1_closed"]
    assert close(frontier["remaining_weighted_budget"], ledger["remaining_budget"])
    assert candidate["artifact"] == artifact
    assert candidate["packet_sha256"] == sha256(packet_path)
    assert candidate["frontier_sha256"] == sha256(frontier_path)
    assert candidate["note_sha256"] == sha256(note_path)
    assert certificate["artifact"] == artifact
    assert certificate["candidate_sha256"] == sha256(candidate_path)
    assert not candidate["closure_claimed"] and not certificate["closure_claimed"]
    return packet_path, packet


def main() -> int:
    predecessor_path = A139
    packets = {}
    for artifact in ARTIFACTS:
        predecessor_path, packets[artifact] = audit_successor(
            predecessor_path, artifact
        )

    final = packets["A176"]
    new = final["new_accepted_full_interval"]
    assert new["distinguished_index"] == 50
    assert new["root_id"] == "selected_047"
    assert new["line_chart"] == "z"
    assert new["coefficient"] == 1
    assert new["tail_regular_segments"] == 768
    assert close(new["tail_radius_upper"], 3.890338897381829e-10)
    assert close(new["main_radius_upper"], 1.258544559744545e-7)
    assert close(new["full_interval_radius_upper"], 1.78374099046863e-7)
    assert [
        row["distinguished_index"] for row in final["accepted_full_intervals"]
    ] == [1, 4, 5, 10, 11, 12, 14, 17, 18, 19, 20, 21, 26, 28, 29, 30, 31, 32, 33, 34, 35, 37, 39, 46, 48, 50, 51, 55, 57, 59, 60, 61, 62, 63, 69, 75, 85, 86, 87, 88, 89]
    ledger = final["weighted_budget_ledger"]
    assert ledger["selected_support_closed"] == 41
    assert ledger["selected_l1_closed"] == 75
    assert ledger["remaining_support"] == 30
    assert ledger["remaining_l1_weight"] == 48
    assert close(ledger["remaining_budget"], 0.0025093956717539695)
    assert final["clearance_ranked_queues"]["y"] == []
    assert final["clearance_ranked_queues"]["z"][0]["distinguished_index"] == 66
    assert final["clearance_ranked_queues"]["z"][0]["root_id"] == "selected_040"
    assert final["clearance_ranked_queues"]["z"][0]["coefficient"] == -3
    assert final["scope"]["covariant_z_chart_interval_adapter_closed"]
    assert [
        row["distinguished_index"]
        for row in final["partial_interval_diagnostics"]
    ] == [47]

    stem = PERIOD_DIRECTORY / "d021_selected_026"
    nodal = load(Path(f"{stem}.nodal_factor.interval.packet.json"))
    main_interval = load(Path(f"{stem}.E32_main.interval.packet.json"))
    tail_interval = load(Path(f"{stem}.E32_tail.interval.packet.json"))
    assert nodal["certified_node"]["pair_seed_method"] == (
        "unique closest pair at a deeper radial seed"
    )
    assert close(nodal["certified_node"]["pair_seed_epsilon"], 1.0e-9)
    assert nodal["certified_node"]["incoming_closest_pair_zero_based"] == [4, 5]
    assert nodal["certified_node"]["jacobian_determinant_absolute_lower"] > 4.95e8
    assert main_interval["selected_thimble"][
        "near_node_colliding_pair_zero_based"
    ] == [4, 5]
    assert main_interval["selected_thimble"]["instantaneous_closest_pair_rule_used"] is False
    assert main_interval["selected_thimble"][
        "node_affinity_separation_margin_lower"
    ] > 8.5
    assert main_interval["scope"]["certified_nodal_pair_selector_consumed"]
    assert tail_interval["selected_thimble"]["cutoff_pair_zero_based"] == [4, 5]
    assert tail_interval["scope"]["certified_nodal_pair_selector_consumed"]

    stem_29 = PERIOD_DIRECTORY / "d029_selected_013"
    nodal_29 = load(Path(f"{stem_29}.nodal_factor.interval.packet.json"))
    main_29 = load(Path(f"{stem_29}.E32_main.interval.packet.json"))
    tail_29 = load(Path(f"{stem_29}.E32_tail.interval.packet.json"))
    assert nodal_29["certified_node"]["pair_seed_epsilon"] == 1.0e-9
    assert nodal_29["certified_node"]["incoming_closest_pair_zero_based"] == [0, 1]
    assert main_29["selected_thimble"]["near_node_colliding_pair_zero_based"] == [0, 1]
    assert main_29["selected_thimble"]["node_affinity_separation_margin_lower"] > 1.5
    assert main_29["scope"]["certified_nodal_pair_selector_consumed"]
    assert tail_29["selected_thimble"]["cutoff_pair_zero_based"] == [0, 1]
    assert tail_29["scope"]["certified_nodal_pair_selector_consumed"]

    stem_5 = PERIOD_DIRECTORY / "d005_selected_012"
    nodal_5 = load(Path(f"{stem_5}.nodal_factor.interval.packet.json"))
    main_5 = load(Path(f"{stem_5}.E32_main.interval.packet.json"))
    tail_5 = load(Path(f"{stem_5}.E32_tail.interval.packet.json"))
    assert nodal_5["certified_node"]["pair_seed_epsilon"] == 1.0e-9
    assert nodal_5["certified_node"]["incoming_closest_pair_zero_based"] == [0, 1]
    assert nodal_5["certified_node"]["jacobian_determinant_absolute_lower"] > 3.81e5
    assert main_5["selected_thimble"]["near_node_colliding_pair_zero_based"] == [0, 1]
    assert main_5["selected_thimble"]["node_affinity_separation_margin_lower"] > 0.96
    assert main_5["scope"]["certified_nodal_pair_selector_consumed"]
    assert main_5["validated_main_transport"]["accepted_step_count"] == 165
    assert main_5["validated_main_transport"]["rejected_step_count"] == 16
    assert close(
        main_5["validated_main_transport"]["uniform_integral_radius_upper"],
        4.130610830379972e-7,
    )
    assert tail_5["selected_thimble"]["cutoff_pair_zero_based"] == [0, 1]
    assert tail_5["scope"]["certified_nodal_pair_selector_consumed"]

    stem_57 = PERIOD_DIRECTORY / "d057_selected_008"
    nodal_57 = load(Path(f"{stem_57}.nodal_factor.interval.packet.json"))
    main_57 = load(Path(f"{stem_57}.E32_main.interval.packet.json"))
    tail_57 = load(Path(f"{stem_57}.E32_tail.interval.packet.json"))
    assert nodal_57["certified_node"]["pair_seed_epsilon"] == 1.0e-9
    assert nodal_57["certified_node"]["incoming_closest_pair_zero_based"] == [3, 4]
    assert nodal_57["certified_node"]["jacobian_determinant_absolute_lower"] > 3.82e18
    assert main_57["selected_thimble"]["near_node_colliding_pair_zero_based"] == [3, 4]
    assert main_57["selected_thimble"]["node_affinity_separation_margin_lower"] > 1.83
    assert main_57["selected_thimble"]["endpoint_cutoff_epsilon"] == 2.0e-5
    assert main_57["scope"]["certified_nodal_pair_selector_consumed"]
    assert main_57["scope"]["uncompressed_physical_generator_zonotope_consumed"]
    assert main_57["validated_main_transport"]["accepted_step_count"] == 252
    assert main_57["validated_main_transport"]["rejected_step_count"] == 21
    assert close(
        main_57["validated_main_transport"]["uniform_integral_radius_upper"],
        1.038675053577015e-5,
    )
    assert tail_57["selected_thimble"]["cutoff_pair_zero_based"] == [3, 4]
    assert tail_57["selected_thimble"]["endpoint_cutoff_epsilon"] == 2.0e-5
    assert tail_57["scope"]["certified_nodal_pair_selector_consumed"]

    stem_37 = PERIOD_DIRECTORY / "d037_selected_002"
    nodal_37 = load(Path(f"{stem_37}.nodal_factor.interval.packet.json"))
    main_37 = load(Path(f"{stem_37}.E32_main.interval.packet.json"))
    tail_37 = load(Path(f"{stem_37}.E32_tail.interval.packet.json"))
    assert nodal_37["certified_node"]["pair_seed_epsilon"] == 1.0e-9
    assert nodal_37["certified_node"]["incoming_closest_pair_zero_based"] == [0, 1]
    assert nodal_37["certified_node"]["jacobian_determinant_absolute_lower"] > 3.06e7
    assert main_37["selected_thimble"]["near_node_colliding_pair_zero_based"] == [0, 1]
    assert main_37["selected_thimble"]["node_affinity_separation_margin_lower"] > 0.66
    assert main_37["selected_thimble"]["endpoint_cutoff_epsilon"] == 1.0e-5
    assert main_37["scope"]["uncompressed_physical_generator_zonotope_consumed"]
    assert main_37["validated_main_transport"]["accepted_step_count"] == 235
    assert main_37["validated_main_transport"]["rejected_step_count"] == 55
    assert close(
        main_37["validated_main_transport"]["uniform_integral_radius_upper"],
        8.253525766885164e-8,
    )
    assert tail_37["selected_thimble"]["cutoff_pair_zero_based"] == [0, 1]
    assert tail_37["selected_thimble"]["endpoint_cutoff_epsilon"] == 1.0e-5

    stem_60 = PERIOD_DIRECTORY / "d060_selected_089"
    nodal_60 = load(Path(f"{stem_60}.nodal_factor.interval.packet.json"))
    main_60 = load(Path(f"{stem_60}.E32_main.interval.packet.json"))
    tail_60 = load(Path(f"{stem_60}.E32_tail.interval.packet.json"))
    assert nodal_60["certified_node"]["pair_seed_epsilon"] == 1.0e-9
    assert nodal_60["certified_node"]["incoming_closest_pair_zero_based"] == [4, 5]
    assert nodal_60["certified_node"]["jacobian_determinant_absolute_lower"] > 1.30e11
    assert main_60["selected_thimble"]["near_node_colliding_pair_zero_based"] == [4, 5]
    assert main_60["selected_thimble"]["node_affinity_separation_margin_lower"] > 1.05
    assert main_60["scope"]["uncompressed_physical_generator_zonotope_consumed"]
    assert main_60["validated_main_transport"]["accepted_step_count"] == 126
    assert main_60["validated_main_transport"]["rejected_step_count"] == 19
    assert close(
        main_60["validated_main_transport"]["uniform_integral_radius_upper"],
        8.26708945089474e-8,
    )
    assert main_60["scope"]["certified_tail_cutoff_period_reuse_consumed"]
    assert tail_60["selected_thimble"]["cutoff_pair_zero_based"] == [4, 5]

    stem_87 = PERIOD_DIRECTORY / "d087_selected_085"
    nodal_87 = load(Path(f"{stem_87}.nodal_factor.interval.packet.json"))
    main_87 = load(Path(f"{stem_87}.E32_main.interval.packet.json"))
    tail_87 = load(Path(f"{stem_87}.E32_tail.interval.packet.json"))
    assert nodal_87["certified_node"]["pair_seed_epsilon"] == 1.0e-9
    assert nodal_87["certified_node"]["incoming_closest_pair_zero_based"] == [3, 4]
    assert nodal_87["certified_node"]["jacobian_determinant_absolute_lower"] > 8.57e4
    assert main_87["selected_thimble"]["near_node_colliding_pair_zero_based"] == [3, 4]
    assert main_87["selected_thimble"]["node_affinity_separation_margin_lower"] > 1.76
    assert main_87["scope"]["uncompressed_physical_generator_zonotope_consumed"]
    assert main_87["scope"]["certified_tail_cutoff_period_reuse_consumed"]
    assert main_87["validated_main_transport"]["accepted_step_count"] == 139
    assert main_87["validated_main_transport"]["rejected_step_count"] == 50
    assert close(
        main_87["validated_main_transport"]["uniform_integral_radius_upper"],
        4.921072286600216e-8,
    )
    assert tail_87["selected_thimble"]["cutoff_pair_zero_based"] == [3, 4]
    assert tail_87["scope"]["certified_nodal_pair_selector_consumed"]

    stem_11 = PERIOD_DIRECTORY / "d011_selected_014"
    nodal_11 = load(Path(f"{stem_11}.nodal_factor.interval.packet.json"))
    main_11 = load(Path(f"{stem_11}.E32_main.interval.packet.json"))
    tail_11 = load(Path(f"{stem_11}.E32_tail.interval.packet.json"))
    assert nodal_11["certified_node"]["pair_seed_epsilon"] == 1.0e-9
    assert nodal_11["certified_node"]["incoming_closest_pair_zero_based"] == [3, 4]
    assert nodal_11["certified_node"]["jacobian_determinant_absolute_lower"] > 4.73e5
    assert main_11["selected_thimble"]["near_node_colliding_pair_zero_based"] == [3, 4]
    assert main_11["selected_thimble"]["node_affinity_separation_margin_lower"] > 1.36
    assert main_11["scope"]["uncompressed_physical_generator_zonotope_consumed"]
    assert main_11["scope"]["certified_tail_cutoff_period_reuse_consumed"]
    assert main_11["validated_main_transport"]["accepted_step_count"] == 145
    assert main_11["validated_main_transport"]["rejected_step_count"] == 56
    assert close(
        main_11["validated_main_transport"]["uniform_integral_radius_upper"],
        2.1153876733524222e-7,
    )
    assert tail_11["selected_thimble"]["cutoff_pair_zero_based"] == [3, 4]
    assert tail_11["scope"]["certified_nodal_pair_selector_consumed"]

    stem_86 = PERIOD_DIRECTORY / "d086_selected_084"
    nodal_86 = load(Path(f"{stem_86}.nodal_factor.interval.packet.json"))
    main_86 = load(Path(f"{stem_86}.E32_main.interval.packet.json"))
    tail_86 = load(Path(f"{stem_86}.E32_tail.interval.packet.json"))
    assert nodal_86["certified_node"]["pair_seed_epsilon"] == 1.0e-9
    assert nodal_86["certified_node"]["incoming_closest_pair_zero_based"] == [3, 4]
    assert nodal_86["certified_node"]["jacobian_determinant_absolute_lower"] > 7.18e4
    assert main_86["selected_thimble"]["near_node_colliding_pair_zero_based"] == [3, 4]
    assert main_86["selected_thimble"]["node_affinity_separation_margin_lower"] > 1.43
    assert main_86["scope"]["uncompressed_physical_generator_zonotope_consumed"]
    assert main_86["scope"]["certified_tail_cutoff_period_reuse_consumed"]
    assert main_86["validated_main_transport"]["accepted_step_count"] == 126
    assert main_86["validated_main_transport"]["rejected_step_count"] == 37
    assert close(
        main_86["validated_main_transport"]["uniform_integral_radius_upper"],
        1.7865286913408602e-7,
    )
    assert tail_86["selected_thimble"]["cutoff_pair_zero_based"] == [3, 4]
    assert tail_86["scope"]["certified_nodal_pair_selector_consumed"]

    z_wall = load(
        PERIOD_DIRECTORY.parent / "selected_alignment_zchart_wall.interval.packet.json"
    )
    assert z_wall["selected_z_line_chart_zeros"]["count"] == 3
    assert float(
        z_wall["selected_z_line_chart_zeros"][
            "minimum_pairwise_torus_ball_separation_lower"
        ]
    ) > 0.355
    assert float(
        z_wall["selected_z_line_chart_zeros"][
            "minimum_torus_distance_to_critical_balls_lower"
        ]
    ) > 0.0159
    stem_48 = PERIOD_DIRECTORY / "d048_selected_046"
    nodal_48 = load(Path(f"{stem_48}.nodal_factor.interval.packet.json"))
    main_48 = load(Path(f"{stem_48}.E32_main.interval.packet.json"))
    tail_48 = load(Path(f"{stem_48}.E32_tail.interval.packet.json"))
    full_48 = load(Path(f"{stem_48}.E32_full.interval.packet.json"))
    assert nodal_48["selected_thimble"]["line_chart"] == "z"
    assert nodal_48["certified_node"]["incoming_closest_pair_zero_based"] == [3, 4]
    assert nodal_48["certified_node"]["jacobian_determinant_absolute_lower"] > 132.8
    assert main_48["selected_thimble"]["line_chart"] == "z"
    assert main_48["selected_thimble"]["near_node_colliding_pair_zero_based"] == [3, 4]
    assert main_48["selected_thimble"]["node_affinity_separation_margin_lower"] > 0.63
    assert main_48["scope"]["A123_projective_line_chart_covariance_consumed"]
    assert main_48["scope"]["certified_tail_cutoff_period_reuse_consumed"]
    assert main_48["validated_main_transport"]["accepted_step_count"] == 68
    assert main_48["validated_main_transport"]["rejected_step_count"] == 18
    assert close(
        main_48["orientation"]["selected_base_center_maximum_difference"],
        1.0541747131767663e-11,
    )
    assert tail_48["selected_thimble"]["line_chart"] == "z"
    assert tail_48["selected_thimble"]["cutoff_pair_zero_based"] == [3, 4]
    assert full_48["selected_thimble"]["line_chart"] == "z"
    assert full_48["full_E32_thimble"]["floating_candidate_contained"]

    stem_88 = PERIOD_DIRECTORY / "d088_selected_064"
    nodal_88 = load(Path(f"{stem_88}.nodal_factor.interval.packet.json"))
    main_88 = load(Path(f"{stem_88}.E32_main.interval.packet.json"))
    tail_88 = load(Path(f"{stem_88}.E32_tail.interval.packet.json"))
    full_88 = load(Path(f"{stem_88}.E32_full.interval.packet.json"))
    assert nodal_88["selected_thimble"]["line_chart"] == "y"
    assert nodal_88["certified_node"]["incoming_closest_pair_zero_based"] == [0, 1]
    assert nodal_88["certified_node"]["jacobian_determinant_absolute_lower"] > 1267
    assert main_88["selected_thimble"]["line_chart"] == "y"
    assert main_88["selected_thimble"]["near_node_colliding_pair_zero_based"] == [0, 1]
    assert main_88["scope"]["certified_tail_cutoff_period_reuse_consumed"]
    assert main_88["scope"]["uncompressed_physical_generator_zonotope_consumed"]
    assert main_88["validated_main_transport"]["accepted_step_count"] == 128
    assert main_88["validated_main_transport"]["rejected_step_count"] == 23
    assert close(
        main_88["validated_main_transport"]["uniform_integral_radius_upper"],
        4.0606162630066217e-7,
    )
    assert main_88["polygonal_homotopy"]["detour_fraction"] == 0.35
    assert main_88["polygonal_homotopy"]["detour_signed_right_offset"] == 0.01
    assert main_88["polygonal_homotopy"]["return_fraction"] == 0.82
    assert main_88["polygonal_homotopy"]["other_critical_ball_clearance_lower"] > 0.0139
    assert tail_88["selected_thimble"]["cutoff_pair_zero_based"] == [0, 1]
    assert len(tail_88["regular_segments"]) == 384
    assert full_88["full_E32_thimble"]["floating_candidate_contained"]
    assert full_88["A134_radius_ledger"]["fallback_met"]

    stem_33 = PERIOD_DIRECTORY / "d033_selected_010"
    nodal_33 = load(Path(f"{stem_33}.nodal_factor.interval.packet.json"))
    main_33 = load(Path(f"{stem_33}.E32_main.interval.packet.json"))
    tail_33 = load(Path(f"{stem_33}.E32_tail.interval.packet.json"))
    full_33 = load(Path(f"{stem_33}.E32_full.interval.packet.json"))
    assert nodal_33["selected_thimble"]["line_chart"] == "y"
    assert nodal_33["certified_node"]["incoming_closest_pair_zero_based"] == [3, 4]
    assert nodal_33["certified_node"]["jacobian_determinant_absolute_lower"] > 2.05e6
    assert main_33["selected_thimble"]["near_node_colliding_pair_zero_based"] == [3, 4]
    assert main_33["scope"]["certified_tail_cutoff_period_reuse_consumed"]
    assert main_33["scope"]["uncompressed_physical_generator_zonotope_consumed"]
    assert main_33["validated_main_transport"]["accepted_step_count"] == 171
    assert main_33["validated_main_transport"]["rejected_step_count"] == 84
    assert close(
        main_33["validated_main_transport"]["uniform_integral_radius_upper"],
        6.326398650143199e-7,
    )
    assert main_33["polygonal_homotopy"]["detour_fraction"] == 0.2
    assert main_33["polygonal_homotopy"]["detour_signed_right_offset"] == 0.0
    assert main_33["polygonal_homotopy"]["return_fraction"] == 0.65
    assert main_33["polygonal_homotopy"]["other_critical_ball_clearance_lower"] > 0.00614
    assert tail_33["selected_thimble"]["cutoff_pair_zero_based"] == [3, 4]
    assert len(tail_33["regular_segments"]) == 384
    assert full_33["full_E32_thimble"]["floating_candidate_contained"]
    assert full_33["A134_radius_ledger"]["fallback_met"]

    stem_35 = PERIOD_DIRECTORY / "d035_selected_004"
    nodal_35 = load(Path(f"{stem_35}.nodal_factor.interval.packet.json"))
    main_35 = load(Path(f"{stem_35}.E32_main.interval.packet.json"))
    tail_35 = load(Path(f"{stem_35}.E32_tail.interval.packet.json"))
    full_35 = load(Path(f"{stem_35}.E32_full.interval.packet.json"))
    assert nodal_35["selected_thimble"]["line_chart"] == "y"
    assert nodal_35["certified_node"]["incoming_closest_pair_zero_based"] == [1, 2]
    assert nodal_35["certified_node"]["jacobian_determinant_absolute_lower"] > 3.81e6
    assert main_35["selected_thimble"]["near_node_colliding_pair_zero_based"] == [1, 2]
    assert main_35["validated_main_transport"]["accepted_step_count"] == 191
    assert main_35["validated_main_transport"]["rejected_step_count"] == 97
    assert close(
        main_35["validated_main_transport"]["uniform_integral_radius_upper"],
        1.4173551537312103e-6,
    )
    assert main_35["polygonal_homotopy"]["detour_fraction"] == 0.2
    assert main_35["polygonal_homotopy"]["detour_signed_right_offset"] == 0.0
    assert main_35["polygonal_homotopy"]["return_fraction"] == 0.74
    assert main_35["polygonal_homotopy"]["other_critical_ball_clearance_lower"] > 0.00535
    assert tail_35["selected_thimble"]["cutoff_pair_zero_based"] == [1, 2]
    assert len(tail_35["regular_segments"]) == 384
    assert full_35["full_E32_thimble"]["floating_candidate_contained"]
    assert full_35["A134_radius_ledger"]["fallback_met"]

    stem_63 = PERIOD_DIRECTORY / "d063_selected_063"
    nodal_63 = load(Path(f"{stem_63}.nodal_factor.interval.packet.json"))
    main_63 = load(Path(f"{stem_63}.E32_main.interval.packet.json"))
    tail_63 = load(Path(f"{stem_63}.E32_tail.interval.packet.json"))
    full_63 = load(Path(f"{stem_63}.E32_full.interval.packet.json"))
    assert nodal_63["selected_thimble"]["line_chart"] == "y"
    assert nodal_63["certified_node"]["incoming_closest_pair_zero_based"] == [1, 2]
    assert nodal_63["certified_node"]["jacobian_determinant_absolute_lower"] > 302.2
    assert main_63["selected_thimble"]["near_node_colliding_pair_zero_based"] == [1, 2]
    assert main_63["validated_main_transport"]["accepted_step_count"] == 100
    assert main_63["validated_main_transport"]["rejected_step_count"] == 17
    assert close(
        main_63["validated_main_transport"]["uniform_integral_radius_upper"],
        3.4309395125334205e-6,
    )
    assert main_63["polygonal_homotopy"]["detour_fraction"] == 0.2
    assert main_63["polygonal_homotopy"]["detour_signed_right_offset"] == 0.02
    assert main_63["polygonal_homotopy"]["return_fraction"] == 0.78
    assert main_63["polygonal_homotopy"]["other_critical_ball_clearance_lower"] > 0.0165
    assert tail_63["selected_thimble"]["cutoff_pair_zero_based"] == [1, 2]
    assert len(tail_63["regular_segments"]) == 384
    assert full_63["full_E32_thimble"]["floating_candidate_contained"]
    assert full_63["A134_radius_ledger"]["fallback_met"]

    stem_26 = PERIOD_DIRECTORY / "d026_selected_015"
    nodal_26 = load(Path(f"{stem_26}.nodal_factor.interval.packet.json"))
    main_26 = load(Path(f"{stem_26}.E32_main.interval.packet.json"))
    tail_26 = load(Path(f"{stem_26}.E32_tail.interval.packet.json"))
    full_26 = load(Path(f"{stem_26}.E32_full.interval.packet.json"))
    assert nodal_26["selected_thimble"]["line_chart"] == "y"
    assert nodal_26["certified_node"]["incoming_closest_pair_zero_based"] == [0, 1]
    assert nodal_26["certified_node"]["jacobian_determinant_absolute_lower"] > 41283.3
    assert main_26["selected_thimble"]["near_node_colliding_pair_zero_based"] == [0, 1]
    assert main_26["validated_main_transport"]["accepted_step_count"] == 148
    assert main_26["validated_main_transport"]["rejected_step_count"] == 46
    assert close(
        main_26["validated_main_transport"]["uniform_integral_radius_upper"],
        1.330671149301234e-6,
    )
    assert main_26["polygonal_homotopy"]["detour_fraction"] == 0.2
    assert main_26["polygonal_homotopy"]["detour_signed_right_offset"] == 0.0
    assert main_26["polygonal_homotopy"]["return_fraction"] == 0.74
    assert main_26["polygonal_homotopy"]["other_critical_ball_clearance_lower"] > 0.00515
    assert tail_26["selected_thimble"]["cutoff_pair_zero_based"] == [0, 1]
    assert len(tail_26["regular_segments"]) == 384
    assert full_26["full_E32_thimble"]["floating_candidate_contained"]
    assert full_26["A134_radius_ledger"]["fallback_met"]

    stem_32 = PERIOD_DIRECTORY / "d032_selected_035"
    nodal_32 = load(Path(f"{stem_32}.nodal_factor.interval.packet.json"))
    main_32 = load(Path(f"{stem_32}.E32_main.interval.packet.json"))
    tail_32 = load(Path(f"{stem_32}.E32_tail.interval.packet.json"))
    full_32 = load(Path(f"{stem_32}.E32_full.interval.packet.json"))
    assert nodal_32["certified_node"]["pair_seed_method"] == (
        "unique closest pair at a deeper radial seed"
    )
    assert nodal_32["certified_node"]["pair_seed_epsilon"] == 1.0e-9
    assert nodal_32["certified_node"]["incoming_closest_pair_zero_based"] == [4, 5]
    assert nodal_32["certified_node"]["jacobian_determinant_absolute_lower"] > 56299.2
    assert main_32["selected_thimble"]["near_node_colliding_pair_zero_based"] == [4, 5]
    assert main_32["validated_main_transport"]["accepted_step_count"] == 100
    assert main_32["validated_main_transport"]["rejected_step_count"] == 33
    assert close(
        main_32["validated_main_transport"]["uniform_integral_radius_upper"],
        2.0334266570578483e-7,
    )
    assert main_32["polygonal_homotopy"]["detour_fraction"] == 0.45
    assert main_32["polygonal_homotopy"]["detour_signed_right_offset"] == -0.02
    assert main_32["polygonal_homotopy"]["return_fraction"] == 0.86
    assert main_32["polygonal_homotopy"]["other_critical_ball_clearance_lower"] > 0.01508
    assert tail_32["selected_thimble"]["cutoff_pair_zero_based"] == [4, 5]
    assert len(tail_32["regular_segments"]) == 384
    assert full_32["full_E32_thimble"]["floating_candidate_contained"]
    assert full_32["A134_radius_ledger"]["fallback_met"]

    stem_30 = PERIOD_DIRECTORY / "d030_selected_034"
    nodal_30 = load(Path(f"{stem_30}.nodal_factor.interval.packet.json"))
    main_30 = load(Path(f"{stem_30}.E32_main.interval.packet.json"))
    tail_30 = load(Path(f"{stem_30}.E32_tail.interval.packet.json"))
    full_30 = load(Path(f"{stem_30}.E32_full.interval.packet.json"))
    orientation_path = ROOT / main_30["authority"]["orientation_synchronization"]
    orientation_source = load(orientation_path)
    assert sha256(orientation_path) == main_30["authority"][
        "orientation_synchronization_sha256"
    ]
    assert orientation_source["strict_scope"][
        "compact_H1_holomorphic_rows_used_for_orientation"
    ] == 2
    assert orientation_source["strict_scope"][
        "higher_meromorphic_rows_used_for_orientation"
    ] == 0
    assert orientation_source["strict_scope"][
        "higher_meromorphic_rows_retain_puncture_lift_dependence"
    ]
    assert nodal_30["certified_node"]["incoming_closest_pair_zero_based"] == [4, 5]
    assert nodal_30["certified_node"]["jacobian_determinant_absolute_lower"] > 12500.7
    assert main_30["selected_thimble"]["near_node_colliding_pair_zero_based"] == [4, 5]
    assert main_30["validated_main_transport"]["accepted_step_count"] == 91
    assert main_30["validated_main_transport"]["rejected_step_count"] == 24
    assert close(
        main_30["validated_main_transport"]["uniform_integral_radius_upper"],
        6.576746775026099e-8,
    )
    assert main_30["polygonal_homotopy"]["detour_fraction"] == 0.25
    assert main_30["polygonal_homotopy"]["detour_signed_right_offset"] == 0.02
    assert main_30["polygonal_homotopy"]["return_fraction"] == 0.86
    assert main_30["polygonal_homotopy"]["other_critical_ball_clearance_lower"] > 0.01392
    assert main_30["orientation"]["selected_sign"] == -1
    assert main_30["orientation"]["compact_H1_holomorphic_component_count"] == 2
    assert not main_30["orientation"]["higher_meromorphic_rows_used_for_orientation"]
    assert close(
        main_30["orientation"]["selected_base_center_maximum_difference"],
        1.922947248965649e-10,
    )
    assert main_30["orientation"][
        "higher_meromorphic_puncture_lift_difference_diagnostic"
    ] > 11.5
    assert main_30["scope"]["compact_H1_orientation_synchronization_consumed"]
    assert main_30["scope"][
        "higher_meromorphic_puncture_lift_rows_excluded_from_orientation"
    ]
    assert tail_30["selected_thimble"]["cutoff_pair_zero_based"] == [4, 5]
    assert len(tail_30["regular_segments"]) == 384
    assert full_30["full_E32_thimble"]["floating_candidate_contained"]
    assert full_30["A134_radius_ledger"]["fallback_met"]

    stem_85 = PERIOD_DIRECTORY / "d085_selected_077"
    nodal_85 = load(Path(f"{stem_85}.nodal_factor.interval.packet.json"))
    main_85 = load(Path(f"{stem_85}.E32_main.interval.packet.json"))
    tail_85 = load(Path(f"{stem_85}.E32_tail.interval.packet.json"))
    full_85 = load(Path(f"{stem_85}.E32_full.interval.packet.json"))
    assert nodal_85["certified_node"]["incoming_closest_pair_zero_based"] == [1, 2]
    assert nodal_85["certified_node"]["jacobian_determinant_absolute_lower"] > 3277.99
    assert main_85["selected_thimble"]["near_node_colliding_pair_zero_based"] == [1, 2]
    assert main_85["selected_thimble"]["node_affinity_separation_margin_lower"] > 0.782
    assert main_85["validated_main_transport"]["accepted_step_count"] == 148
    assert main_85["validated_main_transport"]["rejected_step_count"] == 53
    assert close(
        main_85["validated_main_transport"]["minimum_accepted_step"],
        2.0904836687741756e-6,
    )
    assert close(
        main_85["validated_main_transport"]["uniform_integral_radius_upper"],
        1.1901906201071195e-5,
    )
    assert main_85["polygonal_homotopy"]["detour_fraction"] == 0.2
    assert main_85["polygonal_homotopy"]["detour_signed_right_offset"] == 0.0
    assert main_85["polygonal_homotopy"]["return_fraction"] == 0.7
    assert main_85["polygonal_homotopy"]["other_critical_ball_clearance_lower"] > 0.0030717
    assert main_85["orientation"]["selected_sign"] == 1
    assert main_85["orientation"]["selected_base_center_maximum_difference"] < 2.16e-10
    assert main_85["orientation"]["opposite_base_center_maximum_difference"] > 11.15
    assert main_85["scope"]["certified_nodal_pair_selector_consumed"]
    assert main_85["scope"]["certified_tail_cutoff_period_reuse_consumed"]
    assert main_85["scope"]["compressed_augmented_frame_consumed"]
    assert tail_85["selected_thimble"]["cutoff_pair_zero_based"] == [1, 2]
    assert len(tail_85["regular_segments"]) == 384
    assert full_85["full_E32_thimble"]["floating_candidate_contained"]
    assert full_85["A134_radius_ledger"]["fallback_met"]
    assert close(full_85["A134_radius_ledger"]["fallback_margin"], 4.4890291670103975e-6)

    stem_10 = PERIOD_DIRECTORY / "d010_selected_021"
    nodal_10 = load(Path(f"{stem_10}.nodal_factor.interval.packet.json"))
    main_10 = load(Path(f"{stem_10}.E32_main.interval.packet.json"))
    tail_10 = load(Path(f"{stem_10}.E32_tail.interval.packet.json"))
    full_10 = load(Path(f"{stem_10}.E32_full.interval.packet.json"))
    assert nodal_10["certified_node"]["incoming_closest_pair_zero_based"] == [1, 2]
    assert nodal_10["certified_node"]["jacobian_determinant_absolute_lower"] > 159124.5
    assert main_10["selected_thimble"]["near_node_colliding_pair_zero_based"] == [1, 2]
    assert main_10["selected_thimble"]["node_affinity_separation_margin_lower"] > 1.062
    assert main_10["validated_main_transport"]["accepted_step_count"] == 193
    assert main_10["validated_main_transport"]["rejected_step_count"] == 102
    assert close(
        main_10["validated_main_transport"]["minimum_accepted_step"],
        1.4826219580668807e-6,
    )
    assert close(
        main_10["validated_main_transport"]["uniform_integral_radius_upper"],
        9.198311075311998e-7,
    )
    assert main_10["polygonal_homotopy"]["detour_fraction"] == 0.2
    assert main_10["polygonal_homotopy"]["detour_signed_right_offset"] == -0.01
    assert main_10["polygonal_homotopy"]["return_fraction"] == 0.65
    assert main_10["polygonal_homotopy"]["other_critical_ball_clearance_lower"] > 0.0064859
    assert main_10["orientation"]["selected_sign"] == -1
    assert main_10["orientation"]["selected_base_center_maximum_difference"] < 6.21e-10
    assert main_10["orientation"]["opposite_base_center_maximum_difference"] > 0.282
    assert main_10["scope"]["certified_nodal_pair_selector_consumed"]
    assert main_10["scope"]["certified_tail_cutoff_period_reuse_consumed"]
    assert main_10["scope"]["uncompressed_physical_generator_zonotope_consumed"]
    assert tail_10["selected_thimble"]["cutoff_pair_zero_based"] == [1, 2]
    assert len(tail_10["regular_segments"]) == 384
    assert full_10["full_E32_thimble"]["floating_candidate_contained"]
    assert full_10["A134_radius_ledger"]["fallback_met"]
    assert close(full_10["A134_radius_ledger"]["fallback_margin"], 1.8525900473199315e-5)

    stem_12 = PERIOD_DIRECTORY / "d012_selected_017"
    nodal_12 = load(Path(f"{stem_12}.nodal_factor.interval.packet.json"))
    main_12 = load(Path(f"{stem_12}.E32_main.interval.packet.json"))
    tail_12 = load(Path(f"{stem_12}.E32_tail.interval.packet.json"))
    full_12 = load(Path(f"{stem_12}.E32_full.interval.packet.json"))
    assert nodal_12["certified_node"]["incoming_closest_pair_zero_based"] == [1, 3]
    assert nodal_12["certified_node"]["jacobian_determinant_absolute_lower"] > 3052969.8
    assert main_12["selected_thimble"]["near_node_colliding_pair_zero_based"] == [1, 3]
    assert main_12["selected_thimble"]["node_affinity_separation_margin_lower"] > 1.529
    assert main_12["validated_main_transport"]["accepted_step_count"] == 190
    assert main_12["validated_main_transport"]["rejected_step_count"] == 100
    assert close(
        main_12["validated_main_transport"]["uniform_integral_radius_upper"],
        5.743632409585513e-7,
    )
    assert main_12["polygonal_homotopy"]["detour_fraction"] == 0.32
    assert main_12["polygonal_homotopy"]["detour_signed_right_offset"] == 0.01
    assert main_12["polygonal_homotopy"]["return_fraction"] == 0.86
    assert main_12["polygonal_homotopy"]["other_critical_ball_clearance_lower"] > 0.0041798
    assert main_12["orientation"]["selected_sign"] == -1
    assert main_12["orientation"]["selected_base_center_maximum_difference"] < 6.01e-10
    assert main_12["orientation"]["opposite_base_center_maximum_difference"] > 0.282
    assert main_12["scope"]["certified_nodal_pair_selector_consumed"]
    assert main_12["scope"]["certified_tail_cutoff_period_reuse_consumed"]
    assert main_12["scope"]["uncompressed_physical_generator_zonotope_consumed"]
    assert tail_12["selected_thimble"]["cutoff_pair_zero_based"] == [1, 3]
    assert len(tail_12["regular_segments"]) == 384
    assert full_12["full_E32_thimble"]["floating_candidate_contained"]
    assert full_12["A134_radius_ledger"]["fallback_met"]
    assert close(full_12["A134_radius_ledger"]["fallback_margin"], 2.0778167770308571e-5)

    stem_17 = PERIOD_DIRECTORY / "d017_selected_022"
    nodal_17 = load(Path(f"{stem_17}.nodal_factor.interval.packet.json"))
    main_17 = load(Path(f"{stem_17}.E32_main.interval.packet.json"))
    tail_17 = load(Path(f"{stem_17}.E32_tail.interval.packet.json"))
    full_17 = load(Path(f"{stem_17}.E32_full.interval.packet.json"))
    assert nodal_17["certified_node"]["incoming_closest_pair_zero_based"] == [1, 2]
    assert nodal_17["certified_node"]["jacobian_determinant_absolute_lower"] > 41.878
    assert main_17["selected_thimble"]["near_node_colliding_pair_zero_based"] == [1, 2]
    assert main_17["selected_thimble"]["node_affinity_separation_margin_lower"] > 0.606
    assert main_17["validated_main_transport"]["accepted_step_count"] == 182
    assert main_17["validated_main_transport"]["rejected_step_count"] == 95
    assert close(
        main_17["validated_main_transport"]["uniform_integral_radius_upper"],
        3.831653826366047e-7,
    )
    assert main_17["polygonal_homotopy"]["detour_fraction"] == 0.45
    assert main_17["polygonal_homotopy"]["detour_signed_right_offset"] == 0.01
    assert main_17["polygonal_homotopy"]["return_fraction"] == 0.86
    assert main_17["polygonal_homotopy"]["other_critical_ball_clearance_lower"] > 0.0107324
    assert main_17["orientation"]["selected_sign"] == -1
    assert main_17["orientation"]["selected_base_center_maximum_difference"] < 2.42e-11
    assert main_17["orientation"]["opposite_base_center_maximum_difference"] > 0.550
    assert main_17["scope"]["certified_nodal_pair_selector_consumed"]
    assert main_17["scope"]["certified_tail_cutoff_period_reuse_consumed"]
    assert main_17["scope"]["uncompressed_physical_generator_zonotope_consumed"]
    assert tail_17["selected_thimble"]["cutoff_pair_zero_based"] == [1, 2]
    assert len(tail_17["regular_segments"]) == 384
    assert full_17["full_E32_thimble"]["floating_candidate_contained"]
    assert full_17["A134_radius_ledger"]["fallback_met"]
    assert close(full_17["A134_radius_ledger"]["fallback_margin"], 2.1214567424499748e-5)

    stem_51 = PERIOD_DIRECTORY / "d051_selected_062"
    nodal_51 = load(Path(f"{stem_51}.nodal_factor.interval.packet.json"))
    main_51 = load(Path(f"{stem_51}.E32_main.interval.packet.json"))
    tail_51 = load(Path(f"{stem_51}.E32_tail.interval.packet.json"))
    full_51 = load(Path(f"{stem_51}.E32_full.interval.packet.json"))
    assert nodal_51["certified_node"]["incoming_closest_pair_zero_based"] == [0, 1]
    assert nodal_51["certified_node"]["jacobian_determinant_absolute_lower"] > 525079.1
    assert main_51["selected_thimble"]["near_node_colliding_pair_zero_based"] == [0, 1]
    assert main_51["selected_thimble"]["node_affinity_separation_margin_lower"] > 1.269
    assert main_51["validated_main_transport"]["accepted_step_count"] == 259
    assert main_51["validated_main_transport"]["rejected_step_count"] == 153
    assert close(
        main_51["validated_main_transport"]["uniform_integral_radius_upper"],
        1.1786789306105185e-6,
    )
    assert main_51["polygonal_homotopy"]["detour_fraction"] == 0.2
    assert main_51["polygonal_homotopy"]["detour_signed_right_offset"] == 0.0
    assert main_51["polygonal_homotopy"]["return_fraction"] == 0.74
    assert main_51["polygonal_homotopy"]["other_critical_ball_clearance_lower"] > 0.00054346
    assert main_51["orientation"]["selected_sign"] == -1
    assert main_51["orientation"]["selected_base_center_maximum_difference"] < 1.99e-11
    assert main_51["orientation"]["opposite_base_center_maximum_difference"] > 0.663
    assert main_51["scope"]["certified_nodal_pair_selector_consumed"]
    assert main_51["scope"]["certified_tail_cutoff_period_reuse_consumed"]
    assert main_51["scope"]["uncompressed_physical_generator_zonotope_consumed"]
    assert tail_51["selected_thimble"]["cutoff_pair_zero_based"] == [0, 1]
    assert len(tail_51["regular_segments"]) == 384
    assert full_51["full_E32_thimble"]["floating_candidate_contained"]
    assert full_51["A134_radius_ledger"]["fallback_met"]
    assert close(full_51["A134_radius_ledger"]["fallback_margin"], 2.1067082088555751e-5)

    stem_55 = PERIOD_DIRECTORY / "d055_selected_086"
    nodal_55 = load(Path(f"{stem_55}.nodal_factor.interval.packet.json"))
    main_55 = load(Path(f"{stem_55}.E32_main.interval.packet.json"))
    tail_55 = load(Path(f"{stem_55}.E32_tail.interval.packet.json"))
    full_55 = load(Path(f"{stem_55}.E32_full.interval.packet.json"))
    assert nodal_55["certified_node"]["incoming_closest_pair_zero_based"] == [3, 4]
    assert nodal_55["certified_node"]["jacobian_determinant_absolute_lower"] > 694082191.3
    assert main_55["selected_thimble"]["near_node_colliding_pair_zero_based"] == [3, 4]
    assert main_55["selected_thimble"]["node_affinity_separation_margin_lower"] > 0.856
    assert main_55["validated_main_transport"]["accepted_step_count"] == 243
    assert main_55["validated_main_transport"]["rejected_step_count"] == 145
    assert close(
        main_55["validated_main_transport"]["uniform_integral_radius_upper"],
        1.3338361979199125e-6,
    )
    assert main_55["polygonal_homotopy"]["detour_fraction"] == 0.6
    assert main_55["polygonal_homotopy"]["detour_signed_right_offset"] == 0.01
    assert main_55["polygonal_homotopy"]["return_fraction"] == 0.65
    assert main_55["polygonal_homotopy"]["other_critical_ball_clearance_lower"] > 0.0059786
    assert main_55["orientation"]["selected_sign"] == -1
    assert main_55["orientation"]["selected_base_center_maximum_difference"] < 7.04e-10
    assert main_55["orientation"]["opposite_base_center_maximum_difference"] > 24.8
    assert main_55["scope"]["certified_nodal_pair_selector_consumed"]
    assert main_55["scope"]["certified_tail_cutoff_period_reuse_consumed"]
    assert main_55["scope"]["uncompressed_physical_generator_zonotope_consumed"]
    assert tail_55["selected_thimble"]["cutoff_pair_zero_based"] == [3, 4]
    assert len(tail_55["regular_segments"]) == 384
    assert full_55["full_E32_thimble"]["floating_candidate_contained"]
    assert full_55["A134_radius_ledger"]["fallback_met"]
    assert close(full_55["A134_radius_ledger"]["fallback_margin"], 1.8438725711567756e-5)

    stem_34 = PERIOD_DIRECTORY / "d034_selected_007"
    nodal_34 = load(Path(f"{stem_34}.nodal_factor.interval.packet.json"))
    main_34 = load(Path(f"{stem_34}.E32_main.interval.packet.json"))
    tail_34 = load(Path(f"{stem_34}.E32_tail.interval.packet.json"))
    full_34 = load(Path(f"{stem_34}.E32_full.interval.packet.json"))
    assert nodal_34["certified_node"]["incoming_closest_pair_zero_based"] == [4, 5]
    assert nodal_34["certified_node"]["jacobian_determinant_absolute_lower"] > 33208421.4
    assert main_34["selected_thimble"]["near_node_colliding_pair_zero_based"] == [4, 5]
    assert main_34["selected_thimble"]["node_affinity_separation_margin_lower"] > 1.224
    assert main_34["validated_main_transport"]["accepted_step_count"] == 288
    assert main_34["validated_main_transport"]["rejected_step_count"] == 183
    assert close(
        main_34["validated_main_transport"]["uniform_integral_radius_upper"],
        2.20656062847174e-6,
    )
    assert main_34["polygonal_homotopy"]["detour_fraction"] == 0.2
    assert main_34["polygonal_homotopy"]["detour_signed_right_offset"] == 0.0
    assert main_34["polygonal_homotopy"]["return_fraction"] == 0.74
    assert main_34["polygonal_homotopy"]["other_critical_ball_clearance_lower"] > 0.00014908
    assert main_34["orientation"]["selected_sign"] == 1
    assert main_34["orientation"]["selected_base_center_maximum_difference"] < 1.94e-9
    assert main_34["orientation"]["opposite_base_center_maximum_difference"] > 11.34
    assert main_34["scope"]["certified_nodal_pair_selector_consumed"]
    assert main_34["scope"]["certified_tail_cutoff_period_reuse_consumed"]
    assert main_34["scope"]["uncompressed_physical_generator_zonotope_consumed"]
    assert tail_34["selected_thimble"]["cutoff_pair_zero_based"] == [4, 5]
    assert len(tail_34["regular_segments"]) == 768
    assert full_34["full_E32_thimble"]["floating_candidate_contained"]
    assert full_34["A134_radius_ledger"]["fallback_met"]
    assert close(full_34["A134_radius_ledger"]["fallback_margin"], 1.4439062511818106e-5)

    stem_59 = PERIOD_DIRECTORY / "d059_selected_042"
    nodal_59 = load(Path(f"{stem_59}.nodal_factor.interval.packet.json"))
    main_59 = load(Path(f"{stem_59}.E32_main.interval.packet.json"))
    tail_59 = load(Path(f"{stem_59}.E32_tail.interval.packet.json"))
    full_59 = load(Path(f"{stem_59}.E32_full.interval.packet.json"))
    assert nodal_59["selected_thimble"]["line_chart"] == "z"
    assert nodal_59["certified_node"]["incoming_closest_pair_zero_based"] == [0, 1]
    assert nodal_59["certified_node"]["jacobian_determinant_absolute_lower"] > 16.1298
    assert main_59["selected_thimble"]["near_node_colliding_pair_zero_based"] == [0, 1]
    assert main_59["selected_thimble"]["node_affinity_separation_margin_lower"] > 0.8467
    assert main_59["validated_main_transport"]["accepted_step_count"] == 74
    assert main_59["validated_main_transport"]["rejected_step_count"] == 21
    assert close(
        main_59["validated_main_transport"]["uniform_integral_radius_upper"],
        8.601425856598232e-8,
    )
    assert main_59["polygonal_homotopy"]["detour_fraction"] == 0.2
    assert main_59["polygonal_homotopy"]["detour_signed_right_offset"] == 0.0
    assert main_59["polygonal_homotopy"]["return_fraction"] == 0.82
    assert main_59["polygonal_homotopy"]["other_critical_ball_clearance_lower"] > 0.03020965
    assert main_59["polygonal_homotopy"]["selected_z_chart_zero_clearance_lower"] > 0.2562
    assert main_59["orientation"]["selected_sign"] == -1
    assert main_59["orientation"]["selected_base_center_maximum_difference"] < 4.36e-12
    assert main_59["orientation"]["opposite_base_center_maximum_difference"] > 1.606
    assert main_59["scope"]["A123_projective_line_chart_covariance_consumed"]
    assert main_59["scope"]["certified_nodal_pair_selector_consumed"]
    assert main_59["scope"]["certified_tail_cutoff_period_reuse_consumed"]
    assert main_59["scope"]["uncompressed_physical_generator_zonotope_consumed"]
    assert tail_59["selected_thimble"]["cutoff_pair_zero_based"] == [0, 1]
    assert len(tail_59["regular_segments"]) == 384
    assert full_59["full_E32_thimble"]["floating_candidate_contained"]
    assert full_59["A134_radius_ledger"]["fallback_met"]
    assert close(full_59["A134_radius_ledger"]["fallback_margin"], 2.2961739791727738e-5)

    stem_31 = PERIOD_DIRECTORY / "d031_selected_048"
    nodal_31 = load(Path(f"{stem_31}.nodal_factor.interval.packet.json"))
    main_31 = load(Path(f"{stem_31}.E32_main.interval.packet.json"))
    tail_31 = load(Path(f"{stem_31}.E32_tail.interval.packet.json"))
    full_31 = load(Path(f"{stem_31}.E32_full.interval.packet.json"))
    assert nodal_31["selected_thimble"]["line_chart"] == "z"
    assert nodal_31["certified_node"]["incoming_closest_pair_zero_based"] == [4, 5]
    assert nodal_31["certified_node"]["jacobian_determinant_absolute_lower"] > 670.69
    assert main_31["selected_thimble"]["near_node_colliding_pair_zero_based"] == [4, 5]
    assert main_31["selected_thimble"]["node_affinity_separation_margin_lower"] > 0.6888
    assert main_31["validated_main_transport"]["accepted_step_count"] == 132
    assert main_31["validated_main_transport"]["rejected_step_count"] == 67
    assert close(
        main_31["validated_main_transport"]["uniform_integral_radius_upper"],
        1.816473192839754e-7,
    )
    assert main_31["polygonal_homotopy"]["detour_fraction"] == 0.2
    assert main_31["polygonal_homotopy"]["detour_signed_right_offset"] == 0.0
    assert main_31["polygonal_homotopy"]["return_fraction"] == 0.65
    assert main_31["polygonal_homotopy"]["other_critical_ball_clearance_lower"] > 0.02959575
    assert main_31["polygonal_homotopy"]["selected_z_chart_zero_clearance_lower"] > 0.2562
    assert main_31["orientation"]["selected_sign"] == -1
    assert main_31["orientation"]["selected_base_center_maximum_difference"] < 2.86e-10
    assert main_31["orientation"]["opposite_base_center_maximum_difference"] > 3.91
    assert main_31["scope"]["A123_projective_line_chart_covariance_consumed"]
    assert main_31["scope"]["certified_nodal_pair_selector_consumed"]
    assert main_31["scope"]["certified_tail_cutoff_period_reuse_consumed"]
    assert main_31["scope"]["uncompressed_physical_generator_zonotope_consumed"]
    assert tail_31["selected_thimble"]["cutoff_pair_zero_based"] == [4, 5]
    assert len(tail_31["regular_segments"]) == 384
    assert full_31["full_E32_thimble"]["floating_candidate_contained"]
    assert full_31["A134_radius_ledger"]["fallback_met"]
    assert close(full_31["A134_radius_ledger"]["fallback_margin"], 2.2819092394278002e-5)

    stem_39 = PERIOD_DIRECTORY / "d039_selected_037"
    nodal_39 = load(Path(f"{stem_39}.nodal_factor.interval.packet.json"))
    main_39 = load(Path(f"{stem_39}.E32_main.interval.packet.json"))
    tail_39 = load(Path(f"{stem_39}.E32_tail.interval.packet.json"))
    full_39 = load(Path(f"{stem_39}.E32_full.interval.packet.json"))
    assert nodal_39["selected_thimble"]["line_chart"] == "z"
    assert nodal_39["certified_node"]["incoming_closest_pair_zero_based"] == [1, 2]
    assert nodal_39["certified_node"]["jacobian_determinant_absolute_lower"] > 6.9138
    assert main_39["selected_thimble"]["near_node_colliding_pair_zero_based"] == [1, 2]
    assert main_39["selected_thimble"]["node_affinity_separation_margin_lower"] > 0.5216
    assert main_39["validated_main_transport"]["accepted_step_count"] == 103
    assert main_39["validated_main_transport"]["rejected_step_count"] == 32
    assert close(
        main_39["validated_main_transport"]["uniform_integral_radius_upper"],
        1.0881261871947691e-7,
    )
    assert main_39["polygonal_homotopy"]["detour_fraction"] == 0.45
    assert main_39["polygonal_homotopy"]["detour_signed_right_offset"] == -0.01
    assert main_39["polygonal_homotopy"]["return_fraction"] == 0.86
    assert main_39["polygonal_homotopy"]["other_critical_ball_clearance_lower"] > 0.03370999
    assert main_39["polygonal_homotopy"]["selected_z_chart_zero_clearance_lower"] > 0.2562
    assert main_39["orientation"]["selected_sign"] == 1
    assert main_39["orientation"]["selected_base_center_maximum_difference"] < 2.5e-11
    assert main_39["orientation"]["opposite_base_center_maximum_difference"] > 3.064
    assert main_39["scope"]["A123_projective_line_chart_covariance_consumed"]
    assert main_39["scope"]["certified_nodal_pair_selector_consumed"]
    assert main_39["scope"]["certified_tail_cutoff_period_reuse_consumed"]
    assert main_39["scope"]["uncompressed_physical_generator_zonotope_consumed"]
    assert tail_39["selected_thimble"]["cutoff_pair_zero_based"] == [1, 2]
    assert len(tail_39["regular_segments"]) == 96
    assert full_39["full_E32_thimble"]["floating_candidate_contained"]
    assert full_39["A134_radius_ledger"]["fallback_met"]
    assert close(full_39["A134_radius_ledger"]["fallback_margin"], 2.1526022039487131e-5)

    stem_14 = PERIOD_DIRECTORY / "d014_selected_059"
    nodal_14 = load(Path(f"{stem_14}.nodal_factor.interval.packet.json"))
    main_14 = load(Path(f"{stem_14}.E32_main.interval.packet.json"))
    tail_14 = load(Path(f"{stem_14}.E32_tail.interval.packet.json"))
    full_14 = load(Path(f"{stem_14}.E32_full.interval.packet.json"))
    assert nodal_14["selected_thimble"]["line_chart"] == "z"
    assert nodal_14["certified_node"]["incoming_closest_pair_zero_based"] == [3, 4]
    assert nodal_14["certified_node"]["jacobian_determinant_absolute_lower"] > 139.58
    assert main_14["selected_thimble"]["near_node_colliding_pair_zero_based"] == [3, 4]
    assert main_14["selected_thimble"]["node_affinity_separation_margin_lower"] > 1.4209
    assert main_14["validated_main_transport"]["accepted_step_count"] == 75
    assert main_14["validated_main_transport"]["rejected_step_count"] == 23
    assert close(
        main_14["validated_main_transport"]["uniform_integral_radius_upper"],
        1.2239440876842448e-7,
    )
    assert main_14["polygonal_homotopy"]["detour_fraction"] == 0.2
    assert main_14["polygonal_homotopy"]["detour_signed_right_offset"] == 0.0
    assert main_14["polygonal_homotopy"]["return_fraction"] == 0.65
    assert main_14["polygonal_homotopy"]["other_critical_ball_clearance_lower"] > 0.04818849
    assert main_14["polygonal_homotopy"]["selected_z_chart_zero_clearance_lower"] > 0.2562
    assert main_14["orientation"]["selected_sign"] == 1
    assert main_14["orientation"]["selected_base_center_maximum_difference"] < 5.28e-12
    assert main_14["orientation"]["opposite_base_center_maximum_difference"] > 0.9757
    assert main_14["scope"]["A123_projective_line_chart_covariance_consumed"]
    assert main_14["scope"]["certified_nodal_pair_selector_consumed"]
    assert main_14["scope"]["certified_tail_cutoff_period_reuse_consumed"]
    assert main_14["scope"]["uncompressed_physical_generator_zonotope_consumed"]
    assert tail_14["selected_thimble"]["cutoff_pair_zero_based"] == [3, 4]
    assert len(tail_14["regular_segments"]) == 768
    assert full_14["full_E32_thimble"]["floating_candidate_contained"]
    assert full_14["A134_radius_ledger"]["fallback_met"]
    assert close(full_14["A134_radius_ledger"]["fallback_margin"], 2.2901959166388892e-5)

    stem_75 = PERIOD_DIRECTORY / "d075_selected_067"
    nodal_75 = load(Path(f"{stem_75}.nodal_factor.interval.packet.json"))
    main_75 = load(Path(f"{stem_75}.E32_main.interval.packet.json"))
    tail_75 = load(Path(f"{stem_75}.E32_tail.interval.packet.json"))
    full_75 = load(Path(f"{stem_75}.E32_full.interval.packet.json"))
    assert nodal_75["selected_thimble"]["line_chart"] == "z"
    assert nodal_75["certified_node"]["incoming_closest_pair_zero_based"] == [3, 4]
    assert nodal_75["certified_node"]["jacobian_determinant_absolute_lower"] > 1.297e6
    assert main_75["selected_thimble"]["near_node_colliding_pair_zero_based"] == [3, 4]
    assert main_75["selected_thimble"]["node_affinity_separation_margin_lower"] > 3.5514
    assert main_75["validated_main_transport"]["accepted_step_count"] == 149
    assert main_75["validated_main_transport"]["rejected_step_count"] == 55
    assert close(
        main_75["validated_main_transport"]["uniform_integral_radius_upper"],
        2.127205331505899e-7,
    )
    assert main_75["polygonal_homotopy"]["detour_fraction"] == 0.2
    assert main_75["polygonal_homotopy"]["detour_signed_right_offset"] == 0.0
    assert main_75["polygonal_homotopy"]["return_fraction"] == 0.65
    assert main_75["polygonal_homotopy"]["other_critical_ball_clearance_lower"] > 0.02104034
    assert main_75["polygonal_homotopy"]["selected_z_chart_zero_clearance_lower"] > 0.2355
    assert main_75["orientation"]["selected_sign"] == 1
    assert main_75["orientation"]["selected_base_center_maximum_difference"] < 1.824e-10
    assert main_75["orientation"]["opposite_base_center_maximum_difference"] > 1.922
    assert main_75["scope"]["A123_projective_line_chart_covariance_consumed"]
    assert main_75["scope"]["certified_nodal_pair_selector_consumed"]
    assert main_75["scope"]["certified_tail_cutoff_period_reuse_consumed"]
    assert main_75["scope"]["uncompressed_physical_generator_zonotope_consumed"]
    assert tail_75["selected_thimble"]["cutoff_pair_zero_based"] == [3, 4]
    assert len(tail_75["regular_segments"]) == 384
    assert full_75["full_E32_thimble"]["floating_candidate_contained"]
    assert full_75["A134_radius_ledger"]["fallback_met"]
    assert close(full_75["A134_radius_ledger"]["fallback_margin"], 1.6957870564616357e-5)

    stem_18 = PERIOD_DIRECTORY / "d018_selected_054"
    nodal_18 = load(Path(f"{stem_18}.nodal_factor.interval.packet.json"))
    main_18 = load(Path(f"{stem_18}.E32_main.interval.packet.json"))
    tail_18 = load(Path(f"{stem_18}.E32_tail.interval.packet.json"))
    full_18 = load(Path(f"{stem_18}.E32_full.interval.packet.json"))
    assert nodal_18["selected_thimble"]["line_chart"] == "z"
    assert nodal_18["certified_node"]["incoming_closest_pair_zero_based"] == [4, 5]
    assert nodal_18["certified_node"]["jacobian_determinant_absolute_lower"] > 471609.6
    assert main_18["selected_thimble"]["near_node_colliding_pair_zero_based"] == [4, 5]
    assert main_18["selected_thimble"]["node_affinity_separation_margin_lower"] > 2.9568
    assert main_18["validated_main_transport"]["accepted_step_count"] == 111
    assert main_18["validated_main_transport"]["rejected_step_count"] == 55
    assert close(
        main_18["validated_main_transport"]["uniform_integral_radius_upper"],
        1.1239108844990107e-7,
    )
    assert main_18["polygonal_homotopy"]["detour_fraction"] == 0.45
    assert main_18["polygonal_homotopy"]["detour_signed_right_offset"] == -0.01
    assert main_18["polygonal_homotopy"]["return_fraction"] == 0.86
    assert main_18["polygonal_homotopy"]["other_critical_ball_clearance_lower"] > 0.02032832
    assert main_18["polygonal_homotopy"]["selected_z_chart_zero_clearance_lower"] > 0.2562
    assert main_18["orientation"]["selected_sign"] == -1
    assert main_18["orientation"]["selected_base_center_maximum_difference"] < 7.88e-11
    assert main_18["orientation"]["opposite_base_center_maximum_difference"] > 4.28
    assert main_18["scope"]["A123_projective_line_chart_covariance_consumed"]
    assert main_18["scope"]["certified_nodal_pair_selector_consumed"]
    assert main_18["scope"]["certified_tail_cutoff_period_reuse_consumed"]
    assert main_18["scope"]["uncompressed_physical_generator_zonotope_consumed"]
    assert tail_18["selected_thimble"]["cutoff_pair_zero_based"] == [4, 5]
    assert len(tail_18["regular_segments"]) == 384
    assert full_18["full_E32_thimble"]["floating_candidate_contained"]
    assert full_18["A134_radius_ledger"]["fallback_met"]
    assert close(full_18["A134_radius_ledger"]["fallback_margin"], 2.168482826987524e-5)

    stem_1 = PERIOD_DIRECTORY / "d001_selected_033"
    nodal_1 = load(Path(f"{stem_1}.nodal_factor.interval.packet.json"))
    main_1 = load(Path(f"{stem_1}.E32_main.interval.packet.json"))
    tail_1 = load(Path(f"{stem_1}.E32_tail.interval.packet.json"))
    full_1 = load(Path(f"{stem_1}.E32_full.interval.packet.json"))
    assert nodal_1["selected_thimble"]["line_chart"] == "z"
    assert nodal_1["certified_node"]["incoming_closest_pair_zero_based"] == [0, 1]
    assert nodal_1["certified_node"]["jacobian_determinant_absolute_lower"] > 3472.4
    assert main_1["selected_thimble"]["near_node_colliding_pair_zero_based"] == [0, 1]
    assert main_1["selected_thimble"]["node_affinity_separation_margin_lower"] > 0.5866
    assert main_1["validated_main_transport"]["accepted_step_count"] == 117
    assert main_1["validated_main_transport"]["rejected_step_count"] == 36
    assert close(
        main_1["validated_main_transport"]["uniform_integral_radius_upper"],
        4.5844626040661814e-6,
    )
    assert main_1["polygonal_homotopy"]["detour_fraction"] == 0.55
    assert main_1["polygonal_homotopy"]["detour_signed_right_offset"] == 0.03
    assert main_1["polygonal_homotopy"]["return_fraction"] == 0.86
    assert main_1["polygonal_homotopy"]["other_critical_ball_clearance_lower"] > 0.06054403
    assert main_1["polygonal_homotopy"]["selected_z_chart_zero_clearance_lower"] > 0.1614
    assert main_1["orientation"]["selected_sign"] == -1
    assert main_1["orientation"]["selected_base_center_maximum_difference"] < 8.05e-11
    assert main_1["orientation"]["opposite_base_center_maximum_difference"] > 4.28
    assert main_1["scope"]["A123_projective_line_chart_covariance_consumed"]
    assert main_1["scope"]["certified_nodal_pair_selector_consumed"]
    assert main_1["scope"]["certified_tail_cutoff_period_reuse_consumed"]
    assert main_1["scope"]["uncompressed_physical_generator_zonotope_consumed"]
    assert tail_1["selected_thimble"]["cutoff_pair_zero_based"] == [0, 1]
    assert len(tail_1["regular_segments"]) == 384
    assert full_1["full_E32_thimble"]["floating_candidate_contained"]
    assert full_1["A134_radius_ledger"]["fallback_met"]
    assert close(full_1["A134_radius_ledger"]["fallback_margin"], 1.6056692502664689e-5)

    stem_46 = PERIOD_DIRECTORY / "d046_selected_045"
    nodal_46 = load(Path(f"{stem_46}.nodal_factor.interval.packet.json"))
    main_46 = load(Path(f"{stem_46}.E32_main.interval.packet.json"))
    tail_46 = load(Path(f"{stem_46}.E32_tail.interval.packet.json"))
    full_46 = load(Path(f"{stem_46}.E32_full.interval.packet.json"))
    assert nodal_46["selected_thimble"]["line_chart"] == "z"
    assert nodal_46["certified_node"]["incoming_closest_pair_zero_based"] == [1, 2]
    assert nodal_46["certified_node"]["jacobian_determinant_absolute_lower"] > 4.9849
    assert nodal_46["local_weierstrass_factor"]["quartic_at_double_root_absolute_lower"] > 2.9705
    assert nodal_46["local_weierstrass_factor"]["hensel_jacobian_determinant_absolute_lower"] > 8.8243
    assert main_46["selected_thimble"]["near_node_colliding_pair_zero_based"] == [1, 2]
    assert main_46["selected_thimble"]["node_affinity_separation_margin_lower"] > 0.4151
    assert main_46["validated_main_transport"]["accepted_step_count"] == 164
    assert main_46["validated_main_transport"]["rejected_step_count"] == 66
    assert close(
        main_46["validated_main_transport"]["uniform_integral_radius_upper"],
        6.883023908842079e-7,
    )
    assert main_46["polygonal_homotopy"]["detour_fraction"] == 0.45
    assert main_46["polygonal_homotopy"]["detour_signed_right_offset"] == 0.02
    assert main_46["polygonal_homotopy"]["return_fraction"] == 0.7
    assert main_46["polygonal_homotopy"]["other_critical_ball_clearance_lower"] > 0.0295997
    assert main_46["polygonal_homotopy"]["selected_z_chart_zero_clearance_lower"] > 0.08722
    assert main_46["polygonal_homotopy"]["elliptic_infinity_clearance_lower"] > 0.3455
    assert main_46["orientation"]["selected_sign"] == 1
    assert main_46["orientation"]["selected_base_center_maximum_difference"] < 5.30e-11
    assert main_46["orientation"]["opposite_base_center_maximum_difference"] > 1.606
    assert main_46["scope"]["A123_projective_line_chart_covariance_consumed"]
    assert main_46["scope"]["certified_nodal_pair_selector_consumed"]
    assert main_46["scope"]["certified_tail_cutoff_period_reuse_consumed"]
    assert main_46["scope"]["uncompressed_physical_generator_zonotope_consumed"]
    assert tail_46["selected_thimble"]["cutoff_pair_zero_based"] == [1, 2]
    assert len(tail_46["regular_segments"]) == 768
    assert close(tail_46["E32_endpoint_tail"]["interval_radius_upper"], 1.0406598907053424e-6)
    assert close(tail_46["node_segment"]["absolute_bound"]["contribution_radius_upper"], 5.465056610379216e-10)
    assert full_46["full_E32_thimble"]["floating_candidate_contained"]
    assert full_46["A134_radius_ledger"]["fallback_met"]
    assert close(full_46["full_E32_thimble"]["interval_radius_upper"], 2.0140664531709267e-6)
    assert close(full_46["full_E32_thimble"]["floating_candidate_center_difference"], 2.99585313022337e-7)
    assert close(full_46["A134_radius_ledger"]["fallback_margin"], 2.1072535475630998e-5)

    stem_89 = PERIOD_DIRECTORY / "d089_selected_032"
    nodal_89 = load(Path(f"{stem_89}.nodal_factor.interval.packet.json"))
    main_89 = load(Path(f"{stem_89}.E32_main.interval.packet.json"))
    tail_89 = load(Path(f"{stem_89}.E32_tail.interval.packet.json"))
    full_89 = load(Path(f"{stem_89}.E32_full.interval.packet.json"))
    assert nodal_89["selected_thimble"]["line_chart"] == "z"
    assert nodal_89["certified_node"]["incoming_closest_pair_zero_based"] == [1, 2]
    assert nodal_89["certified_node"]["jacobian_determinant_absolute_lower"] > 82.9402
    assert nodal_89["local_weierstrass_factor"]["quartic_at_double_root_absolute_lower"] > 3.5514
    assert nodal_89["local_weierstrass_factor"]["hensel_jacobian_determinant_absolute_lower"] > 12.6129
    assert main_89["selected_thimble"]["near_node_colliding_pair_zero_based"] == [1, 2]
    assert main_89["selected_thimble"]["node_affinity_separation_margin_lower"] > 0.4415
    assert main_89["validated_main_transport"]["accepted_step_count"] == 71
    assert main_89["validated_main_transport"]["rejected_step_count"] == 16
    assert close(
        main_89["validated_main_transport"]["uniform_integral_radius_upper"],
        2.9346360173223173e-7,
    )
    assert main_89["polygonal_homotopy"]["detour_fraction"] == 0.35
    assert main_89["polygonal_homotopy"]["detour_signed_right_offset"] == 0.0
    assert main_89["polygonal_homotopy"]["return_fraction"] == 0.7
    assert main_89["polygonal_homotopy"]["other_critical_ball_clearance_lower"] > 0.0331755
    assert main_89["polygonal_homotopy"]["selected_z_chart_zero_clearance_lower"] > 0.2562
    assert main_89["polygonal_homotopy"]["elliptic_infinity_clearance_lower"] > 0.3535
    assert main_89["orientation"]["selected_sign"] == -1
    assert main_89["orientation"]["selected_base_center_maximum_difference"] < 1.31e-12
    assert main_89["orientation"]["opposite_base_center_maximum_difference"] > 2.104
    assert main_89["scope"]["A123_projective_line_chart_covariance_consumed"]
    assert main_89["scope"]["certified_nodal_pair_selector_consumed"]
    assert main_89["scope"]["certified_tail_cutoff_period_reuse_consumed"]
    assert main_89["scope"]["uncompressed_physical_generator_zonotope_consumed"]
    assert tail_89["selected_thimble"]["cutoff_pair_zero_based"] == [1, 2]
    assert len(tail_89["regular_segments"]) == 384
    assert close(tail_89["E32_endpoint_tail"]["interval_radius_upper"], 2.1323743014389777e-9)
    assert close(tail_89["node_segment"]["absolute_bound"]["contribution_radius_upper"], 6.794539247640537e-11)
    assert full_89["full_E32_thimble"]["floating_candidate_contained"]
    assert full_89["A134_radius_ledger"]["fallback_met"]
    assert close(full_89["full_E32_thimble"]["interval_radius_upper"], 4.171525822549427e-7)
    assert close(full_89["full_E32_thimble"]["floating_candidate_center_difference"], 4.810576908653842e-11)
    assert close(full_89["A134_radius_ledger"]["fallback_margin"], 2.2669449346546984e-5)

    stem_69 = PERIOD_DIRECTORY / "d069_selected_078"
    nodal_69 = load(Path(f"{stem_69}.nodal_factor.interval.packet.json"))
    main_69 = load(Path(f"{stem_69}.E32_main.interval.packet.json"))
    tail_69 = load(Path(f"{stem_69}.E32_tail.interval.packet.json"))
    full_69 = load(Path(f"{stem_69}.E32_full.interval.packet.json"))
    assert nodal_69["selected_thimble"]["line_chart"] == "z"
    assert nodal_69["certified_node"]["incoming_closest_pair_zero_based"] == [3, 4]
    assert nodal_69["certified_node"]["jacobian_determinant_absolute_lower"] > 859.512
    assert nodal_69["local_weierstrass_factor"]["quartic_at_double_root_absolute_lower"] > 6.5749
    assert nodal_69["local_weierstrass_factor"]["hensel_jacobian_determinant_absolute_lower"] > 43.229
    assert main_69["selected_thimble"]["near_node_colliding_pair_zero_based"] == [3, 4]
    assert main_69["selected_thimble"]["node_affinity_separation_margin_lower"] > 0.5297
    assert main_69["validated_main_transport"]["accepted_step_count"] == 138
    assert main_69["validated_main_transport"]["rejected_step_count"] == 37
    assert close(
        main_69["validated_main_transport"]["uniform_integral_radius_upper"],
        3.0482279579327836e-7,
    )
    assert main_69["polygonal_homotopy"]["detour_fraction"] == 0.35
    assert main_69["polygonal_homotopy"]["detour_signed_right_offset"] == -0.02
    assert main_69["polygonal_homotopy"]["return_fraction"] == 0.7
    assert main_69["polygonal_homotopy"]["other_critical_ball_clearance_lower"] > 0.0303757
    assert main_69["polygonal_homotopy"]["selected_z_chart_zero_clearance_lower"] > 0.2562
    assert main_69["polygonal_homotopy"]["elliptic_infinity_clearance_lower"] > 0.3535
    assert main_69["orientation"]["selected_sign"] == -1
    assert main_69["orientation"]["selected_base_center_maximum_difference"] < 4.91e-11
    assert main_69["orientation"]["opposite_base_center_maximum_difference"] > 0.975
    assert main_69["scope"]["A123_projective_line_chart_covariance_consumed"]
    assert main_69["scope"]["certified_nodal_pair_selector_consumed"]
    assert main_69["scope"]["certified_tail_cutoff_period_reuse_consumed"]
    assert main_69["scope"]["uncompressed_physical_generator_zonotope_consumed"]
    assert tail_69["selected_thimble"]["cutoff_pair_zero_based"] == [3, 4]
    assert len(tail_69["regular_segments"]) == 384
    assert close(tail_69["E32_endpoint_tail"]["interval_radius_upper"], 9.208371682944972e-7)
    assert close(tail_69["node_segment"]["absolute_bound"]["contribution_radius_upper"], 1.9123613565104339e-10)
    assert full_69["full_E32_thimble"]["floating_candidate_contained"]
    assert full_69["A134_radius_ledger"]["fallback_met"]
    assert close(full_69["full_E32_thimble"]["interval_radius_upper"], 1.3519217159085886e-6)
    assert close(full_69["full_E32_thimble"]["floating_candidate_center_difference"], 3.171560931237816e-8)
    assert close(full_69["A134_radius_ledger"]["fallback_margin"], 2.1734680212893338e-5)

    stem_50 = PERIOD_DIRECTORY / "d050_selected_047"
    nodal_50 = load(Path(f"{stem_50}.nodal_factor.interval.packet.json"))
    main_50 = load(Path(f"{stem_50}.E32_main.interval.packet.json"))
    tail_50 = load(Path(f"{stem_50}.E32_tail.interval.packet.json"))
    full_50 = load(Path(f"{stem_50}.E32_full.interval.packet.json"))
    assert nodal_50["selected_thimble"]["line_chart"] == "z"
    assert nodal_50["certified_node"]["incoming_closest_pair_zero_based"] == [1, 2]
    assert nodal_50["certified_node"]["jacobian_determinant_absolute_lower"] > 3.2835
    assert nodal_50["local_weierstrass_factor"]["quartic_at_double_root_absolute_lower"] > 2.5918
    assert nodal_50["local_weierstrass_factor"]["hensel_jacobian_determinant_absolute_lower"] > 6.7177
    assert main_50["selected_thimble"]["near_node_colliding_pair_zero_based"] == [1, 2]
    assert main_50["selected_thimble"]["node_affinity_separation_margin_lower"] > 1.1697
    assert main_50["validated_main_transport"]["accepted_step_count"] == 92
    assert main_50["validated_main_transport"]["rejected_step_count"] == 30
    assert close(
        main_50["validated_main_transport"]["uniform_integral_radius_upper"],
        1.258544559744545e-7,
    )
    assert main_50["polygonal_homotopy"]["detour_fraction"] == 0.2
    assert main_50["polygonal_homotopy"]["detour_signed_right_offset"] == -0.01
    assert main_50["polygonal_homotopy"]["return_fraction"] == 0.86
    assert main_50["polygonal_homotopy"]["other_critical_ball_clearance_lower"] > 0.0209355
    assert main_50["polygonal_homotopy"]["selected_z_chart_zero_clearance_lower"] > 0.2562
    assert main_50["polygonal_homotopy"]["elliptic_infinity_clearance_lower"] > 0.3535
    assert main_50["orientation"]["selected_sign"] == -1
    assert main_50["orientation"]["selected_base_center_maximum_difference"] < 4.15e-11
    assert main_50["orientation"]["opposite_base_center_maximum_difference"] > 0.975
    assert main_50["scope"]["A123_projective_line_chart_covariance_consumed"]
    assert main_50["scope"]["certified_nodal_pair_selector_consumed"]
    assert main_50["scope"]["certified_tail_cutoff_period_reuse_consumed"]
    assert main_50["scope"]["uncompressed_physical_generator_zonotope_consumed"]
    assert tail_50["selected_thimble"]["cutoff_pair_zero_based"] == [1, 2]
    assert len(tail_50["regular_segments"]) == 768
    assert close(tail_50["E32_endpoint_tail"]["interval_radius_upper"], 3.890338897381829e-10)
    assert close(tail_50["node_segment"]["absolute_bound"]["contribution_radius_upper"], 7.627122213969483e-12)
    assert full_50["full_E32_thimble"]["floating_candidate_contained"]
    assert full_50["A134_radius_ledger"]["fallback_met"]
    assert close(full_50["full_E32_thimble"]["interval_radius_upper"], 1.78374099046863e-7)
    assert close(full_50["full_E32_thimble"]["floating_candidate_center_difference"], 8.013350687861496e-12)
    assert close(full_50["A134_radius_ledger"]["fallback_margin"], 2.2908227829755063e-5)

    print("q79 clearance-ranked append chain A140-A176 audit: PASS")
    print("closed: d001,d004,d005,d010,d011,d012,d014,d017,d018,d019,d020,d021,d026,d028,d029,d030,d031,d032,d033,d034,d035,d037,d039,d046,d048,d050,d051,d055,d057,d059,d060,d061,d062,d063,d069,d075,d085,d086,d087,d088,d089; support 41/71 and L1 75/123")
    print("closed: compact-H1 orientation gate, node-selected pipeline, route scanner, zonotope, covariant z adapter, and thirty-seven generic append transitions")
    print("frontier: y queue exhausted; native z queue head d066; d047 hard main remains partial")
    print("open: 30 supports, weighted sum, fixed carrier")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
