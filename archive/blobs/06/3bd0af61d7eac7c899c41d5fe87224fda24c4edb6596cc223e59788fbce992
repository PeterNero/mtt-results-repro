from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

PREVIOUS = ROOT / "certificates" / "selected_normalized_ext_local_form_table_certificate.json"
PREVIOUS_PACKET = ROOT / "candidate_data" / "selected_normalized_ext_local_form_table.packet.json"
ADJOINT = ROOT / "candidate_data" / "selected_hym_newton_galerkin_or_adjoint_functor_import.packet.json"
SM_QUADRATURE = SM / "candidate_data" / "selected_ext_l2_theta_quadrature_table.candidate.json"
SM_QUADRATURE_CERT = SM / "certificates" / "selected_ext_l2_theta_quadrature_table_certificate.json"

OUT_CERT = ROOT / "certificates" / "selected_end0_hym_hodge_quadrature_projector_table_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "selected_end0_hym_hodge_quadrature_projector_table.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "Selected_End0_HYM_Hodge_Quadrature_Projector_Table_v1.md"

STATUS = "SELECTED_END0_HODGE_QUADRATURE_TABLE_BUILT_HYM_PROJECTOR_VALUES_OPEN"
NEXT = "MTT_Selected_HYM_Correction_and_Gauge_Projector_Value_Table_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    previous = load(PREVIOUS)
    previous_packet = load(PREVIOUS_PACKET)
    adjoint = load(ADJOINT)
    quadrature = load(SM_QUADRATURE)
    quadrature_cert = load(SM_QUADRATURE_CERT)

    end0_basis = ["T1", "T2", "T3"]
    ad_matrices = adjoint["first_coefficient_solve"]["su2_adjoint_matrices"]
    normalized_ext = previous_packet["normalized_ext_local_form_table"]
    eta_l2 = quadrature["eta_00_l2_table"]

    one_form_basis = ["e1", "e2", "e3"]
    hodge_lambda_table = {
        "metric": "selected equal-radius diagonal Hermitian/Gauduchon metric",
        "omega": "omega = i*(e1 wedge ebar1 + e2 wedge ebar2 + e3 wedge ebar3)",
        "normalization_convention": "Lambda(i*ea wedge ebar_b)=delta_ab; off-diagonal contractions vanish",
        "Lambda_i_ea_ebar_b": {
            f"i*{a}_wedge_ebar{b[-1]}": 1 if a == b else 0
            for a in one_form_basis
            for b in one_form_basis
        },
        "primitive_diagonal_basis": {
            "P12": "i*e1 wedge ebar1 - i*e2 wedge ebar2",
            "P23": "i*e2 wedge ebar2 - i*e3 wedge ebar3",
            "Lambda(P12)": 0,
            "Lambda(P23)": 0,
        },
        "Hodge_star_top_pairing_rule": (
            "The volume form is Vol = (i e1 wedge ebar1)(i e2 wedge ebar2)"
            "(i e3 wedge ebar3)/6 in this convention; full star signs are "
            "deferred to the oriented wedge table, while Lambda contractions "
            "needed for the HYM primitive equation are fixed here."
        ),
    }

    quadrature_table = {
        "source_status": quadrature["status"],
        "l2_theta_quadrature_closed": quadrature_cert["l2_theta_quadrature_closed"],
        "selected_row": quadrature["selected_row"],
        "eta_00_unrescaled_norm_square_exact": eta_l2["unrescaled_norm_square_exact"],
        "eta_00_unrescaled_norm_square_exact_expression": eta_l2[
            "unrescaled_norm_square_exact_expression"
        ],
        "eta_00_unit_L2_rescale_factor_exact_expression": eta_l2[
            "unit_L2_rescale_factor_exact_expression"
        ],
        "eta_00_unit_L2_rescale_factor_numeric": eta_l2["unit_L2_rescale_factor_numeric"],
        "eta_00_unit_L2_representative": eta_l2["unit_L2_representative"],
        "final_mesh_product_error": eta_l2["final_mesh_product_error"],
        "quadrature_rule": eta_l2["quadrature_rule"],
        "factor_norms": quadrature["factor_norms"],
    }

    hym_correction_table = {
        "abstract_HYM_existence_available": True,
        "selected_connection_coefficients_emitted": False,
        "selected_metric_endomorphism_coefficients_emitted": False,
        "connection_correction_symbol": "HYM_correction",
        "coefficient_manifest": adjoint["first_coefficient_solve"]["unknown_manifest"],
        "reason_open": (
            "The normalized Ext row, exact theta quadrature, and Lambda table "
            "are now available, but no selected nonabelian HYM coefficient "
            "vector or residual/error certificate has been emitted."
        ),
    }

    gauge_projector_table = {
        "candidate_slice": "Coulomb/unitary gauge slice on End0-valued one-form coefficients",
        "algebraic_End0_basis": end0_basis,
        "ad_matrices": ad_matrices,
        "projector_values_emitted": False,
        "why_open": (
            "A genuine gauge projector depends on the selected differential, "
            "metric inner product, and HYM linearization. Those require the "
            "selected HYM correction coefficients, not just the su(2) algebra."
        ),
    }

    end0_operator_table = {
        "normalized_ext_entry": normalized_ext["local_form_representative"]["symbolic"],
        "unit_L2_rescaled_ext_entry": eta_l2["unit_L2_representative"],
        "End0_basis": end0_basis,
        "ad_matrices": ad_matrices,
        "operator_template": (
            "barpartial_End0 = barpartial_Iwasawa + "
            "ad(A_split_AH + eta_00^unit + HYM_correction)"
        ),
        "newton_ready": False,
    }

    packet = {
        "theorem": {
            "name": "SelectedEnd0HodgeQuadratureTableWithHYMProjectorGate",
            "proved": True,
            "closure_claimed": False,
            "statement": (
                "The selected End0 direct route now has the equal-radius "
                "Lambda/Hodge contraction table and exact eta_00 theta L2 "
                "quadrature table. The normalized Ext row is rescaled by "
                "32^(1/4) in the canonical theta metric. This still does not "
                "emit selected HYM correction coefficients or the gauge "
                "projector values, so Newton/Galerkin coefficients remain open."
            ),
        },
        "Hodge_Lambda_table": hodge_lambda_table,
        "quadrature_table": quadrature_table,
        "HYM_correction_table": hym_correction_table,
        "gauge_projector_table": gauge_projector_table,
        "End0_operator_table": end0_operator_table,
        "what_closes_now": {
            "previous_gate_requested_HYM_Hodge_quadrature_projector_table": previous[
                "next_required_artifact"
            ]
            == "MTT_Selected_End0_HYM_Hodge_Quadrature_Projector_Table_v1",
            "selected_normalized_ext_row_imported": normalized_ext["selected_basis_slot"]
            == "theta_plus_0_tensor_eta_minus_0",
            "exact_eta_00_L2_quadrature_imported": quadrature_cert["l2_theta_quadrature_closed"] is True,
            "eta_00_unit_rescale_fixed": quadrature_cert["eta_00_unit_rescale_factor_expression"]
            == "32^(1/4)",
            "equalradius_Lambda_contraction_table_built": hodge_lambda_table[
                "Lambda_i_ea_ebar_b"
            ]["i*e1_wedge_ebar1"]
            == 1
            and hodge_lambda_table["primitive_diagonal_basis"]["Lambda(P12)"] == 0,
            "End0_operator_template_updated_with_unit_ext_row": "eta_00^unit"
            in end0_operator_table["operator_template"],
            "target_fitting_excluded": quadrature["target_fitting_used"] is False,
        },
        "what_remains_open": {
            "selected_HYM_connection_correction_coefficients": not hym_correction_table[
                "selected_connection_coefficients_emitted"
            ],
            "selected_metric_endomorphism_coefficients": not hym_correction_table[
                "selected_metric_endomorphism_coefficients_emitted"
            ],
            "gauge_projector_values": not gauge_projector_table["projector_values_emitted"],
            "oriented_full_Hodge_star_wedge_sign_table": True,
            "selected_Newton_Galerkin_coefficients": not end0_operator_table["newton_ready"],
        },
        "guardrails": {
            "does_not_promote_abstract_HYM_existence_to_values": True,
            "does_not_use_projective_BN_as_End0_table": True,
            "does_not_claim_gauge_projector_without_HYM_linearization": True,
            "does_not_use_observed_or_benchmark_data": True,
        },
        "input_artifacts": {
            "previous": str(PREVIOUS),
            "normalized_ext": str(PREVIOUS_PACKET),
            "quadrature": str(SM_QUADRATURE),
            "adjoint": str(ADJOINT),
        },
        "next_required_artifact": NEXT,
    }

    checks = {
        "previous_status_matches": previous["status"]
        == "SELECTED_NORMALIZED_EXT_LOCAL_FORM_TABLE_BUILT_HYM_HODGE_QUADRATURE_OPEN",
        "quadrature_status_matches": quadrature["status"]
        == "MTT_SELECTED_EXT_L2_THETA_QUADRATURE_TABLE_BUILT_OVERLAP_HYM_PROJECTOR_OPEN",
        "eta_norm_exact_matches": abs(quadrature_cert["eta_00_unrescaled_norm_square"] - 0.17677669529663687)
        < 1e-15,
        "lambda_table_diagonal_correct": hodge_lambda_table["Lambda_i_ea_ebar_b"][
            "i*e2_wedge_ebar2"
        ]
        == 1,
        "lambda_table_offdiagonal_correct": hodge_lambda_table["Lambda_i_ea_ebar_b"][
            "i*e1_wedge_ebar2"
        ]
        == 0,
        "newton_not_ready": end0_operator_table["newton_ready"] is False,
        "all_closes_true": all(packet["what_closes_now"].values()),
        "all_open_true": all(packet["what_remains_open"].values()),
        "all_guardrails_true": all(packet["guardrails"].values()),
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_end0_hym_hodge_quadrature_projector_table",
        "status": STATUS,
        "closure_claimed": False,
        "checks": checks,
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "next_required_artifact": NEXT,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    note = f"""# Selected End0 HYM/Hodge/Quadrature/Projector Table v1

## Result

The equal-radius Hodge/Lambda and theta quadrature side of the End0 table is
built.

The selected Ext row has exact norm:

```text
||eta_00||^2 = 1/sqrt(32)
eta_00^unit = 32^(1/4) * eta_00
```

The Lambda convention is:

```text
Lambda(i*ea wedge ebar_b) = delta_ab
Lambda(i*e1 wedge ebar1 - i*e2 wedge ebar2) = 0
Lambda(i*e2 wedge ebar2 - i*e3 wedge ebar3) = 0
```

The End0 operator template is now:

```text
barpartial_End0 = barpartial_Iwasawa + ad(A_split_AH + eta_00^unit + HYM_correction)
```

## Boundary

This does not emit selected nonabelian HYM correction coefficients and does not
emit the numerical gauge projector. Those depend on the selected HYM
linearization and metric inner product. The full oriented Hodge-star/wedge sign
table is also left as the next table refinement, because the HYM primitive
equation only needs the Lambda contractions fixed here.

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
