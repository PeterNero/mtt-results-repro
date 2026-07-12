from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
NONSM = ROOT.parent / "mtt-nonsm-constants-no-knob"

COMPLEMENT_CERT = ROOT / "certificates" / "explicit_gr_tt_aint_complement_construction_certificate.json"
MODAL_CERT = ROOT / "certificates" / "dimensionless_modal_gap_operator_reduction_certificate.json"
PHYSICAL_ACTION_CERT = NONSM / "certificates" / "physical_action_normalization_gate_certificate.json"
RHO_UV_NORM_CERT = NONSM / "certificates" / "selected_rho_uv_coefficient_normalization_route_certificate.json"
SUPERSET_CERT = NONSM / "certificates" / "superset_rho_uv_cross_encoding_gate_certificate.json"

OUT_CERT = ROOT / "certificates" / "selected_gr_tt_eta_normalization_theorem_certificate.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    complement = load_json(COMPLEMENT_CERT)
    modal = load_json(MODAL_CERT)
    physical_action = load_json(PHYSICAL_ACTION_CERT)
    rho_uv_norm = load_json(RHO_UV_NORM_CERT)
    superset = load_json(SUPERSET_CERT)

    conventions = complement["normalization_conventions"]
    rows = complement["computed_rows"]

    route_decisions = {
        "closure_metric_eta_1": {
            "value": 1.0,
            "mathematically_valid_convention": conventions["closure_metric_normalized"]["closed_as_formal_normalization"],
            "selected_by_MTT_source": False,
            "closes_modal_gap": False,
            "reason": "Unit Rayleigh quotient follows only after choosing the TT closure metric as the spectral inner product.",
        },
        "action_hessian_eta_kappa_STF": {
            "values_by_row": [
                {"N": row["N"], "eta_TT": row["action_hessian_normalized_lambda"]} for row in rows
            ],
            "mathematically_valid_internal_response_spectrum": conventions["action_hessian_normalized"][
                "closed_as_internal_response_spectrum"
            ],
            "selected_by_MTT_source": False,
            "closes_modal_gap": False,
            "reason": "The physical action normalization is an internal action-unit convention and does not itself define the A_int spectral-window normalization.",
        },
        "branch_window_eta_c_kappa_STF": {
            "candidate": "eta_TT = c_window * kappa_STF_int",
            "selected_by_MTT_source": False,
            "closes_modal_gap": False,
            "reason": "This is the only route that can connect eta_TT to nil/Z64-style lambda_* values, but c_window and the selected row are unsourced.",
        },
    }

    cross_encoding_lessons = {
        "canonical_internal_action_units_closed": physical_action["verdict"][
            "canonical_internal_action_normalization_closed"
        ],
        "physical_absolute_no_go": physical_action["verdict"]["no_go_without_external_dimensional_anchor"],
        "coefficient_row_metric_can_close_when_source_selects_inner_product": rho_uv_norm["verdict"][
            "G11_closed_for_coefficient_response_problem"
        ],
        "normalization_ratios_require_same_selected_inner_product": "same selected inner product"
        in superset["verdict"]["remaining_gate"],
        "GR_TT_has_same_kind_of_inner_product_gate": True,
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_gr_tt_eta_normalization_theorem",
        "status": "ETA_NORMALIZATION_DECISION_CLOSED_SELECTED_VALUE_OPEN",
        "input_certificates": {
            "explicit_gr_tt_aint_complement": str(COMPLEMENT_CERT),
            "dimensionless_modal_gap_operator_reduction": str(MODAL_CERT),
            "physical_action_normalization": str(PHYSICAL_ACTION_CERT),
            "rho_uv_coefficient_normalization": str(RHO_UV_NORM_CERT),
            "superset_rho_uv_cross_encoding_gate": str(SUPERSET_CERT),
        },
        "closed_decision": {
            "formal_operator_shape": complement["formal_construction"]["formal_operator_family"],
            "lowest_eigenvalue_symbol": complement["formal_construction"]["lowest_positive_eigenvalue"],
            "eta_TT_is_the_only_remaining_dimensionless_GR_TT_modal_gap_scalar": True,
            "eta_TT_cannot_be_selected_by_convention": True,
            "branch_window_route_is_required_for_nil_or_z64_identification": True,
        },
        "route_decisions": route_decisions,
        "cross_encoding_lessons": cross_encoding_lessons,
        "source_tests": {
            "Aint_operator_shape_closed": modal["verdict"]["dimensionless_operator_shape_closed"],
            "selected_projector_window_chi_tau_open": modal["open_data"][
                "selected_projector_window_chi_tau_on_physical_quotient"
            ]
            is False,
            "selected_kappa_n_open": modal["open_data"]["selected_kappa_n"] is False,
            "selected_fiber_lambda_open": modal["open_data"]["selected_fiber_lambda_n_on_rhoUV_branch"]
            is False,
        },
        "no_go_for_shortcuts": {
            "eta_equals_1_as_prediction": True,
            "eta_equals_kappa_STF_as_modal_gap_without_source": True,
            "eta_equals_nil_floor_by_window_choice": True,
            "eta_equals_z64_by_window_choice": True,
        },
        "remaining_exact_gate": {
            "name": "Selected_TT_Projector_Window_Normalization_Lemma",
            "must_supply": [
                "the TT spectral inner product in the same convention as A_int",
                "the selected projector/window chi,tau on the TT quotient",
                "the selected internal row or proof row-independence",
                "the derived c_window, or a proof that c_window=1 in the A_int convention",
            ],
            "then_eta_TT": "eta_TT = c_window * kappa_STF_int, or eta_TT = 1 if the source proves closure-metric normalization is the A_int convention",
        },
        "guardrails": {
            "claims_eta_TT_numeric_selected": False,
            "claims_eta_TT_equals_1": False,
            "claims_eta_TT_equals_kappa_STF": False,
            "claims_eta_TT_equals_nil_or_z64": False,
            "claims_GR_TT_modal_gap_closed": False,
            "claims_physical_modal_gap_closed": False,
        },
    }

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
