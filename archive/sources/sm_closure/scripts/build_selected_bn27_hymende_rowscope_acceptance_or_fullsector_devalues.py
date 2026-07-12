"""Resolve the BN27 HYM/End(E) row-scope fork.

The previous artifact left two legal routes:

* Route A: prove the BN27 final HYM/End(E) row accepts the row-scope
  diagonal/projective End(E) representative already imported from Step38-40.
* Route B: emit the full-sector validator payload.

This builder executes Route A against the existing validators.  Route A is
rejected: the selected projective rho_E plus diagonal End0 D_E/Riesz/Green/dotD
representative is real row-scope support, but the BN27 connection row still
requires sector transfer, full-sector D_E/projector data, offdiagonal control,
and a final acceptance certificate.

It then reduces Route B by importing the already closed Step38-40 and
active-ledger fields, so the remaining full-sector payload is smaller and
non-looping.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_bn27_hymende_rowscope_acceptance_or_fullsector_devalues"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_A_PACKET = PACKET_DIR / "route_a_rowscope_sufficiency_rejection.packet.json"
ROUTE_B_PACKET = PACKET_DIR / "route_b_reduced_fullsector_validator_payload.packet.json"
GATE_PACKET = PACKET_DIR / "bn27_hymende_final_row_gate_after_rowscope_test.packet.json"
NEXT_PACKET = PACKET_DIR / "next_fullsector_bn27_hymende_validator_payload_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_BN27_HYMEndE_RowScopeAcceptance_or_FullSectorDEValues_v1.md"

PREVIOUS = DATA / "selected_operatorsector_hymende_backimport_after_step40_or_fullsector_guard.candidate.json"
PREVIOUS_REMAINING = (
    DATA
    / "selected_operatorsector_hymende_backimport_after_step40_or_fullsector_guard"
    / "remaining_fullsector_or_rowscope_sufficiency_cutset.packet.json"
)
PREVIOUS_CONTRACT = (
    DATA
    / "selected_operatorsector_hymende_backimport_after_step40_or_fullsector_guard"
    / "next_bn27_hymende_rowscope_or_fullsector_contract.packet.json"
)
EIGHT_TABLE = (
    DATA
    / "selected_derieszgreenkerneltraceexport_promotion_or_remainingconnectiontables"
    / "eight_table_revalidation_after_de_export.packet.json"
)
FIRST_FIELD = DATA / "selected_firstsamesourceconnectionfieldemission_or_directhkrow.candidate.json"
FIRST_FIELD_SCAN = (
    DATA / "selected_firstsamesourceconnectionfieldemission_or_directhkrow" / "first_field_candidate_scan.packet.json"
)
STEP38 = DATA / "selected_step38_finiteheisenberg_rhoe_promotion_or_deoperatorfrontier.candidate.json"
STEP39 = DATA / "selected_step39_diagonalend0_covariantde_import_or_fullsectorfrontier.candidate.json"
STEP40 = DATA / "selected_step40_dotdtransport_alpha1import_or_primitivec1frontier.candidate.json"
ACTIVE_LEDGER = DATA / "selected_activeledger_dotdc1supersession_or_valuelayerfrontier.candidate.json"
FULLSECTOR = DATA / "selected_fullsectorhymoperatorpayload_or_deltas2rowemission.candidate.json"
FULLSECTOR_LEDGER = (
    DATA / "selected_fullsectorhymoperatorpayload_or_deltas2rowemission" / "fullsector_hym_payload_field_ledger.packet.json"
)

STATUS = (
    "MTT_SELECTED_BN27_HYMENDE_ROWSCOPE_ACCEPTANCE_REJECTED_"
    "FULLSECTOR_PAYLOAD_REDUCED"
)
NEXT = "MTT_Selected_FullSectorBN27HYMEndEValidatorPayload_v1"
FINAL_ROW = "selected_HYM_or_projective_connection_coefficients"


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
        raise FileNotFoundError("missing BN27 HYM/End(E) row-scope inputs: " + ", ".join(missing))


def main() -> int:
    sources = [
        PREVIOUS,
        PREVIOUS_REMAINING,
        PREVIOUS_CONTRACT,
        EIGHT_TABLE,
        FIRST_FIELD,
        FIRST_FIELD_SCAN,
        STEP38,
        STEP39,
        STEP40,
        ACTIVE_LEDGER,
        FULLSECTOR,
        FULLSECTOR_LEDGER,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_remaining = load(PREVIOUS_REMAINING)
    previous_contract = load(PREVIOUS_CONTRACT)
    eight = load(EIGHT_TABLE)
    first = load(FIRST_FIELD)
    first_scan = load(FIRST_FIELD_SCAN)
    step38 = load(STEP38)
    step39 = load(STEP39)
    step40 = load(STEP40)
    active = load(ACTIVE_LEDGER)
    fullsector = load(FULLSECTOR)
    fullsector_ledger = load(FULLSECTOR_LEDGER)

    if previous["next_required_artifact"] != "MTT_Selected_BN27HYMEndERowScopeAcceptance_or_FullSectorDEValues_v1":
        raise ValueError("previous artifact no longer points to row-scope/full-sector fork")
    if previous_contract["next_required_artifact"] != "MTT_Selected_BN27HYMEndERowScopeAcceptance_or_FullSectorDEValues_v1":
        raise ValueError("previous contract no longer points to row-scope/full-sector fork")
    if previous["closure_decision"]["row_scope_diagonal_projective_EndE_representative_available"] is not True:
        raise ValueError("row-scope representative is not available")
    if previous["closure_decision"]["HYM_or_EndE_final_row_accepted"]:
        raise ValueError("previous packet already accepted the final row")

    hym_row = eight["rows"][FINAL_ROW]
    first_decision = first["closure_decision"]

    route_a_rejected = (
        hym_row["accepted_as_final_connection_table"] is False
        and first_scan["accepted_transition_or_connection_representative"] is False
        and first_decision["rtheta_diagonal_HYM_promoted_to_BN27_field"] is False
        and first_decision["rank2_to_sector_transfer_closed"] is False
        and first_decision["actual_QaSU3_operator_packet_promoted"] is False
        and first_decision["selected_connection_witness_values_absent"] is True
    )
    if not route_a_rejected:
        raise ValueError("Route A rejection prerequisites no longer hold")

    imported_closed = {
        "operator_level_projective_rhoE_transition_matrices": step38["closure_decision"][
            "operator_level_projective_rhoE_transition_matrices_closed"
        ],
        "selected_diagonal_End0_covariant_D_E": step39["closure_decision"][
            "selected_diagonal_End0_covariant_D_E_closed"
        ],
        "selected_stationary_projector_Riesz_Green_transport": step39["closure_decision"][
            "selected_stationary_projector_Riesz_Green_transport_closed"
        ],
        "selected_dotD_transport_derivative_formula": step40["closure_decision"][
            "selected_dotD_transport_derivative_formula_closed"
        ],
        "same_branch_dotD_alpha1_values": step40["closure_decision"]["same_branch_dotD_alpha1_values_closed"],
        "primitive_C1_first_response_layer": active["closure_decision"][
            "primitive_C1_first_response_layer_closed_by_active_ledger"
        ],
        "source_layer": active["closure_decision"]["source_layer_closed"],
    }
    if not all(imported_closed.values()):
        failed = [key for key, value in imported_closed.items() if not value]
        raise ValueError("expected reduced-payload imports to be closed: " + ", ".join(failed))

    remaining_fullsector = {
        "rank2_to_rank3_sector_transfer_values": step39["closure_decision"][
            "rank2_to_rank3_sector_transfer_values_closed"
        ]
        is False,
        "selected_full_sector_covariant_D_E_matrices": step39["closure_decision"][
            "selected_full_sector_covariant_D_E_matrices_closed"
        ]
        is False,
        "coherent_spectral_zero_mode_projectors": step39["closure_decision"][
            "coherent_spectral_zero_mode_projectors_closed"
        ]
        is False,
        "full_sector_offdiagonal_End0_control": step39["closure_decision"]["offdiagonal_End0_control_closed"]
        is False,
        "BN27_final_row_validator_acceptance_certificate": previous_remaining["remaining_open_items"][
            "BN27_final_row_validator_acceptance_certificate"
        ],
    }
    if not all(remaining_fullsector.values()):
        failed = [key for key, value in remaining_fullsector.items() if not value]
        raise ValueError("expected reduced full-sector blockers to stay open: " + ", ".join(failed))

    route_a_packet = {
        "schema": "MTTBN27HYMEndERowScopeSufficiencyRejection.v1",
        "status": "ROWSCOPE_REPRESENTATIVE_IS_SUPPORT_NOT_FINAL_ROW",
        "closure_claimed": True,
        "row": FINAL_ROW,
        "route_A_evaluated": True,
        "route_A_row_scope_sufficiency_theorem_proved": False,
        "route_A_rejected_by_current_validators": True,
        "row_scope_representative_available": True,
        "validator_evidence": {
            "eight_table_HYM_row_accepted": hym_row["accepted_as_final_connection_table"],
            "first_field_transition_representative_accepted": first_scan[
                "accepted_transition_or_connection_representative"
            ],
            "rtheta_diagonal_HYM_promoted_to_BN27_field": first_decision[
                "rtheta_diagonal_HYM_promoted_to_BN27_field"
            ],
            "rank2_to_sector_transfer_closed": first_decision["rank2_to_sector_transfer_closed"],
            "actual_QaSU3_operator_packet_promoted": first_decision["actual_QaSU3_operator_packet_promoted"],
            "selected_connection_witness_values_absent": first_decision["selected_connection_witness_values_absent"],
        },
        "rejection_reason": (
            "BN27 final-row acceptance is not a pure row-scope existence test. The current validators require "
            "a same-source transition/connection representative or selected HYM/projective coefficients with "
            "sector transfer, full-sector operator data, and an acceptance certificate."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    route_b_packet = {
        "schema": "MTTReducedFullSectorBN27HYMEndEValidatorPayload.v1",
        "status": "FULLSECTOR_PAYLOAD_REDUCED_TO_FOUR_FIELDS_PLUS_ACCEPTANCE",
        "closure_claimed": True,
        "already_closed_for_this_row": imported_closed,
        "remaining_fullsector_fields": remaining_fullsector,
        "old_fullsector_ledger_context": {
            "source": rel(FULLSECTOR_LEDGER),
            "old_required_field_count": fullsector_ledger["required_field_count"],
            "old_selected_payload_field_count": fullsector_ledger["selected_payload_field_count"],
            "old_blocking_field_count": fullsector_ledger["blocking_field_count"],
            "superseded_for_bn27_final_row_scope": [
                "F5_same_branch_dotD_alpha1_transport_derivative",
                "F7_primitive_C1_overlap_contractions",
            ],
        },
        "minimal_payload_to_emit_next": [
            "rank2-to-rank3 sector transfer values from End0/V_alpha into Q,u,d,L,e,N,H bases",
            "selected full-sector covariant D_E matrices on those bases",
            "coherent spectral zero-mode projectors retained in the transported sector bases",
            "full-sector offdiagonal End0 vanish/control theorem or selected correction coefficients",
            "BN27 final-row validator replay accepting selected_HYM_or_projective_connection_coefficients",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    gate_packet = {
        "schema": "MTTBN27HYMEndEFinalRowGateAfterRowScopeTest.v1",
        "status": "FINAL_ROW_OPEN_ROUTE_A_REJECTED_ROUTE_B_REDUCED",
        "closure_claimed": True,
        "strict_final_connection_table_count": "4/8",
        "one_premise_final_connection_table_count": "6/8",
        "two_premise_AH_equivalent_final_connection_table_count": "7/8",
        "route_A_row_scope_sufficiency_rejected": True,
        "route_B_fullsector_payload_reduced": True,
        "HYM_or_EndE_final_row_accepted": False,
        "strict_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextFullSectorBN27HYMEndEValidatorPayloadContract.v1",
        "status": "NEXT_IS_FULLSECTOR_BN27_HYMENDE_VALIDATOR_PAYLOAD",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "current_lanes": {
            "strict_lane": "4/8",
            "one_premise_BN27_lane": "6/8",
            "two_premise_AH_equivalent_lane": "7/8",
        },
        "must_emit": route_b_packet["minimal_payload_to_emit_next"],
        "must_not_reopen": [
            "operator-level projective rhoE transition",
            "diagonal End0 covariant D_E",
            "stationary Riesz/Green transport",
            "same-branch dotD alpha1",
            "primitive C1 first-response source layer",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedBN27HYMEndERowScopeAcceptanceOrFullSectorDEValues",
        "status": STATUS,
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "previous_candidate": rel(PREVIOUS),
            "previous_remaining": rel(PREVIOUS_REMAINING),
            "previous_contract": rel(PREVIOUS_CONTRACT),
            "eight_table_revalidation": rel(EIGHT_TABLE),
            "first_field_candidate": rel(FIRST_FIELD),
            "first_field_scan": rel(FIRST_FIELD_SCAN),
            "step38": rel(STEP38),
            "step39": rel(STEP39),
            "step40": rel(STEP40),
            "active_ledger": rel(ACTIVE_LEDGER),
            "fullsector_context": rel(FULLSECTOR),
        },
        "output_packets": {
            "route_a_rowscope_sufficiency_rejection": rel(ROUTE_A_PACKET),
            "route_b_reduced_fullsector_validator_payload": rel(ROUTE_B_PACKET),
            "bn27_hymende_final_row_gate_after_rowscope_test": rel(GATE_PACKET),
            "next_fullsector_bn27_hymende_validator_payload_contract": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "route_A_evaluated": True,
            "route_A_row_scope_sufficiency_theorem_proved": False,
            "route_A_rejected_by_current_validators": True,
            "route_B_fullsector_payload_reduced": True,
            "already_closed_payload_field_count": len(imported_closed),
            "remaining_fullsector_field_count": len(remaining_fullsector),
            "strict_final_connection_tables_accepted": 4,
            "one_premise_final_connection_tables_accepted": 6,
            "two_premise_AH_equivalent_final_connection_tables_accepted": 7,
            "HYM_or_EndE_final_row_accepted": False,
            "strict_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "BN27HYMEndERowScopeRejectionAndFullSectorReductionTheorem",
            "proved": True,
            "statement": (
                "The selected row-scope diagonal/projective End(E) representative is not sufficient for the "
                "BN27 HYM/End(E) final row under the current validators. The existing eight-table and first-field "
                "validators reject it as a final transition/connection representative because sector transfer, "
                "full-sector operator data, and selected connection witness values remain absent. Therefore Route A "
                "is closed negatively. Route B is reduced by importing Step38-Step40 and active-ledger closures; "
                "the next payload needs only rank2-to-rank3 transfer, full-sector D_E matrices, coherent zero-mode "
                "projectors, offdiagonal End0 control, and final-row validator acceptance."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedBN27HYMEndERowScopeAcceptanceOrFullSectorDEValues",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "route_A_evaluated": True,
        "route_A_row_scope_sufficiency_theorem_proved": False,
        "route_A_rejected_by_current_validators": True,
        "route_B_fullsector_payload_reduced": True,
        "already_closed_payload_field_count": len(imported_closed),
        "remaining_fullsector_field_count": len(remaining_fullsector),
        "two_premise_AH_equivalent_final_connection_tables_accepted": 7,
        "HYM_or_EndE_final_row_accepted": False,
        "strict_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected BN27 HYM/EndE RowScopeAcceptance or FullSectorDEValues v1

## Theorem

`BN27HYMEndERowScopeRejectionAndFullSectorReductionTheorem` is proved.

## Route A Result

Route A is evaluated and rejected under the current BN27 validators.

The row-scope diagonal/projective End(E) representative is real support, but it
is not accepted as the final row `{FINAL_ROW}`.  The eight-table revalidation
still rejects the HYM row, and the first-field scan still rejects
`A_diag=du*T3` as a BN27 transition/connection representative.

So the counted AH-equivalent lane remains `7/8`.

## Route B Reduction

Already closed for this row:

- operator-level projective `rho_E`
- diagonal End0 covariant `D_E`
- stationary Riesz/Green transport
- selected dotD transport derivative
- same-branch dotD/alpha1 values
- primitive C1 first-response layer
- source layer

Remaining full-sector payload:

- rank2-to-rank3 sector transfer values
- selected full-sector covariant `D_E` matrices
- coherent spectral zero-mode projectors
- full-sector offdiagonal End0 control
- BN27 final-row validator acceptance certificate

This does not close `8/8`, strict no-knob closure, or true SM equivalence.

## Next Artifact

`{NEXT}`
"""

    write_json(ROUTE_A_PACKET, route_a_packet)
    write_json(ROUTE_B_PACKET, route_b_packet)
    write_json(GATE_PACKET, gate_packet)
    write_json(NEXT_PACKET, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
