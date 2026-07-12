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
    candidate = load_json("candidate_data/selected_internalvrthetavaluepayloadoperator_or_officialfullprofileworkspace.candidate.json")
    cert = load_json("certificates/selected_internalvrthetavaluepayloadoperator_or_officialfullprofileworkspace_certificate.json")
    transport = load_json("certificates/selected_omegavaluepayloadtransport_or_officiallikelihoodworkspace_certificate.json")
    step69 = load_json("candidate_data/selected_step69_hymthresholdprefactorrows_or_omegascalarexecution/step69_prefactor_solution_formula_rows.packet.json")
    omega = load_json("certificates/selected_strictomegaacceptancebridge_or_hlambdavectorrowbridge_certificate.json")
    profile = load_json("candidate_data/selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution/profile_likelihood_execution_summary.packet.json")

    require(candidate["status"] == cert["status"], "candidate/certificate status mismatch")
    require(candidate["closure_claimed"] is False, "candidate overclaims closure")
    require(cert["closure_claimed"] is False, "certificate overclaims closure")
    require(candidate["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")
    require(candidate["target_fitting_used"] is False, "target fitting used")
    require(candidate["observed_data_used_as_selector"] is False, "observed selector used")

    require(transport["transport_acceptance_contract_closed"] is True, "previous transport contract not closed")
    require(transport["route_B_selected_internal_V_Rtheta_value_payload_operator_closed"] is False, "previous transport overcloses V_Rtheta")
    require(omega["combined_K_to_Omega_formula_row_count"] == 10, "Omega formula row count changed")
    require(omega["accepted_algebraic_omega_source_formula_row_count"] == 10, "Omega algebraic source count changed")
    require(step69["formula_row_count"] == 10, "Step69 formula row count changed")
    require(step69["accepted_formula_skeleton_row_count"] == 10, "Step69 skeleton count changed")
    require(step69["accepted_internal_scalar_value_row_count"] == 0, "Step69 overaccepts scalar rows")

    attempt = candidate["identity_transport_attempt"]
    step69_ids = [row["omega_id"] for row in step69["formula_rows"]]
    step69_labels = [row["scalar_label"] for row in step69["formula_rows"]]
    require(attempt["attempted_slot_count"] == 10, "attempted slot count changed")
    require(attempt["attempted_slots"] == step69_ids, "attempted slots do not match Step69 ids")
    require(attempt["mapped_scalar_labels"] == step69_labels, "mapped scalar labels do not match Step69")
    require(attempt["uniform_pass_clause_count"] == 6, "pass clause count changed")
    require(attempt["uniform_fail_clause_count"] == 3, "fail clause count changed")
    require(attempt["accepted_identity_transport_rows"] == 0, "identity transport overaccepted")
    require("selected_physical_projection_normalization_operator_N_phys" in attempt["uniform_fail_clauses"], "missing N_phys failure")

    decision = candidate["decision"]
    require(decision["identity_transport_attempt_closed"] is True, "identity attempt not closed")
    require(decision["identity_transport_accepted_as_physical_value_operator"] is False, "identity overaccepted")
    require(decision["selected_internal_V_Rtheta_value_payload_operator_closed"] is False, "V_Rtheta overclosed")
    require(decision["accepted_profile_value_payload_row_count"] == 0, "profile values overaccepted")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "scalar values overaccepted")
    require(decision["accepted_true_equivalence_precision_rows"] == 0, "true precision overclaimed")
    require(profile["profile_summary"]["accepted_as_full_covariance_profile"] is False, "profile overclaims full covariance")

    require(cert["identity_transport_attempt_closed"] is True, "certificate lost identity attempt")
    require(cert["identity_transport_accepted_as_physical_value_operator"] is False, "certificate overaccepts identity")
    require(cert["attempted_slot_count"] == 10, "certificate slot count changed")
    require(cert["uniform_pass_clause_count"] == 6, "certificate pass count changed")
    require(cert["uniform_fail_clause_count"] == 3, "certificate fail count changed")
    require(cert["selected_physical_projection_normalization_operator_N_phys_closed"] is False, "certificate overcloses N_phys")
    require(cert["selected_internal_V_Rtheta_value_payload_operator_closed"] is False, "certificate overcloses V_Rtheta")
    require(cert["accepted_internal_scalar_value_row_count"] == 0, "certificate overaccepts scalar rows")
    require(cert["next_required_artifact"] == decision["preferred_next_artifact"], "next artifact mismatch")

    for key in [
        "algebraic_formula_rows_promoted_to_physical_values",
        "identity_transport_promoted_to_value_payload",
        "diagonal_profile_promoted_to_full_covariance",
        "official_likelihood_workspace_imported",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(cert[key] is False, f"certificate overcloses: {key}")

    print(
        json.dumps(
            {
                "candidate": cert["candidate"],
                "status": cert["status"],
                "identity_transport_attempt_closed": True,
                "attempted_slot_count": 10,
                "accepted_identity_transport_rows": 0,
                "selected_N_phys_closed": False,
                "accepted_internal_scalar_value_row_count": 0,
                "next_required_artifact": cert["next_required_artifact"],
            },
            indent=2,
        )
    )
    print("selected internal V_Rtheta value-payload operator / official full-profile workspace audit passed")


if __name__ == "__main__":
    main()
