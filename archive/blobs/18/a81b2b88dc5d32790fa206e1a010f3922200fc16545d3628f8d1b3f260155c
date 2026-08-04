"""Audit Step 16 post-source value-closure reconciliation."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step16_postsourcevalueclosure_reconciliation"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SOURCE_BACKIMPORT = PACKET_DIR / "step16_step14_source_backimport.packet.json"
VALUE_STACK = PACKET_DIR / "step16_postsource_value_stack_reconciliation.packet.json"
SCALAR_GATE = PACKET_DIR / "step16_internal_scalar_gate_after_stronger_packets.packet.json"
NEXT_WORKORDER = PACKET_DIR / "step16_to_step17_fulls2_value_execution_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step16_PostSourceValueClosure_Reconciliation_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP16_POSTSOURCEVALUECLOSURE_RECONCILIATION_CLOSED_SOURCE_PI_THRESHOLD_PROFILE_TO_FULLS2_VALUE_FRONTIER"
NEXT = "MTT_Selected_Step17_FullS2OperatorPayload_or_InternalRThetaScalarRows_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    source_backimport = load(SOURCE_BACKIMPORT)
    value_stack = load(VALUE_STACK)
    scalar_gate = load(SCALAR_GATE)
    next_workorder = load(NEXT_WORKORDER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(source_backimport["old_unpatched_source_identity_closed"] is False, "old branch unexpectedly closed")
    require(source_backimport["source_identity_theorem_promoted"] is True, "Step 14 source identity not promoted")
    require(source_backimport["source_stack_closed"] is True, "Step 14 source stack not closed")
    promoted = source_backimport["promoted_objects"]
    for key in [
        "SelectedFiniteC1SourceIdentityTheorem",
        "PhysicalPhiFinC1ActionSource",
        "A_selected",
        "b_selected",
        "deltaTheta_C1",
    ]:
        require(promoted[key] is True, f"promoted object missing: {key}")
        require(source_backimport["scalar_gate_may_not_reopen"][key] is True, f"anti-reopen missing: {key}")

    require(value_stack["postsource_alpha1_and_static_matter"]["alpha1_driver_closed_at_postsource_tier"] is True, "alpha1 not closed")
    require(value_stack["postsource_alpha1_and_static_matter"]["static_matter_readout_closed"] is True, "static matter not closed")
    require(value_stack["dynamic_first_response"]["same_source_dynamic_matter_overlap_packet_closed"] is True, "dynamic matter not closed")
    require(value_stack["dynamic_first_response"]["selected_dynamic_QaSU3_first_response_layer_closed"] is True, "dynamic QaSU3 not closed")
    require(value_stack["dynamic_first_response"]["accepted_Yukawa_magnitudes_closed"] is False, "Yukawa magnitudes overclosed")
    require(value_stack["rtheta_source_domain"]["selected_Rtheta_scalar_value_functional_source_domain_closed"] is True, "Rtheta source domain not closed")
    require(value_stack["rtheta_source_domain"]["ten_scalar_row_codomain_aligned"] is True, "ten scalar rows not aligned")
    require(value_stack["post_pi_external_replay"]["threshold_matching_source_rows_closed_at_admitted_external_tier"] is True, "threshold rows not admitted")
    require(value_stack["post_pi_external_replay"]["mass_scheme_conversion_source_rows_closed_at_admitted_external_tier"] is True, "mass rows not admitted")
    require(value_stack["post_pi_external_replay"]["accepted_diagonal_profile_theorem_closed"] is True, "diagonal profile not closed")
    require(value_stack["post_pi_external_replay"]["external_import_lane_closed_at_admitted_replay_tier"] is True, "external import lane not closed")
    require(value_stack["post_pi_external_replay"]["Rtheta_readiness_8_of_9"] is True, "Rtheta readiness not 8/9")
    require(value_stack["external_replay_is_not_internal_selection"] is True, "external replay boundary missing")

    closed_before = scalar_gate["closed_before_gate"]
    for key in [
        "source_identity_stack",
        "postsource_alpha1_static_matter",
        "dynamic_first_response_matter_QaSU3",
        "Rtheta_source_domain_and_ten_row_codomain",
        "post_pi_threshold_mass_scheme_external_replay",
        "accepted_diagonal_profile_external_replay",
        "qualitative_second_order_lambda_orbit",
    ]:
        require(closed_before[key] is True, f"closed-before-gate flag missing: {key}")

    require(scalar_gate["direct_scalar_emission_attempted"] is True, "direct scalar attempt not recorded")
    require(scalar_gate["accepted_internal_scalar_row_count"] == 0, "internal scalar rows over-emitted")
    require(scalar_gate["fullS2_payload_ready_in_old_attempt"] is False, "old fullS2 ready unexpectedly")
    require(scalar_gate["transported_sector_payload_imported"] is True, "transport payload not imported")
    require(scalar_gate["higher_response_dotD_alpha1_payload_closed"] is True, "higher alpha1 payload not closed")
    require(scalar_gate["full_S2_value_execution_closed"] is False, "full S2 overclosed")
    require(scalar_gate["selected_operator_payload_closed"] is False, "operator payload overclosed")
    require(scalar_gate["diagonal_End0_operator_payload_closed"] is True, "diagonal End0 not closed")
    require(scalar_gate["rhoE_DE_fullS2_execution_closed"] is False, "rhoE/DE overclosed")
    require(scalar_gate["no_knob_kernel_typed"] is True, "no-knob kernel not typed")
    require(scalar_gate["selected_universal_parameter_count"] == 0, "universal parameter count changed")
    require(scalar_gate["forbidden_reopened_blockers"]["unpatched_PSM_C1_02_source_identity"] is False, "source identity reopened")

    decision = data["closure_decision"]
    require(decision["step16_reconciliation_closed"] is True, "Step 16 reconciliation not closed")
    require(decision["unpatched_source_identity_blocker_retired"] is True, "source identity blocker not retired")
    require(decision["Rtheta_readiness_8_of_9"] is True, "readiness not imported")
    require(decision["accepted_internal_scalar_row_count"] == 0, "internal scalar rows over-emitted")
    require(decision["internal_scalar_row_execution_closed"] is False, "internal scalar execution overclosed")
    require(decision["selected_fullS2_operator_payload_closed"] is False, "fullS2 overclosed")
    require(decision["candidate_specific_universal_source_anchor_closed"] is False, "anchor overclosed")
    require(decision["full_no_knob_closed"] is False, "no-knob overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")

    require(next_workorder["next_step"] == 17, "next step mismatch")
    require(next_workorder["must_not_reopen"]["SelectedFiniteC1SourceIdentityTheorem"] is True, "must-not-reopen missing")
    require(next_workorder["success_criterion"]["observed_values_not_used_as_selectors"] is True, "selector guard missing")

    for phrase in [
        "SelectedFiniteC1SourceIdentityTheorem      promoted by Step 14/15",
        "unpatched_SelectedFiniteC1SourceIdentityLemma` is retired",
        "selected full-S2 operator payload",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
