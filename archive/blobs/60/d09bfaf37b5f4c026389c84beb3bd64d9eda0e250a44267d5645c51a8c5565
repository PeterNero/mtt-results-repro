"""Audit the source-table solve or complement-kernel proof attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_sourcetablesolve_or_complementkernelproof.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_sourcetablesolve_or_complementkernelproof.candidate.json"
WITNESS = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_abstract_z3_cocycle_shadow_witness.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_sourcetablesolve_or_complementkernelproof_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_SourceTableSolve_or_ComplementKernelProof_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_SOURCETABLESOLVE_ABSTRACT_Z3_SHADOW_CLOSED_SMOOTH_SOURCE_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_SmoothSourceCertificate_or_ComplementOperatorPayload_v1"


def check(label: str, condition: bool, detail: object) -> None:
    if not condition:
        print(f"FAIL: {label} -- {detail}")
        sys.exit(1)
    print(f"PASS: {label} -- {detail}")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, text=True, capture_output=True)
    check("script reruns", proc.returncode == 0, proc.stdout + proc.stderr)

    data = load(DATA)
    witness = load(WITNESS)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    decision = data["decision"]
    lane_a = data["lane_A_progress"]
    lane_b = data["lane_B_progress"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("witness status", witness["status"] == "ABSTRACT_Z3_COCYCLE_SHADOW_SOLVED_NOT_SMOOTH_SOURCE_TABLES", witness["status"])
    check("eleven labels", len(witness["labels"]) == 11 and len(witness["tables"]) == 11 and len(witness["checks"]) == 11, witness["labels"])
    check("all abstract checks pass", all(all(value is True for value in checks.values()) for checks in witness["checks"].values()), witness["checks"])
    check("lane A partial only", lane_a["abstract_Z3_projective_cocycle_shadow_solved"] is True and lane_a["smooth_goodcover_source_table_solved"] is False and lane_a["bundle_operator_action_solved"] is False, lane_a)
    check("lane B open", lane_b["finite_no_double_count_policy_available"] is True and lane_b["smooth_operator_domain_solved"] is False and lane_b["complement_heat_kernel_solved"] is False, lane_b)
    check("decision preserves frontier", decision["abstract_Z3_shadow_closed"] is True and decision["smooth_source_certificate_closed"] is False and decision["complement_kernel_proved"] is False, decision)
    check("not claimed list blocks promotion", "selected smooth good-cover incidence" in witness["not_claimed"] and "bundle operator action or E_Qa" in witness["not_claimed"], witness["not_claimed"])
    check("remaining blocker singular", data["remaining_blocker"]["single_blocker_name"] == "selected smooth heterotic source/operator payload", data["remaining_blocker"])
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no closure", data["closure_claimed"] is False and cert["closure_claimed"] is False and data["target_fitting_used"] is False, cert)
    check("note records witness", NEXT in note and str(WITNESS.relative_to(ROOT)) in note and "not yet a selected smooth good-cover table" in note, NOTE)

    print("\nSelected heterotic projective rho_E source-table solve / complement-kernel proof audit")


if __name__ == "__main__":
    main()
