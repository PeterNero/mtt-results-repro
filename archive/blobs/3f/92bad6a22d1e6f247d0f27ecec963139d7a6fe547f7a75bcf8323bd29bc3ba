"""Build CONST-EW-02 B21 dynamic C1 or provisional parameter bridge.

B21 imports the dynamic C1 frontier: the fixed 72-real conditional transfer has
no linear-algebra obstruction, but selected-source promotion remains open. It
also records a provisional few-universal-parameters lane as a bridge, not as
strict no-knob closure.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
NONSM = TEXPAPERS / "mtt-nonsm-constants-no-knob"
Q79 = TEXPAPERS / "mtt-q79-proof-repro"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_ew_02_weak_mixing_b21_dynamic_c1_or_free_parameter_bridge"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
IMPORT_PACKET = BASE / "dynamic_c1_frontier_import.packet.json"
PARAM_PACKET = BASE / "provisional_universal_parameter_bridge.packet.json"
BOUNDARY = BASE / "weak_mixing_b21_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B21_DynamicC1OrFreeParameterBridge_v1.md"

STATUS = "MTT_CONST_EW_02_B21_CONDITIONAL_DYNAMIC_C1_EXACT_SOURCE_OR_PARAMETER_BRIDGE_OPEN"


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

    b20_path = DATA / "const_ew_02_weak_mixing_b20_matterslot_overlap_static_import.candidate.json"
    b20_boundary_path = DATA / "const_ew_02_weak_mixing_b20_matterslot_overlap_static_import" / "weak_mixing_b20_boundary.packet.json"

    dyn_cert_path = NONSM / "certificates" / "dynamic_overlap_or_c1primitive_source_emission_import_certificate.json"
    hess_cert_path = NONSM / "certificates" / "dynamictransferhessian_bselected_or_honestgalerkinc1_valuefill_import_certificate.json"
    replay_cert_path = NONSM / "certificates" / "selected_phifin_s2_value_emission_with_gap_error_honest_replay_certificate.json"
    promo_cert_path = Q79 / "certificates" / "iwasawa_selected_source_promotion_gate_certificate.json"

    dyn_cert = load(dyn_cert_path)
    hess_cert = load(hess_cert_path)
    replay_cert = load(replay_cert_path)
    promo_cert = load(promo_cert_path)
    b20 = load(b20_path)
    b20_boundary = load(b20_boundary_path)

    dynamic_import = {
        "schema": "MTTConstEW02B21DynamicC1FrontierImport.v1",
        "status": "CONDITIONAL_DYNAMIC_C1_GRAM_EXACT_SELECTED_SOURCE_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B21-DYNAMIC-OVERLAP-KERNEL-OR-PRIMITIVE-C1-SOURCE-EMISSION",
        "inputs": {
            "B20_candidate": rel(b20_path),
            "B20_boundary": rel(b20_boundary_path),
            "dynamic_overlap_certificate": rel(dyn_cert_path),
            "dynamic_transfer_hessian_certificate": rel(hess_cert_path),
            "phifin_s2_honest_replay_certificate": rel(replay_cert_path),
            "q79_selected_source_promotion_gate_certificate": rel(promo_cert_path),
        },
        "what_closes_conditionally": {
            "exact_72_real_coordinate_system_fixed": hess_cert["what_closes_now"]["exact_72_real_coordinate_system_fixed"],
            "conditional_A_transpose_A_Gram_computed": hess_cert["what_closes_now"]["conditional_A_transpose_A_Gram_computed"],
            "conditional_b_conditional_computed": hess_cert["what_closes_now"]["conditional_b_conditional_computed"],
            "conditional_deltaTheta_Gram_solve_exact": hess_cert["what_closes_now"]["conditional_deltaTheta_Gram_solve_exact"],
            "linear_algebra_obstruction_removed": hess_cert["what_closes_now"]["linear_algebra_obstruction_removed"],
            "D_E_value_shapes_and_honest_replay_imported": replay_cert["what_closes_now"]["D_E_value_shapes_and_honest_replay_imported"],
            "dotD_projector_value_shapes_and_honest_replay_imported": replay_cert["what_closes_now"]["dotD_projector_value_shapes_and_honest_replay_imported"],
            "selected_source_promotion_gate_ready": promo_cert["verdict"]["promotion_gate_ready"],
        },
        "conditional_values": {
            "coordinate_system": "fixed 72-real C1 row coordinate system",
            "A_transpose_A": [[12, 0], [0, 12]],
            "A_transpose_b": [12, 12],
            "b_norm_square": 24,
            "condition_number": 1,
            "deltaTheta_conditional": [1, 1],
            "residual": 0,
        },
        "not_promoted": {
            "dynamic_kernel_emitted": dyn_cert["guardrails"]["dynamic_kernel_emitted"],
            "selected_C1_primitive_emitted": dyn_cert["guardrails"]["selected_C1_primitive_emitted"],
            "selected_A_selected_claimed": hess_cert["guardrails"]["selected_A_selected_claimed"],
            "selected_b_selected_claimed": hess_cert["guardrails"]["selected_b_selected_claimed"],
            "selected_Hessian_blocks_claimed": hess_cert["guardrails"]["selected_Hessian_blocks_claimed"],
            "selected_deltaTheta_C1_claimed": hess_cert["guardrails"]["selected_deltaTheta_C1_claimed"],
            "selected_D_E_source_promotion": replay_cert["what_remains_open"]["selected_D_E_source_promotion"],
            "selected_dotD_source_verified": replay_cert["what_remains_open"]["selected_dotD_source_verified"],
        },
        "next_strict_gate": hess_cert["next_required_artifact"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    parameter_bridge = {
        "schema": "MTTConstEW02B21ProvisionalUniversalParameterBridge.v1",
        "status": "PROVISIONAL_FEW_PARAMETER_BRIDGE_ALLOWED_NOT_STRICT_NOKNOB",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B21-PROVISIONAL-UNIVERSAL-PARAMETER-BRIDGE",
        "purpose": (
            "Record the user's allowed working assumption that one or a few "
            "universal constants may be provisionally admitted while source "
            "derivation is pursued."
        ),
        "allowed_parameters": [
            {
                "name": "u_dyn",
                "role": "universal dynamic-transfer/source-strength scale for the same-source C1/retarded derivative layer",
                "allowed_as": "temporary bridge parameter",
                "must_later_tie_to": "selected dynamic transfer identity, selected primitive C1 contractions, or alpha1/source-strength theorem",
            },
            {
                "name": "u_phys",
                "role": "universal physical unit/anchor shared with alpha1 metrology if strict alpha_phys remains value-open",
                "allowed_as": "temporary bridge parameter",
                "must_later_tie_to": "rod/clock central-circle or M-theory/modal-gap physical-unit theorem",
            },
        ],
        "forbidden_uses": [
            "choosing source branch by matching observed weak angle",
            "fitting observed alpha(0), alpha(M_Z), masses, CKM, or PMNS",
            "renaming sector-specific residuals as universal constants",
            "claiming no-knob or physical weak-angle closure before source derivation",
        ],
        "credibility_policy": {
            "strict_no_knob_lane_remains_primary": True,
            "few_parameter_lane_is_a_bridge_not_final": True,
            "parameters_must_be_global_not_sector_tuned": True,
            "parameters_must_feed_multiple_constants_or_be_retired": True,
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstEW02B21Boundary.v1",
        "status": "NO_LINEAR_ALGEBRA_OBSTRUCTION_STRICT_SOURCE_AND_PROVISIONAL_PARAMETER_BRIDGES_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B21-BOUNDARY",
        "closed_now": {
            "static_B20_matterslot_overlap_preserved": b20["static_matterslot_overlap_blocker_retired"],
            "conditional_dynamic_C1_Gram_exact": True,
            "conditional_deltaTheta_C1_exact": True,
            "linear_algebra_obstruction_removed": True,
            "source_promotion_gate_ready": True,
            "provisional_few_parameter_lane_formalized": True,
        },
        "still_open": {
            "selected_same_source_dynamic_transfer_identity": True,
            "honest_Galerkin_C1_contractions": True,
            "selected_A_selected": True,
            "selected_b_selected": True,
            "selected_Hessian_blocks": True,
            "selected_D_E_source_promotion": True,
            "selected_dotD_source_verified": True,
            "selected_truncation_error_certificate": True,
            "EndE_rhoE_finite_response": b20_boundary["still_open"]["EndE_rhoE_values_or_threshold_operator"],
            "actual_xL_source_emission": True,
            "physical_weak_angle_closure": True,
            "strict_no_knob_closure": True,
        },
        "provisional_lane": {
            "available": True,
            "not_no_knob": True,
            "maximum_recommended_parameters_before_source_derivation": 2,
            "names": ["u_dyn", "u_phys"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02B21NextWork.v1",
        "status": "NEXT_WORKORDER_SOURCE_PROMOTION_OR_PARAMETERIZED_REPLAY",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B22-SOURCE-PROMOTION-OR-PARAMETERIZED-BRIDGE-REPLAY",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B22-SAME-SOURCE-DYNAMIC-TRANSFER-IDENTITY",
            "task": "Promote the conditional 72-real dynamic transfer/Hessian/b packet by deriving it from the selected same-source operator identity.",
        },
        "parallel": {
            "label": "CONST-EW-02 / WEAK-MIXING / B22-HONEST-GALERKIN-C1-CONTRACTIONS",
            "task": "Emit honest selected Galerkin primitive C1 contractions with D_E/Riesz/Green/dotD provenance and truncation error.",
        },
        "bridge": {
            "label": "CONST-EW-02 / WEAK-MIXING / B22-PROVISIONAL-U-DYN-U-PHYS-REPLAY",
            "task": "Build a transparent two-universal-parameter replay ledger to quantify what remains if u_dyn/u_phys are temporarily admitted, without using observed values as source selectors.",
        },
    }

    candidate = {
        "candidate": "MTTConstEW02WeakMixingB21DynamicC1OrFreeParameterBridge",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B21-DYNAMIC-C1-OR-ENDE-FINITE-RESPONSE",
        "output_packets": {
            "dynamic_c1_frontier_import": rel(IMPORT_PACKET),
            "provisional_universal_parameter_bridge": rel(PARAM_PACKET),
            "weak_mixing_b21_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTEW02B21ConditionalDynamicC1AndParameterBridgeTheorem",
            "proved": True,
            "statement": (
                "After B20 static routing, the dynamic C1 linear algebra is exact "
                "conditionally: A^T A=12 I_2, A^T b=(12,12), ||b||^2=24, "
                "and deltaTheta=(1,1). Therefore the remaining strict proof gap "
                "is source promotion: same-source dynamic transfer identity or "
                "honest Galerkin C1 contractions. A provisional one/few universal "
                "parameter bridge may be used as scaffolding, but it is explicitly "
                "not no-knob closure and cannot select the source branch."
            ),
        },
        "conditional_dynamic_C1_exact": True,
        "dynamic_C1_selected_source_promoted": False,
        "provisional_few_parameter_lane_available": True,
        "provisional_few_parameter_lane_not_no_knob": True,
        "strict_xL_emitted_now": False,
        "physical_weak_angle_closure": False,
        "what_closes_now": boundary["closed_now"],
        "what_remains_open": boundary["still_open"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B21_DynamicC1OrFreeParameterBridge_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "conditional_dynamic_C1_exact": True,
        "dynamic_C1_selected_source_promoted": False,
        "provisional_few_parameter_lane_available": True,
        "provisional_few_parameter_lane_not_no_knob": True,
        "strict_xL_emitted_now": False,
        "physical_weak_angle_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_primary": next_work["primary"]["label"],
        "next_bridge": next_work["bridge"]["label"],
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B21 Dynamic C1 Or Free Parameter Bridge v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B21-DYNAMIC-C1-OR-ENDE-FINITE-RESPONSE`

## Result

B21 imports the dynamic C1 frontier after static matter-slot closure.

Conditional dynamic result:

```text
A^T A = 12 I_2
A^T b = (12, 12)
||b||^2 = 24
condition number = 1
deltaTheta_C1 = (1, 1)
residual = 0
```

This removes the finite linear-algebra obstruction. It does not promote
`A_selected`, `b_selected`, selected Hessian blocks, selected primitive C1
contractions, or the physical weak angle.

## Provisional Parameter Lane

We also record a bridge lane:

```text
u_dyn  = universal dynamic transfer/source-strength bridge
u_phys = universal physical unit/anchor bridge
```

This lane is allowed for exploratory replay only. It is not no-knob closure,
cannot select source branches, and must either tie back to selected source
theorems or be retired.

## Next

`CONST-EW-02 / WEAK-MIXING / B22-SOURCE-PROMOTION-OR-PARAMETERIZED-BRIDGE-REPLAY`
"""

    for path, payload in [
        (IMPORT_PACKET, dynamic_import),
        (PARAM_PACKET, parameter_bridge),
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
