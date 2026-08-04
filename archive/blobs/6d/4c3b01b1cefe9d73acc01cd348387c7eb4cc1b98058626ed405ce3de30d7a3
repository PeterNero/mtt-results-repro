"""Audit the q64=15 to Qa/SU3 local-system bridge attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_q64_to_qa_su3_local_system_bridge_attempt_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Q64_to_Qa_SU3_Local_System_Bridge_Attempt_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_q64_to_qa_su3_local_system_bridge_attempt.py"


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
    reqs = {row["id"]: row for row in cert["bridge_requirements"]}
    verdict = cert["verdict"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "Q64_TO_QA_SU3_LOCAL_SYSTEM_BRIDGE_ATTEMPT_PARTIAL_NOT_CLOSED",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["bridge_requirements"] == cert["bridge_requirements"]
            and computed["selected_data"] == cert["selected_data"],
            computed["verdict"],
        ),
        check(
            "q64 selected and Nil acyclic carried",
            cert["selected_data"]["q64_selected"] is True
            and cert["selected_data"]["nil_pnonzero_acyclic"] is True,
            cert["selected_data"],
        ),
        check(
            "candidate character identified but bridge not closed",
            cert["bridge_candidate"]["status"] == "CANDIDATE_ONLY"
            and verdict["q64_to_nil_character_candidate_identified"] is True
            and verdict["bridge_closed"] is False,
            cert["bridge_candidate"],
        ),
        check(
            "homomorphism missing",
            reqs["homomorphism_to_local_system"]["status"] == "MISSING"
            and "pi_1" in reqs["homomorphism_to_local_system"]["test"],
            reqs["homomorphism_to_local_system"],
        ),
        check(
            "operator domain missing",
            reqs["operator_domain_compatibility"]["status"] == "MISSING",
            reqs["operator_domain_compatibility"],
        ),
        check(
            "torsion finite part missing",
            reqs["torsion_finite_part"]["status"] == "MISSING",
            reqs["torsion_finite_part"],
        ),
        check(
            "no target fitting",
            reqs["no_target_selection"]["status"] == "PASS"
            and verdict["target_fitting_used"] is False,
            reqs["no_target_selection"],
        ),
        check(
            "forbidden shortcuts recorded",
            "q64=15 as Qa/SU3 torsion by name similarity alone" in cert["do_not_use"],
            cert["do_not_use"],
        ),
        check(
            "note records next theorem",
            "Selected_Qa_SU3_Central_Character_Homomorphism_Theorem_v1" in note,
            NOTE,
        ),
    ]

    print("\nSelected q64 to Qa/SU3 local-system bridge attempt audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
