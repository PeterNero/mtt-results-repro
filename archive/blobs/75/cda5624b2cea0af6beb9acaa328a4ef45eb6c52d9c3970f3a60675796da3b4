from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATE = (
    ROOT
    / "certificates"
    / "q79_interacting_low_energy_qg_eft_closure_certificate.json"
)
NOTE = (
    ROOT
    / "proof_corpus"
    / "q79_Interacting_Low_Energy_Quantum_Gravity_EFT_Closure_and_UV_Boundary_v1.md"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    certificate = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    tiers = certificate["claim_tiers"]
    data = certificate["finite_data"]
    params = certificate["parameter_ledger"]
    guards = certificate["guardrails"]

    require(all(certificate["checks"].values()), "one or more EFT checks failed")
    require(
        data["connected_graph_superficial_degree"] == "2L+2"
        and [
            row["superficial_derivative_order"]
            for row in data["loop_derivative_table_L0_to_L4"][:3]
        ]
        == [2, 4, 6],
        "Einstein EFT power counting changed",
    )
    require(
        tiers["interacting_low_energy_quantum_GR_EFT"]
        == "CLOSED_BY_STANDARD_EFT_COMPOSITION_AT_EACH_FIXED_ORDER"
        and tiers["two_parameter_interacting_quantum_GR_at_all_scales"]
        == "CLOSED_NO_GO",
        "low-energy and UV tiers were conflated",
    )
    require(
        tiers["two_loop_pure_GR_divergence"]
        == "CLOSED_NONZERO_GOROFF_SAGNOTTI_STANDARD_RESULT"
        and "209/[2880" in data["Goroff_Sagnotti_dimensionless_prefactor"],
        "two-loop UV boundary changed",
    )
    require(
        data["selected_SM_anomaly_rows_checked"] == 6
        and data["selected_SM_anomaly_rows_cancelled"] == 6,
        "selected SM anomaly table changed",
    )
    require(
        params["two_derivative_law_parameter_count"] == 2
        and params["free_quantum_parameters_beyond_kappa_h"] == 0
        and params["leading_nonanalytic_long_distance_Wilson_parameters"] == 0,
        "low-energy parameter ledger changed",
    )
    require(
        guards["claims_standard_EFT_quantization_is_derived_from_MTT"] is False
        and guards["claims_fixed_order_EFT_is_UV_completion"] is False
        and guards["claims_only_kappa_and_Lambda_suffice_beyond_tree_level"]
        is False,
        "EFT parity closure was overpromoted",
    )
    for phrase in [
        "Obs_QG,EFT^MTT",
        "D = 2L + 2",
        "Goroff-Sagnotti divergence",
        "kappa_gr^2 = 32 pi G_eff = 1/kappa_h",
        "interacting low-energy q79 quantum gravity",
        "not yet emitted by the selected",
    ]:
        require(phrase in note, f"proof note missing: {phrase}")

    print(
        "AUDIT_PASS: q79 reaches interacting quantum-GR EFT parity at every "
        "declared fixed order; the exact two-loop counterterm keeps UV completion open"
    )


if __name__ == "__main__":
    main()
