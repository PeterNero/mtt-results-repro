"""Audit the full-corpus dependency audit artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "full_corpus_dependency_audit_certificate.json"
DATA = REPO / "candidate_data" / "full_corpus_dependency_audit.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Full_Corpus_Dependency_Audit_v1.md"
SCRIPT = REPO / "scripts" / "build_full_corpus_dependency_audit.py"


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
    gates = data["gate_results"]
    assumptions = {item["assumption"]: item["verdict"] for item in data["assumption_checks"]}
    checks = [
        check("status", cert["status"] == "QA_SU3_FULL_CORPUS_DEPENDENCY_AUDIT_BUILT_PERIOD_SELECTOR_AND_OPERATOR_SOURCE_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("all required scans present", all(row["present"] for row in data["source_scans"].values()), data["source_scans"]),
        check("dependency nodes include closure", any(row["node"] == "full_Qa_SU3_packet_closure" and row["status"] == "open" for row in data["dependency_nodes"]), data["dependency_nodes"]),
        check("unsafe assumptions rejected", assumptions["q79/S3 finite torsion can be imported directly."] == "rejected" and assumptions["Chern/Bianchi support is enough to close Qa/SU3."] == "rejected", assumptions),
        check("no contradiction found", gates["contradiction_found"] is False and cert["what_closes"]["no_current_contradiction_with_QG_GR_or_string_flux_layers"] is True, gates),
        check("no hidden selector found", gates["hidden_selector_found"] is False and gates["same_branch_period_selector_found"] is False, gates),
        check("operator packet still open", gates["selected_operator_packet_found"] is False and cert["what_remains_open"]["selected_D_E_or_rho_E_operator_packet"] is True, cert),
        check("closure not claimed", cert["closure_claimed"] is False and cert["what_remains_open"]["qa_su3_packet_closed"] is False, cert),
        check("no target fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
        check("note records next artifacts", cert["next_required_artifact"] in note and cert["parallel_search_artifact"] in note, NOTE),
    ]
    print("\nSelected Qa/SU3 full corpus dependency audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
