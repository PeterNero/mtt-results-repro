from __future__ import annotations

import hashlib
import json
from pathlib import Path

import build_q79_eta9_targeted_original_jacobian_transform_coverage as coverage_builder


ROOT = Path(__file__).resolve().parent
SCHEDULE = ROOT / "q79_eta9_targeted_original_jacobian_macaulay_schedule.packet.json"
COVERAGE = ROOT / "q79_eta9_targeted_original_jacobian_transform_coverage.packet.json"
GROUP_DIR = ROOT / "eta9_targeted_original_jacobian_macaulay_groups"
OUT = ROOT / "q79_eta9_targeted_original_jacobian_macaulay_campaign_status.packet.json"


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


def discover_status() -> dict[str, object]:
    schedule = read_packet(SCHEDULE)
    coverage = read_packet(COVERAGE)
    require(all_checks(schedule), "schedule checks")
    require(all_checks(coverage), "coverage checks")
    require(coverage_builder.records_are_hash_bound(schedule), "schedule provenance")
    require(coverage_builder.records_are_hash_bound(coverage), "coverage provenance")
    groups = {
        int(group["group_index"]): group
        for group in schedule["groups_in_selected_order"]
    }
    order = [int(value) for value in schedule["recommended_execution_group_indices"]]
    require(sorted(groups) == list(range(30)), "schedule groups")
    require(sorted(order) == list(range(30)), "execution order")
    completed = {int(value) for value in coverage["coverage"]["certified_group_indices"]}

    group_status: list[dict[str, object]] = []
    prepared: set[int] = set()
    input_records: dict[str, object] = {
        "schedule": record(SCHEDULE),
        "transform_coverage": record(COVERAGE),
    }
    for group_index in range(30):
        group = groups[group_index]
        base = {
            "group_index": group_index,
            "Cox_degree": group["Cox_degree"],
            "column_interval": [
                group["selected_column_start"],
                group["selected_column_stop"],
            ],
            "target_count": group["selected_generator_count"],
            "matrix_shape": [
                group["ambient_monomials"],
                group["original_Jacobian_Macaulay_columns"],
            ],
            "matrix_nonzeros": group["original_Jacobian_Macaulay_nonzeros"],
        }
        if group_index == 0:
            require(group_index in completed, "group zero completion")
            group_status.append({**base, "state": "completed_by_exact_division"})
            continue

        group_packet_path = GROUP_DIR / f"group_{group_index:02d}.packet.json"
        csc_packet_path = GROUP_DIR / f"group_{group_index:02d}.csc.packet.json"
        files_present = group_packet_path.is_file() and csc_packet_path.is_file()
        if files_present:
            group_packet = read_packet(group_packet_path)
            csc_packet = read_packet(csc_packet_path)
            require(all_checks(group_packet), f"group {group_index} input checks")
            require(all_checks(csc_packet), f"group {group_index} csc checks")
            require(coverage_builder.records_are_hash_bound(group_packet), f"group {group_index} input provenance")
            require(coverage_builder.records_are_hash_bound(csc_packet), f"group {group_index} csc provenance")
            require(group_packet["group_index"] == group_index, f"group {group_index} packet index")
            require(csc_packet["group_index"] == group_index, f"group {group_index} csc index")
            require(group_packet["Cox_degree"] == group["Cox_degree"], f"group {group_index} packet degree")
            require(csc_packet["Cox_degree"] == group["Cox_degree"], f"group {group_index} csc degree")
            require(
                csc_packet["inputs"]["group_packet"]["sha256"] == sha256(group_packet_path),
                f"group {group_index} packet hash chain",
            )
            require(csc_packet["binary"]["shape"] == base["matrix_shape"], f"group {group_index} csc shape")
            require(
                csc_packet["binary"]["nonzero_entries"] == base["matrix_nonzeros"],
                f"group {group_index} csc nonzeros",
            )
            prepared.add(group_index)
            input_records[f"group{group_index:02d}_packet"] = record(group_packet_path)
            input_records[f"group{group_index:02d}_csc_packet"] = record(csc_packet_path)

        if group_index in completed:
            require(files_present, f"completed group {group_index} prepared input")
            state = "completed_and_independently_replayed"
        elif files_present:
            state = "prepared_verified_input_not_yet_completed"
        else:
            state = "input_not_yet_built"
        group_status.append({**base, "state": state})

    prepared_not_completed = [index for index in order if index in prepared - completed]
    unprepared = [index for index in order if index not in prepared and index not in completed]
    checks = {
        "the_frozen_schedule_and_current_transform_coverage_are_hash_bound": True,
        "every_prepared_group_has_passing_group_and_CSC_packets": True,
        "every_prepared_CSC_binary_matches_the_frozen_shape_and_nonzero_count": True,
        "every_completed_group_is_backed_by_the_transform_coverage_theorem": True,
        "prepared_but_uncompleted_groups_are_not_counted_as_transform_coverage": True,
        "all30_groups_are_classified_exactly_once": len(group_status) == 30,
    }
    require(all(checks.values()), "campaign checks")
    return {
        "schema": "MTTQ79Eta9TargetedOriginalJacobianMacaulayCampaignStatus.v1",
        "date": "2026-07-22",
        "status": "OPERATIONAL_EXACT_COX_CAMPAIGN_READINESS_SNAPSHOT",
        "controlling_blocker": "B.ETA9.01",
        "inputs": input_records,
        "summary": {
            "total_groups": 30,
            "completed_groups_in_recommended_order": [index for index in order if index in completed],
            "completed_columns": coverage["coverage"]["certified_columns"],
            "prepared_not_completed_groups_in_recommended_order": prepared_not_completed,
            "unprepared_groups_in_recommended_order": unprepared,
            "next_prepared_group": prepared_not_completed[0] if prepared_not_completed else None,
        },
        "groups_in_selected_order": group_status,
        "checks": checks,
        "guardrails": [
            "Prepared means verified solver input only; it is not a transform theorem.",
            "Completed status is inherited only from the independent transform-coverage packet.",
            "Central calculation job state is dynamic and intentionally excluded from this file.",
        ],
        "next_required_object": (
            "Execute the prepared groups in recommended order, independently replay each "
            "polynomial identity, and refresh both coverage and this readiness snapshot."
        ),
    }


def main() -> None:
    packet = discover_status()
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    summary = packet["summary"]
    print(f"wrote {OUT}")
    print(f"completed_columns={summary['completed_columns']}")
    print(
        "prepared_not_completed="
        + ",".join(str(value) for value in summary["prepared_not_completed_groups_in_recommended_order"])
    )
    print("Q79_ETA9_TARGETED_ORIGINAL_JACOBIAN_MACAULAY_CAMPAIGN_STATUS_PASS")


if __name__ == "__main__":
    main()
