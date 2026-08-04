"""Audit End(E)->B_N operator-intertwiner or smooth-connection source amendment."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_ende_to_bn_operatorintertwiner_or_smoothconnection_sourceamendment.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_ende_to_bn_operatorintertwiner_or_smoothconnection_sourceamendment.candidate.json"
PACKET = ROOT / "candidate_data" / "selected_heterotic_ende_to_bn_operatorintertwiner_required_packet.json"
CERT = ROOT / "certificates" / "selected_heterotic_ende_to_bn_operatorintertwiner_or_smoothconnection_sourceamendment_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_EndE_to_BN_OperatorIntertwiner_or_SmoothConnection_SourceAmendment_v1.md"

STATUS = "HETEROTIC_ENDE_TO_BN_OPERATORINTERTWINER_SOURCEAMENDMENT_BUILT_CENTRAL_OPERATOR_OPEN"
NEXT = "Selected_Heterotic_BN_CentralRankOperator_or_SmoothEQa_SourceEmission_v1"


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
    analysis = data["intertwiner_analysis"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS and packet["status"] == "OPEN_SOURCE_EMISSION_REQUIRED", (data["status"], cert["status"], packet["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("laplacian still fails", decision["selected_PhiFin_laplacian_intertwines"] is False and analysis["laplacian_D_E_intertwines"] is False, analysis)
    check("central operator works as candidate", decision["central_rank_operator_candidate_intertwines"] is True and analysis["central_rank_operator_C_tau"]["intertwines_on_embedding"] is True, analysis["central_rank_operator_C_tau"])
    check("source still open", decision["central_rank_operator_source_selected"] is False and packet["must_emit_to_close"]["source_selects_BN_central_rank_operator_C_tau"] is None, packet["must_emit_to_close"])
    check("operator identity not closed", decision["operator_identity_closed"] is False and decision["E_Qa_computed"] is False and decision["finitepart_regularization_same_scheme"] is False, decision)
    check("packet records known support", packet["already_built"]["phase_preserving_embedding_27x11"] is True and packet["already_built"]["central_rank_operator_candidate_intertwines"] is True, packet["already_built"])
    check("forbidden promotions", "replace selected Phi_fin Laplacian by C_tau without source emission" in packet["forbidden_promotions"], packet["forbidden_promotions"])
    check("guardrails", all(value is True for key, value in data["guardrails"].items() if key != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no closure overclaim", data["closure_claimed"] is False and cert["closure_claimed"] is False and packet["closure_claimed"] is False, cert)
    check("note records operator", NEXT in note and "C_tau" in note and str(PACKET.relative_to(ROOT)) in note, NOTE)

    print("\nSelected heterotic End(E)->B_N operator-intertwiner source-amendment audit")


if __name__ == "__main__":
    main()
