from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = (
    ROOT
    / "certificates"
    / "q79_standard_tlsm_pullback_chirality_nogo_certificate.json"
)


def main() -> None:
    payload = json.loads(CERT.read_text(encoding="utf-8"))
    assert payload["schema"] == "MTTQ79StandardTLSMPullbackChiralityNoGo.v4"
    assert all(payload["checks"].values())
    assert payload["checks"]["A128_all_90_continuous_root_tubes_closed"]
    assert payload["checks"]["A129_handles_and_global_surface_relation_closed"]
    assert payload["checks"]["A130_exact_integral_H2_basis_closed"]
    assert payload["checks"][
        "A131_floating_period_table_and_A132_Z90_quotient_closed"
    ]
    assert payload["checks"][
        "A151_exact_interval_support_is_16_of_71_z_adapter_closed_branch_open"
    ]

    pullback = payload["standard_TLSM_pullback_theorem"]
    assert pullback["base_complex_dimension"] == 2
    assert pullback["base_top_real_cohomology_degree"] == 4
    assert pullback["c3_real_degree"] == 6
    assert pullback["pullback_c3"] == 0

    target = payload["physical_chiral_target"]
    assert target["clutching_winding"] == [3, -3]
    assert target["integral_c3"] == [6, -6]
    assert target["generation_index_half_c3"] == [3, -3]
    assert target["canonical_mixed_c2_class"] == "9 u"
    assert target["simultaneous_c2_c3_topological_existence"] == "CLOSED_EXACT"
    assert target["necessary_Hodge_type_admissibility"] == "CLOSED_EXACT"
    assert target["holomorphic_structure"] == "OPEN"
    assert target["balanced_HYM"] == "OPEN"
    assert target["differential_Bianchi"] == "OPEN"

    tiers = payload["claim_tiers"]
    assert tiers["standard_TLSM_pullback_c3_zero"] == "CLOSED_EXACT_NOGO"
    assert tiers["topological_nonpullback_SU3_c3_plusminus6"] == "CLOSED_EXACT"
    assert tiers["topological_nonpullback_SU3_c2_9u_c3_plusminus6_simultaneous"] == "CLOSED_EXACT"
    assert tiers[
        "Hodge_admissible_nonpullback_SU3_c2_9u_c3_plusminus6_target"
    ].startswith("CLOSED_EXACT")
    assert tiers["holomorphic_nonpullback_SU3_worldsheet_bundle"] == "OPEN"
    assert tiers["same_carrier_twisted_spectral_integral_branch"] == "OPEN"
    assert tiers["UV_complete_q79_quantum_gravity"] == "OPEN"
    spectral = payload["exit_comparison"]["twisted_spectral_Fourier_Mukai"]
    assert "exact 92-column integral H2 presentation" in spectral["closed"]
    assert (
        "16 of 71 weighted E32 thimble intervals with L1 weight 36 of 123"
        in spectral["closed"]
    )
    assert "covariant z-chart interval adapter and first native z row d048" in spectral["closed"]
    assert "remaining 55 weighted E32 thimble interval certificates" in spectral["open"]
    assert not any("z-chart interval adapter" in row for row in spectral["open"])
    assert payload["new_fitted_continuous_parameters"] == 0

    print("Q79_STANDARD_TLSM_PULLBACK_CHIRALITY_NOGO_AUDIT_PASS")


if __name__ == "__main__":
    main()
