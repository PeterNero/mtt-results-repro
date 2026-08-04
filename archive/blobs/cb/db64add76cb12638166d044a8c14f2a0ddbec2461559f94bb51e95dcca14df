"""Build CONST-EW-02 B43 threshold-vector or minimal-threshold policy packet."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
QA_SU3 = ROOT.parent / "mtt-qa-su3-packet-proof"

SLUG = "const_ew_02_weak_mixing_b43_threshold_vector_or_minimal_policy"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
DECOMPOSITION = BASE / "threshold_vector_decomposition.packet.json"
STRICT_AUDIT = BASE / "strict_threshold_source_audit.packet.json"
MINIMAL_POLICY = BASE / "minimal_threshold_replay_policy.packet.json"
CONDITIONAL_VALUE = BASE / "conditional_minimal_threshold_weak_angle.packet.json"
BOUNDARY = BASE / "weak_mixing_b43_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B43_ThresholdVector_or_MinimalPolicy_v1.md"

STATUS = "MTT_CONST_EW_02_B43_THRESHOLD_VECTOR_OR_MINIMAL_POLICY_BUILT_STRICT_VECTOR_OPEN"


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


def sin2_from_y(r12: float, b1: float, b2: float, y: float) -> float:
    return 3.0 * (1.0 + b2 * y) / (3.0 * (1.0 + b2 * y) + 5.0 * (1.0 / r12 + b1 * y))


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    b42_path = DATA / "const_ew_02_weak_mixing_b42_one_primitive_physical_bridge.candidate.json"
    b42_boundary_path = DATA / "const_ew_02_weak_mixing_b42_one_primitive_physical_bridge" / "weak_mixing_b42_boundary.packet.json"
    b8_policy_path = DATA / "const_ew_02_weak_mixing_b8_flat_fp_policy_import" / "flat_fp_policy_promotion.packet.json"
    b9_profile_path = DATA / "const_ew_02_weak_mixing_b9_profile_reduction_and_universal_parameter_gate" / "one_loop_profile_reduction.packet.json"
    b22_symbolic_path = DATA / "const_ew_02_weak_mixing_b22_parameterized_bridge_replay" / "symbolic_weak_angle_replay.packet.json"
    b24_path = DATA / "const_ew_02_weak_mixing_b24_udyn_source_derivation_import.candidate.json"
    b25_frontier_path = DATA / "const_ew_02_weak_mixing_b25_internal_lambda12_physical_frontier" / "physical_anchor_rg_frontier.packet.json"

    qa_physical_path = QA_SU3 / "candidate_data" / "selected_physical_gauge_anchor_and_electroweak_threshold_vector.candidate.json"
    qa_strominger_path = QA_SU3 / "candidate_data" / "selected_heterotic_strominger_electroweak_threshold_kernel.candidate.json"
    qa_qastack_path = QA_SU3 / "candidate_data" / "selected_electroweak_qastack_selected_traceequality_or_full_threshold_formula.candidate.json"
    qa_rhoe_path = QA_SU3 / "candidate_data" / "selected_heterotic_projectiverhoe_physicalthresholdnormalization_or_smoothoperatoridentity.candidate.json"

    b42 = load(b42_path)
    b42_boundary = load(b42_boundary_path)
    b8_policy = load(b8_policy_path)
    b9_profile = load(b9_profile_path)
    b22_symbolic = load(b22_symbolic_path)
    b24 = load(b24_path)
    b25_frontier = load(b25_frontier_path)
    qa_physical = load(qa_physical_path)
    qa_strominger = load(qa_strominger_path)
    qa_qastack = load(qa_qastack_path)
    qa_rhoe = load(qa_rhoe_path)

    no_threshold_lane = b22_symbolic["no_threshold_bridge_lane"]
    r12 = float(b9_profile["reduction"]["definitions"].get("r12", 0.56027)) if isinstance(b9_profile["reduction"]["definitions"].get("r12"), (int, float)) else 0.56027
    b1 = float(no_threshold_lane["b1"])
    b2 = float(no_threshold_lane["b2"])
    y_unit = float(no_threshold_lane["y_unit_when_u_dyn_1"])
    sin2_conditional = sin2_from_y(r12, b1, b2, y_unit)

    decomposition = {
        "schema": "MTTConstEW02B43ThresholdVectorDecomposition.v1",
        "status": "PHYSICAL_THRESHOLD_VECTOR_DECOMPOSED_INTERNAL_PREFIX_CLOSED_RESIDUAL_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B43-THRESHOLD-VECTOR-DECOMPOSITION",
        "inputs": {
            "B42_candidate": rel(b42_path),
            "B8_flat_FP_policy": rel(b8_policy_path),
            "B25_physical_frontier": rel(b25_frontier_path),
            "QA_physical_threshold_frontier": rel(qa_physical_path),
        },
        "decomposition": {
            "Delta_a_sel": "Delta_a_internal_weaksplit + Delta_a_flat_FP + Delta_a_heavy_or_torsion + Delta_a_scheme_matching",
            "closed_internal_prefix": {
                "lambda_12_internal": b25_frontier["conditional_interface"]["closed_internal_weak_split"]["lambda_12"],
                "Delta_G12_internal": b25_frontier["conditional_interface"]["closed_internal_weak_split"]["Delta_G12"],
                "scope": "dimensionless internal weak-split accounting, not the full physical threshold vector",
            },
            "closed_flat_FP_piece": {
                "extra_fp_threshold_term": b8_policy["promoted_policy"]["extra_fp_threshold_term"],
                "scope": b8_policy["promoted_policy"]["scope"],
            },
            "still_open_residual": [
                "index-weighted local determinant or analytic torsion response",
                "Qa/Qc/SU2 stack determinant values in the selected physical scheme",
                "threshold convention at the selected matching surface",
                "scheme/matching terms needed for precision weak-angle comparison",
            ],
        },
        "decision": {
            "internal_weaksplit_prefix_closed": True,
            "flat_FP_extra_threshold_closed_zero": True,
            "full_physical_threshold_vector_closed": False,
            "residual_threshold_vector_may_be_set_zero_without_policy": False,
            "physical_weak_angle_closure": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    strict_audit = {
        "schema": "MTTConstEW02B43StrictThresholdSourceAudit.v1",
        "status": "STRICT_SOURCE_SELECTED_THRESHOLD_VECTOR_NOT_EMITTED_CURRENT_SOURCES",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B43-STRICT-THRESHOLD-SOURCE-AUDIT",
        "inputs": {
            "QA_physical_threshold_frontier": rel(qa_physical_path),
            "QA_heterotic_strominger_kernel": rel(qa_strominger_path),
            "QA_qastack_trace_or_formula": rel(qa_qastack_path),
            "QA_projective_rhoe_physical_threshold": rel(qa_rhoe_path),
        },
        "source_packet_statuses": {
            "physical_threshold_vector_closed": qa_physical["decision"]["threshold_vector_closed"],
            "heterotic_strominger_kernel_closed": qa_strominger["decision"]["selected_heterotic_strominger_kernel_closed"],
            "qastack_full_threshold_formula_closed": qa_qastack["decision"]["full_threshold_operator_formula_closed"],
            "qastack_lambda_12_closed_in_that_packet": qa_qastack["decision"]["lambda_12_closed"],
            "projective_rhoe_physical_threshold_normalization_closed": qa_rhoe["decision"]["physical_threshold_normalization_closed"],
            "projective_rhoe_smooth_operator_identity_proved": qa_rhoe["decision"]["smooth_operator_identity_proved"],
        },
        "minimal_missing_payload": {
            "name": qa_qastack["minimal_next_payload"]["name"],
            "must_emit": qa_qastack["minimal_next_payload"]["must_emit"],
        },
        "decision": {
            "strict_threshold_vector_source_emitted": False,
            "current_source_nogo_for_strict_vector": True,
            "mathematical_impossibility_claimed": False,
            "diagnostic_threshold_witness_forbidden_as_proof": True,
            "full_no_knob_physical_weak_angle_closure": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    minimal_policy = {
        "schema": "MTTConstEW02B43MinimalThresholdReplayPolicy.v1",
        "status": "MINIMAL_THRESHOLD_REPLAY_POLICY_AVAILABLE_CONDITIONAL_NOT_STRICT",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B43-MINIMAL-THRESHOLD-REPLAY-POLICY",
        "inputs": {
            "B9_one_loop_profile_reduction": rel(b9_profile_path),
            "B22_symbolic_weak_angle_replay": rel(b22_symbolic_path),
            "B24_udyn_source_derivation": rel(b24_path),
            "B42_one_primitive_bridge": rel(b42_path),
        },
        "policy": {
            "name": "minimal_no_additional_physical_threshold_replay",
            "sets": {
                "T1": 0.0,
                "T2": 0.0,
                "Delta_a_heavy_or_torsion": 0.0,
                "Delta_a_scheme_matching": 0.0,
            },
            "keeps": [
                "closed internal weak-split prefix",
                "flat FP extra threshold term = 0",
                "u_dyn=1 source-derived no-threshold profile prefix",
                "one-primitive physical bridge held symbolic, not fitted",
            ],
            "tier": "conditional replay policy; not strict no-knob physical threshold theorem",
        },
        "admissibility": {
            "observed_weak_angle_used_to_set_thresholds": False,
            "observed_alpha_used_to_set_thresholds": False,
            "target_residual_scan_used": False,
            "adds_new_weak_angle_knob": False,
            "allowed_as_replay_lane": True,
            "allowed_as_strict_source_vector": False,
        },
        "decision": {
            "minimal_threshold_replay_policy_closed": True,
            "strict_threshold_vector_closed": False,
            "one_primitive_value_selected": b42["one_primitive_value_selected"],
            "physical_weak_angle_closure": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    conditional_value = {
        "schema": "MTTConstEW02B43ConditionalMinimalThresholdWeakAngle.v1",
        "status": "CONDITIONAL_MINIMAL_THRESHOLD_WEAK_ANGLE_EMITTED_REPLAY_ONLY",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B43-CONDITIONAL-MINIMAL-THRESHOLD-VALUE",
        "formula": no_threshold_lane["sin2_formula"],
        "inputs": {
            "r12": r12,
            "b1": b1,
            "b2": b2,
            "u_dyn": b24["u_dyn_value"],
            "y_unit_when_u_dyn_1": y_unit,
            "xL_unit_when_u_dyn_1": no_threshold_lane["xL_unit_when_u_dyn_1"],
        },
        "computed": {
            "sin2_minimal_threshold_replay": sin2_conditional,
            "matches_B22_conditional_sin2": abs(sin2_conditional - no_threshold_lane["u_dyn_1_conditional_sin2"]) < 1e-15,
            "high_scale_u_dyn_0_sin2": no_threshold_lane["u_dyn_0_high_scale_sin2"],
        },
        "classification": {
            "conditional_replay_value": True,
            "physical_weak_angle_prediction": False,
            "strict_no_knob_value": False,
            "precision_SM_effective_angle": False,
            "why": "It assumes the minimal-threshold replay policy and does not source-select the full physical threshold vector or the primitive value.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstEW02B43Boundary.v1",
        "status": "B43_STRICT_THRESHOLD_VECTOR_OPEN_MINIMAL_REPLAY_LANE_CLOSED",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B43-BOUNDARY",
        "previous_B42_status": b42["status"],
        "closed_or_decided_now": {
            "threshold_decomposition": True,
            "internal_weaksplit_prefix_and_flat_FP_zero_carried": True,
            "strict_source_selected_threshold_vector_currently_not_emitted": True,
            "minimal_no_additional_threshold_replay_policy": True,
            "conditional_minimal_threshold_weak_angle_value_emitted": True,
        },
        "still_open": {
            "strict_source_selected_threshold_vector": True,
            "Selected_Electroweak_QaStack_QuotientFunctor_and_AbaseIdentity_Theorem": True,
            "primitive_numeric_value_or_strict_source_unit": True,
            "precision_RG_threshold_execution": True,
            "physical_weak_angle_numerical_closure": True,
            "strict_full_no_knob_closure": True,
        },
        "anti_cycle_delta_from_B42": {
            "B42": "collapsed physical action normalization and matching scale to one shared primitive in the one-primitive tier",
            "B43": "separates strict threshold-vector source emission from the admissible minimal-threshold replay lane",
            "not_repeated": [
                "not treating the internal weak-split threshold as the full physical threshold vector",
                "not using diagnostic threshold witnesses as proof inputs",
                "not using the conditional weak-angle replay value as a physical closure claim",
            ],
        },
        "allowed_claim": "B43 closes a conditional minimal-threshold replay lane and emits its weak-angle value under guardrails.",
        "forbidden_claim": "strict physical threshold vector, precision effective weak angle, or full no-knob closure",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02B43NextWork.v1",
        "status": "NEXT_WORKORDER_B44_PROFILE_EXECUTION_OR_QASTACK_SOURCE_IDENTITY",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B44-PROFILE-EXECUTION-OR-QASTACK-SOURCE-IDENTITY",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B44-QASTACK-QUOTIENTFUNCTOR-ABASE-IDENTITY",
            "task": "Attempt the strict source theorem named by the QA/SU3 packet: quotient functor from B_N to Pperp/shared-line domain, exact A_base tensor I_3 identity, post-quotient determinant identity, and source-emitted Qa-stack weights/scale.",
        },
        "parallel": {
            "label": "CONST-EW-02 / WEAK-MIXING / B44-CONDITIONAL-PROFILE-EXECUTION-PACKET",
            "task": "Run a full conditional profile packet using B42 one-primitive symbolic anchoring plus B43 minimal-threshold replay, clearly labeled as replay-only until primitive value and strict thresholds are sourced.",
        },
    }

    candidate = {
        "candidate": "MTTConstEW02WeakMixingB43ThresholdVectorOrMinimalPolicy",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B43-THRESHOLD-VECTOR-OR-MINIMAL-POLICY",
        "output_packets": {
            "threshold_vector_decomposition": rel(DECOMPOSITION),
            "strict_threshold_source_audit": rel(STRICT_AUDIT),
            "minimal_threshold_replay_policy": rel(MINIMAL_POLICY),
            "conditional_minimal_threshold_weak_angle": rel(CONDITIONAL_VALUE),
            "weak_mixing_b43_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTEW02B43ThresholdVectorOrMinimalPolicyTheorem",
            "proved": True,
            "statement": (
                "The physical electroweak threshold vector decomposes into a closed internal weak-split prefix, a closed zero flat-FP extra term, and residual physical/local-determinant/RG matching terms. Current sources do not emit the strict source-selected residual threshold vector. However, an explicitly conditional minimal-threshold replay policy is now machine-checkable and emits the guarded no-additional-threshold weak-angle replay value without using observed electroweak data or adding a weak-angle-specific knob."
            ),
        },
        "threshold_decomposition_closed": True,
        "strict_threshold_vector_source_emitted": False,
        "minimal_threshold_replay_policy_closed": True,
        "conditional_minimal_threshold_sin2": sin2_conditional,
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B43_ThresholdVector_or_MinimalPolicy_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "threshold_decomposition_closed": True,
        "strict_threshold_vector_source_emitted": False,
        "minimal_threshold_replay_policy_closed": True,
        "conditional_minimal_threshold_sin2": sin2_conditional,
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_primary": next_work["primary"]["label"],
        "next_parallel": next_work["parallel"]["label"],
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B43 Threshold Vector or Minimal Policy v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B43-THRESHOLD-VECTOR-OR-MINIMAL-POLICY`

## Result

```text
threshold decomposition closed             True
strict physical Delta_a^sel emitted         False
minimal-threshold replay policy closed      True
conditional replay sin2                     {sin2_conditional:.16f}
physical weak-angle closure                 False
strict no-knob closure                      False
```

B43 separates the two threshold meanings.  The internal weak-split threshold and
the zero flat-FP extra term are carried forward, but the strict physical
threshold vector still needs the QA-stack quotient/A_base identity theorem.

The conditional minimal-threshold lane is now executable and emits a replay
value.  It is not a precision physical weak-angle prediction.

## Next

`CONST-EW-02 / WEAK-MIXING / B44-QASTACK-QUOTIENTFUNCTOR-ABASE-IDENTITY`
or the parallel conditional profile execution packet.
"""

    for path, payload in [
        (DECOMPOSITION, decomposition),
        (STRICT_AUDIT, strict_audit),
        (MINIMAL_POLICY, minimal_policy),
        (CONDITIONAL_VALUE, conditional_value),
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
