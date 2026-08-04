from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "gr_tt_aint_interface_conversion_requirements_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    require(
        cert["status"] == "AINT_INTERFACE_CONVERSION_FACTORS_COMPUTED_BRIDGE_SOURCE_OPEN",
        "unexpected status",
    )

    ansatz = cert["interface_ansatz_under_test"]
    tables = cert["required_conversion_tables"]
    next_artifact = cert["next_required_artifact"]
    guards = cert["guardrails"]

    nil_rows = tables["to_theta_nil_floor_lambda_0p25"]
    z64_rows = tables["to_z64_lambda_15"]
    require(ansatz["not_assumed_true"] is True, "ansatz must be marked as unproved")
    require(len(nil_rows) == len(z64_rows) >= 3, "expected matching conversion rows")
    require(all(row["required_conversion_c_if_lambda_equals_c_kappa"] > 0 for row in nil_rows), "nil factors positive")
    require(all(row["required_conversion_c_if_lambda_equals_c_kappa"] > 0 for row in z64_rows), "Z64 factors positive")
    require(
        all(
            z64["required_conversion_c_if_lambda_equals_c_kappa"]
            > nil["required_conversion_c_if_lambda_equals_c_kappa"]
            for nil, z64 in zip(nil_rows, z64_rows)
        ),
        "Z64 conversion should exceed nil conversion for same row",
    )
    require(next_artifact["name"] == "Selected_GR_TT_Aint_Interface_Data", "wrong next artifact")
    require(guards["assumes_scalar_interface_ansatz_as_fact"] is False, "must not assume scalar ansatz")
    require(guards["claims_nil_conversion_derived"] is False, "nil conversion must remain underived")
    require(guards["claims_z64_conversion_derived"] is False, "Z64 conversion must remain underived")
    require(guards["claims_GR_TT_modal_gap_closed"] is False, "GR TT modal gap must remain open")

    print("AUDIT_PASS: GR TT/Aint conversion factors computed; bridge source remains open")


if __name__ == "__main__":
    main()
