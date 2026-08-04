"""Build Higgs loop/off-shell route-A derivative rows or precision decision."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgsloopoffshellrouteaderivativerows_or_precisiondecision"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
LOOP_ROWS = PACKET_DIR / "route_a_loop_derivative_rows.packet.json"
COMPARISON = PACKET_DIR / "loop_rows_imported_profile_comparison.packet.json"
OPEN_ROWS = PACKET_DIR / "offshell_and_zgamma_open_kernel_contract.packet.json"
PRECISION_DECISION = PACKET_DIR / "loop_offshell_route_a_precision_decision.packet.json"
UPDATED_TRUE = PACKET_DIR / "updated_true_equivalence_gate_after_loop_offshell_rows.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsLoopOffshellRouteADerivativeRows_or_PrecisionDecision_v1.md"

STATUS = "MTT_SELECTED_HIGGSLOOPOFFSHELLROUTEADERIVATIVEROWS_OR_PRECISIONDECISION_BUILT_GG_GAMMAGAMMA_DERIVATIVES_ZGAMMA_WW_ZZ_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def symmetric_sigma(value: dict[str, Any]) -> float:
    uncertainty = value["uncertainty"]
    if isinstance(uncertainty, dict):
        return (abs(float(uncertainty["plus"])) + abs(float(uncertainty["minus"]))) / 2.0
    return float(uncertainty)


def gev_mass(value: dict[str, Any]) -> tuple[float, float]:
    central = float(value["central_value"])
    sigma = symmetric_sigma(value)
    if value["units"] == "MeV":
        return central / 1000.0, sigma / 1000.0
    if value["units"] == "GeV":
        return central, sigma
    raise ValueError(f"unsupported unit {value['units']}")


def variance(derivatives: dict[str, float], sigmas: dict[str, float]) -> tuple[float, dict[str, float]]:
    contributions = {
        key: derivatives[key] * derivatives[key] * sigmas[key] * sigmas[key]
        for key in derivatives
    }
    return math.sqrt(sum(contributions.values())), contributions


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgsqcdrouteaderivativerows_or_precisiondecision.candidate.json")
    reference = load(DATA / "sm_equivalence_reference_data_values_fill.candidate.json")
    gauge = load(DATA / "sm_equivalence_mixing_and_gauge_replay.candidate.json")
    gg = load(
        DATA
        / "selected_higgsggkernelrow_or_electroweakrows"
        / "higgs_gg_heavytop_kernel_row.packet.json"
    )
    gamma = load(
        DATA
        / "selected_higgsgammagammacorrection_or_qcdthresholdrows"
        / "higgs_gamma_gamma_all_charged_fermion_oneloop.packet.json"
    )
    ew_readiness = load(
        DATA
        / "selected_higgsewformulakernelexecution_or_precisionimportrows"
        / "ew_formula_kernel_execution_readiness.packet.json"
    )
    imported_profile = load(
        DATA
        / "selected_higgsrouteaformuladerivativeengines_or_officiallikelihoodimport"
        / "repo_basis_decay_covariance_import.packet.json"
    )
    previous_true = load(
        DATA
        / "selected_higgsqcdrouteaderivativerows_or_precisiondecision"
        / "updated_true_equivalence_gate_after_qcd_route_a_rows.packet.json"
    )

    masses = reference["reference_values"]["masses"]
    constants = reference["reference_values"]["constants"]
    gauge_inputs = gauge["gauge_replay_MZ"]["filled_inputs"]
    gf = float(constants["G_F"]["central_value"])
    gf_sigma = symmetric_sigma(constants["G_F"])
    mh, mh_sigma = gev_mass(masses["H"])
    alpha_s_sigma = float(gauge_inputs["alpha_s_MZ"]["uncertainty"])
    alpha_em = float(gauge_inputs["alpha_em_MSbar_MZ"]["central_value"])
    alpha_em_sigma = float(gauge_inputs["alpha_em_MSbar_MZ"]["uncertainty"])

    gg_width = float(gg["width_GeV"])
    gg_alpha_s = float(gg["alpha_s_mH_proxy"])
    gg_k = float(gg["NLO_proxy_factor"])
    gg_coeff = float(gg["NLO_QCD_coefficient_nf5"])
    gg_derivatives = {
        "G_F": gg_width / gf,
        "M_H_fixed_alpha_s": 3.0 * gg_width / mh,
        "alpha_s_effective": gg_width * (2.0 / gg_alpha_s + (gg_coeff / math.pi) / gg_k),
        "K_QCD": float(gg["LO_width_GeV"]),
    }
    gg_sigma, gg_var = variance(
        gg_derivatives,
        {
            "G_F": gf_sigma,
            "M_H_fixed_alpha_s": mh_sigma,
            "alpha_s_effective": alpha_s_sigma,
            "K_QCD": abs(gg_k - 1.0) * alpha_s_sigma / gg_alpha_s,
        },
    )

    gamma_width = float(gamma["all_charged_one_loop_width_GeV"])
    amp_abs = float(gamma["amplitude_total"]["abs"])
    gamma_derivatives = {
        "G_F": gamma_width / gf,
        "M_H_fixed_amplitude": 3.0 * gamma_width / mh,
        "alpha_em": 2.0 * gamma_width / alpha_em,
        "amplitude_abs": 2.0 * gamma_width / amp_abs,
    }
    # Amplitude uncertainty is a diagnostic slot, not a precision covariance.
    amplitude_slot_sigma = 0.01 * amp_abs
    gamma_sigma, gamma_var = variance(
        gamma_derivatives,
        {
            "G_F": gf_sigma,
            "M_H_fixed_amplitude": mh_sigma,
            "alpha_em": alpha_em_sigma,
            "amplitude_abs": amplitude_slot_sigma,
        },
    )

    rows = {
        "H_to_gg": {
            "schema": "MTTHiggsLoopRouteADerivativeRow.v1",
            "status": "ROUTE_A_H_TO_GG_HEAVY_TOP_DERIVATIVE_ROW_EXECUTED_PROXY_PRECISION_OPEN",
            "channel": "H_to_gg",
            "formula": gg["kernel_formula"],
            "source_kernel_status": gg["status"],
            "input_values": {
                "G_F_GeV_minus2": gf,
                "M_H_GeV": mh,
                "alpha_s_mH_proxy": gg_alpha_s,
                "K_QCD_proxy": gg_k,
            },
            "input_sigmas": {
                "G_F_GeV_minus2": gf_sigma,
                "M_H_GeV": mh_sigma,
                "alpha_s_MZ_for_effective_sensitivity": alpha_s_sigma,
                "K_QCD_effective": abs(gg_k - 1.0) * alpha_s_sigma / gg_alpha_s,
            },
            "central_width_GeV": gg_width,
            "analytic_derivatives": gg_derivatives,
            "propagated_sigma_GeV": gg_sigma,
            "relative_sigma": gg_sigma / gg_width,
            "variance_contributions_GeV2": gg_var,
            "accepted_as_route_A_formula_derivative_row": True,
            "accepted_as_full_precision_row": False,
            "why_not_full_precision": gg["why_not_precision"],
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
        },
        "H_to_gamma_gamma": {
            "schema": "MTTHiggsLoopRouteADerivativeRow.v1",
            "status": "ROUTE_A_H_TO_GAMMA_GAMMA_ONE_LOOP_DERIVATIVE_ROW_EXECUTED_PROXY_PRECISION_OPEN",
            "channel": "H_to_gamma_gamma",
            "formula": gamma["kernel_formula"],
            "source_kernel_status": gamma["status"],
            "input_values": {
                "G_F_GeV_minus2": gf,
                "M_H_GeV": mh,
                "alpha_em_MSbar_MZ": alpha_em,
                "amplitude_abs": amp_abs,
            },
            "input_sigmas": {
                "G_F_GeV_minus2": gf_sigma,
                "M_H_GeV": mh_sigma,
                "alpha_em_MSbar_MZ": alpha_em_sigma,
                "amplitude_abs_diagnostic_slot": amplitude_slot_sigma,
            },
            "central_width_GeV": gamma_width,
            "analytic_derivatives": gamma_derivatives,
            "propagated_sigma_GeV": gamma_sigma,
            "relative_sigma": gamma_sigma / gamma_width,
            "variance_contributions_GeV2": gamma_var,
            "accepted_as_route_A_formula_derivative_row": True,
            "accepted_as_full_precision_row": False,
            "why_not_full_precision": gamma["why_not_precision"],
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
        },
    }

    row_basis = ["H_to_gg", "H_to_gamma_gamma"]
    covariance = [[0.0 for _ in row_basis] for _ in row_basis]
    covariance[0][0] = gg_sigma**2
    covariance[1][1] = gamma_sigma**2
    covariance[0][1] = covariance[1][0] = (
        gg_derivatives["G_F"] * gamma_derivatives["G_F"] * gf_sigma**2
        + gg_derivatives["M_H_fixed_alpha_s"] * gamma_derivatives["M_H_fixed_amplitude"] * mh_sigma**2
    )

    loop_rows = {
        "schema": "MTTHiggsLoopRouteADerivativeRows.v1",
        "status": "ROUTE_A_GG_AND_GAMMAGAMMA_LOOP_DERIVATIVE_ROWS_EXECUTED_PROXY_PRECISION_OPEN",
        "row_basis": row_basis,
        "rows": rows,
        "loop_covariance_GeV2": covariance,
        "rows_executed": len(row_basis),
        "accepted_as_route_A_loop_derivative_block": True,
        "accepted_as_full_Higgs_precision_block": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    comparison_rows = {}
    for channel in row_basis:
        width = rows[channel]["central_width_GeV"]
        imported_width = imported_profile["central_widths_GeV"][channel]
        delta = width - imported_width
        comparison_rows[channel] = {
            "route_A_loop_proxy_width_GeV": width,
            "imported_profile_central_width_GeV": imported_width,
            "delta_GeV": delta,
            "relative_delta_vs_imported": delta / imported_width,
            "used_for_source_selection": False,
            "interpretation": "Diagnostic comparison only; loop proxy lacks full higher-order scheme and covariance content.",
        }

    comparison = {
        "schema": "MTTHiggsLoopRowsImportedProfileComparison.v1",
        "status": "LOOP_ROUTE_A_PROXY_ROWS_COMPARED_TO_IMPORTED_PROFILE_DIAGNOSTIC_ONLY",
        "comparison_rows": comparison_rows,
        "max_abs_relative_delta_vs_imported": max(abs(row["relative_delta_vs_imported"]) for row in comparison_rows.values()),
        "comparison_used_as_selector": False,
        "precision_promotion_from_comparison": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    open_rows = {
        "schema": "MTTHiggsOffshellAndZGammaOpenKernelContract.v1",
        "status": "ZGAMMA_WW_ZZ_ROUTE_A_KERNELS_OPEN",
        "rows": ew_readiness["rows"],
        "open_row_basis": ["H_to_Z_gamma", "H_to_WW_star", "H_to_ZZ_star"],
        "formula_kernels_filled": 0,
        "central_imports_available_but_not_route_A_derivatives": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    precision_decision = {
        "schema": "MTTHiggsLoopOffshellRouteAPrecisionDecision.v1",
        "status": "GG_GAMMAGAMMA_DERIVATIVE_ROWS_EXECUTED_ZGAMMA_WW_ZZ_OPEN_PRECISION_REJECTED",
        "route_A_loop_rows_executed": row_basis,
        "route_A_rows_closed_total_including_previous": 7,
        "rows_remaining_for_route_A_ten_row_engine": ["H_to_Z_gamma", "H_to_WW_star", "H_to_ZZ_star"],
        "precision_total_width_closed": False,
        "precision_branching_ratios_closed": False,
        "precision_rejection_reasons": [
            "H_to_gg uses heavy-top NLO proxy, not exact mass-dependent multiloop QCD/EW structure.",
            "H_to_gamma_gamma uses one-loop all-charged proxy, not full higher-order scheme conversion.",
            "H_to_Z_gamma, H_to_WW_star, and H_to_ZZ_star route-A kernels remain open.",
        ],
        "next_route_A_block": "construct route-A kernels for Z gamma and off-shell WW*/ZZ* or retire to precision import policy",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    updated_true = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterLoopOffshellRows.v1",
        "status": "ROUTE_A_GG_GAMMAGAMMA_DERIVATIVES_BUILT_ZGAMMA_WW_ZZ_OPEN",
        "previous_gate": rel(
            DATA
            / "selected_higgsqcdrouteaderivativerows_or_precisiondecision"
            / "updated_true_equivalence_gate_after_qcd_route_a_rows.packet.json"
        ),
        "closed_now": previous_true["closed_now"] + [
            "Route-A loop derivative row for H_to_gg",
            "Route-A loop derivative row for H_to_gamma_gamma",
            "Open-kernel contract for H_to_Z_gamma, H_to_WW_star, and H_to_ZZ_star",
        ],
        "remaining_true_equivalence_blockers": previous_true["remaining_true_equivalence_blockers"],
        "next_primary_value_gate": "route-A Zgamma and off-shell WW/ZZ kernels or precision import decision",
        "guardrails": {
            "route_A_loop_rows_executed": True,
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
        "candidate": "MTTSelectedHiggsLoopOffshellRouteADerivativeRowsOrPrecisionDecision",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgsqcdrouteaderivativerows_or_precisiondecision.candidate.json"),
            "gg_kernel": rel(DATA / "selected_higgsggkernelrow_or_electroweakrows" / "higgs_gg_heavytop_kernel_row.packet.json"),
            "gamma_gamma_kernel": rel(DATA / "selected_higgsgammagammacorrection_or_qcdthresholdrows" / "higgs_gamma_gamma_all_charged_fermion_oneloop.packet.json"),
            "ew_readiness": rel(DATA / "selected_higgsewformulakernelexecution_or_precisionimportrows" / "ew_formula_kernel_execution_readiness.packet.json"),
            "imported_profile": rel(DATA / "selected_higgsrouteaformuladerivativeengines_or_officiallikelihoodimport" / "repo_basis_decay_covariance_import.packet.json"),
        },
        "output_packets": {
            "route_a_loop_derivative_rows": rel(LOOP_ROWS),
            "loop_rows_imported_profile_comparison": rel(COMPARISON),
            "offshell_and_zgamma_open_kernel_contract": rel(OPEN_ROWS),
            "loop_offshell_route_a_precision_decision": rel(PRECISION_DECISION),
            "updated_true_equivalence_gate": rel(UPDATED_TRUE),
        },
        "theorem": {
            "name": "HiggsLoopRouteADerivativeRowsTheorem",
            "proved": True,
            "statement": (
                "The executable proxy loop kernels for H_to_gg and H_to_gamma_gamma have route-A derivative rows. "
                "This raises the route-A executed row count to seven of ten, while H_to_Z_gamma, H_to_WW_star, "
                "and H_to_ZZ_star kernels remain open and precision closure is rejected."
            ),
        },
        "what_closes_now": {
            "route_A_H_to_gg_derivative_row": True,
            "route_A_H_to_gamma_gamma_derivative_row": True,
            "open_contract_for_Zgamma_WW_ZZ": True,
        },
        "what_remains_open": {
            "route_A_H_to_Z_gamma_kernel": True,
            "route_A_H_to_WW_star_kernel": True,
            "route_A_H_to_ZZ_star_kernel": True,
            "precision_total_width": True,
            "precision_branching_ratios": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "route_A_loop_derivative_block_closed_for_gg_gammagamma": True,
            "route_A_rows_closed_total_including_previous": 7,
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
        "next_required_artifact": "MTT_Selected_HiggsOffshellZGammaRouteA_or_PrecisionImportDecision_v1",
    }

    cert = {
        "certificate": "MTT_Selected_HiggsLoopOffshellRouteADerivativeRows_or_PrecisionDecision_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "route_A_loop_derivative_block_closed_for_gg_gammagamma": True,
        "route_A_rows_closed_total_including_previous": 7,
        "full_route_A_ten_row_engine_closed": False,
        "precision_total_width_closed": False,
        "precision_branching_ratios_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }

    note = f"""# MTT Selected HiggsLoopOffshellRouteADerivativeRows or PrecisionDecision v1

Status: `{STATUS}`.

This artifact executes route-A derivative rows for the two currently executable
loop proxy kernels: `H_to_gg` and `H_to_gamma_gamma`.

It also records that `H_to_Z_gamma`, `H_to_WW_star`, and `H_to_ZZ_star` remain
open at the route-A kernel level. Their external central rows may be replayed,
but they are not formula-derivative rows.

This raises the route-A derivative-executed Higgs count to seven of ten. It does
not close full route-A, precision Higgs, true SM-equivalence, or no-knob
closure.
"""

    for path, payload in [
        (LOOP_ROWS, loop_rows),
        (COMPARISON, comparison),
        (OPEN_ROWS, open_rows),
        (PRECISION_DECISION, precision_decision),
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
