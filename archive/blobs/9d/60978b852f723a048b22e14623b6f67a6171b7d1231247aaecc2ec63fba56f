"""Build paper-integration manifest for non-theorem-derived Route-C gates.

The repo has several honest caveats of the form "not theorem-derived".  This
artifact maps each caveat to a named theorem/lemma insertion in the relevant
papers, with proof obligations and anti-overclaim wording.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
OUTPUT = DATA / "selected_source_paper_integration_manifest.candidate.json"
CERT = CERTS / "selected_source_paper_integration_manifest_certificate.json"
NOTE = CORPUS / "MTT_Selected_Source_Paper_Integration_Manifest_v1.md"

PAPERS = {
    "strominger_system": r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\16 Strings, Flux, & M-Theory Encodings\Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md",
    "flux_selection": r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\16 Strings, Flux, & M-Theory Encodings\Modal_Triplet_Theory__MTT_as_a_Selection_Principle_for_Heterotic_Flux_Compactifications.md",
    "theta_nonabelian_overlaps": r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\18 Theta-Closure & Execution Program\Theta_Closure_in_Modal_Triplet_Theory_II__Direct_Geometric_Realization_of_Nonabelian_Overlaps.md",
    "theta_execution_flavor": r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\18 Theta-Closure & Execution Program\Execution_of_Modal_Triplet_Theory_II__Flavor__CKM_PMNS__and_Higgs_Sector_on_the_CY_Corner_v2.md",
    "theta_superset": r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\18 Theta-Closure & Execution Program\Superset_Determinations_in_Modal_Triplet_Theory_v2.md",
    "parameters_falsifiability": r"C:\Users\nero_\Downloads\TEXPAPERS\2 Meta & Diagnosis & Universality\_md\Modal_Triplet_Theory__Parameters__Closure__and_Structural_Falsifiability.md",
}


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def main() -> None:
    insertions = [
        {
            "id": "I1_selected_strominger_minimizer_to_phifin_trace",
            "status": "PAPER_SECTION_REQUIRED",
            "target_papers": ["strominger_system", "flux_selection"],
            "section_title": "Selected Strominger Minimizer and Finite Phi_fin Trace",
            "current_blockers_resolved_if_proved": [
                "route_c_residual.selected_source_verified",
                "selected_minimizer_identifier",
                "Phi_fin_selected_values",
            ],
            "theorem_statement": (
                "For the q79/F,m=1 S3/Green-Schwarz branch selected by the MTT admissibility functional, "
                "the Strominger/HYM minimizer has a canonical finite Phi_fin trace whose residual, rho_E, "
                "metric, connection, D_E, Riesz/Green, dotD, and C1 primitive payloads are the Route-C finite packets."
            ),
            "proof_obligations": [
                "Define the exact selection functional on the q79/F,m=1 S3/GS sector.",
                "Prove existence/uniqueness or canonical equivalence class of the selected minimizer.",
                "Define Phi_fin as a functorial Galerkin/Cech trace, not a fitted projection.",
                "Prove Phi_fin preserves branch orientation, torsion m=1, S3 class, and GS cancellation.",
                "Emit selected values or a reproducible algorithm with error/gap certificate.",
            ],
            "safe_wording": (
                "Until this theorem is proved, Route-C packets are admissible numerical/support data, not selected-source proof data."
            ),
        },
        {
            "id": "I2_projective_rhoe_source_promotion",
            "status": "PAPER_SECTION_REQUIRED",
            "target_papers": ["strominger_system", "flux_selection", "theta_nonabelian_overlaps"],
            "section_title": "Projective/Twisted rho_E Source Promotion",
            "current_blockers_resolved_if_proved": [
                "R2_source_promotion_for_rhoE",
                "selected projective/twisted rho_E",
                "ordinary_or_selected_projective_source_promotion",
            ],
            "theorem_statement": (
                "The selected S3 Deligne/Cech class induces the Heisenberg/Weyl projective rho_E packet on the active F3^2 deck shadow, "
                "with central phase fixed by the same gerbe/Green-Schwarz data and not by empirical targets."
            ),
            "proof_obligations": [
                "Construct the gerbe module or twisted Chan-Paton bundle on the selected cover.",
                "Show the active g1,g2 deck image forces the F3^2 Heisenberg cocycle.",
                "Prove g3..g6 are in the kernel or quantify their smooth lift action.",
                "Show the clock/shift packet is canonical up to gauge equivalence.",
                "Prove compatibility with Freed-Witten and GS data.",
            ],
            "safe_wording": (
                "The current Heisenberg/Weyl packet is a canonical numerical candidate; source promotion remains open."
            ),
        },
        {
            "id": "I3_smooth_bn_galerkin_lift_theorem",
            "status": "PAPER_SECTION_REQUIRED",
            "target_papers": ["theta_nonabelian_overlaps", "theta_execution_flavor", "strominger_system"],
            "section_title": "Smooth Gerbe-Twisted B_N Galerkin Lift",
            "current_blockers_resolved_if_proved": [
                "R4_full_selected_basis_data",
                "selected_deck_or_equivalent_cover",
                "smooth scalar basis functions phi_m",
                "full_iwasawa_truncation_error_certificate",
            ],
            "theorem_statement": (
                "The F3^2 x C3 twisted Fourier scaffold is the first finite level of a convergent smooth non-invariant Galerkin basis B_N "
                "for the selected Iwasawa/Strominger branch, with controlled quadrature and truncation error."
            ),
            "proof_obligations": [
                "Define the smooth nil/Heisenberg theta basis extending the F3^2 Fourier scaffold.",
                "Prove quotient/deck equivariance for the selected Iwasawa lattice.",
                "Prove Gram positivity and convergence of quadrature.",
                "Prove complement gap stability under increasing N.",
                "Bound truncation error between model active Laplacian and full Iwasawa/Strominger operator.",
            ],
            "safe_wording": (
                "The 27-mode scaffold gives a verified finite model; it is not yet a full smooth Galerkin convergence theorem."
            ),
        },
        {
            "id": "I4_selected_DE_action_and_source_flags",
            "status": "PAPER_SECTION_REQUIRED",
            "target_papers": ["theta_nonabelian_overlaps", "theta_execution_flavor", "strominger_system"],
            "section_title": "Selected D_E Action, Sector Projectors, and Source Flags",
            "current_blockers_resolved_if_proved": [
                "operator_slots[*].selected_source_verified",
                "selected_D_E_source_promotion",
                "sector_projectors",
                "R3_full_selected_operator_spectral_data",
            ],
            "theorem_statement": (
                "The selected Strominger/HYM operator D_E restricts to the emitted smooth B_N basis with sector kernels Q,u,d,L,e,N,H, "
                "and the selected_source_verified flags are theorem consequences of the minimizer and Phi_fin trace."
            ),
            "proof_obligations": [
                "Derive D_E from the selected connection, not from a model-active substitute.",
                "Prove the 27-mode matrix is the N=1 truncation of the selected D_E.",
                "Construct sector projectors in the same basis.",
                "Prove family kernels have dimension 3 and Higgs kernel dimension 1 for the selected operator.",
                "Specify exactly when selected_source_verified may be set true.",
            ],
            "safe_wording": (
                "The current D_E matrix layer is validator-consistent under diagnostic source lift; the honest selected flags remain false."
            ),
        },
        {
            "id": "I5_dotD_alpha1_and_C1_response",
            "status": "PAPER_SECTION_REQUIRED",
            "target_papers": ["theta_execution_flavor", "theta_nonabelian_overlaps"],
            "section_title": "dotD_alpha1, Riesz/Green Response, and C1 Overlap Tensor",
            "current_blockers_resolved_if_proved": [
                "dotD_alpha1_in_same_basis",
                "selected_dotD_source_verified",
                "alpha1_driver_verified",
                "R5_selected_C1_response",
            ],
            "theorem_statement": (
                "The alpha1 deformation differentiates the selected D_E within the same branch and same B_N basis, producing horizontal responses, "
                "Riesz/Green inverses, and finite C1 overlap tensors used for the Route-C response."
            ),
            "proof_obligations": [
                "Define alpha1 as a same-branch deformation of the selected source.",
                "Compute dotD_alpha1 matrices in the emitted B_N basis.",
                "Prove horizontal gauge and reduced Green equations.",
                "Emit primitive C1 overlap contractions and Hessian/source blocks.",
                "Prove no benchmark masses, CKM/PMNS, or observed constants enter selection.",
            ],
            "safe_wording": (
                "dotD and C1 response should not be promoted until alpha1_driver_verified and selected_dotD_source_verified are theorem-derived."
            ),
        },
        {
            "id": "I6_parameter_policy_appendix_update",
            "status": "PAPER_SECTION_REQUIRED",
            "target_papers": ["parameters_falsifiability", "theta_superset"],
            "section_title": "Diagnostic Lifts, Superset Repairs, and Theorem-Derived Flags",
            "current_blockers_resolved_if_proved": [
                "global wording discipline for diagnostic lifts",
                "no-knob credibility policy",
                "formal-lift guardrail",
            ],
            "theorem_statement": (
                "A candidate may pass diagnostic lifted-flag validators only as algebraic consistency evidence; proof promotion requires an explicitly cited theorem that derives the selected flags from MTT source data."
            ),
            "proof_obligations": [
                "Define diagnostic lift, superset convergence, superset repair, and straight proof.",
                "State which flags require theorem derivation.",
                "Require every promoted flag to cite a named theorem and reproducible artifact.",
                "Forbid observed constants as source selectors.",
                "Add falsifier templates for selected-source promotion failures.",
            ],
            "safe_wording": (
                "Diagnostic success is not proof; it identifies exactly which theorem insertion is missing."
            ),
        },
    ]

    candidate = {
        "candidate": "MTTSelectedSourcePaperIntegrationManifest",
        "status": "MTT_SELECTED_SOURCE_PAPER_INTEGRATION_MANIFEST_BUILT_INSERTIONS_OPEN",
        "papers": PAPERS,
        "insertions": insertions,
        "global_rules": {
            "do_not_set_selected_flags_without_named_theorem": True,
            "diagnostic_lifts_are_algebraic_smoke_tests_only": True,
            "observed_data_cannot_select_sources": True,
            "paper_updates_must_extend_claims_conservatively": True,
            "proof_obligations_must_be_executable_or_citable": True,
        },
        "what_closes_now": {
            "not_theorem_derived_caveats_mapped_to_paper_insertions": True,
            "target_papers_identified": True,
            "proof_obligations_listed": True,
            "safe_wording_supplied": True,
            "formal_lift_guardrail_exported_to_papers": True,
        },
        "what_remains_open": {
            "actual_paper_text_inserted": True,
            "theorem_proofs_written": True,
            "selected_source_flags_promoted": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_Source_Paper_Appendix_Drafts_v1",
    }

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(
        json.dumps(
            {
                "status": candidate["status"],
                "candidate_path": rel(OUTPUT),
                "note_path": rel(NOTE),
                "what_closes": candidate["what_closes_now"],
                "what_remains_open": candidate["what_remains_open"],
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )

    rows = []
    for item in insertions:
        rows.append(
            f"## {item['id']}\n\n"
            f"Target papers: {', '.join(item['target_papers'])}\n\n"
            f"Section title: **{item['section_title']}**\n\n"
            f"Theorem slot: {item['theorem_statement']}\n\n"
            "Proof obligations:\n"
            + "\n".join(f"- {entry}" for entry in item["proof_obligations"])
            + "\n\n"
            f"Safe wording: {item['safe_wording']}\n"
        )

    NOTE.write_text(
        "# MTT Selected Source Paper Integration Manifest\n\n"
        f"Status: `{candidate['status']}`\n\n"
        "Every current `not theorem-derived` or `selected_source_verified=false` blocker must become a named paper insertion, not a loose caveat.  "
        "This manifest maps those blockers to theorem sections, target papers, proof obligations, and conservative wording.\n\n"
        "Global rule: diagnostic lifted flags can prove algebraic consistency only.  Promotion requires a named theorem deriving the selected flags from MTT source data.\n\n"
        + "\n\n".join(rows)
        + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": candidate["status"]}, indent=2))


if __name__ == "__main__":
    main()
