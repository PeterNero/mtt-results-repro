"""Build CONST-EW-02 B27 C1 execution-stack import and source-promotion frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
SM = TEXPAPERS / "mtt-sm-parity-closure"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_ew_02_weak_mixing_b27_c1_execution_stack_import"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
C1_VALUES = BASE / "c1_algebraic_values_import.packet.json"
TRACE_MEASURE = BASE / "trace_measure_and_boundary_import.packet.json"
LAST_SOURCE = BASE / "last_source_contract_import.packet.json"
WEAK_MIXING = BASE / "weak_mixing_b27_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B27_C1ExecutionStackImport_v1.md"

STATUS = "MTT_CONST_EW_02_B27_C1_EXECUTION_STACK_IMPORTED_SOURCE_PROMOTION_OPEN"


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

    b26_path = DATA / "const_ew_02_weak_mixing_b26_two_edge_promotion_contract.candidate.json"
    b26_c1_path = DATA / "const_ew_02_weak_mixing_b26_two_edge_promotion_contract" / "primitive_c1_sourcevalue_contract.packet.json"

    sm_c1_exec_path = SM / "candidate_data" / "selected_c1kernelvaluesexecution_or_physicalsourcepromotion.candidate.json"
    sm_c1_exec_cert_path = SM / "certificates" / "selected_c1kernelvaluesexecution_or_physicalsourcepromotion_certificate.json"
    sm_c1_values_path = SM / "candidate_data" / "selected_c1kernelvaluesexecution_or_physicalsourcepromotion" / "route_b_algebraic_kernel_value_execution_attempt.packet.json"
    sm_c1_barrier_path = SM / "candidate_data" / "selected_c1kernelvaluesexecution_or_physicalsourcepromotion" / "promotion_barrier_and_next_gate.packet.json"
    sm_trace_path = SM / "candidate_data" / "selected_c1tracemeasurepromotion_or_actionboundaryproof.candidate.json"
    sm_trace_cert_path = SM / "certificates" / "selected_c1tracemeasurepromotion_or_actionboundaryproof_certificate.json"
    sm_boundary_path = SM / "candidate_data" / "selected_c1tracemeasurepromotion_or_actionboundaryproof" / "finite_trace_boundary_cancellation_certificate.packet.json"
    sm_physical_equiv_path = SM / "candidate_data" / "selected_physicalc1actionidentity_or_samesourcebselectedemission.candidate.json"
    sm_physical_equiv_cert_path = SM / "certificates" / "selected_physicalc1actionidentity_or_samesourcebselectedemission_certificate.json"
    sm_last_contract_path = SM / "candidate_data" / "selected_physicalphifinc1actionsource_or_provenanceindependencetheorem.candidate.json"
    sm_last_contract_cert_path = SM / "certificates" / "selected_physicalphifinc1actionsource_or_provenanceindependencetheorem_certificate.json"
    sm_final_nogo_path = SM / "candidate_data" / "selected_finalsourceemission_actualfill_or_nogowitness.candidate.json"
    sm_final_nogo_cert_path = SM / "certificates" / "selected_finalsourceemission_actualfill_or_nogowitness_certificate.json"

    b26 = load(b26_path)
    b26_c1 = load(b26_c1_path)
    sm_c1_exec = load(sm_c1_exec_path)
    sm_c1_exec_cert = load(sm_c1_exec_cert_path)
    sm_c1_values = load(sm_c1_values_path)
    sm_c1_barrier = load(sm_c1_barrier_path)
    sm_trace = load(sm_trace_path)
    sm_trace_cert = load(sm_trace_cert_path)
    sm_boundary = load(sm_boundary_path)
    sm_physical_equiv = load(sm_physical_equiv_path)
    sm_physical_equiv_cert = load(sm_physical_equiv_cert_path)
    sm_last_contract = load(sm_last_contract_path)
    sm_last_contract_cert = load(sm_last_contract_cert_path)
    sm_final_nogo = load(sm_final_nogo_path)
    sm_final_nogo_cert = load(sm_final_nogo_cert_path)

    counts = sm_c1_values["counts"]
    algebraic_certificate = sm_c1_values["algebraic_consistency_certificate"]

    c1_values_packet = {
        "schema": "MTTConstEW02B27C1AlgebraicValuesImport.v1",
        "status": "C1_ALGEBRAIC_VALUE_LAYER_IMPORTED_PROMOTION_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B27-PRIMITIVE-C1-ATOM-VALUE-EXECUTION",
        "inputs": {
            "B26_C1_contract": rel(b26_c1_path),
            "sm_c1_execution_candidate": rel(sm_c1_exec_path),
            "sm_c1_execution_certificate": rel(sm_c1_exec_cert_path),
            "sm_algebraic_values_packet": rel(sm_c1_values_path),
            "sm_promotion_barrier": rel(sm_c1_barrier_path),
        },
        "imported_counts": counts,
        "imported_algebraic_certificate": algebraic_certificate,
        "what_this_retires_locally": {
            "primitive_C1_value_slot_bookkeeping": True,
            "conditional_A_transpose_A_and_A_transpose_b_values": True,
            "conditional_deltaTheta_C1_replay": True,
            "locked_target_algebraic_replay": algebraic_certificate["passes_locked_target_by_algebraic_replay"],
        },
        "why_not_promoted": sm_c1_barrier["statement"],
        "promotion_still_required": sm_c1_barrier["minimal_next_gate"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    trace_measure_packet = {
        "schema": "MTTConstEW02B27TraceMeasureBoundaryImport.v1",
        "status": "TRACE_MEASURE_SUPPORT_AND_ALGEBRAIC_BOUNDARY_IMPORTED_PHYSICAL_ACTION_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B27-TRACE-MEASURE-BOUNDARY-IMPORT",
        "inputs": {
            "sm_trace_measure_candidate": rel(sm_trace_path),
            "sm_trace_measure_certificate": rel(sm_trace_cert_path),
            "sm_boundary_certificate": rel(sm_boundary_path),
        },
        "what_closes": sm_trace["what_closes_now"],
        "boundary_certificate": {
            "algebraic_boundary_closed_now": sm_boundary["algebraic_boundary_closed_now"],
            "physical_boundary_promoted_now": sm_boundary["physical_boundary_promoted_now"],
            "scope_limit": sm_boundary["scope_limit"],
        },
        "what_remains_open": sm_trace["what_remains_open"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    last_source_packet = {
        "schema": "MTTConstEW02B27LastSourceContractImport.v1",
        "status": "LAST_C1_SOURCE_CONTRACT_IMPORTED_ACTUAL_SOURCE_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B27-LAST-C1-SOURCE-CONTRACT",
        "inputs": {
            "sm_physical_action_equivalence": rel(sm_physical_equiv_path),
            "sm_physical_action_equivalence_certificate": rel(sm_physical_equiv_cert_path),
            "sm_last_source_contract": rel(sm_last_contract_path),
            "sm_last_source_contract_certificate": rel(sm_last_contract_cert_path),
            "sm_final_actual_fill_nogo": rel(sm_final_nogo_path),
            "sm_final_actual_fill_nogo_certificate": rel(sm_final_nogo_cert_path),
        },
        "equivalence_theorem": sm_physical_equiv["theorem"],
        "last_source_contract_theorem": sm_last_contract["theorem"],
        "latest_actual_fill_result": sm_final_nogo["theorem"],
        "retired_as_blockers": {
            "alpha1_dotD": sm_final_nogo_cert["alpha1_dotd_retired_as_blockers"],
            "canonical_residual_values": sm_final_nogo_cert["canonical_residual_values_retired_as_blocker"],
            "finite_measure_normalization": sm_last_contract["promotion_decision"]["finite_measure_normalization_retired"],
            "formal_computation_layer": sm_last_contract_cert["formal_computation_layer_closed"],
        },
        "remaining_exact_cutset": {
            "same_branch_Phi_fin_C1_source_emission": True,
            "same_source_b_selected_emission": True,
            "phase_R_Z_source_selection": True,
            "shift_R_X_source_selection": True,
            "no_extra_physical_boundary_or_source_term": True,
            "or_independent_Galerkin_or_row_provenance_run": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    weak_mixing_boundary = {
        "schema": "MTTConstEW02B27WeakMixingBoundary.v1",
        "status": "C1_EXECUTION_LAYER_ADVANCED_PHYSICAL_WEAK_ANGLE_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B27-BOUNDARY",
        "preserved_from_B26": {
            "internal_lambda_12_closed": b26["internal_lambda_12_closed_preserved"],
            "internal_lambda_12_value": b26["internal_lambda_12_value"],
            "u_dyn_source_derived": b26["u_dyn_source_derived_preserved"],
            "two_edge_contract_built": b26["two_edge_contract_built"],
        },
        "advanced_now": {
            "primitive_C1_algebraic_values_filled": counts["primitive_values_filled"],
            "total_C1_algebraic_values_filled": counts["total_algebraic_values_filled"],
            "formal_trace_measure_support_imported": sm_trace["what_closes_now"]["formal_measure_pairing_sufficiency_retained"],
            "algebraic_finite_trace_boundary_closed": sm_trace["what_closes_now"]["algebraic_finite_trace_boundary_cancellation"],
            "last_source_contract_built": sm_last_contract_cert["last_source_theorem_contract_built"],
        },
        "still_open": {
            "physical_weak_angle_closure": True,
            "K_phys_or_f_ab": True,
            "mu_match": True,
            "RG_and_threshold_scheme": True,
            "physical_Phi_fin_C1_action_source_theorem": True,
            "same_source_b_selected": True,
            "independent_hessian_or_quadrature_source": True,
            "strict_full_no_knob_closure": True,
        },
        "claim_upgrade": "B27 upgrades the primitive-C1 edge from missing values to value-filled/formal-measure-ready/source-promotion-open.",
        "forbidden_claim": "numeric physical weak angle or strict no-knob electroweak closure",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02B27NextWork.v1",
        "status": "NEXT_WORKORDER_LAST_C1_SOURCE_OR_GAUGEKINETIC_ACTION",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B28-SAMEBRANCH-PHIFIN-C1-SOURCE-OR-GAUGEKINETIC-ACTION",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B28-SAMEBRANCH-PHIFIN-C1-SOURCE-EMISSION",
            "task": "Try to prove the physical Phi_fin^C1 action emits the same R_Z/R_X/b_selected packet with no extra boundary/source term.",
        },
        "parallel": {
            "label": "CONST-EW-02 / WEAK-MIXING / B28-GAUGEKINETIC-ACTION-ANCHOR",
            "task": "Continue the gauge-kinetic edge: try to emit K_phys/f_ab, mu_match, and RG/threshold scheme from same-branch action normalization.",
        },
    }

    candidate = {
        "candidate": "MTTConstEW02WeakMixingB27C1ExecutionStackImport",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B27-EXECUTE-GAUGEKINETIC-OR-C1-EDGE",
        "output_packets": {
            "c1_algebraic_values_import": rel(C1_VALUES),
            "trace_measure_and_boundary_import": rel(TRACE_MEASURE),
            "last_source_contract_import": rel(LAST_SOURCE),
            "weak_mixing_b27_boundary": rel(WEAK_MIXING),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTEW02B27C1ExecutionStackImportTheorem",
            "proved": True,
            "statement": (
                "The sibling SM-parity C1 execution stack can be imported as a support theorem for the weak-mixing primitive-C1 edge: "
                "72 primitive C1 algebraic values, 2 Hessian/source values, and 36 sector response values are filled, formal trace/Frobenius support and finite trace algebraic boundary cancellation are available, and the remaining source-promotion cutset is exactly same-branch Phi_fin^C1 source emission or an independent Galerkin/row-provenance run. This is not physical weak-angle closure."
            ),
        },
        "primitive_C1_algebraic_values_filled": counts["primitive_values_filled"],
        "total_C1_algebraic_values_filled": counts["total_algebraic_values_filled"],
        "formal_computation_layer_closed_as_support": sm_last_contract_cert["formal_computation_layer_closed"],
        "last_source_theorem_contract_built": sm_last_contract_cert["last_source_theorem_contract_built"],
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B27_C1ExecutionStackImport_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "primitive_C1_algebraic_values_filled": counts["primitive_values_filled"],
        "total_C1_algebraic_values_filled": counts["total_algebraic_values_filled"],
        "formal_computation_layer_closed_as_support": sm_last_contract_cert["formal_computation_layer_closed"],
        "last_source_theorem_contract_built": sm_last_contract_cert["last_source_theorem_contract_built"],
        "alpha1_dotD_retired_as_blockers": sm_final_nogo_cert["alpha1_dotd_retired_as_blockers"],
        "canonical_residual_values_retired_as_blocker": sm_final_nogo_cert["canonical_residual_values_retired_as_blocker"],
        "same_branch_phifin_source_closed": sm_final_nogo_cert["same_branch_phifin_source_closed"],
        "independent_hessian_quadrature_source_closed": sm_final_nogo_cert["independent_hessian_quadrature_source_closed"],
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_primary": next_work["primary"]["label"],
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B27 C1 Execution Stack Import v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B27-EXECUTE-GAUGEKINETIC-OR-C1-EDGE`

## Imported Progress

```text
primitive C1 algebraic values filled = {counts["primitive_values_filled"]}
hessian/source values filled         = {counts["hessian_values_filled"]}
sector response values filled        = {counts["sector_values_filled"]}
total algebraic C1 values filled     = {counts["total_algebraic_values_filled"]}
finite trace boundary closed         = {sm_boundary["algebraic_boundary_closed_now"]}
last source contract built           = {sm_last_contract_cert["last_source_theorem_contract_built"]}
```

This retires primitive-C1 value-slot bookkeeping as the active blocker for the
weak-mixing C1 edge. It does not promote those algebraic values as physical
source values.

## Still Open

```text
same-branch Phi_fin^C1 source emission
same-source b_selected emission
phase R_Z and shift R_X source selection
no extra physical boundary/source term
or independent Galerkin/row-provenance run
K_phys/f_ab, mu_match, and RG/threshold scheme on the gauge-kinetic edge
```

## Next

`CONST-EW-02 / WEAK-MIXING / B28-SAMEBRANCH-PHIFIN-C1-SOURCE-OR-GAUGEKINETIC-ACTION`
"""

    for path, payload in [
        (C1_VALUES, c1_values_packet),
        (TRACE_MEASURE, trace_measure_packet),
        (LAST_SOURCE, last_source_packet),
        (WEAK_MIXING, weak_mixing_boundary),
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
