from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]

INTERFACE_DATA_CERT = ROOT / "certificates" / "selected_gr_tt_aint_interface_data_certificate.json"
STIFFNESS_CERT = ROOT / "certificates" / "gr_tt_stiffness_modal_gap_interface_certificate.json"
CONVERSION_CERT = ROOT / "certificates" / "gr_tt_aint_interface_conversion_requirements_certificate.json"

OUT_CERT = ROOT / "certificates" / "gr_tt_aint_operator_relation_source_theorem_certificate.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    interface = load_json(INTERFACE_DATA_CERT)
    stiffness = load_json(STIFFNESS_CERT)
    conversion = load_json(CONVERSION_CERT)

    source = interface["source_tests"]
    rows = stiffness["computed_internal_tt_stiffness"]["rows"]
    nil_table = conversion["required_conversion_tables"]["to_theta_nil_floor_lambda_0p25"]
    z64_table = conversion["required_conversion_tables"]["to_z64_lambda_15"]

    identity_branch = []
    for row in rows:
        identity_branch.append(
            {
                "N": row["N"],
                "lambda_if_A_equals_H": row["kappa_STF_int"],
                "below_nil_floor_0p25": row["kappa_STF_int"] < 0.25,
                "below_z64_15": row["kappa_STF_int"] < 15.0,
            }
        )

    route_tests = {
        "route_A_equals_H_TT": {
            "source_formula_available": source["source_derives_A_GR_TT_equals_H_TT"],
            "would_give_lambda_rows": identity_branch,
            "closed": False,
            "failure_reason": "No source formula identifies the spectral A_GR_TT complement with the response Hessian H_TT.",
        },
        "route_A_equals_c_H_TT": {
            "source_formula_available": source["source_derives_c_interface"],
            "nil_required_c_rows": nil_table,
            "z64_required_c_rows": z64_table,
            "closed": False,
            "failure_reason": "No source theorem derives c_interface or selects the GR internal row.",
        },
        "route_distinct_A_GR_TT": {
            "source_formula_available": False,
            "closed": False,
            "failure_reason": (
                "A distinct selected A_GR_TT complement remains viable, but the corpus "
                "does not yet give the explicit operator, quotient, projector/window, or spectrum."
            ),
        },
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "gr_tt_aint_operator_relation_source_theorem",
        "status": "GR_TT_AINT_OPERATOR_RELATION_THEOREM_BLOCKED_DISTINCT_COMPLEMENT_ROUTE_REQUIRED",
        "input_certificates": {
            "selected_gr_tt_aint_interface_data": str(INTERFACE_DATA_CERT),
            "gr_tt_stiffness_modal_gap_interface": str(STIFFNESS_CERT),
            "gr_tt_aint_interface_conversion_requirements": str(CONVERSION_CERT),
        },
        "source_status": {
            "coherent_projector_and_lambda_star_sourced": source["gr_source_defines_spectral_gap_lambda_star"]
            and source["gr_source_defines_observable_projection"],
            "closure_cost_hessian_sourced": source["closure_source_defines_quadratic_cost_hessian"],
            "tt_response_hessian_form_sourced_in_repo": True,
            "selected_GR_internal_row_sourced": source["source_selects_GR_internal_N_row"],
            "A_GR_TT_equals_H_TT_sourced": source["source_derives_A_GR_TT_equals_H_TT"],
            "c_interface_sourced": source["source_derives_c_interface"],
        },
        "route_tests": route_tests,
        "theorem_result": {
            "A_equals_H_route_closed": False,
            "A_equals_cH_route_closed": False,
            "distinct_A_route_closed": False,
            "GR_TT_modal_gap_closed": False,
            "most_advanced_honest_position": (
                "The TT response Hessian is closed internally, but the GR TT modal "
                "gap requires a selected spectral A_int operator. Current sources do "
                "not identify that operator with H_TT or with the Z64 branch."
            ),
        },
        "next_constructive_route": {
            "name": "Explicit_GR_TT_Aint_Complement_Construction",
            "steps": [
                "define A_GR_TT as the second variation of the coherent-sector leakage/closure functional on TT modes",
                "choose the TT quotient inner product inherited from the closure-strain Hessian or L2 projector calculus",
                "derive whether A_GR_TT commutes with the coherent projector and whether it is scalar on plus/cross",
                "compute its lowest positive eigenvalue for each candidate internal row",
                "compare the derived eigenvalue with kappa_STF, nil 0.25, and Z64 15 only after normalization is fixed",
            ],
        },
        "guardrails": {
            "claims_operator_relation_closed": False,
            "claims_A_equals_H": False,
            "claims_A_equals_cH": False,
            "claims_distinct_A_spectrum_computed": False,
            "claims_GR_TT_modal_gap_closed": False,
            "claims_Z64_GR_identity": False,
        },
    }

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
