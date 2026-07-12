"""Audit dynamic C1 patch to SM-parity ledger / unpatched measure derivation gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_dynamicc1patchtosmparityledger_or_unpatchedmeasurederivation"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
LEDGER = PACKET_DIR / "dynamic_c1_sm_parity_status_update.packet.json"
UPGRADE = PACKET_DIR / "no_knob_upgrade_boundary_after_patch.packet.json"
NEXTSTEPS = PACKET_DIR / "post_patch_sm_parity_next_steps.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_DynamicC1PatchToSMParityLedger_or_UnpatchedMeasureDerivation_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_DYNAMICC1PATCHTOSMPARITYLEDGER_OR_UNPATCHEDMEASUREDERIVATION_BUILT_PATCHED_LEDGER_UPDATED"
NEXT = "MTT_Selected_PatchedDynamicC1EmpiricalReplayIntegration_or_NoKnobDerivation_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    ledger = load(LEDGER)
    upgrade = load(UPGRADE)
    nextsteps = load(NEXTSTEPS)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(ledger["status"] == "PATCHED_DYNAMIC_C1_STATUS_IMPORTED_TO_SM_PARITY_LEDGER", "ledger status mismatch")
    require(ledger["after_patch_status"]["patched_dynamic_C1_packet_closed"] is True, "patched dynamic closure missing")
    require(ledger["after_patch_status"]["patched_A_selected"] == [[12.0, 0.0], [0.0, 12.0]], "patched A mismatch")
    require(ledger["after_patch_status"]["patched_b_selected"] == [12.0, 12.0], "patched b mismatch")
    require(ledger["after_patch_status"]["patched_deltaTheta_C1"] == [1.0, 1.0], "patched delta mismatch")
    require(ledger["after_patch_status"]["patched_sector_response_matrices"] is True, "patched sector response missing")
    require(ledger["full_SM_parity_ledger_closed_now"] is False, "full SM parity overclaimed")
    require(ledger["true_SM_equivalence_closed_now"] is False, "true SM equivalence overclaimed")

    require(upgrade["status"] == "PATCHED_PARITY_CLOSED_NO_KNOB_DERIVATION_OPEN", "upgrade status mismatch")
    for key, value in upgrade["patched_spine_closures"].items():
        require(value is True, f"patched closure missing: {key}")
    for key, value in upgrade["no_knob_upgrade_targets_remaining"].items():
        require(value is True, f"no-knob target missing: {key}")
    require(upgrade["measured_replay_policy_unchanged"]["measured_values_do_not_select_packet"] is True, "measured non-selection missing")
    require(upgrade["measured_replay_policy_unchanged"]["observed_data_used_as_selector"] is False, "observed selector overclaimed")
    require(upgrade["measured_replay_policy_unchanged"]["target_fitting_used"] is False, "target fitting overclaimed")

    require(nextsteps["status"] == "NEXT_STEPS_REDUCED_AFTER_PATCHED_DYNAMIC_C1_CLOSURE", "nextsteps status mismatch")
    require(len(nextsteps["patched_dynamic_C1_no_longer_blocks"]) == 3, "patched no-longer-blocks list incomplete")
    for key, value in nextsteps["remaining_for_full_SM_parity_or_true_equivalence"].items():
        require(value is True, f"remaining global gate missing: {key}")
    require(nextsteps["full_sm_parity_closed_now"] is False, "nextsteps parity overclaimed")

    for key in [
        "patched_dynamic_C1_status_imported_to_SM_parity_ledger",
        "patched_A_b_deltaTheta_sector_response_interface_available",
        "no_knob_boundary_after_patch_declared",
        "post_patch_next_steps_reduced",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "full_SM_parity_ledger_integration",
        "final_integrated_empirical_replay_audit",
        "common_RG_and_covariance_completion",
        "selected_SM_packet_certificate_integration",
        "local_QFT_functor_or_observable_suite",
        "GR_QM_measurement_interfaces",
        "unpatched_no_knob_measure_derivation",
        "true_SM_equivalence_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"open flag missing: {key}")
    require(data["promotion_decision"]["patched_dynamic_C1_no_longer_blocks_SM_parity"] is True, "patched parity decision missing")
    for key in ["full_SM_parity_closed", "true_SM_equivalence_closed", "unpatched_no_knob_dynamic_C1_closed"]:
        require(data["promotion_decision"][key] is False, f"global overclaimed: {key}")

    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["closure_claimed"] is False and cert["closure_claimed"] is False, "full closure overclaimed")
    require(data["patched_spine_closure_claimed"] is True and cert["patched_spine_closure_claimed"] is True, "patched closure missing")
    require(data["observed_data_used"] is False and data["target_fitting_used"] is False, "data guardrail violated")
    require("patched dynamic C1 no longer blocks parity = True" in note, "note missing patched ledger status")
    require("full SM parity closed now                  = False" in note, "note missing full parity guardrail")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
