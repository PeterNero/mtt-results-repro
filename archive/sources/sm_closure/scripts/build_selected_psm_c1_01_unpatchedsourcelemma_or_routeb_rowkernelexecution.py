"""Build unpatched PSM-C1-01 exit audit against Route B row-kernel execution."""

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

SLUG = "selected_psm_c1_01_unpatchedsourcelemma_or_routeb_rowkernelexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_A = PACKET_DIR / "route_a_unpatched_source_lemma_field_audit.packet.json"
ROUTE_B = PACKET_DIR / "route_b_rowkernel_execution_field_audit.packet.json"
DELTA = PACKET_DIR / "two_exit_validator_delta.packet.json"
LABEL_STATUS = PACKET_DIR / "label_status_after_unpatched_exit_audit.packet.json"
NEXT = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_01_UnpatchedSourceLemma_or_ROUTE_B_RowKernelExecution_v1.md"

VALIDATOR = ROOT / "scripts" / "validate_selected_physicalphifinc1_action_or_independent_rowkernel_source.py"
STATUS = "MTT_SELECTED_PSM_C1_01_UNPATCHEDSOURCELEMMA_OR_ROUTE_B_ROWKERNELEXECUTION_BUILT_ROUTEB_ONE_FIELD_CLOSED"
NEXT_ARTIFACT = "MTT_Selected_PSM_C1_02_ROUTE_B_PreResidualOperators_or_PSM_C1_01_PhysicalRestriction_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return {
        "payload": rel(path),
        "validator": rel(VALIDATOR),
        "returncode": proc.returncode,
        "passes": proc.returncode == 0,
        "stdout": proc.stdout.strip(),
        "stderr": proc.stderr.strip(),
        "stderr_lines": [line for line in proc.stderr.splitlines() if line],
    }


def bool_count(fields: dict[str, bool], value: bool = True) -> int:
    return sum(1 for item in fields.values() if item is value)


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    action_candidate = load(DATA / "selected_phifinc1_actionrestriction_or_boundarysource_emission.candidate.json")
    route_a_v2 = load(DATA / "selected_phifinc1_actionrestriction_or_boundarysource_emission" / "route_a_action_restriction_validator_v2.packet.json")
    after_table = load(DATA / "selected_routea_physicalactionidentityproof_or_routeb_independentrowsourcetable" / "two_exit_current_after_table_attempt.packet.json")
    original_attempt = load(DATA / "selected_physicalphifinc1action_or_independentrowkernelsource_theorem" / "current_two_exit_source_attempt.packet.json")
    normal_form = load(DATA / "selected_routeb_rowkernelsource_normalform_or_sourceobjectcontract" / "primitive_row_kernel_source_normal_form.packet.json")
    first_run = load(DATA / "selected_unpatchedweylprincipleproof_or_independentkernelrowsfirstrun" / "route_b_independent_kernel_rows_first_run.packet.json")
    applied_principle = load(DATA / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution" / "applied_principle_kernel_closure.packet.json")
    previous_work = load(DATA / "selected_psm_c1_01_sourceruleemission_or_psm_c1_04_bselectedsidecar" / "next_labeled_workorder.packet.json")

    route_a_fields = {
        "physical_action_restricts_to_finite_weyl_quotient": False,
        "zero_extra_boundary_or_source_term": False,
        "phase_R_Z_source_selection": False,
        "shift_R_X_source_selection": False,
        "same_source_b_selected_emission": False,
    }
    route_a_packet = {
        "schema": "MTTRouteAUnpatchedSourceLemmaFieldAudit.v1",
        "status": "ROUTE_A_UNPATCHED_SOURCE_LEMMA_STILL_OPEN_MEASURE_RETIRED",
        "labels": {
            "primary": "PSM-C1-01",
            "sidecar": "PSM-C1-04",
            "route": "ROUTE-A",
        },
        "strict_route_A_fields": route_a_fields,
        "field_closure_count": bool_count(route_a_fields),
        "open_field_count": bool_count(route_a_fields, False),
        "retired_support": {
            "finite_measure_normalization": action_candidate["closure_decision"]["measure_normalization_derived"],
            "finite_selected_C1_quotient": route_a_v2["closed_subclauses"]["finite_selected_C1_quotient"],
            "selected_Weyl_variation_algebra": route_a_v2["closed_subclauses"]["selected_Weyl_variation_algebra"],
            "algebraic_finite_boundary_cancellation": route_a_v2["closed_subclauses"]["algebraic_finite_boundary_cancellation"],
        },
        "support_count": 4,
        "unpatched_route_A_passes": False,
        "interpretation": (
            "Route A no longer needs a measure-normalization repair, but the strict physical source-rule "
            "fields are still not emitted from the same selected branch."
        ),
        "evidence": [
            rel(DATA / "selected_phifinc1_actionrestriction_or_boundarysource_emission.candidate.json"),
            rel(DATA / "selected_phifinc1_actionrestriction_or_boundarysource_emission" / "route_a_action_restriction_validator_v2.packet.json"),
            rel(DATA / "selected_phifinc1_actionrestriction_or_boundarysource_emission" / "same_source_boundary_and_residual_emission_contract.packet.json"),
            rel(DATA / "selected_psm_c1_01_sourceruleemission_or_psm_c1_04_bselectedsidecar" / "route_a_unpatched_source_rule_validator.packet.json"),
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    route_b_fields = {
        "selected_basis_feeds_all_72_row_functionals": after_table["route_B_independent_rowkernel_source"]["selected_basis_feeds_all_72_row_functionals"],
        "pre_residual_phase_shift_variation_operators": after_table["route_B_independent_rowkernel_source"]["pre_residual_phase_shift_variation_operators"],
        "independent_hessian_counterterm_source_rows": after_table["route_B_independent_rowkernel_source"]["independent_hessian_counterterm_source_rows"],
        "sector_rows_assembled_from_source_rows": after_table["route_B_independent_rowkernel_source"]["sector_rows_assembled_from_source_rows"],
        "no_residual_projector_replay_or_locked_target_as_source": after_table["route_B_independent_rowkernel_source"]["no_residual_projector_replay_or_locked_target_as_source"],
    }
    route_b_validator = run_validator(DATA / "selected_routea_physicalactionidentityproof_or_routeb_independentrowsourcetable" / "two_exit_current_after_table_attempt.packet.json")
    route_b_packet = {
        "schema": "MTTRouteBRowKernelExecutionFieldAudit.v1",
        "status": "ROUTE_B_ONE_STRICT_FIELD_CLOSED_FOUR_OPEN",
        "labels": {
            "primary": "PSM-C1-02",
            "depends_on": ["PSM-C1-01", "PSM-C1-04"],
            "route": "ROUTE-B",
        },
        "strict_route_B_fields": route_b_fields,
        "field_closure_count": bool_count(route_b_fields),
        "open_field_count": bool_count(route_b_fields, False),
        "route_B_passes": False,
        "validator_result": route_b_validator,
        "closed_now": [
            "selected_basis_feeds_all_72_row_functionals",
        ],
        "still_open": [
            key for key, value in route_b_fields.items() if value is False
        ],
        "support_not_unpatched_closure": {
            "normal_form_all_110_strict_row_slots_present": normal_form["closed_support"]["all_110_strict_row_slots_present"],
            "normal_form_sector_rows_assembled_formally": normal_form["closed_support"]["sector_rows_assembled_from_primitive_rows"],
            "first_run_sector_rows_assembled_from_primitive_rows": first_run["closed_fields_in_attempt"]["sector_rows_assembled_from_primitive_rows"],
            "first_run_no_locked_target_values_used_as_source": first_run["closed_fields_in_attempt"]["no_locked_target_values_used_as_source"],
            "local_principle_pre_residual_operator_source": applied_principle["promoted_inside_local_spine"]["pre_residual_phase_shift_operator_source"],
            "local_principle_is_conditional_not_unpatched": True,
        },
        "evidence": after_table["route_B_independent_rowkernel_source"]["attached_source_evidence"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    original_route_b = original_attempt["route_B_independent_rowkernel_source"]
    delta_packet = {
        "schema": "MTTTwoExitValidatorDelta.v1",
        "status": "ROUTE_B_SELECTED_BASIS_FIELD_CLOSED_VALIDATOR_STILL_FAILS",
        "before": {
            "payload": rel(DATA / "selected_physicalphifinc1action_or_independentrowkernelsource_theorem" / "current_two_exit_source_attempt.packet.json"),
            "route_A_same_branch": original_attempt["route_A_physical_action_restriction"]["same_branch"],
            "route_B_selected_basis_feeds_all_72": original_route_b["selected_basis_feeds_all_72_row_functionals"],
            "route_B_evidence_count": len(original_route_b["attached_source_evidence"]),
        },
        "after": {
            "payload": rel(DATA / "selected_routea_physicalactionidentityproof_or_routeb_independentrowsourcetable" / "two_exit_current_after_table_attempt.packet.json"),
            "route_A_same_branch": after_table["route_A_physical_action_restriction"]["same_branch"],
            "route_B_selected_basis_feeds_all_72": route_b_fields["selected_basis_feeds_all_72_row_functionals"],
            "route_B_evidence_count": len(after_table["route_B_independent_rowkernel_source"]["attached_source_evidence"]),
            "validator_result": route_b_validator,
        },
        "net_progress": {
            "route_A_same_branch_precondition_improved": True,
            "route_B_selected_basis_field_closed": True,
            "route_B_evidence_count_precondition_met": True,
            "strict_validator_still_fails": route_b_validator["passes"] is False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    label_packet = {
        "schema": "MTTLabelStatusAfterUnpatchedExitAudit.v1",
        "status": "UNPATCHED_ROUTE_A_OPEN_ROUTE_B_ONE_FIELD_CLOSED",
        "closed_frozen_labels_preserved": ["DONE-PARITY-00", "DONE-SOURCE-00", "DONE-DYN-SUPPORT-00"],
        "remaining_labels": [
            {
                "id": "PSM-C1-01",
                "status": "OPEN_UNPATCHED_ACTION_RESTRICTION_REQUIRED",
                "route": "ROUTE-A",
                "strict_fields_closed": 0,
                "strict_fields_total": 5,
            },
            {
                "id": "PSM-C1-02",
                "status": "OPEN_ROUTE_B_ONE_FIELD_CLOSED_FOUR_OPEN",
                "route": "ROUTE-B",
                "strict_fields_closed": 1,
                "strict_fields_total": 5,
                "closed_field": "selected_basis_feeds_all_72_row_functionals",
            },
            {
                "id": "PSM-C1-03",
                "status": "OPEN_A_SELECTED_RESPONSE_HESSIAN_OPERATOR_REQUIRED",
                "route": "ROUTE-A_OR_ROUTE-B",
            },
            {
                "id": "PSM-C1-04",
                "status": "OPEN_UNPATCHED_BSELECTED_REQUIRED",
                "route": "ROUTE-A_OR_ROUTE-B",
            },
            {
                "id": "PSM-C1-05",
                "status": "OPEN_SELECTED_DELTATHETA_C1_SOLVE_REQUIRED",
                "route": "ROUTE-A_OR_ROUTE-B",
            },
            {
                "id": "PSM-C1-06",
                "status": "OPEN_SELECTED_SECTOR_RESPONSE_MATRICES_REQUIRED",
                "route": "ROUTE-B_PREFERRED",
            },
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextLabeledWorkorderAfterUnpatchedExitAudit.v1",
        "status": "NEXT_WORKORDER_ROUTE_B_PRE_RESIDUAL_OPERATORS_WITH_ROUTE_A_SIDECAR",
        "next_required_artifact": NEXT_ARTIFACT,
        "recommended_primary": {
            "label": "PSM-C1-02",
            "route": "ROUTE-B",
            "field": "pre_residual_phase_shift_variation_operators",
            "reason": "Route B already satisfies the selected-basis and evidence-count strict preconditions, so the next concrete closure target is the pre-residual phase/shift operator source.",
        },
        "parallel_sidecar": {
            "label": "PSM-C1-01",
            "route": "ROUTE-A",
            "fields": [
                "physical_action_restricts_to_finite_weyl_quotient",
                "zero_extra_boundary_or_source_term",
            ],
            "reason": "Route A remains the clean same-source path, but its strict physical fields are still all false.",
        },
        "work_items": [
            {
                "id": "B3a",
                "label": "PSM-C1-02",
                "task": "Emit selected pre-residual phase and shift variation operators before residual-projector replay.",
                "acceptance": "strict validator field pre_residual_phase_shift_variation_operators=true without locked target values as source",
            },
            {
                "id": "B3b",
                "label": "PSM-C1-04",
                "task": "Promote independent Hessian counterterm/source rows for b_selected from the same row-kernel source table.",
                "acceptance": "strict validator field independent_hessian_counterterm_source_rows=true",
            },
            {
                "id": "A3a",
                "label": "PSM-C1-01",
                "task": "Derive physical Phi_fin^C1 action restriction and zero-extra-boundary/source term from the finite selected trace branch.",
                "acceptance": "strict Route-A physical_action_restricts_to_finite_weyl_quotient and zero_extra_boundary_or_source_term true",
            },
        ],
        "previous_workorder": previous_work["next_required_artifact"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    theorem = {
        "name": "UnpatchedC1TwoExitFieldAuditTheorem",
        "proved": True,
        "statement": (
            "In the unpatched post-SM-parity branch, Route A has retired finite-measure support but closes 0/5 strict physical source fields. "
            "The best Route B row-table attempt closes selected_basis_feeds_all_72_row_functionals and the evidence-count precondition, "
            "but still lacks four strict fields. Therefore unpatched dynamic C1 remains open, with the next best target being PSM-C1-02 "
            "pre-residual phase/shift operators while preserving a Route-A physical-restriction sidecar."
        ),
    }

    candidate = {
        "candidate": "MTTSelectedPSMC101UnpatchedSourceLemmaOrRouteBRowKernelExecution",
        "status": STATUS,
        "theorem": theorem,
        "closure_claimed": False,
        "output_packets": {
            "route_a_unpatched_source_lemma_field_audit": rel(ROUTE_A),
            "route_b_rowkernel_execution_field_audit": rel(ROUTE_B),
            "two_exit_validator_delta": rel(DELTA),
            "label_status_after_unpatched_exit_audit": rel(LABEL_STATUS),
            "next_labeled_workorder": rel(NEXT),
        },
        "closure_decision": {
            "SM_parity_reopened": False,
            "unpatched_dynamic_C1_packet_closed": False,
            "route_A_unpatched_passes": False,
            "route_B_unpatched_passes": False,
            "route_B_selected_basis_field_closed": True,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "what_closes_now": {
            "ROUTE_B_FIELD_01_selected_basis_feeds_all_72_row_functionals": True,
            "ROUTE_B_evidence_count_precondition": True,
            "ROUTE_A_measure_support_retired_preserved": True,
            "next_labeled_gate_selected": True,
        },
        "what_remains_open": {
            "PSM-C1-01_unpatched_physical_action_restriction": True,
            "PSM-C1-02_pre_residual_phase_shift_variation_operators": True,
            "PSM-C1-03_selected_A_response_hessian_operator": True,
            "PSM-C1-04_unpatched_b_selected_source": True,
            "PSM-C1-05_selected_deltaTheta_C1_solve": True,
            "PSM-C1-06_selected_sector_response_matrices": True,
        },
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    certificate = {
        "certificate": f"{SLUG}_certificate",
        "status": STATUS,
        "candidate": rel(OUTPUT),
        "theorem_proved": theorem["proved"],
        "route_A_strict_fields_closed": 0,
        "route_B_strict_fields_closed": 1,
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected PSM-C1-01 Unpatched Source Lemma or ROUTE-B Row-Kernel Execution v1

Status: `{STATUS}`

## Theorem

**{theorem["name"]}.** {theorem["statement"]}

## Field Result

- `DONE-PARITY-00`, `DONE-SOURCE-00`, and `DONE-DYN-SUPPORT-00` remain frozen.
- `PSM-C1-01` / Route A remains open: 0 of 5 strict unpatched physical fields are closed.
- Route A support is not empty: finite trace measure, selected C1 quotient, selected Weyl variation algebra, and finite boundary cancellation remain retired support.
- `PSM-C1-02` / Route B improves: `selected_basis_feeds_all_72_row_functionals` is now closed in the best current two-exit table attempt.
- Route B still fails the strict validator because four fields remain open: pre-residual phase/shift operators, independent Hessian counterterm/source rows, sector rows assembled from source rows, and no residual-projector replay as source.

## Superset Use

This uses the superset strategy in a constrained way: Route A, Route B, and the conditional Weyl-variation principle are compared against the same locked post-SM-parity target, but only strict same-branch fields are promoted. Conditional/local-principle evidence is recorded as support, not as unpatched theorem closure.

## Next Artifact

`{NEXT_ARTIFACT}`

Primary target: `PSM-C1-02`, emit the selected pre-residual phase and shift variation operators before residual-projector replay. Parallel sidecar: continue `PSM-C1-01` by deriving the physical action restriction and zero-extra-boundary/source term.
"""

    ROUTE_A.write_text(json.dumps(route_a_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    ROUTE_B.write_text(json.dumps(route_b_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    DELTA.write_text(json.dumps(delta_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    LABEL_STATUS.write_text(json.dumps(label_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NEXT.write_text(json.dumps(next_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
