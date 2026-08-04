from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATE = (
    ROOT
    / "certificates"
    / "q79_shared_rootplane_twisted_exterior_jde_functor_certificate.json"
)
NOTE = (
    ROOT
    / "proof_corpus"
    / "q79_Shared_RootPlane_Twisted_Exterior_JDE_Functor_v1.md"
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
        len(data["S3_twisted_exterior_records"]) == 6
        and all(
            row["determinant_twisted_exterior_matrix"] == row["sheet_matrix"]
            for row in data["S3_twisted_exterior_records"]
        ),
        "determinant-twisted exterior-square identity changed",
    )
    require(
        data["shared_C4_subgroup"] == [0, 16, 32, 48]
        and data["shared_root_real_quarterturn"] == [[0, -1], [1, 0]]
        and data["induced_JDE"]
        == [
            [0, 0, 0, -1, 0, 0],
            [0, 0, 0, 0, -1, 0],
            [0, 0, 0, 0, 0, -1],
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
        ],
        "shared root-plane J_DE changed",
    )
    require(
        tiers["determinant_twisted_exterior_square_edge_identification"]
        == "CLOSED_EXACT"
        and tiers["shared_root_C4_realification"]
        == "CLOSED_EXACT_ROOT_INDEPENDENT"
        and tiers["typed_shared_C4_to_rootstack_strain_JDE_functor"]
        == "CLOSED_EXACT_ON_FLAT_SHEET_SYMBOL"
        and tiers["JDE_parallel_under_minimal_rootstack_flat_connection"]
        == "CLOSED_EXACT",
        "flat-symbol common-source functor was lost",
    )
    require(
        tiers["direct_unital_Herm3_adjoint_realizes_full_JDE"]
        == "CLOSED_NO_GO"
        and data["trace_mode"] == [1, 1, 1, 0, 0, 0]
        and data["JDE_trace_mode_image"] == [0, 0, 0, 1, 1, 1],
        "direct unital algebra-action no-go changed",
    )
    require(
        tiers["shared_C4_to_active_FuYau_parent_representation"]
        == "CLOSED_CONDITIONAL_ON_ACTIVE_TOPOLOGY_TYPING"
        and tiers["MTT_types_C4_as_Lens_redundancy"] == "OPEN"
        and tiers["actual_inverse_Fourier_Mukai_HYM_induced_JDE"] == "OPEN"
        and tiers["selected_HYM_functional_is_JDE_invariant"] == "OPEN"
        and tiers["actual_projected_HYM_Hessian"] == "OPEN",
        "physical HYM/Lens boundary was overpromoted",
    )
    require(
        guards["claims_flat_symbol_functor_is_full_inverse_Fourier_Mukai_functor"]
        is False
        and guards["claims_actual_nonzero_Chern_HYM_connection_is_flat"] is False
        and guards["claims_selected_HYM_functional_is_JDE_invariant"] is False
        and guards["claims_MTT_types_C4_as_Lens_redundancy"] is False
        and guards["claims_direct_theta_adjoint_was_rescued"] is False
        and guards["uses_observed_physics_data"] is False
        and guards["adds_fitted_numeric_parameter"] is False,
        "functor, HYM, Lens, or fitting guardrail changed",
    )
    normalized_note = " ".join(note.lower().split())
    for phrase in [
        "Lambda^2 E_D = sign tensor E_D",
        "E_S := det(E_D) tensor Lambda^2 E_D",
        "chi_1(16m)=chi_33(16m)=i^m",
        "J_DE=[[0,-I3],[I3,0]]",
        "global parallel action",
        "every unital unitary or antiunitary adjoint fixes the identity",
    ]:
        require(
            " ".join(phrase.lower().split()) in normalized_note,
            f"proof note missing: {phrase}",
        )

    print(
        "AUDIT_PASS: the determinant-twisted exterior square and shared odd-root "
        "C4 plane induce the exact global parallel J_DE on the flat q79 sheet "
        "symbol; actual inverse-Fourier-Mukai/HYM invariance or Lens descent remains"
    )


if __name__ == "__main__":
    main()
