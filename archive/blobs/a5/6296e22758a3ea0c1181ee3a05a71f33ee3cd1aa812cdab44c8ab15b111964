"""Audit the nine-line q79 u1=2 cross-space symbolic prefix."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
S5 = ROOT / "candidate_data" / "q79_Ronly_u1_002_space5_symbolic_u2_prefix"
S6 = ROOT / "candidate_data" / "q79_Ronly_u1_002_space6_symbolic_u2_prefix"
CERTIFIER = ROOT / "scripts" / "certify_q79_Ronly_u1_002_cross_space_symbolic_prefix_v3.py"
CERTIFICATE = ROOT / "certificates" / "Q79_Ronly_U1_002_CrossSpace_Symbolic_Prefix_v3.json"
THEOREM = Path(__file__).with_name("Q79_Ronly_U1_002_CrossSpace_Symbolic_Prefix_v3.md")
V2_AUDIT = Path(__file__).with_name("q79_Ronly_u1_002_cross_space_symbolic_prefix_v2_audit.py")
ACCELERATION = ROOT / "certificates" / "Q79_Ronly_U2_Laurent_Line_Acceleration_v1.json"
VARIABLES = (
    "h1", "h2", "h3", "h4", "h5", "h6",
    "u3", "u4", "u5", "u6", "u7", "t",
)


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def literal_unit(path: Path) -> bool:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    return bool(
        text.startswith("#Reduced Groebner basis data\n")
        and "#field characteristic: 101" in text
        and "#variable order:       " + ", ".join(VARIABLES) in text
        and re.search(r"#length of basis:\s+1 element", text)
        and re.search(r"\[1\]:\s*$", text)
    )


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def main() -> None:
    line_paths = {
        "space5_u2_6_input": S5 / "inputs" / "space5_u1_002_u2_006.msolve.in",
        "space5_u2_6_basis": S5 / "inputs" / "space5_u1_002_u2_006.msolve.out",
        "space5_u2_6_log": S5 / "inputs" / "space5_u1_002_u2_006.msolve.log",
        "space6_u2_3_input": S6 / "inputs" / "space6_u1_002_u2_003.msolve.in",
        "space6_u2_3_basis": S6 / "inputs" / "space6_u1_002_u2_003.msolve.out",
        "space6_u2_3_log": S6 / "inputs" / "space6_u1_002_u2_003.msolve.log",
    }
    required = [CERTIFIER, CERTIFICATE, THEOREM, V2_AUDIT, ACCELERATION, *line_paths.values()]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        print("Missing files:\n" + "\n".join(missing))
        raise SystemExit(1)

    v2_run = run([sys.executable, str(V2_AUDIT)])
    with tempfile.TemporaryDirectory(prefix="q79-u1-002-v3-") as directory:
        regenerated_path = Path(directory) / "certificate.json"
        certify_run = run([sys.executable, str(CERTIFIER), "--output", str(regenerated_path)])
        regenerated = json.loads(regenerated_path.read_text(encoding="utf-8")) if regenerated_path.is_file() else {}
    committed = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    family5 = json.loads((S5 / "family.packet.json").read_text(encoding="utf-8"))
    family6 = json.loads((S6 / "family.packet.json").read_text(encoding="utf-8"))
    acceleration = json.loads(ACCELERATION.read_text(encoding="utf-8"))
    inverse = acceleration["canonical_coordinate_bijection"]["inverse_table"]
    accounting = committed.get("accounting", {})
    checks = committed.get("checks", {})
    theorem = THEOREM.read_text(encoding="utf-8")

    family_binding = (
        family5["records"][5]["u2"] == 6
        and family5["records"][5]["input"]["sha256"] == digest(line_paths["space5_u2_6_input"])
        and family6["records"][2]["u2"] == 3
        and family6["records"][2]["input"]["sha256"] == digest(line_paths["space6_u2_3_input"])
    )
    expected_accounting = {
        "space5_symbolic_lines_closed": 6,
        "space6_symbolic_lines_closed": 3,
        "cross_space_symbolic_lines_closed": 9,
        "R_only_unit_lines": 8,
        "D_augmented_unit_lines": 1,
        "canonical_fixed_F101_fibers_closed": 900,
        "cross_space_symbolic_lines_remaining_unclassified": 191,
    }
    gates = [
        Gate("all artifacts present", "PASS", f"files={len(required)}"),
        Gate("seven-line predecessor audit", "PASS" if v2_run.returncode == 0 else "FAIL", v2_run.stdout[-120:].strip()),
        Gate("v3 certifier reruns", "PASS" if certify_run.returncode == 0 else "FAIL", certify_run.stdout[-150:].strip()),
        Gate("v3 certificate reproduces", "PASS" if regenerated == committed else "FAIL", "committed == regenerated"),
        Gate("new inputs bind to families", "PASS" if family_binding else "FAIL", "u2=6 and u2=3"),
        Gate("space-5 u2=6 literal unit", "PASS" if literal_unit(line_paths["space5_u2_6_basis"]) else "FAIL", digest(line_paths["space5_u2_6_basis"])),
        Gate("space-6 u2=3 literal unit", "PASS" if literal_unit(line_paths["space6_u2_3_basis"]) else "FAIL", digest(line_paths["space6_u2_3_basis"])),
        Gate(
            "canonical coordinates",
            "PASS" if inverse["6"] == {"scalar_class": 1, "canonical_a": 44} and inverse["3"] == {"scalar_class": 2, "canonical_a": 13} else "FAIL",
            "u2=6 -> (1,44); u2=3 -> (2,13)",
        ),
        Gate("nine-line accounting", "PASS" if accounting == expected_accounting else "FAIL", "9/200 lines; 900 fibers"),
        Gate("all consolidated checks", "PASS" if len(checks) == 10 and all(checks.values()) else "FAIL", f"{sum(bool(value) for value in checks.values())}/10"),
        Gate(
            "claim boundary retained",
            "PASS" if "remaining unclassified symbolic-u2 lines:         191" in theorem and "`138/140`" in theorem else "FAIL",
            str(THEOREM),
        ),
        Gate("zero fit parameters", "PASS" if committed.get("new_continuous_fit_parameters") == 0 else "FAIL", "zero"),
    ]
    print("q79 u1=2 cross-space nine-line symbolic prefix v3 audit")
    print("==========================================================")
    width = max(len(gate.label) for gate in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:4s}  {gate.detail}")
    if any(gate.status == "FAIL" for gate in gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
