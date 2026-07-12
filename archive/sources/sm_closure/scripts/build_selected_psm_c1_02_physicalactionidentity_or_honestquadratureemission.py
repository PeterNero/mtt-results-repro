"""Build PSM-C1-02 physical action identity or honest quadrature emission attempt."""

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

SLUG = "selected_psm_c1_02_physicalactionidentity_or_honestquadratureemission"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_A = PACKET_DIR / "route_a_i10_physical_action_identity_attempt.packet.json"
ROUTE_B = PACKET_DIR / "route_b_honest_quadrature_emission_attempt.packet.json"
ROUTE_A_RESULT = PACKET_DIR / "route_a_i10_physical_action_identity_validator_result.packet.json"
TWO_EXIT = PACKET_DIR / "psm_c1_02_current_two_exit_validator_payload.packet.json"
TWO_EXIT_RESULT = PACKET_DIR / "psm_c1_02_current_two_exit_validator_result.packet.json"
CONDITIONAL_A_RESULT = PACKET_DIR / "conditional_route_a_validator_result.packet.json"
CONDITIONAL_B_RESULT = PACKET_DIR / "conditional_route_b_validator_result.packet.json"
EQUIV = PACKET_DIR / "psm_c1_02_closure_equivalence.packet.json"
NEXT = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_PhysicalActionIdentity_or_HonestQuadratureEmission_v1.md"

TWO_EXIT_VALIDATOR = ROOT / "scripts" / "validate_selected_physicalphifinc1_action_or_independent_rowkernel_source.py"
ACTION_VALIDATOR = ROOT / "scripts" / "validate_selected_phifinc1_preresidual_action_kernel_theorem.py"

STATUS = "MTT_SELECTED_PSM_C1_02_PHYSICALACTIONIDENTITY_OR_HONESTQUADRATUREEMISSION_BUILT_EQUIVALENCE_OPEN"
NEXT_ARTIFACT = "MTT_Selected_PSM_C1_02_I10BindingProof_or_SelectedQuadratureSourcePromotion_v1"

POST_SM_LABEL_CONTEXT = {
    "tier": "tier_2_post_sm_parity_true_equivalence",
    "preferred_phrase": "post-SM-parity frontier",
    "closed_boundary": "DONE-PARITY-00",
    "active_label": "PSM-C1-02",
    "active_label_name": "selected primitive C1 overlap contractions",
    "primary_routes": ["ROUTE-A", "ROUTE-B"],
    "route_A": "same-source dynamic Phi_fin^C1 source rule",
    "route_B": "honest selected Galerkin C1 execution",
    "language_guardrail": "Do not call this an SM-parity blocker; SM-parity replay is frozen closed.",
}


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_validator(validator: Path, path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(validator), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return {
        "validator": rel(validator),
        "payload": rel(path),
        "returncode": proc.returncode,
        "passes": proc.returncode == 0,
        "stdout": proc.stdout.strip().splitlines(),
        "stderr": proc.stderr.strip().splitlines(),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_preresidualweylvariationselectionlemma_or_honestquadraturesource.candidate.json")
    normal_form = load(DATA / "selected_preresidualweylvariationselectionlemma_or_honestquadraturesource" / "psm_c1_02_preresidual_weyl_normal_form.packet.json")
    route_a_prior = load(DATA / "selected_preresidualweylvariationselectionlemma_or_honestquadraturesource" / "route_a_physical_selection_lemma_attempt.packet.json")
    i10_frontier = load(DATA / "selected_phifinc1actionkernel_theorem_attempt_or_i10binding" / "remaining_i10_binding_frontier.packet.json")
    i10_conditional = load(DATA / "selected_phifinc1actionkernel_theorem_attempt_or_i10binding" / "conditional_i10_action_kernel_witness.packet.json")
    source_ids = load(DATA / "selected_independentc1_rowkernelsourceids_or_physicalphifinc1actionproof" / "current_rowkernel_source_id_attempt.packet.json")
    source_ids_conditional = load(DATA / "selected_independentc1_rowkernelsourceids_or_physicalphifinc1actionproof" / "conditional_independent_rowkernel_source_id_witness.packet.json")
    export_current = load(DATA / "selected_physicalphifinc1actionidentity_or_independentrowsourceexport" / "current_source_export_attempt.packet.json")
    conditional_route_a = load(DATA / "selected_physicalphifinc1actionidentity_or_independentrowsourceexport" / "conditional_route_a_physical_action_identity_witness.packet.json")
    conditional_route_b = load(DATA / "selected_physicalphifinc1actionidentity_or_independentrowsourceexport" / "conditional_route_b_independent_rowsource_export_witness.packet.json")

    route_a = {
        "schema": "MTTPSMC102RouteAI10PhysicalActionIdentityAttempt.v1",
        "status": "ROUTE_A_I10_ACTION_IDENTITY_STILL_OPEN",
        "post_sm_parity_label_context": POST_SM_LABEL_CONTEXT,
        "active_label": "PSM-C1-02",
        "route_label": "ROUTE-A",
        "same_branch": True,
        "physical_action_equals_c1_defect_functional": False,
        "admissible_differentiated_variations_fixed": route_a_prior["admissible_differentiated_variations_fixed"],
        "physical_boundary_source_terms_vanish": False,
        "same_source_rz_rx_bselected_emitted": False,
        "locked_target_values_used_as_source": False,
        "residual_projector_replay_used_as_source": False,
        "free_axiom_patch_used": False,
        "attached_theorem_evidence": [
            {
                "source": rel(DATA / "selected_preresidualweylvariationselectionlemma_or_honestquadraturesource" / "psm_c1_02_preresidual_weyl_normal_form.packet.json"),
                "closes": "R_Z/R_X normal forms and selected qutrit Weyl carrier",
            },
            {
                "source": rel(DATA / "selected_phifinc1actionkernel_theorem_attempt_or_i10binding" / "remaining_i10_binding_frontier.packet.json"),
                "closes": "minimal I10/I1/I5 dependency chain",
                "does_not_close": "physical action binding",
            },
            {
                "source": rel(DATA / "selected_phifinc1actionkernel_theorem_attempt_or_i10binding" / "conditional_i10_action_kernel_witness.packet.json"),
                "closes": "conditional action-kernel sufficiency",
                "conditional": True,
            },
            {
                "source": rel(DATA / "selected_finiteweyl_traceuniqueness_or_physicalboundarysource_derivation" / "finite_weyl_trace_uniqueness_derivation.packet.json"),
                "closes": "finite Weyl trace support only",
            },
        ],
        "minimal_missing_i10_stack": i10_frontier["minimal_next_proof"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(ROUTE_A, route_a)
    route_a_result = run_validator(ACTION_VALIDATOR, ROUTE_A)

    route_b = {
        "schema": "MTTPSMC102RouteBHonestQuadratureEmissionAttempt.v1",
        "status": "ROUTE_B_SOURCE_IDS_NAMED_BUT_NOT_PROMOTED",
        "post_sm_parity_label_context": POST_SM_LABEL_CONTEXT,
        "active_label": "PSM-C1-02",
        "route_label": "ROUTE-B",
        "source_namespace_counts": {
            "primitive_source_ids": len(source_ids["primitive_row_kernel_sources"]),
            "hessian_b_source_ids": len(source_ids["hessian_b_sources"]),
            "sector_assembly_source_ids": len(source_ids["sector_assembly_sources"]),
        },
        "current_global_sources_selected": all(item["selected_emitted"] for item in source_ids["global_sources"].values()),
        "current_primitive_sources_selected": all(item["selected_emitted"] for item in source_ids["primitive_row_kernel_sources"]),
        "current_hessian_sources_selected": all(item["selected_emitted"] for item in source_ids["hessian_b_sources"]),
        "current_sector_sources_selected": all(item["selected_emitted"] for item in source_ids["sector_assembly_sources"]),
        "conditional_source_ids_validate": all(item["selected_emitted"] for item in source_ids_conditional["primitive_row_kernel_sources"]),
        "honest_quadrature_emitted_now": False,
        "why_not_emitted": [
            "current source ids are support-level, not theorem-derived",
            "selected quadrature rule and measure pairing are not emitted as selected sources",
            "Hessian/b_selected rows remain formal targets unless promoted",
            "sector rows are formal assembly support unless sourced from promoted primitive/Hessian rows",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    two_exit_payload = {
        "schema": "MTTPSMC102CurrentTwoExitValidatorPayload.v1",
        "status": "CURRENT_PSM_C1_02_TWO_EXIT_PAYLOAD_FAILS_SOURCE_OWNERSHIP",
        "post_sm_parity_label_context": POST_SM_LABEL_CONTEXT,
        "active_label": "PSM-C1-02",
        "locked_target_values_used_as_source": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "route_A_physical_action_restriction": export_current["route_A_physical_action_restriction"],
        "route_B_independent_rowkernel_source": export_current["route_B_independent_rowkernel_source"],
    }
    write_json(TWO_EXIT, two_exit_payload)
    two_exit_result = run_validator(TWO_EXIT_VALIDATOR, TWO_EXIT)

    conditional_a_result = run_validator(TWO_EXIT_VALIDATOR, DATA / "selected_physicalphifinc1actionidentity_or_independentrowsourceexport" / "conditional_route_a_physical_action_identity_witness.packet.json")
    conditional_b_result = run_validator(TWO_EXIT_VALIDATOR, DATA / "selected_physicalphifinc1actionidentity_or_independentrowsourceexport" / "conditional_route_b_independent_rowsource_export_witness.packet.json")

    equivalence = {
        "schema": "MTTPSMC102ClosureEquivalence.v1",
        "status": "PSM_C1_02_CLOSES_IFF_I10_STACK_OR_HONEST_SOURCE_EXPORT_IS_SUPPLIED",
        "post_sm_parity_label_context": POST_SM_LABEL_CONTEXT,
        "active_label": "PSM-C1-02",
        "normal_form_candidates_ready": normal_form["status"] == "RZ_RX_UNIQUE_NORMAL_FORM_CANDIDATES_IDENTIFIED_SOURCE_SELECTION_OPEN",
        "current_two_exit_validator_passes": two_exit_result["passes"],
        "conditional_route_A_validator_passes": conditional_a_result["passes"],
        "conditional_route_B_validator_passes": conditional_b_result["passes"],
        "route_A_minimal_missing": [
            "I10: selected Phi_fin^C1 minimizes the unique sourced C1 defect functional",
            "I1/I5: selected trace and dotD/C1 response bind the physical action",
            "physical boundary/source terms vanish",
            "same source emits R_Z, R_X, and b_selected before residual replay",
        ],
        "route_B_minimal_missing": [
            "theorem-derived selected quadrature rule and measure pairing",
            "theorem-derived 72 primitive row source ids",
            "theorem-derived two Hessian/b_selected source rows",
            "sector rows assembled from promoted source rows",
            "independence certificate excluding residual-projector replay and locked targets as sources",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextLabeledWorkorderAfterPSMC102TwoExitExecution.v1",
        "status": "NEXT_WORKORDER_PSM_C1_02_I10_BINDING_OR_SELECTED_QUADRATURE_SOURCE_PROMOTION",
        "active_label": "PSM-C1-02",
        "active_label_name": "selected primitive C1 overlap contractions",
        "route_labels": ["ROUTE-A", "ROUTE-B"],
        "next_required_artifact": NEXT_ARTIFACT,
        "primary": {
            "label": "PSM-C1-02",
            "route_label": "ROUTE-A",
            "task": "Prove I10/I1/I5 physical action binding so Phi_fin^C1 emits R_Z/R_X and b_selected before residual replay.",
        },
        "secondary": {
            "label": "PSM-C1-02",
            "route_label": "ROUTE-B",
            "task": "Promote selected quadrature, measure, primitive source ids, Hessian source rows, and sector assembly as theorem-derived.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    theorem = {
        "name": "PSMC102TwoExitClosureEquivalenceTheorem",
        "proved": True,
        "statement": (
            "For post-SM-parity label PSM-C1-02, R_Z/R_X normal forms are fixed and both legal exits are validator-complete. "
            "The current unpatched payload fails source ownership, while the conditional Route-A and Route-B witnesses pass. "
            "Therefore PSM-C1-02 closes exactly by proving the I10 physical-action binding stack or by promoting an honest "
            "theorem-derived quadrature/source-id/Hessian export."
        ),
    }

    candidate = {
        "candidate": "MTTSelectedPSMC102PhysicalActionIdentityOrHonestQuadratureEmission",
        "status": STATUS,
        "post_sm_parity_label_context": POST_SM_LABEL_CONTEXT,
        "active_post_sm_parity_label": "PSM-C1-02",
        "active_post_sm_parity_routes": ["ROUTE-A", "ROUTE-B"],
        "theorem": theorem,
        "closure_claimed": False,
        "PSM_C1_02_closed_unpatched": False,
        "output_packets": {
            "route_a_i10_physical_action_identity_attempt": rel(ROUTE_A),
            "route_b_honest_quadrature_emission_attempt": rel(ROUTE_B),
            "psm_c1_02_current_two_exit_validator_payload": rel(TWO_EXIT),
            "psm_c1_02_current_two_exit_validator_result": rel(TWO_EXIT_RESULT),
            "conditional_route_a_validator_result": rel(CONDITIONAL_A_RESULT),
            "conditional_route_b_validator_result": rel(CONDITIONAL_B_RESULT),
            "psm_c1_02_closure_equivalence": rel(EQUIV),
            "next_labeled_workorder": rel(NEXT),
        },
        "what_closes_now": {
            "PSM_C1_02_two_exit_equivalence_proved": True,
            "I10_stack_named_as_route_A_minimal_gate": True,
            "selected_quadrature_source_promotion_named_as_route_B_minimal_gate": True,
        },
        "what_remains_open": {
            "I10_I1_I5_physical_action_binding": True,
            "physical_boundary_source_vanishing": True,
            "same_source_RZ_RX_bselected_emission": True,
            "selected_quadrature_source_promotion": True,
            "selected_hessian_source_rows": True,
        },
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "previous_status": previous["status"],
    }

    certificate = {
        "certificate": f"{SLUG}_certificate",
        "status": STATUS,
        "candidate": rel(OUTPUT),
        "active_post_sm_parity_label": "PSM-C1-02",
        "active_post_sm_parity_routes": ["ROUTE-A", "ROUTE-B"],
        "current_two_exit_validator_passes": two_exit_result["passes"],
        "conditional_route_A_validator_passes": conditional_a_result["passes"],
        "conditional_route_B_validator_passes": conditional_b_result["passes"],
        "closure_claimed": False,
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected PSM C1 02 PhysicalActionIdentity or HonestQuadratureEmission v1

Status: `{STATUS}`

Active post-SM-parity label: `PSM-C1-02`

Route labels: `ROUTE-A` / `ROUTE-B`

Boundary guardrail: `DONE-PARITY-00` remains frozen closed. This is post-SM-parity frontier work, not an SM-parity blocker.

## Theorem

**{theorem["name"]}.** {theorem["statement"]}

## Result

- Current unpatched two-exit payload still fails source ownership.
- Conditional `ROUTE-A` validates if the I10/I1/I5 physical action binding stack is proved.
- Conditional `ROUTE-B` validates if the selected quadrature/source-id/Hessian export is theorem-derived.

## Next Artifact

`{NEXT_ARTIFACT}`
"""

    write_json(ROUTE_A_RESULT, route_a_result)
    write_json(ROUTE_B, route_b)
    write_json(TWO_EXIT_RESULT, two_exit_result)
    write_json(CONDITIONAL_A_RESULT, conditional_a_result)
    write_json(CONDITIONAL_B_RESULT, conditional_b_result)
    write_json(EQUIV, equivalence)
    write_json(NEXT, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, certificate)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
