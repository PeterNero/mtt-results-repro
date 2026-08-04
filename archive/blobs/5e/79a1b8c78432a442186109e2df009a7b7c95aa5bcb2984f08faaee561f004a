"""Audit precision-transport/covariance rows / final true-SM audit gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_precisiontransportcovariancerows_or_finaltruesmaudit"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
READINESS = PACKET_DIR / "precision_transport_covariance_readiness.packet.json"
COVARIANCE = PACKET_DIR / "full_covariance_target_lock.packet.json"
TRANSPORT = PACKET_DIR / "threshold_rg_observable_transport_subgates.packet.json"
SUPPORT = PACKET_DIR / "already_executed_support_attempts.packet.json"
GATE = PACKET_DIR / "final_true_sm_audit_gate.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PrecisionTransportCovarianceRows_or_FinalTrueSMAudit_v1.md"

STATUS = (
    "MTT_SELECTED_PRECISIONTRANSPORTCOVARIANCEROWS_OR_FINALTRUESMAUDIT_"
    "EASY_WIN_SUBGATES_LOCKED_TRUE_VALUES_OPEN"
)
NEXT_ARTIFACT = "MTT_Selected_AcceptedPrecisionSourceValues_or_FinalTrueSMClosure_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def guard(packet: dict[str, Any], label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    readiness = load(READINESS)
    covariance = load(COVARIANCE)
    transport = load(TRANSPORT)
    support = load(SUPPORT)
    gate = load(GATE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", candidate),
        ("readiness", readiness),
        ("covariance", covariance),
        ("transport", transport),
        ("support", support),
        ("gate", gate),
        ("cert", cert),
    ]:
        guard(packet, label)

    require(candidate["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["theorem"]["name"] == "PrecisionTransportCovarianceRowsOrFinalTrueSMAuditTheorem", "theorem name")
    require(cert["theorem_proved"] is True, "cert theorem")
    require(candidate["next_required_artifact"] == NEXT_ARTIFACT, "candidate next")
    require(gate["next_required_artifact"] == NEXT_ARTIFACT, "gate next")
    require(cert["next_required_artifact"] == NEXT_ARTIFACT, "cert next")

    closed = readiness["easy_win_subgates"]
    expected_closed = [
        "post_PEW_precision_ledger_consumed",
        "independent_local_RG_benchmark_values_filled",
        "local_QFT_observable_functor_interface_built",
        "external_profile_coordinate_count_fixed",
        "full_8x8_covariance_target_shape_fixed",
        "BCT_WZH_cross_covariance_gap_quantified",
        "precision_proxy_inventory_consolidated",
        "eight_slot_operator_manifest_locked",
        "admitted_external_threshold_rows_closed",
        "admitted_external_mass_scheme_rows_closed",
        "accepted_diagonal_profile_theorem_closed_at_replay_tier",
        "final_no_knob_kernel_typed",
        "accepted_profile_import_attempt_executed",
        "profile_row_replacement_payload_candidate_built",
        "diagonal_covariance_surrogate_payload_built",
        "external_correlated_covariance_submatrix_imported",
        "profile_likelihood_import_attempt_executed",
        "partial_precision_value_table_emitted",
        "qasu3_source_slot_layer_closed",
    ]
    require(readiness["easy_win_subgate_count_closed"] == len(expected_closed), "easy-win count")
    for key in expected_closed:
        require(closed[key] is True, f"missing easy win {key}")
    require(readiness["accepted_true_equivalence_precision_rows"] == 0, "accepted true rows overclaimed")
    require(readiness["blocking_true_precision_row_count"] == 8, "blocking row count changed")
    require(readiness["Rtheta_readiness_fraction"] == "8/9", "Rtheta readiness")
    require(readiness["accepted_internal_scalar_row_count"] == 0, "internal scalar overclaimed")
    require(readiness["selected_internal_value_emission_count"] == 0, "internal value overclaimed")
    require(readiness["selected_universal_parameter_count"] == 0, "universal parameter selected")

    require(covariance["status"] == "FULL_8X8_COVARIANCE_TARGET_LOCKED_VALUES_OPEN", "cov status")
    require(covariance["coordinate_count"] == 8, "coordinate count")
    require(covariance["matrix_shape"] == [8, 8], "matrix shape")
    require(covariance["symmetric_unique_entries"] == 36, "symmetric entries")
    require(covariance["strict_full_profile_entries_accepted"] == 0, "profile entries overclaimed")
    require(covariance["surrogate_or_empirical_entries_scaffolded"] == 21, "scaffold entries")
    require(covariance["BCT_WZH_cross_covariance_entries_missing"] == 15, "missing cross entries")
    require(covariance["full_covariance_profile_likelihood_closed"] is False, "cov profile overclaimed")
    require(covariance["published_or_reconstructed_likelihood_required"] is True, "likelihood requirement")

    rg = transport["local_RG_benchmark"]
    require(rg["benchmark_values_filled"] is True, "RG benchmark not filled")
    require(abs(rg["lambda_H_MZ_firstpass"] - 0.1470187677924554) < 1e-15, "lambda_H benchmark")
    require(rg["external_literature_RG_benchmark_values_closed"] is False, "external RG overclaimed")

    qft = transport["local_QFT_functor"]
    require(qft["name"] == "Obs_SM^MTT", "QFT functor name")
    require(qft["signature_declared"] is True, "QFT signature")
    require(qft["actual_correlator_values_filled"] is False, "correlators overclaimed")
    require(qft["local_QFT_observable_functor_values_closed"] is False, "QFT values overclaimed")

    threshold = transport["threshold_mass_scheme_replay"]
    require(threshold["closure_tier"] == "admitted external replay", "threshold tier")
    require(threshold["admitted_external_threshold_row_count"] == 7, "threshold count")
    require(threshold["admitted_external_mass_scheme_row_count"] == 3, "mass scheme count")
    require(threshold["accepted_diagonal_profile_theorem_closed"] is True, "diagonal theorem")
    require(threshold["external_rows_used_as_branch_selector"] is False, "external selector")
    require(threshold["internal_selected_Rtheta_value_row_emitted"] is False, "Rtheta overemitted")

    precision = transport["precision_observable_table"]
    require(precision["proxy_or_scaffold_rows_available"] == 4, "proxy inventory")
    require(precision["accepted_precision_rows_imported_now"] == 0, "precision rows overimported")
    require(precision["accepted_precision_observable_table_closed"] is False, "precision table overclosed")

    qasu3 = transport["qasu3_operator_slots"]
    require(qasu3["required_operator_slot_count"] == 8, "required operator slots")
    require(qasu3["filled_operator_slot_count"] == 0, "operator slots overfilled")
    require(len(qasu3["missing_slots"]) == 8, "missing operator slot list")
    require(qasu3["actual_QaSU3_operator_packet_closed"] is False, "QaSU3 overclosed")

    require(support["status"] == "SUPPORT_AND_ATTEMPT_PACKETS_RECORDED_WITH_VALUE_LAYER_OPEN", "support status")
    require(support["support_attempt_count"] == 11, "support attempt count")
    require(support["support_attempts_with_true_SM_equivalence_closed"] == [], "support overclosed true SM")
    require(support["source_slot_layer_closed_somewhere"] is True, "source slot layer missing")
    require(support["actual_dynamic_operator_payload_closed_somewhere"] is False, "dynamic payload overclosed")
    require(support["accepted_precision_profile_import_closed_somewhere"] is False, "profile import overclosed")
    require(support["profile_likelihood_imported_somewhere"] is False, "profile likelihood overimported")
    by_slug = {record["slug"]: record for record in support["records"]}
    require(
        by_slug["selected_step8_precisionvalueemission_or_actualqasu3operatorpacketclosure"][
            "source_slot_layer_closed"
        ]
        is True,
        "Step8 source slot layer not recorded",
    )
    require(
        by_slug["selected_step8_precisionvalueemission_or_actualqasu3operatorpacketclosure"][
            "operator_source_slots_closed"
        ]
        == 8,
        "Step8 source slot count",
    )

    require(gate["status"] == "FINAL_TRUE_SM_AUDIT_GATE_REDUCED_TO_ACCEPTED_VALUE_SOURCE_ROWS", "gate status")
    require(gate["remaining_hard_blocker_count"] == 8, "hard blocker count")
    require(gate["final_true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(gate["full_no_knob_closed"] is False, "no-knob overclosed")
    require("precision transport/covariance readiness subgates" in gate["not_active_blockers"], "non-blocker missing")
    require(
        "Qa/SU3 source-slot layer, distinct from actual dynamic operator payload values"
        in gate["not_active_blockers"],
        "source-slot non-blocker missing",
    )
    require(gate["already_executed_support_attempt_count"] == 11, "gate support count")
    require(gate["source_slot_layer_closed_somewhere"] is True, "gate source slot layer")
    require(gate["actual_dynamic_operator_payload_closed_somewhere"] is False, "gate dynamic payload overclosed")

    decision = candidate["closure_decision"]
    require(decision["precision_transport_covariance_easy_wins_closed"] is True, "decision easy wins")
    require(decision["easy_win_subgate_count_closed"] == 19, "decision easy-win count")
    require(decision["already_executed_support_attempts_recorded"] is True, "decision support recorded")
    require(decision["already_executed_support_attempt_count"] == 11, "decision support count")
    require(decision["qasu3_source_slot_layer_closed"] is True, "decision source slot")
    require(decision["actual_dynamic_qasu3_operator_payload_closed"] is False, "decision dynamic payload")
    require(decision["accepted_precision_profile_import_closed_somewhere"] is False, "decision profile import")
    require(decision["profile_likelihood_imported_somewhere"] is False, "decision likelihood")
    require(decision["full_8x8_covariance_target_shape_fixed"] is True, "decision covariance shape")
    require(decision["full_covariance_symmetric_unique_entries"] == 36, "decision covariance entries")
    require(decision["BCT_WZH_cross_covariance_entries_missing"] == 15, "decision cross entries")
    require(decision["admitted_external_threshold_row_count"] == 7, "decision threshold")
    require(decision["admitted_external_mass_scheme_row_count"] == 3, "decision mass")
    require(decision["accepted_true_equivalence_precision_rows"] == 0, "decision true rows")
    for key in [
        "accepted_precision_observable_table_closed",
        "actual_QaSU3_operator_packet_closed",
        "full_covariance_profile_likelihood_closed",
        "multi_loop_RG_values_closed",
        "local_QFT_precision_observable_values_closed",
        "strong_CP_problem_solved",
        "full_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"{key} overclosed")

    for phrase in [
        "local RG benchmark values filled                   true",
        "external profile coordinates                       8",
        "missing BCT-WZH cross entries                      15",
        "admitted external threshold rows                   7",
        "already-executed support attempts recorded         11",
        "Qa/SU3 source-slot layer closed                    true",
        "actual dynamic Qa/SU3 payload closed               false",
        "accepted true-equivalence precision rows           0",
        NEXT_ARTIFACT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
