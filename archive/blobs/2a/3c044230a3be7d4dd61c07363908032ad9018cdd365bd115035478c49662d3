from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = (
    ROOT
    / "certificates"
    / "q79_degree2_k3_fuyau_torsion_glsm_base_certificate.json"
)
NOTE = (
    ROOT
    / "proof_corpus"
    / "q79_Degree2_K3_FuYau_Torsion_GLSM_Base_Theorem_v1.md"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    glsm = cert["incidence_GLSM"]
    source = cert["intersection_and_torsion_source"]
    arithmetic = cert["q79_same_branch_arithmetic"]
    tiers = cert["claim_tiers"]
    guards = cert["guardrails"]

    require(all(cert["checks"].values()), "degree-two K3/Fu-Yau GLSM check failed")
    require(
        cert["status"]
        == "Q79_DEGREE2_K3_SPLITTING_CONIC_GLSM_AND_RANKONE_FUYAU_TOPOLOGICAL_SOURCE_CLOSED_EXACT_CONDITIONAL_FULL_HETEROTIC_0_2_BUNDLE_TORSION_ANOMALY_AND_IR_SCFT_OPEN",
        "GLSM status changed",
    )
    require(
        glsm["charge_matrix"]
        == [[1, 1, 1, 3, 0, 1, -3, -4], [0, 0, 0, 0, 1, 1, -1, -1]],
        "incidence GLSM charge matrix changed",
    )
    require(
        glsm["constraint_bidegrees"] == [[3, 1], [4, 1]]
        and glsm["Calabi_Yau_charge_sums"] == [0, 0]
        and glsm["complex_target_dimension"] == 2
        and glsm["paired_2_2_gauge_anomaly_matrix"] == [[0, 0], [0, 0]],
        "GLSM Calabi-Yau, dimension, or anomaly row changed",
    )
    require(
        source["H_square"] == "2"
        and source["H_dot_Rminus"] == "2"
        and source["Rminus_square"] == "-2"
        and source["H_dot_delta"] == "0"
        and source["delta_square"] == "-4"
        and source["Rplus_square"] == "-2"
        and source["Rplus_dot_Rminus"] == "6",
        "intersection or primitive Fu-Yau class changed",
    )
    require(
        source["torsion_shift_charge_skeleton"][
            "twisted_circle_divisor_vector_in_H_L_basis"
        ]
        == [1, -1]
        and source["torsion_shift_charge_skeleton"][
            "shared_circle_divisor_vector_in_H_L_basis"
        ]
        == [0, 0],
        "rank-one/shared-circle torsion source changed",
    )
    require(
        arithmetic["Mukai_Gram"] == [[2, 1], [1, 4]]
        and arithmetic["Mukai_determinant"] == 7
        and arithmetic["reference_Bianchi"]["identity"] == "9+11+4=24"
        and arithmetic["reference_Bianchi"]["NS5_charge"] == 0
        and arithmetic["new_fitted_continuous_parameters"] == 0,
        "q79 arithmetic or reference Bianchi row changed",
    )
    require(
        tiers["explicit_degree_two_K3_smoothness"] == "CLOSED_EXACT"
        and tiers["splitting_conic_incidence_GLSM"] == "CLOSED_EXACT"
        and tiers["rank_one_FuYau_divisor_source_delta_H_minus_L"]
        == "CLOSED_EXACT"
        and tiers["strict_MTT_selection_of_rank_one_FuYau_topology"] == "OPEN"
        and tiers["full_heterotic_0_2_bundle_EJ_system"] == "OPEN"
        and tiers["local_torsion_GLSM_anomaly_cancellation"] == "OPEN"
        and tiers["exact_q79_IR_SCFT"] == "OPEN"
        and tiers["UV_complete_q79_quantum_gravity"] == "OPEN",
        "exact base construction was conflated with full heterotic completion",
    )
    require(
        all(value is False for value in guards.values()),
        "a GLSM guardrail was overpromoted",
    )
    for phrase in [
        "w^2 = F6",
        "U(1)_H",
        "U(1)_L",
        "H^2=2",
        "delta = H-L",
        "delta^2 = -4",
        "P_delta x S1_shared",
        "9+11+4 = 24",
        "local `2x2` anomaly matrix",
        "exact IR `(0,2)` SCFT",
    ]:
        require(phrase in note, f"proof note missing: {phrase}")

    print(
        "AUDIT_PASS: explicit smooth degree-two K3, incidence U(1)^2 GLSM, "
        "delta=H-L rank-one Fu-Yau source, and 9+11+4 reference allocation "
        "are exact; heterotic bundle, local torsion anomaly, source selection, "
        "and IR SCFT remain open"
    )


if __name__ == "__main__":
    main()
