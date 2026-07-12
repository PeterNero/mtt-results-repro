from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

PREVIOUS = ROOT / "certificates" / "selected_end0_hym_hodge_quadrature_projector_table_certificate.json"
PREVIOUS_PACKET = ROOT / "candidate_data" / "selected_end0_hym_hodge_quadrature_projector_table.packet.json"
SM_OVERLAP = SM / "candidate_data" / "selected_ext_overlap_hym_hodge_projector_table.candidate.json"
SM_FIRST_HYM = SM / "candidate_data" / "selected_nonlinear_hym_correction_coefficient_solve.candidate.json"
SM_FIRST_HYM_CERT = SM / "certificates" / "selected_nonlinear_hym_correction_coefficient_solve_certificate.json"

OUT_CERT = ROOT / "certificates" / "selected_hym_correction_and_gauge_projector_value_table_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "selected_hym_correction_and_gauge_projector_value_table.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "Selected_HYM_Correction_and_Gauge_Projector_Value_Table_v1.md"

STATUS = "SELECTED_HYM_FIRST_TRACEFREE_CORRECTION_IMPORTED_FULL_GAUGE_PROJECTOR_OPEN"
NEXT = "MTT_Selected_Full_ExpS_HYM_Newton_Replay_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    previous = load(PREVIOUS)
    previous_packet = load(PREVIOUS_PACKET)
    overlap = load(SM_OVERLAP)
    first_hym = load(SM_FIRST_HYM)
    first_hym_cert = load(SM_FIRST_HYM_CERT)

    row_projector = overlap["gauge_projector_table"]
    solution = first_hym["solution_summary"]
    nonlinear = first_hym["nonlinear_newton_status"]
    finite_problem = first_hym["finite_problem"]

    row_level_value_table = {
        "selected_row": overlap["selected_row"],
        "transition_overlap_table_closed": overlap["transition_overlap_table"]["closed"],
        "harmonic_row_closed": overlap["global_Dolbeault_harmonic_representative"][
            "closed_at_row_level"
        ],
        "Hodge_Lambda_row_table_closed": overlap["Hodge_Lambda_table"]["closed_for_eta_row"],
        "row_projector_name": row_projector["projector_name"],
        "row_projector_formula": row_projector["formula"],
        "matrix_on_eta00_plus_complement": row_projector[
            "matrix_on_basis_eta00_plus_complement"
        ],
        "full_connection_gauge_projector": False,
        "why_limited": (
            "This is the rank-one harmonic eta_00 row projector. It is not the "
            "Coulomb projector for the full nonlinear HYM connection coefficient "
            "space."
        ),
    }

    first_tracefree_hym_correction = {
        "linearized_equation": finite_problem["linearized_HYM_equation_solved"],
        "mesh": finite_problem["mesh"],
        "domain": finite_problem["domain"],
        "mean_density": finite_problem["mean_density"],
        "poisson_residual_l2": solution["poisson_residual_l2"],
        "phi_l2": solution["phi_l2"],
        "phi_min": solution["phi_min"],
        "phi_max": solution["phi_max"],
        "phi_mean_abs": solution["phi_mean_abs"],
        "selected_End0_direction": first_hym["coefficient_packet"]["selected_end0_direction"],
        "correction_interpretation": finite_problem["correction_interpretation"],
        "top_source_fourier_modes": solution["top_source_fourier_modes"],
        "first_tracefree_correction_closed": solution["first_tracefree_correction_closed"],
        "full_selected_A_HYM_coefficients_emitted": nonlinear[
            "full_selected_A_HYM_coefficients_emitted"
        ],
    }

    full_connection_projector_gate = {
        "candidate_slice": previous_packet["gauge_projector_table"]["candidate_slice"],
        "algebraic_End0_basis": previous_packet["gauge_projector_table"]["algebraic_End0_basis"],
        "row_projector_values_emitted": row_projector["closed_for_eta_row"],
        "full_connection_projector_values_emitted": False,
        "requires": [
            "full exp(S) nonlinear HYM correction coefficients",
            "linearized HYM Jacobian at the selected nonlinear solution",
            "selected finite inner-product matrix on End0-valued coefficient space",
            "Coulomb/unitary gauge operator and its Moore-Penrose or exact finite inverse",
        ],
        "reason_open": (
            "The first scalar trace-free correction supplies an honest selected "
            "HYM value, but the full finite gauge projector acts on all selected "
            "connection coefficients after the nonlinear Newton replay. The row "
            "projector P_eta_00 cannot be promoted to that object."
        ),
    }

    packet = {
        "theorem": {
            "name": "SelectedHYMFirstCorrectionAndRowProjectorImport",
            "proved": True,
            "closure_claimed": False,
            "statement": (
                "The selected End0 route imports the row-level eta_00 overlap/"
                "Hodge/projector table and the first selected trace-free HYM "
                "correction solve. The selected density source |eta_00^unit|^2 "
                "has unit mean, the zero-mean Poisson correction is solved to "
                "sub-1e-12 residual, and the forced trace-free direction is T3. "
                "This does not yet emit the full nonlinear HYM connection or the "
                "full finite gauge projector."
            ),
        },
        "row_level_value_table": row_level_value_table,
        "first_tracefree_hym_correction": first_tracefree_hym_correction,
        "full_connection_projector_gate": full_connection_projector_gate,
        "nonlinear_newton_status": nonlinear,
        "what_closes_now": {
            "previous_gate_requested_hym_correction_and_projector_values": previous[
                "next_required_artifact"
            ]
            == "MTT_Selected_HYM_Correction_and_Gauge_Projector_Value_Table_v1",
            "eta00_transition_overlap_table_imported": row_level_value_table[
                "transition_overlap_table_closed"
            ],
            "eta00_rank_one_row_projector_imported": row_projector["closed_for_eta_row"],
            "eta00_harmonic_hodge_row_imported": row_level_value_table[
                "harmonic_row_closed"
            ]
            and row_level_value_table["Hodge_Lambda_row_table_closed"],
            "first_tracefree_hym_density_source_computed": first_tracefree_hym_correction[
                "first_tracefree_correction_closed"
            ],
            "zero_mean_poisson_correction_solved": solution["poisson_residual_l2"] < 1e-12
            and solution["phi_mean_abs"] < 1e-14,
            "selected_T3_direction_identified": first_tracefree_hym_correction[
                "selected_End0_direction"
            ]
            == "T3",
            "no_observed_or_benchmark_targets_used": first_hym["target_fitting_used"] is False
            and overlap["target_fitting_used"] is False,
        },
        "what_remains_open": {
            "full_nonlinear_expS_Newton_iteration": nonlinear[
                "full_expS_nonlinear_iteration_run"
            ]
            is False,
            "quadratic_curvature_terms": nonlinear["quadratic_curvature_terms_included"]
            is False,
            "coercivity_and_truncation_certificate": nonlinear[
                "coercive_jacobian_bound_emitted"
            ]
            is False
            and nonlinear["a_posteriori_truncation_error_emitted"] is False,
            "full_selected_A_HYM_coefficients": nonlinear[
                "full_selected_A_HYM_coefficients_emitted"
            ]
            is False,
            "full_connection_gauge_projector_values": not full_connection_projector_gate[
                "full_connection_projector_values_emitted"
            ],
            "validator_ready_finite_operator_payload": nonlinear[
                "newton_ready_for_operator_extraction"
            ]
            is False,
        },
        "guardrails": {
            "does_not_promote_row_projector_to_full_connection_projector": True,
            "does_not_promote_first_poisson_step_to_full_HYM_connection": True,
            "does_not_use_observed_or_benchmark_data": True,
            "keeps_shared_circle_degree_zero_spectator": overlap["selected_row"][
                "central_shared_circle_factor"
            ]
            == 1,
            "uses_selected_same_branch_eta00_unit_row": overlap["selected_row"]["row_id"]
            == "eta_00",
        },
        "input_artifacts": {
            "previous": str(PREVIOUS),
            "previous_packet": str(PREVIOUS_PACKET),
            "sm_overlap_projector": str(SM_OVERLAP),
            "sm_first_hym_correction": str(SM_FIRST_HYM),
            "sm_first_hym_correction_certificate": str(SM_FIRST_HYM_CERT),
        },
        "next_required_artifact": NEXT,
    }

    checks = {
        "previous_status_matches": previous["status"]
        == "SELECTED_END0_HODGE_QUADRATURE_TABLE_BUILT_HYM_PROJECTOR_VALUES_OPEN",
        "overlap_status_matches": overlap["status"]
        == "MTT_SELECTED_EXT_OVERLAP_HODGE_PROJECTOR_TABLE_BUILT_NONLINEAR_HYM_CORRECTION_OPEN",
        "first_hym_status_matches": first_hym["status"]
        == "MTT_SELECTED_HYM_FIRST_TRACEFREE_CORRECTION_SOLVED_FULL_NONLINEAR_NEWTON_OPEN",
        "certificate_matches_candidate": first_hym_cert["first_tracefree_correction_closed"]
        == solution["first_tracefree_correction_closed"],
        "mean_density_unit": abs(finite_problem["mean_density"] - 1.0) < 1e-12,
        "poisson_residual_small": solution["poisson_residual_l2"] < 1e-12,
        "row_projector_matrix_rank_one": row_projector[
            "matrix_on_basis_eta00_plus_complement"
        ]
        == [[1.0, 0.0], [0.0, 0.0]],
        "full_connection_projector_open": full_connection_projector_gate[
            "full_connection_projector_values_emitted"
        ]
        is False,
        "all_closes_true": all(packet["what_closes_now"].values()),
        "all_open_true": all(packet["what_remains_open"].values()),
        "all_guardrails_true": all(packet["guardrails"].values()),
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_hym_correction_and_gauge_projector_value_table",
        "status": STATUS,
        "closure_claimed": False,
        "checks": checks,
        "first_tracefree_hym_correction": {
            "mean_density": finite_problem["mean_density"],
            "poisson_residual_l2": solution["poisson_residual_l2"],
            "phi_l2": solution["phi_l2"],
            "selected_End0_direction": first_tracefree_hym_correction[
                "selected_End0_direction"
            ],
        },
        "row_projector_imported": True,
        "full_connection_projector_values_emitted": False,
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "next_required_artifact": NEXT,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    note = f"""# Selected HYM Correction and Gauge Projector Value Table v1

## Result

The selected route now has one honest HYM correction value packet, but not the
full nonlinear connection.

Imported row projector:

```text
P_eta_00(v)=<eta_00^unit,v> eta_00^unit
matrix on <eta_00, complement> = [[1,0],[0,0]]
```

Imported first trace-free HYM correction:

```text
rho = |eta_00^unit|^2
mean(rho) = {finite_problem["mean_density"]:.16g}
Delta phi = rho - 1,  mean(phi)=0
||Delta phi - (rho - 1)||_L2 = {solution["poisson_residual_l2"]:.3e}
S_1 = phi * T3
```

The selected direction is `T3`, with `||phi||_L2 =
{solution["phi_l2"]:.16g}` on the imported `{finite_problem["mesh"]}^4`
FFT/Galerkin table.

## Boundary

This is not the full nonlinear HYM connection and not the full finite gauge
projector.  The row projector is a harmonic seed projector; the full gauge
projector needs the nonlinear `exp(S)` solution, its HYM Jacobian, and the
selected finite coefficient-space inner product.

Status:

```text
{STATUS}
```

Next:

```text
{NEXT}
```
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
