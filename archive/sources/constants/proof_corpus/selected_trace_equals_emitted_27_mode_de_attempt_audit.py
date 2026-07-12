"""Audit the SelectedTraceEqualsEmitted27ModeDE attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
SCRIPT = ROOT / "scripts" / "attempt_selected_trace_equals_emitted_27_mode_de.py"
PACKET = DATA / "selected_trace_equals_emitted_27_mode_de_attempt.candidate.json"
CERT = CERTS / "selected_trace_equals_emitted_27_mode_de_attempt_certificate.json"
NOTE = ROOT / "proof_corpus" / "SelectedTraceEqualsEmitted27ModeDE_Attempt_v1.md"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(label: str, condition: bool, detail: object) -> None:
    status = "PASS" if condition else "FAIL"
    print(f"{status}: {label} -- {detail}")
    if not condition:
        raise SystemExit(1)


def main() -> int:
    packet = load_json(PACKET)
    cert = load_json(CERT)
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    check("script runs", proc.returncode == 0, proc.stdout)
    script_cert = json.loads(proc.stdout)

    expected = "EMITTED_DE_FORMULA_CLOSED_SELECTED_TRACE_EQUALITY_OPEN"
    check("certificate status", cert["status"] == expected, cert["status"])
    check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    check("formula theorem closed", packet["formula_theorem"]["proved"], packet["formula_theorem"])
    checks = packet["sector_formula_checks"]
    check(
        "all sectors match formula",
        all(item["matches_canonical_formula"] and item["offdiag_max"] == 0.0 for item in checks.values()),
        checks,
    )
    check(
        "H rank-two shift recorded",
        checks["H"]["higgs_shift_indices"] == [13, 14],
        checks["H"],
    )
    check(
        "selected trace still open",
        not packet["selected_trace_attempt"]["proved"]
        and packet["guardrails"]["does_not_claim_selected_trace_equality"],
        packet["selected_trace_attempt"],
    )
    check(
        "source flags remain false",
        all(not item["selected_source_verified"] for item in checks.values()),
        checks,
    )
    check(
        "eta consequence remains conditional",
        packet["conditional_consequence"]["eta_N_if_gate_closes"] == 1.0
        and packet["conditional_consequence"]["passes_threshold"]
        and not packet["conditional_consequence"]["selected_eta_emitted_now"],
        packet["conditional_consequence"],
    )
    note = NOTE.read_text(encoding="utf-8")
    check("note records formula", "((2*pi)/3)^2" in note and "indices 13,14" in note, NOTE)

    print("\nSelectedTraceEqualsEmitted27ModeDE attempt audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
