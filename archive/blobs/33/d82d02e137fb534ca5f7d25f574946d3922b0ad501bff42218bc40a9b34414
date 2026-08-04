"""Build the locked-base freeze and PEW/direct-K attack contract."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_lockedbasefreeze_or_pewdirectkattackcontract"
OUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
LOCKED_BASE = PACKET_DIR / "locked_base_do_not_reopen.packet.json"
ATTACK = PACKET_DIR / "pew_directk_attack_contract.packet.json"
NEXT = PACKET_DIR / "next_nonlooping_execution_order.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_LockedBaseFreeze_or_PEWDirectKAttackContract_v1.md"

QUTRIT27 = DATA / "selected_qutrit27matrixminimalclosure_or_strictpewupgrade.candidate.json"
AH8 = DATA / "selected_latestah8pickmfrontier_or_nextstrictclosuretargets.candidate.json"
YUKAWA = DATA / "selected_finalyukawareplayresidualexactness_or_strictsmnoknobclosure.candidate.json"
GLOBAL = DATA / "selected_truesmnoknobclosure_globalledger_or_remainingnonyukawarows.candidate.json"
STRICT_PEW = DATA / "selected_strictpewdirectksourcerows_or_finalsmnoknobaudit.candidate.json"
ONE_PRIMITIVE = DATA / "selected_oneprimitiveclosurepaperupdate_or_strictnoknobupgradeprogram.candidate.json"
PHYS_AXIOM = DATA / "selected_physicalnormalizationsourceaxiom_or_directkcertificate.candidate.json"
PHYS_DERIVATION = DATA / "selected_physicalnormalizationaxiomderivation_or_strictpewnoknobupgrade.candidate.json"
STEP10 = DATA / "selected_strictpewdirectk_or_qasu3step10valueexecution.candidate.json"
FULLS2 = DATA / "selected_fulls2noproxyrows_or_strictpewnormalizationpayload.candidate.json"
THRESHOLD_IMPORT = DATA / "selected_thresholdresponsefunctionalrowemission_or_externalsourcerowimport.candidate.json"
SECTOR_TRANSFER = DATA / "selected_selectedsectortransferoverlapderivative_or_rowlocalprefactoremission.candidate.json"

STATUS = (
    "MTT_SELECTED_LOCKEDBASEFREEZE_OR_PEWDIRECTKATTACKCONTRACT_"
    "BUILT_BASE_LOCKED_PEW_DIRECTK_SHARPENED"
)
NEXT_ARTIFACT = "MTT_Selected_RowwiseScalarRetardedOverlapQuadratureValues_or_TSchemeLambdaHExecution_v1"


def write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def main() -> int:
    qutrit27 = load(QUTRIT27)
    ah8 = load(AH8)
    yukawa = load(YUKAWA)
    global_ledger = load(GLOBAL)
    strict_pew = load(STRICT_PEW)
    one_primitive = load(ONE_PRIMITIVE)
    phys_axiom = load(PHYS_AXIOM)
    phys_derivation = load(PHYS_DERIVATION)
    step10 = load(STEP10)
    fulls2 = load(FULLS2)
    threshold_import = load(THRESHOLD_IMPORT)
    sector_transfer = load(SECTOR_TRANSFER)

    strict_pew_rows = strict_pew["key_numbers"]["accepted_strict_P_EW_source_rows"]
    direct_k_rows = strict_pew["key_numbers"]["accepted_direct_K_threshold_Omega_H_lambda_rows"]
    strict_derivation_routes = phys_derivation["closure_decision"][
        "accepted_strict_derivation_route_count"
    ]
    finite_yukawa_rows = global_ledger["key_numbers"][
        "accepted_finite_replay_yukawa_magnitude_rows"
    ]

    locked_base = {
        "schema": "MTTLockedBaseDoNotReopen.v1",
        "status": "BASE_LOCKED_FOR_NEXT_PEW_DIRECTK_ATTACK",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "locked_results": {
            "finite_27x27_qutrit_spectral_package_closed": qutrit27["closure_decision"][
                "finite_27x27_qutrit_spectral_package_closed"
            ],
            "minimal_one_primitive_matrix_ledger_closed": qutrit27["closure_decision"][
                "minimal_one_primitive_matrix_ledger_closed"
            ],
            "two_premise_AH_equivalent_lane_closed": ah8["closure_decision"][
                "two_premise_AH_equivalent_lane_closed"
            ],
            "Pi_CKM_weight_rows_closed": ah8["closure_decision"]["Pi_CKM_weight_rows_closed"],
            "CKM_diagonal_profile_admission_closed": ah8["closure_decision"][
                "CKM_diagonal_profile_admission_closed"
            ],
            "finite_replay_yukawa_exactness_closed": yukawa["closure_decision"][
                "finite_replay_yukawa_exactness_closed"
            ],
            "strict_no_knob_yukawa_closure_at_finite_replay_standard": yukawa[
                "closure_decision"
            ]["strict_no_knob_yukawa_closure_at_finite_replay_standard"],
            "one_shared_primitive_tier_closed": one_primitive["closure_decision"][
                "one_shared_primitive_tier_closed"
            ],
        },
        "do_not_reopen": [
            "27x27 qutrit-Weyl matrix package at the minimal one-shared-primitive/projected standard",
            "AH-equivalent BN27 projected Route-C lane at 8/8",
            "Pi_CKM selected weight rows at 3/3 and CKM diagonal-profile admission",
            "finite-replay charged-Yukawa magnitude exactness with nine rows",
            "finite H scalar source and zero H-specific lambda knob",
        ],
        "not_claimed_by_locked_base": [
            "strict zero-primitive PEW/direct-K rows",
            "literal global good-cover Cech/HYM witness closure",
            "full precision true-SM equivalence",
            "analytic zero-residual Yukawa theorem beyond finite replay",
        ],
        "key_numbers": {
            "AH_equivalent_BN27_connection_rows": ah8["key_numbers"][
                "two_premise_AH_equivalent_connection_rows"
            ],
            "strict_connection_rows": ah8["key_numbers"]["strict_connection_rows"],
            "finite_replay_yukawa_magnitude_rows": finite_yukawa_rows,
            "final_yukawa_max_abs_log_residual": yukawa["key_numbers"][
                "final_max_abs_log_residual"
            ],
            "shared_physical_primitive_count": one_primitive["key_numbers"][
                "shared_physical_primitive_count"
            ],
            "H_specific_parameter_count": one_primitive["key_numbers"][
                "H_specific_parameter_count"
            ],
        },
    }

    attack = {
        "schema": "MTTPEWDirectKAttackContract.v1",
        "status": "STRICT_ROWS_ZERO_ATTACK_REDUCED_TO_TWO_EXITS",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "current_counts": {
            "accepted_strict_P_EW_source_rows": strict_pew_rows,
            "accepted_direct_K_threshold_Omega_H_lambda_rows": direct_k_rows,
            "accepted_strict_derivation_route_count": strict_derivation_routes,
            "premised_P_EW_source_rows": phys_axiom["closure_decision"][
                "premised_P_EW_source_rows"
            ],
            "premised_direct_K_threshold_Omega_H_lambda_rows": phys_axiom["closure_decision"][
                "premised_direct_K_threshold_Omega_H_lambda_rows"
            ],
            "premised_selected_K_row_count": phys_axiom["closure_decision"][
                "premised_selected_K_row_count"
            ],
            "strict_PEW_source_filled_field_count": fulls2["key_numbers"][
                "strict_PEW_source_filled_field_count"
            ],
            "strict_PEW_source_required_field_count": fulls2["key_numbers"][
                "strict_PEW_source_required_field_count"
            ],
        },
        "closed_support": {
            "Step10_route_A_source_rule_closed": step10["closure_decision"][
                "step10_route_A_source_rule_closed"
            ],
            "first_dynamic_value_rows_accepted": step10["closure_decision"][
                "first_dynamic_value_rows_accepted"
            ],
            "external_import_lane_closed_at_admitted_replay_tier": threshold_import[
                "closure_decision"
            ]["external_import_lane_closed_at_admitted_replay_tier"],
            "selected_sector_transfer_imported": sector_transfer["closure_decision"][
                "stationary_sector_transfer_imported"
            ],
            "physical_dotD_alpha1_imported": sector_transfer["closure_decision"][
                "physical_dotD_alpha1_imported"
            ],
        },
        "open_rows_preventing_strict_close": {
            "rowwise_scalar_retarded_overlap_values_emitted": sector_transfer[
                "closure_decision"
            ]["rowwise_scalar_retarded_overlap_values_emitted"],
            "selected_T_scheme_rows_emitted": sector_transfer["closure_decision"][
                "selected_T_scheme_rows_emitted"
            ],
            "selected_lambda_H_payload_emitted": sector_transfer["closure_decision"][
                "selected_lambda_H_payload_emitted"
            ],
            "selected_threshold_response_functional_instantiated": threshold_import[
                "closure_decision"
            ]["selected_threshold_response_functional_instantiated"],
            "selected_internal_value_emission_count": threshold_import["closure_decision"][
                "selected_internal_value_emission_count"
            ],
        },
        "two_legal_exits": [
            {
                "exit": "derive_P_EW_from_same_branch_source",
                "required_result": "one accepted strict P_EW source row or derived physical-normalization axiom",
                "current_accepted_rows": strict_pew_rows,
                "current_derivation_routes": strict_derivation_routes,
            },
            {
                "exit": "emit_direct_K_threshold_Omega_H_lambda",
                "required_result": "one accepted direct K_threshold.Omega_H.lambda row from selected rowwise scalar retarded-overlap/T-scheme/lambda_H payload",
                "current_accepted_rows": direct_k_rows,
                "next_source_object": NEXT_ARTIFACT,
            },
        ],
        "attack_decision": {
            "strict_PEW_directK_closed_now": False,
            "one_shared_primitive_lane_remains_valid": True,
            "next_nonlooping_route": "rowwise scalar retarded-overlap quadrature/T-scheme/lambda_H execution",
        },
    }

    next_order = {
        "schema": "MTTNextNonLoopingExecutionOrderAfterBaseFreeze.v1",
        "status": "NEXT_ORDER_SELECTED",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "ordered_targets": [
            NEXT_ARTIFACT,
            "MTT_Selected_TSchemeLambdaH_SourceRows_or_KThresholdRowClosure_v1",
            "MTT_Selected_PhysicalNormalizationAxiomDerivation_or_StrictPEWNoKnobUpgrade_v1",
            "MTT_Selected_InternalRThetaThresholdValueRows_or_MinimalUniversalSourceAnchor_v1",
            "MTT_Selected_FullPrecisionProfileEquivalence_v1",
        ],
        "why_this_is_not_a_loop": [
            "It does not reopen 27x27 matrix closure.",
            "It does not reopen finite-replay Yukawa magnitude closure.",
            "It attacks the currently zero strict PEW/direct-K rows through the missing scalar row source object.",
            "It keeps admitted external replay separate from internal selected value emission.",
        ],
    }

    candidate = {
        "candidate": "MTTSelectedLockedBaseFreezeOrPEWDirectKAttackContract",
        "status": STATUS,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "qutrit27_matrix": rel(QUTRIT27),
            "latest_AH8_PiCKM_frontier": rel(AH8),
            "final_yukawa_replay": rel(YUKAWA),
            "global_true_sm_noknob_ledger": rel(GLOBAL),
            "strict_pew_final_audit": rel(STRICT_PEW),
            "one_primitive_standard": rel(ONE_PRIMITIVE),
            "physical_normalization_axiom": rel(PHYS_AXIOM),
            "physical_normalization_derivation": rel(PHYS_DERIVATION),
            "step10_reduction": rel(STEP10),
            "fulls2_no_proxy": rel(FULLS2),
            "threshold_response_external_import": rel(THRESHOLD_IMPORT),
            "sector_transfer_overlap_derivative": rel(SECTOR_TRANSFER),
        },
        "output_packets": {
            "locked_base_do_not_reopen": rel(LOCKED_BASE),
            "pew_directk_attack_contract": rel(ATTACK),
            "next_nonlooping_execution_order": rel(NEXT),
        },
        "theorem": {
            "name": "LockedBaseFreezeAndPEWDirectKAttackContractTheorem",
            "proved": True,
            "statement": (
                "The 27x27 matrix package and finite-replay charged-Yukawa magnitudes are "
                "locked as consumed results at the current accepted standard and must not be "
                "reopened as active blockers. The active strict upgrade is reduced to PEW/direct-K: "
                "either derive the physical-normalization primitive from same-branch source data "
                "or emit a selected direct K_threshold.Omega_H.lambda row. Current strict rows remain "
                "zero, so this artifact closes the freeze/attack contract only, not strict no-knob SM."
            ),
        },
        "closure_decision": {
            "locked_base_freeze_closed": True,
            "qutrit27_matrix_locked": True,
            "yukawa_finite_replay_locked": True,
            "one_shared_primitive_standard_locked": True,
            "PEW_directK_attack_contract_closed": True,
            "strict_PEW_directK_source_rows_closed": False,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "key_numbers": {
            "finite_replay_yukawa_magnitude_rows": finite_yukawa_rows,
            "final_yukawa_max_abs_log_residual": yukawa["key_numbers"][
                "final_max_abs_log_residual"
            ],
            "AH_equivalent_BN27_connection_rows": ah8["key_numbers"][
                "two_premise_AH_equivalent_connection_rows"
            ],
            "accepted_strict_P_EW_source_rows": strict_pew_rows,
            "accepted_direct_K_threshold_Omega_H_lambda_rows": direct_k_rows,
            "accepted_strict_derivation_route_count": strict_derivation_routes,
            "strict_PEW_source_filled_field_count": fulls2["key_numbers"][
                "strict_PEW_source_filled_field_count"
            ],
            "strict_PEW_source_required_field_count": fulls2["key_numbers"][
                "strict_PEW_source_required_field_count"
            ],
            "shared_physical_primitive_count": one_primitive["key_numbers"][
                "shared_physical_primitive_count"
            ],
        },
        "next_required_artifact": NEXT_ARTIFACT,
    }

    cert = {
        "certificate": "MTT_Selected_LockedBaseFreeze_or_PEWDirectKAttackContract_v1",
        "status": STATUS,
        "candidate": rel(OUT),
        "locked_base_freeze_closed": True,
        "qutrit27_matrix_locked": True,
        "yukawa_finite_replay_locked": True,
        "PEW_directK_attack_contract_closed": True,
        "accepted_strict_P_EW_source_rows": strict_pew_rows,
        "accepted_direct_K_threshold_Omega_H_lambda_rows": direct_k_rows,
        "strict_PEW_directK_source_rows_closed": False,
        "one_shared_primitive_lane_remains_valid": True,
        "full_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }

    note = f"""# MTT Selected LockedBaseFreeze or PEWDirectKAttackContract v1

Status: `{STATUS}`

## Locked Base

- 27x27 qutrit-Weyl matrix package: locked at the current accepted one-shared-primitive/projected standard.
- AH-equivalent BN27 projected Route-C lane: `{locked_base["key_numbers"]["AH_equivalent_BN27_connection_rows"]}/8`.
- finite-replay charged-Yukawa magnitude rows: `{finite_yukawa_rows}`.
- final finite-replay Yukawa max log residual: `{yukawa["key_numbers"]["final_max_abs_log_residual"]}`.
- shared physical primitive count: `{one_primitive["key_numbers"]["shared_physical_primitive_count"]}`.
- H-specific parameter count: `{one_primitive["key_numbers"]["H_specific_parameter_count"]}`.

These are consumed results for the current standard and must not be reopened as
active blockers.

## Active Attack

Strict PEW/direct-K remains the sharp upgrade target.

- accepted strict `P_EW` source rows: `{strict_pew_rows}`
- accepted direct `K_threshold.Omega_H.lambda` rows: `{direct_k_rows}`
- accepted strict derivation routes: `{strict_derivation_routes}`
- strict PEW payload fields filled: `{fulls2["key_numbers"]["strict_PEW_source_filled_field_count"]}/{fulls2["key_numbers"]["strict_PEW_source_required_field_count"]}`

There are two legal exits:

1. derive `P_EW` from same-branch source data, or
2. emit direct `K_threshold.Omega_H.lambda` from selected rowwise scalar
   retarded-overlap / T-scheme / `lambda_H` payload rows.

Next required artifact: `{NEXT_ARTIFACT}`.
"""

    write_json(LOCKED_BASE, locked_base)
    write_json(ATTACK, attack)
    write_json(NEXT, next_order)
    write_json(OUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
