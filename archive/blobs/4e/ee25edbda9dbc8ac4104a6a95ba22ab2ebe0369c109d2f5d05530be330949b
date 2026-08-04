"""Audit the Qa/SU3 automorphy-factor constraint solver."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "automorphy_factor_constraint_solver_certificate.json"
DATA = REPO / "candidate_data" / "automorphy_factor_constraint_solver.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Automorphy_Factor_Constraint_Solver_v1.md"
SCRIPT = REPO / "scripts" / "build_automorphy_factor_constraint_solver.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
    computed = json.loads(proc.stdout)
    coverage = {item["id"]: item for item in data["coverage"]}
    checks = [
        check("status", cert["status"] == "QA_SU3_AUTOMORPHY_FACTOR_SOLVER_BUILT_FULL_NIL_THETA_OR_GERBE_REQUIRED", cert["status"]),
        check("script agreement", computed["ansatz_results"] == cert["ansatz_results"], computed["ansatz_results"]),
        check("flat rejected", cert["ansatz_results"]["flat_character_rejected"] is True and coverage["flat_character"]["covered_count"] == 0, coverage["flat_character"]),
        check("base pullback partial", 0 < coverage["base_torus_appell_humbert_pullback"]["covered_count"] < 11, coverage["base_torus_appell_humbert_pullback"]),
        check("full nil covers axes", coverage["full_nil_theta_automorphy"]["covers_all_required_charges"] is True, coverage["full_nil_theta_automorphy"]),
        check("gerbe alternative covers axes", coverage["projective_gerbe_twisted_factor"]["covers_all_required_charges"] is True, coverage["projective_gerbe_twisted_factor"]),
        check("no closure or fitting", cert["closure_claimed"] is False and cert["target_fitting_used"] is False, cert),
        check("note records next equations", "Phi_q(gamma1 gamma2,z)" in note and "projective gerbe" in note, NOTE),
    ]
    print("\nSelected Qa/SU3 automorphy factor constraint solver audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
