from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "q79_f3x2_discrete_torsion_modular_orbit_certificate.json"
NOTE = ROOT / "proof_corpus" / "q79_F3x2_Discrete_Torsion_Modular_Orbit_Theorem_v1.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    data = cert["finite_data"]
    tiers = cert["claim_tiers"]
    guards = cert["guardrails"]

    require(all(cert["checks"].values()), "finite modular-orbit check failed")
    require(
        cert["status"]
        == "Q79_F3X2_DISCRETE_TORSION_MODULAR_ST_ORBIT_CLOSED_EXACT_FULL_HETEROTIC_PARTITION_FUNCTION_OPEN",
        "finite modular-orbit status changed",
    )
    require(
        data["torus_twist_sector_count"] == 81
        and data["cocycle_triples_checked"] == 729
        and data["cocycle_failures"] == 0
        and data["S_phase_failures"] == 0
        and data["T_phase_failures"] == 0,
        "finite cocycle or S/T orbit changed",
    )
    require(
        data["phase_exponent_multiplicities"] == {"0": 33, "1": 24, "2": 24}
        and data["nontrivial_phase_sector_count"] == 48,
        "discrete-torsion phase spectrum changed",
    )
    require(
        data["modular_orbit_count"] == 7
        and data["modular_orbit_sizes"] == [1, 8, 8, 8, 8, 24, 24]
        and data["modular_orbit_rank_counts"] == {"0": 1, "1": 4, "2": 2},
        "finite modular-orbit reduction changed",
    )
    require(
        tiers["finite_discrete_torsion_S_T_phase_covariance"]
        == "CLOSED_EXACT_81_OF_81"
        and tiers["q79_full_torus_partition_function"]
        == "OPEN_FINITE_TORSION_PHASE_SUBSECTOR_CLOSED"
        and tiers["q79_exact_worldsheet_CFT"] == "OPEN",
        "finite phase was conflated with full worldsheet modular invariance",
    )
    require(
        guards["claims_finite_phase_covariance_is_full_modular_invariance"]
        is False
        and guards["claims_GSO_projection_constructed"] is False
        and guards["claims_UV_complete_QG_closed"] is False,
        "finite phase theorem was overpromoted",
    )
    for phrase in [
        "9^3=729",
        "9^2=81",
        "S^2=(ST)^3=charge conjugation",
        "33,24,24",
        "48 sectors",
        "exactly seven modular orbits",
        "seed character blocks",
        "does not construct a full heterotic torus partition function",
    ]:
        require(phrase in note, f"proof note missing: {phrase}")

    print(
        "AUDIT_PASS: the selected q79/F F3x2 gerbe phase is exactly modular "
        "covariant on all 81 torus sectors and reduces them to seven character "
        "seeds; the full heterotic character/GSO packet remains open"
    )


if __name__ == "__main__":
    main()
