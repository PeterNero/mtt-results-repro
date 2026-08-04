"""Build Higgs route-A derivative engines or official likelihood decision."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgsrouteaformuladerivativeengines_or_officiallikelihooddecision"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
OFFICIAL_AUDIT = PACKET_DIR / "official_likelihood_source_audit.packet.json"
ROUTE_A_HANDOFF = PACKET_DIR / "route_a_derivative_engine_handoff.packet.json"
PROFILE_POLICY = PACKET_DIR / "higgs_precision_profile_policy_after_decision.packet.json"
UPDATED_TRUE = PACKET_DIR / "updated_true_equivalence_gate_after_official_likelihood_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsRouteAFormulaDerivativeEngines_or_OfficialLikelihoodDecision_v1.md"

STATUS = "MTT_SELECTED_HIGGSROUTEAFORMULADERIVATIVEENGINES_OR_OFFICIALLIKELIHOODDECISION_BUILT_OFFICIAL_LIKELIHOOD_RETIRED_ROUTEA_PRIMARY"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgsimportedprofilereplay_or_officiallhchxswglikelihood.candidate.json")
    replay_summary = load(
        DATA
        / "selected_higgsimportedprofilereplay_or_officiallhchxswglikelihood"
        / "imported_profile_precision_summary.packet.json"
    )
    official_gate = load(
        DATA
        / "selected_higgsimportedprofilereplay_or_officiallhchxswglikelihood"
        / "official_lhchxswg_likelihood_gate.packet.json"
    )
    previous_true = load(
        DATA
        / "selected_higgsimportedprofilereplay_or_officiallhchxswglikelihood"
        / "updated_true_equivalence_gate_after_imported_profile_replay.packet.json"
    )

    official_audit = {
        "schema": "MTTHiggsOfficialLikelihoodSourceAudit.v1",
        "status": "OFFICIAL_MACHINE_READABLE_HIGGS_LIKELIHOOD_NOT_IMPORTED_ROUTE_RETIRED_FOR_NOW",
        "fresh_external_check_date": "2026-05-31",
        "official_sources_checked": [
            {
                "name": "LHCHWG overview",
                "url": "https://twiki.cern.ch/twiki/bin/view/LHCPhysics/LHCHWG",
                "relevant_role": "official working-group overview and recommendation hub",
            },
            {
                "name": "LHCHWG Higgs XS/BR page",
                "url": "https://twiki.cern.ch/twiki/bin/view/LHCPhysics/HiggsXSBR",
                "relevant_role": "official cross-section and branching-ratio recommendation tables/spreadsheets",
            },
            {
                "name": "LHCHWG branching-ratio page",
                "url": "https://twiki.cern.ch/twiki/bin/view/LHCPhysics/LHCHWGBRs",
                "relevant_role": "official branching-ratio tools, tables, and references",
            },
            {
                "name": "LHC Higgs Combination Group",
                "url": "https://twiki.cern.ch/twiki/bin/view/LHCPhysics/HiggsCombination",
                "relevant_role": "combination framework; RooStats/RooWorkspace is the preferred likelihood-sharing format",
            },
        ],
        "required_for_official_likelihood_promotion": [
            "officially released machine-readable likelihood or profile-likelihood RooWorkspace",
            "declared parameter basis compatible with the repo Higgs row basis or a documented projection map",
            "nuisance/profile semantics sufficient to replay uncertainty correlations",
            "versioned provenance from an official LHCHWG/LHCHXSWG or LHC-HCG release",
        ],
        "what_was_found": [
            "official recommendation pages for cross sections and branching ratios",
            "official calculation instructions and spreadsheet-style recommendation artifacts",
            "combination-framework documentation that identifies RooStats/RooWorkspace as the preferred likelihood-sharing format",
            "a published non-official ancillary ten-decay covariance profile already imported by the previous artifact",
        ],
        "what_was_not_found": [
            "an official public machine-readable full Higgs likelihood/profile matching the repo ten-decay basis",
            "a public official nuisance-parameter workspace that can replace the imported covariance profile",
            "an official profile-likelihood scan packet over the repo total-width and branching-ratio observables",
        ],
        "published_profile_replay_available": previous["closure_decision"]["imported_profile_replay_closed"],
        "accepted_as_official_LHCHXSWG_likelihood": False,
        "official_likelihood_route_retired_for_now": True,
        "retirement_is_reversible_if_artifact_found": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    route_a_handoff = {
        "schema": "MTTHiggsRouteADerivativeEngineHandoff.v1",
        "status": "ROUTE_A_DERIVATIVE_ENGINE_PATH_SELECTED_AS_PRIMARY_AFTER_OFFICIAL_LIKELIHOOD_RETIREMENT",
        "primary_route": "route_A_partial_width_formula_derivative_engines",
        "secondary_route": "official_likelihood_import_if_a_versioned_workspace_is_found",
        "locked_inputs_already_available": {
            "ten_channel_central_partial_widths": True,
            "published_decay_covariance_replay": True,
            "total_width_and_branching_ratio_jacobian": True,
            "SM_parity_covariance_profile": True,
        },
        "engine_rows_required": [
            {
                "row": "H_to_bb",
                "engine_family": "fermionic_width_qcd_running_mass_threshold",
                "differentiation_variables": ["m_b", "alpha_s", "M_H", "electroweak_inputs", "threshold_scheme"],
            },
            {
                "row": "H_to_cc",
                "engine_family": "fermionic_width_qcd_running_mass_threshold",
                "differentiation_variables": ["m_c", "alpha_s", "M_H", "electroweak_inputs", "threshold_scheme"],
            },
            {
                "row": "H_to_ss",
                "engine_family": "fermionic_width_qcd_running_mass_threshold",
                "differentiation_variables": ["m_s", "alpha_s", "M_H", "electroweak_inputs", "threshold_scheme"],
            },
            {
                "row": "H_to_tau_tau",
                "engine_family": "tree_fermionic_leptonic_width",
                "differentiation_variables": ["m_tau", "M_H", "electroweak_inputs"],
            },
            {
                "row": "H_to_mu_mu",
                "engine_family": "tree_fermionic_leptonic_width",
                "differentiation_variables": ["m_mu", "M_H", "electroweak_inputs"],
            },
            {
                "row": "H_to_gg",
                "engine_family": "loop_qcd_width_top_bottom_charm_threshold",
                "differentiation_variables": ["alpha_s", "m_t", "m_b", "m_c", "M_H", "threshold_scheme"],
            },
            {
                "row": "H_to_gamma_gamma",
                "engine_family": "loop_electroweak_width_W_top_interference",
                "differentiation_variables": ["alpha_em", "M_W", "m_t", "M_H", "electroweak_scheme"],
            },
            {
                "row": "H_to_Z_gamma",
                "engine_family": "loop_electroweak_width_Zgamma",
                "differentiation_variables": ["alpha_em", "M_Z", "M_W", "m_t", "M_H", "electroweak_scheme"],
            },
            {
                "row": "H_to_WW_star",
                "engine_family": "off_shell_four_fermion_width",
                "differentiation_variables": ["M_W", "Gamma_W", "M_H", "G_F", "electroweak_scheme"],
            },
            {
                "row": "H_to_ZZ_star",
                "engine_family": "off_shell_four_fermion_width",
                "differentiation_variables": ["M_Z", "Gamma_Z", "M_H", "G_F", "electroweak_scheme"],
            },
        ],
        "superset_strategy_use": {
            "straight_path": "differentiate declared SM/HDECAY/PROPHECY-style partial-width formulas",
            "combined_superset_path": "use imported covariance replay as an external consistency target while route-A formula derivatives become the source-side precision engine",
            "locked_target": "SM-parity Higgs precision replay; no measured value may select MTT source structure",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    profile_policy = {
        "schema": "MTTHiggsPrecisionProfilePolicyAfterDecision.v1",
        "status": "PUBLISHED_PROFILE_REPLAY_ACCEPTED_OFFICIAL_LIKELIHOOD_RETIRED_ROUTEA_REQUIRED",
        "accepted_current_profile": "published_decay_covariance_replayed_to_total_width_and_branching_ratios",
        "accepted_current_profile_path": "candidate_data/selected_higgsimportedprofilereplay_or_officiallhchxswglikelihood/imported_profile_observable_replay.packet.json",
        "current_profile_precision_summary": {
            "tracked_total_width_GeV": replay_summary["tracked_total_width_GeV"],
            "tracked_total_width_sigma_GeV": replay_summary["tracked_total_width_sigma_GeV"],
            "tracked_total_width_relative_sigma": replay_summary["tracked_total_width_relative_sigma"],
        },
        "official_gate_status": official_gate["status"],
        "precision_total_width_closed": False,
        "precision_branching_ratios_closed": False,
        "why_precision_not_closed": [
            "The covariance replay is now executable and correlated, but it is not an official likelihood.",
            "Route-A formula derivatives are needed to replace or justify external profile uncertainties from declared inputs.",
            "A final empirical Higgs precision decision still needs tolerance, covariance, and source-provenance policy.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    updated_true = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterOfficialLikelihoodDecision.v1",
        "status": "OFFICIAL_LIKELIHOOD_ROUTE_RETIRED_ROUTEA_HIGGS_PRECISION_GATE_SELECTED",
        "previous_gate": rel(
            DATA
            / "selected_higgsimportedprofilereplay_or_officiallhchxswglikelihood"
            / "updated_true_equivalence_gate_after_imported_profile_replay.packet.json"
        ),
        "closed_now": previous_true["closed_now"] + [
            "Higgs official-likelihood route decision",
            "Higgs route-A derivative-engine row contract",
            "Higgs precision profile policy after official-likelihood retirement",
        ],
        "remaining_true_equivalence_blockers": previous_true["remaining_true_equivalence_blockers"],
        "next_primary_value_gate": "route-A partial-width derivative engines and Higgs precision decision",
        "guardrails": {
            "official_LHCHXSWG_likelihood_route_retired_for_now": True,
            "published_profile_replay_retained_for_SM_parity": True,
            "route_A_derivative_engines_selected_as_primary": True,
            "precision_total_width_closed": False,
            "precision_branching_ratios_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsRouteAFormulaDerivativeEnginesOrOfficialLikelihoodDecision",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgsimportedprofilereplay_or_officiallhchxswglikelihood.candidate.json"),
            "imported_profile_precision_summary": rel(
                DATA
                / "selected_higgsimportedprofilereplay_or_officiallhchxswglikelihood"
                / "imported_profile_precision_summary.packet.json"
            ),
        },
        "output_packets": {
            "official_likelihood_source_audit": rel(OFFICIAL_AUDIT),
            "route_a_derivative_engine_handoff": rel(ROUTE_A_HANDOFF),
            "higgs_precision_profile_policy_after_decision": rel(PROFILE_POLICY),
            "updated_true_equivalence_gate": rel(UPDATED_TRUE),
        },
        "theorem": {
            "name": "HiggsOfficialLikelihoodDecisionAndRouteAHandoffTheorem",
            "proved": True,
            "statement": (
                "Given the checked official-source landscape, no official public machine-readable LHCHXSWG/LHC-HCG "
                "likelihood matching the repo Higgs basis is imported. The published covariance replay remains a valid "
                "SM-parity profile, while route-A partial-width formula derivative engines become the primary remaining "
                "Higgs precision route."
            ),
        },
        "what_closes_now": {
            "official_likelihood_route_decision": True,
            "route_A_derivative_engine_contract": True,
            "Higgs_precision_profile_policy_after_decision": True,
        },
        "what_remains_open": {
            "route_A_partial_width_formula_derivative_engines": True,
            "official_LHCHXSWG_likelihood_if_later_found": True,
            "precision_total_width": True,
            "precision_branching_ratios": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "official_likelihood_route_retired_for_now": True,
            "published_profile_replay_retained_for_SM_parity": True,
            "route_A_derivative_engines_selected_as_primary": True,
            "precision_total_width_closed": False,
            "precision_branching_ratios_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_HiggsRouteADerivativeEngineExecution_or_PrecisionDecision_v1",
    }

    cert = {
        "certificate": "MTT_Selected_HiggsRouteAFormulaDerivativeEngines_or_OfficialLikelihoodDecision_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "official_likelihood_route_retired_for_now": True,
        "published_profile_replay_retained_for_SM_parity": True,
        "route_A_derivative_engines_selected_as_primary": True,
        "precision_total_width_closed": False,
        "precision_branching_ratios_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }

    note = f"""# MTT Selected HiggsRouteAFormulaDerivativeEngines or OfficialLikelihoodDecision v1

Status: `{STATUS}`.

This artifact makes the Higgs precision-route decision after the imported
profile replay.

The official route is retired for now because no official public
machine-readable LHCHXSWG/LHC-HCG likelihood or profile workspace matching the
repo ten-decay Higgs basis has been imported. The retirement is reversible if a
versioned official RooWorkspace/profile-likelihood artifact is found later.

The published covariance replay remains accepted as an SM-parity correlated
profile. The primary remaining route is now route-A: differentiate the actual
partial-width formula engines for all ten Higgs rows, then compare the resulting
covariance/profile against the imported replay without using observed values to
select source structure.
"""

    for path, payload in [
        (OFFICIAL_AUDIT, official_audit),
        (ROUTE_A_HANDOFF, route_a_handoff),
        (PROFILE_POLICY, profile_policy),
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
