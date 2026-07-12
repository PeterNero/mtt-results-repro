"""Build the direct End_0 differential-table attempt from AH/Ext form data."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
Q79 = ROOT.parent / "mtt-q79-proof-repro"

OUT_CANDIDATE = ROOT / "candidate_data" / "selected_end0_direct_differential_table_from_ah_ext_forms.candidate.json"
OUT_CERT = ROOT / "certificates" / "selected_end0_direct_differential_table_from_ah_ext_forms_certificate.json"
OUT_PROOF = ROOT / "proof_corpus" / "MTT_Selected_End0_Direct_Differential_Table_From_AH_Ext_Forms_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    dual_path_path = ROOT / "candidate_data" / "selected_end0_basis_differential_table_or_bn_identification.candidate.json"
    first_solve_path = ROOT / "candidate_data" / "selected_hym_adjoint_galerkin_first_coefficient_solve.candidate.json"
    ah_source_path = ROOT / "candidate_data" / "selected_routec_ah_source_selection_or_routec_selected_residual.candidate.json"
    automorphy_path = Q79 / "candidate_data" / "visible_rank2_l2_appell_humbert_automorphy.candidate.json"
    cohomology_path = Q79 / "candidate_data" / "visible_rank2_l2_pullback_cech_attempt.cohomology.json"
    pullback_path = Q79 / "candidate_data" / "visible_rank2_l2_pullback_cech_attempt.candidate.json"

    dual_path = load(dual_path_path)
    first_solve = load(first_solve_path)
    ah_source = load(ah_source_path)
    automorphy = load(automorphy_path)
    cohomology = load(cohomology_path)
    pullback = load(pullback_path)

    selected_ah_source = ah_source["selected_AH_goodcover_stability_layer"]["proved"] is True
    automorphy_ready = all(
        [
            automorphy["construction_checks"]["cocycle_law_holds_on_generators_mod_2pi_i"],
            automorphy["construction_checks"]["c1_matrix_matches_required_order"],
            automorphy["construction_checks"]["central_shared_circle_trivial"],
        ]
    )
    ext_closed = all(
        [
            cohomology["acceptance_tests"]["extension_class_closed"],
            cohomology["acceptance_tests"]["extension_class_not_exact"],
            cohomology["reported_cohomology"]["extension_class_vector_C1"][0] == 1,
        ]
    )

    # This is a symbolic local-form lift, not a numerical good-cover table.
    selected_symbolic_ext_form_template = selected_ah_source and automorphy_ready and ext_closed
    raw_good_cover_transition_table_emitted = False
    selected_hym_connection_terms_emitted = False
    hodge_lambda_quadrature_table_emitted = False
    gauge_projector_emitted = False
    newton_solve_ready = all(
        [
            selected_symbolic_ext_form_template,
            raw_good_cover_transition_table_emitted,
            selected_hym_connection_terms_emitted,
            hodge_lambda_quadrature_table_emitted,
            gauge_projector_emitted,
        ]
    )

    ext_label = cohomology["reported_cohomology"]["nonzero_extension_class_label"]
    c1_matrix = automorphy["model"]["c1_deck_alternating_matrix_order_g1_to_g6"]

    candidate = {
        "candidate": "MTTSelectedEnd0DirectDifferentialTableFromAHExtForms",
        "status": "MTT_SELECTED_END0_DIRECT_TABLE_PARTIAL_AH_EXT_FORM_TEMPLATE_BUILT_HYM_TABLES_OPEN",
        "closure_claimed": False,
        "target_fitting_used": False,
        "inputs": {
            "dual_path_gate": str(dual_path_path),
            "adjoint_galerkin_first_solve": str(first_solve_path),
            "selected_AH_source_layer": str(ah_source_path),
            "q79_Appell_Humbert_automorphy": str(automorphy_path),
            "q79_pullback_Cech_cohomology": str(cohomology_path),
            "q79_pullback_Cech_attempt": str(pullback_path),
        },
        "selected_source_boundary": {
            "selected_AH_source_layer_imported": selected_ah_source,
            "automorphy_formula_constructed": automorphy_ready,
            "cohomology_Ext_vector_closed_nonexact": ext_closed,
            "raw_good_cover_transition_table_emitted": raw_good_cover_transition_table_emitted,
            "why_boundary_matters": "The selected terminal/AH layer promotes the ordered source, but q79 still marks the finite cohomology payload as an unselected fixture unless it is bound to raw transition/local-form data. This artifact supplies a symbolic local-form template, not the full good-cover table.",
        },
        "AH_transition_seed": {
            "built": automorphy_ready,
            "line": "L^2=(2,-4,0)",
            "factor_formula": automorphy["model"]["factor_formula"],
            "c1_deck_matrix_order_g1_to_g6": c1_matrix,
            "central_shared_circle_degree_zero": automorphy["construction_checks"]["central_shared_circle_trivial"],
            "curvature_seed_symbolic": {
                "E1_pair_g1_g2": 2,
                "E2_pair_g3_g4": -4,
                "central_pair_g5_g6": 0,
                "role": "Chern/Appell-Humbert seed for the L^2 off-diagonal extension block, before solving the nonabelian HYM metric.",
            },
        },
        "Ext_local_form_template": {
            "built": selected_symbolic_ext_form_template,
            "selected_basis_slot": ext_label,
            "cohomology_vector_C1": cohomology["reported_cohomology"]["extension_class_vector_C1"],
            "symbolic_representative": "theta_plus_0(z1) tensor eta_minus_0(z2) dbar_z2",
            "interpretation": "degree +2 theta section on E1 times degree -4 Serre-dual/H1 representative on E2, pulled back to the Iwasawa base; central shared circle degree is zero",
            "closed_nonexact": ext_closed,
            "not_yet_numeric_local_form": True,
            "needed_to_become_numeric": [
                "chosen theta-function normalization and good-cover trivializations",
                "explicit partition of unity or equivalent Dolbeault representative",
                "transition-compatible local expression on overlaps",
                "Hermitian metric normalization for the non-split extension",
            ],
        },
        "partial_End0_differential_table": {
            "built": True,
            "End0_basis": first_solve["algebraic_adjoint_packet"]["basis"],
            "ad_matrices": first_solve["algebraic_adjoint_packet"]["ad_matrices_on_End0_basis"],
            "manifold_structure_dbar": dual_path["path_B_direct_End0_table"]["emitted_universal_tables"]["Iwasawa_left_invariant_dbar_rules"],
            "off_diagonal_Ext_entry": "eta = theta_plus_0 tensor eta_minus_0 dbar_z2 in the L^2 block",
            "symbolic_operator_template": "barpartial_End0 = barpartial_Iwasawa + ad(A_split_AH + eta_offdiag + HYM_correction)",
            "safe_to_use_for_newton": False,
            "why_not_safe_yet": "The HYM correction, Hodge/Lambda table, quadrature, and gauge projector are not emitted; the Ext form is symbolic rather than a normalized local table.",
        },
        "newton_readiness": {
            "ready": newton_solve_ready,
            "raw_good_cover_transition_table_emitted": raw_good_cover_transition_table_emitted,
            "selected_hym_connection_terms_emitted": selected_hym_connection_terms_emitted,
            "hodge_lambda_quadrature_table_emitted": hodge_lambda_quadrature_table_emitted,
            "gauge_projector_emitted": gauge_projector_emitted,
            "first_blocker": "selected_normalized_local_form_table_for_theta_plus_0_tensor_eta_minus_0",
        },
        "superset_strategy": {
            "straight_path": "AH/Appell-Humbert L^2 transition seed plus selected Ext local-form representative, then End_0 adjoint differential table.",
            "support_path": "Use B_N and Route-C validators only after the direct End_0 table emits selected matrices.",
            "locked_target": "selected V_alpha branch L=(1,-2,0), L^2=(2,-4,0), equal-radius metric, no measured constants.",
        },
        "what_closes_now": {
            "AH_transition_seed_for_L2_recorded": True,
            "selected_symbolic_Ext_local_form_template_built": selected_symbolic_ext_form_template,
            "direct_End0_operator_template_built": True,
            "Newton_first_blocker_reduced_to_normalized_local_form_table": True,
        },
        "what_remains_open": {
            "normalized_theta_eta_local_form_table": True,
            "raw_good_cover_transition_functions_or_equivalent_Dolbeault_representative": True,
            "selected_HYM_metric_connection_correction": True,
            "Hodge_Lambda_quadrature_gauge_projector_tables": True,
            "selected_Newton_Galerkin_coefficients": True,
            "full_SM_or_no_knob_closure": True,
        },
        "next_required_artifact": "MTT_Selected_Normalized_Ext_Local_Form_Table_v1",
    }

    cert = {
        "certificate": "MTT_Selected_End0_Direct_Differential_Table_From_AH_Ext_Forms_v1",
        "status": candidate["status"],
        "closure_claimed": False,
        "target_fitting_used": False,
        "selected_symbolic_Ext_local_form_template_built": selected_symbolic_ext_form_template,
        "newton_ready": newton_solve_ready,
        "first_blocker": candidate["newton_readiness"]["first_blocker"],
        "next_required_artifact": candidate["next_required_artifact"],
    }

    proof = """# MTT Selected End0 Direct Differential Table From AH Ext Forms v1

## Claim

The direct `End_0(V_alpha)` route now has a symbolic local-form bridge:

```text
eta = theta_plus_0(z1) tensor eta_minus_0(z2) dbar_z2
```

This corresponds to the selected first Ext slot
`theta_plus_0_tensor_eta_minus_0` in the eight-dimensional
`H^1(X,L^2)` packet.  Appell-Humbert data supplies the ordered `L^2=(2,-4,0)`
transition seed and curvature row.

## What Closes

- The AH/Appell-Humbert transition seed for `L^2` is recorded.
- The selected Ext cohomology slot is lifted to a symbolic local-form template.
- The direct `End_0` operator template is:

```text
barpartial_End0 = barpartial_Iwasawa + ad(A_split_AH + eta_offdiag + HYM_correction)
```

## What Does Not Close

This is not yet a Newton-ready table.  The symbolic Ext representative must be
normalized into an actual local table: theta basis, overlap/trivialization
rules, partition-of-unity or equivalent Dolbeault representative, and Hermitian
normalization.  The HYM correction, Hodge/Lambda, quadrature, and gauge
projector tables are also still open.

## Next Artifact

`MTT_Selected_Normalized_Ext_Local_Form_Table_v1`.
"""

    OUT_CANDIDATE.parent.mkdir(parents=True, exist_ok=True)
    OUT_CERT.parent.mkdir(parents=True, exist_ok=True)
    OUT_PROOF.parent.mkdir(parents=True, exist_ok=True)
    OUT_CANDIDATE.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_PROOF.write_text(proof, encoding="utf-8")
    print(f"Wrote {OUT_CANDIDATE}")
    print(f"Wrote {OUT_CERT}")
    print(f"Wrote {OUT_PROOF}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
