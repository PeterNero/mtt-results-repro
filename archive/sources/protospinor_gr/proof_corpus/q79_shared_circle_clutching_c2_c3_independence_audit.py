from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = (
    ROOT
    / "certificates"
    / "q79_shared_circle_clutching_c2_c3_independence_certificate.json"
)


def main() -> None:
    payload = json.loads(CERT.read_text(encoding="utf-8"))
    assert payload["schema"] == "MTTQ79SharedCircleClutchingC2C3Independence.v1"
    assert all(payload["checks"].values())

    gysin = payload["gysin_calculation"]
    assert gysin["delta_divisibility"] == 1
    assert gysin["cup_delta_H2_to_H4"]["surjective"]
    assert gysin["P_delta_integral_cohomology_ranks"] == {
        "H0": 1,
        "H1": 0,
        "H2": 21,
        "H3": 21,
        "H4": 0,
        "H5": 1,
    }
    assert gysin["canonical_H_lift"]["exists"]
    assert gysin["canonical_H_lift"]["unique"]
    assert gysin["canonical_H_lift"]["primitive"]

    total = payload["total_space_calculation"]
    assert total["H4_rank"] == 21
    assert total["H6_rank"] == 1
    assert total["u_primitive"]
    assert total["pullback_c2_TX"] == 0

    classification = payload["clutching_classification"]
    assert classification["K1_P_delta"] == "Z^22"
    assert classification["AHSS_graded_pieces"] == {"H1": 0, "H3": 21, "H5": 1}
    assert "H5(P_delta,Z)" in classification["Postnikov_exact_sequence"]
    assert classification["normalization"]["c2"] == "-a cup t"
    assert classification["normalization"]["c3"] == "2 k [P_delta]^* cup t"

    candidate = payload["q79_candidate_specialization"]
    assert candidate["A103_original_pure_chirality_member"] == {
        "c2": 0,
        "c3": [6, -6],
        "k": [3, -3],
        "m": 0,
    }
    simultaneous = candidate["simultaneous_reference_member"]
    assert simultaneous["m"] == 9
    assert simultaneous["k"] == [3, -3]
    assert simultaneous["c2"] == "9 u"
    assert simultaneous["c3"] == [6, -6]
    assert simultaneous["generation_index_half_c3"] == [3, -3]
    assert candidate["new_fitted_continuous_parameters"] == 0

    tiers = payload["claim_tiers"]
    assert tiers["smooth_SU3_candidate_with_c2_9u_and_c3_plusminus6"] == "CLOSED_EXACT_TOPOLOGICAL_EXISTENCE"
    assert tiers["holomorphic_nonpullback_SU3_bundle"] == "OPEN"
    assert tiers["balanced_stability_and_HYM"] == "OPEN"
    assert tiers["differential_total_space_Bianchi_identity"] == "OPEN"
    assert tiers["UV_complete_q79_quantum_gravity"] == "OPEN"

    print("Q79_SHARED_CIRCLE_CLUTCHING_C2_C3_INDEPENDENCE_AUDIT_PASS")


if __name__ == "__main__":
    main()
