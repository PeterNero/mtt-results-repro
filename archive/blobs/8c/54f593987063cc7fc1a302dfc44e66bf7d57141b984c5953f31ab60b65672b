"""Audit Step 13 physical action-kernel field audit ledger."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step13_physicalactionkernelfields_or_independentrowsourceids"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PLAN_POSITION = PACKET_DIR / "step13_plan_position.packet.json"
ACTION_AUDIT = PACKET_DIR / "step13_action_kernel_field_audit.packet.json"
CONDITIONAL_BRIDGE = PACKET_DIR / "step13_conditional_principle_bridge.packet.json"
ROW_SOURCE_AUDIT = PACKET_DIR / "step13_independent_row_source_id_audit.packet.json"
NEXT_WORKORDER = PACKET_DIR / "step13_to_step14_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step13_PhysicalActionKernelFields_or_IndependentRowSourceIDs_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_STEP13_PHYSICALACTIONKERNELFIELDS_OR_INDEPENDENTROWSOURCEIDS_"
    "CLOSED_FIELD_AUDIT_LOCAL_PRINCIPLE_DERIVATION_OPEN"
)
NEXT = "MTT_Selected_Step14_SelectedWeylVariationActionPrincipleDerivation_or_HonestRowSourceExecution_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    plan = load(PLAN_POSITION)
    action = load(ACTION_AUDIT)
    bridge = load(CONDITIONAL_BRIDGE)
    rows = load(ROW_SOURCE_AUDIT)
    next_workorder = load(NEXT_WORKORDER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["step13_contract_closure_claimed"] is True, "contract closure missing")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(plan["active_step"] == 13, "plan active step mismatch")
    require(plan["remaining_steps_after_13"]["step14"].startswith("derive selected"), "step14 missing")

    require(action["admissible_differentiated_variations_fixed"] is True, "variation clause not retained")
    require(action["RZ_RX_operator_discovery_closed"] is True, "RZ/RX discovery reopened")
    require(action["physical_action_equals_c1_defect_functional"] is False, "action equality overclosed")
    require(action["physical_boundary_source_terms_vanish"] is False, "boundary overclosed")
    require(action["same_source_rz_rx_bselected_emitted"] is False, "same-source emission overclosed")
    require(action["validator_returncode"] == 1, "route A validator should reject")
    require(
        action["missing_action_kernel_fields"]
        == [
            "physical_action_equals_c1_defect_functional",
            "physical_boundary_source_terms_vanish",
            "same_source_rz_rx_bselected_emitted",
        ],
        "missing action fields mismatch",
    )
    require(action["free_axiom_patch_used"] is False, "free axiom patch used")
    require(action["residual_projector_replay_used_as_source"] is False, "residual replay used")

    require(bridge["accepted_here"] is False, "local principle accepted as free patch")
    require(bridge["must_not_be_used_as_free_patch"] is True, "free-patch guard missing")
    for key in [
        "selected_variation_functional",
        "same_source_hessian",
        "sector_functor",
        "independence_certificate",
        "pre_residual_phase_shift_operator_source",
        "same_source_hessian_b_selected_rows",
        "sector_rows_physical_source_promotion",
    ]:
        require(bridge["would_close_if_derived_from_selected_MTT_geometry"][key] is True, f"bridge witness missing {key}")

    require(rows["selected_variation_space_source_emitted"] is True, "variation-space source missing")
    require(rows["selected_measure_pairing_source_emitted"] is False, "measure overemitted")
    require(rows["selected_quadrature_rule_emitted"] is False, "quadrature overemitted")
    require(rows["primitive_row_kernel_source_count"] == 72, "primitive count mismatch")
    require(rows["primitive_row_kernel_sources_emitted_count"] == 0, "primitive sources overemitted")
    require(rows["hessian_b_source_count"] == 2, "hessian count mismatch")
    require(rows["hessian_b_sources_emitted_count"] == 0, "hessian sources overemitted")
    require(rows["sector_assembly_source_count"] == 36, "sector count mismatch")
    require(rows["sector_assembly_sources_emitted_count"] == 0, "sector sources overemitted")
    require(rows["new_independent_row_source_ids_emitted"] is False, "row source IDs overemitted")

    require(next_workorder["completed_step"] == 13, "workorder completed step mismatch")
    require(next_workorder["next_step"] == 14, "workorder next step mismatch")
    require(next_workorder["closure_claimed"] is False, "workorder closure overclaimed")
    require(
        next_workorder["step14_must_not_repeat"]["conditional_local_principle_as_free_patch"] is True,
        "anti-loop guard missing",
    )

    decision = data["closure_decision"]
    require(decision["step13_closed_for_plan_contract"] is True, "step13 contract not closed")
    for key in [
        "operator_discovery_reopened",
        "admissible_variation_space_reopened",
        "physical_action_equals_c1_defect_functional_proved_now",
        "physical_boundary_source_terms_vanish_proved_now",
        "same_source_rz_rx_bselected_emitted_now",
        "selected_weyl_variation_action_principle_accepted_now",
        "independent_row_source_ids_emitted_now",
        "SelectedFiniteC1SourceIdentityTheorem_proved",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclaimed: {key}")

    for phrase in [
        "Step 13   : current action-kernel field audit and route split",
        "physical action = C1 defect functional        false",
        "conditional local principle isolated          true",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
