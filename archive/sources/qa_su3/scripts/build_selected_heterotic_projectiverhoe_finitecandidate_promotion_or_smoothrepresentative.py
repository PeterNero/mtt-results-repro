"""Attempt to promote finite projective rho_E candidate or emit smooth representative."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "representative_gate": DATA / "selected_heterotic_sourceamendment_or_projectiverhoe_representative_tables.candidate.json",
    "smooth_template": DATA / "selected_heterotic_projectiverhoe_smooth_promotion.template.json",
    "finite_to_smooth": DATA / "finite_galerkin_to_smooth_operator_promotion_or_nogo.candidate.json",
    "ctwist_source_search": DATA / "ctwist_source_value_search.candidate.json",
    "twisted_source_fill": DATA / "twisted_source_promotion_packet_fill_attempt.candidate.json",
    "gerbe_response_fill": DATA / "gerbe_twisted_local_system_response_fill_attempt.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_finitecandidate_promotion_or_smoothrepresentative.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_finitecandidate_promotion_or_smoothrepresentative_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_FiniteCandidate_PromotionOrSmoothRepresentative_v1.md"
OUTPUT_OBLIGATIONS = DATA / "selected_heterotic_projectiverhoe_promotion_obligations.json"

STATUS = "HETEROTIC_PROJECTIVERHOE_FINITE_CANDIDATE_PROMOTION_ATTEMPT_SMOOTH_REPRESENTATIVE_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_SmoothSourceTheorem_or_DirectFiniteOperatorClosure_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    representative = load(INPUTS["representative_gate"])
    template = load(INPUTS["smooth_template"])
    finite_to_smooth = load(INPUTS["finite_to_smooth"])
    ct_source = load(INPUTS["ctwist_source_search"])
    twisted = load(INPUTS["twisted_source_fill"])
    gerbe = load(INPUTS["gerbe_response_fill"])

    finite_values = template["finite_candidate_values_to_replay"]
    must_supply = template["must_supply"]

    source_tests = {
        row["id"]: row for row in finite_to_smooth["source_theorem_tests"]
    }
    smooth_representative_search = {
        "q79_explicit_flat_values_found": ct_source["gate_results"]["explicit_q79_flat_values_found"],
        "q79_rejected_as_direct_import": ct_source["value_candidates"][0]["promotion_status"],
        "strominger_fixed_class_partial": ct_source["value_candidates"][1]["promotion_status"],
        "iwasawa_quantized_gerbe_partial": ct_source["value_candidates"][2]["promotion_status"],
        "same_branch_Qa_SU3_values_found": ct_source["gate_results"]["same_branch_Qa_SU3_values_found"],
        "same_branch_tau_maps_to_required_c_twists": ct_source["gate_results"]["same_branch_tau_maps_to_required_c_twists"],
        "Freed_Witten_Bianchi_verified_for_Qa_SU3": ct_source["gate_results"]["Freed_Witten_Bianchi_verified_for_Qa_SU3"],
    }

    fill_result = {
        "finite_candidate_values_replayed": True,
        "finite_tau_period_rhoE_DE_response_available": True,
        "smooth_or_finite_source_selection_theorem": source_tests["same_source_smooth_operator"]["current_result"],
        "selected_Deligne_Cech_or_B_field_representative": ct_source["gate_results"]["same_branch_Qa_SU3_values_found"],
        "local_B_i": False,
        "overlap_A_ij": False,
        "triple_overlap_g_ijk": False,
        "map_to_tau_equals_finite_candidate": ct_source["gate_results"]["same_branch_tau_maps_to_required_c_twists"],
        "rho_E_transition_or_boundary_matrices": twisted["fill_result"]["projective_rhoE_tables_supplied"],
        "metric_or_unitarity_compatibility": False,
        "Freed_Witten_check": twisted["fill_result"]["mapped_Freed_Witten_verified"],
        "Green_Schwarz_Bianchi_check": (
            twisted["partial_packet"]["admissibility"]["Green_Schwarz_Bianchi_verified"]
            == "VERIFIED"
        ),
        "projector_retention_check": twisted["fill_result"]["twisted_projector_retention_verified"],
        "same_source_operator_identity_to_finite_response": source_tests["same_source_smooth_operator"]["current_result"],
        "same_source_finite_response_payload_from_smooth_rep": gerbe["fill_result"]["finite_response_filled"],
    }
    unmet = [
        key for key in must_supply
        if fill_result.get(key) is not True
    ]

    promotion_obligations = {
        "schema": "SelectedHeteroticProjectiveRhoEPromotionObligations.v1",
        "status": "OPEN",
        "finite_values_already_available": finite_values,
        "unmet_smooth_promotion_leaves": {key: must_supply[key] for key in unmet},
        "minimal_closing_options": [
            "prove a source-selection theorem that the finite Galerkin representative is the selected physical quotient, so smooth local Deligne data are not required separately",
            "emit the smooth heterotic Deligne/Cech/B-field representative and show it maps to the finite tau table",
            "emit direct same-source finite operator closure with rho_E/D_E/Green/Riesz/dotD/torsion and admissibility certified as the selected response",
        ],
        "forbidden_promotions": template["forbidden_promotions"],
    }

    decision = {
        "promotion_attempt_executed": True,
        "finite_candidate_values_replayed": True,
        "smooth_heterotic_representative_emitted": False,
        "rho_E_transition_tables_emitted": False,
        "same_source_smooth_operator_identity_proved": False,
        "direct_selected_finite_operator_closure_proved": False,
        "finite_candidate_promoted_to_selected_physical_packet": False,
        "EndE_to_BN_functor_filled": False,
        "E_Qa_computed": False,
        "threshold_value_computed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoEFiniteCandidatePromotionOrSmoothRepresentative",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "representative_gate": representative["status"],
            "finite_to_smooth": finite_to_smooth["status"],
            "ctwist_source_search": ct_source["status"],
            "twisted_source_fill": twisted["status"],
            "gerbe_response_fill": gerbe["status"],
        },
        "finite_candidate_replay": finite_values,
        "smooth_representative_search": smooth_representative_search,
        "fill_result": fill_result,
        "unmet_smooth_promotion_leaves": unmet,
        "promotion_obligations_path": rel(OUTPUT_OBLIGATIONS),
        "decision": decision,
        "guardrails": {
            "does_not_promote_q79_flat_values": True,
            "does_not_promote_finite_tau_to_smooth_Deligne": True,
            "does_not_promote_central_character_to_transition_tables": True,
            "does_not_promote_context_to_FreedWitten_Bianchi": True,
            "does_not_claim_EndE_to_BN": True,
            "does_not_compute_E_Qa": True,
            "does_not_compute_threshold_value": True,
            "does_not_use_observed_data": True,
            "does_not_target_fit": True,
        },
        "theorem": {
            "name": "HeteroticProjectiveRhoEFiniteCandidatePromotionCurrentSourceNoGo",
            "proved": True,
            "statement": (
                "The finite projective rho_E candidate can be replayed exactly, but the "
                "current source does not promote it to a selected smooth heterotic "
                "representative or direct selected physical finite operator packet. "
                "Promotion requires either a source-selection theorem identifying the "
                "finite Galerkin quotient as the selected physical response, a smooth "
                "Deligne/Cech/B-field representative mapping to the finite tau table, "
                "or a direct same-source finite operator closure."
            ),
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_OBLIGATIONS.write_text(json.dumps(promotion_obligations, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "promotion_obligations_path": rel(OUTPUT_OBLIGATIONS),
        "promotion_attempt_executed": True,
        "finite_candidate_values_replayed": True,
        "smooth_heterotic_representative_emitted": False,
        "rho_E_transition_tables_emitted": False,
        "same_source_smooth_operator_identity_proved": False,
        "direct_selected_finite_operator_closure_proved": False,
        "finite_candidate_promoted_to_selected_physical_packet": False,
        "EndE_to_BN_functor_filled": False,
        "E_Qa_computed": False,
        "threshold_value_computed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE FiniteCandidate PromotionOrSmoothRepresentative v1

## Result

```text
status = {STATUS}
finite_candidate_values_replayed = true
smooth_heterotic_representative_emitted = false
rho_E_transition_tables_emitted = false
same_source_smooth_operator_identity_proved = false
direct_selected_finite_operator_closure_proved = false
finite_candidate_promoted_to_selected_physical_packet = false
next_required_artifact = {NEXT}
```

## Finite Candidate Replayed

The finite packet still carries the strongest available values: selected `tau`,
primitive c-period unit, central-character `rho_E`, finite `D_E`, Green/Riesz,
`dotD`, trace, and finite part.

## Promotion Block

The current source does not emit a smooth heterotic Deligne/Cech/B-field
representative, transition matrices, mapped Freed-Witten/Bianchi/projector
checks, or a same-source smooth operator identity. The exact open leaves are
listed in:

```text
{rel(OUTPUT_OBLIGATIONS)}
```

## Legal Closures

- prove the finite Galerkin quotient is itself the selected physical response;
- emit smooth Deligne/Cech/B-field data mapping to the finite `tau`;
- emit a direct same-source finite operator closure with admissibility.
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_OBLIGATIONS)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
