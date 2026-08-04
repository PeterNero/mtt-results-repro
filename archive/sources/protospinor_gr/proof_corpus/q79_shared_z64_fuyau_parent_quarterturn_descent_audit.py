from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATE = (
    ROOT
    / "certificates"
    / "q79_shared_z64_fuyau_parent_quarterturn_descent_certificate.json"
)
NOTE = (
    ROOT
    / "proof_corpus"
    / "q79_Shared_Z64_FuYau_Parent_QuarterTurn_and_Descent_Dichotomy_v1.md"
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
        data["Z64_order4_subgroup"] == [0, 16, 32, 48]
        and data["Z64_order4_generators"] == [16, 48]
        and data["weight1_root_restriction_i_exponents"]
        == {"1": [0, 1, 2, 3], "33": [0, 1, 2, 3]},
        "root-independent Z64 order-four source changed",
    )
    require(
        data["Chern_orbit_coefficients_of_delta"]
        == [[1, 0], [0, 1], [-1, 0], [0, -1]]
        and tiers["active_rank_one_FuYau_parent_integral_C4_action"]
        == "CLOSED_CONDITIONAL_ON_ACTIVE_TOPOLOGY_TYPING"
        and tiers["minimal_four_branch_FuYau_parent"] == "CLOSED_EXACT",
        "Fu-Yau parent action changed",
    )
    require(
        tiers["free_orbit_covariance_implies_single_branch_Hessian_invariance"]
        == "CLOSED_NO_GO"
        and data["single_branch_equivariant_Hessian_dimension"] == 6
        and data["free_orbit_covariant_Hessian_family_dimension"] == 6
        and data["free_orbit_H0_commutator_rank"] > 0,
        "free-orbit covariance no-go changed",
    )
    require(
        tiers["autonomous_Lens_quotient_descent_implies_quarterturn_invariance"]
        == "CLOSED_EXACT_CONDITIONAL"
        and tiers["physical_TT_scalarization_under_Lens_descent"]
        == "CLOSED_EXACT_CONDITIONAL"
        and data["Lens_descent_physical_block"] == "H_std=kappa_standard*I2"
        and data["Lens_descent_physical_block_dimension"] == 1,
        "Lens-descent scalarization changed",
    )
    require(
        tiers["primitive_MTT_shared_circle_to_FuYau_source"] == "OPEN"
        and tiers["MTT_types_C4_as_Lens_redundancy_not_physical_superselection"]
        == "OPEN"
        and tiers["typed_retarded_representative_selector"] == "OPEN"
        and tiers["actual_inverse_Fourier_Mukai_HYM_operator"] == "OPEN",
        "remaining source fork was overpromoted",
    )
    require(
        guards["claims_active_rank_one_topology_is_primitive_MTT_selected"] is False
        and guards["claims_free_orbit_covariance_scalarizes_one_branch"] is False
        and guards["claims_C4_parent_action_is_single_branch_automorphism"] is False
        and guards["claims_odd_root_or_retarded_orientation_selected"] is False
        and guards["claims_actual_HYM_operator_computed"] is False,
        "source, branch, or HYM guardrail changed",
    )
    for phrase in [
        "C4=<16>={0,16,32,48}",
        "chi_1(16m)=chi_33(16m)=i^m",
        "covariance is not invariance",
        "H_0=diag(I3,2I3)",
        "Lens-redundancy exit",
        "Physical-branch exit",
    ]:
        require(phrase.lower() in note.lower(), f"proof note missing: {phrase}")

    print(
        "AUDIT_PASS: shared Z64 supplies a root-independent C4 Fu-Yau parent "
        "action; free-orbit covariance does not scalarize one branch, while "
        "autonomous Lens descent conditionally does"
    )


if __name__ == "__main__":
    main()
