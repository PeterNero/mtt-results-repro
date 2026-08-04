"""Audit the durable q79 u1=2, u2=21 execution result without promoting it."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "scripts" / "run_q79_Ronly_u1_002_exact_line_job.py"
RESULT = (
    ROOT
    / "candidate_data"
    / "q79_Ronly_u1_002_u2_021_job"
    / "q79_Ronly_u1_002_u2_021.result.packet.json"
)
VARIABLES = (
    "h1", "h2", "h3", "h4", "h5", "h6",
    "u3", "u4", "u5", "u6", "u7", "t",
)


@dataclass(frozen=True)
class Gate:
    label: str
    passed: bool
    detail: str


def resolve(path_text: str) -> Path:
    path = Path(path_text.replace("/", "\\"))
    return path if path.is_absolute() else ROOT / path


def matches(entry: dict[str, object]) -> bool:
    path = resolve(str(entry.get("path", "")))
    return matches_path(entry, path)


def matches_path(entry: dict[str, object], path: Path) -> bool:
    return bool(
        path.is_file()
        and path.stat().st_size == entry.get("bytes")
        and hashlib.sha256(path.read_bytes()).hexdigest() == entry.get("sha256")
    )


def matches_at_commit(entry: dict[str, object], commit: str) -> bool:
    if matches(entry):
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


def classify(path: Path) -> str | None:
    if not path.is_file() or path.stat().st_size == 0:
        return None
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    if not (
        text.startswith("#Reduced Groebner basis data\n")
        and "#field characteristic: 101" in text
        and "#variable order:       " + ", ".join(VARIABLES) in text
        and text.rstrip().endswith("]:")
    ):
        return None
    length = re.search(r"#length of basis:\s+(\d+) element", text)
    if length is None or int(length.group(1)) < 1:
        return None
    return "R_ONLY_UNIT" if re.search(r"\[1\]:\s*$", text) else "R_ONLY_NONUNIT"


def exact_log(path: Path, classification: str, seed: int) -> bool:
    if not path.is_file():
        return False
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    patterns = (
        rf"Initial seed for pseudo-random number generator is {seed}",
        r"field characteristic\s+101",
        r"monomial order\s+DRL",
        r"#threads\s+1",
        r"linear algebra option\s+2",
        r"reduce gb\s+1",
        r"#invalid equations\s+0",
        r"msolve overall time",
    )
    verdict = all(re.search(pattern, text) for pattern in patterns)
    if classification == "R_ONLY_UNIT":
        verdict = verdict and "Grobner basis has a single element" in text and "No solution" in text
    return verdict


def main(*, result_path: Path = RESULT, expected_u2: int = 21) -> None:
    contract = Path(__file__).with_name(
        f"Q79_Ronly_U1_002_U2_{expected_u2:03d}_Execution_Contract_v1.md"
    )
    required = [RUNNER, contract, result_path]
    if any(not path.is_file() for path in required):
        missing = [str(path) for path in required if not path.is_file()]
        print("Missing files:\n" + "\n".join(missing))
        raise SystemExit(1)

    packet = json.loads(result_path.read_text(encoding="utf-8"))
    config = packet.get("config", {})
    rows = packet.get("results", [])
    checks = packet.get("checks", {})
    provenance = packet.get("provenance", {})
    solver = provenance.get("solver", {})
    runner = provenance.get("runner", {})
    authority_inputs = provenance.get("authority_inputs", {})
    coordinates = [
        (row.get("space_index"), row.get("u1"), row.get("u2")) for row in rows
    ]
    row_artifacts = all(
        all(matches(row[key]) for key in ("family_packet", "input", "basis", "log"))
        for row in rows
    )
    classifications = [classify(resolve(str(row["basis"]["path"]))) for row in rows]
    class_match = all(
        classification is not None and classification == row.get("classification")
        for row, classification in zip(rows, classifications)
    )
    logs = all(
        exact_log(resolve(str(row["log"]["path"])), row["classification"], config["deterministic_seed"])
        for row in rows
    )
    git_commit = provenance.get("git", {}).get("commit", "")
    git_object = subprocess.run(
        ["git", "cat-file", "-e", f"{git_commit}^{{commit}}"],
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    ).returncode == 0
    accounting = packet.get("accounting", {})
    expected_accounting = {
        "requested_lines": 2,
        "exact_R_only_lines": 2,
        "R_only_unit_lines": sum(value == "R_ONLY_UNIT" for value in classifications),
        "R_only_nonunit_lines": sum(value == "R_ONLY_NONUNIT" for value in classifications),
    }
    runner_archive = result_path.parent / "run_q79_Ronly_u1_002_exact_line_job.executed.py"
    runner_source_matches = matches_at_commit(runner, str(git_commit)) or matches_path(
        runner, runner_archive
    )
    gates = [
        Gate("execution packet schema/status", packet.get("schema") == "MTTQ79RonlyU1002ExactLineJobResult.v1" and packet.get("status") == "EXACT_U1_002_U2_LINE_R_ONLY_CLASSIFIED", str(packet.get("status"))),
        Gate("requested coordinates", coordinates == [(5, 2, expected_u2), (6, 2, expected_u2)], str(coordinates)),
        Gate("all emitted artifacts hash-bind", row_artifacts, f"rows={len(rows)}"),
        Gate("basis classifications reproduce", class_match, str(classifications)),
        Gate("solver logs prove exact mode", logs, f"seed={config.get('deterministic_seed')}"),
        Gate("selected msolve binary", solver.get("engine") == "msolve 0.10.1" and solver.get("sha256") == "a4c2beb9a7d186394af6bb21e235f76e3bfb3d0e6fdf872c27b517b8a6e87e13", str(solver.get("sha256"))),
        Gate("runner source hash", runner_source_matches, f"live, commit, or immutable archive; {runner.get('sha256')}"),
        Gate("authority inputs hash-bind", bool(authority_inputs) and all(matches_at_commit(entry, str(git_commit)) for entry in authority_inputs.values()), f"live-or-commit={git_commit}; {sorted(authority_inputs)}"),
        Gate("recorded Git commit exists", git_object, str(git_commit)),
        Gate("accounting is exact", accounting == expected_accounting, str(accounting)),
        Gate("all job checks pass", bool(checks) and all(checks.values()), f"{sum(bool(value) for value in checks.values())}/{len(checks)}"),
        Gate("zero fit parameters", packet.get("new_continuous_fit_parameters") == 0, "zero"),
        Gate("claim boundary is retained", "do not promote" in packet.get("claim_boundary", ""), packet.get("claim_boundary", "")),
    ]
    print(f"q79 u1=2, u2={expected_u2} durable execution audit")
    print("=============================================")
    width = max(len(gate.label) for gate in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {'PASS' if gate.passed else 'FAIL':4s}  {gate.detail}")
    if not all(gate.passed for gate in gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
