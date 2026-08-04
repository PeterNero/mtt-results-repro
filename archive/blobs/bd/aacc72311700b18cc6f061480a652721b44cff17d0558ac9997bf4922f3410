"""Audit cross-block covariance values or Rtheta coefficient execution artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_crossblockcovariancevalues_or_rthetacoefficientexecution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
MATRIX = PACKET_DIR / "deduplicated_interim_block_covariance_matrix.packet.json"
GATE = PACKET_DIR / "cross_block_numeric_value_gate.packet.json"
RTHETA = PACKET_DIR / "rtheta_coefficient_execution_gate.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_interim_covariance_values.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_CrossBlockCovarianceValues_or_RThetaCoefficientExecution_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_CROSSBLOCKCOVARIANCEVALUES_OR_RTHETACOEFFICIENTEXECUTION_"
    "BUILT_NUMERIC_INTERIM_BLOCK_MATRIX_CROSS_VALUES_OPEN"
)
NEXT = "MTT_Selected_CommonScaleJacobian_or_RThetaThresholdResponseExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    matrix = load(MATRIX)
    gate = load(GATE)
    rtheta = load(RTHETA)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    for key in ["closure_claimed", "unpatched_theorem_closure_claimed", "observed_data_used_as_selector", "target_fitting_used"]:
        require(data[key] is False, f"candidate guardrail overclaimed: {key}")

    require(matrix["status"] == "NUMERIC_INTERIM_BLOCK_COVARIANCE_MATRIX_BUILT_CROSS_BLOCK_ENTRIES_OPEN", "matrix status mismatch")
    require(matrix["row_count"] == 19, "matrix row count mismatch")
    require(len(matrix["row_basis"]) == 19, "basis length mismatch")
    require(len(matrix["covariance_matrix"]) == 19, "matrix dimension mismatch")
    require(all(len(row) == 19 for row in matrix["covariance_matrix"]), "matrix not square")
    for i, row in enumerate(matrix["covariance_matrix"]):
        require(row[i] > 0.0, f"nonpositive diagonal at {i}")
        for j, value in enumerate(row):
            require(abs(value - matrix["covariance_matrix"][j][i]) <= 1e-20, "matrix not symmetric")
    require(matrix["diagnostics"]["has_BCT_internal_correlations"] is True, "BCT correlations missing")
    require(matrix["diagnostics"]["has_Higgs_internal_correlations"] is True, "Higgs correlations missing")
    require(matrix["diagnostics"]["has_numeric_cross_block_covariance_values"] is False, "cross-block values overclaimed")
    require(matrix["diagnostics"]["nonzero_cross_block_entries_upper_triangle"] == 0, "cross-block nonzeros present")
    require(matrix["accepted_as_numeric_interim_block_covariance"] is True, "interim matrix not accepted")
    require(matrix["accepted_as_full_cross_block_covariance"] is False, "full cross-block covariance overclaimed")
    require(matrix["accepted_as_full_profile_likelihood"] is False, "full profile overclaimed")

    require(gate["numeric_interim_block_covariance_values_closed"] is True, "numeric interim gate not closed")
    require(gate["numeric_cross_block_covariance_values_closed"] is False, "numeric cross-block overclosed")
    require(gate["full_covariance_profile_likelihood_closed"] is False, "full profile gate overclosed")
    require(len(gate["remaining_cross_block_value_requirements"]) == 4, "remaining cross-block requirement count changed")
    require(gate["closure_claimed"] is False, "gate overclosed")

    require(rtheta["Rtheta_coefficient_values_closed"] is False, "Rtheta coefficients overclosed")
    require(rtheta["selected_Rtheta_source_rows_closed"] is False, "Rtheta source rows overclosed")
    require(rtheta["accepted_Rtheta_source_row_count"] == 0, "Rtheta row count mismatch")
    require(rtheta["closure_claimed"] is False, "Rtheta gate overclosed")

    for key in [
        "numeric_interim_block_covariance_matrix",
        "BCT_internal_covariance_values_integrated",
        "Higgs_internal_covariance_values_integrated",
        "Rtheta_coefficient_execution_gate_rechecked",
    ]:
        require(cutset["closed_now"][key] is True, f"cutset closed flag missing: {key}")
    for key in [
        "numeric_cross_block_covariance_values",
        "common_scale_convention_map",
        "common_scale_MZ_to_Mt_jacobian",
        "Rtheta_coefficient_values",
        "selected_threshold_response_functional",
        "selected_Rtheta_source_rows",
        "full_covariance_profile_likelihood",
        "true_SM_equivalence",
        "full_no_knob",
    ]:
        require(cutset["still_open"][key] is True, f"cutset open flag missing: {key}")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(cert["row_count"] == 19, "certificate row count mismatch")
    require("row count                              : 19" in note, "note missing row count")
    require("numeric cross-block covariance closed  : false" in note, "note missing cross-block guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
