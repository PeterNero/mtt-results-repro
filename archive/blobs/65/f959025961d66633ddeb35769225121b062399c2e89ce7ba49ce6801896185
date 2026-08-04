"""Audit the gamma-gamma formula extension and QCD-threshold next gate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgsgammagammacorrection_or_qcdthresholdrows"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
GAMMA = PACKET_DIR / "higgs_gamma_gamma_all_charged_fermion_oneloop.packet.json"
PULL = PACKET_DIR / "gamma_gamma_pull_after_formula_extension.packet.json"
QCD = PACKET_DIR / "qcd_threshold_rows_next_gate.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsGammaGammaCorrection_or_QCDThresholdRows_v1.md"

STATUS = "MTT_SELECTED_HIGGSGAMMAGAMMACORRECTION_OR_QCDTHRESHOLDROWS_BUILT_ALL_CHARGED_ONELOOP_EXTENSION"
NEXT = "MTT_Selected_HiggsQCDThresholdRows_or_CorrelatedProfileFill_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    gamma = load(GAMMA)
    pull = load(PULL)
    qcd = load(QCD)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["target_fitting_used"] is False, "target fitting overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector guard missing")
    require(gamma["accepted_as_formula_extension"] is True, "formula extension not accepted")
    require(gamma["accepted_as_precision_formula_row"] is False, "precision overclaimed")
    particles = {row["particle"] for row in gamma["contributions"]}
    for particle in ["W", "t", "b", "c", "s", "u", "d", "tau", "mu", "e"]:
        require(particle in particles, f"missing loop contribution: {particle}")
    require(gamma["all_charged_one_loop_width_GeV"] > 0.0, "nonpositive width")
    require(pull["extension_selected_by_benchmark"] is False, "benchmark selector guard missing")
    require(pull["accepted_as_precision"] is False, "pull precision overclaim")
    require(pull["old_pull"] != pull["new_pull"], "extension did not change pull")
    require(qcd["status"] == "QCD_THRESHOLD_ROWS_SELECTED_AS_NEXT_GATE_VALUES_OPEN", "QCD next gate status mismatch")
    channels = {row["channel"] for row in qcd["rows"]}
    require(channels == {"H_to_ss", "H_to_gg"}, "QCD next rows mismatch")
    require(data["closure_decision"]["formula_extension_closed"] is True, "formula extension not closed")
    require(data["closure_decision"]["gamma_gamma_precision_promoted"] is False, "gamma precision overclaim")
    require(data["closure_decision"]["QCD_threshold_rows_closed"] is False, "QCD threshold overclaim")
    require(cert["next_required_artifact"] == NEXT, "next artifact mismatch")
    require("not fitted to the benchmark" in note, "note missing no-fit guard")
    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
