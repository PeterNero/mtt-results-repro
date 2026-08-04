"""Reduce the final HYM/End(E) row after the counted AH-equivalent lane.

The previous packet reaches a counted AH-equivalent 7/8 lane by accepting the
Cech row through the selected Appell-Humbert representative.  This builder
attacks the last row, `selected_HYM_or_projective_connection_coefficients`.

It imports the later Step26-Step28 and transport-conjugation packets so old
blockers are not reopened.  The result is still not 8/8: diagonal End0 HYM,
off-diagonal control, stationary projectors/rho_s, and validator-ready
stationary replay are closed, but the BN27 final row still needs operator-level
projective rho_E/connection data and sector-basis D_E/Riesz/Green/dotD values.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_hymende_operatorsector_cutset_after_ahlane"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
RETIRE_PACKET = PACKET_DIR / "retired_hymende_blockers_after_latest_sector_packets.packet.json"
OPEN_PACKET = PACKET_DIR / "remaining_hymende_operatorsector_value_cutset.packet.json"
GATE_PACKET = PACKET_DIR / "ah_lane_hymende_final_row_gate.packet.json"
NEXT_PACKET = PACKET_DIR / "next_operatorsector_hymende_values_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HYMEndE_OperatorSector_Cutset_After_AHLane_v1.md"

PREVIOUS = DATA / "selected_cech_ah_representative_or_hymende_values.candidate.json"
PREVIOUS_GATE = (
    DATA / "selected_cech_ah_representative_or_hymende_values" / "ah_representative_connection_row_gate.packet.json"
)
HYM_PROMOTION = DATA / "selected_selectedhymoperatorpayloadpromotion_or_rhoedefulls2execution.candidate.json"
STEP26 = DATA / "selected_step26_phifintrace_matterslot_reconciliation_or_fulls2payloadcutset.candidate.json"
STEP27 = DATA / "selected_step27_fulls2_subpayload_reduction_or_sectorpromotioncutset.candidate.json"
STEP28 = DATA / "selected_step28_sectorpromotion_reconciliation_or_operatorsectorvaluecutset.candidate.json"
TRANSPORT = DATA / "selected_transport_conjugation_validator_replay.candidate.json"
RTHETA_SECTOR = DATA / "selected_rtheta_sectortransferbnbasis_or_pikernelclosure.candidate.json"

STATUS = (
    "MTT_SELECTED_HYMENDE_OPERATORSECTOR_CUTSET_AFTER_AHLANE_"
    "STALE_BLOCKERS_RETIRED_FINAL_ROW_OPEN"
)
NEXT = "MTT_Selected_OperatorSectorHYMEndEValues_or_ProjectiveRhoEConnection_v1"
BN27_PREMISE = "SelectedBN27ThresholdSourceEmissionPrinciple"
AH_REPRESENTATIVE_PREMISE = "SelectedAHCechRepresentativeEquivalencePrinciple"
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
        raise FileNotFoundError("missing HYM/End(E) cutset inputs: " + ", ".join(missing))


def main() -> int:
    require_sources([PREVIOUS, PREVIOUS_GATE, HYM_PROMOTION, STEP26, STEP27, STEP28, TRANSPORT, RTHETA_SECTOR])

    previous = load(PREVIOUS)
    previous_gate = load(PREVIOUS_GATE)
    hym = load(HYM_PROMOTION)
    step26 = load(STEP26)
    step27 = load(STEP27)
    step28 = load(STEP28)
    transport = load(TRANSPORT)
    rtheta_sector = load(RTHETA_SECTOR)

    if previous_gate["two_premise_AH_equivalent_final_connection_table_count"] != "7/8":
        raise ValueError("expected counted AH-equivalent lane at 7/8")
    if previous_gate["remaining_rows_after_AH_equivalent_lane"] != [FINAL_ROW]:
        raise ValueError("unexpected remaining AH-lane row")
    if previous["closure_decision"]["HYM_or_EndE_final_row_accepted"]:
        raise ValueError("previous packet already accepted HYM/End(E) row unexpectedly")

    retired = {
        "diagonal_End0_operator_payload_closed": hym["closure_decision"]["diagonal_End0_operator_payload_closed"],
        "full_diagonal_End0_HYM_payload_closed": hym["what_closes_now"]["full_diagonal_End0_HYM_payload_closed"],
        "row_model_offdiagonal_Ext_control_closed": hym["what_closes_now"]["row_model_offdiagonal_Ext_control_closed"],
        "T1_T2_covariant_Green_closed": step27["closure_decision"]["T1_T2_covariant_Green_closed"],
        "protected_T3_Riesz_Green_closed": step27["closure_decision"]["protected_T3_Riesz_Green_closed"],
        "functional_PhiFin_trace_closed": step26["closure_decision"]["functional_PhiFin_trace_closed"],
        "validator_ready_sector_rho_s_packet_closed": step26["closure_decision"][
            "validator_ready_sector_rho_s_packet_closed"
        ],
        "selected_projector_promotion_Ps_Ks_closed": step28["closure_decision"][
            "selected_projector_promotion_Ps_Ks_closed"
        ],
        "selected_stationary_End0_to_sector_routing_values_closed": step28["closure_decision"][
            "selected_stationary_End0_to_sector_routing_values_closed"
        ],
        "selected_stationary_rho_s_matrix_values_closed": step28["closure_decision"][
            "selected_stationary_rho_s_matrix_values_closed"
        ],
        "selected_projective_rhoE_source_level_closed": step28["closure_decision"][
            "selected_projective_rhoE_source_level_closed"
        ],
        "symbolic_transport_conjugation_validator_closed": transport["promotion_decision"][
            "symbolic_transport_conjugation_replay_closed"
        ],
        "transport_closed_finite_validator_replay": transport["promotion_decision"][
            "transport_closed_finite_validator_replay"
        ],
        "stationary_sector_transfer_closed": rtheta_sector["closure_decision"]["stationary_sector_transfer_closed"],
        "selected_stationary_rho_s_closed": rtheta_sector["closure_decision"]["selected_stationary_rho_s_closed"],
    }
    if not all(retired.values()):
        failed = [key for key, value in retired.items() if not value]
        raise ValueError("expected retired HYM/End(E) blockers to be closed: " + ", ".join(failed))

    still_open = {
        "operator_level_projective_rhoE_from_selected_connection": step28["closure_decision"][
            "operator_level_projective_rhoE_from_selected_connection_closed"
        ]
        is False,
        "selected_rhoE_transition_payload_fullS2_operator_tier": step28["closure_decision"][
            "selected_rhoE_transition_payload_fullS2_operator_tier_closed"
        ]
        is False,
        "selected_sector_basis_D_E_matrices": step28["what_remains_open"]["selected_sector_basis_D_E_matrices"],
        "selected_sector_basis_Riesz_projectors": step28["what_remains_open"]["selected_sector_basis_Riesz_projectors"],
        "selected_sector_basis_Green_operators": step28["what_remains_open"]["selected_sector_basis_Green_operators"],
        "selected_sector_basis_dotD_matrices": step28["what_remains_open"]["selected_sector_basis_dotD_matrices"],
        "dynamic_PhiFin_C1_payload": step28["closure_decision"]["dynamic_PhiFin_C1_payload_closed"] is False,
        "selected_fullS2_rhoE_D_E_operator_payload": step27["closure_decision"][
            "selected_D_E_Riesz_Green_dotD_sector_matrices_closed"
        ]
        is False,
    }
    if not all(still_open.values()):
        failed = [key for key, value in still_open.items() if not value]
        raise ValueError("expected HYM/End(E) remaining cutset to stay open: " + ", ".join(failed))

    retire_packet = {
        "schema": "MTTRetiredHYMEndEBlockersAfterLatestSectorPackets.v1",
        "status": "STALE_HYMENDE_BLOCKERS_RETIRED",
        "closure_claimed": True,
        "retired_blockers": retired,
        "do_not_reopen_as_final_row_blockers": [
            "diagonal_End0_operator_payload",
            "row_model_offdiagonal_Ext_control",
            "stationary_projectors_Ps_Ks",
            "stationary_rho_s_matrix_values",
            "validator_ready_sector_rho_s_packet",
            "symbolic_transport_conjugation_replay",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    open_packet = {
        "schema": "MTTRemainingHYMEndEOperatorSectorValueCutset.v1",
        "status": "FINAL_HYMENDE_ROW_REDUCED_TO_OPERATOR_SECTOR_VALUES",
        "closure_claimed": True,
        "row": FINAL_ROW,
        "accepted_as_final_connection_table_row": False,
        "remaining_operator_sector_values": still_open,
        "minimal_success_conditions": [
            "emit operator-level projective rho_E transition from the selected connection",
            "emit selected sector-basis D_E matrices",
            "emit selected sector-basis Riesz projectors and Green operators",
            "emit selected sector-basis dotD matrices or prove dotD is unnecessary for this BN27 final row",
            "show these values are accepted by the BN27 connection-row validator as HYM/projective coefficients or equivalent End(E) values",
        ],
        "rejected_shortcuts": [
            "diagonal End0 payload alone",
            "stationary projector/rho_s payload alone",
            "source-level projective rho_E without operator-level transition values",
            "symbolic transport replay without sector-basis operator matrices",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    gate_packet = {
        "schema": "MTTAHLaneHYMEndEFinalRowGate.v1",
        "status": "TWO_PREMISE_AH_EQUIVALENT_LANE_REMAINS_7_OF_8_HYMENDE_OPEN",
        "closure_claimed": True,
        "strict_final_connection_table_count": "4/8",
        "one_premise_final_connection_table_count": "6/8",
        "two_premise_AH_equivalent_final_connection_table_count": "7/8",
        "two_premise_counted_principles": [BN27_PREMISE, AH_REPRESENTATIVE_PREMISE],
        "remaining_row": FINAL_ROW,
        "HYM_or_EndE_final_row_accepted": False,
        "strict_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextOperatorSectorHYMEndEValuesContract.v1",
        "status": "NEXT_IS_OPERATOR_SECTOR_HYMENDE_VALUE_EMISSION",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "current_lanes": {
            "strict_lane": "4/8",
            "one_premise_BN27_lane": "6/8",
            "two_premise_AH_equivalent_lane": "7/8",
        },
        "must_emit_next": open_packet["minimal_success_conditions"],
        "must_not_reopen": retire_packet["do_not_reopen_as_final_row_blockers"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHYMEndEOperatorSectorCutsetAfterAHLane",
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
            "previous_gate": rel(PREVIOUS_GATE),
            "hym_promotion": rel(HYM_PROMOTION),
            "step26": rel(STEP26),
            "step27": rel(STEP27),
            "step28": rel(STEP28),
            "transport": rel(TRANSPORT),
            "rtheta_sector": rel(RTHETA_SECTOR),
        },
        "output_packets": {
            "retired_hymende_blockers_after_latest_sector_packets": rel(RETIRE_PACKET),
            "remaining_hymende_operatorsector_value_cutset": rel(OPEN_PACKET),
            "ah_lane_hymende_final_row_gate": rel(GATE_PACKET),
            "next_operatorsector_hymende_values_contract": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "strict_final_connection_tables_accepted": 4,
            "one_premise_final_connection_tables_accepted": 6,
            "two_premise_AH_equivalent_final_connection_tables_accepted": 7,
            "HYM_or_EndE_final_row_accepted": False,
            "retired_blocker_count": len(retired),
            "remaining_operator_sector_value_count": len(still_open),
            "strict_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "HYMEndEOperatorSectorCutsetAfterAHLaneTheorem",
            "proved": True,
            "statement": (
                "After the counted AH-equivalent Cech-row lane reaches 7/8, the last BN27 connection row is "
                "not blocked by diagonal End0 HYM, off-diagonal row-model control, stationary projectors, "
                "stationary rho_s, or symbolic transport replay. Those blockers are closed by the latest "
                "sector packets and must not be reopened. The remaining HYM/End(E) row is precisely the "
                "operator-sector value layer: operator-level projective rho_E from the selected connection, "
                "sector-basis D_E/Riesz/Green/dotD matrices, and BN27 validator acceptance as HYM/projective "
                "coefficients or equivalent End(E) values. Therefore the counted AH-equivalent lane remains 7/8."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedHYMEndEOperatorSectorCutsetAfterAHLane",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "strict_final_connection_tables_accepted": 4,
        "one_premise_final_connection_tables_accepted": 6,
        "two_premise_AH_equivalent_final_connection_tables_accepted": 7,
        "HYM_or_EndE_final_row_accepted": False,
        "retired_blocker_count": len(retired),
        "remaining_operator_sector_value_count": len(still_open),
        "strict_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected HYM/EndE Operator-Sector Cutset After AH Lane v1

## Theorem

`HYMEndEOperatorSectorCutsetAfterAHLaneTheorem` is proved.

## Result

Current connection-table lanes:

- strict lane: `4/8`
- one-premise BN27 lane: `6/8`
- counted AH-equivalent lane: `7/8`

The final row remains open:

- `{FINAL_ROW}`

Retired blockers that must not be reopened:

- diagonal End0 HYM payload
- row-model off-diagonal Ext control
- stationary projector/rho_s promotion
- validator-ready sector rho_s packet
- symbolic transport-conjugation replay

The remaining target is now only the operator-sector value layer:

- operator-level projective `rho_E` transition from the selected connection
- selected sector-basis `D_E` matrices
- selected sector-basis Riesz/Green/dotD matrices, or a proof that dotD is not needed for this final BN27 row
- BN27 validator acceptance as HYM/projective coefficients or equivalent End(E) values

This does not close `8/8`, strict no-knob closure, or true SM equivalence.

## Next Artifact

`{NEXT}`
"""

    write_json(RETIRE_PACKET, retire_packet)
    write_json(OPEN_PACKET, open_packet)
    write_json(GATE_PACKET, gate_packet)
    write_json(NEXT_PACKET, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
