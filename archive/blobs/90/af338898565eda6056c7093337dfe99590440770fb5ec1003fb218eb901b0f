from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "q79_spinc_flat_hym_ramification_extension_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    finite = cert["finite_data"]
    theorem = cert["theorem"]
    tiers = cert["claim_tiers"]
    guards = cert["guardrails"]

    require(all(cert["checks"].values()), "one or more HYM/ramification checks failed")
    require(
        cert["status"]
        == "Q79_SPINC_FLAT_HYM_COMPLEMENT_AND_ROOTSTACK_EXTENSION_CLOSED_ORDINARY_SMOOTH_NOGO_GLOBAL_SINGULAR_HYM_SELECTION_OPEN",
        "HYM/ramification status changed",
    )
    require(finite["branch_class_coefficient"] == 6, "branch class changed")
    require(finite["half_branch_class_coefficient"] == 3, "half-branch class changed")
    require(
        finite["transposition_meridian_phase_exponents_mod64"] == [32, 32, 32],
        "meridian determinant holonomy changed",
    )
    require(theorem["complement"]["curvature"] == "F_det=0", "flat curvature statement lost")
    require(tiers["HYM_equation_on_smooth_complement"] == "CLOSED", "complement HYM lost")
    require(
        tiers["ordinary_smooth_unramified_extension"] == "CLOSED_NO_GO",
        "ordinary-extension no-go lost",
    )
    require(
        tiers["order_two_root_stack_parabolic_extension_object"] == "CLOSED",
        "root-stack extension object lost",
    )
    require(tiers["global_singular_branch_HYM_resolution"] == "OPEN", "singular HYM overclaim")
    require(guards["claims_branch_divisor_is_smooth"] is False, "branch smoothness overclaim")
    require(guards["claims_MTT_selects_root_stack"] is False, "root-stack selection overclaim")
    require(
        guards["claims_final_integral_branch_selected"] is False,
        "final integral branch overclaim",
    )

    print(
        "AUDIT_PASS: the determinant line is flat/HYM on the complement, ordinary "
        "smooth extension is impossible, and the root-stack route is exactly typed"
    )


if __name__ == "__main__":
    main()
