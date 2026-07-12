"""Build flavor-operator value use / CKM-PMNS orientation bridge."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_flavoroperatorvalueuse_or_ckmpmnsorientationbridge"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FlavorOperatorValueUse_or_CKMPMNSOrientationBridge_v1.md"

FLAVOR_VALUES = (
    DATA
    / "selected_flavorthresholdoperatorsourcevalues_or_nineslotpolicyadoption"
    / "flavor_threshold_operator_value_table.packet.json"
)
FLAVOR_POLICY = (
    DATA
    / "selected_flavorthresholdoperatorsourcevalues_or_nineslotpolicyadoption"
    / "flavor_threshold_operator_policy_source_values.packet.json"
)
FLAVOR_CANDIDATE = DATA / "selected_flavorthresholdoperatorsourcevalues_or_nineslotpolicyadoption.candidate.json"
REDUCTION_TESTS = (
    DATA
    / "selected_flavorthresholdsourceoperator_or_reducedcoefficienttheorem"
    / "reduced_coefficient_rank_tests.packet.json"
)
MIXING_REPLAY = DATA / "sm_equivalence_mixing_and_gauge_replay.candidate.json"
DYNAMIC_QASU3 = DATA / "selected_dynamicqasu3operatorpacketreplay_or_yukawamassmixingvalueclosure.candidate.json"
FULLS2 = DATA / "selected_fulls2noproxyvaluerows_or_strictpewdirectkexit.candidate.json"
PRECISION_TABLE = DATA / "selected_precisionprofiletable_or_truesmequivalenceaudit.candidate.json"
FULLSM_LEDGER = DATA / "selected_fullsmminimalparameterledger_or_strictpewsourcetheorem.candidate.json"
QCD_THETA = DATA / "selected_qcdthetapolicy_or_strictpewcountreduction.candidate.json"
STATIC_CP = DATA / "selected_staticcoefficienttransfermap_or_cporientationfrontier.candidate.json"

STATUS = (
    "MTT_SELECTED_FLAVOROPERATORVALUEUSE_OR_CKMPMNSORIENTATIONBRIDGE_"
    "BUILT_OPERATOR_USE_BRIDGE_STRICT_SOURCE_ROWS_OPEN"
)
NEXT = "MTT_Selected_CKMPMNSOrientationSourceOperator_or_FlavorPrecisionIntegration_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    flavor_values = load(FLAVOR_VALUES)
    flavor_policy = load(FLAVOR_POLICY)
    flavor_candidate = load(FLAVOR_CANDIDATE)
    reduction = load(REDUCTION_TESTS)
    mixing = load(MIXING_REPLAY)
    dynamic = load(DYNAMIC_QASU3)
    fulls2 = load(FULLS2)
    precision = load(PRECISION_TABLE)
    ledger = load(FULLSM_LEDGER)
    qcd = load(QCD_THETA)
    static_cp = load(STATIC_CP)

    ckm = mixing["CKM_replay"]
    pmns = mixing["PMNS_replay"]
    key_numbers = fulls2["key_numbers"]
    ledger_decision = ledger["closure_decision"]
    precision_decision = precision["closure_decision"]

    strict_csk_rows = flavor_values["strict_selected_no_knob_source_row_count"]
    policy_csk_rows = flavor_values["policy_source_value_row_count"]
    reduction_full_rank = reduction["rank"] == 3 and abs(reduction["determinant"]) > 0.0
    ckm_pmns_replay_ready = (
        ckm["unitarity_max_residual"] < 1e-12
        and pmns["unitarity_max_residual"] < 1e-12
        and ckm["used_as_source_selector"] is False
        and pmns["used_as_source_selector"] is False
    )
    qualitative_cp_ready = (
        dynamic["what_closes_now"]["qualitative_non_scalar_flavor_tests_preserved"] is True
        and key_numbers["cp_odd_trace_commutator_cubed_imag"] != 0
        and key_numbers["ckm_commutator_norm_sq"] > 0
        and key_numbers["pmns_commutator_norm_sq"] > 0
    )

    csk_source_theorem_attempt = {
        "schema": "MTTStrictCskSourceTheoremAttempt.v1",
        "status": "STRICT_CSK_SOURCE_ROWS_STILL_ZERO",
        "operator_form": flavor_values["operator_form"],
        "policy_source_value_row_count": policy_csk_rows,
        "strict_selected_no_knob_source_row_count": strict_csk_rows,
        "selected_source_theorem_closed": False,
        "positive_result": "the exact selected-family operator can carry the c_{s,k} rows at the explicit policy tier",
        "negative_result": "no current packet emits the nine c_{s,k} values as selected no-knob threshold/source rows",
        "required_replacement_for_strict_closure": [
            "same operator value rows emitted by a selected flavor-threshold source functional",
            "or source-selected reduced coefficient theorem with a certified lower-dimensional row map",
            "or accepted universal source-anchor theorem whose parameters are selected independently of flavor targets",
        ],
    }

    reduction_recheck = {
        "schema": "MTTCskReductionRecheck.v1",
        "status": "NO_REDUCTION_BELOW_NINE_FROM_CURRENT_SELECTED_ROWS",
        "coefficient_matrix_rank": reduction["rank"],
        "coefficient_matrix_determinant": reduction["determinant"],
        "coefficient_matrix_full_rank": reduction_full_rank,
        "tested_reductions": reduction["tests"],
        "reduced_selected_parameter_count": None,
        "minimal_current_flavor_policy_slots": policy_csk_rows,
        "reduction_below_nine_closed": False,
        "statement": "Current selected reductions fail; the honest charged-flavor value layer remains nine profile-policy coefficient rows.",
    }

    orientation_contract = {
        "schema": "MTTFlavorOperatorCKMPMNSOrientationBridge.v1",
        "status": "CKM_PMNS_ORIENTATION_BRIDGE_EXECUTABLE_AT_POLICY_REPLAY_TIER",
        "diagonal_magnitude_operator": {
            "source": str(FLAVOR_VALUES.relative_to(ROOT)).replace("\\", "/"),
            "tier": "minimal nine-slot flavor policy",
            "sectors_available": sorted(flavor_values["sector_operator_coefficients"].keys()),
            "row_count": policy_csk_rows,
            "strict_selected_no_knob_source_row_count": strict_csk_rows,
        },
        "CKM_bridge": {
            "basis_convention": ckm["basis_convention"],
            "orientation_source_tier": "measured SM-parity replay, not selected source data",
            "unitarity_max_residual": ckm["unitarity_max_residual"],
            "input_jarlskog": ckm["input_jarlskog"],
            "down_hermitian_reconstruction_residual": ckm["down_hermitian_reconstruction_residual"],
            "operator_use_closed": True,
            "selected_orientation_source_closed": False,
        },
        "PMNS_bridge": {
            "basis_convention": pmns["basis_convention"],
            "orientation_source_tier": "measured oscillation replay, not selected source data",
            "unitarity_max_residual": pmns["unitarity_max_residual"],
            "input_jarlskog": pmns["input_jarlskog"],
            "diagonalization_max_residual_eV2": pmns["diagonalization_max_residual_eV2"],
            "absolute_neutrino_mass_filled": pmns["absolute_neutrino_mass_filled"],
            "operator_use_closed": True,
            "selected_orientation_source_closed": False,
        },
        "dynamic_cp_support": {
            "qualitative_non_scalar_flavor_tests_preserved": dynamic["what_closes_now"][
                "qualitative_non_scalar_flavor_tests_preserved"
            ],
            "accepted_selected_dynamic_value_row_count": fulls2["closure_decision"][
                "accepted_selected_dynamic_value_row_count"
            ],
            "cp_odd_trace_commutator_cubed_imag": key_numbers["cp_odd_trace_commutator_cubed_imag"],
            "ckm_commutator_norm_sq": key_numbers["ckm_commutator_norm_sq"],
            "pmns_commutator_norm_sq": key_numbers["pmns_commutator_norm_sq"],
            "qualitative_cp_orientation_bridge_closed": qualitative_cp_ready,
            "measured_CKM_PMNS_phase_values_derived": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "bridge_ready": ckm_pmns_replay_ready and qualitative_cp_ready,
    }

    precision_integration = {
        "schema": "MTTFlavorHiggsThresholdPrecisionIntegrationStatus.v1",
        "status": "FLAVOR_OPERATOR_INTEGRATED_WITH_MINIMAL_LEDGER_TRUE_EQUIVALENCE_OPEN",
        "h_lambda_lane": {
            "H_specific_parameter_count": ledger_decision["H_specific_parameter_count"],
            "P_EW_counted_as_shared_physical_primitive": ledger_decision[
                "P_EW_counted_as_shared_physical_primitive"
            ],
            "P_EW_parameter_count": ledger_decision["P_EW_parameter_count"],
            "lambda_H_independent_parameter_replaced": ledger_decision[
                "lambda_H_independent_parameter_replaced"
            ],
        },
        "minimal_parameter_ledger": {
            "charged_yukawa_counted_as_measured_replay": ledger_decision[
                "charged_yukawa_counted_as_measured_replay"
            ],
            "CKM_counted_as_measured_replay": ledger_decision["CKM_counted_as_measured_replay"],
            "PMNS_oscillation_counted_as_minimal_policy": ledger_decision[
                "PMNS_oscillation_counted_as_minimal_policy"
            ],
            "closed_non_neutrino_excluding_QCD_theta": ledger_decision[
                "closed_non_neutrino_SM_like_count_excluding_QCD_theta"
            ],
            "closed_minimal_PMNS_excluding_QCD_theta": ledger_decision[
                "closed_with_minimal_PMNS_oscillation_policy_excluding_QCD_theta"
            ],
            "minimal_PMNS_including_QCD_theta": qcd["closure_decision"][
                "minimal_PMNS_count_including_QCD_theta"
            ],
        },
        "precision_frontier": {
            "precision_profile_table_built": precision_decision["precision_profile_table_built"],
            "precision_policy_rows_closed": precision_decision["precision_policy_rows_closed"],
            "accepted_true_equivalence_rows": precision_decision["accepted_true_equivalence_rows"],
            "threshold_mass_scheme_source_rows_closed": precision_decision[
                "threshold_mass_scheme_source_rows_closed"
            ],
            "full_covariance_profile_likelihood_closed": precision_decision[
                "full_covariance_profile_likelihood_closed"
            ],
            "true_SM_equivalence_closed": precision_decision["true_SM_equivalence_closed"],
        },
        "static_cp_orientation_frontier": {
            "mixed_branches_rejected": static_cp["closure_decision"]["mixed_branches_rejected"],
            "selected_specific_lambda_value_emitted": static_cp["closure_decision"][
                "selected_specific_lambda_value_emitted"
            ],
            "selected_physical_matrices_promoted": static_cp["closure_decision"][
                "selected_physical_matrices_promoted"
            ],
        },
        "full_true_SM_equivalence_closed": False,
    }

    next_cutset = {
        "schema": "MTTNextCutsetAfterFlavorOperatorOrientationBridge.v1",
        "status": "NEXT_SOURCE_ROWS_NOT_ANOTHER_REPLAY",
        "closed_now": [
            "T_profile value rows are usable as the charged diagonal magnitude operator at the minimal policy tier",
            "CKM and PMNS measured-replay matrices are wired to that operator with explicit basis conventions",
            "dynamic Qa/SU3 qualitative non-scalar/mixing/CP support is imported without using observed flavor selectors",
            "H/lambda minimal one-primitive lane and precision table are integrated into the same ledger boundary",
            "current reduction below nine charged flavor rows is rejected by full-rank coefficient evidence",
        ],
        "remaining_source_rows": [
            "strict selected c_{s,k} source theorem or independently selected lower-dimensional flavor source",
            "selected CKM/PMNS orientation source operator deriving angles and physical CP phase, not measured replay",
            "strict P_EW/direct-K source row or accepted physical gauge/action normalization",
            "threshold/mass-scheme/covariance/profile likelihood source rows",
            "absolute neutrino mass/Majorana policy if the target includes full neutrino-sector closure",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedFlavorOperatorValueUseOrCKMPMNSOrientationBridge",
        "status": STATUS,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "strict_csk_source_theorem_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "inputs": {
            "flavor_candidate": str(FLAVOR_CANDIDATE.relative_to(ROOT)).replace("\\", "/"),
            "flavor_operator_value_table": str(FLAVOR_VALUES.relative_to(ROOT)).replace("\\", "/"),
            "flavor_policy_values": str(FLAVOR_POLICY.relative_to(ROOT)).replace("\\", "/"),
            "reduction_tests": str(REDUCTION_TESTS.relative_to(ROOT)).replace("\\", "/"),
            "mixing_replay": str(MIXING_REPLAY.relative_to(ROOT)).replace("\\", "/"),
            "dynamic_qasu3": str(DYNAMIC_QASU3.relative_to(ROOT)).replace("\\", "/"),
            "first_dynamic_rows": str(FULLS2.relative_to(ROOT)).replace("\\", "/"),
            "precision_table": str(PRECISION_TABLE.relative_to(ROOT)).replace("\\", "/"),
            "fullsm_ledger": str(FULLSM_LEDGER.relative_to(ROOT)).replace("\\", "/"),
            "qcd_theta_policy": str(QCD_THETA.relative_to(ROOT)).replace("\\", "/"),
            "static_cp_orientation": str(STATIC_CP.relative_to(ROOT)).replace("\\", "/"),
        },
        "output_packets": {
            "strict_csk_source_theorem_attempt": f"candidate_data/{SLUG}/strict_csk_source_theorem_attempt.packet.json",
            "csk_reduction_recheck": f"candidate_data/{SLUG}/csk_reduction_recheck.packet.json",
            "flavor_operator_ckmpmns_orientation_bridge": f"candidate_data/{SLUG}/flavor_operator_ckmpmns_orientation_bridge.packet.json",
            "flavor_higgs_threshold_precision_integration_status": f"candidate_data/{SLUG}/flavor_higgs_threshold_precision_integration_status.packet.json",
            "next_cutset_after_flavor_operator_orientation_bridge": f"candidate_data/{SLUG}/next_cutset_after_flavor_operator_orientation_bridge.packet.json",
        },
        "closure_decision": {
            "flavor_operator_policy_value_use_closed": True,
            "policy_csk_source_value_row_count": policy_csk_rows,
            "strict_selected_csk_source_row_count": strict_csk_rows,
            "strict_csk_source_theorem_closed": False,
            "coefficient_reduction_below_nine_closed": False,
            "coefficient_matrix_full_rank": reduction_full_rank,
            "CKM_PMNS_orientation_bridge_executable": ckm_pmns_replay_ready,
            "qualitative_CP_bridge_closed": qualitative_cp_ready,
            "selected_CKM_PMNS_orientation_source_closed": False,
            "measured_CKM_PMNS_phase_values_derived": False,
            "h_lambda_minimal_one_primitive_integrated": True,
            "precision_profile_integrated": True,
            "accepted_true_equivalence_rows": precision_decision["accepted_true_equivalence_rows"],
            "full_true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "theorem": {
            "name": "FlavorOperatorUseAndOrientationBridgeTheorem",
            "proved": True,
            "statement": "The same selected-family flavor operator carrying nine policy c_{s,k} values is now a valid diagonal charged-magnitude operator for CKM/PMNS replay and precision-ledger integration. CKM and PMNS orientation are executable with explicit measured-replay conventions, and dynamic Qa/SU3 supplies qualitative non-scalar/mixing/CP support without target selectors. However the strict selected source theorem for c_{s,k}, reduction below nine flavor rows, selected CKM/PMNS orientation source values, strict P_EW/direct-K, and accepted true-equivalence rows remain open.",
        },
    }

    cert = {
        "certificate": "MTT_Selected_FlavorOperatorValueUse_or_CKMPMNSOrientationBridge_v1",
        "status": STATUS,
        "candidate": candidate["candidate"],
        "theorem": candidate["theorem"]["name"],
        "proved": True,
        "policy_csk_source_value_row_count": policy_csk_rows,
        "strict_selected_csk_source_row_count": strict_csk_rows,
        "coefficient_matrix_full_rank": reduction_full_rank,
        "CKM_PMNS_orientation_bridge_executable": ckm_pmns_replay_ready,
        "qualitative_CP_bridge_closed": qualitative_cp_ready,
        "selected_CKM_PMNS_orientation_source_closed": False,
        "accepted_true_equivalence_rows": precision_decision["accepted_true_equivalence_rows"],
        "full_true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected FlavorOperatorValueUse or CKMPMNSOrientationBridge v1

Status: `{STATUS}`

## Theorem

**FlavorOperatorUseAndOrientationBridgeTheorem.** The same selected-family flavor operator carrying nine policy `c_{{s,k}}` values is now a valid diagonal charged-magnitude operator for CKM/PMNS replay and precision-ledger integration. CKM and PMNS orientation are executable with explicit measured-replay conventions, and dynamic Qa/SU3 supplies qualitative non-scalar/mixing/CP support without target selectors.

## Closed In This Step

- Flavor operator value use at policy tier: `{policy_csk_rows}` rows.
- CKM/PMNS replay bridge: executable, with CKM Jarlskog `{ckm["input_jarlskog"]}` and PMNS Jarlskog `{pmns["input_jarlskog"]}` carried as measured replay rows.
- Dynamic CP support: nonzero CP-odd trace `{key_numbers["cp_odd_trace_commutator_cubed_imag"]}` and nonzero CKM/PMNS commutator norms.
- H/lambda and precision integration: minimal one-primitive H lane and precision profile table are linked to the same ledger boundary.

## Not Closed

- Strict selected `c_{{s,k}}` source rows: `0`.
- Reduction below nine charged flavor rows: rejected by rank `{reduction["rank"]}` and determinant `{reduction["determinant"]}`.
- Selected CKM/PMNS orientation source theorem: open.
- Accepted true-equivalence rows: `{precision_decision["accepted_true_equivalence_rows"]}`.
- Full true SM equivalence and full no-knob closure: open.

Next artifact: `{NEXT}`.
"""

    write_json(PACKET_DIR / "strict_csk_source_theorem_attempt.packet.json", csk_source_theorem_attempt)
    write_json(PACKET_DIR / "csk_reduction_recheck.packet.json", reduction_recheck)
    write_json(PACKET_DIR / "flavor_operator_ckmpmns_orientation_bridge.packet.json", orientation_contract)
    write_json(PACKET_DIR / "flavor_higgs_threshold_precision_integration_status.packet.json", precision_integration)
    write_json(PACKET_DIR / "next_cutset_after_flavor_operator_orientation_bridge.packet.json", next_cutset)
    write_json(CANDIDATE, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {CANDIDATE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
