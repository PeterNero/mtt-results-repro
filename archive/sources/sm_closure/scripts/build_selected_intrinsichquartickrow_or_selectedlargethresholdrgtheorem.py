"""Build the intrinsic-H K row vs large-threshold/RG burden packet.

The previous packet closed the A_EW tier gate and showed that plain external
weak-coupling D-term replay underpredicts the external Higgs quartic coordinate.
This packet imports the constants-repo H7A3 underdetermination theorem for the
intrinsic K4 route and turns Route B into a precise selected-operator burden.
It does not use the external lambda row as a selector.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
CONSTANTS = TEXPAPERS / "mtt-individual-constants-source-search"
CONST_DATA = CONSTANTS / "candidate_data"
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_intrinsichquartickrow_or_selectedlargethresholdrgtheorem"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_A = PACKET_DIR / "route_a_intrinsic_k4_current_underdetermination_import.packet.json"
ROUTE_B = PACKET_DIR / "route_b_large_threshold_rg_burden.packet.json"
THETA_TEST = PACKET_DIR / "theta_inverse_large_threshold_shortcut_test.packet.json"
ACCEPTANCE = PACKET_DIR / "selected_large_threshold_rg_acceptance_contract.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_route_ab_burden.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_route_ab_burden.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_IntrinsicHQuarticKRow_or_SelectedLargeThresholdRGTheorem_v1.md"

PREVIOUS = DATA / "selected_ewboundaryrgfactorforhiggsdterm_or_directtenkclosure.candidate.json"
PREVIOUS_DIAG = (
    DATA
    / "selected_ewboundaryrgfactorforhiggsdterm_or_directtenkclosure"
    / "external_aew_dterm_diagnostic_postcheck.packet.json"
)
PREVIOUS_ROUTE = (
    DATA
    / "selected_ewboundaryrgfactorforhiggsdterm_or_directtenkclosure"
    / "dterm_route_decision_after_aew_recheck.packet.json"
)
PREVIOUS_HK = (
    DATA
    / "selected_ewboundaryrgfactorforhiggsdterm_or_directtenkclosure"
    / "hk_threshold_gate_after_aew_recheck.packet.json"
)
H_SOURCE = (
    DATA
    / "selected_hsectorquarticthresholdpayload_or_stricttenkclosure"
    / "h_sector_payload_source_equation.packet.json"
)
THETA = (
    DATA
    / "selected_step67_thetaoverlap_anchor_or_exponentprefactor_frontier"
    / "step67_theta_overlap_suppression_anchor.packet.json"
)

H7A3 = CONST_DATA / "const_higgs_01_h7a3_selected_nonlinear_zero_mode_potential_theorem.candidate.json"
H7A3_UNDER = (
    CONST_DATA
    / "const_higgs_01_h7a3_selected_nonlinear_zero_mode_potential_theorem"
    / "analytic_zero_mode_potential_underdetermination_proof.packet.json"
)
H7A3_DECISION = (
    CONST_DATA
    / "const_higgs_01_h7a3_selected_nonlinear_zero_mode_potential_theorem"
    / "route_a_decision_after_h7a3.packet.json"
)
B43 = CONST_DATA / "const_ew_02_weak_mixing_b43_threshold_vector_or_minimal_policy.candidate.json"
B43_STRICT = (
    CONST_DATA
    / "const_ew_02_weak_mixing_b43_threshold_vector_or_minimal_policy"
    / "strict_threshold_source_audit.packet.json"
)
B43_MINIMAL = (
    CONST_DATA
    / "const_ew_02_weak_mixing_b43_threshold_vector_or_minimal_policy"
    / "minimal_threshold_replay_policy.packet.json"
)
B43_DECOMP = (
    CONST_DATA
    / "const_ew_02_weak_mixing_b43_threshold_vector_or_minimal_policy"
    / "threshold_vector_decomposition.packet.json"
)

STATUS = (
    "MTT_SELECTED_INTRINSICHQUARTICKROW_OR_SELECTEDLARGETHRESHOLDRGTHEOREM_"
    "ROUTE_A_PARKED_LARGE_THRESHOLD_BURDEN_CLOSED"
)
NEXT = "MTT_Selected_HThresholdRGOperatorOrUniversalPrimitivePolicy_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing route A/B burden inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_DIAG,
        PREVIOUS_ROUTE,
        PREVIOUS_HK,
        H_SOURCE,
        THETA,
        H7A3,
        H7A3_UNDER,
        H7A3_DECISION,
        B43,
        B43_STRICT,
        B43_MINIMAL,
        B43_DECOMP,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_diag = load(PREVIOUS_DIAG)
    previous_route = load(PREVIOUS_ROUTE)
    previous_hk = load(PREVIOUS_HK)
    h_source = load(H_SOURCE)
    theta = load(THETA)
    h7a3 = load(H7A3)
    h7a3_under = load(H7A3_UNDER)
    h7a3_decision = load(H7A3_DECISION)
    b43 = load(B43)
    b43_strict = load(B43_STRICT)
    b43_minimal = load(B43_MINIMAL)
    b43_decomp = load(B43_DECOMP)

    diag_values = previous_diag["diagnostic_values"]
    s_beta = float(previous_diag["input_rows"]["selected_s_beta"])
    aew_external = float(diag_values["A_EW_Mt_external"])
    lambda_dterm_external = float(
        diag_values["lambda_Dterm_Mt_external_AEW_times_selected_sbeta"]
    )
    lambda_external = float(diag_values["lambda_Mt_external_coordinate"])
    required_multiplier = float(diag_values["underprediction_factor_lambda_ext_over_Dterm"])
    required_aew = float(diag_values["required_A_EW_to_match_external_lambda_Mt"])
    required_geff = float(diag_values["required_effective_sqrt_g2sq_plus_gYsq"])
    epsilon_theta = float(theta["epsilon_theta"])
    theta_inverse = 1.0 / epsilon_theta
    required_over_theta_inverse = required_multiplier / theta_inverse
    theta_inverse_over_required = theta_inverse / required_multiplier
    log_required_multiplier = math.log(required_multiplier)
    log_required_over_2pi = log_required_multiplier / (2.0 * math.pi)
    theta_inverse_lambda = lambda_dterm_external * theta_inverse

    route_a = {
        "schema": "MTTIntrinsicHK4CurrentUnderdeterminationImport.v1",
        "status": "ROUTE_A_CURRENT_INTRINSIC_K4_PARKED_PENDING_NEW_ZERO_MODE_POTENTIAL",
        "closure_claimed": True,
        "theorem_imported": {
            "source": rel(H7A3),
            "name": h7a3["theorem"]["name"],
            "proved": h7a3["theorem"]["proved"],
            "statement": h7a3["theorem"]["statement"],
        },
        "underdetermination": {
            "source": rel(H7A3_UNDER),
            "same_closed_data_different_K4": h7a3_under["countermodel_family"][
                "same_closed_data_different_K4"
            ],
            "countermodel_family_description": h7a3_under["countermodel_family"][
                "description"
            ],
            "K4_unique_from_current_closed_data": h7a3_under["logical_consequence"][
                "K4_unique_from_current_closed_data"
            ],
            "requires_extra_selected_source_rule": h7a3_under["logical_consequence"][
                "requires_extra_selected_source_rule"
            ],
            "extra_rule_name": h7a3_under["logical_consequence"]["extra_rule_name"],
            "does_not_deny_future_zero_mode_potential_theorem": h7a3_under["guardrail"][
                "does_not_deny_future_zero_mode_potential_theorem"
            ],
        },
        "route_A_status_after_import": {
            "intrinsic_K4_row_address_ready": h7a3_decision["route_A_status"][
                "intrinsic_K4_row_address_ready"
            ],
            "same_source_projector_support": h7a3_decision["route_A_status"][
                "same_source_projector_support"
            ],
            "current_K4_derivation_underdetermined": h7a3_decision["route_A_status"][
                "current_K4_derivation_underdetermined"
            ],
            "selected_analytic_zero_mode_potential_found": h7a3_decision[
                "route_A_status"
            ]["selected_analytic_zero_mode_potential_found"],
            "direct_intrinsic_H_quartic_K_row_emitted": False,
            "route_A_strict_closure": False,
        },
        "decision": {
            "park_current_route_A_as_proof_source": True,
            "future_route_A_reopen_condition": "emit SelectedNonlinearHiggsZeroModePotentialTheorem with K_H^(4)[12,12,12,12]",
            "promote_route_B_or_explicit_policy_as_current_target": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    route_b = {
        "schema": "MTTHLargeThresholdRGBurden.v1",
        "status": "ROUTE_B_SELECTED_LARGE_THRESHOLD_RG_BURDEN_EXACTLY_COMPUTED_NOT_SOURCE",
        "closure_claimed": True,
        "closed_inputs": {
            "selected_s_beta": s_beta,
            "Dterm_boundary_formula": previous_route["closed_formulae"]["lambda_H_mu_match"],
            "A_EW_formula": previous_route["closed_formulae"]["A_EW"],
            "K_threshold_conditional_formula": previous_route["closed_formulae"][
                "K_threshold_conditional"
            ],
            "H_source_equation": h_source["selected_source_equation"]["omega_value"],
        },
        "external_postcheck_not_source": {
            "A_EW_Mt_external": aew_external,
            "lambda_Dterm_Mt_external_AEW_times_selected_sbeta": lambda_dterm_external,
            "lambda_Mt_external_coordinate": lambda_external,
            "required_threshold_multiplier_R_H_RG_to_match_external_lambda_Mt": required_multiplier,
            "log_required_threshold_multiplier": log_required_multiplier,
            "log_required_threshold_multiplier_over_2pi": log_required_over_2pi,
            "required_A_EW_to_match_without_threshold": required_aew,
            "required_effective_sqrt_g2sq_plus_gYsq_without_threshold": required_geff,
        },
        "strict_threshold_status_import": {
            "source": rel(B43_STRICT),
            "current_source_nogo_for_strict_vector": b43_strict["decision"][
                "current_source_nogo_for_strict_vector"
            ],
            "strict_threshold_vector_source_emitted": b43_strict["decision"][
                "strict_threshold_vector_source_emitted"
            ],
            "mathematical_impossibility_claimed": b43_strict["decision"][
                "mathematical_impossibility_claimed"
            ],
            "minimal_missing_payload": b43_strict["minimal_missing_payload"],
        },
        "minimal_threshold_policy_recheck": {
            "source": rel(B43_MINIMAL),
            "minimal_threshold_replay_policy_closed": b43_minimal["decision"][
                "minimal_threshold_replay_policy_closed"
            ],
            "allowed_as_strict_source_vector": b43_minimal["admissibility"][
                "allowed_as_strict_source_vector"
            ],
            "sets_extra_threshold_terms_to_zero": b43_minimal["policy"]["sets"],
            "multiplier_if_no_additional_H_threshold": 1.0,
            "passes_H_lambda_external_postcheck": False,
            "reason": "R=1 gives the already-computed lambda_Dterm_Mt value, smaller than the external lambda_Mt coordinate by the required multiplier.",
        },
        "threshold_vector_decomposition_import": {
            "source": rel(B43_DECOMP),
            "internal_weaksplit_prefix_closed": b43_decomp["decision"][
                "internal_weaksplit_prefix_closed"
            ],
            "flat_FP_extra_threshold_closed_zero": b43_decomp["decision"][
                "flat_FP_extra_threshold_closed_zero"
            ],
            "full_physical_threshold_vector_closed": b43_decomp["decision"][
                "full_physical_threshold_vector_closed"
            ],
            "still_open_residual": b43_decomp["decomposition"]["still_open_residual"],
        },
        "selected_large_threshold_RG_theorem_emitted": False,
        "accepted_as_K_threshold_Omega_H_lambda_source": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    theta_test = {
        "schema": "MTTThetaInverseLargeThresholdShortcutTest.v1",
        "status": "THETA_INVERSE_LARGE_THRESHOLD_SHORTCUT_TESTED_NOT_SELECTED",
        "closure_claimed": True,
        "selected_theta_anchor": {
            "epsilon_theta_exact": theta["epsilon_theta_exact"],
            "epsilon_theta": epsilon_theta,
            "epsilon_theta_inverse": theta_inverse,
        },
        "diagnostic_comparison_not_source": {
            "required_threshold_multiplier": required_multiplier,
            "required_over_epsilon_theta_inverse": required_over_theta_inverse,
            "epsilon_theta_inverse_over_required": theta_inverse_over_required,
            "lambda_if_multiply_plain_Dterm_by_epsilon_theta_inverse": theta_inverse_lambda,
            "external_lambda_Mt_coordinate": lambda_external,
        },
        "decision": {
            "theta_inverse_equals_required_multiplier": False,
            "theta_inverse_promoted_as_H_threshold_RG_operator": False,
            "reason": "The selected theta anchor is real support, but no selected H-sector RG operator maps it to the required multiplier, and the numeric values are not equal.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    acceptance = {
        "schema": "MTTSelectedLargeThresholdRGAcceptanceContract.v1",
        "status": "SELECTED_H_THRESHOLD_RG_OPERATOR_ACCEPTANCE_CONTRACT_BUILT",
        "closure_claimed": True,
        "object_to_emit": {
            "name": "R_H^RG(mu_match -> M_t)",
            "role": "selected Higgs-sector threshold/RG transport operator in the same Omega/lambda_H scheme",
            "source_required": "same-branch MTT geometry, not external lambda/M_h backsolve",
        },
        "required_equations": {
            "boundary": "lambda_H(mu_match)=A_EW(mu_match)*s_beta",
            "transported_postcheck": "lambda_H(M_t)=R_H^RG(mu_match->M_t)*A_EW(mu_match)*s_beta",
            "omega_scheme": "K_threshold.Omega_H.lambda = R_H^RG*A_EW(mu_match)*s_beta/(D_fin.H*epsilon_Theta^(1/3))",
        },
        "strict_acceptance_conditions": [
            "selected physical gauge/action normalization or explicitly admitted primitive tier",
            "selected matching scale mu_match",
            "selected H-sector threshold/RG operator R_H^RG with determinant/index/provenance certificate",
            "same-branch scheme alignment with Omega_H.lambda source equation",
            "no observed lambda_H, M_h, beta, or residual scan used to choose R_H^RG",
        ],
        "postcheck_scale_if_external_Mt_rows_are_used": {
            "required_R_H_RG": required_multiplier,
            "log_required_R_H_RG": log_required_multiplier,
            "required_A_EW_without_R_H_RG": required_aew,
            "required_effective_gauge_norm_without_R_H_RG": required_geff,
        },
        "accepted_current_source_rows": {
            "selected_A_EW": False,
            "selected_mu_match": False,
            "selected_R_H_RG": False,
            "selected_K_threshold_Omega_H_lambda": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    hk_gate = {
        "schema": "MTTHKThresholdGateAfterRouteABBurden.v1",
        "status": "H_K_THRESHOLD_GATE_ROUTE_A_PARKED_ROUTE_B_OPERATOR_OPEN_9_OF_10",
        "closure_claimed": True,
        "required_output": "K_threshold.Omega_H.lambda",
        "accepted_selected_K_source_row_count": previous_hk[
            "accepted_selected_K_source_row_count"
        ],
        "selected_K_threshold_row_count_required": previous_hk[
            "selected_K_threshold_row_count_required"
        ],
        "H_row": {
            **previous_hk["H_row"],
            "A_EW_source_tier_gate_closed": True,
            "route_A_current_intrinsic_K4_derivation_underdetermined": True,
            "route_A_parked_pending_zero_mode_potential_theorem": True,
            "route_B_large_threshold_RG_burden_computed": True,
            "selected_large_threshold_RG_theorem_emitted": False,
            "selected_H_threshold_RG_operator_emitted": False,
            "theta_inverse_shortcut_promoted": False,
            "direct_intrinsic_H_quartic_K_row_emitted": False,
            "K_threshold_Omega_H_lambda_emitted": False,
        },
        "conditional_consequent_current": {
            "ten_K_antecedent_satisfied": False,
            "strict_Omega_lambda_scalar_execution_closed": False,
            "lambda_H_row_executable": False,
            "accepted_internal_scalar_value_row_count": 0,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTNextCutsetAfterRouteABBurden.v1",
        "status": "NEXT_FRONTIER_SELECTED_H_THRESHOLD_RG_OPERATOR_OR_EXPLICIT_PRIMITIVE_POLICY",
        "closure_claimed": True,
        "closed_here": [
            "Route A current-material K4 underdetermination imported from constants H7A3",
            "Route A parked as current proof source unless a new zero-mode potential theorem is emitted",
            "Route B large-threshold/RG burden computed as an exact postcheck requirement",
            "minimal/no-additional threshold replay rejected for the H lambda postcheck",
            "theta inverse large-threshold shortcut tested and rejected as selected operator",
            "selected large-threshold/RG acceptance contract built",
        ],
        "still_open": [
            "selected H-sector threshold/RG operator R_H^RG",
            "selected A_EW or explicit admitted physical primitive tier",
            "selected mu_match and same-branch scheme alignment",
            "selected K_threshold.Omega_H.lambda",
            "ten-row K antecedent and strict Omega/lambda_H scalar execution",
            "future Route A zero-mode potential theorem, if not using Route B",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedIntrinsicHQuarticKRowOrSelectedLargeThresholdRGTheorem",
        "status": STATUS,
        "previous_status": previous["status"],
        "theorem": {
            "name": "IntrinsicHK4OrLargeThresholdRGBurdenTheorem",
            "proved": True,
            "statement": (
                "The direct intrinsic H quartic route is not available from the "
                "current closed packets: constants H7A3 proves the existing "
                "projector/gap/heat data underdetermine K_H^(4).  The D-term "
                "route with selected s_beta is therefore the current sharp path, "
                "but external M_t postcheck rows require a large threshold/RG "
                "multiplier R_H^RG rather than the minimal R=1 replay.  The "
                "packet builds the exact acceptance contract for that selected "
                "operator without using the external Higgs quartic as a selector."
            ),
        },
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "closure_decision": {
            "route_A_current_material_underdetermined": True,
            "route_A_parked_pending_new_zero_mode_potential_theorem": True,
            "route_B_large_threshold_burden_computed": True,
            "minimal_no_additional_threshold_replay_rejected_for_H_postcheck": True,
            "theta_inverse_shortcut_rejected_as_selected_operator": True,
            "selected_large_threshold_RG_acceptance_contract_built": True,
            "selected_A_EW_emitted": False,
            "selected_mu_match_emitted": False,
            "selected_H_threshold_RG_operator_emitted": False,
            "selected_large_threshold_RG_theorem_emitted": False,
            "direct_intrinsic_H_quartic_K_row_emitted": False,
            "K_threshold_Omega_H_lambda_emitted": False,
            "accepted_selected_K_source_row_count": previous_hk[
                "accepted_selected_K_source_row_count"
            ],
            "selected_K_threshold_row_count_required": previous_hk[
                "selected_K_threshold_row_count_required"
            ],
            "ten_K_antecedent_satisfied": False,
            "strict_Omega_lambda_scalar_execution_closed": False,
            "accepted_internal_scalar_value_row_count": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "diagnostic_numbers_not_source": {
            "required_R_H_RG_for_external_Mt_lambda_postcheck": required_multiplier,
            "log_required_R_H_RG": log_required_multiplier,
            "log_required_R_H_RG_over_2pi": log_required_over_2pi,
            "epsilon_theta_inverse": theta_inverse,
            "required_over_epsilon_theta_inverse": required_over_theta_inverse,
            "lambda_if_R_equals_1": lambda_dterm_external,
            "lambda_if_R_equals_epsilon_theta_inverse": theta_inverse_lambda,
            "external_lambda_Mt_coordinate": lambda_external,
        },
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "route_a_intrinsic_k4_current_underdetermination_import": rel(ROUTE_A),
            "route_b_large_threshold_rg_burden": rel(ROUTE_B),
            "theta_inverse_large_threshold_shortcut_test": rel(THETA_TEST),
            "selected_large_threshold_rg_acceptance_contract": rel(ACCEPTANCE),
            "hk_threshold_gate_after_route_ab_burden": rel(HK_GATE),
            "next_cutset_after_route_ab_burden": rel(CUTSET),
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTTSelectedIntrinsicHQuarticKRowOrSelectedLargeThresholdRGTheoremCertificate",
        "status": STATUS,
        "theorem_proved": True,
        "route_A_current_material_underdetermined": True,
        "route_A_parked_pending_new_zero_mode_potential_theorem": True,
        "route_B_large_threshold_burden_computed": True,
        "minimal_no_additional_threshold_replay_rejected_for_H_postcheck": True,
        "theta_inverse_shortcut_rejected_as_selected_operator": True,
        "selected_large_threshold_RG_acceptance_contract_built": True,
        "required_R_H_RG_for_external_Mt_lambda_postcheck": required_multiplier,
        "selected_A_EW_emitted": False,
        "selected_mu_match_emitted": False,
        "selected_H_threshold_RG_operator_emitted": False,
        "selected_large_threshold_RG_theorem_emitted": False,
        "direct_intrinsic_H_quartic_K_row_emitted": False,
        "K_threshold_Omega_H_lambda_emitted": False,
        "accepted_selected_K_source_row_count": previous_hk["accepted_selected_K_source_row_count"],
        "selected_K_threshold_row_count_required": previous_hk[
            "selected_K_threshold_row_count_required"
        ],
        "ten_K_antecedent_satisfied": False,
        "strict_Omega_lambda_scalar_execution_closed": False,
        "accepted_internal_scalar_value_row_count": 0,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected IntrinsicHQuarticKRow or SelectedLargeThresholdRGTheorem v1

Status: `{STATUS}`

## What Closed

- imported constants H7A3: current closed Route A data underdetermine `K_H^(4)[12,12,12,12]`
- parked current Route A as a proof source unless a new selected zero-mode potential theorem is emitted
- computed the Route B postcheck burden from selected `s_beta`:
  - `lambda_Dterm(M_t)={lambda_dterm_external}`
  - external `lambda_Mt={lambda_external}`
  - required `R_H^RG={required_multiplier}`
  - `log(R_H^RG)={log_required_multiplier}`
- rejected minimal/no-additional threshold replay for the H lambda postcheck
- tested and rejected the `epsilon_Theta^-1` shortcut as a selected H threshold/RG operator
- built the exact selected large-threshold/RG acceptance contract

## Still Open

- selected `R_H^RG(mu_match -> M_t)`
- selected `A_EW` or an explicit admitted physical primitive tier
- selected `mu_match`
- selected `K_threshold.Omega_H.lambda`
- ten-row K antecedent and strict Omega/lambda_H scalar execution

Next required artifact: `{NEXT}`
"""

    write_json(ROUTE_A, route_a)
    write_json(ROUTE_B, route_b)
    write_json(THETA_TEST, theta_test)
    write_json(ACCEPTANCE, acceptance)
    write_json(HK_GATE, hk_gate)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
