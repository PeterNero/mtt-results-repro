"""Audit direct BN27 source-identity transport fill or typed connection values."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_directbn27_sourceidentitytransport_fill_or_typedconnectionwitnessvalues.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_directbn27_sourceidentitytransport_fill_or_typedconnectionwitnessvalues.candidate.json"
CONTRACT = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_directbn27_sourceidentitytransport_acceptance_contract.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_directbn27_sourceidentitytransport_fill_or_typedconnectionwitnessvalues_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_DirectBN27_SourceIdentityTransport_Fill_or_TypedConnectionWitnessValues_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_DIRECTBN27_SOURCEIDENTITY_FILL_DE_GAP_IMPORTED_TRANSPORT_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_SourceIdentity_DirectSourceTheorem_or_ConnectionValuesExternalConstruction_v1"


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
    support = data["new_support_imported"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("DE support imported", all(support.values()) and decision["DE_gap_Riesz_Green_export_support_closed"] is True, support)
    check("direct source identity still open", decision["source_object_named_S_QaSU3_BN27"] is False and decision["direct_source_identity_transport_closed"] is False, decision)
    check("typed values still open", decision["typed_connection_witness_values_found"] is False and data["lane_evaluation"]["typed_connection_witness_values"]["closed_now"] is False, data["lane_evaluation"]["typed_connection_witness_values"])
    check("finite routec not full connection", decision["finite_routec_hym_full_connection_closed"] is False and data["lane_evaluation"]["finite_routec_hym_solve"]["support_promoted_for_gap_layer"] is True, data["lane_evaluation"]["finite_routec_hym_solve"])
    check("no transport closure", decision["BN27_source_ownership_transport_closed"] is False and decision["selected_connection_witness_export_closed"] is False and data["closure_claimed"] is False, decision)
    check("no logdet promotion", decision["oriented_logdet_promoted"] is False and cert["oriented_logdet_promoted"] is False, cert)
    check("contract has direct source payload", set(contract["direct_source_identity_payload"].keys()) == {
        "source_object_named_S_QaSU3_BN27",
        "full_F3xF3_rank_slot_carrier_emitted_before_finite_comparison",
        "C_tau_and_PhiFin_DE_coemitted_by_source",
        "RouteC_q79_row_internal_to_source_not_imported",
        "kernel_shared_circle_policy_source_owned",
        "finitepart_log92160000_identity_source_owned",
        "theorem_derived_selected_source_flags",
    }, contract["direct_source_identity_payload"])
    check("contract has connection payload", set(contract["typed_or_connection_payload"].keys()) == {
        "typed_f_sections",
        "typed_g_sections",
        "cech_transitions_and_cocycles",
        "g_after_f_zero_and_exactness_certificate",
        "selected_HYM_or_projective_connection_coefficients",
        "residual_bounds_or_exact_connection_equations",
        "BN27_operator_export_to_DE_Riesz_Green_kernel_trace",
        "no_lifted_flags_replay_audit",
    }, contract["typed_or_connection_payload"])
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records contract", NEXT in note and str(CONTRACT.relative_to(ROOT)) in note and "DE_gap_Riesz_Green_export_support_closed = true" in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin direct BN27 source-identity fill / typed connection values audit passed")


if __name__ == "__main__":
    main()
