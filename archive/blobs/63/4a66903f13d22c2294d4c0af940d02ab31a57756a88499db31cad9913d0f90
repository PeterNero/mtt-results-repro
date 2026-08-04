"""Build PSM-C1-02 pre-residual Weyl selection lemma or honest quadrature source gate."""

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

SLUG = "selected_preresidualweylvariationselectionlemma_or_honestquadraturesource"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
NORMAL_FORM = PACKET_DIR / "psm_c1_02_preresidual_weyl_normal_form.packet.json"
ROUTE_A = PACKET_DIR / "route_a_physical_selection_lemma_attempt.packet.json"
ROUTE_A_RESULT = PACKET_DIR / "route_a_physical_selection_lemma_validator_result.packet.json"
ROUTE_B = PACKET_DIR / "route_b_honest_quadrature_source_contract.packet.json"
EXIT = PACKET_DIR / "psm_c1_02_two_route_exit_matrix.packet.json"
NEXT = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PreResidualWeylVariationSelectionLemma_or_HonestQuadratureSource_v1.md"

ACTION_VALIDATOR = ROOT / "scripts" / "validate_selected_phifinc1_preresidual_action_kernel_theorem.py"
STATUS = "MTT_SELECTED_PRERESIDUALWEYLVARIATIONSELECTIONLEMMA_OR_HONESTQUADRATURESOURCE_BUILT_NORMAL_FORM_SELECTION_OPEN"
NEXT_ARTIFACT = "MTT_Selected_PSM_C1_02_PhysicalActionIdentity_or_HonestQuadratureEmission_v1"

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


def run_action_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(ACTION_VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return {
        "validator": rel(ACTION_VALIDATOR),
        "payload": rel(path),
        "returncode": proc.returncode,
        "passes": proc.returncode == 0,
        "stdout": proc.stdout.strip(),
        "stderr": proc.stderr.strip(),
        "stderr_lines": [line for line in proc.stderr.splitlines() if line],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_primitiverows_replayindependencelemma_or_sourceidentitybackfill.candidate.json")
    next_work = load(DATA / "selected_primitiverows_replayindependencelemma_or_sourceidentitybackfill" / "next_labeled_workorder.packet.json")
    psm_c102 = load(DATA / "selected_psm_c1_02_preresidualoperators_or_routea_physicalrestriction.candidate.json")
    unpatched_audit = load(DATA / "selected_psm_c1_02_preresidualoperators_or_routea_physicalrestriction" / "psm_c1_02_current_unpatched_operator_source_audit.packet.json")
    residual = load(DATA / "selected_residual_weylpolynomial_source_theorem_attempt" / "residual_weyl_polynomial_decomposition.packet.json")
    derivation = load(DATA / "selected_weylvariation_actionprinciple_derivation_or_explicitinsertion" / "unpatched_weylvariation_actionprinciple_derivation_attempt.packet.json")
    local_apply = load(DATA / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution.candidate.json")
    unpatched_exit = load(DATA / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution" / "unpatched_or_independent_kernel_execution_exit.packet.json")
    counter = load(DATA / "selected_minimalfinitec1sourcepromotionlemma_proof_or_countermodel" / "minimal_lemma_obligation_status.packet.json")

    normal_form = {
        "schema": "MTTPSMC102PreResidualWeylNormalForm.v1",
        "status": "RZ_RX_UNIQUE_NORMAL_FORM_CANDIDATES_IDENTIFIED_SOURCE_SELECTION_OPEN",
        "post_sm_parity_label_context": POST_SM_LABEL_CONTEXT,
        "active_label": "PSM-C1-02",
        "route_labels": ["ROUTE-A", "ROUTE-B"],
        "basis": residual["basis"],
        "orthogonality": residual["orthogonality"],
        "source_level_weyl_carrier_selected": residual["source_level_weyl_carrier_selected"],
        "static_source_selector_selected": residual["static_source_selector_selected"],
        "exact_polynomial_form": residual["exact_polynomial_form"],
        "normal_form_checks": {
            "R_Z_coefficient_count": residual["decompositions"]["R_Z"]["coefficient_count"],
            "R_X_coefficient_count": residual["decompositions"]["R_X"]["coefficient_count"],
            "R_Z_reconstruction_error_norm_sq": residual["decompositions"]["R_Z"]["reconstruction_error_norm_sq"],
            "R_X_reconstruction_error_norm_sq": residual["decompositions"]["R_X"]["reconstruction_error_norm_sq"],
            "R_Z_norm_sq": residual["decompositions"]["R_Z"]["norm_sq"],
            "R_X_norm_sq": residual["decompositions"]["R_X"]["norm_sq"],
        },
        "what_this_proves": [
            "R_Z and R_X are the unique exact low-degree qutrit Weyl-polynomial candidates currently identified by the selected carrier.",
            "The primitive values have no remaining finite-matrix discovery problem.",
            "This is a source-ordering normal form, not a physical Phi_fin^C1 source-selection theorem.",
        ],
        "what_this_does_not_prove": [
            "physical_action_equals_c1_defect_functional",
            "physical_boundary_source_terms_vanish",
            "same_source_rz_rx_bselected_emitted",
            "residual projector replay is postcheck-only for the physical source",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    route_a = {
        "schema": "MTTPSMC102RouteAPhysicalSelectionLemmaAttempt.v1",
        "status": "ROUTE_A_NORMAL_FORM_READY_PHYSICAL_ACTION_IDENTITY_OPEN",
        "post_sm_parity_label_context": POST_SM_LABEL_CONTEXT,
        "active_label": "PSM-C1-02",
        "route_label": "ROUTE-A",
        "same_branch": True,
        "physical_action_equals_c1_defect_functional": False,
        "admissible_differentiated_variations_fixed": derivation["closed_support"]["conditional_PhiFinC1_application"],
        "physical_boundary_source_terms_vanish": False,
        "same_source_rz_rx_bselected_emitted": False,
        "locked_target_values_used_as_source": False,
        "residual_projector_replay_used_as_source": False,
        "free_axiom_patch_used": False,
        "attached_theorem_evidence": [
            {
                "source": rel(NORMAL_FORM),
                "closes": "exact R_Z/R_X normal form and no matrix discovery gap",
            },
            {
                "source": rel(DATA / "selected_weylvariation_actionprinciple_derivation_or_explicitinsertion" / "unpatched_weylvariation_actionprinciple_derivation_attempt.packet.json"),
                "closes": "maximal unpatched support inventory",
                "does_not_close": "physical action identity and boundary/source vanishing",
            },
            {
                "source": rel(DATA / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution.candidate.json"),
                "closes": "local premise conditional closure only",
                "conditional": True,
            },
            {
                "source": rel(DATA / "selected_minimalfinitec1sourcepromotionlemma_proof_or_countermodel" / "minimal_lemma_obligation_status.packet.json"),
                "closes": "countermodel to closed-support-only promotion",
            },
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(ROUTE_A, route_a)
    route_a_result = run_action_validator(ROUTE_A)

    route_b = {
        "schema": "MTTPSMC102RouteBHonestQuadratureSourceContract.v1",
        "status": "ROUTE_B_HONEST_QUADRATURE_CONTRACT_READY_EXECUTION_NOT_SUPPLIED",
        "post_sm_parity_label_context": POST_SM_LABEL_CONTEXT,
        "active_label": "PSM-C1-02",
        "route_label": "ROUTE-B",
        "honest_quadrature_source_emitted_now": False,
        "independent_kernel_execution_supplied": unpatched_exit["independent_kernel_execution_supplied"],
        "must_emit": [
            "72 primitive row values from a selected quadrature/export source independent of residual-projector replay",
            "exactness/error certificates from that source",
            "source ids and quadrature rule ids not inherited from R_Z/R_X replay",
            "a validator payload where residual-projector replay is explicitly postcheck-only",
        ],
        "rejected_as_honest_quadrature": [
            "copying exact R_Z/R_X residual Weyl-polynomial rows",
            "copying formal 110-row replay tables",
            "using the hypothetical source-ordering validator payload as proof",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    exit_matrix = {
        "schema": "MTTPSMC102TwoRouteExitMatrix.v1",
        "status": "PSM_C1_02_REDUCED_TO_PHYSICAL_ACTION_IDENTITY_OR_HONEST_QUADRATURE_EMISSION",
        "post_sm_parity_label_context": POST_SM_LABEL_CONTEXT,
        "active_label": "PSM-C1-02",
        "route_A": {
            "route_label": "ROUTE-A",
            "normal_form_candidates_ready": True,
            "validator_passes": route_a_result["passes"],
            "missing_strict_fields": route_a_result["stderr_lines"],
            "next_missing_object": "physical Phi_fin^C1 action identity plus boundary/source vanishing",
        },
        "route_B": {
            "route_label": "ROUTE-B",
            "contract_ready": True,
            "honest_quadrature_source_emitted_now": False,
            "next_missing_object": "independent selected quadrature/export source for 72 primitive rows",
        },
        "countermodel_guardrail": {
            "closed_support_only_is_insufficient": counter["full_lemma_proved"] is False,
            "countermodel_source": counter["countermodel_to_closed_support_only"],
            "blocked_promotion": "Do not promote exact Weyl polynomials to physical source selection without the action identity or independent execution.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextLabeledWorkorderAfterPSMC102NormalForm.v1",
        "status": "NEXT_WORKORDER_PSM_C1_02_PHYSICAL_ACTION_IDENTITY_OR_HONEST_QUADRATURE_EMISSION",
        "active_label": "PSM-C1-02",
        "active_label_name": "selected primitive C1 overlap contractions",
        "route_labels": ["ROUTE-A", "ROUTE-B"],
        "next_required_artifact": NEXT_ARTIFACT,
        "primary": {
            "label": "PSM-C1-02",
            "route_label": "ROUTE-A",
            "task": "Prove physical Phi_fin^C1 action identity and boundary/source vanishing that select R_Z/R_X before residual replay.",
        },
        "secondary": {
            "label": "PSM-C1-02",
            "route_label": "ROUTE-B",
            "task": "Emit honest selected quadrature/export rows for all 72 primitive contractions.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    theorem = {
        "name": "PSMC102PreResidualWeylNormalFormAndExitTheorem",
        "proved": True,
        "statement": (
            "For post-SM-parity label PSM-C1-02, the exact qutrit Weyl normal forms for R_Z and R_X "
            "remove the operator-discovery problem. The remaining unpatched work is source selection: "
            "either prove the physical Phi_fin^C1 action identity and boundary/source vanishing that select "
            "those operators before residual replay, or emit an honest independent quadrature source."
        ),
    }

    candidate = {
        "candidate": "MTTSelectedPreResidualWeylVariationSelectionLemmaOrHonestQuadratureSource",
        "status": STATUS,
        "post_sm_parity_label_context": POST_SM_LABEL_CONTEXT,
        "active_post_sm_parity_label": "PSM-C1-02",
        "active_post_sm_parity_routes": ["ROUTE-A", "ROUTE-B"],
        "theorem": theorem,
        "closure_claimed": False,
        "PSM_C1_02_closed_unpatched": False,
        "normal_form_candidates_identified": True,
        "route_A_validator_passes": route_a_result["passes"],
        "route_B_honest_quadrature_emitted": False,
        "output_packets": {
            "psm_c1_02_preresidual_weyl_normal_form": rel(NORMAL_FORM),
            "route_a_physical_selection_lemma_attempt": rel(ROUTE_A),
            "route_a_physical_selection_lemma_validator_result": rel(ROUTE_A_RESULT),
            "route_b_honest_quadrature_source_contract": rel(ROUTE_B),
            "psm_c1_02_two_route_exit_matrix": rel(EXIT),
            "next_labeled_workorder": rel(NEXT),
        },
        "inputs": {
            "previous_workorder": rel(DATA / "selected_primitiverows_replayindependencelemma_or_sourceidentitybackfill" / "next_labeled_workorder.packet.json"),
            "psm_c1_02_prior": rel(DATA / "selected_psm_c1_02_preresidualoperators_or_routea_physicalrestriction.candidate.json"),
            "residual_weyl_decomposition": rel(DATA / "selected_residual_weylpolynomial_source_theorem_attempt" / "residual_weyl_polynomial_decomposition.packet.json"),
            "weylvariation_unpatched_attempt": rel(DATA / "selected_weylvariation_actionprinciple_derivation_or_explicitinsertion" / "unpatched_weylvariation_actionprinciple_derivation_attempt.packet.json"),
        },
        "what_closes_now": {
            "PSM_C1_02_RZ_RX_normal_form_locked": True,
            "ROUTE_A_action_identity_gap_isolated": True,
            "ROUTE_B_honest_quadrature_contract_built": True,
        },
        "what_remains_open": {
            "physical_PhiFinC1_action_identity": True,
            "boundary_source_vanishing": True,
            "same_source_RZ_RX_bselected_emission": True,
            "honest_quadrature_source_emission": True,
        },
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "prior_next_work_status": next_work["status"],
        "prior_psm_c1_02_status": psm_c102["status"],
        "prior_unpatched_audit_status": unpatched_audit["status"],
    }

    certificate = {
        "certificate": f"{SLUG}_certificate",
        "status": STATUS,
        "candidate": rel(OUTPUT),
        "active_post_sm_parity_label": "PSM-C1-02",
        "active_post_sm_parity_routes": ["ROUTE-A", "ROUTE-B"],
        "normal_form_candidates_identified": True,
        "route_A_validator_passes": route_a_result["passes"],
        "route_B_honest_quadrature_emitted": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected PreResidualWeylVariationSelectionLemma or HonestQuadratureSource v1

Status: `{STATUS}`

Active post-SM-parity label: `PSM-C1-02`

Route labels: `ROUTE-A` / `ROUTE-B`

Boundary guardrail: `DONE-PARITY-00` remains frozen closed. This is post-SM-parity frontier work, not an SM-parity blocker.

## Theorem

**{theorem["name"]}.** {theorem["statement"]}

## Result

- `R_Z` and `R_X` are now locked as exact qutrit Weyl normal-form candidates.
- `ROUTE-A` still fails the strict action-kernel validator because the physical action identity, boundary/source vanishing, and same-source emission are not proved.
- `ROUTE-B` now has an honest quadrature source contract, but no independent execution has been emitted.

## Next Artifact

`{NEXT_ARTIFACT}`
"""

    write_json(NORMAL_FORM, normal_form)
    write_json(ROUTE_A_RESULT, route_a_result)
    write_json(ROUTE_B, route_b)
    write_json(EXIT, exit_matrix)
    write_json(NEXT, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, certificate)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
