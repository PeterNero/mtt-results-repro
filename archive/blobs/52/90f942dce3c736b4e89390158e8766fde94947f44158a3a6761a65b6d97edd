"""Audit final Higgs SM-parity profile policy or remaining route-A kernels."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgsfinalsmparityprofilepolicy_or_remainingrouteakernels"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
POLICY = PACKET_DIR / "final_higgs_smparity_profile_policy.packet.json"
TEN_ROW = PACKET_DIR / "ten_row_higgs_replay_closure_ledger.packet.json"
REMAINING = PACKET_DIR / "remaining_route_a_kernel_execution_contract.packet.json"
TRUE_GATE = PACKET_DIR / "updated_true_equivalence_gate_after_final_higgs_policy.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsFinalSMParityProfilePolicy_or_RemainingRouteAKernels_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_HIGGSFINALSMPARITYPROFILEPOLICY_OR_REMAININGROUTEAKERNELS_BUILT_SMPARITY_HIGGS_REPLAY_CLOSED_ROUTEA_OPEN"
NEXT = "MTT_Selected_FullSMParityReplayClosureOr_NonHiggsProfilePolicy_v1"
REMAINING_ROWS = ["H_to_Z_gamma", "H_to_WW_star", "H_to_ZZ_star"]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    policy = load(POLICY)
    ten_row = load(TEN_ROW)
    remaining = load(REMAINING)
    true_gate = load(TRUE_GATE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem not proved")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    require(policy["declared_standard"] == "SM_PARITY_REPLAY", "wrong declared standard")
    require(policy["ten_row_replay_admitted_for_SM_parity"] is True, "SM-parity replay not admitted")
    require(policy["route_A_rows_executed_count"] == 7, "route-A executed count mismatch")
    require(policy["route_A_rows_remaining_count"] == 3, "route-A remaining count mismatch")
    require(policy["full_route_A_ten_row_engine_closed"] is False, "route-A overclosed")
    require(policy["precision_total_width_closed_by_formula"] is False, "precision width overclosed")
    require(policy["precision_branching_ratios_closed_by_formula"] is False, "precision BR overclosed")
    require(policy["official_likelihood_imported"] is False, "official likelihood overclaimed")
    require(policy["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(policy["no_knob_closed"] is False, "no-knob overclosed")

    require(ten_row["row_count"] == 10, "ten-row ledger row count mismatch")
    require(ten_row["all_rows_have_SM_parity_replay_source"] is True, "row replay source missing")
    require(ten_row["SM_parity_Higgs_profile_replay_closed"] is True, "Higgs replay not closed")
    require(ten_row["route_A_Higgs_profile_closed"] is False, "route-A profile overclosed")
    require(ten_row["precision_Higgs_profile_closed"] is False, "precision profile overclosed")
    require(ten_row["route_A_rows_remaining"] == REMAINING_ROWS, "remaining row mismatch")

    for row in ten_row["rows"]:
        require(row["SM_parity_replay_admitted"] is True, "row replay not admitted")
        require(row["accepted_as_precision_formula_row"] is False, "row precision overclaimed")
        if row["channel"] in REMAINING_ROWS:
            require(row["route_A_formula_derivative_available"] is False, "remaining row overfilled")
            require(row["policy_status"] == "DOWNSTREAM_IMPORT_REPLAY_ONLY_ROUTE_A_KERNEL_OPEN", "remaining row policy mismatch")

    require(remaining["remaining_channels"] == REMAINING_ROWS, "remaining contract row mismatch")
    require(remaining["alternate_SM_parity_path_closed_now"] is True, "SM-parity alternate path not closed")
    require(remaining["route_A_formula_path_closed_now"] is False, "route-A path overclosed")

    require(true_gate["guardrails"]["SM_parity_Higgs_profile_replay_closed"] is True, "true gate replay missing")
    require(true_gate["guardrails"]["route_A_Higgs_profile_closed"] is False, "true gate route-A overclosed")
    require(true_gate["guardrails"]["true_SM_equivalence_closed"] is False, "true gate SM overclosed")
    require(true_gate["guardrails"]["no_knob_closed"] is False, "true gate no-knob overclosed")

    require(data["closure_decision"]["SM_parity_Higgs_profile_replay_closed"] is True, "candidate replay closure missing")
    require(data["closure_decision"]["full_route_A_ten_row_engine_closed"] is False, "candidate route-A overclosed")
    require(cert["SM_parity_Higgs_profile_replay_closed"] is True, "certificate replay closure missing")
    require("SM-parity replay level" in note, "note missing scope")

    for packet in [policy, ten_row, remaining, true_gate, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
