"""Audit the U1/hypercharge local determinant spectrum attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1_hypercharge_local_determinant_spectrum_attempt.py"
DATA = REPO / "candidate_data" / "selected_u1_hypercharge_local_determinant_spectrum_attempt.candidate.json"
CERT = REPO / "certificates" / "selected_u1_hypercharge_local_determinant_spectrum_attempt_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1_Hypercharge_Local_Determinant_Spectrum_Attempt_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(name: str, condition: bool, detail: object) -> None:
    if condition:
        print(f"PASS: {name} -- {detail}")
        return
    print(f"FAIL: {name} -- {detail}")
    raise SystemExit(1)


def main() -> int:
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(proc.stdout)
    check("builder exits cleanly", proc.returncode == 0, proc.returncode)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    attempts = data["attempts"]

    check("status exact", data["status"] == "U1_HYPERCHARGE_SPECTRUM_ATTEMPT_DONE_SELECTED_SPECTRUM_OPEN", data["status"])
    expected_checks = dict(data["source_checks"])
    target_fitting = expected_checks.pop("target_fitting_used")
    check("all source checks pass", all(expected_checks.values()) is True and target_fitting is False, data["source_checks"])
    check("closure refused", data["decision"]["u1_hypercharge_spectrum_closed"] is False and data["decision"]["lambda_12_closed"] is False, data["decision"])
    check("projector identity rejected", attempts["quotient_identity"]["status"] == "REJECTED_PROJECTOR_IS_NOT_THRESHOLD_OPERATOR", attempts["quotient_identity"])
    check("central reuse rejected", attempts["central_circle_reuse"]["status"] == "REJECTED_DOUBLE_COUNTS_QUOTIENTED_SHARED_CIRCLE", attempts["central_circle_reuse"])
    check("primary route open", attempts["heterotic_section_ring"]["status"] == "OPEN_PRIMARY_ROUTE" and len(attempts["heterotic_section_ring"]["required_fields"]) == 5, attempts["heterotic_section_ring"])
    check("hypercharge missing row", data["hypercharge_gate"]["missing_part"] == "selected U1/Qa/hypercharge local determinant spectral row", data["hypercharge_gate"])
    check("certificate agrees", cert["open"]["selected_U1_hypercharge_positive_spectrum"] is True and cert["closed"]["bad_spectrum_shortcuts_rejected"] is True, cert)
    check("note records guardrails", "Do not treat P_perp itself" in note and "target_fitting_used = false" in note, NOTE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
