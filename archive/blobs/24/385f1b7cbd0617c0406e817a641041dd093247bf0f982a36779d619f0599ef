from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "stf_hessian_scale_to_geff_relation_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    require(
        cert["status"] == "STF_HESSIAN_SCALE_TIED_TO_GEFF_ABSOLUTE_NORMALIZATION_OPEN",
        "unexpected status",
    )
    closed = cert["closed_tests"]
    open_tests = cert["open_tests"]
    guardrails = cert["guardrails"]

    require(closed["hessian_form_closed"] is True, "Hessian form should be closed")
    require(
        closed["kernel_target_supplies_quadratic_action_convention"] is True,
        "quadratic action convention should be available",
    )
    require(closed["block_template_supplies_G_eff_inverse_relation"] is True, "G_eff relation should be available")
    require(closed["kappa_is_not_independent_of_G_eff"] is True, "kappa should be tied to G_eff")
    require(open_tests["absolute_G_eff_computed_without_observed_Newton_input"] is False, "absolute G_eff remains open")
    require(open_tests["absolute_kappa_STF_computed_without_observed_GR_input"] is False, "absolute kappa remains open")
    require(guardrails["claims_new_independent_GR_knob"] is False, "should not introduce a new GR knob")
    require(guardrails["claims_full_GR_closed"] is False, "must not claim full GR closure")

    print("AUDIT_PASS: STF Hessian scale is tied to G_eff; absolute normalization remains open")


if __name__ == "__main__":
    main()
