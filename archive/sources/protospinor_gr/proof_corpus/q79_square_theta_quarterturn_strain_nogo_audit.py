from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATE = (
    ROOT
    / "certificates"
    / "q79_square_theta_quarterturn_strain_nogo_certificate.json"
)
NOTE = (
    ROOT
    / "proof_corpus"
    / "q79_Square_Theta_QuarterTurn_to_Strain_DirectFunctor_NoGo_v1.md"
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

    require(all(certificate["checks"].values()), "one or more exact checks failed")
    require(
        data["adjoint_plus1_eigenspace_dimension"] == 3
        and data["adjoint_minus1_eigenspace_dimension"] == 2
        and data["adjoint_J2_minus1_sector_dimension"] == 4
        and data["desired_JDE_sector_dimension"] == 6,
        "direct theta adjoint eigenspace inventory changed",
    )
    require(
        data["strain_to_orientation_block_rank"] == 2
        and tiers["direct_theta_adjoint_preserves_q79_D_plus_S_strain"]
        == "CLOSED_NO_GO",
        "D-plus-S non-invariance result changed",
    )
    require(
        tiers["square_elliptic_degree_three_quarterturn"] == "CLOSED_EXACT"
        and tiers["direct_theta_adjoint_on_Herm3"] == "CLOSED_EXACT"
        and tiers["direct_theta_adjoint_realizes_six_dimensional_JDE"]
        == "CLOSED_NO_GO"
        and tiers["abstract_C4_matrix_match_is_sufficient_same_carrier_functor"]
        == "CLOSED_NO_GO",
        "direct-functor no-go changed",
    )
    require(
        tiers["nontrivial_inverse_Fourier_Mukai_induced_JDE_functor"] == "OPEN"
        and tiers["actual_projected_HYM_Hessian"] == "OPEN",
        "remaining constructive routes were overpromoted",
    )
    require(
        guards["claims_trial_tau_i_or_identity_alignment_is_MTT_selected"] is False
        and guards["claims_no_possible_nontrivial_Fourier_Mukai_functor_exists"]
        is False
        and guards["claims_actual_HYM_Hessian_computed"] is False
        and guards["uses_observed_physics_data"] is False
        and guards["adds_fitted_numeric_parameter"] is False,
        "selection, Fourier-Mukai, HYM, or fitting guardrail changed",
    )
    for phrase in [
        "U_theta=diag(-1,i,1)",
        "dim ker(Ad(U)^2+I)=4",
        "D direct-sum S",
        "nontrivial inverse-Fourier-Mukai functor",
    ]:
        require(phrase.lower() in note.lower(), f"proof note missing: {phrase}")

    print(
        "AUDIT_PASS: the direct square-theta adjoint has a four-dimensional "
        "quarter-turn sector and mixes D+S into K, so it cannot realize the "
        "six-dimensional J_DE; nontrivial inverse-Fourier-Mukai or direct HYM "
        "construction remains"
    )


if __name__ == "__main__":
    main()
