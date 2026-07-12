"""Audit partial executable Higgs uniform-kernel rows."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgsuniformkernelrows_or_fullchannelvalues"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
KERNELS = PACKET_DIR / "executable_higgs_uniform_kernel_rows.packet.json"
OPEN = PACKET_DIR / "open_higgs_kernel_obligations.packet.json"
GATE = PACKET_DIR / "full_channel_value_promotion_gate.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_uniform_kernel_rows.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsUniformKernelRows_or_FullChannelValues_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_HIGGSUNIFORMKERNELROWS_OR_FULLCHANNELVALUES_BUILT_PARTIAL_KERNEL_ROWS_FULL_VALUES_OPEN"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    kernels = load(KERNELS)
    open_rows = load(OPEN)
    gate = load(GATE)
    updated = load(UPDATED)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["closure_decision"]["partial_uniform_kernel_rows_closed"] is True, "partial kernel rows not closed")
    require(data["closure_decision"]["uniform_formula_rows_fully_closed"] is False, "full formula rows overclaimed")
    require(data["closure_decision"]["full_channel_values_closed"] is False, "full values overclaimed")

    executable = kernels["executable_rows"]
    require(len(executable) == 4, "expected four executable rows")
    require(kernels["summary"]["executable_kernel_row_count"] == 4, "kernel count mismatch")
    require(kernels["summary"]["open_kernel_row_count"] == 6, "open row count mismatch")
    require(kernels["summary"]["all_executable_widths_positive"] is True, "nonpositive executable width")
    require(kernels["summary"]["uniform_formula_rows_fully_filled"] is False, "uniform rows overclaimed")
    for channel in ["H_to_bb", "H_to_cc", "H_to_tau_tau", "H_to_mu_mu"]:
        row = next((item for item in executable if item["channel"] == channel), None)
        require(row is not None, f"missing executable row {channel}")
        require(row["accepted_as_uniform_kernel_row"] is True, f"row not accepted {channel}")
        require(row["accepted_as_precision_formula_row"] is False, f"precision overclaimed {channel}")
        require(row["width_GeV"] > 0.0, f"nonpositive width {channel}")

    require(open_rows["status"] == "SIX_HIGGS_KERNEL_ROWS_REMAIN_OPEN", "open obligation status mismatch")
    require(len(open_rows["rows"]) == 6, "expected six open kernel rows")
    require("H_to_gg" in open_rows["blocked_channels"], "gg open channel missing")
    require("H_to_ss" in open_rows["color_sensitive_open_channels"], "ss color-sensitive row missing")
    require("H_to_WW_star" in open_rows["electroweak_loop_or_offshell_open_channels"], "WW open channel missing")

    require(gate["full_channel_values_closed"] is False, "full channel values overclaimed")
    require(gate["full_covariance_profile_closed"] is False, "covariance overclaimed")
    require("full cross-channel Higgs covariance/profile likelihood" in updated["remaining_true_equivalence_blockers"], "covariance blocker missing")
    require("uniform precision Higgs partial-width formula rows" in updated["remaining_true_equivalence_blockers"], "uniform blocker missing")
    require(updated["guardrails"]["partial_kernel_rows_not_full_uniform_formula_set"] is True, "partial guard missing")

    for packet in [kernels, open_rows, gate, updated, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    require("H_to_bb" in note and "H_to_mu_mu" in note, "note missing filled channels")
    require("deliberately partial" in note, "note missing partial guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
