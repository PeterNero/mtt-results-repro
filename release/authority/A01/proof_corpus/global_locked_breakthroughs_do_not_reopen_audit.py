from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def require_status(path: str, expected: str) -> dict:
    data = load_json(path)
    require(data.get("status") == expected, f"{path} has unexpected status: {data.get('status')}")
    return data


def main() -> None:
    q27 = require_status(
        "certificates/selected_qutrit27matrixminimalclosure_or_strictpewupgrade_certificate.json",
        "MTT_SELECTED_QUTRIT27MATRIXMINIMALCLOSURE_OR_STRICTPEWUPGRADE_TEN_ROW_MINIMAL_LEDGER_CLOSED_STRICT_PEW_OPEN",
    )
    yukawa = require_status(
        "certificates/selected_finalyukawareplayresidualexactness_or_strictsmnoknobclosure_certificate.json",
        "MTT_SELECTED_FINALYUKAWAREPLAYRESIDUALEXACTNESS_BUILT_FINITE_REPLAY_YUKAWA_CLOSED_TRUE_SM_OPEN",
    )
    pi_ckm = require_status(
        "certificates/selected_pickmnumeratorbranchretentionprinciple_or_weightrows_certificate.json",
        "MTT_SELECTED_PICKM_NUMERATOR_BRANCH_RETENTION_PROVED_WEIGHT_ROWS_EMITTED_EXACT_CKM_OPEN",
    )
    pi_ckm_residual = require_status(
        "certificates/selected_pickmweightrows_ckmresidualdecision_or_higherorderclosure_certificate.json",
        "MTT_SELECTED_PICKM_WEIGHT_ROWS_RESIDUAL_CAUSE_AUDITED_HIGHERORDER_OR_PROFILE_OPEN",
    )
    require_status(
        "certificates/selected_ckmpmnsrows_or_higgsthresholdstrictpewexit_certificate.json",
        "MTT_SELECTED_CKMPMNSROWS_OR_HIGGSTHRESHOLDSTRICTPEWEXIT_BUILT_CKM_WEIGHTROWS_CLOSED_PMNS_HIGGS_PEW_OPEN",
    )
    ah8 = require_status(
        "certificates/selected_strictglobalcechhym_or_truesmafterah8_certificate.json",
        "MTT_SELECTED_STRICTGLOBALCECHHYM_OR_TRUESMAFTERAH8_AH8_CONSUMED_STRICT_WITNESSES_AND_PRECISION_VALUES_OPEN",
    )
    route_a = require_status(
        "certificates/selected_gaugetransported_bn_phifin_trace_or_independentcomplexrowexecution_certificate.json",
        "MTT_SELECTED_GAUGETRANSPORTED_BN_PHIFIN_TRACE_OR_INDEPENDENTCOMPLEXROWEXECUTION_ROUTE_A_SOURCE_PROMOTION_CLOSED_FULLSM_OPEN",
    )
    post_source = require_status(
        "certificates/selected_postsourcepromotionfullsmgapaudit_or_dotdalpha1matterroutingclosure_certificate.json",
        "MTT_SELECTED_POSTSOURCEPROMOTIONFULLSMGAPAUDIT_OR_DOTDALPHA1MATTERROUTINGCLOSURE_BUILT_ALPHA1_CLOSED_STATIC_MATTER_CLOSED_DYNAMIC_FULLSM_OPEN",
    )
    dynamic_overlap = require_status(
        "certificates/selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure_certificate.json",
        "MTT_SELECTED_SAMESOURCEDYNAMICMATTEROVERLAPOPERATORPACKET_OR_PRIMITIVEC1VALUECLOSURE_BUILT_DYNAMIC_MATTER_PACKET_VALIDATES_YUKAWA_MAGNITUDES_OPEN",
    )
    dynamic_qasu3 = require_status(
        "certificates/selected_dynamicqasu3operatorpacketreplay_or_yukawamassmixingvalueclosure_certificate.json",
        "MTT_SELECTED_DYNAMICQASU3OPERATORPACKETREPLAY_OR_YUKAWAMASSMIXINGVALUECLOSURE_BUILT_DYNAMIC_PACKET_REPLAYED_VALUE_CLOSURE_OPEN",
    )
    qasu3_step9 = require_status(
        "certificates/selected_step9_dynamicqasu3c1response_or_precisionprofilecompletion_certificate.json",
        "MTT_SELECTED_STEP9_DYNAMICQASU3C1RESPONSE_OR_PRECISIONPROFILECOMPLETION_CLOSED_FRONTIER_REDUCTION_SOURCE_RULE_OPEN",
    )
    qasu3_de = require_status(
        "certificates/selected_qasu3_selectedmonaddevalues_or_bn27strictsourcetheorem_certificate.json",
        "MTT_SELECTED_QASU3_SELECTEDMONADDEVALUES_OR_BN27STRICTSOURCETHEOREM_PRIMITIVE_VALUES_SELECTED_DE_VALUES_IMPORTED_STRICT_PROMOTION_OPEN",
    )
    one_primitive = require_status(
        "certificates/selected_physicalnormalizationaxiomderivation_or_oneprimitiveadoptiondecision_certificate.json",
        "MTT_SELECTED_PHYSICALNORMALIZATIONAXIOMDERIVATION_OR_ONEPRIMITIVEADOPTIONDECISION_ADOPTED_ONE_SHARED_PRIMITIVE_STANDARD",
    )
    require_status(
        "certificates/selected_oneprimitiveclosurepaperupdate_or_strictnoknobupgradeprogram_certificate.json",
        "MTT_SELECTED_ONEPRIMITIVECLOSUREPAPERUPDATE_OR_STRICTNOKNOBUPGRADEPROGRAM_BUILT_PUBLICATION_STANDARD_AND_UPGRADE_PROGRAM",
    )
    pew = require_status(
        "certificates/selected_strictpewdenominatorselectiontheorem_or_directkpromotion_certificate.json",
        "MTT_SELECTED_STRICTPEWDENOMINATORSELECTIONTHEOREM_OR_DIRECTKPROMOTION_STRICT_PEW_AND_DIRECTK_PROMOTED",
    )
    precision = require_status(
        "certificates/selected_precisionequivalencerows_or_truesmclosureaudit_certificate.json",
        "MTT_SELECTED_PRECISIONEQUIVALENCEROWS_OR_TRUESMCLOSUREAUDIT_POST_PEW_LEDGER_REBUILT_PRECISION_OPEN",
    )
    candidate = load_json("candidate_data/global_locked_breakthroughs_do_not_reopen.candidate.json")

    require(q27.get("theorem_proved") is True, "27x27 matrix/minimal ledger theorem not proved")
    require(q27.get("closure_claimed") is True, "27x27 matrix/minimal ledger not closed")
    require(yukawa.get("true_SM_equivalence_closed") is False, "Yukawa packet overclaims true SM closure")
    require(pi_ckm.get("accepted_weight_rows") == 3, "Pi_CKM 3/3 weight rows not locked")
    require(pi_ckm.get("theorem_proved") is True, "Pi_CKM branch-retention theorem not proved")
    require(pi_ckm_residual.get("accepted_weight_rows") == 3, "Pi_CKM residual audit lost 3/3 rows")
    require(ah8.get("closure_claimed") is True and ah8.get("theorem_proved") is True, "AH8 consumed lane not locked")
    require(route_a.get("closure_claimed") is True and route_a.get("theorem_proved") is True, "Route A dynamic source promotion not locked")
    require(post_source.get("true_SM_equivalence_closed") is False, "Post-source audit overclaims full closure")
    require(dynamic_overlap.get("true_SM_equivalence_closed") is False, "Dynamic overlap packet overclaims full closure")
    require(dynamic_qasu3.get("true_SM_equivalence_closed") is False, "Dynamic Qa/SU3 packet overclaims full closure")
    require(dynamic_qasu3.get("dynamic_QaSU3_first_response_layer_closed") is True, "Dynamic Qa/SU3 first response is not locked")
    require(qasu3_step9.get("all_operator_source_slots_closed") is True, "Qa/SU3 operator source slots are not locked")
    require(qasu3_step9.get("actual_dynamic_QaSU3_operator_packet_closed") is False, "Qa/SU3 payload value frontier unexpectedly closed")
    require(qasu3_de.get("closure_claimed") is True and qasu3_de.get("theorem_proved") is True, "Qa/SU3 selected monad DE import not locked")
    require(one_primitive.get("H_specific_parameter_count") == 0, "H-specific parameter count changed")
    require(one_primitive.get("shared_physical_primitive_count") == 1, "one-shared primitive count changed")
    require(pew.get("accepted_global_strict_P_EW_source_rows") == 1, "strict P_EW row not locked")
    require(pew.get("accepted_global_direct_K_threshold_Omega_H_lambda_rows") == 1, "direct-K row not locked")
    require(pew.get("strict_zero_primitive_K_threshold_row_count") == 10, "strict K threshold ledger not 10/10")
    require(pew.get("strict_zero_primitive_ten_K_closed") is True, "strict ten-K closure flag false")
    require(precision.get("strict_PEW_directK_blocker_closed") is True, "precision ledger reopens EW/direct-K")
    require(
        candidate["closure_decision"]["strict_P_EW_and_directK_locked"] is True,
        "global lock candidate does not lock EW/direct-K",
    )

    print(
        json.dumps(
            {
                "candidate": "candidate_data/global_locked_breakthroughs_do_not_reopen.candidate.json",
                "status": candidate["status"],
                "qutrit27_matrix_minimal_ledger_locked": True,
                "finite_replay_yukawa_locked": True,
                "pi_ckm_weight_rows": pi_ckm["accepted_weight_rows"],
                "ah8_bn27_consumed_locked": True,
                "dynamic_c1_source_promotion_stack_locked": True,
                "qasu3_operator_source_slots_locked": qasu3_step9["all_operator_source_slots_closed"],
                "qasu3_actual_payload_values_open": not qasu3_step9["actual_dynamic_QaSU3_operator_packet_closed"],
                "qasu3_first_response_locked": dynamic_qasu3["dynamic_QaSU3_first_response_layer_closed"],
                "one_shared_physical_primitive_count": one_primitive["shared_physical_primitive_count"],
                "strict_P_EW_rows": pew["accepted_global_strict_P_EW_source_rows"],
                "direct_K_rows": pew["accepted_global_direct_K_threshold_Omega_H_lambda_rows"],
                "K_threshold_rows": pew["strict_zero_primitive_K_threshold_row_count"],
            },
            indent=2,
        )
    )
    print("global locked breakthroughs do-not-reopen audit passed")


if __name__ == "__main__":
    main()
