"""Audit the executable H->ss kernel row."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgssskernelrow_or_remainingchannels"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SS = PACKET_DIR / "higgs_ss_running_mass_kernel_row.packet.json"
EXTENDED = PACKET_DIR / "extended_executable_higgs_kernel_rows.packet.json"
OPEN = PACKET_DIR / "remaining_higgs_kernel_obligations_after_ss.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_ss_kernel.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsSSKernelRow_or_RemainingChannels_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_HIGGSSSKERNELROW_OR_REMAININGCHANNELS_BUILT_SS_KERNEL_FIVE_CHANNELS_OPEN"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    ss = load(SS)
    extended = load(EXTENDED)
    open_rows = load(OPEN)
    updated = load(UPDATED)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["closure_decision"]["H_to_ss_kernel_closed"] is True, "ss row not closed")
    require(data["closure_decision"]["uniform_formula_rows_fully_closed"] is False, "uniform rows overclaimed")

    require(ss["channel"] == "H_to_ss", "wrong channel")
    require(ss["accepted_as_uniform_kernel_row"] is True, "ss not accepted as kernel row")
    require(ss["accepted_as_precision_formula_row"] is False, "ss precision overclaimed")
    require(ss["width_GeV"] > 0.0, "ss width must be positive")
    require(ss["running_mass_at_mH_GeV"] < ss["reference_mass_GeV_at_2GeV"], "strange mass should run downward to mH in proxy")
    require(ss["N3LO_massless_QCD_factor"] > 1.0, "QCD factor should exceed one")
    require(abs(ss["relative_residual_to_benchmark_fill"]) < 2.0, "ss residual unexpectedly large")
    require("Qa/SU3" in ss["operator_attachment_required"] or "color" in ss["operator_attachment_required"], "color attachment missing")

    executable = extended["executable_rows"]
    require(extended["summary"]["executable_kernel_row_count"] == 5, "expected five executable rows")
    require(extended["summary"]["open_kernel_row_count"] == 5, "expected five open rows")
    require(extended["summary"]["all_executable_widths_positive"] is True, "nonpositive executable width")
    require(any(row["channel"] == "H_to_ss" for row in executable), "extended packet missing ss")
    require(extended["summary"]["uniform_formula_rows_fully_filled"] is False, "full rows overclaimed")

    require(open_rows["status"] == "FIVE_HIGGS_KERNEL_ROWS_REMAIN_OPEN", "open status mismatch")
    require(len(open_rows["rows"]) == 5, "expected five open rows")
    require("H_to_ss" not in open_rows["blocked_channels"], "ss should no longer be blocked")
    require("H_to_gg" in open_rows["color_sensitive_open_channels"], "gg color blocker missing")
    require("H_to_WW_star" in open_rows["electroweak_loop_or_offshell_open_channels"], "WW blocker missing")

    require("H_to_gg" in updated["next_primary_value_gate"], "next gate should point to gg")
    require(updated["guardrails"]["ss_kernel_not_precision"] is True, "ss guard missing")

    for packet in [ss, extended, open_rows, updated, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    require("H_to_ss" in note, "note missing ss")
    require("not a precision" in note, "note missing precision guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
