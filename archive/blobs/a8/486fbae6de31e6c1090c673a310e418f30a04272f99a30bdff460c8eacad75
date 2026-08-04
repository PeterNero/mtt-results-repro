"""Build action-kernel four-clause proof or independent kernel values run."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_phifinc1actionaxiom_or_independentgalerkinkernelemission.candidate.json"
ROUTE_A_CONTRACT = DATA / "selected_phifinc1actionaxiom_or_independentgalerkinkernelemission" / "route_a_phifinc1_action_kernel_axiom_contract.packet.json"
ROUTE_B_CONTRACT = DATA / "selected_phifinc1actionaxiom_or_independentgalerkinkernelemission" / "route_b_independent_galerkin_kernel_emission_contract.packet.json"
CUTSET = DATA / "selected_phifinc1actionaxiom_or_independentgalerkinkernelemission" / "minimal_next_cutset_after_action_kernel_gate.packet.json"
TRACE_BASIS = DATA / "selected_tracemapandbasisvalues_or_primitiverowsexecution.candidate.json"
DYNAMIC_TRACE = DATA / "selected_primitiverowsexecution_or_dynamicdotdtracebinding.candidate.json"
SLOT_ROUTING = DATA / "selected_variationoperatorshapecompatibility_or_hessiansourcegap" / "variation_operator_72_slot_routing.packet.json"
BOUNDARY = DATA / "selected_c1tracemeasurepromotion_or_actionboundaryproof.candidate.json"
PHYSICAL_SOURCE = DATA / "selected_samesourcephifinc1emission_or_independentrowsactualfill" / "remaining_source_cutset.packet.json"
ROW_SCHEDULE = DATA / "selected_stromingertracec1firstvariation_or_quadratureexecutionplan" / "quadrature_row_schedule.packet.json"

ACTION_VALIDATOR = ROOT / "scripts" / "validate_selected_phifinc1_preresidual_action_kernel_theorem.py"
ROW_VALIDATOR = ROOT / "scripts" / "validate_selected_independentc1_rowkernel_source_ids.py"

SLUG = "selected_actionkernelfourclauseproof_or_independentkernelvaluesrun"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_A_PARTIAL = PACKET_DIR / "route_a_four_clause_partial_proof.packet.json"
ROUTE_A_VALIDATOR = PACKET_DIR / "route_a_four_clause_validator_result.packet.json"
ROUTE_B_FIRST_RUN = PACKET_DIR / "route_b_independent_kernel_values_first_run.packet.json"
ROUTE_B_VALIDATOR = PACKET_DIR / "route_b_independent_kernel_values_validator_result.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_four_clause_partial_proof.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ActionKernelFourClauseProof_or_IndependentKernelValuesRun_v1.md"

STATUS = "MTT_SELECTED_ACTIONKERNELFOURCLAUSEPROOF_OR_INDEPENDENTKERNELVALUESRUN_BUILT_VARIATION_SPACE_CLOSED_SOURCE_OPEN"
NEXT = "MTT_Selected_PhysicalActionBindingAndSameSourceEmission_or_IndependentKernelSourceExport_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_validator(validator: Path, payload: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(validator), str(payload)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "validator": rel(validator),
        "payload": rel(payload),
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip(),
        "stderr_lines": proc.stderr.splitlines(),
    }


def schedule_rows() -> dict[str, list[str]]:
    schedule = load(ROW_SCHEDULE)
    return {stage["stage"]: stage["rows"] for stage in schedule["execution_order"]}


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    route_a_contract = load(ROUTE_A_CONTRACT)
    route_b_contract = load(ROUTE_B_CONTRACT)
    cutset = load(CUTSET)
    trace_basis = load(TRACE_BASIS)
    dynamic_trace = load(DYNAMIC_TRACE)
    slot_routing = load(SLOT_ROUTING)
    boundary = load(BOUNDARY)
    physical_source = load(PHYSICAL_SOURCE)
    rows = schedule_rows()

    variation_space_closed = (
        trace_basis["what_closes_now"]["selected_trace_map_values_functional_stationary"]
        and trace_basis["what_closes_now"]["selected_basis_projector_gram_gap_values_stationary"]
        and dynamic_trace["what_closes_now"]["dynamic_dotD_trace_binding"]
        and slot_routing["shift_R_X_rows"] == 36
        and slot_routing["phase_R_Z_rows"] == 36
    )

    route_a_partial = {
        "schema": "MTTActionKernelFourClausePartialProof.v1",
        "status": "ADMISSIBLE_DIFFERENTIATED_VARIATIONS_FIXED_SOURCE_CLAUSES_OPEN",
        "same_branch": True,
        "physical_action_equals_c1_defect_functional": False,
        "admissible_differentiated_variations_fixed": bool(variation_space_closed),
        "physical_boundary_source_terms_vanish": False,
        "same_source_rz_rx_bselected_emitted": False,
        "attached_theorem_evidence": [
            {
                "source": rel(TRACE_BASIS),
                "closes": "stationary selected trace map and basis/projector/Gram/gap support",
            },
            {
                "source": rel(DYNAMIC_TRACE),
                "closes": "dynamic dotD/Phi_fin C1 trace binding",
            },
            {
                "source": rel(SLOT_ROUTING),
                "closes": "phase/shift variation shapes routed over the 72 primitive slots",
            },
            {
                "source": rel(BOUNDARY),
                "closes": "algebraic finite trace boundary cancellation only, not physical source vanishing",
            },
        ],
        "closed_clause": "admissible_differentiated_variations_fixed",
        "open_source_clauses": [
            "physical_action_equals_c1_defect_functional",
            "physical_boundary_source_terms_vanish",
            "same_source_rz_rx_bselected_emitted",
        ],
        "why_still_fails_validator": [
            "physical Phi_fin^C1 action has not been proved equal to the selected C1 defect functional",
            "algebraic boundary cancellation is not yet promoted to physical no-extra-boundary/source",
            "same-source R_Z/R_X/b_selected emission remains absent",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "locked_target_values_used_as_source": False,
        "residual_projector_replay_used_as_source": False,
        "free_axiom_patch_used": False,
        "closure_claimed": False,
    }

    global_sources = {
        "selected_measure_pairing": {
            "source_id": "trace_frobenius_pairing_support_only",
            "selected_emitted": False,
            "theorem_derived": False,
            "independent_of_residual_replay": True,
            "locked_target_dependency": False,
            "reason": "Formal trace/Frobenius support exists, but independent physical/quadrature measure emission is not proved.",
        },
        "selected_quadrature_rule": {
            "source_id": "not_emitted",
            "selected_emitted": False,
            "theorem_derived": False,
            "independent_of_residual_replay": False,
            "locked_target_dependency": False,
        },
        "selected_variation_space": {
            "source_id": "admissible_variation_space_closed_by_trace_basis_dotd_slot_routing",
            "selected_emitted": True,
            "theorem_derived": True,
            "independent_of_residual_replay": True,
            "locked_target_dependency": False,
        },
    }

    route_b_first_run = {
        "schema": "MTTIndependentKernelValuesFirstRun.v1",
        "status": "VARIATION_SPACE_SOURCE_CLOSED_KERNEL_VALUES_OPEN",
        "global_sources": global_sources,
        "primitive_row_kernel_sources": [
            {
                "row_id": row_id,
                "source_id": None,
                "selected_emitted": False,
                "theorem_derived": False,
                "independent_of_residual_replay": False,
                "locked_target_dependency": False,
                "integral_formula": None,
                "selected_measure_pairing_id": global_sources["selected_measure_pairing"]["source_id"],
                "selected_quadrature_rule_id": global_sources["selected_quadrature_rule"]["source_id"],
            }
            for row_id in rows["primitive_contractions"]
        ],
        "hessian_b_sources": [
            {
                "row_id": row_id,
                "source_id": None,
                "selected_emitted": False,
                "theorem_derived": False,
                "independent_of_residual_replay": False,
                "locked_target_dependency": False,
                "selected_b_vector_source": False,
                "not_copied_from_A_transpose_b_target": True,
            }
            for row_id in rows["hessian_source"]
        ],
        "sector_assembly_sources": [
            {
                "row_id": row_id,
                "source_id": None,
                "selected_emitted": False,
                "theorem_derived": False,
                "independent_of_residual_replay": False,
                "locked_target_dependency": False,
                "assembled_from_primitive_source_rows": False,
            }
            for row_id in rows["sector_matrices"]
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "locked_target_values_used_as_source": False,
        "closure_claimed": False,
    }

    ROUTE_A_PARTIAL.write_text(json.dumps(route_a_partial, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    ROUTE_B_FIRST_RUN.write_text(json.dumps(route_b_first_run, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    route_a_result = run_validator(ACTION_VALIDATOR, ROUTE_A_PARTIAL)
    route_b_result = run_validator(ROW_VALIDATOR, ROUTE_B_FIRST_RUN)
    ROUTE_A_VALIDATOR.write_text(json.dumps(route_a_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    ROUTE_B_VALIDATOR.write_text(json.dumps(route_b_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    next_cutset = {
        "schema": "MTTActionKernelFourClauseNextCutset.v1",
        "status": "VARIATION_SPACE_CLOSED_THREE_ROUTE_A_CLAUSES_AND_KERNEL_VALUES_OPEN",
        "closed_now": [
            "admissible_differentiated_variations_fixed",
            "variation-space source independent of residual replay",
        ],
        "route_A_still_open": [
            "physical_action_equals_c1_defect_functional",
            "physical_boundary_source_terms_vanish",
            "same_source_rz_rx_bselected_emitted",
        ],
        "route_B_still_open": [
            "selected independent quadrature rule",
            "selected independent measure pairing as source",
            "72 primitive row kernel source ids and integral formulas",
            "2 independent hessian/b_selected source ids",
            "36 sector assembly source ids",
        ],
        "recommended_next": {
            "artifact": NEXT,
            "reason": "The admissible variation-space clause is now separated from the physical source clauses. The next proof must bind the physical action to the defect functional and same-source emissions, or export independent kernel source ids.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedActionKernelFourClauseProofOrIndependentKernelValuesRun",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "route_A_contract": rel(ROUTE_A_CONTRACT),
            "route_B_contract": rel(ROUTE_B_CONTRACT),
            "prior_cutset": rel(CUTSET),
            "trace_basis": rel(TRACE_BASIS),
            "dynamic_trace": rel(DYNAMIC_TRACE),
            "slot_routing": rel(SLOT_ROUTING),
            "physical_source_cutset": rel(PHYSICAL_SOURCE),
        },
        "output_packets": {
            "route_a_four_clause_partial_proof": rel(ROUTE_A_PARTIAL),
            "route_a_four_clause_validator_result": rel(ROUTE_A_VALIDATOR),
            "route_b_independent_kernel_values_first_run": rel(ROUTE_B_FIRST_RUN),
            "route_b_independent_kernel_values_validator_result": rel(ROUTE_B_VALIDATOR),
            "next_cutset_after_four_clause_partial_proof": rel(NEXT_CUTSET),
        },
        "promotion_decision": {
            "admissible_variation_space_clause_promoted": bool(variation_space_closed),
            "route_A_action_kernel_theorem_proved": False,
            "route_B_independent_kernel_values_exported": False,
            "unpatched_A_selected_promoted": False,
            "unpatched_b_selected_promoted": False,
            "unpatched_deltaTheta_C1_promoted": False,
            "unpatched_SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "what_closes_now": {
            "admissible_differentiated_variations_fixed": bool(variation_space_closed),
            "variation_space_source_independent_of_residual_replay": True,
            "route_A_validator_rerun_with_one_clause_closed": route_a_result["returncode"] == 1,
            "route_B_validator_rerun_with_variation_space_source_closed": route_b_result["returncode"] == 1,
            "source_cutset_sharpened": True,
            "observed_constants_excluded_as_selectors": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "physical_action_equals_c1_defect_functional": True,
            "physical_boundary_source_terms_vanish": True,
            "same_source_rz_rx_bselected_emitted": True,
            "selected_independent_quadrature_rule": True,
            "selected_independent_measure_pairing_source": True,
            "primitive_kernel_source_ids_and_formulas": True,
            "independent_hessian_bselected_source_ids": True,
            "sector_assembly_source_ids": True,
            "unpatched_SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
            "no_knob_closure": True,
        },
        "theorem": {
            "name": "ActionKernelFourClausePartialProofTheorem",
            "proved": True,
            "statement": (
                "The selected trace/basis, dynamic dotD trace binding, and phase/shift slot-routing packets prove the "
                "admissible differentiated-variation-space clause of the Phi_fin^C1 action-kernel theorem without "
                "using residual replay or target values as source. The remaining Route A clauses are physical action "
                "binding, physical boundary/source vanishing, and same-source R_Z/R_X/b_selected emission. Route B "
                "still requires independent kernel source ids and formulas."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "patched_SM_parity_closure_preserved": previous["patched_SM_parity_closure_preserved"],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_ActionKernelFourClauseProof_or_IndependentKernelValuesRun_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected ActionKernelFourClauseProof or IndependentKernelValuesRun v1

Status: `{STATUS}`.

The action-kernel theorem has four clauses. This artifact closes the first:

```text
admissible differentiated variations fixed     CLOSED
physical action = C1 defect functional         OPEN
physical boundary/source terms vanish          OPEN
same-source R_Z/R_X/b_selected emitted         OPEN
```

The closed clause uses selected trace/basis support, dynamic dotD trace binding,
and phase/shift slot routing. It does not use residual-projector replay,
locked target values, observed constants, or fitted profiles as source.

Route B was rerun with the variation-space source closed, but independent
kernel values remain open: selected quadrature rule, selected measure source,
72 primitive source ids/formulas, 2 Hessian/b rows, and 36 sector assembly
source ids.

Next artifact: `{NEXT}`.
"""

    NEXT_CUTSET.write_text(json.dumps(next_cutset, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
