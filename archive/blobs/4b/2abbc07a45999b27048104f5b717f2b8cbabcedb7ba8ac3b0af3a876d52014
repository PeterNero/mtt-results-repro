"""Audit source-owned positive-operator / E_Qa payload fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_sourceownedpositiveoperator_or_eqapayload_fill.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_sourceownedpositiveoperator_or_eqapayload_fill.candidate.json"
PACKET = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_sourceownedpositiveoperator_or_eqapayload_minimal_source_packet.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_sourceownedpositiveoperator_or_eqapayload_fill_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_SourceOwnedPositiveOperator_or_EQaPayload_Fill_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_SOURCEOWNED_POSITIVE_OPERATOR_OR_EQA_PAYLOAD_FILL_VALUES_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_MinimalNewSourcePacket_Fill_or_ProofClosure_v1"


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
    direct = data["attempts"]["direct_source_owned_positive_operator"]
    smooth = data["attempts"]["smooth_EQa_payload"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("direct support retained", direct["same_branch_certificate"] is True and direct["orientation_binding"] is True and direct["table_D_E_Riesz_Green_positive_spectrum_materialized"] is True and direct["exact_finitepart_ready"] is True, direct)
    check("direct source values still open", direct["oriented_BN_carrier_emitted"] is False and direct["EndE_or_rhoE_operator_functor_or_quotient"] is False and direct["positive_PhiFin_magnitude_owned"] is False and direct["finitepart_trace_identity"] is False, direct)
    check("smooth support retained", smooth["standard_embedding_retired_for_current_branch"] is True and smooth["finite_internal_trace_policy_closed"] is True and smooth["R_plus_geometry_filled"] is True, smooth)
    check("smooth source values still open", smooth["selected_bundle_connection_A"] is False and smooth["bundle_curvature_F_A"] is False and smooth["E_Qa_matrix_or_equivalent_zero_order_block"] is False and smooth["trace_lift_or_complement_quotient_proof"] is False, smooth)
    check("minimal packet written", decision["minimal_source_packet_written"] is True and packet["status"] == "OPEN_SOURCE_VALUES_REQUIRED", packet)
    check("minimal packet exact value", packet["known_values"]["oriented_abs_sector_logdet_exact"] == "log(92160000)", packet["known_values"])
    check("two routes named", "route_A_direct_source_owned_positive_operator" in packet and "route_B_smooth_EQa_payload" in packet, packet)
    check("forbidden shortcuts retained", "declare the oriented 27-mode table source-owned by naming alone" in packet["forbidden_shortcuts"], packet["forbidden_shortcuts"])
    check("no promotion", decision["direct_source_owned_positive_operator_closed"] is False and decision["smooth_EQa_payload_closed"] is False and decision["oriented_logdet_promoted"] is False, decision)
    check("guardrails", all(value is True for key, value in data["guardrails"].items() if key != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no overclaim", data["closure_claimed"] is False and cert["closure_claimed"] is False and data["target_fitting_used"] is False, cert)
    check("note records packet", str(PACKET.relative_to(ROOT)) in note and NEXT in note and "log(92160000)" in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin source-owned positive-operator/EQa payload fill audit passed")


if __name__ == "__main__":
    main()
