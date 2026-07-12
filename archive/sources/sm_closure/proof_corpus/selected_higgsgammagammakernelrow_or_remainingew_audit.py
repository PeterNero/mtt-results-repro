"""Audit the executable H->gamma gamma proxy kernel row."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgsgammagammakernelrow_or_remainingew"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
GAMMA = PACKET_DIR / "higgs_gamma_gamma_oneloop_kernel_row.packet.json"
EXTENDED = PACKET_DIR / "extended_executable_higgs_kernel_rows_after_gamma_gamma.packet.json"
OPEN = PACKET_DIR / "remaining_electroweak_higgs_kernel_obligations_after_gamma_gamma.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_gamma_gamma_kernel.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsGammaGammaKernelRow_or_RemainingEW_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_HIGGSGAMMAGAMMAKERNELROW_OR_REMAININGEW_BUILT_GAMMAGAMMA_KERNEL_THREE_EW_ROWS_OPEN"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    gamma = load(GAMMA)
    extended = load(EXTENDED)
    open_rows = load(OPEN)
    updated = load(UPDATED)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["closure_decision"]["H_to_gamma_gamma_proxy_kernel_closed"] is True, "gamma gamma row not closed")

    require(gamma["channel"] == "H_to_gamma_gamma", "wrong channel")
    require(gamma["accepted_as_uniform_kernel_row"] is True, "gamma gamma not accepted as proxy kernel row")
    require(gamma["accepted_as_precision_formula_row"] is False, "gamma gamma precision overclaimed")
    require(gamma["width_GeV"] > 0.0, "gamma gamma width must be positive")
    require(gamma["tau_W"] > 1.0 and gamma["tau_t"] > 1.0, "real loop proxy expects tau >= 1")
    require(gamma["A_W"] < 0.0 and gamma["A_top_spin_half"] > 0.0, "expected W/top amplitude signs missing")
    require(abs(gamma["relative_residual_to_benchmark_fill"]) < 0.25, "gamma gamma residual unexpectedly large")

    executable = extended["executable_rows"]
    require(extended["summary"]["executable_kernel_row_count"] == 7, "expected seven executable rows")
    require(extended["summary"]["open_kernel_row_count"] == 3, "expected three open rows")
    require(extended["summary"]["all_executable_widths_positive"] is True, "nonpositive executable width")
    require(any(row["channel"] == "H_to_gamma_gamma" for row in executable), "extended packet missing gamma gamma")
    require(extended["summary"]["uniform_formula_rows_fully_filled"] is False, "full formula rows overclaimed")

    require(open_rows["status"] == "THREE_ELECTROWEAK_HIGGS_KERNEL_ROWS_REMAIN_OPEN", "open status mismatch")
    require(len(open_rows["rows"]) == 3, "expected three open rows")
    require("H_to_gamma_gamma" not in open_rows["blocked_channels"], "gamma gamma should no longer be blocked")
    for channel in ["H_to_WW_star", "H_to_ZZ_star", "H_to_Z_gamma"]:
        require(channel in open_rows["blocked_channels"], f"missing EW blocker {channel}")

    require("WW*, ZZ*, and Z gamma" in updated["next_primary_value_gate"], "next gate should point to remaining EW rows")
    require(updated["guardrails"]["gamma_gamma_kernel_not_precision"] is True, "gamma guard missing")

    for packet in [gamma, extended, open_rows, updated, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    require("H_to_gamma_gamma" in note, "note missing gamma gamma")
    require("not a precision" in note, "note missing precision guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
