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
PACKET = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_successor_A140.packet.json"
PREDECESSOR = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_fourth_full_interval.packet.json"
FRONTIER = PERIOD_DIRECTORY / "U6_frontier_after_A140.packet.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79E32ClearanceRankedSuccessor_A140_v1.md"
CANDIDATE = ROOT / "candidate_data" / "selected_q79e32clearancerankedsuccessora140.candidate.json"
CERTIFICATE = ROOT / "certificates" / "selected_q79e32clearancerankedsuccessora140.certificate.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def close(left: float, right: float, tolerance: float = 2e-18) -> bool:
    return math.isclose(left, right, rel_tol=1e-13, abs_tol=tolerance)


def main() -> int:
    packet = load(PACKET)
    predecessor = load(PREDECESSOR)
    frontier = load(FRONTIER)
    candidate = load(CANDIDATE)
    certificate = load(CERTIFICATE)
    assert packet["artifact"] == "A140"
    assert packet["schema"] == "MTTQ79SelectedE32ClearanceRankedAppendSuccessor.v1"
    assert packet["builder_configuration"] == {
        "predecessor": str(PREDECESSOR.relative_to(ROOT)).replace("\\", "/"),
        "distinguished_index": 20,
        "queue_chart": "y",
        "queue_head_enforced": True,
    }
    assert packet["append_only_predecessor"]["sha256"] == sha256(PREDECESSOR)
    assert packet["append_only_predecessor"]["accepted_distinguished_indices"] == [4, 19, 28, 61]
    for authority in packet["authority"]:
        path = ROOT / authority["path"]
        assert path.exists(), authority["path"]
        assert sha256(path) == authority["sha256"], authority["path"]

    rows = packet["accepted_full_intervals"]
    assert [row["distinguished_index"] for row in rows] == [4, 19, 20, 28, 61]
    new = packet["new_accepted_full_interval"]
    assert new == next(row for row in rows if row["distinguished_index"] == 20)
    assert new["root_id"] == "selected_027"
    assert new["coefficient"] == -3
    assert new["coefficient_l1"] == 3
    assert new["tail_regular_segments"] == 384
    assert close(new["tail_radius_upper"], 2.207052666847176e-6)
    assert close(new["main_radius_upper"], 4.938223754893146e-7)
    assert close(new["full_interval_radius_upper"], 2.9053709624804473e-6)
    assert new["fallback_margin"] > 0
    expected_cost = 3 * (
        new["full_interval_radius_upper"] + new["A131_center_difference"]
    )
    assert close(new["weighted_radius_plus_displacement_cost"], expected_cost)

    ledger = packet["weighted_budget_ledger"]
    old = predecessor["weighted_budget_ledger"]
    assert ledger["selected_support_closed"] == 5
    assert ledger["selected_support_total"] == 71
    assert ledger["selected_l1_closed"] == 13
    assert ledger["selected_l1_total"] == 123
    assert ledger["remaining_support"] == 66
    assert ledger["remaining_l1_weight"] == 110
    assert close(
        ledger["certified_radius_plus_displacement_cost"],
        old["certified_radius_plus_displacement_cost"] + expected_cost,
    )
    assert close(ledger["remaining_budget"], old["remaining_budget"] - expected_cost)
    assert close(
        ledger["A134_initial_remaining_budget"]
        - ledger["certified_radius_plus_displacement_cost"],
        ledger["remaining_budget"],
    )
    assert ledger["remaining_budget"] > 0
    assert packet["scope"]["selected_full_interval_count"] == 5
    assert packet["scope"]["new_queue_head_full_interval_closed"]
    assert packet["scope"]["all_accepted_intervals_meet_uniform_fallback"]
    assert not packet["scope"]["weighted_71_thimble_interval_closed"]
    assert not packet["scope"]["observed_SM_values_used"]

    queued = [
        row
        for chart in ("y", "z")
        for row in packet["clearance_ranked_queues"][chart]
    ]
    assert not ({4, 19, 20, 28, 61} & {row["distinguished_index"] for row in queued})
    assert packet["clearance_ranked_queues"]["y"][0]["distinguished_index"] == 62
    assert [row["distinguished_index"] for row in packet["partial_interval_diagnostics"]] == [47]

    assert frontier["artifact"] == "A140"
    assert frontier["selected_support_closed"] == 5
    assert frontier["selected_l1_closed"] == 13
    assert frontier["partial_hard_rows"] == [47]
    assert close(frontier["remaining_weighted_budget"], ledger["remaining_budget"])
    assert candidate["artifact"] == "A140"
    assert candidate["accepted_full_interval_count"] == 5
    assert candidate["packet_sha256"] == sha256(PACKET)
    assert candidate["frontier_sha256"] == sha256(FRONTIER)
    assert candidate["note_sha256"] == sha256(NOTE)
    assert certificate["artifact"] == "A140"
    assert certificate["candidate_sha256"] == sha256(CANDIDATE)
    assert certificate["accepted_full_interval_count"] == 5
    assert not candidate["closure_claimed"] and not certificate["closure_claimed"]
    note = NOTE.read_text(encoding="utf-8")
    assert "5/71 support" in note and "d062" in note

    print("q79 A140 clearance-ranked append-successor audit: PASS")
    print("closed: d004, d019, d020, d028, d061; support 5/71 and L1 13/123")
    print("closed: reusable queue-head append builder; deterministic d062 successor")
    print("open: d047 hard main, 66 supports, z adapter, weighted sum, fixed carrier")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
