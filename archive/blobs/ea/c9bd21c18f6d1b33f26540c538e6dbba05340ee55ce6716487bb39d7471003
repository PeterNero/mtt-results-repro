"""Build remaining Higgs EW formula-kernel/precision-import execution gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgsewformulakernelexecution_or_precisionimportrows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
READINESS = PACKET_DIR / "ew_formula_kernel_execution_readiness.packet.json"
IMPORT_CONTRACT = PACKET_DIR / "ew_precision_import_row_contract.packet.json"
DIAGONAL = PACKET_DIR / "ew_three_channel_diagonal_profile_fallback.packet.json"
STRESS = PACKET_DIR / "ew_three_channel_correlation_stress_profile.packet.json"
DECISION = PACKET_DIR / "precision_import_decision_after_ew_profile.packet.json"
UPDATED_TRUE = PACKET_DIR / "updated_true_equivalence_gate_after_ew_import_profile.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsEWFormulaKernelExecution_or_PrecisionImportRows_v1.md"

STATUS = "MTT_SELECTED_HIGGSEWFORMULAKERNELEXECUTION_OR_PRECISIONIMPORTROWS_BUILT_PROFILE_IMPORT_GATE_VALUES_OPEN"
CHANNELS = ["H_to_WW_star", "H_to_ZZ_star", "H_to_Z_gamma"]


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
        pivot = max(range(col, n), key=lambda row: abs(aug[row][col]))
        if abs(aug[pivot][col]) < 1e-40:
            raise ValueError("singular covariance matrix")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [value / scale for value in aug[col]]
        for row in range(n):
            if row == col:
                continue
            factor = aug[row][col]
            aug[row] = [aug[row][k] - factor * aug[col][k] for k in range(2 * n)]
    return [row[n:] for row in aug]


def matvec(matrix: list[list[float]], vector: list[float]) -> list[float]:
    return [sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix]


def quad(vector: list[float], matrix: list[list[float]]) -> float:
    mv = matvec(matrix, vector)
    return sum(vector[i] * mv[i] for i in range(len(vector)))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgsremainingewformularows_or_precisiontotalwidth.candidate.json")
    ew_gate = load(
        DATA
        / "selected_higgsremainingewformularows_or_precisiontotalwidth"
        / "remaining_ew_formula_or_precision_import_gate.packet.json"
    )
    refreshed = load(
        DATA
        / "selected_higgscomputedchannelrefresh_or_totalwidthreplay"
        / "refreshed_higgs_total_width_replay.packet.json"
    )
    covariance_contract = load(
        DATA
        / "selected_higgscovarianceprofilecontract_or_uniformformularows"
        / "higgs_covariance_profile_contract.packet.json"
    )
    previous_true = load(
        DATA
        / "selected_higgsremainingewformularows_or_precisiontotalwidth"
        / "updated_true_equivalence_gate_after_remaining_ew_gate.packet.json"
    )

    gate_by_channel = {row["channel"]: row for row in ew_gate["rows"]}
    replay_by_channel = {row["channel"]: row for row in refreshed["rows"]}
    variances = covariance_contract["diagonal_fallback_from_sidecars"]["diagonal_variances_GeV2"]

    readiness_rows = []
    import_rows = []
    residual_vector = []
    sigma_vector = []
    diagonal_rows = []
    covariance_matrix = []
    for channel in CHANNELS:
        gate = gate_by_channel[channel]
        replay = replay_by_channel[channel]
        residual = float(replay["width_GeV"]) - float(gate["benchmark_width_GeV"])
        variance = float(variances[channel])
        sigma = variance**0.5
        residual_vector.append(residual)
        sigma_vector.append(sigma)
        readiness_rows.append(
            {
                "channel": channel,
                "formula_family": gate["required_formula_family"],
                "operator_attachment_required": gate["operator_attachment_required"],
                "minimum_kernel_inputs": [
                    "declared electroweak input scheme",
                    "declared Higgs and vector-boson mass convention",
                    "declared perturbative and threshold order",
                    "uncertainty propagation into the ten-channel profile basis",
                ],
                "formula_kernel_filled": False,
                "formula_kernel_executable_now": False,
                "accepted_as_precision_formula_row": False,
                "benchmark_used_as_source_selector": False,
            }
        )
        import_rows.append(
            {
                "channel": channel,
                "current_external_width_GeV": replay["width_GeV"],
                "benchmark_width_GeV": gate["benchmark_width_GeV"],
                "absolute_uncertainty_GeV": gate["absolute_uncertainty_GeV"],
                "minimum_precision_import_requirements": [
                    "source/provenance version frozen",
                    "same electroweak input scheme and total-width convention declared",
                    "row covariance/profile semantics supplied or profiled",
                    "central value imported after source selection, never used to select the source",
                    "replacement path to executable formula kernel remains recorded",
                ],
                "external_value_replayed": True,
                "zero_residual_by_import_identity": residual == 0.0,
                "accepted_precision_import_filled": False,
                "accepted_as_precision_total_width_row": False,
                "observed_data_used_as_selector": False,
                "target_fitting_used": False,
            }
        )
        diagonal_rows.append(
            {
                "channel": channel,
                "residual_GeV": residual,
                "sigma_GeV": sigma,
                "variance_GeV2": variance,
                "diagonal_pull": residual / sigma if sigma else 0.0,
                "external_import_identity_row": True,
                "not_formula_validation": True,
                "accepted_as_full_profile": False,
            }
        )

    for i in range(len(CHANNELS)):
        covariance_matrix.append([0.0 for _ in CHANNELS])
        covariance_matrix[i][i] = sigma_vector[i] ** 2

    diagonal_inverse = invert(covariance_matrix)
    diagonal_chi_square = quad(residual_vector, diagonal_inverse)
    diagonal = {
        "schema": "MTTHiggsEWThreeChannelDiagonalProfileFallback.v1",
        "status": "EW_DIAGONAL_PROFILE_FALLBACK_BUILT_IMPORT_IDENTITY_NOT_FORMULA_VALIDATION",
        "channels": CHANNELS,
        "residual_vector_GeV": residual_vector,
        "covariance_matrix_GeV2": covariance_matrix,
        "rows": diagonal_rows,
        "summary": {
            "channel_count": len(CHANNELS),
            "diagonal_chi_square": diagonal_chi_square,
            "all_rows_zero_residual_by_import_identity": all(row["residual_GeV"] == 0.0 for row in diagonal_rows),
            "accepted_as_diagonal_fallback": True,
            "accepted_as_full_correlated_profile": False,
            "accepted_as_formula_validation": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    rho_values = [-0.25, 0.0, 0.25, 0.5]
    stress_rows = []
    for rho in rho_values:
        covariance = []
        for i in range(len(CHANNELS)):
            row = []
            for j in range(len(CHANNELS)):
                row.append(sigma_vector[i] * sigma_vector[j] * (1.0 if i == j else rho))
            covariance.append(row)
        inverse = invert(covariance)
        stress_rows.append(
            {
                "rho": rho,
                "covariance_model": "equicorrelated electroweak three-row stress test",
                "minimum_eigenvalue_positive_by_equicorrelation_bound": rho > -1.0 / (len(CHANNELS) - 1) and rho < 1.0,
                "chi_square": quad(residual_vector, inverse),
                "zero_residual_by_import_identity": True,
                "accepted_as_correlation_stress_test": True,
                "accepted_as_full_correlated_profile": False,
            }
        )
    chi_values = [row["chi_square"] for row in stress_rows]
    stress = {
        "schema": "MTTHiggsEWThreeChannelCorrelationStressProfile.v1",
        "status": "EW_CORRELATION_STRESS_PROFILE_BUILT_FULL_PROFILE_OPEN",
        "channels": CHANNELS,
        "rho_grid": rho_values,
        "rows": stress_rows,
        "summary": {
            "stress_models_checked": len(stress_rows),
            "all_models_psd_by_equicorrelation_bound": all(
                row["minimum_eigenvalue_positive_by_equicorrelation_bound"] for row in stress_rows
            ),
            "min_chi_square": min(chi_values),
            "max_chi_square": max(chi_values),
            "accepted_as_correlation_stress_profile": True,
            "accepted_as_full_correlated_profile": False,
            "accepted_as_formula_validation": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    readiness = {
        "schema": "MTTHiggsEWFormulaKernelExecutionReadiness.v1",
        "status": "EW_FORMULA_KERNEL_READINESS_BUILT_KERNELS_OPEN",
        "rows": readiness_rows,
        "summary": {
            "row_count": len(readiness_rows),
            "formula_kernels_filled": 0,
            "formula_kernels_open": len(readiness_rows),
            "all_rows_have_operator_attachment_requirement": True,
            "all_rows_have_minimum_kernel_inputs": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    import_contract = {
        "schema": "MTTHiggsEWPrecisionImportRowContract.v1",
        "status": "EW_PRECISION_IMPORT_CONTRACT_BUILT_ACCEPTED_IMPORTS_OPEN",
        "rows": import_rows,
        "summary": {
            "row_count": len(import_rows),
            "external_values_replayed": len(import_rows),
            "accepted_precision_import_count": 0,
            "all_rows_have_import_requirements": True,
            "central_values_used_as_replay_inputs_only": True,
            "accepted_as_precision_import_layer": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTPrecisionImportDecisionAfterEWProfile.v1",
        "status": "EW_PROFILE_AND_IMPORT_CONTRACT_BUILT_PRECISION_TOTAL_WIDTH_STILL_OPEN",
        "formula_kernel_readiness_built": True,
        "precision_import_contract_built": True,
        "diagonal_profile_fallback_built": True,
        "correlation_stress_profile_built": True,
        "formula_kernels_filled": False,
        "accepted_precision_imports_filled": False,
        "values_promotable_to_precision_total_width_now": False,
        "blocked_by": [
            "WW*/ZZ*/Z gamma executable formula kernels not filled",
            "accepted external precision imports lack full provenance/covariance/profile semantics",
            "diagonal and stress profiles are replay infrastructure, not full empirical correlated likelihoods",
            "ten-channel precision total-width profile still open",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    updated_true = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterEWImportProfile.v1",
        "status": "EW_IMPORT_PROFILE_GATE_BUILT_TRUE_EQUIVALENCE_STILL_OPEN",
        "previous_true_equivalence_blockers": previous_true["remaining_true_equivalence_blockers"],
        "closed_now": previous_true["closed_now"] + [
            "Higgs EW formula-kernel readiness matrix",
            "Higgs EW precision-import row contract",
            "Higgs EW diagonal profile fallback and equicorrelation stress profile",
        ],
        "remaining_true_equivalence_blockers": previous_true["remaining_true_equivalence_blockers"],
        "next_primary_value_gate": "fill WW*/ZZ*/Z gamma formula kernels or accepted precision imports with full profile semantics",
        "guardrails": {
            "import_identity_not_formula_validation": True,
            "stress_profile_not_full_profile_likelihood": True,
            "precision_total_width_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsEWFormulaKernelExecutionOrPrecisionImportRows",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgsremainingewformularows_or_precisiontotalwidth.candidate.json"),
            "remaining_ew_gate": rel(
                DATA
                / "selected_higgsremainingewformularows_or_precisiontotalwidth"
                / "remaining_ew_formula_or_precision_import_gate.packet.json"
            ),
            "refreshed_total_width_replay": rel(
                DATA
                / "selected_higgscomputedchannelrefresh_or_totalwidthreplay"
                / "refreshed_higgs_total_width_replay.packet.json"
            ),
            "covariance_profile_contract": rel(
                DATA
                / "selected_higgscovarianceprofilecontract_or_uniformformularows"
                / "higgs_covariance_profile_contract.packet.json"
            ),
        },
        "output_packets": {
            "formula_kernel_execution_readiness": rel(READINESS),
            "precision_import_row_contract": rel(IMPORT_CONTRACT),
            "ew_three_channel_diagonal_profile_fallback": rel(DIAGONAL),
            "ew_three_channel_correlation_stress_profile": rel(STRESS),
            "precision_import_decision": rel(DECISION),
            "updated_true_equivalence_gate": rel(UPDATED_TRUE),
        },
        "theorem": {
            "name": "HiggsEWFormulaKernelExecutionOrPrecisionImportGateTheorem",
            "proved": True,
            "statement": (
                "For the three remaining external-fill Higgs electroweak rows, the repo can construct a "
                "formula-kernel readiness matrix, a precision-import contract, and executable diagonal/stress "
                "profile infrastructure without using benchmark values as source selectors. This closes the "
                "execution gate, but not the formula kernels, accepted precision imports, precision total width, "
                "true SM equivalence, or no-knob closure."
            ),
        },
        "what_closes_now": {
            "EW_formula_kernel_readiness_matrix": True,
            "EW_precision_import_contract": True,
            "EW_three_channel_diagonal_profile_fallback": True,
            "EW_equicorrelation_stress_profile": True,
            "import_identity_guardrail": True,
        },
        "what_remains_open": {
            "WW_star_executable_formula_kernel_or_accepted_import": True,
            "ZZ_star_executable_formula_kernel_or_accepted_import": True,
            "Z_gamma_executable_formula_kernel_or_accepted_import": True,
            "full_ten_channel_covariance_profile": True,
            "precision_total_width": True,
            "branching_ratios": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "formula_kernel_readiness_built": True,
            "precision_import_contract_built": True,
            "ew_profile_fallback_built": True,
            "ew_correlation_stress_profile_built": True,
            "formula_kernels_filled": False,
            "precision_import_rows_accepted": False,
            "precision_total_width_closed": False,
            "branching_ratios_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_HiggsEWFormulaKernelExecution_or_PrecisionImportRows_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "formula_kernel_readiness_built": True,
        "precision_import_contract_built": True,
        "ew_profile_fallback_built": True,
        "ew_correlation_stress_profile_built": True,
        "formula_kernels_filled": False,
        "precision_import_rows_accepted": False,
        "precision_total_width_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_HiggsTenChannelCovarianceProfile_or_BranchingReplay_v1",
    }

    note = f"""# MTT Selected HiggsEWFormulaKernelExecution or PrecisionImportRows v1

Status: `{STATUS}`.

This artifact advances the three remaining Higgs electroweak rows:
`H_to_WW_star`, `H_to_ZZ_star`, and `H_to_Z_gamma`.

It builds a formula-kernel readiness matrix, a precision-import contract, and
executable diagonal plus equicorrelated stress-profile packets. The zero
residuals in these EW rows are import identities from the current replay layer;
they are not formula validation and not a precision-import acceptance.

Precision total width, branching ratios, true SM equivalence, and no-knob
closure remain open.
"""

    for path, payload in [
        (READINESS, readiness),
        (IMPORT_CONTRACT, import_contract),
        (DIAGONAL, diagonal),
        (STRESS, stress),
        (DECISION, decision),
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
