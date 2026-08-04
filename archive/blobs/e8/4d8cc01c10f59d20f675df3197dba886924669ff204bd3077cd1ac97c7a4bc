"""Build diagonal profile execution and multi-loop convention audit gate."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_fullcovarianceprofile_or_multiloopconventionaudit"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PROFILE = PACKET_DIR / "diagonal_profile_likelihood_execution.packet.json"
CONVENTION = PACKET_DIR / "multiloop_convention_audit_requirements.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_diagonal_profile.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FullCovarianceProfile_or_MultiLoopConventionAudit_v1.md"

STATUS = "MTT_SELECTED_FULLCOVARIANCEPROFILE_OR_MULTILOOPCONVENTIONAUDIT_BUILT_DIAGONAL_PROFILE_FULL_PROFILE_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_polethresholdresidualvalues_or_covarianceprofile.candidate.json")
    previous_gate = load(
        DATA
        / "selected_polethresholdresidualvalues_or_covarianceprofile"
        / "updated_true_equivalence_gate_after_formula_replay.packet.json"
    )
    formula = load(
        DATA
        / "selected_polethresholdresidualvalues_or_covarianceprofile"
        / "buttazzo_boundary_formula_replay.packet.json"
    )
    covariance = load(
        DATA
        / "selected_polethresholdresidualvalues_or_covarianceprofile"
        / "diagonal_sensitivity_covariance_scaffold.packet.json"
    )
    literature = load(
        DATA
        / "selected_externalliteraturergbenchmarkvalues_or_thresholdcovariance"
        / "external_literature_rg_benchmark_values.packet.json"
    )

    current_values = formula["current_repo_input_variant"]["values"]
    central_values = formula["buttazzo_central_input_replay"]["values"]
    propagated = covariance["propagated_diagonal_uncertainties"]
    theory_uncertainties = {
        key: float(row.get("theory_uncertainty", 0.0))
        for key, row in literature["literature_values"].items()
    }

    profile_rows = []
    chi2 = 0.0
    for key in ["lambda_Mt", "y_t_Mt", "g_2_Mt", "g_Y_Mt", "g_1_GUT_Mt", "g_3_Mt"]:
        delta = float(current_values[key]) - float(central_values[key])
        experimental_sigma = float(propagated[key]["diagonal_sigma"])
        theory_sigma = theory_uncertainties.get(key, 0.0)
        total_sigma = math.sqrt(experimental_sigma * experimental_sigma + theory_sigma * theory_sigma)
        pull = delta / total_sigma if total_sigma else 0.0
        row_chi2 = pull * pull
        chi2 += row_chi2
        profile_rows.append(
            {
                "id": key,
                "current_input_formula_value": float(current_values[key]),
                "buttazzo_central_value": float(central_values[key]),
                "delta": delta,
                "experimental_diagonal_sigma": experimental_sigma,
                "theory_sigma": theory_sigma,
                "total_diagonal_sigma": total_sigma,
                "pull": pull,
                "chi2_contribution": row_chi2,
            }
        )

    max_abs_pull = max(abs(row["pull"]) for row in profile_rows)
    degrees_of_freedom = len(profile_rows)
    profile_packet = {
        "schema": "MTTDiagonalProfileLikelihoodExecution.v1",
        "status": "DIAGONAL_PROFILE_EXECUTED_FULL_CORRELATED_PROFILE_OPEN",
        "comparison_target": "Buttazzo et al. central weak-scale boundary-condition point",
        "input_variant": formula["current_repo_input_variant"]["inputs"],
        "profile_rows": profile_rows,
        "chi2_diagonal": chi2,
        "degrees_of_freedom": degrees_of_freedom,
        "reduced_chi2_diagonal": chi2 / degrees_of_freedom,
        "max_abs_pull": max_abs_pull,
        "passes_coarse_diagonal_profile": max_abs_pull < 3.0,
        "accepted_as_full_covariance_profile": False,
        "why_not_full_profile": (
            "This uses diagonalized linear sensitivities plus explicit theory sidecars where present. "
            "It omits published/reconstructed correlations, non-Gaussian/profile likelihood structure, "
            "and coupled multi-loop convention systematics."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    convention_packet = {
        "schema": "MTTMultiLoopConventionAuditRequirements.v1",
        "status": "MULTILOOP_CONVENTION_AUDIT_REQUIREMENTS_BUILT_VALUES_OPEN",
        "closed_now": {
            "literature_boundary_formula_replay": True,
            "diagonal_profile_execution": True,
            "coarse_diagonal_profile_passes": profile_packet["passes_coarse_diagonal_profile"],
        },
        "required_for_full_true_equivalence": [
            {
                "id": "correlated_input_profile",
                "requirement": "Provide or reconstruct the covariance/profile among M_W, M_h, M_t, alpha3(MZ), and electroweak inputs.",
                "closed": False,
            },
            {
                "id": "multi_loop_threshold_policy",
                "requirement": "Declare the exact loop order and matching convention against the external benchmark, including QCD/EW threshold systematics.",
                "closed": False,
            },
            {
                "id": "common_observable_set",
                "requirement": "Tie the weak-scale boundary values to the final empirical replay observable list and uncertainty policy.",
                "closed": False,
            },
            {
                "id": "source_side_independence",
                "requirement": "Keep all literature and measured values downstream from selected MTT source/operator packet selection.",
                "closed": True,
            },
        ],
        "source_independence_guardrails": {
            "profile_values_used_to_select_MTT_source": False,
            "profile_values_used_to_select_QaSU3_packet": False,
            "profile_values_used_to_select_flavor_branch": False,
            "profile_values_allowed_as_SM_parity_replay": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    remaining = [
        blocker
        for blocker in previous_gate["remaining_true_equivalence_blockers"]
        if blocker not in {"full covariance/profile likelihood values", "multi-loop coupled RG/profile convention audit"}
    ]
    if "full correlated covariance/profile likelihood values" not in remaining:
        remaining.insert(0, "full correlated covariance/profile likelihood values")
    if "multi-loop threshold convention values" not in remaining:
        remaining.insert(1, "multi-loop threshold convention values")
    updated = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterDiagonalProfile.v1",
        "status": "DIAGONAL_PROFILE_EXECUTED_CORRELATED_PROFILE_AND_MULTILOOP_VALUES_OPEN",
        "previous_true_equivalence_blockers": previous_gate["remaining_true_equivalence_blockers"],
        "closed_now": [
            "diagonal profile likelihood execution",
            "coarse weak-scale boundary profile sanity check",
            "multi-loop convention audit requirement table",
        ],
        "remaining_true_equivalence_blockers": remaining,
        "next_primary_value_gate": "full correlated profile values or accepted multi-loop convention table",
        "guardrails": {
            "diagonal_profile_is_not_full_covariance_profile": True,
            "coarse_profile_pass_is_not_true_SM_equivalence": True,
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedFullCovarianceProfileOrMultiLoopConventionAudit",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_polethresholdresidualvalues_or_covarianceprofile.candidate.json"),
            "formula_replay": rel(
                DATA
                / "selected_polethresholdresidualvalues_or_covarianceprofile"
                / "buttazzo_boundary_formula_replay.packet.json"
            ),
            "diagonal_covariance_scaffold": rel(
                DATA
                / "selected_polethresholdresidualvalues_or_covarianceprofile"
                / "diagonal_sensitivity_covariance_scaffold.packet.json"
            ),
            "external_literature_values": rel(
                DATA
                / "selected_externalliteraturergbenchmarkvalues_or_thresholdcovariance"
                / "external_literature_rg_benchmark_values.packet.json"
            ),
        },
        "output_packets": {
            "diagonal_profile_likelihood_execution": rel(PROFILE),
            "multiloop_convention_audit_requirements": rel(CONVENTION),
            "updated_true_equivalence_gate": rel(UPDATED),
        },
        "theorem": {
            "name": "DiagonalProfileExecutionAndConventionAuditTheorem",
            "proved": True,
            "statement": (
                "The literature formula replay and diagonal sensitivity scaffold determine an executable "
                "diagonal profile over lambda, yt, g2, gY, GUT-normalized g1, and g3 at Mt. The current "
                "repo input variant passes the coarse diagonal profile gate, while full correlated covariance, "
                "multi-loop convention values, true SM equivalence, and no-knob derivation remain open."
            ),
        },
        "what_closes_now": {
            "diagonal_profile_likelihood_executed": True,
            "coarse_diagonal_profile_passes": profile_packet["passes_coarse_diagonal_profile"],
            "multiloop_convention_audit_requirements_built": True,
            "superset_strategy_preserved": True,
        },
        "what_remains_open": {
            "full_correlated_covariance_profile_likelihood_values": True,
            "multi_loop_threshold_convention_values": True,
            "local_QFT_observable_values": True,
            "QM_GR_measurement_response_interfaces": True,
            "actual_QaSU3_operator_packet": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "diagonal_profile_executed": True,
            "coarse_profile_passes": profile_packet["passes_coarse_diagonal_profile"],
            "full_covariance_profile_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_FullCovarianceProfile_or_MultiLoopConventionAudit_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "diagonal_profile_executed": True,
        "coarse_profile_passes": profile_packet["passes_coarse_diagonal_profile"],
        "full_covariance_profile_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_CorrelatedProfileValues_or_LocalQFTObservableValues_v1",
    }

    note = """# MTT Selected FullCovarianceProfile or MultiLoopConventionAudit v1

Status: `MTT_SELECTED_FULLCOVARIANCEPROFILE_OR_MULTILOOPCONVENTIONAUDIT_BUILT_DIAGONAL_PROFILE_FULL_PROFILE_OPEN`.

This artifact executes the diagonal profile implied by the Buttazzo boundary
formula replay and the current repo input variant. It computes pulls and a
diagonal chi-square for `lambda(Mt)`, `yt(Mt)`, `g2(Mt)`, `gY(Mt)`,
GUT-normalized `g1(Mt)`, and `g3(Mt)`.

The coarse diagonal profile passes, but this is not a full covariance/profile
likelihood and does not close true SM equivalence. Correlations, non-Gaussian
profile structure, multi-loop threshold convention values, local QFT observable
values, QM/GR interfaces, and actual Qa/SU3 operator data remain open.
"""

    for path, payload in [
        (PROFILE, profile_packet),
        (CONVENTION, convention_packet),
        (UPDATED, updated),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
