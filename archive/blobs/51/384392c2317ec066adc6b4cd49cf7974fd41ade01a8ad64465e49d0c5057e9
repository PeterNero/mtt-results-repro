"""Try both End_0 differential-table paths: identify B_N or build directly."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
Q79 = ROOT.parent / "mtt-q79-proof-repro"

OUT_CANDIDATE = ROOT / "candidate_data" / "selected_end0_basis_differential_table_or_bn_identification.candidate.json"
OUT_CERT = ROOT / "certificates" / "selected_end0_basis_differential_table_or_bn_identification_certificate.json"
OUT_PROOF = ROOT / "proof_corpus" / "MTT_Selected_End0_Basis_Differential_Table_or_BN_Identification_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    first_solve_path = ROOT / "candidate_data" / "selected_hym_adjoint_galerkin_first_coefficient_solve.candidate.json"
    smooth_bn_path = ROOT / "candidate_data" / "selected_routec_smooth_bn_galerkin_lift.candidate.json"
    invariant_dolbeault_path = Q79 / "certificates" / "visible_rank2_l2_invariant_dolbeault_attempt_certificate.json"

    first_solve = load(first_solve_path)
    smooth_bn = load(smooth_bn_path)
    invariant_dolbeault = load(invariant_dolbeault_path)

    b_n_lift = smooth_bn["B_N_lift"]
    b_n_gates = smooth_bn["gates"]
    equivariance = b_n_lift["bundle_equivariance"]
    basis = b_n_lift["basis"]
    basis_dimension = len(basis)
    zero_cluster = b_n_lift["zero_cluster"]

    lane_a_dimension_match = basis_dimension == 27
    lane_a_vector_space_shape_match = lane_a_dimension_match and zero_cluster["dimension"] == 3
    lane_a_selected_identification_closed = (
        lane_a_vector_space_shape_match
        and equivariance["ordinary_bundle_equivariance"] is True
        and equivariance["projective_equivariance_up_to_central_phase"] is False
    )

    dbar_rules = invariant_dolbeault["ansatz"]["basis_rules"]
    lane_b_invariant_structure_table_emitted = True
    lane_b_selected_connection_table_closed = False
    lane_b_ext_local_form_closed = False
    lane_b_hodge_quadrature_closed = False
    lane_b_gauge_projector_closed = False

    direct_table_closed = all(
        [
            lane_b_invariant_structure_table_emitted,
            lane_b_selected_connection_table_closed,
            lane_b_ext_local_form_closed,
            lane_b_hodge_quadrature_closed,
            lane_b_gauge_projector_closed,
        ]
    )

    candidate = {
        "candidate": "MTTSelectedEnd0BasisDifferentialTableOrBNIdentification",
        "status": "MTT_SELECTED_END0_BASIS_DIFFERENTIAL_TABLE_DUAL_PATH_ATTEMPTED_SELECTED_TABLES_OPEN",
        "closure_claimed": False,
        "target_fitting_used": False,
        "inputs": {
            "adjoint_galerkin_first_solve": str(first_solve_path),
            "smooth_BN_galerkin_lift": str(smooth_bn_path),
            "visible_rank2_invariant_dolbeault_attempt": str(invariant_dolbeault_path),
        },
        "path_A_identify_existing_BN": {
            "attempted": True,
            "closed": lane_a_selected_identification_closed,
            "result": "REJECTED_AS_SELECTED_END0_TABLE",
            "support_retained": {
                "dimension_match_27": lane_a_dimension_match,
                "zero_cluster_dimension_3": zero_cluster["dimension"] == 3,
                "positive_model_gap": b_n_gates["complement_gap_positive"],
                "validator_shape_available": True,
            },
            "blocking_evidence": {
                "basis_id": b_n_lift["basis_id"],
                "bundle_equivariance_type": equivariance["type"],
                "ordinary_bundle_equivariance": equivariance["ordinary_bundle_equivariance"],
                "projective_equivariance_up_to_central_phase": equivariance["projective_equivariance_up_to_central_phase"],
                "rho_E_source": equivariance["rho_E_source"],
            },
            "why_not_selected_End0": [
                "End_0(V_alpha) is an ordinary adjoint bundle once V_alpha is fixed; the current B_N scaffold is explicitly gerbe-twisted projective.",
                "The B_N fiber e_0,e_1,e_2 is a qutrit/projective family carrier, not theorem-identified with the adjoint basis T1,T2,T3.",
                "The B_N active F3^2 Fourier modes provide a useful finite execution shape but no selected local d/barpartial/wedge/Hodge table for End_0(V_alpha).",
            ],
        },
        "path_B_direct_End0_table": {
            "attempted": True,
            "closed": direct_table_closed,
            "result": "PARTIAL_STRUCTURAL_TABLE_ONLY",
            "emitted_universal_tables": {
                "End0_basis": first_solve["algebraic_adjoint_packet"]["basis"],
                "ad_matrices": first_solve["algebraic_adjoint_packet"]["ad_matrices_on_End0_basis"],
                "Iwasawa_left_invariant_dbar_rules": dbar_rules,
                "ordinary_product_rule_template": "dbar(alpha tensor T_i)=dbar(alpha) tensor T_i plus connection commutator terms once A_HYM is supplied",
            },
            "what_is_still_not_selected": {
                "selected_End0_local_basis": True,
                "selected_A_HYM_connection_terms": True,
                "selected_Ext_local_form_representative": True,
                "selected_Hodge_Lambda_table_for_equalradius_metric": True,
                "selected_quadrature_table": True,
                "selected_gauge_projector": True,
            },
            "guardrail": "The invariant dbar rules are manifold-structure support only. They are not a selected End_0(V_alpha) Dolbeault operator until transition/automorphy and HYM connection terms are supplied.",
        },
        "two_path_verdict": {
            "path_A_best_use": "Keep B_N as a validator/execution scaffold and model spectral shape; do not identify it as selected End_0(V_alpha).",
            "path_B_best_use": "Build the selected End_0 table directly from AH/Appell-Humbert transition data, selected Ext local forms, and the gauge-fixed HYM connection.",
            "winner_for_rigor": "Path B",
            "reason": "Path A has projective/ordinary type mismatch; Path B preserves the selected rank-2 source and only asks for concrete differential data.",
        },
        "what_closes_now": {
            "both_paths_tested": True,
            "BN_identification_rejected_at_selected_End0_level": True,
            "BN_support_retained_as_scaffold": True,
            "direct_End0_universal_algebra_and_invariant_dbar_table_emitted": True,
            "next_missing_tables_identified": True,
        },
        "what_remains_open": {
            "selected_End0_local_basis": True,
            "selected_transition_or_automorphy_to_local_form_map": True,
            "selected_Ext_local_form_representative": True,
            "selected_HYM_connection_terms": True,
            "selected_Hodge_Lambda_quadrature_gauge_projector_tables": True,
            "selected_Newton_Galerkin_coefficients": True,
            "full_SM_or_no_knob_closure": True,
        },
        "next_required_artifact": "MTT_Selected_End0_Direct_Differential_Table_From_AH_Ext_Forms_v1",
    }

    cert = {
        "certificate": "MTT_Selected_End0_Basis_Differential_Table_or_BN_Identification_v1",
        "status": candidate["status"],
        "closure_claimed": False,
        "target_fitting_used": False,
        "both_paths_tested": True,
        "path_A_BN_identification_closed": lane_a_selected_identification_closed,
        "path_B_direct_table_closed": direct_table_closed,
        "winner_for_rigor": "Path B",
        "next_required_artifact": candidate["next_required_artifact"],
    }

    proof = """# MTT Selected End0 Basis Differential Table or BN Identification v1

## Claim

Both paths were tried.

Path A asks whether the existing 27-mode `B_N` scaffold can be identified as
the selected finite `End_0(V_alpha)` differential table.  It cannot be promoted
at the selected level: it has the right vector-space size and a useful
three-dimensional zero cluster, but it is explicitly gerbe-twisted projective
data with `ordinary_bundle_equivariance = false`.

Path B builds directly.  It emits the universal `End_0` adjoint algebra and the
available Iwasawa left-invariant structural Dolbeault rules, but it does not yet
emit the selected connection-dependent differential table.

## Path A Verdict

Keep `B_N` as scaffold, validator shape, and finite spectral inspiration.  Do
not identify it with selected `End_0(V_alpha)` until a theorem maps the qutrit
projective carrier to the ordinary adjoint bundle or changes the carrier
definition.

## Path B Verdict

Path B is the rigorous route.  The direct table must be built from:

- selected AH/Appell-Humbert transition data;
- a local-form representative of the selected Ext class;
- the gauge-fixed HYM connection terms;
- Hodge/Lambda, quadrature, and gauge-projector tables at equal radius.

The invariant rules `dbar e1=0`, `dbar e2=0`, `dbar e3=e1 wedge e2` are
manifold-structure support only.  They are not the selected `End_0(V_alpha)`
operator by themselves.

## Next Artifact

`MTT_Selected_End0_Direct_Differential_Table_From_AH_Ext_Forms_v1`.
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
