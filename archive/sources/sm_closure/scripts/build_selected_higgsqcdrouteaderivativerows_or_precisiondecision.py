"""Build Higgs QCD route-A derivative rows or precision decision."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgsqcdrouteaderivativerows_or_precisiondecision"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
QCD_ROWS = PACKET_DIR / "route_a_qcd_fermionic_derivative_rows.packet.json"
COMPARISON = PACKET_DIR / "qcd_rows_imported_profile_comparison.packet.json"
PRECISION_DECISION = PACKET_DIR / "qcd_route_a_precision_decision.packet.json"
UPDATED_TRUE = PACKET_DIR / "updated_true_equivalence_gate_after_qcd_route_a_rows.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsQCDRouteADerivativeRows_or_PrecisionDecision_v1.md"

STATUS = "MTT_SELECTED_HIGGSQCDROUTEADERIVATIVEROWS_OR_PRECISIONDECISION_BUILT_QCD_FERMIONIC_DERIVATIVES_LOOPS_EW_OPEN"


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


def qcd_row(
    channel: str,
    quark_key: str,
    source: dict[str, Any],
    mh: float,
    mh_sigma: float,
    gf: float,
    gf_sigma: float,
    ref_mass: float,
    ref_mass_sigma: float,
    alpha_s_mh: float,
    alpha_s_mz_sigma: float,
) -> dict[str, Any]:
    if channel == "H_to_ss":
        gamma0 = float(source["Gamma0_running_mass_GeV"])
        k_factor = float(source["N3LO_massless_QCD_factor"])
        running_mass = float(source["running_mass_at_mH_GeV"])
        width = float(source["width_GeV"])
        kernel = source["kernel_formula"]
        source_status = source["status"]
    else:
        gamma0 = float(source["tree_width_with_running_mass_GeV"])
        k_factor = float(source["qcd_k_factor_at_mH_proxy"])
        running_mass = float(source["running_mass_at_mH_GeV"])
        width = float(source["running_mass_qcd_proxy_width_GeV"])
        kernel = "Gamma0(m_q(M_H))*K_QCD(alpha_s,M_H,thresholds)"
        source_status = source["id"]

    running_mass_sigma = abs(running_mass) * (ref_mass_sigma / ref_mass)
    # Effective K uncertainty from the local K(alpha_s) proxy slope. This is a
    # sensitivity diagnostic, not a full threshold/matching derivative.
    dk_dalpha_effective = (k_factor - 1.0) / alpha_s_mh if alpha_s_mh else 0.0
    k_sigma_effective = abs(dk_dalpha_effective) * alpha_s_mz_sigma

    derivatives = {
        "dGamma_dG_F": width / gf,
        "dGamma_dM_H_fixed_running_mass": width / mh,
        "dGamma_dm_q_running": 2.0 * width / running_mass,
        "dGamma_dK_QCD": gamma0,
        "effective_dGamma_dalpha_s_MZ_via_K_slot": gamma0 * dk_dalpha_effective,
    }
    variance_contributions = {
        "G_F": derivatives["dGamma_dG_F"] ** 2 * gf_sigma**2,
        "M_H": derivatives["dGamma_dM_H_fixed_running_mass"] ** 2 * mh_sigma**2,
        "m_q_running_from_reference_mass": derivatives["dGamma_dm_q_running"] ** 2 * running_mass_sigma**2,
        "K_QCD_effective_from_alpha_s_MZ": derivatives["dGamma_dK_QCD"] ** 2 * k_sigma_effective**2,
    }
    sigma = math.sqrt(sum(variance_contributions.values()))
    return {
        "schema": "MTTHiggsQCDRouteAFermionicDerivativeRow.v1",
        "status": "ROUTE_A_QCD_FERMIONIC_DERIVATIVE_ROW_EXECUTED_PROXY_PRECISION_OPEN",
        "channel": channel,
        "quark": quark_key,
        "formula": "Gamma(H->qq)=3*G_F*M_H*m_q(M_H)^2/(4*pi*sqrt(2))*K_QCD",
        "source_kernel_status": source_status,
        "source_kernel_formula": kernel,
        "input_values": {
            "G_F_GeV_minus2": gf,
            "M_H_GeV": mh,
            "m_q_running_at_M_H_GeV": running_mass,
            "K_QCD_proxy": k_factor,
            "alpha_s_mH_proxy": alpha_s_mh,
        },
        "input_sigmas": {
            "G_F_GeV_minus2": gf_sigma,
            "M_H_GeV": mh_sigma,
            "m_q_running_at_M_H_GeV_from_reference_mass": running_mass_sigma,
            "K_QCD_effective_from_alpha_s_MZ": k_sigma_effective,
        },
        "central_width_GeV": width,
        "Gamma0_running_mass_GeV": gamma0,
        "analytic_derivatives": derivatives,
        "propagated_sigma_GeV": sigma,
        "relative_sigma": sigma / width,
        "variance_contributions_GeV2": variance_contributions,
        "accepted_as_route_A_formula_derivative_row": True,
        "accepted_as_full_precision_row": False,
        "alpha_s_derivative_status": "EFFECTIVE_K_SLOT_SENSITIVITY_ONLY_FULL_THRESHOLD_DERIVATIVE_OPEN",
        "why_not_full_precision": (
            "The derivative row uses the repo running-mass/QCD proxy carrier. Full precision needs multiloop "
            "running and matching, finite-mass/EW corrections, full threshold covariance, and selected Qa/SU3."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgsrouteaderivativeengineexecution_or_precisiondecision.candidate.json")
    reference = load(DATA / "sm_equivalence_reference_data_values_fill.candidate.json")
    gauge = load(DATA / "sm_equivalence_mixing_and_gauge_replay.candidate.json")
    running_proxy = load(
        DATA
        / "selected_runningmasshiggsdecayproxy_or_precisionwidths"
        / "one_loop_running_mass_higgs_decay_proxy.packet.json"
    )
    ss_source = load(
        DATA
        / "selected_higgssskernelrow_or_remainingchannels"
        / "higgs_ss_running_mass_kernel_row.packet.json"
    )
    imported_profile = load(
        DATA
        / "selected_higgsrouteaformuladerivativeengines_or_officiallikelihoodimport"
        / "repo_basis_decay_covariance_import.packet.json"
    )
    previous_true = load(
        DATA
        / "selected_higgsrouteaderivativeengineexecution_or_precisiondecision"
        / "updated_true_equivalence_gate_after_route_a_leptonic_execution.packet.json"
    )

    masses = reference["reference_values"]["masses"]
    constants = reference["reference_values"]["constants"]
    gf = float(constants["G_F"]["central_value"])
    gf_sigma = symmetric_sigma(constants["G_F"])
    mh, mh_sigma = gev_mass(masses["H"])
    alpha_s_mz_sigma = float(gauge["gauge_replay_MZ"]["filled_inputs"]["alpha_s_MZ"]["uncertainty"])
    alpha_s_mh = float(running_proxy["alpha_s_values"]["alpha_s_mH_proxy"])
    source_by_quark = {row["fermion"]: row for row in running_proxy["rows"]}

    row_specs = [
        ("H_to_bb", "b", source_by_quark["b"]),
        ("H_to_cc", "c", source_by_quark["c"]),
        ("H_to_ss", "s", ss_source),
    ]
    rows = {}
    for channel, quark, source in row_specs:
        ref_mass, ref_mass_sigma = gev_mass(masses[quark])
        rows[channel] = qcd_row(
            channel,
            quark,
            source,
            mh,
            mh_sigma,
            gf,
            gf_sigma,
            ref_mass,
            ref_mass_sigma,
            alpha_s_mh,
            alpha_s_mz_sigma,
        )

    row_basis = [channel for channel, _, _ in row_specs]
    covariance = [[0.0 for _ in row_basis] for _ in row_basis]
    for i, left in enumerate(row_basis):
        left_row = rows[left]
        for j, right in enumerate(row_basis):
            right_row = rows[right]
            shared = (
                left_row["analytic_derivatives"]["dGamma_dG_F"]
                * right_row["analytic_derivatives"]["dGamma_dG_F"]
                * gf_sigma**2
                + left_row["analytic_derivatives"]["dGamma_dM_H_fixed_running_mass"]
                * right_row["analytic_derivatives"]["dGamma_dM_H_fixed_running_mass"]
                * mh_sigma**2
                + left_row["analytic_derivatives"]["effective_dGamma_dalpha_s_MZ_via_K_slot"]
                * right_row["analytic_derivatives"]["effective_dGamma_dalpha_s_MZ_via_K_slot"]
                * alpha_s_mz_sigma**2
            )
            covariance[i][j] = shared
        covariance[i][i] = rows[left]["propagated_sigma_GeV"] ** 2

    qcd_rows = {
        "schema": "MTTHiggsQCDRouteAFermionicDerivativeRows.v1",
        "status": "ROUTE_A_QCD_FERMIONIC_DERIVATIVE_ROWS_EXECUTED_PROXY_PRECISION_OPEN",
        "row_basis": row_basis,
        "rows": rows,
        "qcd_fermionic_covariance_GeV2": covariance,
        "rows_executed": len(row_basis),
        "shared_covariance_sources": ["G_F", "M_H", "effective alpha_s_MZ through K_QCD slot"],
        "independent_covariance_sources": ["running quark mass uncertainty inherited from reference mass"],
        "accepted_as_route_A_qcd_fermionic_derivative_block": True,
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
            "route_A_qcd_proxy_width_GeV": formula_width,
            "imported_profile_central_width_GeV": imported_width,
            "delta_GeV": delta,
            "relative_delta_vs_imported": delta / imported_width,
            "used_for_source_selection": False,
            "interpretation": (
                "Diagnostic comparison only. The route-A row uses the repo QCD proxy carrier; the imported profile "
                "contains precision convention and higher-order content."
            ),
        }

    comparison = {
        "schema": "MTTHiggsQCDRowsImportedProfileComparison.v1",
        "status": "QCD_ROUTE_A_PROXY_ROWS_COMPARED_TO_IMPORTED_PROFILE_DIAGNOSTIC_ONLY",
        "comparison_rows": comparison_rows,
        "max_abs_relative_delta_vs_imported": max(abs(row["relative_delta_vs_imported"]) for row in comparison_rows.values()),
        "comparison_used_as_selector": False,
        "precision_promotion_from_comparison": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    precision_decision = {
        "schema": "MTTHiggsQCDRouteAPrecisionDecision.v1",
        "status": "QCD_FERMIONIC_DERIVATIVE_BLOCK_EXECUTED_PRECISION_REJECTED",
        "route_A_qcd_fermionic_rows_executed": row_basis,
        "route_A_rows_closed_total_including_leptonic": 5,
        "rows_remaining_for_route_A_ten_row_engine": [
            "H_to_gg",
            "H_to_gamma_gamma",
            "H_to_Z_gamma",
            "H_to_WW_star",
            "H_to_ZZ_star",
        ],
        "precision_total_width_closed": False,
        "precision_branching_ratios_closed": False,
        "precision_rejection_reasons": [
            "QCD rows use proxy running/massless coefficient carriers, not full HDECAY-style multiloop threshold formulas.",
            "alpha_s derivative is currently an effective K-slot sensitivity, not a full threshold/matching derivative.",
            "finite-mass, electroweak/mixed corrections, full covariance, and selected Qa/SU3 operator data remain open.",
        ],
        "next_route_A_block": "loop-induced H_to_gg derivative row, then electroweak gamma gamma/Z gamma and off-shell WW/ZZ rows",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    updated_true = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterQCDRouteARows.v1",
        "status": "ROUTE_A_QCD_FERMIONIC_DERIVATIVES_BUILT_TRUE_EQUIVALENCE_STILL_OPEN",
        "previous_gate": rel(
            DATA
            / "selected_higgsrouteaderivativeengineexecution_or_precisiondecision"
            / "updated_true_equivalence_gate_after_route_a_leptonic_execution.packet.json"
        ),
        "closed_now": previous_true["closed_now"] + [
            "Route-A QCD fermionic derivative rows for H_to_bb, H_to_cc, and H_to_ss",
            "Effective QCD K-slot uncertainty propagation for fermionic rows",
            "Diagnostic imported-profile comparison for QCD fermionic rows",
        ],
        "remaining_true_equivalence_blockers": previous_true["remaining_true_equivalence_blockers"],
        "next_primary_value_gate": "route-A loop/off-shell derivative rows for gg, gamma gamma, Z gamma, WW*, ZZ*",
        "guardrails": {
            "route_A_qcd_fermionic_rows_executed": True,
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
        "candidate": "MTTSelectedHiggsQCDRouteADerivativeRowsOrPrecisionDecision",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgsrouteaderivativeengineexecution_or_precisiondecision.candidate.json"),
            "reference_values": rel(DATA / "sm_equivalence_reference_data_values_fill.candidate.json"),
            "running_mass_proxy": rel(
                DATA
                / "selected_runningmasshiggsdecayproxy_or_precisionwidths"
                / "one_loop_running_mass_higgs_decay_proxy.packet.json"
            ),
            "ss_kernel": rel(
                DATA
                / "selected_higgssskernelrow_or_remainingchannels"
                / "higgs_ss_running_mass_kernel_row.packet.json"
            ),
            "imported_profile": rel(
                DATA
                / "selected_higgsrouteaformuladerivativeengines_or_officiallikelihoodimport"
                / "repo_basis_decay_covariance_import.packet.json"
            ),
        },
        "output_packets": {
            "route_a_qcd_fermionic_derivative_rows": rel(QCD_ROWS),
            "qcd_rows_imported_profile_comparison": rel(COMPARISON),
            "qcd_route_a_precision_decision": rel(PRECISION_DECISION),
            "updated_true_equivalence_gate": rel(UPDATED_TRUE),
        },
        "theorem": {
            "name": "HiggsQCDRouteAFermionicDerivativeRowsTheorem",
            "proved": True,
            "statement": (
                "The route-A QCD fermionic proxy carriers for H_to_bb, H_to_cc, and H_to_ss have explicit derivative "
                "rows with respect to G_F, M_H, running quark mass, and a QCD K-factor slot. This closes the QCD "
                "fermionic derivative block at proxy tier, while full multiloop threshold precision, loop/off-shell rows, "
                "true SM-equivalence, and no-knob closure remain open."
            ),
        },
        "what_closes_now": {
            "route_A_H_to_bb_qcd_derivative_row": True,
            "route_A_H_to_cc_qcd_derivative_row": True,
            "route_A_H_to_ss_qcd_derivative_row": True,
            "qcd_fermionic_route_A_uncertainty_propagation": True,
            "diagnostic_imported_profile_comparison": True,
        },
        "what_remains_open": {
            "full_multiloop_QCD_threshold_derivatives": True,
            "loop_rows_gg_gamma_gamma_Z_gamma": True,
            "off_shell_rows_WW_ZZ": True,
            "precision_total_width": True,
            "precision_branching_ratios": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "route_A_qcd_fermionic_derivative_block_closed": True,
            "route_A_rows_closed_total_including_leptonic": 5,
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
        "next_required_artifact": "MTT_Selected_HiggsLoopOffshellRouteADerivativeRows_or_PrecisionDecision_v1",
    }

    cert = {
        "certificate": "MTT_Selected_HiggsQCDRouteADerivativeRows_or_PrecisionDecision_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "route_A_qcd_fermionic_derivative_block_closed": True,
        "route_A_rows_closed_total_including_leptonic": 5,
        "full_route_A_ten_row_engine_closed": False,
        "precision_total_width_closed": False,
        "precision_branching_ratios_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }

    note = f"""# MTT Selected HiggsQCDRouteADerivativeRows or PrecisionDecision v1

Status: `{STATUS}`.

This artifact executes the route-A QCD fermionic derivative block for
`H_to_bb`, `H_to_cc`, and `H_to_ss`.

The row formula is the repo's running-mass QCD proxy carrier:

`Gamma(H->qq)=3 G_F M_H m_q(M_H)^2 K_QCD/(4 pi sqrt(2))`.

For each row it records derivatives with respect to `G_F`, `M_H`, the running
quark mass, and a QCD `K_QCD` slot. The alpha_s derivative is currently only an
effective K-slot sensitivity, so this is not promoted to full multiloop
precision.

This closes the QCD fermionic derivative block at proxy tier only. Loop rows,
off-shell rows, full threshold derivatives, precision Higgs closure, true SM
equivalence, and no-knob closure remain open.
"""

    for path, payload in [
        (QCD_ROWS, qcd_rows),
        (COMPARISON, comparison),
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
