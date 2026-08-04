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
ADAPTER = ROOT / "scripts" / "certify_q79_height4_d032_continued_pair_full_residue_interval.py"
DEEP_SEED = (
    ROOT
    / "scripts"
    / "certify_q79_selected_alignment_single_E32_thimble_nodal_factor_deep_seed.py"
)
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourD032RefinedFullResidueInterval_A248_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    summary = audit_target(
        index=32,
        root_id="selected_035",
        coefficient=-3,
        artifact="A248",
    )
    node = load(VALIDATED / "d032.n3.node.refined.json")
    checkpoint = load(VALIDATED / "d032.n3.main8.refined.checkpoint.json")
    main_packet = load(VALIDATED / "d032.n3.main8.refined.json")
    tail_packet = load(VALIDATED / "d032.n3.tail8.refined.json")
    full = load(VALIDATED / "d032.n3.full8.refined.json")

    adapter_hash = sha256(ADAPTER)
    deep_seed_hash = sha256(DEEP_SEED)
    require(checkpoint["cutoff_pair_zero_based"] == [4, 5], "A248 checkpoint pair changed")
    require(
        checkpoint["d032_continued_pair_adapter_sha256"] == adapter_hash,
        "A248 checkpoint adapter authority changed",
    )
    require(
        checkpoint["deep_radial_pair_seed_engine_sha256"] == deep_seed_hash,
        "A248 checkpoint deep-seed authority changed",
    )
    configuration = checkpoint["configuration"]
    require(checkpoint["complete"], "A248 production checkpoint is incomplete")
    require(int(configuration["order"]) == 16, "A248 production order changed")
    require(float(configuration["maximum_step"]) == 0.006, "A248 maximum step changed")
    require(
        float(configuration["maximum_integral_radius"]) == 1.0e-4,
        "A248 radius gate changed",
    )
    require(int(main_packet["numerics"]["Taylor_order"]) == 16, "A248 main order changed")
    require(int(main_packet["numerics"]["dps"]) == 70, "A248 main precision changed")
    require(
        main_packet["selected_target"]["near_node_colliding_pair_zero_based"] == [4, 5],
        "A248 main selected pair changed",
    )
    require(
        tail_packet["selected_target"]["cutoff_pair_zero_based"] == [4, 5],
        "A248 tail selected pair changed",
    )
    for label, packet in (("node", node), ("main", main_packet), ("tail", tail_packet), ("full", full)):
        require(
            packet["authority"]["d032_continued_pair_adapter"]["sha256"] == adapter_hash,
            f"A248 {label} adapter hash changed",
        )
        require(
            packet["authority"]["deep_radial_pair_seed_engine"]["sha256"]
            == deep_seed_hash,
            f"A248 {label} deep-seed hash changed",
        )
        require(
            packet["strict_scope"]["certified_nodal_pair_selector_consumed"],
            f"A248 {label} lost nodal-pair provenance",
        )
        require(
            not packet["strict_scope"]["instantaneous_closest_pair_rule_used"],
            f"A248 {label} reverted to instantaneous pair selection",
        )

    require(summary["accepted_steps"] == 313, "A248 accepted-step count changed")
    require(summary["orientation"] == -1, "A248 orientation changed")
    note = NOTE.read_text(encoding="utf-8")
    require("coefficient-minus-three" in note, "A248 note lost chain coefficient")
    print("q79 A248 d032 continued-pair refined full-residue interval audit: PASS")
    print(
        "closed: A219 rank 14 with certified pair [4,5] and coefficient-minus-three "
        f"chain ball; max row radius={summary['maximum_full_radius']:.6e}"
    )
    print("open: d027 and 61 successors, moving handle/beta intervals, interval Jacobian")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
