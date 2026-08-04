from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = (
    ROOT
    / "certificates"
    / "q79_seven_seed_modular_induction_stabilizers_certificate.json"
)
NOTE = (
    ROOT
    / "proof_corpus"
    / "q79_Seven_Seed_Modular_Induction_and_Stabilizer_Theorem_v1.md"
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

    require(all(cert["checks"].values()), "seven-seed modular check failed")
    require(
        cert["status"]
        == "Q79_SEVEN_SEED_MODULAR_INDUCTION_AND_STABILIZER_THEOREM_CLOSED_EXACT_SEED_FUNCTIONS_GSO_OPEN",
        "seven-seed status changed",
    )
    require(
        data["SL2_F3_order"] == 24
        and data["sector_count"] == 81
        and data["modular_orbit_count"] == 7,
        "finite modular action changed",
    )
    require(
        data["orbit_sizes"] == [1, 8, 8, 8, 8, 24, 24]
        and data["stabilizer_orders"] == [1, 1, 3, 3, 3, 3, 24]
        and data["phase_orbit_counts"] == {"0": 5, "1": 1, "2": 1}
        and data["phase_sector_counts"] == {"0": 33, "1": 24, "2": 24},
        "orbit, stabilizer, or phase split changed",
    )
    require(
        data["finite_invariant_seed_dimension"] == 7
        and data["finite_invariance_constraint_rank"] == 74,
        "seven-seed minimality changed",
    )
    require(
        tiers["seven_modular_orbits_and_stabilizers"] == "CLOSED_EXACT"
        and tiers["seven_seed_modular_induction_theorem"]
        == "CLOSED_CONDITIONAL_ON_ANALYTIC_STABILIZER_MULTIPLIERS"
        and tiers["finite_symmetry_reduces_below_seven_seeds"]
        == "CLOSED_NO_GO"
        and tiers["seven_tau_dependent_seed_characters"] == "OPEN"
        and tiers["full_q79_heterotic_partition_function"] == "OPEN",
        "finite induction was conflated with analytic character construction",
    )
    require(
        guards["claims_finite_orbit_induction_constructs_analytic_seed_functions"]
        is False
        and guards["claims_stabilizer_orders_fix_Gamma3_multipliers"] is False
        and guards["claims_full_GSO_partition_function_closed"] is False
        and guards["claims_UV_complete_QG_closed"] is False,
        "seven-seed theorem was overpromoted",
    )
    for phrase in [
        "SL(2,F_3)",
        "1,8,8,8,8,24,24",
        "24,3,3,3,3,1,1",
        "rank 74",
        "nullity 7",
        "cannot reduce the seven analytic seeds",
        "Gamma(3)",
    ]:
        require(phrase in note, f"proof note missing: {phrase}")

    print(
        "AUDIT_PASS: all 81 q79 finite sectors induce from seven exact modular "
        "orbits with certified stabilizers; finite covariance cannot reduce the "
        "seven analytic seeds, whose GLSM/GSO content remains open"
    )


if __name__ == "__main__":
    main()
