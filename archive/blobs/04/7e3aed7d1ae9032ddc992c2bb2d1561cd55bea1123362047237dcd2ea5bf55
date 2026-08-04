"""Audit accepted value-layer frontier / non-looping source rows artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_acceptedvaluelayerfrontier_or_nonloopingsourcerows"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
FRONTIER = PACKET_DIR / "accepted_value_layer_frontier.packet.json"
ATTACK_ORDER = PACKET_DIR / "nonlooping_attack_order.packet.json"
ROW_LEDGER = PACKET_DIR / "value_row_acceptance_ledger.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_AcceptedValueLayerFrontier_or_NonLoopingSourceRows_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_ACCEPTEDVALUELAYERFRONTIER_OR_NONLOOPINGSOURCEROWS_"
    "BUILT_LOOP_RETIRED_FIRST_VALUE_SOURCE_TARGET_OPEN"
)
NEXT = "MTT_Selected_ValueLayerFirstNonLoopingRowEmission_or_ThresholdImportExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    frontier = load(FRONTIER)
    attack = load(ATTACK_ORDER)
    ledger = load(ROW_LEDGER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(frontier["source_layer_closed"] is True, "source layer not closed")
    require(
        frontier["prior_dynamic_qasu3_replay_already_in_value_chain"] is True,
        "prior dynamic replay not detected",
    )
    require(frontier["vsd01_next_points_to_forward_frontier"] is True, "VSD01 handoff not redirected")
    require(frontier["upstream_replay_retired_as_next_target"] is True, "loop not retired")
    require(frontier["current_frontier"] == "accepted SM value-source rows", "wrong frontier")
    require(frontier["closed_inputs"]["VSD01_source_assembly_subgate_closed"] is True, "VSD01 source not closed")
    require(frontier["closed_inputs"]["VSD01_dynamic_overlap_subgate_closed"] is True, "VSD01 dynamic not closed")
    require(frontier["closed_inputs"]["common_scale_values_for_SM_parity"] is True, "common-scale support missing")
    require(frontier["closed_inputs"]["obligation_kernel_closed"] is True, "obligation kernel missing")
    require(frontier["closed_inputs"]["first_primitive_exactness_backimported"] is True, "primitive backimport missing")
    for value in frontier["not_closed_as_values"].values():
        require(value is True, "value-layer open flag should remain true")
    for key, value in frontier["guardrails"].items():
        if key in ["observed_data_used_as_selector", "target_fitting_used", "diagnostic_or_surrogate_rows_can_close_source_selection", "upstream_dynamic_replay_can_be_reused_as_next_target"]:
            require(value is False, f"guardrail should be false: {key}")
    require(frontier["closure_claimed"] is False, "frontier overclaimed")

    require(ledger["kernel_required_row_count"] == 5, "wrong required row count")
    require(ledger["kernel_closed_row_count"] == 0, "value rows overclosed")
    require(ledger["accepted_external_rows_present"] is False, "external rows overimported")
    require(ledger["first_numeric_payload_emitted"] is True, "first numeric payload missing")
    require(ledger["first_numeric_payload_accepted_as_selected_source"] is False, "first row overpromoted")
    require(ledger["first_primitive_exactness_backimported"] is True, "first primitive not backimported")
    require(ledger["first_primitive_promoted_to_selected_dynamic_source"] is False, "primitive overpromoted")
    require(ledger["zero_rows_accepted_for_true_value_closure"] is True, "zero-accepted-row guard missing")

    require(attack["recommended_next_artifact"] == NEXT, "attack next mismatch")
    require(len(attack["next_attack_order"]) == 3, "wrong attack order length")
    require(attack["next_attack_order"][0]["target"] == "VSD-01-selected-overlap-value-kernel", "wrong first target")
    require("upstream DynamicQaSU3 first-response replay" in attack["do_not_reopen"], "do-not-reopen guard missing")
    require(attack["observed_data_used_as_selector"] is False, "attack observed selector used")
    require(attack["target_fitting_used"] is False, "attack target fitting used")

    closes = data["what_closes_now"]
    for key in [
        "loop_back_to_dynamic_QaSU3_retired",
        "accepted_value_layer_frontier_frozen",
        "value_row_acceptance_ledger_built",
        "first_nonlooping_attack_order_selected",
        "observed_constants_excluded_as_selectors",
    ]:
        require(closes[key] is True, f"close flag missing: {key}")
    remains = data["what_remains_open"]
    for key in [
        "accepted_Yukawa_magnitudes_for_true_precision",
        "running_mass_ratios",
        "CKM_PMNS_measured_value_closure",
        "lambda_H_threshold_rows",
        "accepted_threshold_mass_scheme_source_rows",
        "no_knob_value_source_derivation",
        "full_correlated_likelihood_source",
    ]:
        require(remains[key] is True, f"remaining flag missing: {key}")
    require(data["readiness"]["source_layer_closed"] is True, "readiness source layer not closed")
    require(data["readiness"]["value_layer_required_rows"] == 5, "readiness required rows mismatch")
    require(data["readiness"]["value_layer_accepted_source_rows"] == 0, "readiness overaccepted")
    require(data["readiness"]["first_numeric_payload_available_but_unpromoted"] is True, "first payload state mismatch")
    require(data["closure_claimed"] is False, "candidate closure overclaimed")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("solved-layer loop" in note, "note missing loop guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
