from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> None:
    candidate = load_json("candidate_data/selected_rthetathresholdresponsevectoremitter_or_officiallikelihoodworkspace.candidate.json")
    cert = load_json("certificates/selected_rthetathresholdresponsevectoremitter_or_officiallikelihoodworkspace_certificate.json")
    factor = load_json("certificates/selected_rthetarowownerformulavalueemitter_or_officiallikelihoodworkspace_certificate.json")
    workorder = load_json("candidate_data/selected_internalthresholdresponsefunctionalvaluerows_or_externalsourceimportdecision/source_selected_threshold_functional_execution_workorder.packet.json")
    row_ledger = load_json("candidate_data/selected_internalthresholdresponsefunctionalvaluerows_or_externalsourceimportdecision/ten_row_internal_external_source_decision_ledger.packet.json")
    gate = load_json("candidate_data/selected_internalthresholdresponsefunctionalvaluerows_or_externalsourceimportdecision/internal_threshold_response_value_row_gate.packet.json")
    step74 = load_json("certificates/selected_step74_pivsd01backimport_or_rowlocalthresholdvaluefrontier_certificate.json")
    rowlocal = load_json("certificates/selected_rowlocalthresholdvaluerows_or_lambdahprefactorexecution_certificate.json")
    quadrature = load_json("certificates/selected_rowlocalhymoverlapquadraturefunctional_or_thresholdschemesourcetheorem_certificate.json")
    scheme = load_json("certificates/selected_thresholdschemevaluerows_or_sourceselecteduniversalanchorexecution_certificate.json")

    require(candidate["status"] == cert["status"], "candidate/certificate status mismatch")
    require(candidate["closure_claimed"] is False, "candidate overclaims closure")
    require(cert["closure_claimed"] is False, "certificate overclaims closure")
    require(candidate["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require(cert["target_fitting_used"] is False, "target fitting changed")
    require(cert["observed_data_used_as_selector"] is False, "observed selector changed")

    require(factor["four_missing_clauses_factorization_closed"] is True, "previous factorization not closed")
    require(factor["accepted_emitter_count"] == 0, "previous factorization overaccepts emitter")
    require(workorder["functional_contract"]["row_formula"] == "Omega_i = D_fin[class(i)] * L_rowlocal_i * T_scheme_i * exp(-2*pi*n_i)", "row formula changed")
    require(workorder["functional_contract"]["charged_rows"] == 9, "charged row count changed")
    require(workorder["functional_contract"]["higgs_rows"] == 1, "H row count changed")
    require(row_ledger["row_count"] == 10, "row ledger count changed")
    require(row_ledger["admitted_external_replay_row_count"] == 10, "external replay count changed")
    require(row_ledger["internal_selected_value_row_count"] == 0, "row ledger overaccepts internal rows")
    require(row_ledger["forbidden_target_fit_row_count"] == 10, "forbidden target-fit count changed")
    require(gate["accepted_internal_scalar_value_row_count"] == 0, "gate overaccepts scalar rows")
    require(gate["selected_threshold_response_functional_instantiated"] is False, "gate overinstantiates threshold response")
    require(step74["selected_L_rowlocal_rows_emitted"] is False, "Step74 overemits L rows")
    require(step74["selected_T_scheme_rows_emitted"] is False, "Step74 overemits T rows")
    require(step74["strict_omega_acceptance_closed"] is False, "Step74 overcloses Omega acceptance")
    require(rowlocal["accepted_rowlocal_source_row_count"] == 0, "rowlocal overaccepts rows")
    require(rowlocal["strict_omega_acceptance_closed"] is False, "rowlocal overcloses Omega acceptance")
    require(quadrature["accepted_L_rowlocal_source_row_count"] == 0, "quadrature overaccepts L rows")
    require(quadrature["accepted_T_scheme_source_row_count"] == 0, "quadrature overaccepts T rows")
    require(scheme["accepted_threshold_scheme_value_row_count"] == 0, "scheme overaccepts T rows")
    require(scheme["accepted_lambda_H_value_row"] is False, "scheme overaccepts lambda_H")

    contract = candidate["vector_emitter_contract"]
    require(contract["factorization_closed"] is True, "vector factorization not closed")
    require(contract["emitter_symbol"] == "E_Rtheta", "emitter symbol changed")
    require(contract["row_count"] == 10, "contract row count changed")
    require(contract["charged_rows"] == 9, "contract charged count changed")
    require(contract["higgs_rows"] == 1, "contract H count changed")
    require(contract["current_accepted_vector_emitter_count"] == 0, "contract overaccepts emitter")
    require(contract["current_accepted_omega_source_row_count"] == 0, "contract overaccepts omega rows")
    for field in ["selected_L_rowlocal_i", "selected_T_scheme_i", "strict_Omega_acceptance_i", "selected_charged_threshold_value_row_i"]:
        require(field in contract["open_uniform_subfields"], f"open field missing: {field}")
    require(contract["open_H_specific_subfield"] == "selected_lambda_H_payload_row", "H-specific open field changed")

    summary = candidate["row_decision_summary"]
    require(summary["row_count"] == 10, "summary row count changed")
    require(summary["admitted_external_replay_row_count"] == 10, "summary external replay count changed")
    require(summary["internal_selected_value_row_count"] == 0, "summary overaccepts internal rows")
    require(summary["all_rows_have_D_fin_and_theta_weight"] is True, "D/theta support lost")
    require(summary["all_rows_missing_L_rowlocal"] is True, "L missing guard changed")
    require(summary["all_rows_missing_T_scheme"] is True, "T missing guard changed")
    require(summary["all_rows_missing_strict_Omega_acceptance"] is True, "Omega missing guard changed")
    require(summary["H_row_missing_lambda_payload"] is True, "H lambda missing guard changed")
    require(summary["external_replay_rows_count_as_internal_source_rows"] is False, "external rows promoted")

    decision = candidate["decision"]
    require(decision["vector_emitter_factorization_closed"] is True, "decision did not close vector factorization")
    require(decision["route_A_official_workspace_closed"] is False, "decision overcloses official route")
    require(decision["route_B_vector_emitter_closed"] is False, "decision overcloses vector route")
    require(decision["remaining_payload_count"] == 2, "decision payload count changed")
    require(cert["next_required_artifact"] == decision["preferred_next_artifact"], "next artifact mismatch")

    for key in [
        "vector_emitter_factorization_closed",
        "all_rows_have_D_fin_and_theta_weight",
        "all_rows_missing_L_rowlocal",
        "all_rows_missing_T_scheme",
        "all_rows_missing_strict_Omega_acceptance",
        "H_row_missing_lambda_payload",
    ]:
        require(cert[key] is True, f"certificate lost true field: {key}")
    for key in [
        "admitted_external_replay_promoted_to_internal_rows",
        "accepted_full_likelihood_function_or_workspace_closed",
        "route_A_official_workspace_closed",
        "route_B_vector_emitter_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(cert[key] is False, f"certificate overcloses: {key}")
    require(cert["accepted_vector_emitter_count"] == 0, "certificate overaccepts emitter")
    require(cert["accepted_omega_source_row_count"] == 0, "certificate overaccepts omega rows")
    require(cert["accepted_internal_scalar_value_row_count"] == 0, "certificate overaccepts scalar rows")

    print(
        json.dumps(
            {
                "candidate": cert["candidate"],
                "status": cert["status"],
                "vector_emitter_factorization_closed": cert["vector_emitter_factorization_closed"],
                "row_count": cert["row_count"],
                "accepted_vector_emitter_count": cert["accepted_vector_emitter_count"],
                "next_required_artifact": cert["next_required_artifact"],
            },
            indent=2,
        )
    )
    print("selected Rtheta threshold-response vector emitter audit passed")


if __name__ == "__main__":
    main()
