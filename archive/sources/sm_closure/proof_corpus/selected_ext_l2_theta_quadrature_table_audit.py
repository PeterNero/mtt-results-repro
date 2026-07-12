"""Audit the selected L2 theta quadrature table for eta_00."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "candidate_data" / "selected_ext_l2_theta_quadrature_table.candidate.json"
CERT = ROOT / "certificates" / "selected_ext_l2_theta_quadrature_table_certificate.json"
PROOF = ROOT / "proof_corpus" / "MTT_Selected_Ext_L2_Theta_Quadrature_Table_v1.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    proof = PROOF.read_text(encoding="utf-8")

    require(
        data["status"] == "MTT_SELECTED_EXT_L2_THETA_QUADRATURE_TABLE_BUILT_OVERLAP_HYM_PROJECTOR_OPEN",
        "unexpected status",
    )
    require(data["closure_claimed"] is False, "must not claim full closure")
    require(data["target_fitting_used"] is False, "must not use target fitting")
    row = data["selected_row"]
    require(row["row_id"] == "eta_00", "wrong row")
    require(row["central_shared_circle_factor"] == 1, "central circle factor must be one")
    require("Serre duality" in row["serre_dual_convention"], "negative degree guardrail missing")
    table = data["eta_00_l2_table"]
    exact = 1.0 / math.sqrt(32.0)
    require(abs(table["unrescaled_norm_square_exact"] - exact) < 1e-14, "wrong eta norm square")
    require(table["unrescaled_norm_square_exact_expression"] == "1/sqrt(32)", "wrong exact expression")
    require(abs(table["unit_L2_rescale_factor_numeric"] - 32.0 ** 0.25) < 1e-14, "wrong rescale")
    require(table["final_mesh_product_error"] < 1e-12, "quadrature did not converge tightly")
    require(data["factor_norms"]["Theta_2_0_E1"]["final_error"] < 1e-12, "degree 2 quadrature weak")
    require(
        data["factor_norms"]["Serre_dual_Eta_minus4_0_E2_via_Theta_4_0"]["final_error"] < 1e-12,
        "degree 4 quadrature weak",
    )
    readiness = data["overlap_and_newton_status"]
    require(readiness["l2_theta_quadrature_closed"] is True, "L2 theta quadrature should close")
    require(readiness["analytic_overlap_trivialization_values_closed"] is False, "overlaps must remain open")
    require(readiness["selected_HYM_metric_connection_correction_closed"] is False, "HYM must remain open")
    require(readiness["newton_ready"] is False, "Newton must remain blocked")
    require(cert["l2_theta_quadrature_closed"] is True, "certificate should close L2 quadrature")
    require(cert["newton_ready"] is False, "certificate must keep Newton blocked")
    require("32^(1/4)" in proof, "proof must state unit rescale")
    require("End0 Newton/Galerkin solve is not yet ready" in proof, "proof must state nonclosure")

    print("PASS selected Ext L2 theta quadrature table audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
