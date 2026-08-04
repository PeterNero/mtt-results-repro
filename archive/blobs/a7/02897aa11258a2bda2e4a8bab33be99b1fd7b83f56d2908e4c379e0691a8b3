"""Audit the q79 u1=2, u2=29..100 exact R-only batch."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

from q79_Ronly_u1_002_u2_021_execution_audit import (
    Gate,
    classify,
    exact_log,
)


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
MANIFEST = (
    ROOT
    / "candidate_data"
    / "q79_Ronly_u1_002_remaining_029_100_batch"
    / "input_manifest.json"
)
RESULT = (
    ROOT
    / "candidate_data"
    / "q79_Ronly_u1_002_remaining_029_100_batch"
    / "q79_Ronly_u1_002_remaining_029_100.result.packet.json"
)
CONTRACT = (
    ROOT
    / "proof_corpus"
    / "Q79_Ronly_U1_002_Remaining_029_100_Batch_Execution_Contract_v1.md"
)
BATCH_RUNNER = SCRIPTS / "run_q79_Ronly_u1_002_remaining_029_100_batch_v1.py"
LINE_RUNNER = SCRIPTS / "run_q79_Ronly_u1_002_exact_line_job_v2.py"
EXPECTED_ROWS_SHA256 = (
    "dab8dd378995a01b12c9e72b7d574f9982e356a6f53b0749472c8086f76c4824"
)
EXPECTED_MSOLVE_SHA256 = (
    "a4c2beb9a7d186394af6bb21e235f76e3bfb3d0e6fdf872c27b517b8a6e87e13"
)


def resolve(entry: dict[str, object]) -> Path:
    path = Path(str(entry["path"]))
    return path if path.is_absolute() else ROOT / path


def artifact_matches(entry: dict[str, object]) -> bool:
    path = resolve(entry)
    return bool(
        path.is_file()
        and path.stat().st_size == entry.get("bytes")
        and hashlib.sha256(path.read_bytes()).hexdigest() == entry.get("sha256")
    )


def artifact_matches_at_commit(entry: dict[str, object], commit: str) -> bool:
    if artifact_matches(entry):
        return True
    path_text = str(entry.get("path", "")).replace("\\", "/")
    if not path_text or Path(path_text).is_absolute() or not commit:
        return False
    completed = subprocess.run(
        ["git", "show", f"{commit}:{path_text}"],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    if completed.returncode != 0:
        return False
    candidates = [completed.stdout]
    if b"\r\n" not in completed.stdout:
        candidates.append(completed.stdout.replace(b"\n", b"\r\n"))
    return any(
        len(value) == entry.get("bytes")
        and hashlib.sha256(value).hexdigest() == entry.get("sha256")
        for value in candidates
    )


def show_gates(gates: list[Gate]) -> None:
    width = max(len(gate.label) for gate in gates)
    for gate in gates:
        print(
            f"{gate.label:{width}s}  "
            f"{'PASS' if gate.passed else 'FAIL':4s}  {gate.detail}"
        )


def manifest_checks() -> tuple[list[Gate], dict[str, object]]:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    rows = manifest.get("rows", [])
    expected_keys = [(space, u2) for u2 in range(29, 101) for space in (5, 6)]
    observed_keys = [(int(row["space"]), int(row["u2"])) for row in rows]
    gates = [
        Gate("manifest artifacts exist", all(path.is_file() for path in (MANIFEST, CONTRACT, BATCH_RUNNER, LINE_RUNNER)), "files=4"),
        Gate(
            "manifest schema/status",
            manifest.get("schema") == "MTTQ79RonlyU1002RemainingInputManifest.v1"
            and manifest.get("status") == "EXACT_REMAINING_INPUT_MANIFEST_FROZEN",
            str(manifest.get("status")),
        ),
        Gate(
            "manifest range/order",
            manifest.get("u1") == 2
            and manifest.get("u2_range") == [29, 100]
            and manifest.get("spaces") == [5, 6]
            and observed_keys == expected_keys,
            f"rows={len(rows)}",
        ),
        Gate(
            "manifest input digest",
            manifest.get("input_rows_sha256") == EXPECTED_ROWS_SHA256,
            str(manifest.get("input_rows_sha256")),
        ),
        Gate(
            "all manifest inputs hash-bind",
            all(artifact_matches(row) for row in rows),
            f"rows={len(rows)}",
        ),
        Gate(
            "manifest accounting",
            manifest.get("row_count") == 144
            and manifest.get("total_input_bytes") == 1095915
            and manifest.get("new_continuous_fit_parameters") == 0,
            f"rows={manifest.get('row_count')}; bytes={manifest.get('total_input_bytes')}",
        ),
    ]
    return gates, manifest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--preflight", action="store_true")
    args = parser.parse_args()

    print("q79 u1=2 remaining exact-batch audit")
    print("=======================================")
    gates, manifest = manifest_checks()
    if args.preflight:
        show_gates(gates)
        failed = [gate for gate in gates if not gate.passed]
        if failed:
            raise SystemExit(1)
        print("preflight result               PASS  batch source is ready for immutable commit")
        return 0

    packet = json.loads(RESULT.read_text(encoding="utf-8"))
    config = packet.get("config", {})
    provenance = packet.get("provenance", {})
    rows = packet.get("results", [])
    expected_keys = [(space, u2) for u2 in range(29, 101) for space in (5, 6)]
    observed_keys = [
        (int(row["space_index"]), int(row["u2"]))
        for row in rows
    ]
    classifications = [classify(resolve(row["basis"])) for row in rows]
    exact_logs = [
        exact_log(
            resolve(row["log"]),
            str(row["classification"]),
            int(row["deterministic_seed"]),
        )
        for row in rows
    ]
    artifact_rows = all(
        all(artifact_matches(row[key]) for key in ("family_packet", "input", "basis", "log"))
        for row in rows
    )
    commit = str(provenance.get("git", {}).get("commit", ""))
    commit_exists = bool(commit) and subprocess.run(
        ["git", "cat-file", "-e", f"{commit}^{{commit}}"],
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    ).returncode == 0
    accounting = {
        "requested_lines": 144,
        "exact_R_only_lines": 144,
        "R_only_unit_lines": sum(value == "R_ONLY_UNIT" for value in classifications),
        "R_only_nonunit_lines": sum(value == "R_ONLY_NONUNIT" for value in classifications),
        "completed_u2_values": 72,
        "spaces_per_u2": 2,
    }
    gates.extend(
        [
            Gate(
                "execution packet schema/status",
                packet.get("schema") == "MTTQ79RonlyU1002RemainingExactBatchResult.v1"
                and packet.get("status") == "EXACT_U1_002_REMAINING_R_ONLY_LINES_CLASSIFIED",
                str(packet.get("status")),
            ),
            Gate("requested coordinates", observed_keys == expected_keys, f"rows={len(rows)}"),
            Gate("all emitted artifacts hash-bind", artifact_rows, f"rows={len(rows)}"),
            Gate(
                "basis classifications reproduce",
                all(
                    classification is not None
                    and classification == row.get("classification")
                    for row, classification in zip(rows, classifications)
                ),
                str(accounting),
            ),
            Gate(
                "per-line seeds and exact logs",
                all(
                    row.get("deterministic_seed") == 790000 + int(row["u2"])
                    for row in rows
                )
                and all(exact_logs),
                "seed=790000+u2",
            ),
            Gate(
                "selected msolve binary",
                provenance.get("solver", {}).get("sha256") == EXPECTED_MSOLVE_SHA256,
                str(provenance.get("solver", {}).get("sha256")),
            ),
            Gate(
                "batch source hash-binds",
                all(
                    artifact_matches_at_commit(provenance[key], commit)
                    for key in ("batch_runner", "line_runner")
                )
                and all(
                    artifact_matches_at_commit(entry, commit)
                    for entry in provenance.get("authority_inputs", {}).values()
                ),
                commit,
            ),
            Gate(
                "clean recorded Git commit",
                commit_exists
                and provenance.get("git", {}).get("status_before_execution") == [],
                commit,
            ),
            Gate(
                "manifest is the selected source",
                config.get("input_rows_sha256") == EXPECTED_ROWS_SHA256
                and config.get("input_manifest_sha256")
                == provenance.get("authority_inputs", {}).get("input_manifest", {}).get("sha256"),
                str(config.get("input_rows_sha256")),
            ),
            Gate("accounting is exact", packet.get("accounting") == accounting, str(accounting)),
            Gate(
                "all declared checks pass",
                bool(packet.get("checks"))
                and all(packet["checks"].values()),
                f"{sum(packet.get('checks', {}).values())}/{len(packet.get('checks', {}))}",
            ),
            Gate(
                "zero fit parameters",
                packet.get("new_continuous_fit_parameters") == 0
                and manifest.get("new_continuous_fit_parameters") == 0,
                "zero",
            ),
            Gate(
                "claim boundary retained",
                "does not promote the contiguous prefix" in packet.get("claim_boundary", "")
                and "nonunit result still requires" in packet.get("claim_boundary", ""),
                packet.get("claim_boundary", ""),
            ),
        ]
    )
    show_gates(gates)
    if any(not gate.passed for gate in gates):
        raise SystemExit(1)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
