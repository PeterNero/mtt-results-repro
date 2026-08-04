from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "massless_tt_pole_internal_gap_no_go_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    numerics = cert["numerics"]
    tiers = cert["claim_tiers"]
    guards = cert["guardrails"]

    require(all(cert["checks"].values()), "one or more massless-pole checks failed")
    require(
        cert["status"]
        == "PURE_LAMBDA15_PHYSICAL_TT_CARRIER_CLOSED_NOGO_COHERENT_ZERO_MODE_POLE_CHANNEL_REQUIRED",
        "massless-pole status changed",
    )
    require(numerics["lambda_gap"] == 15, "gap changed")
    require(numerics["metric_zero_value_exact"] == "4/15", "metric zero value changed")
    require(numerics["strain_zero_value_exact"] == "1/15", "strain zero value changed")
    require(tiers["pure_lambda15_carrier_as_massless_graviton"] == "CLOSED_NO_GO", "no-go lost")
    require(tiers["zero_internal_atom_required_for_massless_pole"] == "CLOSED", "zero-atom theorem lost")
    require(tiers["coherent_zero_mode_TT_source_row"] == "OPEN", "zero-mode row overpromoted")
    require(guards["claims_lambda15_is_physical_graviton_mass_or_pole"] is False, "lambda15 overclaim")
    require(guards["claims_full_GR_or_QG_closed"] is False, "full QG overclaim")

    print(
        "AUDIT_PASS: a pure positive lambda=15 carrier cannot contain a massless "
        "TT pole; a coherent zero-mode atom is necessary"
    )


if __name__ == "__main__":
    main()
