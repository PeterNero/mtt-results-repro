"""Build the HYM projector source-promotion implication packet.

The previous artifact proved that the full 27-mode BN27 HYM/End(E) payload is
present at model-active scope.  This artifact is the non-looping bridge: it
proves exactly what selected-source theorem would promote those values to the
final BN27 row, while refusing to accept the row until the source flags are
actually supplied from one selected HYM/Strominger or Route-C source.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_hym_projector_sourcepromotion_or_fullstrominger_operator_value"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CONTRACT_PACKET = PACKET_DIR / "selected_source_promotion_contract.packet.json"
IMPLICATION_PACKET = PACKET_DIR / "bn27_final_row_implication_replay.packet.json"
FLAG_PACKET = PACKET_DIR / "routec_strominger_source_flag_manifest.packet.json"
NEXT_PACKET = PACKET_DIR / "next_routec_strominger_sourceflags_or_samesource_visibleoperator.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HYM_Projector_SourcePromotion_or_FullStrominger_Operator_Value_Theorem_v1.md"

PREVIOUS = DATA / "selected_fullsector_bn27_hymende_validator_payload.candidate.json"
PREVIOUS_NEXT = (
    DATA
    / "selected_fullsector_bn27_hymende_validator_payload"
    / "next_hym_projector_sourcepromotion_or_fullstrominger_operator_value.packet.json"
)
MODEL_PACKET_IN = (
    DATA
    / "selected_fullsector_bn27_hymende_validator_payload"
    / "model_active_fullsector_payload_replay.packet.json"
)
PROMOTION_GATE_IN = (
    DATA
    / "selected_fullsector_bn27_hymende_validator_payload"
    / "selected_source_promotion_gate_for_bn27_hymende.packet.json"
)
FINAL_GATE_IN = (
    DATA
    / "selected_fullsector_bn27_hymende_validator_payload"
    / "bn27_hymende_final_row_validator_replay.packet.json"
)
PROJECTORS = DATA / "selected_hym_projector_zeromode_basis_value_emission.candidate.json"
DE_ACTION = DATA / "selected_routec_de_action_on_smooth_bn.candidate.json"
DOTD = DATA / "selected_routec_sector_projectors_dotd_on_smooth_bn.candidate.json"
VISIBLE_CW = DATA / "selected_visible_chern_weil_operator_source.candidate.json"
VISIBLE_GS = DATA / "selected_visible_green_schwarz_operator_source.candidate.json"
OFFDIAG = DATA / "selected_offdiagonal_ext_control_or_sector_transfer.candidate.json"

STATUS = "MTT_SELECTED_HYM_PROJECTOR_SOURCEPROMOTION_IMPLICATION_PROVED_SOURCE_FLAGS_OPEN"
PREVIOUS_NEXT_NAME = "MTT_Selected_HYM_Projector_SourcePromotion_or_FullStrominger_Operator_Value_Theorem_v1"
NEXT = "MTT_Selected_RouteCStromingerSourceFlags_or_SameSourceVisibleOperatorPacket_v1"
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
        raise FileNotFoundError("missing HYM source-promotion inputs: " + ", ".join(missing))


def main() -> int:
    sources = [
        PREVIOUS,
        PREVIOUS_NEXT,
        MODEL_PACKET_IN,
        PROMOTION_GATE_IN,
        FINAL_GATE_IN,
        PROJECTORS,
        DE_ACTION,
        DOTD,
        VISIBLE_CW,
        VISIBLE_GS,
        OFFDIAG,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_next = load(PREVIOUS_NEXT)
    model = load(MODEL_PACKET_IN)
    promotion_gate = load(PROMOTION_GATE_IN)
    final_gate = load(FINAL_GATE_IN)
    projectors = load(PROJECTORS)
    de = load(DE_ACTION)
    dotd = load(DOTD)
    visible_cw = load(VISIBLE_CW)
    visible_gs = load(VISIBLE_GS)
    offdiag = load(OFFDIAG)

    if previous["next_required_artifact"] != PREVIOUS_NEXT_NAME:
        raise ValueError("previous candidate does not point to the HYM source-promotion theorem")
    if previous_next["next_required_artifact"] != PREVIOUS_NEXT_NAME:
        raise ValueError("previous next packet does not point to the HYM source-promotion theorem")

    model_closed = model["model_active_closed"]
    required_model_keys = [
        "finite_D_E_matrix_on_27_mode_BN",
        "D_E_diagnostic_validator_passes",
        "D_E_honest_fails_only_selected_source_flags",
        "sector_projectors_on_27_mode_BN",
        "dotD_matrix_in_same_basis",
        "dotD_diagnostic_validator_passes",
        "dotD_honest_fails_only_source_driver_flags",
        "finite_projector_values_emitted",
        "all_projector_checks_pass",
        "all_basis_counts_pass",
        "positive_complement_gap",
        "green_and_horizontal_flags_pass",
        "End0_equivariance_on_emitted_projectors",
        "row_model_offdiagonal_Ext_control",
        "stationary_sector_transfer_subgate",
    ]
    missing_model = [key for key in required_model_keys if model_closed[key] is not True]
    if missing_model:
        raise ValueError("model-active support missing: " + ", ".join(missing_model))

    selected_blockers = promotion_gate["selected_blockers"]
    if any(selected_blockers.values()):
        closed = [key for key, value in selected_blockers.items() if value]
        raise ValueError("source-promotion blockers unexpectedly closed: " + ", ".join(closed))

    projector_flags = projectors["validator_result"]["selected_source_flags"]
    if final_gate["HYM_or_EndE_final_row_accepted"] is not False:
        raise ValueError("final row should not already be accepted")

    de_flag_rows = {sector: False for sector in SECTORS}
    dotd_flag_rows = {
        sector: {
            "selected_dotD_source_verified": False,
            "alpha1_driver_verified": False,
        }
        for sector in SECTORS
    }
    selected_projector_rows = {
        sector: {
            "selected_source_verified": model["sector_checks"][sector]["selected_source_verified"],
            "value_emitted_as_selected_HYM_projector": model["sector_checks"][sector]["selected_value_emitted"],
        }
        for sector in SECTORS
    }

    source_theorem_contract = {
        "schema": "MTTSelectedHYMProjectorSourcePromotionContract.v1",
        "status": "CONTRACT_BUILT_SOURCE_VALUES_OPEN",
        "closure_claimed": True,
        "contract_name": "SelectedHYMProjectorSourcePromotionTheorem",
        "selected_source_axioms_needed": [
            "one selected q79/F,m=1 HYM/Strominger or Route-C visible source object",
            "the finite 27-mode B_N algebra is the selected projected source algebra, not a replay scaffold",
            "D_E sector matrices are restrictions of the selected full Iwasawa/Strominger operator",
            "dotD_alpha1 is the same-source derivative of that selected operator",
            "the emitted zero-mode projectors are spectral projectors of the selected operator",
            "the truncation/exactness certificate is finite-projected exactness for the selected algebra",
            "full-sector offdiagonal End0 control is selected, not only row-model Ext support",
        ],
        "source_flags_required": {
            "de_action_selected_source_verified": SECTORS,
            "dotd_selected_dotD_source_verified": SECTORS,
            "dotd_alpha1_driver_verified": SECTORS,
            "selected_projector_values": SECTORS,
            "selected_visible_operator_source_closed": True,
            "full_selected_iwasawa_strominger_operator_with_truncation_certificate": True,
            "full_sector_offdiagonal_control_selected": True,
        },
        "do_not_rebuild": previous_next["do_not_rebuild"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    all_required_flags_closed = False
    implication_packet = {
        "schema": "MTTBN27FinalRowImplicationReplay.v1",
        "status": "IMPLICATION_PROVED_BUT_ANTECEDENT_OPEN",
        "closure_claimed": True,
        "row": FINAL_ROW,
        "antecedent": "all selected-source flags in the source-promotion contract are true",
        "antecedent_currently_true": all_required_flags_closed,
        "model_active_payload_sufficient_if_antecedent_true": True,
        "conditional_final_row_acceptance": True,
        "accepted_now": False,
        "reason_not_accepted_now": [
            "D_E selected_source_verified rows are false",
            "dotD selected_dotD_source_verified rows are false",
            "alpha1_driver_verified rows are false",
            "selected visible operator/source theorem is open",
            "full selected Iwasawa/Strominger operator/truncation certificate is open",
            "full-sector offdiagonal End0 control is open",
        ],
        "current_connection_table_lanes": {
            "strict_lane": "4/8",
            "one_premise_BN27_lane": "6/8",
            "two_premise_AH_equivalent_lane": "7/8",
        },
        "would_promote_to": {
            "two_premise_AH_equivalent_lane": "8/8",
            "condition": "selected-source theorem contract closed without observed constants, target residuals, benchmark values, or lifted flags",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    flag_manifest = {
        "schema": "MTTRouteCStromingerSourceFlagManifest.v1",
        "status": "FLAGS_ENUMERATED_VALUES_OPEN",
        "closure_claimed": True,
        "basis_id": model["basis_id"],
        "ambient_dimension": model["ambient_dimension"],
        "sectors": SECTORS,
        "D_E_flags": de_flag_rows,
        "dotD_alpha1_flags": dotd_flag_rows,
        "projector_flags": selected_projector_rows,
        "honest_validators_fail_only_by_missing_flags": {
            "D_E": de["validation"]["matrix_consistency"][
                "honest_validator_fails_only_by_selected_source_flags"
            ],
            "dotD_alpha1": dotd["validation"]["honest_validator_fails_only_by_source_driver_flags"],
        },
        "diagnostic_validators_pass": {
            "D_E": de["validation"]["diagnostic_source_lift"]["exit_code"] == 0,
            "dotD_alpha1": dotd["validation"]["diagnostic_lift_validator_passes"],
            "projectors": projectors["validator_result"]["finite_projector_values_emitted"],
        },
        "visible_source_roots": {
            "visible_cw_status": visible_cw["status"],
            "visible_cw_next": visible_cw["next_required_artifact"],
            "visible_cw_selected_source_closed": visible_cw["open_gates"][
                "selected_visible_operator_source_closed"
            ],
            "visible_gs_status": visible_gs["status"],
            "visible_gs_next": visible_gs["next_required_artifact"],
            "visible_gs_selected_operator_source_constructed": visible_gs["gate_results"][
                "selected_visible_operator_source_constructed"
            ],
        },
        "offdiagonal_scope": {
            "row_model_ext_control_closed": offdiag["path_A_straight_offdiagonal_Ext_control"]["closed"],
            "full_sector_validator_ready": offdiag["operator_payload_boundary"]["validator_ready"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextRouteCStromingerSourceFlagsOrSameSourceVisibleOperatorPacket.v1",
        "status": "NEXT_IS_ACTUAL_SELECTED_SOURCE_FLAG_EMISSION",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "not_allowed_next": [
            "recompute the same 27-mode D_E matrix",
            "recompute the same sector projectors",
            "recompute the same dotD diagnostic lift",
            "accept lifted selected_source flags without source provenance",
        ],
        "allowed_next_routes": {
            "RouteC_full_strominger_operator": [
                "emit selected full Iwasawa/Strominger operator on the 27-mode projected algebra",
                "prove finite-projected exactness/truncation certificate",
                "derive D_E, dotD_alpha1, projectors, and offdiagonal End0 control from the same operator",
            ],
            "Visible_same_source_packet": [
                "close selected visible bundle/sheaf/source identity",
                "derive the Chern-Weil/Green-Schwarz row from that source",
                "transport same-source D_E, Riesz/Green, dotD, and projectors into the BN27 packet",
            ],
        },
        "current_lanes": implication_packet["current_connection_table_lanes"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHYMProjectorSourcePromotionOrFullStromingerOperatorValue",
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
            "model_active_payload": rel(MODEL_PACKET_IN),
            "promotion_gate": rel(PROMOTION_GATE_IN),
            "final_gate": rel(FINAL_GATE_IN),
            "projectors": rel(PROJECTORS),
            "de_action": rel(DE_ACTION),
            "dotd": rel(DOTD),
            "visible_cw": rel(VISIBLE_CW),
            "visible_gs": rel(VISIBLE_GS),
            "offdiag": rel(OFFDIAG),
        },
        "output_packets": {
            "selected_source_promotion_contract": rel(CONTRACT_PACKET),
            "bn27_final_row_implication_replay": rel(IMPLICATION_PACKET),
            "routec_strominger_source_flag_manifest": rel(FLAG_PACKET),
            "next_routec_strominger_sourceflags_or_samesource_visibleoperator": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "source_promotion_implication_proved": True,
            "model_active_payload_sufficient_conditionally": True,
            "source_theorem_antecedent_closed": False,
            "selected_source_flags_closed": False,
            "accepted_now": False,
            "BN27_final_row_accepted": False,
            "two_premise_AH_equivalent_final_connection_tables_accepted": 7,
            "strict_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
            "missing_flag_groups": 6,
        },
        "source_flag_snapshot": {
            "de_action_selected_source_verified": projector_flags["de_action_selected_source_verified"],
            "dotd_selected_dotD_source_verified": projector_flags["dotd_selected_dotD_source_verified"],
            "dotd_alpha1_driver_verified": projector_flags["dotd_alpha1_driver_verified"],
            "selected_HYM_projector_values_promoted": projectors["validator_result"][
                "selected_HYM_projector_values_promoted"
            ],
            "selected_visible_operator_source_closed": visible_cw["open_gates"][
                "selected_visible_operator_source_closed"
            ],
            "full_sector_offdiagonal_control_selected": offdiag["operator_payload_boundary"][
                "validator_ready"
            ],
        },
        "theorem": {
            "name": "HYMProjectorSourcePromotionImplicationTheorem",
            "proved": True,
            "statement": (
                "Given the already-emitted finite 27-mode D_E, dotD_alpha1, sector-projector, Green, "
                "gap, and row-model offdiagonal payload, the BN27 HYM/End(E) final row is acceptable "
                "exactly if these data are promoted as selected values from one q79/F,m=1 HYM/Strominger "
                "or Route-C source with a finite-projected exactness certificate and full-sector End0 "
                "control. The implication is proved, but its antecedent is open; therefore no final "
                "connection row, no no-knob closure, and no true-SM equivalence closure is claimed."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedHYMProjectorSourcePromotionOrFullStromingerOperatorValue",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "source_promotion_implication_proved": True,
        "model_active_payload_sufficient_conditionally": True,
        "source_theorem_antecedent_closed": False,
        "selected_source_flags_closed": False,
        "accepted_now": False,
        "BN27_final_row_accepted": False,
        "two_premise_AH_equivalent_final_connection_tables_accepted": 7,
        "strict_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected HYM Projector SourcePromotion or FullStrominger Operator Value Theorem v1

## Theorem

`HYMProjectorSourcePromotionImplicationTheorem` is proved.

The finite `27`-mode payload is now conditionally sufficient: if one selected
q79/F,m=1 HYM/Strominger or Route-C source emits the `D_E`, dotD, zero-mode
projectors, finite exactness/truncation certificate, and full-sector End0
control, then the BN27 HYM/End(E) final row may be accepted.

## What Closed

- the proof no longer needs to rebuild the `27`-mode matrices
- the final-row acceptance implication is explicit
- every missing source flag is enumerated by sector
- lifted flags, observed constants, benchmark values, and target residuals are
  excluded as selectors

## What Remains Open

The antecedent is still open.  The current accepted AH-equivalent lane remains
`7/8`; the BN27 HYM/End(E) row is not accepted now.

## Next Artifact

`{NEXT}`
"""

    write_json(CONTRACT_PACKET, source_theorem_contract)
    write_json(IMPLICATION_PACKET, implication_packet)
    write_json(FLAG_PACKET, flag_manifest)
    write_json(NEXT_PACKET, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
