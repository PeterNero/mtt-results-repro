"""Audit the Qa/SU3 repair fork resolution requirements."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_repair_fork_resolution_requirements_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Repair_Fork_Resolution_Requirements_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_qa_su3_repair_fork_resolution_requirements.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def run_script() -> dict:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    return json.loads(proc.stdout)


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    computed = run_script()
    note = NOTE.read_text(encoding="utf-8")

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_REPAIR_FORK_RESOLUTION_REQUIREMENTS_COMPUTED_NO_CLOSURE",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["repair_A_requirement"] == cert["repair_A_requirement"]
            and computed["repair_B_requirement"] == cert["repair_B_requirement"],
            computed["verdict"],
        ),
        check(
            "repair A extra nullity recorded",
            cert["repair_A_requirement"]["extra_noncentral_nullity"] >= 1,
            cert["repair_A_requirement"],
        ),
        check(
            "repair B correction nonzero",
            cert["repair_B_requirement"]["samples"][1]["correction_norm_squared"] > 0,
            cert["repair_B_requirement"]["samples"][1],
        ),
        check(
            "forbidden shortcut present",
            "desired Qa/SU3" in cert["fork_resolution"]["forbidden_shortcut"],
            cert["fork_resolution"],
        ),
        check(
            "no closure claimed",
            cert["verdict"]["fork_resolved"] is False
            and cert["verdict"]["safe_to_close_Qa_SU3"] is False,
            cert["verdict"],
        ),
        check(
            "note records next fork test",
            "Selected_Qa_SU3_Repair_A_Quotient_Mode_or_Repair_B_Torsion_Source_Test_v1"
            in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 repair fork resolution requirements audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
