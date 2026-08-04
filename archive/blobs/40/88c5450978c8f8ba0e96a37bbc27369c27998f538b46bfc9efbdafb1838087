"""Audit oriented Phi_fin direct finite-response fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_directfiniteresponse_fillattempt.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_directfiniteresponse_fillattempt.candidate.json"
PACKET = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_directfiniteresponse_fillattempt_packet.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_directfiniteresponse_fillattempt_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_DirectFiniteResponse_FillAttempt_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_DIRECTFINITE_RESPONSE_FILLATTEMPT_SUPPORT_ONLY_SOURCE_IDENTITY_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_SourceIdentity_or_OrientedBN_OperatorEmission_v1"


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
    leaves = packet["leaf_status"]
    values = packet["operator_values_materialized"]
    finitepart = packet["finitepart_candidates"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("packet materialized", decision["oriented_diagonal_response_materialized"] is True and len(values["D_E_diagonal_on_oriented_nonzero_BN"]) == 16, values)
    check("positive spectrum support", min(values["positive_spectrum"]) > 0 and values["minimum_positive_eigenvalue"] == 1.0, values)
    check("orientation and policy leaves closed only", leaves["orientation_operator_Ctau_binding"]["closed"] is True and leaves["no_double_count_replay"]["closed"] is True, leaves)
    check("source leaves open", leaves["same_branch_source_certificate"]["closed"] is False and leaves["selected_domain_or_quotient_map_to_oriented_BN"]["closed"] is False, leaves)
    check("operator promotion open", leaves["D_E_or_EQa_matrix_on_oriented_BN"]["closed"] is False and leaves["Riesz_or_Green_operator"]["closed"] is False, leaves)
    check("finitepart not promoted", leaves["finitepart_trace_identity_for_oriented_logdet"]["closed"] is False and finitepart["promoted_to_threshold_finitepart"] is False, finitepart)
    check("no closure", decision["direct_same_source_finite_response_closed"] is False and decision["oriented_logdet_promoted"] is False and decision["new_threshold_value_closed"] is False, decision)
    check("guardrails", all(value is True for key, value in data["guardrails"].items() if key != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no overclaim", data["closure_claimed"] is False and cert["closure_claimed"] is False and data["target_fitting_used"] is False, cert)
    check("note records open frontier", str(PACKET.relative_to(ROOT)) in note and NEXT in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin direct finite-response fill-attempt audit passed")


if __name__ == "__main__":
    main()
