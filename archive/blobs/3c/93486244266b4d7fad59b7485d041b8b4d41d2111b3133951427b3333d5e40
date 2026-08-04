"""Audit the H-lambda finite Galerkin execution / radial Hessian scalar run."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hlambdafinitegalerkinexecution_or_radialhessianscalarrun"


def read_json(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    candidate = read_json(f"candidate_data/{SLUG}.candidate.json")
    alignment = read_json(f"candidate_data/{SLUG}/step74_backimport_alignment.packet.json")
    execution = read_json(f"candidate_data/{SLUG}/h_lambda_finite_galerkin_execution_run.packet.json")
    hessian = read_json(f"candidate_data/{SLUG}/direct_radial_hessian_scalar_run.packet.json")
    next_cutset = read_json(f"candidate_data/{SLUG}/next_cutset.packet.json")
    cert = read_json(f"certificates/{SLUG}_certificate.json")

    require(candidate["theorem"]["proved"] is True, "theorem proved")
    require(candidate["decision"]["step74_backimport_aligned"] is True, "Step74 alignment")
    require(candidate["decision"]["operator_domain_ready_for_H_lambda_execution"] is True, "operator domain")
    require(candidate["decision"]["finite_galerkin_execution_attempted"] is True, "execution attempted")
    require(candidate["decision"]["selected_L_rowlocal_Omega_H_lambda_emitted"] is False, "L emitted")
    require(candidate["decision"]["selected_T_scheme_Omega_H_lambda_emitted"] is False, "T emitted")
    require(candidate["decision"]["lambda_H_source_value_payload_emitted"] is False, "lambda payload emitted")
    require(candidate["decision"]["direct_N_H_value_emitted"] is False, "N_H emitted")
    require(candidate["decision"]["accepted_H_scalar_value_rows"] == 0, "accepted H scalar rows")
    require(candidate["next_target"] == "MTT_Selected_RowLocalThresholdValueRows_or_LambdaHPrefactorExecution_v1", "next target")

    require(alignment["decision"]["do_not_loop_to_projector_sector_domain_blockers"] is True, "loop guard")
    require(alignment["decision"]["operator_domain_ready_for_H_lambda_execution"] is True, "alignment domain")
    require(alignment["decision"]["value_rows_still_open"] is True, "value rows open")
    require(alignment["operator_domain_closed_after_backimport"] is True, "Step74 domain not closed")
    require(alignment["retired_as_active_domain_blockers"]["Pi_Rtheta"] is True, "Pi retired")
    require(alignment["retired_as_active_domain_blockers"]["stationary_sector_transfer"] is True, "sector transfer retired")

    h_row = execution["H_lambda_row_after_step74"]
    require(h_row["omega_id"] == "Omega_H.lambda", "H row omega")
    require(h_row["operator_domain_ready_after_backimport"] is True, "H row domain")
    require(h_row["rowlocal_numeric_prefactor_ready"] is False, "H row numeric prefactor")
    require("lambda_H H-sector source value payload" in h_row["missing_value_rows"], "lambda payload missing row")
    require(execution["execution_counts"]["operator_domain_ready_row_count"] == 10, "ready rows")
    require(execution["execution_counts"]["ten_row_count"] == 10, "ten rows")
    require(execution["execution_counts"]["accepted_rowlocal_source_row_count"] == 0, "L row count")
    require(execution["execution_counts"]["accepted_prefactor_source_row_count"] == 0, "prefactor count")
    require(execution["execution_counts"]["accepted_omega_source_row_count"] == 0, "Omega count")
    require(execution["H_lambda_execution_decision"]["accepted_H_lambda_source_row"] is False, "H source accepted")

    require(hessian["decision"]["direct_N_H_value_emitted"] is False, "direct N_H")
    require(hessian["decision"]["accepted_direct_radial_hessian_value_rows"] == 0, "direct N_H rows")
    require(hessian["decision"]["controlled_r_H_not_counted_as_direct_N_H"] is True, "controlled guard")

    require(next_cutset["next_required_artifact"] == "MTT_Selected_RowLocalThresholdValueRows_or_LambdaHPrefactorExecution_v1", "cutset target")
    require("selected L_rowlocal.Omega_H.lambda numerical source row" in next_cutset["still_missing"], "missing L")
    require("selected T_scheme.Omega_H.lambda threshold/scale/scheme source row" in next_cutset["still_missing"], "missing T")
    require("or direct selected N_H=Hess(F_H)[U_H,U_H]" in next_cutset["still_missing"], "missing N_H")

    require(cert["proved"] is True, "cert proved")
    require(cert["checks"]["step74_backimport_aligned"] is True, "cert Step74")
    require(cert["checks"]["operator_domain_ready_for_H_lambda_execution"] is True, "cert domain")
    require(cert["checks"]["selected_L_rowlocal_Omega_H_lambda_emitted"] is False, "cert L")
    require(cert["checks"]["selected_T_scheme_Omega_H_lambda_emitted"] is False, "cert T")
    require(cert["checks"]["lambda_H_source_value_payload_emitted"] is False, "cert lambda")
    require(cert["checks"]["direct_N_H_value_emitted"] is False, "cert N_H")
    require(cert["checks"]["accepted_H_scalar_value_rows"] == 0, "cert rows")

    print("selected_hlambdafinitegalerkinexecution_or_radialhessianscalarrun audit: PASS")


if __name__ == "__main__":
    main()
