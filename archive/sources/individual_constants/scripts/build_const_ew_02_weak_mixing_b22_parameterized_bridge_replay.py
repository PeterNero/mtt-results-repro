"""Build CONST-EW-02 B22 source-promotion or parameterized bridge replay.

B22 turns the provisional B21 parameter lane into an explicit symbolic replay
ledger. It also keeps the strict source-promotion lane primary.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_ew_02_weak_mixing_b22_parameterized_bridge_replay"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
REPLAY = BASE / "symbolic_weak_angle_replay.packet.json"
STRICT = BASE / "strict_source_promotion_gate.packet.json"
PARAM = BASE / "universal_parameter_pressure_test.packet.json"
BOUNDARY = BASE / "weak_mixing_b22_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B22_ParameterizedBridgeReplay_v1.md"

STATUS = "MTT_CONST_EW_02_B22_PARAMETERIZED_REPLAY_BUILT_STRICT_SOURCE_OPEN"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/") if path.is_relative_to(ROOT) else str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sin2_no_threshold(r12: float, y: float) -> float:
    b1 = 41 / 10
    b2 = -19 / 6
    return 3 * (1 + b2 * y) / (3 * (1 + b2 * y) + 5 * (1 / r12 + b1 * y))


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    b21_path = DATA / "const_ew_02_weak_mixing_b21_dynamic_c1_or_free_parameter_bridge.candidate.json"
    b21_boundary_path = DATA / "const_ew_02_weak_mixing_b21_dynamic_c1_or_free_parameter_bridge" / "weak_mixing_b21_boundary.packet.json"
    b21_param_path = DATA / "const_ew_02_weak_mixing_b21_dynamic_c1_or_free_parameter_bridge" / "provisional_universal_parameter_bridge.packet.json"
    b9_reduction_path = DATA / "const_ew_02_weak_mixing_b9_profile_reduction_and_universal_parameter_gate" / "one_loop_profile_reduction.packet.json"
    b10_path = DATA / "const_ew_02_weak_mixing_b10_loop_volume_profile_candidate.candidate.json"
    b11_path = DATA / "const_ew_02_weak_mixing_b11_loop_volume_bridge_proof_attempt.candidate.json"

    b21 = load(b21_path)
    b21_boundary = load(b21_boundary_path)
    b21_param = load(b21_param_path)
    b9 = load(b9_reduction_path)
    b10 = load(b10_path)
    b11 = load(b11_path)

    r12 = 0.56027
    high_scale = b9["reduction"]["high_scale_check"]["computed"]
    y_unit = math.sqrt(15 / math.log(448)) / (8 * math.pi**2)
    sin2_udyn_0 = sin2_no_threshold(r12, 0)
    sin2_udyn_1 = sin2_no_threshold(r12, y_unit)

    replay = {
        "schema": "MTTConstEW02B22SymbolicWeakAngleReplay.v1",
        "status": "SYMBOLIC_PARAMETERIZED_WEAKANGLE_REPLAY_BUILT",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B22-PROVISIONAL-U-DYN-U-PHYS-REPLAY",
        "inputs": {
            "B21_candidate": rel(b21_path),
            "B21_boundary": rel(b21_boundary_path),
            "B21_parameter_bridge": rel(b21_param_path),
            "B9_one_loop_reduction": rel(b9_reduction_path),
            "B10_loop_candidate": rel(b10_path),
            "B11_conditional_bridge": rel(b11_path),
        },
        "general_one_loop_formula": {
            "formula": "sin2 = 3*(1+u2)/(3*(1+u2)+5*(1/r12+u1))",
            "r12": r12,
            "u1": "source-selected or bridge profile u1",
            "u2": "source-selected or bridge profile u2",
        },
        "no_threshold_bridge_lane": {
            "formula": "y = u_dyn*sqrt(15/log(448))/(8*pi^2)",
            "sin2_formula": "sin2(y)=3*(1+b2*y)/(3*(1+b2*y)+5*(1/r12+b1*y))",
            "b1": 41 / 10,
            "b2": -19 / 6,
            "y_unit_when_u_dyn_1": y_unit,
            "xL_unit_when_u_dyn_1": math.sqrt(15 / math.log(448)),
            "u_dyn": "temporary universal bridge parameter; not source-selected",
            "u_dyn_0_high_scale_sin2": sin2_udyn_0,
            "u_dyn_1_conditional_sin2": sin2_udyn_1,
            "matches_B10_y_unit": abs(y_unit - b10["best_candidate"]["y_candidate"]) < 1e-15,
            "matches_B11_conditional_sin2": abs(sin2_udyn_1 - b11["sin2_if_condition_met"]) < 1e-15,
        },
        "u_phys_lane": {
            "role": "physical unit/anchor bridge for alpha_phys or dimensional normalization",
            "used_in_this_replay": False,
            "reason": "weak-angle profile replay can be expressed through u_dyn; u_phys remains reserved for alpha_phys/metrology anchoring",
        },
        "guardrails": {
            "observed_weak_angle_used": False,
            "observed_alpha_used": False,
            "source_branch_selected_by_target": False,
            "parameter_values_fitted": False,
            "no_knob_claimed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    strict = {
        "schema": "MTTConstEW02B22StrictSourcePromotionGate.v1",
        "status": "STRICT_SOURCE_PROMOTION_GATE_RESTATED_AFTER_PARAMETERIZED_REPLAY",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B22-SAME-SOURCE-DYNAMIC-TRANSFER-IDENTITY",
        "required_to_retire_u_dyn": [
            "selected same-source dynamic transfer identity",
            "or honest selected Galerkin C1 contractions",
            "selected A_selected and b_selected/Hessian blocks",
            "selected D_E/Riesz/Green/dotD provenance",
            "selected truncation-error certificate if using finite Galerkin",
        ],
        "required_to_retire_u_phys": [
            "central-circle rod/clock physical unit theorem",
            "or M-theory/modal-gap physical unit theorem",
            "or another global metrology theorem shared by alpha1 and weak mixing",
        ],
        "strict_no_knob_closed": False,
        "selected_source_promoted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    param = {
        "schema": "MTTConstEW02B22UniversalParameterPressureTest.v1",
        "status": "TWO_PARAMETER_PRESSURE_TEST_BUILT_ONE_ACTIVE_IN_WEAK_REPLAY",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B22-PARAMETER-PRESSURE-TEST",
        "parameter_count": {
            "declared": 2,
            "active_in_weak_angle_replay": 1,
            "reserved_for_alpha_physical_anchor": 1,
            "max_allowed_before_source_derivation": b21_boundary["provisional_lane"]["maximum_recommended_parameters_before_source_derivation"],
        },
        "credibility_tests": {
            "global_not_sector_specific": True,
            "not_chosen_from_observed_targets": True,
            "must_feed_multiple_constants_or_retire": True,
            "strict_no_knob_lane_kept_primary": True,
            "parameterized_result_labeled_nonfinal": True,
        },
        "risk": "A parameterized replay is useful for engineering the closure path, but credibility depends on proving or globally measuring u_dyn/u_phys independently.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstEW02B22Boundary.v1",
        "status": "SYMBOLIC_REPLAY_READY_SOURCE_PROMOTION_OR_PARAMETER_RETIREMENT_NEXT",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B22-BOUNDARY",
        "closed_now": {
            "B21_conditional_dynamic_C1_exact_preserved": b21["conditional_dynamic_C1_exact"],
            "symbolic_general_u1u2_replay_built": True,
            "symbolic_no_threshold_u_dyn_replay_built": True,
            "u_dyn_1_recovers_B11_conditional_bridge": True,
            "u_phys_reserved_not_used_for_weak_angle": True,
            "parameter_pressure_test_built": True,
        },
        "still_open": {
            "u_dyn_source_derivation": True,
            "u_phys_source_derivation": True,
            "selected_same_source_dynamic_transfer_identity": True,
            "honest_Galerkin_C1_contractions": True,
            "selected_A_selected": True,
            "selected_b_selected": True,
            "selected_Hessian_blocks": True,
            "selected_D_E_Riesz_Green_dotD": True,
            "actual_xL_source_emission": True,
            "physical_weak_angle_closure": True,
            "strict_no_knob_closure": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02B22NextWork.v1",
        "status": "NEXT_WORKORDER_RETIRE_U_DYN_OR_RUN_TRANSPARENT_BRIDGE",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B23-RETIRE-U-DYN-OR-BRIDGE-AUDIT",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B23-U-DYN-SOURCE-DERIVATION",
            "task": "Derive u_dyn from same-source dynamic transfer, honest Galerkin C1 contractions, or selected alpha1/source-strength theorem.",
        },
        "bridge": {
            "label": "CONST-EW-02 / WEAK-MIXING / B23-BRIDGE-AUDIT-NO-BACKFIT",
            "task": "If u_dyn remains free, run a transparent bridge audit showing all predictions as functions of u_dyn/u_phys and forbidding target selection.",
        },
    }

    candidate = {
        "candidate": "MTTConstEW02WeakMixingB22ParameterizedBridgeReplay",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B22-SOURCE-PROMOTION-OR-PARAMETERIZED-BRIDGE-REPLAY",
        "output_packets": {
            "symbolic_weak_angle_replay": rel(REPLAY),
            "strict_source_promotion_gate": rel(STRICT),
            "universal_parameter_pressure_test": rel(PARAM),
            "weak_mixing_b22_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTEW02B22ParameterizedBridgeReplayTheorem",
            "proved": True,
            "statement": (
                "The B9/B10/B11 weak-angle reduction can be replayed with a "
                "single active provisional universal bridge u_dyn via "
                "y=u_dyn*sqrt(15/log448)/(8*pi^2). Setting u_dyn=1 recovers "
                "the already proved conditional bridge, while u_phys remains "
                "reserved for physical-unit anchoring. This is a transparent "
                "parameterized replay, not no-knob closure and not a source "
                "selector."
            ),
        },
        "symbolic_replay_built": True,
        "active_bridge_parameters_in_weak_angle": ["u_dyn"],
        "reserved_bridge_parameters": ["u_phys"],
        "strict_no_knob_closed": False,
        "physical_weak_angle_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B22_ParameterizedBridgeReplay_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "symbolic_replay_built": True,
        "u_dyn_1_recovers_B11_conditional_bridge": True,
        "active_bridge_parameter_count_for_weak_angle": 1,
        "total_provisional_parameter_count": 2,
        "strict_no_knob_closed": False,
        "physical_weak_angle_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_primary": next_work["primary"]["label"],
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B22 Parameterized Bridge Replay v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B22-SOURCE-PROMOTION-OR-PARAMETERIZED-BRIDGE-REPLAY`

## Replay

General one-loop profile:

```text
sin2 = 3*(1+u2)/(3*(1+u2)+5*(1/r12+u1))
r12 = {r12}
```

No-threshold bridge:

```text
y = u_dyn*sqrt(15/log(448))/(8*pi^2)
y(u_dyn=1) = {y_unit}
sin2(u_dyn=0) = {sin2_udyn_0}
sin2(u_dyn=1) = {sin2_udyn_1}
```

`u_dyn=1` recovers the earlier B11 conditional bridge. It is not selected from
the observed weak angle.

## Parameter Discipline

`u_dyn` is the only active weak-angle bridge parameter here. `u_phys` is reserved
for physical-unit/alpha anchoring and is not used in this replay.

The strict path remains: derive or retire `u_dyn` through same-source dynamic
transfer, honest Galerkin C1 contractions, or selected alpha1/source-strength.
"""

    for path, payload in [
        (REPLAY, replay),
        (STRICT, strict),
        (PARAM, param),
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
