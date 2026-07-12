"""Build Higgs imported-profile replay or official LHCHXSWG likelihood gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgsimportedprofilereplay_or_officiallhchxswglikelihood"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
OBS_REPLAY = PACKET_DIR / "imported_profile_observable_replay.packet.json"
PRECISION_SUMMARY = PACKET_DIR / "imported_profile_precision_summary.packet.json"
OFFICIAL_GATE = PACKET_DIR / "official_lhchxswg_likelihood_gate.packet.json"
UPDATED_TRUE = PACKET_DIR / "updated_true_equivalence_gate_after_imported_profile_replay.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsImportedProfileReplay_or_OfficialLHCHXSWGLikelihood_v1.md"

STATUS = "MTT_SELECTED_HIGGSIMPORTEDPROFILEREPLAY_OR_OFFICIALLHCHXSWGLIKELIHOOD_BUILT_IMPORTED_PROFILE_REPLAY_OFFICIAL_LIKELIHOOD_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [
        [sum(a_ik * b[k][j] for k, a_ik in enumerate(a_row)) for j in range(len(b[0]))]
        for a_row in a
    ]


def transpose(a: list[list[float]]) -> list[list[float]]:
    return [list(col) for col in zip(*a)]


def correlation(cov: list[list[float]]) -> list[list[float]]:
    sigmas = [max(row[i], 0.0) ** 0.5 for i, row in enumerate(cov)]
    corr: list[list[float]] = []
    for i, row in enumerate(cov):
        corr_row = []
        for j, value in enumerate(row):
            denom = sigmas[i] * sigmas[j]
            corr_row.append(value / denom if denom else 0.0)
        corr.append(corr_row)
    return corr


def max_asymmetry(matrix: list[list[float]]) -> float:
    return max(
        abs(matrix[i][j] - matrix[j][i])
        for i in range(len(matrix))
        for j in range(len(matrix))
    )


def dominant_offdiagonal_pairs(
    basis: list[str], corr: list[list[float]], limit: int = 12
) -> list[dict[str, float | str]]:
    pairs = []
    for i, left in enumerate(basis):
        for j, right in enumerate(basis):
            if j <= i:
                continue
            pairs.append(
                {
                    "left": left,
                    "right": right,
                    "correlation": corr[i][j],
                    "abs_correlation": abs(corr[i][j]),
                }
            )
    pairs.sort(key=lambda item: float(item["abs_correlation"]), reverse=True)
    return pairs[:limit]


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgsrouteaformuladerivativeengines_or_officiallikelihoodimport.candidate.json")
    imported = load(
        DATA
        / "selected_higgsrouteaformuladerivativeengines_or_officiallikelihoodimport"
        / "repo_basis_decay_covariance_import.packet.json"
    )
    jacobian = load(
        DATA
        / "selected_higgsofficialprofile_or_routeaformuladifferentiation"
        / "total_width_and_branching_ratio_replay_jacobian.packet.json"
    )
    previous_gate = load(
        DATA
        / "selected_higgsrouteaformuladerivativeengines_or_officiallikelihoodimport"
        / "updated_true_equivalence_gate_after_higgs_profile_import.packet.json"
    )

    row_basis = imported["repo_row_basis"]
    if row_basis != jacobian["input_width_basis"]:
        raise ValueError("imported covariance basis and replay Jacobian basis differ")

    observable_basis = jacobian["output_observable_basis"]
    jacobian_matrix = [jacobian["jacobian_rows"][row] for row in observable_basis]
    width_cov = imported["covariance_matrix_GeV2"]
    observable_cov = matmul(matmul(jacobian_matrix, width_cov), transpose(jacobian_matrix))
    observable_corr = correlation(observable_cov)
    sigmas = {
        observable_basis[i]: max(observable_cov[i][i], 0.0) ** 0.5
        for i in range(len(observable_basis))
    }
    central = {
        "Gamma_total_tracked": jacobian["tracked_total_width_GeV"],
        **{f"BR::{key}": value for key, value in jacobian["tracked_branching_ratios"].items()},
    }
    relative_sigmas = {
        key: (sigmas[key] / abs(value) if value else None)
        for key, value in central.items()
    }

    obs_replay = {
        "schema": "MTTHiggsImportedProfileObservableReplay.v1",
        "status": "IMPORTED_DECAY_PROFILE_PROPAGATED_THROUGH_REPLAY_MAP",
        "source_import": rel(
            DATA
            / "selected_higgsrouteaformuladerivativeengines_or_officiallikelihoodimport"
            / "repo_basis_decay_covariance_import.packet.json"
        ),
        "replay_jacobian": rel(
            DATA
            / "selected_higgsofficialprofile_or_routeaformuladifferentiation"
            / "total_width_and_branching_ratio_replay_jacobian.packet.json"
        ),
        "input_partial_width_basis": row_basis,
        "observable_basis": observable_basis,
        "central_observables": central,
        "observable_covariance": observable_cov,
        "observable_correlation": observable_corr,
        "observable_sigmas": sigmas,
        "observable_relative_sigmas": relative_sigmas,
        "max_covariance_asymmetry": max_asymmetry(observable_cov),
        "covariance_propagation_rule": "Cov[Gamma_total, BR] = J Cov[partial_widths] J^T",
        "accepted_as_imported_profile_replay": True,
        "accepted_as_official_LHCHXSWG_likelihood": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    precision_summary = {
        "schema": "MTTHiggsImportedProfilePrecisionSummary.v1",
        "status": "IMPORTED_PROFILE_PRECISION_SUMMARY_BUILT",
        "tracked_total_width_GeV": central["Gamma_total_tracked"],
        "tracked_total_width_sigma_GeV": sigmas["Gamma_total_tracked"],
        "tracked_total_width_relative_sigma": relative_sigmas["Gamma_total_tracked"],
        "branching_ratio_sigmas": {
            key.removeprefix("BR::"): value
            for key, value in sigmas.items()
            if key.startswith("BR::")
        },
        "branching_ratio_relative_sigmas": {
            key.removeprefix("BR::"): value
            for key, value in relative_sigmas.items()
            if key.startswith("BR::")
        },
        "dominant_observable_correlations": dominant_offdiagonal_pairs(observable_basis, observable_corr),
        "precision_profile_usable_for_SM_parity_replay": True,
        "precision_profile_sufficient_for_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    official_gate = {
        "schema": "MTTOfficialLHCHXSWGLikelihoodGate.v1",
        "status": "OFFICIAL_LHCHXSWG_FULL_LIKELIHOOD_STILL_NOT_IMPORTED",
        "published_decay_covariance_profile_imported": True,
        "official_machine_readable_likelihood_imported": False,
        "nuisance_profile_semantics_imported": False,
        "profile_likelihood_scan_imported": False,
        "accepted_as_SM_parity_decay_covariance_replay": True,
        "accepted_as_official_LHCHXSWG_likelihood": False,
        "why_not_official_likelihood": [
            "The imported source is a published ancillary covariance/correlation profile, not an official LHCHXSWG likelihood release.",
            "It supplies covariance information for decay/profile replay, but not full nuisance-parameter profiling semantics.",
            "It therefore closes an SM-parity covariance replay gate, not the official-likelihood gate.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    updated_true = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterImportedProfileReplay.v1",
        "status": "IMPORTED_HIGGS_PROFILE_REPLAY_BUILT_TRUE_EQUIVALENCE_STILL_OPEN",
        "previous_gate": rel(
            DATA
            / "selected_higgsrouteaformuladerivativeengines_or_officiallikelihoodimport"
            / "updated_true_equivalence_gate_after_higgs_profile_import.packet.json"
        ),
        "closed_now": previous_gate["closed_now"] + [
            "Higgs imported decay covariance propagated through total-width/branching replay Jacobian",
            "Higgs imported-profile observable covariance/correlation packet",
            "Higgs official-likelihood gate separated from SM-parity covariance replay",
        ],
        "remaining_true_equivalence_blockers": previous_gate["remaining_true_equivalence_blockers"],
        "next_primary_value_gate": "official LHCHXSWG likelihood or route-A partial-width derivative engines",
        "guardrails": {
            "imported_profile_replay_built": True,
            "official_LHCHXSWG_likelihood_imported": False,
            "nuisance_profile_semantics_imported": False,
            "route_A_physics_formula_differentiation_closed": False,
            "precision_total_width_closed": False,
            "precision_branching_ratios_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsImportedProfileReplayOrOfficialLHCHXSWGLikelihood",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgsrouteaformuladerivativeengines_or_officiallikelihoodimport.candidate.json"),
            "published_decay_covariance_import": rel(
                DATA
                / "selected_higgsrouteaformuladerivativeengines_or_officiallikelihoodimport"
                / "repo_basis_decay_covariance_import.packet.json"
            ),
            "replay_jacobian": rel(
                DATA
                / "selected_higgsofficialprofile_or_routeaformuladifferentiation"
                / "total_width_and_branching_ratio_replay_jacobian.packet.json"
            ),
        },
        "output_packets": {
            "imported_profile_observable_replay": rel(OBS_REPLAY),
            "imported_profile_precision_summary": rel(PRECISION_SUMMARY),
            "official_lhchxswg_likelihood_gate": rel(OFFICIAL_GATE),
            "updated_true_equivalence_gate": rel(UPDATED_TRUE),
        },
        "theorem": {
            "name": "HiggsImportedProfileReplayTheorem",
            "proved": True,
            "statement": (
                "Given the imported published ten-channel decay covariance and the already built replay Jacobian, "
                "the observable covariance over total width and branching ratios is fixed by J Cov J^T. This closes "
                "the imported-profile SM-parity replay gate while leaving the official LHCHXSWG likelihood and "
                "route-A formula-derivative gates open."
            ),
        },
        "what_closes_now": {
            "imported_decay_covariance_replayed_to_total_width_and_branching_ratios": True,
            "observable_covariance_and_correlation_packet_built": True,
            "official_likelihood_claim_separated_from_published_profile_replay": True,
        },
        "what_remains_open": {
            "official_LHCHXSWG_likelihood_import": True,
            "nuisance_profile_semantics": True,
            "route_A_partial_width_formula_derivative_engines": True,
            "precision_total_width": True,
            "precision_branching_ratios": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "imported_profile_replay_closed": True,
            "accepted_as_SM_parity_covariance_replay": True,
            "accepted_as_official_LHCHXSWG_likelihood": False,
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
        "certificate": "MTT_Selected_HiggsImportedProfileReplay_or_OfficialLHCHXSWGLikelihood_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "imported_profile_replay_closed": True,
        "accepted_as_SM_parity_covariance_replay": True,
        "accepted_as_official_LHCHXSWG_likelihood": False,
        "official_machine_readable_likelihood_imported": False,
        "route_A_physics_formula_differentiation_closed": False,
        "precision_total_width_closed": False,
        "precision_branching_ratios_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_HiggsRouteAFormulaDerivativeEngines_or_OfficialLikelihoodDecision_v1",
    }

    note = f"""# MTT Selected HiggsImportedProfileReplay or OfficialLHCHXSWGLikelihood v1

Status: `{STATUS}`.

This artifact propagates the imported published Higgs decay covariance profile
through the already built total-width and branching-ratio replay Jacobian.

The replay is a locked SM-parity covariance construction:

- input: published ten-channel decay covariance in the repo Higgs basis;
- map: `Gamma_total = sum_i Gamma_i`, `BR_i = Gamma_i / Gamma_total`;
- output: observable covariance/correlation over total width and ten branching
  ratios by `J Cov(Gamma) J^T`.

This closes the imported-profile replay gate. It does not import or claim an
official LHCHXSWG machine-readable likelihood, and it does not close no-knob or
route-A partial-width formula differentiation.
"""

    for path, payload in [
        (OBS_REPLAY, obs_replay),
        (PRECISION_SUMMARY, precision_summary),
        (OFFICIAL_GATE, official_gate),
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
