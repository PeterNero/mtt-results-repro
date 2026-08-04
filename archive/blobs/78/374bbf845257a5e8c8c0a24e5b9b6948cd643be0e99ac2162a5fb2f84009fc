"""Audit external literature RG benchmark values and threshold/covariance gap."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_externalliteraturergbenchmarkvalues_or_thresholdcovariance"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
LIT = PACKET_DIR / "external_literature_rg_benchmark_values.packet.json"
COMPARE = PACKET_DIR / "literature_vs_local_convention_comparison.packet.json"
UPDATED = PACKET_DIR / "threshold_covariance_gap_after_literature_benchmark.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ExternalLiteratureRGBenchmarkValues_or_ThresholdCovariance_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_EXTERNALLITERATURERGBENCHMARKVALUES_OR_THRESHOLDCOVARIANCE_BUILT_LIT_VALUES_FILLED_THRESHOLDS_OPEN"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    lit = load(LIT)
    compare = load(COMPARE)
    updated = load(UPDATED)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(lit["filled_external_literature_values"] is True, "literature values not filled")
    require(lit["accepted_as_external_literature_benchmark_reference"] is True, "literature reference not accepted")
    require(lit["accepted_as_full_precision_match"] is False, "full precision match overclaimed")
    require(lit["source"]["arxiv"] == "1307.3536", "source arxiv mismatch")

    vals = lit["literature_values"]
    for key in ["lambda_Mt", "y_t_Mt", "g_2_Mt", "g_Y_Mt", "g_1_GUT_Mt", "g_3_Mt"]:
        require(key in vals, f"missing literature value: {key}")
        require(math.isfinite(vals[key]["central_value"]), f"nonfinite literature value: {key}")
    require(abs(vals["g_1_GUT_Mt"]["central_value"] - math.sqrt(5.0 / 3.0) * vals["g_Y_Mt"]["central_value"]) < 1e-15, "GUT normalization mismatch")

    require(compare["all_deltas_finite"] is True, "nonfinite comparison delta")
    require(compare["comparison_closes"]["external_literature_values_filled"] is True, "comparison does not close literature values")
    require(compare["comparison_closes"]["full_precision_agreement_claimed"] is False, "precision agreement overclaimed")
    require(compare["comparison_closes"]["threshold_and_pole_matching_needed"] is True, "threshold gap not retained")
    require(len(compare["comparison_rows"]) >= 7, "comparison rows incomplete")
    require(compare["max_absolute_delta"] > 0.0, "comparison unexpectedly zero")

    require(updated["closed_now"] == ["external literature RG benchmark values"], "closed_now mismatch")
    require("external literature RG benchmark values" in updated["previous_true_equivalence_blockers"], "previous blocker missing")
    require("external literature RG benchmark values" not in updated["remaining_true_equivalence_blockers"], "external blocker not removed")
    require("literature/local convention agreement after threshold maps" in updated["remaining_true_equivalence_blockers"], "threshold agreement blocker missing")
    require(updated["new_primary_value_gate"] == "precision threshold and pole-to-running maps", "new primary gate mismatch")
    require(updated["guardrails"]["true_SM_equivalence_closed"] is False, "true equivalence overclaimed")
    require(updated["guardrails"]["no_knob_closed"] is False, "no-knob overclaimed")
    require(updated["guardrails"]["external_values_are_downstream_benchmark_not_source_selector"] is True, "source selector guard missing")

    for key in [
        "external_literature_rg_benchmark_values_filled",
        "literature_vs_local_convention_comparison_built",
        "threshold_covariance_gap_identified",
        "superset_strategy_preserved",
    ]:
        require(data["what_closes_now"][key] is True, f"missing close flag: {key}")
    require(data["closure_decision"]["SM_parity_closed"] is True, "SM parity flag mismatch")
    require(data["closure_decision"]["external_literature_rg_values_filled"] is True, "lit values flag mismatch")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "candidate true equivalence overclaimed")
    require(data["closure_decision"]["no_knob_closed"] is False, "candidate no-knob overclaimed")
    require(cert["next_required_artifact"] == "MTT_Selected_ThresholdPoleRunningMaps_or_CovarianceProfileValues_v1", "next artifact mismatch")

    for packet in [lit, compare, updated, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    require("Buttazzo" in note, "note missing literature source")
    require("threshold matching" in note, "note missing threshold gap")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
