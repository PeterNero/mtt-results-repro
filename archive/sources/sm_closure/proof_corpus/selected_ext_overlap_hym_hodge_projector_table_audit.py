"""Audit the selected eta_00 overlap/Hodge/projector table."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "candidate_data" / "selected_ext_overlap_hym_hodge_projector_table.candidate.json"
CERT = ROOT / "certificates" / "selected_ext_overlap_hym_hodge_projector_table_certificate.json"
PROOF = ROOT / "proof_corpus" / "MTT_Selected_Ext_Overlap_HYM_Hodge_Projector_Table_v1.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    proof = PROOF.read_text(encoding="utf-8")

    require(
        data["status"] == "MTT_SELECTED_EXT_OVERLAP_HODGE_PROJECTOR_TABLE_BUILT_NONLINEAR_HYM_CORRECTION_OPEN",
        "unexpected status",
    )
    require(data["closure_claimed"] is False, "must not claim full closure")
    require(data["target_fitting_used"] is False, "must not use target fitting")
    trans = data["transition_overlap_table"]
    require(trans["closed"] is True, "transition table should close")
    require(trans["generator_factor_formulas"]["g2"] == "exp(2*pi - 4*pi*i*z1)", "wrong g2 factor")
    require(trans["generator_factor_formulas"]["g4"] == "exp(-4*pi + 8*pi*i*z2)", "wrong g4 factor")
    require(trans["generator_factor_formulas"]["g5"] == "1", "shared circle g5 must be trivial")
    require(trans["generator_factor_formulas"]["g6"] == "1", "shared circle g6 must be trivial")
    harmonic = data["global_Dolbeault_harmonic_representative"]
    require(harmonic["closed_at_row_level"] is True, "harmonic row should close")
    require(harmonic["barpartial_eta"] == "0", "barpartial closure missing")
    require(harmonic["partition_of_unity_needed"] is False, "partition should not be required for AH equivariant row")
    hodge = data["Hodge_Lambda_table"]
    require(hodge["closed_for_eta_row"] is True, "Hodge row should close")
    require(hodge["pointwise_norm_of_dbar_z2"] == 1, "wrong dbar norm")
    require(hodge["L2_norm_of_unit_eta_00"] == 1, "unit row should have L2 norm one")
    projector = data["gauge_projector_table"]
    require(projector["closed_for_eta_row"] is True, "projector should close")
    require(projector["matrix_on_basis_eta00_plus_complement"] == [[1.0, 0.0], [0.0, 0.0]], "wrong projector")
    hym = data["HYM_correction_status"]
    require(hym["row_level_harmonic_seed_closed"] is True, "row seed should close")
    require(hym["nonlinear_non_split_HYM_metric_correction_closed"] is False, "HYM correction must remain open")
    readiness = data["newton_readiness"]
    require(readiness["transition_overlap_table_closed"] is True, "readiness transition flag wrong")
    require(readiness["nonlinear_HYM_connection_correction_closed"] is False, "nonlinear HYM must block")
    require(readiness["ready"] is False, "Newton must remain blocked")
    require(cert["newton_ready"] is False, "certificate must keep Newton blocked")
    require("This does not solve the nonlinear HYM connection" in proof, "proof must state HYM guardrail")
    require("MTT_Selected_Nonlinear_HYM_Correction_Coefficient_Solve_v1" in proof, "proof must state next artifact")

    print("PASS selected Ext overlap/Hodge/projector table audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
