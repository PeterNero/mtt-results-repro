"""Audit the new-source insertion interface for smooth rho_E closure."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_newsourceinsertion_goodcovertables_or_exactfactorization.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_newsourceinsertion_goodcovertables_or_exactfactorization.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_newsourceinsertion_goodcovertables_or_exactfactorization_certificate.json"
TEMPLATE = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_newsourceinsertion.template.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_NewSourceInsertion_GoodCoverTables_or_ExactFactorization_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_NEWSOURCE_INSERTION_INTERFACE_BUILT_VALUES_REQUIRED"
NEXT = "Selected_Heterotic_ProjectiveRhoE_NewSourceInsertion_FillAttempt_v1"


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
    template = load(TEMPLATE)
    note = NOTE.read_text(encoding="utf-8")

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", data["decision"]["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, data["decision"])
    check("interface built", data["decision"]["interface_built"] is True and cert["interface_built"] is True, data["decision"])
    check("values absent", data["decision"]["values_filled"] is False and cert["values_filled"] is False and template["status"] == "VALUES_REQUIRED", template)
    check("template lanes", set(template) >= {"lane_A_good_cover_transition_tables", "lane_B_exact_complement_factorization", "promotion_outputs"}, template.keys())
    check("source certificate open", template["source_certificate"]["same_branch_Qa_SU3_heterotic_projective_source"] is None and template["source_certificate"]["selected_by_MTT_before_target_comparison"] is None, template["source_certificate"])
    check("no promotion", template["promotion_outputs"]["smooth_transition_tables_emitted"] is False and template["promotion_outputs"]["exact_smooth_complement_quotient_closed"] is False, template["promotion_outputs"])
    check("acceptance predicates", len(data["acceptance_predicates"]["lane_A_closes_if"]) >= 8 and len(data["acceptance_predicates"]["lane_B_closes_if"]) >= 5, data["acceptance_predicates"])
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no closure", data["closure_claimed"] is False and cert["closure_claimed"] is False and cert["smooth_finitepart_computed"] is False, cert)
    check("note records template", NEXT in note and str(TEMPLATE.relative_to(ROOT)) in note and "strict insertion interface" in note, NOTE)

    print("\nSelected heterotic projective rho_E new-source insertion interface audit")


if __name__ == "__main__":
    main()
