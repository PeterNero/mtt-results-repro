"""Build PSM-C1-02 physical-action finite-trace ownership proof/countermodel.

This is the SI-1a/SI-1b attack following the source-identity reduction:
try to prove PhysicalActionOwnsFiniteTraceKernel directly, and import the
support-only countermodel when the proof cannot be completed from closed
finite trace support alone.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_psm_c1_02_physicalactionowns_finitetracekernel_proof_or_countermodel"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
DIRECT = PACKET_DIR / "direct_proof_attempt.packet.json"
COUNTERMODEL = PACKET_DIR / "support_only_countermodel_import.packet.json"
REMAINING = PACKET_DIR / "remaining_kernel_theorem.packet.json"
NEXT_WORK = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_PhysicalActionOwnsFiniteTraceKernel_Proof_or_Countermodel_v1.md"

PREVIOUS = DATA / "selected_psm_c1_02_sourceidentitylemma_derivation_attempt.candidate.json"
PREVIOUS_OBSTRUCTION = DATA / "selected_psm_c1_02_sourceidentitylemma_derivation_attempt" / "single_surviving_obstruction.packet.json"
ROUTE_C = DATA / "selected_routec_weylvariation_sourceprinciple_or_kernelclosure" / "routec_decision_and_next_gate.packet.json"
ROUTE_A = DATA / "selected_phifinc1_actionrestriction_or_boundarysource_emission" / "route_a_action_restriction_validator_v2.packet.json"
SUPPORT_COUNTERMODEL = (
    DATA
    / "selected_minimalfinitec1sourcepromotionlemma_proof_or_countermodel"
    / "closed_support_not_enough_countermodel.packet.json"
)
SUPPORT_COUNTERMODEL_VALIDATOR = (
    DATA
    / "selected_minimalfinitec1sourcepromotionlemma_proof_or_countermodel"
    / "countermodel_validator_result.packet.json"
)
SOURCE_ROUTE_AUDIT = (
    DATA
    / "selected_unpatchedfinitec1sourceidentity_or_honestindependentkernelexport"
    / "source_identity_route_audit.packet.json"
)
FORMAL_110 = (
    DATA
    / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource"
    / "formal_110_row_replay_integrated.packet.json"
)

STATUS = "MTT_SELECTED_PSM_C1_02_PHYSICALACTIONOWNS_FINITETRACEKERNEL_ATTACK_BUILT_COUNTERMODEL_SUPPORT_ONLY_PROOF_BLOCKED"
NEXT = "MTT_Selected_PSM_C1_02_SelectedPhiFinC1PreResidualActionKernelTheorem_Proof_or_LocalPrincipleDecision_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    previous_obstruction = load(PREVIOUS_OBSTRUCTION)
    route_c = load(ROUTE_C)
    route_a = load(ROUTE_A)
    support_countermodel = load(SUPPORT_COUNTERMODEL)
    support_validator = load(SUPPORT_COUNTERMODEL_VALIDATOR)
    source_route_audit = load(SOURCE_ROUTE_AUDIT)
    formal_110 = load(FORMAL_110)
    kernel = route_c["minimal_action_axiom_or_theorem"]

    direct = {
        "schema": "MTTPSMC102PhysicalActionOwnsFiniteTraceKernelDirectProofAttempt.v1",
        "active_label": "PSM-C1-02",
        "route_label": "SOURCE-IDENTITY",
        "clause": "SI-1a",
        "target": "PhysicalActionOwnsFiniteTraceKernel",
        "statement_needed": previous_obstruction["statement_needed"],
        "closed_subclauses": route_a["closed_subclauses"],
        "still_required_physical_subclauses": route_a["still_required_physical_subclauses"],
        "attempted_sources": {
            "previous_reduction": rel(PREVIOUS),
            "previous_obstruction": rel(PREVIOUS_OBSTRUCTION),
            "route_a_action_restriction_validator": rel(ROUTE_A),
            "route_c_weyl_variation_decision": rel(ROUTE_C),
            "source_identity_route_audit": rel(SOURCE_ROUTE_AUDIT),
            "formal_110_replay": rel(FORMAL_110),
        },
        "closed_support": {
            "formal_110_rows_executed": formal_110["formal_110_rows_executed"],
            "formal_110_row_counts": formal_110["row_counts"],
            "finite_trace_and_weyl_support_closed": True,
            "route_a_mathematical_support_closed": all(route_a["closed_subclauses"].values()),
        },
        "proof_result": {
            "physical_action_owns_finite_trace_kernel_proved_now": False,
            "reason_not_proved": [
                *route_a["why_not_closed"],
                "Route C identifies the needed action kernel theorem but explicitly reports it as not proved here.",
                "The existing support-only countermodel validates that closed finite support facts do not force source promotion.",
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    countermodel = {
        "schema": "MTTPSMC102SupportOnlyCountermodelImport.v1",
        "active_label": "PSM-C1-02",
        "route_label": "SOURCE-IDENTITY",
        "clause": "SI-1b",
        "imports": {
            "closed_support_countermodel": rel(SUPPORT_COUNTERMODEL),
            "countermodel_validator_result": rel(SUPPORT_COUNTERMODEL_VALIDATOR),
        },
        "support_only_countermodel_valid": support_countermodel["status"]
        == "COUNTERMODEL_TO_DERIVING_SOURCE_PROMOTION_FROM_CLOSED_SUPPORT_ONLY",
        "closed_support_not_enough": True,
        "validator_rejects_current_two_exit_packet": support_validator["returncode"] == 1,
        "blocks_derivation_from_closed_support_alone": True,
        "closed_support_facts_true": support_countermodel["closed_support_facts_true"],
        "additional_structural_support_true": support_countermodel["additional_structural_support_true"],
        "source_promotion_fields_false": support_countermodel["source_promotion_fields_false"],
        "therefore": (
            "Closed q79/F,m=1 finite support, exact finite trace algebra, and formal row replay do not by themselves "
            "prove that the physical differentiated Phi_fin^C1 action owns the finite trace/Frobenius row kernel."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    remaining = {
        "schema": "MTTPSMC102RemainingKernelTheorem.v1",
        "active_label": "PSM-C1-02",
        "route_label": "SOURCE-IDENTITY",
        "clause": "SI-1c",
        "theorem_name": kernel["name"],
        "statement": kernel["statement"],
        "proved_now": kernel["proved_here"],
        "acceptable_proof_sources": kernel["acceptable_proof_sources"],
        "forbidden_shortcuts": kernel["forbidden_shortcuts"],
        "would_close": kernel["would_close"],
        "must_not_be_used_as_free_patch": kernel["must_not_be_used_as_free_patch"],
        "next_target": "PSM-C1-02 / SOURCE-IDENTITY / SI-1c",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterPSMC102SI1aSI1b.v1",
        "previous_artifact": "MTT_Selected_PSM_C1_02_PhysicalActionOwnsFiniteTraceKernel_Proof_or_Countermodel_v1",
        "next_required_artifact": NEXT,
        "primary": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1c",
            "task": (
                "Prove or explicitly promote the SelectedPhiFinC1PreResidualActionKernelTheorem: the selected "
                "physical differentiated Phi_fin^C1 action must be the least-defect trace/Frobenius source "
                "functional emitting R_Z/R_X and b_selected with zero extra boundary/source term."
            ),
        },
        "secondary": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1b",
            "task": "Keep the support-only countermodel as a guardrail against reusing closed row values as source proof.",
        },
        "superset_strategy": {
            "mode": "straight physical-action, Route C Weyl-variation, and independent Galerkin routes are constrained exits to the same locked theorem",
            "paths_used_as_free_parameters": False,
            "locked_target_used_only_as_postcheck": True,
        },
        "status": "NEXT_WORKORDER_SELECTED_PHIFINC1_PRERESIDUAL_ACTION_KERNEL_THEOREM",
    }

    candidate = {
        "candidate": "MTTSelectedPSMC102PhysicalActionOwnsFiniteTraceKernelProofOrCountermodel",
        "active_label": "PSM-C1-02",
        "active_routes": ["SOURCE-IDENTITY/SI-1a", "SOURCE-IDENTITY/SI-1b"],
        "closed_boundary": "DONE-PARITY-00",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "inputs": {
            "previous": rel(PREVIOUS),
            "previous_status": previous["status"],
            "previous_obstruction": rel(PREVIOUS_OBSTRUCTION),
            "route_a_action_restriction_validator": rel(ROUTE_A),
            "route_c_decision_and_next_gate": rel(ROUTE_C),
            "support_only_countermodel": rel(SUPPORT_COUNTERMODEL),
            "support_only_validator": rel(SUPPORT_COUNTERMODEL_VALIDATOR),
            "source_identity_route_audit": rel(SOURCE_ROUTE_AUDIT),
            "formal_110_replay": rel(FORMAL_110),
        },
        "output_packets": {
            "direct_proof_attempt": rel(DIRECT),
            "support_only_countermodel_import": rel(COUNTERMODEL),
            "remaining_kernel_theorem": rel(REMAINING),
            "next_workorder": rel(NEXT_WORK),
        },
        "what_closes_now": {
            "direct_proof_attempt_completed": True,
            "support_only_countermodel_imported": True,
            "closed_support_alone_blocked_as_derivation_route": True,
            "remaining_kernel_theorem_identified": True,
            "superset_paths_constrained_to_locked_target": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "SelectedPhiFinC1PreResidualActionKernelTheorem": True,
            "PhysicalActionOwnsFiniteTraceKernel": True,
            "SelectedFiniteC1SourceIdentityLemma_unpatched": True,
            "selected_source_promotion": True,
            "true_equivalence_closed": False,
        },
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_PSM_C1_02_PhysicalActionOwnsFiniteTraceKernel_Proof_or_Countermodel_v1",
        "active_label": "PSM-C1-02",
        "active_routes": candidate["active_routes"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "next_required_artifact": NEXT,
        "physical_action_owns_finite_trace_kernel_proved": False,
        "support_only_countermodel_valid": countermodel["support_only_countermodel_valid"],
        "closed_support_alone_blocked_as_derivation_route": True,
        "remaining_kernel_theorem": kernel["name"],
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    for path, obj in [
        (DIRECT, direct),
        (COUNTERMODEL, countermodel),
        (REMAINING, remaining),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    NOTE.write_text(
        f"""# MTT Selected PSM C1 02 PhysicalActionOwnsFiniteTraceKernel Proof or Countermodel v1

Status label: `PSM-C1-02 / SOURCE-IDENTITY / SI-1a`

Countermodel label: `PSM-C1-02 / SOURCE-IDENTITY / SI-1b`

Status: `{STATUS}`

Closed boundary label: `DONE-PARITY-00`

## Result

The direct proof attempt for `PhysicalActionOwnsFiniteTraceKernel` is complete but not closed. The repo/corpus closes the finite selected C1 quotient, trace/Frobenius normalization, selected Weyl variation algebra, algebraic finite boundary cancellation, and formal 110-row replay. It does not yet prove that the physical differentiated `Phi_fin^C1` action restricts to and owns that finite trace/Frobenius row kernel with zero extra physical boundary/source term.

The support-only countermodel is imported as a guardrail: closed finite support and exact replay rows do not force source promotion.

## Remaining Theorem

`SelectedPhiFinC1PreResidualActionKernelTheorem`

{kernel["statement"]}

This theorem is not assumed and is not used as a free patch.

## Superset Strategy

The straight physical-action route, Route C Weyl-variation route, and independent Galerkin route are constrained exits to the same locked target. They are not knobs. Observed SM values, benchmark profiles, locked `A^T b` values, and replay rows remain postchecks only.

## Next Artifact

`{NEXT}`
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
