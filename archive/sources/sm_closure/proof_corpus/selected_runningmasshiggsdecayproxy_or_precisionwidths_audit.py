"""Audit running-mass Higgs decay proxy values."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_runningmasshiggsdecayproxy_or_precisionwidths"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
RUNNING = PACKET_DIR / "one_loop_running_mass_higgs_decay_proxy.packet.json"
BENCH = PACKET_DIR / "higgs_decay_plausibility_benchmark.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_running_mass_proxy.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_RunningMassHiggsDecayProxy_or_PrecisionWidths_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_RUNNINGMASSHIGGSDECAYPROXY_OR_PRECISIONWIDTHS_BUILT_RUNNING_MASS_PROXY_PRECISION_OPEN"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    running = load(RUNNING)
    bench = load(BENCH)
    updated = load(UPDATED)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["closure_decision"]["running_mass_proxy_layer_closed"] is True, "proxy layer not closed")
    require(data["closure_decision"]["full_precision_Higgs_widths_closed"] is False, "precision width overclaimed")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "true equivalence overclaimed")

    rows = running["rows"]
    require(len(rows) == 2, "expected b and c rows")
    by_f = {row["fermion"]: row for row in rows}
    require(set(by_f) == {"b", "c"}, "unexpected running-mass rows")
    require(running["summary"]["all_running_mass_proxy_widths_finite_nonnegative"] is True, "width positivity failed")
    require(running["summary"]["running_masses_reduce_widths_vs_reference_mass_proxy"] is True, "running masses should decrease")
    require(running["alpha_s_values"]["alpha_s_mH_proxy"] < running["alpha_s_values"]["alpha_s_MZ_input"], "alpha_s should decrease from MZ to mH")
    require(by_f["b"]["running_mass_qcd_proxy_width_GeV"] > by_f["c"]["running_mass_qcd_proxy_width_GeV"], "bb should exceed cc")
    for row in rows:
        require(row["accepted_as_running_mass_proxy"] is True, "row not accepted as proxy")
        require(row["accepted_as_precision_SM_decay_width"] is False, "row overpromoted")
        require(row["running_mass_at_mH_GeV"] < row["reference_mass_GeV"], "mass was not reduced")

    require(bench["not_used_for_fit"] is True, "benchmark should not be fit")
    require(bench["observed_data_used_as_selector"] is False, "benchmark selector violation")
    require(bench["plausibility_result"] == "RUNNING_MASS_PROXY_IN_CORRECT_ORDER_OF_MAGNITUDE_FOR_HIGGS_QUARK_WIDTHS", "plausibility result mismatch")
    require(0.5 < bench["proxy_comparison"]["b"]["ratio_proxy_to_reference_approx"] < 2.0, "bb proxy implausible ratio")
    require(0.5 < bench["proxy_comparison"]["c"]["ratio_proxy_to_reference_approx"] < 2.0, "cc proxy implausible ratio")

    require(updated["guardrails"]["running_mass_proxy_is_not_full_precision_width"] is True, "precision guard missing")
    require("multiloop running-mass Higgs decay widths" in updated["remaining_true_equivalence_blockers"], "multiloop blocker missing")
    require("actual selected Qa/SU3 operator packet" in updated["remaining_true_equivalence_blockers"], "Qa/SU3 blocker missing")

    for packet in [running, bench, updated, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    require("not precision-plausible" in note, "note missing plausibility correction")
    require("remains a proxy" in note, "note missing proxy guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
