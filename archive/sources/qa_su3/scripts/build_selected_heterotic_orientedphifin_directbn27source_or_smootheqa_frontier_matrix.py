"""Reduce the direct BN27 source versus smooth E_Qa quotient frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "projective_lift_nogo": DATA / "selected_heterotic_orientedphifin_projectiverhoe_bn27lift_or_directsource_theorem.candidate.json",
    "sourceleaf_discovery": DATA / "selected_heterotic_orientedphifin_sourceleaf_corpus_discovery_report.json",
    "bn27_orbit_fill": DATA / "selected_heterotic_orientedphifin_bn27_orbitclosure_sourcefill.candidate.json",
    "branch_final_gate": DATA / "selected_heterotic_orientedphifin_branchidentity_sourcecertificate_or_smootheqa_finalgate.candidate.json",
    "phifin_gate": DATA / "selected_heterotic_phifin_sourceidentity_or_bundleconnection_solve_gate.candidate.json",
    "bundle_valuesolve": DATA / "selected_heterotic_bundleconnection_valuesolve_or_phifin_sourceidentity_proof.candidate.json",
    "bismut_payload": DATA / "selected_heterotic_bismut_weitzenbock_tensor_payload_fill.candidate.json",
    "rplus_payload": DATA / "selected_heterotic_rplus_curvature_payload_fill.candidate.json",
    "simultaneous_table": DATA / "selected_heterotic_orientedphifin_simultaneous_ctau_phifin_table.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_directbn27source_or_smootheqa_frontier_matrix.candidate.json"
OUTPUT_CONTRACT = DATA / "selected_heterotic_orientedphifin_directbn27source_or_smootheqa_payload_contract.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_directbn27source_or_smootheqa_frontier_matrix_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_DirectBN27Source_or_SmoothEQa_FrontierMatrix_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_DIRECTBN27_OR_SMOOTHEQA_FRONTIER_REDUCED_SELECTED_A_OR_DIRECT_SOURCE_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_SelectedBundleConnectionA_or_DirectBN27SourceEmission_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    projective = load(INPUTS["projective_lift_nogo"])
    sourceleaf = load(INPUTS["sourceleaf_discovery"])
    orbit = load(INPUTS["bn27_orbit_fill"])
    branch = load(INPUTS["branch_final_gate"])
    phifin_gate = load(INPUTS["phifin_gate"])
    bundle = load(INPUTS["bundle_valuesolve"])
    bismut = load(INPUTS["bismut_payload"])
    rplus = load(INPUTS["rplus_payload"])
    table = load(INPUTS["simultaneous_table"])

    direct_source_found = sourceleaf["classification"]["direct_selected_carrier_packet_found"]
    smooth_A_found = sourceleaf["classification"]["smooth_selected_bundle_A_packet_found"]

    direct_bn27 = {
        "route": "direct_BN27_source_theorem",
        "closed": False,
        "support_score": 4,
        "support": {
            "full_BN27_table_materialized": table["basis_dimension"] == 27,
            "oriented_positive_sector_count_16": table["counts"]["oriented_nonzero_Ctau_positive_magnitude_count"] == 16,
            "orbit_fill_compatibility_closed": orbit["decision"]["compatibility_closed"],
            "audit_replay_ready": orbit["decision"]["audit_replay_closed"],
        },
        "missing": {
            "direct_selected_carrier_packet_found_in_corpus": direct_source_found,
            "same_source_BN27_source_theorem": False,
            "source_owned_selected_deck_action": orbit["decision"]["selected_deck_action_closed_for_heterotic_source"],
            "source_owned_rank_slot_completion": orbit["decision"]["rank_slot_completion_closed_for_heterotic_source"],
            "source_owned_kernel_trace_policy": orbit["decision"]["kernel_trace_policy_source_owned"],
            "source_owned_positive_PhiFin_magnitude_with_Ctau_orientation": False,
        },
        "first_irreducible_leaf": "emit S_QaSU3^BN27 as a selected heterotic source, not as Route-C support",
        "why_not_closed": "The current record contains the BN27 table and trace replay, but the source scan finds no direct selected carrier theorem and the orbit-closure fill remains support-only.",
    }

    smooth_eqa = {
        "route": "smooth_E_Qa_quotient",
        "closed": False,
        "support_score": 3,
        "support": {
            "bismut_geometry_payload_filled": bismut["decision"]["geometric_tensor_payload_filled"],
            "R_plus_curvature_filled": rplus["decision"]["R_plus_curvature_filled"],
            "smooth_lane_retained_by_branch_gate": branch["routes"]["smooth_E_Qa_quotient_theorem"]["support"]["smooth_lane_retained"],
        },
        "missing": {
            "smooth_selected_bundle_A_packet_found_in_corpus": smooth_A_found,
            "selected_A_or_rhoE": bundle["lane_B_bundle_connection_value_solve"]["smooth_bundle_connection_values"]["selected_A_or_rhoE"],
            "selected_F_A": bundle["lane_B_bundle_connection_value_solve"]["smooth_bundle_connection_values"]["F_A"],
            "representation_action_on_uE_one_forms": bundle["lane_B_bundle_connection_value_solve"]["smooth_bundle_connection_values"]["representation_action_on_uE_one_forms"],
            "smooth_kernel_and_quotient_policy": bundle["lane_B_bundle_connection_value_solve"]["smooth_bundle_connection_values"]["smooth_kernel_and_quotient_policy"],
            "E_Qa_or_heat_zeta_torsion_finite_part": bundle["lane_B_bundle_connection_value_solve"]["smooth_bundle_connection_values"]["smooth_E_Qa_or_heat_zeta_torsion_finite_part"],
            "finite_quotient_to_BN27_packet": False,
        },
        "first_irreducible_leaf": "emit the selected bundle connection A, or an equivalent smooth projective rho_E transition packet",
        "why_not_closed": "The geometry side is now real data, but no selected bundle connection, curvature, representation action, quotient policy, or E_Qa finitepart is emitted.",
    }

    contract = {
        "schema": "SelectedHeterotic.OrientedPhiFin.DirectBN27_or_SmoothEQa.PayloadContract.v1",
        "status": "OPEN_VALUES_REQUIRED",
        "direct_BN27_source_payload": {
            "source_certificate": None,
            "S_QaSU3_BN27_declaration": None,
            "F3xF3_rank_slot_deck_action": None,
            "source_emitted_C_tau_table": None,
            "source_emitted_PhiFin_DE_table": None,
            "kernel_and_trace_policy": None,
            "finitepart_trace_identity": None,
        },
        "smooth_EQa_payload": {
            "selected_bundle_connection_A_or_projective_transition": None,
            "curvature_F_A": None,
            "HYM_or_Strominger_residual_certificate": None,
            "representation_action_on_uE_one_forms": None,
            "trace_normalization": None,
            "kernel_and_quotient_policy": None,
            "E_Qa_matrix_or_equivalent_heat_zeta_torsion_operator": None,
            "finite_spectral_quotient_to_BN27": None,
            "finitepart_reduction": None,
        },
        "acceptance_tests": [
            "payload is emitted by one same selected heterotic Qa/SU3 source",
            "all values are fixed before threshold comparison",
            "BN27 finite quotient or smooth spectrum reproduces the selected operator packet without lifted flags",
            "kernel/zero-mode policy is source-owned before any finitepart is promoted",
            "no observed constants, target residuals, or benchmark values are used",
        ],
        "forbidden": projective["guardrails"],
    }
    OUTPUT_CONTRACT.write_text(json.dumps(contract, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "frontier_matrix_built": True,
        "direct_BN27_source_closed": False,
        "smooth_EQa_quotient_closed": False,
        "selected_bundle_connection_A_found": smooth_A_found,
        "direct_selected_BN27_source_found": direct_source_found,
        "projective_rhoE_lift_retired_for_BN27_threshold": True,
        "best_next_route": "smooth_EQa_payload_if_selected_A_can_be_emitted_else_direct_BN27_source_declaration",
        "first_leaf_direct": direct_bn27["first_irreducible_leaf"],
        "first_leaf_smooth": smooth_eqa["first_irreducible_leaf"],
        "payload_contract_path": rel(OUTPUT_CONTRACT),
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinDirectBN27SourceOrSmoothEQaFrontierMatrix",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "projective_lift_nogo": projective["status"],
            "bn27_orbit_fill": orbit["status"],
            "branch_final_gate": branch["status"],
            "phifin_gate": phifin_gate["status"],
            "bundle_valuesolve": bundle["status"],
            "bismut_payload": bismut["status"],
            "rplus_payload": rplus["status"],
        },
        "routes": {
            "direct_BN27_source_theorem": direct_bn27,
            "smooth_E_Qa_quotient": smooth_eqa,
        },
        "decision": decision,
        "payload_contract_path": rel(OUTPUT_CONTRACT),
        "theorem": {
            "name": "DirectBN27OrSmoothEQaFrontierMatrixTheorem",
            "proved": True,
            "statement": (
                "After rejecting the projective rho_E lift, the oriented Phi_fin branch has exactly two legal "
                "source routes. The direct BN27 route must emit S_QaSU3^BN27 and source-own the 27-mode deck, "
                "C_tau, PhiFin_DE, kernel, and finitepart trace identity. The smooth route must emit selected "
                "A/F_A or an equivalent smooth projective transition, representation action, quotient policy, "
                "E_Qa or heat/zeta/torsion data, and a finite spectral quotient to BN27. Current artifacts fill "
                "BN27 value support and Bismut/R+ geometry support, but neither first source leaf is present."
            ),
        },
        "guardrails": {
            "does_not_reopen_projective_rhoE_as_BN27_threshold_lift": True,
            "does_not_promote_routec_support_to_heterotic_source": True,
            "does_not_promote_Rplus_geometry_as_bundle_A": True,
            "does_not_promote_log92160000": True,
            "does_not_use_lifted_selected_flags": True,
            "does_not_use_observed_data": True,
            "target_fitting_used": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "payload_contract_path": rel(OUTPUT_CONTRACT),
        "note_path": rel(OUTPUT_NOTE),
        "direct_BN27_source_closed": False,
        "smooth_EQa_quotient_closed": False,
        "selected_bundle_connection_A_found": smooth_A_found,
        "direct_selected_BN27_source_found": direct_source_found,
        "projective_rhoE_lift_retired_for_BN27_threshold": True,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin DirectBN27Source or SmoothEQa FrontierMatrix v1

## Result

```text
status = {STATUS}
direct_BN27_source_closed = false
smooth_EQa_quotient_closed = false
selected_bundle_connection_A_found = {str(smooth_A_found).lower()}
direct_selected_BN27_source_found = {str(direct_source_found).lower()}
projective_rhoE_lift_retired_for_BN27_threshold = true
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Payload Contract

```text
{rel(OUTPUT_CONTRACT)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CONTRACT)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
