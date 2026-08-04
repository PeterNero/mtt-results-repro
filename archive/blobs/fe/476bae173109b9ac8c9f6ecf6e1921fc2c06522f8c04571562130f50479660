"""Audit patched finite C1 source identity integration into SM-parity ledger."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_sourceidentitypatcheddynamicc1ledger_or_unpatchedactionproof"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
LEDGER = PACKET_DIR / "source_identity_patched_dynamic_c1_ledger_update.packet.json"
INTERFACE = PACKET_DIR / "patched_dynamic_c1_source_and_value_interface.packet.json"
UPGRADE = PACKET_DIR / "unpatched_action_proof_upgrade_matrix.packet.json"
NEXTSTEPS = PACKET_DIR / "post_source_identity_patch_next_steps.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SourceIdentityPatchedDynamicC1Ledger_or_UnpatchedActionProof_v1.md"

STATUS = "MTT_SELECTED_SOURCEIDENTITYPATCHEDDYNAMICC1LEDGER_OR_UNPATCHEDACTIONPROOF_BUILT_PATCHED_LEDGER_STRENGTHENED"
NEXT = "MTT_Selected_FinalIntegratedSMParityReplayAfterSourceIdentityPatch_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")


def main() -> int:
    proc = subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, text=True, capture_output=True)
    if proc.returncode:
        print(proc.stdout)
        print(proc.stderr, file=sys.stderr)
        return proc.returncode

    candidate = load(CANDIDATE)
    ledger = load(LEDGER)
    interface = load(INTERFACE)
    upgrade = load(UPGRADE)
    nextsteps = load(NEXTSTEPS)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "cert next mismatch")
    require(candidate["theorem"]["proved"] is True and candidate["theorem"]["patched"] is True, "theorem metadata mismatch")
    require(cert["theorem_proved"] is True and cert["theorem_patched"] is True, "cert theorem metadata mismatch")

    require(ledger["status"] == "PATCHED_SOURCE_IDENTITY_IMPORTED_TO_SM_PARITY_LEDGER", "ledger status mismatch")
    require(ledger["previous_dynamic_c1_ledger"]["patched_dynamic_C1_no_longer_blocks_SM_parity"] is True, "previous ledger not imported")
    require(ledger["strengthened_patch"]["strict_source_id_validator_ok"] is True, "source validator not imported")
    require(ledger["strengthened_patch"]["row_counts"]["total_source_rows"] == 110, "source row total mismatch")
    require(ledger["strengthened_patch"]["source_identity_packet_closed_under_local_principle"] is True, "source identity not closed under local principle")
    require(ledger["full_SM_parity_closed_now"] is False, "full SM parity overclaimed")
    require(ledger["true_SM_equivalence_closed_now"] is False, "true equivalence overclaimed")
    require(ledger["unpatched_no_knob_dynamic_C1_closed"] is False, "unpatched dynamic C1 overclaimed")

    require(interface["status"] == "PATCHED_SOURCE_AND_VALUE_INTERFACE_AVAILABLE", "interface status mismatch")
    require(interface["source_layer"]["primitive_rows"] == 72, "primitive count mismatch")
    require(interface["source_layer"]["sector_rows"] == 36, "sector count mismatch")
    require(interface["source_layer"]["hessian_source_rows"] == 2, "hessian count mismatch")
    require(interface["source_layer"]["strict_source_id_validator_ok"] is True, "interface source validator missing")
    require(interface["value_layer"]["patched_A_selected"] == [[12.0, 0.0], [0.0, 12.0]], "A mismatch")
    require(interface["value_layer"]["patched_b_selected"] == [12.0, 12.0], "b mismatch")
    require(interface["value_layer"]["patched_deltaTheta_C1"] == [1.0, 1.0], "delta mismatch")
    require(interface["value_layer"]["patched_dynamic_C1_packet_closed"] is True, "value closure missing")
    require(interface["superset_strategy"]["free_parameters_used"] is False, "free parameters used")

    require(upgrade["status"] == "UNPATCHED_ACTION_PROOF_REMAINS_NO_KNOB_UPGRADE_TARGET", "upgrade status mismatch")
    require(upgrade["patched_local_closure"]["source_identity_packet"] is True, "source packet not patched closed")
    require(upgrade["patched_local_closure"]["dynamic_C1_value_packet"] is True, "value packet not patched closed")
    require(upgrade["patched_local_closure"]["SM_parity_dynamic_C1_blocker_removed"] is True, "blocker not removed")
    for key, value in upgrade["unpatched_upgrade_tasks"].items():
        require(value is True, f"unpatched upgrade missing: {key}")
    require("unpatched no-knob derivation" in upgrade["patched_closure_not_allowed_for"], "no-knob exclusion missing")

    require(nextsteps["status"] == "NEXT_STEPS_REDUCED_TO_FINAL_SM_PARITY_REPLAY_AND_UNPATCHED_UPGRADE", "nextsteps status mismatch")
    require(len(nextsteps["patched_dynamic_C1_no_longer_blocks"]) == 4, "no-longer-blocks incomplete")
    for key, value in nextsteps["remaining_for_SM_parity"].items():
        require(value is True, f"SM parity remaining gate missing: {key}")
    for key, value in nextsteps["remaining_for_no_knob"].items():
        require(value is True, f"no-knob remaining gate missing: {key}")

    require(candidate["promotion_decision"]["patched_dynamic_C1_no_longer_blocks_SM_parity"] is True, "promotion decision missing")
    require(candidate["promotion_decision"]["patched_source_identity_closed"] is True, "source identity decision missing")
    require(candidate["promotion_decision"]["patched_value_interface_closed"] is True, "value decision missing")
    for key in ["full_SM_parity_closed", "true_SM_equivalence_closed", "unpatched_no_knob_dynamic_C1_closed"]:
        require(candidate["promotion_decision"][key] is False, f"global overclaim: {key}")
    require(candidate["closure_claimed"] is False and cert["closure_claimed"] is False, "global closure overclaimed")
    require(candidate["patched_spine_closure_claimed"] is True and cert["patched_spine_closure_claimed"] is True, "patched closure missing")
    require("strict source rows validated       = True" in note, "note missing source validation")
    require("full SM parity closed now          = False" in note, "note missing parity guardrail")
    require("unpatched no-knob dynamic C1 closed = False" in note, "note missing no-knob guardrail")

    for packet in [candidate, ledger, interface, upgrade, nextsteps, cert]:
        guard(packet)

    print(proc.stdout.strip())
    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
