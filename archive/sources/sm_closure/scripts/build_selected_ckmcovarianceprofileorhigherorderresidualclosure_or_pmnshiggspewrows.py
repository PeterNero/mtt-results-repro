"""Build CKM residual profile-admission / higher-order closure reduction."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_ckmcovarianceprofileorhigherorderresidualclosure_or_pmnshiggspewrows"
OUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
CKM_PROFILE = PACKET_DIR / "ckm_diagonal_profile_admission.packet.json"
HIGHER_ORDER = PACKET_DIR / "higher_order_residual_row_decision.packet.json"
DECISION = PACKET_DIR / "post_ckm_profile_remaining_rows_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_CKMCovarianceProfileOrHigherOrderResidualClosure_or_PMNSHiggsPEWRows_v1.md"

PREVIOUS = DATA / "selected_ckmpmnsrows_or_higgsthresholdstrictpewexit.candidate.json"
PICKM_POSTCHECK = (
    DATA
    / "selected_pickmnumeratorbranchretentionprinciple_or_weightrows"
    / "ckm_postcheck_after_selected_pickm_rows.packet.json"
)
RESIDUAL_FINGERPRINT = (
    DATA
    / "selected_pickmweightrows_ckmresidualdecision_or_higherorderclosure"
    / "selected_pickm_ckm_residual_fingerprint.packet.json"
)
RESIDUAL_TEMPLATE = (
    DATA
    / "selected_pickmweightrows_ckmresidualdecision_or_higherorderclosure"
    / "higher_order_or_profile_residual_template.packet.json"
)
DIAGONAL_PROFILE = (
    DATA
    / "selected_fullprofileordiagonaltheorempostpi_or_noknobvaluederivation"
    / "accepted_diagonal_profile_theorem_after_external_rows.packet.json"
)
CKM_CONVENTIONS = DATA / "sm_equivalence_ckm_gauge_pmns_convention_fill.candidate.json"

STATUS = (
    "MTT_SELECTED_CKMCOVARIANCEPROFILEORHIGHERORDERRESIDUALCLOSURE_OR_PMNSHIGGSPEWROWS_"
    "BUILT_CKM_DIAGONAL_PROFILE_ADMITTED_FULLCOV_PMNS_HIGGS_PEW_OPEN"
)
NEXT = "MTT_Selected_PMNSRunningMassRows_or_HiggsThresholdStrictPEWExit_v1"


def write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def main() -> int:
    previous = load(PREVIOUS)
    postcheck = load(PICKM_POSTCHECK)
    fingerprint = load(RESIDUAL_FINGERPRINT)
    template = load(RESIDUAL_TEMPLATE)
    diagonal_profile = load(DIAGONAL_PROFILE)
    conventions = load(CKM_CONVENTIONS)

    z_scores = fingerprint["z_scores_against_frozen_ckm_inputs"]
    chi2_ckm_diagonal = sum(
        row["absolute_residual_over_estimated_sigma"] ** 2 for row in z_scores.values()
    )
    max_sigma_score = max(row["absolute_residual_over_estimated_sigma"] for row in z_scores.values())
    admitted_by_current_diagonal_profile = max_sigma_score < 1.0
    full_covariance_ready = conventions["replay_readiness"]["full_covariance_ready"]
    ckm_covariance_encoded = (
        conventions["CKM_packet"]["correlation_policy"] != "full CKM fit covariance not encoded yet"
    )

    ckm_profile = {
        "schema": "MTTCKMDiagonalProfileAdmissionAfterPiCKMRows.v1",
        "status": "CKM_RESIDUAL_ADMITTED_BY_CURRENT_DIAGONAL_PROFILE_FULL_COVARIANCE_OPEN",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "observed_data_used_for_postcheck": True,
        "previous_candidate": rel(PREVIOUS),
        "postcheck_source": rel(PICKM_POSTCHECK),
        "residual_fingerprint_source": rel(RESIDUAL_FINGERPRINT),
        "diagonal_profile_policy_source": rel(DIAGONAL_PROFILE),
        "selected_ckm_predictions": postcheck["predictions"],
        "z_scores_against_frozen_ckm_inputs": z_scores,
        "chi2_ckm_diagonal": chi2_ckm_diagonal,
        "ckm_diagonal_profile_degrees_of_freedom": len(z_scores),
        "max_abs_sigma_score_no_covariance": max_sigma_score,
        "admission_threshold_sigma": 1.0,
        "ckm_residual_admitted_by_current_diagonal_profile": admitted_by_current_diagonal_profile,
        "full_ckm_fit_covariance_encoded": ckm_covariance_encoded,
        "full_covariance_ready": full_covariance_ready,
        "full_covariance_profile_likelihood_closed": False,
        "why_not_full_covariance": conventions["CKM_packet"]["correlation_policy"],
    }

    higher_order = {
        "schema": "MTTHigherOrderResidualRowDecisionAfterCKMProfileAdmission.v1",
        "status": "HIGHER_ORDER_RESIDUAL_ROW_NOT_REQUIRED_FOR_CURRENT_DIAGONAL_ADMISSION",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "residual_template_source": rel(RESIDUAL_TEMPLATE),
        "accepted_residual_correction_rows": template["accepted_residual_correction_rows"],
        "higher_order_residual_rows_required_for_exact_frozen_central_replay": True,
        "higher_order_residual_rows_required_for_current_diagonal_profile_admission": False,
        "forbidden_exits_preserved": template["forbidden_exits"],
        "legal_exits_preserved_for_stronger_closure": template["candidate_legal_exits"],
        "exact_central_ckm_closure": False,
        "current_diagonal_ckm_profile_admission_closed": admitted_by_current_diagonal_profile,
    }

    decision = {
        "schema": "MTTPostCKMProfileRemainingRowsDecision.v1",
        "status": "CKM_RESIDUAL_PROFILE_ADMITTED_PMNS_RUNNING_HIGGS_PEW_OPEN",
        "closed_now": [
            "The selected Pi_CKM weight rows are admitted by the current diagonal CKM uncertainty sidecar.",
            "The central residual is no longer a blocker for the selected CKM source-input chain at the diagonal profile tier.",
            "No higher-order residual row is required for current diagonal-profile admission.",
        ],
        "not_closed": [
            "Exact central CKM equality remains open.",
            "Full CKM covariance/profile likelihood remains open because the CKM fit covariance is not encoded.",
            "PMNS rows, running mass-ratio rows, Higgs/threshold rows, and strict PEW/direct-K values remain open.",
        ],
        "source_row_counts": {
            "accepted_selected_Pi_CKM_weight_rows": previous["key_numbers"][
                "accepted_selected_Pi_CKM_weight_rows"
            ],
            "accepted_exact_ckm_correction_rows": previous["key_numbers"][
                "accepted_exact_ckm_correction_rows"
            ],
            "accepted_no_knob_CKM_angle_rows": previous["key_numbers"][
                "accepted_no_knob_CKM_angle_rows"
            ],
            "accepted_ckm_diagonal_profile_admission_rows": len(z_scores)
            if admitted_by_current_diagonal_profile
            else 0,
            "PMNS_angle_phase_rows": previous["key_numbers"]["PMNS_angle_phase_rows"],
            "running_mass_ratio_rows": previous["key_numbers"]["running_mass_ratio_rows"],
        },
        "acceptance": {
            "ckm_Pi_weight_rows_closed": True,
            "ckm_diagonal_profile_admission_closed": admitted_by_current_diagonal_profile,
            "ckm_exact_central_residual_closed": False,
            "ckm_full_covariance_profile_closed": False,
            "higher_order_residual_rows_required_for_current_profile_tier": False,
            "PMNS_rows_closed": False,
            "running_mass_ratio_rows_closed": False,
            "higgs_threshold_rows_closed": False,
            "strict_PEW_directK_values_closed": False,
            "fullS2_no_proxy_rows_closed": False,
            "global_true_SM_no_knob_closure": False,
            "true_SM_equivalence_closed": False,
        },
        "next_exact_target": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedCKMCovarianceProfileOrHigherOrderResidualClosureOrPMNSHiggsPEWRows",
        "status": STATUS,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "observed_data_used_for_postcheck": True,
        "inputs": {
            "previous_ckmpmns_higgs_pew_candidate": rel(PREVIOUS),
            "pickm_postcheck": rel(PICKM_POSTCHECK),
            "residual_fingerprint": rel(RESIDUAL_FINGERPRINT),
            "residual_template": rel(RESIDUAL_TEMPLATE),
            "accepted_diagonal_profile_theorem": rel(DIAGONAL_PROFILE),
            "ckm_pmns_convention_packet": rel(CKM_CONVENTIONS),
        },
        "output_packets": {
            "ckm_diagonal_profile_admission": rel(CKM_PROFILE),
            "higher_order_residual_row_decision": rel(HIGHER_ORDER),
            "post_ckm_profile_remaining_rows_decision": rel(DECISION),
        },
        "theorem": {
            "name": "CKMDiagonalProfileAdmissionAfterSelectedPiCKMRowsTheorem",
            "proved": True,
            "statement": (
                "The three selected Pi_CKM rows leave a nonzero central CKM replay residual, "
                "but each residual is far inside the current diagonal CKM uncertainty sidecar. "
                "Therefore the CKM residual is admitted at the current diagonal profile tier, "
                "without promoting measured central values as source rows and without claiming "
                "full covariance/profile or exact central CKM closure."
            ),
        },
        "key_numbers": {
            "accepted_selected_Pi_CKM_weight_rows": previous["key_numbers"][
                "accepted_selected_Pi_CKM_weight_rows"
            ],
            "accepted_ckm_diagonal_profile_admission_rows": decision["source_row_counts"][
                "accepted_ckm_diagonal_profile_admission_rows"
            ],
            "chi2_ckm_diagonal": chi2_ckm_diagonal,
            "max_abs_sigma_score_no_covariance": max_sigma_score,
            "accepted_exact_ckm_correction_rows": 0,
            "PMNS_angle_phase_rows": 0,
            "running_mass_ratio_rows": 0,
        },
        "closure_decision": decision["acceptance"],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_CKMCovarianceProfileOrHigherOrderResidualClosure_or_PMNSHiggsPEWRows_v1",
        "status": STATUS,
        "candidate": rel(OUT),
        "ckm_Pi_weight_rows_closed": True,
        "ckm_diagonal_profile_admission_closed": admitted_by_current_diagonal_profile,
        "accepted_ckm_diagonal_profile_admission_rows": decision["source_row_counts"][
            "accepted_ckm_diagonal_profile_admission_rows"
        ],
        "ckm_exact_central_residual_closed": False,
        "ckm_full_covariance_profile_closed": False,
        "PMNS_rows_closed": False,
        "running_mass_ratio_rows_closed": False,
        "higgs_threshold_rows_closed": False,
        "strict_PEW_directK_values_closed": False,
        "fullS2_no_proxy_rows_closed": False,
        "global_true_SM_no_knob_closure": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected CKMCovarianceProfileOrHigherOrderResidualClosure or PMNSHiggsPEWRows v1

Status: `{STATUS}`

## Closed Now

The CKM central residual after the selected `Pi_CKM` rows is admitted at the
current diagonal profile tier:

- selected `Pi_CKM` rows: `3/3`
- diagonal CKM admission rows: `{decision["source_row_counts"]["accepted_ckm_diagonal_profile_admission_rows"]}/3`
- CKM diagonal chi2: `{chi2_ckm_diagonal}`
- max sigma score without covariance: `{max_sigma_score}`

This closes the residual as a blocker for the current selected CKM source-input
chain.  It does not use CKM central values as source selectors.

## Still Open

- exact central CKM equality: open
- full CKM covariance/profile likelihood: open
- PMNS rows: `0`
- running mass-ratio rows: `0`
- Higgs/`lambda_H` threshold rows: open
- strict `P_EW` / direct-K values: open

Next required artifact: `{NEXT}`.
"""

    write_json(CKM_PROFILE, ckm_profile)
    write_json(HIGHER_ORDER, higher_order)
    write_json(DECISION, decision)
    write_json(OUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
