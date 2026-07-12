"""Audit CONST-HIGGS-01 H1 shared-metrology primitive test packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h1_shared_metrology_primitive_test"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
SHARED_METROLOGY = BASE / "shared_metrology_import.packet.json"
SOURCE_SCAN = BASE / "higgs_source_scan.packet.json"
PROJECTOR_STATUS = BASE / "projector_and_27mode_support_status.packet.json"
PARITY_REPLAY = BASE / "downstream_higgs_replay_boundary.packet.json"
THRESHOLD_GATE = BASE / "quartic_threshold_gate.packet.json"
BOUNDARY = BASE / "h1_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H1_SharedMetrologyPrimitiveTest_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H1_SHARED_METROLOGY_PRIMITIVE_TEST_BUILT"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def clean(packet: dict[str, object], name: str) -> None:
    require(packet["observed_data_used_as_selector"] is False, f"{name} observed selector")
    require(packet["target_fitting_used"] is False, f"{name} target fitting")
    require(packet["closure_claimed"] is False, f"{name} closure overclaim")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    require(computed["status"] == STATUS, "builder status mismatch")

    candidate = load(DATA)
    shared_metrology = load(SHARED_METROLOGY)
    source_scan = load(SOURCE_SCAN)
    projector_status = load(PROJECTOR_STATUS)
    parity_replay = load(PARITY_REPLAY)
    threshold_gate = load(THRESHOLD_GATE)
    boundary = load(BOUNDARY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("shared_metrology", shared_metrology),
        ("source_scan", source_scan),
        ("projector_status", projector_status),
        ("parity_replay", parity_replay),
        ("threshold_gate", threshold_gate),
        ("boundary", boundary),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["G4_one_metrology_primitive_reused"] is True, "G4 reuse")
    require(candidate["new_Higgs_specific_parameters"] == 0, "Higgs-specific parameters")
    require(candidate["block_family_Higgs_projector_support_closed"] is True, "block support")
    require(candidate["diagnostic_27mode_eta_within_budget"] is True, "eta diagnostic")
    require(candidate["selected_PhiFin_provenance_closed"] is False, "Phi_fin overclosed")
    require(candidate["selected_Higgs_quartic_threshold_kernel_emitted"] is False, "kernel overemitted")
    require(candidate["Higgs_quartic_numeric_value_derived"] is False, "lambda overderived")
    require(candidate["downstream_Higgs_replay_nonselector_boundary_closed"] is True, "downstream boundary")
    require(candidate["strict_no_knob_Higgs_closure"] is False, "strict overclosed")

    require(shared_metrology["status"] == "G4_ONE_METROLOGY_PRIMITIVE_IMPORTED_FOR_HIGGS_TEST", "metrology status")
    require(shared_metrology["imported_from_G4"]["one_universal_metrology_primitive_tier_defined"] is True, "G4 primitive")
    require(shared_metrology["imported_from_G4"]["selected_metrology_primitive_value"] is False, "primitive value")
    require(shared_metrology["parameter_budget"]["new_Higgs_specific_parameters"] == 0, "metrology Higgs params")
    require(shared_metrology["parameter_budget"]["new_universal_primitives"] == 0, "new universal primitive")
    require(shared_metrology["parameter_budget"]["imported_universal_metrology_primitives"] == 1, "imported primitive")

    evidence = source_scan["source_side_evidence"]
    require(evidence["block_projector_layer_closed"] is True, "block layer")
    require(evidence["block_vs_spectral_distinction_closed"] is True, "block/spectral distinction")
    require(evidence["routec_operator_shape_support_imported"] is True, "Route-C shape")
    require(evidence["hessian_kernel_derivation_interface_built"] is True, "Hessian interface")
    require(evidence["actual_27_mode_matrix_entries_emitted"] is True, "27-mode emitted")
    require(evidence["same_27_mode_basis_available"] is True, "27-mode basis")
    open_ = source_scan["source_side_open"]
    require(open_["coherent_spectral_projector_retention"] is True, "coherent spectral open")
    require(open_["selected_DE_Riesz_Green_dotD_values"] is True, "selected DE open")
    require(open_["functorial_finite_Phi_fin_trace_proved"] is True, "Phi_fin open")
    require(open_["existing_27_mode_matrices_identified_as_selected_compression"] is True, "compression open")
    require(source_scan["superset_strategy"]["locked_target"] == "SelectedHiggsQuarticThresholdKernel, not measured lambda_H or Higgs mass.", "locked target")

    require(projector_status["status"] == "PROJECTOR_SUPPORT_CLOSED_27MODE_DIAGNOSTIC_WITHIN_BUDGET_SELECTED_SOURCE_OPEN", "projector status")
    require(projector_status["higgs_27mode_formula"]["formula_theorem_proved"] is True, "formula theorem")
    require(projector_status["higgs_27mode_formula"]["H_sector_formula_check"]["uses_higgs_zero_cluster_shift"] is True, "H shift")
    require(projector_status["higgs_27mode_formula"]["H_sector_formula_check"]["selected_source_verified"] is False, "H source oververified")
    require(projector_status["higgs_27mode_formula"]["selected_trace_attempt_proved"] is False, "trace overproved")
    require(projector_status["eta_budget"]["eta_if_provenance_supplied"] == 1.0, "eta")
    require(projector_status["eta_budget"]["threshold"] == 2.1932454224643014, "threshold")
    require(projector_status["eta_budget"]["passes_threshold"] is True, "passes threshold")
    require(projector_status["eta_budget"]["selected_eta_emitted_now"] is False, "eta overemitted")

    replay_evidence = parity_replay["downstream_replay_evidence"]
    require(replay_evidence["common_scale_transport_kernel_specified"] is True, "common scale")
    require(replay_evidence["lambda_H_MZ_value_remains_open"] is True, "lambda MZ open")
    require(replay_evidence["external_literature_rg_benchmark_values_filled"] is True, "external RG")
    require(replay_evidence["SM_parity_Higgs_replay_rows_closed"] is True, "SM-parity rows")
    require(replay_evidence["accepted_profile_import"] is False, "accepted profile overclosed")
    require(parity_replay["classification"]["usable_for_H1"] == "comparison and target-interface discipline only", "downstream use")

    verdict = threshold_gate["current_verdict"]
    require(verdict["projector_support_sufficient_to_continue"] is True, "continue")
    require(verdict["diagnostic_eta_budget_promising"] is True, "eta promising")
    require(verdict["strict_selected_Higgs_kernel_emitted"] is False, "kernel emitted")
    require(verdict["Higgs_quartic_numeric_value_derived"] is False, "lambda derived")
    require(verdict["one_metrology_primitive_reuse_consistent_so_far"] is True, "primitive reuse")
    require(threshold_gate["best_next_artifact"] == "MTT_CONST_HIGGS_01_H2_SelectedHiggsProjectorAndQuarticKernelSourcePacket_v1", "H2")

    closed = boundary["closed_or_decided_now"]
    require(closed["G4_one_metrology_primitive_imported_without_new_Higgs_knob"] is True, "boundary primitive")
    require(closed["Higgs_projector_source_scan_completed"] is True, "boundary scan")
    require(closed["block_family_Higgs_projector_support_imported"] is True, "boundary block")
    require(closed["downstream_Higgs_replay_classified_as_non_selector"] is True, "boundary replay")
    still_open = boundary["still_open"]
    require(still_open["strict_selected_Higgs_projector_values"] is True, "projector open")
    require(still_open["selected_PhiFin_finite_trace_morphism"] is True, "morphism open")
    require(still_open["selected_Higgs_quartic_threshold_kernel"] is True, "kernel open")
    require(still_open["Higgs_quartic_numeric_value"] is True, "numeric open")
    require("not using SM-parity Higgs replay rows as source proof" in boundary["anti_cycle_delta_from_G4"]["not_repeated"], "anti-cycle")

    require(next_work["primary"]["label"] == "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H2-SELECTED-HIGGS-PROJECTOR-AND-QUARTIC-KERNEL-SOURCE-PACKET", "primary")
    require(next_work["parallel"]["label"] == "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H2B-FINITE-TRACE-MORPHISM-IDENTIFIES-27MODE", "parallel")

    require(cert["status"] == STATUS, "cert status")
    require(cert["new_Higgs_specific_parameters"] == 0, "cert params")
    require(cert["selected_Higgs_quartic_threshold_kernel_emitted"] is False, "cert kernel")
    require(cert["Higgs_quartic_numeric_value_derived"] is False, "cert numeric")
    require(cert["strict_no_knob_Higgs_closure"] is False, "cert strict")
    require("H1-SHARED-METROLOGY-PRIMITIVE-TEST" in note and "SelectedHiggsQuarticThresholdKernel" in note, "note")

    print("CONST-HIGGS-01 H1 shared-metrology primitive test audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
