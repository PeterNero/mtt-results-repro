"""Audit BN27 source-branch identity source-amendment template / connection-values gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_bn27_sourcebranchidentity_sourceamendment_template_or_connectionvalues.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_sourcebranchidentity_sourceamendment_template_or_connectionvalues.candidate.json"
TEMPLATE = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_sourcebranchidentity_sourceamendment_template.json"
FILL = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_sourcebranchidentity_sourceamendment_current_fill.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_bn27_sourcebranchidentity_sourceamendment_template_or_connectionvalues_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_BN27_SourceBranchIdentity_SourceAmendment_Template_or_ConnectionValues_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BN27_SOURCEBRANCHIDENTITY_SOURCEAMENDMENT_TEMPLATE_BUILT_CURRENT_FILL_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_SourceObject_or_ConnectionValuePayload_FillAttempt_v1"


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
    template = load(TEMPLATE)
    fill = load(FILL)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("template built", decision["template_built"] is True and TEMPLATE.exists(), decision)
    check("current fill built", decision["current_fill_built"] is True and FILL.exists(), decision)
    check("source fields count", decision["source_object_required_field_count"] == 11 and decision["source_object_filled_field_count"] == 0, decision)
    check("connection fields count", decision["connection_values_required_field_count"] == 8 and decision["connection_values_filled_field_count"] == 0, decision)
    check("source template open", all(value is None for value in template["source_object_template"].values()), template["source_object_template"])
    check("connection template open", all(value is None for value in template["connection_values_template"].values()), template["connection_values_template"])
    check("reusable support retained", all(fill["support_reusable"].values()), fill["support_reusable"])
    check("no closure", decision["source_branch_identity_closed"] is False and decision["same_source_export_to_BN27_validators"] is False, decision)
    check("no connection closure", decision["connection_values_closed"] is False and cert["connection_values_closed"] is False, cert)
    check("no logdet promotion", decision["oriented_logdet_promoted"] is False and cert["oriented_logdet_promoted"] is False, cert)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records template", NEXT in note and str(TEMPLATE.relative_to(ROOT)) in note and "source_object_filled_field_count = 0 / 11" in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin BN27 source-branch amendment template audit passed")


if __name__ == "__main__":
    main()
