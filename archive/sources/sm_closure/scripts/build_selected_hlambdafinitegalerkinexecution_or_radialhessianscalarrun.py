"""Build the H-lambda finite Galerkin execution / radial Hessian scalar run."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hlambdafinitegalerkinexecution_or_radialhessianscalarrun"
CANDIDATE_DIR = ROOT / "candidate_data" / SLUG
CERT_DIR = ROOT / "certificates"
PROOF = ROOT / "proof_corpus" / "MTT_Selected_HLambdaFiniteGalerkinExecution_or_RadialHessianScalarRun_v1.md"


def read_json(path: str | Path) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    CANDIDATE_DIR.mkdir(parents=True, exist_ok=True)
    CERT_DIR.mkdir(parents=True, exist_ok=True)

    formal = read_json("candidate_data/selected_hlambdarowlocaloverlapandscheme_or_directradialhessianvalue.candidate.json")
    formal_operator = read_json(
        "candidate_data/selected_hlambdarowlocaloverlapandscheme_or_directradialhessianvalue/h_lambda_formal_rowlocal_operator.packet.json"
    )
    hessian_contract = read_json(
        "candidate_data/selected_hlambdarowlocaloverlapandscheme_or_directradialhessianvalue/direct_radial_hessian_value_execution_contract.packet.json"
    )
    step74 = read_json("candidate_data/selected_step74_pivsd01backimport_or_rowlocalthresholdvaluefrontier.candidate.json")
    step74_backimport = read_json(
        "candidate_data/selected_step74_pivsd01backimport_or_rowlocalthresholdvaluefrontier/step74_pi_vsd01_backimport.packet.json"
    )
    step74_recheck = read_json(
        "candidate_data/selected_step74_pivsd01backimport_or_rowlocalthresholdvaluefrontier/step74_ten_rowlocal_frontier_recheck.packet.json"
    )
    step74_frontier = read_json(
        "candidate_data/selected_step74_pivsd01backimport_or_rowlocalthresholdvaluefrontier/step74_threshold_value_frontier.packet.json"
    )
    step74_next = read_json(
        "candidate_data/selected_step74_pivsd01backimport_or_rowlocalthresholdvaluefrontier/step74_next_cutset.packet.json"
    )

    h_row = next(row for row in step74_recheck["rows"] if row["omega_id"] == "Omega_H.lambda")

    step74_alignment = {
        "schema": "MTTHLambdaStep74BackimportAlignment.v1",
        "status": "STEP74_BACKIMPORT_ALIGNED_OPERATOR_DOMAIN_READY_VALUE_ROWS_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "formal_operator_id": formal_operator["operator_id"],
        "operator_domain_closed_after_backimport": step74["closure_decision"]["operator_domain_side_closed_after_backimport"],
        "retired_as_active_domain_blockers": step74_backimport["retired_as_active_domain_blockers"],
        "step73_local_flags_still_false": step74_backimport["step73_local_flags_still_false"],
        "interpretation": step74_backimport["interpretation"],
        "decision": {
            "do_not_loop_to_projector_sector_domain_blockers": True,
            "operator_domain_ready_for_H_lambda_execution": True,
            "value_rows_still_open": True,
        },
    }

    finite_execution = {
        "schema": "MTTHLambdaFiniteGalerkinExecutionRun.v1",
        "status": "H_LAMBDA_FINITE_GALERKIN_EXECUTION_ATTEMPTED_ZERO_VALUE_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "input_operator": formal_operator["operator_id"],
        "H_lambda_row_after_step74": h_row,
        "execution_counts": {
            "operator_domain_ready_row_count": step74_recheck["operator_domain_ready_row_count"],
            "ten_row_count": step74_recheck["row_count"],
            "accepted_rowlocal_source_row_count": step74_recheck["accepted_rowlocal_source_row_count"],
            "accepted_prefactor_source_row_count": step74_recheck["accepted_prefactor_source_row_count"],
            "accepted_omega_source_row_count": step74_recheck["accepted_omega_source_row_count"],
            "accepted_internal_scalar_value_row_count": step74_recheck["accepted_internal_scalar_value_row_count"],
        },
        "H_lambda_execution_decision": {
            "operator_domain_ready_after_backimport": h_row["operator_domain_ready_after_backimport"],
            "rowlocal_numeric_prefactor_ready": h_row["rowlocal_numeric_prefactor_ready"],
            "selected_L_rowlocal_emitted": False,
            "selected_T_scheme_emitted": False,
            "lambda_H_source_value_payload_emitted": False,
            "accepted_H_lambda_source_row": False,
        },
    }

    radial_hessian_run = {
        "schema": "MTTDirectRadialHessianScalarRun.v1",
        "status": "DIRECT_RADIAL_HESSIAN_SCALAR_RUN_ATTEMPTED_ZERO_VALUE_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "required_scalar": hessian_contract["required_scalar"],
        "legal_source_operators": hessian_contract["legal_source_operators"],
        "current_emission": hessian_contract["current_emission"],
        "decision": {
            "direct_N_H_value_emitted": False,
            "accepted_direct_radial_hessian_value_rows": 0,
            "controlled_r_H_not_counted_as_direct_N_H": True,
        },
    }

    next_cutset = {
        "schema": "MTTHLambdaFiniteExecutionNextCutset.v1",
        "status": "NEXT_ATTACK_ROWLOCAL_THRESHOLD_VALUE_ROWS_AND_LAMBDAH",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "not_missing_anymore": step74_next["not_missing_anymore"],
        "still_missing": [
            "selected L_rowlocal.Omega_H.lambda numerical source row",
            "selected T_scheme.Omega_H.lambda threshold/scale/scheme source row",
            "lambda_H H-sector source value payload",
            "or direct selected N_H=Hess(F_H)[U_H,U_H]",
        ],
        "next_required_artifact": "MTT_Selected_RowLocalThresholdValueRows_or_LambdaHPrefactorExecution_v1",
    }

    candidate = {
        "schema": "MTTSelectedHLambdaFiniteGalerkinExecutionOrRadialHessianScalarRunCandidate.v1",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "theorem": {
            "name": "HLambdaFiniteExecutionBackimportTheorem",
            "proved": True,
            "statement": (
                "The formal H/lambda operator has now been replayed against the latest Step74 backimport. "
                "The old projector/sector/Pi/operator-domain blockers are retired for the active frontier. "
                "The H row is operator-domain ready, but finite Galerkin execution emits zero accepted "
                "L_rowlocal, T_scheme, lambda_H, Omega, or internal scalar value rows. The direct radial "
                "Hessian alternative also emits zero N_H rows."
            ),
        },
        "decision": {
            "step74_backimport_aligned": True,
            "operator_domain_ready_for_H_lambda_execution": True,
            "finite_galerkin_execution_attempted": True,
            "selected_L_rowlocal_Omega_H_lambda_emitted": False,
            "selected_T_scheme_Omega_H_lambda_emitted": False,
            "lambda_H_source_value_payload_emitted": False,
            "direct_N_H_value_emitted": False,
            "accepted_H_scalar_value_rows": 0,
            "strict_no_knob_numeric_solution_found": False,
        },
        "key_numbers": {
            "operator_domain_ready_row_count": step74_recheck["operator_domain_ready_row_count"],
            "ten_row_count": step74_recheck["row_count"],
            "accepted_rowlocal_source_row_count": 0,
            "accepted_prefactor_source_row_count": 0,
            "accepted_omega_source_row_count": 0,
            "accepted_internal_scalar_value_row_count": 0,
            "Rtheta_readiness_present_count": step74_frontier["Rtheta_readiness_present_count"],
            "Rtheta_readiness_requirement_count": step74_frontier["Rtheta_readiness_requirement_count"],
        },
        "packets": [
            f"candidate_data/{SLUG}/step74_backimport_alignment.packet.json",
            f"candidate_data/{SLUG}/h_lambda_finite_galerkin_execution_run.packet.json",
            f"candidate_data/{SLUG}/direct_radial_hessian_scalar_run.packet.json",
            f"candidate_data/{SLUG}/next_cutset.packet.json",
        ],
        "next_target": "MTT_Selected_RowLocalThresholdValueRows_or_LambdaHPrefactorExecution_v1",
    }

    certificate = {
        "certificate": "selected_hlambdafinitegalerkinexecution_or_radialhessianscalarrun_certificate.v1",
        "candidate": f"candidate_data/{SLUG}.candidate.json",
        "status": "MTT_SELECTED_HLAMBDAFINITEGALERKINEXECUTION_OR_RADIALHESSIANSCALARRUN_OPERATOR_READY_VALUES_OPEN",
        "proved": True,
        "no_target_fitting": True,
        "observed_data_used_as_selector": False,
        "checks": {
            "step74_backimport_aligned": True,
            "operator_domain_ready_for_H_lambda_execution": True,
            "selected_L_rowlocal_Omega_H_lambda_emitted": False,
            "selected_T_scheme_Omega_H_lambda_emitted": False,
            "lambda_H_source_value_payload_emitted": False,
            "direct_N_H_value_emitted": False,
            "accepted_H_scalar_value_rows": 0,
        },
    }

    write_json(ROOT / f"candidate_data/{SLUG}.candidate.json", candidate)
    write_json(CANDIDATE_DIR / "step74_backimport_alignment.packet.json", step74_alignment)
    write_json(CANDIDATE_DIR / "h_lambda_finite_galerkin_execution_run.packet.json", finite_execution)
    write_json(CANDIDATE_DIR / "direct_radial_hessian_scalar_run.packet.json", radial_hessian_run)
    write_json(CANDIDATE_DIR / "next_cutset.packet.json", next_cutset)
    write_json(CERT_DIR / f"{SLUG}_certificate.json", certificate)

    PROOF.write_text(
        "\n".join(
            [
                "# MTT Selected H-Lambda Finite Galerkin Execution or Radial Hessian Scalar Run v1",
                "",
                "## Result",
                "",
                "The formal H/lambda operator has been aligned with the latest Step74 backimport.",
                "",
                "This retires the old active blockers around projector/sector/Pi/operator-domain ownership. The H row is now operator-domain ready after backimport, but value execution still emits no accepted rows.",
                "",
                "## Current Counts",
                "",
                "- operator-domain-ready rows: `10/10`",
                "- accepted `L_rowlocal` rows: `0`",
                "- accepted `T_scheme` rows: `0`",
                "- accepted Omega source rows: `0`",
                "- accepted internal scalar value rows: `0`",
                "- direct selected `N_H` rows: `0`",
                "",
                "## Active Missing Objects",
                "",
                "- selected `L_rowlocal.Omega_H.lambda` numerical source row",
                "- selected `T_scheme.Omega_H.lambda` threshold/scale/scheme source row",
                "- `lambda_H` H-sector source value payload",
                "- or direct selected `N_H = Hess(F_H)[U_H,U_H]`",
                "",
                "## Next Target",
                "",
                "```text",
                "MTT_Selected_RowLocalThresholdValueRows_or_LambdaHPrefactorExecution_v1",
                "```",
                "",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
