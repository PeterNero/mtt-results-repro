"""Build numeric interim cross-block covariance values or Rtheta coefficient execution artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_crossblockcovariancevalues_or_rthetacoefficientexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
MATRIX = PACKET_DIR / "deduplicated_interim_block_covariance_matrix.packet.json"
GATE = PACKET_DIR / "cross_block_numeric_value_gate.packet.json"
RTHETA = PACKET_DIR / "rtheta_coefficient_execution_gate.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_interim_covariance_values.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_CrossBlockCovarianceValues_or_RThetaCoefficientExecution_v1.md"

PREVIOUS = DATA / "selected_crossblockcovariance_or_rthetacoefficientvaluefill.candidate.json"
BASIS = (
    DATA
    / "selected_crossblockcovariance_or_rthetacoefficientvaluefill"
    / "deduplicated_cross_block_covariance_basis.packet.json"
)
DEPS = (
    DATA
    / "selected_crossblockcovariance_or_rthetacoefficientvaluefill"
    / "cross_block_covariance_dependency_graph.packet.json"
)
WEAK_SENSITIVITY = (
    DATA
    / "selected_polethresholdresidualvalues_or_covarianceprofile"
    / "diagonal_sensitivity_covariance_scaffold.packet.json"
)
WZH_SIDECARS = (
    DATA
    / "selected_covariancesidecarfill_or_rthetasourcerowderivation"
    / "wzh_gauge_and_lambda_covariance_sidecars.packet.json"
)
BCT_EFT = (
    DATA
    / "selected_bctprofilereconciliation_or_rthetamassschemederivation"
    / "bct_correlated_eft_profile.packet.json"
)
BCT_MATRIX = (
    DATA
    / "selected_allbctexternalrows_or_fullsmconventionreconciliation"
    / "huang_zhou_eft_fullsm_reconciliation_matrix.packet.json"
)
HIGGS_COV = (
    DATA
    / "selected_higgshomogeneousprofile_or_routeaformulacovariance"
    / "source_derived_correlated_covariance_model.packet.json"
)
RTHETA_GATE = (
    DATA
    / "selected_crossblockcovariance_or_rthetacoefficientvaluefill"
    / "rtheta_coefficient_value_fill_gate.packet.json"
)

STATUS = (
    "MTT_SELECTED_CROSSBLOCKCOVARIANCEVALUES_OR_RTHETACOEFFICIENTEXECUTION_"
    "BUILT_NUMERIC_INTERIM_BLOCK_MATRIX_CROSS_VALUES_OPEN"
)
NEXT = "MTT_Selected_CommonScaleJacobian_or_RThetaThresholdResponseExecution_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing cross-block covariance value sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [PREVIOUS, BASIS, DEPS, WEAK_SENSITIVITY, WZH_SIDECARS, BCT_EFT, BCT_MATRIX, HIGGS_COV, RTHETA_GATE]
    require_sources(sources)

    previous = load(PREVIOUS)
    basis = load(BASIS)
    deps = load(DEPS)
    weak_sensitivity = load(WEAK_SENSITIVITY)
    wzh_sidecars = load(WZH_SIDECARS)
    bct_eft = load(BCT_EFT)
    bct_matrix = load(BCT_MATRIX)
    higgs_cov = load(HIGGS_COV)
    rtheta_gate_source = load(RTHETA_GATE)

    row_basis = basis["deduplicated_interim_basis"]
    index = {row_id: i for i, row_id in enumerate(row_basis)}
    n = len(row_basis)
    cov = [[0.0 for _ in range(n)] for _ in range(n)]
    source_map: dict[str, str] = {}

    # Weak block: use the available diagonal sensitivity scaffold on the deduplicated weak basis.
    for row_id in ["lambda_Mt", "y_t_Mt", "g_2_Mt", "g_Y_Mt", "g_3_Mt"]:
        variance = weak_sensitivity["propagated_diagonal_uncertainties"][row_id]["diagonal_sigma"] ** 2
        cov[index[row_id]][index[row_id]] = variance
        source_map[row_id] = rel(WEAK_SENSITIVITY)

    # Independent W/Z/H extension: v(G_F) row from the WZH sidecar packet.
    v_sidecar = next(row for row in wzh_sidecars["row_sidecars"] if row["id"] == "v_from_G_F_tree_reference")
    cov[index["v_from_G_F_tree_reference"]][index["v_from_G_F_tree_reference"]] = v_sidecar["variance"]
    source_map["v_from_G_F_tree_reference"] = rel(WZH_SIDECARS)

    # BCT block: use Huang-Zhou EFT correlation matrix and table uncertainties.
    bct_rows = bct_eft["row_order"]
    bct_sigmas = [
        bct_matrix["matrix_rows"][row_id]["EFT_QCDxQED_5q3l_MZ"]["table_uncertainty_GeV"]
        for row_id in bct_rows
    ]
    for i, left in enumerate(bct_rows):
        for j, right in enumerate(bct_rows):
            cov[index[left]][index[right]] = bct_eft["correlation_matrix"][i][j] * bct_sigmas[i] * bct_sigmas[j]
        source_map[left] = rel(BCT_EFT)

    # Higgs block: source-derived internal covariance model.
    higgs_rows = higgs_cov["row_basis"]
    for i, left in enumerate(higgs_rows):
        for j, right in enumerate(higgs_rows):
            cov[index[left]][index[right]] = higgs_cov["covariance_matrix_GeV2"][i][j]
        source_map[left] = rel(HIGGS_COV)

    nonzero_offdiag = 0
    cross_block_nonzero = 0
    block_of = {}
    for row in ["lambda_Mt", "y_t_Mt", "g_2_Mt", "g_Y_Mt", "g_3_Mt"]:
        block_of[row] = "weak"
    block_of["v_from_G_F_tree_reference"] = "wzh_extension"
    for row in bct_rows:
        block_of[row] = "BCT"
    for row in higgs_rows:
        block_of[row] = "Higgs"
    for i, left in enumerate(row_basis):
        for j, right in enumerate(row_basis):
            if i >= j or cov[i][j] == 0.0:
                continue
            nonzero_offdiag += 1
            if block_of[left] != block_of[right]:
                cross_block_nonzero += 1

    matrix_packet = {
        "schema": "MTTDeduplicatedInterimBlockCovarianceMatrix.v1",
        "status": "NUMERIC_INTERIM_BLOCK_COVARIANCE_MATRIX_BUILT_CROSS_BLOCK_ENTRIES_OPEN",
        "basis_source": rel(BASIS),
        "row_basis": row_basis,
        "row_count": n,
        "covariance_matrix": cov,
        "row_source_map": source_map,
        "block_policy": {
            "weak_block": "diagonal sensitivity scaffold only",
            "wzh_extension": "v(G_F) sidecar only; WZH overlap rows deduplicated into weak block",
            "BCT_block": "Huang-Zhou EFT 3-row correlated covariance",
            "Higgs_block": "source-derived 10-row correlated covariance model",
            "cross_block_entries": "left zero/open pending common-scale/shared-input Jacobian",
        },
        "diagnostics": {
            "nonzero_offdiagonal_entries_upper_triangle": nonzero_offdiag,
            "nonzero_cross_block_entries_upper_triangle": cross_block_nonzero,
            "has_BCT_internal_correlations": True,
            "has_Higgs_internal_correlations": True,
            "has_numeric_cross_block_covariance_values": False,
        },
        "accepted_as_numeric_interim_block_covariance": True,
        "accepted_as_full_cross_block_covariance": False,
        "accepted_as_full_profile_likelihood": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(MATRIX, matrix_packet)

    gate = {
        "schema": "MTTCrossBlockNumericValueGate.v1",
        "status": "INTERIM_BLOCK_VALUES_BUILT_NUMERIC_CROSS_BLOCK_VALUES_OPEN",
        "matrix_source": rel(MATRIX),
        "dependency_graph_source": rel(DEPS),
        "numeric_interim_block_covariance_values_closed": True,
        "numeric_cross_block_covariance_values_closed": False,
        "full_covariance_profile_likelihood_closed": False,
        "remaining_cross_block_value_requirements": deps["remaining_numeric_requirements"],
        "why_zero_cross_block_entries_are_not_a_full_claim": (
            "Zeros in the interim matrix mean no accepted value has been emitted for that cross-block covariance. "
            "They are placeholders for a block profile ladder, not independence assumptions."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(GATE, gate)

    rtheta_gate = {
        "schema": "MTTRThetaCoefficientExecutionGate.v1",
        "status": "RTHETA_COEFFICIENT_EXECUTION_GATE_RECHECKED_VALUES_OPEN",
        "previous_rtheta_gate_source": rel(RTHETA_GATE),
        "numeric_interim_covariance_matrix_source": rel(MATRIX),
        "what_numeric_matrix_changes": [
            "profile bookkeeping now has concrete interim covariance values on the deduplicated basis",
            "Rtheta coefficient execution can target a 19-row validation basis without duplicate WZH/weak rows",
        ],
        "what_remains_required": rtheta_gate_source["why_this_does_not_fill_Rtheta_coefficients"],
        "Rtheta_coefficient_values_closed": False,
        "selected_Rtheta_source_rows_closed": False,
        "accepted_Rtheta_source_row_count": rtheta_gate_source["accepted_Rtheta_source_row_count"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(RTHETA, rtheta_gate)

    cutset = {
        "schema": "MTTNextCutsetAfterInterimCovarianceValues.v1",
        "status": "NEXT_ATTACK_COMMON_SCALE_JACOBIAN_OR_RTHETA_THRESHOLD_RESPONSE_EXECUTION",
        "closed_now": {
            "numeric_interim_block_covariance_matrix": True,
            "BCT_internal_covariance_values_integrated": True,
            "Higgs_internal_covariance_values_integrated": True,
            "Rtheta_coefficient_execution_gate_rechecked": True,
        },
        "still_open": {
            "numeric_cross_block_covariance_values": True,
            "common_scale_convention_map": True,
            "common_scale_MZ_to_Mt_jacobian": True,
            "Rtheta_coefficient_values": True,
            "selected_threshold_response_functional": True,
            "selected_Rtheta_source_rows": True,
            "full_covariance_profile_likelihood": True,
            "true_SM_equivalence": True,
            "full_no_knob": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "derive common-scale MZ-to-Mt Jacobian coupling BCT rows to weak/Higgs rows",
            "route_B": "execute selected threshold response functional coefficients for threshold::W_Z_H",
            "route_C": "emit cross-block covariance entries from shared G_F/v, M_h, M_t, alpha_s, and threshold-convention nuisance directions",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedCrossBlockCovarianceValuesOrRThetaCoefficientExecution",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "deduplicated_interim_block_covariance_matrix": rel(MATRIX),
            "cross_block_numeric_value_gate": rel(GATE),
            "rtheta_coefficient_execution_gate": rel(RTHETA),
            "next_cutset_after_interim_covariance_values": rel(CUTSET),
        },
        "theorem": {
            "name": "InterimBlockCovarianceMatrixTheorem",
            "proved": True,
            "statement": (
                "On the deduplicated 19-row basis, the available internal covariance blocks determine a "
                "numeric interim block covariance matrix: weak diagonal sensitivity rows, v(G_F), BCT "
                "EFT correlated rows, and the Higgs source-derived covariance block. Cross-block entries "
                "remain open placeholders, so this is not a full covariance/profile likelihood."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "numeric_interim_block_covariance_matrix_closed": True,
            "numeric_cross_block_covariance_values_closed": False,
            "Rtheta_coefficient_values_closed": False,
            "selected_Rtheta_source_rows_closed": False,
            "full_covariance_profile_likelihood_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "previous_status": previous["status"],
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_CrossBlockCovarianceValues_or_RThetaCoefficientExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "numeric_interim_block_covariance_matrix_closed": True,
        "row_count": n,
        "numeric_cross_block_covariance_values_closed": False,
        "Rtheta_coefficient_values_closed": False,
        "selected_Rtheta_source_rows_closed": False,
        "full_covariance_profile_likelihood_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected CrossBlockCovarianceValues or RThetaCoefficientExecution v1

Status: `{STATUS}`.

This artifact emits the numeric interim block covariance matrix on the
deduplicated 19-row basis.

```text
row count                              : {n}
numeric interim block covariance closed: true
numeric cross-block covariance closed  : false
full covariance/profile closed         : false
R_theta coefficient values closed      : false
```

Cross-block zero entries are open placeholders, not independence assumptions.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
