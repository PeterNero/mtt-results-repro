"""Audit BN27 source-branch identity three-clause fill / connection solve gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_bn27_sourcebranchidentity_threeclause_fill_or_connectionsolve.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_sourcebranchidentity_threeclause_fill_or_connectionsolve.candidate.json"
PACKET = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_sourcebranchidentity_threeclause_acceptance_packet.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_bn27_sourcebranchidentity_threeclause_fill_or_connectionsolve_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_BN27_SourceBranchIdentity_ThreeClause_Fill_or_ConnectionSolve_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BN27_SOURCEBRANCHIDENTITY_THREECLAUSE_FILL_REDUCED_TO_SOURCE_AMENDMENT_OR_CONNECTIONVALUES"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_SourceBranchIdentity_SourceAmendment_Template_or_ConnectionValues_v1"


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
    packet = load(PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("three clauses present", set(data["clause_fill"].keys()) == {"one_selected_source_names_both_branches", "eleven_label_to_full_BN27_threshold_carrier", "routec_row_not_external_import"}, data["clause_fill"])
    check("support all, emit none", decision["support_count"] == 3 and decision["emitted_count"] == 0, decision)
    check("source identity open", decision["source_branch_identity_closed"] is False and decision["one_source_owns_both_branches"] is False, decision)
    check("full carrier open", decision["full_BN27_carrier_emitted"] is False, decision)
    check("routec internalization open", decision["routec_internalized"] is False, decision)
    check("connection solve open", decision["selected_connection_solve_closed"] is False and cert["selected_connection_solve_closed"] is False, cert)
    check("acceptance packet built", decision["source_amendment_packet_built"] is True and PACKET.exists(), decision)
    check("source payload open", all(value is None for value in packet["source_amendment_payload"].values()), packet["source_amendment_payload"])
    check("connection payload open", all(value is None for value in packet["connection_values_payload"].values()), packet["connection_values_payload"])
    check("trace equality scoped support only", data["root_reuse"]["selected_trace_equality_for_27mode_DE_gap_layer_closed"] is True and data["root_reuse"]["full_operator_formula_closed"] is False, data["root_reuse"])
    check("no logdet promotion", decision["oriented_logdet_promoted"] is False and cert["oriented_logdet_promoted"] is False, cert)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records packet", NEXT in note and str(PACKET.relative_to(ROOT)) in note and "emitted_count = 0" in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin BN27 source-branch three-clause fill/connection-solve audit passed")


if __name__ == "__main__":
    main()
