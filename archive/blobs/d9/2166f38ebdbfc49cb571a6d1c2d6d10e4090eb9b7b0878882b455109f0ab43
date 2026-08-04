from __future__ import annotations

import hashlib
import json
from pathlib import Path

from flint import acb

import certify_q79_selected_alignment_E32_thimble_polygonal_main_interval_tail_reuse_zonotope as reuse
import certify_q79_selected_side_beta_defect_transport as validated


ROOT = Path(__file__).resolve().parents[1]
PERIOD_DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
)
MAIN = PERIOD_DIRECTORY / "d047_selected_058.E32_main.interval.packet.json"
TAIL = PERIOD_DIRECTORY / "d047_selected_058.E32_tail.interval.packet.json"
ARCHIVE = PERIOD_DIRECTORY / "d047_selected_058.E32_main.pre_tail_refinement.interval.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def main() -> int:
    main_packet = load(MAIN)
    tail = load(TAIL)
    if int(main_packet["selected_thimble"]["distinguished_index"]) != 47:
        raise AssertionError("main packet is not d047")
    if int(tail["selected_thimble"]["distinguished_index"]) != 47:
        raise AssertionError("tail packet is not d047")
    if not main_packet["scope"]["main_homogeneous_Gauss_Manin_segment_interval_closed"]:
        raise AssertionError("main interval is not closed")
    if not tail["scope"]["endpoint_tail_interval_closed"]:
        raise AssertionError("refined endpoint tail is not closed")
    if len(tail["regular_segments"]) not in {384, 768, 1536, 3072, 6144}:
        raise AssertionError("d047 refined tail is outside the certified doubling ladder")

    reference = tail["cutoff_direct_period_reference"]
    transported = main_packet["near_node_direct_cycle_interval"]
    if reference["pair_zero_based"] != transported["pair_zero_based"]:
        raise AssertionError("refined tail changed the certified nodal pair")
    if len(reference["period_centers"]) != len(transported["initial_period_intervals"]):
        raise AssertionError("cutoff period dimensions differ")
    source_radius = float(reference["maximum_component_radius"])
    current_balls = []
    containments = []
    for center, old_bounds in zip(
        reference["period_centers"],
        transported["initial_period_intervals"],
    ):
        current = acb(
            reuse.serialized_center_ball(center["real"], source_radius),
            reuse.serialized_center_ball(center["imaginary"], source_radius),
        )
        old = validated.interval_from_bounds(old_bounds)
        contained = old.contains(current)
        current_balls.append(current)
        containments.append(bool(contained))
    if not all(containments):
        raise AssertionError("a refined cutoff-period ball escapes the transported initial interval")

    if not ARCHIVE.exists():
        ARCHIVE.write_bytes(MAIN.read_bytes())
    archive = load(ARCHIVE)
    if archive["validated_main_transport"] != main_packet["validated_main_transport"]:
        raise AssertionError("pre-refinement main archive changed")
    old_tail_hash = main_packet["authority"]["certified_tail_cutoff_period_source_sha256"]
    current_tail_hash = sha256(TAIL)
    main_packet["authority"]["pre_refinement_main_source"] = relative(ARCHIVE)
    main_packet["authority"]["pre_refinement_main_source_sha256"] = sha256(ARCHIVE)
    main_packet["authority"]["refined_tail_reuse_promotion_source"] = relative(Path(__file__))
    main_packet["authority"]["refined_tail_reuse_promotion_source_sha256"] = sha256(Path(__file__))
    main_packet["authority"]["certified_tail_cutoff_period_source_sha256"] = current_tail_hash
    main_packet["refined_tail_reuse_promotion"] = {
        "theorem": (
            "a validated transport from an initial interval remains valid when the "
            "replacement certified initial payload is contained in that interval"
        ),
        "pre_refinement_tail_sha256": old_tail_hash,
        "refined_tail_path": relative(TAIL),
        "refined_tail_sha256": current_tail_hash,
        "refined_tail_regular_segments": len(tail["regular_segments"]),
        "refined_tail_radius_upper": tail["E32_endpoint_tail"]["interval_radius_upper"],
        "refined_source_maximum_component_radius": source_radius,
        "transported_initial_interval_count": len(current_balls),
        "refined_cutoff_balls_contained_componentwise": containments,
        "all_refined_cutoff_balls_contained": True,
        "main_transport_steps_reused_without_recalculation": True,
    }
    main_packet["scope"]["refined_endpoint_tail_cutoff_payload_contained"] = True
    main_packet["scope"]["refined_tail_main_transport_reuse_promoted"] = True
    dump(MAIN, main_packet)
    print(f"wrote {relative(ARCHIVE)}")
    print(f"updated {relative(MAIN)}")
    print(
        json.dumps(
            {
                "distinguished_index": 47,
                "refined_tail_regular_segments": len(tail["regular_segments"]),
                "refined_tail_radius_upper": tail["E32_endpoint_tail"]["interval_radius_upper"],
                "all_refined_cutoff_balls_contained": True,
                "transported_main_radius_upper": main_packet["E32_main_segment"]["interval_radius_upper"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
