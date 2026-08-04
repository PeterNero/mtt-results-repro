from __future__ import annotations

import argparse
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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Append one newly certified selected E32 full interval to a frozen ranked ledger."
    )
    parser.add_argument("--artifact", required=True)
    parser.add_argument("--predecessor", required=True)
    parser.add_argument("--distinguished-index", type=int, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    artifact = args.artifact.upper()
    if not artifact.startswith("A") or not artifact[1:].isdigit():
        raise AssertionError("artifact must have the form A<number>")
    predecessor_path = ROOT / Path(args.predecessor)
    if not predecessor_path.exists():
        raise AssertionError(f"missing predecessor {args.predecessor}")
    predecessor = load(predecessor_path)
    a134 = load(A134)
    index = args.distinguished_index
    if index in {
        int(row["distinguished_index"])
        for row in predecessor["accepted_full_intervals"]
    }:
        raise AssertionError(f"d{index:03d} is already closed")

    source_path = unique(f"d{index:03d}_*.thimble_period.candidate.json")
    nodal_path = unique(f"d{index:03d}_*.nodal_factor.interval.packet.json")
    tail_path = unique(f"d{index:03d}_*.E32_tail.interval.packet.json")
    main_path = unique(f"d{index:03d}_*.E32_main.interval.packet.json")
    full_path = unique(f"d{index:03d}_*.E32_full.interval.packet.json")
    source = load(source_path)
    tail = load(tail_path)
    main_interval = load(main_path)
    full = load(full_path)
    if int(source["distinguished_index"]) != index:
        raise AssertionError("source index mismatch")
    chart = source["line_chart"]
    if chart not in ("y", "z"):
        raise AssertionError("unsupported line chart")
    if not predecessor["clearance_ranked_queues"][chart]:
        raise AssertionError(f"predecessor {chart} queue is empty")
    if int(
        predecessor["clearance_ranked_queues"][chart][0]["distinguished_index"]
    ) != index:
        raise AssertionError(
            f"d{index:03d} is not the frozen head of the {chart} queue"
        )
    if not full["scope"]["single_full_E32_thimble_interval_closed"]:
        raise AssertionError("full interval is not closed")
    if not full["A134_radius_ledger"]["fallback_met"]:
        raise AssertionError("full interval misses the A134 per-unit fallback")
    if not full["full_E32_thimble"]["floating_candidate_contained"]:
        raise AssertionError("independent A131 center is outside the full interval")

    manifest = a134["selected_E32_decomposition"]["primitive_thimble_chain"]
    coefficient_by_index = {
        int(row["distinguished_index"]): int(row["coefficient"])
        for row in manifest
    }
    coefficient = coefficient_by_index[index]
    queue_coefficient = int(
        predecessor["clearance_ranked_queues"][chart][0]["coefficient"]
    )
    if coefficient != queue_coefficient:
        raise AssertionError("queue coefficient disagrees with the A134 chain")

    fallback = float(
        a134["strict_budget_ledger"]["sufficient_uniform_per_unit_thimble_radius"]
    )
    radius = float(full["full_E32_thimble"]["interval_radius_upper"])
    displacement = float(
        full["full_E32_thimble"]["floating_candidate_center_difference"]
    )
    cost = abs(coefficient) * (radius + displacement)
    row = {
        "distinguished_index": index,
        "root_id": source["root_id"],
        "line_chart": chart,
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
    closed = sorted(
        predecessor["accepted_full_intervals"] + [row],
        key=lambda item: int(item["distinguished_index"]),
    )
    old_ledger = predecessor["weighted_budget_ledger"]
    support_closed = int(old_ledger["selected_support_closed"]) + 1
    l1_closed = int(old_ledger["selected_l1_closed"]) + abs(coefficient)
    remaining_support = int(old_ledger["remaining_support"]) - 1
    remaining_l1 = int(old_ledger["remaining_l1_weight"]) - abs(coefficient)
    certified_cost = float(
        old_ledger["certified_radius_plus_displacement_cost"]
    ) + cost
    remaining_budget = float(old_ledger["remaining_budget"]) - cost
    if remaining_budget <= 0:
        raise AssertionError("new row exhausts the weighted radius budget")

    queues = {
        queue_chart: [
            queue_row
            for queue_row in predecessor["clearance_ranked_queues"][queue_chart]
            if int(queue_row["distinguished_index"]) != index
        ]
        for queue_chart in ("y", "z")
    }
    z_adapter_closed = any(
        item["line_chart"] == "z" for item in closed
    )
    suffix = artifact.lower()
    packet_path = PERIOD_DIRECTORY / f"selected_alignment_E32_clearance_ranked_successor_{artifact}.packet.json"
    frontier_path = PERIOD_DIRECTORY / f"U6_frontier_after_{artifact}.packet.json"
    note_path = ROOT / "proof_corpus" / f"MTT_Selected_q79E32ClearanceRankedSuccessor_{artifact}_v1.md"
    slug = f"selected_q79e32clearancerankedsuccessor{suffix}"
    candidate_path = ROOT / "candidate_data" / f"{slug}.candidate.json"
    certificate_path = ROOT / "certificates" / f"{slug}.certificate.json"
    authority_paths = {
        A134,
        predecessor_path,
        source_path,
        nodal_path,
        tail_path,
        main_path,
        full_path,
        Path(__file__),
    }
    packet = {
        "schema": "MTTQ79SelectedE32ClearanceRankedAppendSuccessor.v1",
        "artifact": artifact,
        "status": "SELECTED_FULL_E32_THIMBLE_INTERVAL_SUCCESSOR_CLOSED_BATCH_EXECUTION_OPEN",
        "builder_configuration": {
            "predecessor": relative(predecessor_path),
            "distinguished_index": index,
            "queue_chart": chart,
            "queue_head_enforced": True,
        },
        "authority": [
            {"path": relative(path), "sha256": sha256(path)}
            for path in sorted(authority_paths, key=relative)
        ],
        "append_only_predecessor": {
            "path": relative(predecessor_path),
            "sha256": sha256(predecessor_path),
            "accepted_distinguished_indices": sorted(
                int(item["distinguished_index"])
                for item in predecessor["accepted_full_intervals"]
            ),
        },
        "new_accepted_full_interval": row,
        "accepted_full_intervals": closed,
        "partial_interval_diagnostics": predecessor[
            "partial_interval_diagnostics"
        ],
        "weighted_budget_ledger": {
            "A134_initial_remaining_budget": old_ledger[
                "A134_initial_remaining_budget"
            ],
            "certified_radius_plus_displacement_cost": certified_cost,
            "remaining_budget": remaining_budget,
            "selected_support_closed": support_closed,
            "selected_support_total": old_ledger["selected_support_total"],
            "selected_l1_closed": l1_closed,
            "selected_l1_total": old_ledger["selected_l1_total"],
            "remaining_support": remaining_support,
            "remaining_l1_weight": remaining_l1,
        },
        "clearance_ranked_queues": {
            "policy": predecessor["clearance_ranked_queues"]["policy"],
            "y": queues["y"],
            "z": queues["z"],
        },
        "scope": {
            "observed_SM_values_used": False,
            "selected_full_interval_count": support_closed,
            "new_queue_head_full_interval_closed": True,
            "all_accepted_intervals_meet_uniform_fallback": all(
                item["full_interval_radius_upper"] < fallback for item in closed
            ),
            "covariant_z_chart_interval_adapter_closed": z_adapter_closed,
            "weighted_71_thimble_interval_closed": False,
            "fixed_carrier_exact_separation_closed": False,
        },
        "next_required_artifact": (
            f"execute d{int(queues['y'][0]['distinguished_index']):03d} from the ranked y queue "
            + (
                "and continue the chart-covariant ranked batch"
                if z_adapter_closed
                else "while constructing the covariant z-chart interval adapter"
            )
            if queues["y"]
            else (
                "continue the certified z-chart queue"
                if z_adapter_closed
                else "construct the covariant z-chart interval adapter and execute the z queue"
            )
        ),
    }
    dump(packet_path, packet)

    frontier = {
        "schema": "MTTU6ClearanceRankedAppendFrontier.v1",
        "artifact": artifact,
        "status": "U6_SELECTED_E32_APPEND_SUCCESSOR_CLOSED_WEIGHTED_BATCH_OPEN",
        "newly_closed": f"d{index:03d} coefficient {coefficient:+d} full interval",
        "active_target": packet["next_required_artifact"],
        "selected_support_closed": support_closed,
        "selected_support_total": old_ledger["selected_support_total"],
        "selected_l1_closed": l1_closed,
        "selected_l1_total": old_ledger["selected_l1_total"],
        "remaining_weighted_budget": remaining_budget,
        "partial_hard_rows": sorted(
            int(item["distinguished_index"])
            for item in predecessor["partial_interval_diagnostics"]
        ),
        "not_closed": [
            f"remaining {remaining_support} full E32 thimble intervals",
            *([] if z_adapter_closed else ["z-chart interval adapter"]),
            "weighted 71-thimble E32 interval",
            "exact frozen-carrier decision",
        ],
    }
    dump(frontier_path, frontier)

    next_y = (
        f"d{int(queues['y'][0]['distinguished_index']):03d}"
        if queues["y"]
        else "none"
    )
    note = f"""# MTT Selected q79 E32 Clearance-Ranked Successor {artifact} v1

## Result

This append-only successor closes `d{index:03d}/{source['root_id']}` with
coefficient `{coefficient:+d}`. It was the frozen head of the predecessor's
`{chart}` queue. The node/Hensel factor, endpoint tail, polygonal main
transport, orientation splice, fallback, and independent-center containment
are all certified.

```text
tail radius = {row['tail_radius_upper']:.16g}
main radius = {row['main_radius_upper']:.16g}
full radius = {radius:.16g}
weighted cost including A131 displacement = {cost:.16g}
remaining weighted budget = {remaining_budget:.16g}
```

The ledger is now {support_closed}/71 support and L1 weight {l1_closed}/123.
There are {remaining_support} supports and L1 weight {remaining_l1} left. The
next ranked y-chart row is `{next_y}`. The d047 partial row remains uncounted.
The covariant z-chart interval adapter is {'closed by this append' if chart == 'z' else ('already closed' if z_adapter_closed else 'still open')}.
"""
    note_path.write_text(note, encoding="utf-8")
    candidate = {
        "schema": "MTTSelectedQ79E32ClearanceRankedAppendSuccessor.v1",
        "artifact": artifact,
        "status": packet["status"],
        "packet": relative(packet_path),
        "packet_sha256": sha256(packet_path),
        "frontier": relative(frontier_path),
        "frontier_sha256": sha256(frontier_path),
        "note": relative(note_path),
        "note_sha256": sha256(note_path),
        "observed_SM_values_used": False,
        "accepted_full_interval_count": support_closed,
        "weighted_interval_closed": False,
        "closure_claimed": False,
    }
    dump(candidate_path, candidate)
    certificate = {
        "schema": "MTTCertificate.v1",
        "certificate": "MTTSelectedQ79E32ClearanceRankedAppendSuccessor",
        "artifact": artifact,
        "status": packet["status"],
        "candidate_path": relative(candidate_path),
        "candidate_sha256": sha256(candidate_path),
        "observed_SM_values_used": False,
        "accepted_full_interval_count": support_closed,
        "weighted_interval_closed": False,
        "closure_claimed": False,
    }
    dump(certificate_path, certificate)
    for path in (
        packet_path,
        frontier_path,
        note_path,
        candidate_path,
        certificate_path,
    ):
        print(f"wrote {relative(path)}")
    print(
        json.dumps(
            {
                "artifact": artifact,
                "closed_support": support_closed,
                "closed_l1": l1_closed,
                "remaining_support": remaining_support,
                "remaining_l1": remaining_l1,
                "remaining_budget": remaining_budget,
                "next_y": queues["y"][0] if queues["y"] else None,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
