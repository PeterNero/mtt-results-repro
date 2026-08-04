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
PACKET = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_fourth_full_interval.packet.json"
A138 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_batch_frontier.packet.json"
FRONTIER = PERIOD_DIRECTORY / "U6_frontier_after_A139.packet.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79E32ClearanceRankedFourthFullInterval_v1.md"
CANDIDATE = ROOT / "candidate_data" / "selected_q79e32clearancerankedfourthfullinterval.candidate.json"
CERTIFICATE = ROOT / "certificates" / "selected_q79e32clearancerankedfourthfullinterval.certificate.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def resolve(path: str) -> Path:
    return ROOT / Path(path)


def close(left: float, right: float, tolerance: float = 2e-18) -> bool:
    return math.isclose(left, right, rel_tol=1e-13, abs_tol=tolerance)


def main() -> int:
    packet = load(PACKET)
    prior = load(A138)
    frontier = load(FRONTIER)
    candidate = load(CANDIDATE)
    certificate = load(CERTIFICATE)

    assert packet["artifact"] == "A139"
    assert packet["schema"] == "MTTQ79SelectedE32ClearanceRankedFourthFullInterval.v1"
    assert packet["status"] == "FOUR_SELECTED_FULL_E32_THIMBLE_INTERVALS_CLOSED_BATCH_EXECUTION_OPEN"
    assert packet["scope"]["four_selected_full_E32_thimble_intervals_closed"]
    assert packet["scope"]["all_accepted_intervals_meet_uniform_fallback"]
    assert not packet["scope"]["weighted_71_thimble_interval_closed"]
    assert not packet["scope"]["fixed_carrier_exact_separation_closed"]
    assert not packet["scope"]["observed_SM_values_used"]

    for authority in packet["authority"]:
        path = resolve(authority["path"])
        assert path.exists(), authority["path"]
        assert sha256(path) == authority["sha256"], authority["path"]
    predecessor = packet["append_only_predecessor"]
    assert predecessor["path"] == str(A138.relative_to(ROOT)).replace("\\", "/")
    assert predecessor["sha256"] == sha256(A138)
    assert predecessor["accepted_distinguished_indices"] == [4, 19, 61]

    rows = packet["accepted_full_intervals"]
    assert [row["distinguished_index"] for row in rows] == [4, 19, 28, 61]
    assert {row["distinguished_index"] for row in prior["accepted_full_intervals"]} == {4, 19, 61}
    new = packet["new_accepted_full_interval"]
    assert new == next(row for row in rows if row["distinguished_index"] == 28)
    assert new["root_id"] == "selected_018"
    assert new["line_chart"] == "y"
    assert new["coefficient"] == 2
    assert new["coefficient_l1"] == 2
    assert new["tail_regular_segments"] == 384
    assert close(new["tail_radius_upper"], 4.2489083895702615e-6)
    assert close(new["main_radius_upper"], 5.821845422307775e-7)
    assert close(new["full_interval_radius_upper"], 5.072241506809406e-6)
    assert new["fallback_margin"] > 0

    expected_cost = abs(new["coefficient"]) * (
        new["full_interval_radius_upper"] + new["A131_center_difference"]
    )
    assert close(new["weighted_radius_plus_displacement_cost"], expected_cost)
    ledger = packet["weighted_budget_ledger"]
    old_ledger = prior["weighted_budget_ledger"]
    assert ledger["selected_support_closed"] == 4
    assert ledger["selected_support_total"] == 71
    assert ledger["selected_l1_closed"] == 10
    assert ledger["selected_l1_total"] == 123
    assert ledger["remaining_support"] == 67
    assert ledger["remaining_l1_weight"] == 113
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

    queued = [
        row
        for chart in ("y", "z")
        for row in packet["clearance_ranked_queues"][chart]
    ]
    assert not ({4, 19, 28, 61} & {row["distinguished_index"] for row in queued})
    assert packet["clearance_ranked_queues"]["y"][0]["distinguished_index"] == 20
    assert packet["clearance_ranked_queues"]["y"][0]["coefficient"] == -3
    assert [row["distinguished_index"] for row in packet["partial_interval_diagnostics"]] == [47]

    assert frontier["schema"] == "MTTU6FrontierAfterA139.v1"
    assert frontier["selected_support_closed"] == 4
    assert frontier["selected_l1_closed"] == 10
    assert close(frontier["remaining_weighted_budget"], ledger["remaining_budget"])
    assert frontier["partial_hard_rows"] == [47]

    assert candidate["artifact"] == "A139"
    assert candidate["accepted_full_interval_count"] == 4
    assert candidate["packet_sha256"] == sha256(PACKET)
    assert candidate["frontier_sha256"] == sha256(FRONTIER)
    assert candidate["note_sha256"] == sha256(NOTE)
    assert not candidate["weighted_interval_closed"]
    assert not candidate["closure_claimed"]
    assert certificate["candidate_sha256"] == sha256(CANDIDATE)
    assert certificate["accepted_full_interval_count"] == 4
    assert not certificate["weighted_interval_closed"]
    assert not certificate["closure_claimed"]
    note = NOTE.read_text(encoding="utf-8")
    assert "4/71 support" in note
    assert "d020" in note
    assert "d047 row remains" in note and "partial" in note

    print("q79 A139 clearance-ranked fourth E32 interval audit: PASS")
    print("closed: d004, d019, d028, d061; support 4/71 and L1 10/123")
    print("closed: append-only budget transition and deterministic d020 successor")
    print("open: d047 hard main, 67 supports, z adapter, weighted sum, fixed carrier")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
