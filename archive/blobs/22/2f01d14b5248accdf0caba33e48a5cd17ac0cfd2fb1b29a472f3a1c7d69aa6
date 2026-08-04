"""Audit global true-SM/no-knob ledger after Yukawa finite-replay closure."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_truesmnoknobclosure_globalledger_or_remainingnonyukawarows"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
LEDGER = PACKET_DIR / "global_true_sm_noknob_ledger.packet.json"
BLOCKERS = PACKET_DIR / "remaining_nonyukawa_blocker_matrix.packet.json"
PLAN = PACKET_DIR / "next_closure_plan_after_yukawa_finite_replay.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_TrueSMNoKnobClosure_GlobalLedger_or_RemainingNonYukawaRows_v1.md"

STATUS = "MTT_SELECTED_TRUESMNOKNOBCLOSURE_GLOBALLEDGER_BUILT_YUKAWA_FINITE_REPLAY_CLOSED_NONYUKAWA_OPEN"
NEXT = "MTT_Selected_StrictPEWDirectK_or_QaSU3Step10ValueExecution_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    ledger = load(LEDGER)
    blockers = load(BLOCKERS)
    plan = load(PLAN)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(data["closure_claimed"] is False, "global overclosed")
    require(data["observed_data_used_as_selector"] is False, "candidate observed selector")
    require(data["target_fitting_used"] is False, "candidate target fitting")

    require(ledger["status"] == "YUKAWA_FINITE_REPLAY_CLOSED_NONYUKAWA_LEDGER_OPEN", "ledger status")
    require(ledger["observed_data_used_as_selector"] is False, "ledger observed selector")
    require(ledger["target_fitting_used"] is False, "ledger target fitting")
    rows = ledger["accepted_updated_rows"]
    require(rows["finite_replay_yukawa_magnitude_rows"] == 9, "Yukawa rows")
    require(rows["strict_phase_antisymmetry_scalar_source_rows"] == 1, "phase source rows")
    require(rows["finite_tail_source_rows"] == 2, "tail rows")
    require(rows["accepted_precision_true_equivalence_rows"] == 0, "precision rows overaccepted")
    require(rows["strict_P_EW_source_rows"] == 0, "PEW rows overaccepted")

    sectors = ledger["sector_status"]
    require(sectors["charged_yukawa_magnitudes"]["closed"] is True, "Yukawa not closed")
    require(sectors["charged_yukawa_magnitudes"]["accepted_rows"] == 9, "Yukawa accepted row count")
    require(
        sectors["charged_yukawa_magnitudes"]["status"] == "CLOSED_FINITE_REPLAY_STANDARD",
        "Yukawa status",
    )
    for key in [
        "strict_P_EW_direct_K_H_lambda",
        "qcd_theta",
        "neutrino_absolute_majorana_dirac",
        "precision_threshold_mass_scheme_profile",
        "local_qft_precision_observables",
        "qasu3_dynamic_operator_payload",
    ]:
        require(sectors[key]["closed"] is False, f"{key} overclosed")
    require(sectors["qasu3_dynamic_operator_payload"]["operator_source_slots_closed"] == 8, "QaSU3 slots")
    require(sectors["qasu3_dynamic_operator_payload"]["operator_source_slots_remaining"] == 0, "QaSU3 remaining slots")
    require(
        sectors["precision_threshold_mass_scheme_profile"]["accepted_true_equivalence_rows"] == 0,
        "precision accepted rows",
    )
    require(sectors["local_qft_precision_observables"]["tree_tier_closed"] is True, "tree QFT tier")

    require(blockers["status"] == "NONYUKAWA_BLOCKERS_REMAIN_ORDERED", "blocker status")
    expected_blockers = [
        "strict_P_EW_direct_K_H_lambda",
        "qcd_theta",
        "neutrino_absolute_majorana_dirac",
        "precision_threshold_mass_scheme_profile",
        "local_qft_precision_observables",
        "qasu3_dynamic_operator_payload",
    ]
    require(blockers["remaining_hard_blockers"] == expected_blockers, "blocker list")
    require(blockers["global_true_sm_no_knob_closed"] is False, "blockers global overclosed")
    ordered = blockers["ordered_closure_targets"]
    require(len(ordered) == 6, "ordered target count")
    require(ordered[0]["id"] == "strict_P_EW_or_direct_K_H_lambda", "first target")
    require(ordered[1]["id"] == "QaSU3_Step10_dynamic_value_execution", "second target")

    require(plan["status"] == "NEXT_TARGET_LOCKED_TO_STRICT_PEW_OR_QASU3_STEP10", "plan status")
    require(plan["do_next"]["artifact"] == NEXT, "plan next")
    require(len(plan["do_next"]["success_criteria"]) == 3, "success criteria")
    require(len(plan["do_not_repeat"]) == 3, "do-not-repeat count")

    require(data["theorem"]["name"] == "GlobalTrueSMNoKnobLedgerAfterYukawaFiniteReplayTheorem", "theorem name")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    key_numbers = data["key_numbers"]
    require(key_numbers["accepted_finite_replay_yukawa_magnitude_rows"] == 9, "key Yukawa")
    require(key_numbers["remaining_hard_blocker_count"] == 6, "key blocker count")
    closure = data["closure_decision"]
    require(closure["yukawa_finite_replay_magnitudes_closed"] is True, "closure Yukawa")
    require(closure["global_true_SM_no_knob_closure"] is False, "closure global")
    require(closure["true_SM_equivalence_closed"] is False, "closure true SM")
    require(closure["remaining_non_yukawa_blockers_ordered"] is True, "closure blockers")

    require(cert["yukawa_finite_replay_magnitudes_closed"] is True, "cert Yukawa")
    require(cert["accepted_finite_replay_yukawa_magnitude_rows"] == 9, "cert Yukawa rows")
    require(cert["remaining_hard_blocker_count"] == 6, "cert blocker count")
    require(cert["remaining_hard_blockers"] == expected_blockers, "cert blockers")
    require(cert["global_true_SM_no_knob_closure"] is False, "cert global")
    require(cert["true_SM_equivalence_closed"] is False, "cert true SM")
    require(cert["observed_data_used_as_selector"] is False, "cert observed selector")
    require(cert["target_fitting_used"] is False, "cert target fitting")

    for phrase in [
        "Yukawa magnitudes are now closed",
        "strict `P_EW` / direct `K_threshold.Omega_H.lambda`",
        "Qa/SU3 Step10 actual dynamic value execution",
        "Accepted true-equivalence precision rows remain",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
