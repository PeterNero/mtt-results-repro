"""Audit the SM-parity repro import boundary for the rhoE frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM_REPRO = ROOT.parent / "mtt-sm-parity-repro"
SCRIPT = ROOT / "scripts" / "build_smparity_repro_import_boundary_for_rhoe_frontier.py"
DATA = ROOT / "candidate_data" / "smparity_repro_import_boundary_for_rhoe_frontier.candidate.json"
CERT = ROOT / "certificates" / "smparity_repro_import_boundary_for_rhoe_frontier_certificate.json"
NOTE = ROOT / "proof_corpus" / "SMParity_Repro_ImportBoundary_for_RhoE_Frontier_v1.md"

STATUS = "SMPARITY_REPRO_IMPORT_BOUNDARY_BUILT_RHOE_NOKNOB_FRONTIER_PRESERVED"
NEXT = "Selected_Heterotic_ProjectiveRhoE_SourceTableSolve_or_ComplementKernelProof_v1"


def check(label: str, condition: bool, detail: object) -> None:
    if not condition:
        print(f"FAIL: {label} -- {detail}")
        sys.exit(1)
    print(f"PASS: {label} -- {detail}")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    repro_proc = subprocess.run([sys.executable, "scripts\\verify.py"], cwd=SM_REPRO, text=True, capture_output=True)
    check("sm parity repro verifies", repro_proc.returncode == 0 and "Verification result: PASS" in repro_proc.stdout, repro_proc.stdout + repro_proc.stderr)

    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, text=True, capture_output=True)
    check("script reruns", proc.returncode == 0, proc.stdout + proc.stderr)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    decision = data["decision"]
    closures = data["imported_closures"]
    nonclosures = data["imported_nonclosures"]
    alignment = data["rhoe_frontier_alignment"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("closures imported for context", all(closures.values()) and decision["SM_parity_can_be_marked_closed_for_context"] is True, closures)
    check("nonclosures preserve frontier", all(nonclosures.values()) and decision["rhoe_no_knob_frontier_preserved"] is True, nonclosures)
    check("rhoE lanes not filled", alignment["sm_parity_repro_can_close_smooth_rhoE_transition_values"] is False and alignment["sm_parity_repro_can_close_complement_kernel"] is False and alignment["sm_parity_repro_can_close_same_branch_smooth_source_certificate"] is False, alignment)
    check("allowed imports are context only", "parity-interface closure status" in data["allowed_imports"] and "source-boundary and no-target-fitting certificate" in data["allowed_imports"], data["allowed_imports"])
    check("forbidden imports include operator data", "selected D_E/rho_E operator data" in data["forbidden_imports"] and "smooth heterotic rho_E transition matrices" in data["forbidden_imports"], data["forbidden_imports"])
    check("hashes recorded", len(data["input_hashes"]) == 5 and all(len(v) == 64 for v in data["input_hashes"].values()), data["input_hashes"])
    check("source/complement still required", decision["source_table_solve_still_required"] is True and decision["complement_kernel_proof_still_required"] is True, decision)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no closure", data["closure_claimed"] is False and cert["closure_claimed"] is False and data["target_fitting_used"] is False, cert)
    check("note records boundary", NEXT in note and "may not be imported as smooth heterotic" in note, NOTE)

    print("\nSM parity repro import boundary for rhoE frontier audit")


if __name__ == "__main__":
    main()
