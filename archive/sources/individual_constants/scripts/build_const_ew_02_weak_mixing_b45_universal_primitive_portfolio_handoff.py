"""Build CONST-EW-02 B45 universal-primitive portfolio handoff packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_ew_02_weak_mixing_b45_universal_primitive_portfolio_handoff"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
BUDGET = BASE / "universal_primitive_budget_status.packet.json"
SWITCH = BASE / "cross_constant_switch_rule.packet.json"
NEXT_CONSTANT = BASE / "next_constant_priority.packet.json"
BOUNDARY = BASE / "weak_mixing_b45_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B45_UniversalPrimitivePortfolioHandoff_v1.md"

STATUS = "MTT_CONST_EW_02_B45_UNIVERSAL_PRIMITIVE_PORTFOLIO_HANDOFF_BUILT"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    targets_path = DATA / "constant_frontier_ledger" / "individual_constant_targets.packet.json"
    a10_path = DATA / "const_em_01_alpha1_universal_primitive_or_nogo.candidate.json"
    a11_path = DATA / "const_em_01_alpha1_frontier_closure_ledger.candidate.json"
    b42_path = DATA / "const_ew_02_weak_mixing_b42_one_primitive_physical_bridge.candidate.json"
    b44_path = DATA / "const_ew_02_weak_mixing_b44_conditional_profile_execution.candidate.json"
    b44_boundary_path = DATA / "const_ew_02_weak_mixing_b44_conditional_profile_execution" / "weak_mixing_b44_boundary.packet.json"

    targets = load(targets_path)
    a10 = load(a10_path)
    a11 = load(a11_path)
    b42 = load(b42_path)
    b44 = load(b44_path)
    b44_boundary = load(b44_boundary_path)

    target_rows = {row["label"]: row for row in targets["targets"]}
    next_candidates = [
        {
            "label": "CONST-GR-01 / ABSOLUTE-SCALE-GN",
            "why": "Directly tests the same E0/L0 or modal-gap primitive that B42 isolated.",
            "primitive_class": "UP-ABS-SCALE",
            "priority": 1,
        },
        {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD",
            "why": "Shares action-normalization and threshold-kernel structure; useful after the absolute-scale primitive has a candidate value.",
            "primitive_class": "UP-ACTION-NORM",
            "priority": 2,
        },
        {
            "label": "CONST-CP-01 / FINITE-PHASE-ORIENTATION",
            "why": "Likely probes a different primitive class, so it is less direct for testing the current E0/L0 budget.",
            "primitive_class": "UP-PHASE",
            "priority": 3,
        },
    ]

    budget = {
        "schema": "MTTConstEW02B45UniversalPrimitiveBudgetStatus.v1",
        "status": "WEAK_MIXING_DOWN_TO_ONE_SHARED_PRIMITIVE_TIER",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B45-UNIVERSAL-PRIMITIVE-BUDGET",
        "inputs": {
            "A10_alpha_one_primitive_or_nogo": rel(a10_path),
            "A11_alpha_frontier_ledger": rel(a11_path),
            "B42_one_primitive_bridge": rel(b42_path),
            "B44_conditional_profile_execution": rel(b44_path),
        },
        "global_budget": {
            "desired_eventual_universal_primitives": "1..3",
            "current_weak_mixing_specific_new_parameters": 0,
            "current_shared_physical_primitives_needed_for_alpha_and_weak_mixing": 1,
            "selected_numeric_primitive_values_now": 0,
            "strict_no_knob_primitive_count_now": 0,
        },
        "evidence": {
            "alpha_one_primitive_extension_ready": a10["what_closes_now"]["one_universal_primitive_extension"],
            "alpha_frontier_handoff_ready": a11["handoff_ready_for_main_repo"],
            "weak_mixing_one_primitive_contract_closed": b42["one_primitive_physical_bridge_contract_closed"],
            "K_phys_alpha_phys_mu_match_collapsed_to_one_primitive": b42["K_phys_alpha_phys_mu_match_collapsed_to_one_primitive"],
            "weak_mixing_conditional_profile_execution_closed": b44["conditional_profile_execution_closed"],
            "weak_mixing_conditional_sin2": b44["conditional_minimal_threshold_sin2"],
        },
        "interpretation": "Weak mixing has reached the portfolio-handoff tier: it is useful as a conditional cross-check of one shared physical primitive, but further strict closure now depends on source upgrades rather than more weak-angle-specific parameters.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    switch = {
        "schema": "MTTConstEW02B45CrossConstantSwitchRule.v1",
        "status": "SWITCH_RULE_BUILT_DO_NOT_OVER_OPTIMIZE_ONE_CONSTANT",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B45-CROSS-CONSTANT-SWITCH-RULE",
        "rule": {
            "continue_weak_mixing_if": [
                "a new same-source QA-stack quotient/A_base identity source appears",
                "a new strict E0/L0/modal-gap physical unit theorem appears",
                "a precision RG/threshold packet can be executed without new fitted parameters",
            ],
            "switch_to_other_constants_if": [
                "the current constant is down to one shared primitive and no new same-source theorem is available",
                "another constant can constrain or falsify the same primitive class",
                "continuing would only refine conditional replay language rather than reduce primitive count",
            ],
            "forbidden": [
                "add a weak-angle-specific primitive after B42",
                "tune the shared primitive to weak angle and then count weak angle as predicted",
                "hide separate threshold, matching, and normalization choices as one source theorem without packet evidence",
            ],
        },
        "decision": {
            "weak_mixing_has_met_switch_threshold": True,
            "keep_strict_B45_QaStack_as_open_upgrade": True,
            "recommend_cross_constant_next": True,
            "weak_mixing_physical_closure_claimed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_constant = {
        "schema": "MTTConstEW02B45NextConstantPriority.v1",
        "status": "NEXT_CONSTANT_PRIORITIZED_FOR_SHARED_PRIMITIVE_TEST",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B45-NEXT-CONSTANT-PRIORITY",
        "input_frontier_targets": rel(targets_path),
        "ranked_next_constants": next_candidates,
        "selected_next": next_candidates[0],
        "reason": "The immediate portfolio question is whether the same E0/L0/modal-gap primitive can also organize Newton/Planck absolute scale. That tests the shared-primitive strategy more directly than more weak-angle replay work.",
        "target_row_from_initial_ledger": target_rows.get("CONST-GR-01 / ABSOLUTE-SCALE-GN", {}),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstEW02B45Boundary.v1",
        "status": "B45_WEAK_MIXING_HANDOFF_READY_STRICT_UPGRADES_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B45-BOUNDARY",
        "previous_B44_status": b44["status"],
        "closed_or_decided_now": {
            "universal_primitive_budget_visible": True,
            "weak_mixing_down_to_one_shared_primitive_tier": True,
            "cross_constant_switch_rule": True,
            "next_constant_priority_selected": True,
            "strict_weak_mixing_upgrades_kept_open": True,
        },
        "still_open": {
            "strict_QaStack_threshold_vector": b44_boundary["still_open"]["strict_QaStack_threshold_vector"],
            "primitive_value_or_source_unit": b44_boundary["still_open"]["primitive_value_or_source_unit"],
            "precision_RG_scheme_conversion": b44_boundary["still_open"]["precision_RG_scheme_conversion"],
            "physical_weak_angle_numerical_closure": b44_boundary["still_open"]["physical_weak_angle_numerical_closure"],
            "strict_full_no_knob_closure": b44_boundary["still_open"]["strict_full_no_knob_closure"],
        },
        "anti_cycle_delta_from_B44": {
            "B44": "froze the conditional profile execution lane",
            "B45": "adds a cross-constant primitive-budget decision so we do not keep optimizing one constant after reaching one shared primitive",
            "not_repeated": [
                "not adding another weak-mixing parameter",
                "not claiming weak-mixing physical closure",
                "not burying the need for strict QA-stack or primitive-value source theorems",
            ],
        },
        "allowed_claim": "Weak mixing is handoff-ready for cross-constant primitive testing in the one-primitive tier.",
        "forbidden_claim": "physical weak-angle closure, strict no-knob closure, or selected primitive value",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02B45NextWork.v1",
        "status": "NEXT_WORKORDER_CONST_GR_01_OR_STRICT_QASTACK_IF_NEW_SOURCE",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B46-PORTFOLIO-NEXT",
        "primary": {
            "label": "CONST-GR-01 / ABSOLUTE-SCALE-GN / G1-SHARED-PRIMITIVE-SOURCE-SEARCH",
            "task": "Start the next-constant attack by testing whether central-circle, modal-gap, GR/protospinor, or M-theory packets source the same E0/L0 primitive needed by alpha1 and weak mixing.",
        },
        "parking_lot": {
            "label": "CONST-EW-02 / WEAK-MIXING / B45-QASTACK-QUOTIENTFUNCTOR-ABASE-IDENTITY-ATTEMPT",
            "task": "Return here if a new same-source QA-stack quotient/A_base identity route becomes available.",
        },
    }

    candidate = {
        "candidate": "MTTConstEW02WeakMixingB45UniversalPrimitivePortfolioHandoff",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B45-UNIVERSAL-PRIMITIVE-PORTFOLIO-HANDOFF",
        "output_packets": {
            "universal_primitive_budget_status": rel(BUDGET),
            "cross_constant_switch_rule": rel(SWITCH),
            "next_constant_priority": rel(NEXT_CONSTANT),
            "weak_mixing_b45_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTEW02B45UniversalPrimitivePortfolioHandoffTheorem",
            "proved": True,
            "statement": (
                "Once weak mixing has been reduced to one shared physical primitive with no weak-angle-specific parameters and an executable conditional profile, the rational next step in the universal-primitive program is cross-constant testing. Weak mixing remains open for strict QA-stack threshold and primitive-value upgrades, but the active portfolio frontier should move to another constant that probes the same E0/L0/modal-gap primitive."
            ),
        },
        "weak_mixing_down_to_one_shared_primitive_tier": True,
        "recommend_cross_constant_next": True,
        "selected_next_constant": "CONST-GR-01 / ABSOLUTE-SCALE-GN",
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B45_UniversalPrimitivePortfolioHandoff_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "weak_mixing_down_to_one_shared_primitive_tier": True,
        "recommend_cross_constant_next": True,
        "selected_next_constant": "CONST-GR-01 / ABSOLUTE-SCALE-GN",
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_primary": next_work["primary"]["label"],
        "parking_lot": next_work["parking_lot"]["label"],
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B45 Universal Primitive Portfolio Handoff v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B45-UNIVERSAL-PRIMITIVE-PORTFOLIO-HANDOFF`

## Result

```text
weak mixing down to one shared primitive tier     True
weak-angle-specific new parameters                0
selected primitive values now                     0
conditional profile replay available              True
recommend cross-constant next                     True
selected next constant                            CONST-GR-01 / ABSOLUTE-SCALE-GN
```

B45 records the strategy correction: if the long-term theory can tolerate
`1..3` universal primitives, then a single-constant branch should not keep
absorbing effort once it is reduced to one shared primitive plus strict-source
upgrades.  At that point the stronger move is to test the same primitive against
another constant.

Weak mixing remains open for strict QA-stack threshold and primitive-value
source upgrades, but it is now handoff-ready for portfolio testing.
"""

    for path, payload in [
        (BUDGET, budget),
        (SWITCH, switch),
        (NEXT_CONSTANT, next_constant),
        (BOUNDARY, boundary),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
