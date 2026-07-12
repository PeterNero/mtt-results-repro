"""Build the first selected HYM adjoint-Galerkin coefficient solve attempt."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

OUT_CANDIDATE = ROOT / "candidate_data" / "selected_hym_adjoint_galerkin_first_coefficient_solve.candidate.json"
OUT_CERT = ROOT / "certificates" / "selected_hym_adjoint_galerkin_first_coefficient_solve_certificate.json"
OUT_PROOF = ROOT / "proof_corpus" / "MTT_Selected_HYM_AdjointGalerkin_FirstCoefficientSolve_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def skew3(axis: int) -> list[list[int]]:
    if axis == 0:
        return [[0, 0, 0], [0, 0, -1], [0, 1, 0]]
    if axis == 1:
        return [[0, 0, 1], [0, 0, 0], [-1, 0, 0]]
    if axis == 2:
        return [[0, -1, 0], [1, 0, 0], [0, 0, 0]]
    raise ValueError(axis)


def main() -> int:
    adjoint_path = ROOT / "candidate_data" / "selected_hym_adjoint_transfer_functor.candidate.json"
    solve_gate_path = ROOT / "candidate_data" / "selected_hym_gaugefixed_connection_or_galerkin_solve.candidate.json"
    smooth_bn_path = ROOT / "candidate_data" / "selected_routec_smooth_bn_galerkin_lift.candidate.json"
    de_bn_path = ROOT / "candidate_data" / "selected_routec_de_action_on_smooth_bn.candidate.json"

    adjoint = load(adjoint_path)
    solve_gate = load(solve_gate_path)
    smooth_bn = load(smooth_bn_path)
    de_bn = load(de_bn_path)

    basis = smooth_bn.get("B_N_lift", {}).get("basis", [])
    basis_dimension = len(basis)
    su2_generators = ["T1", "T2", "T3"]
    real_one_form_directions = ["dx1", "dy1", "dx2", "dy2", "dx3", "dy3"]

    hermitian_metric_unknowns = basis_dimension * len(su2_generators)
    connection_unknowns = basis_dimension * len(su2_generators) * len(real_one_form_directions)
    adjoint_matrices = {name: skew3(i) for i, name in enumerate(su2_generators)}

    algebraic_adjoint_basis_emitted = adjoint["what_closes_now"]["abstract_rank2_to_rank3_transfer_functor"] is True
    selected_end0_basis_identified = False
    local_differential_tables_available = False
    selected_hym_coefficients_solved = False
    residual_values_emitted = False

    first_solve_closed = all(
        [
            algebraic_adjoint_basis_emitted,
            selected_end0_basis_identified,
            local_differential_tables_available,
            selected_hym_coefficients_solved,
            residual_values_emitted,
        ]
    )

    candidate = {
        "candidate": "MTTSelectedHYMAdjointGalerkinFirstCoefficientSolve",
        "status": "MTT_SELECTED_HYM_ADJOINT_GALERKIN_FIRST_COEFFICIENT_SOLVE_ATTEMPTED_DIFFERENTIAL_TABLES_OPEN",
        "closure_claimed": False,
        "target_fitting_used": False,
        "inputs": {
            "adjoint_transfer_functor": str(adjoint_path),
            "gaugefixed_solve_gate": str(solve_gate_path),
            "smooth_BN_galerkin_lift": str(smooth_bn_path),
            "DE_action_on_smooth_BN": str(de_bn_path),
        },
        "straight_vs_superset": {
            "straight_path": "Use the selected rank-2 V_alpha HYM problem, pass through End_0(V_alpha), and solve the gauge-fixed adjoint Galerkin equations.",
            "combined_support_path": "Use the existing 27-mode qutrit B_N scaffold only as a candidate execution basis and validator shape, until it is identified with the selected End_0(V_alpha) basis.",
            "locked_target": "selected q79/F,m=1 V_alpha branch at equal radius; no observed SM constants or benchmark matrices enter the solve.",
        },
        "algebraic_adjoint_packet": {
            "emitted": algebraic_adjoint_basis_emitted,
            "basis": su2_generators,
            "normalization": "epsilon_ijk real adjoint normalization; overall physical trace normalization remains part of the later operator/threshold convention",
            "ad_matrices_on_End0_basis": adjoint_matrices,
            "commutator_rule": "[T_i,T_j]=epsilon_ijk T_k in the real adjoint convention",
            "continuous_parameters_added": 0,
        },
        "coefficient_unknown_manifest": {
            "basis_dimension_from_current_BN_support": basis_dimension,
            "real_one_form_directions": real_one_form_directions,
            "Hermitian_metric_endomorphism_coefficients": hermitian_metric_unknowns,
            "connection_one_form_coefficients": connection_unknowns,
            "total_first_newton_unknown_slots_if_connection_form_used": hermitian_metric_unknowns + connection_unknowns,
            "selected_coefficients_emitted": selected_hym_coefficients_solved,
        },
        "residual_operator_requirements": {
            "needed_before_newton_run": [
                "selected finite End_0(V_alpha) basis or proof the 27-mode B_N scaffold is it",
                "d and barpartial tables for basis modes in the selected AH/good-cover coordinates",
                "wedge/product tables for one-form and End_0 basis elements",
                "Hodge-star/Lambda_J contraction table for the selected equal-radius Gauduchon metric",
                "Cech/Ext off-diagonal representative as actual local form data, not only the 8-slot cohomology vector",
                "quadrature/integration table tied to the selected basis",
                "gauge-fixing projector and gauge-orbit nullspace basis",
            ],
            "available_now": {
                "abstract_adjoint_transfer": algebraic_adjoint_basis_emitted,
                "candidate_27_mode_BN_shape": basis_dimension == 27,
                "diagnostic_D_E_matrix_shape": de_bn.get("status"),
            },
            "missing_now": {
                "selected_End0_basis_identification": not selected_end0_basis_identified,
                "selected_local_differential_tables": not local_differential_tables_available,
                "selected_HYM_coefficients": not selected_hym_coefficients_solved,
                "selected_residual_values": not residual_values_emitted,
            },
        },
        "first_coefficient_solve_attempt": {
            "attempted": True,
            "closed": first_solve_closed,
            "result": "NOT_SOLVED",
            "why_not_solved": "The algebraic adjoint carrier is available, but the local End_0 Galerkin differential tables and selected HYM coefficient vector are not present in the repo/corpus artifacts.",
            "important_guardrail": "The split Chern connection plus Ext label can seed Newton only after the Ext class is represented by actual local forms; the 8-slot Cech vector alone is not a connection coefficient vector.",
        },
        "what_closes_now": {
            "su2_adjoint_matrices_emitted": True,
            "first_newton_unknown_dimensions_locked": True,
            "needed_differential_tables_enumerated": True,
            "cohomology_vector_not_misused_as_connection_coefficients": True,
        },
        "what_remains_open": {
            "selected_End0_basis_or_BN_identification": True,
            "selected_local_differential_product_hodge_tables": True,
            "selected_Ext_local_form_representative": True,
            "selected_HYM_Newton_solution_coefficients": True,
            "selected_operator_payload_replay_without_lifted_flags": True,
            "full_SM_or_no_knob_closure": True,
        },
        "next_required_artifact": "MTT_Selected_End0_Basis_Differential_Table_or_BN_Identification_v1",
    }

    cert = {
        "certificate": "MTT_Selected_HYM_AdjointGalerkin_FirstCoefficientSolve_v1",
        "status": candidate["status"],
        "closure_claimed": False,
        "target_fitting_used": False,
        "su2_adjoint_matrices_emitted": True,
        "first_coefficient_solve_closed": first_solve_closed,
        "selected_coefficients_emitted": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }

    proof = """# MTT Selected HYM Adjoint-Galerkin First Coefficient Solve v1

## Claim

The first coefficient solve has been attempted honestly.  The algebraic adjoint
carrier is now explicit: `End_0(V_alpha)` has the three real generators
`T1,T2,T3` with `epsilon_ijk` commutator matrices.  This adds no continuous
parameter.

The solve does not close.  The current artifacts still do not contain the
selected local differential tables needed to run Newton/Galerkin.

## Unknown Vector

At the current 27-mode support level:

```text
Hermitian metric endomorphism coefficients: 27 * 3 = 81
connection one-form coefficients:          27 * 3 * 6 = 486
total connection-form solve slots:          567
```

These are solve slots, not fitted parameters.  They must be fixed by the HYM
residual, gauge slice, selected Ext local representative, and selected
Gauduchon metric.

## Missing Tables

The next true object is not another abstract HYM theorem.  It is the selected
finite differential table for `End_0(V_alpha)`:

- selected `End_0(V_alpha)` basis, or proof that the 27-mode `B_N` scaffold is
  that basis;
- `d`, `barpartial`, wedge/product, Hodge/Lambda, quadrature, and gauge
  projector tables;
- local-form representative of the selected Ext class.

The 8-slot Cech cohomology vector is not a connection coefficient vector; it can
seed the solve only after it is represented by local forms.

## Next Artifact

`MTT_Selected_End0_Basis_Differential_Table_or_BN_Identification_v1`.
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
