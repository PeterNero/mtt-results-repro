"""Audit Step 24 dynamic-gate reconciliation / value-layer cutset."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step24_dynamicgate_reconciliation_or_valuelayercutset"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
RECON_PACKET = PACKET_DIR / "step24_superseded_dynamic_gate_reconciliation.packet.json"
CLOSED_PACKET = PACKET_DIR / "step24_selected_dynamic_bhessian_closure.packet.json"
NEXT_CUTSET = PACKET_DIR / "step24_value_layer_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step24_DynamicGateReconciliation_or_ValueLayerCutset_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP24_DYNAMIC_GATE_RECONCILIATION_OR_VALUELAYERCUTSET_BUILT_DYNAMIC_BHESSIAN_GATE_CLOSED_VALUE_FUNCTIONAL_OPEN"
NEXT = "MTT_Selected_ThresholdResponseFunctionalRowEmission_or_ExternalSourceRowImport_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    recon = load(RECON_PACKET)
    closed = load(CLOSED_PACKET)
    cutset = load(NEXT_CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaimed")

    require(recon["older_step23_workorder_is_currently_closed"] is True, "Step23 workorder not closed")
    require("unpatched_source_stack" in recon["superseding_artifacts"], "source stack evidence missing")
    require("same_source_dynamic_matter_overlap_packet" in recon["superseding_artifacts"], "dynamic packet evidence missing")

    source_stack = closed["source_stack"]
    require(source_stack["closure_claimed"] is True, "source stack not closed")
    require(source_stack["psm_validator_returncode"] == 0, "PSM validator failed")
    require(source_stack["physical_validator_returncode"] == 0, "physical validator failed")
    require(source_stack["psm_source_fields_all_selected"] is True, "PSM fields not all selected")
    require(source_stack["physical_action_route_A_validates"] is True, "physical route A not valid")
    require(source_stack["no_extra_boundary_or_source_term"] is True, "boundary/source term not eliminated")
    require(source_stack["same_source_b_selected_emission"] is True, "same-source b missing")
    promoted = source_stack["promoted_objects"]
    for key in ["A_selected", "b_selected", "deltaTheta_C1", "SelectedFiniteC1SourceIdentityTheorem"]:
        require(promoted[key] is True, f"source stack did not promote {key}")

    dynamic = closed["dynamic_matter_overlap"]
    require(dynamic["closure_claimed"] is True, "dynamic packet not closed")
    require(dynamic["selected_dynamic_overlap_tensor_promoted"] is True, "dynamic overlap not promoted")
    require(dynamic["primitive_C1_contractions_selected_emitted_first_response_layer"] is True, "primitive layer not emitted")
    require(dynamic["selected_A_selected_b_selected_preserved"] is True, "A/b preservation missing")
    require(dynamic["selected_values_selected_by_MTT"] is True, "selected values not selected by MTT")
    require(dynamic["same_source_fields_all_selected"] is True, "matter fields not selected")
    require(dynamic["packet_promotes_A_selected"] is True, "matter packet does not promote A")
    require(dynamic["packet_promotes_b_selected"] is True, "matter packet does not promote b")
    require(dynamic["matter_validator_returncode"] == 0, "matter validator failed")

    vsd01 = closed["vsd01_assembly"]
    require(vsd01["source_assembly_subgate_closed"] is True, "VSD01 source subgate not closed")
    require(vsd01["dynamic_overlap_subgate_closed"] is True, "VSD01 dynamic subgate not closed")
    require(vsd01["full_vsd01_obligation_closed"] is False, "VSD01 overclosed")
    require(vsd01["source_stack_closed"] is True, "VSD01 did not import source stack")
    require(vsd01["dynamic_matter_overlap_packet_closed"] is True, "VSD01 did not import dynamic packet")
    rows = vsd01["row_evidence"]
    require(rows["all_72_primitive_rows_exact"] is True, "72 primitive rows not exact")
    require(rows["formal_110_rows_executed"] is True, "formal 110 rows not executed")
    require(rows["formal_110_row_counts"]["total_rows"] == 110, "wrong formal row count")
    require(rows["formal_110_row_counts"]["hessian_source_rows"] == 2, "hessian/source rows missing")
    require(rows["formal_110_max_abs_error"] < 1e-12, "formal replay error too large")

    closed_items = closed["step24_closed_items"]
    for key in [
        "selected_source_to_C1_transfer_map_emitted",
        "selected_dynamic_overlap_tensor_or_transfer_functor",
        "selected_primitive_C1_contractions_first_response_layer",
        "selected_b_selected_promoted",
        "selected_Hessian_source_normalization_promoted",
        "selected_A_selected_promoted",
        "selected_deltaTheta_C1_promoted",
    ]:
        require(closed_items[key] is True, f"Step24 closure missing: {key}")

    decision = data["closure_decision"]
    require(decision["step23_dynamic_workorder_superseded_and_closed"] is True, "candidate did not close Step23 workorder")
    require(decision["selected_dynamic_overlap_tensor_or_transfer_functor"] is True, "candidate dynamic overlap missing")
    require(decision["selected_b_selected_promoted"] is True, "candidate b missing")
    require(decision["selected_Hessian_source_normalization_promoted"] is True, "candidate Hessian/source missing")
    require(decision["accepted_value_functional_rows_closed"] is False, "value functional overclosed")
    require(decision["accepted_Yukawa_magnitudes_closed"] is False, "Yukawa overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(decision["full_no_knob_closed"] is False, "no-knob overclosed")

    require(cutset["active_frontier_now"] == "selected value-functional rows, not source-promotion or Galerkin replay", "wrong active frontier")
    require(cutset["current_value_frontier"]["source_layer_closed"] is True, "value frontier source layer not closed")
    require(cutset["current_value_frontier"]["value_layer_accepted_source_rows"] == 0, "accepted rows unexpectedly present")
    require(cutset["current_value_frontier"]["accepted_true_value_source_row_emitted"] is False, "first value row overemitted")
    require(cutset["closure_claimed"] is False, "cutset overclaimed")
    require(cutset["next_required_artifact"] == NEXT, "cutset next mismatch")

    for phrase in [
        "selected dynamic overlap tensor / transfer functor          closed",
        "selected threshold response functional                       open",
        "not full true-SM closure",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
