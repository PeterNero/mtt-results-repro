"""Audit CONST-EW-02 B45 universal-primitive portfolio handoff packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b45_universal_primitive_portfolio_handoff"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
BUDGET = BASE / "universal_primitive_budget_status.packet.json"
SWITCH = BASE / "cross_constant_switch_rule.packet.json"
NEXT_CONSTANT = BASE / "next_constant_priority.packet.json"
BOUNDARY = BASE / "weak_mixing_b45_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EW_02_WeakMixing_B45_UniversalPrimitivePortfolioHandoff_v1.md"

STATUS = "MTT_CONST_EW_02_B45_UNIVERSAL_PRIMITIVE_PORTFOLIO_HANDOFF_BUILT"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def clean(packet: dict[str, object], name: str) -> None:
    require(packet["observed_data_used_as_selector"] is False, f"{name} observed selector")
    require(packet["target_fitting_used"] is False, f"{name} target fitting")
    require(packet["closure_claimed"] is False, f"{name} closure overclaim")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    require(computed["status"] == STATUS, "builder status mismatch")

    candidate = load(DATA)
    budget = load(BUDGET)
    switch = load(SWITCH)
    next_constant = load(NEXT_CONSTANT)
    boundary = load(BOUNDARY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("budget", budget),
        ("switch", switch),
        ("next_constant", next_constant),
        ("boundary", boundary),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["weak_mixing_down_to_one_shared_primitive_tier"] is True, "one primitive tier")
    require(candidate["recommend_cross_constant_next"] is True, "cross constant")
    require(candidate["selected_next_constant"] == "CONST-GR-01 / ABSOLUTE-SCALE-GN", "selected next")
    require(candidate["physical_weak_angle_closure"] is False, "weak angle overclosed")
    require(candidate["strict_full_no_knob_closure"] is False, "strict overclosed")

    global_budget = budget["global_budget"]
    require(global_budget["desired_eventual_universal_primitives"] == "1..3", "budget range")
    require(global_budget["current_weak_mixing_specific_new_parameters"] == 0, "weak-specific parameters")
    require(global_budget["current_shared_physical_primitives_needed_for_alpha_and_weak_mixing"] == 1, "shared primitive count")
    require(global_budget["selected_numeric_primitive_values_now"] == 0, "selected values")
    evidence = budget["evidence"]
    require(evidence["alpha_one_primitive_extension_ready"] is True, "alpha primitive")
    require(evidence["weak_mixing_one_primitive_contract_closed"] is True, "weak primitive")
    require(evidence["weak_mixing_conditional_profile_execution_closed"] is True, "profile")

    decision = switch["decision"]
    require(decision["weak_mixing_has_met_switch_threshold"] is True, "switch threshold")
    require(decision["keep_strict_B45_QaStack_as_open_upgrade"] is True, "parking strict")
    require(decision["recommend_cross_constant_next"] is True, "switch next")
    require(decision["weak_mixing_physical_closure_claimed"] is False, "switch weak closure")
    require("add a weak-angle-specific primitive after B42" in switch["rule"]["forbidden"], "forbid weak primitive")

    require(next_constant["selected_next"]["label"] == "CONST-GR-01 / ABSOLUTE-SCALE-GN", "next label")
    require(next_constant["selected_next"]["primitive_class"] == "UP-ABS-SCALE", "next primitive class")
    require(len(next_constant["ranked_next_constants"]) == 3, "ranked constants")

    closed = boundary["closed_or_decided_now"]
    require(closed["universal_primitive_budget_visible"] is True, "boundary budget")
    require(closed["weak_mixing_down_to_one_shared_primitive_tier"] is True, "boundary one primitive")
    require(closed["cross_constant_switch_rule"] is True, "boundary switch")
    require(closed["next_constant_priority_selected"] is True, "boundary next")
    require(boundary["still_open"]["strict_QaStack_threshold_vector"] is True, "strict threshold open")
    require(boundary["still_open"]["physical_weak_angle_numerical_closure"] is True, "physical weak open")
    require("not adding another weak-mixing parameter" in boundary["anti_cycle_delta_from_B44"]["not_repeated"], "anti-cycle")

    require(next_work["primary"]["label"] == "CONST-GR-01 / ABSOLUTE-SCALE-GN / G1-SHARED-PRIMITIVE-SOURCE-SEARCH", "primary")
    require(next_work["parking_lot"]["label"] == "CONST-EW-02 / WEAK-MIXING / B45-QASTACK-QUOTIENTFUNCTOR-ABASE-IDENTITY-ATTEMPT", "parking")

    require(cert["status"] == STATUS, "cert status")
    require(cert["recommend_cross_constant_next"] is True, "cert next")
    require(cert["physical_weak_angle_closure"] is False, "cert weak")
    require(cert["strict_full_no_knob_closure"] is False, "cert strict")
    require("B45" in note and "1..3" in note and "handoff-ready" in note, "note")

    print("CONST-EW-02 B45 universal-primitive portfolio handoff audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
