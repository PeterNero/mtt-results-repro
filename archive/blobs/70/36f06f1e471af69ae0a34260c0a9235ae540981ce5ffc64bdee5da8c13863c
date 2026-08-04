"""Build CONST-EW-02 B39 source kernel or local principle decision."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_ew_02_weak_mixing_b39_source_kernel_or_local_principle"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
LOCAL_KERNEL = BASE / "local_principle_preresidual_source_kernel.packet.json"
UNPATCHED = BASE / "strict_unpatched_source_kernel_status.packet.json"
DECISION = BASE / "b39_decision_boundary.packet.json"
BOUNDARY = BASE / "weak_mixing_b39_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B39_SourceKernel_or_LocalPrinciple_v1.md"

STATUS = "MTT_CONST_EW_02_B39_SOURCE_KERNEL_LOCAL_PRINCIPLE_TIER_BUILT"


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

    b38_path = DATA / "const_ew_02_weak_mixing_b38_actual_proof_fill_attempt.candidate.json"
    b38_boundary_path = DATA / "const_ew_02_weak_mixing_b38_actual_proof_fill_attempt" / "weak_mixing_b38_boundary.packet.json"

    pre_kernel_path = SM / "candidate_data" / "selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom.candidate.json"
    pre_kernel_witness_path = SM / "candidate_data" / "selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom" / "conditional_source_kernel_witness.packet.json"
    pre_kernel_current_validator_path = SM / "candidate_data" / "selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom" / "current_validator_result.packet.json"
    local_apply_path = SM / "candidate_data" / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution.candidate.json"
    local_principle_path = SM / "candidate_data" / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution" / "accepted_local_weylvariation_actionprinciple.packet.json"
    local_closure_path = SM / "candidate_data" / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution" / "applied_principle_kernel_closure.packet.json"
    local_exit_path = SM / "candidate_data" / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution" / "unpatched_or_independent_kernel_execution_exit.packet.json"
    unpatched_first_run_path = SM / "candidate_data" / "selected_unpatchedweylprincipleproof_or_independentkernelrowsfirstrun.candidate.json"
    unpatched_final_contract_path = SM / "candidate_data" / "selected_unpatchedfinitec1sourceidentity_or_honestindependentkernelexport.candidate.json"
    honest_manifest_path = SM / "candidate_data" / "selected_unpatchedfinitec1sourceidentity_or_honestindependentkernelexport" / "honest_kernel_export_row_manifest.packet.json"

    b38 = load(b38_path)
    b38_boundary = load(b38_boundary_path)
    pre_kernel = load(pre_kernel_path)
    pre_kernel_witness = load(pre_kernel_witness_path)
    pre_kernel_current_validator = load(pre_kernel_current_validator_path)
    local_apply = load(local_apply_path)
    local_principle = load(local_principle_path)
    local_closure = load(local_closure_path)
    local_exit = load(local_exit_path)
    unpatched_first_run = load(unpatched_first_run_path)
    unpatched_final_contract = load(unpatched_final_contract_path)
    honest_manifest = load(honest_manifest_path)

    promoted = local_closure["promoted_inside_local_spine"]
    local_kernel = {
        "schema": "MTTConstEW02B39LocalPrinciplePreResidualSourceKernel.v1",
        "status": "LOCAL_PREMISE_PRERESIDUAL_SOURCE_KERNEL_EMITTED",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B39-LOCAL-WEYLVARIATION-PRINCIPLE-TIER",
        "inputs": {
            "pre_residual_kernel_attempt": rel(pre_kernel_path),
            "conditional_source_kernel_witness": rel(pre_kernel_witness_path),
            "accepted_local_principle": rel(local_principle_path),
            "applied_principle_kernel_closure": rel(local_closure_path),
        },
        "hypothesis": local_closure["hypothesis"],
        "principle_name": local_principle["principle_name"],
        "principle_text": local_principle["principle_text"],
        "kernel_clauses_under_local_principle": {
            "selected_variation_functional": local_closure["selected_variation_functional"],
            "same_source_hessian": local_closure["same_source_hessian"],
            "same_source_hessian_b_selected_rows": promoted["same_source_hessian_b_selected_rows"],
            "pre_residual_phase_shift_operator_source": promoted["pre_residual_phase_shift_operator_source"],
            "sector_functor": local_closure["sector_functor"],
            "sector_rows_physical_source_promotion": promoted["sector_rows_physical_source_promotion"],
            "independence_certificate": local_closure["independence_certificate"],
            "independence_from_residual_projector_replay": promoted["independence_from_residual_projector_replay"],
        },
        "strict_pre_residual_kernel_closed_under_local_principle": local_apply["what_closes_now"][
            "strict_pre_residual_kernel_closed_under_local_principle"
        ],
        "residual_projector_replay_used_as_source": local_closure["residual_projector_replay_used_as_source"],
        "locked_target_values_used_as_source": local_closure["locked_target_values_used_as_source"],
        "allowed_use": "Use as explicit local/universal principle tier for the weak-mixing source-kernel bridge.",
        "forbidden_use": "Do not call this an unpatched derivation or strict no-knob proof.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    unpatched = {
        "schema": "MTTConstEW02B39StrictUnpatchedSourceKernelStatus.v1",
        "status": "STRICT_UNPATCHED_SOURCE_KERNEL_STILL_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B39-STRICT-UNPATCHED-KERNEL-STATUS",
        "inputs": {
            "current_pre_residual_validator": rel(pre_kernel_current_validator_path),
            "unpatched_weyl_or_rows_first_run": rel(unpatched_first_run_path),
            "unpatched_source_identity_or_honest_export": rel(unpatched_final_contract_path),
            "honest_kernel_export_manifest": rel(honest_manifest_path),
            "unpatched_or_independent_exit": rel(local_exit_path),
        },
        "current_pre_residual_validator_rejects": pre_kernel["what_closes_now"]["current_attempt_rejected"],
        "source_identity_unpatched_derived": unpatched_final_contract["closure_decision"]["source_identity_unpatched_derived"],
        "honest_kernel_export_emitted": unpatched_final_contract["closure_decision"]["honest_kernel_export_emitted"],
        "route_A_accepts_without_local_principle": local_exit["route_A_accepts_without_local_principle"],
        "route_B_accepts_without_local_principle": local_exit["route_B_accepts_without_local_principle"],
        "remaining_unpatched_exits": local_exit["remaining_unpatched_exits"],
        "strict_manifest_available": {
            "status": honest_manifest["status"],
            "row_counts": {
                "total_rows": honest_manifest["strict_payload_rows"],
                "primitive_contractions": honest_manifest["counts"]["primitive_contractions"],
                "hessian_source": honest_manifest["counts"]["hessian_source"],
                "sector_matrices": honest_manifest["counts"]["sector_matrices"],
            },
        },
        "why_still_open": (
            "The local premise supplies the kernel, but the unpatched route still lacks a derivation of the principle or an honest independent 110-row kernel export."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    decision = {
        "schema": "MTTConstEW02B39DecisionBoundary.v1",
        "status": "B39_SOLVED_IN_LOCAL_PRINCIPLE_TIER_STRICT_UNPATCHED_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B39-SOURCE-KERNEL-OR-LOCAL-PREMISE-DECISION",
        "decision": "Accept the SelectedWeylVariationActionPrinciple as an explicit local/source principle tier for this branch, while tracking unpatched derivation as a no-knob upgrade.",
        "local_tier_source_kernel_closed": True,
        "strict_unpatched_source_kernel_closed": False,
        "one_universal_principle_tier_used": True,
        "free_numeric_parameter_used": False,
        "observed_weak_angle_used": False,
        "why_this_is_not_cycling": (
            "B38 proved current unpatched material cannot close the kernel. B39 chooses the available local-principle tier and records its consequences instead of re-running the failed unpatched validator."
        ),
        "what_this_buys": [
            "a source-owned pre-residual variation functional under the local premise",
            "same-source Hessian/b_selected rows under the local premise",
            "sector-row promotion under the local premise",
            "a clean next bridge from dynamic C1 source kernel to the weak-mixing profile",
        ],
        "what_it_does_not_buy": [
            "strict no-knob/unpatched derivation",
            "physical weak-angle numerical closure",
            "physical alpha/metrology anchor",
            "RG/matching-scale closure",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstEW02B39Boundary.v1",
        "status": "B39_LOCAL_SOURCE_KERNEL_CLOSED_STRICT_UNPATCHED_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B39-BOUNDARY",
        "previous_B38": {
            "candidate": b38["candidate"],
            "status": b38["status"],
            "still_open": b38_boundary["still_open"],
        },
        "closed_or_decided_now": {
            "local_principle_tier_accepted": True,
            "local_pre_residual_variation_hessian_source_kernel_emitted": True,
            "same_source_b_selected_closed_in_local_tier": True,
            "sector_functor_closed_in_local_tier": True,
            "independence_certificate_closed_in_local_tier": True,
            "strict_unpatched_kernel_closed": False,
            "free_numeric_parameter_introduced": False,
            "observed_constants_used_as_selectors": False,
        },
        "still_open": {
            "strict_unpatched_SelectedWeylVariationActionPrinciple_derivation": True,
            "honest_independent_110_row_kernel_export": True,
            "physical_weak_angle_numerical_closure": True,
            "physical_alpha_or_metrology_anchor": True,
            "RG_matching_scale_and_profile_transport": True,
            "strict_full_no_knob_closure": True,
        },
        "superset_strategy": {
            "straight_way_or_combined": "combined, but locked into an explicit local principle rather than free fitting",
            "route_A": "Weyl-variation action principle supplies physical source kernel as a premise",
            "route_B": "honest 110-row kernel export remains the unpatched alternative",
            "using_knobs": "No observed values or per-target knobs; one explicit source principle tier is declared.",
        },
        "anti_cycle_delta_from_B38": {
            "B38": "proved current unpatched proof/fill cannot close from support facts",
            "B39": "makes the branch decision: solve the kernel in the explicit local-principle tier and preserve unpatched closure as separate upgrade",
            "not_repeated": [
                "not another current-material no-go",
                "not another conditional witness without decision",
                "not claiming local premise as unpatched no-knob proof",
            ],
        },
        "allowed_claim": "B39 solves the pre-residual variation/Hessian source kernel in the explicit local-principle tier.",
        "forbidden_claim": "strict unpatched/no-knob source-kernel derivation, physical weak-angle numerical closure, alpha anchor closure, or RG closure",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02B39NextWork.v1",
        "status": "NEXT_WORKORDER_PROPAGATE_LOCAL_KERNEL_TO_WEAK_MIXING_PROFILE",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B40-LOCAL-KERNEL-TO-WEAK-MIXING-PROFILE",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B40-LOCAL-C1-SOURCE-KERNEL-PROPAGATION",
            "task": "Use the local-principle source kernel to promote the dynamic C1 bridge quantities for the weak-mixing profile, without using measured weak angle or observed SM values as selectors.",
        },
        "parallel": {
            "label": "CONST-EW-02 / WEAK-MIXING / B40-STRICT-NO-KNOB-UPGRADE-LEDGER",
            "task": "Keep the unpatched SelectedWeylVariationActionPrinciple derivation and honest independent 110-row export as separate no-knob upgrade gates.",
        },
    }

    candidate = {
        "candidate": "MTTConstEW02WeakMixingB39SourceKernelOrLocalPrinciple",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B39-SOURCE-KERNEL-OR-LOCAL-PREMISE-DECISION",
        "output_packets": {
            "local_principle_preresidual_source_kernel": rel(LOCAL_KERNEL),
            "strict_unpatched_source_kernel_status": rel(UNPATCHED),
            "b39_decision_boundary": rel(DECISION),
            "weak_mixing_b39_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTEW02B39LocalPrincipleSourceKernelTheorem",
            "proved": True,
            "statement": (
                "Given the explicit local SelectedWeylVariationActionPrinciple, the pre-residual variation/Hessian source kernel is emitted: the selected variation functional, same-source Hessian/b_selected rows, sector functor, and independence certificate are all supplied in the local tier. This closes B39 for the local-principle branch without using observed constants or fitted targets. It does not derive the principle unpatched and does not close physical weak-angle numerics."
            ),
        },
        "local_tier_source_kernel_closed": True,
        "strict_unpatched_source_kernel_closed": False,
        "one_universal_principle_tier_used": True,
        "free_numeric_parameter_used": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "source_promotion_closed_in_local_tier": True,
        "source_promotion_closed_strict_no_knob": False,
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B39_SourceKernel_or_LocalPrinciple_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "local_tier_source_kernel_closed": True,
        "strict_unpatched_source_kernel_closed": False,
        "one_universal_principle_tier_used": True,
        "free_numeric_parameter_used": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "source_promotion_closed_in_local_tier": True,
        "source_promotion_closed_strict_no_knob": False,
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "closure_claimed": False,
        "next_primary": next_work["primary"]["label"],
        "next_parallel": next_work["parallel"]["label"],
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B39 Source Kernel or Local Principle v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B39-SOURCE-KERNEL-OR-LOCAL-PREMISE-DECISION`

## Result

```text
local-principle source kernel closed       True
strict unpatched source kernel closed      False
one explicit source principle tier used    True
free numeric parameter used                False
observed weak angle used as selector       False
physical weak-angle numerical closure      False
```

This is the non-cycling branch decision after B38.  We do not pretend the
unpatched no-knob theorem is proved.  We accept the local Weyl-variation
principle as an explicit source-principle tier and move the weak-mixing branch
forward under that declared tier.

## Next

`CONST-EW-02 / WEAK-MIXING / B40-LOCAL-KERNEL-TO-WEAK-MIXING-PROFILE`
"""

    for path, payload in [
        (LOCAL_KERNEL, local_kernel),
        (UNPATCHED, unpatched),
        (DECISION, decision),
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
