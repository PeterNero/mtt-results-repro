"""Build PSM-C1-02 source-identity lemma derivation attempt.

The goal is to derive the SelectedFiniteC1SourceIdentityLemma without using
the local principle patch.  This builder separates what is actually derived
from what remains a physical-action ownership obstruction.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_psm_c1_02_ra3_samesourceemission_or_rb5_dynamicvalueownerfill.candidate.json"
SOURCE_IDENTITY = DATA / "selected_unpatchedfinitec1sourceidentity_or_honestindependentkernelexport" / "source_identity_route_audit.packet.json"
ACTION_ATTEMPT = DATA / "selected_finitec1sourceidentityprincipleinsertion_or_selectedactionderivation" / "selected_action_derivation_attempt.packet.json"
GUARDRAIL = DATA / "selected_finitec1sourceidentityprincipleinsertion_or_selectedactionderivation" / "unpatched_no_knob_guardrail.packet.json"
BOUNDARY = DATA / "selected_c1tracemeasurepromotion_or_actionboundaryproof" / "finite_trace_boundary_cancellation_certificate.packet.json"
SOURCE_OWNER = DATA / "selected_dynamicc1_sourceowner_fill_or_connectiontables_export_run" / "source_owner_field_matrix_after_backimport.packet.json"
NORMAL_FORM = DATA / "selected_samesource_dynamictransferidentity_or_galerkinc1contractions_emission.candidate.json"
RB3 = DATA / "selected_psm_c1_02_ra1_physicalactionequality_or_rb3_hessiansourcefill" / "route_b_rb3_hessian_source_fill.packet.json"

OUTPUT = DATA / "selected_psm_c1_02_sourceidentitylemma_derivation_attempt.candidate.json"
PACKET_DIR = DATA / "selected_psm_c1_02_sourceidentitylemma_derivation_attempt"
SUBCLAIM_MATRIX = PACKET_DIR / "source_identity_subclaim_derivation_matrix.packet.json"
OBSTRUCTION = PACKET_DIR / "single_surviving_obstruction.packet.json"
EXTERNAL_SUPPORT = PACKET_DIR / "external_methodology_support.packet.json"
NEXT_WORKORDER = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = CERTS / "selected_psm_c1_02_sourceidentitylemma_derivation_attempt_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_SourceIdentityLemma_DerivationAttempt_v1.md"

STATUS = "MTT_SELECTED_PSM_C1_02_SOURCEIDENTITYLEMMA_DERIVATION_ATTEMPT_BUILT_REDUCED_TO_ACTION_OWNERSHIP_OPEN"
NEXT = "MTT_Selected_PSM_C1_02_PhysicalActionOwnsFiniteTraceKernel_Proof_or_Countermodel_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    source_identity = load(SOURCE_IDENTITY)
    action_attempt = load(ACTION_ATTEMPT)
    guardrail = load(GUARDRAIL)
    boundary = load(BOUNDARY)
    owner = load(SOURCE_OWNER)
    normal = load(NORMAL_FORM)
    rb3 = load(RB3)
    fields = owner["field_results"]

    subclaims = {
        "selected_branch_restricts_Phi_fin_C1_to_finite_qutrit_weyl_quotient": {
            "derived_now": False,
            "support_closed": True,
            "source": rel(SOURCE_IDENTITY),
            "reason": "Finite Weyl support is maximized, but the physical action restriction is not theorem-emitted.",
        },
        "normalized_trace_frobenius_pairing_as_finite_source_measure": {
            "derived_now": False,
            "mathematical_pairing_closed": True,
            "physical_source_measure_closed": False,
            "source": rel(BOUNDARY),
            "reason": "Trace/Frobenius algebra and finite boundary cancellation are closed; physical source-measure ownership remains tied to the action restriction.",
        },
        "admissible_c1_variation_space": {
            "derived_now": fields["admissible_c1_variation_space"]["theorem_derived"],
            "source_owner_verified": fields["admissible_c1_variation_space"]["source_owner_verified"],
            "source": fields["admissible_c1_variation_space"]["source"],
            "reason": fields["admissible_c1_variation_space"]["reason"],
        },
        "pre_residual_phase_shift_variations_emit_R_Z_R_X": {
            "derived_now": False,
            "normal_form_ready": True,
            "source": rel(NORMAL_FORM),
            "reason": "The normal form identifies the needed equations, but selected Phi_fin^C1 transfer is not emitted.",
        },
        "same_source_second_variation_emits_b_selected": {
            "derived_now": False,
            "support_hessian_ready": rb3["hessian_source_support"]["positive_definite_support_hessian"],
            "source": rel(RB3),
            "reason": "The support Hessian/source equations are exact, but same-source Hessian emission is not theorem-derived.",
        },
        "finite_trace_rule_assembles_sector_and_hessian_rows": {
            "derived_now": False,
            "formal_replay_closed": True,
            "source": rel(SOURCE_IDENTITY),
            "reason": "Formal 110-row assembly is integrated; source-owned assembly still depends on the physical action ownership lemma.",
        },
        "postcheck_independence_guard": {
            "derived_now": fields["independence_guard"]["theorem_derived"],
            "source_owner_verified": fields["independence_guard"]["source_owner_verified"],
            "source": fields["independence_guard"]["source"],
            "reason": fields["independence_guard"]["reason"],
        },
    }

    derived_count = sum(1 for item in subclaims.values() if item["derived_now"] is True)
    mathematical_support_count = sum(
        1
        for item in subclaims.values()
        if item.get("support_closed") is True
        or item.get("mathematical_pairing_closed") is True
        or item.get("normal_form_ready") is True
        or item.get("support_hessian_ready") is True
        or item.get("formal_replay_closed") is True
        or item.get("source_owner_verified") is True
    )

    obstruction = {
        "schema": "MTTPSMC102SingleSurvivingSourceIdentityObstruction.v1",
        "active_label": "PSM-C1-02",
        "status": "SINGLE_SURVIVING_OBSTRUCTION_IS_PHYSICAL_ACTION_OWNERSHIP",
        "obstruction_name": "PhysicalActionOwnsFiniteTraceKernel",
        "statement_needed": (
            "The selected physical differentiated Phi_fin^C1 action on the q79/F,m=1 branch "
            "restricts to the selected finite qutrit Weyl trace/Frobenius row kernel before "
            "residual projection."
        ),
        "why_this_is_enough": [
            "Once physical action ownership is proved, the finite trace/Frobenius measure becomes the physical source measure.",
            "The selected admissible C1 variation space is already source-owner verified.",
            "The normal-form identity then emits R_Z, R_X, and b_selected from the same source.",
            "The finite trace rule then promotes primitive, sector, and Hessian/source rows together.",
        ],
        "why_not_derived_now": action_attempt["why_open"],
        "guardrail": guardrail["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    external_support = {
        "schema": "MTTPSMC102ExternalMethodologySupportForSourceIdentity.v1",
        "status": "EXTERNAL_SUPPORT_CLASSIFIED_AS_METHOD_ONLY_NOT_SOURCE_PROOF",
        "references": [
            {
                "title": "Finite-dimensional Weyl/Heisenberg operator trace orthogonality",
                "url": "https://en.wikipedia.org/wiki/Generalizations_of_Pauli_matrices",
                "supports": "finite Weyl operators naturally carry trace/Hilbert-Schmidt orthogonality",
                "used_as_mtt_source_proof": False,
            },
            {
                "title": "Galerkin method",
                "url": "https://en.wikipedia.org/wiki/Galerkin_method",
                "supports": "weighted-residual/weak-form projection explains the finite normal-equation shape",
                "used_as_mtt_source_proof": False,
            },
            {
                "title": "DOLFINx variational/Galerkin demo",
                "url": "https://docs.fenicsproject.org/dolfinx/v0.10.0/python/demos/demo_biharmonic.html",
                "supports": "methodological precedent for deriving finite matrix equations from a variational weak form",
                "used_as_mtt_source_proof": False,
            },
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterPSMC102SI1.v1",
        "previous_artifact": "MTT_Selected_PSM_C1_02_SourceIdentityLemma_DerivationAttempt_v1",
        "next_required_artifact": NEXT,
        "primary": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1a",
            "task": "Prove PhysicalActionOwnsFiniteTraceKernel from selected action/Theta/Strominger/Phi_fin structure.",
        },
        "secondary": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1b",
            "task": "Try to build a countermodel showing the closed finite support does not force physical action ownership.",
        },
        "status": "NEXT_WORKORDER_PHYSICAL_ACTION_OWNS_FINITE_TRACE_KERNEL_PROOF_OR_COUNTERMODEL",
    }

    candidate = {
        "candidate": "MTTSelectedPSMC102SourceIdentityLemmaDerivationAttempt",
        "active_label": "PSM-C1-02",
        "active_routes": ["SOURCE-IDENTITY/SI-1"],
        "closed_boundary": "DONE-PARITY-00",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "inputs": {
            "previous": rel(PREVIOUS),
            "previous_status": previous["status"],
            "source_identity_route_audit": rel(SOURCE_IDENTITY),
            "selected_action_derivation_attempt": rel(ACTION_ATTEMPT),
            "unpatched_guardrail": rel(GUARDRAIL),
            "finite_trace_boundary": rel(BOUNDARY),
            "source_owner_matrix": rel(SOURCE_OWNER),
            "same_source_normal_form": rel(NORMAL_FORM),
            "rb3_hessian_source": rel(RB3),
        },
        "output_packets": {
            "subclaim_derivation_matrix": rel(SUBCLAIM_MATRIX),
            "single_surviving_obstruction": rel(OBSTRUCTION),
            "external_methodology_support": rel(EXTERNAL_SUPPORT),
            "next_workorder": rel(NEXT_WORKORDER),
        },
        "theorem": {
            "name": "PSMC102SourceIdentityLemmaDerivationReductionTheorem",
            "proved": True,
            "statement": (
                "The current corpus/repo support derives the admissible C1 variation space and "
                "postcheck independence guard, and closes the finite trace algebra, normal-form "
                "identity, and support Hessian as mathematical support. It does not derive the "
                "SelectedFiniteC1SourceIdentityLemma unpatched. The single surviving obstruction is "
                "PhysicalActionOwnsFiniteTraceKernel: the selected physical differentiated Phi_fin^C1 "
                "action must be proved to restrict to the selected finite qutrit Weyl trace/Frobenius "
                "row kernel before residual projection."
            ),
        },
        "what_closes_now": {
            "SI1_derivation_attempt_completed": True,
            "admissible_c1_variation_space_derived": subclaims["admissible_c1_variation_space"]["derived_now"],
            "postcheck_independence_guard_derived": subclaims["postcheck_independence_guard"]["derived_now"],
            "single_surviving_obstruction_identified": True,
            "external_support_classified_method_only": True,
            "observed_constants_excluded_as_selectors": True,
            "superset_paths_constrained_to_locked_target": True,
        },
        "what_remains_open": {
            "PhysicalActionOwnsFiniteTraceKernel": True,
            "SelectedFiniteC1SourceIdentityLemma_unpatched": True,
            "selected_source_promotion": True,
            "true_equivalence_closed": False,
        },
        "subclaim_counts": {
            "derived_now": derived_count,
            "support_or_method_closed": mathematical_support_count,
            "total": len(subclaims),
        },
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_PSM_C1_02_SourceIdentityLemma_DerivationAttempt_v1",
        "active_label": "PSM-C1-02",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "next_required_artifact": NEXT,
        "lemma_derived_unpatched": False,
        "single_surviving_obstruction": "PhysicalActionOwnsFiniteTraceKernel",
        "derived_subclaim_count": derived_count,
        "support_or_method_closed_count": mathematical_support_count,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    for path, obj in [
        (SUBCLAIM_MATRIX, {"schema": "MTTPSMC102SourceIdentitySubclaimDerivationMatrix.v1", "active_label": "PSM-C1-02", "status": "SUBCLAIMS_AUDITED_LEMMA_UNPATCHED_OPEN", "subclaims": subclaims, "derived_count": derived_count, "support_or_method_closed_count": mathematical_support_count, "observed_data_used_as_selector": False, "target_fitting_used": False}),
        (OBSTRUCTION, obstruction),
        (EXTERNAL_SUPPORT, external_support),
        (NEXT_WORKORDER, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    NOTE.write_text(
        f"""# MTT Selected PSM C1 02 SourceIdentityLemma DerivationAttempt v1

Status label: `PSM-C1-02 / SOURCE-IDENTITY / SI-1`

Status: `{STATUS}`

Closed boundary label: `DONE-PARITY-00`

## Theorem

**PSMC102SourceIdentityLemmaDerivationReductionTheorem.** The current corpus/repo support derives the admissible C1 variation space and the postcheck independence guard, and closes finite trace algebra, the normal-form identity, and the support Hessian as mathematical support. It does **not** derive the `SelectedFiniteC1SourceIdentityLemma` unpatched.

The single surviving obstruction is:

`PhysicalActionOwnsFiniteTraceKernel`

That is, the selected physical differentiated `Phi_fin^C1` action must be proved to restrict to the selected finite qutrit Weyl trace/Frobenius row kernel before residual projection.

## Superset Strategy

The straight physical-action route, the finite Weyl route, the Galerkin route, and external variational analogies all point to the same object. They are not knobs. External references are methodology only, not MTT source proof.

## Next Artifact

`{NEXT}`
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
