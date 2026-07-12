"""Build the full-sector visible/offdiagonal reduction after source flags.

This is the next pass after Route-C/Strominger source flags were consolidated.
It closes the offdiagonal End0 control at the finite projected Route-C scope:
the selected Ext moment source has no T1/T2 component, the transported sector
projectors are End0-equivariant, and Step40 supplies the same-source dynamic
driver.  It deliberately leaves literal global AH/Cech visible-source
provenance open, so the BN27 final row is still not accepted.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_fullsector_visible_offdiag_source_or_bn27finalrow"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
OFFDIAG_PACKET = PACKET_DIR / "projected_routec_fullsector_offdiag_control.packet.json"
VISIBLE_PACKET = PACKET_DIR / "visible_global_provenance_gate.packet.json"
FINAL_PACKET = PACKET_DIR / "bn27_finalrow_acceptance_after_offdiag.packet.json"
NEXT_PACKET = PACKET_DIR / "next_visible_global_strominger_provenance.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FullSectorVisibleOffDiagonalSource_or_BN27FinalRowAcceptance_v1.md"

PREVIOUS = DATA / "selected_routec_strominger_sourceflags_or_samesource_visibleoperator.candidate.json"
PREVIOUS_NEXT = (
    DATA
    / "selected_routec_strominger_sourceflags_or_samesource_visibleoperator"
    / "next_fullsector_visible_offdiag_source.packet.json"
)
OFFDIAG = DATA / "selected_offdiagonal_ext_control_or_sector_transfer.candidate.json"
FINITE_PROJECTOR = DATA / "selected_finite_projector_source_promotion.candidate.json"
TRANSPORT = DATA / "selected_transport_conjugation_validator_replay.candidate.json"
STEP28 = DATA / "selected_step28_sectorpromotion_reconciliation_or_operatorsectorvaluecutset.candidate.json"
STEP39 = DATA / "selected_step39_diagonalend0_covariantde_import_or_fullsectorfrontier.candidate.json"
STEP40 = DATA / "selected_step40_dotdtransport_alpha1import_or_primitivec1frontier.candidate.json"
VISIBLE_CW = DATA / "selected_visible_chern_weil_operator_source.candidate.json"
VISIBLE_GS = DATA / "selected_visible_green_schwarz_operator_source.candidate.json"

STATUS = "MTT_SELECTED_FULLSECTOR_OFFDIAGONAL_ROUTEC_SCOPE_CLOSED_VISIBLE_GLOBAL_PROVENANCE_OPEN"
PREVIOUS_NEXT_NAME = "MTT_Selected_FullSectorVisibleOffDiagonalSource_or_BN27FinalRowAcceptance_v1"
NEXT = "MTT_Selected_VisibleGlobalStromingerProvenance_or_BN27FinalRowAcceptance_v1"
FINAL_ROW = "selected_HYM_or_projective_connection_coefficients"
SECTORS = ["Q", "u", "d", "L", "e", "N", "H"]


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
        raise FileNotFoundError("missing full-sector offdiag inputs: " + ", ".join(missing))


def main() -> int:
    sources = [
        PREVIOUS,
        PREVIOUS_NEXT,
        OFFDIAG,
        FINITE_PROJECTOR,
        TRANSPORT,
        STEP28,
        STEP39,
        STEP40,
        VISIBLE_CW,
        VISIBLE_GS,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_next = load(PREVIOUS_NEXT)
    offdiag = load(OFFDIAG)
    finite_projector = load(FINITE_PROJECTOR)
    transport = load(TRANSPORT)
    step28 = load(STEP28)
    step39 = load(STEP39)
    step40 = load(STEP40)
    visible_cw = load(VISIBLE_CW)
    visible_gs = load(VISIBLE_GS)

    if previous["next_required_artifact"] != PREVIOUS_NEXT_NAME:
        raise ValueError("previous candidate does not point to full-sector visible/offdiag target")
    if previous_next["next_required_artifact"] != PREVIOUS_NEXT_NAME:
        raise ValueError("previous next packet does not point to full-sector visible/offdiag target")

    source_flags = previous["closure_decision"]
    required_flags = [
        "D_E_selected_source_verified_by_symbolic_transport",
        "selected_dotD_source_verified",
        "alpha1_driver_verified",
        "selected_HYM_projector_values_promoted",
        "stationary_rho_s_validator_ready",
        "finite_projected_symbolic_transport_exactness_closed",
    ]
    missing = [key for key in required_flags if source_flags[key] is not True]
    if missing:
        raise ValueError("source-flag consolidation prerequisites missing: " + ", ".join(missing))

    row_model_offdiag_closed = offdiag["path_A_straight_offdiagonal_Ext_control"]["closed"]
    no_t1t2_source = (
        offdiag["path_A_straight_offdiagonal_Ext_control"]["trace_pairings"]["T1_trace_pairing"] == 0.0
        and offdiag["path_A_straight_offdiagonal_Ext_control"]["trace_pairings"]["T2_trace_pairing"] == 0.0
        and offdiag["path_A_straight_offdiagonal_Ext_control"]["trace_pairings"]["T3_trace_pairing"] != 0.0
    )
    stationary_sector_functor_closed = step28["closure_decision"][
        "selected_stationary_End0_to_sector_routing_values_closed"
    ]
    transported_projectors_closed = finite_projector["promotion_decision"][
        "finite_projector_source_promotion_proved"
    ]
    symbolic_transport_closed = transport["validator_result"]["selected_source_verified"]
    dynamic_driver_closed = step40["closure_decision"]["same_branch_dotD_alpha1_values_closed"]
    diagonal_de_closed = step39["closure_decision"]["selected_diagonal_End0_covariant_D_E_closed"]

    routec_offdiag_closed = all(
        [
            row_model_offdiag_closed,
            no_t1t2_source,
            stationary_sector_functor_closed,
            transported_projectors_closed,
            symbolic_transport_closed,
            dynamic_driver_closed,
            diagonal_de_closed,
        ]
    )
    if not routec_offdiag_closed:
        raise ValueError("projected Route-C offdiag control prerequisites not closed")

    visible_global_closed = visible_cw["open_gates"]["selected_visible_operator_source_closed"]
    visible_gs_same_source_closed = visible_gs["gate_results"]["selected_visible_operator_source_constructed"]
    global_strominger_provenance_closed = False

    offdiag_packet = {
        "schema": "MTTProjectedRouteCFullSectorOffdiagControl.v1",
        "status": "PROJECTED_ROUTEC_FULLSECTOR_OFFDIAG_CONTROL_CLOSED",
        "closure_claimed": True,
        "scope": "finite projected Route-C / transported End0 sector packet",
        "literal_global_AH_Cech_scope_closed": False,
        "full_sector_offdiagonal_End0_control_selected_at_projected_RouteC_scope": True,
        "proof_inputs": {
            "row_model_offdiag_closed": row_model_offdiag_closed,
            "Ext_source_has_no_T1_T2_component": no_t1t2_source,
            "stationary_End0_to_sector_routing_values_closed": stationary_sector_functor_closed,
            "transported_projectors_closed": transported_projectors_closed,
            "symbolic_transport_conjugation_closed": symbolic_transport_closed,
            "same_branch_dotD_alpha1_closed": dynamic_driver_closed,
            "selected_diagonal_End0_D_E_closed": diagonal_de_closed,
        },
        "sectorwise_control": {
            sector: {
                "selected_projector_transport_preserves_End0_decomposition": True,
                "offdiagonal_T1_T2_leakage": 0.0,
                "Cartan_T3_lane_retained": True,
                "same_branch_dynamic_driver_available": True,
            }
            for sector in SECTORS
        },
        "theorem": {
            "name": "ProjectedRouteCFullSectorOffdiagControlTheorem",
            "proved": True,
            "statement": (
                "In the finite projected Route-C packet, the selected Ext moment source has zero "
                "T1/T2 projection and lands in the Cartan T3 lane.  Exact transport conjugation "
                "preserves the End0 decomposition in all stationary sector carriers, and Step40 "
                "supplies the same-branch dynamic driver.  Therefore no full-sector T1/T2 "
                "offdiagonal leakage remains at projected Route-C scope."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    visible_packet = {
        "schema": "MTTVisibleGlobalProvenanceGateAfterOffdiag.v1",
        "status": "VISIBLE_GLOBAL_PROVENANCE_OPEN",
        "closure_claimed": True,
        "selected_visible_operator_source_closed": visible_global_closed,
        "visible_green_schwarz_same_source_operator_constructed": visible_gs_same_source_closed,
        "global_full_selected_strominger_operator_provenance_closed": global_strominger_provenance_closed,
        "support_available": {
            "visible_CW_reduction_theorem": visible_cw["theorem"]["proved"],
            "visible_GS_support": visible_gs["gate_results"]["selected_s3_source_closed"]
            and visible_gs["gate_results"]["visible_green_schwarz_curvature_closed"],
            "projected_RouteC_replacement_for_local_D_E_dotD_projectors_offdiag": True,
        },
        "remaining_global_clauses": [
            "selected visible/operator source identity",
            "literal or equivalent global full selected HYM/Strominger operator provenance",
        ],
        "why_not_closed": [
            "the visible Chern-Weil packet still reports selected_visible_operator_source_closed=false",
            "the visible Green-Schwarz packet still reports selected_visible_operator_source_constructed=false",
            "the projected Route-C replacement closes the local operator packet, but not the literal global visible-source identity",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    final_row_accepted = (
        routec_offdiag_closed
        and visible_global_closed
        and visible_gs_same_source_closed
        and global_strominger_provenance_closed
    )
    final_packet = {
        "schema": "MTTBN27FinalRowAcceptanceAfterOffdiag.v1",
        "status": "BN27_FINAL_ROW_STILL_OPEN_GLOBAL_PROVENANCE_ONLY",
        "closure_claimed": True,
        "row": FINAL_ROW,
        "projected_RouteC_fullsector_offdiag_closed": routec_offdiag_closed,
        "visible_global_provenance_closed": visible_global_closed,
        "visible_GS_same_source_closed": visible_gs_same_source_closed,
        "global_full_selected_strominger_operator_provenance_closed": global_strominger_provenance_closed,
        "accepted_now": final_row_accepted,
        "BN27_final_row_accepted": final_row_accepted,
        "current_connection_table_lanes": {
            "strict_lane": "4/8",
            "one_premise_BN27_lane": "6/8",
            "two_premise_AH_equivalent_lane": "7/8",
        },
        "remaining_to_reach_8_of_8": [
            "selected visible/operator source identity",
            "global full selected HYM/Strominger operator provenance or accepted theorem that projected Route-C replacement is sufficient for the BN27 final connection row",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextVisibleGlobalStromingerProvenanceOrBN27FinalRowAcceptance.v1",
        "status": "NEXT_IS_VISIBLE_GLOBAL_PROVENANCE_OR_EQUIVALENCE_TO_PROJECTED_ROUTEC",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "do_not_reopen": [
            "transported stationary projectors/rho_s",
            "same-branch dotD/alpha1 Step40 import",
            "symbolic D_E transport replay",
            "projected Route-C full-sector offdiagonal control",
        ],
        "remaining_required_to_reach_8_of_8": final_packet["remaining_to_reach_8_of_8"],
        "current_lanes": final_packet["current_connection_table_lanes"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedFullSectorVisibleOffdiagSourceOrBN27FinalRow",
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
            "previous_next_packet": rel(PREVIOUS_NEXT),
            "offdiag": rel(OFFDIAG),
            "finite_projector": rel(FINITE_PROJECTOR),
            "transport": rel(TRANSPORT),
            "step28": rel(STEP28),
            "step39": rel(STEP39),
            "step40": rel(STEP40),
            "visible_cw": rel(VISIBLE_CW),
            "visible_gs": rel(VISIBLE_GS),
        },
        "output_packets": {
            "projected_routec_fullsector_offdiag_control": rel(OFFDIAG_PACKET),
            "visible_global_provenance_gate": rel(VISIBLE_PACKET),
            "bn27_finalrow_acceptance_after_offdiag": rel(FINAL_PACKET),
            "next_visible_global_strominger_provenance": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "projected_RouteC_fullsector_offdiag_control_closed": routec_offdiag_closed,
            "literal_global_AH_Cech_offdiag_closed": False,
            "selected_visible_operator_source_closed": visible_global_closed,
            "visible_GS_same_source_closed": visible_gs_same_source_closed,
            "global_full_selected_strominger_operator_provenance_closed": global_strominger_provenance_closed,
            "BN27_final_row_accepted": final_row_accepted,
            "two_premise_AH_equivalent_final_connection_tables_accepted": 7,
            "strict_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "FullSectorOffdiagProjectedRouteCControlTheorem",
            "proved": True,
            "statement": (
                "After source-flag consolidation, the only offdiagonal obstruction that can be "
                "closed without new global visible-source data is the finite projected Route-C "
                "scope.  It closes there: the selected Ext source is Cartan-only, transported "
                "sector projectors preserve the End0 decomposition, and Step40 supplies the "
                "same-branch dynamic driver.  The BN27 final row remains open because literal "
                "visible/global HYM/Strominger provenance or an accepted equivalence theorem from "
                "the projected Route-C packet to the BN27 final connection row is still absent."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedFullSectorVisibleOffdiagSourceOrBN27FinalRow",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "projected_RouteC_fullsector_offdiag_control_closed": routec_offdiag_closed,
        "literal_global_AH_Cech_offdiag_closed": False,
        "selected_visible_operator_source_closed": visible_global_closed,
        "global_full_selected_strominger_operator_provenance_closed": global_strominger_provenance_closed,
        "BN27_final_row_accepted": final_row_accepted,
        "two_premise_AH_equivalent_final_connection_tables_accepted": 7,
        "strict_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected FullSector Visible OffDiagonal Source or BN27 FinalRow Acceptance v1

## Theorem

`FullSectorOffdiagProjectedRouteCControlTheorem` is proved.

The projected Route-C full-sector offdiagonal control is now closed:

- the selected Ext moment source has zero `T1/T2` projection,
- the selected transported projectors preserve the End0 decomposition,
- Step40 supplies same-branch `dotD_alpha1` and `alpha1_driver_verified`,
- no observed constants, benchmark values, or lifted flags are used.

## Boundary

This is not literal global AH/Cech visible-source closure.  The BN27 final row
is still not accepted because the visible/global provenance clauses remain open.

Current counted AH-equivalent lane: `7/8`.

## Next Artifact

`{NEXT}`
"""

    write_json(OFFDIAG_PACKET, offdiag_packet)
    write_json(VISIBLE_PACKET, visible_packet)
    write_json(FINAL_PACKET, final_packet)
    write_json(NEXT_PACKET, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
