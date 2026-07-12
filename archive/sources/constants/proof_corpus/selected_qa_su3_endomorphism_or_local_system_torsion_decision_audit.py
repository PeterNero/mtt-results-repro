"""Audit the Qa/SU3 endomorphism or local-system torsion route decision."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_endomorphism_or_local_system_torsion_decision_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Endomorphism_or_Local_System_Torsion_Decision_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_qa_su3_endomorphism_or_local_system_torsion_decision.py"


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
    routes = {route["route"]: route for route in cert["route_decision"]}
    verdict = cert["verdict"]

    checks = [
        check(
            "certificate status",
            cert["status"]
            == "QA_SU3_ENDOMORPHISM_OR_LOCAL_SYSTEM_TORSION_DECISION_BUILT_TORSION_PRIMARY",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["route_decision"] == cert["route_decision"]
            and computed["decision_tests"] == cert["decision_tests"],
            computed["verdict"],
        ),
        check(
            "retired matrix respected",
            cert["decision_tests"]["retired_matrix_route"] is True
            and routes["selected_endomorphism_E_or_color_threshold_operator"]["status"]
            == "PHYSICALLY_PRIMARY_BUT_SOURCE_BLOCKED",
            cert["decision_tests"],
        ),
        check(
            "torsion is next executable route",
            routes["acyclic_local_system_torsion"]["rank_as_current_executable_next_step"] == 1
            and routes["acyclic_local_system_torsion"]["status"] == "BEST_CURRENT_EXECUTABLE_ROUTE",
            routes["acyclic_local_system_torsion"],
        ),
        check(
            "no numeric closure claimed",
            verdict["qa_su3_closed"] is False
            and verdict["torsion_route_currently_computable"] is False
            and verdict["target_fitting_used"] is False,
            verdict,
        ),
        check(
            "forbidden target-fitting shortcut recorded",
            "observed Qa/SU3 residual to choose a torsion character" in cert["do_not_use"],
            cert["do_not_use"],
        ),
        check(
            "next artifact named",
            cert["selected_next_artifact"]["name"]
            == "Selected_Qa_SU3_Local_System_Torsion_Source_Extraction_v1"
            and "Selected_Qa_SU3_Local_System_Torsion_Source_Extraction_v1" in note,
            cert["selected_next_artifact"],
        ),
    ]

    print("\nSelected Qa/SU3 endomorphism or local-system torsion decision audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
