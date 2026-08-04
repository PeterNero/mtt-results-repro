"""Import published Higgs decay covariance profile or keep route-A engines open."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgsrouteaformuladerivativeengines_or_officiallikelihoodimport"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ANCILLARY_PROFILE = PACKET_DIR / "published_ancillary_decay_correlation_profile.packet.json"
REPO_IMPORT = PACKET_DIR / "repo_basis_decay_covariance_import.packet.json"
ROUTE_A_STATUS = PACKET_DIR / "route_a_derivative_engines_status.packet.json"
PROMOTION = PACKET_DIR / "higgs_likelihood_import_promotion_decision.packet.json"
UPDATED_TRUE = PACKET_DIR / "updated_true_equivalence_gate_after_higgs_profile_import.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsRouteAFormulaDerivativeEngines_or_OfficialLikelihoodImport_v1.md"

STATUS = "MTT_SELECTED_HIGGSROUTEAFORMULADERIVATIVEENGINES_OR_OFFICIALLIKELIHOODIMPORT_BUILT_PUBLISHED_DECAY_PROFILE_IMPORTED_OFFICIAL_LIKELIHOOD_OPEN"

SOURCE_LABELS = ["WW", "ZZ", "gaga", "Zga", "gg", "bb", "cc", "ss", "tautau", "mumu"]
SOURCE_UNCERTAINTIES = {
    "WW": 0.0212868996,
    "ZZ": 0.0244791689,
    "gaga": 0.0115440106,
    "Zga": 0.0176206817,
    "gg": 0.0388107541,
    "bb": 0.0125266676,
    "cc": 0.0543992901,
    "ss": 0.0243697187,
    "tautau": 0.0130541174,
    "mumu": 0.0130560345,
}

SOURCE_CORRELATION = {
    "WW": {"WW": 1.0, "ZZ": 0.996559302, "gaga": 0.562851304, "Zga": 0.990035921, "gg": 0.363947582, "bb": -0.862681491, "cc": -0.154185949, "ss": -0.286139144, "tautau": 0.0984486322, "mumu": 0.0981835974},
    "ZZ": {"WW": 0.996559302, "ZZ": 1.0, "gaga": 0.492903533, "Zga": 0.975199384, "gg": 0.307556014, "bb": -0.827162208, "cc": -0.151867744, "ss": -0.288019028, "tautau": 0.0163705001, "mumu": 0.0161111414},
    "gaga": {"WW": 0.562851304, "ZZ": 0.492903533, "gaga": 1.0, "Zga": 0.673199281, "gg": 0.771696416, "bb": -0.816359449, "cc": -0.114027604, "ss": -0.154836191, "tautau": 0.877385853, "mumu": 0.877251929},
    "Zga": {"WW": 0.990035921, "ZZ": 0.975199384, "gaga": 0.673199281, "Zga": 1.0, "gg": 0.455341675, "bb": -0.909844337, "cc": -0.156845110, "ss": -0.280771325, "tautau": 0.237233649, "mumu": 0.236981260},
    "gg": {"WW": 0.363947582, "ZZ": 0.307556014, "gaga": 0.771696416, "Zga": 0.455341675, "gg": 1.0, "bb": -0.732084436, "cc": -0.203233616, "ss": -0.702538437, "tautau": 0.696961880, "mumu": 0.696928743},
    "bb": {"WW": -0.862681491, "ZZ": -0.827162208, "gaga": -0.816359449, "Zga": -0.909844337, "gg": -0.732084436, "bb": 1.0, "cc": -0.0109218431, "ss": 0.459292012, "tautau": -0.476250458, "mumu": -0.476051672},
    "cc": {"WW": -0.154185949, "ZZ": -0.151867744, "gaga": -0.114027604, "Zga": -0.156845110, "gg": -0.203233616, "bb": -0.0109218431, "cc": 1.0, "ss": 0.246419889, "tautau": -0.0375762117, "mumu": -0.0375402289},
    "ss": {"WW": -0.286139144, "ZZ": -0.288019028, "gaga": -0.154836191, "Zga": -0.280771325, "gg": -0.702538437, "bb": 0.459292012, "cc": 0.246419889, "ss": 1.0, "tautau": 0.0105965081, "mumu": 0.0105776233},
    "tautau": {"WW": 0.0984486322, "ZZ": 0.0163705001, "gaga": 0.877385853, "Zga": 0.237233649, "gg": 0.696961880, "bb": -0.476250458, "cc": -0.0375762117, "ss": 0.0105965081, "tautau": 1.0, "mumu": 0.999999763},
    "mumu": {"WW": 0.0981835974, "ZZ": 0.0161111414, "gaga": 0.877251929, "Zga": 0.236981260, "gg": 0.696928743, "bb": -0.476051672, "cc": -0.0375402289, "ss": 0.0105776233, "tautau": 0.999999763, "mumu": 1.0},
}

REPO_TO_SOURCE = {
    "H_to_bb": "bb",
    "H_to_cc": "cc",
    "H_to_tau_tau": "tautau",
    "H_to_mu_mu": "mumu",
    "H_to_WW_star": "WW",
    "H_to_ZZ_star": "ZZ",
    "H_to_gg": "gg",
    "H_to_gamma_gamma": "gaga",
    "H_to_Z_gamma": "Zga",
    "H_to_ss": "ss",
}


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgsofficialprofile_or_routeaformuladifferentiation.candidate.json")
    previous_true = load(
        DATA
        / "selected_higgsofficialprofile_or_routeaformuladifferentiation"
        / "updated_true_equivalence_gate_after_higgs_replay_differentiation.packet.json"
    )
    central = load(
        DATA
        / "selected_higgsexternalprofiledata_or_routeaformularows"
        / "hybrid_external_central_profile_values.packet.json"
    )

    repo_basis = central["row_basis"]
    widths = {channel: central["central_widths_GeV"][channel] for channel in repo_basis}
    imported_unc = {channel: SOURCE_UNCERTAINTIES[REPO_TO_SOURCE[channel]] for channel in repo_basis}
    imported_corr = [
        [SOURCE_CORRELATION[REPO_TO_SOURCE[row]][REPO_TO_SOURCE[col]] for col in repo_basis]
        for row in repo_basis
    ]
    imported_cov = [
        [
            widths[row] * widths[col] * imported_unc[row] * imported_unc[col] * imported_corr[i][j]
            for j, col in enumerate(repo_basis)
        ]
        for i, row in enumerate(repo_basis)
    ]

    ancillary_profile = {
        "schema": "MTTPublishedAncillaryHiggsDecayCorrelationProfile.v1",
        "status": "PUBLISHED_ANCILLARY_DECAY_CORRELATION_PROFILE_IMPORTED",
        "source": {
            "title": "The correlation matrix of Higgs rates at the LHC",
            "arxiv": "1606.00455v2",
            "report_number": "CERN-TH-2016-130",
            "paper_url": "https://arxiv.org/abs/1606.00455",
            "ancillary_txt_url": "https://arxiv.org/src/1606.00455v2/anc/tables_i.txt",
            "ancillary_c_url": "https://arxiv.org/src/1606.00455v2/anc/tables_i.c",
            "retrieved_or_generated_date": "2026-05-31",
        },
        "source_decay_labels": SOURCE_LABELS,
        "relative_uncertainties": SOURCE_UNCERTAINTIES,
        "correlation_matrix": [[SOURCE_CORRELATION[row][col] for col in SOURCE_LABELS] for row in SOURCE_LABELS],
        "coverage": {
            "has_decay_uncertainties": True,
            "has_decay_correlation_matrix": True,
            "covers_repo_ten_decay_rows_after_mapping": True,
            "includes_production_rates_too": True,
        },
        "accepted_as_published_external_decay_correlation_profile": True,
        "accepted_as_official_LHCHXSWG_likelihood": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    repo_import = {
        "schema": "MTTRepoBasisHiggsDecayCovarianceImport.v1",
        "status": "REPO_BASIS_DECAY_COVARIANCE_IMPORTED_FROM_PUBLISHED_PROFILE",
        "repo_row_basis": repo_basis,
        "repo_to_source_label_map": REPO_TO_SOURCE,
        "central_widths_GeV": widths,
        "relative_uncertainties": imported_unc,
        "correlation_matrix": imported_corr,
        "covariance_matrix_GeV2": imported_cov,
        "is_symmetric": True,
        "has_nontrivial_offdiagonal_correlations": True,
        "covers_all_repo_rows": True,
        "accepted_as_external_full_decay_covariance_profile": True,
        "accepted_as_official_full_likelihood": False,
        "replaces_source_derived_covariance_model_for_replay": True,
        "guards": {
            "used_to_select_source": False,
            "fit_factor_applied_to_repo_rows": False,
            "benchmark_ratio_used_as_correction": False,
            "official_likelihood_claimed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    route_a_status = {
        "schema": "MTTHiggsRouteADerivativeEnginesStatus.v1",
        "status": "ROUTE_A_DERIVATIVE_ENGINES_STILL_OPEN_EXTERNAL_PROFILE_IMPORTED",
        "route_A_derivative_engines_built": False,
        "route_A_partial_width_formula_rows_differentiated": 0,
        "external_decay_covariance_profile_imported": True,
        "external_profile_can_drive_replay_covariance": True,
        "route_A_formula_differentiation_still_required_for_no_knob_or_formula_proof": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    promotion = {
        "schema": "MTTHiggsLikelihoodImportPromotionDecision.v1",
        "status": "PUBLISHED_EXTERNAL_DECAY_PROFILE_IMPORTED_OFFICIAL_LIKELIHOOD_STILL_OPEN",
        "published_external_decay_profile_imported": True,
        "repo_basis_decay_covariance_imported": True,
        "covers_repo_ten_rows": True,
        "accepted_as_external_full_decay_covariance_profile": True,
        "accepted_as_official_LHCHXSWG_likelihood": False,
        "route_A_derivative_engines_built": False,
        "precision_total_width_closed": False,
        "precision_branching_ratios_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "why_not_official_likelihood": [
            "The imported covariance profile is from a published CERN-TH/arXiv ancillary package, not an official LHCHXSWG likelihood release.",
            "It supplies uncertainties and correlations, but not a full likelihood/nuisance model with experimental/profile semantics.",
            "It enters downstream replay and cannot select MTT source structure.",
        ],
        "next_required_action": (
            "propagate this imported decay covariance through the repo replay maps, or locate an official LHCHXSWG "
            "machine-readable likelihood/profile with equivalent row coverage"
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    updated_true = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterHiggsProfileImport.v1",
        "status": "PUBLISHED_HIGGS_DECAY_PROFILE_IMPORTED_TRUE_EQUIVALENCE_STILL_OPEN",
        "previous_true_equivalence_blockers": previous_true["remaining_true_equivalence_blockers"],
        "closed_now": previous_true["closed_now"] + [
            "published Higgs decay uncertainty/correlation ancillary import",
            "repo-basis ten-row Higgs decay covariance import",
            "official-likelihood versus published-profile promotion split",
        ],
        "remaining_true_equivalence_blockers": previous_true["remaining_true_equivalence_blockers"],
        "next_primary_value_gate": "propagate imported decay covariance through replay maps or import official LHCHXSWG likelihood",
        "guardrails": {
            "published_external_decay_profile_imported": True,
            "accepted_as_official_LHCHXSWG_likelihood": False,
            "route_A_derivative_engines_built": False,
            "precision_total_width_closed": False,
            "precision_branching_ratios_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsRouteAFormulaDerivativeEnginesOrOfficialLikelihoodImport",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgsofficialprofile_or_routeaformuladifferentiation.candidate.json"),
            "central_profile_values": rel(
                DATA
                / "selected_higgsexternalprofiledata_or_routeaformularows"
                / "hybrid_external_central_profile_values.packet.json"
            ),
        },
        "output_packets": {
            "published_ancillary_decay_correlation_profile": rel(ANCILLARY_PROFILE),
            "repo_basis_decay_covariance_import": rel(REPO_IMPORT),
            "route_a_derivative_engines_status": rel(ROUTE_A_STATUS),
            "higgs_likelihood_import_promotion_decision": rel(PROMOTION),
            "updated_true_equivalence_gate": rel(UPDATED_TRUE),
        },
        "theorem": {
            "name": "PublishedHiggsDecayCovarianceImportTheorem",
            "proved": True,
            "statement": (
                "The published ancillary correlation profile from arXiv:1606.00455v2 contains a ten-decay "
                "uncertainty and correlation submatrix covering the repo Higgs decay rows after a fixed label map. "
                "It can be imported as an external full decay covariance profile for downstream replay, but it is "
                "not promoted to an official LHCHXSWG likelihood or to route-A formula differentiation."
            ),
        },
        "what_closes_now": {
            "published_external_decay_correlation_profile_import": True,
            "repo_basis_ten_row_decay_covariance_import": True,
            "official_likelihood_vs_external_profile_split": True,
        },
        "what_remains_open": {
            "official_LHCHXSWG_likelihood_import": True,
            "route_A_formula_derivative_engines": True,
            "precision_total_width": True,
            "precision_branching_ratios": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "external_full_decay_covariance_profile_imported": True,
            "accepted_as_official_LHCHXSWG_likelihood": False,
            "route_A_derivative_engines_built": False,
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
        "certificate": "MTT_Selected_HiggsRouteAFormulaDerivativeEngines_or_OfficialLikelihoodImport_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "external_full_decay_covariance_profile_imported": True,
        "accepted_as_official_LHCHXSWG_likelihood": False,
        "route_A_derivative_engines_built": False,
        "precision_total_width_closed": False,
        "precision_branching_ratios_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_HiggsImportedProfileReplay_or_OfficialLHCHXSWGLikelihood_v1",
    }

    note = f"""# MTT Selected HiggsRouteAFormulaDerivativeEngines or OfficialLikelihoodImport v1

Status: `{STATUS}`.

This artifact imports the published ancillary Higgs decay uncertainty and
correlation profile from arXiv:1606.00455v2 into the repo's ten-row Higgs decay
basis. It is a genuine external full decay covariance profile for downstream
replay.

It is not promoted to an official LHCHXSWG likelihood/profile: the source is a
published CERN-TH/arXiv ancillary covariance package, not an official likelihood
release, and it does not provide full nuisance/profile-likelihood semantics.
Route-A formula derivative engines also remain open.
"""

    for path, payload in [
        (ANCILLARY_PROFILE, ancillary_profile),
        (REPO_IMPORT, repo_import),
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
