from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PERIOD_DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
)
A134 = PERIOD_DIRECTORY / "selected_alignment_height4_E32_handle_interval_and_thimble_cutset.packet.json"
A138 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_batch_frontier.packet.json"
PACKET = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_fourth_full_interval.packet.json"
FRONTIER = PERIOD_DIRECTORY / "U6_frontier_after_A139.packet.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79E32ClearanceRankedFourthFullInterval_v1.md"
SLUG = "selected_q79e32clearancerankedfourthfullinterval"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}.certificate.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def unique(pattern: str) -> Path:
    rows = list(PERIOD_DIRECTORY.glob(pattern))
    if len(rows) != 1:
        raise AssertionError(f"expected one artifact for {pattern}, found {len(rows)}")
    return rows[0]


def main() -> int:
    a134 = load(A134)
    a138 = load(A138)
    prior_closed = a138["accepted_full_intervals"]
    if {row["distinguished_index"] for row in prior_closed} != {4, 19, 61}:
        raise AssertionError("A138 accepted support changed")
    if a138["weighted_budget_ledger"]["selected_support_closed"] != 3:
        raise AssertionError("A138 ledger is not the frozen three-row baseline")

    index = 28
    source_path = unique("d028_*.thimble_period.candidate.json")
    nodal_path = unique("d028_*.nodal_factor.interval.packet.json")
    tail_path = unique("d028_*.E32_tail.interval.packet.json")
    main_path = unique("d028_*.E32_main.interval.packet.json")
    full_path = unique("d028_*.E32_full.interval.packet.json")
    source = load(source_path)
    tail = load(tail_path)
    main_interval = load(main_path)
    full = load(full_path)
    if source["distinguished_index"] != index or source["root_id"] != "selected_018":
        raise AssertionError("d028 source identity changed")
    if source["line_chart"] != "y":
        raise AssertionError("d028 is not on the certified y-chart route")
    if not full["scope"]["single_full_E32_thimble_interval_closed"]:
        raise AssertionError("d028 full interval is not closed")
    if not full["A134_radius_ledger"]["fallback_met"]:
        raise AssertionError("d028 misses the A134 per-unit fallback")
    if not full["full_E32_thimble"]["floating_candidate_contained"]:
        raise AssertionError("d028 does not contain the independent A131 center")

    manifest = a134["selected_E32_decomposition"]["primitive_thimble_chain"]
    coefficient_by_index = {
        int(row["distinguished_index"]): int(row["coefficient"])
        for row in manifest
    }
    coefficient = coefficient_by_index[index]
    if coefficient != 2:
        raise AssertionError("d028 coefficient changed")
    radius = float(full["full_E32_thimble"]["interval_radius_upper"])
    displacement = float(
        full["full_E32_thimble"]["floating_candidate_center_difference"]
    )
    fallback = float(
        a134["strict_budget_ledger"]["sufficient_uniform_per_unit_thimble_radius"]
    )
    cost = abs(coefficient) * (radius + displacement)
    row = {
        "distinguished_index": index,
        "root_id": source["root_id"],
        "line_chart": source["line_chart"],
        "coefficient": coefficient,
        "coefficient_l1": abs(coefficient),
        "tail_regular_segments": len(tail["regular_segments"]),
        "tail_radius_upper": tail["E32_endpoint_tail"]["interval_radius_upper"],
        "main_certificate_method": main_interval["validated_main_transport"][
            "certificate_method"
        ],
        "main_radius_upper": main_interval["E32_main_segment"][
            "interval_radius_upper"
        ],
        "full_interval_center": full["full_E32_thimble"]["interval_center"],
        "full_interval_radius_upper": radius,
        "A131_center_difference": displacement,
        "weighted_radius_plus_displacement_cost": cost,
        "fallback_margin": fallback - radius,
    }
    closed = sorted(prior_closed + [row], key=lambda item: item["distinguished_index"])
    if {item["distinguished_index"] for item in closed} != {4, 19, 28, 61}:
        raise AssertionError("A139 accepted support is not the append-only successor")

    prior_ledger = a138["weighted_budget_ledger"]
    remaining_budget = float(prior_ledger["remaining_budget"]) - cost
    certified_cost = float(
        prior_ledger["certified_radius_plus_displacement_cost"]
    ) + cost
    closed_l1 = int(prior_ledger["selected_l1_closed"]) + abs(coefficient)
    if remaining_budget <= 0:
        raise AssertionError("d028 exhausts the weighted radius budget")

    queues = {
        chart: [
            queue_row
            for queue_row in a138["clearance_ranked_queues"][chart]
            if int(queue_row["distinguished_index"]) != index
        ]
        for chart in ("y", "z")
    }
    if any(
        int(queue_row["distinguished_index"]) == index
        for chart in ("y", "z")
        for queue_row in queues[chart]
    ):
        raise AssertionError("closed d028 remains in a fresh queue")

    authority_paths = {
        A134,
        A138,
        source_path,
        nodal_path,
        tail_path,
        main_path,
        full_path,
        Path(__file__),
    }
    packet = {
        "schema": "MTTQ79SelectedE32ClearanceRankedFourthFullInterval.v1",
        "artifact": "A139",
        "status": "FOUR_SELECTED_FULL_E32_THIMBLE_INTERVALS_CLOSED_BATCH_EXECUTION_OPEN",
        "authority": [
            {"path": relative(path), "sha256": sha256(path)}
            for path in sorted(authority_paths, key=relative)
        ],
        "append_only_predecessor": {
            "path": relative(A138),
            "sha256": sha256(A138),
            "accepted_distinguished_indices": [4, 19, 61],
        },
        "new_accepted_full_interval": row,
        "accepted_full_intervals": closed,
        "partial_interval_diagnostics": a138["partial_interval_diagnostics"],
        "weighted_budget_ledger": {
            "A134_initial_remaining_budget": prior_ledger[
                "A134_initial_remaining_budget"
            ],
            "certified_radius_plus_displacement_cost": certified_cost,
            "remaining_budget": remaining_budget,
            "selected_support_closed": 4,
            "selected_support_total": prior_ledger["selected_support_total"],
            "selected_l1_closed": closed_l1,
            "selected_l1_total": prior_ledger["selected_l1_total"],
            "remaining_support": int(prior_ledger["remaining_support"]) - 1,
            "remaining_l1_weight": int(prior_ledger["remaining_l1_weight"])
            - abs(coefficient),
        },
        "clearance_ranked_queues": {
            "policy": a138["clearance_ranked_queues"]["policy"],
            "y": queues["y"],
            "z": queues["z"],
        },
        "scope": {
            "observed_SM_values_used": False,
            "four_selected_full_E32_thimble_intervals_closed": True,
            "all_accepted_intervals_meet_uniform_fallback": all(
                item["full_interval_radius_upper"] < fallback for item in closed
            ),
            "weighted_71_thimble_interval_closed": False,
            "fixed_carrier_exact_separation_closed": False,
        },
        "next_required_artifact": "execute d020 from the ranked y queue while constructing the covariant z-chart interval adapter",
    }
    if queues["y"][0]["distinguished_index"] != 20:
        raise AssertionError("d020 is not the next ranked fresh y row")
    dump(PACKET, packet)

    frontier = {
        "schema": "MTTU6FrontierAfterA139.v1",
        "status": "U6_FOUR_FULL_E32_THIMBLE_INTERVALS_CLOSED_WEIGHTED_BATCH_OPEN",
        "closed": [
            "d004 coefficient +2 full interval",
            "d019 coefficient +3 full interval",
            "d028 coefficient +2 full interval",
            "d061 coefficient -3 full interval",
            "append-only A138-to-A139 weighted ledger",
        ],
        "active_target": packet["next_required_artifact"],
        "selected_support_closed": 4,
        "selected_support_total": prior_ledger["selected_support_total"],
        "selected_l1_closed": closed_l1,
        "selected_l1_total": prior_ledger["selected_l1_total"],
        "remaining_weighted_budget": remaining_budget,
        "partial_hard_rows": sorted(
            row["distinguished_index"]
            for row in a138["partial_interval_diagnostics"]
        ),
        "not_closed": [
            f"remaining {int(prior_ledger['remaining_support']) - 1} full E32 thimble intervals",
            "z-chart interval adapter",
            "weighted 71-thimble E32 interval",
            "exact frozen-carrier decision",
        ],
    }
    dump(FRONTIER, frontier)

    note = f"""# MTT Selected q79 E32 Clearance-Ranked Fourth Full Interval v1

## A139 result

The append-only successor to A138 closes `d028/selected_018`, coefficient
`+2`, without changing the first three accepted rows. Its source-side node,
Hensel factor, 384-segment endpoint tail, polygonal main transport, and
orientation splice are all interval certified.

```text
tail radius = {row['tail_radius_upper']:.16g}
main radius = {row['main_radius_upper']:.16g}
full radius = {radius:.16g}
fallback    = {fallback:.16g}
weighted cost including A131 displacement = {cost:.16g}
```

The ledger is now 4/71 support and L1 weight {closed_l1}/123. The remaining
weighted budget is `{remaining_budget:.16g}`. The next fresh y-chart row under
the frozen A138 ranking is `d020`, coefficient `-3`. The d047 row remains
partial and is not counted.

## Open

- {int(prior_ledger['remaining_support']) - 1} complete thimble intervals,
  L1 weight {int(prior_ledger['remaining_l1_weight']) - abs(coefficient)};
- the covariant z-chart interval adapter;
- the weighted sum and exact frozen-carrier decision.
"""
    NOTE.write_text(note, encoding="utf-8")
    candidate = {
        "schema": "MTTSelectedQ79E32ClearanceRankedFourthFullInterval.v1",
        "artifact": "A139",
        "status": packet["status"],
        "packet": relative(PACKET),
        "packet_sha256": sha256(PACKET),
        "frontier": relative(FRONTIER),
        "frontier_sha256": sha256(FRONTIER),
        "note": relative(NOTE),
        "note_sha256": sha256(NOTE),
        "observed_SM_values_used": False,
        "accepted_full_interval_count": 4,
        "weighted_interval_closed": False,
        "closure_claimed": False,
    }
    dump(CANDIDATE, candidate)
    certificate = {
        "schema": "MTTCertificate.v1",
        "certificate": "MTTSelectedQ79E32ClearanceRankedFourthFullInterval",
        "status": packet["status"],
        "candidate_path": relative(CANDIDATE),
        "candidate_sha256": sha256(CANDIDATE),
        "observed_SM_values_used": False,
        "accepted_full_interval_count": 4,
        "weighted_interval_closed": False,
        "closure_claimed": False,
    }
    dump(CERTIFICATE, certificate)
    for path in (PACKET, FRONTIER, NOTE, CANDIDATE, CERTIFICATE):
        print(f"wrote {relative(path)}")
    print(
        json.dumps(
            {
                "closed_support": 4,
                "closed_l1": closed_l1,
                "remaining_support": int(prior_ledger["remaining_support"]) - 1,
                "remaining_l1": int(prior_ledger["remaining_l1_weight"])
                - abs(coefficient),
                "remaining_budget": remaining_budget,
                "next_y": queues["y"][0],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
