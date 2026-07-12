"""Audit terminal finite cochain connection-table promotion."""

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
BUILDER = ROOT / "scripts" / "build_selected_terminalfinitecochain_connectiontablepromotion_or_fulldevalues.py"

SLUG = "selected_terminalfinitecochain_connectiontablepromotion_or_fulldevalues"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_TerminalFiniteCochain_ConnectionTablePromotion_or_FullDEValues_v1.md"
FINITE_PACKET = PACKET_DIR / "terminal_finite_cochain_connection_packet.packet.json"
REVALIDATION_PACKET = PACKET_DIR / "eight_connection_table_revalidation_after_selector.packet.json"
NEXT_PACKET = PACKET_DIR / "next_remaining_connection_tables_contract.packet.json"

STATUS = (
    "MTT_SELECTED_TERMINALFINITECOCHAIN_CONNECTIONTABLEPROMOTION_OR_FULLDEVALUES_"
    "THREE_OF_EIGHT_TABLES_ACCEPTED_REMAINING_FIVE_OPEN"
)
NEXT = "MTT_Selected_RemainingCechHYMDEConnectionTables_or_DirectHKRow_v1"
ACCEPTED = [
    "typed_f_sections",
    "typed_g_sections",
    "g_after_f_zero_exactness_certificate",
]
REMAINING = [
    "cech_transition_cocycles",
    "selected_HYM_or_projective_connection_coefficients",
    "BN27_DE_Riesz_Green_kernel_trace_export",
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
    finite = load(FINITE_PACKET)
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

    for payload in [candidate, cert, finite, revalidation, next_packet]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    require(finite["status"] == "SELECTED_TERMINAL_FINITE_COCHAIN_PACKET_EMITTED_FOR_SCALAR_TABLE_ROWS", "finite packet status")
    require(len(finite["selected_bases"]) == 11, "basis count mismatch")
    require(len(finite["f_sections"]) == 5, "f sections count")
    require(len(finite["g_sections"]) == 5, "g sections count")
    require(len(finite["product_tables"]) == 5, "product table count")
    require(finite["monad_exactness"]["gf_terms"] == [1, 1, 1, 1, -4], "gf terms")
    require(finite["monad_exactness"]["gf_sum"] == 0, "gf sum")
    require(finite["monad_exactness"]["gf_zero_exact"] is True, "gf zero")
    promotions = finite["finite_gate_promotions"]
    for key in [
        "selected_finite_basis_for_each_space",
        "selected_product_tables",
        "selected_map_entries",
        "post_selection_monad_check",
        "selected_differentials",
    ]:
        require(promotions[key] is True, f"finite promotion missing: {key}")
    for key in ["same_source_bridge_to_full_operator", "admissibility_retention_full_smooth"]:
        require(promotions[key] is False, f"finite packet overclaim: {key}")

    require(revalidation["previous_accepted_count"] == 0, "previous count should be zero")
    require(revalidation["accepted_final_same_source_connection_tables"] == 3, "accepted count mismatch")
    require(revalidation["required_final_same_source_connection_tables"] == 8, "required count mismatch")
    require(revalidation["accepted_rows"] == ACCEPTED, "accepted rows mismatch")
    require(revalidation["remaining_rows"] == REMAINING, "remaining rows mismatch")
    for row in ACCEPTED:
        require(revalidation["rows"][row]["accepted_as_final_connection_table"] is True, f"row not accepted: {row}")
    for row in REMAINING:
        require(revalidation["rows"][row]["accepted_as_final_connection_table"] is False, f"row overaccepted: {row}")

    decision = candidate["closure_decision"]
    require(decision["terminal_finite_cochain_packet_emitted"] is True, "cochain packet not emitted")
    require(decision["accepted_final_same_source_connection_tables"] == 3, "decision accepted count")
    require(decision["required_final_same_source_connection_tables"] == 8, "decision required count")
    require(decision["accepted_rows"] == ACCEPTED, "decision accepted rows")
    require(decision["remaining_rows"] == REMAINING, "decision remaining rows")
    require(decision["g_after_f_zero_exact"] is True, "decision gf exact")
    for key in [
        "smooth_cech_representative_emitted",
        "selected_hym_connection_coefficients_emitted",
        "full_same_source_DE_operator_values_selected",
        "BN27_logdet_no_lift_unconditional_from_final_rows",
        "direct_H_K_row_emitted",
        "strict_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"decision overclaim: {key}")
        require(cert[key] is False, f"cert overclaim: {key}")

    require(next_packet["current_count"] == "3/8", "next current count")
    require(next_packet["closed_rows"] == ACCEPTED, "next closed rows")
    require(next_packet["remaining_rows"] == REMAINING, "next remaining rows")

    require("Previous final table count: `0/8`" in note, "note missing previous count")
    require("New final table count: `3/8`" in note, "note missing new count")
    require(NEXT in note, "note missing next artifact")

    print("Terminal finite cochain connection-table promotion audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
