"""Back-import Step38-Step40 operator values into the HYM/End(E) final row.

The previous AH-lane HYM/End(E) cutset was written before the later
operator-sector packets were available.  This builder imports those later
results without overclaiming the final BN27 row:

* Step38 closes the non-identity projective rho_E transition gauge class.
* Step39 closes the diagonal End0 covariant D_E representative and stationary
  Riesz/Green transport.
* Step40 closes same-branch dotD/alpha1 transport.
* The active ledger supersedes stale local C1-open wording for the first
  primitive C1 response layer.

The final row is still not accepted: the remaining proof is either a
row-scope sufficiency theorem saying these diagonal/projective End(E)
representatives are exactly what BN27 requires, or a full-sector validator
payload with covariant D_E/Riesz/Green/dotD matrices, coherent projectors, and
the accepted connection-row certificate.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_operatorsector_hymende_backimport_after_step40_or_fullsector_guard"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
IMPORT_PACKET = PACKET_DIR / "step38_step40_operatorsector_backimport.packet.json"
GATE_PACKET = PACKET_DIR / "bn27_hymende_row_scope_gate_after_step40.packet.json"
REMAINING_PACKET = PACKET_DIR / "remaining_fullsector_or_rowscope_sufficiency_cutset.packet.json"
NEXT_PACKET = PACKET_DIR / "next_bn27_hymende_rowscope_or_fullsector_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_OperatorSector_HYMEndE_Backimport_AfterStep40_or_FullSectorGuard_v1.md"

PREVIOUS = DATA / "selected_hymende_operatorsector_cutset_after_ahlane.candidate.json"
PREVIOUS_CONTRACT = (
    DATA / "selected_hymende_operatorsector_cutset_after_ahlane" / "next_operatorsector_hymende_values_contract.packet.json"
)
STEP38 = DATA / "selected_step38_finiteheisenberg_rhoe_promotion_or_deoperatorfrontier.candidate.json"
STEP38_PACKET = (
    DATA
    / "selected_step38_finiteheisenberg_rhoe_promotion_or_deoperatorfrontier"
    / "step38_finite_heisenberg_rhoe_promotion.packet.json"
)
STEP39 = DATA / "selected_step39_diagonalend0_covariantde_import_or_fullsectorfrontier.candidate.json"
STEP39_PACKET = (
    DATA
    / "selected_step39_diagonalend0_covariantde_import_or_fullsectorfrontier"
    / "step39_diagonal_end0_covariant_de_import.packet.json"
)
STEP40 = DATA / "selected_step40_dotdtransport_alpha1import_or_primitivec1frontier.candidate.json"
STEP40_PACKET = (
    DATA
    / "selected_step40_dotdtransport_alpha1import_or_primitivec1frontier"
    / "step40_dotd_transport_alpha1_import.packet.json"
)
ACTIVE_LEDGER = DATA / "selected_activeledger_dotdc1supersession_or_valuelayerfrontier.candidate.json"
ACTIVE_DECISION = (
    DATA / "selected_activeledger_dotdc1supersession_or_valuelayerfrontier" / "active_ledger_supersession_decision.packet.json"
)
ACTIVE_SOURCE = (
    DATA / "selected_activeledger_dotdc1supersession_or_valuelayerfrontier" / "closed_source_layer_after_step24.packet.json"
)

STATUS = (
    "MTT_SELECTED_OPERATORSECTOR_HYMENDE_BACKIMPORT_AFTER_STEP40_"
    "ROW_SCOPE_GUARD_FULLSECTOR_OPEN"
)
NEXT = "MTT_Selected_BN27HYMEndERowScopeAcceptance_or_FullSectorDEValues_v1"
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
        raise FileNotFoundError("missing HYM/End(E) backimport inputs: " + ", ".join(missing))


def main() -> int:
    sources = [
        PREVIOUS,
        PREVIOUS_CONTRACT,
        STEP38,
        STEP38_PACKET,
        STEP39,
        STEP39_PACKET,
        STEP40,
        STEP40_PACKET,
        ACTIVE_LEDGER,
        ACTIVE_DECISION,
        ACTIVE_SOURCE,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_contract = load(PREVIOUS_CONTRACT)
    step38 = load(STEP38)
    step38_packet = load(STEP38_PACKET)
    step39 = load(STEP39)
    step39_packet = load(STEP39_PACKET)
    step40 = load(STEP40)
    step40_packet = load(STEP40_PACKET)
    active = load(ACTIVE_LEDGER)
    active_decision = load(ACTIVE_DECISION)
    active_source = load(ACTIVE_SOURCE)

    if previous["closure_decision"]["two_premise_AH_equivalent_final_connection_tables_accepted"] != 7:
        raise ValueError("expected previous counted AH-equivalent lane at 7/8")
    if previous["closure_decision"]["HYM_or_EndE_final_row_accepted"]:
        raise ValueError("previous packet unexpectedly accepted HYM/End(E) final row")
    if previous_contract["next_required_artifact"] != "MTT_Selected_OperatorSectorHYMEndEValues_or_ProjectiveRhoEConnection_v1":
        raise ValueError("previous contract no longer points at operator-sector HYM/End(E) values")

    step38_closed = {
        "operator_level_projective_rhoE_transition_matrices_closed": step38["closure_decision"][
            "operator_level_projective_rhoE_transition_matrices_closed"
        ],
        "nonidentity_projective_rhoE_selected_up_to_unitary_gauge": step38["closure_decision"][
            "nonidentity_projective_rhoE_selected_up_to_unitary_gauge"
        ],
        "step38_packet_numeric_gate_passes": step38_packet["selected_projective_rhoE_gauge_representative"][
            "numeric_gates"
        ]["passes_numeric_packet_gate"],
    }
    step39_closed = {
        "selected_diagonal_End0_covariant_D_E_closed": step39["closure_decision"][
            "selected_diagonal_End0_covariant_D_E_closed"
        ],
        "selected_stationary_projector_Riesz_Green_transport_closed": step39["closure_decision"][
            "selected_stationary_projector_Riesz_Green_transport_closed"
        ],
        "step39_operator_formula_present": step39_packet["selected_diagonal_end0_operator"]["D_E_formula"]
        == "D_E = d + du ad(T3)",
    }
    step40_closed = {
        "selected_dotD_transport_derivative_formula_closed": step40["closure_decision"][
            "selected_dotD_transport_derivative_formula_closed"
        ],
        "selected_alpha1_driver_normalization_closed": step40["closure_decision"][
            "selected_alpha1_driver_normalization_closed"
        ],
        "same_branch_dotD_alpha1_values_closed": step40["closure_decision"][
            "same_branch_dotD_alpha1_values_closed"
        ],
        "honest_dotD_alpha1_replay_closed": step40["closure_decision"]["honest_dotD_alpha1_replay_closed"],
        "step40_validator_math_passes": step40_packet["proof_checks"][
            "validator_math_passes_when_flags_theorem_derived"
        ],
    }
    active_closed = {
        "source_layer_closed": active["closure_decision"]["source_layer_closed"],
        "A_selected_closed_by_active_ledger": active["closure_decision"]["A_selected_closed_by_active_ledger"],
        "b_selected_closed_by_active_ledger": active["closure_decision"]["b_selected_closed_by_active_ledger"],
        "deltaTheta_C1_closed_by_active_ledger": active["closure_decision"][
            "deltaTheta_C1_closed_by_active_ledger"
        ],
        "primitive_C1_first_response_layer_closed_by_active_ledger": active["closure_decision"][
            "primitive_C1_first_response_layer_closed_by_active_ledger"
        ],
        "active_decision_supersedes_primitive_C1_open_wording": active_decision["superseded_now"][
            "selected_primitive_C1_contractions_first_response_layer"
        ],
        "formal_110_rows_executed": active_source["formal_rows"]["formal_110_rows_executed"],
    }

    imported = {**step38_closed, **step39_closed, **step40_closed, **active_closed}
    if not all(imported.values()):
        failed = [key for key, value in imported.items() if not value]
        raise ValueError("expected imported Step38-Step40/active-ledger rows to be closed: " + ", ".join(failed))

    still_open = {
        "selected_full_sector_covariant_D_E_matrices": step39["closure_decision"][
            "selected_full_sector_covariant_D_E_matrices_closed"
        ]
        is False,
        "coherent_spectral_zero_mode_projectors": step39["closure_decision"][
            "coherent_spectral_zero_mode_projectors_closed"
        ]
        is False,
        "rank2_to_rank3_sector_transfer_values": step39["closure_decision"][
            "rank2_to_rank3_sector_transfer_values_closed"
        ]
        is False,
        "full_sector_offdiagonal_End0_control": step39["closure_decision"]["offdiagonal_End0_control_closed"]
        is False,
        "accepted_internal_scalar_rows": step40["closure_decision"]["accepted_internal_scalar_row_count"] == 0,
        "accepted_value_functional_rows": active["closure_decision"]["accepted_value_functional_rows_closed"]
        is False,
        "BN27_row_scope_sufficiency_theorem": True,
        "BN27_final_row_validator_acceptance_certificate": True,
    }
    if not all(still_open.values()):
        failed = [key for key, value in still_open.items() if not value]
        raise ValueError("expected remaining full-sector/acceptance blockers to stay open: " + ", ".join(failed))

    import_packet = {
        "schema": "MTTStep38Step40OperatorSectorBackimport.v1",
        "status": "STEP38_STEP40_OPERATOR_VALUES_IMPORTED_FOR_HYMENDE_FINAL_ROW",
        "closure_claimed": True,
        "imported_operator_values": imported,
        "selected_representatives": {
            "rhoE_basis": step38_packet["selected_projective_rhoE_gauge_representative"]["basis"],
            "rhoE_active_generators": step38_packet["selected_projective_rhoE_gauge_representative"][
                "active_generators"
            ],
            "rhoE_kernel_generators": step38_packet["selected_projective_rhoE_gauge_representative"][
                "kernel_generators"
            ],
            "D_E_formula": step39_packet["selected_diagonal_end0_operator"]["D_E_formula"],
            "D_E_basis": step39_packet["selected_diagonal_end0_operator"]["basis"],
            "D_E_active_directions": step39_packet["selected_diagonal_end0_operator"]["active_directions"],
        },
        "old_operator_subblockers_retired": [
            "operator-level projective rho_E transition",
            "diagonal End0 covariant D_E representative",
            "stationary Riesz/Green transport",
            "same-branch dotD alpha1 transport",
            "primitive C1 first-response layer",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    gate_packet = {
        "schema": "MTTBN27HYMEndERowScopeGateAfterStep40.v1",
        "status": "ROW_SCOPE_REPRESENTATIVE_AVAILABLE_FINAL_ACCEPTANCE_OPEN",
        "closure_claimed": True,
        "row": FINAL_ROW,
        "strict_final_connection_table_count": "4/8",
        "one_premise_final_connection_table_count": "6/8",
        "two_premise_AH_equivalent_final_connection_table_count": "7/8",
        "row_scope_diagonal_projective_EndE_representative_available": True,
        "row_scope_sufficiency_theorem_proved": False,
        "full_sector_validator_ready": False,
        "HYM_or_EndE_final_row_accepted": False,
        "strict_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    remaining_packet = {
        "schema": "MTTRemainingFullSectorOrRowScopeSufficiencyCutset.v1",
        "status": "ONLY_ROWSCOPE_SUFFICIENCY_OR_FULLSECTOR_VALIDATOR_REMAINS",
        "closure_claimed": True,
        "remaining_open_items": still_open,
        "two_legal_routes": {
            "route_A_row_scope_sufficiency": [
                "prove the BN27 final row accepts the selected projective rho_E plus diagonal End0 covariant D_E/Riesz/Green/dotD representative as equivalent HYM/End(E) coefficients",
                "prove full-sector offdiagonal and coherent-projector data are not required for this row",
                "emit the BN27 final-row acceptance certificate",
            ],
            "route_B_full_sector_validator_payload": [
                "emit selected full-sector covariant D_E matrices",
                "emit coherent spectral zero-mode projectors",
                "emit rank2-to-rank3 sector-transfer values",
                "emit full-sector offdiagonal End0 control",
                "replay the BN27 final-row validator and accept the row",
            ],
        },
        "forbidden_loops": [
            "reopening projective rho_E transition after Step38",
            "reopening diagonal D_E or stationary Riesz/Green after Step39",
            "reopening dotD/alpha1 after Step40 and the active ledger",
            "counting first-response C1 source closure as final scalar/value-functional rows",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextBN27HYMEndERowScopeOrFullSectorContract.v1",
        "status": "NEXT_IS_ROWSCOPE_ACCEPTANCE_OR_FULLSECTOR_VALUES",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "must_choose_one_route": list(remaining_packet["two_legal_routes"].keys()),
        "route_A_minimal_theorem": remaining_packet["two_legal_routes"]["route_A_row_scope_sufficiency"],
        "route_B_minimal_payload": remaining_packet["two_legal_routes"]["route_B_full_sector_validator_payload"],
        "current_lanes": {
            "strict_lane": "4/8",
            "one_premise_BN27_lane": "6/8",
            "two_premise_AH_equivalent_lane": "7/8",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedOperatorSectorHYMEndEBackimportAfterStep40OrFullSectorGuard",
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
            "previous_contract": rel(PREVIOUS_CONTRACT),
            "step38_candidate": rel(STEP38),
            "step38_packet": rel(STEP38_PACKET),
            "step39_candidate": rel(STEP39),
            "step39_packet": rel(STEP39_PACKET),
            "step40_candidate": rel(STEP40),
            "step40_packet": rel(STEP40_PACKET),
            "active_ledger_candidate": rel(ACTIVE_LEDGER),
            "active_decision": rel(ACTIVE_DECISION),
            "active_source": rel(ACTIVE_SOURCE),
        },
        "output_packets": {
            "step38_step40_operatorsector_backimport": rel(IMPORT_PACKET),
            "bn27_hymende_row_scope_gate_after_step40": rel(GATE_PACKET),
            "remaining_fullsector_or_rowscope_sufficiency_cutset": rel(REMAINING_PACKET),
            "next_bn27_hymende_rowscope_or_fullsector_contract": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "imported_operator_value_count": len(imported),
            "old_operator_subblockers_retired_count": len(import_packet["old_operator_subblockers_retired"]),
            "row_scope_diagonal_projective_EndE_representative_available": True,
            "row_scope_sufficiency_theorem_proved": False,
            "full_sector_validator_ready": False,
            "strict_final_connection_tables_accepted": 4,
            "one_premise_final_connection_tables_accepted": 6,
            "two_premise_AH_equivalent_final_connection_tables_accepted": 7,
            "HYM_or_EndE_final_row_accepted": False,
            "strict_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "OperatorSectorHYMEndEBackimportAfterStep40Theorem",
            "proved": True,
            "statement": (
                "For the counted AH-equivalent BN27 lane, Step38-Step40 plus the active ledger retire the old "
                "operator-sector blockers: nonidentity projective rho_E, diagonal End0 covariant D_E, stationary "
                "Riesz/Green transport, same-branch dotD/alpha1, and first primitive C1 response.  This supplies "
                "a selected row-scope diagonal/projective End(E) representative for the HYM row, but it does not "
                "by itself prove BN27 final-row acceptance.  The remaining proof is exactly either a row-scope "
                "sufficiency theorem or a full-sector validator payload."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedOperatorSectorHYMEndEBackimportAfterStep40OrFullSectorGuard",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "imported_operator_value_count": len(imported),
        "old_operator_subblockers_retired_count": len(import_packet["old_operator_subblockers_retired"]),
        "row_scope_diagonal_projective_EndE_representative_available": True,
        "row_scope_sufficiency_theorem_proved": False,
        "full_sector_validator_ready": False,
        "two_premise_AH_equivalent_final_connection_tables_accepted": 7,
        "HYM_or_EndE_final_row_accepted": False,
        "strict_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected Operator-Sector HYM/EndE Backimport After Step40 v1

## Theorem

`OperatorSectorHYMEndEBackimportAfterStep40Theorem` is proved.

## What Closed

The older HYM/End(E) final-row cutset did not consume the later Step38-Step40
operator-sector packets.  This artifact imports them:

- Step38 closes operator-level nonidentity projective `rho_E`.
- Step39 closes diagonal End0 covariant `D_E = d + du ad(T3)` plus stationary
  Riesz/Green transport.
- Step40 closes same-branch dotD/alpha1 transport.
- The active ledger closes `A_selected`, `b_selected`, `deltaTheta_C1`, and the
  first primitive C1 response layer at source-layer scope.

So the old operator subblockers are retired.  They should not be reopened.

## What Did Not Close

The counted AH-equivalent lane remains `7/8`.  The final row remains:

- `{FINAL_ROW}`

The row-scope diagonal/projective End(E) representative is now available, but
BN27 final-row acceptance is not yet proved.  The remaining fork is exact:

- Route A: prove row-scope sufficiency for the diagonal/projective End(E)
  representative and emit the BN27 acceptance certificate.
- Route B: emit the full-sector covariant `D_E`/Riesz/Green/dotD matrices,
  coherent zero-mode projectors, rank2-to-rank3 transfer, offdiagonal End0
  control, and replay the final-row validator.

This does not close `8/8`, strict no-knob closure, or true SM equivalence.

## Next Artifact

`{NEXT}`
"""

    write_json(IMPORT_PACKET, import_packet)
    write_json(GATE_PACKET, gate_packet)
    write_json(REMAINING_PACKET, remaining_packet)
    write_json(NEXT_PACKET, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
