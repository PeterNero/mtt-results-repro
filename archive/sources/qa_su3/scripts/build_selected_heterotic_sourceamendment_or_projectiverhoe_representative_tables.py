"""Build source-amendment or projective rho_E representative-table gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "sourcefill": DATA / "selected_heterotic_typedmaptables_or_projectiverhoetables_sourcefill.candidate.json",
    "missing_leaves": DATA / "selected_heterotic_typedmaptables_or_projectiverhoetables_missing_leaves.json",
    "finite_galerkin_packet": DATA / "hessian_kernel_central_cocycle_finite_galerkin_candidate.packet.json",
    "ctwist_template": DATA / "ctwist_deligne_cech_template.candidate.json",
    "gerbe_twist": DATA / "gerbe_twist_cancellation_packet.candidate.json",
    "central_search": DATA / "central_cocycle_map_source_search_or_derivation.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_sourceamendment_or_projectiverhoe_representative_tables.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_sourceamendment_or_projectiverhoe_representative_tables_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_SourceAmendment_or_ProjectiveRhoE_RepresentativeTables_v1.md"
OUTPUT_TEMPLATE = DATA / "selected_heterotic_projectiverhoe_smooth_promotion.template.json"

STATUS = "HETEROTIC_SOURCEAMENDMENT_PROJECTIVERHOE_REPRESENTATIVE_TABLES_FINITE_CANDIDATE_PROMOTION_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_FiniteCandidate_PromotionOrSmoothRepresentative_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    sourcefill = load(INPUTS["sourcefill"])
    missing = load(INPUTS["missing_leaves"])
    finite = load(INPUTS["finite_galerkin_packet"])
    template = load(INPUTS["ctwist_template"])
    gerbe_twist = load(INPUTS["gerbe_twist"])
    central = load(INPUTS["central_search"])

    typed_missing_count = len(missing["typed_missing"])
    projective_missing_count = len(missing["projective_missing"])

    projective_tables = {
        "scope": "finite_Galerkin_projective_representative_candidate",
        "source_identity": finite["source_identity"],
        "twist_projection": finite["twist_projection"],
        "tau_extraction": finite["tau_extraction"],
        "projective_rhoE": finite["response_payload"]["projective_rhoE"],
        "finite_response": finite["response_payload"],
        "admissibility": finite["admissibility"],
        "retarded_kernel": finite["retarded_kernel"],
        "fills_finite_candidate_leaves": {
            "period_denominator_or_smooth_unit": finite["tau_extraction"]["period_denominator_or_smooth_unit"],
            "representative_to_central_cocycle_map": finite["tau_extraction"]["extraction_formula"],
            "central_cocycle_law_checked": finite["tau_extraction"]["cocycle_law_checked"],
            "nontrivial_central_twist": True,
            "rho_E_central_character": finite["response_payload"]["projective_rhoE"]["central_character"],
            "tau_values": finite["response_payload"]["projective_rhoE"]["tau_values"],
            "D_E": finite["response_payload"]["D_E"],
            "Green_operator": finite["response_payload"]["Green_operator"],
            "Riesz_projector": finite["response_payload"]["Riesz_projector"],
            "dotD": finite["response_payload"]["dotD"],
            "finite_part": finite["response_payload"]["heat_zeta_or_torsion_finite_part"],
            "trace_normalization": finite["response_payload"]["trace_normalization"],
        },
        "does_not_fill_smooth_heterotic_leaves": {
            "selected_Deligne_Cech_or_B_field_representative": None,
            "local_B_i_A_ij_g_ijk": template["required_source_values"],
            "rho_E_generator_or_boundary_matrices_as_transition_tables": None,
            "metric_or_unitarity_compatibility_on_smooth_bundle": None,
            "mapped_Freed_Witten_for_smooth_Qa_SU3_module": False,
            "Green_Schwarz_Bianchi_for_mapped_smooth_module": "FINITE_CONTEXT_ONLY",
            "twisted_projector_retains_smooth_sector": False,
            "same_source_smooth_operator_identity": False,
        },
    }

    typed_source_amendment_contract = {
        "scope": "ordinary_or_nil_theta_typed_map_source_amendment",
        "reason_kept_live": "typed lane remains the most direct End(E) domain route if the corpus is amended with actual nil-theta automorphy and sections",
        "required_first_tables": [
            "explicit compact Iwasawa good cover or finite quotient domain",
            "lattice generator action on H_3(C)",
            "charge-to-factor map q -> a_q(gamma,z)",
            "factor-of-automorphy cocycle check",
            "section bases and dimensions for F1..F5,G1..G5,P",
            "multiplication constants F_i times G_i -> P",
            "typed f,g coefficients and machine g o f = 0",
            "local freeness/exactness certificate",
            "End(E) cochain/harmonic basis and trace/shared-line policy",
        ],
        "current_missing_count": typed_missing_count,
        "can_be_shortcut_by_generic_constant_maps": False,
    }

    smooth_promotion_template = {
        "schema": "SelectedHeteroticProjectiveRhoESmoothPromotion.v1",
        "finite_candidate_path": rel(INPUTS["finite_galerkin_packet"]),
        "must_supply": {
            "smooth_or_finite_source_selection_theorem": None,
            "selected_Deligne_Cech_or_B_field_representative": None,
            "local_B_i": None,
            "overlap_A_ij": None,
            "triple_overlap_g_ijk": None,
            "map_to_tau_equals_finite_candidate": None,
            "rho_E_transition_or_boundary_matrices": None,
            "metric_or_unitarity_compatibility": None,
            "Freed_Witten_check": None,
            "Green_Schwarz_Bianchi_check": None,
            "projector_retention_check": None,
            "same_source_operator_identity_to_finite_response": None,
        },
        "finite_candidate_values_to_replay": projective_tables["fills_finite_candidate_leaves"],
        "forbidden_promotions": [
            "finite Galerkin tau as smooth Deligne representative without source theorem",
            "central character as full rho_E transition matrices without generator/boundary tables",
            "finite Bianchi/Freed-Witten wording as mapped smooth admissibility",
            "q79/S3 Deligne values as Qa/SU3 source values",
        ],
    }

    decision = {
        "repair_gate_built": True,
        "primary_next_lane": "projective_rhoE_finite_candidate_promotion_or_smooth_representative",
        "why_primary": (
            "The finite Galerkin packet already emits tau, period unit, central character, "
            "D_E, Green/Riesz, dotD, and finite trace. The typed lane still lacks the "
            "automorphy/section-ring tables needed before f,g can be checked."
        ),
        "finite_projective_candidate_built": True,
        "smooth_heterotic_representative_emitted": False,
        "rho_E_transition_tables_emitted": False,
        "same_source_smooth_operator_identity_proved": False,
        "typed_source_amendment_filled": False,
        "EndE_to_BN_functor_filled": False,
        "E_Qa_computed": False,
        "threshold_value_computed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "SelectedHeteroticSourceAmendmentOrProjectiveRhoERepresentativeTables",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "sourcefill": sourcefill["status"],
            "finite_galerkin_packet": finite["status"],
            "ctwist_template": template["status"],
            "gerbe_twist": gerbe_twist["status"],
            "central_search": central["status"],
        },
        "repair_comparison": {
            "typed_missing_count": typed_missing_count,
            "projective_missing_count": projective_missing_count,
            "projective_has_finite_candidate_response": True,
            "typed_has_f_g_tables": False,
            "selected_primary_lane": decision["primary_next_lane"],
        },
        "projective_representative_tables": projective_tables,
        "typed_source_amendment_contract": typed_source_amendment_contract,
        "smooth_promotion_template_path": rel(OUTPUT_TEMPLATE),
        "decision": decision,
        "guardrails": {
            "does_not_claim_smooth_Deligne_representative": True,
            "does_not_claim_rhoE_transition_matrices": True,
            "does_not_claim_smooth_admissibility": True,
            "does_not_claim_EndE_to_BN": True,
            "does_not_compute_E_Qa": True,
            "does_not_compute_threshold_value": True,
            "does_not_use_observed_data": True,
            "does_not_target_fit": True,
        },
        "theorem": {
            "name": "HeteroticFiniteProjectiveRhoERepresentativeCandidateSelection",
            "proved": True,
            "statement": (
                "Among the currently legal repairs, the projective rho_E lane is the "
                "first executable lane because a same-branch finite Galerkin packet "
                "already emits tau, period unit, central character, finite D_E, Green/"
                "Riesz, dotD, and finite trace. This proves a finite representative "
                "candidate and a precise smooth-promotion contract, but it does not "
                "yet emit a smooth heterotic Deligne/Cech/B-field representative, "
                "rho_E transition matrices, or a same-source smooth operator identity."
            ),
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_TEMPLATE.write_text(json.dumps(smooth_promotion_template, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "smooth_promotion_template_path": rel(OUTPUT_TEMPLATE),
        "finite_projective_candidate_built": True,
        "primary_next_lane": decision["primary_next_lane"],
        "smooth_heterotic_representative_emitted": False,
        "rho_E_transition_tables_emitted": False,
        "same_source_smooth_operator_identity_proved": False,
        "typed_source_amendment_filled": False,
        "EndE_to_BN_functor_filled": False,
        "E_Qa_computed": False,
        "threshold_value_computed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic SourceAmendment or ProjectiveRhoE RepresentativeTables v1

## Result

```text
status = {STATUS}
primary_next_lane = {decision["primary_next_lane"]}
finite_projective_candidate_built = true
smooth_heterotic_representative_emitted = false
rho_E_transition_tables_emitted = false
same_source_smooth_operator_identity_proved = false
next_required_artifact = {NEXT}
```

## What Is New

The finite Galerkin Hessian/kernel packet is now explicitly promoted to the
primary repair candidate, but only at finite-candidate scope. It supplies:

- selected `tau` by `Pi_tw = +e3`;
- primitive integer c-period unit;
- central-character `rho_E` candidate on the module labels;
- finite `D_E`, Green, Riesz, `dotD`, trace, and finite-part payload.

## Boundary

This does not yet supply the smooth heterotic Deligne/Cech/B-field
representative, local transition matrices, smooth admissibility checks, or the
same-source smooth operator identity. Those are collected in:

```text
{rel(OUTPUT_TEMPLATE)}
```

## Typed Lane

The typed source-amendment lane remains live, but it still needs nil-theta or
automorphy/section-ring source data before selected `f,g` tables can become
machine-checkable values.
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_TEMPLATE)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
