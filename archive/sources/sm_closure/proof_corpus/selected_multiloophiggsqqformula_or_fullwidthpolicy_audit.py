"""Audit the multiloop Higgs-to-quark formula scaffold."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_multiloophiggsqqformula_or_fullwidthpolicy"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
FORMULA = PACKET_DIR / "versioned_massless_qcd_higgs_qq_formula.packet.json"
VALUES = PACKET_DIR / "n3lo_qcd_higgs_qq_proxy_values.packet.json"
GATE = PACKET_DIR / "full_higgs_width_policy_gate.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_multiloop_qq_formula.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_MultiloopHiggsQQFormula_or_FullWidthPolicy_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_MULTILOOPHIGGSQQFORMULA_OR_FULLWIDTHPOLICY_BUILT_N3LO_QCD_QQ_PROXY_FULL_WIDTH_OPEN"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    formula = load(FORMULA)
    values = load(VALUES)
    gate = load(GATE)
    updated = load(UPDATED)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["closure_decision"]["qq_formula_scaffold_closed"] is True, "qq formula scaffold not closed")
    require(data["closure_decision"]["complete_Higgs_width_policy_closed"] is False, "complete width policy overclaimed")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "true equivalence overclaimed")

    require(formula["accepted_as_versioned_QCD_formula_scaffold"] is True, "formula scaffold not accepted")
    require(formula["accepted_as_full_width_policy"] is False, "full width policy overclaimed")
    require(formula["coefficients"]["c1"] == 17.0 / 3.0, "c1 mismatch")
    require(formula["coefficients"]["c2_nf5"] > 0.0, "c2 missing")
    require(formula["coefficients"]["c3_nf5"] > 0.0, "c3 missing")

    rows = values["rows"]
    require(len(rows) == 2, "expected b and c rows")
    require(values["summary"]["N3LO_exceeds_NLO_factor"] is True, "N3LO factor should exceed NLO")
    require(values["summary"]["all_widths_finite_nonnegative"] is True, "width positivity failed")
    require(values["accepted_as_multiloop_QCD_proxy_layer"] is True, "multiloop proxy not accepted")
    require(values["accepted_as_precision_SM_decay_widths"] is False, "precision width overclaimed")
    for row in rows:
        require(row["accepted_as_N3LO_massless_QCD_proxy"] is True, "row proxy flag missing")
        require(row["accepted_as_precision_SM_decay_width"] is False, "row overpromoted")
        require(row["qcd_factors"]["N3LO"] > row["qcd_factors"]["NLO"], "N3LO factor not larger than NLO")
        require(row["stage_widths_GeV"]["N3LO"] > row["stage_widths_GeV"]["NLO"], "N3LO width not larger than NLO")

    require(gate["precision_promotion_accepted"] is False, "gate overpromoted")
    require("complete channel set: tau, mu, WW*, ZZ*, gg, gamma gamma, Z gamma" in gate["still_required_before_precision_width_promotion"], "complete channel requirement missing")
    require("complete Higgs partial-width channel formula set" in updated["remaining_true_equivalence_blockers"], "channel blocker missing")
    require(updated["guardrails"]["qq_formula_scaffold_not_complete_higgs_width_policy"] is True, "guard missing")

    for packet in [formula, values, gate, updated, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    require("not a complete Higgs-width policy" in note, "note missing width-policy guard")
    require("downstream benchmark/QFT machinery" in note, "note missing downstream guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
