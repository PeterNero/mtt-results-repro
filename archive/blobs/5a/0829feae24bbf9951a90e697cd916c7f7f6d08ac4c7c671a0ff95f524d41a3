"""Audit the generated maximal closed contiguous q79 u1=2 prefixes."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERTIFIER = ROOT / "scripts" / "certify_q79_Ronly_u1_002_contiguous_prefix.py"
RENDERER = ROOT / "scripts" / "render_q79_Ronly_u1_002_contiguous_prefix_theorem.py"
CERTIFICATE = ROOT / "certificates" / "Q79_Ronly_U1_002_Contiguous_CrossSpace_Prefix_v1.json"
THEOREM = Path(__file__).with_name("Q79_Ronly_U1_002_Contiguous_CrossSpace_Prefix_v1.md")
V3_AUDIT = Path(__file__).with_name("q79_Ronly_u1_002_cross_space_symbolic_prefix_v3_audit.py")
BATCH_AUDIT = Path(__file__).with_name(
    "q79_Ronly_u1_002_remaining_029_100_batch_execution_audit.py"
)
D_AUDIT = Path(__file__).with_name(
    "q79_Ronly_u1_002_remaining_exception_D_closure_audit.py"
)


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def artifact_matches(entry: dict[str, object]) -> bool:
    path = ROOT / str(entry["path"])
    return bool(
        path.is_file()
        and path.stat().st_size == entry["bytes"]
        and hashlib.sha256(path.read_bytes()).hexdigest() == entry["sha256"]
    )


def main() -> None:
    required = [
        CERTIFIER,
        RENDERER,
        CERTIFICATE,
        THEOREM,
        V3_AUDIT,
        BATCH_AUDIT,
        D_AUDIT,
    ]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        print("Missing files:\n" + "\n".join(missing))
        raise SystemExit(1)

    predecessor_run = run([sys.executable, str(V3_AUDIT)])
    batch_run = run([sys.executable, str(BATCH_AUDIT)])
    d_run = run([sys.executable, str(D_AUDIT)])
    with tempfile.TemporaryDirectory(prefix="q79-u1-002-prefix-") as directory:
        temporary = Path(directory)
        regenerated_certificate_path = temporary / "certificate.json"
        regenerated_theorem_path = temporary / "theorem.md"
        certifier_run = run(
            [sys.executable, str(CERTIFIER), "--output", str(regenerated_certificate_path)]
        )
        renderer_run = run(
            [
                sys.executable, str(RENDERER),
                "--certificate", str(regenerated_certificate_path),
                "--output", str(regenerated_theorem_path),
            ]
        )
        regenerated = (
            json.loads(regenerated_certificate_path.read_text(encoding="utf-8"))
            if regenerated_certificate_path.is_file()
            else {}
        )
        theorem_equal = (
            regenerated_theorem_path.is_file()
            and regenerated_theorem_path.read_bytes() == THEOREM.read_bytes()
        )
    committed = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    rows5 = committed.get("space5_closed_lines", [])
    rows6 = committed.get("space6_closed_lines", [])
    accounting = committed.get("accounting", {})
    checks = committed.get("checks", {})
    n5 = len(rows5)
    n6 = len(rows6)
    total = n5 + n6
    all_rows = rows5 + rows6
    sequences = (
        [row.get("u2") for row in rows5] == list(range(1, n5 + 1))
        and [row.get("u2") for row in rows6] == list(range(1, n6 + 1))
    )
    source_bound = all(
        artifact_matches(row["R_only_input"])
        and artifact_matches(row["R_only_basis"])
        and artifact_matches(row["R_only_log"])
        and (
            row["complete_status"] == "EXACT_R_ONLY_UNIT"
            or artifact_matches(row["D_unit_certificate"])
        )
        for row in all_rows
    )
    r_units = sum(row["complete_status"] == "EXACT_R_ONLY_UNIT" for row in all_rows)
    d_units = sum(row["complete_status"] == "EXACT_FULL_R_Y_D_UNIT" for row in all_rows)
    expected_accounting = {
        "space5_contiguous_symbolic_lines_closed": n5,
        "space6_contiguous_symbolic_lines_closed": n6,
        "cross_space_symbolic_lines_closed": total,
        "R_only_unit_lines": r_units,
        "D_augmented_unit_lines": d_units,
        "canonical_fixed_F101_fibers_closed": 100 * total,
        "cross_space_symbolic_lines_remaining_unclassified": 200 - total,
    }
    stops = committed.get("first_unproved_line", {})
    stop_exact = (
        stops.get("space5", {}).get("next_u2") == n5 + 1
        and stops.get("space6", {}).get("next_u2") == n6 + 1
    )
    theorem = THEOREM.read_text(encoding="utf-8")
    complete_cover = (
        n5 == 100
        and n6 == 100
        and total == 200
        and r_units == 190
        and d_units == 10
        and accounting.get("cross_space_symbolic_lines_remaining_unclassified") == 0
        and committed.get("coverage_status") == "COMPLETE_NONZERO_U2_CROSSSPACE_COVER"
    )
    gates = [
        Gate("all artifacts present", "PASS", f"files={len(required)}"),
        Gate("nine-line predecessor audit", "PASS" if predecessor_run.returncode == 0 else "FAIL", predecessor_run.stdout[-120:].strip()),
        Gate("remaining batch audit", "PASS" if batch_run.returncode == 0 else "FAIL", batch_run.stdout[-140:].strip()),
        Gate("six-exception D replay audit", "PASS" if d_run.returncode == 0 else "FAIL", d_run.stdout[-140:].strip()),
        Gate("contiguous certifier reruns", "PASS" if certifier_run.returncode == 0 else "FAIL", certifier_run.stdout[-180:].strip()),
        Gate("certificate reproduces", "PASS" if regenerated == committed else "FAIL", "committed == regenerated"),
        Gate("theorem renderer reruns", "PASS" if renderer_run.returncode == 0 else "FAIL", renderer_run.stdout[-150:].strip()),
        Gate("theorem reproduces", "PASS" if theorem_equal else "FAIL", "byte-for-byte"),
        Gate("u2 prefixes are contiguous", "PASS" if sequences else "FAIL", f"space5={n5}; space6={n6}"),
        Gate("all counted artifacts are hash bound", "PASS" if source_bound else "FAIL", f"rows={total}"),
        Gate("accounting is exact", "PASS" if accounting == expected_accounting else "FAIL", f"closed={total}/200; fibers={100 * total}"),
        Gate(
            "complete nonzero-u2 cross-space cover",
            "PASS" if complete_cover else "FAIL",
            f"space5={n5}; space6={n6}; R={r_units}; D={d_units}",
        ),
        Gate("first unproved lines follow prefixes", "PASS" if stop_exact else "FAIL", str(stops)),
        Gate(
            "all certificate checks",
            "PASS" if checks and all(checks.values()) else "FAIL",
            f"{sum(bool(value) for value in checks.values())}/{len(checks)}",
        ),
        Gate(
            "claim boundary retained",
            "PASS"
            if "All `200` nonzero-`u2`, `u1=2` cross-space lines are classified."
            in theorem
            and "characteristic-zero system" in theorem
            and "`138/140`" in theorem
            else "FAIL",
            str(THEOREM),
        ),
        Gate("zero fit parameters", "PASS" if committed.get("new_continuous_fit_parameters") == 0 else "FAIL", "zero"),
    ]
    print("q79 u1=2 contiguous cross-space prefix audit")
    print("================================================")
    width = max(len(gate.label) for gate in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:4s}  {gate.detail}")
    if any(gate.status == "FAIL" for gate in gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
