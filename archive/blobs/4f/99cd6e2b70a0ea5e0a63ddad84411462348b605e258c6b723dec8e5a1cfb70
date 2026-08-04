"""Build Higgs route-A derivative engine execution or precision decision."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgsrouteaderivativeengineexecution_or_precisiondecision"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
LEPTONIC_ROWS = PACKET_DIR / "route_a_leptonic_derivative_rows.packet.json"
COMPARISON = PACKET_DIR / "leptonic_rows_imported_profile_comparison.packet.json"
EXECUTION_STATUS = PACKET_DIR / "route_a_derivative_engine_execution_status.packet.json"
UPDATED_TRUE = PACKET_DIR / "updated_true_equivalence_gate_after_route_a_leptonic_execution.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsRouteADerivativeEngineExecution_or_PrecisionDecision_v1.md"

STATUS = "MTT_SELECTED_HIGGSROUTEADERIVATIVEENGINEEXECUTION_OR_PRECISIONDECISION_BUILT_LEPTONIC_DERIVATIVES_QCD_EW_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def symmetric_sigma(value: dict[str, Any]) -> float:
    uncertainty = value["uncertainty"]
    return (abs(float(uncertainty["plus"])) + abs(float(uncertainty["minus"]))) / 2.0


def gev_mass(value: dict[str, Any]) -> tuple[float, float]:
    central = float(value["central_value"])
    sigma = symmetric_sigma(value)
    if value["units"] == "MeV":
        return central / 1000.0, sigma / 1000.0
    if value["units"] == "GeV":
        return central, sigma
    raise ValueError(f"unsupported mass unit {value['units']}")


def leptonic_width(gf: float, mh: float, ml: float) -> float:
    beta2 = 1.0 - 4.0 * ml * ml / (mh * mh)
    return gf * mh * ml * ml * beta2**1.5 / (4.0 * math.pi * math.sqrt(2.0))


def derivative_row(gf: float, mh: float, ml: float) -> dict[str, float]:
    gamma = leptonic_width(gf, mh, ml)
    beta2 = 1.0 - 4.0 * ml * ml / (mh * mh)
    # d log Gamma = d log G_F + d log M_H + 2 d log m_l + 3/2 d log beta2.
    d_gf = gamma / gf
    d_mh = gamma * (1.0 / mh + 12.0 * ml * ml / (mh**3 * beta2))
    d_ml = gamma * (2.0 / ml - 12.0 * ml / (mh * mh * beta2))
    return {"G_F": d_gf, "M_H": d_mh, "m_l": d_ml}


def propagate_sigma(derivatives: dict[str, float], sigmas: dict[str, float]) -> tuple[float, dict[str, float]]:
    contributions = {
        key: derivatives[key] * derivatives[key] * sigmas[key] * sigmas[key]
        for key in derivatives
    }
    return math.sqrt(sum(contributions.values())), contributions


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgsrouteaformuladerivativeengines_or_officiallikelihooddecision.candidate.json")
    reference = load(DATA / "sm_equivalence_reference_data_values_fill.candidate.json")
    imported_profile = load(
        DATA
        / "selected_higgsrouteaformuladerivativeengines_or_officiallikelihoodimport"
        / "repo_basis_decay_covariance_import.packet.json"
    )
    previous_true = load(
        DATA
        / "selected_higgsrouteaformuladerivativeengines_or_officiallikelihooddecision"
        / "updated_true_equivalence_gate_after_official_likelihood_decision.packet.json"
    )

    masses = reference["reference_values"]["masses"]
    constants = reference["reference_values"]["constants"]
    gf = float(constants["G_F"]["central_value"])
    gf_sigma = symmetric_sigma(constants["G_F"])
    mh, mh_sigma = gev_mass(masses["H"])

    row_specs = [
        ("H_to_tau_tau", "tau"),
        ("H_to_mu_mu", "mu"),
    ]

    rows = {}
    covariance = [[0.0 for _ in row_specs] for _ in row_specs]
    for i, (channel, lepton_key) in enumerate(row_specs):
        ml, ml_sigma = gev_mass(masses[lepton_key])
        gamma = leptonic_width(gf, mh, ml)
        derivatives = derivative_row(gf, mh, ml)
        sigma, variance_contributions = propagate_sigma(
            derivatives,
            {"G_F": gf_sigma, "M_H": mh_sigma, "m_l": ml_sigma},
        )
        rows[channel] = {
            "schema": "MTTHiggsRouteALeptonicDerivativeRow.v1",
            "status": "ROUTE_A_TREE_LEPTONIC_DERIVATIVE_ROW_EXECUTED",
            "channel": channel,
            "formula": "Gamma(H->ll)=G_F*M_H*m_l^2/(4*pi*sqrt(2))*(1-4*m_l^2/M_H^2)^(3/2)",
            "input_values": {
                "G_F_GeV_minus2": gf,
                "M_H_GeV": mh,
                "m_l_GeV": ml,
            },
            "input_sigmas": {
                "G_F_GeV_minus2": gf_sigma,
                "M_H_GeV": mh_sigma,
                "m_l_GeV": ml_sigma,
            },
            "central_width_GeV": gamma,
            "analytic_derivatives": {
                "dGamma_dG_F": derivatives["G_F"],
                "dGamma_dM_H": derivatives["M_H"],
                "dGamma_dm_l": derivatives["m_l"],
            },
            "propagated_sigma_GeV": sigma,
            "relative_sigma": sigma / gamma,
            "variance_contributions_GeV2": {
                "G_F": variance_contributions["G_F"],
                "M_H": variance_contributions["M_H"],
                "m_l": variance_contributions["m_l"],
            },
            "accepted_as_route_A_formula_derivative_row": True,
            "accepted_as_full_precision_row": False,
            "why_not_full_precision": (
                "This is the tree-level leptonic row with input uncertainty propagation. "
                "Electroweak/radiative correction policy and full ten-row covariance remain open."
            ),
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
        }
        covariance[i][i] += sigma * sigma
        for j in range(i):
            # G_F and M_H are common inputs, so they induce cross-row covariance.
            other_channel = row_specs[j][0]
            other = rows[other_channel]
            cross = (
                derivatives["G_F"] * other["analytic_derivatives"]["dGamma_dG_F"] * gf_sigma * gf_sigma
                + derivatives["M_H"] * other["analytic_derivatives"]["dGamma_dM_H"] * mh_sigma * mh_sigma
            )
            covariance[i][j] = cross
            covariance[j][i] = cross

    row_basis = [channel for channel, _ in row_specs]
    route_a_rows = {
        "schema": "MTTHiggsRouteALeptonicDerivativeRows.v1",
        "status": "ROUTE_A_LEPTONIC_DERIVATIVE_ROWS_EXECUTED",
        "row_basis": row_basis,
        "rows": rows,
        "leptonic_covariance_GeV2": covariance,
        "covariance_sources": [
            "diagonal lepton mass uncertainties",
            "shared G_F uncertainty",
            "shared Higgs-mass uncertainty",
        ],
        "rows_executed": len(row_basis),
        "accepted_as_route_A_leptonic_derivative_block": True,
        "accepted_as_full_Higgs_precision_block": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    comparison_rows = {}
    for channel in row_basis:
        formula_width = rows[channel]["central_width_GeV"]
        imported_width = imported_profile["central_widths_GeV"][channel]
        delta = formula_width - imported_width
        comparison_rows[channel] = {
            "route_A_tree_formula_width_GeV": formula_width,
            "imported_profile_central_width_GeV": imported_width,
            "delta_GeV": delta,
            "relative_delta_vs_imported": delta / imported_width,
            "used_for_source_selection": False,
            "interpretation": (
                "Diagnostic comparison only. The imported central profile contains precision/radiative convention "
                "content, while this route-A row is tree-level."
            ),
        }

    comparison = {
        "schema": "MTTHiggsLeptonicRowsImportedProfileComparison.v1",
        "status": "TREE_LEPTONIC_ROUTE_A_ROWS_COMPARED_TO_IMPORTED_PROFILE_DIAGNOSTIC_ONLY",
        "comparison_rows": comparison_rows,
        "max_abs_relative_delta_vs_imported": max(
            abs(row["relative_delta_vs_imported"]) for row in comparison_rows.values()
        ),
        "comparison_used_as_selector": False,
        "precision_promotion_from_comparison": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    execution_status = {
        "schema": "MTTHiggsRouteADerivativeEngineExecutionStatus.v1",
        "status": "LEPTONIC_ROUTE_A_ROWS_EXECUTED_REMAINING_ROWS_OPEN",
        "rows_required_total": 10,
        "rows_executed_now": row_basis,
        "rows_remaining": [
            "H_to_bb",
            "H_to_cc",
            "H_to_ss",
            "H_to_gg",
            "H_to_gamma_gamma",
            "H_to_Z_gamma",
            "H_to_WW_star",
            "H_to_ZZ_star",
        ],
        "precision_total_width_closed": False,
        "precision_branching_ratios_closed": False,
        "next_route_A_block": "fermionic_width_qcd_running_mass_threshold for bb, cc, ss",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    updated_true = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterRouteALeptonicExecution.v1",
        "status": "ROUTE_A_LEPTONIC_DERIVATIVES_BUILT_TRUE_EQUIVALENCE_STILL_OPEN",
        "previous_gate": rel(
            DATA
            / "selected_higgsrouteaformuladerivativeengines_or_officiallikelihooddecision"
            / "updated_true_equivalence_gate_after_official_likelihood_decision.packet.json"
        ),
        "closed_now": previous_true["closed_now"] + [
            "Route-A analytic derivative rows for H_to_tau_tau and H_to_mu_mu",
            "Route-A leptonic input uncertainty propagation",
            "Diagnostic imported-profile comparison for leptonic rows",
        ],
        "remaining_true_equivalence_blockers": previous_true["remaining_true_equivalence_blockers"],
        "next_primary_value_gate": "route-A QCD fermionic derivative rows for bb, cc, ss",
        "guardrails": {
            "route_A_leptonic_rows_executed": True,
            "full_route_A_ten_row_engine_closed": False,
            "comparison_used_as_selector": False,
            "precision_total_width_closed": False,
            "precision_branching_ratios_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsRouteADerivativeEngineExecutionOrPrecisionDecision",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgsrouteaformuladerivativeengines_or_officiallikelihooddecision.candidate.json"),
            "reference_values": rel(DATA / "sm_equivalence_reference_data_values_fill.candidate.json"),
            "imported_profile": rel(
                DATA
                / "selected_higgsrouteaformuladerivativeengines_or_officiallikelihoodimport"
                / "repo_basis_decay_covariance_import.packet.json"
            ),
        },
        "output_packets": {
            "route_a_leptonic_derivative_rows": rel(LEPTONIC_ROWS),
            "leptonic_rows_imported_profile_comparison": rel(COMPARISON),
            "route_a_derivative_engine_execution_status": rel(EXECUTION_STATUS),
            "updated_true_equivalence_gate": rel(UPDATED_TRUE),
        },
        "theorem": {
            "name": "HiggsRouteALeptonicDerivativeExecutionTheorem",
            "proved": True,
            "statement": (
                "The route-A tree-level leptonic Higgs partial-width formula has been executed and analytically "
                "differentiated for H_to_tau_tau and H_to_mu_mu using downstream reference inputs only. This closes "
                "the leptonic derivative block, while QCD, loop, off-shell, precision, true SM-equivalence, and "
                "no-knob closure remain open."
            ),
        },
        "what_closes_now": {
            "route_A_H_to_tau_tau_tree_derivative_row": True,
            "route_A_H_to_mu_mu_tree_derivative_row": True,
            "leptonic_route_A_uncertainty_propagation": True,
            "diagnostic_imported_profile_comparison": True,
        },
        "what_remains_open": {
            "QCD_fermionic_rows_bb_cc_ss": True,
            "loop_rows_gg_gamma_gamma_Z_gamma": True,
            "off_shell_rows_WW_ZZ": True,
            "electroweak_and_radiative_correction_policy": True,
            "precision_total_width": True,
            "precision_branching_ratios": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "route_A_leptonic_derivative_block_closed": True,
            "full_route_A_ten_row_engine_closed": False,
            "accepted_as_full_Higgs_precision": False,
            "precision_total_width_closed": False,
            "precision_branching_ratios_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_HiggsQCDRouteADerivativeRows_or_PrecisionDecision_v1",
    }

    cert = {
        "certificate": "MTT_Selected_HiggsRouteADerivativeEngineExecution_or_PrecisionDecision_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "route_A_leptonic_derivative_block_closed": True,
        "full_route_A_ten_row_engine_closed": False,
        "precision_total_width_closed": False,
        "precision_branching_ratios_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }

    note = f"""# MTT Selected HiggsRouteADerivativeEngineExecution or PrecisionDecision v1

Status: `{STATUS}`.

This artifact executes the first route-A Higgs derivative engines: the tree-level
leptonic rows `H_to_tau_tau` and `H_to_mu_mu`.

For each row it records:

- the analytic formula;
- the central partial width from downstream reference inputs;
- analytic derivatives with respect to `G_F`, `M_H`, and the lepton mass;
- first-order uncertainty propagation;
- a diagnostic comparison against the imported profile, with no source
  selection or fitting.

This closes the leptonic derivative block only. QCD fermionic rows, loop rows,
off-shell rows, electroweak/radiative corrections, total precision Higgs
closure, true SM equivalence, and no-knob closure remain open.
"""

    for path, payload in [
        (LEPTONIC_ROWS, route_a_rows),
        (COMPARISON, comparison),
        (EXECUTION_STATUS, execution_status),
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
