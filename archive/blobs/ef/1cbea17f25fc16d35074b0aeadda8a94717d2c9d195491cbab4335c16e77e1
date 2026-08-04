"""Audit source-branch identity source-amendment/connection-values attack."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_sourcebranchidentity_sourceamendment_or_connectionvalues.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_sourcebranchidentity_sourceamendment_or_connectionvalues.candidate.json"
REQUEST = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_projectiverhoe_bn27_lift_or_directsource_theorem_request.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_sourcebranchidentity_sourceamendment_or_connectionvalues_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_SourceBranchIdentity_SourceAmendment_or_ConnectionValues_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_SOURCEBRANCHIDENTITY_REPAIR_ATTACK_PROJECTIVERHOE_PRIMARY_BN27_LIFT_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_ProjectiveRhoE_BN27Lift_or_DirectSourceTheorem_v1"


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
    request = load(REQUEST)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    attack = data["projective_attack"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("projective primary", decision["projective_rhoE_primary"] is True and data["lane_ranking"]["selected_connection_values_alternative"]["rank"] == 1, data["lane_ranking"])
    check("finite candidate available", attack["finite_candidate_available"] is True and all(attack["finite_values_inserted"].values()), attack)
    check("BN27 lift open", decision["projective_BN27_lift_closed"] is False and attack["closes_sourcebranch_identity_now"] is False, attack)
    check("request built", decision["next_request_built"] is True and request["status"] == "BN27_LIFT_OR_DIRECT_SOURCE_THEOREM_REQUIRED", request)
    check("request fields", set(request["must_emit"]) == {"domain_lift", "operator_lift", "source_identity", "audit_replay"}, request["must_emit"])
    check("no branch closure", decision["source_branch_identity_closed"] is False and cert["source_branch_identity_closed"] is False, cert)
    check("no export closure", decision["selected_connection_witness_export_closed"] is False and cert["selected_connection_witness_export_closed"] is False, cert)
    check("no logdet promotion", decision["oriented_logdet_promoted"] is False and cert["oriented_logdet_promoted"] is False, cert)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records request", NEXT in note and str(REQUEST.relative_to(ROOT)) in note and "projective_BN27_lift_closed = false" in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin source-branch identity source-amendment/connection-values audit passed")


if __name__ == "__main__":
    main()
