"""Audit oriented Phi_fin direct finite-response / projective-rhoE source-amendment gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_directfiniteresponse_or_projectiverhoe_sourceamendment.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_directfiniteresponse_or_projectiverhoe_sourceamendment.candidate.json"
CONTRACT = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_directfiniteresponse_source_contract.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_directfiniteresponse_or_projectiverhoe_sourceamendment_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_DirectFiniteResponse_or_ProjectiveRhoE_SourceAmendment_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_DIRECTFINITE_RESPONSE_CONTRACT_BUILT_VALUES_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_DirectFiniteResponse_FillAttempt_v1"


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
    contract = load(CONTRACT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    minimum = contract["minimum_payload"]
    internal = contract["candidate_sources_tested"]["internal_direct_candidate"]
    routec = contract["candidate_sources_tested"]["routec_direct_candidate"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("contract built", decision["direct_contract_built"] is True and contract["status"] == "VALUES_REQUIRED", contract)
    check("orientation support only", minimum["orientation_operator_Ctau_binding"] is True and minimum["no_double_count_replay"] is True, minimum)
    check("critical values open", minimum["same_branch_source_certificate"] is False and minimum["D_E_or_EQa_matrix_on_oriented_BN"] is False and minimum["finitepart_trace_identity_for_oriented_logdet"] is False, minimum)
    check("internal rejected", internal["source_emitted"] is True and internal["has_internal_finitepart"] is True and internal["can_close_oriented_27mode_response"] is False, internal)
    check("routec rejected", routec["source_emitted"] is True and routec["has_D_E_Riesz_Green_dotD"] is True and routec["can_close_oriented_heterotic_response"] is False, routec)
    check("no closure", decision["direct_same_source_finite_response_closed"] is False and decision["projective_rhoE_source_amendment_closed"] is False and decision["oriented_logdet_promoted"] is False, decision)
    check("guardrails", all(value is True for key, value in data["guardrails"].items() if key != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no overclaim", data["closure_claimed"] is False and cert["closure_claimed"] is False and data["target_fitting_used"] is False, cert)
    check("note records contract", str(CONTRACT.relative_to(ROOT)) in note and NEXT in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin direct finite-response/source-amendment audit")


if __name__ == "__main__":
    main()
