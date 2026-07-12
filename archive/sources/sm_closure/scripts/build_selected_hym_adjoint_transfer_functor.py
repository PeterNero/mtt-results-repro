"""Build the selected HYM adjoint-transfer functor gate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
Q79 = ROOT.parent / "mtt-q79-proof-repro"

OUT_CANDIDATE = ROOT / "candidate_data" / "selected_hym_adjoint_transfer_functor.candidate.json"
OUT_CERT = ROOT / "certificates" / "selected_hym_adjoint_transfer_functor_certificate.json"
OUT_PROOF = ROOT / "proof_corpus" / "MTT_Selected_HYM_Adjoint_Transfer_Functor_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    solve_gate_path = ROOT / "candidate_data" / "selected_hym_gaugefixed_connection_or_galerkin_solve.candidate.json"
    ordered_source_path = Q79 / "candidate_data" / "visible_rank2_l2_ordered_source.terminal_lane_hypothetical_selected.json"
    cohomology_path = Q79 / "candidate_data" / "visible_rank2_l2_pullback_cech_attempt.cohomology.json"
    smooth_bn_path = ROOT / "candidate_data" / "selected_routec_smooth_bn_galerkin_lift.candidate.json"

    solve_gate = load(solve_gate_path)
    ordered_source = load(ordered_source_path)
    cohomology = load(cohomology_path)
    smooth_bn = load(smooth_bn_path)

    target = ordered_source["target"]
    h1 = cohomology["reported_cohomology"]["h1"]
    ext_vector = cohomology["reported_cohomology"]["extension_class_vector_C1"]
    basis_dimension = len(smooth_bn.get("B_N_lift", {}).get("basis", []))

    determinant_trivial = target["L"] == [1, -2, 0] and target["L2"] == [2, -4, 0]
    rank2_hym_source_ready = solve_gate["superset_strategy"]["straight_path"]["closed_inputs"]["abstract_HYM_existence"] is True

    abstract_adjoint_transfer_closed = determinant_trivial and rank2_hym_source_ready
    finite_basis_identification_closed = False
    first_coefficients_emitted = False

    candidate = {
        "candidate": "MTTSelectedHYMAdjointTransferFunctor",
        "status": "MTT_SELECTED_HYM_ADJOINT_TRANSFER_FUNCTOR_BUILT_FINITE_IDENTIFICATION_OPEN",
        "closure_claimed": False,
        "target_fitting_used": False,
        "inputs": {
            "gaugefixed_solve_gate": str(solve_gate_path),
            "ordered_rank2_source": str(ordered_source_path),
            "cohomology_ext_packet": str(cohomology_path),
            "smooth_BN_galerkin_lift": str(smooth_bn_path),
        },
        "straight_path": {
            "rank2_source": {
                "bundle": "V_alpha",
                "rank": 2,
                "determinant": "trivial by construction: det(V_alpha)=L tensor L^-1",
                "L": target["L"],
                "L2": target["L2"],
                "h1_L2": h1,
                "selected_ext_seed_vector": ext_vector,
            },
            "functor": {
                "name": "Ad_SU2_or_End0",
                "definition": "Ad(V_alpha)=End_0(V_alpha), with induced connection ad(A) on trace-free endomorphisms",
                "rank": 3,
                "continuous_parameters_added": 0,
                "gauge_functorial": True,
                "curvature_rule": "F_ad(A)=ad(F_A)",
                "hym_residual_transfer": "If A is HYM and det(V_alpha) is fixed, the induced End_0 connection has primitive trace-free curvature by functoriality.",
                "abstract_transfer_closed": abstract_adjoint_transfer_closed,
            },
        },
        "superset_strategy": {
            "straight_component": "rank-2 selected HYM solve on V_alpha, then canonical adjoint transfer to a rank-3 operator carrier",
            "combined_component": "compare the induced rank-3 End_0 carrier with the existing qutrit/family B_N scaffold and Route-C validators",
            "locked_target": "same q79/F,m=1 selected branch; no observed flavor or gauge constants are used",
            "what_this_changes": "The rank-2-versus-rank-3 mismatch is no longer a conceptual blocker if the sector carrier is End_0(V_alpha). It becomes a finite basis/isomorphism and coefficient-emission problem.",
        },
        "finite_galerkin_layout": {
            "rank2_hessian_unknown_real_dimension_per_mode": 3,
            "rank2_Hermitian_endomorphism_unknowns_at_BN_level": 3 * basis_dimension if basis_dimension else None,
            "rank2_connection_correction_unknowns_six_real_directions": 18 * basis_dimension if basis_dimension else None,
            "adjoint_rank3_basis_dimension_from_BN_support": basis_dimension,
            "first_solve_coefficients_emitted": first_coefficients_emitted,
            "finite_basis_identification_closed": finite_basis_identification_closed,
            "missing_identification": "prove the qutrit/family 27-mode B_N scaffold is the selected finite trace of End_0(V_alpha), or replace it with the actual End_0 Galerkin basis",
        },
        "acceptance_gate": {
            "to_promote_abstract_functor": [
                "det(V_alpha)=trivial",
                "selected rank-2 HYM branch exists",
                "operator carrier declared as End_0(V_alpha) rather than an unrelated rank-3 scaffold",
            ],
            "to_promote_finite_values": [
                "selected finite basis for End_0(V_alpha)",
                "selected HYM coefficient vector or analytic A_HYM",
                "ad(A_HYM) matrix tables on that basis",
                "residual/gap/truncation certificate",
                "validator replay without lifted flags",
            ],
        },
        "what_closes_now": {
            "abstract_rank2_to_rank3_transfer_functor": abstract_adjoint_transfer_closed,
            "rank_mismatch_reduced_to_finite_basis_identification": True,
            "no_new_knob_introduced_by_transfer": True,
            "first_solve_unknown_dimensions_locked": True,
        },
        "what_remains_open": {
            "selected_HYM_coefficients_or_analytic_representative": True,
            "End0_finite_basis_identification_with_qutrit_BN": True,
            "selected_adjoint_DE_rhoE_metric_tables": True,
            "sector_routing_from_End0_to_Q_u_d_L_e_N_H": True,
            "full_SM_or_no_knob_closure": True,
        },
        "next_required_artifact": "MTT_Selected_HYM_AdjointGalerkin_FirstCoefficientSolve_v1",
    }

    cert = {
        "certificate": "MTT_Selected_HYM_Adjoint_Transfer_Functor_v1",
        "status": candidate["status"],
        "closure_claimed": False,
        "target_fitting_used": False,
        "abstract_rank2_to_rank3_transfer_functor": abstract_adjoint_transfer_closed,
        "finite_basis_identification_closed": finite_basis_identification_closed,
        "first_solve_coefficients_emitted": first_coefficients_emitted,
        "next_required_artifact": candidate["next_required_artifact"],
    }

    proof = """# MTT Selected HYM Adjoint Transfer Functor v1

## Claim

The rank mismatch is reduced.  The selected rank-2 source does not have to be
forced directly into an unrelated rank-3 scaffold.  Because
`det(V_alpha)=L tensor L^-1` is trivial, the canonical carrier

```text
Ad(V_alpha) = End_0(V_alpha)
```

is rank 3.  A selected HYM connection `A` on `V_alpha` induces the connection
`ad(A)` on `End_0(V_alpha)`, with curvature `F_ad(A)=ad(F_A)`.  Thus HYM
residual zero transfers functorially at the abstract bundle level.

This adds no continuous parameter.

## What Closes

The abstract rank-2-to-rank-3 transfer functor is available if the operator
carrier is declared as `End_0(V_alpha)`.  The previous type mismatch is now a
finite basis/isomorphism problem, not a conceptual source contradiction.

## What Remains Open

No finite operator values are emitted here.  We still need:

- the selected HYM coefficient vector or analytic representative;
- a selected finite basis for `End_0(V_alpha)`;
- proof that the existing 27-mode qutrit/family `B_N` scaffold is that selected
  finite trace, or replacement by the actual `End_0(V_alpha)` basis;
- `rho_E`, metric, `D_E`, Riesz/Green, `dotD`, and C1 replay without lifted
  flags.

## Next Artifact

`MTT_Selected_HYM_AdjointGalerkin_FirstCoefficientSolve_v1`.
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
