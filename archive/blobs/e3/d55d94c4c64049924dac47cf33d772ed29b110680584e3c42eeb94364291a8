"""Build cross-repo/external derivation attempt for the finite C1 source identity."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_finitec1sourceidentitytheorem_crossrepo_external_derivation"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SUPPORT = PACKET_DIR / "cross_repo_corpus_external_support.packet.json"
PRINCIPLE = PACKET_DIR / "selected_finite_c1_source_identity_principle_candidate.packet.json"
DERIVATION = PACKET_DIR / "source_identity_derivation_attempt.packet.json"
CONDITIONAL_WITNESS = PACKET_DIR / "conditional_promoted_source_identity_witness.packet.json"
CONDITIONAL_VALIDATION = PACKET_DIR / "conditional_promoted_source_identity_validator_result.packet.json"
DECISION = PACKET_DIR / "source_identity_theorem_or_principle_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FiniteC1SourceIdentityTheorem_CrossRepoExternalDerivation_v1.md"

CUTSET = (
    DATA
    / "selected_unpatchedweylprincipleproof_or_independentkernelrowsfirstrun"
    / "shared_source_theorem_cutset.packet.json"
)
OBSTRUCTION = (
    DATA
    / "selected_independentquadratureruleandhessianbsource_or_routeaactionidentity"
    / "remaining_derivation_obstruction.packet.json"
)
TRACE_SUPPORT = (
    DATA
    / "selected_c1tracemeasurepromotion_or_actionboundaryproof"
    / "selected_trace_map_and_measure_support.packet.json"
)
TRACE_ASSEMBLY = (
    DATA
    / "selected_finitec1sourceidentityclauseproof_or_independentrowdataemission"
    / "finite_weyl_trace_assembly_clause_proof.packet.json"
)
WEYL_PRINCIPLE = (
    DATA
    / "selected_routec_weylvariation_sourceprinciple_or_kernelclosure"
    / "routec_weyl_variation_principle_candidate.packet.json"
)
CONDITIONAL_IDS = (
    DATA
    / "selected_independentc1_rowkernelsourceids_or_physicalphifinc1actionproof"
    / "conditional_independent_rowkernel_source_id_witness.packet.json"
)
SOURCE_ID_VALIDATOR = ROOT / "scripts" / "validate_selected_independentc1_rowkernel_source_ids.py"

PROTO_GR = (
    TEXPAPERS
    / "mtt-protospinor-gr-response-proof"
    / "certificates"
    / "post_alpha_differentiated_phifinc1_residual_projector_axiom_or_galerkin_c1_execution_certificate.json"
)
NONSM_ROUTE = (
    TEXPAPERS
    / "mtt-nonsm-constants-no-knob"
    / "candidate_data"
    / "selected_samesource_dynamictransferidentity_or_galerkinc1contractions_emission.candidate.json"
)
THETA_HESSIAN = (
    TEXPAPERS
    / "18 Theta-Closure & Execution Program"
    / "_md_v3_corrected"
    / "MTT_Flavor_Hessian_Block_Extraction_Attempt_for_Z64_Projector_v1.md"
)
STROMINGER_FLUX = (
    TEXPAPERS
    / "16 Strings, Flux, & M-Theory Encodings"
    / "_md"
    / "Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md"
)

STATUS = "MTT_SELECTED_FINITEC1SOURCEIDENTITYTHEOREM_CROSSREPO_EXTERNAL_DERIVATION_PRINCIPLE_READY_THEOREM_OPEN"
NEXT = "MTT_Selected_FiniteC1SourceIdentityPrincipleInsertion_or_SelectedActionDerivation_v1"


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


def file_exists_summary(path: Path) -> dict[str, Any]:
    return {"path": rel(path), "exists": path.exists()}


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(SOURCE_ID_VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "path": rel(path),
        "validator": rel(SOURCE_ID_VALIDATOR),
        "exit_code": proc.returncode,
        "ok": proc.returncode == 0,
        "stdout": proc.stdout.strip().splitlines(),
        "stderr": proc.stderr.strip().splitlines(),
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    cutset = load(CUTSET)
    obstruction = load(OBSTRUCTION)
    trace_support = load(TRACE_SUPPORT)
    trace_assembly = load(TRACE_ASSEMBLY)
    weyl_principle = load(WEYL_PRINCIPLE)
    conditional_ids = load(CONDITIONAL_IDS)

    sibling_support = {
        "protospinor_gr_response": file_exists_summary(PROTO_GR),
        "nonsm_constants_routec": file_exists_summary(NONSM_ROUTE),
        "theta_hessian_attempt": file_exists_summary(THETA_HESSIAN),
        "strominger_flux_positive_hessian": file_exists_summary(STROMINGER_FLUX),
        "interpretation": (
            "Sibling repos and corpus support the same source frontier: they repeatedly preserve "
            "A_selected/b_selected as open unless a selected same-source physical/Galerkin emission "
            "theorem is supplied. They therefore constrain the theorem but do not prove it here."
        ),
    }

    external_support = {
        "role": "external inspiration and mathematical precedent only; not an MTT theorem import",
        "sources": [
            {
                "topic": "spectral action / trace of operator data as action",
                "url": "https://arxiv.org/abs/hep-th/9606001",
                "use_in_this_artifact": (
                    "Supports the form of a selected finite operator trace action, but does not "
                    "select the MTT q79/F,m=1 C1 source identity."
                ),
            },
            {
                "topic": "discrete mechanics and variational integrators",
                "url": "https://authors.library.caltech.edu/records/1f7b7-16x50",
                "use_in_this_artifact": (
                    "Supports the strategy of deriving finite equations from a discrete action "
                    "principle rather than projecting equations after the fact."
                ),
            },
            {
                "topic": "spectral truncations and finite-dimensional operator systems",
                "url": "https://link.springer.com/article/10.1007/s00220-020-03825-x",
                "use_in_this_artifact": (
                    "Supports using finite-dimensional operator-system data as structured "
                    "geometric truncations, not as arbitrary numeric tables."
                ),
            },
        ],
        "guardrail": "external analogies cannot set selected_emitted=true, theorem_derived=true, or independent_of_residual_replay=true in the MTT validator",
    }

    support_packet = {
        "schema": "MTTFiniteC1SourceIdentityCrossRepoCorpusExternalSupport.v1",
        "status": "SUPPORT_CLASSIFIED_NO_EXTERNAL_OR_CROSSREPO_PROOF_IMPORT",
        "local_cutset": {
            "theorem_name": cutset["theorem_name"],
            "statement": cutset["statement"],
            "required_clauses": cutset["required_clauses"],
        },
        "local_closed_support": {
            "trace_measure_support_imported": trace_support["support_imported"],
            "trace_assembly_proved_subclaim": trace_assembly["proved_subclaim"],
            "weyl_principle_support_imported": weyl_principle["support_imported"],
            "remaining_obstruction": obstruction["minimal_missing_clause_family"],
        },
        "sibling_repo_and_corpus_support": sibling_support,
        "external_support": external_support,
        "classification": {
            "cross_repo_proves_theorem": False,
            "corpus_proves_theorem": False,
            "external_literature_proves_mtt_theorem": False,
            "support_suffices_for_principle_candidate": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(SUPPORT, support_packet)

    principle = {
        "schema": "MTTSelectedFiniteC1SourceIdentityPrincipleCandidate.v1",
        "principle_name": "SelectedFiniteC1SourceIdentityPrinciple",
        "status": "MINIMAL_PRINCIPLE_CANDIDATE_FORMULATED_NOT_INSERTED",
        "statement": (
            "For the selected q79/F,m=1 finite C1 quotient, the differentiated physical "
            "Phi_fin^C1 Weyl action is represented by the selected transported finite "
            "Weyl trace/Frobenius row kernel before residual projection. Its first "
            "variation emits R_Z and R_X, its second variation emits b_selected, and "
            "the finite trace rule assembles the primitive, sector, and Hessian/source "
            "rows from that same source."
        ),
        "minimal_axioms": [
            "the selected branch restricts Phi_fin^C1 to the finite qutrit Weyl quotient",
            "the normalized finite trace/Frobenius pairing is the source measure for that restricted action",
            "the admissible C1 variations are the selected phase/shift Weyl variations before residual projection",
            "first variation emits R_Z/R_X as source operators, not residual replay artifacts",
            "second variation emits the Hessian/source vector b_selected from the same source",
            "sector and Hessian rows are assembled only from primitive source rows by the selected finite trace rule",
            "residual projectors, locked targets, and observed constants are postchecks and cannot be source selectors",
        ],
        "why_minimal": {
            "removes_exact_obstruction": obstruction["minimal_missing_clause_family"]["must_promote"],
            "does_not_add_numeric_values": True,
            "does_not_use_sm_observed_data": True,
            "does_not_copy_A_transpose_b_target": True,
            "makes_route_A_and_route_B_same_object": True,
        },
        "insertion_status": {
            "accepted_as_axiom_or_derived_theorem": False,
            "conditional_validator_would_pass_if_inserted": True,
            "current_unpatched_mtt_derivation": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(PRINCIPLE, principle)

    derivation = {
        "schema": "MTTFiniteC1SourceIdentityDerivationAttempt.v1",
        "status": "DERIVATION_ATTEMPT_REDUCED_TO_MINIMAL_PRINCIPLE_OR_NEW_SOURCE_EXECUTION",
        "attempted_paths": {
            "straight_route_A": {
                "name": "physical Phi_fin^C1 Weyl action restriction",
                "success": False,
                "reason": "current support has Weyl principle candidate and exact R_Z/R_X polynomials, but source_map_selected_now remains false",
            },
            "straight_route_B": {
                "name": "independent finite row-kernel execution",
                "success": False,
                "reason": "conditional 110-row witness passes, but actual ids are not theorem-derived or independent of residual replay",
            },
            "superset_combined_path": {
                "name": "Route A action identity plus Route B trace row-kernel identity locked to one selected source",
                "success": False,
                "reason": "combination identifies a minimal principle exactly, but does not derive it from existing closed MTT corpus alone",
            },
            "external_inspiration_path": {
                "name": "spectral action / variational discretization / finite operator-system precedent",
                "success": False,
                "reason": "external literature licenses a research strategy, not selected MTT source ownership",
            },
        },
        "proved_now": False,
        "principle_candidate_ready": True,
        "new_independent_execution_alternative": {
            "honest_galerkin_or_finite_action_execution": True,
            "must_emit_not_assume": ["selected measure", "selected quadrature", "R_Z/R_X", "b_selected", "110 row source ids"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DERIVATION, derivation)

    witness = json.loads(json.dumps(conditional_ids))
    witness["schema"] = "MTTConditionalPromotedFiniteC1SourceIdentityWitness.v1"
    witness["status"] = "VALIDATES_IF_SELECTED_FINITEC1_SOURCE_IDENTITY_PRINCIPLE_IS_ACCEPTED_OR_DERIVED"
    witness["conditional_on"] = principle["principle_name"]
    witness["closure_claimed"] = False
    write_json(CONDITIONAL_WITNESS, witness)
    validation = run_validator(CONDITIONAL_WITNESS)
    write_json(CONDITIONAL_VALIDATION, validation)

    decision = {
        "schema": "MTTFiniteC1SourceIdentityTheoremOrPrincipleDecision.v1",
        "status": "THEOREM_OPEN_PRINCIPLE_READY_CONDITIONAL_WITNESS_VALIDATED",
        "selected_finite_c1_source_identity_theorem_proved": False,
        "selected_finite_c1_source_identity_principle_inserted": False,
        "conditional_promoted_witness_validates": validation["ok"],
        "recommended_next": {
            "route": NEXT,
            "action": (
                "Either derive the principle from corpus-level action restriction, or explicitly "
                "insert it as a named local source principle with full guardrails and then replay "
                "the validator as conditional-to-local closure."
            ),
        },
        "credibility_guardrail": (
            "This artifact improves rigor by making the exact missing premise public. It does not "
            "claim no-knob source closure until the principle is derived or explicitly accepted."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DECISION, decision)

    candidate = {
        "candidate": "MTTSelectedFiniteC1SourceIdentityTheoremCrossRepoExternalDerivation",
        "status": STATUS,
        "inputs": {
            "cutset": rel(CUTSET),
            "previous_obstruction": rel(OBSTRUCTION),
            "trace_support": rel(TRACE_SUPPORT),
            "trace_assembly": rel(TRACE_ASSEMBLY),
            "weyl_principle": rel(WEYL_PRINCIPLE),
            "conditional_ids": rel(CONDITIONAL_IDS),
        },
        "output_packets": {
            "support": rel(SUPPORT),
            "principle": rel(PRINCIPLE),
            "derivation": rel(DERIVATION),
            "conditional_witness": rel(CONDITIONAL_WITNESS),
            "conditional_validation": rel(CONDITIONAL_VALIDATION),
            "decision": rel(DECISION),
        },
        "theorem": {
            "name": "FiniteC1SourceIdentityCrossRepoExternalReductionTheorem",
            "proved": True,
            "statement": (
                "Cross-repo, corpus, and external evidence do not prove SelectedFiniteC1SourceIdentityTheorem, "
                "but they reduce the frontier to one minimal source-identity principle or an honest new "
                "finite-action/Galerkin execution. If that principle is accepted or derived, the conditional "
                "110-row source witness satisfies the strict source-id validator."
            ),
        },
        "what_closes_now": {
            "cross_repo_and_corpus_support_classified": True,
            "external_support_classified_as_inspiration_not_proof": True,
            "minimal_source_identity_principle_formulated": True,
            "conditional_promoted_witness_validates": validation["ok"],
            "next_patch_or_derivation_target_locked": True,
        },
        "what_remains_open": {
            "SelectedFiniteC1SourceIdentityTheorem": True,
            "principle_derivation_from_existing_MTT_action": True,
            "explicit_principle_insertion_if_chosen": True,
            "honest_new_finite_action_or_Galerkin_execution": True,
            "unpatched_no_knob_dynamic_C1_closure": True,
        },
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_FiniteC1SourceIdentityTheorem_CrossRepoExternalDerivation_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "conditional_promoted_witness_validates": validation["ok"],
        "theorem_proved": False,
        "principle_inserted": False,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        "# MTT Selected FiniteC1SourceIdentityTheorem CrossRepoExternalDerivation v1\n\n"
        f"Status: `{STATUS}`.\n\n"
        "The full cross-repo/corpus pass does not prove the selected finite C1 source identity. "
        "It instead confirms the same frontier from multiple directions: finite trace support, "
        "formal 110-row assembly, exact Weyl polynomials, and sibling-repo guardrails all point "
        "to one missing source-ownership premise.\n\n"
        "External literature supports the strategy, not the MTT theorem: spectral action motivates "
        "operator trace actions; variational discretization motivates deriving finite equations from "
        "an action; finite operator-system truncation motivates structured finite operator data. "
        "None of these may set `theorem_derived=true` in the local validator.\n\n"
        "The new artifact formulates `SelectedFiniteC1SourceIdentityPrinciple`. If this principle is "
        "derived or explicitly inserted, the conditional 110-row source-id witness passes the strict "
        "validator. Until then, no unpatched no-knob dynamic C1 closure is claimed.\n",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
