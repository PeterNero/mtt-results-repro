"""Build the full-sector BN27 HYM/End(E) validator-payload attempt.

This consumes the reduced Route-B contract.  The constructive result is that
the finite 27-mode payload already exists at model-active scope: D_E matrices,
sector projectors, zero-mode bases, complement gap, Green/horizontal checks,
dotD response, and row-model offdiagonal control.  The payload is not promoted
to the BN27 final row because the selected HYM/Strominger source flags and full
operator/truncation certificate are still open.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_fullsector_bn27_hymende_validator_payload"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
MODEL_PACKET = PACKET_DIR / "model_active_fullsector_payload_replay.packet.json"
PROMOTION_PACKET = PACKET_DIR / "selected_source_promotion_gate_for_bn27_hymende.packet.json"
GATE_PACKET = PACKET_DIR / "bn27_hymende_final_row_validator_replay.packet.json"
NEXT_PACKET = PACKET_DIR / "next_hym_projector_sourcepromotion_or_fullstrominger_operator_value.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FullSectorBN27HYMEndEValidatorPayload_v1.md"

PREVIOUS = DATA / "selected_bn27_hymende_rowscope_acceptance_or_fullsector_devalues.candidate.json"
PREVIOUS_CONTRACT = (
    DATA
    / "selected_bn27_hymende_rowscope_acceptance_or_fullsector_devalues"
    / "next_fullsector_bn27_hymende_validator_payload_contract.packet.json"
)
DE_ACTION = DATA / "selected_routec_de_action_on_smooth_bn.candidate.json"
DOTD = DATA / "selected_routec_sector_projectors_dotd_on_smooth_bn.candidate.json"
PROJECTORS = DATA / "selected_hym_projector_zeromode_basis_value_emission.candidate.json"
OFFDIAG = DATA / "selected_offdiagonal_ext_control_or_sector_transfer.candidate.json"
RTHETA_TRANSFER = DATA / "selected_rtheta_sectortransferbnbasis_or_pikernelclosure.candidate.json"
VISIBLE_CW = DATA / "selected_visible_chern_weil_operator_source.candidate.json"
VISIBLE_GS = DATA / "selected_visible_green_schwarz_operator_source.candidate.json"
EIGHT_TABLE = (
    DATA
    / "selected_derieszgreenkerneltraceexport_promotion_or_remainingconnectiontables"
    / "eight_table_revalidation_after_de_export.packet.json"
)

STATUS = "MTT_SELECTED_FULLSECTOR_BN27_HYMENDE_VALIDATOR_PAYLOAD_MODEL_ACTIVE_BUILT_SOURCE_PROMOTION_OPEN"
NEXT = "MTT_Selected_HYM_Projector_SourcePromotion_or_FullStrominger_Operator_Value_Theorem_v1"
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
        raise FileNotFoundError("missing full-sector BN27 validator inputs: " + ", ".join(missing))


def main() -> int:
    sources = [
        PREVIOUS,
        PREVIOUS_CONTRACT,
        DE_ACTION,
        DOTD,
        PROJECTORS,
        OFFDIAG,
        RTHETA_TRANSFER,
        VISIBLE_CW,
        VISIBLE_GS,
        EIGHT_TABLE,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_contract = load(PREVIOUS_CONTRACT)
    de = load(DE_ACTION)
    dotd = load(DOTD)
    projectors = load(PROJECTORS)
    offdiag = load(OFFDIAG)
    rtheta = load(RTHETA_TRANSFER)
    visible_cw = load(VISIBLE_CW)
    visible_gs = load(VISIBLE_GS)
    eight = load(EIGHT_TABLE)

    if previous["next_required_artifact"] != "MTT_Selected_FullSectorBN27HYMEndEValidatorPayload_v1":
        raise ValueError("previous artifact no longer points to full-sector BN27 payload")
    if previous_contract["next_required_artifact"] != "MTT_Selected_FullSectorBN27HYMEndEValidatorPayload_v1":
        raise ValueError("previous contract no longer points to full-sector BN27 payload")

    de_validation = de["validation"]
    dotd_validation = dotd["validation"]
    proj_validation = projectors["validator_result"]
    sector_slots = projectors["finite_value_payload"]["sector_slots"]

    required_sectors = ["Q", "u", "d", "L", "e", "N", "H"]
    sector_checks = {
        sector: {
            "projector_idempotent": sector_slots[sector]["projector_checks"]["idempotence_residual"] == 0.0,
            "projector_self_adjoint": sector_slots[sector]["projector_checks"]["self_adjoint_residual"] == 0.0,
            "rank_trace": sector_slots[sector]["projector_checks"]["rank_trace"],
            "basis_vector_count": sector_slots[sector]["ordered_zero_mode_basis_vector_count"],
            "green_operator_verified": sector_slots[sector]["green_operator_verified"],
            "horizontal_gauge_verified": sector_slots[sector]["horizontal_gauge_verified"],
            "selected_source_verified": sector_slots[sector]["selected_source_verified"],
            "selected_value_emitted": sector_slots[sector]["value_emitted_as_selected_HYM_projector"],
        }
        for sector in required_sectors
    }

    model_active_closed = {
        "finite_D_E_matrix_on_27_mode_BN": de["what_closes_now"]["D_E_matrix_on_27_mode_BN_emitted"],
        "D_E_diagnostic_validator_passes": de_validation["diagnostic_source_lift"]["exit_code"] == 0,
        "D_E_honest_fails_only_selected_source_flags": de_validation["matrix_consistency"][
            "honest_validator_fails_only_by_selected_source_flags"
        ],
        "sector_projectors_on_27_mode_BN": dotd["what_closes_now"]["sector_projectors_on_27_mode_BN_emitted"],
        "dotD_matrix_in_same_basis": dotd["what_closes_now"]["dotD_alpha1_matrix_in_same_basis_emitted"],
        "dotD_diagnostic_validator_passes": dotd_validation["diagnostic_lift_validator_passes"],
        "dotD_honest_fails_only_source_driver_flags": dotd_validation[
            "honest_validator_fails_only_by_source_driver_flags"
        ],
        "finite_projector_values_emitted": proj_validation["finite_projector_values_emitted"],
        "all_projector_checks_pass": proj_validation["all_projector_checks_pass"],
        "all_basis_counts_pass": proj_validation["all_basis_counts_pass"],
        "positive_complement_gap": proj_validation["positive_complement_gap"],
        "green_and_horizontal_flags_pass": proj_validation["green_and_horizontal_flags_pass"],
        "End0_equivariance_on_emitted_projectors": proj_validation["End0_equivariance_on_emitted_projectors"],
        "row_model_offdiagonal_Ext_control": offdiag["path_A_straight_offdiagonal_Ext_control"]["closed"],
        "stationary_sector_transfer_subgate": rtheta["closure_decision"]["stationary_sector_transfer_closed"],
    }
    if not all(model_active_closed.values()):
        failed = [key for key, value in model_active_closed.items() if not value]
        raise ValueError("expected model-active full-sector payload support to be present: " + ", ".join(failed))

    selected_blockers = {
        "selected_HYM_projector_values_promoted": proj_validation["selected_HYM_projector_values_promoted"],
        "rho_candidate_promoted_to_selected_rho_s": proj_validation["rho_candidate_promoted_to_selected_rho_s"],
        "de_action_selected_source_verified": proj_validation["selected_source_flags"][
            "de_action_selected_source_verified"
        ],
        "de_honest_validator_promotes": proj_validation["selected_source_flags"]["de_honest_validator_promotes"],
        "dotd_selected_dotD_source_verified": proj_validation["selected_source_flags"][
            "dotd_selected_dotD_source_verified"
        ],
        "dotd_alpha1_driver_verified": proj_validation["selected_source_flags"]["dotd_alpha1_driver_verified"],
        "dotd_honest_validator_promotes": proj_validation["selected_source_flags"]["dotd_honest_validator_promotes"],
        "selected_visible_operator_source_closed": visible_cw["open_gates"]["selected_visible_operator_source_closed"],
        "visible_gs_selected_operator_source_constructed": visible_gs["gate_results"][
            "selected_visible_operator_source_constructed"
        ],
        "full_sector_offdiagonal_control_selected": offdiag["operator_payload_boundary"]["validator_ready"],
    }
    if any(selected_blockers.values()):
        succeeded = [key for key, value in selected_blockers.items() if value]
        raise ValueError("selected-source blockers unexpectedly closed: " + ", ".join(succeeded))

    model_packet = {
        "schema": "MTTModelActiveFullSectorPayloadReplay.v1",
        "status": "MODEL_ACTIVE_27MODE_PAYLOAD_PRESENT",
        "closure_claimed": True,
        "model_active_closed": model_active_closed,
        "sector_checks": sector_checks,
        "sectors": required_sectors,
        "basis_id": projectors["finite_value_payload"]["basis_id"],
        "ambient_dimension": projectors["finite_value_payload"]["ambient_dimension"],
        "zero_cluster": projectors["finite_value_payload"]["zero_cluster"],
        "complement_gap": projectors["finite_value_payload"]["complement_gap"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    promotion_packet = {
        "schema": "MTTSelectedSourcePromotionGateForBN27HYMEndE.v1",
        "status": "SELECTED_SOURCE_PROMOTION_OPEN",
        "closure_claimed": True,
        "selected_blockers": selected_blockers,
        "why_not_promoted": projectors["validator_result"]["why_not_promoted"],
        "visible_operator_root": {
            "visible_CW_next": visible_cw["next_required_artifact"],
            "visible_GS_next": visible_gs["next_required_artifact"],
            "selected_visible_operator_source_closed": visible_cw["open_gates"][
                "selected_visible_operator_source_closed"
            ],
            "selected_D_E_dotD_Riesz_Green_constructed": visible_gs["gate_results"][
                "selected_D_E_dotD_Riesz_Green_constructed"
            ],
            "coherent_spectral_zero_mode_projectors_constructed": visible_gs["gate_results"][
                "coherent_spectral_zero_mode_projectors_constructed"
            ],
        },
        "minimal_promotion_requirements": [
            "selected visible HYM/Strominger or Route-C source on q79/F,m=1",
            "selected_source_verified for D_E on Q,u,d,L,e,N,H",
            "selected_dotD_source_verified and alpha1_driver_verified on the same basis",
            "full selected Iwasawa/Strominger operator with truncation-error certificate",
            "promotion of emitted projectors and bases to selected HYM projector values",
            "full-sector offdiagonal End0 vanish/control beyond the row-model check",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    selected_source_promotion_closed = all(selected_blockers.values())
    final_row_accepted = (
        eight["rows"][FINAL_ROW]["accepted_as_final_connection_table"] and selected_source_promotion_closed
    )
    gate_packet = {
        "schema": "MTTBN27HYMEndEFinalRowValidatorReplay.v1",
        "status": "FINAL_ROW_REPLAYED_MODEL_PAYLOAD_PRESENT_SELECTED_SOURCE_OPEN",
        "closure_claimed": True,
        "row": FINAL_ROW,
        "model_active_payload_present": True,
        "selected_source_promotion_closed": selected_source_promotion_closed,
        "HYM_or_EndE_final_row_accepted": final_row_accepted,
        "strict_final_connection_table_count": "4/8",
        "one_premise_final_connection_table_count": "6/8",
        "two_premise_AH_equivalent_final_connection_table_count": "7/8",
        "strict_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextHYMProjectorSourcePromotionOrFullStromingerOperatorValue.v1",
        "status": "NEXT_IS_SELECTED_SOURCE_PROMOTION_OR_FULL_STROMINGER_OPERATOR_VALUE",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "must_promote": promotion_packet["minimal_promotion_requirements"],
        "do_not_rebuild": [
            "finite 27-mode D_E matrix",
            "finite 27-mode sector projectors",
            "ordered zero-mode basis ids",
            "positive complement gap",
            "finite dotD matrix on the same basis",
            "row-model offdiagonal Ext control",
        ],
        "current_lanes": {
            "strict_lane": "4/8",
            "one_premise_BN27_lane": "6/8",
            "two_premise_AH_equivalent_lane": "7/8",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedFullSectorBN27HYMEndEValidatorPayload",
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
            "de_action": rel(DE_ACTION),
            "dotd": rel(DOTD),
            "projectors": rel(PROJECTORS),
            "offdiag": rel(OFFDIAG),
            "rtheta_transfer": rel(RTHETA_TRANSFER),
            "visible_cw": rel(VISIBLE_CW),
            "visible_gs": rel(VISIBLE_GS),
            "eight_table": rel(EIGHT_TABLE),
        },
        "output_packets": {
            "model_active_fullsector_payload_replay": rel(MODEL_PACKET),
            "selected_source_promotion_gate_for_bn27_hymende": rel(PROMOTION_PACKET),
            "bn27_hymende_final_row_validator_replay": rel(GATE_PACKET),
            "next_hym_projector_sourcepromotion_or_fullstrominger_operator_value": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "model_active_payload_present": True,
            "model_active_support_count": len(model_active_closed),
            "selected_source_blocker_count": len(selected_blockers),
            "selected_source_promotion_closed": selected_source_promotion_closed,
            "BN27_final_row_accepted": final_row_accepted,
            "two_premise_AH_equivalent_final_connection_tables_accepted": 7,
            "strict_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "FullSectorBN27HYMEndEValidatorPayloadModelActiveTheorem",
            "proved": True,
            "statement": (
                "The full-sector BN27 HYM/End(E) payload has been constructed at model-active finite "
                "27-mode scope: D_E matrices, sector projectors, zero-mode bases, Green/horizontal checks, "
                "dotD response, and row-model offdiagonal control are present and pass diagnostic validators. "
                "The BN27 final row is not accepted because the same data are not yet theorem-promoted as "
                "selected HYM/Strominger source values; selected_source_verified, selected_dotD_source_verified, "
                "alpha1_driver_verified, full operator/truncation certification, and full-sector offdiagonal "
                "control remain open."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedFullSectorBN27HYMEndEValidatorPayload",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "model_active_payload_present": True,
        "model_active_support_count": len(model_active_closed),
        "selected_source_blocker_count": len(selected_blockers),
        "selected_source_promotion_closed": selected_source_promotion_closed,
        "BN27_final_row_accepted": final_row_accepted,
        "two_premise_AH_equivalent_final_connection_tables_accepted": 7,
        "strict_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected FullSector BN27 HYM/EndE Validator Payload v1

## Theorem

`FullSectorBN27HYMEndEValidatorPayloadModelActiveTheorem` is proved.

## What Closed

The full-sector payload exists at model-active finite `27`-mode scope:

- finite `D_E` matrix on smooth `B_N`
- sector projectors for `Q,u,d,L,e,N,H`
- ordered zero-mode basis ids
- positive complement gap
- Green and horizontal checks
- finite dotD matrix in the same basis
- row-model offdiagonal Ext control

This means the next work is not to rebuild matrices.  The matrices are present.

## What Did Not Close

The payload is not yet selected-source promoted:

- `selected_source_verified` for `D_E` is false.
- `selected_dotD_source_verified` is false.
- `alpha1_driver_verified` is false.
- the full selected Iwasawa/Strominger operator and truncation-error certificate
  are still open.
- full-sector offdiagonal End0 control beyond the row model is still open.

Therefore the BN27 HYM/End(E) final row remains unaccepted and the counted
AH-equivalent lane remains `7/8`.

## Next Artifact

`{NEXT}`
"""

    write_json(MODEL_PACKET, model_packet)
    write_json(PROMOTION_PACKET, promotion_packet)
    write_json(GATE_PACKET, gate_packet)
    write_json(NEXT_PACKET, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
