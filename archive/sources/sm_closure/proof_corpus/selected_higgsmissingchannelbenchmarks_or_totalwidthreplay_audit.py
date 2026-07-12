"""Audit missing Higgs channel benchmarks and hybrid total-width replay."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgsmissingchannelbenchmarks_or_totalwidthreplay"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
BENCH = PACKET_DIR / "missing_higgs_channel_benchmark_rows.packet.json"
HYBRID = PACKET_DIR / "hybrid_higgs_total_width_replay.packet.json"
GATE = PACKET_DIR / "precision_total_width_promotion_gate.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_missing_channel_benchmarks.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsMissingChannelBenchmarks_or_TotalWidthReplay_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_HIGGSMISSINGCHANNELBENCHMARKS_OR_TOTALWIDTHREPLAY_BUILT_HYBRID_REPLAY_PRECISION_OPEN"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    bench = load(BENCH)
    hybrid = load(HYBRID)
    gate = load(GATE)
    updated = load(UPDATED)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["closure_decision"]["channel_coverage_closed_at_hybrid_replay_tier"] is True, "coverage tier not closed")
    require(data["closure_decision"]["precision_total_width_closed"] is False, "precision total width overclaimed")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "true equivalence overclaimed")

    require(len(bench["rows"]) == 6, "expected six missing channel benchmark rows")
    require(bench["all_missing_ledger_channels_filled_as_benchmarks"] is True, "benchmark rows incomplete")
    require(bench["accepted_as_downstream_SM_parity_benchmark_rows"] is True, "benchmark tier not accepted")
    require(bench["accepted_as_no_knob_or_source_derived_values"] is False, "benchmark overpromoted")
    for row in bench["rows"]:
        require(row["width_GeV"] > 0.0, "benchmark width must be positive")
        require(row["used_as_source_selector"] is False, "benchmark selector violation")
        require(row["accepted_as_MTT_computed_width"] is False, "benchmark row overclaimed as computed")

    require(hybrid["summary"]["all_major_channels_have_a_width_row"] is True, "hybrid width rows incomplete")
    require(hybrid["accepted_as_total_width_replay_scaffold"] is True, "hybrid scaffold not accepted")
    require(hybrid["accepted_as_precision_total_width"] is False, "hybrid precision overclaimed")
    require(abs(hybrid["summary"]["hybrid_relative_residual_to_reference"]) < 0.25, "hybrid residual unexpectedly large")

    require(gate["precision_promotion_accepted"] is False, "promotion overclaimed")
    require("uniform precision Higgs partial-width formula rows" in updated["remaining_true_equivalence_blockers"], "uniform formula blocker missing")
    require(updated["guardrails"]["benchmark_rows_are_downstream_not_source"] is True, "benchmark guard missing")
    require(updated["guardrails"]["hybrid_total_width_not_precision"] is True, "hybrid guard missing")

    for packet in [bench, hybrid, gate, updated, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    require("not a uniform" in note, "note missing precision guard")
    require("external benchmark rows" in note, "note missing benchmark wording")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
