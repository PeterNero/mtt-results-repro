"""Audit benchmark-replay policy for remaining electroweak Higgs rows."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgsewbenchmarkpolicy_or_fullformulas"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
POLICY = PACKET_DIR / "remaining_electroweak_benchmark_replay_policy.packet.json"
COMPLETION = PACKET_DIR / "higgs_ten_channel_replay_completion.packet.json"
OPEN = PACKET_DIR / "remaining_higgs_precision_formula_obligations.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_ew_benchmark_policy.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsEWBenchmarkPolicy_or_FullFormulas_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_HIGGSEWBENCHMARKPOLICY_OR_FULLFORMULAS_BUILT_TEN_CHANNEL_REPLAY_PRECISION_OPEN"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    policy = load(POLICY)
    completion = load(COMPLETION)
    open_obligations = load(OPEN)
    updated = load(UPDATED)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["closure_decision"]["ten_channel_replay_completed"] is True, "ten-channel replay not completed")
    require(data["closure_decision"]["uniform_formula_rows_fully_closed"] is False, "uniform formulas overclaimed")
    require(data["closure_decision"]["cross_channel_covariance_profile_closed"] is False, "covariance overclaimed")

    rows = policy["rows"]
    require(len(rows) == 3, "expected three benchmark policy rows")
    require(policy["summary"]["all_remaining_EW_rows_have_benchmark_policy"] is True, "missing EW benchmark policy")
    require(policy["summary"]["accepted_as_SM_parity_replay_policy"] is True, "policy not accepted for replay")
    require(policy["summary"]["accepted_as_formula_kernel_policy"] is False, "formula policy overclaimed")
    require(policy["summary"]["accepted_as_precision_policy"] is False, "precision policy overclaimed")
    for channel in ["H_to_WW_star", "H_to_ZZ_star", "H_to_Z_gamma"]:
        row = next((item for item in rows if item["channel"] == channel), None)
        require(row is not None, f"missing benchmark policy row {channel}")
        require(row["benchmark_width_GeV"] > 0.0, f"missing benchmark width {channel}")
        require(row["accepted_as_downstream_benchmark_replay_row"] is True, f"row not accepted {channel}")
        require(row["accepted_as_executable_formula_kernel"] is False, f"formula overclaimed {channel}")
        require(row["accepted_as_precision_formula_row"] is False, f"precision overclaimed {channel}")

    require(completion["summary"]["row_count"] == 10, "completion row count mismatch")
    require(completion["summary"]["all_ten_channels_have_replay_rows"] is True, "ten-channel replay incomplete")
    require(completion["summary"]["executable_proxy_kernel_count"] == 7, "expected seven proxy kernels")
    require(completion["summary"]["audited_benchmark_replay_count"] == 3, "expected three benchmark rows")
    require(completion["summary"]["precision_promotion_accepted"] is False, "precision promotion overclaimed")

    require(len(open_obligations["formula_rows_still_required_for_precision"]) == 3, "formula obligation count mismatch")
    require("supply ten-channel covariance/profile matrix" in open_obligations["global_obligations"], "covariance obligation missing")
    require(updated["guardrails"]["benchmark_replay_not_formula_kernel"] is True, "benchmark guard missing")
    require(updated["guardrails"]["ten_channel_replay_not_precision"] is True, "precision guard missing")

    for packet in [policy, completion, open_obligations, updated, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    require("WW*" in note and "Z gamma" in note, "note missing EW rows")
    require("not a uniform formula" in note, "note missing formula guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
