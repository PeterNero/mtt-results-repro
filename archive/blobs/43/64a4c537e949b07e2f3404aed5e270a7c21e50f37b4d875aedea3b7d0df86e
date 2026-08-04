from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]

ABS_NORM_CERT = ROOT / "certificates" / "absolute_normalization_bridge_from_nonsm_certificate.json"
MODAL_REDUCTION_CERT = ROOT / "certificates" / "dimensionless_modal_gap_operator_reduction_certificate.json"
BRANCH_CERT = ROOT / "certificates" / "selected_aint_packet_branch_bridge_audit_certificate.json"
Z64_IDENTITY_CERT = ROOT / "certificates" / "gr_tt_aint_z64_identity_source_hunt_certificate.json"

OUT_CERT = ROOT / "certificates" / "gr_tt_stiffness_modal_gap_interface_certificate.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    abs_norm = load_json(ABS_NORM_CERT)
    modal = load_json(MODAL_REDUCTION_CERT)
    branch = load_json(BRANCH_CERT)
    z64_identity = load_json(Z64_IDENTITY_CERT)

    nil_branch = branch["branch_gap_table"][0]
    z64_branch = branch["branch_gap_table"][1]
    rows = []
    for row in abs_norm["closed_internal_units"]["computed_rows"]:
        kappa_stf = row["kappa_STF_int"]
        rows.append(
            {
                "N": row["N"],
                "Vol_int": row["Vol_int"],
                "G_eff_int": row["G_eff_int"],
                "kappa_STF_int": kappa_stf,
                "ratio_kappa_STF_to_nil_lambda_floor_0p25": kappa_stf / nil_branch["lambda_star"],
                "ratio_kappa_STF_to_z64_lambda15": kappa_stf / z64_branch["lambda_star"],
            }
        )

    stiffness_positive = all(row["kappa_STF_int"] > 0 for row in rows)
    z64_identity_closed = z64_identity["verdict"]["z64_closes_gr_gap_now"]
    selected_global_aint_closed = branch["verdict"]["selected_global_Aint_packet_closed"]

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "gr_tt_stiffness_modal_gap_interface",
        "status": "TT_STIFFNESS_INTERNAL_COMPUTED_MODAL_GAP_IDENTIFICATION_OPEN",
        "input_certificates": {
            "absolute_normalization_bridge": str(ABS_NORM_CERT),
            "dimensionless_modal_gap_operator_reduction": str(MODAL_REDUCTION_CERT),
            "selected_aint_packet_branch_bridge": str(BRANCH_CERT),
            "gr_tt_aint_z64_identity_source_hunt": str(Z64_IDENTITY_CERT),
        },
        "computed_internal_tt_stiffness": {
            "formula": "kappa_STF_int = Vol_int / (32*pi*G10_int), with G10_int=1",
            "rows": rows,
            "all_positive": stiffness_positive,
        },
        "modal_gap_candidates_in_same_audit_context": {
            "theta_nil_floor_benchmark": {
                "lambda_star": nil_branch["lambda_star"],
                "status": nil_branch["status"],
                "can_replace_GR_gap": branch["import_decisions"]["can_import_theta_nil_floor_as_selected_global_saturation"],
            },
            "z64_central_circle_exact_branch": {
                "lambda_star": z64_branch["lambda_star"],
                "status": z64_branch["status"],
                "can_replace_GR_gap": branch["import_decisions"]["can_replace_GR_modal_gap_with_z64_without_bridge"],
            },
            "selected_global_Aint_packet_closed": selected_global_aint_closed,
            "dimensionless_operator_shape_closed": modal["verdict"]["dimensionless_operator_shape_closed"],
        },
        "interface_decision": {
            "tt_response_stiffness_computed_in_internal_units": True,
            "tt_response_stiffness_is_positive": stiffness_positive,
            "tt_response_stiffness_identified_with_modal_gap": False,
            "gr_tt_Aint_identified_with_z64_tower": z64_identity_closed,
            "can_use_kappa_STF_as_Aint_lowest_eigenvalue": False,
            "reason": (
                "kappa_STF is the coefficient of the projected TT quadratic response "
                "block. lambda_* is the spectral bottom of a selected internal "
                "A_int complement after quotient/projector/window choices. They can "
                "coincide only after a source theorem identifies the TT response "
                "operator convention with the selected A_int complement."
            ),
        },
        "next_required_theorem": {
            "name": "GR_TT_Response_to_Aint_Spectral_Interface_Theorem",
            "must_show": [
                "the exact domain and inner product for the GR TT closure-strain operator",
                "the quotient/projector removing diffeomorphism, scalar, and coherence zero modes",
                "whether the resulting spectral operator is H_TT, a rescaling of H_TT, or a distinct A_int block",
                "the lowest positive eigenvalue in the same normalization as the branch gap table",
                "only then whether nil 0.25, Z64 15, kappa_STF_int, or a new number is the GR modal gap",
            ],
            "fallback_if_identity_fails": (
                "compute the distinct GR TT complement directly rather than importing "
                "the Z64 central-circle value"
            ),
        },
        "guardrails": {
            "claims_kappa_STF_is_lambda_star": False,
            "claims_z64_lambda15_is_GR_gap": False,
            "claims_nil_floor_saturates_GR_gap": False,
            "claims_physical_modal_gap": False,
            "claims_physical_Newton_constant": False,
        },
    }

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
