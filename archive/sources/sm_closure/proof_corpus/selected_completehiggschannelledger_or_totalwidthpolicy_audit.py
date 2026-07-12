"""Audit the complete Higgs channel ledger and total-width policy gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_completehiggschannelledger_or_totalwidthpolicy"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
LEDGER = PACKET_DIR / "complete_higgs_channel_status_ledger.packet.json"
PARTIAL = PACKET_DIR / "currently_computed_higgs_partial_width_sum.packet.json"
POLICY = PACKET_DIR / "total_width_branching_policy_gate.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_channel_ledger.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_CompleteHiggsChannelLedger_or_TotalWidthPolicy_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_COMPLETEHIGGSCHANNELLEDGER_OR_TOTALWIDTHPOLICY_BUILT_LEDGER_TOTAL_WIDTH_OPEN"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    ledger = load(LEDGER)
    partial = load(PARTIAL)
    policy = load(POLICY)
    updated = load(UPDATED)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["closure_decision"]["channel_ledger_closed"] is True, "channel ledger not closed")
    require(data["closure_decision"]["total_Higgs_width_closed"] is False, "total width overclaimed")
    require(data["closure_decision"]["branching_ratios_closed"] is False, "branching ratios overclaimed")

    channels = {row["channel"]: row for row in ledger["channels"]}
    for channel in ["H_to_bb", "H_to_cc", "H_to_tau_tau", "H_to_mu_mu", "H_to_WW_star", "H_to_ZZ_star", "H_to_gg", "H_to_gamma_gamma", "H_to_Z_gamma", "H_to_ss"]:
        require(channel in channels, f"missing channel: {channel}")
    require(ledger["summary"]["channel_count"] == 10, "channel count mismatch")
    require(ledger["summary"]["computed_proxy_channel_count"] == 4, "computed channel count mismatch")
    require(ledger["summary"]["placeholder_channel_count"] == 6, "placeholder count mismatch")
    require(ledger["summary"]["all_major_channels_classified"] is True, "classification incomplete")

    require(partial["accepted_as_total_width"] is False, "partial sum overclaimed")
    require(partial["computed_proxy_width_sum_GeV"] > 0.0, "partial sum missing")
    require(0.5 < partial["fraction_of_reference_total_width"] < 1.0, "partial sum fraction should be partial but sizable")
    require("H_to_WW_star" in partial["missing_channels"], "WW* missing channel not tracked")

    require(policy["current_acceptance"]["channel_ledger_complete"] is True, "ledger acceptance missing")
    require(policy["current_acceptance"]["partial_width_values_complete"] is False, "partial widths overclaimed")
    require(policy["current_acceptance"]["total_width_value_complete"] is False, "total width overclaimed")
    require("H_to_gg width row" in policy["next_value_targets"], "gg next target missing")
    require("computed values for missing Higgs channels" in updated["remaining_true_equivalence_blockers"], "missing-channel blocker absent")
    require(updated["guardrails"]["channel_ledger_not_total_width"] is True, "ledger guard missing")

    for packet in [ledger, partial, policy, updated, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    require("not a total Higgs width" in note, "note missing total-width guard")
    require("missing formula/benchmark rows" in note, "note missing missing-row wording")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
