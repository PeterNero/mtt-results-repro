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
        description="Promote the sole partial q79 E32 row after both ranked queues close."
    )
    parser.add_argument("--artifact", required=True)
    parser.add_argument("--predecessor", required=True)
    parser.add_argument("--distinguished-index", type=int, default=47)
    return parser.parse_args()


def main() -> int:
    arguments = parse_args()
    artifact = arguments.artifact.upper()
    if not artifact.startswith("A") or not artifact[1:].isdigit():
        raise AssertionError("artifact must have the form A<number>")
    predecessor_path = ROOT / arguments.predecessor
    predecessor = load(predecessor_path)
    a134 = load(A134)
    index = arguments.distinguished_index

    if predecessor["clearance_ranked_queues"]["y"] or predecessor["clearance_ranked_queues"]["z"]:
        raise AssertionError("both fresh ranked queues must close before partial-row promotion")
    partial = predecessor["partial_interval_diagnostics"]
    if len(partial) != 1 or int(partial[0]["distinguished_index"]) != index:
        raise AssertionError("requested row is not the sole frozen partial diagnostic")
    if partial[0]["main_interval_closed"] or partial[0]["full_interval_closed"]:
        raise AssertionError("predecessor no longer records the expected partial state")

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
    if source["root_id"] != partial[0]["root_id"] or source["line_chart"] != partial[0]["line_chart"]:
        raise AssertionError("partial diagnostic and selected source disagree")
    if not full["scope"]["single_full_E32_thimble_interval_closed"]:
        raise AssertionError("partial row full interval is not closed")
    if not full["A134_radius_ledger"]["fallback_met"]:
        raise AssertionError("partial row misses the A134 per-unit fallback")
    if not full["full_E32_thimble"]["floating_candidate_contained"]:
        raise AssertionError("independent A131 center is outside the partial-row interval")

    manifest = a134["selected_E32_decomposition"]["primitive_thimble_chain"]
    coefficient_by_index = {
        int(item["distinguished_index"]): int(item["coefficient"])
        for item in manifest
    }
    coefficient = coefficient_by_index[index]
    fallback = float(a134["strict_budget_ledger"]["sufficient_uniform_per_unit_thimble_radius"])
    radius = float(full["full_E32_thimble"]["interval_radius_upper"])
    displacement = float(full["full_E32_thimble"]["floating_candidate_center_difference"])
    cost = abs(coefficient) * (radius + displacement)
    row = {
        "distinguished_index": index,
        "root_id": source["root_id"],
        "line_chart": source["line_chart"],
        "coefficient": coefficient,
        "coefficient_l1": abs(coefficient),
        "tail_regular_segments": len(tail["regular_segments"]),
        "tail_radius_upper": tail["E32_endpoint_tail"]["interval_radius_upper"],
        "main_certificate_method": main_interval["validated_main_transport"]["certificate_method"],
        "main_radius_upper": main_interval["E32_main_segment"]["interval_radius_upper"],
        "full_interval_center": full["full_E32_thimble"]["interval_center"],
        "full_interval_radius_upper": radius,
        "A131_center_difference": displacement,
        "weighted_radius_plus_displacement_cost": cost,
        "fallback_margin": fallback - radius,
        "promoted_from_partial_diagnostic": True,
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
    certified_cost = float(old_ledger["certified_radius_plus_displacement_cost"]) + cost
    remaining_budget = float(old_ledger["remaining_budget"]) - cost
    if (support_closed, l1_closed, remaining_support, remaining_l1) != (71, 123, 0, 0):
        raise AssertionError("partial promotion does not complete the frozen 71/123 manifest")
    if remaining_budget <= 0:
        raise AssertionError("partial promotion exhausts the weighted radius budget")
    if {int(item["distinguished_index"]) for item in closed} != set(coefficient_by_index):
        raise AssertionError("accepted support does not equal the A134 manifest")

    suffix = artifact.lower()
    packet_path = PERIOD_DIRECTORY / f"selected_alignment_E32_clearance_ranked_successor_{artifact}.packet.json"
    frontier_path = PERIOD_DIRECTORY / f"U6_frontier_after_{artifact}.packet.json"
    note_path = ROOT / "proof_corpus" / f"MTT_Selected_q79E32PartialFinalAppend_{artifact}_v1.md"
    slug = f"selected_q79e32partialfinalappend{suffix}"
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
        "schema": "MTTQ79SelectedE32PartialFinalAppend.v1",
        "artifact": artifact,
        "status": "ALL_71_SELECTED_SINGLE_E32_THIMBLE_INTERVALS_CLOSED_WEIGHTED_SUM_PENDING",
        "builder_configuration": {
            "predecessor": relative(predecessor_path),
            "distinguished_index": index,
            "partial_diagnostic_promotion_enforced": True,
            "fresh_queues_required_empty": True,
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
        "partial_interval_diagnostics": [],
        "weighted_budget_ledger": {
            "A134_initial_remaining_budget": old_ledger["A134_initial_remaining_budget"],
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
            "y": [],
            "z": [],
        },
        "scope": {
            "observed_SM_values_used": False,
            "selected_full_interval_count": support_closed,
            "partial_hard_row_promoted": True,
            "all_accepted_intervals_meet_uniform_fallback": all(
                float(item["full_interval_radius_upper"]) < fallback for item in closed
            ),
            "covariant_z_chart_interval_adapter_closed": True,
            "all_71_single_thimble_intervals_closed": True,
            "weighted_71_thimble_interval_closed": False,
            "fixed_carrier_exact_separation_closed": False,
        },
        "next_required_artifact": (
            "sum the 71 certified E32 balls with the exact A134 integer coefficients "
            "and execute the frozen-carrier zero-exclusion decision"
        ),
    }
    dump(packet_path, packet)
    frontier = {
        "schema": "MTTU6PartialFinalAppendFrontier.v1",
        "artifact": artifact,
        "status": packet["status"],
        "newly_closed": f"d{index:03d} coefficient {coefficient:+d} full interval",
        "active_target": packet["next_required_artifact"],
        "selected_support_closed": 71,
        "selected_support_total": 71,
        "selected_l1_closed": 123,
        "selected_l1_total": 123,
        "remaining_weighted_budget": remaining_budget,
        "partial_hard_rows": [],
        "not_closed": [
            "weighted 71-thimble E32 interval",
            "exact frozen-carrier decision",
        ],
    }
    dump(frontier_path, frontier)
    note = f"""# MTT Selected q79 E32 Partial Final Append {artifact} v1

## Result

This append promotes the sole frozen partial row `d{index:03d}/{source['root_id']}`
only after both ranked queues are empty and its main, tail, orientation splice,
fallback, and independent-center containment gates are certified. The selected
E32 support is now exactly 71/71 with coefficient L1 weight 123/123.

```text
full radius = {radius:.16g}
weighted cost including A131 displacement = {cost:.16g}
remaining weighted budget = {remaining_budget:.16g}
```

No weighted-sum or carrier conclusion is claimed here; those require the direct
71-ball interval sum in the next artifact.
"""
    note_path.write_text(note, encoding="utf-8")
    candidate = {
        "schema": "MTTSelectedQ79E32PartialFinalAppend.v1",
        "artifact": artifact,
        "status": packet["status"],
        "packet": relative(packet_path),
        "packet_sha256": sha256(packet_path),
        "frontier": relative(frontier_path),
        "frontier_sha256": sha256(frontier_path),
        "note": relative(note_path),
        "note_sha256": sha256(note_path),
        "observed_SM_values_used": False,
        "accepted_full_interval_count": 71,
        "weighted_interval_closed": False,
        "closure_claimed": False,
    }
    dump(candidate_path, candidate)
    certificate = {
        "schema": "MTTCertificate.v1",
        "certificate": "MTTSelectedQ79E32PartialFinalAppend",
        "artifact": artifact,
        "status": packet["status"],
        "candidate_path": relative(candidate_path),
        "candidate_sha256": sha256(candidate_path),
        "observed_SM_values_used": False,
        "accepted_full_interval_count": 71,
        "weighted_interval_closed": False,
        "closure_claimed": False,
    }
    dump(certificate_path, certificate)
    for path in (packet_path, frontier_path, note_path, candidate_path, certificate_path):
        print(f"wrote {relative(path)}")
    print(
        json.dumps(
            {
                "artifact": artifact,
                "closed_support": 71,
                "closed_l1": 123,
                "remaining_support": 0,
                "remaining_l1": 0,
                "remaining_budget": remaining_budget,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
