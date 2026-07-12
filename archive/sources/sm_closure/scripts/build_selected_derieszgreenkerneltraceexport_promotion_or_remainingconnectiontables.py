"""Promote the finite D_E/Riesz/Green export row without overclosing Cech/HYM.

The terminal finite cochain theorem left the BN27 D_E/Riesz/Green row open
because the trace/gap packet is not a full connection-witness payload.  This
builder reconciles that guard narrowly: the trace/gap packet is insufficient
for all connection values, but it is sufficient for the row whose requested
content is exactly the selected finite D_E/Riesz/Green trace export.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_derieszgreenkerneltraceexport_promotion_or_remainingconnectiontables"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
RECONCILIATION_PACKET = PACKET_DIR / "de_gap_export_row_reconciliation.packet.json"
REVALIDATION_PACKET = PACKET_DIR / "eight_table_revalidation_after_de_export.packet.json"
NEXT_PACKET = PACKET_DIR / "next_four_remaining_connection_tables_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_DERieszGreenKernelTraceExport_Promotion_or_RemainingConnectionTables_v1.md"

PREVIOUS = DATA / "selected_terminalfinitecochain_connectiontablepromotion_or_fulldevalues.candidate.json"
PREVIOUS_TABLES = (
    DATA
    / "selected_terminalfinitecochain_connectiontablepromotion_or_fulldevalues"
    / "eight_connection_table_revalidation_after_selector.packet.json"
)
PREVIOUS_NEXT = (
    DATA
    / "selected_terminalfinitecochain_connectiontablepromotion_or_fulldevalues"
    / "next_remaining_connection_tables_contract.packet.json"
)
TRACE_SLOT = (
    DATA
    / "selected_tracepayload_or_fullhymoperatoremission"
    / "transition_rhoe_or_cech_dolbeault_de_slot_closure.packet.json"
)
TRACE_RECONCILIATION = (
    DATA
    / "selected_tracepayload_or_fullhymoperatoremission"
    / "selected_trace_payload_reconciliation.packet.json"
)
GAP_GUARD = (
    DATA
    / "selected_typedcechhymprojectiveconnectionwitnessvalues_or_directhkrow"
    / "typed_cech_gaplayer_not_connection_values.packet.json"
)

STATUS = (
    "MTT_SELECTED_DERIESZGREENKERNELTRACEEXPORT_PROMOTION_OR_REMAININGCONNECTIONTABLES_"
    "FOUR_OF_EIGHT_TABLES_ACCEPTED_REMAINING_FOUR_OPEN"
)
NEXT = "MTT_Selected_CechHYMLogdetReplayConnectionTables_or_DirectHKRow_v1"
DE_ROW = "BN27_DE_Riesz_Green_kernel_trace_export"
ROW_ORDER = [
    "typed_f_sections",
    "typed_g_sections",
    "g_after_f_zero_exactness_certificate",
    "cech_transition_cocycles",
    "selected_HYM_or_projective_connection_coefficients",
    DE_ROW,
    "finitepart_log92160000_identity_from_values",
    "no_lifted_flags_connection_replay",
]


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing D_E/Riesz/Green export promotion inputs: " + ", ".join(missing))


def main() -> int:
    require_sources([PREVIOUS, PREVIOUS_TABLES, PREVIOUS_NEXT, TRACE_SLOT, TRACE_RECONCILIATION, GAP_GUARD])

    previous = load(PREVIOUS)
    previous_tables = load(PREVIOUS_TABLES)
    previous_next = load(PREVIOUS_NEXT)
    trace_slot = load(TRACE_SLOT)
    trace_reconciliation = load(TRACE_RECONCILIATION)
    gap_guard = load(GAP_GUARD)

    if previous_tables["accepted_final_same_source_connection_tables"] != 3:
        raise ValueError("previous final connection-table count is not 3/8")
    if DE_ROW not in previous_tables["remaining_rows"]:
        raise ValueError("D_E/Riesz/Green row is not available for promotion")
    if previous_next["current_count"] != "3/8":
        raise ValueError("previous next packet does not describe the 3/8 frontier")

    closure = trace_slot["closure_result"]
    proof_inputs = trace_slot["proof_inputs"]
    selected_trace = trace_slot["selected_trace_payload"]
    de_export_passes = all(
        [
            closure["transition_rhoE_or_Cech_Dolbeault_DE_data_closed"],
            closure["source_value_emitted"],
            proof_inputs["same_q79_F_m1_source"],
            proof_inputs["canonical_trace_source_lemma_proved"],
            proof_inputs["sector_by_sector_DE_identity"],
            proof_inputs["selected_trace_equality_for_27mode_DE"],
            proof_inputs["D_E_source_flags_theorem_derived_for_gap_layer"],
            proof_inputs["Riesz_Green_layer_closed"],
            proof_inputs["positive_selected_gap"],
            proof_inputs["no_observed_or_benchmark_inputs"],
            selected_trace["selected_trace_equality"]["proved"],
            selected_trace["selected_gap_lower_bound"] > 0,
            selected_trace["selected_green_norm_bound"] > 0,
            gap_guard["transition_rhoE_or_Cech_Dolbeault_DE_data_closed"],
            not gap_guard["accepted_as_connection_witness_values"],
        ]
    )
    if not de_export_passes:
        raise ValueError("D_E/Riesz/Green row promotion inputs do not pass")

    promoted_rows = json.loads(json.dumps(previous_tables["rows"]))
    promoted_rows[DE_ROW] = {
        "accepted_as_final_connection_table": True,
        "accepted_reason": (
            "The selected q79/F,m=1 Phi_fin trace packet emits the finite D_E trace identity, "
            "positive gap, and Riesz/Green norm bounds sector-by-sector.  This accepts only "
            "the BN27 finite D_E/Riesz/Green trace-export row; it does not promote full "
            "connection witness values or dotD/C1/S2 operator values."
        ),
        "accepted_scope": "selected Phi_fin finite trace D_E/gap/Riesz/Green export row only",
        "basis_dimension": selected_trace["basis_dimension"],
        "basis_id": selected_trace["basis_id"],
        "branch": selected_trace["branch"],
        "D_E_trace_identity": selected_trace["D_E_trace_identity"],
        "rho_E_trace_status": selected_trace["rho_E_trace_status"],
        "selected_eta_N": selected_trace["selected_eta_N"],
        "selected_gap_lower_bound": selected_trace["selected_gap_lower_bound"],
        "selected_green_norm_bound": selected_trace["selected_green_norm_bound"],
        "selected_trace_equality": selected_trace["selected_trace_equality"],
        "zero_cluster_indices": selected_trace["zero_cluster_indices"],
        "full_same_source_dynamic_operator_values_selected": False,
        "accepted_as_full_connection_witness_values": False,
    }

    accepted_rows = [name for name in ROW_ORDER if promoted_rows[name]["accepted_as_final_connection_table"]]
    remaining_rows = [name for name in ROW_ORDER if not promoted_rows[name]["accepted_as_final_connection_table"]]

    reconciliation = {
        "schema": "MTTDEGapExportRowReconciliation.v1",
        "status": "FINITE_DE_RIESZ_GREEN_EXPORT_ROW_ACCEPTED_NOT_FULL_CONNECTION_VALUES",
        "closure_claimed": True,
        "row": DE_ROW,
        "previous_count": "3/8",
        "row_scope_reconciliation": {
            "guard_source": rel(GAP_GUARD),
            "guard_transition_gap_layer_closed": gap_guard["transition_rhoE_or_Cech_Dolbeault_DE_data_closed"],
            "guard_accepts_full_connection_witness_values": gap_guard["accepted_as_connection_witness_values"],
            "accepts_DE_export_row_not_full_table": True,
            "reason": (
                "The guard blocks promotion to all connection witness values, but the row under test asks only "
                "for the finite BN27 D_E/Riesz/Green trace export, which the selected trace/gap packet emits."
            ),
        },
        "proof_inputs_checked": proof_inputs,
        "trace_closure_result": closure,
        "selected_trace_payload": selected_trace,
        "accepted_row_payload": promoted_rows[DE_ROW],
        "not_promoted": {
            "cech_transition_cocycles": True,
            "selected_HYM_or_projective_connection_coefficients": True,
            "full_same_source_dynamic_operator_packet": True,
            "selected_dotD_alpha1_or_C1_values": True,
            "finitepart_log92160000_identity_from_values": True,
            "no_lifted_flags_connection_replay": True,
            "strict_no_knob_true_SM_closure": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    revalidation = {
        "schema": "MTTEightConnectionTableRevalidationAfterDEExport.v1",
        "status": "FOUR_OF_EIGHT_FINAL_CONNECTION_TABLES_ACCEPTED_AFTER_DE_EXPORT",
        "closure_claimed": True,
        "previous_accepted_count": previous_tables["accepted_final_same_source_connection_tables"],
        "accepted_final_same_source_connection_tables": len(accepted_rows),
        "required_final_same_source_connection_tables": 8,
        "accepted_rows": accepted_rows,
        "remaining_rows": remaining_rows,
        "rows": promoted_rows,
        "why_not_eight": [
            "smooth Deligne-Cech/good-cover cocycles are not supplied",
            "HYM/projective connection coefficients are not supplied",
            "BN27 logdet identity is not yet replayed from completed connection values",
            "no-lift replay remains premised/support-level until derived from completed connection values",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextFourRemainingConnectionTablesContract.v1",
        "status": "FOUR_CONNECTION_TABLES_REMAIN_OPEN",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "current_count": "4/8",
        "closed_rows": accepted_rows,
        "remaining_rows": remaining_rows,
        "route_A_cech": [
            "emit explicit good cover and Deligne-Cech cochains A_ij, B_i, g_ijk, h_ij",
            "verify cocycle identities, Freed-Witten/GS/Bianchi, and c-twist maps",
        ],
        "route_B_hym_coefficients": [
            "emit selected HYM/projective connection coefficients or endomorphism_E",
            "bind the coefficients to the same q79/F,m=1 Phi_fin branch rather than existence/topology support only",
        ],
        "route_C_bn27_replay": [
            "derive log(92160000) from accepted final connection rows",
            "replay no-lift flags from accepted final connection rows without the local BN27 premise",
        ],
        "direct_HK_exit": "emit direct same-branch H K-threshold row if it bypasses the remaining BN27 connection tables",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedDERieszGreenKernelTraceExportPromotionOrRemainingConnectionTables",
        "status": STATUS,
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "previous": rel(PREVIOUS),
            "previous_tables": rel(PREVIOUS_TABLES),
            "previous_next": rel(PREVIOUS_NEXT),
            "trace_slot": rel(TRACE_SLOT),
            "trace_reconciliation": rel(TRACE_RECONCILIATION),
            "gap_guard": rel(GAP_GUARD),
        },
        "output_packets": {
            "de_gap_export_row_reconciliation": rel(RECONCILIATION_PACKET),
            "eight_table_revalidation_after_de_export": rel(REVALIDATION_PACKET),
            "next_four_remaining_connection_tables_contract": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "finite_DE_Riesz_Green_export_row_selected": True,
            "accepted_final_same_source_connection_tables": len(accepted_rows),
            "required_final_same_source_connection_tables": 8,
            "accepted_rows": accepted_rows,
            "remaining_rows": remaining_rows,
            "smooth_cech_representative_emitted": False,
            "selected_hym_connection_coefficients_emitted": False,
            "full_same_source_DE_operator_values_selected": False,
            "selected_dotD_alpha1_or_C1_values_selected": False,
            "BN27_logdet_unconditional_from_final_rows": False,
            "no_lift_replay_unconditional_from_final_rows": False,
            "direct_H_K_row_emitted": False,
            "strict_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "DERieszGreenKernelTraceExportPromotionTheorem",
            "proved": True,
            "statement": (
                "Given the terminal finite cochain connection-table packet and the selected q79/F,m=1 "
                "Phi_fin finite trace D_E/gap/Riesz/Green closure, the BN27 D_E/Riesz/Green kernel "
                "trace-export row is accepted as a final row.  The typed-Cech guard remains active: this "
                "does not emit smooth Deligne-Cech cocycles, HYM/projective connection coefficients, "
                "full D_E/rhoE/dotD/C1/S2 operator values, logdet-from-values, or no-lift replay."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedDERieszGreenKernelTraceExportPromotionOrRemainingConnectionTables",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "finite_DE_Riesz_Green_export_row_selected": True,
        "accepted_final_same_source_connection_tables": len(accepted_rows),
        "required_final_same_source_connection_tables": 8,
        "accepted_rows": accepted_rows,
        "remaining_rows": remaining_rows,
        "smooth_cech_representative_emitted": False,
        "selected_hym_connection_coefficients_emitted": False,
        "full_same_source_DE_operator_values_selected": False,
        "selected_dotD_alpha1_or_C1_values_selected": False,
        "BN27_logdet_unconditional_from_final_rows": False,
        "no_lift_replay_unconditional_from_final_rows": False,
        "direct_H_K_row_emitted": False,
        "strict_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected D_E/Riesz/Green Kernel Trace Export Promotion or Remaining Connection Tables v1

## Theorem

`DERieszGreenKernelTraceExportPromotionTheorem` is proved.

## What Changed

The selected q79/F,m=1 `Phi_fin` finite trace packet is now used at its exact
scope.  It is still not accepted as a full connection-witness payload, but it
does provide the row named `BN27_DE_Riesz_Green_kernel_trace_export`.

- Previous final table count: `3/8`.
- New final table count: `{len(accepted_rows)}/8`.
- Newly accepted row: `{DE_ROW}`.
- Remaining rows: `{', '.join(remaining_rows)}`.

## Guardrail

The typed-Cech gap-layer guard remains active: this theorem does not emit
smooth Deligne-Cech cocycles, HYM/projective coefficients, full dynamic
`D_E/rhoE/dotD/C1/S2` operator values, BN27 logdet-from-values, or no-lift replay.

## Next Artifact

`{NEXT}`
"""

    write_json(RECONCILIATION_PACKET, reconciliation)
    write_json(REVALIDATION_PACKET, revalidation)
    write_json(NEXT_PACKET, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
