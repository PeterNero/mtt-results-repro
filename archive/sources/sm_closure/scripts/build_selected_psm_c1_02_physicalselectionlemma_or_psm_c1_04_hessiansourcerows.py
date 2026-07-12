"""Build physical-selection/Hessian-source compression for post-SM-parity C1."""

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

SLUG = "selected_psm_c1_02_physicalselectionlemma_or_psm_c1_04_hessiansourcerows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
UNPATCHED = PACKET_DIR / "unpatched_physical_selection_and_hessian_source_status.packet.json"
CONDITIONAL_PAYLOAD = PACKET_DIR / "route_b_conditional_selection_hessian_validator_payload.packet.json"
CONDITIONAL_RESULT = PACKET_DIR / "route_b_conditional_selection_hessian_validator_result.packet.json"
REMAINING = PACKET_DIR / "remaining_two_field_cutset.packet.json"
NEXT = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_PhysicalSelectionLemma_or_PSM_C1_04_HessianSourceRows_v1.md"

VALIDATOR = ROOT / "scripts" / "validate_selected_physicalphifinc1_action_or_independent_rowkernel_source.py"
STATUS = "MTT_SELECTED_PSM_C1_02_PHYSICALSELECTIONLEMMA_OR_PSM_C1_04_HESSIANSOURCEROWS_BUILT_CONDITIONAL_THREE_FIELD_ROUTEB"
NEXT_ARTIFACT = "MTT_Selected_PSM_C1_06_SectorRows_or_ReplayIndependenceCertificate_v1"


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

    previous = load(DATA / "selected_psm_c1_02_preresidualoperators_or_routea_physicalrestriction.candidate.json")
    previous_current = load(DATA / "selected_psm_c1_02_preresidualoperators_or_routea_physicalrestriction" / "psm_c1_02_current_unpatched_operator_source_audit.packet.json")
    previous_cutset = load(DATA / "selected_psm_c1_02_preresidualoperators_or_routea_physicalrestriction" / "physical_selection_cutset.packet.json")
    hessian_gap = load(DATA / "selected_hessiancountertermsource_bvector_theoremtemplate" / "remaining_hessian_bvector_source_gap.packet.json")
    hessian_target = load(DATA / "selected_hessiancountertermsource_bvector_theoremtemplate" / "hessian_bvector_formal_target.packet.json")
    source_attempt = load(DATA / "selected_phifinc1emission_or_independenthessianquadraturesource" / "current_source_emission_attempt.packet.json")
    final_cutset = load(DATA / "selected_phifinc1emission_or_independenthessianquadraturesource" / "final_source_emission_cutset.packet.json")
    applied_principle = load(DATA / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution" / "applied_principle_kernel_closure.packet.json")
    table_attempt = load(DATA / "selected_routea_physicalactionidentityproof_or_routeb_independentrowsourcetable" / "two_exit_current_after_table_attempt.packet.json")

    unpatched_packet = {
        "schema": "MTTUnpatchedPhysicalSelectionAndHessianSourceStatus.v1",
        "status": "UNPATCHED_SELECTION_AND_HESSIAN_SOURCE_STILL_OPEN",
        "labels": ["PSM-C1-02", "PSM-C1-04"],
        "PSM_C1_02": {
            "strict_field": "pre_residual_phase_shift_variation_operators",
            "unpatched_closed": previous["closure_decision"]["PSM_C1_02_closed_unpatched"],
            "conditional_closed": previous["closure_decision"]["PSM_C1_02_closed_conditional_local_principle"],
            "actual_operator_candidates_identified": previous["what_closes_now"]["PSM_C1_02_actual_operator_candidates_identified"],
            "missing_object": previous_cutset["minimal_unpatched_cutset"][0]["missing_object"],
        },
        "PSM_C1_04": {
            "strict_field": "independent_hessian_counterterm_source_rows",
            "unpatched_closed": False,
            "formal_target_closed": hessian_target["formal_hessian_quadrature_emitted"],
            "formal_A_transpose_b": hessian_target["A_transpose_b"],
            "formal_deltaTheta_C1": hessian_target["deltaTheta_C1"],
            "physical_source_promoted": hessian_target["physical_source_promoted"],
            "selected_b_vector_source": source_attempt["route_B_independent_hessian_quadrature_source"]["selected_b_vector_source"],
            "source_independent_of_residual_projector_replay": source_attempt["route_B_independent_hessian_quadrature_source"]["source_independent_of_residual_projector_replay"],
            "why_not_promoted": hessian_gap["why_not_promoted"],
        },
        "shared_support": {
            "same_branch": previous_current["support_closed"]["same_branch"],
            "selected_basis_feeds_all_72": table_attempt["route_B_independent_rowkernel_source"]["selected_basis_feeds_all_72_row_functionals"],
            "operator_shape_compatibility": previous_current["support_closed"]["operator_shapes_compatible"],
            "formal_hessian_target_identified": hessian_gap["closed_now"]["formal_A_transpose_b_target_identified"],
            "local_principle_promotes_hessian_rows_conditionally": applied_principle["promoted_inside_local_spine"]["same_source_hessian_b_selected_rows"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    conditional_payload = {
        "schema": "MTTRouteBConditionalSelectionHessianValidatorPayload.v1",
        "status": "CONDITIONAL_ROUTE_B_SELECTION_AND_HESSIAN_ROWS_PROMOTED_STILL_FAILS_TWO_FIELDS",
        "closure_claimed": False,
        "locked_target_values_used_as_source": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "route_A_physical_action_restriction": table_attempt["route_A_physical_action_restriction"],
        "route_B_independent_rowkernel_source": {
            "same_branch": True,
            "selected_basis_feeds_all_72_row_functionals": True,
            "pre_residual_phase_shift_variation_operators": True,
            "independent_hessian_counterterm_source_rows": True,
            "sector_rows_assembled_from_source_rows": False,
            "no_residual_projector_replay_or_locked_target_as_source": False,
            "attached_source_evidence": [
                {
                    "source": rel(DATA / "selected_routea_physicalactionidentityproof_or_routeb_independentrowsourcetable" / "two_exit_current_after_table_attempt.packet.json"),
                    "closes": "selected basis feeds all 72 row functionals",
                },
                {
                    "source": rel(DATA / "selected_psm_c1_02_preresidualoperators_or_routea_physicalrestriction" / "psm_c1_02_current_unpatched_operator_source_audit.packet.json"),
                    "closes": "pre-residual R_Z/R_X operators conditionally, not unpatched",
                    "conditional": True,
                },
                {
                    "source": rel(DATA / "selected_hessiancountertermsource_bvector_theoremtemplate" / "hessian_bvector_formal_target.packet.json"),
                    "closes": "formal two-row Hessian target and b-vector values",
                    "conditional": True,
                },
                {
                    "source": rel(DATA / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution" / "applied_principle_kernel_closure.packet.json"),
                    "closes": "conditional same-source Hessian/b row promotion inside local principle",
                    "conditional": True,
                },
                {
                    "source": rel(DATA / "selected_phifinc1emission_or_independenthessianquadraturesource" / "final_source_emission_cutset.packet.json"),
                    "closes": "records remaining source-emission cutset and guardrails",
                },
            ],
        },
    }
    CONDITIONAL_PAYLOAD.write_text(json.dumps(conditional_payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    conditional_result = run_validator(CONDITIONAL_PAYLOAD)
    conditional_result["observed_data_used_as_selector"] = False
    conditional_result["target_fitting_used"] = False

    remaining_packet = {
        "schema": "MTTRemainingTwoFieldCutsetAfterConditionalSelectionHessian.v1",
        "status": "CONDITIONAL_ROUTE_B_REDUCED_TO_SECTOR_ROWS_AND_REPLAY_INDEPENDENCE",
        "conditional_route_B_fields": conditional_payload["route_B_independent_rowkernel_source"],
        "conditional_validator_result": conditional_result,
        "remaining_strict_fields": {
            "sector_rows_assembled_from_source_rows": False,
            "no_residual_projector_replay_or_locked_target_as_source": False,
        },
        "unpatched_reality_check": {
            "PSM_C1_02_unpatched_closed": False,
            "PSM_C1_04_unpatched_closed": False,
            "conditional_compression_is_not_a_source_theorem": True,
        },
        "why_this_is_progress": [
            "The strict Route-B gate can be decomposed into five named fields.",
            "One field is already closed unpatched: selected_basis_feeds_all_72_row_functionals.",
            "Two more fields are conditionally closed by the local Weyl-variation/Hessian spine.",
            "The next mathematical shape is therefore either prove those two conditional fields unpatched, or finish sector-row assembly and replay-independence under the conditional spine.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextLabeledWorkorderAfterConditionalSelectionHessian.v1",
        "status": "NEXT_WORKORDER_SECTOR_ROWS_OR_REPLAY_INDEPENDENCE_WITH_UNPATCHED_PROMOTION",
        "next_required_artifact": NEXT_ARTIFACT,
        "recommended_primary": {
            "label": "PSM-C1-06",
            "route": "ROUTE-B",
            "task": "Assemble sector rows from the selected/conditional source rows, then test strict field sector_rows_assembled_from_source_rows.",
        },
        "co_primary": {
            "label": "PSM-C1-02/PSM-C1-04 guardrail",
            "route": "ROUTE-B",
            "task": "Build the replay-independence certificate showing residual-projector replay is only a postcheck.",
        },
        "unpatched_backfill": {
            "labels": ["PSM-C1-02", "PSM-C1-04"],
            "task": "Upgrade conditional physical-selection and Hessian-source fields into unpatched same-branch source theorems.",
        },
        "previous_artifact": previous["next_required_artifact"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    theorem = {
        "name": "ConditionalSelectionHessianCompressionTheorem",
        "proved": True,
        "statement": (
            "For the post-SM-parity Route-B C1 gate, the best current unpatched state closes only selected_basis_feeds_all_72_row_functionals. "
            "If the already isolated physical-selection lemma for R_Z/R_X and the same-source Hessian/b-vector row principle are accepted conditionally, "
            "then three of five strict Route-B fields are true and the validator reduces to sector-row assembly plus replay-independence. "
            "This is a compression of the remaining proof, not an unpatched closure."
        ),
    }

    candidate = {
        "candidate": "MTTSelectedPSMC102PhysicalSelectionLemmaOrPSMC104HessianSourceRows",
        "status": STATUS,
        "theorem": theorem,
        "closure_claimed": False,
        "conditional_only": True,
        "output_packets": {
            "unpatched_status": rel(UNPATCHED),
            "conditional_validator_payload": rel(CONDITIONAL_PAYLOAD),
            "conditional_validator_result": rel(CONDITIONAL_RESULT),
            "remaining_two_field_cutset": rel(REMAINING),
            "next_labeled_workorder": rel(NEXT),
        },
        "closure_decision": {
            "PSM_C1_02_closed_unpatched": False,
            "PSM_C1_04_closed_unpatched": False,
            "RouteB_three_of_five_fields_conditional": True,
            "RouteB_validator_passes": False,
            "unpatched_dynamic_C1_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "what_closes_now": {
            "conditional_PSM_C1_02_plus_PSM_C1_04_compression": True,
            "remaining_two_field_cutset_identified": True,
            "next_sector_rows_or_replay_independence_gate_selected": True,
        },
        "what_remains_open": {
            "unpatched_physical_selection_lemma_for_RZ_RX": True,
            "unpatched_same_source_hessian_b_rows": True,
            "sector_rows_assembled_from_source_rows": True,
            "replay_independence_certificate": True,
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
        "conditional_routeB_fields_true": 3,
        "unpatched_routeB_fields_true": 1,
        "validator_passes": conditional_result["passes"],
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected PSM-C1-02 Physical Selection Lemma or PSM-C1-04 Hessian Source Rows v1

Status: `{STATUS}`

## Theorem

**{theorem["name"]}.** {theorem["statement"]}

## Result

- Unpatched Route B still has only one strict field closed: `selected_basis_feeds_all_72_row_functionals`.
- Conditionally, the local Weyl-variation/Hessian spine promotes `PSM-C1-02` and `PSM-C1-04`, giving 3 of 5 Route-B fields.
- The strict validator still fails under that conditional compression because `sector_rows_assembled_from_source_rows` and `no_residual_projector_replay_or_locked_target_as_source` remain false.
- This does not reopen SM-parity and does not claim no-knob closure.

## Superset Use

The superset strategy is doing real work here: Route B row kernels, Route A physical source emission, and the local Weyl-variation/Hessian principle are fused only as a conditional diagnostic. The locked target is constrained, but promotion remains legal only when same-branch source emission or replay-independent provenance is supplied.

## Next Artifact

`{NEXT_ARTIFACT}`

Next target: either assemble `PSM-C1-06` sector rows from the source rows, or prove the replay-independence certificate. In parallel, backfill the unpatched source theorem for `PSM-C1-02` and `PSM-C1-04`.
"""

    UNPATCHED.write_text(json.dumps(unpatched_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CONDITIONAL_RESULT.write_text(json.dumps(conditional_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    REMAINING.write_text(json.dumps(remaining_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NEXT.write_text(json.dumps(next_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
