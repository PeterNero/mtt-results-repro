from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATE = (
    ROOT
    / "certificates"
    / "q79_complement_quarterturn_hessian_scalarization_certificate.json"
)
NOTE = (
    ROOT
    / "proof_corpus"
    / "q79_Complement_QuarterTurn_Hessian_Scalarization_Theorem_v1.md"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    certificate = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    tiers = certificate["claim_tiers"]
    data = certificate["finite_data"]
    guards = certificate["guardrails"]

    require(all(certificate["checks"].values()), "one or more finite checks failed")
    require(
        tiers["canonical_q79_complement_lane_complex_structure"]
        == "CLOSED_EXACT"
        and tiers["self_adjoint_S3_quarterturn_Hessian_scalarization"]
        == "CLOSED_EXACT",
        "exact quarter-turn scalarization changed",
    )
    require(
        data["single_branch_self_adjoint_S3_commutant_dimension"] == 6
        and data["exchange_invariant_self_adjoint_commutant_dimension"] == 4
        and data["quarterturn_invariant_self_adjoint_commutant_dimension"] == 2,
        "6-to-4-to-2 commutant reduction changed",
    )
    require(
        data["physical_TT_block"] == "H_std=kappa_standard*I2"
        and data["physical_TT_conditions"][:2]
        == ["h_DE=0", "h_DD=h_EE=kappa_standard"],
        "physical TT scalarization changed",
    )
    require(
        tiers["physical_TT_block_scalarization"]
        == "CLOSED_CONDITIONAL_ON_SELECTED_QUARTERTURN_INVARIANCE"
        and tiers["selected_HYM_action_is_quarterturn_invariant"] == "OPEN"
        and tiers["typed_lane_quarterturn_to_FuYau_Chern_orbit_source_functor"]
        == "OPEN",
        "conditional same-carrier boundary was overpromoted",
    )
    require(
        tiers["single_rank_one_FuYau_branch_supplies_order4_symmetry"]
        == "CLOSED_NO_GO"
        and tiers["minimal_four_branch_FuYau_Chern_orbit"] == "CLOSED_EXACT",
        "Fu-Yau branch-orbit classification changed",
    )
    require(
        guards["claims_abstract_Z4_match_is_same_carrier_source_theorem"] is False
        and guards["claims_actual_HYM_Hessian_computed"] is False
        and guards["claims_shared_central_U1_is_lane_quarterturn"] is False
        and guards["adds_fitted_numeric_parameter"] is False,
        "source, HYM, or parameter guardrail changed",
    )
    for phrase in [
        "J_DE^2=-I6",
        "H_std=kappa_standard*I2",
        "h_DE=0",
        "h_DD=h_EE=kappa_standard",
        "LensQuarterTurnToFuYauChernOrbitSourceTheorem",
        "functor is still open",
    ]:
        require(phrase in note, f"proof note missing: {phrase}")

    print(
        "AUDIT_PASS: the canonical complement quarter-turn reduces the "
        "self-adjoint S3 commutant 6->2 and conditionally scalarizes the "
        "physical HYM/TT block; the typed Fu-Yau source functor remains open"
    )


if __name__ == "__main__":
    main()
