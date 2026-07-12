"""Audit one-loop QCD proxy values for Higgs quark decay rows."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_loopqcddecayproxyvalues_or_fullprecisionqft"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
QCD = PACKET_DIR / "one_loop_qcd_higgs_quark_decay_proxy_values.packet.json"
MISSING = PACKET_DIR / "full_precision_decay_width_missing_terms.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_qcd_proxy.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_LoopQCDDecayProxyValues_or_FullPrecisionQFT_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_LOOPQCDDECAYPROXYVALUES_OR_FULLPRECISIONQFT_BUILT_QCD_PROXY_FULL_PRECISION_OPEN"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    qcd = load(QCD)
    missing = load(MISSING)
    updated = load(UPDATED)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["closure_decision"]["first_loop_QFT_proxy_layer_closed"] is True, "proxy layer not closed")
    require(data["closure_decision"]["full_precision_QFT_values_closed"] is False, "full precision overclaimed")
    require(data["closure_decision"]["actual_QaSU3_operator_packet_closed"] is False, "Qa/SU3 overclaimed")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "true equivalence overclaimed")

    rows = qcd["qcd_rows"]
    require(len(rows) == 2, "expected b and c open quark proxy rows")
    require(qcd["summary"]["qcd_corrected_open_quark_channels_count"] == 2, "summary row count mismatch")
    require(qcd["summary"]["all_proxy_widths_finite_nonnegative"] is True, "proxy width positivity failed")
    require(qcd["summary"]["proxy_increases_positive_quark_widths"] is True, "QCD factor should increase positive widths")
    require(qcd["summary"]["qcd_k_factor"] > 1.0, "QCD K factor should exceed unity")
    for row in rows:
        require(row["accepted_as_one_loop_qcd_proxy"] is True, "proxy row not accepted")
        require(row["accepted_as_precision_SM_decay_width"] is False, "proxy row overpromoted")
        require(row["qcd_proxy_width_GeV"] > row["tree_width_GeV"], "proxy width not larger than tree")
        require(row["alpha_s_input"]["used_as_source_selector"] is False, "alpha_s selector violation")

    require(qcd["accepted_as_first_loop_QFT_value_layer"] is True, "first loop layer not accepted")
    require(qcd["accepted_as_full_precision_decay_widths"] is False, "full precision widths overclaimed")
    require(missing["full_precision_widths_closed"] is False, "missing terms packet overclaimed closure")
    require("running quark masses at the declared scale" in missing["terms_required_before_precision_promotion"], "running mass term missing")
    require("full precision loop-corrected QFT correlator/S-matrix/decay rows" in updated["remaining_true_equivalence_blockers"], "full precision blocker missing")
    require(updated["guardrails"]["qcd_proxy_is_not_full_precision_width"] is True, "proxy guard missing")

    for packet in [qcd, missing, updated, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    require("not a full precision Higgs-width computation" in note, "note missing precision guard")
    require("alpha_s(M_Z)" in note, "note missing alpha_s convention")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
