from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "dimensionless_modal_gap_operator_reduction_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    require(
        cert["status"] == "DIMENSIONLESS_MODAL_GAP_REDUCED_TO_KAPPAS_AND_FIBER_EIGENVALUES_PHYSICAL_UNITS_OPEN",
        "unexpected status",
    )
    source = cert["source_tests"]
    reduction = cert["reduction"]
    open_data = cert["open_data"]
    guards = cert["guardrails"]

    require(source["finite_coherent_defines_Aint_sum"] is True, "A_int source form should be present")
    require(source["fixed_points_defines_lambda_A"] is True, "lambda_A source formula should be present")
    require(source["qg_links_uv_scale_to_gap"] is True, "QG UV-gap relation should be present")
    require(abs(reduction["known_internal_gap_bound"] - 0.25) < 1e-15, "lambda_star should be 0.25")
    require(abs(reduction["derived_internal_gap_energy"] - 0.5) < 1e-15, "sqrt(lambda_star) should be 0.5")
    require(abs(reduction["derived_internal_tau0_if_saturated"] - 4.0) < 1e-15, "tau0 should be 4 if saturated")
    require(open_data["selected_kappa_n"] is False, "selected kappas should remain open")
    require(open_data["proof_gap_bound_is_saturated"] is False, "saturation should remain open")
    require(open_data["physical_unit_conversion"] is False, "physical units should remain open")
    require(guards["claims_lambda_star_saturation"] is False, "must not claim saturation")
    require(guards["claims_physical_gap"] is False, "must not claim physical gap")

    print("AUDIT_PASS: dimensionless modal-gap operator reduced; selected packet and physical units remain open")


if __name__ == "__main__":
    main()
