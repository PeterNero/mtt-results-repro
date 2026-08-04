"""Try the smooth-source theorem or direct finite-operator closure routes."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "promotion_attempt": DATA / "selected_heterotic_projectiverhoe_finitecandidate_promotion_or_smoothrepresentative.candidate.json",
    "promotion_obligations": DATA / "selected_heterotic_projectiverhoe_promotion_obligations.json",
    "gr_internal_separation": DATA / "gr_surface_internal_quantum_separation_theorem.candidate.json",
    "chi_qa": DATA / "selected_response_functional_chi_qa.candidate.json",
    "bundle_direct_gate": DATA / "selected_heterotic_bundle_curvature_trace_or_direct_operator_gate.candidate.json",
    "ctwist_source_search": DATA / "ctwist_source_value_search.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_smoothsourcetheorem_or_directfiniteoperatorclosure.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_smoothsourcetheorem_or_directfiniteoperatorclosure_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_SmoothSourceTheorem_or_DirectFiniteOperatorClosure_v1.md"
OUTPUT_CONTRACT = DATA / "selected_heterotic_projectiverhoe_source_selection_theorem_contract.json"

STATUS = "HETEROTIC_PROJECTIVERHOE_SMOOTHSOURCE_OR_DIRECTFINITE_CLOSURE_REDUCED_SOURCE_SELECTION_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_SourceSelectionTheorem_or_DirectOperatorIdentity_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    promotion = load(INPUTS["promotion_attempt"])
    obligations = load(INPUTS["promotion_obligations"])
    gr_sep = load(INPUTS["gr_internal_separation"])
    chi_qa = load(INPUTS["chi_qa"])
    direct_gate = load(INPUTS["bundle_direct_gate"])
    ct_source = load(INPUTS["ctwist_source_search"])

    finite = promotion["finite_candidate_replay"]

    lane_a = {
        "lane": "finite_quotient_source_selection_theorem",
        "support": {
            "gr_internal_quantum_separation_accepts_finite_internal_packet": (
                gr_sep["decision"]["internal_reduced_Qa_SU3_determinant"] == "CLOSED_LOG_2008"
            ),
            "chi_Qa_selected_finite_response_closed": chi_qa["decision"]["selected_chi_Qa"] == "1",
            "finite_tau_DE_Green_Riesz_dotD_available": promotion["fill_result"]["finite_tau_period_rhoE_DE_response_available"],
            "no_observed_data_used": not promotion["target_fitting_used"] and not chi_qa["target_fitting_used"],
        },
        "blocks": {
            "finite_candidate_identified_as_selected_heterotic_projective_rhoE_source": False,
            "source_selection_theorem_names_this_projective_rhoE_packet": False,
            "admissibility_promoted_from_finite_context_to_selected_response": False,
            "EndE_to_BN_or_heterotic_threshold_functor_identity": False,
        },
        "closes_now": False,
        "verdict": "PARTIAL_FINITE_RESPONSE_SUPPORT_NOT_HETEROTIC_RHOE_SOURCE_SELECTION",
    }

    lane_b = {
        "lane": "smooth_Deligne_Cech_B_field_representative",
        "support": {
            "strominger_fixed_differential_class_partial": ct_source["value_candidates"][1]["promotion_status"],
            "iwasawa_quantized_gerbe_partial": ct_source["value_candidates"][2]["promotion_status"],
            "q79_flat_values_guardrail": ct_source["value_candidates"][0]["promotion_status"],
        },
        "blocks": {
            "same_branch_Qa_SU3_values_found": ct_source["gate_results"]["same_branch_Qa_SU3_values_found"],
            "same_branch_tau_maps_to_required_c_twists": ct_source["gate_results"]["same_branch_tau_maps_to_required_c_twists"],
            "Freed_Witten_Bianchi_verified_for_Qa_SU3": ct_source["gate_results"]["Freed_Witten_Bianchi_verified_for_Qa_SU3"],
            "local_B_i_A_ij_g_ijk_emitted": False,
        },
        "closes_now": False,
        "verdict": "SMOOTH_REPRESENTATIVE_NOT_EMITTED",
    }

    direct_required = direct_gate["routes"]["B_direct_finite_operator"]["required_payload"]
    lane_c = {
        "lane": "direct_same_source_finite_operator_closure",
        "support": {
            "finite_candidate_values": finite,
            "bundle_direct_gate_written": direct_gate["what_closes_now"]["direct_operator_acceptance_contract_written"],
            "direct_gate_support": direct_gate["routes"]["B_direct_finite_operator"]["support"],
        },
        "required_payload": direct_required,
        "blocks": {
            "direct_operator_emission_found": direct_gate["routes"]["B_direct_finite_operator"]["support"]["direct_operator_emission_found"],
            "source_certificate_found": direct_gate["routes"]["B_direct_finite_operator"]["support"]["source_certificate_found"],
            "selected_bundle_connection_A": direct_gate["what_remains_open"]["selected_bundle_connection_A"],
            "E_Qa_or_direct_finite_operator": direct_gate["what_remains_open"]["E_Qa_or_direct_finite_operator"],
            "finite_heat_zeta_torsion_part": direct_gate["what_remains_open"]["finite_heat_zeta_torsion_part"],
        },
        "closes_now": False,
        "verdict": "DIRECT_OPERATOR_ACCEPTANCE_CONTRACT_EXISTS_VALUES_OPEN",
    }

    contract = {
        "schema": "SelectedHeteroticProjectiveRhoESourceSelectionTheoremContract.v1",
        "status": "OPEN",
        "must_prove_one_of": {
            "finite_physical_quotient_selection": [
                "the selected heterotic Qa/SU3 projective response domain is exactly the finite Galerkin quotient labels F_i,G_i,P",
                "the physical quotient removes all smooth/GR/universal complement modes before the heterotic threshold response",
                "the finite tau/rho_E/D_E/Green/Riesz/dotD packet is the selected response, not only a validator candidate",
                "finite admissibility and trace convention are theorem-derived for this heterotic threshold source",
            ],
            "smooth_representative_map": [
                "emit selected Deligne/Cech/B-field local data",
                "prove its DD/tau class maps to the finite tau table",
                "emit rho_E transition/boundary matrices and metric compatibility",
                "verify mapped Freed-Witten, Green-Schwarz/Bianchi, and projector retention",
            ],
            "direct_operator_identity": [
                "emit the selected source certificate for the heterotic bundle/twist",
                "emit the direct finite operator packet with rho_E or D_E action",
                "emit Riesz/gap, Green, dotD, E_Qa or zero-order block",
                "emit finite heat/zeta/torsion determinant convention and trace weights",
            ],
        },
        "finite_values_available": finite,
        "forbidden_shortcuts": obligations["forbidden_promotions"],
    }

    decision = {
        "three_lane_attempt_executed": True,
        "finite_response_support_reused": True,
        "finite_physical_quotient_selection_proved": False,
        "smooth_representative_emitted": False,
        "direct_finite_operator_closure_proved": False,
        "source_selection_theorem_contract_written": True,
        "EndE_to_BN_functor_filled": False,
        "E_Qa_computed": False,
        "threshold_value_computed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoESmoothSourceTheoremOrDirectFiniteOperatorClosure",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "promotion_attempt": promotion["status"],
            "gr_internal_separation": gr_sep["status"],
            "chi_qa": chi_qa["status"],
            "bundle_direct_gate": direct_gate["status"],
            "ctwist_source_search": ct_source["status"],
        },
        "lane_a_finite_quotient": lane_a,
        "lane_b_smooth_representative": lane_b,
        "lane_c_direct_operator": lane_c,
        "source_selection_theorem_contract_path": rel(OUTPUT_CONTRACT),
        "decision": decision,
        "guardrails": {
            "does_not_treat_chi_Qa_as_rhoE_source_selection": True,
            "does_not_treat_GR_separation_as_heterotic_operator_identity": True,
            "does_not_promote_structural_gerbe_context": True,
            "does_not_promote_q79_values": True,
            "does_not_compute_E_Qa": True,
            "does_not_compute_threshold_value": True,
            "does_not_use_observed_data": True,
            "does_not_target_fit": True,
        },
        "theorem": {
            "name": "HeteroticProjectiveRhoESmoothSourceOrDirectFiniteClosureReduction",
            "proved": True,
            "statement": (
                "The finite Qa/SU3 response support is strong enough to define the exact "
                "source-selection theorem contract, but it does not by itself prove the "
                "heterotic projective rho_E source identity. The smooth representative "
                "and direct finite operator lanes also remain open. Therefore the next "
                "single frontier is to prove one source-selection theorem or direct "
                "operator identity, without importing q79 values or observed data."
            ),
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_CONTRACT.write_text(json.dumps(contract, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "source_selection_theorem_contract_path": rel(OUTPUT_CONTRACT),
        "three_lane_attempt_executed": True,
        "finite_response_support_reused": True,
        "finite_physical_quotient_selection_proved": False,
        "smooth_representative_emitted": False,
        "direct_finite_operator_closure_proved": False,
        "source_selection_theorem_contract_written": True,
        "EndE_to_BN_functor_filled": False,
        "E_Qa_computed": False,
        "threshold_value_computed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE SmoothSourceTheorem or DirectFiniteOperatorClosure v1

## Result

```text
status = {STATUS}
finite_response_support_reused = true
finite_physical_quotient_selection_proved = false
smooth_representative_emitted = false
direct_finite_operator_closure_proved = false
next_required_artifact = {NEXT}
```

## Reduction

The finite response support is now strong: GR/internal separation, `chi_Qa=1`,
and the finite projective `rho_E` packet all point to the same finite internal
response. But none of those artifacts proves the missing heterotic source
identity by itself.

The next theorem contract is written here:

```text
{rel(OUTPUT_CONTRACT)}
```

One of three things must now be proved:

- finite Galerkin quotient is the selected heterotic projective response;
- smooth Deligne/Cech/B-field representative maps to the finite `tau`;
- direct finite operator identity emits the selected `rho_E/D_E` response.
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_CONTRACT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
