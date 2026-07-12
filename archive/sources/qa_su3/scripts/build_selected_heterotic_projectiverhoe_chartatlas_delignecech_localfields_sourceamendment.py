"""Build the chart-atlas / Deligne-Cech local-fields source-amendment packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "request": DATA / "selected_heterotic_projectiverhoe_chartatlas_delignecech_localfields_request.json",
    "sourceproof": DATA / "selected_heterotic_projectiverhoe_goodcoverembedding_or_deligne_representative_sourceproof.candidate.json",
    "finite_nerve": DATA / "selected_heterotic_projectiverhoe_finitegoodcovernerve_incidence_table.json",
    "transition_equations": DATA / "selected_heterotic_projectiverhoe_goodcover_transition_skeleton_or_complement_kernel.equations.json",
    "bismut_payload": DATA / "selected_heterotic_bismut_weitzenbock_tensor_payload_fill.candidate.json",
    "ctwist_template": DATA / "ctwist_deligne_cech_template.candidate.json",
    "ctwist_source_search": DATA / "ctwist_source_value_search.candidate.json",
    "cech_scaffold": DATA / "cech_dolbeault_matrix_packet_scaffold.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_chartatlas_delignecech_localfields_sourceamendment.candidate.json"
OUTPUT_EQUATIONS = DATA / "selected_heterotic_projectiverhoe_chartatlas_delignecech_localfields_equations.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_chartatlas_delignecech_localfields_sourceamendment_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_ChartAtlas_DeligneCech_LocalFields_SourceAmendment_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_CHARTATLAS_DELIGNECECH_LOCALFIELDS_EQUATIONPACKET_BUILT_VALUES_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_LocalFieldSolve_or_CoverSelectionNoGo_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    request = load(INPUTS["request"])
    sourceproof = load(INPUTS["sourceproof"])
    finite_nerve = load(INPUTS["finite_nerve"])
    transition_equations = load(INPUTS["transition_equations"])
    bismut_payload = load(INPUTS["bismut_payload"])
    ct_template = load(INPUTS["ctwist_template"])
    ct_source = load(INPUTS["ctwist_source_search"])
    cech_scaffold = load(INPUTS["cech_scaffold"])

    geometry = bismut_payload["filled_payload"]["geometric_tensors"]
    finite_tau = request["finite_target_shadow_allowed_as_check_only"]["tau"]
    labels = list(finite_tau)
    cover_nodes = finite_nerve["cover_nodes"]
    pair_overlaps = finite_nerve["pair_overlaps"]
    triple_overlaps = finite_nerve["triple_overlaps"]

    # This is an equation packet, not a selected local solution. The unknowns are
    # intentionally symbolic and are audited as open source leaves.
    local_field_unknowns = {
        "chart_atlas": {
            "X_selected": "compact Iwasawa/Nil quotient X = Gamma\\H_3(C), selected by MTT branch",
            "U0_U1_U2": {node: f"smooth contractible open set {node} in X" for node in cover_nodes},
            "coordinate_maps": {node: f"phi_{node}: {node} -> R^6" for node in cover_nodes},
            "partition_of_unity": {node: f"rho_{node}" for node in cover_nodes},
            "realization_status": "SYMBOLIC_REQUIRED_NOT_EMITTED",
        },
        "deligne_cech_fields": {
            "B_i": {node: f"B_{node} in Omega^2({node})" for node in cover_nodes},
            "A_ij": {name: f"A_{name} in Omega^1({name})" for name in pair_overlaps},
            "g_ijk": {name: f"g_{name}: {name} -> U(1)" for name in triple_overlaps},
            "h_plus_ij": {name: f"h^+_{name}" for name in pair_overlaps},
            "h_minus_ij": {name: f"h^-_{name}" for name in pair_overlaps},
            "realization_status": "SYMBOLIC_REQUIRED_NOT_EMITTED",
        },
        "label_transition_unknowns": {
            label: {
                "tau": tau,
                "projective_triple_target": f"zeta_3^{tau}",
                "transition_matrices": {name: f"T_{name}^{label}" for name in pair_overlaps},
            }
            for label, tau in finite_tau.items()
        },
    }

    equation_packet = {
        "schema": "SelectedHeteroticProjectiveRhoE.ChartAtlasDeligneCechLocalFieldsEquations.v1",
        "status": "EQUATION_PACKET_BUILT_VALUES_OPEN",
        "known_same_branch_geometry": {
            "selected_geometry_scope": "invariant compact Iwasawa/Strominger frame support",
            "orthonormal_coframe": geometry["orthonormal_coframe"],
            "complex_coframe": geometry["complex_coframe"],
            "complex_structure_J": geometry["complex_structure_J"],
            "Hermitian_form_omega": geometry["Hermitian_form_omega"],
            "structure_constants_c_ij_k": geometry["structure_constants_c_ij_k"],
            "supporting_structure_equations": geometry["supporting_structure_equations"],
            "torsion_H_or_d_c_omega_components": geometry["torsion_H_or_d_c_omega_components"],
            "known_geometry_can_supply_curvature_H": True,
            "known_geometry_can_supply_local_potentials_B_i": False,
        },
        "finite_nerve_scaffold": {
            "cover_nodes": cover_nodes,
            "pair_overlaps": pair_overlaps,
            "triple_overlaps": triple_overlaps,
            "nerve_is_two_simplex": finite_nerve["nerve_is_two_simplex"],
            "smooth_embedding_status": finite_nerve["smooth_embedding_fields"],
        },
        "local_field_unknowns": local_field_unknowns,
        "required_equations": {
            "good_cover_realization": [
                "each U_i is contractible",
                "each nonempty pair overlap U_ij is contractible",
                "the triple overlap U_012 is nonempty and contractible",
                "the smooth cover realizes the formal finite nerve without post-hoc relabeling",
            ],
            "deligne_cech": ct_template["deligne_2_gerbe_template"]["cocycle_equations"],
            "curvature_match": "d B_i = H_Iwasawa on every U_i, with H_Iwasawa the selected torsion/Green-Schwarz curvature from the invariant geometry",
            "transition_shadow": transition_equations["transition_skeleton"]["required_equations"],
            "twisted_module_products": [
                "h^+_ij h^+_jk h^+_ki = g_ijk",
                "h^-_ij h^-_jk h^-_ki = g_ijk^{-1}",
                "T_+ tensor T_- -> T_0 for every F_i G_i -> P product",
            ],
            "finite_tau_shadow_check_only": {
                label: f"g_012^{tau} must map to exp(2*pi*i*{tau}/3) before comparison to finite packet"
                for label, tau in finite_tau.items()
            },
        },
        "source_status": {
            "same_branch_geometry_available": True,
            "formal_finite_nerve_available": True,
            "deligne_template_available": True,
            "cech_dolbeault_formal_basis_available": cech_scaffold["gate_results"]["eleven_formal_spaces_indexed"],
            "same_branch_local_B_i_A_ij_g_ijk_values_found": ct_source["gate_results"]["same_branch_Qa_SU3_values_found"],
            "selected_smooth_cover_values_found": False,
            "selected_transition_matrices_found": False,
            "selected_operator_domain_found": False,
        },
        "forbidden_promotions": request["forbidden_shortcuts"],
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_EQUATIONS.write_text(json.dumps(equation_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    open_leaves = {
        "selected_compact_Iwasawa_or_Nil_quotient": True,
        "coordinate_charts_U0_U1_U2": True,
        "contractibility_proof_for_cover_and_overlaps": True,
        "local_B_i_two_forms": True,
        "local_A_ij_one_forms": True,
        "local_g_ijk_functions": True,
        "h_ij_twisted_module_transitions": True,
        "map_to_finite_tau_table_before_target_comparison": True,
        "mapped_Freed_Witten_Bianchi_projector_checks": True,
        "smooth_operator_or_complement_domain": True,
    }

    closed_support = {
        "invariant_Iwasawa_geometry_payload": True,
        "torsion_H_components_known": True,
        "formal_three_node_nerve": True,
        "finite_tau_shadow_table": True,
        "Deligne_Cech_equation_template": True,
        "formal_Cech_Dolbeault_label_scaffold": True,
    }

    decision = {
        "equation_packet_built": True,
        "geometry_anchor_promoted_to_known_support": True,
        "local_field_values_emitted": False,
        "selected_chart_atlas_emitted": False,
        "smooth_cover_contractibility_proved": False,
        "smooth_tau_shadow_derived": False,
        "S1_closed": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoEChartAtlasDeligneCechLocalFieldsSourceAmendment",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "equation_packet_path": rel(OUTPUT_EQUATIONS),
        "closed_support": closed_support,
        "open_leaves": open_leaves,
        "decision": decision,
        "guardrails": {
            "does_not_promote_invariant_geometry_to_local_B": True,
            "does_not_promote_formal_nerve_to_smooth_cover": True,
            "does_not_promote_symbolic_unknowns_to_values": True,
            "does_not_assign_tau_after_finite_table": True,
            "does_not_use_observed_data": True,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "ChartAtlasDeligneCechEquationPacketTheorem",
            "proved": True,
            "statement": (
                "The selected invariant Iwasawa/Strominger geometry, formal finite "
                "three-node nerve, Deligne/Cech template, and finite tau table define "
                "a single local-field equation packet for S1. This advances the "
                "frontier from an unstructured source request to explicit equations "
                "for charts, local B_i/A_ij/g_ijk fields, twisted transitions, and "
                "finite-shadow checks. It does not solve those equations or close S1."
            ),
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "equation_packet_path": rel(OUTPUT_EQUATIONS),
        "note_path": rel(OUTPUT_NOTE),
        "equation_packet_built": True,
        "known_geometry_can_supply_curvature_H": True,
        "known_geometry_can_supply_local_potentials_B_i": False,
        "local_field_values_emitted": False,
        "S1_closed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE ChartAtlas DeligneCech LocalFields SourceAmendment v1

## Result

```text
status = {STATUS}
equation_packet_built = true
known_geometry_can_supply_curvature_H = true
known_geometry_can_supply_local_potentials_B_i = false
S1_closed = false
next_required_artifact = {NEXT}
```

## Construction

This packet combines the strongest available ingredients: selected invariant
Iwasawa/Strominger geometry, the formal three-node nerve, the Deligne/Cech
gerbe template, and the finite `tau` shadow. It turns the previous request into
an explicit local-field equation system for chart data, `B_i,A_ij,g_ijk`,
twisted transitions, and finite-shadow checks.

It does not emit the chart atlas or local fields. The invariant torsion gives
the curvature target `H`; it is not a substitute for local potentials on a
selected good cover.

Equation packet:

```text
{rel(OUTPUT_EQUATIONS)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_EQUATIONS)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
