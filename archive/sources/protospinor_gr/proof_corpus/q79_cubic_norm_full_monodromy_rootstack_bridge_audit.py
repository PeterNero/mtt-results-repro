from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = (
    ROOT
    / "certificates"
    / "q79_cubic_norm_full_monodromy_rootstack_bridge_certificate.json"
)
NOTE = (
    ROOT
    / "proof_corpus"
    / "q79_Cubic_Norm_and_Full_Monodromy_RootStack_Strain_Bridge_v1.md"
)

STATUS = (
    "Q79_CUBIC_NORM_MAP_AND_COARSE_BRANCH_NOGO_CLOSED_"
    "FULL_MONODROMY_ROOTSTACK_STRAIN_BRIDGE_CLOSED_"
    "STRICT_SAME_SOURCE_MINIMAL_CONTINUATION_SELECTED_"
    "INVERSE_FOURIER_MUKAI_HESSIAN_AND_PRIMITIVE_PHYSICAL_BRANCH_OPEN"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    certificate = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")

    require(certificate["status"] == STATUS, "status mismatch")
    require(all(certificate["checks"].values()), "one or more exact checks failed")

    data = certificate["finite_data"]
    require(data["full_S3_intertwiner_dimension"] == 8, "full Hom dimension changed")
    require(
        data["lane_preserving_intertwiner_dimension"] == 4,
        "lane-preserving Hom dimension changed",
    )
    require(data["equivariant_atom_bijection_count"] == 1, "atom map not unique")
    require(data["simple_branch_rank"] == 3, "simple-branch rank must be three")
    require(
        data["simple_branch_smith_valuations"] == [0, 0, 0, 1, 1, 1],
        "simple-branch Smith profile changed",
    )
    require(data["minimal_root_orders"] == [2, 3, 2, 1], "root orders changed")

    tiers = certificate["claim_tiers"]
    require(
        tiers["unbranched_q79_strain_map_natural_uniqueness"] == "CLOSED_EXACT",
        "natural uniqueness was not closed",
    )
    require(
        tiers["coarse_finite_flat_branch_extension_as_isomorphism"]
        == "CLOSED_NO_GO",
        "coarse branch no-go missing",
    )
    require(
        tiers["minimal_full_monodromy_rootstack"] == "CLOSED_UNIQUE_MINIMAL",
        "minimal root-stack theorem missing",
    )
    require(
        tiers["rootstack_rank_six_strain_bundle_isomorphism"] == "CLOSED_EXACT",
        "rank-six root-stack bridge missing",
    )
    require(
        tiers["rootstack_flat_HYM_connection_intertwining"] == "CLOSED_EXACT",
        "flat HYM intertwining missing",
    )
    require(
        tiers["inverse_Fourier_Mukai_HYM_Hessian_intertwining"] == "OPEN",
        "inverse-Fourier-Mukai boundary was overpromoted",
    )
    require(
        tiers["primitive_MTT_selects_physical_rootstack_realization"] == "OPEN",
        "primitive physical branch was overpromoted",
    )

    guards = certificate["guardrails"]
    require(
        guards["claims_coarse_q79_algebra_map_stays_invertible_at_branch"] is False,
        "coarse-map guard missing",
    )
    require(
        guards["claims_previous_order_two_determinant_rootstack_was_full_S3_completion"]
        is False,
        "determinant/full-monodromy guard missing",
    )
    require(
        guards["claims_primitive_MTT_physical_branch_selection_closed"] is False,
        "primitive-selection guard missing",
    )
    require(guards["adds_fitted_numeric_parameter"] is False, "fit parameter added")
    require(guards["uses_observed_physics_data"] is False, "observed data used")

    for token in (
        "det(J_flat)=(-Disc(t^3+p*t+q))^3",
        "strict transform : transposition, root order 2",
        "E1               : three-cycle,  root order 3",
        "minimal full-monodromy completion",
        STATUS,
    ):
        require(token in note, f"note missing token: {token}")

    print(
        "AUDIT_PASS: q79 cubic norm map classified; coarse branch extension "
        "ruled out; minimal full-monodromy root-stack strain bridge closed"
    )


if __name__ == "__main__":
    main()
