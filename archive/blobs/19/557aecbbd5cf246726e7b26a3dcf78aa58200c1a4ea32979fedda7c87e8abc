"""Audit the full nil-theta cocycle equation gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "full_nil_theta_cocycle_equations_certificate.json"
DATA = REPO / "candidate_data" / "full_nil_theta_cocycle_equations.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Full_Nil_Theta_Cocycle_Equations_v1.md"
SCRIPT = REPO / "scripts" / "build_full_nil_theta_cocycle_equations.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
    computed = json.loads(proc.stdout)
    commutators = {tuple(item["pair"]): item["central"] for item in data["commutators"]}
    checks = [
        check("status", cert["status"] == "QA_SU3_FULL_NIL_THETA_COCYCLE_EQUATIONS_BUILT_SOLVER_VALUES_OPEN", cert["status"]),
        check("script agreement", computed["counts"] == cert["counts"] and computed["what_closes"] == cert["what_closes"], computed["counts"]),
        check("six generators", len(data["generators"]) == 6, len(data["generators"])),
        check("commutator g1 g3", commutators[("g1", "g3")] == {"g5": 1, "g6": 0}, commutators),
        check("commutator g2 g4", commutators[("g2", "g4")] == {"g5": -1, "g6": 0}, commutators),
        check("all charges represented", len(data["charge_targets"]) == 11 and all("target_cocycle" in item for item in data["charge_targets"]), data["charge_targets"]),
        check("central charges detected", data["counts"]["charges_with_central_component"] == 8, data["counts"]),
        check("values remain open", cert["what_remains_open"]["explicit_Phi_q_solution"] is True and cert["what_remains_open"]["qa_su3_packet_closed"] is False, cert["what_remains_open"]),
        check("no fitting", cert["closure_claimed"] is False and cert["target_fitting_used"] is False, cert),
        check("note records central commutators", "[g1,g3]=g5" in note and "Phi_q(gamma1*gamma2,z)" in note, NOTE),
    ]
    print("\nSelected Qa/SU3 full nil-theta cocycle equations audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
