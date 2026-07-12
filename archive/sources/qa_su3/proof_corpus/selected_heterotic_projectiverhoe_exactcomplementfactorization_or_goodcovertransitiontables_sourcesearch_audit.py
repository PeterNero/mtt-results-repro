"""Audit the source search for exact complement factorization or good-cover tables."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_exactcomplementfactorization_or_goodcovertransitiontables_sourcesearch.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_exactcomplementfactorization_or_goodcovertransitiontables_sourcesearch.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_exactcomplementfactorization_or_goodcovertransitiontables_sourcesearch_certificate.json"
REQUEST = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_minimal_smooth_closure_source_request.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_ExactComplementFactorization_or_GoodCoverTransitionTables_SourceSearch_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_SOURCESEARCH_SUPPORT_FOUND_GOODCOVER_AND_EXACT_FACTORIZATION_VALUES_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_MinimalSmoothClosure_SourceRequest_or_DirectNoGo_v1"


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
    request = load(REQUEST)
    note = NOTE.read_text(encoding="utf-8")

    support = data["decision"]["support_found"]
    blockers = data["decision"]["blockers"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", data["decision"]["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, data["decision"])
    check("source scans present", all(scan["present"] for scan in data["source_scans"].values()), data["source_scans"])
    check("support found", support["SPT_or_heat_factorization_support_found"] is True and support["finite_projection_and_lens_factorization_guardrail_found"] is True and support["transition_function_language_found"] is True, support)
    check("values absent", data["decision"]["goodcover_transition_values_found"] is False and data["decision"]["exact_complement_factorization_found"] is False, data["decision"])
    check("blockers all closed false", all(value is False for value in blockers.values()), blockers)
    check("request minimal payloads", len(request["minimal_acceptable_payloads"]["good_cover_transition_tables"]) == 6 and len(request["minimal_acceptable_payloads"]["exact_complement_factorization"]) == 5, request["minimal_acceptable_payloads"])
    check("already closed retained", all(request["already_closed"].values()), request["already_closed"])
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no closure", data["closure_claimed"] is False and cert["closure_claimed"] is False and data["decision"]["can_close_smooth_finitepart_now"] is False, data["decision"])
    check("note records no source values", NEXT in note and "No source emits" in note and str(REQUEST.relative_to(ROOT)) in note, NOTE)

    print("\nSelected heterotic projective rho_E exact-complement/good-cover source-search audit")


if __name__ == "__main__":
    main()
