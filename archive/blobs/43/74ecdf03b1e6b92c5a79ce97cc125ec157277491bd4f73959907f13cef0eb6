from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

VALUE_SOLVE = ROOT / "certificates" / "selected_hym_value_solve_attempt_certificate.json"
ADJOINT_CERT = SM / "certificates" / "selected_hym_adjoint_transfer_functor_certificate.json"
ADJOINT_PACKET = SM / "candidate_data" / "selected_hym_adjoint_transfer_functor.candidate.json"
COEFF_CERT = SM / "certificates" / "selected_hym_adjoint_galerkin_first_coefficient_solve_certificate.json"
COEFF_PACKET = SM / "candidate_data" / "selected_hym_adjoint_galerkin_first_coefficient_solve.candidate.json"

OUT_CERT = ROOT / "certificates" / "selected_hym_newton_galerkin_or_adjoint_functor_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "selected_hym_newton_galerkin_or_adjoint_functor_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "Selected_HYM_NewtonGalerkin_or_AdjointFunctor_Import_v1.md"

STATUS = "SELECTED_HYM_ADJOINT_TRANSFER_IMPORTED_FIRST_COEFFICIENT_SOLVE_TABLES_OPEN"
NEXT = "MTT_Selected_End0_Basis_Differential_Table_or_BN_Identification_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    value_solve = load(VALUE_SOLVE)
    adj_cert = load(ADJOINT_CERT)
    adj = load(ADJOINT_PACKET)
    coeff_cert = load(COEFF_CERT)
    coeff = load(COEFF_PACKET)

    manifest = coeff["coefficient_unknown_manifest"]
    residual_reqs = coeff["residual_operator_requirements"]
    finite_layout = adj["finite_galerkin_layout"]

    theorem = {
        "name": "SelectedHYMAdjointTransferAndFirstCoefficientSolveImport",
        "proved": True,
        "closure_claimed": False,
        "statement": (
            "The selected HYM value-solve gate advances through the canonical "
            "adjoint carrier. Since det(V_alpha)=L tensor L^-1 is trivial, "
            "End_0(V_alpha) is a rank-3 carrier and a selected rank-2 HYM "
            "connection A induces ad(A) with F_ad(A)=ad(F_A), adding no "
            "continuous parameter. The abstract rank-2-to-rank-3 functor is "
            "therefore available. The first coefficient solve is attempted and "
            "emits the su(2) adjoint matrices and unknown-count manifest, but "
            "does not emit selected HYM coefficients because the selected "
            "End_0 finite basis/differential/Hodge/quadrature tables are absent."
        ),
    }

    what_closes_now = {
        "abstract_rank2_to_rank3_transfer_functor": adj_cert["abstract_rank2_to_rank3_transfer_functor"] is True,
        "no_new_knob_introduced_by_transfer": adj["what_closes_now"]["no_new_knob_introduced_by_transfer"] is True,
        "rank_mismatch_reduced_to_finite_basis_identification": adj["what_closes_now"][
            "rank_mismatch_reduced_to_finite_basis_identification"
        ]
        is True,
        "su2_adjoint_matrices_emitted": coeff_cert["su2_adjoint_matrices_emitted"] is True,
        "first_newton_unknown_dimensions_locked": coeff["what_closes_now"]["first_newton_unknown_dimensions_locked"] is True,
        "cohomology_vector_not_misused_as_connection_coefficients": coeff["what_closes_now"][
            "cohomology_vector_not_misused_as_connection_coefficients"
        ]
        is True,
        "target_fitting_excluded": (
            value_solve["guardrails"]["does_not_use_observed_flavor_data"] is True
            and adj_cert["target_fitting_used"] is False
            and coeff_cert["target_fitting_used"] is False
        ),
    }

    what_remains_open = {
        "End0_finite_basis_or_BN_identification": coeff["what_remains_open"][
            "selected_End0_basis_or_BN_identification"
        ],
        "selected_local_differential_product_hodge_tables": coeff["what_remains_open"][
            "selected_local_differential_product_hodge_tables"
        ],
        "selected_Ext_local_form_representative": coeff["what_remains_open"]["selected_Ext_local_form_representative"],
        "selected_HYM_Newton_solution_coefficients": coeff["what_remains_open"][
            "selected_HYM_Newton_solution_coefficients"
        ],
        "selected_operator_payload_replay_without_lifted_flags": coeff["what_remains_open"][
            "selected_operator_payload_replay_without_lifted_flags"
        ],
    }

    promotion = {
        "abstract_transfer_promotable": adj_cert["abstract_rank2_to_rank3_transfer_functor"] is True,
        "finite_basis_identification_closed": adj_cert["finite_basis_identification_closed"],
        "first_solve_coefficients_emitted": coeff_cert["selected_coefficients_emitted"],
        "may_promote_A_selected_or_b_selected": False,
        "reason": (
            "The abstract adjoint carrier is closed, but the finite basis and "
            "differential tables required for selected coefficient emission are open."
        ),
    }

    packet = {
        "theorem": theorem,
        "imported_statuses": {
            "previous_value_solve": value_solve["status"],
            "adjoint_transfer": adj_cert["status"],
            "first_coefficient_solve": coeff_cert["status"],
        },
        "adjoint_transfer": {
            "source_rank": adj["straight_path"]["rank2_source"]["rank"],
            "carrier": adj["straight_path"]["functor"]["definition"],
            "carrier_rank": adj["straight_path"]["functor"]["rank"],
            "curvature_rule": adj["straight_path"]["functor"]["curvature_rule"],
            "continuous_parameters_added": adj["straight_path"]["functor"]["continuous_parameters_added"],
            "finite_basis_identification_closed": adj_cert["finite_basis_identification_closed"],
        },
        "first_coefficient_solve": {
            "su2_adjoint_matrices": coeff["algebraic_adjoint_packet"]["ad_matrices_on_End0_basis"],
            "unknown_manifest": manifest,
            "available_now": residual_reqs["available_now"],
            "missing_now": residual_reqs["missing_now"],
            "needed_before_newton_run": residual_reqs["needed_before_newton_run"],
            "finite_layout": finite_layout,
        },
        "promotion": promotion,
        "what_closes_now": what_closes_now,
        "what_remains_open": what_remains_open,
        "guardrails": {
            "no_observed_or_benchmark_inputs": True,
            "no_lifted_flags_promoted": True,
            "no_cech_vector_as_connection_coefficients": True,
            "no_abstract_transfer_as_finite_values": True,
        },
        "next_required_artifact": NEXT,
        "input_certificates": {
            "value_solve": str(VALUE_SOLVE),
            "adjoint_transfer": str(ADJOINT_CERT),
            "first_coefficient_solve": str(COEFF_CERT),
        },
    }

    checks = {
        "previous_value_solve_open": value_solve["legal_value_solve_closed"] is False,
        "abstract_transfer_closed": adj_cert["abstract_rank2_to_rank3_transfer_functor"] is True,
        "finite_basis_still_open": adj_cert["finite_basis_identification_closed"] is False,
        "first_coefficients_not_emitted": coeff_cert["selected_coefficients_emitted"] is False,
        "su2_adjoint_matrices_emitted": coeff_cert["su2_adjoint_matrices_emitted"] is True,
        "unknown_count_81": manifest["Hermitian_metric_endomorphism_coefficients"] == 81,
        "unknown_count_486": manifest["connection_one_form_coefficients"] == 486,
        "unknown_count_567": manifest["total_first_newton_unknown_slots_if_connection_form_used"] == 567,
        "next_artifact_matches": coeff_cert["next_required_artifact"] == NEXT,
        "all_closes_true": all(what_closes_now.values()),
        "all_open_true": all(what_remains_open.values()),
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_hym_newton_galerkin_or_adjoint_functor_import",
        "status": STATUS,
        "theorem": theorem,
        "checks": checks,
        "promotion": promotion,
        "what_closes_now": what_closes_now,
        "what_remains_open": what_remains_open,
        "next_required_artifact": NEXT,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    note = f"""# Selected HYM Newton/Galerkin or Adjoint Functor Import v1

## Result

The value-solve gate advances one level.

The rank-2 versus rank-3 mismatch is no longer a conceptual blocker: because
`det(V_alpha)=L tensor L^-1` is trivial, the canonical adjoint carrier

```text
End_0(V_alpha)
```

has rank 3. A selected HYM connection `A` induces `ad(A)`, with curvature
`F_ad(A)=ad(F_A)`. This adds no continuous parameter.

## First Coefficient Solve

The first coefficient solve is attempted in the adjoint Galerkin carrier. The
algebraic `su(2)` adjoint matrices are emitted, and the unknown manifest is now
fixed:

```text
Hermitian metric endomorphism coefficients: {manifest["Hermitian_metric_endomorphism_coefficients"]}
connection one-form coefficients:          {manifest["connection_one_form_coefficients"]}
total connection-form solve slots:          {manifest["total_first_newton_unknown_slots_if_connection_form_used"]}
```

The solve still does not emit selected coefficients. The next true object is
the selected `End_0(V_alpha)` finite basis/differential table, or a proof that
the current 27-mode `B_N` scaffold is that selected finite basis.

## Status

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
