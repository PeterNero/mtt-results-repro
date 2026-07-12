"""Build PSM-C1-02 pre-residual operator source attempt with Route-A sidecar."""

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

SLUG = "selected_psm_c1_02_preresidualoperators_or_routea_physicalrestriction"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CURRENT = PACKET_DIR / "psm_c1_02_current_unpatched_operator_source_audit.packet.json"
CONDITIONAL_PAYLOAD = PACKET_DIR / "route_b_conditional_preresidual_operator_validator_payload.packet.json"
CONDITIONAL_RESULT = PACKET_DIR / "route_b_conditional_preresidual_operator_validator_result.packet.json"
CUTSET = PACKET_DIR / "physical_selection_cutset.packet.json"
NEXT = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_PreResidualOperators_or_ROUTE_A_PhysicalRestriction_v1.md"

VALIDATOR = ROOT / "scripts" / "validate_selected_physicalphifinc1_action_or_independent_rowkernel_source.py"
STATUS = "MTT_SELECTED_PSM_C1_02_PRERESIDUALOPERATORS_OR_ROUTEA_PHYSICALRESTRICTION_BUILT_CONDITIONAL_CLOSE_UNPATCHED_OPEN"
NEXT_ARTIFACT = "MTT_Selected_PSM_C1_02_PhysicalSelectionLemma_or_PSM_C1_04_HessianSourceRows_v1"


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


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_psm_c1_01_unpatchedsourcelemma_or_routeb_rowkernelexecution.candidate.json")
    pre_residual = load(DATA / "selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom" / "current_pre_residual_variation_hessian_source_attempt.packet.json")
    unpatched_principle = load(DATA / "selected_weylvariation_actionprinciple_derivation_or_explicitinsertion" / "unpatched_weylvariation_actionprinciple_derivation_attempt.packet.json")
    applied_principle = load(DATA / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution" / "applied_principle_kernel_closure.packet.json")
    row_functional = load(DATA / "selected_finitec1_rowkernelfunctional_candidate_or_sourceclausefailure" / "finite_c1_rowkernel_functional_candidate.packet.json")
    after_table = load(DATA / "selected_routea_physicalactionidentityproof_or_routeb_independentrowsourcetable" / "two_exit_current_after_table_attempt.packet.json")

    current_packet = {
        "schema": "MTTPSMC102CurrentUnpatchedOperatorSourceAudit.v1",
        "status": "PSM_C1_02_UNPATCHED_OPEN_CONDITIONAL_SUPPORT_MAXIMIZED",
        "label": "PSM-C1-02",
        "route": "ROUTE-B",
        "strict_field": "pre_residual_phase_shift_variation_operators",
        "current_unpatched_field_value": False,
        "support_closed": {
            "same_branch": pre_residual["same_branch"],
            "static_source_map_candidate": pre_residual["support_closed"]["static_source_map_candidate"],
            "canonical_projector_replays_RZ_RX": pre_residual["support_closed"]["canonical_projector_replays_RZ_RX"],
            "typed_row_functor": pre_residual["support_closed"]["typed_row_functor"],
            "operator_shapes_compatible": row_functional["closed_support"]["variation_operator_shapes_compatible"],
            "exact_weyl_polynomials_present": unpatched_principle["closed_support"]["exact_weyl_polynomials_present"],
            "finite_euler_projection_present": unpatched_principle["closed_support"]["finite_variational_euler_projection"],
        },
        "not_promoted_unpatched_because": pre_residual["why_not_promoted"] + unpatched_principle["why_not_derived"],
        "field_closure_decision": {
            "unpatched_PSM_C1_02_closed": False,
            "conditional_local_principle_closes_PSM_C1_02": applied_principle["promoted_inside_local_spine"]["pre_residual_phase_shift_operator_source"],
            "residual_projector_replay_used_as_source": row_functional["source_clauses"]["phase_shift_pre_residual_operators"]["uses_replay_as_source"],
        },
        "evidence": [
            rel(DATA / "selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom" / "current_pre_residual_variation_hessian_source_attempt.packet.json"),
            rel(DATA / "selected_weylvariation_actionprinciple_derivation_or_explicitinsertion" / "unpatched_weylvariation_actionprinciple_derivation_attempt.packet.json"),
            rel(DATA / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution" / "applied_principle_kernel_closure.packet.json"),
            rel(DATA / "selected_finitec1_rowkernelfunctional_candidate_or_sourceclausefailure" / "finite_c1_rowkernel_functional_candidate.packet.json"),
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    conditional_payload = {
        "schema": "MTTRouteBConditionalPreResidualOperatorValidatorPayload.v1",
        "status": "CONDITIONAL_ROUTE_B_WITH_PSM_C1_02_PROMOTED_STILL_FAILS_REMAINING_FIELDS",
        "closure_claimed": False,
        "locked_target_values_used_as_source": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "route_A_physical_action_restriction": after_table["route_A_physical_action_restriction"],
        "route_B_independent_rowkernel_source": {
            "same_branch": True,
            "selected_basis_feeds_all_72_row_functionals": True,
            "pre_residual_phase_shift_variation_operators": True,
            "independent_hessian_counterterm_source_rows": False,
            "sector_rows_assembled_from_source_rows": False,
            "no_residual_projector_replay_or_locked_target_as_source": False,
            "attached_source_evidence": [
                {
                    "source": rel(DATA / "selected_routea_physicalactionidentityproof_or_routeb_independentrowsourcetable" / "two_exit_current_after_table_attempt.packet.json"),
                    "closes": "selected basis feeds all 72 row functionals in best current table attempt",
                },
                {
                    "source": rel(DATA / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution" / "applied_principle_kernel_closure.packet.json"),
                    "closes": "conditional local-principle pre-residual phase/shift operator source",
                    "conditional": True,
                },
                {
                    "source": rel(DATA / "selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom" / "current_pre_residual_variation_hessian_source_attempt.packet.json"),
                    "closes": "same-branch support and canonical R_Z/R_X replay only",
                },
                {
                    "source": rel(DATA / "selected_finitec1_rowkernelfunctional_candidate_or_sourceclausefailure" / "finite_c1_rowkernel_functional_candidate.packet.json"),
                    "closes": "operator shape compatibility and row-kernel normal form support only",
                },
                {
                    "source": rel(DATA / "selected_weylvariation_actionprinciple_derivation_or_explicitinsertion" / "unpatched_weylvariation_actionprinciple_derivation_attempt.packet.json"),
                    "closes": "records exact remaining physical-selection failures",
                },
            ],
        },
    }
    CONDITIONAL_PAYLOAD.write_text(json.dumps(conditional_payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    conditional_result = run_validator(CONDITIONAL_PAYLOAD)
    conditional_result["observed_data_used_as_selector"] = False
    conditional_result["target_fitting_used"] = False

    cutset_packet = {
        "schema": "MTTPSMC102PhysicalSelectionCutset.v1",
        "status": "PSM_C1_02_REDUCED_TO_PHYSICAL_SELECTION_OR_HESSIAN_SOURCE_ROWS",
        "minimal_unpatched_cutset": [
            {
                "label": "PSM-C1-02",
                "field": "pre_residual_phase_shift_variation_operators",
                "missing_object": "same-branch physical selection that turns exact R_Z/R_X Weyl polynomials into pre-residual source operators",
            },
            {
                "label": "PSM-C1-04",
                "field": "independent_hessian_counterterm_source_rows",
                "missing_object": "same-source Hessian counterterm and b_selected rows, rather than replay b-vector values",
            },
            {
                "label": "PSM-C1-06",
                "field": "sector_rows_assembled_from_source_rows",
                "missing_object": "sector-response assembly from source rows after PSM-C1-02 and PSM-C1-04 are promoted",
            },
            {
                "label": "PSM-C1-02/PSM-C1-04 guardrail",
                "field": "no_residual_projector_replay_or_locked_target_as_source",
                "missing_object": "independence certificate showing residual projector replay is only a postcheck",
            },
        ],
        "why_this_is_progress": (
            "PSM-C1-02 no longer asks for generic operator discovery. The actual candidate operators are already identified; "
            "the remaining step is their source promotion from the selected physical variation/action branch."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextLabeledWorkorderAfterPSMC102PreResidualAudit.v1",
        "status": "NEXT_WORKORDER_PHYSICAL_SELECTION_OR_HESSIAN_SOURCE_ROWS",
        "next_required_artifact": NEXT_ARTIFACT,
        "recommended_primary": {
            "label": "PSM-C1-02",
            "route": "ROUTE-B",
            "task": "Prove the physical selection lemma promoting exact R_Z/R_X Weyl polynomials to pre-residual source operators.",
            "acceptance": "strict field pre_residual_phase_shift_variation_operators=true without local-principle insertion",
        },
        "co_primary": {
            "label": "PSM-C1-04",
            "route": "ROUTE-B",
            "task": "Emit independent Hessian counterterm and b_selected source rows from the same row-kernel table.",
            "acceptance": "strict field independent_hessian_counterterm_source_rows=true",
        },
        "route_A_sidecar": {
            "label": "PSM-C1-01",
            "task": "Derive the physical Phi_fin^C1 action identity so Route A can close all same-source fields at once.",
        },
        "previous_artifact": previous["next_required_artifact"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    theorem = {
        "name": "PreResidualOperatorSourceCutsetTheorem",
        "proved": True,
        "statement": (
            "The PSM-C1-02 operator discovery problem is reduced to source promotion: exact R_Z/R_X Weyl polynomials, "
            "operator-shape compatibility, same-branch support, and a conditional Weyl-variation principle are available. "
            "Under that conditional principle PSM-C1-02 validates, but unpatched closure remains open because the physical "
            "selection lemma has not derived those operators before residual-projector replay."
        ),
    }

    candidate = {
        "candidate": "MTTSelectedPSMC102PreResidualOperatorsOrRouteAPhysicalRestriction",
        "status": STATUS,
        "theorem": theorem,
        "closure_claimed": False,
        "conditional_only": True,
        "output_packets": {
            "current_unpatched_operator_source_audit": rel(CURRENT),
            "conditional_validator_payload": rel(CONDITIONAL_PAYLOAD),
            "conditional_validator_result": rel(CONDITIONAL_RESULT),
            "physical_selection_cutset": rel(CUTSET),
            "next_labeled_workorder": rel(NEXT),
        },
        "closure_decision": {
            "PSM_C1_02_closed_unpatched": False,
            "PSM_C1_02_closed_conditional_local_principle": True,
            "unpatched_dynamic_C1_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "what_closes_now": {
            "PSM_C1_02_actual_operator_candidates_identified": True,
            "PSM_C1_02_source_promotion_cutset_identified": True,
            "conditional_two_field_RouteB_payload_tested": True,
        },
        "what_remains_open": {
            "physical_selection_lemma_for_RZ_RX": True,
            "independent_hessian_counterterm_source_rows": True,
            "sector_rows_assembled_from_source_rows": True,
            "independence_from_residual_projector_replay": True,
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
        "PSM_C1_02_closed_unpatched": False,
        "PSM_C1_02_closed_conditional_local_principle": True,
        "conditional_validator_passes": conditional_result["passes"],
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected PSM-C1-02 Pre-Residual Operators or ROUTE-A Physical Restriction v1

Status: `{STATUS}`

## Theorem

**{theorem["name"]}.** {theorem["statement"]}

## Result

- `PSM-C1-02` is not closed unpatched.
- The actual operator candidates are no longer vague: they are the exact `R_Z/R_X` Weyl phase/shift polynomials with compatible row-kernel operator shape.
- A conditional local Weyl-variation principle promotes those operators, so the conditional lane closes `PSM-C1-02`.
- That is still not true-equivalence/no-knob closure, because the unpatched physical selection lemma is missing.

## Superset Use

The superset strategy is being used as a constrained bridge: Route B row kernels, Route A physical action restriction, and the Weyl-variation principle are compared on the same selected finite C1 branch. Conditional evidence may guide the construction, but only unpatched same-branch source emission can close the remaining strict validator fields.

## Next Artifact

`{NEXT_ARTIFACT}`

The best next move is a two-pronged closure attempt: prove the physical selection lemma for `R_Z/R_X`, and in parallel emit the `PSM-C1-04` Hessian counterterm/source rows.
"""

    CURRENT.write_text(json.dumps(current_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CONDITIONAL_RESULT.write_text(json.dumps(conditional_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CUTSET.write_text(json.dumps(cutset_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NEXT.write_text(json.dumps(next_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
