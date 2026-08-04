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
ADAPTER = ROOT / "scripts" / "certify_q79_height4_d021_continued_pair_full_residue_interval.py"
DEEP_SEED = (
    ROOT
    / "scripts"
    / "certify_q79_selected_alignment_single_E32_thimble_nodal_factor_deep_seed.py"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    summary = audit_target(
        index=21,
        root_id="selected_026",
        coefficient=3,
        artifact="A236",
    )
    main_packet = load(VALIDATED / "d021.n3.main8.refined.json")
    checkpoint = load(VALIDATED / "d021.n3.main8.refined.checkpoint.json")
    tail_packet = load(VALIDATED / "d021.n3.tail8.refined.json")
    full = load(VALIDATED / "d021.n3.full8.refined.json")
    assert checkpoint["d021_continued_pair_adapter_sha256"] == sha256(ADAPTER)
    assert checkpoint["deep_radial_pair_seed_engine_sha256"] == sha256(DEEP_SEED)
    assert checkpoint["cutoff_pair_zero_based"] == [4, 5]
    selected = main_packet["selected_target"]
    assert selected["near_node_colliding_pair_zero_based"] == [4, 5]
    assert not selected["instantaneous_closest_pair_rule_used"]
    assert selected["node_affinity_separation_margin_lower"] > 0.0
    assert tail_packet["selected_target"]["cutoff_pair_zero_based"] == [4, 5]
    assert full["strict_scope"]["certified_nodal_pair_selector_consumed"]
    assert not full["strict_scope"]["instantaneous_closest_pair_rule_used"]
    print("q79 A236 d021 refined full-residue interval audit: PASS")
    print(
        "closed: continued certified-node pair, eight-row main/tail splice, and "
        f"coefficient-plus-three chain ball; max row radius={summary['maximum_full_radius']:.6e}"
    )
    print("open: remaining exact chain, moving handle/beta intervals, and interval Jacobian")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
