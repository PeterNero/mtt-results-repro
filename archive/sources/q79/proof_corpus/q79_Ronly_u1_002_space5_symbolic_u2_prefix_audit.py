"""Audit the first three exact q79 space-5 symbolic-u2 lines at u1=2."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "q79_Ronly_u1_002_space5_symbolic_u2_prefix"
PARENT = ROOT / "candidate_data" / "q79_Ronly_classfree_representative_lines" / "space5_classfree_saturated_hR_core.msolve.in"
BUILDER = ROOT / "scripts" / "build_q79_Ronly_fixed_u1_u2_symbolic_family.py"
CERTIFIER = ROOT / "scripts" / "certify_q79_Ronly_u1_002_space5_symbolic_u2_prefix.py"
CERTIFICATE = ROOT / "certificates" / "Q79_Ronly_U1_002_Space5_Symbolic_U2_Prefix_v1.json"
THEOREM = Path(__file__).with_name("Q79_Ronly_U1_002_Space5_Symbolic_U2_Prefix_v1.md")


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def packet_without_paths(packet: dict[str, object]) -> dict[str, object]:
    cleaned = json.loads(json.dumps(packet))
    cleaned["parent_input"].pop("path", None)
    for row in cleaned["records"]:
        row["input"].pop("path", None)
    return cleaned


def main() -> None:
    required = [PARENT, BUILDER, CERTIFIER, CERTIFICATE, THEOREM, DATA / "family.packet.json"]
    required.extend(DATA / "inputs" / f"space5_u1_002_u2_{u2:03d}.msolve.{suffix}" for u2 in range(1, 4) for suffix in ("in", "out", "log"))
    required.extend(DATA / "inputs" / f"space5_u1_002_u2_{u2:03d}.msolve.in" for u2 in range(4, 101))
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        print("Missing files:\n" + "\n".join(missing))
        raise SystemExit(1)

    with tempfile.TemporaryDirectory(prefix="q79-u1-002-prefix-") as directory:
        temporary = Path(directory)
        rebuilt_dir = temporary / "inputs"
        rebuilt_packet_path = temporary / "family.packet.json"
        build_run = subprocess.run(
            [
                sys.executable,
                str(BUILDER),
                "--input",
                str(PARENT),
                "--space",
                "5",
                "--u1",
                "2",
                "--output-dir",
                str(rebuilt_dir),
                "--packet",
                str(rebuilt_packet_path),
            ],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        rebuilt_inputs_equal = build_run.returncode == 0 and all(
            (rebuilt_dir / f"space5_u1_002_u2_{u2:03d}.msolve.in").read_bytes()
            == (DATA / "inputs" / f"space5_u1_002_u2_{u2:03d}.msolve.in").read_bytes()
            for u2 in range(1, 101)
        )
        committed_packet = json.loads((DATA / "family.packet.json").read_text(encoding="utf-8"))
        rebuilt_packet = (
            json.loads(rebuilt_packet_path.read_text(encoding="utf-8"))
            if rebuilt_packet_path.is_file()
            else {}
        )
        rebuilt_packet_equal = packet_without_paths(rebuilt_packet) == packet_without_paths(committed_packet)

        regenerated_path = temporary / "certificate.json"
        certify_run = subprocess.run(
            [sys.executable, str(CERTIFIER), "--output", str(regenerated_path)],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        regenerated = json.loads(regenerated_path.read_text(encoding="utf-8")) if regenerated_path.is_file() else {}

    committed = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    theorem = THEOREM.read_text(encoding="utf-8")
    accounting = regenerated.get("accounting", {})
    checks = regenerated.get("checks", {})
    coordinates = [
        (row.get("u2"), row.get("canonical_scalar_class"), row.get("canonical_a"))
        for row in regenerated.get("exact_unit_lines", [])
    ]
    gates = [
        Gate("all artifacts present", "PASS", f"files={len(required)}"),
        Gate("family builder reruns", "PASS" if build_run.returncode == 0 else "FAIL", build_run.stdout[-160:].strip()),
        Gate("all 100 symbolic inputs reproduce", "PASS" if rebuilt_inputs_equal else "FAIL", "byte-for-byte"),
        Gate("family packet reproduces", "PASS" if rebuilt_packet_equal else "FAIL", "path-normalized equality"),
        Gate("certifier reruns", "PASS" if certify_run.returncode == 0 else "FAIL", certify_run.stdout[-180:].strip()),
        Gate("certificate reproduces", "PASS" if regenerated == committed else "FAIL", "committed == regenerated"),
        Gate(
            "exact prefix status",
            "PASS" if regenerated.get("status") == "EXACT_U1_002_SPACE5_THREE_U2_SYMBOLIC_LINES_CLOSED" else "FAIL",
            "three literal [1] bases",
        ),
        Gate("canonical coordinates", "PASS" if coordinates == [(1, 1, 1), (2, 2, 1), (3, 2, 13)] else "FAIL", str(coordinates)),
        Gate(
            "exact accounting",
            "PASS" if accounting == {
                "symbolic_u2_lines_emitted": 100,
                "symbolic_u2_lines_exactly_classified": 3,
                "symbolic_u2_lines_proved_unit": 3,
                "symbolic_u2_lines_remaining_unclassified": 97,
                "canonical_fixed_F101_fibers_closed": 300,
                "fixed_fibers_per_symbolic_line": 100,
            } else "FAIL",
            "3/100 lines; 300 fibers",
        ),
        Gate("all exact checks", "PASS" if len(checks) == 10 and all(checks.values()) else "FAIL", f"{sum(bool(value) for value in checks.values())}/10"),
        Gate(
            "claim boundary retained",
            "PASS" if "remaining unclassified:                   97" in theorem and "remains `138/140`" in theorem else "FAIL",
            str(THEOREM),
        ),
        Gate("zero fit parameters", "PASS" if regenerated.get("new_continuous_fit_parameters") == 0 else "FAIL", "zero"),
    ]

    print("q79 u1=2 space-5 symbolic-u2 prefix audit")
    print("=============================================")
    width = max(len(gate.label) for gate in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:4s}  {gate.detail}")
    if any(gate.status == "FAIL" for gate in gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
