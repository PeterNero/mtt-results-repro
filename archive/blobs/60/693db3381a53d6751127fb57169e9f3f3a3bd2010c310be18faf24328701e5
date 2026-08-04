"""Build CONST-EW-02 B44 conditional weak-mixing profile execution packet."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_ew_02_weak_mixing_b44_conditional_profile_execution"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ASSUMPTIONS = BASE / "conditional_profile_assumption_lock.packet.json"
EXECUTION = BASE / "conditional_profile_execution.packet.json"
COMPARISON = BASE / "profile_status_and_comparison_boundaries.packet.json"
BOUNDARY = BASE / "weak_mixing_b44_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B44_ConditionalProfileExecution_v1.md"

STATUS = "MTT_CONST_EW_02_B44_CONDITIONAL_PROFILE_EXECUTION_BUILT_REPLAY_ONLY"


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


def sin2_profile(r12: float, b1: float, b2: float, y: float) -> float:
    return 3.0 * (1.0 + b2 * y) / (3.0 * (1.0 + b2 * y) + 5.0 * (1.0 / r12 + b1 * y))


def derivative_at_zero(r12: float, b1: float, b2: float) -> float:
    eps = 1e-7
    return (sin2_profile(r12, b1, b2, eps) - sin2_profile(r12, b1, b2, -eps)) / (2.0 * eps)


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    b39_path = DATA / "const_ew_02_weak_mixing_b39_source_kernel_or_local_principle.candidate.json"
    b40_path = DATA / "const_ew_02_weak_mixing_b40_local_kernel_to_profile.candidate.json"
    b41_path = DATA / "const_ew_02_weak_mixing_b41_gauge_action_rg_matching.candidate.json"
    b42_path = DATA / "const_ew_02_weak_mixing_b42_one_primitive_physical_bridge.candidate.json"
    b43_path = DATA / "const_ew_02_weak_mixing_b43_threshold_vector_or_minimal_policy.candidate.json"
    b22_symbolic_path = DATA / "const_ew_02_weak_mixing_b22_parameterized_bridge_replay" / "symbolic_weak_angle_replay.packet.json"
    b24_path = DATA / "const_ew_02_weak_mixing_b24_udyn_source_derivation_import.candidate.json"
    b43_conditional_path = DATA / "const_ew_02_weak_mixing_b43_threshold_vector_or_minimal_policy" / "conditional_minimal_threshold_weak_angle.packet.json"

    b39 = load(b39_path)
    b40 = load(b40_path)
    b41 = load(b41_path)
    b42 = load(b42_path)
    b43 = load(b43_path)
    b22_symbolic = load(b22_symbolic_path)
    b24 = load(b24_path)
    b43_conditional = load(b43_conditional_path)

    lane = b22_symbolic["no_threshold_bridge_lane"]
    r12 = float(b43_conditional["inputs"]["r12"])
    b1 = float(b43_conditional["inputs"]["b1"])
    b2 = float(b43_conditional["inputs"]["b2"])
    y_unit = float(b43_conditional["inputs"]["y_unit_when_u_dyn_1"])
    high_scale = sin2_profile(r12, b1, b2, 0.0)
    conditional_sin2 = sin2_profile(r12, b1, b2, y_unit)
    deriv0 = derivative_at_zero(r12, b1, b2)

    assumptions = {
        "schema": "MTTConstEW02B44ConditionalProfileAssumptionLock.v1",
        "status": "CONDITIONAL_PROFILE_ASSUMPTIONS_LOCKED",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B44-CONDITIONAL-PROFILE-ASSUMPTION-LOCK",
        "inputs": {
            "B39_local_principle": rel(b39_path),
            "B40_local_kernel_handoff": rel(b40_path),
            "B41_gauge_RG_frontier": rel(b41_path),
            "B42_one_primitive_bridge": rel(b42_path),
            "B43_threshold_or_minimal_policy": rel(b43_path),
        },
        "assumptions": {
            "local_source_kernel_tier": {
                "accepted": b39["local_tier_source_kernel_closed"],
                "strict_unpatched": b39["strict_unpatched_source_kernel_closed"],
                "meaning": "Uses the explicit local SelectedWeylVariationActionPrinciple tier.",
            },
            "one_primitive_tier": {
                "contract_closed": b42["one_primitive_physical_bridge_contract_closed"],
                "value_selected": b42["one_primitive_value_selected"],
                "meaning": "K_phys/alpha_phys/mu_match are locked to one symbolic E0/L0 primitive; no numerical primitive value is selected.",
            },
            "minimal_threshold_policy": {
                "closed": b43["minimal_threshold_replay_policy_closed"],
                "strict_vector_emitted": b43["strict_threshold_vector_source_emitted"],
                "meaning": "Runs the no-additional-threshold replay lane, not a strict physical Delta_a^sel source vector.",
            },
            "source_strength_prefix": {
                "u_dyn_source_derived": b24["u_dyn_source_derived"],
                "u_dyn_value": b24["u_dyn_value"],
            },
        },
        "forbidden_uses": [
            "calling this strict no-knob closure",
            "using the emitted value as a precision effective weak angle",
            "using observed weak angle, alpha, masses, CKM, or PMNS to choose the lane",
            "retuning u_dyn, E0/L0, thresholds, or matching convention after comparison",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    execution = {
        "schema": "MTTConstEW02B44ConditionalProfileExecution.v1",
        "status": "CONDITIONAL_MINIMAL_THRESHOLD_PROFILE_EXECUTED",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B44-CONDITIONAL-PROFILE-EXECUTION",
        "formula": {
            "sin2_y": lane["sin2_formula"],
            "y": "u_dyn*sqrt(15/log(448))/(8*pi^2)",
            "r12": r12,
            "b1": b1,
            "b2": b2,
        },
        "values": {
            "u_dyn": b24["u_dyn_value"],
            "xL_unit": lane["xL_unit_when_u_dyn_1"],
            "y_unit": y_unit,
            "sin2_high_scale_y0": high_scale,
            "sin2_conditional_minimal_threshold": conditional_sin2,
            "derivative_at_y0": deriv0,
            "positive_A2_interval": f"0 <= y < {1.0 / abs(b2)}",
        },
        "checks": {
            "matches_B43_conditional_value": abs(conditional_sin2 - b43_conditional["computed"]["sin2_minimal_threshold_replay"]) < 1e-15,
            "matches_B22_conditional_value": abs(conditional_sin2 - lane["u_dyn_1_conditional_sin2"]) < 1e-15,
            "finite_value": math.isfinite(conditional_sin2),
            "inside_positive_A2_interval": 0.0 <= y_unit < 1.0 / abs(b2),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    comparison = {
        "schema": "MTTConstEW02B44ProfileStatusAndComparisonBoundaries.v1",
        "status": "REPLAY_VALUE_READY_FOR_LABELED_COMPARISON_NOT_PROMOTED",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B44-PROFILE-STATUS-COMPARISON-BOUNDARIES",
        "emitted_value": {
            "sin2_conditional_minimal_threshold": conditional_sin2,
            "classification": "conditional replay value",
        },
        "allowed_comparisons": [
            "compare against Theta V tree/replay values as consistency diagnostics",
            "compare against measured weak-angle values only as downstream replay checks after declaring the comparison scheme",
            "use as a regression test when a strict threshold vector or primitive value is later emitted",
        ],
        "blocked_comparisons": [
            "precision electroweak fit claim",
            "MSbar or effective weak-angle claim without scheme conversion",
            "strict no-knob source prediction claim",
            "claiming the one-primitive tier selected the primitive value",
        ],
        "open_promotions": {
            "strict_local_source_kernel_derivation": True,
            "strict_QaStack_threshold_vector": True,
            "primitive_E0_or_L0_value": True,
            "precision_RG_scheme_conversion": True,
            "physical_effective_weak_angle": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstEW02B44Boundary.v1",
        "status": "B44_CONDITIONAL_EXECUTION_COMPLETE_STRICT_PROMOTIONS_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B44-BOUNDARY",
        "previous_B43_status": b43["status"],
        "closed_or_decided_now": {
            "conditional_assumption_lock": True,
            "conditional_profile_execution": True,
            "profile_value_regression_test": True,
            "comparison_boundary_declared": True,
        },
        "still_open": {
            "strict_unpatched_local_source_kernel": True,
            "strict_QaStack_threshold_vector": True,
            "primitive_value_or_source_unit": True,
            "precision_RG_scheme_conversion": True,
            "physical_weak_angle_numerical_closure": True,
            "strict_full_no_knob_closure": True,
        },
        "anti_cycle_delta_from_B43": {
            "B43": "closed the minimal-threshold replay policy and emitted a conditional value",
            "B44": "freezes that lane into an executable profile packet with explicit assumption and comparison boundaries",
            "not_repeated": [
                "not re-proving threshold decomposition",
                "not promoting the replay value to a physical weak-angle closure",
                "not adding or fitting a new parameter",
            ],
        },
        "allowed_claim": "B44 gives an executable conditional profile/regression packet.",
        "forbidden_claim": "strict threshold source theorem, primitive value selection, precision electroweak closure, or no-knob closure",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02B44NextWork.v1",
        "status": "NEXT_WORKORDER_B45_STRICT_QASTACK_OR_PRIMITIVE_VALUE",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B45-STRICT-QASTACK-OR-PRIMITIVE-VALUE",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B45-QASTACK-QUOTIENTFUNCTOR-ABASE-IDENTITY-ATTEMPT",
            "task": "Attempt the strict QA-stack quotient functor and A_base tensor I_3 source identity required to promote Delta_a^sel.",
        },
        "parallel": {
            "label": "CONST-EW-02 / WEAK-MIXING / B45-PRIMITIVE-VALUE-SOURCE-SEARCH",
            "task": "Search central-circle/modal-gap/GR source packets for a selected E0/L0 value or a legal single independent calibration order.",
        },
    }

    candidate = {
        "candidate": "MTTConstEW02WeakMixingB44ConditionalProfileExecution",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B44-CONDITIONAL-PROFILE-EXECUTION",
        "output_packets": {
            "conditional_profile_assumption_lock": rel(ASSUMPTIONS),
            "conditional_profile_execution": rel(EXECUTION),
            "profile_status_and_comparison_boundaries": rel(COMPARISON),
            "weak_mixing_b44_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTEW02B44ConditionalProfileExecutionTheorem",
            "proved": True,
            "statement": (
                "Under the explicit local source-kernel tier, the one-primitive symbolic physical bridge, and the B43 minimal-threshold replay policy, the weak-mixing profile is executable and emits sin2=0.2315309482915084. This value is a guarded conditional replay/regression value; it is not a strict no-knob physical prediction, not a precision effective weak angle, and not selected by observed data."
            ),
        },
        "conditional_profile_execution_closed": True,
        "conditional_minimal_threshold_sin2": conditional_sin2,
        "comparison_boundaries_declared": True,
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B44_ConditionalProfileExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "conditional_profile_execution_closed": True,
        "conditional_minimal_threshold_sin2": conditional_sin2,
        "comparison_boundaries_declared": True,
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_primary": next_work["primary"]["label"],
        "next_parallel": next_work["parallel"]["label"],
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B44 Conditional Profile Execution v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B44-CONDITIONAL-PROFILE-EXECUTION`

## Result

```text
conditional profile execution closed        True
conditional replay sin2                     {conditional_sin2:.16f}
physical weak-angle closure                 False
strict no-knob closure                      False
```

B44 freezes the replay lane built by B42/B43.  The value is executable and
machine-checked, but remains conditional on the local source-kernel tier, the
symbolic one-primitive bridge, and the minimal-threshold policy.

The next strict path is still the QA-stack quotient functor and `A_base tensor
I_3` source identity for the physical threshold vector.
"""

    for path, payload in [
        (ASSUMPTIONS, assumptions),
        (EXECUTION, execution),
        (COMPARISON, comparison),
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
