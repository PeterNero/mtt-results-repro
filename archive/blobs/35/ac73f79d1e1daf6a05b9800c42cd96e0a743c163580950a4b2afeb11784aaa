"""Audit the selected heterotic endomorphism threshold value-packet fill."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_endomorphism_threshold_valuepacket_fill.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_endomorphism_threshold_valuepacket_fill.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_endomorphism_threshold_valuepacket_fill_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_Endomorphism_Threshold_ValuePacket_Fill_v1.md"

STATUS = "HETEROTIC_ENDOMORPHISM_THRESHOLD_VALUEPACKET_FILL_ATTEMPT_BLOCKED_SOURCE_VALUES_OPEN"
NEXT = "Selected_Heterotic_SourceCertificate_or_DirectOperatorEmission_Search_v1"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return proc.returncode

    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    flags = data["required_flags"]
    missing = data["missing_fields"]
    packet = data["filled_packet"]
    guards = data["guardrails"]

    checks = [
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 3, proc.stdout),
        check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"])),
        check("next", data["decision"]["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, cert),
        check("quotient partial only", packet["operator_domain"]["domain_after_p0_and_p_nonzero_quotient"].startswith("partial imported"), packet["operator_domain"]),
        check("source missing", flags["source_certificate"] is False and flags["same_branch_identity"] is False, flags),
        check("operator values missing", flags["connection_or_curvature"] is False and flags["endomorphism_E"] is False and flags["finite_part_data"] is False, flags),
        check("missing count substantial", len(missing) >= 10 and cert["missing_field_count"] == len(missing), missing),
        check("not determinant computable", data["decision"]["template_filled_enough_for_determinant"] is False and cert["template_filled_enough_for_determinant"] is False, data["decision"]),
        check("guardrails", all(value is False for value in guards.values()), guards),
        check("note records no-go", "no determinant finite part can be promoted" in note, NOTE),
    ]
    print("\nSelected heterotic endomorphism threshold value-packet fill audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
