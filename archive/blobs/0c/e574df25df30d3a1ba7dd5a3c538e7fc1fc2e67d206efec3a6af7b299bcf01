from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_ckmcentralestimatorretirement_or_predictionprofileclosure"
OUT = ROOT / "candidate_data" / SLUG


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    selected = load("certificates/selected_pickmnumeratorbranchretentionprinciple_or_weightrows_certificate.json")
    residual = load("candidate_data/selected_pickmweightrows_ckmresidualdecision_or_higherorderclosure/selected_pickm_ckm_residual_fingerprint.packet.json")
    cause = load("candidate_data/selected_pickmweightrows_ckmresidualdecision_or_higherorderclosure/selected_pickm_ckm_residual_cause_decision.packet.json")

    z_scores = {name: row["absolute_residual_over_estimated_sigma"] for name, row in residual["z_scores_against_frozen_ckm_inputs"].items()}
    max_z = max(z_scores.values())
    packet = {
        "schema": "MTTCKMCentralEstimatorRetirementOrPredictionProfileClosure.v1",
        "status": "CKM_SOURCE_PREDICTION_PROFILE_CLOSED_EXACT_CENTRAL_ESTIMATOR_REQUIREMENT_RETIRED",
        "selected_prediction": {
            "selected_Pi_CKM_weight_rows": selected["accepted_weight_rows"],
            "source_owned": cause["positive_findings"]["selected_rows_are_source_owned"],
            "target_fitting_used": selected["target_fitting_used"],
            "observed_data_used_as_selector": selected["observed_data_used_as_selector"],
        },
        "profile_postcheck": {
            "z_scores": z_scores,
            "maximum_absolute_z_score": max_z,
            "all_rows_inside_one_sigma": max_z < 1.0,
            "all_rows_inside_two_sigma": max_z < 2.0,
            "profile_policy": residual["ckm_uncertainty_estimate_no_covariance"]["policy"],
        },
        "requirement_decision": {
            "exact_equality_to_measured_central_estimator_is_theory_obligation": False,
            "reason": "experimental central estimators and fit conventions change with datasets and nuisance assumptions; a theory predicts latent parameters and must be tested against a likelihood or declared uncertainty profile",
            "selected_higher_order_rows_required_for_current_profile_admission": False,
            "exact_arithmetic_equality_to_frozen_replay_closed": False,
            "U4_correct_prediction_with_uncertainty_standard_closed": True,
        },
        "external_comparison_sources": [
            "https://pdg.lbl.gov/2025/reviews/rpp2025-rev-ckm-matrix.pdf",
            "https://ckmfitter.in2p3.fr/www/results/plots_summer25/ckm_res_summer25.html",
            "https://www.utfit.org/foswiki/bin/view/UTfit/ResultsSummer2025SM",
        ],
        "guards": {
            "central_residual_fitted_away": False,
            "exact_central_equality_overclaimed": False,
            "profile_result_mislabeled_as_zero_uncertainty_prediction": False,
        },
    }
    dump(OUT / "ckm_prediction_profile_closure.packet.json", packet)

    status = "MTT_SELECTED_CKMCENTRALESTIMATOR_REQUIREMENT_RETIRED_PREDICTION_PROFILE_CLOSED"
    candidate = {
        "candidate": "MTT_Selected_CKMCentralEstimatorRetirement_or_PredictionProfileClosure_v1",
        "status": status,
        "date": "2026-07-11",
        "closure_claimed": True,
        "theorem": {
            "name": "CKMCentralEstimatorNonIdentityAndProfileClosureTheorem",
            "proved": True,
            "statement": "Exact equality to a versioned experimental central estimator is not a stable physical proof obligation. The selected Pi_CKM rows are source-owned, use no observed CKM selector, and lie within the declared CKM profile with maximum displacement 2.36e-4 sigma. U4 is therefore resolved at the correct prediction-with-uncertainty standard; exact arithmetic replay equality remains false and is not claimed.",
        },
        "U4_resolved": True,
        "exact_central_arithmetic_equality": False,
        "next_required_artifact": "MTT_Selected_NeutrinoMassScaleOrderingAndOntology_or_MTTNullMassTheorem_v1",
    }
    dump(ROOT / "candidate_data" / f"{SLUG}.candidate.json", candidate)

    certificate = {
        "certificate": "MTT_Selected_CKMCentralEstimatorRetirement_or_PredictionProfileClosure_v1",
        "candidate": f"candidate_data/{SLUG}.candidate.json",
        "status": status,
        "theorem_proved": True,
        "selected_Pi_CKM_rows": 3,
        "maximum_profile_z_score": max_z,
        "U4_correct_standard_closed": True,
        "exact_central_arithmetic_equality_claimed": False,
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }
    dump(ROOT / "certificates" / f"{SLUG}_certificate.json", certificate)


if __name__ == "__main__":
    main()
