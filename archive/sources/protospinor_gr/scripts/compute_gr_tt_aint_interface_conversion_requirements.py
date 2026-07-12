from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]

INTERFACE_CERT = ROOT / "certificates" / "gr_tt_stiffness_modal_gap_interface_certificate.json"
OUT_CERT = ROOT / "certificates" / "gr_tt_aint_interface_conversion_requirements_certificate.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def conversion_rows(stiffness_rows: list[dict[str, Any]], target_lambda: float) -> list[dict[str, Any]]:
    rows = []
    for row in stiffness_rows:
        kappa = row["kappa_STF_int"]
        rows.append(
            {
                "N": row["N"],
                "kappa_STF_int": kappa,
                "target_lambda_star": target_lambda,
                "required_conversion_c_if_lambda_equals_c_kappa": target_lambda / kappa,
            }
        )
    return rows


def main() -> None:
    interface = load_json(INTERFACE_CERT)
    stiffness_rows = interface["computed_internal_tt_stiffness"]["rows"]
    nil_lambda = interface["modal_gap_candidates_in_same_audit_context"]["theta_nil_floor_benchmark"]["lambda_star"]
    z64_lambda = interface["modal_gap_candidates_in_same_audit_context"]["z64_central_circle_exact_branch"]["lambda_star"]

    nil_rows = conversion_rows(stiffness_rows, nil_lambda)
    z64_rows = conversion_rows(stiffness_rows, z64_lambda)

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "gr_tt_aint_interface_conversion_requirements",
        "status": "AINT_INTERFACE_CONVERSION_FACTORS_COMPUTED_BRIDGE_SOURCE_OPEN",
        "input_certificates": {
            "gr_tt_stiffness_modal_gap_interface": str(INTERFACE_CERT),
        },
        "interface_ansatz_under_test": {
            "formula": "lambda_GR_TT = c_interface * kappa_STF_int",
            "meaning": (
                "If the selected GR TT spectral complement is a scalar rescaling "
                "of the TT response block in internal units, then the missing "
                "spectral-interface theorem must derive c_interface."
            ),
            "not_assumed_true": True,
        },
        "required_conversion_tables": {
            "to_theta_nil_floor_lambda_0p25": nil_rows,
            "to_z64_lambda_15": z64_rows,
        },
        "interpretation": {
            "nil_floor": (
                "Identifying the GR TT spectral gap with the nil floor would require "
                "a branch-dependent conversion factor of order 3 to 6 across the "
                "tested internal-volume rows unless the selected N row is fixed first."
            ),
            "z64_branch": (
                "Identifying the GR TT spectral gap with the Z64 value would require "
                "a much larger conversion factor of order 180 to 325 across the tested "
                "rows. This is possible only if the spectral-interface theorem derives "
                "that normalization from selected operator data."
            ),
            "row_dependence": (
                "The conversion factor depends on the selected internal volume row. "
                "Therefore the bridge must select the row/branch before importing a "
                "numerical modal gap."
            ),
        },
        "next_required_artifact": {
            "name": "Selected_GR_TT_Aint_Interface_Data",
            "required_fields": [
                "selected N or selected internal volume row",
                "operator relation between A_GR_TT and H_TT",
                "derived c_interface or proof c_interface=1",
                "quotient/projector/window used for the TT spectral complement",
                "lowest positive eigenvalue after quotienting",
            ],
        },
        "guardrails": {
            "assumes_scalar_interface_ansatz_as_fact": False,
            "claims_nil_conversion_derived": False,
            "claims_z64_conversion_derived": False,
            "claims_GR_TT_modal_gap_closed": False,
            "claims_physical_units_closed": False,
        },
    }

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
