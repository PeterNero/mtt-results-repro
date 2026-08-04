from __future__ import annotations

import hashlib
import json
from pathlib import Path

from q79_height4_target_refined_full_residue_audit_common import audit_target


ROOT = Path(__file__).resolve().parents[1]
VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
ADAPTER = ROOT / "scripts" / "certify_q79_height4_d057_continued_pair_full_residue_interval.py"
DEEP_SEED = (
    ROOT
    / "scripts"
    / "certify_q79_selected_alignment_single_E32_thimble_nodal_factor_deep_seed.py"
)
RETIRED = VALIDATED / "d057.n3.m8.o16.retired.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourD057RefinedFullResidueInterval_A246_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    summary = audit_target(
        index=57,
        root_id="selected_008",
        coefficient=4,
        artifact="A246",
    )
    checkpoint = load(VALIDATED / "d057.n3.main8.refined.checkpoint.json")
    main_packet = load(VALIDATED / "d057.n3.main8.refined.json")
    tail_packet = load(VALIDATED / "d057.n3.tail8.refined.json")
    full = load(VALIDATED / "d057.n3.full8.refined.json")
    retired = load(RETIRED)

    adapter_hash = sha256(ADAPTER)
    deep_seed_hash = sha256(DEEP_SEED)
    for label, packet in (("production", checkpoint), ("retired", retired)):
        require(packet["cutoff_pair_zero_based"] == [3, 4], f"A246 {label} pair changed")
        require(
            packet["d057_continued_pair_adapter_sha256"] == adapter_hash,
            f"A246 {label} adapter authority changed",
        )
        require(
            packet["deep_radial_pair_seed_engine_sha256"] == deep_seed_hash,
            f"A246 {label} deep-seed authority changed",
        )
        require(
            float(packet["configuration"]["maximum_integral_radius"]) == 1.0e-4,
            f"A246 {label} radius gate changed",
        )

    production_config = checkpoint["configuration"]
    require(checkpoint["complete"], "A246 production checkpoint is incomplete")
    require(int(production_config["order"]) == 24, "A246 production order changed")
    require(
        float(production_config["maximum_step"]) == 0.003,
        "A246 production maximum step changed",
    )
    require(int(main_packet["numerics"]["Taylor_order"]) == 24, "A246 main order changed")
    require(int(main_packet["numerics"]["dps"]) == 90, "A246 main precision changed")
    require(
        main_packet["selected_target"]["near_node_colliding_pair_zero_based"] == [3, 4],
        "A246 main selected pair changed",
    )
    require(
        tail_packet["selected_target"]["cutoff_pair_zero_based"] == [3, 4],
        "A246 tail selected pair changed",
    )
    for label, packet in (("main", main_packet), ("tail", tail_packet), ("full", full)):
        require(
            packet["authority"]["d057_continued_pair_adapter"]["sha256"] == adapter_hash,
            f"A246 {label} adapter hash changed",
        )
        require(
            packet["authority"]["deep_radial_pair_seed_engine"]["sha256"]
            == deep_seed_hash,
            f"A246 {label} deep-seed hash changed",
        )
        require(
            packet["strict_scope"]["certified_nodal_pair_selector_consumed"],
            f"A246 {label} lost nodal-pair provenance",
        )
        require(
            not packet["strict_scope"]["instantaneous_closest_pair_rule_used"],
            f"A246 {label} reverted to instantaneous pair selection",
        )

    retired_config = retired["configuration"]
    require(not retired["complete"], "A246 order-16 diagnostic unexpectedly completed")
    require(int(retired_config["order"]) == 16, "A246 retired order changed")
    require(
        float(retired_config["maximum_step"]) == 0.006,
        "A246 retired maximum step changed",
    )
    retired_fraction = float(retired["position"]) / float(retired["path_length"])
    require(0.4005 < retired_fraction < 0.4007, "A246 retired stopping fraction changed")
    retired_radius = float(retired["accepted_steps"][-1]["maximum_residue_coordinate_radius_upper"])
    require(0.999e-4 < retired_radius < 1.0e-4, "A246 retired run did not reach the radius gate")

    crossing = next(
        row
        for row in checkpoint["accepted_steps"]
        if float(row["end_arclength"]) / float(checkpoint["path_length"]) >= 0.4005
    )
    crossing_fraction = float(crossing["end_arclength"]) / float(checkpoint["path_length"])
    require(crossing_fraction < 0.404, "A246 production crossing moved")
    require(
        float(crossing["maximum_residue_coordinate_radius_upper"]) < 3.0e-5,
        "A246 order-24 crossing radius regressed",
    )

    note = NOTE.read_text(encoding="utf-8")
    require("order-16 straight transport" in note, "A246 note lost retired-run diagnosis")
    require("No larger radius budget or detour" in note, "A246 note lost unchanged-path claim")
    print("q79 A246 d057 continued-pair refined full-residue interval audit: PASS")
    print(
        "closed: A219 rank 13 with certified pair [3,4], unchanged straight path, "
        f"and coefficient-plus-four chain ball; max row radius={summary['maximum_full_radius']:.6e}"
    )
    print("open: d032 and 62 successors, moving handle/beta intervals, interval Jacobian")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
