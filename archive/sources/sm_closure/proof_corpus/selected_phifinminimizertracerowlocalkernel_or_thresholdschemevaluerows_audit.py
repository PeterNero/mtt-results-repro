"""Audit selected Phi_fin row-local kernel / threshold-scheme value-row gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_phifinminimizertracerowlocalkernel_or_thresholdschemevaluerows"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SOURCE_DOMAIN_PACKET = PACKET_DIR / "latest_source_domain_import.packet.json"
TRACE_QUOTIENT_PACKET = PACKET_DIR / "phifin_trace_only_rank_quotient_nogo.packet.json"
EXECUTION_GATE_PACKET = PACKET_DIR / "rowlocal_value_execution_gate_after_phifin_import.packet.json"
EIGENPROFILE_PACKET = PACKET_DIR / "eigenprofile_sector_bruteforce_diagnostic.packet.json"
THRESHOLD_SYSTEM_PACKET = PACKET_DIR / "threshold_scheme_value_rows_minimal_system.packet.json"
CUTSET_PACKET = PACKET_DIR / "next_cutset_after_phifin_kernel_gate.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhiFinMinimizerTraceRowLocalKernel_or_ThresholdSchemeValueRows_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_PHIFINMINIMIZERTRACEROWLOCALKERNEL_OR_THRESHOLDSCHEMEVALUEROWS_"
    "BUILT_SOURCE_DOMAIN_CLOSED_TRACE_QUOTIENT_NOGO_VALUES_OPEN"
)
NEXT = "MTT_Selected_ThresholdSchemeValueRows_or_SourceSelectedUniversalAnchorExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str, *, allow_target_fit: bool = False) -> None:
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector violation")
    if allow_target_fit:
        require(packet.get("target_fitting_used") is True, f"{label} diagnostic target-fit flag missing")
    else:
        require(packet.get("target_fitting_used") is False, f"{label} target fitting violation")
    require(packet.get("closure_claimed") is True, f"{label} should close its audit theorem")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    source = load(SOURCE_DOMAIN_PACKET)
    quotient = load(TRACE_QUOTIENT_PACKET)
    execution = load(EXECUTION_GATE_PACKET)
    eigen = load(EIGENPROFILE_PACKET)
    threshold = load(THRESHOLD_SYSTEM_PACKET)
    cutset = load(CUTSET_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("certificate", cert),
        ("source", source),
        ("quotient", quotient),
        ("execution", execution),
        ("threshold", threshold),
        ("cutset", cutset),
    ]:
        guard(packet, label)
    guard(eigen, "eigenprofile diagnostic", allow_target_fit=True)

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "candidate theorem missing")
    require(cert["theorem_proved"] is True, "certificate theorem missing")

    retired = source["retired_by_later_imports"]
    for key in [
        "premise_free_transport_closed_Phi_fin",
        "stationary_projectors_promoted",
        "validator_ready_stationary_rho_s",
        "stationary_sector_transfer_closed",
        "dotD_alpha1_transport_subgate_closed",
        "matter_slot_routing_closed",
        "primitive_C1_overlap_contractions_closed",
        "Pi_Rtheta_closed",
        "coefficient_functional_skeleton_closed",
    ]:
        require(retired[key] is True, f"latest source import failed to retire {key}")
    still = source["still_open_for_numerical_scalar_rows"]
    require(still["selected_threshold_response_functional_instantiated"] is False, "threshold functional overclosed")
    require(still["accepted_coefficient_value_count"] == 0, "coefficient rows overaccepted")
    require(still["accepted_lambda_H_value"] is False, "lambda_H overaccepted")
    require(still["full_no_knob_closed"] is False, "no-knob overclosed")

    require(quotient["theorem"]["proved"] is True, "trace quotient theorem missing")
    require(quotient["trace_equivalence_class_count"] == 2, "trace quotient class count changed")
    require(quotient["typed_total_scalar_rows"] == 10, "scalar row count mismatch")
    require(quotient["typed_charged_functional_rows"] == 9, "charged functional row count mismatch")
    require(quotient["accepted_source_row_count"] == 0, "trace quotient overaccepted source rows")
    require(quotient["selected_value_rows_emitted"] is False, "trace quotient emitted values")

    require(execution["row_count"] == 10, "execution row count mismatch")
    require(execution["charged_row_count"] == 9, "execution charged row count mismatch")
    for key in [
        "accepted_L_rowlocal_kernel_value_count",
        "accepted_T_scheme_value_count",
        "accepted_omega_source_row_count",
        "accepted_internal_scalar_value_row_count",
    ]:
        require(execution[key] == 0, f"execution overaccepted {key}")
    for retired_label in [
        "selected transported stationary projector source",
        "validator-ready stationary rho_s",
        "dotD_alpha1 transport derivative and alpha1 source normalization",
        "static matter-slot routing",
        "primitive C1 overlap / Pi_Rtheta dependency",
    ]:
        require(retired_label in execution["retired_blockers"], f"retired blocker missing {retired_label}")
    for row in execution["execution_rows"]:
        require(row["source_domain_closed"] is True, f"source domain not closed for {row['omega_id']}")
        require(row["stationary_projector_source_closed"] is True, f"projector not closed for {row['omega_id']}")
        require(row["Pi_Rtheta_closed"] is True, f"Pi not closed for {row['omega_id']}")
        require(row["threshold_response_functional_instantiated"] is False, f"threshold overclosed for {row['omega_id']}")
        require(row["emitted_L_rowlocal_kernel_value"] is None, f"L emitted early for {row['omega_id']}")
        require(row["emitted_T_scheme_value"] is None, f"T emitted early for {row['omega_id']}")
        require(row["accepted_as_selected_rowlocal_kernel_value"] is False, f"L row overaccepted {row['omega_id']}")
        require(row["accepted_as_selected_threshold_scheme_value"] is False, f"T row overaccepted {row['omega_id']}")
        require(row["accepted_as_omega_source_row"] is False, f"Omega row overaccepted {row['omega_id']}")
        for phrase in [
            "selected threshold response functional is not instantiated",
            "accepted internal threshold matching and mass-scheme conversion rows are empty",
            "magnitude-bearing projection weights remain distinct from source-normalized unit weights",
        ]:
            require(phrase in row["blocking_reasons"], f"row blocker missing {phrase}")
    h_row = next(row for row in execution["execution_rows"] if row["omega_id"] == "Omega_H.lambda")
    require("lambda_H H-sector value payload is not selected" in h_row["blocking_reasons"], "H blocker missing")

    require(eigen["charged_row_count"] == 9, "eigen diagnostic row count mismatch")
    require(eigen["tested_model_count"] > 0, "eigen diagnostic did not run")
    require(eigen["decision"]["accepted_as_selected_threshold_or_rowlocal_source_rule"] is False, "fit overpromoted")
    require(eigen["best_models"][0]["accepted_as_source_rule"] is False, "best fit overaccepted")
    require(eigen["best_models"][0]["max_multiplicative_error_factor"] > 1.1, "diagnostic suspiciously exact")

    require(threshold["requirement_count"] == 9, "threshold requirement count mismatch")
    require(threshold["present_count"] == 4, "threshold present count mismatch")
    for failure in [
        "same_branch_scale_scheme_loop_convention",
        "threshold_matching_source_rows",
        "mass_scheme_conversion_source_rows",
        "no_knob_value_derivation",
        "full_profile_likelihood_or_accepted_diagonal_theorem",
    ]:
        require(failure in threshold["blocking_failures"], f"threshold failure missing {failure}")
    require(threshold["universal_anchor_policy"]["one_to_three_source_selected_parameters_allowed"] is True, "anchor policy missing")
    require(threshold["universal_anchor_policy"]["ordinary_fit_parameters_allowed"] is False, "ordinary knobs allowed")
    require(threshold["universal_anchor_policy"]["current_selected_value_parameter_count_for_this_gate"] == 0, "anchor overselected")

    for phrase in [
        "selected threshold response functional value rows T_scheme.*",
        "selected magnitude-bearing projection weights or equivalent value functional",
        "lambda_H H-sector selected value row",
        "selected CKM/PMNS/offdiagonal matrix extension",
    ]:
        require(phrase in cutset["still_missing"], f"cutset missing {phrase}")
    for phrase in [
        "treat trace-only Phi_fin conjugacy classes as generation-resolved magnitudes",
        "promote compact target-scored eigenprofile fits as source laws",
        "use 1-3 knobs unless the knob values are source-selected before replay",
    ]:
        require(phrase in cutset["forbidden_routes"], f"forbidden route missing {phrase}")

    decision = data["closure_decision"]
    for key in [
        "latest_source_domain_imported",
        "stale_projector_dotd_pi_blockers_retired",
        "trace_only_rank_quotient_nogo_proved",
        "rowlocal_value_execution_gate_built",
        "eigenprofile_sector_bruteforce_executed",
        "threshold_scheme_minimal_system_built",
    ]:
        require(decision[key] is True, f"decision did not close {key}")
        require(cert[key] is True, f"certificate did not close {key}")
    for key in [
        "accepted_L_rowlocal_kernel_value_count",
        "accepted_T_scheme_value_count",
        "accepted_omega_source_row_count",
        "accepted_internal_scalar_value_row_count",
    ]:
        require(decision[key] == 0, f"decision overaccepted {key}")
        require(cert[key] == 0, f"certificate overaccepted {key}")
    for key in [
        "selected_threshold_response_functional_instantiated",
        "lambda_H_value_row_emitted",
        "strict_omega_acceptance_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
        require(cert[key] is False, f"certificate overclosed {key}")

    for phrase in [
        "trace equivalence classes             : 2",
        "accepted L_rowlocal kernel values     : 0",
        "accepted T_scheme values              : 0",
        "accepted as source rule               : False",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
