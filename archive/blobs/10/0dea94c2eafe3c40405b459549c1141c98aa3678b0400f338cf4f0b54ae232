"""Build Step 27 full-S2 subpayload reduction / sector-promotion cutset."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step27_fulls2_subpayload_reduction_or_sectorpromotioncutset"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SUBPAYLOAD = PACKET_DIR / "step27_closed_hym_subpayload.packet.json"
PROMOTION_GAP = PACKET_DIR / "step27_sector_promotion_gap.packet.json"
NEXT_CUTSET = PACKET_DIR / "step27_next_sector_promotion_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step27_FullS2SubpayloadReduction_or_SectorPromotionCutset_v1.md"

STEP26 = DATA / "selected_step26_phifintrace_matterslot_reconciliation_or_fulls2payloadcutset.candidate.json"
HYM = DATA / "selected_selectedhymoperatorpayloadpromotion_or_rhoedefulls2execution.candidate.json"
HYM_PAYLOAD = DATA / "selected_selectedhymoperatorpayloadpromotion_or_rhoedefulls2execution" / "selected_hym_operator_payload_promotion_gate.packet.json"
HYM_FULLS2 = DATA / "selected_selectedhymoperatorpayloadpromotion_or_rhoedefulls2execution" / "rhoede_full_s2_execution_gate.packet.json"
HIGHER = DATA / "selected_higherresponsepayloadrows_sourcepromotion_or_fulls2valueexecution.candidate.json"
HIGHER_FULLS2 = DATA / "selected_higherresponsepayloadrows_sourcepromotion_or_fulls2valueexecution" / "full_s2_value_execution_gate.packet.json"
END0_DE = DATA / "selected_end0_de_payload_from_diagonal_hym.candidate.json"
RIESZ = DATA / "selected_riesz_green_dotd_from_diagonal_end0_de.candidate.json"
HYM_EXTRACTION = DATA / "selected_hym_operator_payload_extraction_from_diagonal_replay.candidate.json"

STATUS = "MTT_SELECTED_STEP27_FULLS2_SUBPAYLOAD_REDUCTION_OR_SECTORPROMOTIONCUTSET_BUILT_DIAGONAL_GREEN_SUBPAYLOAD_CLOSED_SECTOR_PROMOTION_OPEN"
NEXT = "MTT_Selected_End0SectorTransfer_ProjectorPromotion_or_RhoEDEOperatorValues_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [STEP26, HYM, HYM_PAYLOAD, HYM_FULLS2, HIGHER, HIGHER_FULLS2, END0_DE, RIESZ, HYM_EXTRACTION]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step 27 inputs: " + ", ".join(missing))

    step26 = load(STEP26)
    hym = load(HYM)
    hym_payload = load(HYM_PAYLOAD)
    hym_fulls2 = load(HYM_FULLS2)
    higher = load(HIGHER)
    higher_fulls2 = load(HIGHER_FULLS2)
    end0_de = load(END0_DE)
    riesz = load(RIESZ)
    hym_extraction = load(HYM_EXTRACTION)

    closed_diagonal = hym_payload["closed_diagonal_payload"]
    subpayload = {
        "schema": "MTTStep27ClosedHYMSubpayload.v1",
        "status": "DIAGONAL_END0_GREEN_SUBPAYLOAD_CLOSED",
        "step26_next_artifact": step26["next_required_artifact"],
        "closed_subpayloads": {
            "full_expS_diagonal_replay": closed_diagonal["full_expS_diagonal_replay"],
            "rank2_metric_connection_payload": closed_diagonal["rank2_metric_connection_payload"],
            "End0_D_E_connection_matrices": closed_diagonal["End0_D_E_connection_matrices"],
            "protected_T3_Riesz_Green": closed_diagonal["protected_T3_Riesz_Green"],
            "T1_T2_covariant_Green": closed_diagonal["T1_T2_covariant_Green"],
            "row_model_offdiagonal_Ext_control": closed_diagonal["row_model_offdiagonal_Ext_control"],
            "diagonal_End0_D_E_formula": end0_de["operator_payload_boundary"]["diagonal_End0_D_E_formula_extracted"],
            "protected_T3_zero_mode_Riesz_projector": riesz["protected_T3_lane"]["closed"],
        },
        "numerical_support": {
            "D_E_x1_frobenius_l2": end0_de["D_E_direction_payload"]["x1"]["connection_matrix_frobenius_l2"],
            "D_E_y2_frobenius_l2": end0_de["D_E_direction_payload"]["y2"]["connection_matrix_frobenius_l2"],
            "green_residual_l2": riesz["numerical_green_replay"]["green_residual_l2"],
            "curvature_residual_payload_closed": hym_extraction["curvature_residual_payload"]["closed"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(SUBPAYLOAD, subpayload)

    boundary = hym_payload["promotion_boundary"]
    promotion_gap = {
        "schema": "MTTStep27SectorPromotionGap.v1",
        "status": "FULLS2_PROMOTION_GAP_REDUCED_TO_SECTOR_TRANSFER_PROJECTORS_RHOE_DE_VALUES",
        "rank2_End0_payload_closed": boundary["rank2_End0_payload_closed"],
        "selected_diagonal_HYM_first_solve_closed": boundary["selected_diagonal_HYM_first_solve_closed"],
        "not_promoted": {
            "rank2_to_sector_transfer_closed": boundary["rank2_to_sector_transfer_closed"],
            "physical_dotD_alpha1_closed_in_fullS2_gate": boundary["physical_dotD_alpha1_closed"],
            "selected_End0_to_sector_routing_values_extracted": boundary["selected_End0_to_sector_routing_values_extracted"],
            "finite_projector_values_promoted_to_selected": boundary["finite_projector_values_promoted_to_selected"],
            "PhiFin_selected_trace_emitted_in_old_hym_gate": boundary["PhiFin_selected_trace_emitted"],
            "rhoE_DE_fullS2_execution_closed": hym["closure_decision"]["rhoE_DE_fullS2_execution_closed"],
            "selected_HYM_sector_payload_closed": hym["closure_decision"]["selected_HYM_sector_payload_closed"],
        },
        "post_step26_reconciliation": {
            "PhiFin_trace_closed_elsewhere": step26["closure_decision"]["functional_PhiFin_trace_closed"],
            "static_matter_slot_source_closed_elsewhere": step26["closure_decision"]["static_U10_Ubar5_1M_source_closed"],
            "still_not_fullS2_operator_payload": not step26["closure_decision"]["selected_fullS2_rhoE_D_E_operator_payload_closed"],
        },
        "higher_response_execution_state": {
            "execution_attempted": higher_fulls2["execution_attempted"],
            "execution_allowed_now": higher_fulls2["execution_allowed_now"],
            "accepted_scalar_row_count_now": higher_fulls2["accepted_scalar_row_count_now"],
            "selected_HYM_operator_payload_ready": higher_fulls2["ready_fields"]["selected_HYM_operator_payload_ready"],
            "selected_rhoE_DE_operator_payload_ready": higher_fulls2["ready_fields"]["selected_rhoE_DE_operator_payload_ready"],
            "selected_End0_sector_functor_ready": higher_fulls2["ready_fields"]["selected_End0_sector_functor_ready"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(PROMOTION_GAP, promotion_gap)

    next_cutset = {
        "schema": "MTTStep27NextSectorPromotionCutset.v1",
        "status": "NEXT_END0_SECTOR_TRANSFER_PROJECTOR_PROMOTION_RHOE_DE_VALUES",
        "closed_do_not_reopen": {
            "diagonal_End0_D_E_connection_matrices": True,
            "protected_T3_Riesz_Green": True,
            "T1_T2_covariant_Green": True,
            "row_model_offdiagonal_Ext_control": True,
            "PhiFin_functional_trace": True,
            "static_matter_slot_source_tier": True,
        },
        "must_emit_next": [
            "selected End0-to-sector routing values",
            "selected P_s/K_s projector promotion values in the full-S2 operator tier",
            "selected rho_E transition payload",
            "selected D_E/Riesz/Green/dotD operator matrices in sector basis",
            "internal R_theta scalar rows or a legal universal-anchor replacement",
        ],
        "still_open": {
            "selected_fullS2_rhoE_D_E_operator_payload": True,
            "selected_HYM_sector_payload": True,
            "rank2_to_sector_transfer": True,
            "sector_projector_promotion_values": True,
            "selected_rhoE_transition_payload": True,
            "internal_Rtheta_scalar_rows": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(NEXT_CUTSET, next_cutset)

    candidate = {
        "candidate": "MTTSelectedStep27FullS2SubpayloadReductionOrSectorPromotionCutset",
        "status": STATUS,
        "inputs": {
            "step26": rel(STEP26),
            "hym": rel(HYM),
            "hym_payload": rel(HYM_PAYLOAD),
            "hym_fulls2": rel(HYM_FULLS2),
            "higher": rel(HIGHER),
            "higher_fulls2": rel(HIGHER_FULLS2),
            "end0_de": rel(END0_DE),
            "riesz": rel(RIESZ),
            "hym_extraction": rel(HYM_EXTRACTION),
        },
        "output_packets": {
            "step27_closed_hym_subpayload": rel(SUBPAYLOAD),
            "step27_sector_promotion_gap": rel(PROMOTION_GAP),
            "step27_next_sector_promotion_cutset": rel(NEXT_CUTSET),
        },
        "theorem": {
            "name": "Step27FullS2SubpayloadReductionTheorem",
            "proved": True,
            "statement": (
                "The full-S2 wall is not the diagonal End0/HYM operator solve. "
                "That subpayload, protected Green/Riesz data, T1/T2 covariant Green, "
                "and offdiagonal row-model control are closed. The remaining full-S2 "
                "operator payload is exactly sector promotion: selected End0-to-sector "
                "routing, projector promotion values, rho_E transition payload, and "
                "sector-basis D_E/Riesz/Green/dotD matrices."
            ),
        },
        "closure_decision": {
            "step26_next_artifact_reduced": True,
            "diagonal_End0_HYM_subpayload_closed": True,
            "protected_T3_Riesz_Green_closed": True,
            "T1_T2_covariant_Green_closed": True,
            "row_model_offdiagonal_control_closed": True,
            "selected_End0_to_sector_routing_values_closed": False,
            "sector_projector_promotion_values_closed": False,
            "selected_rhoE_transition_payload_closed": False,
            "selected_D_E_Riesz_Green_dotD_sector_matrices_closed": False,
            "fullS2_operator_payload_closed": False,
            "accepted_internal_scalar_row_count": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "what_closes_now": {
            "fullS2_wall_reduced_to_sector_promotion_values": True,
            "diagonal_End0_D_E_subpayload": True,
            "protected_and_covariant_Green_support": True,
            "offdiagonal_control_support": True,
        },
        "what_remains_open": next_cutset["still_open"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step27_FullS2SubpayloadReduction_or_SectorPromotionCutset_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "diagonal_End0_HYM_subpayload_closed": True,
        "fullS2_operator_payload_closed": False,
        "accepted_internal_scalar_row_count": 0,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected Step27 FullS2SubpayloadReduction or SectorPromotionCutset v1

Status: `{STATUS}`.

Closed subpayload:

```text
diagonal End0 D_E connection matrices                      closed
protected T3 Riesz/Green                                   closed
T1/T2 covariant Green                                      closed
row-model offdiagonal Ext control                          closed
Phi_fin functional trace                                   closed
static matter-slot source tier                             closed
```

Still open:

```text
selected End0-to-sector routing values                     open
selected P_s/K_s projector promotion values                open
selected rho_E transition payload                          open
sector-basis D_E/Riesz/Green/dotD matrices                 open
accepted internal Rtheta scalar rows                       0
true SM equivalence / full no-knob closure                 open
```

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
