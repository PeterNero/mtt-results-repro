"""Attempt the exact-complement or smooth rho_E transition value packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "contract": DATA / "selected_heterotic_projectiverhoe_exact_complement_or_smooth_transition_value_contract.json",
    "nodoublecount": DATA / "selected_heterotic_projectiverhoe_smoothtransitiontables_or_complementquotient_nodoublecount.candidate.json",
    "finite_rep_packet": DATA / "selected_heterotic_projectiverhoe_finite_representative_to_cocycle_packet.json",
    "finite_operator_packet": DATA / "selected_heterotic_projectiverhoe_finite_internal_operator_packet.json",
    "gr_internal_separation": DATA / "gr_surface_internal_quantum_separation_theorem.candidate.json",
    "smooth_source_fill": DATA / "selected_heterotic_projectiverhoe_smoothoperator_sourcepacket_fillattempt.candidate.json",
    "smooth_trace_lift": DATA / "selected_heterotic_projectiverhoe_smoothtracelift_or_eqafinitepart.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_exactcomplement_or_smoothrhoetransition_valuepacket.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_exactcomplement_or_smoothrhoetransition_valuepacket_certificate.json"
OUTPUT_PACKET = DATA / "selected_heterotic_projectiverhoe_exactcomplement_or_smoothrhoetransition_valuepacket.values.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_ExactComplementQuotient_or_SmoothRhoETransitionTables_ValuePacket_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_VALUEPACKET_ATTEMPT_INTERNAL_PROJECTION_CLOSED_SMOOTH_TABLES_EXACT_QUOTIENT_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_ExactComplementFactorization_or_GoodCoverTransitionTables_SourceSearch_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def zero_matrix(n: int) -> list[list[int]]:
    return [[0 for _ in range(n)] for _ in range(n)]


def diagonal_from_tau(labels: list[str], tau: dict[str, int]) -> list[list[int]]:
    matrix = zero_matrix(len(labels))
    for i, label in enumerate(labels):
        matrix[i][i] = tau[label]
    return matrix


def main() -> dict[str, Any]:
    contract = load(INPUTS["contract"])
    nodoublecount = load(INPUTS["nodoublecount"])
    finite_rep = load(INPUTS["finite_rep_packet"])
    finite_operator = load(INPUTS["finite_operator_packet"])
    gr_sep = load(INPUTS["gr_internal_separation"])
    smooth_source_fill = load(INPUTS["smooth_source_fill"])
    trace_lift = load(INPUTS["smooth_trace_lift"])

    labels = finite_operator["labels"]
    tau = {key: int(value) for key, value in finite_operator["tau_values"].items()}
    finite_projection = {
        "domain": "internal_quantized_projective_Qa_SU3_packet",
        "codomain": labels,
        "projection_rule": "Retain exactly the selected F_i,G_i,P quotient labels; route GR/protospinor smooth surface modes outside this internal determinant.",
        "projector_matrix_on_ordered_labels": [[1 if i == j else 0 for j in range(len(labels))] for i in range(len(labels))],
        "D_E_after_projection": diagonal_from_tau(labels, tau),
        "closed_for_internal_quotient": True,
    }

    smooth_transition_lane = {
        "attempted": True,
        "selected_good_cover_or_smooth_quotient_cover": None,
        "Deligne_Cech_or_B_field_representative": None,
        "period_unit_map_to_finite_c_unit": None,
        "rho_E_overlap_or_generator_boundary_tables": None,
        "cocycle_law_checked_on_smooth_tables": False,
        "metric_unitarity_compatibility": None,
        "mapped_Freed_Witten_Bianchi_projector_checks": None,
        "bundle_operator_action_A_or_F_A": None,
        "verdict": "OPEN_NO_SMOOTH_TRANSITION_TABLES_IN_CURRENT_SOURCE",
    }

    exact_complement_lane = {
        "attempted": True,
        "finite_projection_family_internal": finite_projection,
        "smooth_domain_projection_family": None,
        "smooth_complement_universal_or_GR_only": "SUPPORT_ONLY_FROM_GR_INTERNAL_SEPARATION",
        "heat_zeta_torsion_factorization_theorem": None,
        "BRST_FP_gauge_quotient_counted_once": nodoublecount["no_double_count_policy"],
        "finite_part_equals_log2008_after_exact_quotient": None,
        "verdict": "PARTIAL_INTERNAL_PROJECTION_CLOSED_EXACT_SMOOTH_FACTORISATION_OPEN",
    }

    value_packet = {
        "schema": "SelectedHeteroticProjectiveRhoEExactComplementOrSmoothRhoETransitionValuePacket.v1",
        "status": "PARTIAL_INTERNAL_VALUE_PACKET_SMOOTH_VALUES_OPEN",
        "closed_prerequisites": contract["closed_prerequisites"],
        "finite_internal_values": {
            "labels": labels,
            "tau": tau,
            "rho_E_central_character": finite_operator["rho_E_central_character"],
            "D_E": finite_operator["D_E_diagonal_matrix_on_labels"],
            "H_sel": finite_operator["H_sel"],
            "Green_operator": finite_operator["Green_operator"],
            "Riesz_projector": finite_operator["Riesz_projector"],
            "chi_Qa": finite_operator["chi_Qa"],
            "finite_internal_part": "log(2008)",
        },
        "lane_A_smooth_transition_tables": smooth_transition_lane,
        "lane_B_exact_complement_quotient": exact_complement_lane,
        "not_promoted": {
            "finite_character_table_is_not_smooth_transition_data": True,
            "internal_projection_is_not_smooth_heat_factorization": True,
            "no_double_count_is_not_exact_complement_cancellation": True,
            "log2008_not_physical_coupling_match": True,
        },
    }

    closed_leaf_count = 0
    closed_leaf_count += int(all(contract["closed_prerequisites"].values()))
    closed_leaf_count += int(finite_projection["closed_for_internal_quotient"])
    closed_leaf_count += int(nodoublecount["decision"]["no_double_count_policy_closed"])
    closed_leaf_count += int(finite_rep["central_cocycle_map"]["all_Fi_Gi_products_cancel_to_P"])

    decision = {
        "value_packet_attempted": True,
        "internal_projection_family_closed": True,
        "finite_internal_values_reemitted": True,
        "no_double_count_policy_imported": True,
        "smooth_transition_tables_emitted": False,
        "exact_smooth_complement_quotient_closed": False,
        "heat_zeta_torsion_factorization_closed": False,
        "E_Qa_computed": False,
        "smooth_finitepart_computed": False,
        "closed_leaf_count": closed_leaf_count,
        "remaining_hard_blockers": [
            "selected smooth good cover or quotient-cover source",
            "smooth Deligne/Cech/B-field representative",
            "smooth rho_E overlap/generator transition tables",
            "smooth projector-retention and mapped admissibility checks",
            "smooth heat/zeta/torsion factorization or E_Qa operator theorem",
        ],
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoEExactComplementOrSmoothRhoETransitionValuePacket",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "nodoublecount": nodoublecount["status"],
            "smooth_source_fill": smooth_source_fill["status"],
            "smooth_trace_lift": trace_lift["status"],
            "gr_internal_separation": gr_sep["status"],
        },
        "value_packet_path": rel(OUTPUT_PACKET),
        "decision": decision,
        "cross_checks": {
            "contract_prerequisites_all_closed": all(contract["closed_prerequisites"].values()),
            "finite_rep_map_closed": finite_rep["central_cocycle_map"]["all_Fi_Gi_products_cancel_to_P"],
            "no_double_count_closed": nodoublecount["decision"]["no_double_count_policy_closed"],
            "smooth_source_values_absent": smooth_source_fill["decision"]["smooth_operator_source_packet_filled"] is False,
            "trace_lift_no_go_retained": trace_lift["decision"]["current_source_no_go_for_trace_lift"],
            "GR_routing_support_retained": gr_sep["decision"]["GR_smooth_surface_response"] == "ROUTED_TO_GR_PROTOSPINOR_SECTOR",
        },
        "guardrails": {
            "does_not_promote_internal_projection_to_smooth_factorization": True,
            "does_not_promote_finite_rhoE_to_smooth_tables": True,
            "does_not_claim_E_Qa": True,
            "does_not_claim_smooth_finitepart": True,
            "does_not_claim_physical_coupling_match": True,
            "does_not_use_observed_couplings_or_scales": True,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "ExactComplementOrSmoothTransitionValuePacketCurrentSourceAttempt",
            "proved": True,
            "statement": (
                "The current source emits the selected finite internal value packet, "
                "including the internal projection to F_i,G_i,P, tau, rho_E, D_E, "
                "Green/Riesz, chi_Qa, log(2008), and no-double-count policy. It does "
                "not emit smooth transition tables and does not prove exact smooth "
                "heat/zeta/torsion complement factorization. The remaining source "
                "search is therefore reduced to a good-cover/transition-table source "
                "or an exact complement-factorization theorem."
            ),
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    OUTPUT_PACKET.write_text(json.dumps(value_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "value_packet_path": rel(OUTPUT_PACKET),
        "note_path": rel(OUTPUT_NOTE),
        "internal_projection_family_closed": True,
        "smooth_transition_tables_emitted": False,
        "exact_smooth_complement_quotient_closed": False,
        "E_Qa_computed": False,
        "smooth_finitepart_computed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE ExactComplementQuotient or SmoothRhoETransitionTables ValuePacket v1

## Result

```text
status = {STATUS}
internal_projection_family_closed = true
smooth_transition_tables_emitted = false
exact_smooth_complement_quotient_closed = false
E_Qa_computed = false
smooth_finitepart_computed = false
next_required_artifact = {NEXT}
```

## Closed Now

The value packet re-emits the selected finite internal data and closes the
internal projection family to the eleven labels `F_i,G_i,P`. It also imports the
no-double-count theorem: smooth GR/protospinor surface modes are not appended as
a second Qa/SU3 determinant.

## Still Missing

The current source still lacks smooth good-cover/transition-table data and an
exact heat/zeta/torsion complement-factorization theorem. Those are now the two
remaining legal ways to turn the internal value packet into a smooth finite-part
closure.
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_PACKET)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
