from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79e32clearancerankedbatchfrontier"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}.certificate.json"
LEGACY_D047_TAIL_SHA256 = "34195caa0a17c11dbe19f80a3b48491063c9c8e9762d810d79c4e08b43b01d37"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def close(left: float, right: float, tolerance: float = 1.0e-15) -> bool:
    return abs(left - right) <= tolerance * max(1.0, abs(left), abs(right))


def compatible_d047_tail_refinement(path: Path, expected: str) -> bool:
    if path.name != "d047_selected_058.E32_tail.interval.packet.json":
        return False
    if expected != LEGACY_D047_TAIL_SHA256:
        return False
    main_path = path.with_name("d047_selected_058.E32_main.interval.packet.json")
    archived_main_path = path.with_name(
        "d047_selected_058.E32_main.pre_tail_refinement.interval.packet.json"
    )
    if not main_path.exists() or not archived_main_path.exists():
        return False
    tail = load(path)
    main = load(main_path)
    archived_main = load(archived_main_path)
    return bool(
        tail["scope"]["endpoint_tail_interval_closed"]
        and len(tail["regular_segments"]) == 768
        and float(tail["E32_endpoint_tail"]["interval_radius_upper"])
        < 3.3274612007971886e-6
        and main["scope"]["refined_endpoint_tail_cutoff_payload_contained"]
        and main["scope"]["refined_tail_main_transport_reuse_promoted"]
        and main["refined_tail_reuse_promotion"]["all_refined_cutoff_balls_contained"]
        and main["authority"]["certified_tail_cutoff_period_source_sha256"]
        == sha256(path)
        and main["authority"]["pre_refinement_main_source_sha256"]
        == sha256(archived_main_path)
        and archived_main["authority"]["certified_tail_cutoff_period_source_sha256"]
        == expected
    )


def main() -> int:
    candidate = load(CANDIDATE)
    certificate = load(CERTIFICATE)
    require(certificate["candidate_sha256"] == sha256(CANDIDATE), "candidate hash")
    packet_path = ROOT / candidate["packet"]
    frontier_path = ROOT / candidate["frontier"]
    note_path = ROOT / candidate["note"]
    require(candidate["packet_sha256"] == sha256(packet_path), "packet hash")
    require(candidate["frontier_sha256"] == sha256(frontier_path), "frontier hash")
    require(candidate["note_sha256"] == sha256(note_path), "note hash")
    packet = load(packet_path)
    frontier = load(frontier_path)
    for row in packet["authority"]:
        path = ROOT / row["path"]
        require(path.exists(), f"missing authority {path}")
        require(
            sha256(path) == row["sha256"]
            or compatible_d047_tail_refinement(path, row["sha256"]),
            f"authority hash {path}",
        )
    require(packet["artifact"] == "A138", "artifact")
    require(
        packet["status"]
        == "THREE_SELECTED_FULL_E32_THIMBLE_INTERVALS_CLOSED_BATCH_EXECUTION_OPEN",
        "status",
    )

    authority = {row["path"]: ROOT / row["path"] for row in packet["authority"]}
    a134_path = next(
        path
        for name, path in authority.items()
        if name.endswith("selected_alignment_height4_E32_handle_interval_and_thimble_cutset.packet.json")
    )
    a134 = load(a134_path)
    coefficients = {
        int(row["distinguished_index"]): int(row["coefficient"])
        for row in a134["selected_E32_decomposition"]["primitive_thimble_chain"]
    }
    accepted = {
        int(row["distinguished_index"]): row
        for row in packet["accepted_full_intervals"]
    }
    require(set(accepted) == {4, 19, 61}, "accepted ids")
    require(
        {index: coefficients[index] for index in accepted}
        == {4: 2, 19: 3, 61: -3},
        "accepted coefficients",
    )
    fallback = float(
        a134["strict_budget_ledger"]["sufficient_uniform_per_unit_thimble_radius"]
    )
    total_cost = 0.0
    for index, row in accepted.items():
        full_path = next(
            path
            for name, path in authority.items()
            if name.endswith(f"d{index:03d}_{row['root_id']}.E32_full.interval.packet.json")
        )
        full = load(full_path)
        radius = float(full["full_E32_thimble"]["interval_radius_upper"])
        displacement = float(
            full["full_E32_thimble"]["floating_candidate_center_difference"]
        )
        cost = abs(coefficients[index]) * (radius + displacement)
        total_cost += cost
        require(close(row["full_interval_radius_upper"], radius), f"radius d{index:03d}")
        require(close(row["weighted_radius_plus_displacement_cost"], cost), f"cost d{index:03d}")
        require(radius < fallback, f"fallback d{index:03d}")
        require(full["full_E32_thimble"]["floating_candidate_contained"], f"containment d{index:03d}")
        require(full["scope"]["single_full_E32_thimble_interval_closed"], f"closure d{index:03d}")

    ledger = packet["weighted_budget_ledger"]
    initial = float(
        a134["strict_budget_ledger"]["remaining_weighted_thimble_combination_radius_budget"]
    )
    require(close(ledger["certified_radius_plus_displacement_cost"], total_cost), "total cost")
    require(close(ledger["remaining_budget"], initial - total_cost), "remaining budget")
    require(ledger["selected_support_closed"] == 3, "support closed")
    require(ledger["selected_support_total"] == 71, "support total")
    require(ledger["selected_l1_closed"] == 8, "L1 closed")
    require(ledger["selected_l1_total"] == 123, "L1 total")
    require(ledger["remaining_support"] == 68, "remaining support")
    require(ledger["remaining_l1_weight"] == 115, "remaining L1")

    partial = packet["partial_interval_diagnostics"]
    require(len(partial) == 1, "partial count")
    require(partial[0]["distinguished_index"] == 47, "partial d047")
    require(partial[0]["nodal_factor_closed"], "d047 node")
    require(partial[0]["endpoint_tail_closed"], "d047 tail")
    require(not partial[0]["main_interval_closed"], "d047 main remains open")

    y_queue = packet["clearance_ranked_queues"]["y"]
    z_queue = packet["clearance_ranked_queues"]["z"]
    require(y_queue[0]["distinguished_index"] == 28, "next y row")
    require(len(y_queue) == 26, "fresh y queue length")
    require(len(z_queue) == 41, "fresh z queue length")
    require(
        all(
            y_queue[index]["priority_score_l1_times_clearance"]
            >= y_queue[index + 1]["priority_score_l1_times_clearance"]
            for index in range(len(y_queue) - 1)
        ),
        "y priority order",
    )
    require(packet["scope"]["three_selected_full_E32_thimble_intervals_closed"], "three-row scope")
    require(packet["scope"]["all_accepted_intervals_meet_uniform_fallback"], "uniform fallback scope")
    require(not packet["scope"]["weighted_71_thimble_interval_closed"], "weighted remains open")
    require(not packet["scope"]["fixed_carrier_exact_separation_closed"], "carrier remains open")
    require(frontier["selected_support_closed"] == 3, "frontier support")
    require(frontier["selected_l1_closed"] == 8, "frontier L1")
    require(not candidate["closure_claimed"], "candidate overclaim")
    require(not certificate["closure_claimed"], "certificate overclaim")
    print("q79 A138 clearance-ranked E32 batch frontier audit: PASS")
    print("closed: d004, d019, d061; support 3/71 and L1 8/123")
    print("closed: reusable weighted ledger and deterministic y/z execution queues")
    print("open: d047 hard main, 68 supports, z adapter, weighted sum, fixed carrier")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
