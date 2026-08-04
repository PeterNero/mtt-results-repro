from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SCHEDULE = ROOT / "q79_eta9_targeted_original_jacobian_macaulay_schedule.packet.json"
SUPPORT = ROOT / "q79_eta9_pole_six_groebner_support_union.packet.json"
CHUNK_DIR = ROOT / "eta9_targeted_original_jacobian_transform_chunks"
GROUP_DIR = ROOT / "eta9_targeted_original_jacobian_macaulay_groups"
FIRST_PACKET = CHUNK_DIR / "columns_0000_0000.packet.json"
FIRST_IDENTITY = CHUNK_DIR / "columns_0000_0000.identity.packet.json"
FIRST_TRANSFORM = CHUNK_DIR / "columns_0000_0000.transform.ssi"
OUT = ROOT / "q79_eta9_targeted_original_jacobian_transform_coverage.packet.json"


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while block := handle.read(1024 * 1024):
            digest.update(block)
    return digest.hexdigest()


def record(path: Path) -> dict[str, object]:
    return {"path": str(path), "sha256": sha256(path), "bytes": path.stat().st_size}


def read_packet(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def all_checks(packet: dict[str, object]) -> bool:
    checks = packet.get("checks")
    return isinstance(checks, dict) and bool(checks) and all(checks.values())


def records_are_hash_bound(value: object) -> bool:
    if isinstance(value, dict):
        if "path" in value and "sha256" in value:
            path = Path(str(value["path"]))
            if not path.is_absolute():
                path = ROOT / path
            if not path.is_file() or sha256(path) != value["sha256"]:
                return False
        return all(records_are_hash_bound(child) for child in value.values())
    if isinstance(value, list):
        return all(records_are_hash_bound(child) for child in value)
    return True


def merge_intervals(columns: list[bool], value: bool) -> list[list[int]]:
    intervals: list[list[int]] = []
    start: int | None = None
    for index, state in enumerate(columns + [not value]):
        if state == value and start is None:
            start = index
        elif state != value and start is not None:
            intervals.append([start, index])
            start = None
    return intervals


def discover_coverage() -> dict[str, object]:
    schedule = read_packet(SCHEDULE)
    support = read_packet(SUPPORT)
    require(all_checks(schedule), "schedule checks")
    require(all_checks(support), "support checks")
    require(records_are_hash_bound(schedule), "schedule provenance")
    require(records_are_hash_bound(support), "support provenance")
    require(
        schedule["inputs"]["support_union"]["sha256"] == sha256(SUPPORT),
        "schedule support hash",
    )
    support_indices = [int(value) for value in support["support_union_indices_one_based"]]
    require(len(support_indices) == 225, "support width")
    groups = {
        int(group["group_index"]): group
        for group in schedule["groups_in_selected_order"]
    }
    require(sorted(groups) == list(range(30)), "schedule group indices")

    covered = [False] * len(support_indices)
    entries: list[dict[str, object]] = []
    input_records: dict[str, object] = {
        "schedule": record(SCHEDULE),
        "support_union": record(SUPPORT),
    }

    first = read_packet(FIRST_PACKET)
    first_identity = read_packet(FIRST_IDENTITY)
    first_schedule = groups[0]
    first_interval = [
        int(first_schedule["selected_column_start"]),
        int(first_schedule["selected_column_stop"]),
    ]
    require(first_interval == [0, 1], "first schedule interval")
    require(all_checks(first) and all_checks(first_identity), "first packet checks")
    require(records_are_hash_bound(first), "first packet provenance")
    require(records_are_hash_bound(first_identity), "first identity provenance")
    require([first["column_start"], first["column_stop"]] == first_interval, "first interval")
    require(
        [first_identity["column_start"], first_identity["column_stop"]] == first_interval,
        "first identity interval",
    )
    require(first["support_indices_one_based"] == support_indices[:1], "first support")
    require(first_identity["support_indices_one_based"] == support_indices[:1], "first identity support")
    require(first["transform"]["shape"] == [10, 1], "first transform shape")
    require(first_identity["identity"]["shape"] == [10, 1], "first identity shape")
    require(first_identity["identity"]["residual_nonzero_columns"] == 0, "first residual")
    require(first["transform"]["cache"]["sha256"] == sha256(FIRST_TRANSFORM), "first transform hash")
    require(first_identity["inputs"]["chunk_packet"]["sha256"] == sha256(FIRST_PACKET), "first packet hash chain")
    require(first_identity["inputs"]["transform"]["sha256"] == sha256(FIRST_TRANSFORM), "first transform hash chain")
    covered[0] = True
    input_records["group00_division_packet"] = record(FIRST_PACKET)
    input_records["group00_identity_packet"] = record(FIRST_IDENTITY)
    input_records["group00_transform"] = record(FIRST_TRANSFORM)
    entries.append(
        {
            "group_index": 0,
            "method": "exact bounded division plus independent polynomial replay",
            "Cox_degree": first_schedule["Cox_degree"],
            "column_interval": first_interval,
            "column_count": 1,
            "support_indices_one_based": support_indices[:1],
            "transform": record(FIRST_TRANSFORM),
            "source_packet": record(FIRST_PACKET),
            "identity_packet": record(FIRST_IDENTITY),
            "residual_nonzero_columns": 0,
        }
    )

    incomplete_groups: list[dict[str, object]] = []
    for group_index in range(1, 30):
        transform_packet_path = GROUP_DIR / f"group_{group_index:02d}.transform.packet.json"
        identity_packet_path = GROUP_DIR / f"group_{group_index:02d}.transform.verify.packet.json"
        transform_path = GROUP_DIR / f"group_{group_index:02d}.transform.ssi"
        present = [path.is_file() for path in (transform_packet_path, identity_packet_path, transform_path)]
        if not any(present):
            continue
        if not all(present):
            incomplete_groups.append(
                {
                    "group_index": group_index,
                    "present_files": [
                        path.name
                        for path, exists in zip(
                            (transform_packet_path, identity_packet_path, transform_path), present
                        )
                        if exists
                    ],
                    "reason": "not admitted because all three final certificate files are required",
                }
            )
            continue

        transform_packet = read_packet(transform_packet_path)
        identity_packet = read_packet(identity_packet_path)
        group = groups[group_index]
        start = int(group["selected_column_start"])
        stop = int(group["selected_column_stop"])
        interval = [start, stop]
        width = stop - start
        expected_support = support_indices[start:stop]
        require(all_checks(transform_packet), f"group {group_index} transform checks")
        require(all_checks(identity_packet), f"group {group_index} identity checks")
        require(records_are_hash_bound(transform_packet), f"group {group_index} transform provenance")
        require(records_are_hash_bound(identity_packet), f"group {group_index} identity provenance")
        require(transform_packet["group_index"] == group_index, f"group {group_index} transform index")
        require(identity_packet["group_index"] == group_index, f"group {group_index} identity index")
        require(transform_packet["Cox_degree"] == group["Cox_degree"], f"group {group_index} transform degree")
        require(identity_packet["Cox_degree"] == group["Cox_degree"], f"group {group_index} identity degree")
        require(transform_packet["selected_column_interval"] == interval, f"group {group_index} transform interval")
        require(identity_packet["selected_column_interval"] == interval, f"group {group_index} identity interval")
        require(
            transform_packet["selected_Groebner_indices_one_based"] == expected_support,
            f"group {group_index} support",
        )
        require(transform_packet["polynomial_transform"]["shape"] == [10, width], f"group {group_index} transform shape")
        require(identity_packet["identity"]["shape"] == [10, width], f"group {group_index} identity shape")
        require(identity_packet["identity"]["residual_nonzero_columns"] == 0, f"group {group_index} residual")
        require(transform_packet["polynomial_transform"]["sha256"] == sha256(transform_path), f"group {group_index} transform hash")
        require(
            identity_packet["inputs"]["transform_packet"]["sha256"] == sha256(transform_packet_path),
            f"group {group_index} packet hash chain",
        )
        require(
            identity_packet["inputs"]["polynomial_transform"]["sha256"] == sha256(transform_path),
            f"group {group_index} transform hash chain",
        )
        require(not any(covered[start:stop]), f"group {group_index} overlap")
        covered[start:stop] = [True] * width
        key = f"group{group_index:02d}"
        input_records[f"{key}_transform_packet"] = record(transform_packet_path)
        input_records[f"{key}_identity_packet"] = record(identity_packet_path)
        input_records[f"{key}_transform"] = record(transform_path)
        entries.append(
            {
                "group_index": group_index,
                "method": "exact Cox-degree Macaulay solve plus independent polynomial replay",
                "Cox_degree": group["Cox_degree"],
                "column_interval": interval,
                "column_count": width,
                "support_indices_one_based": expected_support,
                "transform": record(transform_path),
                "source_packet": record(transform_packet_path),
                "identity_packet": record(identity_packet_path),
                "residual_nonzero_columns": 0,
            }
        )

    certified_groups = [int(entry["group_index"]) for entry in entries]
    remaining_groups = [index for index in range(30) if index not in certified_groups]
    covered_count = sum(covered)
    covered_indices = [index for index, state in enumerate(covered) if state]
    missing_indices = [index for index, state in enumerate(covered) if not state]
    checks = {
        "the_frozen_schedule_and_support_union_are_hash_bound": True,
        "every_admitted_source_and_identity_packet_has_all_checks_true": True,
        "every_admitted_interval_matches_its_frozen_Cox_group": True,
        "every_admitted_support_slice_matches_the_frozen225_order": True,
        "every_admitted_transform_is_hash_bound_through_its_identity_packet": True,
        "every_admitted_independent_polynomial_replay_has_zero_residual_columns": True,
        "the_certified_intervals_are_pairwise_disjoint": True,
        "the_certified_and_missing_columns_partition_all225_columns": covered_count + len(missing_indices) == 225,
        "no_incomplete_or_uncovered_group_is_counted_as_certified": True,
    }
    require(all(checks.values()), "coverage checks")
    return {
        "schema": "MTTQ79Eta9TargetedOriginalJacobianTransformCoverage.v1",
        "date": "2026-07-22",
        "status": "EXACT_GF11_INDEPENDENTLY_REPLAYED_TRANSFORM_COVERAGE",
        "controlling_blocker": "B.ETA9.01",
        "inputs": input_records,
        "coverage": {
            "total_columns": 225,
            "certified_columns": covered_count,
            "remaining_columns": len(missing_indices),
            "certified_group_indices": certified_groups,
            "remaining_group_indices": remaining_groups,
            "certified_column_indices_zero_based": covered_indices,
            "remaining_column_indices_zero_based": missing_indices,
            "certified_intervals_half_open": merge_intervals(covered, True),
            "remaining_intervals_half_open": merge_intervals(covered, False),
            "incomplete_groups_not_admitted": incomplete_groups,
        },
        "certificates": entries,
        "checks": checks,
        "theorem": {
            "name": "q79 eta9 Independently Replayed Transform Coverage Theorem",
            "statement": (
                "Exactly the listed frozen support columns, and no others, have explicit "
                "ten-generator polynomial transforms whose original-Jacobian identities "
                "have been replayed independently over GF(11)."
            ),
            "tier": "exact finite-field certificate aggregation",
        },
        "guardrails": [
            "Coverage is not promoted from intermediate solver files or process success.",
            "The complete transform remains open until certified_columns equals 225.",
            "No downstream divergence, connection, monodromy, cycle or period is inferred.",
        ],
        "next_required_object": (
            "Execute and independently replay the remaining Cox groups, then assemble and "
            "freshly verify the complete 10 by 225 polynomial transform."
        ),
    }


def main() -> None:
    packet = discover_coverage()
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    coverage = packet["coverage"]
    print(f"wrote {OUT}")
    print(f"certified_columns={coverage['certified_columns']}")
    print(f"remaining_columns={coverage['remaining_columns']}")
    print("Q79_ETA9_TARGETED_ORIGINAL_JACOBIAN_TRANSFORM_COVERAGE_PASS")


if __name__ == "__main__":
    main()
