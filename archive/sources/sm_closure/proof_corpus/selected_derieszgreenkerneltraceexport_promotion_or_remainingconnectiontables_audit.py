"""Audit the narrow D_E/Riesz/Green export-row promotion."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
BUILDER = ROOT / "scripts" / "build_selected_derieszgreenkerneltraceexport_promotion_or_remainingconnectiontables.py"

SLUG = "selected_derieszgreenkerneltraceexport_promotion_or_remainingconnectiontables"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_DERieszGreenKernelTraceExport_Promotion_or_RemainingConnectionTables_v1.md"
RECONCILIATION_PACKET = PACKET_DIR / "de_gap_export_row_reconciliation.packet.json"
REVALIDATION_PACKET = PACKET_DIR / "eight_table_revalidation_after_de_export.packet.json"
NEXT_PACKET = PACKET_DIR / "next_four_remaining_connection_tables_contract.packet.json"

STATUS = (
    "MTT_SELECTED_DERIESZGREENKERNELTRACEEXPORT_PROMOTION_OR_REMAININGCONNECTIONTABLES_"
    "FOUR_OF_EIGHT_TABLES_ACCEPTED_REMAINING_FOUR_OPEN"
)
NEXT = "MTT_Selected_CechHYMLogdetReplayConnectionTables_or_DirectHKRow_v1"
ACCEPTED = [
    "typed_f_sections",
    "typed_g_sections",
    "g_after_f_zero_exactness_certificate",
    "BN27_DE_Riesz_Green_kernel_trace_export",
]
REMAINING = [
    "cech_transition_cocycles",
    "selected_HYM_or_projective_connection_coefficients",
    "finitepart_log92160000_identity_from_values",
    "no_lifted_flags_connection_replay",
]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    reconciliation = load(RECONCILIATION_PACKET)
    revalidation = load(REVALIDATION_PACKET)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(next_packet["next_required_artifact"] == NEXT, "next packet mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")

    for payload in [candidate, cert, reconciliation, revalidation, next_packet]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    row_scope = reconciliation["row_scope_reconciliation"]
    require(row_scope["guard_transition_gap_layer_closed"] is True, "gap layer guard should be closed")
    require(row_scope["guard_accepts_full_connection_witness_values"] is False, "guard overaccepted")
    require(row_scope["accepts_DE_export_row_not_full_table"] is True, "row-scope reconciliation missing")

    closure = reconciliation["trace_closure_result"]
    require(closure["transition_rhoE_or_Cech_Dolbeault_DE_data_closed"] is True, "transition trace closure missing")
    require(closure["source_value_emitted"] is True, "source value not emitted")
    for key in [
        "actual_dynamic_QaSU3_operator_packet_closed",
        "determinant_torsion_slot_closed",
        "full_S2_value_emission_closed",
        "selected_dotD_alpha1_source_identity_closed",
    ]:
        require(closure[key] is False, f"trace closure overclaim: {key}")

    proof_inputs = reconciliation["proof_inputs_checked"]
    for key in [
        "same_q79_F_m1_source",
        "canonical_trace_source_lemma_proved",
        "sector_by_sector_DE_identity",
        "selected_trace_equality_for_27mode_DE",
        "D_E_source_flags_theorem_derived_for_gap_layer",
        "Riesz_Green_layer_closed",
        "positive_selected_gap",
        "no_observed_or_benchmark_inputs",
    ]:
        require(proof_inputs[key] is True, f"missing proof input: {key}")

    accepted_payload = reconciliation["accepted_row_payload"]
    require(accepted_payload["accepted_as_final_connection_table"] is True, "DE row not accepted")
    require(accepted_payload["basis_dimension"] == 27, "basis dimension mismatch")
    require(accepted_payload["branch"] == {"orientation": "F", "q": 79, "torsion_label_m": 1}, "branch mismatch")
    require(accepted_payload["selected_trace_equality"]["proved"] is True, "trace equality not proved")
    require(accepted_payload["selected_gap_lower_bound"] > 0, "gap not positive")
    require(accepted_payload["selected_green_norm_bound"] > 0, "green bound not positive")
    require(accepted_payload["full_same_source_dynamic_operator_values_selected"] is False, "dynamic values overaccepted")
    require(accepted_payload["accepted_as_full_connection_witness_values"] is False, "connection witness overaccepted")

    for key, value in reconciliation["not_promoted"].items():
        require(value is True, f"not-promoted guard missing: {key}")

    require(revalidation["previous_accepted_count"] == 3, "previous accepted count")
    require(revalidation["accepted_final_same_source_connection_tables"] == 4, "accepted count mismatch")
    require(revalidation["required_final_same_source_connection_tables"] == 8, "required count mismatch")
    require(revalidation["accepted_rows"] == ACCEPTED, "accepted rows mismatch")
    require(revalidation["remaining_rows"] == REMAINING, "remaining rows mismatch")
    for row in ACCEPTED:
        require(revalidation["rows"][row]["accepted_as_final_connection_table"] is True, f"row not accepted: {row}")
    for row in REMAINING:
        require(revalidation["rows"][row]["accepted_as_final_connection_table"] is False, f"row overaccepted: {row}")

    decision = candidate["closure_decision"]
    require(decision["finite_DE_Riesz_Green_export_row_selected"] is True, "decision DE row missing")
    require(decision["accepted_final_same_source_connection_tables"] == 4, "decision accepted count")
    require(decision["required_final_same_source_connection_tables"] == 8, "decision required count")
    require(decision["accepted_rows"] == ACCEPTED, "decision accepted rows")
    require(decision["remaining_rows"] == REMAINING, "decision remaining rows")
    for key in [
        "smooth_cech_representative_emitted",
        "selected_hym_connection_coefficients_emitted",
        "full_same_source_DE_operator_values_selected",
        "selected_dotD_alpha1_or_C1_values_selected",
        "BN27_logdet_unconditional_from_final_rows",
        "no_lift_replay_unconditional_from_final_rows",
        "direct_H_K_row_emitted",
        "strict_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"decision overclaim: {key}")
        require(cert[key] is False, f"cert overclaim: {key}")

    require(next_packet["current_count"] == "4/8", "next current count")
    require(next_packet["closed_rows"] == ACCEPTED, "next closed rows")
    require(next_packet["remaining_rows"] == REMAINING, "next remaining rows")

    require("Previous final table count: `3/8`" in note, "note missing previous count")
    require("New final table count: `4/8`" in note, "note missing new count")
    require(NEXT in note, "note missing next artifact")

    print("D_E/Riesz/Green export-row promotion audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
