"""Audit the GR-surface / internal-quantum separation theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "gr_surface_internal_quantum_separation_theorem_certificate.json"
DATA = REPO / "candidate_data" / "gr_surface_internal_quantum_separation_theorem.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_GR_Surface_Internal_Quantum_Separation_Theorem_v1.md"
SCRIPT = REPO / "scripts" / "build_gr_surface_internal_quantum_separation_theorem.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    theorem = data["theorem"]
    conclusions = theorem["conclusions"]
    decision = data["decision"]
    guardrails = data["guardrails"]
    checks = [
        check("status", cert["status"] == "QA_SU3_GR_SURFACE_INTERNAL_QUANTUM_SEPARATION_SOURCE_AMENDMENT_ACCEPTED_REDUCED_DETERMINANT_PROMOTED", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("source amendment present", data["inputs"]["authorial_source_amendment"] is True and "GR/protospinor/TT" in data["source_amendment"]["authorial_intended_setup"][0], data["source_amendment"]),
        check("internal finite domain", conclusions["Qa_SU3_internal_determinant_domain"] == "selected finite coherent packet H_sel", conclusions),
        check("GR surface routed away", "GR_protospinor" in conclusions["smooth_complement_policy"] and decision["GR_smooth_surface_response"] == "ROUTED_TO_GR_PROTOSPINOR_SECTOR", decision),
        check("logdet promoted only internally", conclusions["internal_reduced_logdet"] == "log(2008)" and data["closure_scope"] == "internal_reduced_Qa_SU3_determinant_only", conclusions),
        check("full SM not claimed", conclusions["measured_coupling_or_full_SM_closure_claimed"] is False and decision["full_SM_closure_now"] is False, decision),
        check("guardrails include no target fitting and no double count", any("fit observed couplings" in item for item in guardrails) and any("double-count" in item for item in guardrails), guardrails),
        check("finite packet locked", data["locked_finite_data"]["determinant"] == 2008 and data["locked_finite_data"]["Pi_tw"] == [0, 0, 1], data["locked_finite_data"]),
        check("note records theorem", "Selected internal reduced Qa/SU3 determinant = log(2008)" in note and "GR/protospinor" in note and "full SM closure = not claimed" in note, NOTE),
    ]
    print("\nSelected Qa/SU3 GR surface / internal quantum separation theorem audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
