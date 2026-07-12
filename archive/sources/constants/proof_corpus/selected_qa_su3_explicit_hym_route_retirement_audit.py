"""Audit the explicit Qa/SU3 HYM route retirement decision."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_explicit_hym_route_retirement_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Explicit_HYM_Route_Retirement_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_qa_su3_explicit_hym_route_retirement.py"


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
    verdict = cert["verdict"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_EXPLICIT_HYM_MATRIX_ROUTE_RETIRED_CURRENT_SOURCE_RECORD",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["retirement_basis"] == cert["retirement_basis"]
            and computed["selected_next_routes"] == cert["selected_next_routes"],
            computed["verdict"],
        ),
        check(
            "three blocked branches recorded",
            len(cert["retirement_basis"]) == 3
            and all(item["status"] in {"blocked", "retired_under_selected_branch", "current_source_no_go"} for item in cert["retirement_basis"]),
            cert["retirement_basis"],
        ),
        check(
            "retirement scoped to current proof",
            cert["retirement_scope"]["explicit_hym_matrix_route_retired_for_current_proof"] is True
            and cert["retirement_scope"]["future_erratum_can_reopen"] is True
            and cert["retirement_scope"]["mathematical_hym_bundle_existence_retired"] is False,
            cert["retirement_scope"],
        ),
        check(
            "next routes ranked",
            [route["rank"] for route in cert["selected_next_routes"]] == [1, 2, 3],
            cert["selected_next_routes"],
        ),
        check(
            "forbidden shortcuts recorded",
            "observed electroweak or Qa residuals to choose determinant factors" in cert["do_not_use"],
            cert["do_not_use"],
        ),
        check(
            "no closure claimed",
            verdict["qa_su3_closed"] is False
            and verdict["target_fitting_used"] is False,
            verdict,
        ),
        check(
            "note records next decision gate",
            "Selected_Qa_SU3_Endomorphism_or_Local_System_Torsion_Decision_v1" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 explicit HYM route retirement audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
