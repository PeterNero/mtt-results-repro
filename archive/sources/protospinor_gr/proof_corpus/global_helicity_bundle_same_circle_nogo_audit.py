from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "global_helicity_bundle_same_circle_nogo_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    finite = cert["finite_data"]
    tiers = cert["claim_tiers"]
    guards = cert["guardrails"]

    require(all(cert["checks"].values()), "one or more global helicity no-go checks failed")
    require(
        cert["status"]
        == "GLOBAL_SHARED_Z64_HELICITY_LINE_IDENTIFICATION_NOGO_LOCAL_DG_AND_INTERNAL_SPINC_HYM_CLOSED_COVARIANT_ACTION_SOURCE_OPEN",
        "global helicity status changed",
    )
    require(finite["external_weight_one_Chern_number"] == -2, "weight-one Chern number changed")
    require(finite["external_weight_two_Chern_number"] == -4, "weight-two Chern number changed")
    require(
        finite["internal_flat_de_Rham_Chern_number_on_momentum_sphere"] == 0,
        "internal flat Chern number changed",
    )
    require(tiers["global_internal_external_line_identity"] == "CLOSED_NO_GO", "global no-go lost")
    require(tiers["fixed_direction_local_DG"] == "CLOSED", "local DG was lost")
    require(
        tiers["finite_Z64_support_and_lambda15"] == "CLOSED_UNCHANGED",
        "finite support/pole result changed",
    )
    require(
        tiers["global_covariant_helicity_bundle_source"] == "OPEN_CONSTRUCTION",
        "covariant source was overclaimed",
    )
    require(guards["claims_global_plus_cross_frame_exists"] is False, "global frame overclaim")
    require(
        guards["claims_finite_Z64_is_the_global_transverse_U1_bundle"] is False,
        "finite/continuous bundle overclaim",
    )
    require(guards["claims_local_DG_result_invalid"] is False, "local result was discarded")

    print(
        "AUDIT_PASS: global shared/helicity line identity is topologically impossible; "
        "local DG survives and the target is a covariant bundle-valued source"
    )


if __name__ == "__main__":
    main()
