from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
PERIOD_DIRECTORY = DIRECTORY / "selected_alignment_thimble_periods"
A134 = PERIOD_DIRECTORY / "selected_alignment_height4_E32_handle_interval_and_thimble_cutset.packet.json"
A135 = PERIOD_DIRECTORY / "selected_alignment_height4_E32_thimble_regular_singular_reduction.packet.json"
A136 = PERIOD_DIRECTORY / "selected_alignment_E32_hensel_seed_and_first_full_interval.packet.json"
A137 = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_second_full_interval.packet.json"
FAN = DIRECTORY / "selected_alignment_distinguished_radial_fan.interval.packet.json"
PACKET = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_batch_frontier.packet.json"
FRONTIER = PERIOD_DIRECTORY / "U6_frontier_after_A138.packet.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79E32ClearanceRankedBatchFrontier_v1.md"
SLUG = "selected_q79e32clearancerankedbatchfrontier"
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


def unique(pattern: str) -> Path | None:
    rows = list(PERIOD_DIRECTORY.glob(pattern))
    if len(rows) > 1:
        raise AssertionError(f"non-unique batch artifact pattern: {pattern}")
    return rows[0] if rows else None


def main() -> int:
    a134 = load(A134)
    a135 = load(A135)
    a136 = load(A136)
    a137 = load(A137)
    fan = load(FAN)
    if not a135["local_theorem"]["proved_for_all_selected_thimbles"]:
        raise AssertionError("A135 local theorem is not closed")
    if not a136["scope"]["first_selected_full_E32_thimble_interval_closed"]:
        raise AssertionError("A136 first full interval is not closed")
    if not a137["scope"]["second_selected_full_E32_thimble_interval_closed"]:
        raise AssertionError("A137 second full interval is not closed")

    manifest = a134["selected_E32_decomposition"]["primitive_thimble_chain"]
    coefficients = {
        int(row["distinguished_index"]): int(row["coefficient"])
        for row in manifest
    }
    candidate_rows = {}
    for path in PERIOD_DIRECTORY.glob("*.thimble_period.candidate.json"):
        row = load(path)
        candidate_rows[int(row["distinguished_index"])] = (path, row)
    fan_rows = {
        int(row["distinguished_index"]): row
        for row in fan["distinguished_positive_meridians"]
    }
    if len(candidate_rows) != 90 or len(fan_rows) != 90:
        raise AssertionError("selected thimble/fan inventory changed")

    fallback = float(
        a134["strict_budget_ledger"]["sufficient_uniform_per_unit_thimble_radius"]
    )
    initial_budget = float(
        a134["strict_budget_ledger"]["remaining_weighted_thimble_combination_radius_budget"]
    )
    authority_paths = {A134, A135, A136, A137, FAN, Path(__file__)}
    closed = []
    partial = []
    total_cost = 0.0
    for index in sorted(coefficients):
        candidate_path, source = candidate_rows[index]
        stem = f"d{index:03d}_{source['root_id']}"
        nodal_path = PERIOD_DIRECTORY / f"{stem}.nodal_factor.interval.packet.json"
        tail_path = PERIOD_DIRECTORY / f"{stem}.E32_tail.interval.packet.json"
        main_path = PERIOD_DIRECTORY / f"{stem}.E32_main.interval.packet.json"
        full_path = PERIOD_DIRECTORY / f"{stem}.E32_full.interval.packet.json"
        if full_path.exists():
            if not all(path.exists() for path in (nodal_path, tail_path, main_path)):
                raise AssertionError(f"full interval d{index:03d} misses a component")
            full = load(full_path)
            if not full["scope"]["single_full_E32_thimble_interval_closed"]:
                raise AssertionError(f"full interval d{index:03d} is not closed")
            if not full["A134_radius_ledger"]["fallback_met"]:
                raise AssertionError(f"full interval d{index:03d} misses fallback")
            if not full["full_E32_thimble"]["floating_candidate_contained"]:
                raise AssertionError(f"A131 center d{index:03d} is outside the ball")
            radius = float(full["full_E32_thimble"]["interval_radius_upper"])
            displacement = float(
                full["full_E32_thimble"]["floating_candidate_center_difference"]
            )
            coefficient = coefficients[index]
            cost = abs(coefficient) * (radius + displacement)
            total_cost += cost
            main = load(main_path)
            tail = load(tail_path)
            closed.append(
                {
                    "distinguished_index": index,
                    "root_id": source["root_id"],
                    "line_chart": source["line_chart"],
                    "coefficient": coefficient,
                    "coefficient_l1": abs(coefficient),
                    "tail_regular_segments": len(tail["regular_segments"]),
                    "tail_radius_upper": tail["E32_endpoint_tail"][
                        "interval_radius_upper"
                    ],
                    "main_certificate_method": main["validated_main_transport"][
                        "certificate_method"
                    ],
                    "main_radius_upper": main["E32_main_segment"][
                        "interval_radius_upper"
                    ],
                    "full_interval_center": full["full_E32_thimble"][
                        "interval_center"
                    ],
                    "full_interval_radius_upper": radius,
                    "A131_center_difference": displacement,
                    "weighted_radius_plus_displacement_cost": cost,
                    "fallback_margin": fallback - radius,
                }
            )
            authority_paths.update(
                {candidate_path, nodal_path, tail_path, main_path, full_path}
            )
        elif nodal_path.exists() or tail_path.exists() or main_path.exists():
            partial.append(
                {
                    "distinguished_index": index,
                    "root_id": source["root_id"],
                    "line_chart": source["line_chart"],
                    "coefficient": coefficients[index],
                    "nodal_factor_closed": nodal_path.exists(),
                    "endpoint_tail_closed": tail_path.exists(),
                    "main_interval_closed": main_path.exists(),
                    "full_interval_closed": False,
                }
            )
            authority_paths.add(candidate_path)
            authority_paths.update(
                path for path in (nodal_path, tail_path, main_path) if path.exists()
            )

    closed_ids = {row["distinguished_index"] for row in closed}
    partial_ids = {row["distinguished_index"] for row in partial}
    remaining_budget = initial_budget - total_cost
    closed_l1 = sum(row["coefficient_l1"] for row in closed)
    total_l1 = sum(abs(value) for value in coefficients.values())
    if remaining_budget <= 0:
        raise AssertionError("closed batch exhausts the weighted budget")

    queues = {"y": [], "z": []}
    for index, coefficient in coefficients.items():
        if index in closed_ids or index in partial_ids:
            continue
        _candidate_path, source = candidate_rows[index]
        fan_row = fan_rows[index]
        critical = float(
            fan_row["outbound_segment"]["critical_ball_clearance_lower"]
        )
        chart = float(
            fan_row["outbound_segment"]["selected_y_chart_zero_clearance_lower"]
        )
        clearance = min(critical, chart)
        queues[source["line_chart"]].append(
            {
                "distinguished_index": index,
                "root_id": source["root_id"],
                "coefficient": coefficient,
                "coefficient_l1": abs(coefficient),
                "critical_clearance_lower": critical,
                "selected_y_chart_zero_clearance_lower": chart,
                "priority_score_l1_times_clearance": abs(coefficient) * clearance,
            }
        )
    for rows in queues.values():
        rows.sort(
            key=lambda row: (
                -row["priority_score_l1_times_clearance"],
                -row["coefficient_l1"],
                row["distinguished_index"],
            )
        )

    packet = {
        "schema": "MTTQ79SelectedE32ClearanceRankedBatchFrontier.v1",
        "artifact": "A138",
        "status": "THREE_SELECTED_FULL_E32_THIMBLE_INTERVALS_CLOSED_BATCH_EXECUTION_OPEN",
        "authority": [
            {"path": relative(path), "sha256": sha256(path)}
            for path in sorted(authority_paths, key=lambda path: relative(path))
        ],
        "accepted_full_intervals": closed,
        "partial_interval_diagnostics": partial,
        "weighted_budget_ledger": {
            "A134_initial_remaining_budget": initial_budget,
            "certified_radius_plus_displacement_cost": total_cost,
            "remaining_budget": remaining_budget,
            "selected_support_closed": len(closed),
            "selected_support_total": len(manifest),
            "selected_l1_closed": closed_l1,
            "selected_l1_total": total_l1,
            "remaining_support": len(manifest) - len(closed),
            "remaining_l1_weight": total_l1 - closed_l1,
        },
        "clearance_ranked_queues": {
            "policy": "within each available chart, maximize coefficient-L1 times certified radial clearance; keep partial hard rays out of the fresh queue",
            "y": queues["y"],
            "z": queues["z"],
        },
        "scope": {
            "observed_SM_values_used": False,
            "three_selected_full_E32_thimble_intervals_closed": len(closed) == 3,
            "all_accepted_intervals_meet_uniform_fallback": all(
                row["full_interval_radius_upper"] < fallback for row in closed
            ),
            "weighted_71_thimble_interval_closed": False,
            "fixed_carrier_exact_separation_closed": False,
        },
        "next_required_artifact": "execute the y queue with the final-radius segmented policy while constructing the covariant z-chart interval adapter",
    }
    if closed_ids != {4, 19, 61}:
        raise AssertionError(f"A138 closed support changed: {sorted(closed_ids)}")
    dump(PACKET, packet)

    frontier = {
        "schema": "MTTU6FrontierAfterA138.v1",
        "status": "U6_THREE_FULL_E32_THIMBLE_INTERVALS_CLOSED_WEIGHTED_BATCH_OPEN",
        "closed": [
            "d004 coefficient +2 full interval",
            "d061 coefficient -3 full interval",
            "d019 coefficient +3 full interval",
            "reusable clearance-ranked weighted batch ledger",
        ],
        "active_target": packet["next_required_artifact"],
        "selected_support_closed": len(closed),
        "selected_support_total": len(manifest),
        "selected_l1_closed": closed_l1,
        "selected_l1_total": total_l1,
        "remaining_weighted_budget": remaining_budget,
        "partial_hard_rows": sorted(partial_ids),
        "not_closed": [
            f"remaining {len(manifest) - len(closed)} full E32 thimble intervals",
            "z-chart interval adapter",
            "weighted 71-thimble E32 interval",
            "exact frozen-carrier decision",
        ],
    }
    dump(FRONTIER, frontier)

    third = next(row for row in closed if row["distinguished_index"] == 19)
    note = f"""# MTT Selected q79 E32 Clearance-Ranked Batch Frontier v1

## A138 result

The reusable weighted batch ledger now accepts three complete interval
thimbles: `d004` with coefficient `+2`, `d061` with coefficient `-3`, and
`d019` with coefficient `+3`. The new d019 execution has

```text
tail radius = {third['tail_radius_upper']:.16g}
main radius = {third['main_radius_upper']:.16g}
full radius = {third['full_interval_radius_upper']:.16g}
fallback    = {fallback:.16g}
```

The d019 tail required 1,536 local intervals because its widest initial
factor enclosure was not discriminant-separated at lower subdivisions. That
refinement produced a very tight full ball. All three independent A131 centers
are contained but are not used as bounds.

The exact ledger is now {len(closed)}/71 support and L1 weight
{closed_l1}/123. The remaining weighted budget is
`{remaining_budget:.16g}`. The d047 coefficient-four row remains partial with
node/Hensel and tail closed but no accepted main interval.

## Non-looping execution policy

The builder emits the remaining y and z queues directly from the selected A134
integer chain and the certified A127 radial clearances. Fresh rows are ordered
by coefficient L1 times available clearance. Accepted full packets are found
and charged automatically, so later runs do not reconstruct the ledger by
hand.

## Open

- {len(manifest) - len(closed)} complete thimble intervals, L1 weight {total_l1 - closed_l1};
- the covariant z-chart interval adapter;
- the weighted sum and exact frozen-carrier decision.
"""
    NOTE.write_text(note, encoding="utf-8")
    candidate = {
        "schema": "MTTSelectedQ79E32ClearanceRankedBatchFrontier.v1",
        "artifact": "A138",
        "status": packet["status"],
        "packet": relative(PACKET),
        "packet_sha256": sha256(PACKET),
        "frontier": relative(FRONTIER),
        "frontier_sha256": sha256(FRONTIER),
        "note": relative(NOTE),
        "note_sha256": sha256(NOTE),
        "observed_SM_values_used": False,
        "accepted_full_interval_count": len(closed),
        "weighted_interval_closed": False,
        "closure_claimed": False,
    }
    dump(CANDIDATE, candidate)
    certificate = {
        "schema": "MTTCertificate.v1",
        "certificate": "MTTSelectedQ79E32ClearanceRankedBatchFrontier",
        "status": packet["status"],
        "candidate_path": relative(CANDIDATE),
        "candidate_sha256": sha256(CANDIDATE),
        "observed_SM_values_used": False,
        "accepted_full_interval_count": len(closed),
        "weighted_interval_closed": False,
        "closure_claimed": False,
    }
    dump(CERTIFICATE, certificate)
    for path in (PACKET, FRONTIER, NOTE, CANDIDATE, CERTIFICATE):
        print(f"wrote {relative(path)}")
    print(
        json.dumps(
            {
                "closed_support": len(closed),
                "closed_l1": closed_l1,
                "remaining_support": len(manifest) - len(closed),
                "remaining_l1": total_l1 - closed_l1,
                "remaining_budget": remaining_budget,
                "next_y": queues["y"][0] if queues["y"] else None,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
