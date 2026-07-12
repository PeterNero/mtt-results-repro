"""Build CONST-EW-02 B42 one-primitive physical bridge packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_ew_02_weak_mixing_b42_one_primitive_physical_bridge"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
BRIDGE = BASE / "one_primitive_physical_bridge.packet.json"
COLLAPSE = BASE / "action_unit_mu_match_collapse.packet.json"
BUDGET = BASE / "parameter_budget_and_guardrail.packet.json"
BOUNDARY = BASE / "weak_mixing_b42_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B42_OnePrimitivePhysicalBridge_v1.md"

STATUS = "MTT_CONST_EW_02_B42_ONE_PRIMITIVE_PHYSICAL_BRIDGE_BUILT_VALUE_OPEN"


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

    b41_path = DATA / "const_ew_02_weak_mixing_b41_gauge_action_rg_matching.candidate.json"
    b41_boundary_path = DATA / "const_ew_02_weak_mixing_b41_gauge_action_rg_matching" / "weak_mixing_b41_boundary.packet.json"
    b22_symbolic_path = DATA / "const_ew_02_weak_mixing_b22_parameterized_bridge_replay" / "symbolic_weak_angle_replay.packet.json"
    b23_protocol_path = DATA / "const_ew_02_weak_mixing_b23_cross_use_universal_parameter_admissibility" / "fit_once_predict_elsewhere_protocol.packet.json"
    b23_ledger_path = DATA / "const_ew_02_weak_mixing_b23_cross_use_universal_parameter_admissibility" / "u_dyn_u_phys_cross_use_ledger.packet.json"
    a10_primitive_path = DATA / "const_em_01_alpha1_universal_primitive_or_nogo" / "one_universal_primitive.packet.json"
    a11_path = DATA / "const_em_01_alpha1_frontier_closure_ledger.candidate.json"

    b41 = load(b41_path)
    b41_boundary = load(b41_boundary_path)
    b22_symbolic = load(b22_symbolic_path)
    b23_protocol = load(b23_protocol_path)
    b23_ledger = load(b23_ledger_path)
    a10_primitive = load(a10_primitive_path)
    a11 = load(a11_path)

    primitive_options = a10_primitive["primitive_options"]

    bridge = {
        "schema": "MTTConstEW02B42OnePrimitivePhysicalBridge.v1",
        "status": "ONE_PRIMITIVE_PHYSICAL_BRIDGE_DECLARED_VALUE_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B42-SELECTED-ACTION-UNIT-OR-ONE-PRIMITIVE-BRIDGE",
        "inputs": {
            "B41_candidate": rel(b41_path),
            "B41_boundary": rel(b41_boundary_path),
            "B23_fit_once_predict_elsewhere_protocol": rel(b23_protocol_path),
            "B23_u_dyn_u_phys_cross_use_ledger": rel(b23_ledger_path),
            "A10_one_universal_primitive": rel(a10_primitive_path),
            "A11_alpha1_frontier_ledger": rel(a11_path),
        },
        "superset_path_use": {
            "alpha1_path": "A10/A11 already isolate the physical alpha/K_phys obstruction and provide one universal primitive formulae.",
            "weak_mixing_path": "B41 reduces the remaining weak-angle blocker to the same physical action-unit plus RG/matching frontier.",
            "locked_target": "A single physical unit primitive is shared before checking alpha1 and weak mixing; the weak angle does not get its own knob.",
        },
        "bridge_modes": {
            "strict_source_unit": {
                "description": "A same-branch theorem emits E0, L0, Omega0, ell_p/kappa11/modal gap, or equivalent physical action unit.",
                "available_now": False,
                "strict_no_knob_possible": True,
            },
            "one_universal_primitive": {
                "description": "Declare E0 or L0 once as a universal metrological primitive; use it unchanged for alpha1/K_phys and weak-mixing physical matching.",
                "available_now": True,
                "strict_no_knob_possible": False,
                "value_selected_now": False,
            },
        },
        "primitive_options": primitive_options,
        "decision": {
            "one_primitive_tier_contract_closed": True,
            "one_primitive_value_selected": False,
            "strict_source_unit_derived": False,
            "weak_angle_extra_physical_knob_added": False,
            "alpha1_and_weak_mixing_share_same_physical_bridge": True,
            "physical_weak_angle_numerical_closure": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    collapse = {
        "schema": "MTTConstEW02B42ActionUnitMuMatchCollapse.v1",
        "status": "K_PHYS_ALPHA_PHYS_AND_MU_MATCH_COLLAPSED_TO_ONE_SYMBOLIC_PRIMITIVE_IN_ONE_PRIMITIVE_TIER",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B42-ACTION-UNIT-MU-MATCH-COLLAPSE",
        "input_formulae": {
            "energy_primitive": primitive_options["energy"]["formulae"],
            "length_primitive": primitive_options["length"]["formulae"],
            "weak_angle_symbolic_formula": b22_symbolic["general_one_loop_formula"],
            "weak_angle_no_threshold_lane": b22_symbolic["no_threshold_bridge_lane"],
        },
        "collapsed_slots": {
            "K_phys_or_action_unit": "alpha_phys or equivalent action normalization becomes a function of the same E0/L0 primitive",
            "mu_match": "Lambda_eff=E0 or 1/L0 supplies the matching-scale slot in the one-primitive tier",
            "Omega0_or_gap": "Omega0=sqrt(tau_int)*E0 or sqrt(tau_int)/L0 supplies the gap/action-frequency slot",
        },
        "what_is_not_collapsed": {
            "threshold_vector": "selected Delta_a threshold values or a vanishing theorem are still required",
            "precision_RG_policy_values": "loop order and scheme exist as policy scaffolding, but selected threshold/matching values are not executed as source closure",
            "strict_source_derivation": "the primitive is not derived by this packet",
        },
        "decision": {
            "number_of_physical_unit_primitives_needed_in_this_tier": 1,
            "K_phys_and_mu_match_count_as_separate_knobs": False,
            "threshold_vector_closed": False,
            "RG_execution_closed": False,
            "physical_weak_angle_closure": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    budget = {
        "schema": "MTTConstEW02B42ParameterBudgetAndGuardrail.v1",
        "status": "ONE_PRIMITIVE_PARAMETER_BUDGET_GUARDRAILED_NO_BACKFIT",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B42-PARAMETER-BUDGET",
        "policy_imports": {
            "B23_success_rule": b23_protocol["success_rule"],
            "B23_calibration_modes": b23_protocol["calibration_modes"],
            "A10_acceptance_policy": a10_primitive["acceptance_policy"],
        },
        "budget": {
            "strict_no_knob_selected_parameter_count": 0,
            "one_primitive_tier_new_global_parameters": 1,
            "weak_angle_specific_parameters": 0,
            "maximum_live_universal_parameters_from_B23": b23_ledger["global_policy"]["maximum_live_universal_parameters"],
            "current_selected_numeric_value_count": 0,
        },
        "allowed_calibration_order": [
            "source theorem emits primitive value; then alpha1 and weak mixing are both predictions",
            "one independent physical-unit measurement fixes the primitive once; then alpha1 and weak mixing are conditional cross-sector predictions",
            "alpha1 fixes the primitive once; then weak mixing is a conditional prediction",
        ],
        "forbidden_calibration_order": [
            "weak angle fixes the primitive and is then counted as predicted",
            "alpha1 and weak angle are jointly fit to choose the primitive",
            "primitive value is retuned between alpha1, weak mixing, gravity, or cosmology",
        ],
        "decision": {
            "fit_once_predict_elsewhere_protocol_closed": True,
            "per_observable_retuning_forbidden": True,
            "one_primitive_tier_is_not_no_knob": True,
            "measured_weak_angle_not_allowed_as_calibration_for_weak_angle_claim": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstEW02B42Boundary.v1",
        "status": "B42_ONE_PRIMITIVE_BRIDGE_CONTRACT_CLOSED_VALUE_AND_THRESHOLDS_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B42-BOUNDARY",
        "previous_B41_status": b41["status"],
        "closed_or_decided_now": {
            "one_primitive_physical_bridge_contract": True,
            "K_phys_alpha_phys_mu_match_collapse_to_one_symbolic_primitive": True,
            "parameter_budget_guardrail": True,
            "weak_angle_specific_physical_knob_forbidden": True,
            "strict_source_unit_route_kept_separate": True,
        },
        "still_open": {
            "one_primitive_numeric_value": True,
            "strict_source_unit_derivation": True,
            "source_selected_threshold_vector": True,
            "source_selected_precision_RG_execution": True,
            "physical_weak_angle_numerical_closure": True,
            "strict_full_no_knob_closure": True,
        },
        "anti_cycle_delta_from_B41": {
            "B41": "named the physical action-unit and RG/matching lanes",
            "B42": "collapses K_phys/alpha_phys/mu_match to one symbolic physical primitive in the allowed one-primitive tier",
            "not_repeated": [
                "not using weak angle to calibrate itself",
                "not counting K_phys and mu_match as independent knobs in the one-primitive tier",
                "not promoting the primitive tier as strict no-knob closure",
            ],
        },
        "allowed_claim": "B42 reduces the conditional physical-normalization branch to a single global primitive plus threshold/RG execution.",
        "forbidden_claim": "physical weak-angle numerical closure or strict no-knob source-unit derivation",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02B42NextWork.v1",
        "status": "NEXT_WORKORDER_B43_THRESHOLD_VECTOR_OR_PRIMITIVE_CALIBRATION_SOURCE",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B43-THRESHOLD-VECTOR-OR-PRIMITIVE-CALIBRATION-SOURCE",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B43-SOURCE-SELECTED-THRESHOLD-VECTOR",
            "task": "Emit selected Delta_a threshold values, or prove the missing threshold components vanish in the selected weak-mixing scheme.",
        },
        "parallel": {
            "label": "CONST-EW-02 / WEAK-MIXING / B43-PRIMITIVE-VALUE-SOURCE-OR-ONE-CALIBRATION",
            "task": "Either derive the E0/L0 primitive from central-circle/modal-gap sources or document a single independent calibration and downstream prediction order.",
        },
    }

    candidate = {
        "candidate": "MTTConstEW02WeakMixingB42OnePrimitivePhysicalBridge",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B42-ONE-PRIMITIVE-PHYSICAL-BRIDGE",
        "output_packets": {
            "one_primitive_physical_bridge": rel(BRIDGE),
            "action_unit_mu_match_collapse": rel(COLLAPSE),
            "parameter_budget_and_guardrail": rel(BUDGET),
            "weak_mixing_b42_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTEW02B42OnePrimitivePhysicalBridgeTheorem",
            "proved": True,
            "statement": (
                "In the explicitly non-no-knob one-primitive tier, the alpha1 physical anchor and weak-mixing physical normalization/matching slots can be tied to one universal E0 or L0 primitive. Therefore K_phys, alpha_phys, and mu_match are not separate weak-angle knobs in this tier. The primitive value, strict source-unit derivation, selected threshold vector, and precision RG execution remain open."
            ),
        },
        "one_primitive_physical_bridge_contract_closed": True,
        "K_phys_alpha_phys_mu_match_collapsed_to_one_primitive": True,
        "parameter_budget_guardrail_closed": True,
        "one_primitive_value_selected": False,
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B42_OnePrimitivePhysicalBridge_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "one_primitive_physical_bridge_contract_closed": True,
        "K_phys_alpha_phys_mu_match_collapsed_to_one_primitive": True,
        "parameter_budget_guardrail_closed": True,
        "one_primitive_value_selected": False,
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_primary": next_work["primary"]["label"],
        "next_parallel": next_work["parallel"]["label"],
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B42 One Primitive Physical Bridge v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B42-ONE-PRIMITIVE-PHYSICAL-BRIDGE`

## Result

```text
one-primitive bridge contract closed        True
K_phys/alpha_phys/mu_match collapse         True
weak-angle-specific physical knob added     False
one primitive numeric value selected        False
physical weak-angle numerical closure       False
strict no-knob closure                      False
```

B42 is a parameter-accounting theorem.  If we enter the explicitly labeled
one-primitive tier, the physical action unit and matching scale come from the
same `E0` or `L0` primitive already isolated by the alpha branch.  That prevents
the weak-angle branch from quietly acquiring separate knobs for `K_phys`,
`alpha_phys`, and `mu_match`.

## What Remains

The next unresolved object is either a source-selected threshold vector or a
source/one-calibration value for the shared primitive.  The measured weak angle
is not allowed to calibrate the primitive for a weak-angle prediction claim.
"""

    for path, payload in [
        (BRIDGE, bridge),
        (COLLAPSE, collapse),
        (BUDGET, budget),
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
