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
    candidate = load_json("candidate_data/crossrepo_qasu3_payload_value_contract_import.candidate.json")
    certificate = load_json("certificates/crossrepo_qasu3_payload_value_contract_import_certificate.json")
    terminal = load_json("candidate_data/selected_terminalfinitecochain_connectiontablepromotion_or_fulldevalues.candidate.json")
    de_export = load_json("candidate_data/selected_derieszgreenkerneltraceexport_promotion_or_remainingconnectiontables.candidate.json")

    require(candidate["status"] == certificate["status"], "candidate/certificate status mismatch")
    require(candidate["closure_claimed"] is False, "contract import must not claim payload closure")
    require(certificate["actual_qasu3_payload_values_closed"] is False, "payload values were over-promoted")
    require(candidate["target_fitting_used"] is False, "target fitting must remain excluded")
    require(candidate["decision"]["crossrepo_contract_imported"] is True, "crossrepo contract not imported")
    require(candidate["decision"]["actual_qasu3_payload_values_closed"] is False, "candidate overclaims payload closure")
    require(candidate["decision"]["source_object_exports_required"] == 9, "source-object export count changed")
    require(candidate["decision"]["source_object_exports_filled"] == 0, "source-object exports unexpectedly filled")
    require(candidate["decision"]["connection_exports_required"] == 7, "connection export count changed")
    require(candidate["decision"]["connection_exports_filled"] == 4, "connection exports must be 4/7 after D_E/Riesz/Green export promotion")
    require(candidate["decision"]["minimal_root_flags_required"] == 4, "minimal root count changed")
    require(candidate["decision"]["minimal_root_flags_closed"] == 0, "minimal roots unexpectedly closed")
    require(len(candidate["source_object_required_exports"]) == 9, "source-object required export ledger is not 9")
    require(len(candidate["equivalent_connection_required_exports"]) == 7, "connection required export ledger is not 7")
    require(all(value is None for value in candidate["source_object_required_exports"].values()), "source-object export ledger contains promoted values")
    accepted = terminal["closure_decision"]["accepted_rows"]
    require("typed_f_sections" in accepted, "terminal packet does not accept typed_f_sections")
    require("typed_g_sections" in accepted, "terminal packet does not accept typed_g_sections")
    require("g_after_f_zero_exactness_certificate" in accepted, "terminal packet does not accept g_after_f_zero_exactness_certificate")
    require(terminal["closure_decision"]["g_after_f_zero_exact"] is True, "terminal packet does not prove g after f exact")
    require(terminal["closure_decision"]["terminal_finite_cochain_packet_emitted"] is True, "terminal packet not emitted")
    de_rows = de_export["closure_decision"]["accepted_rows"]
    require("BN27_DE_Riesz_Green_kernel_trace_export" in de_rows, "D_E/Riesz/Green export row not accepted")
    require(de_export["closure_decision"]["finite_DE_Riesz_Green_export_row_selected"] is True, "D_E/Riesz/Green row not selected")
    connection_exports = candidate["equivalent_connection_required_exports"]
    for key in [
        "typed_f_sections",
        "typed_g_sections",
        "g_after_f_zero_and_exactness_certificate",
        "BN27_operator_export_to_DE_Riesz_Green_kernel_trace",
    ]:
        require(isinstance(connection_exports[key], dict) and connection_exports[key]["accepted"] is True, f"{key} not promoted in contract")
    for key in [
        "cech_transitions_and_cocycles",
        "selected_HYM_or_projective_connection_coefficients",
        "no_lifted_flags_replay_audit",
    ]:
        require(connection_exports[key] is None, f"{key} should remain open")
    require(all(value is False for value in candidate["minimal_roots"].values()), "minimal root flags contain promoted values")
    require(candidate["known_support_values_to_retain"]["oriented_abs_sector_product"] == 92160000, "oriented product support value changed")
    require(candidate["known_support_values_to_retain"]["oriented_nonzero_positive_rows"] == 16, "oriented positive-row support count changed")
    require(candidate["known_support_values_to_retain"]["u1y_support_candidate_N_alpha1_h_ext"] == 1.0, "U1/Y alpha1 support value changed")
    require(candidate["known_support_values_to_retain"]["u1y_support_candidate_tangent_residual_l2"] == 0.0, "U1/Y tangent residual support changed")
    require(candidate["theorem"]["proved"] is True, "contract import theorem not proved")

    print(
        json.dumps(
            {
                "candidate": "candidate_data/crossrepo_qasu3_payload_value_contract_import.candidate.json",
                "status": candidate["status"],
                "crossrepo_contract_imported": True,
                "actual_qasu3_payload_values_closed": False,
                "source_object_exports": "0/9",
                "connection_exports": "4/7",
                "accepted_connection_exports": [
                    "typed_f_sections",
                    "typed_g_sections",
                    "g_after_f_zero_exactness_certificate",
                    "BN27_operator_export_to_DE_Riesz_Green_kernel_trace",
                ],
                "minimal_root_flags": "0/4",
                "support_values_retained": [
                    "log(92160000)",
                    "16 oriented positive rows",
                    "N_alpha1(h_ext)=1",
                ],
            },
            indent=2,
        )
    )
    print("cross-repo Qa/SU3 payload value contract import audit passed")


if __name__ == "__main__":
    main()
