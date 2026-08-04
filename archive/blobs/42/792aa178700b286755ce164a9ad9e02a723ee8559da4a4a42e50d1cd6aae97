from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "q79_branch_cusp_resolution_rootstack_hym_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    finite = cert["finite_data"]
    tiers = cert["claim_tiers"]
    guards = cert["guardrails"]

    require(all(cert["checks"].values()), "one or more cusp-resolution checks failed")
    require(
        cert["status"]
        == "Q79_SELECTED_BRANCH_18_CUSPS_AND_EXPLICIT_RESOLVED_ROOTSTACK_HYM_CARRIER_CLOSED_MTT_ACTION_TRANSVERSE_SELECTION_OPEN",
        "cusp-resolution status changed",
    )
    require(finite["total_flex_count"] == 9, "elliptic flex count changed")
    require(finite["normalization_branch_point_count"] == 36, "branch point count changed")
    require(finite["normalization_genus"] == 19, "normalization genus changed")
    require(finite["branch_arithmetic_genus"] == 37, "arithmetic genus changed")
    require(finite["total_delta"] == 18, "delta budget changed")
    require(finite["ordinary_cusp_count"] == 18, "ordinary cusp count changed")
    require(
        [row["multiplicity"] for row in finite["resolution_components"]]
        == [1, 2, 3, 6],
        "cusp resolution multiplicities changed",
    )
    require(
        finite["root_stack_odd_components"] == ["strict_transform", "E2"],
        "root-stack odd divisor changed",
    )
    require(
        tiers["resolved_order_two_rootstack_flat_HYM_carrier"] == "CLOSED",
        "resolved root-stack HYM carrier was lost",
    )
    require(
        tiers["ordinary_smooth_line_descent_to_original_K3"] == "CLOSED_NO_GO",
        "ordinary descent no-go was lost",
    )
    require(tiers["MTT_selection_of_resolved_rootstack_carrier"] == "OPEN", "MTT selection overclaim")
    require(guards["claims_original_branch_divisor_is_smooth"] is False, "smoothness overclaim")
    require(guards["claims_selected_action_closed"] is False, "action overclaim")
    require(
        guards["claims_final_integral_branch_selected"] is False,
        "final integral branch overclaim",
    )

    print(
        "AUDIT_PASS: the selected branch has exactly eighteen ordinary cusps "
        "and an explicit resolved root-stack flat-HYM carrier"
    )


if __name__ == "__main__":
    main()
