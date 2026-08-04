from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "global_tt_hessian_action_uniqueness_reduction_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    checks = cert["checks"]
    theorem = cert["theorem"]
    tiers = cert["claim_tiers"]
    guards = cert["guardrails"]

    require(all(checks.values()), "one or more global TT Hessian checks failed")
    require(
        cert["status"]
        == "GLOBAL_TT_HESSIAN_PATCHING_COORDINATE_TRANSPORT_AND_FIERZ_PAULI_UNIQUENESS_CLOSED_SELECTED_MTT_ACTION_SOURCE_OPEN",
        "global TT Hessian status changed",
    )
    require(
        theorem["part_A_global_fiber_hessian"]["proof_data"]["solution_dimension"] == 1,
        "symmetric weight-two commutant should be one-dimensional",
    )
    require(
        theorem["part_B_coordinate_transport"]["metric_coordinate_hessian"]
        == "H_h=(kappa_e/4) Id_E",
        "metric-coordinate factor changed",
    )
    require(
        theorem["part_C_action_uniqueness_reduction"]["unique_vector_up_to_scale"]
        == ["1", "-1", "1", "1", "-1"],
        "Fierz-Pauli coefficient vector changed",
    )
    require(
        tiers["selected_MTT_action_satisfies_hypotheses"] == "OPEN",
        "selected action was overpromoted",
    )
    require(
        tiers["selected_numeric_kappa_h"] == "OPEN",
        "absolute TT scale was overpromoted",
    )
    require(guards["claims_selected_MTT_action_closed"] is False, "action overclaim")
    require(guards["claims_numeric_kappa_or_Newton_constant"] is False, "normalization overclaim")
    require(guards["claims_full_GR_or_QG_closed"] is False, "full QG overclaim")

    print(
        "AUDIT_PASS: global TT Hessian form, factor-four coordinate transport, "
        "and conditional Fierz-Pauli uniqueness are exact"
    )


if __name__ == "__main__":
    main()
