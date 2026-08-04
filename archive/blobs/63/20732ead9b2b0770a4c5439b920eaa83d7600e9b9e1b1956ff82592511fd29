from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "stf_shear_tt_bridge_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    require(
        cert["status"] == "STF_SHEAR_TO_TT_PLUS_CROSS_BRIDGE_CLOSED_LENS_SOURCE_OPEN",
        "unexpected status",
    )
    la = cert["linear_algebra"]
    require(la["spatial_symmetric_components"] == 6, "symmetric 3x3 component count should be 6")
    require(la["constraint_rank"] == 4, "constraint rank should be 4")
    require(la["tt_dimension"] == 2, "TT dimension should be 2")
    require(la["plus_satisfies_constraints"] is True, "plus should satisfy constraints")
    require(la["cross_satisfies_constraints"] is True, "cross should satisfy constraints")
    require(la["plus_cross_independent"] is True, "plus and cross should be independent")
    require(cert["bridge_closed"] is True, "STF to TT bridge should close")
    require(cert["guardrails"]["claims_lens_selected_as_STF"] is False, "must not claim lens selected")
    require(cert["guardrails"]["claims_selected_P_GR"] is False, "must not claim selected P_GR")

    print("AUDIT_PASS: STF shear to TT plus/cross bridge is closed with lens source open")


if __name__ == "__main__":
    main()

