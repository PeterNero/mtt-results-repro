from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]

OPERATOR_RELATION_CERT = ROOT / "certificates" / "gr_tt_aint_operator_relation_source_theorem_certificate.json"
STIFFNESS_CERT = ROOT / "certificates" / "gr_tt_stiffness_modal_gap_interface_certificate.json"
CONVERSION_CERT = ROOT / "certificates" / "gr_tt_aint_interface_conversion_requirements_certificate.json"
INTERFACE_PACKET = ROOT / "candidate_data" / "selected_gr_tt_aint_interface_data.template.json"

OUT_CERT = ROOT / "certificates" / "explicit_gr_tt_aint_complement_construction_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "explicit_gr_tt_aint_complement_construction.template.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    relation = load_json(OPERATOR_RELATION_CERT)
    stiffness = load_json(STIFFNESS_CERT)
    conversion = load_json(CONVERSION_CERT)
    interface_packet = load_json(INTERFACE_PACKET)

    rows = stiffness["computed_internal_tt_stiffness"]["rows"]
    nil_rows = conversion["required_conversion_tables"]["to_theta_nil_floor_lambda_0p25"]
    z64_rows = conversion["required_conversion_tables"]["to_z64_lambda_15"]

    formal_rows = []
    for row, nil_row, z64_row in zip(rows, nil_rows, z64_rows):
        formal_rows.append(
            {
                "N": row["N"],
                "Vol_int": row["Vol_int"],
                "closure_metric_normalized_lambda": 1.0,
                "action_hessian_normalized_lambda": row["kappa_STF_int"],
                "nil_floor_window_factor_if_forced": nil_row["required_conversion_c_if_lambda_equals_c_kappa"],
                "z64_window_factor_if_forced": z64_row["required_conversion_c_if_lambda_equals_c_kappa"],
            }
        )

    packet = {
        "artifact": "Explicit_GR_TT_Aint_Complement_Construction",
        "construction": {
            "domain": interface_packet["closed_structural_fields"]["domain_candidate"],
            "basis": interface_packet["closed_structural_fields"]["tt_basis"],
            "quotient": interface_packet["closed_structural_fields"]["quotiented_directions_algebraic"],
            "formal_operator_family": "A_GR_TT(eta_TT) = eta_TT * I_2 on span{TT_plus, TT_cross}",
            "why_scalar": (
                "After the TT quotient, transverse-plane rotation covariance forces any "
                "parity-even quadratic leakage/complement operator to be scalar on "
                "plus/cross."
            ),
            "lowest_positive_eigenvalue": "eta_TT",
        },
        "normalization_conventions": {
            "closure_metric_normalized": {
                "eta_TT": 1.0,
                "meaning": "Use the selected TT closure metric itself as the inner product.",
                "closed_as_formal_normalization": True,
                "closed_as_MTT_selected_modal_gap": False,
            },
            "action_hessian_normalized": {
                "eta_TT": "kappa_STF_int",
                "meaning": "Keep the action-response Hessian normalization.",
                "closed_as_internal_response_spectrum": True,
                "closed_as_MTT_selected_modal_gap": False,
            },
            "branch_window_normalized": {
                "eta_TT": "c_window * kappa_STF_int",
                "meaning": "A selected projector/window rescales the action Hessian into the A_int spectral convention.",
                "closed_as_MTT_selected_modal_gap": False,
                "requires_source_for_c_window": True,
            },
        },
        "computed_rows": formal_rows,
        "open_selection_fields": {
            "selected_normalization_convention": None,
            "selected_internal_row": None,
            "source_formula_for_eta_TT": None,
            "projector_window_chi_tau": None,
            "proof_eta_TT_matches_nil_or_z64_or_new_value": None,
        },
        "forbidden_promotions": [
            "calling closure-metric lambda=1 the physical modal gap without selected normalization",
            "calling kappa_STF_int the modal gap without A_GR_TT=H_TT source",
            "forcing nil or Z64 by choosing c_window",
        ],
    }
    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "explicit_gr_tt_aint_complement_construction",
        "status": "FORMAL_GR_TT_AINT_COMPLEMENT_CONSTRUCTED_SELECTED_NORMALIZATION_OPEN",
        "input_certificates": {
            "operator_relation_source_theorem": str(OPERATOR_RELATION_CERT),
            "gr_tt_stiffness_modal_gap_interface": str(STIFFNESS_CERT),
            "conversion_requirements": str(CONVERSION_CERT),
            "interface_packet": str(INTERFACE_PACKET),
        },
        "packet_written": str(OUT_PACKET),
        "formal_construction": packet["construction"],
        "normalization_conventions": packet["normalization_conventions"],
        "computed_rows": formal_rows,
        "closed_tests": {
            "TT_quotient_domain_closed": True,
            "rotational_covariance_forces_scalar_operator_on_TT": True,
            "formal_lowest_positive_eigenvalue_is_eta_TT": True,
            "closure_metric_normalized_spectrum_computable": True,
            "action_hessian_normalized_spectrum_computable": True,
        },
        "open_tests": {
            "eta_TT_selected_by_MTT_source": True,
            "selected_normalization_convention": True,
            "selected_internal_row": True,
            "projector_window_chi_tau": True,
            "physical_modal_gap": True,
        },
        "relation_to_previous_blocker": {
            "resolves_distinct_A_route_as_formal_family": True,
            "resolves_selected_GR_TT_modal_gap": False,
            "why_not_fully_closed": (
                "The operator family A_GR_TT(eta_TT)=eta_TT I_2 follows from the closed "
                "TT quotient and covariance, but eta_TT is exactly the missing selected "
                "normalization/projector-window datum."
            ),
            "previous_status": relation["status"],
        },
        "next_required_theorem": {
            "name": "Selected_GR_TT_Eta_Normalization_Theorem",
            "must_derive": [
                "whether the A_int inner product is closure-metric normalized, action-Hessian normalized, or window-rescaled",
                "the selected internal row or proof row-independence",
                "eta_TT in the same convention as lambda_*",
                "whether eta_TT equals 1, kappa_STF_int, nil 0.25, Z64 15, or a distinct selected value",
            ],
        },
        "guardrails": {
            "claims_selected_eta_TT": False,
            "claims_lambda_GR_TT_equals_1": False,
            "claims_lambda_GR_TT_equals_kappa_STF": False,
            "claims_lambda_GR_TT_equals_nil_floor": False,
            "claims_lambda_GR_TT_equals_z64": False,
            "claims_physical_modal_gap": False,
        },
    }

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
