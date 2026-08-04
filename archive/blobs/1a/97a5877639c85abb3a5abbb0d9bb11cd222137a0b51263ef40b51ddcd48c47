"""Audit first value-source row promotion or honest Galerkin primitive-row bridge."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_firstvaluesourcerowpromotion_or_honestgalerkinprimitiverow"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
BACKIMPORT = PACKET_DIR / "primitive_exactness_backimport.packet.json"
RECONCILE = PACKET_DIR / "first_value_row_promotion_reconciliation.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_primitive_backimport.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FirstValueSourceRowPromotion_or_HonestGalerkinPrimitiveRow_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_FIRSTVALUESOURCEROWPROMOTION_OR_HONESTGALERKINPRIMITIVEROW_"
    "BUILT_EXACT_PRIMITIVE_BACKIMPORT_ASSEMBLY_OPEN"
)
NEXT = "MTT_Selected_VSD01_AllPrimitiveRowsAssemblyMap_or_PhysicalPhiFinC1ActionSource_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    backimport = load(BACKIMPORT)
    reconcile = load(RECONCILE)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    for key in [
        "closure_claimed",
        "unpatched_theorem_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(data[key] is False, f"candidate guardrail overclaimed: {key}")

    require(backimport["target_obligation"] == "VSD-01-selected-overlap-value-kernel", "wrong target")
    require(backimport["target_value_source_row"] == "VSD-01.phase.I_plus_Z.u_e.first_dynamic_row", "wrong value row")
    require(backimport["primitive_row_id"] == "u:phase:r0c0", "wrong primitive row")
    require(backimport["primitive_exact_value"]["exact"] == "4/3", "wrong exact primitive value")
    require(backimport["computed_independent_complex_entry_value"] is True, "primitive value not computed")
    require(backimport["exactness_certificate_emitted"] is True, "exactness not emitted")
    require(backimport["primitive_exactness_certificate"]["roundoff_bound"] == 0.0, "not exact")
    require(backimport["provenance_independent_of_residual_projector_replay"] is False, "provenance overclaimed")
    require(backimport["physical_PhiFinC1_action_source_closed"] is False, "physical action source overclosed")
    require(backimport["closure_claimed"] is False, "backimport overclaimed")

    checks = reconcile["direct_identity_checks"]
    for key in [
        "primitive_value_equals_u_correction_dY_00",
        "primitive_value_equals_e_correction_dY_00",
        "primitive_value_equals_u_first_hermitian_response_H1_00",
        "primitive_value_equals_e_first_hermitian_response_H1_00",
    ]:
        require(checks[key] is False, f"primitive/dynamic identity overaccepted: {key}")

    gate = reconcile["assembly_gate"]
    require(gate["all_72_row_exactness_available"] is True, "all-row exactness not imported")
    require(gate["formal_110_row_replay_integrated"] is True, "formal replay missing")
    require(gate["formal_A_b_deltaTheta_replay_integrated"] is True, "formal A/b replay missing")
    require(gate["same_source_identity_normal_form_built"] is True, "same-source normal form missing")
    for key in [
        "selected_dynamic_transfer_identity_promoted",
        "selected_b_selected_promoted",
        "physical_PhiFinC1_action_source_closed",
        "provenance_independent_of_residual_projector_replay",
    ]:
        require(gate[key] is False, f"assembly gate overclosed: {key}")
    require(reconcile["accepted_as_selected_dynamic_value_source_row_now"] is False, "dynamic row overaccepted")
    require(reconcile["closure_claimed"] is False, "reconciliation overclaimed")

    closes = cutset["closed_now"]
    for key in [
        "first_primitive_seed_value_exact",
        "first_primitive_seed_exactness_certificate",
        "first_value_row_backimport_reconciliation",
        "direct_primitive_to_dynamic_identity_rejected",
        "no_observed_data_selector_guard_preserved",
    ]:
        require(closes[key] is True, f"close flag missing: {key}")
    remains = cutset["still_open"]
    for key in [
        "selected_dynamic_overlap_threshold_tensor_T_selected",
        "assembly_map_from_primitive_rows_to_dynamic_value_source_row",
        "same_branch_linking_tensor_rows_to_versioned_value_packet",
        "physical_PhiFinC1_action_source_or_independent_provenance",
        "selected_A_b_deltaTheta_promotion",
        "accepted_as_selected_dynamic_value_source_row",
    ]:
        require(remains[key] is True, f"remaining blocker missing: {key}")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(cutset["closure_claimed"] is False, "cutset overclaimed")

    decision = data["closure_decision"]
    require(decision["primitive_exactness_backimported"] is True, "primitive exactness not backimported")
    require(decision["first_value_row_promoted_to_selected_dynamic_source"] is False, "value row overpromoted")
    require(decision["VSD_01_closed"] is False, "VSD-01 overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "SM equivalence overclosed")
    require(decision["full_no_knob_closed"] is False, "no-knob overclosed")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("not a selected dynamic value-source row yet" in note, "note missing guardrail")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
