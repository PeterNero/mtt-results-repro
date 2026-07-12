from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

RHOE_IMPORT = ROOT / "certificates" / "routec_nonidentity_rhoe_bn_construction_import_certificate.json"
SRC_CERT = SM / "certificates" / "selected_routec_smooth_bn_galerkin_lift_certificate.json"
SRC_DATA = SM / "candidate_data" / "selected_routec_smooth_bn_galerkin_lift.candidate.json"

OUT_CERT = ROOT / "certificates" / "routec_smooth_bn_galerkin_lift_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "routec_smooth_bn_galerkin_lift_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "RouteC_Smooth_BN_Galerkin_Lift_Import_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def is_identity(matrix: list[list[float]]) -> bool:
    return all(abs(value - (1.0 if i == j else 0.0)) < 1e-12 for i, row in enumerate(matrix) for j, value in enumerate(row))


def main() -> None:
    rhoe_import = load(RHOE_IMPORT)
    src_cert = load(SRC_CERT)
    src = load(SRC_DATA)
    lift = src["B_N_lift"]
    gates = src["gates"]
    fields = src["contract_comparison"]["fields_emitted_now"]
    missing = src["contract_comparison"]["still_missing_for_full_contract"]
    straight = src["superset_mode"]["straight_path"]

    closed_now = {
        "previous_nonidentity_rhoE_imported": rhoe_import["theorem"]["proved"],
        "smooth_scalar_basis_functions_phi_m_emitted": src_cert["what_closes"]["smooth_scalar_basis_functions_phi_m_emitted"],
        "metric_quadrature_emitted": src_cert["what_closes"]["metric_quadrature_emitted"],
        "Gram_matrix_entries_emitted": src_cert["what_closes"]["Gram_matrix_entries_emitted"],
        "stiffness_matrix_entries_emitted_for_model_active_laplacian": src_cert["what_closes"]["stiffness_matrix_entries_emitted_for_model_active_laplacian"],
        "generalized_eigenpairs_emitted": src_cert["what_closes"]["generalized_eigenpairs_emitted"],
        "kernel_dimension_three_for_model_active_laplacian": src_cert["what_closes"]["kernel_dimension_three_for_model_active_laplacian"],
        "positive_model_complement_gap": src_cert["what_closes"]["positive_model_complement_gap"],
        "Riesz_and_reduced_Green_emitted_for_model_active_laplacian": src_cert["what_closes"]["Riesz_and_reduced_Green_emitted_for_model_active_laplacian"],
        "target_fitting_excluded": src_cert["what_closes"]["target_fitting_excluded"],
    }

    numeric_checks = {
        "basis_dimension_27": lift["dimension"] == 27 and len(lift["basis"]) == 27,
        "quadrature_has_9_active_deck_nodes": len(lift["quadrature_rule"]["nodes"]) == 9,
        "gram_matrix_identity": is_identity(lift["gram_matrix"]),
        "kernel_dimension_three": lift["zero_cluster"]["dimension"] == 3,
        "positive_complement_gap": lift["complement_gap"] > 0,
        "complement_gap_value_matches": abs(lift["complement_gap"] - 4.386490844928603) < 1e-12,
        "basis_extends_beyond_left_invariant_forms": gates["basis_extends_beyond_left_invariant_forms"] is True,
        "projective_equivariance_only": (
            lift["bundle_equivariance"]["ordinary_bundle_equivariance"] is False
            and lift["bundle_equivariance"]["projective_equivariance_up_to_central_phase"] is True
        ),
        "riesz_and_green_fields_emitted": fields["Riesz_projectors"] is True and fields["reduced_Green_operators"] is True,
    }

    still_open_checks = {
        "full_BN_payload_gate_open": straight["full_BN_payload_gate"] is False,
        "selected_D_E_action_open": gates["selected_D_E_action_on_basis"] is False and missing["selected_D_E_action_on_basis"] is True,
        "sector_projectors_open": gates["sector_projection_maps_constructed"] is False and missing["sector_projection_maps_constructed"] is True,
        "dotD_alpha1_open": gates["dotD_alpha1_and_Green_operator_constructed"] is False and missing["dotD_alpha1_in_same_basis"] is True,
        "full_iwasawa_truncation_error_open": (
            gates["truncation_error_certified_for_full_iwasawa_operator"] is False
            and missing["full_iwasawa_operator_truncation_error"] is True
        ),
        "honest_replay_not_ready": straight["honest_replay_ready"] is False,
        "closure_not_claimed": src["closure_claimed"] is False,
    }

    theorem = {
        "name": "RouteCSmoothBNGalerkinLiftImportTheorem",
        "proved": all(closed_now.values()) and all(numeric_checks.values()) and all(still_open_checks.values()),
        "statement": (
            "The non-identity rho_E packet admits a smooth gerbe-twisted F3^2 "
            "Fourier Galerkin scaffold with 27 modes, exact active-deck "
            "quadrature, identity Gram matrix, diagonal model stiffness, a "
            "three-dimensional zero cluster, positive complement gap, Riesz "
            "projector, and reduced Green operator. The scaffold is not yet "
            "the full selected Iwasawa/Strominger D_E basis."
        ),
    }

    verdict = {
        "smooth_BN_scaffold_built": True,
        "model_active_laplacian_payload_built": True,
        "selected_D_E_action_closed": False,
        "sector_projectors_closed": False,
        "dotD_alpha1_closed": False,
        "full_BN_payload_gate_closed": False,
        "R6_honest_replay_ready": False,
        "next_required_artifact": src["next_required_artifact"],
    }

    packet = {
        "theorem": theorem,
        "source_status": src["status"],
        "summary": {
            "basis_id": lift["basis_id"],
            "dimension": lift["dimension"],
            "zero_cluster": lift["zero_cluster"],
            "complement_gap": lift["complement_gap"],
            "bundle_equivariance": lift["bundle_equivariance"],
        },
        "closed_now": closed_now,
        "numeric_checks": numeric_checks,
        "still_open_checks": still_open_checks,
        "contract_comparison": src["contract_comparison"],
        "what_remains_open": src["what_remains_open"],
        "verdict": verdict,
    }

    note = """# Route-C Smooth B_N Galerkin Lift Import v1

## Result

The first smooth `B_N` numerical scaffold has been imported. It lifts the
finite `F3^2 x C3` twisted deck/fiber packet to a gerbe-twisted Fourier
Galerkin scaffold.

Closed in the model active-laplacian scaffold:

```text
basis dimension = 27
zero cluster dimension = 3
complement gap = 4.386490844928603
quadrature = 3 x 3 active-deck trapezoid rule
Gram matrix = identity
model stiffness = diagonal active-deck Laplacian
Riesz projector and reduced Green operator emitted
```

## Boundary

This is not the full selected Iwasawa/Strominger `B_N` payload. The remaining
objects are:

```text
selected D_E action on the smooth basis
sector projectors and ordered zero-mode bases
dotD_alpha1 in the same basis
full Iwasawa truncation-error certificate
honest R6 replay without lifted flags
```

## Status

```text
ROUTEC_SMOOTH_BN_GALERKIN_LIFT_IMPORTED_SELECTED_DE_STILL_OPEN
```

The next required artifact is:

```text
MTT_Selected_RouteC_DE_Action_on_Smooth_BN_v1
```
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(
        json.dumps(
            {
                "program": "MTT protospinor GR response proof",
                "certificate": "routec_smooth_bn_galerkin_lift_import",
                "status": "ROUTEC_SMOOTH_BN_GALERKIN_LIFT_IMPORTED_SELECTED_DE_STILL_OPEN",
                "input_certificates": {
                    "routec_nonidentity_rhoe_bn_construction_import": str(RHOE_IMPORT),
                    "selected_routec_smooth_bn_galerkin_lift": str(SRC_CERT),
                },
                "theorem": theorem,
                "closed_now": closed_now,
                "numeric_checks": numeric_checks,
                "still_open_checks": still_open_checks,
                "verdict": verdict,
                "packet_written": str(OUT_PACKET),
                "note_written": str(OUT_NOTE),
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print("STATUS: ROUTEC_SMOOTH_BN_GALERKIN_LIFT_IMPORTED_SELECTED_DE_STILL_OPEN")


if __name__ == "__main__":
    main()
