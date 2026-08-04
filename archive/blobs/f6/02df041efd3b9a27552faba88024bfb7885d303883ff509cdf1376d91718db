from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "quadratic_tt_nonlinear_action_nogo_certificate.json"
NOTE = ROOT / "proof_corpus" / "Quadratic_TT_Data_Nonlinear_Action_NoGo_and_Spectral_Exit_v1.md"


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

    require(all(checks.values()), "one or more nonlinear-action no-go checks failed")
    require(
        cert["status"]
        == "QUADRATIC_TT_TO_NONLINEAR_ACTION_SELECTION_NOGO_CLOSED_DIRECT_TWO_DERIVATIVE_AND_SPECTRAL_SUPERSET_EXITS_ISOLATED",
        "nonlinear-action frontier status changed",
    )
    require(
        theorem["order_proof"]["vanishing"]
        == [
            "Delta S_alpha[eta]=0",
            "D Delta S_alpha[eta]=0",
            "D2 Delta S_alpha[eta]=0",
        ],
        "counterfamily no longer has identical Hessian",
    )
    require(
        theorem["deformation_family"]["uses_new_dimensionful_scale"] is False,
        "counterfamily unexpectedly uses a new dimensionful scale",
    )
    require(
        tiers["quadratic_TT_data_select_unique_nonlinear_action"] == "CLOSED_NO_GO"
        and tiers["two_derivative_IR_clause_is_logically_indispensable"] == "CLOSED",
        "nonlinear independence theorem was lost",
    )
    require(
        tiers["spectral_action_is_pure_Einstein_gravity"] == "CLOSED_NO"
        and tiers["spectral_action_as_same_operator_SM_gravity_candidate"]
        == "CLOSED_ARCHITECTURALLY",
        "spectral-action classification changed",
    )
    require(
        tiers["selected_MTT_product_spectral_action"] == "OPEN"
        and tiers["selected_Einstein_IR_limit_of_spectral_action"] == "OPEN"
        and tiers["direct_selected_spacetime_closure_action"] == "OPEN",
        "one action route was overpromoted",
    )
    require(
        guards["claims_quadratic_Hessian_fixes_nonlinear_vertices"] is False
        and guards["claims_spectral_action_is_pure_two_derivative_GR"] is False
        and guards["claims_selected_MTT_action_closed"] is False,
        "claim guard failed",
    )
    for phrase in [
        "Exact no-go",
        "Spectral-action corpus audit",
        "Direct closure-action exit",
        "Spectral superset exit",
        "C[g(epsilon)] = epsilon C1[h]",
    ]:
        require(phrase.lower() in note.lower(), f"note missing: {phrase}")

    print(
        "AUDIT_PASS: quadratic TT data do not select nonlinear gravity; direct "
        "two-derivative and controlled spectral-action exits are exactly isolated"
    )


if __name__ == "__main__":
    main()
