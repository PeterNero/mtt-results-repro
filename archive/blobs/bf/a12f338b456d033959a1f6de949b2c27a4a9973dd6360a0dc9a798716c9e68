"""Build Step 28 sector-promotion reconciliation / operator-sector value cutset."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step28_sectorpromotion_reconciliation_or_operatorsectorvaluecutset"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
LOCKED = PACKET_DIR / "step28_locked_stationary_sector_promotions.packet.json"
FRONTIER = PACKET_DIR / "step28_refined_operator_sector_frontier.packet.json"
CONTRACT = PACKET_DIR / "step28_operator_sector_value_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step28_SectorPromotionReconciliation_or_OperatorSectorValueCutset_v1.md"

STEP17 = DATA / "selected_step17_projectorrhos_promotion_or_routecsolve.candidate.json"
STEP17_PROJECTOR = DATA / "selected_step17_projectorrhos_promotion_or_routecsolve" / "step17_selected_projector_rhos_promotion.packet.json"
STEP17_SOURCE = DATA / "selected_step17_projectorrhos_promotion_or_routecsolve" / "step17_projective_rhoe_source_boundary.packet.json"
STEP18 = DATA / "selected_step18_qasu3_alphadotd_import_or_primitivec1frontier.candidate.json"
STEP18_ALPHA = DATA / "selected_step18_qasu3_alphadotd_import_or_primitivec1frontier" / "step18_imported_qasu3_operator_alpha_dotd.packet.json"
STEP26 = DATA / "selected_step26_phifintrace_matterslot_reconciliation_or_fulls2payloadcutset.candidate.json"
STEP27 = DATA / "selected_step27_fulls2_subpayload_reduction_or_sectorpromotioncutset.candidate.json"
STEP27_GAP = DATA / "selected_step27_fulls2_subpayload_reduction_or_sectorpromotioncutset" / "step27_sector_promotion_gap.packet.json"
STEP27_CUTSET = DATA / "selected_step27_fulls2_subpayload_reduction_or_sectorpromotioncutset" / "step27_next_sector_promotion_cutset.packet.json"

STATUS = "MTT_SELECTED_STEP28_SECTORPROMOTION_RECONCILIATION_BUILT_STATIONARY_PROMOTION_LOCKED_OPERATORSECTOR_VALUES_OPEN"
NEXT = "MTT_Selected_Step29_OperatorSectorRhoEDEValues_or_InternalRThetaRows_v1"
SECTORS = ["Q", "u", "d", "L", "e", "N", "H"]


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

    inputs = [STEP17, STEP17_PROJECTOR, STEP17_SOURCE, STEP18, STEP18_ALPHA, STEP26, STEP27, STEP27_GAP, STEP27_CUTSET]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step 28 inputs: " + ", ".join(missing))

    step17 = load(STEP17)
    step17_projector = load(STEP17_PROJECTOR)
    step17_source = load(STEP17_SOURCE)
    step18 = load(STEP18)
    step18_alpha = load(STEP18_ALPHA)
    step26 = load(STEP26)
    step27 = load(STEP27)
    step27_gap = load(STEP27_GAP)
    step27_cutset = load(STEP27_CUTSET)

    locked = {
        "schema": "MTTStep28LockedStationarySectorPromotions.v1",
        "status": "STATIONARY_SECTOR_PROMOTIONS_LOCKED_DO_NOT_REOPEN",
        "from_step17": {
            "selected_projector_promotion_Ps_Ks_closed": step17["closure_decision"]["selected_projector_promotion_Ps_Ks_closed"],
            "selected_stationary_rho_s_matrix_values_closed": step17["closure_decision"]["selected_stationary_rho_s_matrix_values_closed"],
            "selected_projective_rhoE_source_level_closed": step17["closure_decision"]["selected_projective_rhoE_source_level_closed"],
            "operator_level_projective_rhoE_from_selected_connection_closed": step17["closure_decision"]["operator_level_projective_rhoE_from_selected_connection_closed"],
            "selected_DE_Riesz_Green_dotD_values_closed": step17["closure_decision"]["selected_DE_Riesz_Green_dotD_values_closed"],
        },
        "projector_packet": {
            "finite_projector_source_promotion_proved": step17_projector["finite_projector_source_promotion_proved"],
            "selected_projector_source_verified": step17_projector["selected_projector_source_verified"],
            "transported_packet_promoted": step17_projector["transported_packet_promoted"],
            "validator_ready_stationary_rho_s": step17_projector["validator_ready_stationary_rho_s"],
            "selected_dotD_source_verified": step17_projector["selected_dotD_source_verified"],
            "alpha1_driver_verified": step17_projector["alpha1_driver_verified"],
            "sector_summary": step17_projector["sector_summary"],
        },
        "from_step18": {
            "alpha1_dotD_driver_imported": step18["closure_decision"]["alpha1_dotD_driver_imported"],
            "honest_dotD_replay_imported": step18["closure_decision"]["honest_dotD_replay_imported"],
            "matter_slot_orientation_imported": step18["closure_decision"]["matter_slot_orientation_imported"],
            "operator_blocks_imported": step18["closure_decision"]["operator_blocks_imported"],
            "overlap_normalization_imported": step18["closure_decision"]["overlap_normalization_imported"],
            "selected_dotD_source_verified": step18_alpha["alpha_dotd_imported"]["selected_dotD_source_verified"],
            "alpha1_driver_verified": step18_alpha["alpha_dotd_imported"]["alpha1_driver_verified"],
        },
        "anti_reopen_rule": {
            "stationary_Ps_Ks": "closed by Step17",
            "stationary_rho_s": "closed by Step17",
            "source_level_projective_rhoE": "closed by Step17",
            "functional_matter_slot_blocks_and_normalization": "closed by Step18",
            "these_must_not_be_relisted_as_open_sector_promotion_items": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(LOCKED, locked)

    frontier = {
        "schema": "MTTStep28RefinedOperatorSectorFrontier.v1",
        "status": "SECTOR_PROMOTION_REFINED_TO_OPERATOR_LEVEL_RHOE_DE_RIESZ_GREEN_DOTD",
        "step27_wording_reconciled": True,
        "closed_from_step27": {
            "diagonal_End0_HYM_subpayload_closed": step27["closure_decision"]["diagonal_End0_HYM_subpayload_closed"],
            "protected_T3_Riesz_Green_closed": step27["closure_decision"]["protected_T3_Riesz_Green_closed"],
            "T1_T2_covariant_Green_closed": step27["closure_decision"]["T1_T2_covariant_Green_closed"],
            "row_model_offdiagonal_control_closed": step27["closure_decision"]["row_model_offdiagonal_control_closed"],
            "functional_PhiFin_trace_closed": step26["closure_decision"]["functional_PhiFin_trace_closed"],
            "static_U10_Ubar5_1M_source_closed": step26["closure_decision"]["static_U10_Ubar5_1M_source_closed"],
        },
        "retired_from_step27_open_list": {
            "selected_End0_to_sector_routing_values": "retired as stationary/functional routing by Step17+Step18",
            "selected_Ps_Ks_projector_promotion_values": "retired by Step17",
            "selected_stationary_rho_s_matrix_values": "retired by Step17",
            "source_level_projective_rhoE": "retired by Step17",
        },
        "still_open_after_reconciliation": {
            "operator_level_projective_rhoE_from_selected_connection": True,
            "selected_rhoE_transition_payload_in_fullS2_operator_tier": True,
            "selected_sector_basis_D_E_matrices": True,
            "selected_sector_basis_Riesz_projectors": True,
            "selected_sector_basis_Green_operators": True,
            "selected_sector_basis_dotD_matrices": True,
            "dynamic_PhiFin_C1_payload": True,
            "internal_Rtheta_scalar_rows": True,
            "lambda_H": True,
            "Yukawa_CKM_PMNS_mass_values": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "scalar_row_state": {
            "accepted_internal_scalar_row_count": step27["closure_decision"]["accepted_internal_scalar_row_count"],
            "value_functional_rows_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(FRONTIER, frontier)

    contract = {
        "schema": "MTTStep28OperatorSectorValueContract.v1",
        "status": "NEXT_CONTRACT_OPERATOR_LEVEL_VALUES_ONLY",
        "next_required_artifact": NEXT,
        "must_emit_next": [
            "selected projective rho_E transition operator induced by the selected connection, not only source-level gerbe rho_E",
            "sector-basis D_E matrices for Q,u,d,L,e,N,H in the Step17 stationary projector bases",
            "sector-basis Riesz projectors and reduced Green operators with complement-gap certificates",
            "sector-basis dotD matrices compatible with the Step18 alpha1 dotD driver and overlap normalization",
            "dynamic Phi_fin C1 payload or a legal replacement that makes internal R_theta scalar rows executable",
        ],
        "must_not_reopen": [
            "stationary transported P_s/K_s projector promotion",
            "stationary rho_s matrix values",
            "source-level projective S3 gerbe rho_E",
            "functional U10/Ubar5/1M matter-slot orientation",
            "rho_s(T_i)/sqrt(2) overlap normalization",
            "diagonal End0 D_E and Green subpayload",
        ],
        "acceptance_tests": {
            "all_sector_slots_present": SECTORS,
            "selected_source_flags_derived_by_theorem_not_flipped": True,
            "observed_masses_mixings_cp_not_inputs": True,
            "operator_payload_closes_fullS2_before_scalar_rows": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CONTRACT, contract)

    candidate = {
        "candidate": "MTTSelectedStep28SectorPromotionReconciliationOrOperatorSectorValueCutset",
        "status": STATUS,
        "inputs": {
            "step17": rel(STEP17),
            "step17_projector": rel(STEP17_PROJECTOR),
            "step17_source": rel(STEP17_SOURCE),
            "step18": rel(STEP18),
            "step18_alpha": rel(STEP18_ALPHA),
            "step26": rel(STEP26),
            "step27": rel(STEP27),
            "step27_gap": rel(STEP27_GAP),
            "step27_cutset": rel(STEP27_CUTSET),
        },
        "output_packets": {
            "locked_stationary_sector_promotions": rel(LOCKED),
            "refined_operator_sector_frontier": rel(FRONTIER),
            "operator_sector_value_contract": rel(CONTRACT),
        },
        "theorem": {
            "name": "Step28SectorPromotionReconciliationTheorem",
            "proved": True,
            "statement": (
                "The sector-promotion frontier after Step27 must be read with the active "
                "Step17 and Step18 ledger facts. Stationary transported projectors P_s/K_s, "
                "stationary rho_s matrices, source-level projective rho_E, functional "
                "matter-slot routing, and rho_s(T_i)/sqrt(2) normalization are closed and "
                "must not be reopened. The remaining full-S2 wall is operator-level: "
                "selected projective rho_E transition, sector-basis D_E/Riesz/Green/dotD, "
                "and then internal R_theta scalar rows."
            ),
        },
        "closure_decision": {
            "step27_sector_promotion_frontier_refined": True,
            "selected_stationary_End0_to_sector_routing_values_closed": True,
            "selected_projector_promotion_Ps_Ks_closed": True,
            "selected_stationary_rho_s_matrix_values_closed": True,
            "selected_projective_rhoE_source_level_closed": True,
            "functional_matter_slot_blocks_and_overlap_normalization_closed": True,
            "operator_level_projective_rhoE_from_selected_connection_closed": False,
            "selected_rhoE_transition_payload_fullS2_operator_tier_closed": False,
            "selected_sector_basis_D_E_Riesz_Green_dotD_matrices_closed": False,
            "dynamic_PhiFin_C1_payload_closed": False,
            "fullS2_operator_payload_closed": False,
            "accepted_internal_scalar_row_count": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "what_closes_now": {
            "anti_reopen_stationary_projector_rhos_promotion": True,
            "anti_reopen_source_level_projective_rhoE": True,
            "anti_reopen_functional_matter_slot_blocks": True,
            "step27_open_list_refined_to_operator_sector_values": True,
        },
        "what_remains_open": frontier["still_open_after_reconciliation"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step28_SectorPromotionReconciliation_or_OperatorSectorValueCutset_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "stationary_projector_rhos_promotion_locked": True,
        "operator_sector_values_closed": False,
        "accepted_internal_scalar_row_count": 0,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected Step28 SectorPromotionReconciliation or OperatorSectorValueCutset v1

Status: `{STATUS}`.

This step corrects the active plan boundary:

```text
stationary transported P_s/K_s projectors              closed by Step17
stationary rho_s matrix values                         closed by Step17
source-level projective S3 gerbe rho_E                 closed by Step17
functional U10/Ubar5/1M matter-slot blocks             closed by Step18
rho_s(T_i)/sqrt(2) overlap normalization               closed by Step18
diagonal End0 D_E / protected Green subpayload         closed by Step27
operator-level projective rho_E transition             open
sector-basis D_E/Riesz/Green/dotD matrices             open
internal R_theta scalar rows                           open
true SM equivalence / full no-knob closure             open
```

The mistake this prevents is reopening stationary sector promotion whenever
Step27 says "sector promotion."  The only live meaning after reconciliation is
operator-sector value promotion in the full-S2 tier.

Next artifact: `{NEXT}`.

No observed masses, mixings, CP phases, or benchmark rows are used as selectors.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
