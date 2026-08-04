from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = (
    ROOT
    / "certificates"
    / "q79_twisted_group_algebra_topological_character_certificate.json"
)
NOTE = (
    ROOT
    / "proof_corpus"
    / "q79_Twisted_Group_Algebra_and_Finite_Topological_Character_Theorem_v1.md"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    data = cert["finite_data"]
    tiers = cert["claim_tiers"]
    guards = cert["guardrails"]

    require(all(cert["checks"].values()), "twisted-algebra check failed")
    require(
        cert["status"]
        == "Q79_SELECTED_FINITE_TWISTED_GROUP_ALGEBRA_MAT3_AND_TOPOLOGICAL_INDEX_CLOSED_EXACT_FULL_WORLDSHEET_CHARACTERS_OPEN",
        "twisted-algebra status changed",
    )
    require(
        data["group_order"] == 9
        and data["twisted_group_algebra_dimension"] == 9
        and data["matrix_span_rank"] == 9
        and data["twisted_algebra_center_dimension"] == 1,
        "Mat3 twisted-algebra computation changed",
    )
    require(
        data["unique_projective_irrep_count"] == 1
        and data["unique_projective_irrep_dimension"] == 3
        and data["projective_character_trace_distribution"]
        == {"trace_3": 1, "trace_0": 8},
        "unique projective character changed",
    )
    require(
        data["unnormalized_finite_torus_sum_in_basis_1_omega"] == [9, 0]
        and data["normalized_finite_topological_torus_index"] == "1",
        "finite topological torus index changed",
    )
    require(
        data["closed_string_modular_seed_orbit_count"] == 7
        and data["seed_stabilizer_orders_in_SL2_F3"]
        == [1, 1, 3, 3, 3, 3, 24],
        "closed-string seed boundary changed",
    )
    require(
        tiers["selected_q79_twisted_group_algebra"]
        == "CLOSED_EXACT_ISOMORPHIC_TO_MAT3C"
        and tiers["selected_q79_projective_module"]
        == "CLOSED_UNIQUE_IRREP_DIMENSION_3"
        and tiers["finite_discrete_torsion_topological_torus_index"]
        == "CLOSED_EXACT_ONE"
        and tiers["seven_closed_string_seed_characters"] == "OPEN"
        and tiers["full_heterotic_GSO_partition_function"] == "OPEN",
        "finite module was conflated with full worldsheet characters",
    )
    require(
        guards["claims_unique_projective_module_is_full_closed_string_spectrum"]
        is False
        and guards[
            "claims_finite_topological_index_is_full_heterotic_partition_function"
        ]
        is False
        and guards["claims_UV_complete_QG_closed"] is False,
        "finite character theorem was overpromoted",
    )
    for phrase in [
        "All 81 multiplication rows",
        "C^c[F_3^2] = Mat_3(C)",
        "exactly one",
        "33 + 24 omega + 24 omega^2",
        "normalized finite topological torus index",
        "seven modular",
        "does not make the full heterotic partition function equal to one",
    ]:
        require(phrase in note, f"proof note missing: {phrase}")

    print(
        "AUDIT_PASS: the selected q79 m=1 cocycle has twisted algebra Mat3(C), "
        "one three-dimensional projective irrep, and finite torus index one; "
        "the seven heterotic seed characters and GSO completion remain open"
    )


if __name__ == "__main__":
    main()
