"""Build Higgs homogeneous-profile assessment or route-A covariance model."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgshomogeneousprofile_or_routeaformulacovariance"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
HOMOGENEOUS_ASSESSMENT = PACKET_DIR / "homogeneous_profile_route_assessment.packet.json"
CORRELATED_MODEL = PACKET_DIR / "source_derived_correlated_covariance_model.packet.json"
ROUTE_A_STATUS = PACKET_DIR / "route_a_formula_covariance_status.packet.json"
PROMOTION = PACKET_DIR / "higgs_precision_promotion_after_covariance_model.packet.json"
UPDATED_TRUE = PACKET_DIR / "updated_true_equivalence_gate_after_higgs_covariance_model.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsHomogeneousProfile_or_RouteAFormulaCovariance_v1.md"

STATUS = "MTT_SELECTED_HIGGSHOMOGENEOUSPROFILE_OR_ROUTEAFORMULACOVARIANCE_BUILT_CORRELATED_COVARIANCE_MODEL_FULL_PROFILE_OPEN"

ROW_BASIS = [
    "H_to_bb",
    "H_to_cc",
    "H_to_tau_tau",
    "H_to_mu_mu",
    "H_to_WW_star",
    "H_to_ZZ_star",
    "H_to_gg",
    "H_to_gamma_gamma",
    "H_to_Z_gamma",
    "H_to_ss",
]

BR_PARAMETRIC_REL = {
    "H_to_bb": 0.015,
    "H_to_cc": 0.085,
    "H_to_tau_tau": 0.025,
    "H_to_mu_mu": 0.025,
    "H_to_WW_star": 0.025,
    "H_to_ZZ_star": 0.025,
    "H_to_gg": 0.061,
    "H_to_gamma_gamma": 0.025,
    "H_to_Z_gamma": 0.025,
    "H_to_ss": math.sqrt(0.0702**2 + 0.0211**2),
}

BR_THEORY_REL = {
    "H_to_bb": 0.013,
    "H_to_cc": 0.038,
    "H_to_tau_tau": 0.036,
    "H_to_mu_mu": 0.039,
    "H_to_WW_star": 0.022,
    "H_to_ZZ_star": 0.022,
    "H_to_gg": 0.045,
    "H_to_gamma_gamma": 0.029,
    "H_to_Z_gamma": 0.069,
    "H_to_ss": 0.0073,
}

TOTAL_WIDTH_REL = 0.0387
NUISANCE_BASIS = ["total_width_norm", "branching_ratio_parametric", "branching_ratio_theory"]


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_response_matrix(widths: dict[str, float]) -> dict[str, dict[str, float]]:
    return {
        channel: {
            "total_width_norm": TOTAL_WIDTH_REL,
            "branching_ratio_parametric": BR_PARAMETRIC_REL[channel],
            "branching_ratio_theory": BR_THEORY_REL[channel],
        }
        for channel in widths
    }


def build_covariance(widths: dict[str, float], responses: dict[str, dict[str, float]]) -> list[list[float]]:
    covariance: list[list[float]] = []
    for row_channel in ROW_BASIS:
        row = []
        for col_channel in ROW_BASIS:
            rel_cov = sum(
                responses[row_channel][nuisance] * responses[col_channel][nuisance]
                for nuisance in NUISANCE_BASIS
            )
            row.append(widths[row_channel] * widths[col_channel] * rel_cov)
        covariance.append(row)
    return covariance


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgsexternalprofiledata_or_routeaformularows.candidate.json")
    central = load(
        DATA
        / "selected_higgsexternalprofiledata_or_routeaformularows"
        / "hybrid_external_central_profile_values.packet.json"
    )
    previous_promotion = load(
        DATA
        / "selected_higgsexternalprofiledata_or_routeaformularows"
        / "higgs_precision_promotion_after_central_values.packet.json"
    )
    previous_true = load(
        DATA
        / "selected_higgsexternalprofiledata_or_routeaformularows"
        / "updated_true_equivalence_gate_after_higgs_central_values.packet.json"
    )

    widths = {channel: central["central_widths_GeV"][channel] for channel in ROW_BASIS}
    responses = build_response_matrix(widths)
    covariance = build_covariance(widths, responses)
    diagonal_variances = {channel: covariance[i][i] for i, channel in enumerate(ROW_BASIS)}

    homogeneous_assessment = {
        "schema": "MTTHiggsHomogeneousProfileRouteAssessment.v1",
        "status": "HOMOGENEOUS_PROFILE_ROUTE_ASSESSED_NOT_CLOSED",
        "single_source_profile_found": False,
        "primary_source_family": "LHCHXSWG/CERN Yellow Report Higgs branching-ratio tables",
        "primary_source_rows_covered": [
            "H_to_bb",
            "H_to_cc",
            "H_to_tau_tau",
            "H_to_mu_mu",
            "H_to_WW_star",
            "H_to_ZZ_star",
            "H_to_gg",
            "H_to_gamma_gamma",
            "H_to_Z_gamma",
        ],
        "separate_source_rows_required": ["H_to_ss"],
        "full_covariance_or_nuisance_profile_found": False,
        "accepted_as_homogeneous_correlated_profile": False,
        "reason": (
            "The repo's ten-row basis includes H_to_ss. The current central packet uses a 2025 LHCHWG strange-row "
            "update in addition to the 125.09 GeV LHCHXSWG table, and no single full ten-row covariance/nuisance "
            "profile is imported."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    correlated_model = {
        "schema": "MTTHiggsSourceDerivedCorrelatedCovarianceModel.v1",
        "status": "SOURCE_DERIVED_CORRELATED_COVARIANCE_MODEL_BUILT_NOT_OFFICIAL_PROFILE",
        "row_basis": ROW_BASIS,
        "nuisance_basis": NUISANCE_BASIS,
        "central_widths_GeV": widths,
        "relative_response_matrix": responses,
        "covariance_matrix_GeV2": covariance,
        "diagonal_variances_GeV2": diagonal_variances,
        "construction": (
            "For central partial widths Gamma_i, set Cov_ij = Gamma_i Gamma_j sum_a r_ia r_ja. "
            "The three aggregate nuisance directions are total-width normalization, branching-ratio parametric "
            "uncertainty, and branching-ratio theory uncertainty."
        ),
        "is_symmetric": True,
        "is_psd_by_gram_construction": True,
        "rank_bound": len(NUISANCE_BASIS),
        "improves_over_diagonal_sidecar": True,
        "accepted_as_official_full_correlated_profile": False,
        "accepted_as_route_A_formula_covariance": False,
        "accepted_as_source_derived_covariance_model": True,
        "guardrails": {
            "aggregate_uncertainty_model_not_official_likelihood": True,
            "single_source_homogeneous_profile_not_claimed": True,
            "route_A_formula_rows_not_computed": True,
            "used_to_select_source": False,
            "fit_factor_applied_to_repo_rows": False,
            "benchmark_ratio_used_as_correction": False,
        },
        "provenance": central["provenance"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    route_a_status = {
        "schema": "MTTHiggsRouteAFormulaCovarianceStatus.v1",
        "status": "ROUTE_A_FORMULA_COVARIANCE_NOT_COMPUTED_SOURCE_MODEL_AVAILABLE",
        "route_A_formula_rows_computed": 0,
        "route_A_formula_covariance_contributions_computed": 0,
        "source_derived_covariance_model_available": True,
        "source_derived_covariance_model_accepted": True,
        "source_model_can_support_central_replay_uncertainty": True,
        "source_model_can_replace_route_A_formula_covariance": False,
        "why_route_A_still_open": [
            "The covariance model is inferred from source uncertainty components, not from independent formula differentiation.",
            "The WW*/ZZ*/Zgamma off-shell kernels are still imported by convention rather than recomputed.",
            "QCD and rare-loop rows are not recomputed under a unified route-A formula engine.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    promotion = {
        "schema": "MTTHiggsPrecisionPromotionAfterCovarianceModel.v1",
        "status": "CORRELATED_MODEL_READY_FULL_PROFILE_AND_ROUTEA_PRECISION_OPEN",
        "central_values_filled": True,
        "source_derived_correlated_covariance_model_built": True,
        "diagonal_sidecar_upgraded_to_correlated_model": True,
        "homogeneous_single_source_profile_closed": False,
        "official_full_covariance_or_nuisance_profile_closed": False,
        "route_A_formula_covariance_closed": False,
        "accepted_as_downstream_central_replay_with_covariance_model": True,
        "precision_total_width_closed": False,
        "precision_branching_ratios_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "remaining_gap": (
            "Promote by importing one official homogeneous ten-row profile with covariance/nuisance semantics, or by "
            "executing route-A formulas and differentiating their declared inputs to obtain covariance contributions."
        ),
        "previous_promotion_status": previous_promotion["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    updated_true = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterHiggsCovarianceModel.v1",
        "status": "HIGGS_CORRELATED_MODEL_BUILT_TRUE_EQUIVALENCE_STILL_OPEN",
        "previous_true_equivalence_blockers": previous_true["remaining_true_equivalence_blockers"],
        "closed_now": previous_true["closed_now"] + [
            "Higgs homogeneous-profile route assessment",
            "Higgs source-derived correlated covariance model",
            "Higgs route-A formula covariance status split",
        ],
        "remaining_true_equivalence_blockers": previous_true["remaining_true_equivalence_blockers"],
        "next_primary_value_gate": "official homogeneous Higgs covariance profile or independent route-A covariance differentiation",
        "guardrails": {
            "correlated_covariance_model_built": True,
            "accepted_as_official_full_correlated_profile": False,
            "route_A_formula_covariance_closed": False,
            "precision_total_width_closed": False,
            "precision_branching_ratios_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsHomogeneousProfileOrRouteAFormulaCovariance",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgsexternalprofiledata_or_routeaformularows.candidate.json"),
            "hybrid_external_central_profile": rel(
                DATA
                / "selected_higgsexternalprofiledata_or_routeaformularows"
                / "hybrid_external_central_profile_values.packet.json"
            ),
        },
        "output_packets": {
            "homogeneous_profile_route_assessment": rel(HOMOGENEOUS_ASSESSMENT),
            "source_derived_correlated_covariance_model": rel(CORRELATED_MODEL),
            "route_a_formula_covariance_status": rel(ROUTE_A_STATUS),
            "higgs_precision_promotion_after_covariance_model": rel(PROMOTION),
            "updated_true_equivalence_gate": rel(UPDATED_TRUE),
        },
        "theorem": {
            "name": "HiggsSourceDerivedCovarianceModelTheorem",
            "proved": True,
            "statement": (
                "The homogeneous profile route is assessed and remains open, while the diagonal uncertainty sidecar "
                "is upgraded to a source-derived correlated covariance model by Gram construction over aggregate "
                "total-width, parametric, and theory nuisance directions. This improves central replay uncertainty "
                "bookkeeping but does not close the official full profile or route-A formula covariance gates."
            ),
        },
        "what_closes_now": {
            "homogeneous_profile_route_assessment": True,
            "source_derived_correlated_covariance_model": True,
            "diagonal_uncertainty_sidecar_upgrade": True,
            "route_A_formula_covariance_status_split": True,
        },
        "what_remains_open": {
            "official_homogeneous_correlated_profile": True,
            "route_A_formula_value_and_covariance_execution": True,
            "precision_total_width": True,
            "precision_branching_ratios": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "correlated_covariance_model_built": True,
            "accepted_as_source_derived_covariance_model": True,
            "accepted_as_official_full_correlated_profile": False,
            "route_A_formula_covariance_closed": False,
            "precision_total_width_closed": False,
            "precision_branching_ratios_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_HiggsHomogeneousProfile_or_RouteAFormulaCovariance_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "correlated_covariance_model_built": True,
        "accepted_as_source_derived_covariance_model": True,
        "accepted_as_official_full_correlated_profile": False,
        "route_A_formula_covariance_closed": False,
        "precision_total_width_closed": False,
        "precision_branching_ratios_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_HiggsOfficialProfile_or_RouteAFormulaDifferentiation_v1",
    }

    note = f"""# MTT Selected HiggsHomogeneousProfile or RouteAFormulaCovariance v1

Status: `{STATUS}`.

This artifact assesses the homogeneous external-profile route and upgrades the
previous diagonal uncertainty sidecar to a source-derived correlated covariance
model. The covariance is built by a Gram formula over aggregate total-width,
parametric, and theory nuisance directions.

The model improves central SM-parity replay uncertainty bookkeeping, but it is
not an official full LHCHXSWG nuisance profile and not an independent route-A
formula covariance calculation. Precision total-width and branching-ratio
closure remain open.
"""

    for path, payload in [
        (HOMOGENEOUS_ASSESSMENT, homogeneous_assessment),
        (CORRELATED_MODEL, correlated_model),
        (ROUTE_A_STATUS, route_a_status),
        (PROMOTION, promotion),
        (UPDATED_TRUE, updated_true),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
