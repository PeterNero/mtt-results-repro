#!/usr/bin/env python3
"""Run one crash-resumable q79 u1=2 exact symbolic-line job through WSL."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import re
import shlex
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path, PureWindowsPath


ROOT = Path(__file__).resolve().parents[1]
PRIME = 101
VARIABLES = (
    "h1", "h2", "h3", "h4", "h5", "h6",
    "u3", "u4", "u5", "u6", "u7", "t",
)
FAMILY_DIRS = {
    5: ROOT / "candidate_data" / "q79_Ronly_u1_002_space5_symbolic_u2_prefix",
    6: ROOT / "candidate_data" / "q79_Ronly_u1_002_space6_symbolic_u2_prefix",
}
DEFAULT_CHECKPOINT = ROOT / "runtime" / "q79_Ronly_u1_002_u2_021.checkpoint.json"
DEFAULT_RESULT = (
    ROOT
    / "candidate_data"
    / "q79_Ronly_u1_002_u2_021_job"
    / "q79_Ronly_u1_002_u2_021.result.packet.json"
)
CONTROLLING_CERTIFICATE = (
    ROOT / "certificates" / "Q79_Ronly_U1_002_Contiguous_CrossSpace_Prefix_v1.json"
)
EXECUTION_CONTRACT = (
    ROOT / "proof_corpus" / "Q79_Ronly_U1_002_U2_021_Execution_Contract_v1.md"
)


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def artifact(path: Path) -> dict[str, object]:
    require(path.is_file(), f"artifact exists: {path}")
    try:
        display = path.relative_to(ROOT).as_posix()
    except ValueError:
        display = str(path)
    return {"path": display, "bytes": path.stat().st_size, "sha256": sha256(path)}


def atomic_json(path: Path, value: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
    os.replace(temporary, path)


def run_text(command: list[str], *, timeout: float = 30.0) -> str:
    completed = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=timeout,
        check=False,
    )
    require(completed.returncode == 0, f"command failed: {command}\n{completed.stdout}")
    return completed.stdout.strip()


def wsl_path(path: Path) -> str:
    windows = PureWindowsPath(path.resolve())
    require(bool(windows.drive), f"absolute Windows path: {path}")
    drive = windows.drive.rstrip(":").lower()
    return "/mnt/" + drive + "/" + "/".join(windows.parts[1:])


def wsl_command(distribution: str, command: str) -> list[str]:
    return [
        "wsl.exe", "--distribution", distribution, "--exec",
        "bash", "-lc", command,
    ]


def classify_basis(path: Path) -> str | None:
    if not path.is_file() or path.stat().st_size == 0:
        return None
    text = path.read_text(encoding="utf-8", errors="strict").replace("\r\n", "\n")
    if not (
        text.startswith("#Reduced Groebner basis data\n")
        and "#field characteristic: 101" in text
        and "#variable order:       " + ", ".join(VARIABLES) in text
        and text.rstrip().endswith("]:")
    ):
        return None
    length = re.search(r"#length of basis:\s+(\d+) element", text)
    require(length is not None and int(length.group(1)) >= 1, f"basis length: {path}")
    return "R_ONLY_UNIT" if re.search(r"\[1\]:\s*$", text) else "R_ONLY_NONUNIT"


def validate_log(path: Path, classification: str, seed: int) -> None:
    require(path.is_file() and path.stat().st_size > 0, f"solver log: {path}")
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    required = (
        rf"Initial seed for pseudo-random number generator is {seed}",
        r"field characteristic\s+101",
        r"monomial order\s+DRL",
        r"#threads\s+1",
        r"linear algebra option\s+2",
        r"reduce gb\s+1",
        r"#invalid equations\s+0",
        r"msolve overall time",
    )
    require(all(re.search(pattern, text) for pattern in required), f"exact solver mode: {path}")
    if classification == "R_ONLY_UNIT":
        require(
            "Grobner basis has a single element" in text and "No solution" in text,
            f"unit basis verdict: {path}",
        )


def validate_input(path: Path, expected: dict[str, object]) -> None:
    require(path.is_file() and sha256(path) == expected["sha256"], f"input hash: {path}")
    lines = path.read_text(encoding="ascii").replace("\r\n", "\n").splitlines()
    require(tuple(lines[0].split(",")) == VARIABLES, f"variable order: {path}")
    require(int(lines[1]) == PRIME, f"field: {path}")
    rows = "\n".join(lines[2:]).rstrip().removesuffix(",").split(",\n")
    require(len(rows) == 13, f"13 symbolic rows: {path}")


def git_provenance() -> dict[str, object]:
    head = run_text(["git", "rev-parse", "HEAD"])
    status = run_text(["git", "status", "--short"])
    return {"commit": head, "status_before_execution": status.splitlines() if status else []}


def solver_provenance(distribution: str, solver: str) -> dict[str, object]:
    quoted = shlex.quote(solver)
    output = run_text(
        wsl_command(
            distribution,
            "set -e; "
            f"test -x {quoted}; "
            f"sha256sum {quoted}; "
            f"stat -c %s {quoted}; "
            f"{quoted} -h 2>&1 | grep -m 1 '^msolve library'; "
            "uname -a; "
            "ldd --version 2>&1 | head -n 1; "
            f"(ldd {quoted} 2>&1 || true)",
        )
    )
    lines = output.splitlines()
    require(len(lines) >= 5, "solver provenance output")
    digest, name = lines[0].split(maxsplit=1)
    require(name == solver and len(digest) == 64, "solver hash output")
    require(lines[1].isdigit(), "solver byte count")
    require("version 0.10.1" in lines[2], "msolve version")
    return {
        "engine": "msolve 0.10.1",
        "path_in_wsl": solver,
        "bytes": int(lines[1]),
        "sha256": digest,
        "version_banner": lines[2],
        "wsl_uname": lines[3],
        "dynamic_library_report": lines[4:],
    }


def load_family(space: int, u2: int) -> tuple[Path, dict[str, object], dict[str, object]]:
    packet_path = FAMILY_DIRS[space] / "family.packet.json"
    family = json.loads(packet_path.read_text(encoding="utf-8"))
    require(
        family.get("schema") == "MTTQ79RonlyFixedU1U2SymbolicFamily.v1"
        and family.get("status") == "EXACT_100_NONZERO_U2_SYMBOLIC_INPUTS_EMITTED"
        and family.get("space_index") == space
        and family.get("fixed_u1") == 2,
        f"space-{space} exact family",
    )
    record = family["records"][u2 - 1]
    require(record.get("u2") == u2, f"space-{space} u2 ordering")
    input_path = ROOT / str(record["input"]["path"])
    validate_input(input_path, record["input"])
    return packet_path, record, artifact(input_path)


def run_line(
    *,
    space: int,
    u2: int,
    distribution: str,
    solver: str,
    timeout_seconds: int,
    memory_mib: int,
    seed: int,
    checkpoint_dir: Path,
) -> dict[str, object]:
    packet_path, record, input_artifact = load_family(space, u2)
    input_path = ROOT / str(record["input"]["path"])
    output_path = input_path.with_suffix(".out")
    log_path = input_path.with_suffix(".log")
    saved = classify_basis(output_path)
    if saved is not None and log_path.is_file():
        validate_log(log_path, saved, seed)
        return {
            "space_index": space,
            "u1": 2,
            "u2": u2,
            "execution_status": f"RESUMED_EXACT_{saved}",
            "classification": saved,
            "elapsed_seconds": 0.0,
            "family_packet": artifact(packet_path),
            "input": input_artifact,
            "basis": artifact(output_path),
            "log": artifact(log_path),
        }

    checkpoint_dir.mkdir(parents=True, exist_ok=True)
    partial_output = checkpoint_dir / f"space{space}_u1_002_u2_{u2:03d}.out.partial"
    partial_log = checkpoint_dir / f"space{space}_u1_002_u2_{u2:03d}.log.partial"
    partial_output.unlink(missing_ok=True)
    partial_log.unlink(missing_ok=True)
    command = " ".join(
        [
            "set -o pipefail;",
            "timeout", "--signal=TERM", "--kill-after=30s", f"{timeout_seconds}s",
            "prlimit", f"--as={memory_mib * 1024 * 1024}", "--",
            shlex.quote(solver),
            "-t", "1", "-l", "2", "-d", "0", "-c", "0", "-g", "2",
            "--random-seed", str(seed),
            "-f", shlex.quote(wsl_path(input_path)),
            "-o", shlex.quote(wsl_path(partial_output)),
            "-v", "1", "-q", "0",
        ]
    )
    print(f"START space={space} u1=2 u2={u2} timeout={timeout_seconds}s", flush=True)
    started = time.perf_counter()
    completed = subprocess.run(
        wsl_command(distribution, command),
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=timeout_seconds + 90,
        check=False,
    )
    elapsed = time.perf_counter() - started
    partial_log.write_text(completed.stdout, encoding="utf-8", newline="\n")
    classification = classify_basis(partial_output) if completed.returncode == 0 else None
    require(
        completed.returncode == 0 and classification is not None,
        f"space-{space} u2={u2} incomplete exit={completed.returncode}; log={partial_log}",
    )
    validate_log(partial_log, classification, seed)
    os.replace(partial_output, output_path)
    os.replace(partial_log, log_path)
    print(
        f"DONE space={space} u1=2 u2={u2} {classification} elapsed={elapsed:.1f}s",
        flush=True,
    )
    return {
        "space_index": space,
        "u1": 2,
        "u2": u2,
        "execution_status": f"EXACT_{classification}",
        "classification": classification,
        "elapsed_seconds": elapsed,
        "family_packet": artifact(packet_path),
        "input": input_artifact,
        "basis": artifact(output_path),
        "log": artifact(log_path),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--u2", type=int, default=21)
    parser.add_argument("--spaces", default="5,6")
    parser.add_argument("--checkpoint", type=Path, default=DEFAULT_CHECKPOINT)
    parser.add_argument("--result", type=Path, default=DEFAULT_RESULT)
    parser.add_argument(
        "--controlling-certificate", type=Path, default=CONTROLLING_CERTIFICATE
    )
    parser.add_argument("--execution-contract", type=Path, default=EXECUTION_CONTRACT)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--wsl-distribution", default="Ubuntu")
    parser.add_argument("--msolve", default="/home/nerodes/.local/opt/msolve-0.10.1/msolve")
    parser.add_argument("--timeout-seconds", type=int, default=7200)
    parser.add_argument("--memory-mib", type=int, default=12288)
    parser.add_argument("--seed", type=int, default=790021)
    args = parser.parse_args()

    spaces = [int(value) for value in args.spaces.split(",") if value]
    require(spaces and len(spaces) == len(set(spaces)) and set(spaces) <= {5, 6}, "spaces")
    require(1 <= args.u2 < PRIME, "nonzero u2")
    require(args.timeout_seconds > 0 and args.memory_mib >= 512 and args.seed >= 0, "bounds")
    if args.resume:
        require(args.checkpoint.is_file(), "--resume requires an existing checkpoint")

    runner = Path(__file__).resolve()
    provenance = {
        "git": git_provenance(),
        "runner": artifact(runner),
        "authority_inputs": {
            "controlling_certificate": artifact(args.controlling_certificate.resolve()),
            "execution_contract": artifact(args.execution_contract.resolve()),
        },
        "python": {
            "version": sys.version,
            "executable": sys.executable,
            "platform": platform.platform(),
        },
        "solver": solver_provenance(args.wsl_distribution, args.msolve),
    }
    require(
        provenance["solver"]["sha256"]
        == "a4c2beb9a7d186394af6bb21e235f76e3bfb3d0e6fdf872c27b517b8a6e87e13",
        "selected msolve binary",
    )
    source_hashes: dict[str, object] = {
        "runner": provenance["runner"]["sha256"],
        "solver": provenance["solver"]["sha256"],
        "controlling_certificate": provenance["authority_inputs"]["controlling_certificate"]["sha256"],
        "execution_contract": provenance["authority_inputs"]["execution_contract"]["sha256"],
        "spaces": {},
    }
    for space in spaces:
        packet_path, _record, input_entry = load_family(space, args.u2)
        source_hashes["spaces"][str(space)] = {
            "family_packet": sha256(packet_path),
            "input": input_entry["sha256"],
        }
    config = {
        "u1": 2,
        "u2": args.u2,
        "spaces": spaces,
        "field": "F_101",
        "wsl_distribution": args.wsl_distribution,
        "msolve": args.msolve,
        "timeout_seconds_per_line": args.timeout_seconds,
        "memory_mib_per_line": args.memory_mib,
        "deterministic_seed": args.seed,
        "source_hashes": source_hashes,
    }
    config_fingerprint = hashlib.sha256(
        json.dumps(config, sort_keys=True).encode("utf-8")
    ).hexdigest()
    checkpoint: dict[str, object]
    if args.checkpoint.is_file():
        checkpoint = json.loads(args.checkpoint.read_text(encoding="utf-8"))
        require(checkpoint.get("config_fingerprint") == config_fingerprint, "checkpoint config")
        results = list(checkpoint.get("completed_lines", []))
    else:
        results = []
        checkpoint = {
            "schema": "MTTQ79RonlyExactLineJobCheckpoint.v1",
            "state": "running",
            "started_at_utc": datetime.now(timezone.utc).isoformat(),
            "config": config,
            "config_fingerprint": config_fingerprint,
            "completed_lines": results,
        }
        atomic_json(args.checkpoint, checkpoint)

    completed_spaces = {int(row["space_index"]) for row in results}
    for space in spaces:
        if space in completed_spaces:
            print(f"CHECKPOINT space={space} u1=2 u2={args.u2} already complete", flush=True)
            continue
        row = run_line(
            space=space,
            u2=args.u2,
            distribution=args.wsl_distribution,
            solver=args.msolve,
            timeout_seconds=args.timeout_seconds,
            memory_mib=args.memory_mib,
            seed=args.seed,
            checkpoint_dir=args.checkpoint.parent,
        )
        results.append(row)
        results.sort(key=lambda value: int(value["space_index"]))
        checkpoint["completed_lines"] = results
        checkpoint["last_completed_space"] = space
        atomic_json(args.checkpoint, checkpoint)

    require([row["space_index"] for row in results] == sorted(spaces), "all requested spaces")
    checks = {
        "checkpoint_completed_all_requested_spaces": True,
        "each_family_packet_and_input_is_hash_bound": True,
        "each_output_is_a_complete_exact_reduced_Groebner_basis": True,
        "each_log_records_F101_DRL_one_thread_exact_sparse_linear_algebra": True,
        "selected_msolve_version_and_binary_hash_are_recorded": True,
        "git_commit_runner_hash_python_environment_and_libraries_are_recorded": True,
        "partial_outputs_were_not_accepted": True,
        "nonunit_R_only_lines_are_not_promoted_to_full_R_y_D_closure": True,
        "no_continuous_fit_parameter_is_added": True,
    }
    result = {
        "schema": "MTTQ79RonlyU1002ExactLineJobResult.v1",
        "date": datetime.now(timezone.utc).date().isoformat(),
        "completed_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "EXACT_U1_002_U2_LINE_R_ONLY_CLASSIFIED",
        "config": config,
        "config_fingerprint": config_fingerprint,
        "provenance": provenance,
        "results": results,
        "accounting": {
            "requested_lines": len(spaces),
            "exact_R_only_lines": len(results),
            "R_only_unit_lines": sum(row["classification"] == "R_ONLY_UNIT" for row in results),
            "R_only_nonunit_lines": sum(row["classification"] == "R_ONLY_NONUNIT" for row in results),
        },
        "checks": checks,
        "exit_certificate": (
            "The two requested R-only symbolic lines have complete exact reduced Groebner "
            "bases with hash-bound inputs, outputs, logs, code, solver, Git, and environment "
            "provenance. A nonunit R-only result remains open pending an independent selected "
            "D-augmented unit certificate."
        ),
        "claim_boundary": (
            "Process success and R-only classification do not promote the contiguous-prefix "
            "theorem, the q79 physical branch, characteristic zero, HYM, or quantum gravity."
        ),
        "new_continuous_fit_parameters": 0,
    }
    atomic_json(args.result, result)
    checkpoint["state"] = "complete"
    checkpoint["result"] = artifact(args.result)
    atomic_json(args.checkpoint, checkpoint)
    print(result["status"], flush=True)
    print(args.result, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
