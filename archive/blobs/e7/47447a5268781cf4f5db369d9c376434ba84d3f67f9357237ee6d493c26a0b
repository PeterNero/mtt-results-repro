from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from q79_y_chart_conservative_extension import (
    audit_source_compatibility,
    compatible_source_hash,
)


PERIOD_DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
)
STEM = PERIOD_DIRECTORY / "d057_selected_008"
MAIN = Path(f"{STEM}.E32_main.interval.packet.json")
TAIL = Path(f"{STEM}.E32_tail.interval.packet.json")
FULL = Path(f"{STEM}.E32_full.interval.packet.json")
A145 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_successor_A145.packet.json"
A146 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_successor_A146.packet.json"
A147 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_successor_A147.packet.json"
A148 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_successor_A148.packet.json"
A149 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_successor_A149.packet.json"
A150 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_successor_A150.packet.json"
A151 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_successor_A151.packet.json"
A152 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_successor_A152.packet.json"
A153 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_successor_A153.packet.json"
A154 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_successor_A154.packet.json"
A155 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_successor_A155.packet.json"
A156 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_successor_A156.packet.json"
A157 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_successor_A157.packet.json"
A158 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_successor_A158.packet.json"
A159 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_successor_A159.packet.json"
A160 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_successor_A160.packet.json"
A161 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_successor_A161.packet.json"
A162 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_successor_A162.packet.json"
A163 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_successor_A163.packet.json"
A164 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_successor_A164.packet.json"
A165 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_successor_A165.packet.json"
A166 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_successor_A166.packet.json"
A167 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_successor_A167.packet.json"
A168 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_successor_A168.packet.json"
A169 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_successor_A169.packet.json"
A170 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_successor_A170.packet.json"
A171 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_successor_A171.packet.json"
A172 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_successor_A172.packet.json"
A173 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_successor_A173.packet.json"
A174 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_successor_A174.packet.json"
A175 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_successor_A175.packet.json"
A176 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_successor_A176.packet.json"
STEM_37 = PERIOD_DIRECTORY / "d037_selected_002"
MAIN_37 = Path(f"{STEM_37}.E32_main.interval.packet.json")
TAIL_37 = Path(f"{STEM_37}.E32_tail.interval.packet.json")
FULL_37 = Path(f"{STEM_37}.E32_full.interval.packet.json")
STEM_60 = PERIOD_DIRECTORY / "d060_selected_089"
MAIN_60 = Path(f"{STEM_60}.E32_main.interval.packet.json")
TAIL_60 = Path(f"{STEM_60}.E32_tail.interval.packet.json")
FULL_60 = Path(f"{STEM_60}.E32_full.interval.packet.json")
STEM_87 = PERIOD_DIRECTORY / "d087_selected_085"
MAIN_87 = Path(f"{STEM_87}.E32_main.interval.packet.json")
TAIL_87 = Path(f"{STEM_87}.E32_tail.interval.packet.json")
FULL_87 = Path(f"{STEM_87}.E32_full.interval.packet.json")
STEM_11 = PERIOD_DIRECTORY / "d011_selected_014"
STEM_86 = PERIOD_DIRECTORY / "d086_selected_084"
STEM_48 = PERIOD_DIRECTORY / "d048_selected_046"
STEM_88 = PERIOD_DIRECTORY / "d088_selected_064"
STEM_33 = PERIOD_DIRECTORY / "d033_selected_010"
STEM_10 = PERIOD_DIRECTORY / "d010_selected_021"
STEM_12 = PERIOD_DIRECTORY / "d012_selected_017"
STEM_17 = PERIOD_DIRECTORY / "d017_selected_022"
STEM_51 = PERIOD_DIRECTORY / "d051_selected_062"
STEM_55 = PERIOD_DIRECTORY / "d055_selected_086"
STEM_34 = PERIOD_DIRECTORY / "d034_selected_007"
STEM_59 = PERIOD_DIRECTORY / "d059_selected_042"
STEM_31 = PERIOD_DIRECTORY / "d031_selected_048"
STEM_39 = PERIOD_DIRECTORY / "d039_selected_037"
STEM_14 = PERIOD_DIRECTORY / "d014_selected_059"
STEM_75 = PERIOD_DIRECTORY / "d075_selected_067"
STEM_18 = PERIOD_DIRECTORY / "d018_selected_054"
STEM_1 = PERIOD_DIRECTORY / "d001_selected_033"
STEM_46 = PERIOD_DIRECTORY / "d046_selected_045"
STEM_89 = PERIOD_DIRECTORY / "d089_selected_032"
STEM_69 = PERIOD_DIRECTORY / "d069_selected_078"
STEM_50 = PERIOD_DIRECTORY / "d050_selected_047"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79E32PhysicalGeneratorZonotopeTransport_v1.md"
CHART_ADAPTER = ROOT / "certificates" / "selected_q79projectivechartcovariante32intervaladapter.certificate.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def close(left: float, right: float, tolerance: float = 2e-18) -> bool:
    return math.isclose(left, right, rel_tol=1e-13, abs_tol=tolerance)


def audit_generator_recurrence(packet: dict, expected_steps: int) -> None:
    transport = packet["validated_main_transport"]
    assert transport["accepted_step_count"] == expected_steps
    steps = transport["steps"]
    assert len(steps) == expected_steps
    for index, step in enumerate(steps, start=1):
        assert step["physical_generator_block_count"] == 1 + 2 * index
        assert step["physical_generator_column_count"] == 6 * (1 + 2 * index)
    assert close(float(steps[-1]["completed_path_fraction"]), 1.0)


def main() -> int:
    main_packet = load(MAIN)
    tail = load(TAIL)
    full = load(FULL)
    successor = load(A145)
    main_37 = load(MAIN_37)
    tail_37 = load(TAIL_37)
    full_37 = load(FULL_37)
    successor_146 = load(A146)
    main_60 = load(MAIN_60)
    tail_60 = load(TAIL_60)
    full_60 = load(FULL_60)
    successor_147 = load(A147)
    main_87 = load(MAIN_87)
    tail_87 = load(TAIL_87)
    full_87 = load(FULL_87)
    successor_148 = load(A148)
    successor_149 = load(A149)
    successor_150 = load(A150)
    successor_151 = load(A151)
    successor_152 = load(A152)
    successor_153 = load(A153)
    successor_154 = load(A154)
    successor_155 = load(A155)
    successor_156 = load(A156)
    successor_157 = load(A157)
    successor_158 = load(A158)
    successor_159 = load(A159)
    successor_160 = load(A160)
    successor_161 = load(A161)
    successor_162 = load(A162)
    successor_163 = load(A163)
    successor_164 = load(A164)
    successor_165 = load(A165)
    successor_166 = load(A166)
    successor_167 = load(A167)
    successor_168 = load(A168)
    successor_169 = load(A169)
    successor_170 = load(A170)
    successor_171 = load(A171)
    successor_172 = load(A172)
    successor_173 = load(A173)
    successor_174 = load(A174)
    successor_175 = load(A175)
    successor_176 = load(A176)
    main_11 = load(Path(f"{STEM_11}.E32_main.interval.packet.json"))
    tail_11 = load(Path(f"{STEM_11}.E32_tail.interval.packet.json"))
    full_11 = load(Path(f"{STEM_11}.E32_full.interval.packet.json"))
    main_86 = load(Path(f"{STEM_86}.E32_main.interval.packet.json"))
    tail_86 = load(Path(f"{STEM_86}.E32_tail.interval.packet.json"))
    full_86 = load(Path(f"{STEM_86}.E32_full.interval.packet.json"))
    main_48 = load(Path(f"{STEM_48}.E32_main.interval.packet.json"))
    tail_48 = load(Path(f"{STEM_48}.E32_tail.interval.packet.json"))
    full_48 = load(Path(f"{STEM_48}.E32_full.interval.packet.json"))
    main_88 = load(Path(f"{STEM_88}.E32_main.interval.packet.json"))
    tail_88 = load(Path(f"{STEM_88}.E32_tail.interval.packet.json"))
    full_88 = load(Path(f"{STEM_88}.E32_full.interval.packet.json"))
    main_33 = load(Path(f"{STEM_33}.E32_main.interval.packet.json"))
    tail_33 = load(Path(f"{STEM_33}.E32_tail.interval.packet.json"))
    full_33 = load(Path(f"{STEM_33}.E32_full.interval.packet.json"))
    main_10 = load(Path(f"{STEM_10}.E32_main.interval.packet.json"))
    tail_10 = load(Path(f"{STEM_10}.E32_tail.interval.packet.json"))
    full_10 = load(Path(f"{STEM_10}.E32_full.interval.packet.json"))
    main_12 = load(Path(f"{STEM_12}.E32_main.interval.packet.json"))
    tail_12 = load(Path(f"{STEM_12}.E32_tail.interval.packet.json"))
    full_12 = load(Path(f"{STEM_12}.E32_full.interval.packet.json"))
    main_17 = load(Path(f"{STEM_17}.E32_main.interval.packet.json"))
    tail_17 = load(Path(f"{STEM_17}.E32_tail.interval.packet.json"))
    full_17 = load(Path(f"{STEM_17}.E32_full.interval.packet.json"))
    main_51 = load(Path(f"{STEM_51}.E32_main.interval.packet.json"))
    tail_51 = load(Path(f"{STEM_51}.E32_tail.interval.packet.json"))
    full_51 = load(Path(f"{STEM_51}.E32_full.interval.packet.json"))
    main_55 = load(Path(f"{STEM_55}.E32_main.interval.packet.json"))
    tail_55 = load(Path(f"{STEM_55}.E32_tail.interval.packet.json"))
    full_55 = load(Path(f"{STEM_55}.E32_full.interval.packet.json"))
    main_34 = load(Path(f"{STEM_34}.E32_main.interval.packet.json"))
    tail_34 = load(Path(f"{STEM_34}.E32_tail.interval.packet.json"))
    full_34 = load(Path(f"{STEM_34}.E32_full.interval.packet.json"))
    main_59 = load(Path(f"{STEM_59}.E32_main.interval.packet.json"))
    tail_59 = load(Path(f"{STEM_59}.E32_tail.interval.packet.json"))
    full_59 = load(Path(f"{STEM_59}.E32_full.interval.packet.json"))
    main_31 = load(Path(f"{STEM_31}.E32_main.interval.packet.json"))
    tail_31 = load(Path(f"{STEM_31}.E32_tail.interval.packet.json"))
    full_31 = load(Path(f"{STEM_31}.E32_full.interval.packet.json"))
    main_39 = load(Path(f"{STEM_39}.E32_main.interval.packet.json"))
    tail_39 = load(Path(f"{STEM_39}.E32_tail.interval.packet.json"))
    full_39 = load(Path(f"{STEM_39}.E32_full.interval.packet.json"))
    main_14 = load(Path(f"{STEM_14}.E32_main.interval.packet.json"))
    tail_14 = load(Path(f"{STEM_14}.E32_tail.interval.packet.json"))
    full_14 = load(Path(f"{STEM_14}.E32_full.interval.packet.json"))
    main_75 = load(Path(f"{STEM_75}.E32_main.interval.packet.json"))
    tail_75 = load(Path(f"{STEM_75}.E32_tail.interval.packet.json"))
    full_75 = load(Path(f"{STEM_75}.E32_full.interval.packet.json"))
    main_18 = load(Path(f"{STEM_18}.E32_main.interval.packet.json"))
    tail_18 = load(Path(f"{STEM_18}.E32_tail.interval.packet.json"))
    full_18 = load(Path(f"{STEM_18}.E32_full.interval.packet.json"))
    main_1 = load(Path(f"{STEM_1}.E32_main.interval.packet.json"))
    tail_1 = load(Path(f"{STEM_1}.E32_tail.interval.packet.json"))
    full_1 = load(Path(f"{STEM_1}.E32_full.interval.packet.json"))
    main_46 = load(Path(f"{STEM_46}.E32_main.interval.packet.json"))
    tail_46 = load(Path(f"{STEM_46}.E32_tail.interval.packet.json"))
    full_46 = load(Path(f"{STEM_46}.E32_full.interval.packet.json"))
    main_89 = load(Path(f"{STEM_89}.E32_main.interval.packet.json"))
    tail_89 = load(Path(f"{STEM_89}.E32_tail.interval.packet.json"))
    full_89 = load(Path(f"{STEM_89}.E32_full.interval.packet.json"))
    main_69 = load(Path(f"{STEM_69}.E32_main.interval.packet.json"))
    tail_69 = load(Path(f"{STEM_69}.E32_tail.interval.packet.json"))
    full_69 = load(Path(f"{STEM_69}.E32_full.interval.packet.json"))
    main_50 = load(Path(f"{STEM_50}.E32_main.interval.packet.json"))
    tail_50 = load(Path(f"{STEM_50}.E32_tail.interval.packet.json"))
    full_50 = load(Path(f"{STEM_50}.E32_full.interval.packet.json"))
    chart_adapter = load(CHART_ADAPTER)
    compatibility = audit_source_compatibility()
    assert chart_adapter["byte_exact_historical_y_specialization_closed"]
    assert chart_adapter["reconstructed_historical_y_source_hashes"] == compatibility[
        "reconstructed_historical_y_hashes"
    ]

    assert main_packet["schema"] == "MTTQ79SelectedAlignmentSingleE32ThimbleMainInterval.v1"
    assert main_packet["scope"]["main_homogeneous_Gauss_Manin_segment_interval_closed"]
    assert main_packet["scope"]["certified_nodal_pair_selector_consumed"]
    assert main_packet["scope"]["uncompressed_physical_generator_zonotope_consumed"]
    assert not main_packet["scope"]["observed_SM_values_used"]
    assert main_packet["selected_thimble"]["near_node_colliding_pair_zero_based"] == [3, 4]
    assert main_packet["selected_thimble"]["endpoint_cutoff_epsilon"] == 2.0e-5

    authority = main_packet["authority"]
    for path_key, hash_key in (
        ("builder_source", "builder_source_sha256"),
        ("certified_node_pair_source", "certified_node_pair_source_sha256"),
        ("distinguished_fan", "distinguished_fan_sha256"),
        ("dual_discriminant", "dual_discriminant_sha256"),
        ("floating_candidate", "floating_candidate_sha256"),
        ("validated_transport_engine", "validated_transport_engine_sha256"),
    ):
        path = ROOT / authority[path_key]
        assert path.exists(), authority[path_key]
        if path_key == "validated_transport_engine":
            assert compatible_source_hash(path, authority[hash_key])
        else:
            assert sha256(path) == authority[hash_key], authority[path_key]

    builder = (ROOT / authority["builder_source"]).read_text(encoding="utf-8")
    assert "endpoint_fundamental * block for block in input_frame.blocks" in builder
    assert "endpoint_fundamental * diagonal_block(correction_radius)" in builder
    assert "diagonal_block(rounding_radius)" in builder

    transport = main_packet["validated_main_transport"]
    assert transport["certificate_method"] == (
        "six-dimensional augmented uncompressed physical-generator zonotope "
        "on a certified polygonal homotopy"
    )
    assert transport["accepted_step_count"] == 252
    assert transport["rejected_step_count"] == 21
    assert close(transport["uniform_integral_radius_upper"], 1.038675053577015e-5)
    steps = transport["steps"]
    assert len(steps) == 252
    for index, step in enumerate(steps, start=1):
        assert step["error_frame_kind"] == "uncompressed physical-generator zonotope"
        assert step["physical_generator_block_count"] == 1 + 2 * index
        assert step["physical_generator_column_count"] == 6 * (1 + 2 * index)
    assert steps[-1]["completed_path_fraction"] == 1.0
    assert steps[-1]["physical_generator_block_count"] == 505
    assert steps[-1]["physical_generator_column_count"] == 3030
    radii = [float(step["E32_coordinate_radius_upper"]) for step in steps]
    assert any(right < left for left, right in zip(radii, radii[1:]))
    assert close(radii[-1], transport["uniform_integral_radius_upper"])

    assert tail["selected_thimble"]["cutoff_pair_zero_based"] == [3, 4]
    assert tail["selected_thimble"]["endpoint_cutoff_epsilon"] == 2.0e-5
    assert close(tail["E32_endpoint_tail"]["interval_radius_upper"], 1.716579923538575e-6)
    assert full["scope"]["single_full_E32_thimble_interval_closed"]
    assert not full["scope"]["floating_candidate_used_as_bound"]
    assert full["full_E32_thimble"]["floating_candidate_contained"]
    assert close(full["full_E32_thimble"]["interval_radius_upper"], 1.640566262040011e-5)
    assert full["A134_radius_ledger"]["fallback_met"]
    assert close(full["A134_radius_ledger"]["fallback_margin"], 6.68093930840182e-6)

    new = successor["new_accepted_full_interval"]
    assert successor["artifact"] == "A145"
    assert new["distinguished_index"] == 57
    assert new["root_id"] == "selected_008"
    assert new["coefficient"] == 3
    assert successor["weighted_budget_ledger"]["selected_support_closed"] == 10
    assert successor["weighted_budget_ledger"]["selected_l1_closed"] == 25
    assert close(
        successor["weighted_budget_ledger"]["remaining_budget"],
        0.0026619050855207723,
    )

    assert main_37["scope"]["uncompressed_physical_generator_zonotope_consumed"]
    assert main_37["selected_thimble"]["near_node_colliding_pair_zero_based"] == [0, 1]
    assert main_37["selected_thimble"]["endpoint_cutoff_epsilon"] == 1.0e-5
    authority_37 = main_37["authority"]
    builder_37 = ROOT / authority_37["builder_source"]
    assert sha256(builder_37) == authority_37["builder_source_sha256"]
    transport_37 = main_37["validated_main_transport"]
    assert transport_37["accepted_step_count"] == 235
    assert transport_37["rejected_step_count"] == 55
    assert close(transport_37["uniform_integral_radius_upper"], 8.253525766885164e-8)
    steps_37 = transport_37["steps"]
    assert len(steps_37) == 235
    for index, step in enumerate(steps_37, start=1):
        assert step["physical_generator_block_count"] == 1 + 2 * index
        assert step["physical_generator_column_count"] == 6 * (1 + 2 * index)
    assert steps_37[-1]["physical_generator_block_count"] == 471
    assert steps_37[-1]["physical_generator_column_count"] == 2826
    assert close(tail_37["E32_endpoint_tail"]["interval_radius_upper"], 6.588022287701279e-7)
    assert full_37["scope"]["single_full_E32_thimble_interval_closed"]
    assert full_37["full_E32_thimble"]["floating_candidate_contained"]
    assert close(full_37["full_E32_thimble"]["interval_radius_upper"], 7.755247146690182e-7)
    assert full_37["A134_radius_ledger"]["fallback_met"]
    new_146 = successor_146["new_accepted_full_interval"]
    assert successor_146["artifact"] == "A146"
    assert new_146["distinguished_index"] == 37
    assert new_146["coefficient"] == -2
    assert successor_146["weighted_budget_ledger"]["selected_support_closed"] == 11
    assert successor_146["weighted_budget_ledger"]["selected_l1_closed"] == 27
    assert close(
        successor_146["weighted_budget_ledger"]["remaining_budget"],
        0.002660338672401141,
    )

    assert main_60["scope"]["uncompressed_physical_generator_zonotope_consumed"]
    assert main_60["selected_thimble"]["near_node_colliding_pair_zero_based"] == [4, 5]
    authority_60 = main_60["authority"]
    builder_60 = ROOT / authority_60["builder_source"]
    assert sha256(builder_60) == authority_60["builder_source_sha256"]
    assert sha256(TAIL_60) == authority_60["certified_tail_cutoff_period_source_sha256"]
    assert authority_60["certified_tail_cutoff_period_source"] == str(
        TAIL_60.relative_to(ROOT)
    ).replace("\\", "/")
    builder_60_text = builder_60.read_text(encoding="utf-8")
    assert "source radius plus two binary64 ulps per real coordinate" in builder_60_text
    assert "zonotope.validated_e32_zonotope_flow_step" in builder_60_text
    assert sha256(ROOT / "scripts" / "certify_q79_selected_alignment_E32_thimble_polygonal_main_interval_node_pair_zonotope.py") == authority["builder_source_sha256"]
    geometry_60 = main_60["polygonal_homotopy"]
    assert geometry_60["relative_homotopy_class_equals_original_radial_path"]
    assert geometry_60["detour_fraction"] == 0.45
    assert geometry_60["detour_signed_right_offset"] == -0.01
    assert geometry_60["return_fraction"] == 0.86
    assert geometry_60["other_critical_ball_clearance_lower"] > 0.0155
    transport_60 = main_60["validated_main_transport"]
    assert transport_60["certificate_method"].endswith(
        "with certified tail cutoff-period reuse"
    )
    assert transport_60["accepted_step_count"] == 126
    assert transport_60["rejected_step_count"] == 19
    assert close(transport_60["uniform_integral_radius_upper"], 8.26708945089474e-8)
    assert (
        main_60["near_node_direct_cycle_interval"]["source_maximum_component_radius"]
        == 4.219981740596756e-44
    )
    assert math.isclose(
        main_60["near_node_direct_cycle_interval"]["maximum_component_radius"],
        2.77555757707253e-17,
        rel_tol=1e-13,
        abs_tol=1e-30,
    )
    steps_60 = transport_60["steps"]
    assert len(steps_60) == 126
    for index, step in enumerate(steps_60, start=1):
        assert step["physical_generator_block_count"] == 1 + 2 * index
        assert step["physical_generator_column_count"] == 6 * (1 + 2 * index)
    assert steps_60[-1]["physical_generator_block_count"] == 253
    assert steps_60[-1]["physical_generator_column_count"] == 1518
    assert close(tail_60["E32_endpoint_tail"]["interval_radius_upper"], 5.516838641028699e-6)
    assert full_60["scope"]["single_full_E32_thimble_interval_closed"]
    assert full_60["full_E32_thimble"]["floating_candidate_contained"]
    assert close(full_60["full_E32_thimble"]["interval_radius_upper"], 5.63375292017554e-6)
    new_147 = successor_147["new_accepted_full_interval"]
    assert successor_147["artifact"] == "A147"
    assert new_147["distinguished_index"] == 60
    assert new_147["coefficient"] == 1
    assert successor_147["weighted_budget_ledger"]["selected_support_closed"] == 12
    assert successor_147["weighted_budget_ledger"]["selected_l1_closed"] == 28
    assert close(
        successor_147["weighted_budget_ledger"]["remaining_budget"],
        0.0026544874745351448,
    )

    assert main_87["scope"]["uncompressed_physical_generator_zonotope_consumed"]
    assert main_87["scope"]["certified_tail_cutoff_period_reuse_consumed"]
    assert main_87["selected_thimble"]["near_node_colliding_pair_zero_based"] == [3, 4]
    authority_87 = main_87["authority"]
    assert sha256(ROOT / authority_87["builder_source"]) == authority_87["builder_source_sha256"]
    assert sha256(TAIL_87) == authority_87["certified_tail_cutoff_period_source_sha256"]
    geometry_87 = main_87["polygonal_homotopy"]
    assert geometry_87["relative_homotopy_class_equals_original_radial_path"]
    assert geometry_87["detour_fraction"] == 0.25
    assert geometry_87["detour_signed_right_offset"] == 0.0
    assert geometry_87["return_fraction"] == 0.74
    assert geometry_87["other_critical_ball_clearance_lower"] > 0.0092
    transport_87 = main_87["validated_main_transport"]
    assert transport_87["certificate_method"].endswith(
        "with certified tail cutoff-period reuse"
    )
    assert transport_87["accepted_step_count"] == 139
    assert transport_87["rejected_step_count"] == 50
    assert close(transport_87["uniform_integral_radius_upper"], 4.921072286600216e-8)
    assert (
        main_87["near_node_direct_cycle_interval"]["source_maximum_component_radius"]
        == 7.828079142811571e-42
    )
    assert math.isclose(
        main_87["near_node_direct_cycle_interval"]["maximum_component_radius"],
        3.55271369203539e-15,
        rel_tol=1e-13,
        abs_tol=1e-28,
    )
    steps_87 = transport_87["steps"]
    assert len(steps_87) == 139
    for index, step in enumerate(steps_87, start=1):
        assert step["physical_generator_block_count"] == 1 + 2 * index
        assert step["physical_generator_column_count"] == 6 * (1 + 2 * index)
    assert steps_87[-1]["physical_generator_block_count"] == 279
    assert steps_87[-1]["physical_generator_column_count"] == 1674
    assert close(tail_87["E32_endpoint_tail"]["interval_radius_upper"], 4.295933031528421e-6)
    assert full_87["scope"]["single_full_E32_thimble_interval_closed"]
    assert full_87["full_E32_thimble"]["floating_candidate_contained"]
    assert close(full_87["full_E32_thimble"]["interval_radius_upper"], 4.365527402683257e-6)
    assert full_87["A134_radius_ledger"]["fallback_met"]
    new_148 = successor_148["new_accepted_full_interval"]
    assert successor_148["artifact"] == "A148"
    assert new_148["distinguished_index"] == 87
    assert new_148["root_id"] == "selected_085"
    assert new_148["coefficient"] == -1
    assert successor_148["weighted_budget_ledger"]["selected_support_closed"] == 13
    assert successor_148["weighted_budget_ledger"]["selected_l1_closed"] == 29
    assert close(
        successor_148["weighted_budget_ledger"]["remaining_budget"],
        0.0026497313599235218,
    )

    for packet in (main_11, main_86, main_48, main_88, main_33, main_10, main_12, main_17, main_51, main_55, main_34, main_59, main_31, main_39, main_14, main_75, main_18, main_1, main_46, main_89, main_69, main_50):
        assert packet["scope"]["uncompressed_physical_generator_zonotope_consumed"]
        assert packet["scope"]["certified_tail_cutoff_period_reuse_consumed"]
        assert packet["validated_main_transport"]["certificate_method"].endswith(
            "with certified tail cutoff-period reuse"
        )
    audit_generator_recurrence(main_11, 145)
    audit_generator_recurrence(main_86, 126)
    audit_generator_recurrence(main_48, 68)
    audit_generator_recurrence(main_88, 128)
    audit_generator_recurrence(main_33, 171)
    audit_generator_recurrence(main_10, 193)
    audit_generator_recurrence(main_12, 190)
    audit_generator_recurrence(main_17, 182)
    audit_generator_recurrence(main_51, 259)
    audit_generator_recurrence(main_55, 243)
    audit_generator_recurrence(main_34, 288)
    audit_generator_recurrence(main_59, 74)
    audit_generator_recurrence(main_31, 132)
    audit_generator_recurrence(main_39, 103)
    audit_generator_recurrence(main_14, 75)
    audit_generator_recurrence(main_75, 149)
    audit_generator_recurrence(main_18, 111)
    audit_generator_recurrence(main_1, 117)
    audit_generator_recurrence(main_46, 164)
    audit_generator_recurrence(main_89, 71)
    audit_generator_recurrence(main_69, 138)
    audit_generator_recurrence(main_50, 92)

    assert close(
        main_11["validated_main_transport"]["uniform_integral_radius_upper"],
        2.1153876733524222e-7,
    )
    assert close(tail_11["E32_endpoint_tail"]["interval_radius_upper"], 2.3480975066547676e-6)
    assert close(full_11["full_E32_thimble"]["interval_radius_upper"], 2.647258515509066e-6)
    assert successor_149["new_accepted_full_interval"]["distinguished_index"] == 11
    assert successor_149["weighted_budget_ledger"]["selected_support_closed"] == 14

    assert close(
        main_86["validated_main_transport"]["uniform_integral_radius_upper"],
        1.7865286913408602e-7,
    )
    assert close(tail_86["E32_endpoint_tail"]["interval_radius_upper"], 2.270697873285599e-6)
    assert close(full_86["full_E32_thimble"]["interval_radius_upper"], 2.523348872074394e-6)
    assert successor_150["new_accepted_full_interval"]["distinguished_index"] == 86
    assert successor_150["weighted_budget_ledger"]["selected_support_closed"] == 15

    assert main_48["selected_thimble"]["line_chart"] == "z"
    assert main_48["scope"]["A123_projective_line_chart_covariance_consumed"]
    assert close(
        main_48["validated_main_transport"]["uniform_integral_radius_upper"],
        7.936130431453395e-8,
    )
    assert close(tail_48["E32_endpoint_tail"]["interval_radius_upper"], 4.079888063675264e-10)
    assert close(full_48["full_E32_thimble"]["interval_radius_upper"], 1.1264182253611922e-7)
    assert successor_151["new_accepted_full_interval"]["distinguished_index"] == 48
    assert successor_151["scope"]["covariant_z_chart_interval_adapter_closed"]
    assert successor_151["weighted_budget_ledger"]["selected_support_closed"] == 16

    assert main_88["selected_thimble"]["line_chart"] == "y"
    assert main_88["polygonal_homotopy"]["relative_homotopy_class_equals_original_radial_path"]
    assert close(
        main_88["validated_main_transport"]["uniform_integral_radius_upper"],
        4.0606162630066217e-7,
    )
    assert close(tail_88["E32_endpoint_tail"]["interval_radius_upper"], 1.33992724832277e-8)
    assert close(full_88["full_E32_thimble"]["interval_radius_upper"], 5.876571353979899e-7)
    assert full_88["full_E32_thimble"]["floating_candidate_contained"]
    assert full_88["A134_radius_ledger"]["fallback_met"]
    assert successor_152["new_accepted_full_interval"]["distinguished_index"] == 88
    assert successor_152["weighted_budget_ledger"]["selected_support_closed"] == 17
    assert successor_152["weighted_budget_ledger"]["selected_l1_closed"] == 37
    assert close(
        successor_152["weighted_budget_ledger"]["remaining_budget"],
        0.0026377595477375983,
    )

    assert main_33["selected_thimble"]["line_chart"] == "y"
    assert main_33["polygonal_homotopy"]["relative_homotopy_class_equals_original_radial_path"]
    assert close(
        main_33["validated_main_transport"]["uniform_integral_radius_upper"],
        6.326398650143199e-7,
    )
    assert close(tail_33["E32_endpoint_tail"]["interval_radius_upper"], 4.038975447429039e-6)
    assert close(full_33["full_E32_thimble"]["interval_radius_upper"], 4.933663213080309e-6)
    assert full_33["full_E32_thimble"]["floating_candidate_contained"]
    assert full_33["A134_radius_ledger"]["fallback_met"]
    assert successor_153["new_accepted_full_interval"]["distinguished_index"] == 33
    assert successor_154["new_accepted_full_interval"]["distinguished_index"] == 35
    assert successor_155["new_accepted_full_interval"]["distinguished_index"] == 63
    assert successor_156["new_accepted_full_interval"]["distinguished_index"] == 26
    assert successor_157["new_accepted_full_interval"]["distinguished_index"] == 32
    assert successor_158["new_accepted_full_interval"]["distinguished_index"] == 30
    assert successor_158["weighted_budget_ledger"]["selected_support_closed"] == 23
    assert successor_158["weighted_budget_ledger"]["selected_l1_closed"] == 44
    assert close(
        successor_158["weighted_budget_ledger"]["remaining_budget"],
        0.002612147943407349,
    )
    assert successor_159["new_accepted_full_interval"]["distinguished_index"] == 85
    assert successor_159["weighted_budget_ledger"]["selected_support_closed"] == 24
    assert successor_159["weighted_budget_ledger"]["selected_l1_closed"] == 45
    assert close(
        successor_159["weighted_budget_ledger"]["remaining_budget"],
        0.002593391779119974,
    )
    assert close(
        main_10["validated_main_transport"]["uniform_integral_radius_upper"],
        9.198311075311998e-7,
    )
    assert close(tail_10["E32_endpoint_tail"]["interval_radius_upper"], 3.2598659274185597e-6)
    assert close(full_10["full_E32_thimble"]["interval_radius_upper"], 4.560701455602612e-6)
    assert full_10["full_E32_thimble"]["floating_candidate_contained"]
    assert full_10["A134_radius_ledger"]["fallback_met"]
    assert successor_160["new_accepted_full_interval"]["distinguished_index"] == 10
    assert successor_160["weighted_budget_ledger"]["selected_support_closed"] == 25
    assert successor_160["weighted_budget_ledger"]["selected_l1_closed"] == 46
    assert close(
        successor_160["weighted_budget_ledger"]["remaining_budget"],
        0.0025886771432555504,
    )
    assert close(
        main_12["validated_main_transport"]["uniform_integral_radius_upper"],
        5.743632409585513e-7,
    )
    assert close(tail_12["E32_endpoint_tail"]["interval_radius_upper"], 1.49679504168887e-6)
    assert close(full_12["full_E32_thimble"]["interval_radius_upper"], 2.3084341584933558e-6)
    assert full_12["full_E32_thimble"]["floating_candidate_contained"]
    assert full_12["A134_radius_ledger"]["fallback_met"]
    assert successor_161["new_accepted_full_interval"]["distinguished_index"] == 12
    assert successor_161["weighted_budget_ledger"]["selected_support_closed"] == 26
    assert successor_161["weighted_budget_ledger"]["selected_l1_closed"] == 47
    assert close(
        successor_161["weighted_budget_ledger"]["remaining_budget"],
        0.002586203981129001,
    )
    assert close(
        main_17["validated_main_transport"]["uniform_integral_radius_upper"],
        3.831653826366047e-7,
    )
    assert close(tail_17["E32_endpoint_tail"]["interval_radius_upper"], 1.3301582466596076e-6)
    assert close(full_17["full_E32_thimble"]["interval_radius_upper"], 1.8720345043021782e-6)
    assert full_17["full_E32_thimble"]["floating_candidate_contained"]
    assert full_17["A134_radius_ledger"]["fallback_met"]
    assert successor_162["new_accepted_full_interval"]["distinguished_index"] == 17
    assert successor_162["weighted_budget_ledger"]["selected_support_closed"] == 27
    assert successor_162["weighted_budget_ledger"]["selected_l1_closed"] == 49
    assert close(
        successor_162["weighted_budget_ledger"]["remaining_budget"],
        0.0025824578558143025,
    )
    assert close(
        main_51["validated_main_transport"]["uniform_integral_radius_upper"],
        1.1786789306105185e-6,
    )
    assert close(tail_51["E32_endpoint_tail"]["interval_radius_upper"], 3.526161225231306e-7)
    assert close(full_51["full_E32_thimble"]["interval_radius_upper"], 2.019519840246176e-6)
    assert full_51["full_E32_thimble"]["floating_candidate_contained"]
    assert full_51["A134_radius_ledger"]["fallback_met"]
    assert successor_163["new_accepted_full_interval"]["distinguished_index"] == 51
    assert successor_163["weighted_budget_ledger"]["selected_support_closed"] == 28
    assert successor_163["weighted_budget_ledger"]["selected_l1_closed"] == 51
    assert close(
        successor_163["weighted_budget_ledger"]["remaining_budget"],
        0.0025784083934571335,
    )
    assert close(
        main_55["validated_main_transport"]["uniform_integral_radius_upper"],
        1.3338361979199125e-6,
    )
    assert close(tail_55["E32_endpoint_tail"]["interval_radius_upper"], 2.761550554453152e-6)
    assert close(full_55["full_E32_thimble"]["interval_radius_upper"], 4.647876217234171e-6)
    assert full_55["full_E32_thimble"]["floating_candidate_contained"]
    assert full_55["A134_radius_ledger"]["fallback_met"]
    assert successor_164["new_accepted_full_interval"]["distinguished_index"] == 55
    assert successor_164["weighted_budget_ledger"]["selected_support_closed"] == 29
    assert successor_164["weighted_budget_ledger"]["selected_l1_closed"] == 52
    assert close(
        successor_164["weighted_budget_ledger"]["remaining_budget"],
        0.002573558691735344,
    )
    assert close(
        main_34["validated_main_transport"]["uniform_integral_radius_upper"],
        2.20656062847174e-6,
    )
    assert close(tail_34["E32_endpoint_tail"]["interval_radius_upper"], 5.526991380122582e-6)
    assert len(tail_34["regular_segments"]) == 768
    assert close(full_34["full_E32_thimble"]["interval_radius_upper"], 8.64753941698382e-6)
    assert full_34["full_E32_thimble"]["floating_candidate_contained"]
    assert full_34["A134_radius_ledger"]["fallback_met"]
    assert successor_165["new_accepted_full_interval"]["distinguished_index"] == 34
    assert successor_165["weighted_budget_ledger"]["selected_support_closed"] == 30
    assert successor_165["weighted_budget_ledger"]["selected_l1_closed"] == 55
    assert successor_165["clearance_ranked_queues"]["y"] == []
    assert successor_165["clearance_ranked_queues"]["z"][0]["distinguished_index"] == 59
    assert close(
        successor_165["weighted_budget_ledger"]["remaining_budget"],
        0.0025467698558757695,
    )
    assert main_59["selected_thimble"]["line_chart"] == "z"
    assert main_59["selected_thimble"]["near_node_colliding_pair_zero_based"] == [0, 1]
    assert main_59["scope"]["A123_projective_line_chart_covariance_consumed"]
    assert close(
        main_59["validated_main_transport"]["uniform_integral_radius_upper"],
        8.601425856598232e-8,
    )
    assert main_59["validated_main_transport"]["accepted_step_count"] == 74
    assert main_59["validated_main_transport"]["rejected_step_count"] == 21
    assert close(tail_59["E32_endpoint_tail"]["interval_radius_upper"], 3.2196170278442353e-9)
    assert len(tail_59["regular_segments"]) == 384
    assert close(full_59["full_E32_thimble"]["interval_radius_upper"], 1.2486213707418872e-7)
    assert full_59["full_E32_thimble"]["floating_candidate_contained"]
    assert full_59["A134_radius_ledger"]["fallback_met"]
    assert successor_166["new_accepted_full_interval"]["distinguished_index"] == 59
    assert successor_166["weighted_budget_ledger"]["selected_support_closed"] == 31
    assert successor_166["weighted_budget_ledger"]["selected_l1_closed"] == 58
    assert successor_166["clearance_ranked_queues"]["y"] == []
    assert successor_166["clearance_ranked_queues"]["z"][0]["distinguished_index"] == 31
    assert close(
        successor_166["weighted_budget_ledger"]["remaining_budget"],
        0.002546395231699759,
    )
    assert main_31["selected_thimble"]["line_chart"] == "z"
    assert main_31["selected_thimble"]["near_node_colliding_pair_zero_based"] == [4, 5]
    assert main_31["scope"]["A123_projective_line_chart_covariance_consumed"]
    assert close(
        main_31["validated_main_transport"]["uniform_integral_radius_upper"],
        1.816473192839754e-7,
    )
    assert main_31["validated_main_transport"]["accepted_step_count"] == 132
    assert main_31["validated_main_transport"]["rejected_step_count"] == 67
    assert close(tail_31["E32_endpoint_tail"]["interval_radius_upper"], 1.0621430429624825e-8)
    assert len(tail_31["regular_segments"]) == 384
    assert close(full_31["full_E32_thimble"]["interval_radius_upper"], 2.675095345239243e-7)
    assert full_31["full_E32_thimble"]["floating_candidate_contained"]
    assert full_31["A134_radius_ledger"]["fallback_met"]
    assert successor_167["new_accepted_full_interval"]["distinguished_index"] == 31
    assert successor_167["weighted_budget_ledger"]["selected_support_closed"] == 32
    assert successor_167["weighted_budget_ledger"]["selected_l1_closed"] == 60
    assert successor_167["clearance_ranked_queues"]["y"] == []
    assert successor_167["clearance_ranked_queues"]["z"][0]["distinguished_index"] == 39
    assert close(
        successor_167["weighted_budget_ledger"]["remaining_budget"],
        0.002545859410138626,
    )
    assert main_39["selected_thimble"]["line_chart"] == "z"
    assert main_39["selected_thimble"]["near_node_colliding_pair_zero_based"] == [1, 2]
    assert main_39["scope"]["A123_projective_line_chart_covariance_consumed"]
    assert close(
        main_39["validated_main_transport"]["uniform_integral_radius_upper"],
        1.0881261871947691e-7,
    )
    assert main_39["validated_main_transport"]["accepted_step_count"] == 103
    assert main_39["validated_main_transport"]["rejected_step_count"] == 32
    assert close(tail_39["E32_endpoint_tail"]["interval_radius_upper"], 1.4066956168790059e-6)
    assert len(tail_39["regular_segments"]) == 96
    assert close(full_39["full_E32_thimble"]["interval_radius_upper"], 1.5605798893147951e-6)
    assert full_39["full_E32_thimble"]["floating_candidate_contained"]
    assert full_39["A134_radius_ledger"]["fallback_met"]
    assert successor_168["new_accepted_full_interval"]["distinguished_index"] == 39
    assert successor_168["weighted_budget_ledger"]["selected_support_closed"] == 33
    assert successor_168["weighted_budget_ledger"]["selected_l1_closed"] == 62
    assert successor_168["clearance_ranked_queues"]["y"] == []
    assert successor_168["clearance_ranked_queues"]["z"][0]["distinguished_index"] == 14
    assert close(
        successor_168["weighted_budget_ledger"]["remaining_budget"],
        0.002542615358404724,
    )
    assert main_14["selected_thimble"]["line_chart"] == "z"
    assert main_14["selected_thimble"]["near_node_colliding_pair_zero_based"] == [3, 4]
    assert main_14["scope"]["A123_projective_line_chart_covariance_consumed"]
    assert close(
        main_14["validated_main_transport"]["uniform_integral_radius_upper"],
        1.2239440876842448e-7,
    )
    assert main_14["validated_main_transport"]["accepted_step_count"] == 75
    assert main_14["validated_main_transport"]["rejected_step_count"] == 23
    assert close(tail_14["E32_endpoint_tail"]["interval_radius_upper"], 1.1550937359383619e-8)
    assert len(tail_14["regular_segments"]) == 768
    assert close(full_14["full_E32_thimble"]["interval_radius_upper"], 1.8464276241303426e-7)
    assert full_14["full_E32_thimble"]["floating_candidate_contained"]
    assert full_14["A134_radius_ledger"]["fallback_met"]
    assert successor_169["new_accepted_full_interval"]["distinguished_index"] == 14
    assert successor_169["weighted_budget_ledger"]["selected_support_closed"] == 34
    assert successor_169["weighted_budget_ledger"]["selected_l1_closed"] == 63
    assert successor_169["clearance_ranked_queues"]["y"] == []
    assert successor_169["clearance_ranked_queues"]["z"][0]["distinguished_index"] == 75
    assert close(
        successor_169["weighted_budget_ledger"]["remaining_budget"],
        0.0025424306551317393,
    )
    assert main_75["selected_thimble"]["line_chart"] == "z"
    assert main_75["selected_thimble"]["near_node_colliding_pair_zero_based"] == [3, 4]
    assert main_75["scope"]["A123_projective_line_chart_covariance_consumed"]
    assert close(
        main_75["validated_main_transport"]["uniform_integral_radius_upper"],
        2.127205331505899e-7,
    )
    assert main_75["validated_main_transport"]["accepted_step_count"] == 149
    assert main_75["validated_main_transport"]["rejected_step_count"] == 55
    assert close(tail_75["E32_endpoint_tail"]["interval_radius_upper"], 5.82789970593467e-6)
    assert len(tail_75["regular_segments"]) == 384
    assert close(full_75["full_E32_thimble"]["interval_radius_upper"], 6.12873136418557e-6)
    assert full_75["full_E32_thimble"]["floating_candidate_contained"]
    assert full_75["A134_radius_ledger"]["fallback_met"]
    assert successor_170["new_accepted_full_interval"]["distinguished_index"] == 75
    assert successor_170["weighted_budget_ledger"]["selected_support_closed"] == 35
    assert successor_170["weighted_budget_ledger"]["selected_l1_closed"] == 65
    assert successor_170["clearance_ranked_queues"]["y"] == []
    assert successor_170["clearance_ranked_queues"]["z"][0]["distinguished_index"] == 18
    assert close(
        successor_170["weighted_budget_ledger"]["remaining_budget"],
        0.0025296490651101886,
    )
    assert main_18["selected_thimble"]["line_chart"] == "z"
    assert main_18["selected_thimble"]["near_node_colliding_pair_zero_based"] == [4, 5]
    assert main_18["scope"]["A123_projective_line_chart_covariance_consumed"]
    assert close(
        main_18["validated_main_transport"]["uniform_integral_radius_upper"],
        1.1239108844990107e-7,
    )
    assert main_18["validated_main_transport"]["accepted_step_count"] == 111
    assert main_18["validated_main_transport"]["rejected_step_count"] == 55
    assert close(tail_18["E32_endpoint_tail"]["interval_radius_upper"], 1.2428286488841425e-6)
    assert len(tail_18["regular_segments"]) == 384
    assert close(full_18["full_E32_thimble"]["interval_radius_upper"], 1.4017736589266863e-6)
    assert full_18["full_E32_thimble"]["floating_candidate_contained"]
    assert full_18["A134_radius_ledger"]["fallback_met"]
    assert successor_171["new_accepted_full_interval"]["distinguished_index"] == 18
    assert successor_171["weighted_budget_ledger"]["selected_support_closed"] == 36
    assert successor_171["weighted_budget_ledger"]["selected_l1_closed"] == 67
    assert successor_171["clearance_ranked_queues"]["y"] == []
    assert successor_171["clearance_ranked_queues"]["z"][0]["distinguished_index"] == 1
    assert close(
        successor_171["weighted_budget_ledger"]["remaining_budget"],
        0.002526744359302269,
    )
    assert main_1["selected_thimble"]["line_chart"] == "z"
    assert main_1["selected_thimble"]["near_node_colliding_pair_zero_based"] == [0, 1]
    assert main_1["scope"]["A123_projective_line_chart_covariance_consumed"]
    assert close(
        main_1["validated_main_transport"]["uniform_integral_radius_upper"],
        4.5844626040661814e-6,
    )
    assert main_1["validated_main_transport"]["accepted_step_count"] == 117
    assert main_1["validated_main_transport"]["rejected_step_count"] == 36
    assert close(tail_1["E32_endpoint_tail"]["interval_radius_upper"], 5.4652383241204927e-7)
    assert len(tail_1["regular_segments"]) == 384
    assert close(full_1["full_E32_thimble"]["interval_radius_upper"], 7.0299094261372383e-6)
    assert full_1["full_E32_thimble"]["floating_candidate_contained"]
    assert full_1["A134_radius_ledger"]["fallback_met"]
    assert successor_172["new_accepted_full_interval"]["distinguished_index"] == 1
    assert successor_172["weighted_budget_ledger"]["selected_support_closed"] == 37
    assert successor_172["weighted_budget_ledger"]["selected_l1_closed"] == 68
    assert successor_172["clearance_ranked_queues"]["y"] == []
    assert successor_172["clearance_ranked_queues"]["z"][0]["distinguished_index"] == 46
    assert close(
        successor_172["weighted_budget_ledger"]["remaining_budget"],
        0.002519699484503413,
    )
    assert main_46["selected_thimble"]["line_chart"] == "z"
    assert main_46["selected_thimble"]["near_node_colliding_pair_zero_based"] == [1, 2]
    assert main_46["scope"]["A123_projective_line_chart_covariance_consumed"]
    assert close(
        main_46["validated_main_transport"]["uniform_integral_radius_upper"],
        6.883023908842079e-7,
    )
    assert main_46["validated_main_transport"]["accepted_step_count"] == 164
    assert main_46["validated_main_transport"]["rejected_step_count"] == 66
    assert close(tail_46["E32_endpoint_tail"]["interval_radius_upper"], 1.0406598907053424e-6)
    assert len(tail_46["regular_segments"]) == 768
    assert close(full_46["full_E32_thimble"]["interval_radius_upper"], 2.0140664531709267e-6)
    assert full_46["full_E32_thimble"]["floating_candidate_contained"]
    assert full_46["A134_radius_ledger"]["fallback_met"]
    assert successor_173["new_accepted_full_interval"]["distinguished_index"] == 46
    assert successor_173["weighted_budget_ledger"]["selected_support_closed"] == 38
    assert successor_173["weighted_budget_ledger"]["selected_l1_closed"] == 71
    assert successor_173["clearance_ranked_queues"]["y"] == []
    assert successor_173["clearance_ranked_queues"]["z"][0]["distinguished_index"] == 89
    assert close(
        successor_173["weighted_budget_ledger"]["remaining_budget"],
        0.002512758529204833,
    )
    assert main_89["selected_thimble"]["line_chart"] == "z"
    assert main_89["selected_thimble"]["near_node_colliding_pair_zero_based"] == [1, 2]
    assert main_89["scope"]["A123_projective_line_chart_covariance_consumed"]
    assert close(
        main_89["validated_main_transport"]["uniform_integral_radius_upper"],
        2.9346360173223173e-7,
    )
    assert main_89["validated_main_transport"]["accepted_step_count"] == 71
    assert main_89["validated_main_transport"]["rejected_step_count"] == 16
    assert close(tail_89["E32_endpoint_tail"]["interval_radius_upper"], 2.1323743014389777e-9)
    assert len(tail_89["regular_segments"]) == 384
    assert close(full_89["full_E32_thimble"]["interval_radius_upper"], 4.171525822549427e-7)
    assert full_89["full_E32_thimble"]["floating_candidate_contained"]
    assert full_89["A134_radius_ledger"]["fallback_met"]
    assert successor_174["new_accepted_full_interval"]["distinguished_index"] == 89
    assert successor_174["weighted_budget_ledger"]["selected_support_closed"] == 39
    assert successor_174["weighted_budget_ledger"]["selected_l1_closed"] == 72
    assert successor_174["clearance_ranked_queues"]["y"] == []
    assert successor_174["clearance_ranked_queues"]["z"][0]["distinguished_index"] == 69
    assert close(
        successor_174["weighted_budget_ledger"]["remaining_budget"],
        0.002512341328516809,
    )
    assert main_69["selected_thimble"]["line_chart"] == "z"
    assert main_69["selected_thimble"]["near_node_colliding_pair_zero_based"] == [3, 4]
    assert main_69["scope"]["A123_projective_line_chart_covariance_consumed"]
    assert close(
        main_69["validated_main_transport"]["uniform_integral_radius_upper"],
        3.0482279579327836e-7,
    )
    assert main_69["validated_main_transport"]["accepted_step_count"] == 138
    assert main_69["validated_main_transport"]["rejected_step_count"] == 37
    assert close(tail_69["E32_endpoint_tail"]["interval_radius_upper"], 9.208371682944972e-7)
    assert len(tail_69["regular_segments"]) == 384
    assert close(full_69["full_E32_thimble"]["interval_radius_upper"], 1.3519217159085886e-6)
    assert full_69["full_E32_thimble"]["floating_candidate_contained"]
    assert full_69["A134_radius_ledger"]["fallback_met"]
    assert successor_175["new_accepted_full_interval"]["distinguished_index"] == 69
    assert successor_175["weighted_budget_ledger"]["selected_support_closed"] == 40
    assert successor_175["weighted_budget_ledger"]["selected_l1_closed"] == 74
    assert successor_175["clearance_ranked_queues"]["y"] == []
    assert successor_175["clearance_ranked_queues"]["z"][0]["distinguished_index"] == 50
    assert close(
        successor_175["weighted_budget_ledger"]["remaining_budget"],
        0.002509574053866367,
    )
    assert main_50["selected_thimble"]["line_chart"] == "z"
    assert main_50["selected_thimble"]["near_node_colliding_pair_zero_based"] == [1, 2]
    assert main_50["scope"]["A123_projective_line_chart_covariance_consumed"]
    assert close(
        main_50["validated_main_transport"]["uniform_integral_radius_upper"],
        1.258544559744545e-7,
    )
    assert main_50["validated_main_transport"]["accepted_step_count"] == 92
    assert main_50["validated_main_transport"]["rejected_step_count"] == 30
    assert close(tail_50["E32_endpoint_tail"]["interval_radius_upper"], 3.890338897381829e-10)
    assert len(tail_50["regular_segments"]) == 768
    assert close(full_50["full_E32_thimble"]["interval_radius_upper"], 1.78374099046863e-7)
    assert full_50["full_E32_thimble"]["floating_candidate_contained"]
    assert full_50["A134_radius_ledger"]["fallback_met"]
    assert successor_176["new_accepted_full_interval"]["distinguished_index"] == 50
    assert successor_176["weighted_budget_ledger"]["selected_support_closed"] == 41
    assert successor_176["weighted_budget_ledger"]["selected_l1_closed"] == 75
    assert successor_176["clearance_ranked_queues"]["y"] == []
    assert successor_176["clearance_ranked_queues"]["z"][0]["distinguished_index"] == 66
    assert close(
        successor_176["weighted_budget_ledger"]["remaining_budget"],
        0.0025093956717539695,
    )
    note = NOTE.read_text(encoding="utf-8")
    assert "Intermediate endpoint radii can contract" in note
    assert "Earlier manually aborted d057 probes therefore do not" in note

    print("q79 E32 physical-generator zonotope transport audit: PASS")
    print("closed: d057,d037,d060,d087,d011,d086,d048,d088,d033,d010,d012,d017,d051,d055,d034,d059,d031,d039,d014,d075,d018,d001,d046,d089,d069,d050 zonotope main/full intervals")
    print("closed: 3971 uncompressed recurrence steps; certified cutoff-period reuse")
    print("frontier: A176 support 41/71 and L1 75/123; y queue exhausted, 30 supports remain")
    print("open: weighted sum and fixed-carrier exact decision")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
