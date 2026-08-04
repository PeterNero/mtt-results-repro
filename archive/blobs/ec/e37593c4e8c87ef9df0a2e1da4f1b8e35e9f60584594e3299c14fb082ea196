"""Audit the precision-observable promotion policy."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_precisionobservablepromotionpolicy_or_loopqftvalues"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
POLICY = PACKET_DIR / "precision_observable_promotion_policy.packet.json"
MATRIX = PACKET_DIR / "observable_tier_promotion_matrix.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_promotion_policy.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PrecisionObservablePromotionPolicy_or_LoopQFTValues_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_PRECISIONOBSERVABLEPROMOTIONPOLICY_OR_LOOPQFTVALUES_BUILT_POLICY_LOOP_VALUES_OPEN"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    policy = load(POLICY)
    matrix = load(MATRIX)
    updated = load(UPDATED)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["closure_decision"]["promotion_policy_closed"] is True, "promotion policy not closed")
    require(data["closure_decision"]["precision_loop_QFT_values_closed"] is False, "loop values overclaimed")
    require(data["closure_decision"]["actual_QaSU3_operator_packet_closed"] is False, "Qa/SU3 overclaimed")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "true SM equivalence overclaimed")

    require(policy["hard_guards"]["tree_identity_does_not_imply_precision_equivalence"] is True, "tree guard missing")
    require(policy["hard_guards"]["representative_decay_does_not_imply_loop_width"] is True, "decay guard missing")
    require(policy["hard_guards"]["literature_benchmark_does_not_select_MTT_source"] is True, "source guard missing")
    require("precision_loop_QFT_observable" in policy["promotion_requirements"], "precision tier requirements missing")

    require(matrix["all_current_rows_classified"] is True, "rows not classified")
    require(matrix["any_row_promoted_to_true_precision_equivalence"] is False, "precision promotion overclaimed")
    require(matrix["row_counts"]["tree_identity_rows"] == 5, "tree identity count mismatch")
    require(matrix["row_counts"]["higgs_tree_decay_rows"] == 5, "Higgs decay count mismatch")
    require(matrix["row_counts"]["w_tree_decay_rows"] == 3, "W decay count mismatch")
    tiers = {row["tier"]: row for row in matrix["tiers"]}
    for tier in [
        "tree_identity_rows",
        "representative_tree_decay_rows",
        "RG_and_threshold_benchmark_rows",
        "correlated_profile_rows",
        "actual_QaSU3_operator_sensitive_rows",
    ]:
        require(tier in tiers, f"tier missing: {tier}")
        require(tiers[tier]["accepted_for_true_precision_equivalence"] is False, f"tier overpromoted: {tier}")

    require(updated["guardrails"]["policy_closes_classification_not_values"] is True, "classification guard missing")
    require(updated["guardrails"]["no_tree_row_promoted_to_precision"] is True, "tree precision guard missing")
    require("loop-corrected local QFT correlator/S-matrix/decay rows" in updated["remaining_true_equivalence_blockers"], "loop blocker missing")
    require("actual selected Qa/SU3 operator packet" in updated["remaining_true_equivalence_blockers"], "Qa/SU3 blocker missing")

    for packet in [policy, matrix, updated, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    require("cannot be silently promoted" in note, "note missing promotion guard")
    require("not the loop-corrected values" in note, "note missing value-open guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
