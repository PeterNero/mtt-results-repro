"""Audit the executable H->gg proxy kernel row."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgsggkernelrow_or_electroweakrows"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
GG = PACKET_DIR / "higgs_gg_heavytop_kernel_row.packet.json"
EXTENDED = PACKET_DIR / "extended_executable_higgs_kernel_rows_after_gg.packet.json"
OPEN = PACKET_DIR / "remaining_electroweak_higgs_kernel_obligations.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_gg_kernel.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsGGKernelRow_or_ElectroweakRows_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_HIGGSGGKERNELROW_OR_ELECTROWEAKROWS_BUILT_GG_KERNEL_EW_ROWS_OPEN"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    gg = load(GG)
    extended = load(EXTENDED)
    open_rows = load(OPEN)
    updated = load(UPDATED)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["closure_decision"]["H_to_gg_proxy_kernel_closed"] is True, "gg row not closed")
    require(data["closure_decision"]["actual_QaSU3_operator_packet_closed"] is False, "Qa/SU3 overclaimed")

    require(gg["channel"] == "H_to_gg", "wrong channel")
    require(gg["accepted_as_uniform_kernel_row"] is True, "gg not accepted as proxy kernel row")
    require(gg["accepted_as_precision_formula_row"] is False, "gg precision overclaimed")
    require(gg["LO_width_GeV"] > 0.0 and gg["width_GeV"] > gg["LO_width_GeV"], "NLO proxy should increase LO width")
    require(gg["NLO_proxy_factor"] > 1.0, "NLO factor should exceed one")
    require(abs(gg["relative_residual_to_benchmark_fill"]) < 0.35, "gg residual unexpectedly large")
    require("Qa/SU3" in gg["operator_attachment_required"], "Qa/SU3 attachment missing")

    executable = extended["executable_rows"]
    require(extended["summary"]["executable_kernel_row_count"] == 6, "expected six executable rows")
    require(extended["summary"]["open_kernel_row_count"] == 4, "expected four open rows")
    require(extended["summary"]["all_executable_widths_positive"] is True, "nonpositive executable width")
    require(any(row["channel"] == "H_to_gg" for row in executable), "extended packet missing gg")
    require(extended["summary"]["color_sensitive_precision_rows_still_require_QaSU3"] is True, "Qa/SU3 guard missing")

    require(open_rows["status"] == "FOUR_ELECTROWEAK_HIGGS_KERNEL_ROWS_REMAIN_OPEN", "open status mismatch")
    require(len(open_rows["rows"]) == 4, "expected four open rows")
    require(open_rows["color_sensitive_open_channels"] == [], "color-sensitive row should be proxy-filled")
    for channel in ["H_to_WW_star", "H_to_ZZ_star", "H_to_gamma_gamma", "H_to_Z_gamma"]:
        require(channel in open_rows["blocked_channels"], f"missing EW blocker {channel}")

    require("electroweak off-shell/loop Higgs rows" in updated["next_primary_value_gate"], "next gate should point to EW rows")
    require(updated["guardrails"]["gg_kernel_not_precision"] is True, "gg guard missing")
    require(updated["guardrails"]["color_proxy_rows_still_require_actual_QaSU3_for_precision"] is True, "color guard missing")

    for packet in [gg, extended, open_rows, updated, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    require("H_to_gg" in note, "note missing gg")
    require("not a precision" in note, "note missing precision guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
