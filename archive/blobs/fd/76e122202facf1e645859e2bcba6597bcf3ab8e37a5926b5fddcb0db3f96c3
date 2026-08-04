"""Audit the minimal smooth-closure source request or direct no-go artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_minimalsmoothclosure_sourcerequest_or_directnogo.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_minimalsmoothclosure_sourcerequest_or_directnogo.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_minimalsmoothclosure_sourcerequest_or_directnogo_certificate.json"
OPEN = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_minimal_smooth_closure_open_gate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_MinimalSmoothClosure_SourceRequest_or_DirectNoGo_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_MINIMAL_SMOOTH_CLOSURE_CURRENT_CORPUS_NOGO_SOURCE_REQUEST_LOCKED"
NEXT = "Selected_Heterotic_ProjectiveRhoE_NewSourceInsertion_GoodCoverTables_or_ExactFactorization_v1"


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
    cert = load(CERT)
    open_gate = load(OPEN)
    note = NOTE.read_text(encoding="utf-8")

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", data["decision"]["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, data["decision"])
    check("no-go conditions", all(data["no_go_conditions"].values()), data["no_go_conditions"])
    check("direct no-go proved", data["decision"]["direct_current_corpus_nogo_proved"] is True and cert["direct_current_corpus_nogo_proved"] is True, data["decision"])
    check("request locked", data["decision"]["source_request_locked"] is True and open_gate["status"] == "OPEN_REQUIRES_NEW_SOURCE_INSERTION", open_gate)
    check("closed internal retained", all(open_gate["closed_without_new_source"][key] is True for key in ["finite_internal_projection_packet", "finite_tau_rhoE_DE_Green_Riesz_chi_logdet", "no_double_count_policy"]), open_gate["closed_without_new_source"])
    check("blockers all absent", all(value is False for value in data["remaining_source_values"].values()) and all(value is False for value in open_gate["cannot_close_without_new_source"].values()), data["remaining_source_values"])
    check("two legal insertions", set(open_gate["two_legal_new_source_insertions"]) == {"exact_complement_factorization", "good_cover_transition_tables"}, open_gate["two_legal_new_source_insertions"])
    check("acceptance tests", len(open_gate["acceptance_tests_after_insertion"]) == 5 and "python scripts\\verify.py" in open_gate["acceptance_tests_after_insertion"][-1], open_gate["acceptance_tests_after_insertion"])
    check("no closure", data["closure_claimed"] is False and cert["closure_claimed"] is False and data["decision"]["smooth_finitepart_can_close_now"] is False, data["decision"])
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records open gate", NEXT in note and str(OPEN.relative_to(ROOT)) in note and "Direct No-Go" in note, NOTE)

    print("\nSelected heterotic projective rho_E minimal smooth-closure source request/direct no-go audit")


if __name__ == "__main__":
    main()
