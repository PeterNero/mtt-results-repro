from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "global_covariant_helicity2_dg_bundle_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    numerics = cert["numerics"]
    tiers = cert["claim_tiers"]
    guards = cert["guardrails"]

    require(all(cert["checks"].values()), "one or more covariant DG checks failed")
    require(
        cert["status"]
        == "GLOBAL_COVARIANT_HELICITY2_DG_BUNDLE_CONSTRUCTED_EXACT_SUPPORT_CLOSED_SELECTED_ACTION_STRESS_LORENTZIAN_OPEN",
        "covariant DG status changed",
    )
    require(numerics["Z64_to_SO2_representation_residual"] == 0.0, "representation match changed")
    require(numerics["fiber_ranks"] == [2, 2, 2, 2, 2], "TT fiber rank changed")
    require(numerics["max_SO3_equivariance_residual"] < 1.0e-12, "SO3 equivariance failed")
    require(numerics["north_patch_plus_cross_residual"] == 0.0, "north-patch recovery failed")
    require(tiers["global_helicity2_associated_bundle"] == "CLOSED", "helicity bundle lost")
    require(tiers["global_covariant_TT_projector"] == "CLOSED", "global TT projector lost")
    require(
        tiers["global_covariant_DG_bundle_map"] == "CLOSED_FOR_CONSTRUCTED_REALIZATION",
        "global DG construction lost",
    )
    require(
        tiers["global_exact_Z64_support_identity"] == "CLOSED_FIBERWISE",
        "global support identity lost",
    )
    require(tiers["selected_MTT_action_uses_global_DG"] == "OPEN", "action overclaim")
    require(guards["claims_global_scalar_plus_cross_rows"] is False, "global scalar-row overclaim")
    require(guards["claims_Lorentzian_QG_closed"] is False, "Lorentzian QG overclaim")

    print(
        "AUDIT_PASS: the local weight-two DG globalizes as an SO(3)-covariant "
        "helicity bundle map with exact finite support"
    )


if __name__ == "__main__":
    main()
