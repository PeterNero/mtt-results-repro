from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "closure_to_einstein_action_reduction_certificate.json"
NOTE = ROOT / "proof_corpus" / "Closure_to_Einstein_Action_Reduction_and_One_Scale_NoGo_v1.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    checks = cert["checks"]
    theorem = cert["theorem"]
    tiers = cert["claim_tiers"]
    guards = cert["guardrails"]

    require(all(checks.values()), "one or more closure-to-Einstein checks failed")
    require(
        cert["status"]
        == "CLOSURE_HESSIAN_RECIPROCITY_NONLINEAR_EINSTEIN_STRESS_REDUCTION_AND_ONE_SCALE_NOGO_CLOSED_SELECTED_SPACETIME_ACTION_SCALE_AND_LAMBDA_OPEN",
        "closure-to-Einstein status changed",
    )
    require(
        tiers["finite_closure_Hessian_self_adjointness"]
        == "CLOSED_FROM_C3_SCALAR_FUNCTIONAL",
        "finite Hessian reciprocity was lost",
    )
    require(
        tiers["four_dimensional_nonlinear_metric_completion"]
        == "CLOSED_UNIQUE_CONDITIONAL_ON_LOVELOCK_HYPOTHESES",
        "nonlinear completion tier changed",
    )
    require(
        theorem["part_C_stress_and_coefficient"]["field_equation"]
        == "G_mn+Lambda g_mn=(4*kappa_h)^(-1) T_mn",
        "stress coefficient changed",
    )
    require(
        theorem["part_E_scale_no_go"]["transformations"]["V6"]
        == "V6 -> r^6 V6",
        "six-volume scaling changed",
    )
    require(
        tiers["scale_free_q79_data_fix_numeric_kappa_h"] == "CLOSED_NO_GO",
        "scale no-go was weakened or overpromoted",
    )
    require(
        tiers["theta_IV_31_8_R1_CUBED_volume"]
        == "RETIRED_FOR_ACTIVE_Q79_BRANCH",
        "obsolete Theta IV volume was retained",
    )
    require(
        tiers["selected_MTT_local_diffeomorphism_natural_action"] == "OPEN"
        and tiers["selected_numeric_kappa_h_or_G4"]
        == "OPEN_ONE_EFFECTIVE_NORMALIZATION"
        and tiers["selected_Lambda_eff"] == "OPEN",
        "selected physical data were overpromoted",
    )
    require(
        theorem["parameter_count"]["new_fitted_parameters"] == 0
        and theorem["parameter_count"]["remaining_effective_Newton_coefficients"] == 1,
        "parameter accounting changed",
    )
    require(
        guards["claims_Lovelock_hypotheses_selected_by_MTT"] is False
        and guards["claims_numeric_G4_or_kappa_h"] is False
        and guards["claims_full_GR_or_QG"] is False,
        "claim guard failed",
    )
    for phrase in [
        "Hessian reciprocity is automatic",
        "Nonlinear Einstein completion",
        "Stress and exact normalization",
        "unavoidable scale",
        "Theta IV reconciliation",
        "SelectedSpacetimeClosureActionSource.v1",
    ]:
        require(phrase.lower() in note.lower(), f"note is missing section: {phrase}")

    print(
        "AUDIT_PASS: closure Hessian reciprocity, conditional nonlinear Einstein "
        "completion, stress normalization, and the one-scale no-go are exact"
    )


if __name__ == "__main__":
    main()
