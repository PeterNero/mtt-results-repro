"""Audit End(E)->B_N label embedding or smooth transition/connection value packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_ende_to_bn_labelembedding_or_smoothtransitionconnection_valuepacket.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_ende_to_bn_labelembedding_or_smoothtransitionconnection_valuepacket.candidate.json"
VALUES = ROOT / "candidate_data" / "selected_heterotic_ende_to_bn_labelembedding_candidate_values.json"
CERT = ROOT / "certificates" / "selected_heterotic_ende_to_bn_labelembedding_or_smoothtransitionconnection_valuepacket_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_EndE_to_BN_LabelEmbedding_or_SmoothTransitionConnection_ValuePacket_v1.md"

STATUS = "HETEROTIC_ENDE_TO_BN_LABELEMBEDDING_ATTEMPT_RHOE_INTERTWINES_DE_FINITEPART_OPEN"
NEXT = "Selected_Heterotic_EndE_to_BN_OperatorIntertwiner_or_SmoothConnection_SourceAmendment_v1"


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
    values = load(VALUES)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS and values["status"] == "CANDIDATE_VALUES_BUILT_RHOE_ONLY_NOT_OPERATOR_INTERTWINER", (data["status"], cert["status"], values["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("matrix shape", values["projection_pair_checks"]["matrix_shape"] == [27, 11] and len(values["embedding_matrix_27x11"]) == 27 and len(values["embedding_matrix_27x11"][0]) == 11, values["projection_pair_checks"])
    check("injection valid", values["projection_pair_checks"]["unique_rows"] is True and values["projection_pair_checks"]["P_transpose_P_equals_identity_11"] is True, values["projection_pair_checks"])
    check("rhoE intertwines", decision["rhoE_character_intertwines"] is True and values["rho_checks"]["all_labels_preserve_tau_mod3_rank_slot"] is True, values["rho_checks"])
    check("products retained", values["rho_checks"]["product_cancellation_retained"] is True and values["rho_checks"]["triple_tau_shadow_retained"] is True, values["rho_checks"])
    check("DE does not intertwine", decision["D_E_or_EQa_intertwines"] is False and values["D_E_intertwiner_checks"]["intertwines"] is False, values["D_E_intertwiner_checks"])
    check("finite part not same", decision["finitepart_regularization_same_scheme"] is False and values["finitepart_checks"]["same_finitepart"] is False, values["finitepart_checks"])
    check("smooth lane open", decision["smooth_transition_connection_values_emitted"] is False and data["smooth_transition_connection_lane"]["attempted"] is False, data["smooth_transition_connection_lane"])
    check("no closure", data["closure_claimed"] is False and cert["closure_claimed"] is False and decision["closure_claimed"] is False, cert)
    check("guardrails", all(value is True for key, value in data["guardrails"].items() if key != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records rho only", NEXT in note and "rho_E" in note and "D_E_or_EQa_intertwines = false" in note, NOTE)

    print("\nSelected heterotic End(E)->B_N label-embedding value-packet audit")


if __name__ == "__main__":
    main()
