from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_stf_hessian_form_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    require(
        cert["status"] == "SELECTED_STF_HESSIAN_FORM_CLOSED_POSITIVE_SCALE_OPEN",
        "unexpected status",
    )
    closed = cert["closed_tests"]
    open_tests = cert["open_tests"]
    selected = cert["selected_form"]
    guardrails = cert["guardrails"]

    require(cert["input_certificate"]["tt_basis_closed"] is True, "TT basis should be closed upstream")
    require(closed["hessian_form_closed"] is True, "Hessian form should be closed")
    require(closed["covariance_forces_equal_plus_cross_stiffness"] is True, "covariance should force equality")
    require(closed["positive_normal_form_forces_kappa_positive"] is True, "positive normal form should force kappa > 0")
    require(selected["matrix"] == [["kappa_STF", "0"], ["0", "kappa_STF"]], "unexpected selected form")
    require(open_tests["numeric_kappa_STF_computed_from_selected_MTT_data"] is False, "numeric kappa must remain open")
    require(open_tests["absolute_Newton_or_Planck_normalization_computed"] is False, "absolute normalization must remain open")
    require(guardrails["claims_numeric_kappa"] is False, "must not claim numeric kappa")
    require(guardrails["claims_full_GR_closed"] is False, "must not claim full GR closure")

    print("AUDIT_PASS: selected STF Hessian form is closed up to a positive scale")


if __name__ == "__main__":
    main()
