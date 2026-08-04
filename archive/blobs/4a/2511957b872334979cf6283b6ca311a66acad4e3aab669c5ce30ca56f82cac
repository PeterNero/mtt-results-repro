"""Audit the first selected HYM adjoint-Galerkin coefficient solve attempt."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "candidate_data" / "selected_hym_adjoint_galerkin_first_coefficient_solve.candidate.json"
CERT = ROOT / "certificates" / "selected_hym_adjoint_galerkin_first_coefficient_solve_certificate.json"
PROOF = ROOT / "proof_corpus" / "MTT_Selected_HYM_AdjointGalerkin_FirstCoefficientSolve_v1.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    proof = PROOF.read_text(encoding="utf-8")

    require(
        data["status"] == "MTT_SELECTED_HYM_ADJOINT_GALERKIN_FIRST_COEFFICIENT_SOLVE_ATTEMPTED_DIFFERENTIAL_TABLES_OPEN",
        "unexpected status",
    )
    require(data["closure_claimed"] is False, "must not claim closure")
    require(data["target_fitting_used"] is False, "must not use target fitting")
    require(data["algebraic_adjoint_packet"]["emitted"] is True, "adjoint packet not emitted")
    require(data["algebraic_adjoint_packet"]["continuous_parameters_added"] == 0, "must add no knobs")
    require(len(data["algebraic_adjoint_packet"]["ad_matrices_on_End0_basis"]) == 3, "expected three adjoint matrices")
    manifest = data["coefficient_unknown_manifest"]
    require(manifest["basis_dimension_from_current_BN_support"] == 27, "expected 27-mode support")
    require(manifest["Hermitian_metric_endomorphism_coefficients"] == 81, "wrong Hermitian unknown count")
    require(manifest["connection_one_form_coefficients"] == 486, "wrong connection unknown count")
    require(manifest["total_first_newton_unknown_slots_if_connection_form_used"] == 567, "wrong total unknown count")
    require(manifest["selected_coefficients_emitted"] is False, "must not emit coefficients")
    require(data["first_coefficient_solve_attempt"]["attempted"] is True, "solve attempt missing")
    require(data["first_coefficient_solve_attempt"]["closed"] is False, "solve must remain open")
    require(data["what_closes_now"]["cohomology_vector_not_misused_as_connection_coefficients"] is True, "Ext guardrail missing")
    require(data["what_remains_open"]["selected_local_differential_product_hodge_tables"] is True, "differential tables must remain open")
    require(
        data["next_required_artifact"] == "MTT_Selected_End0_Basis_Differential_Table_or_BN_Identification_v1",
        "wrong next artifact",
    )
    require(cert["first_coefficient_solve_closed"] is False, "certificate must keep solve open")
    require(cert["selected_coefficients_emitted"] is False, "certificate must not emit coefficients")
    require("The 8-slot Cech cohomology vector is not a connection coefficient vector" in proof, "proof must preserve Ext guardrail")
    require("27 * 3 * 6 = 486" in proof, "proof must record unknown count")

    print("PASS selected HYM adjoint-Galerkin first coefficient solve audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
