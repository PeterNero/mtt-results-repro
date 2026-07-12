"""Build the selected HYM gauge-fixed representative / Galerkin solve gate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

OUT_CANDIDATE = ROOT / "candidate_data" / "selected_hym_gaugefixed_connection_or_galerkin_solve.candidate.json"
OUT_CERT = ROOT / "certificates" / "selected_hym_gaugefixed_connection_or_galerkin_solve_certificate.json"
OUT_PROOF = ROOT / "proof_corpus" / "MTT_Selected_HYM_GaugeFixed_Connection_Representative_or_Galerkin_Solve_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def list_len(value: object) -> int | None:
    return len(value) if isinstance(value, list) else None


def main() -> int:
    extraction_path = ROOT / "candidate_data" / "selected_hym_connection_to_finite_operator_extraction.candidate.json"
    hym_bridge_path = ROOT / "candidate_data" / "selected_routec_equalradius_gauduchon_hym_bridge.candidate.json"
    ah_source_path = ROOT / "candidate_data" / "selected_routec_ah_source_selection_or_routec_selected_residual.candidate.json"
    smooth_bn_path = ROOT / "candidate_data" / "selected_routec_smooth_bn_galerkin_lift.candidate.json"
    de_bn_path = ROOT / "candidate_data" / "selected_routec_de_action_on_smooth_bn.candidate.json"
    galerkin_spec_path = ROOT / "candidate_data" / "selected_routec_strominger_galerkin_solve_spec.candidate.json"

    extraction = load(extraction_path)
    hym_bridge = load(hym_bridge_path)
    ah_source = load(ah_source_path)
    smooth_bn = load(smooth_bn_path)
    de_bn = load(de_bn_path)
    galerkin_spec = load(galerkin_spec_path)

    b_n_lift = smooth_bn.get("B_N_lift", {})
    b_n_scaffold = smooth_bn.get("B_N_scaffold", {})
    basis = b_n_lift.get("basis", [])
    basis_dimension = list_len(basis)
    complement_gap = b_n_lift.get("complement_gap")
    mesh_counts = galerkin_spec.get("mesh_scaffold", {}).get("counts", {})

    abstract_hym_closed = (
        extraction["straight_path"]["stage_E0_selected_bundle_and_metric"]["closed"] is True
        and hym_bridge["HYM_existence_bridge"]["abstract_HYM_existence_for_selected_bundle_metric"] is True
    )
    selected_ah_layer = ah_source["selected_AH_goodcover_stability_layer"]["proved"] is True
    bn_scaffold_built = b_n_scaffold.get("passes_B_N_payload_gate") is True or basis_dimension == 27
    de_scaffold_built = de_bn.get("status") == "MTT_SELECTED_ROUTEC_DE_ACTION_ON_SMOOTH_BN_MATRIX_BUILT_SOURCE_PROMOTION_OPEN"

    analytic_representative_emitted = False
    finite_newton_values_emitted = False
    rank2_to_sector_functor_emitted = False
    posteriori_error_certificate_emitted = False

    first_solve_closed = all(
        [
            abstract_hym_closed,
            selected_ah_layer,
            analytic_representative_emitted or finite_newton_values_emitted,
            rank2_to_sector_functor_emitted,
            posteriori_error_certificate_emitted,
        ]
    )

    candidate = {
        "candidate": "MTTSelectedHYMGaugeFixedConnectionRepresentativeOrGalerkinSolve",
        "status": "MTT_SELECTED_HYM_GAUGEFIXED_CONNECTION_OR_GALERKIN_SOLVE_SPEC_BUILT_SOLVE_VALUES_OPEN",
        "closure_claimed": False,
        "target_fitting_used": False,
        "inputs": {
            "extraction_contract": str(extraction_path),
            "equalradius_HYM_bridge": str(hym_bridge_path),
            "selected_AH_source_layer": str(ah_source_path),
            "smooth_BN_galerkin_lift": str(smooth_bn_path),
            "DE_action_on_smooth_BN": str(de_bn_path),
            "routec_galerkin_solve_spec": str(galerkin_spec_path),
        },
        "superset_strategy": {
            "straight_path": {
                "description": "Solve the selected rank-2 HYM problem on V_alpha in a fixed unitary/Coulomb gauge, then derive finite operator data from that connection.",
                "target": "selected AH/Cech extension V_alpha with L=(1,-2,0) at equal radius p=(1,1,1)",
                "closed_inputs": {
                    "selected_AH_source_layer": selected_ah_layer,
                    "abstract_HYM_existence": abstract_hym_closed,
                },
            },
            "combined_support_paths": [
                "Route-C/Strominger Galerkin spec supplies residual slots and validator order",
                "smooth B_N scaffold supplies a 27-mode qutrit/sector execution basis shape",
                "finite D_E scaffold supplies algebraic matrix slots only",
                "q79 validators supply acceptance schemas but not selected HYM values",
            ],
            "locked_target": "same q79/F,m=1 selected S3/GS branch; no observed SM constants are used to choose the solve",
            "important_type_warning": "The straight HYM object is rank-2 V_alpha, while the current B_N execution scaffold is rank-3 qutrit/family-sector data. A functorial rank2-to-sector transfer is therefore required before promotion.",
        },
        "gauge_fixed_hym_problem": {
            "formulated": True,
            "rank": 2,
            "bundle": "0 -> L -> V_alpha -> L^-1 -> 0 with selected non-exact Ext class",
            "metric_source": "selected equal-radius Gauduchon metric p=(1,1,1)",
            "unknown": "trace-free Hermitian endomorphism S or unitary connection correction a, with H=exp(S)",
            "gauge_slice": [
                "unitary connection convention",
                "trace-free determinant normalization",
                "Coulomb slice d_A^* a = 0 modulo infinitesimal unitary gauge",
                "Pic0 quotient fixed only at ordered Chern/H1/ordinary-curvature layer",
            ],
            "residual_equations": [
                "F_A^(0,2)=0 for the selected holomorphic structure",
                "Lambda_J F_A - mu(V_alpha) I = 0 in trace-free primitive part",
                "d_A^* a = 0 gauge-fixing equation",
                "metric compatibility A^*H + H A = dH",
                "Green-Schwarz/Bianchi alpha1 consistency row before operator promotion",
            ],
            "analytic_representative_emitted": analytic_representative_emitted,
        },
        "finite_newton_galerkin_contract": {
            "built": True,
            "basis_id": b_n_lift.get("basis_id"),
            "basis_dimension": basis_dimension,
            "bn_scaffold_built": bn_scaffold_built,
            "complement_gap_from_scaffold": complement_gap,
            "mesh_counts": mesh_counts,
            "unknown_blocks": {
                "rank2_HYM_connection_coefficients": "open",
                "Hermitian_metric_endomorphism_coefficients": "open",
                "rho_E_transition_tables_for_selected_connection": "open",
                "rank2_to_rank3_sector_transfer_functor": "open",
                "sector_D_E_dotD_Riesz_Green_C1_payload": "open",
            },
            "newton_iteration_schema": [
                "initialize from the split Chern connection plus the selected non-exact Ext seed",
                "project residual to trace-free primitive HYM equations and the Coulomb slice",
                "solve the finite Jacobian/Hessian system on the selected basis",
                "prove coercivity/gap for the gauge-fixed linearization",
                "emit residual norm, truncation error, and validator-ready operator tables",
            ],
            "values_emitted": finite_newton_values_emitted,
            "posteriori_error_certificate_emitted": posteriori_error_certificate_emitted,
        },
        "first_solve_attempt": {
            "attempted": True,
            "closed": first_solve_closed,
            "result": "NOT_SOLVED",
            "blocked_before_numeric_values": True,
            "direct_cause": "No selected gauge-fixed HYM connection representative or finite Newton/Galerkin coefficient vector is present in the corpus/repo artifacts.",
            "secondary_cause": "The available 27-mode B_N/qutrit scaffold has rank-3 family-sector type, so selected rank-2 HYM data still needs a theorem-derived sector-transfer functor.",
            "existing_scaffolds_used_only_as_support": {
                "B_N_scaffold_built": bn_scaffold_built,
                "D_E_scaffold_built": de_scaffold_built,
                "basis_dimension": basis_dimension,
            },
        },
        "acceptance_gate_for_promotion": {
            "must_emit": [
                "selected A_HYM or S/H coefficient vector",
                "gauge residual norm and HYM residual norm",
                "coercive gauge-fixed Jacobian/Hessian lower bound",
                "selected quadrature/truncation error bound",
                "rank2-to-sector transfer map or proof it is unnecessary",
                "rho_E, metric, D_E, Riesz/Green, dotD, and C1/overlap data replayed without lifted flags",
            ],
            "must_not_use": [
                "observed SM masses or mixings",
                "formal-lift selected flags",
                "identity smoke as selected rho_E",
                "the abstract existence theorem as a finite matrix table",
            ],
        },
        "what_closes_now": {
            "gauge_fixed_equations_formulated": True,
            "finite_newton_galerkin_contract_built": True,
            "rank2_vs_rank3_type_mismatch_exposed": True,
            "promotion_acceptance_gate_locked": True,
            "first_solve_attempt_executed": True,
        },
        "what_remains_open": {
            "selected_A_HYM_or_H_coefficients": True,
            "gauge_fixed_hym_residual_values": True,
            "coercivity_and_truncation_certificate": True,
            "rank2_HYM_to_rank3_sector_operator_functor": True,
            "selected_operator_payload_replay_without_lifted_flags": True,
            "full_SM_or_no_knob_closure": True,
        },
        "next_required_artifact": "MTT_Selected_HYM_NewtonGalerkin_FirstSolve_or_Rank2SectorFunctor_v1",
    }

    cert = {
        "certificate": "MTT_Selected_HYM_GaugeFixed_Connection_Representative_or_Galerkin_Solve_v1",
        "status": candidate["status"],
        "closure_claimed": False,
        "target_fitting_used": False,
        "gauge_fixed_equations_formulated": True,
        "finite_newton_galerkin_contract_built": True,
        "first_solve_closed": first_solve_closed,
        "rank2_to_sector_functor_emitted": rank2_to_sector_functor_emitted,
        "next_required_artifact": candidate["next_required_artifact"],
    }

    proof = """# MTT Selected HYM Gauge-Fixed Connection Representative or Galerkin Solve v1

## Claim

The next object is now specified as an executable solve gate.  Abstract HYM
existence is already imported, but the branch still lacks either:

1. an analytic selected gauge-fixed HYM representative `A_HYM`, or
2. a finite Newton/Galerkin coefficient vector with residual, coercivity, and
   truncation certificates.

No selected finite operator values are promoted in this artifact.

## Straight Path

The straight proof path is rank-2:

```text
selected V_alpha
+ selected equal-radius Gauduchon metric
+ gauge-fixed rank-2 HYM solve
=> selected A_HYM
=> selected rho_E / metric / D_E / Green / dotD / C1 payload
```

The gauge conditions are unitary convention, determinant normalization, and a
Coulomb slice modulo infinitesimal unitary gauge.  The residual equations are
the holomorphic-structure condition, primitive trace-free HYM equation, gauge
slice equation, metric compatibility, and Green-Schwarz/Bianchi consistency
row.

## Superset Support

The combined support path uses the Route-C/Strominger Galerkin spec, the smooth
`B_N` scaffold, and the finite `D_E` scaffold as execution infrastructure.  It
does not use those smoke/scaffold matrices as selected values.

The important type issue is now explicit: the HYM source is rank-2 `V_alpha`,
whereas the available 27-mode execution scaffold is rank-3 qutrit/family-sector
data.  A theorem-derived rank-2-to-sector transfer functor, or a proof that the
selected solve can be run directly in sector form, is required before promotion.

## First Attempt

The first solve attempt is executed at the proof-contract level and stops before
numeric values.  Existing artifacts contain no selected `A_HYM`, no selected
Newton coefficient vector, no selected residual values, and no selected
rank-2-to-sector transfer map.

## Next Artifact

`MTT_Selected_HYM_NewtonGalerkin_FirstSolve_or_Rank2SectorFunctor_v1`.
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
