"""Audit source-branch identity emission attempt or current-source no-go."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_sourcebranchidentity_emission_or_nogo.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_sourcebranchidentity_emission_or_nogo.candidate.json"
REPAIR = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_sourcebranchidentity_repair_packet.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_sourcebranchidentity_emission_or_nogo_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_SourceBranchIdentity_Emission_or_NoGo_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_SOURCEBRANCHIDENTITY_CURRENT_SOURCE_NOGO_REPAIR_PACKET_BUILT"
NEXT = "Selected_Heterotic_OrientedPhiFin_SourceBranchIdentity_SourceAmendment_or_ConnectionValues_v1"


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
    repair = load(REPAIR)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    clauses = data["clauses"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("all clauses present", set(clauses) == {"one_selected_source_names_both_branches", "eleven_label_to_full_BN27_threshold_carrier", "routec_row_not_external_import"}, clauses.keys())
    check("all support present", decision["support_count"] == 3 and all(item["support_present"] for item in clauses.values()), clauses)
    check("none emitted", decision["emitted_count"] == 0 and all(item["emitted_by_current_source"] is False for item in clauses.values()), clauses)
    check("current no-go scoped", decision["current_source_nogo"] is True and "current repo/source artifacts only" in repair["current_nogo_scope"], repair)
    check("repair packet groups", set(repair["minimal_success_payload"]) == {"source_identity_transport_theorem", "BN27_domain_emission", "selected_connection_values_alternative"}, repair["minimal_success_payload"])
    check("no transport closure", decision["transport_reduced_leaf_resolved"] is False and decision["source_branch_identity_closed"] is False, decision)
    check("no export closure", decision["selected_connection_witness_export_closed"] is False and cert["selected_connection_witness_export_closed"] is False, cert)
    check("no logdet promotion", decision["oriented_logdet_promoted"] is False and cert["oriented_logdet_promoted"] is False, cert)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records repair", NEXT in note and str(REPAIR.relative_to(ROOT)) in note and "current_source_nogo = true" in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin source-branch identity emission/no-go audit passed")


if __name__ == "__main__":
    main()
