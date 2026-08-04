#!/usr/bin/env python3
"""Classify all remaining q79 u1=2 R-only lines in one resumable batch."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path

from run_q79_Ronly_u1_002_exact_line_job_v2 import (
    ROOT,
    artifact,
    atomic_json,
    classify_basis,
    git_provenance,
    load_family,
    require,
    run_line,
    sha256,
    solver_provenance,
    validate_log,
)


DEFAULT_START = 29
DEFAULT_END = 100
DEFAULT_SPACES = (5, 6)
DEFAULT_SEED_BASE = 790000
DEFAULT_CHECKPOINT = (
    ROOT / "runtime" / "q79_Ronly_u1_002_remaining_029_100.checkpoint.json"
)
DEFAULT_RESULT = (
    ROOT
    / "candidate_data"
    / "q79_Ronly_u1_002_remaining_029_100_batch"
    / "q79_Ronly_u1_002_remaining_029_100.result.packet.json"
)
DEFAULT_MANIFEST = (
    ROOT
    / "candidate_data"
    / "q79_Ronly_u1_002_remaining_029_100_batch"
    / "input_manifest.json"
)
CONTROLLING_CERTIFICATE = (
    ROOT / "certificates" / "Q79_Ronly_U1_002_Contiguous_CrossSpace_Prefix_v1.json"
)
EXECUTION_CONTRACT = (
    ROOT
    / "proof_corpus"
    / "Q79_Ronly_U1_002_Remaining_029_100_Batch_Execution_Contract_v1.md"
)
LINE_RUNNER = ROOT / "scripts" / "run_q79_Ronly_u1_002_exact_line_job_v2.py"
SELECTED_MSOLVE_SHA256 = (
    "a4c2beb9a7d186394af6bb21e235f76e3bfb3d0e6fdf872c27b517b8a6e87e13"
)


def parse_spaces(text: str) -> list[int]:
    spaces = [int(value) for value in text.split(",") if value]
    require(
        spaces
        and len(spaces) == len(set(spaces))
        and set(spaces) <= set(DEFAULT_SPACES),
        "spaces",
    )
    return spaces


def input_rows(u2_start: int, u2_end: int, spaces: list[int]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for u2 in range(u2_start, u2_end + 1):
        for space in spaces:
            _packet_path, _record, input_entry = load_family(space, u2)
            rows.append(
                {
                    "space": space,
                    "u2": u2,
                    "bytes": input_entry["bytes"],
                    "sha256": input_entry["sha256"],
                    "path": input_entry["path"],
                }
            )
    return rows


def input_rows_sha256(rows: list[dict[str, object]]) -> str:
    payload = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def build_manifest(
    u2_start: int = DEFAULT_START,
    u2_end: int = DEFAULT_END,
    spaces: list[int] | None = None,
) -> dict[str, object]:
    selected_spaces = list(DEFAULT_SPACES) if spaces is None else spaces
    rows = input_rows(u2_start, u2_end, selected_spaces)
    families = {}
    for space in selected_spaces:
        packet_path, _record, _input_entry = load_family(space, u2_start)
        families[str(space)] = artifact(packet_path)
    return {
        "schema": "MTTQ79RonlyU1002RemainingInputManifest.v1",
        "status": "EXACT_REMAINING_INPUT_MANIFEST_FROZEN",
        "field": "F_101",
        "u1": 2,
        "u2_range": [u2_start, u2_end],
        "spaces": selected_spaces,
        "ordering": "u2_ascending_then_space_ascending",
        "row_count": len(rows),
        "total_input_bytes": sum(int(row["bytes"]) for row in rows),
        "input_rows_sha256": input_rows_sha256(rows),
        "family_packets": families,
        "rows": rows,
        "checks": {
            "every_requested_input_exists_and_hashes": True,
            "all_rows_are_over_F101_with_fixed_u1_002": True,
            "ordering_is_contiguous_and_duplicate_free": True,
            "no_solver_output_is_used_as_manifest_input": True,
        },
        "new_continuous_fit_parameters": 0,
    }


def resolve_artifact(entry: dict[str, object]) -> Path:
    path = Path(str(entry["path"]))
    return path if path.is_absolute() else ROOT / path


def artifact_matches(entry: dict[str, object]) -> bool:
    path = resolve_artifact(entry)
    return (
        path.is_file()
        and path.stat().st_size == int(entry["bytes"])
        and sha256(path) == entry["sha256"]
    )


def validate_completed_row(row: dict[str, object], seed_base: int) -> None:
    space = int(row["space_index"])
    u2 = int(row["u2"])
    require(space in DEFAULT_SPACES and DEFAULT_START <= u2 <= DEFAULT_END, "row coordinates")
    seed = seed_base + u2
    require(row.get("u1") == 2 and row.get("deterministic_seed") == seed, "row seed")
    require(
        all(
            artifact_matches(row[key])
            for key in ("family_packet", "input", "basis", "log")
        ),
        "row artifacts",
    )
    classification = classify_basis(resolve_artifact(row["basis"]))
    require(classification == row.get("classification"), "row classification")
    validate_log(resolve_artifact(row["log"]), str(classification), seed)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--u2-start", type=int, default=DEFAULT_START)
    parser.add_argument("--u2-end", type=int, default=DEFAULT_END)
    parser.add_argument("--spaces", default="5,6")
    parser.add_argument("--checkpoint", type=Path, default=DEFAULT_CHECKPOINT)
    parser.add_argument("--result", type=Path, default=DEFAULT_RESULT)
    parser.add_argument("--input-manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument(
        "--controlling-certificate", type=Path, default=CONTROLLING_CERTIFICATE
    )
    parser.add_argument("--execution-contract", type=Path, default=EXECUTION_CONTRACT)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--write-manifest-only", action="store_true")
    parser.add_argument("--preflight-only", action="store_true")
    parser.add_argument("--wsl-distribution", default="Ubuntu")
    parser.add_argument("--msolve", default="/home/nerodes/.local/opt/msolve-0.10.1/msolve")
    parser.add_argument("--timeout-seconds", type=int, default=7200)
    parser.add_argument("--memory-mib", type=int, default=12288)
    parser.add_argument("--seed-base", type=int, default=DEFAULT_SEED_BASE)
    args = parser.parse_args()

    spaces = parse_spaces(args.spaces)
    require(
        1 <= args.u2_start <= args.u2_end < 101,
        "nonzero contiguous u2 range",
    )
    require(
        args.timeout_seconds > 0 and args.memory_mib >= 512 and args.seed_base >= 0,
        "resource and seed bounds",
    )

    expected_manifest = build_manifest(args.u2_start, args.u2_end, spaces)
    if args.write_manifest_only:
        atomic_json(args.input_manifest, expected_manifest)
        print("EXACT_REMAINING_INPUT_MANIFEST_WRITTEN", flush=True)
        print(args.input_manifest, flush=True)
        return 0

    require(args.input_manifest.is_file(), "committed input manifest")
    manifest = json.loads(args.input_manifest.read_text(encoding="utf-8"))
    require(manifest == expected_manifest, "input manifest reproduces")

    checkpoint_exists = args.checkpoint.is_file()
    if checkpoint_exists:
        require(args.resume, "existing checkpoint requires --resume")
    else:
        require(not args.resume, "--resume requires an existing checkpoint")

    runner = Path(__file__).resolve()
    live_provenance = {
        "git": git_provenance(),
        "batch_runner": artifact(runner),
        "line_runner": artifact(LINE_RUNNER),
        "authority_inputs": {
            "controlling_certificate": artifact(args.controlling_certificate.resolve()),
            "execution_contract": artifact(args.execution_contract.resolve()),
            "input_manifest": artifact(args.input_manifest.resolve()),
        },
        "python": {
            "version": sys.version,
            "executable": sys.executable,
            "platform": platform.platform(),
        },
        "solver": solver_provenance(args.wsl_distribution, args.msolve),
    }
    require(
        live_provenance["solver"]["sha256"] == SELECTED_MSOLVE_SHA256,
        "selected msolve binary",
    )
    if checkpoint_exists:
        checkpoint = json.loads(args.checkpoint.read_text(encoding="utf-8"))
        provenance = checkpoint.get("provenance", {})
        require(bool(provenance), "checkpoint provenance")
        require(
            live_provenance["git"]["commit"] == provenance["git"]["commit"],
            "resume Git commit",
        )
        require(
            live_provenance["batch_runner"] == provenance["batch_runner"]
            and live_provenance["line_runner"] == provenance["line_runner"]
            and live_provenance["authority_inputs"] == provenance["authority_inputs"]
            and live_provenance["python"] == provenance["python"]
            and live_provenance["solver"] == provenance["solver"],
            "resume immutable source and solver provenance",
        )
    else:
        require(
            live_provenance["git"]["status_before_execution"] == [],
            "batch must start from a clean Git worktree",
        )
        provenance = live_provenance

    config = {
        "u1": 2,
        "u2_start": args.u2_start,
        "u2_end": args.u2_end,
        "spaces": spaces,
        "field": "F_101",
        "ordering": "u2_ascending_then_space_ascending",
        "wsl_distribution": args.wsl_distribution,
        "msolve": args.msolve,
        "timeout_seconds_per_line": args.timeout_seconds,
        "memory_mib_per_line": args.memory_mib,
        "deterministic_seed_rule": f"{args.seed_base}+u2",
        "seed_base": args.seed_base,
        "input_manifest_sha256": provenance["authority_inputs"]["input_manifest"]["sha256"],
        "input_rows_sha256": manifest["input_rows_sha256"],
        "batch_runner_sha256": provenance["batch_runner"]["sha256"],
        "line_runner_sha256": provenance["line_runner"]["sha256"],
        "solver_sha256": provenance["solver"]["sha256"],
        "controlling_certificate_sha256": provenance["authority_inputs"][
            "controlling_certificate"
        ]["sha256"],
        "execution_contract_sha256": provenance["authority_inputs"][
            "execution_contract"
        ]["sha256"],
    }
    config_fingerprint = hashlib.sha256(
        json.dumps(config, sort_keys=True).encode("utf-8")
    ).hexdigest()
    if args.preflight_only:
        require(not args.resume and not checkpoint_exists, "fresh preflight")
        print("EXACT_REMAINING_BATCH_PREFLIGHT_PASS", flush=True)
        print(f"commit={provenance['git']['commit']}", flush=True)
        print(f"inputs={manifest['row_count']}", flush=True)
        print(f"input_rows_sha256={manifest['input_rows_sha256']}", flush=True)
        print(f"solver_sha256={provenance['solver']['sha256']}", flush=True)
        return 0

    if checkpoint_exists:
        require(checkpoint.get("config_fingerprint") == config_fingerprint, "checkpoint config")
        results = list(checkpoint.get("completed_lines", []))
    else:
        results: list[dict[str, object]] = []
        checkpoint = {
            "schema": "MTTQ79RonlyU1002RemainingBatchCheckpoint.v1",
            "state": "running",
            "started_at_utc": datetime.now(timezone.utc).isoformat(),
            "config": config,
            "config_fingerprint": config_fingerprint,
            "provenance": provenance,
            "completed_lines": results,
        }
        atomic_json(args.checkpoint, checkpoint)

    expected_keys = [
        (space, u2)
        for u2 in range(args.u2_start, args.u2_end + 1)
        for space in spaces
    ]
    for row in results:
        validate_completed_row(row, args.seed_base)
    observed_keys = [
        (int(row["space_index"]), int(row["u2"]))
        for row in results
    ]
    require(
        observed_keys == expected_keys[: len(observed_keys)],
        "checkpoint is a contiguous batch prefix",
    )
    completed_keys = set(observed_keys)

    for space, u2 in expected_keys:
        if (space, u2) in completed_keys:
            print(f"CHECKPOINT space={space} u1=2 u2={u2} already complete", flush=True)
            continue
        seed = args.seed_base + u2
        row = run_line(
            space=space,
            u2=u2,
            distribution=args.wsl_distribution,
            solver=args.msolve,
            timeout_seconds=args.timeout_seconds,
            memory_mib=args.memory_mib,
            seed=seed,
            checkpoint_dir=args.checkpoint.parent,
        )
        row["deterministic_seed"] = seed
        validate_completed_row(row, args.seed_base)
        results.append(row)
        completed_keys.add((space, u2))
        checkpoint["completed_lines"] = results
        checkpoint["last_completed"] = {"space": space, "u2": u2}
        checkpoint["updated_at_utc"] = datetime.now(timezone.utc).isoformat()
        atomic_json(args.checkpoint, checkpoint)
        print(
            f"BATCH_PROGRESS completed={len(results)}/{len(expected_keys)} "
            f"last=space{space},u2={u2}",
            flush=True,
        )

    require(
        [
            (int(row["space_index"]), int(row["u2"]))
            for row in results
        ]
        == expected_keys,
        "all requested lines complete",
    )
    accounting = {
        "requested_lines": len(expected_keys),
        "exact_R_only_lines": len(results),
        "R_only_unit_lines": sum(
            row["classification"] == "R_ONLY_UNIT" for row in results
        ),
        "R_only_nonunit_lines": sum(
            row["classification"] == "R_ONLY_NONUNIT" for row in results
        ),
        "completed_u2_values": args.u2_end - args.u2_start + 1,
        "spaces_per_u2": len(spaces),
    }
    checks = {
        "checkpoint_completed_all_requested_lines": True,
        "checkpoint_order_is_u2_then_space_and_contiguous": True,
        "every_manifest_input_hash_reproduces": True,
        "every_output_is_a_complete_exact_reduced_Groebner_basis": True,
        "every_log_records_F101_DRL_one_thread_exact_sparse_linear_algebra": True,
        "each_line_uses_the_declared_deterministic_seed_rule": True,
        "selected_msolve_version_and_binary_hash_are_recorded": True,
        "clean_git_commit_runner_hash_python_environment_and_libraries_are_recorded": True,
        "partial_outputs_were_not_accepted": True,
        "nonunit_R_only_lines_are_not_promoted_to_full_R_y_D_closure": True,
        "no_continuous_fit_parameter_is_added": True,
    }
    result = {
        "schema": "MTTQ79RonlyU1002RemainingExactBatchResult.v1",
        "date": datetime.now(timezone.utc).date().isoformat(),
        "completed_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "EXACT_U1_002_REMAINING_R_ONLY_LINES_CLASSIFIED",
        "config": config,
        "config_fingerprint": config_fingerprint,
        "provenance": provenance,
        "results": results,
        "accounting": accounting,
        "checks": checks,
        "exit_certificate": (
            "All requested u1=2, u2=29..100 R-only symbolic lines in spaces 5 and 6 "
            "have complete exact reduced Groebner bases with hash-bound inputs, outputs, "
            "logs, code, solver, Git, and environment provenance."
        ),
        "claim_boundary": (
            "This batch classifies R-only lines. A nonunit result still requires an "
            "independent selected finite-quotient R/y/D unit certificate. Process success "
            "does not promote the contiguous prefix, characteristic zero, the physical "
            "q79 branch, HYM, quantum gravity, or any Standard Model claim."
        ),
        "new_continuous_fit_parameters": 0,
    }
    atomic_json(args.result, result)
    checkpoint["state"] = "complete"
    checkpoint["completed_at_utc"] = result["completed_at_utc"]
    checkpoint["result"] = artifact(args.result)
    atomic_json(args.checkpoint, checkpoint)
    print(result["status"], flush=True)
    print(args.result, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
