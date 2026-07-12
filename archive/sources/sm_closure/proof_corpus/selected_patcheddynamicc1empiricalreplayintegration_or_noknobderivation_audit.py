"""Audit patched dynamic C1 empirical replay integration / no-knob derivation gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_patcheddynamicc1empiricalreplayintegration_or_noknobderivation"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
REPLAY = PACKET_DIR / "patched_dynamic_c1_empirical_replay_interface.packet.json"
LEDGER = PACKET_DIR / "empirical_ledger_post_patch_update.packet.json"
GATES = PACKET_DIR / "remaining_global_sm_parity_gates.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PatchedDynamicC1EmpiricalReplayIntegration_or_NoKnobDerivation_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_PATCHEDDYNAMICC1EMPIRICALREPLAYINTEGRATION_OR_NOKNOBDERIVATION_BUILT_REPLAY_INTERFACE_UPDATED"
NEXT = "MTT_Selected_FinalSMParityGapMatrix_or_ClosureAttempt_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    replay = load(REPLAY)
    ledger = load(LEDGER)
    gates = load(GATES)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(replay["status"] == "PATCHED_DYNAMIC_C1_INTERFACE_READY_FOR_EMPIRICAL_REPLAY", "replay status mismatch")
    c1 = replay["patched_dynamic_C1_inputs"]
    require(c1["patched_dynamic_C1_packet_closed"] is True, "patched C1 not closed")
    require(c1["A_selected"] == [[12.0, 0.0], [0.0, 12.0]], "A mismatch")
    require(c1["b_selected"] == [12.0, 12.0], "b mismatch")
    require(c1["deltaTheta_C1"] == [1.0, 1.0], "delta mismatch")
    require(c1["sector_response_matrices"] is True, "sector matrices missing")
    require(len(replay["forbidden_uses"]) == 4, "forbidden replay uses incomplete")
    for slot in ["yukawa_matrices", "CKM_PMNS_CP", "Higgs_parameters", "gauge_couplings"]:
        require(replay["measured_slots_still_downstream"][slot]["admitted_for_SM_equivalence"] is True, f"slot not admitted: {slot}")
        require(replay["measured_slots_still_downstream"][slot]["blocked_as_source_selector"] is True, f"slot selector guardrail missing: {slot}")

    require(ledger["status"] == "EMPIRICAL_LEDGER_UPDATED_WITH_PATCHED_DYNAMIC_C1_INTERFACE", "ledger status mismatch")
    require(ledger["patched_dynamic_C1_no_longer_blocks_empirical_replay_interface"] is True, "ledger patched status missing")
    summary = ledger["acceptance_summary_after_patch"]
    require(summary["patched_dynamic_C1_interface_ready"] is True, "summary patched flag missing")
    require(summary["actual_numeric_equivalence_computed"] is False, "numeric equivalence overclaimed")
    require(summary["sm_parity_closure_claimed"] is False, "SM parity overclaimed")
    updated = [r for r in ledger["updated_ledger_rows"] if r["domain"] == "Yukawa, CP, and Higgs phenomenology"]
    require(len(updated) == 1, "updated empirical row missing")
    require(updated[0]["status"] == "PATCHED_DYNAMIC_C1_INTERFACE_READY_MEASURED_REPLAY_STILL_REQUIRED", "updated row status mismatch")
    require(updated[0]["patched_dynamic_C1_update"]["A_b_deltaTheta_sector_interface_ready"] is True, "updated row patched interface missing")
    require(updated[0]["patched_dynamic_C1_update"]["measured_Yukawa_CKM_PMNS_Higgs_still_downstream"] is True, "downstream measured guardrail missing")

    require(gates["status"] == "GLOBAL_GAP_MATRIX_AFTER_PATCHED_DYNAMIC_C1_BUILT", "gates status mismatch")
    for key, value in gates["closed_or_no_longer_blocking"].items():
        require(value is True, f"closed/no-longer-blocking flag missing: {key}")
    for key, value in gates["still_open"].items():
        require(value is True, f"remaining global gate missing: {key}")
    require(gates["full_SM_parity_closed_now"] is False, "full SM parity overclaimed")
    require(gates["true_SM_equivalence_closed_now"] is False, "true SM equivalence overclaimed")

    for key in [
        "patched_dynamic_C1_empirical_replay_interface_ready",
        "Yukawa_CP_Higgs_ledger_row_updated_after_patch",
        "global_gap_matrix_after_patch_built",
        "dynamic_C1_removed_from_patched_parity_blocker_list",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key, value in data["what_remains_open"].items():
        require(value is True, f"open flag missing: {key}")
    decision = data["promotion_decision"]
    require(decision["patched_dynamic_C1_empirical_interface_ready"] is True, "patched empirical decision missing")
    for key in ["actual_numeric_SM_equivalence_computed", "full_SM_parity_closed", "true_SM_equivalence_closed", "full_no_knob_closed"]:
        require(decision[key] is False, f"closure overclaimed: {key}")

    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["closure_claimed"] is False and cert["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used"] is False and data["target_fitting_used"] is False, "data guardrail violated")
    require("patched C1 empirical interface ready = True" in note, "note missing patched interface")
    require("full SM parity closed                = False" in note, "note missing SM parity guardrail")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
