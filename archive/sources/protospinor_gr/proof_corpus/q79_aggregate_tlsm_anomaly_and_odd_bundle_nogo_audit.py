from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = (
    ROOT
    / "certificates"
    / "q79_aggregate_tlsm_anomaly_and_odd_bundle_nogo_certificate.json"
)


def main() -> None:
    payload = json.loads(CERT.read_text(encoding="utf-8"))
    checks = payload["checks"]

    assert payload["schema"] == "MTTQ79AggregateTLSMAnomalyAndOddBundleMonadNoGo.v1"
    assert all(checks.values())

    anomaly = payload["local_TLSM_anomaly"]
    assert anomaly["delta_charge_vector_H_L"] == [1, -1]
    assert anomaly["circle_shift_rows_M"] == [[1, -1], [0, 0]]
    assert anomaly["axial_rows_N"] == [[4, -4], [0, 0]]
    assert anomaly["active_fiber_radius_squared"] == 2
    assert anomaly["quantum_anomaly_matrix"] == [[2, -2], [-2, 2]]
    assert anomaly["classical_Green_Schwarz_matrix_half_NM"] == [
        [2, -2],
        [-2, 2],
    ]
    assert anomaly["matrix_residual"] == [[0, 0], [0, 0]]
    assert anomaly["weighted_curvature_norm_cost"] == 8
    assert anomaly["Chern_normalized_torus_cost"] == 4

    monad = payload["aggregate_rank12_bundle_monad"]
    assert monad["rank"] == 12
    assert monad["c1_charge_sum_B"] == monad["c1_charge_sum_C"] == [12, 4]
    assert monad["c2_coefficient_matrix"] == [[14, 4], [4, 2]]
    assert monad["integral_c2"] == 20
    assert monad["E_dot_J"] == 0

    tiers = payload["claim_tiers"]
    assert tiers["aggregate_local_TLSM_anomaly_matrix"].startswith("CLOSED_EXACT")
    assert tiers["separate_odd_SU3_SU9_Picard_line_monads"] == "CLOSED_EXACT_NOGO"
    assert tiers["physical_SU3_SU9_nonAbelian_EJ_maps"] == "OPEN"
    assert tiers["exact_q79_IR_SCFT"] == "OPEN"
    assert tiers["UV_complete_q79_quantum_gravity"] == "OPEN"
    assert payload["new_fitted_continuous_parameters"] == 0

    print("Q79_AGGREGATE_TLSM_ANOMALY_AND_ODD_BUNDLE_NOGO_AUDIT_PASS")


if __name__ == "__main__":
    main()
