"""Audit the exact R-only q79 triple-fiber unit and degree lower bound."""

from __future__ import annotations

import gzip
import hashlib
import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "q79_Ronly_triple_fiber_min_degree"
SCRIPT = ROOT / "scripts" / "certify_q79_Ronly_triple_fiber_min_degree_frontier.py"
CERTIFICATE = ROOT / "certificates" / "Q79_Ronly_Triple_Fiber_Unit_and_Min_Degree_v1.json"
THEOREM = Path(__file__).with_name("Q79_Ronly_Triple_Fiber_Unit_and_Degree_Lower_Bound_v1.md")


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def gzip_sha256(path: Path) -> tuple[str, str]:
    digest = hashlib.sha256()
    first_line = b""
    with gzip.open(path, "rb") as stream:
        first_line = stream.readline().rstrip(b"\r\n")
        digest.update(first_line + b"\n")
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest(), first_line.decode("ascii")


def main() -> None:
    required = [
        SCRIPT,
        CERTIFICATE,
        THEOREM,
        DATA / "parent_space5_class1_inverse_root.msolve.in",
        DATA / "direct_Ronly_f4.packet.json",
        DATA / "carrier_input.packet.json",
        DATA / "carrier.msolve.in",
        DATA / "carrier_linalg1.msolve.out",
        DATA / "carrier_linalg2.msolve.out",
        DATA / "D6.sms.packet.json",
        DATA / "D6.augmented.packet.json",
        DATA / "D6.exact_sparse_rank.log",
        DATA / "D6.augmented.exact_sparse_rank.log",
        DATA / "D6.transpose.sms.gz",
        DATA / "D6.transpose.sms.rhs",
        DATA / "D7.sms.packet.json",
        DATA / "D7.augmented.packet.json",
        DATA / "D7.exact_sparse_rank.log",
        DATA / "D7.augmented.exact_sparse_rank.log",
        DATA / "D7.transpose.sms.gz",
        DATA / "D7.transpose.sms.rhs",
    ]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        print("Missing files:")
        print("\n".join(missing))
        raise SystemExit(1)

    matrix_checks = {}
    for degree in (6, 7):
        packet = json.loads((DATA / f"D{degree}.sms.packet.json").read_text(encoding="utf-8"))
        digest, header = gzip_sha256(DATA / f"D{degree}.transpose.sms.gz")
        expected_header = (
            "38760 15640 M" if degree == 6 else "116280 66096 M"
        )
        matrix_checks[degree] = (
            digest == packet["operator"]["matrix"]["sha256"]
            and header == expected_header
            and hashlib.sha256((DATA / f"D{degree}.transpose.sms.rhs").read_bytes()).hexdigest()
            == packet["operator"]["right_hand_side"]["sha256"]
        )

    with tempfile.TemporaryDirectory(prefix="q79-r-only-audit-") as directory:
        regenerated = Path(directory) / "frontier.packet.json"
        command = [
            sys.executable,
            str(SCRIPT),
            "--parent-input", str(DATA / "parent_space5_class1_inverse_root.msolve.in"),
            "--direct-f4-packet", str(DATA / "direct_Ronly_f4.packet.json"),
            "--carrier-input-packet", str(DATA / "carrier_input.packet.json"),
            "--carrier-input", str(DATA / "carrier.msolve.in"),
            "--carrier-linalg1-output", str(DATA / "carrier_linalg1.msolve.out"),
            "--carrier-linalg2-output", str(DATA / "carrier_linalg2.msolve.out"),
            "--D6-packet", str(DATA / "D6.sms.packet.json"),
            "--D6-augmented-packet", str(DATA / "D6.augmented.packet.json"),
            "--D6-rank-log", str(DATA / "D6.exact_sparse_rank.log"),
            "--D6-augmented-rank-log", str(DATA / "D6.augmented.exact_sparse_rank.log"),
            "--D7-packet", str(DATA / "D7.sms.packet.json"),
            "--D7-augmented-packet", str(DATA / "D7.augmented.packet.json"),
            "--D7-rank-log", str(DATA / "D7.exact_sparse_rank.log"),
            "--D7-augmented-rank-log", str(DATA / "D7.augmented.exact_sparse_rank.log"),
            "--output", str(regenerated),
        ]
        completed = subprocess.run(
            command,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        regenerated_packet = (
            json.loads(regenerated.read_text(encoding="utf-8"))
            if completed.returncode == 0 and regenerated.exists()
            else {}
        )

    committed = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    theorem = THEOREM.read_text(encoding="utf-8")
    expected_status = "EXACT_R_ONLY_TRIPLE_FIBER_UNIT_WITH_CERTIFICATE_DEGREE_AT_LEAST_8"
    gates = [
        Gate("all artifacts present", "PASS", f"files={len(required)}"),
        Gate("D6 matrix hash and header", "PASS" if matrix_checks[6] else "FAIL", "38760x15640"),
        Gate("D7 matrix hash and header", "PASS" if matrix_checks[7] else "FAIL", "116280x66096"),
        Gate("consolidator reruns", "PASS" if completed.returncode == 0 else "FAIL", completed.stdout[-200:]),
        Gate("committed status", "PASS" if committed.get("status") == expected_status else "FAIL", expected_status),
        Gate("regenerated status", "PASS" if regenerated_packet.get("status") == expected_status else "FAIL", expected_status),
        Gate(
            "exact D6 rank jump",
            "PASS" if regenerated_packet.get("ordinary_total_degree_obstructions", {}).get("degree_6", {}).get("augmented", {}).get("rank") == 14832 else "FAIL",
            "14831 -> 14832",
        ),
        Gate(
            "exact D7 rank jump",
            "PASS" if regenerated_packet.get("ordinary_total_degree_obstructions", {}).get("degree_7", {}).get("augmented", {}).get("rank") == 58491 else "FAIL",
            "58490 -> 58491",
        ),
        Gate("D rows unused", "PASS" if committed.get("selected_rows", {}).get("D_terminal_rows_used") == [] else "FAIL", "R-only"),
        Gate("one-fiber boundary retained", "PASS" if "one displayed R-only triple fiber" in committed.get("claim_boundary", "") else "FAIL", "no chart promotion"),
        Gate("theorem note saved", "PASS" if "first unexcluded Macaulay degree is 8" in theorem else "FAIL", str(THEOREM)),
    ]

    print("q79 R-only triple-fiber minimum-degree frontier audit")
    print("========================================================")
    print()
    width = max(len(gate.label) for gate in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:4s}  {gate.detail}")
    if any(gate.status == "FAIL" for gate in gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
