"""Audit first-pass non-fit Higgs QCD formula execution and forward replay."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgsqcdnonfitformulavalueexecution_or_forwardreplay"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
EXECUTION = PACKET_DIR / "higgs_qcd_nonfit_formula_execution.packet.json"
REPLAY = PACKET_DIR / "higgs_qcd_forward_replay_after_nonfit_formula_execution.packet.json"
PROMOTION = PACKET_DIR / "higgs_qcd_formula_value_promotion_status.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsQCDNonFitFormulaValueExecution_or_ForwardReplay_v1.md"

STATUS = "MTT_SELECTED_HIGGSQCDNONFITFORMULAVALUEEXECUTION_OR_FORWARDREPLAY_BUILT_FIRSTPASS_VALUES_PRECISION_OPEN"
NEXT = "MTT_Selected_HiggsQCDPrecisionThresholdRows_or_CorrelatedProfileUpgrade_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    execution = load(EXECUTION)
    replay = load(REPLAY)
    promotion = load(PROMOTION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["target_fitting_used"] is False, "target fitting guard missing")
    require(data["observed_data_used_as_selector"] is False, "observed selector guard missing")
    require(execution["channels"] == ["H_to_ss", "H_to_gg"], "execution channels mismatch")
    require(execution["benchmarks_used_in_execution"] is False, "benchmarks leaked into execution")
    require(execution["benchmark_over_proxy_ratios_applied"] is False, "benchmark ratios applied")
    require(execution["accepted_formula_value_count"] == 2, "formula value count mismatch")
    require(execution["accepted_as_precision_formula_values"] is False, "precision overclaimed")
    require(execution["all_widths_finite_nonnegative"] is True, "invalid formula widths")
    require(replay["summary"]["row_count"] == 2, "replay row count mismatch")
    require(replay["summary"]["all_benchmarks_compared_after_execution"] is True, "forward replay order missing")
    require(replay["summary"]["any_benchmark_used_as_selector"] is False, "benchmark selector violation")
    require(promotion["firstpass_nonfit_formula_values_filled"] is True, "first-pass values not filled")
    require(promotion["formula_repair_values_filled_at_precision_tier"] is False, "precision repair overfilled")
    require(promotion["values_promotable_to_precision_now"] is False, "values overpromoted")
    require(promotion["qasu3_attachment_closed_for_sm_parity"] is True, "Qa/SU3 parity attachment missing")
    require(promotion["qasu3_attachment_closed_as_no_knob"] is False, "Qa/SU3 no-knob overclaimed")
    require(data["closure_decision"]["firstpass_nonfit_formula_values_filled"] is True, "candidate first-pass closure missing")
    require(data["closure_decision"]["forward_replay_executed"] is True, "candidate replay missing")
    require(data["closure_decision"]["precision_formula_values_filled"] is False, "candidate precision overclaimed")
    require(cert["next_required_artifact"] == NEXT, "next artifact mismatch")
    require("Benchmark/proxy ratios are not applied" in note, "note missing fit-factor guard")
    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
