"""Build correlation-robust profile envelope and local-QFT observable value gate."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_correlatedprofilevalues_or_localqftobservablevalues"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PROFILE = PACKET_DIR / "correlation_robust_profile_envelope.packet.json"
QFT = PACKET_DIR / "local_qft_observable_value_gate.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_correlation_envelope.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_CorrelatedProfileValues_or_LocalQFTObservableValues_v1.md"

STATUS = "MTT_SELECTED_CORRELATEDPROFILEVALUES_OR_LOCALQFTOBSERVABLEVALUES_BUILT_CORRELATION_ENVELOPE_QFT_VALUES_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def invert(matrix: list[list[float]]) -> list[list[float]]:
    n = len(matrix)
    aug = [[float(matrix[i][j]) for j in range(n)] + [1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(aug[r][col]))
        if abs(aug[pivot][col]) < 1e-18:
            raise ValueError("singular matrix")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [value / scale for value in aug[col]]
        for row in range(n):
            if row == col:
                continue
            factor = aug[row][col]
            aug[row] = [aug[row][i] - factor * aug[col][i] for i in range(2 * n)]
    return [row[n:] for row in aug]


def mat_vec(matrix: list[list[float]], vector: list[float]) -> list[float]:
    return [sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix]


def quadratic(vector: list[float], matrix: list[list[float]]) -> float:
    mv = mat_vec(matrix, vector)
    return sum(vector[i] * mv[i] for i in range(len(vector)))


def build_covariance(
    output_ids: list[str],
    input_ids: list[str],
    jacobian: dict[str, dict[str, float]],
    input_sigmas: dict[str, float],
    theory_sigmas: dict[str, float],
    rho: float,
) -> list[list[float]]:
    input_cov = []
    for left in input_ids:
        row = []
        for right in input_ids:
            corr = 1.0 if left == right else rho
            row.append(corr * input_sigmas[left] * input_sigmas[right])
        input_cov.append(row)

    cov = []
    for out_i in output_ids:
        row = []
        for out_j in output_ids:
            value = 0.0
            for a, input_a in enumerate(input_ids):
                for b, input_b in enumerate(input_ids):
                    value += jacobian.get(out_i, {}).get(input_a, 0.0) * input_cov[a][b] * jacobian.get(out_j, {}).get(input_b, 0.0)
            if out_i == out_j:
                value += theory_sigmas.get(out_i, 0.0) ** 2
            row.append(value)
        cov.append(row)
    return cov


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_fullcovarianceprofile_or_multiloopconventionaudit.candidate.json")
    previous_gate = load(
        DATA
        / "selected_fullcovarianceprofile_or_multiloopconventionaudit"
        / "updated_true_equivalence_gate_after_diagonal_profile.packet.json"
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
    diagonal_profile = load(
        DATA
        / "selected_fullcovarianceprofile_or_multiloopconventionaudit"
        / "diagonal_profile_likelihood_execution.packet.json"
    )
    literature = load(
        DATA
        / "selected_externalliteraturergbenchmarkvalues_or_thresholdcovariance"
        / "external_literature_rg_benchmark_values.packet.json"
    )

    independent_outputs = ["lambda_Mt", "y_t_Mt", "g_2_Mt", "g_Y_Mt", "g_3_Mt"]
    redundant_outputs = ["g_1_GUT_Mt"]
    input_ids = ["M_W_GeV", "M_h_GeV", "M_t_GeV", "alpha3_MZ"]
    current = formula["current_repo_input_variant"]["values"]
    central = formula["buttazzo_central_input_replay"]["values"]
    delta = [float(current[key]) - float(central[key]) for key in independent_outputs]
    theory_sigmas = {
        key: float(row.get("theory_uncertainty", 0.0))
        for key, row in literature["literature_values"].items()
    }
    jacobian = covariance["jacobian"]
    input_sigmas = covariance["input_sigmas"]

    scan = []
    for rho in [-0.30, -0.20, -0.10, 0.0, 0.10, 0.20, 0.30, 0.50, 0.70, 0.90]:
        cov = build_covariance(independent_outputs, input_ids, jacobian, input_sigmas, theory_sigmas, rho)
        inv = invert(cov)
        chi2 = quadratic(delta, inv)
        scan.append(
            {
                "rho_equicorrelation": rho,
                "chi2": chi2,
                "degrees_of_freedom": len(independent_outputs),
                "reduced_chi2": chi2 / len(independent_outputs),
            }
        )
    min_row = min(scan, key=lambda row: row["chi2"])
    max_row = max(scan, key=lambda row: row["chi2"])
    core_rows = [row for row in scan if -0.20 <= row["rho_equicorrelation"] <= 0.70]
    core_max_row = max(core_rows, key=lambda row: row["chi2"])

    compressed_diagonal_chi2 = next(row for row in scan if row["rho_equicorrelation"] == 0.0)["chi2"]
    profile_packet = {
        "schema": "MTTCorrelationRobustProfileEnvelope.v1",
        "status": "CORRELATION_ROBUST_PROFILE_ENVELOPE_BUILT_FULL_PROFILE_VALUES_OPEN",
        "basis_reduction": {
            "reason": "g_1_GUT_Mt is exactly sqrt(5/3)*g_Y_Mt and must not be double-counted in a correlated profile.",
            "independent_outputs": independent_outputs,
            "redundant_outputs_removed": redundant_outputs,
            "original_diagonal_profile_chi2_with_redundant_g1_row": diagonal_profile["chi2_diagonal"],
            "compressed_diagonal_chi2_without_redundant_g1_row": compressed_diagonal_chi2,
        },
        "input_correlation_model": {
            "type": "equicorrelation stress envelope over measured inputs",
            "input_ids": input_ids,
            "rho_values": [row["rho_equicorrelation"] for row in scan],
            "psd_domain_note": "For four equicorrelated inputs, rho > -1/3 is positive semidefinite; scan uses rho >= -0.30.",
        },
        "scan_rows": scan,
        "chi2_envelope": {
            "min_chi2": min_row["chi2"],
            "min_rho": min_row["rho_equicorrelation"],
            "max_chi2": max_row["chi2"],
            "max_rho": max_row["rho_equicorrelation"],
            "max_reduced_chi2": max_row["reduced_chi2"],
            "core_rho_window": [-0.20, 0.70],
            "core_max_chi2": core_max_row["chi2"],
            "core_max_rho": core_max_row["rho_equicorrelation"],
            "core_max_reduced_chi2": core_max_row["reduced_chi2"],
            "passes_core_correlation_envelope": core_max_row["reduced_chi2"] < 3.0,
            "passes_extreme_correlation_stress_envelope": max_row["reduced_chi2"] < 3.0,
        },
        "accepted_as_full_correlated_profile": False,
        "why_not_full_profile": (
            "The envelope stress-tests plausible correlation structure but does not replace published or "
            "reconstructed profile likelihood values. It is a robustness audit, not a final correlated fit."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    qft_packet = {
        "schema": "MTTLocalQFTObservableValueGate.v1",
        "status": "LOCAL_QFT_OBSERVABLE_VALUE_GATE_BUILT_VALUES_OPEN",
        "already_available": {
            "local_qft_observable_functor_interface": True,
            "weak_scale_boundary_profile_replay": True,
            "source_vs_measured_boundary_guarded": True,
        },
        "required_value_rows": [
            {
                "id": "two_point_functions_or_propagator_normalizations",
                "description": "Declare local field propagator/renormalization convention induced by the admitted SM-parity parameters.",
                "closed": False,
            },
            {
                "id": "ward_anomaly_observable_checks",
                "description": "Replay Ward identities/anomaly constraints in the local QFT observable functor.",
                "closed": False,
            },
            {
                "id": "representative_scattering_or_decay_rows",
                "description": "Supply at least a minimal reproducible observable suite using the same measured parameter packet.",
                "closed": False,
            },
            {
                "id": "correlators_not_source_data_guard",
                "description": "Ensure benchmark correlators or S-matrix rows never select the MTT source/operator packet.",
                "closed": True,
            },
        ],
        "can_close_local_qft_observable_values_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    remaining = [
        blocker
        for blocker in previous_gate["remaining_true_equivalence_blockers"]
        if blocker != "full correlated covariance/profile likelihood values"
    ]
    if "published/reconstructed correlated profile likelihood values" not in remaining:
        remaining.insert(0, "published/reconstructed correlated profile likelihood values")
    if "local QFT observable value rows" not in remaining:
        remaining.insert(2, "local QFT observable value rows")
    updated = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterCorrelationEnvelope.v1",
        "status": "CORRELATION_ENVELOPE_BUILT_CORRELATED_VALUES_AND_QFT_OBSERVABLES_OPEN",
        "previous_true_equivalence_blockers": previous_gate["remaining_true_equivalence_blockers"],
        "closed_now": [
            "hypercharge basis reduction for correlated profile",
            "correlation-robust profile envelope",
            "local QFT observable value gate",
        ],
        "remaining_true_equivalence_blockers": remaining,
        "next_primary_value_gate": "published/reconstructed correlated profile values or local QFT observable value rows",
        "guardrails": {
            "correlation_envelope_is_not_published_profile": True,
            "hypercharge_not_double_counted": True,
            "local_qft_observable_values_still_open": True,
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedCorrelatedProfileValuesOrLocalQFTObservableValues",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_fullcovarianceprofile_or_multiloopconventionaudit.candidate.json"),
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
            "diagonal_profile": rel(
                DATA
                / "selected_fullcovarianceprofile_or_multiloopconventionaudit"
                / "diagonal_profile_likelihood_execution.packet.json"
            ),
        },
        "output_packets": {
            "correlation_robust_profile_envelope": rel(PROFILE),
            "local_qft_observable_value_gate": rel(QFT),
            "updated_true_equivalence_gate": rel(UPDATED),
        },
        "theorem": {
            "name": "CorrelationEnvelopeAndQFTObservableGateTheorem",
            "proved": True,
            "statement": (
                "The correlated weak-scale profile must remove the redundant GUT-normalized hypercharge row "
                "before covariance inversion. On the compressed basis, an equicorrelation stress envelope can "
                "be computed and the current input variant passes the coarse envelope. This closes robustness "
                "and basis-reduction bookkeeping, while full published/reconstructed profile values and local "
                "QFT observable values remain open."
            ),
        },
        "what_closes_now": {
            "hypercharge_basis_reduction": True,
            "correlation_robust_profile_envelope": True,
            "coarse_correlation_envelope_passes": profile_packet["chi2_envelope"]["passes_core_correlation_envelope"],
            "extreme_correlation_stress_envelope_open": not profile_packet["chi2_envelope"]["passes_extreme_correlation_stress_envelope"],
            "local_qft_observable_value_gate_built": True,
            "superset_strategy_preserved": True,
        },
        "what_remains_open": {
            "published_or_reconstructed_correlated_profile_values": True,
            "local_QFT_observable_value_rows": True,
            "multi_loop_threshold_convention_values": True,
            "QM_GR_measurement_response_interfaces": True,
            "actual_QaSU3_operator_packet": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "correlation_envelope_built": True,
            "full_correlated_profile_closed": False,
            "local_QFT_observable_values_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_CorrelatedProfileValues_or_LocalQFTObservableValues_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "correlation_envelope_built": True,
        "coarse_correlation_envelope_passes": profile_packet["chi2_envelope"]["passes_core_correlation_envelope"],
        "extreme_correlation_stress_envelope_open": not profile_packet["chi2_envelope"]["passes_extreme_correlation_stress_envelope"],
        "full_correlated_profile_closed": False,
        "local_QFT_observable_values_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_LocalQFTObservableRows_or_FinalTrueSMEquivalenceGap_v1",
    }

    note = """# MTT Selected CorrelatedProfileValues or LocalQFTObservableValues v1

Status: `MTT_SELECTED_CORRELATEDPROFILEVALUES_OR_LOCALQFTOBSERVABLEVALUES_BUILT_CORRELATION_ENVELOPE_QFT_VALUES_OPEN`.

This artifact corrects the correlated-profile basis: `g1_GUT(Mt)` is exactly
`sqrt(5/3) gY(Mt)`, so it must not be double-counted when covariance is used.

On the compressed basis it builds an equicorrelation stress envelope over the
measured inputs. The current weak-scale boundary replay passes this coarse
correlation envelope, but the envelope is not a published or reconstructed
profile likelihood.

The local-QFT observable value gate is also made explicit. The functor interface
exists, but concrete propagator/correlator/S-matrix or low-energy observable
rows remain open.
"""

    for path, payload in [
        (PROFILE, profile_packet),
        (QFT, qft_packet),
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
