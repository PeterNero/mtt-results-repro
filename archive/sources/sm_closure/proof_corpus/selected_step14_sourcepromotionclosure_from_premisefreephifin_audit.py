"""Audit Step 14/15 source-promotion closure from premise-free Phi_fin replay."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step14_sourcepromotionclosure_from_premisefreephifin"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SOURCE_REPLAY = PACKET_DIR / "step14_validator_replay_import.packet.json"
ANTI_LOOP = PACKET_DIR / "step14_antiloop_source_legality.packet.json"
PROMOTION = PACKET_DIR / "step14_step15_source_identity_promotion.packet.json"
NEXT_WORKORDER = PACKET_DIR / "step14_to_step16_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step14_SourcePromotionClosure_from_PremiseFreePhiFin_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

PHYSICAL_PACKET = ROOT / "candidate_data" / "selected_unpatchedsourcepromotionreplay_or_fullsmclosuregate" / "physical_action_rowkernel_source_replay.packet.json"
ACTION_PACKET = ROOT / "candidate_data" / "selected_unpatchedsourcepromotionreplay_or_fullsmclosuregate" / "action_kernel_theorem_replay.packet.json"
PHYSICAL_VALIDATOR = ROOT / "scripts" / "validate_selected_physicalphifinc1_action_or_independent_rowkernel_source.py"
ACTION_VALIDATOR = ROOT / "scripts" / "validate_selected_phifinc1_preresidual_action_kernel_theorem.py"

STATUS = "MTT_SELECTED_STEP14_SOURCEPROMOTIONCLOSURE_FROM_PREMISEFREEPHIFIN_CLOSED_STEP14_STEP15_SOURCE_IDENTITY_PROMOTED_STEP16_VALUES_OPEN"
NEXT = "MTT_Selected_Step16_PostSourceValueClosure_DotDAlpha1MatterYukawaAudit_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def run_validator(validator: Path, packet: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(validator), str(packet)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    source_replay = load(SOURCE_REPLAY)
    anti_loop = load(ANTI_LOOP)
    promotion = load(PROMOTION)
    next_workorder = load(NEXT_WORKORDER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(run_validator(PHYSICAL_VALIDATOR, PHYSICAL_PACKET).returncode == 0, "physical validator failed live")
    require(run_validator(ACTION_VALIDATOR, ACTION_PACKET).returncode == 0, "action validator failed live")

    for key in [
        "physical_action_rowkernel_source_validator_passes",
        "narrowed_phifinc1_emission_validator_passes",
        "action_kernel_theorem_validator_passes",
        "psm_c1_02_source_promotion_validator_passes",
    ]:
        require(source_replay[key] is True, f"validator flag missing: {key}")

    route_a = source_replay["route_A_physical_action_restriction_fields"]
    for key in [
        "physical_action_restricts_to_finite_weyl_quotient",
        "zero_extra_boundary_or_source_term",
        "phase_R_Z_source_selection",
        "shift_R_X_source_selection",
        "same_source_b_selected_emission",
    ]:
        require(route_a[key] is True, f"Route A field missing: {key}")

    action_fields = source_replay["action_kernel_fields"]
    for key in [
        "physical_action_equals_c1_defect_functional",
        "admissible_differentiated_variations_fixed",
        "physical_boundary_source_terms_vanish",
        "same_source_rz_rx_bselected_emitted",
    ]:
        require(action_fields[key] is True, f"action-kernel field missing: {key}")

    shortcuts = anti_loop["forbidden_shortcuts_used"]
    require(shortcuts["RZ_RX_normal_form_discovery_as_source"] is False, "RZ/RX discovery reused")
    require(shortcuts["conditional_local_principle_as_free_patch"] is False, "local principle used as patch")
    require(shortcuts["exact_72_row_value_replay_as_source"] is False, "72-row replay used as source")
    require(anti_loop["premise_free_route_A_certificate"]["source_row_premise_used"] is False, "source row premise used")
    require(anti_loop["premise_free_phi_fin_restriction_morphism"]["source_row_used_as_premise"] is False, "morphism source row premise used")
    require(anti_loop["raw_27mode_truncation_used_as_closure"] is False, "raw truncation used")

    promoted = promotion["promoted_objects"]
    require(promotion["source_stack_closed"] is True, "source stack not closed")
    require(promoted["SelectedFiniteC1SourceIdentityTheorem"] is True, "source identity not promoted")
    require(promoted["PhysicalPhiFinC1ActionSource"] is True, "physical source not promoted")
    require(promoted["A_selected"] is True, "A_selected not promoted")
    require(promoted["b_selected"] is True, "b_selected not promoted")
    require(promoted["deltaTheta_C1"] is True, "deltaTheta_C1 not promoted")
    require(promotion["full_SM_no_knob_closed"] is False, "full SM overclosed")
    require(promotion["true_SM_equivalence_closed"] is False, "true SM overclosed")

    decision = data["closure_decision"]
    require(decision["step14_closed"] is True, "Step 14 not closed")
    require(decision["step15_collapsed_and_closed"] is True, "Step 15 not closed")
    require(decision["source_identity_theorem_promoted"] is True, "source identity decision missing")
    require(decision["local_principle_used_as_free_patch"] is False, "local patch used")
    require(decision["source_row_used_as_premise"] is False, "source row premise used")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")

    require(next_workorder["completed_steps"] == [14, 15], "completed steps mismatch")
    require(next_workorder["next_step"] == 16, "next step mismatch")
    require(next_workorder["step16_must_not_repeat"]["source_identity_theorem"] is True, "anti-repeat missing")

    for phrase in [
        "physical action/row-kernel validator       PASS",
        "SelectedFiniteC1SourceIdentityTheorem      promoted",
        "does not use the conditional local principle as a free patch",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
