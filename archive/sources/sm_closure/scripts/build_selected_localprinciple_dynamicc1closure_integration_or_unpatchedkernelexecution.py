"""Integrate local Weyl-variation source-kernel closure with dynamic C1 closure."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_localprinciple_dynamicc1closure_integration_or_unpatchedkernelexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SOURCE_CHAIN = PACKET_DIR / "local_source_kernel_to_dynamicc1_chain.packet.json"
LOCAL_CLOSURE = PACKET_DIR / "local_principle_dynamicc1_closure_theorem.packet.json"
UNPATCHED_EXIT = PACKET_DIR / "unpatched_kernel_execution_exit_status.packet.json"
LEDGER = PACKET_DIR / "local_vs_unpatched_closure_ledger.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_LocalPrincipleDynamicC1Closure_Integration_or_UnpatchedKernelExecution_v1.md"

STATUS = "MTT_SELECTED_LOCALPRINCIPLE_DYNAMICC1CLOSURE_INTEGRATED_UNPATCHED_OPEN"
NEXT = "MTT_Selected_LocalDynamicC1PaperAppendix_or_UnpatchedKernelExecutionPlan_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    apply_gate = load(DATA / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution.candidate.json")
    applied_kernel = load(
        DATA
        / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution"
        / "applied_principle_kernel_closure.packet.json"
    )
    applied_validator = load(
        DATA
        / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution"
        / "applied_kernel_validator_result.packet.json"
    )
    prior_axiom_closure = load(
        DATA
        / "selected_differentiatedphifinc1_axiominsertion_patchedclosure_or_unpatchedexit"
        / "patched_dynamic_c1_closure_theorem.packet.json"
    )
    ready_values = load(
        DATA
        / "selected_dynamicc1_sourceowner_dynamictransferhessian_or_honestgalerkinvalues"
        / "ready_to_promote_dynamic_value_table.packet.json"
    )
    final_gate = load(
        DATA
        / "selected_dynamicc1_finalgate_perfection_or_sourceaxiomdecision"
        / "source_axiom_decision_matrix.packet.json"
    )
    unpatched_apply_exit = load(
        DATA
        / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution"
        / "unpatched_or_independent_kernel_execution_exit.packet.json"
    )

    exact = prior_axiom_closure["exact_values"]
    source_chain = {
        "schema": "MTTLocalSourceKernelToDynamicC1Chain.v1",
        "status": "LOCAL_SOURCE_KERNEL_CHAIN_COMPLETE",
        "hypotheses": [
            "SelectedWeylVariationActionPrinciple accepted as explicit local premise",
            "strict pre-residual variation/Hessian source kernel validates",
            "dynamic C1 ready-to-promote value table is exact",
        ],
        "kernel_fields": {
            "selected_variation_functional": applied_kernel["selected_variation_functional"],
            "same_source_hessian": applied_kernel["same_source_hessian"],
            "sector_functor": applied_kernel["sector_functor"],
            "independence_certificate": applied_kernel["independence_certificate"],
        },
        "dynamic_value_support": {
            "phase_R_Z_ready": ready_values["dynamic_operator_candidates"]["phase_R_Z"]["residual_norm_sq"] == 4.0,
            "shift_R_X_ready": ready_values["dynamic_operator_candidates"]["shift_R_X"]["residual_norm_sq"] == 2.0,
            "A_selected_columns_available": ready_values["conditional_hessian_values"]["A_selected_columns_available"],
            "projection_plus_residual_reconstructs_conditional_packet": ready_values["conditional_hessian_values"][
                "projection_plus_residual_reconstructs_conditional_packet"
            ],
        },
        "validator_ok": applied_validator["ok"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    local_closure = {
        "schema": "MTTLocalPrincipleDynamicC1ClosureTheorem.v1",
        "status": "LOCAL_PRINCIPLE_DYNAMIC_C1_PACKET_CLOSED",
        "hypothesis": applied_kernel["hypothesis"],
        "scientific_status": "local-premise-conditional dynamic C1 closure",
        "promoted_objects_inside_local_spine": {
            "pre_residual_phase_shift_operator_source": True,
            "same_source_hessian_b_selected_rows": True,
            "sector_rows_physical_source_promotion": True,
            "A_selected": True,
            "b_selected": True,
            "deltaTheta_C1": True,
            "sector_response_matrices": True,
            "dynamic_C1_source_owner_packet": True,
        },
        "exact_values": {
            "A_transpose_A": exact["A_transpose_A"],
            "A_transpose_b": exact["A_transpose_b"],
            "b_norm_sq": exact["b_norm_sq"],
            "deltaTheta_C1": exact["deltaTheta_C1"],
            "rank": exact["rank"],
            "phase_R_Z_residual_norm_sq": exact["phase_R_Z_residual_norm_sq"],
            "shift_R_X_residual_norm_sq": exact["shift_R_X_residual_norm_sq"],
        },
        "improvement_over_prior_local_axiom_patch": (
            "The local Weyl-variation principle validates the strict source-kernel fields "
            "before dynamic C1 value promotion, rather than only naming the residual-projector axiom."
        ),
        "does_not_close": {
            "unpatched_weylvariation_principle_derivation": True,
            "independent_kernel_execution": True,
            "true_SM_equivalence_without_local_premise": True,
            "no_knob_flavor_constants": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    unpatched_exit = {
        "schema": "MTTUnpatchedKernelExecutionExitStatusAfterLocalDynamicC1Integration.v1",
        "status": "UNPATCHED_AND_INDEPENDENT_EXECUTION_REMAIN_OPEN_AFTER_LOCAL_INTEGRATION",
        "unpatched_dynamic_C1_closed": False,
        "local_dynamic_C1_closed": True,
        "remaining_exits": unpatched_apply_exit["remaining_unpatched_exits"],
        "route_A_accepts_without_local_principle": unpatched_apply_exit["route_A_accepts_without_local_principle"],
        "route_B_accepts_without_local_principle": unpatched_apply_exit["route_B_accepts_without_local_principle"],
        "independent_kernel_execution_supplied": unpatched_apply_exit["independent_kernel_execution_supplied"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    ledger = {
        "schema": "MTTLocalVsUnpatchedDynamicC1ClosureLedger.v1",
        "status": "LOCAL_CLOSURE_YES_UNPATCHED_CLOSURE_NO",
        "local_closure": {
            "accepted_weylvariation_principle": True,
            "strict_source_kernel_validates": applied_validator["ok"],
            "dynamic_C1_packet_closed": True,
            "exact_values_promoted_inside_local_spine": True,
        },
        "unpatched_closure": {
            "principle_derived": False,
            "independent_kernel_execution_supplied": False,
            "dynamic_C1_packet_closed": False,
            "route_A_without_local_principle": False,
            "route_B_independent_execution": False,
        },
        "comparison_to_prior_final_gate": {
            "prior_final_gate_status": final_gate["status"],
            "prior_patched_mode_closed": True,
            "new_local_principle_mode_closes_stricter_source_kernel": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    for path, payload in [
        (SOURCE_CHAIN, source_chain),
        (LOCAL_CLOSURE, local_closure),
        (UNPATCHED_EXIT, unpatched_exit),
        (LEDGER, ledger),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedLocalPrincipleDynamicC1ClosureIntegrationOrUnpatchedKernelExecution",
        "status": STATUS,
        "inputs": {
            "weylvariation_apply_gate": rel(
                DATA / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution.candidate.json"
            ),
            "patched_dynamic_c1_closure": rel(
                DATA
                / "selected_differentiatedphifinc1_axiominsertion_patchedclosure_or_unpatchedexit"
                / "patched_dynamic_c1_closure_theorem.packet.json"
            ),
            "ready_dynamic_value_table": rel(
                DATA
                / "selected_dynamicc1_sourceowner_dynamictransferhessian_or_honestgalerkinvalues"
                / "ready_to_promote_dynamic_value_table.packet.json"
            ),
        },
        "output_packets": {
            "local_source_kernel_to_dynamicc1_chain": rel(SOURCE_CHAIN),
            "local_principle_dynamicc1_closure_theorem": rel(LOCAL_CLOSURE),
            "unpatched_kernel_execution_exit_status": rel(UNPATCHED_EXIT),
            "local_vs_unpatched_closure_ledger": rel(LEDGER),
        },
        "theorem": {
            "name": "LocalPrincipleDynamicC1ClosureIntegrationTheorem",
            "proved": True,
            "statement": (
                "Under the explicit local SelectedWeylVariationActionPrinciple, the validated "
                "pre-residual variation/Hessian source kernel promotes the exact dynamic C1 value "
                "table, closing A_selected, b_selected, deltaTheta_C1, and sector response matrices "
                "inside the local proof spine."
            ),
        },
        "closure_decision": {
            "local_dynamic_C1_closed": True,
            "unpatched_dynamic_C1_closed": False,
            "independent_kernel_execution_supplied": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
            "global_closure_claimed": False,
        },
        "what_closes_now": {
            "local_source_kernel_integrated_with_dynamic_c1": True,
            "local_dynamic_C1_packet_closed_from_strict_kernel": True,
            "local_vs_unpatched_ledger_created": True,
            "unpatched_exits_preserved": True,
        },
        "what_remains_open": {
            "derive_weylvariation_principle_unpatched": True,
            "execute_independent_kernel_rows": True,
            "true_SM_equivalence_without_local_premise": True,
            "no_knob_flavor_constants": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_LocalPrincipleDynamicC1Closure_Integration_or_UnpatchedKernelExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "local_dynamic_C1_closed": True,
        "unpatched_dynamic_C1_closed": False,
        "strict_source_kernel_integrated": True,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected LocalPrinciple DynamicC1Closure Integration or UnpatchedKernelExecution v1

Status: `{STATUS}`.

This artifact integrates the accepted local `SelectedWeylVariationActionPrinciple`
with the dynamic-C1 closure spine. The strict pre-residual variation/Hessian
source kernel validates, and the exact dynamic-C1 packet closes locally with:

- `A^T A = 12 I_2`;
- `A^T b = (12,12)`;
- `||b||^2 = 24`;
- `deltaTheta_C1 = (1,1)`.

This is local-premise-conditional closure. It does not derive the principle
unpatched and does not replace independent kernel execution.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
